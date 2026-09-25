"""
Galaxy Zoo Mini Challenge - libreria compartida.

Todos los experimentos importan de aqui para garantizar:
  - mismos folds (StratifiedKFold 5, shuffle, seed 42)
  - mismos feature sets
  - misma metrica (F1-macro) y mismo reporte por clase
  - misma separacion CV-fold-score vs OOF-global-score

Reglas de no-fuga aplicadas:
  - label, p_cs, p_el, ID, objID nunca son features.
  - Toda transformacion que aprende parametros (scaler) va dentro de Pipeline,
    por tanto se ajusta solo con el fold de entrenamiento.
  - La ingenieria de features es fila-a-fila (diferencias de columnas), no
    aprende parametros globales -> no introduce fuga.
  - Los centinelas -9999 se convierten a NaN fila-a-fila (sin fuga).
"""
from __future__ import annotations

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, precision_recall_fscore_support, confusion_matrix

SEED = 42
N_SPLITS = 5
TARGET = "label"
LEAKY = ["ID", "objID", "p_el", "p_cs", "label"]
BANDS = ["u", "g", "r", "i", "z"]

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TRAIN_CSV = os.path.join(ROOT, "GZ_mini_challenge_train.csv")
TEST_CSV = os.path.join(ROOT, "GZ_mini_challenge_test.csv")
ANALYSIS_DIR = os.path.join(ROOT, "analysis")
OUTPUT_DIR = os.path.join(ROOT, "outputs")

MAG_FAMILIES = ["psfMag", "fiberMag", "petroMag", "modelMag", "cModelMag", "dered"]
COLOR_PAIRS = [("u", "g"), ("g", "r"), ("r", "i"), ("i", "z"),
               ("u", "r"), ("g", "i"), ("r", "z")]
MORPH_COMPARISONS = [
    ("psfMag", "modelMag", "psf_minus_model"),
    ("psfMag", "cModelMag", "psf_minus_cmodel"),
    ("petroMag", "modelMag", "petro_minus_model"),
    ("fiberMag", "modelMag", "fiber_minus_model"),
]

# Columnas de metadatos de observacion / posicion en el cielo.
# Auditoria: presentan el drift train-test mas alto (KS 0.21-0.32) y no son
# propiedades fisicas de la galaxia -> candidatas a exclusion (feature set E).
META_DRIFT_COLS = ["mjd", "cx", "cy", "cz", "score",
                   "extinction_u", "extinction_g", "extinction_r",
                   "extinction_i", "extinction_z"]


# --------------------------------------------------------------------------
# Carga
# --------------------------------------------------------------------------
def load_raw():
    return pd.read_csv(TRAIN_CSV), pd.read_csv(TEST_CSV)


def clean_sentinels(df: pd.DataFrame, cols) -> pd.DataFrame:
    """SDSS codifica mediciones invalidas como -9999. Sustituir por NaN.

    Es una operacion fila-a-fila con un umbral fisico fijo (una magnitud
    aparente nunca es <= -99), por tanto no aprende nada de los datos y no
    puede generar fuga entre folds.
    """
    out = df.copy()
    sub = out[cols]
    out[cols] = sub.mask(sub <= -99.0)
    return out


def base_feature_list(train: pd.DataFrame):
    """Features originales usables: sin leaky, sin constantes (medido en train)."""
    feats = [c for c in train.columns if c not in LEAKY]
    const = [c for c in feats if train[c].nunique(dropna=False) <= 1]
    return [c for c in feats if c not in const], const


# --------------------------------------------------------------------------
# Ingenieria de features
# --------------------------------------------------------------------------
def add_colors(out: pd.DataFrame, src: pd.DataFrame) -> pd.DataFrame:
    for fam in MAG_FAMILIES:
        for a, b in COLOR_PAIRS:
            ca, cb = f"{fam}_{a}", f"{fam}_{b}"
            if ca in src.columns and cb in src.columns:
                out[f"{fam}_color_{a}_{b}"] = src[ca] - src[cb]
    return out


def add_morph(out: pd.DataFrame, src: pd.DataFrame) -> pd.DataFrame:
    for band in BANDS:
        for left, right, name in MORPH_COMPARISONS:
            c1, c2 = f"{left}_{band}", f"{right}_{band}"
            if c1 in src.columns and c2 in src.columns:
                out[f"{name}_{band}"] = src[c1] - src[c2]
    return out


def build_features(src: pd.DataFrame, base: list, variant: str) -> pd.DataFrame:
    """variant in {A,B,C,D,E}.

    A = originales
    B = A + colores
    C = A + diferencias morfologicas
    D = A + colores + diferencias   (equivalente al notebook original)
    E = D sin metadatos de observacion/posicion (META_DRIFT_COLS)
    """
    if variant == "E":
        keep = [c for c in base if c not in META_DRIFT_COLS]
        out = src[keep].copy()
        out = add_colors(out, src)
        out = add_morph(out, src)
        return out

    out = src[base].copy()
    if variant in ("B", "D"):
        out = add_colors(out, src)
    if variant in ("C", "D"):
        out = add_morph(out, src)
    return out


def get_xy(variant: str, clean: bool = True):
    """Devuelve X_train, y, X_test alineados para un feature set."""
    train, test = load_raw()
    base, const = base_feature_list(train)
    if clean:
        magcols = [c for c in base if ("Mag" in c) or c.startswith("dered") or c.startswith("mRrCc")]
        train = clean_sentinels(train, magcols)
        test = clean_sentinels(test, magcols)
    X = build_features(train, base, variant)
    Xt = build_features(test, base, variant)
    y = train[TARGET].astype(int).copy()
    assert list(X.columns) == list(Xt.columns), "desalineacion train/test"
    return X, y, Xt, test["ID"].values, const


