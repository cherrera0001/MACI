"""
Ablacion de feature sets con folds identicos y modelo identico (CatBoost del
notebook). Tambien cuantifica el efecto del bug de centinelas -9999.

Feature sets:
  A = originales (sin constantes)
  B = A + colores
  C = A + diferencias morfologicas
  D = A + colores + diferencias  (= notebook)
  E = D sin metadatos de observacion/posicion (mjd, cx, cy, cz, score, extinction_*)

Cada uno se evalua con y sin limpieza de centinelas para separar los dos
efectos. Se reportan CV fold scores (mean/std) y el OOF global, que NO son
lo mismo.
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


def catboost_factory(fold):
    return CatBoostClassifier(
        iterations=700, depth=5, learning_rate=0.03, l2_leaf_reg=5,
        loss_function="MultiClass", auto_class_weights="Balanced",
        random_seed=G.SEED + fold, verbose=False, thread_count=8)


def main():
    rows = []
    store = {}
    for clean in (False, True):
        for variant in ("A", "B", "C", "D", "E"):
            X, y, Xt, test_ids, const = G.get_xy(variant, clean=clean)
            fl = G.folds(X, y)
            oof, fs = G.run_oof(catboost_factory, X, y, fl)
            pred = oof.argmax(axis=1)
            m = G.metrics_row(y, pred, f"{variant}{'_clean' if clean else '_raw'}")
            m.update({
                "variante": variant,
                "centinelas_limpiados": clean,
                "n_features": X.shape[1],
                "cv_fold_mean": float(fs.mean()),
                "cv_fold_std": float(fs.std()),
                "oof_f1_macro": m["f1_macro"],
            })
            rows.append(m)
            store[(variant, clean)] = oof
            print(f"{variant} clean={clean!s:5s} nfeat={X.shape[1]:4d} "
                  f"CVfold={fs.mean():.4f}+-{fs.std():.4f}  "
                  f"OOF={m['f1_macro']:.4f}  f1_0={m['f1_0']:.4f} rec_0={m['rec_0']:.4f}",
                  flush=True)

    df = pd.DataFrame(rows)
    cols = ["nombre", "variante", "centinelas_limpiados", "n_features",
            "cv_fold_mean", "cv_fold_std", "oof_f1_macro",
            "prec_0", "rec_0", "f1_0", "f1_1", "f1_2", "n_pred_0"]
    df = df[cols].sort_values("oof_f1_macro", ascending=False)
    G.save_csv(df, os.path.join(G.ANALYSIS_DIR, "ablation_results.csv"))
    print("\n" + df.to_string(index=False))

    np.savez(os.path.join(G.ANALYSIS_DIR, "oof_ablation.npz"),
             **{f"{v}_{int(c)}": p for (v, c), p in store.items()})
    print("\nguardado analysis/oof_ablation.npz")


if __name__ == "__main__":
    main()
