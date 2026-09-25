"""
Reproduccion LITERAL del notebook original
(Galaxy_Zoo_Mini_Challenge_resuelto_paso_a_paso.ipynb).

No se corrige nada aqui a proposito: el objetivo es medir si las metricas
declaradas por el usuario son reproducibles.

Metricas declaradas a verificar:
  VERSION MACRO : F1-macro 0.6339 | rec_0 0.4688 | f1_0 0.3557 | w=[1.7,0.9,0.9]
  VERSION CLASE0: F1-macro 0.6317 | rec_0 0.5000 | f1_0 0.3609 | w=[1.9,0.8,1.0]
"""
import json
import os
import warnings

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from catboost import CatBoostClassifier

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ANALYSIS = os.path.join(ROOT, "analysis")
os.makedirs(ANALYSIS, exist_ok=True)

SEED = 42
np.random.seed(SEED)

train = pd.read_csv(os.path.join(ROOT, "GZ_mini_challenge_train.csv"))
test = pd.read_csv(os.path.join(ROOT, "GZ_mini_challenge_test.csv"))
print("Train:", train.shape, "Test:", test.shape)

TARGET = "label"
EXCLUDE = ["ID", "objID", "p_el", "p_cs", "label"]
feature_cols = [c for c in train.columns if c not in EXCLUDE]
y = train[TARGET].astype(int).copy()

constant_cols = [c for c in feature_cols if train[c].nunique(dropna=False) <= 1]
base_features = [c for c in feature_cols if c not in constant_cols]
print("constantes:", len(constant_cols), "| base_features:", len(base_features))

BANDS = ["u", "g", "r", "i", "z"]


def engineer_features(df, base_features):
    out = df[base_features].copy()
    magnitude_families = ["psfMag", "fiberMag", "petroMag", "modelMag", "cModelMag", "dered"]
    color_pairs = [("u", "g"), ("g", "r"), ("r", "i"), ("i", "z"),
                   ("u", "r"), ("g", "i"), ("r", "z")]
    for family in magnitude_families:
        for a, b in color_pairs:
            ca, cb = f"{family}_{a}", f"{family}_{b}"
            if ca in out.columns and cb in out.columns:
                out[f"{family}_color_{a}_{b}"] = out[ca] - out[cb]
    comparisons = [("psfMag", "modelMag", "psf_minus_model"),
                   ("psfMag", "cModelMag", "psf_minus_cmodel"),
                   ("petroMag", "modelMag", "petro_minus_model"),
                   ("fiberMag", "modelMag", "fiber_minus_model")]
    for band in BANDS:
        for left, right, name in comparisons:
            c1, c2 = f"{left}_{band}", f"{right}_{band}"
            if c1 in out.columns and c2 in out.columns:
                out[f"{name}_{band}"] = out[c1] - out[c2]
    return out


X = engineer_features(train, base_features)
X_test_final = engineer_features(test, base_features)
print("features tras ingenieria:", X.shape[1])
assert list(X.columns) == list(X_test_final.columns)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
resultados = []


def evaluar_cv(nombre, modelo):
    scores = cross_val_score(modelo, X, y, cv=cv, scoring="f1_macro", n_jobs=-1)
    print(f"{nombre}: folds={np.round(scores,4)} mean={scores.mean():.4f} std={scores.std():.4f}")
    resultados.append({"modelo": nombre,
                       "f1_macro_mean": float(scores.mean()),
                       "f1_macro_std": float(scores.std()),
                       "folds": [float(s) for s in scores]})


print("\n== 1. COMPARACION DE MODELOS (CV fold scores, como el notebook) ==")
evaluar_cv("LinearSVC balanceado", Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearSVC(C=0.1, class_weight="balanced", max_iter=20000, random_state=SEED))]))
evaluar_cv("ExtraTrees balanceado", ExtraTreesClassifier(
    n_estimators=600, min_samples_leaf=2, max_features="sqrt",
    class_weight="balanced", random_state=SEED, n_jobs=-1))