# --------------------------------------------------------------------------
# Validacion
# --------------------------------------------------------------------------
def folds(X, y):
    cv = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    return list(cv.split(X, y))


def _proba(model, X, n_classes=3):
    """Probabilidades para modelos con predict_proba o solo decision_function."""
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X)
    d = model.decision_function(X)
    d = np.asarray(d, dtype=float)
    if d.ndim == 1:
        d = np.column_stack([-d, d])
    d = d - d.max(axis=1, keepdims=True)
    e = np.exp(d)
    return e / e.sum(axis=1, keepdims=True)


def run_oof(model_factory, X, y, fold_list=None, needs_dense_nan_fill=False):
    """Genera probabilidades OOF y scores por fold.

    model_factory(fold_idx) -> estimador nuevo sin entrenar.
    Devuelve (oof_proba, fold_scores).
    """
    fold_list = fold_list or folds(X, y)
    oof = np.zeros((len(X), 3), dtype=float)
    fold_scores = []
    yv = np.asarray(y)
    for k, (itr, iva) in enumerate(fold_list):
        Xtr, Xva = X.iloc[itr], X.iloc[iva]
        if needs_dense_nan_fill:
            med = Xtr.median(numeric_only=True)
            Xtr = Xtr.fillna(med)
            Xva = Xva.fillna(med)
        m = model_factory(k)
        m.fit(Xtr, yv[itr])
        p = _proba(m, Xva)
        oof[iva] = p
        fold_scores.append(f1_score(yv[iva], p.argmax(axis=1), average="macro"))
    return oof, np.array(fold_scores)


# --------------------------------------------------------------------------
# Metricas
# --------------------------------------------------------------------------
def metrics_row(y, pred, label=""):
    y = np.asarray(y)
    p, r, f, s = precision_recall_fscore_support(y, pred, labels=[0, 1, 2], zero_division=0)
    return {
        "nombre": label,
        "f1_macro": f1_score(y, pred, average="macro"),
        "prec_0": p[0], "rec_0": r[0], "f1_0": f[0],
        "prec_1": p[1], "rec_1": r[1], "f1_1": f[1],
        "prec_2": p[2], "rec_2": r[2], "f1_2": f[2],
        "n_pred_0": int((pred == 0).sum()),
    }


def report(y, pred, title=""):
    y = np.asarray(y)
    m = metrics_row(y, pred, title)
    print(f"--- {title} ---")
    print(f"F1-macro OOF: {m['f1_macro']:.4f}")
    for c in (0, 1, 2):
        print(f"  clase {c}: P={m[f'prec_{c}']:.4f} R={m[f'rec_{c}']:.4f} F1={m[f'f1_{c}']:.4f}")
    print("matriz de confusion (filas=real, cols=pred):")
    print(confusion_matrix(y, pred, labels=[0, 1, 2]))
    return m


# --------------------------------------------------------------------------
# Regla de decision
# --------------------------------------------------------------------------
def apply_weights(proba, w):
    return (proba * np.asarray(w, dtype=float)).argmax(axis=1)


def weight_grid(step=0.05, lo=0.5, hi=2.6):
    """Pesos normalizados con w1 fijo = 1.0 (la escala global es irrelevante
    para el argmax, solo importan los cocientes w0/w1 y w2/w1)."""
    g = np.arange(lo, hi + 1e-9, step)
    for w0 in g:
        for w2 in g:
            yield (w0, 1.0, w2)


def search_weights(proba, y, step=0.05, lo=0.5, hi=2.6):
    """Barrido sistematico. Devuelve DataFrame con todas las combinaciones."""
    y = np.asarray(y)
    rows = []
    for w in weight_grid(step, lo, hi):
        pred = apply_weights(proba, w)
        p, r, f, _ = precision_recall_fscore_support(y, pred, labels=[0, 1, 2], zero_division=0)
        rows.append({
            "w0": w[0], "w1": w[1], "w2": w[2],
            "f1_macro": f1_score(y, pred, average="macro"),
            "f1_0": f[0], "rec_0": r[0], "prec_0": p[0],
            "f1_1": f[1], "f1_2": f[2],
        })
    return pd.DataFrame(rows)


def pareto_front(df, objs=("f1_macro", "f1_0", "rec_0")):
    """Frente de Pareto (maximizacion) sobre las columnas objs."""
    V = df[list(objs)].to_numpy()
    keep = np.ones(len(V), dtype=bool)
    for i in range(len(V)):
        if not keep[i]:
            continue
        dominated = np.all(V >= V[i], axis=1) & np.any(V > V[i], axis=1)
        if dominated.any():
            keep[i] = False
    return df[keep].copy()


def nested_weight_score(proba, y, fold_list, step=0.05, lo=0.5, hi=2.6):
    """Estimacion HONESTA del beneficio de optimizar pesos.

    Los pesos se ajustan en los folds de entrenamiento (usando sus propias
    probabilidades OOF) y se aplican al fold de validacion, que no participo
    en la busqueda. Evita el sesgo optimista de tunear y reportar sobre el
    mismo OOF completo.
    """
    y = np.asarray(y)
    pred = np.zeros(len(y), dtype=int)
    chosen = []
    for itr, iva in fold_list:
        res = search_weights(proba[itr], y[itr], step, lo, hi)
        best = res.sort_values("f1_macro", ascending=False).iloc[0]
        w = (best.w0, best.w1, best.w2)
        chosen.append(w)
        pred[iva] = apply_weights(proba[iva], w)
    return pred, chosen


def save_csv(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print("escrito:", path)
