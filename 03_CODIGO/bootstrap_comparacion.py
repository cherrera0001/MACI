"""
Comparacion estadistica de los 3 ensambles (target log) sobre 2017:
  - Bootstrap pareado (B=2000) del delta MAE entre modelos, IC 95%.
  - Error por segmento (Type, Regionname, suburbio nuevo, cuartil de precio).
  - Importancia por permutacion (post-hoc) del mejor modelo sobre 2017.
Guarda: predicciones_2017.csv, comparacion_estadistica.json
"""
import json, warnings
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_absolute_error
warnings.filterwarnings("ignore")
rng = np.random.default_rng(42)

CSV = r"F:\MACI\02_PROYECTO_FCD\Hito1\Corrección\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
df = pd.read_csv(CSV); df["Date"] = pd.to_datetime(df["Date"], dayfirst=True); df["Year"] = df["Date"].dt.year
tr, te = df[df.Year == 2016].copy(), df[df.Year == 2017].copy()
NUM = ["Rooms", "Distance", "Bedroom2", "Bathroom", "Car", "Landsize", "BuildingArea", "YearBuilt", "Lattitude", "Longtitude", "Propertycount"]
CAT = ["Type", "Method", "Regionname"]
prep = lambda: ColumnTransformer([("num", SimpleImputer(strategy="median", add_indicator=True), NUM),
                                  ("cat", Pipeline([("imp", SimpleImputer(strategy="constant", fill_value="missing")), ("oh", OneHotEncoder(handle_unknown="ignore"))]), CAT)])
X_tr, X_te, y_tr, y_te = tr[NUM + CAT], te[NUM + CAT], tr["Price"].values, te["Price"].values
modelos = {
    "Random Forest": RandomForestRegressor(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=400, max_depth=4, learning_rate=0.05, subsample=0.8, random_state=0),
    "HistGradientBoosting": HistGradientBoostingRegressor(max_iter=500, learning_rate=0.05, max_leaf_nodes=31, l2_regularization=1.0, random_state=0),
}
pipes, pred = {}, {}
for n, m in modelos.items():
    p = Pipeline([("prep", prep()), ("m", m)]).fit(X_tr, np.log1p(y_tr)); pipes[n] = p
    pred[n] = np.expm1(p.predict(X_te)); print(f"{n:22s} MAE 2017 = {mean_absolute_error(y_te, pred[n]):,.0f}", flush=True)

out = te[["Suburb", "Type", "Regionname", "Rooms", "Distance", "Price"]].copy()
for n in pred: out[f"pred_{n.replace(' ', '_')}"] = pred[n]
out["suburbio_nuevo"] = ~te["Suburb"].isin(set(tr["Suburb"]))
out.to_csv(r"F:\MACI\05_RESULTADOS\predicciones_2017.csv", index=False)

# --- bootstrap pareado
res = {"bootstrap_delta_MAE": {}}
abs_err = {n: np.abs(y_te - pred[n]) for n in pred}
B, N = 2000, len(y_te)
idx = rng.integers(0, N, size=(B, N))
pares = [("HistGradientBoosting", "Gradient Boosting"), ("HistGradientBoosting", "Random Forest"), ("Gradient Boosting", "Random Forest")]
for a, b in pares:
    d = abs_err[a] - abs_err[b]                      # negativo => a mejor
    boots = d[idx].mean(axis=1)
    lo, hi = np.percentile(boots, [2.5, 97.5])
    res["bootstrap_delta_MAE"][f"{a} - {b}"] = dict(delta=float(d.mean()), ic95=[float(lo), float(hi)],
                                                     p_a_mejor=float((boots < 0).mean()), significativo=bool(hi < 0 or lo > 0))
    print(f"dMAE({a} - {b}) = {d.mean():+,.0f}  IC95 [{lo:+,.0f}, {hi:+,.0f}]  P(a mejor)={(boots<0).mean():.3f}", flush=True)

# --- error por segmento (mejor modelo = menor MAE)
best = min(pred, key=lambda n: abs_err[n].mean()); res["mejor_modelo"] = best
seg = {}
e = pd.Series(abs_err[best], index=te.index)
seg["Type"] = te.groupby("Type").apply(lambda g: dict(n=len(g), MAE=float(e[g.index].mean()), MAPE=float((e[g.index] / g["Price"]).mean() * 100))).to_dict()
seg["Regionname"] = te.groupby("Regionname").apply(lambda g: dict(n=len(g), MAE=float(e[g.index].mean()), MAPE=float((e[g.index] / g["Price"]).mean() * 100))).to_dict()
seg["suburbio_nuevo"] = out.groupby("suburbio_nuevo").apply(lambda g: dict(n=len(g), MAE=float(e[g.index].mean()), MAPE=float((e[g.index] / g["Price"]).mean() * 100))).to_dict()
q = pd.qcut(te["Price"], 4, labels=["Q1 bajo", "Q2", "Q3", "Q4 alto"])
seg["cuartil_precio"] = te.groupby(q).apply(lambda g: dict(n=len(g), rango=[float(g.Price.min()), float(g.Price.max())], MAE=float(e[g.index].mean()), MAPE=float((e[g.index] / g["Price"]).mean() * 100))).to_dict()
res["error_por_segmento"] = {k: {str(kk): vv for kk, vv in v.items()} for k, v in seg.items()}
res["MAPE_global"] = float((e / te["Price"]).mean() * 100)
res["pct_dentro"] = {f"±{m//1000}k": float((e <= m).mean() * 100) for m in (50000, 100000, 150000, 200000)}
res["pct_dentro_10pct"] = float(((e / te["Price"]) <= 0.10).mean() * 100)
res["pct_dentro_20pct"] = float(((e / te["Price"]) <= 0.20).mean() * 100)
print("\nMejor:", best, "| MAPE global", f"{res['MAPE_global']:.1f}%", "| dentro de ±10%:", f"{res['pct_dentro_10pct']:.1f}%", "| ±20%:", f"{res['pct_dentro_20pct']:.1f}%", flush=True)
for k, v in res["error_por_segmento"].items():
    print(f"  [{k}]"); [print(f"     {kk:32s} n={vv['n']:5d} MAE={vv['MAE']:>9,.0f} MAPE={vv['MAPE']:.1f}%") for kk, vv in v.items()]

# --- importancia por permutacion sobre 2017 (post-hoc), en escala log
pi = permutation_importance(pipes[best], X_te, np.log1p(y_te), n_repeats=10, random_state=0, n_jobs=-1, scoring="neg_mean_absolute_error")
imp = sorted(zip(NUM + CAT, pi.importances_mean, pi.importances_std), key=lambda t: -t[1])
res["importancia_permutacion_2017"] = [dict(feature=f, mean=float(m), std=float(s)) for f, m, s in imp]
print("\nImportancia por permutacion (2017, delta MAE log):")
for f, m, s in imp: print(f"  {f:14s} {m:+.4f} ± {s:.4f}")
json.dump(res, open(r"F:\MACI\05_RESULTADOS\comparacion_estadistica.json", "w"), indent=2, default=str)
print("\nGuardado: comparacion_estadistica.json, predicciones_2017.csv")
