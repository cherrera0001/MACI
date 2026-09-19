"""
Auditoria de la configuracion de CatBoost del notebook.

    python src/09_catboost_tuning.py <variante>

Busqueda PEQUENA y CONTROLADA, deliberadamente no combinatoria: se parte de la
configuracion del notebook y se varia UN factor a la vez (one-factor-at-a-time),
mas unas pocas combinaciones prometedoras. ~12 configuraciones x 5 folds.

Motivo metodologico: con n=1000 y una desviacion entre folds de 0.02-0.04, una
rejilla grande garantiza encontrar un maximo de ruido. Toda diferencia se
compara contra la std entre folds antes de declararla mejora.

Se registra F1-macro (CV fold y OOF) y ademas F1/recall de clase 0.
"""
import os
import sys
import warnings

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

warnings.filterwarnings("ignore")
VARIANT = sys.argv[1] if len(sys.argv) > 1 else "D"

BASE = dict(iterations=700, depth=5, learning_rate=0.03, l2_leaf_reg=5,
            auto_class_weights="Balanced")

CONFIGS = [
    ("notebook (base)", {}),
    ("depth=4", {"depth": 4}),
    ("depth=6", {"depth": 6}),
    ("depth=7", {"depth": 7}),
    ("lr=0.02", {"learning_rate": 0.02}),
    ("lr=0.05", {"learning_rate": 0.05}),
    ("lr=0.10", {"learning_rate": 0.10}),
    ("iters=300", {"iterations": 300}),
    ("iters=1500", {"iterations": 1500}),
    ("l2=1", {"l2_leaf_reg": 1}),
    ("l2=10", {"l2_leaf_reg": 10}),
    ("sin balanceo", {"auto_class_weights": None}),
    ("SqrtBalanced", {"auto_class_weights": "SqrtBalanced"}),
    # combinacion prometedora: mas capacidad + mas regularizacion
    ("depth=6 lr=0.05 l2=10", {"depth": 6, "learning_rate": 0.05, "l2_leaf_reg": 10}),
]


def factory(params):
    def build(fold):
        p = dict(BASE)
        p.update(params)
        return CatBoostClassifier(
            loss_function="MultiClass", random_seed=G.SEED + fold,
            verbose=False, thread_count=8, **p)
    return build


def main():
    X, y, Xt, test_ids, const = G.get_xy(VARIANT, clean=True)
    fl = G.folds(X, y)
    print(f"feature set {VARIANT}: {X.shape[1]} features\n")

    rows = []
    for name, params in CONFIGS:
        oof, fs = G.run_oof(factory(params), X, y, fl)
        m = G.metrics_row(y, oof.argmax(axis=1), name)
        m.update({"cv_fold_mean": float(fs.mean()), "cv_fold_std": float(fs.std()),
                  "config": str(params) if params else "base"})
        rows.append(m)
        print(f"{name:24s} CVfold={fs.mean():.4f}+-{fs.std():.4f} "
              f"OOF={m['f1_macro']:.4f} f1_0={m['f1_0']:.4f} rec_0={m['rec_0']:.4f}",
              flush=True)

    df = pd.DataFrame(rows)[["nombre", "config", "f1_macro", "cv_fold_mean",
                             "cv_fold_std", "prec_0", "rec_0", "f1_0",
                             "f1_1", "f1_2", "n_pred_0"]]
    df = df.sort_values("f1_macro", ascending=False)
    G.save_csv(df, os.path.join(G.ANALYSIS_DIR, f"catboost_tuning_{VARIANT}.csv"))
    print("\n" + df.to_string(index=False))

    base_f1 = float(df.loc[df.nombre == "notebook (base)", "f1_macro"].iloc[0])
    base_std = float(df.loc[df.nombre == "notebook (base)", "cv_fold_std"].iloc[0])
    best = df.iloc[0]
    print(f"\nbase OOF={base_f1:.4f} | mejor={best.nombre} OOF={best.f1_macro:.4f} "
          f"delta={best.f1_macro - base_f1:+.4f} | std entre folds del base={base_std:.4f}")
    if best.f1_macro - base_f1 < base_std:
        print("=> La mejora es MENOR que la desviacion entre folds: NO se declara")
        print("   mejora. La configuracion del notebook queda justificada por")
        print("   parsimonia (no hay evidencia de que otra sea mejor).")
    else:
        print("=> Mejora por encima de la desviacion entre folds: candidata real.")


if __name__ == "__main__":
    main()