evaluar_cv("CatBoost balanceado", CatBoostClassifier(
    iterations=700, depth=5, learning_rate=0.03, l2_leaf_reg=5,
    loss_function="MultiClass", auto_class_weights="Balanced",
    random_seed=SEED, verbose=False))

print("\n== 2. OOF CatBoost (semilla SEED+fold, como el notebook) ==")
oof_proba = np.zeros((len(X), 3), dtype=float)
for fold, (idx_train, idx_valid) in enumerate(cv.split(X, y), start=1):
    model = CatBoostClassifier(
        iterations=700, depth=5, learning_rate=0.03, l2_leaf_reg=5,
        loss_function="MultiClass", auto_class_weights="Balanced",
        random_seed=SEED + fold, verbose=False)
    model.fit(X.iloc[idx_train], y.iloc[idx_train])
    oof_proba[idx_valid] = model.predict_proba(X.iloc[idx_valid])

oof_pred = oof_proba.argmax(axis=1)
f1_argmax = f1_score(y, oof_pred, average="macro")
print("F1-macro OOF (argmax):", round(f1_argmax, 4))
print(classification_report(y, oof_pred, digits=4))
print(confusion_matrix(y, oof_pred))
np.save(os.path.join(ANALYSIS, "oof_proba_repro.npy"), oof_proba)


def full_metrics(pred):
    from sklearn.metrics import precision_recall_fscore_support
    p, r, f, _ = precision_recall_fscore_support(y, pred, labels=[0, 1, 2], zero_division=0)
    return {"f1_macro": float(f1_score(y, pred, average="macro")),
            "prec_0": float(p[0]), "rec_0": float(r[0]), "f1_0": float(f[0]),
            "f1_1": float(f[1]), "f1_2": float(f[2])}


print("\n== 3. GRID DE PESOS DEL NOTEBOOK (w0 .7-1.8, w1 .7-1.5, w2 .7-1.4, paso .1) ==")
best_score, best_weights = -1, np.ones(3)
for w0 in np.arange(0.7, 1.81, 0.1):
    for w1 in np.arange(0.7, 1.51, 0.1):
        for w2 in np.arange(0.7, 1.41, 0.1):
            w = np.array([w0, w1, w2])
            s = f1_score(y, (oof_proba * w).argmax(axis=1), average="macro")
            if s > best_score:
                best_score, best_weights = s, w.copy()
print("mejor F1-macro OOF:", round(best_score, 4), "| pesos:", np.round(best_weights, 2))

print("\n== 4. METRICAS EN LOS PESOS DECLARADOS POR EL USUARIO ==")
declarados = {}
for name, w in [("argmax [1,1,1]", [1, 1, 1]),
                ("declarado MACRO [1.7,0.9,0.9]", [1.7, 0.9, 0.9]),
                ("declarado CLASE0 [1.9,0.8,1.0]", [1.9, 0.8, 1.0]),
                ("grid-notebook best", list(np.round(best_weights, 2)))]:
    m = full_metrics((oof_proba * np.array(w, dtype=float)).argmax(axis=1))
    declarados[name] = {"pesos": [float(x) for x in w], **m}
    print(f"{name:34s} F1m={m['f1_macro']:.4f} rec0={m['rec_0']:.4f} f1_0={m['f1_0']:.4f}")

with open(os.path.join(ANALYSIS, "repro_notebook.json"), "w", encoding="utf-8") as fh:
    json.dump({"cv_modelos": resultados,
               "oof_argmax_f1_macro": float(f1_argmax),
               "grid_notebook_best": {"f1_macro": float(best_score),
                                      "pesos": [float(x) for x in best_weights]},
               "pesos_declarados": declarados}, fh, indent=2, ensure_ascii=False)
print("\nescrito analysis/repro_notebook.json")
