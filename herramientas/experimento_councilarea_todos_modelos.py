"""
Extension del experimento CouncilArea a TODOS los modelos.

El experimento original (experimento_councilarea.py) solo probo
HistGradientBoosting. Esto lo extiende a la jerarquia completa para que la
comparacion A vs B sea del mismo alcance que resultados_temporal.json.

Reutiliza la configuracion del script original: mismo preprocesamiento, mismas
features, mismas semillas, mismos folds. Solo cambia el modelo evaluado.

FASE 1 unicamente: solo 2016. No toca 2017.

USO
  python 03_SCRIPTS/experimento_councilarea_todos_modelos.py
"""
import json
import warnings
from datetime import date

import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import (GradientBoostingRegressor,
                              HistGradientBoostingRegressor,
                              RandomForestRegressor)
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

from experimento_councilarea import (CAT_A, CAT_B, CSV, NUM, N_VALIDATION, RS,
                                     SEEDS, evaluar, preproc)

warnings.filterwarnings("ignore")

OUT = r"F:\MACI\09_RESULTADOS\experimento_councilarea_todos_modelos_%s.json" % date.today().isoformat()
METRICAS = ("MAE", "RMSE", "R2")


def modelos(seed):
    """Misma jerarquia y mismos hiperparametros que modelamiento_temporal.py."""
    return {
        "Baseline (mediana)": (False, DummyRegressor(strategy="median")),
        "Ridge (lineal)": (True, Ridge(alpha=1.0, random_state=seed)),
        "Arbol de decision": (False, DecisionTreeRegressor(
            max_depth=8, min_samples_leaf=20, random_state=seed)),
        "Random Forest": (False, RandomForestRegressor(
            n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=seed)),
        "Gradient Boosting": (False, GradientBoostingRegressor(
            n_estimators=400, max_depth=4, learning_rate=0.05,
            subsample=0.8, random_state=seed)),
        "HistGradientBoosting": (False, HistGradientBoostingRegressor(
            max_iter=500, learning_rate=0.05, max_leaf_nodes=31,
            l2_regularization=1.0, random_state=seed)),
    }


def construir(nombre, cats, seed):
    scale, reg = modelos(seed)[nombre]
    pasos = [("prep", preproc(cats))]
    if scale:
        pasos.append(("sc", StandardScaler(with_mean=False)))
    pasos.append(("reg", reg))
    return Pipeline(pasos)


def main():
    df = pd.read_csv(CSV)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df["Year"] = df["Date"].dt.year
    a = df[df.Year == 2016].copy()
    y = a["Price"].values

    idx_tr, idx_va = train_test_split(
        np.arange(len(a)), test_size=N_VALIDATION, random_state=RS, shuffle=True)
    folds = list(KFold(n_splits=5, shuffle=True, random_state=RS).split(a))

    nombres = list(modelos(0).keys())
    doc = {
        "experimento": "CouncilArea A vs B, jerarquia completa de modelos",
        "fecha": date.today().isoformat(),
        "alcance": "FASE 1 - solo 2016. 2017 no fue tocado.",
        "target": "log1p(Price), metricas en AUD originales",
        "semillas": SEEDS, "random_state": RS,
        "cat_A": CAT_A, "cat_B": CAT_B, "features_num": NUM,
        "resultados": {},
    }

    print(f"{'modelo':<24}{'cfg':>4}{'CV MAE':>12}{'±std':>9}{'CV R2':>9}"
          f"{'HO MAE':>12}{'HO R2':>8}")
    print("-" * 78)

    for nombre in nombres:
        # El baseline y Ridge no dependen de la semilla del modelo de forma
        # relevante; se mantienen las 5 para que el diseno sea identico.
        for cfg, cats in (("A", CAT_A), ("B", CAT_B)):
            X = a[NUM + cats]
            cv, ho = [], []
            for s in SEEDS:
                for k, (tr, va) in enumerate(folds):
                    m = evaluar(construir(nombre, cats, s),
                                X.iloc[tr], y[tr], X.iloc[va], y[va])
                    m.update(seed=s, fold=k)
                    cv.append(m)
                ho.append(evaluar(construir(nombre, cats, s),
                                  X.iloc[idx_tr], y[idx_tr],
                                  X.iloc[idx_va], y[idx_va]))

            doc["resultados"].setdefault(nombre, {})[cfg] = {
                "cv": {
                    "n_medidas": len(cv),
                    "media": {m: float(np.mean([x[m] for x in cv])) for m in METRICAS},
                    "std": {m: float(np.std([x[m] for x in cv])) for m in METRICAS},
                    "detalle": cv,
                },
                "holdout": {
                    "n_train": int(len(idx_tr)), "n_validation": int(len(idx_va)),
                    "media": {m: float(np.mean([x[m] for x in ho])) for m in METRICAS},
                    "std": {m: float(np.std([x[m] for x in ho])) for m in METRICAS},
                },
            }
            r = doc["resultados"][nombre][cfg]
            print(f"{nombre:<24}{cfg:>4}{r['cv']['media']['MAE']:>12,.0f}"
                  f"{r['cv']['std']['MAE']:>9,.0f}{r['cv']['media']['R2']:>9.4f}"
                  f"{r['holdout']['media']['MAE']:>12,.0f}"
                  f"{r['holdout']['media']['R2']:>8.4f}", flush=True)

        # Diferencias pareadas A vs B: mismo fold, misma semilla.
        ca = doc["resultados"][nombre]["A"]["cv"]["detalle"]
        cb = doc["resultados"][nombre]["B"]["cv"]["detalle"]
        dmae = [xa["MAE"] - xb["MAE"] for xa, xb in zip(ca, cb)]
        dr2 = [xb["R2"] - xa["R2"] for xa, xb in zip(ca, cb)]
        media, std = float(np.mean(dmae)), float(np.std(dmae))
        doc["resultados"][nombre]["pareado"] = {
            "delta_MAE_media": media, "delta_MAE_std": std,
            "delta_R2_media": float(np.mean(dr2)),
            "veces_B_mejor": int(sum(d > 0 for d in dmae)),
            "n_pares": len(dmae),
            "pct_MAE": media / doc["resultados"][nombre]["A"]["cv"]["media"]["MAE"] * 100,
            "t_aprox": media / (std / np.sqrt(len(dmae))) if std > 0 else None,
        }
        p = doc["resultados"][nombre]["pareado"]
        t = p["t_aprox"]
        print(f"{'  -> delta B-A':<28}{media:>+12,.0f} AUD  ({p['pct_MAE']:+.2f}%)  "
              f"B gana {p['veces_B_mejor']}/{p['n_pares']}  "
              f"t={t:.2f}" if t is not None else "")
        print()

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f"-> guardado en {OUT}")
    print("2017 NO fue tocado en este script.")


if __name__ == "__main__":
    main()
