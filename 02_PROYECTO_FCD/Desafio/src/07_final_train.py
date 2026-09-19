"""
Entrenamiento final y generacion de submission.

Reentrena EXACTAMENTE el pipeline validado usando TODO train, predice test y
escribe ID,predicted con asserts de formato.

    python src/07_final_train.py --model catboost --variant D \
        --w 1.7 0.9 0.9 --out outputs/predicted_best_macro.csv

Para el modo jerarquico:
    python src/07_final_train.py --model hier --variant D --t 0.35 \
        --out outputs/predicted_best_class0.csv
"""
import argparse
import os
import sys
import warnings

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

warnings.filterwarnings("ignore")


def make_model(kind, seed):
    if kind == "catboost":
        return CatBoostClassifier(
            iterations=700, depth=5, learning_rate=0.03, l2_leaf_reg=5,
            loss_function="MultiClass", auto_class_weights="Balanced",
            random_seed=seed, verbose=False, thread_count=8)
    if kind == "lightgbm":
        return LGBMClassifier(
            n_estimators=600, learning_rate=0.03, num_leaves=15,
            min_child_samples=20, subsample=0.9, subsample_freq=1,
            colsample_bytree=0.7, reg_lambda=5.0, class_weight="balanced",
            random_state=seed, n_jobs=8, verbose=-1)
    if kind == "extratrees":
        return ExtraTreesClassifier(
            n_estimators=800, min_samples_leaf=2, max_features="sqrt",
            class_weight="balanced", random_state=seed, n_jobs=8)
    if kind == "randomforest":
        return RandomForestClassifier(
            n_estimators=800, min_samples_leaf=2, max_features="sqrt",
            class_weight="balanced_subsample", random_state=seed, n_jobs=8)
    raise ValueError(kind)


def predict_flat(kind, X, y, Xt, seeds):
    P = np.zeros((len(Xt), 3))
    for s in seeds:
        m = make_model(kind, s)
        if kind in ("extratrees", "randomforest"):
            med = X.median(numeric_only=True)
            m.fit(X.fillna(med), y)
            P += m.predict_proba(Xt.fillna(med))
        else:
            m.fit(X, y)
            P += m.predict_proba(Xt)
    return P / len(seeds)


def predict_hier(X, y, Xt, seeds):
    yv = np.asarray(y)
    pA0 = np.zeros(len(Xt))
    p2 = np.zeros(len(Xt))
    for s in seeds:
        mA = CatBoostClassifier(iterations=700, depth=5, learning_rate=0.03,
                                l2_leaf_reg=5, loss_function="Logloss",
                                auto_class_weights="Balanced", random_seed=s,
                                verbose=False, thread_count=8)
        mA.fit(X, (yv == 0).astype(int))
        pA0 += mA.predict_proba(Xt)[:, 1]

        dec = yv != 0
        mB = CatBoostClassifier(iterations=700, depth=5, learning_rate=0.03,
                                l2_leaf_reg=5, loss_function="Logloss",
                                auto_class_weights="Balanced", random_seed=s,
                                verbose=False, thread_count=8)
        mB.fit(X[dec], (yv[dec] == 2).astype(int))
        p2 += mB.predict_proba(Xt)[:, 1]
    pA0 /= len(seeds)
    p2 /= len(seeds)
    return pA0, p2


def write_submission(test_ids, pred, out_path, n_test_expected):
    sub = pd.DataFrame({"ID": np.asarray(test_ids), "predicted": np.asarray(pred).astype(int)})

    assert list(sub.columns) == ["ID", "predicted"], "columnas incorrectas"
    assert sub.shape[1] == 2, "debe tener exactamente dos columnas"
    assert len(sub) == n_test_expected, f"filas {len(sub)} != test {n_test_expected}"
    assert sub["ID"].is_unique, "ID duplicado"
    assert sub.isna().sum().sum() == 0, "hay NaN"
    assert set(sub["predicted"].unique()).issubset({0, 1, 2}), "clases fuera de {0,1,2}"
    assert sub["predicted"].dtype.kind in "iu", "predicted no es entero"

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    sub.to_csv(out_path, index=False)

    # verificacion de que no se escribio indice accidental
    with open(out_path, "r", encoding="utf-8") as fh:
        head = fh.readline().strip()
    assert head == "ID,predicted", f"cabecera inesperada: {head}"
    re_read = pd.read_csv(out_path)
    assert list(re_read.columns) == ["ID", "predicted"], "indice accidental detectado"
    assert len(re_read) == n_test_expected

    print(f"OK -> {out_path}")
    print("  distribucion:", re_read["predicted"].value_counts(normalize=True)
          .sort_index().round(4).to_dict())
    print("  conteos     :", re_read["predicted"].value_counts().sort_index().to_dict())
    return sub


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--variant", default="D")
    ap.add_argument("--w", nargs=3, type=float, default=[1.0, 1.0, 1.0])
    ap.add_argument("--t", type=float, default=None, help="umbral P(clase0) modo hier")
    ap.add_argument("--seeds", type=int, default=1)
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-clean", action="store_true")
    a = ap.parse_args()

    seeds = [G.SEED + i for i in range(a.seeds)]
    X, y, Xt, test_ids, const = G.get_xy(a.variant, clean=not a.no_clean)
    print(f"modelo={a.model} variante={a.variant} nfeat={X.shape[1]} "
          f"seeds={seeds} pesos={a.w} t={a.t}")

    if a.model == "hier":
        pA0, p2 = predict_hier(X, y, Xt, seeds)
        assert a.t is not None, "modo hier requiere --t"
        pred = np.where(pA0 >= a.t, 0, np.where(p2 >= 0.5, 2, 1))
    else:
        P = predict_flat(a.model, X, y, Xt, seeds)
        pred = G.apply_weights(P, a.w)

    write_submission(test_ids, pred, os.path.join(G.ROOT, a.out), len(Xt))


if __name__ == "__main__":
    main()
