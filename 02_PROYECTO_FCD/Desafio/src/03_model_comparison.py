"""
Comparacion de modelos con folds identicos, feature set identico y metrica
identica. Se pasa el feature set por linea de comandos:

    python src/03_model_comparison.py D

Todos los modelos que no aceptan NaN reciben imputacion por mediana ajustada
DENTRO del fold de entrenamiento (via run_oof(needs_dense_nan_fill=True)),
de modo que no hay fuga.

Se guardan las probabilidades OOF de cada modelo para el ensemble posterior.
"""
import os
import sys
import warnings

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

warnings.filterwarnings("ignore")

VARIANT = sys.argv[1] if len(sys.argv) > 1 else "D"


def build_models(y):
    n = len(y)
    classes, counts = np.unique(y, return_counts=True)
    cw = {int(c): n / (len(classes) * k) for c, k in zip(classes, counts)}
    sample_w = np.array([cw[int(v)] for v in y])

    return {
        "LinearSVC(bal)": (lambda f: Pipeline([
            ("sc", StandardScaler()),
            ("m", LinearSVC(C=0.1, class_weight="balanced",
                            max_iter=20000, random_state=G.SEED))]), True, None),
        "LogisticRegression(bal)": (lambda f: Pipeline([
            ("sc", StandardScaler()),
            ("m", LogisticRegression(C=0.1, class_weight="balanced",
                                     max_iter=5000, random_state=G.SEED))]), True, None),
        "RandomForest(bal_sub)": (lambda f: RandomForestClassifier(
            n_estimators=800, min_samples_leaf=2, max_features="sqrt",
            class_weight="balanced_subsample", random_state=G.SEED + f,
            n_jobs=8), True, None),
        "ExtraTrees(bal)": (lambda f: ExtraTreesClassifier(
            n_estimators=800, min_samples_leaf=2, max_features="sqrt",
            class_weight="balanced", random_state=G.SEED + f,
            n_jobs=8), True, None),
        "LightGBM(bal)": (lambda f: LGBMClassifier(
            n_estimators=600, learning_rate=0.03, num_leaves=15,
            min_child_samples=20, subsample=0.9, subsample_freq=1,
            colsample_bytree=0.7, reg_lambda=5.0, class_weight="balanced",
            random_state=G.SEED + f, n_jobs=8, verbose=-1), False, None),
        "XGBoost(w)": (lambda f: XGBClassifier(
            n_estimators=600, learning_rate=0.03, max_depth=4,
            subsample=0.9, colsample_bytree=0.7, reg_lambda=5.0,
            objective="multi:softprob", num_class=3, tree_method="hist",
            random_state=G.SEED + f, n_jobs=8, eval_metric="mlogloss"), False, sample_w),
        "CatBoost(bal)": (lambda f: CatBoostClassifier(
            iterations=700, depth=5, learning_rate=0.03, l2_leaf_reg=5,
            loss_function="MultiClass", auto_class_weights="Balanced",
            random_seed=G.SEED + f, verbose=False, thread_count=8), False, None),
    }


def run_oof_weighted(factory, X, y, fl, sample_w, fill):
    """run_oof pero pasando sample_weight (XGBoost no tiene class_weight)."""
    oof = np.zeros((len(X), 3))
    scores = []
    yv = np.asarray(y)
    from sklearn.metrics import f1_score
    for k, (itr, iva) in enumerate(fl):
        Xtr, Xva = X.iloc[itr], X.iloc[iva]
        if fill:
            med = Xtr.median(numeric_only=True)
            Xtr, Xva = Xtr.fillna(med), Xva.fillna(med)
        m = factory(k)
        m.fit(Xtr, yv[itr], sample_weight=sample_w[itr])
        oof[iva] = m.predict_proba(Xva)
        scores.append(f1_score(yv[iva], oof[iva].argmax(1), average="macro"))
    return oof, np.array(scores)


def main():
    X, y, Xt, test_ids, const = G.get_xy(VARIANT, clean=True)
    fl = G.folds(X, y)
    print(f"feature set {VARIANT}: {X.shape[1]} features, {len(X)} filas\n")

    rows, store = [], {}
    for name, (factory, fill, sw) in build_models(y).items():
        if sw is not None:
            oof, fs = run_oof_weighted(factory, X, y, fl, sw, fill)
        else:
            oof, fs = G.run_oof(factory, X, y, fl, needs_dense_nan_fill=fill)
        pred = oof.argmax(axis=1)
        m = G.metrics_row(y, pred, name)
        m.update({"features": VARIANT, "n_features": X.shape[1],
                  "balance": "balanced",
                  "cv_fold_mean": float(fs.mean()), "cv_fold_std": float(fs.std())})
        rows.append(m)
        store[name] = oof
        print(f"{name:26s} CVfold={fs.mean():.4f}+-{fs.std():.4f} "
              f"OOF={m['f1_macro']:.4f} f1_0={m['f1_0']:.4f} rec_0={m['rec_0']:.4f}",
              flush=True)

    df = pd.DataFrame(rows)[[
        "nombre", "features", "n_features", "balance", "f1_macro",
        "cv_fold_mean", "cv_fold_std", "prec_0", "rec_0", "f1_0",
        "f1_1", "f1_2", "n_pred_0"]].sort_values("f1_macro", ascending=False)
    G.save_csv(df, os.path.join(G.ANALYSIS_DIR, f"model_comparison_{VARIANT}.csv"))
    print("\n" + df.to_string(index=False))

    np.savez(os.path.join(G.ANALYSIS_DIR, f"oof_models_{VARIANT}.npz"), **store)
    print(f"\nguardado analysis/oof_models_{VARIANT}.npz")


if __name__ == "__main__":
    main()
