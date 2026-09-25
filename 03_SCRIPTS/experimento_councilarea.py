"""
Experimento controlado: aporta señal CouncilArea al modelo de Melbourne?

DISENO
  A (control)     Configuracion actual reproducible, SIN CouncilArea.
  B (experimento) Identica en todo, SOLO anade CouncilArea a las categoricas.

Se aisla una unica variable. No cambian modelo, hiperparametros, split,
preprocesamiento ni semillas entre A y B.

HIPOTESIS
  H0  Anadir CouncilArea no produce mejora reproducible respecto de A.
  H1  CouncilArea aporta senal y produce mejora reproducible.

FASES
  fase1   Solo 2016. Holdout 5.702/634 + CV 5-fold x 5 semillas, pareado.
          Incluye el analisis de faltantes de CouncilArea (fase 4 del encargo).
  fase3   Test temporal sobre 2017. UNA sola vez, y solo tras decidir en fase1.
          Exige --config A|B explicito: el test no se toca por accidente.

USO
  python 03_SCRIPTS/experimento_councilarea.py fase1
  python 03_SCRIPTS/experimento_councilarea.py fase3 --config B

Los resultados se guardan como experimento independiente con fecha. No se
sobrescribe ningun resultado anterior.
"""
import argparse
import json
import sys
import warnings
from datetime import date

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

warnings.filterwarnings("ignore")

CSV = r"F:\MACI\08_PROYECTO_FCD\Hito1\Corrección\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
OUT = r"F:\MACI\09_RESULTADOS\experimento_councilarea_%s.json" % date.today().isoformat()

RS = 42
SEEDS = [0, 1, 2, 3, 4]
N_VALIDATION = 634          # el split existente: 5.702 train + 634 validation

# Identicas a 03_SCRIPTS/modelamiento_temporal.py
NUM = ["Rooms", "Distance", "Bedroom2", "Bathroom", "Car", "Landsize",
       "Lattitude", "Longtitude", "Propertycount"]
CAT_A = ["Type", "Method", "Regionname"]
CAT_B = ["Type", "Method", "Regionname", "CouncilArea"]


def cargar():
    df = pd.read_csv(CSV)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df["Year"] = df["Date"].dt.year
    return df


def preproc(cats):
    """Mismo preprocesamiento del modelo actual.

    Las categoricas ya usan imputacion por constante 'missing': los faltantes
    de CouncilArea entran como categoria explicita MISSING, no se inventan ni
    se imputan por moda. OneHotEncoder(handle_unknown='ignore') absorbe ademas
    cualquier categoria que aparezca solo en 2017.
    """
    return ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median", add_indicator=True))]), NUM),
        ("cat", Pipeline([
            ("imp", SimpleImputer(strategy="constant", fill_value="missing")),
            ("oh", OneHotEncoder(handle_unknown="ignore")),
        ]), cats),
    ])


def modelo(seed):
    return HistGradientBoostingRegressor(
        max_iter=500, learning_rate=0.05, max_leaf_nodes=31,
        l2_regularization=1.0, random_state=seed,
    )


def pipe(cats, seed):
    return Pipeline([("prep", preproc(cats)), ("reg", modelo(seed))])


def evaluar(p, Xtr, ytr, Xva, yva):
    """Entrena sobre log1p(Price) y mide en AUD originales."""
    p.fit(Xtr, np.log1p(ytr))
    pred = np.expm1(p.predict(Xva))
    return dict(
        MAE=float(mean_absolute_error(yva, pred)),
        RMSE=float(np.sqrt(mean_squared_error(yva, pred))),
        R2=float(r2_score(yva, pred)),
    )


# ---------------------------------------------------------------- fase 4
def analisis_faltantes(df):
    a, b = df[df.Year == 2016], df[df.Year == 2017]
    out = {
        "n_2016": int(len(a)),
        "n_2017": int(len(b)),
        "faltantes_2016": int(a.CouncilArea.isna().sum()),
        "faltantes_2017": int(b.CouncilArea.isna().sum()),
        "pct_2016": round(float(a.CouncilArea.isna().mean() * 100), 2),
        "pct_2017": round(float(b.CouncilArea.isna().mean() * 100), 2),
        "categorias_2016": int(a.CouncilArea.nunique()),
        "categorias_2017": int(b.CouncilArea.nunique()),
        "categorias_solo_en_2017": sorted(
            set(b.CouncilArea.dropna()) - set(a.CouncilArea.dropna())
        ),
    }
    out["cambia_patron_temporal"] = bool(abs(out["pct_2017"] - out["pct_2016"]) > 5)

    # Se puede recuperar CouncilArea desde otra columna existente?
    # Suburb -> CouncilArea deberia ser casi funcional (un suburbio pertenece a
    # un municipio). Se mide SOLO con 2016: usar 2017 seria mirar el test.
    mapa = (a.dropna(subset=["CouncilArea"])
              .groupby("Suburb")["CouncilArea"]
              .agg(lambda s: s.mode().iat[0] if len(s.mode()) else np.nan))
    consistencia = (a.dropna(subset=["CouncilArea"])
                     .groupby("Suburb")["CouncilArea"]
                     .nunique())
    faltan_2016 = a[a.CouncilArea.isna()]
    out["recuperable_desde_suburb"] = {
        "suburbios_con_council_conocido_en_2016": int(len(mapa)),
        "suburbios_con_council_ambiguo": int((consistencia > 1).sum()),
        "filas_2016_sin_council_cuyo_suburb_si_lo_tiene":
            int(faltan_2016.Suburb.isin(mapa.index).sum()),
        "filas_2016_sin_council_ni_suburb_conocido":
            int((~faltan_2016.Suburb.isin(mapa.index)).sum()),
    }
    return out


# ---------------------------------------------------------------- fase 1
def fase1(df):
    a = df[df.Year == 2016].copy()
    y = a["Price"].values

    idx_tr, idx_va = train_test_split(
        np.arange(len(a)), test_size=N_VALIDATION, random_state=RS, shuffle=True
    )

    res = {"holdout": {}, "cv": {}}

    # --- Holdout fijo 5.702 / 634 -------------------------------------
    for nombre, cats in (("A", CAT_A), ("B", CAT_B)):
        X = a[NUM + cats]
        por_semilla = [
            evaluar(pipe(cats, s), X.iloc[idx_tr], y[idx_tr], X.iloc[idx_va], y[idx_va])
            for s in SEEDS
        ]
        res["holdout"][nombre] = {
            "n_train": int(len(idx_tr)), "n_validation": int(len(idx_va)),
            "por_semilla": por_semilla,
            "media": {m: float(np.mean([d[m] for d in por_semilla])) for m in ("MAE", "RMSE", "R2")},
            "std": {m: float(np.std([d[m] for d in por_semilla])) for m in ("MAE", "RMSE", "R2")},
        }

    # --- CV 5-fold x 5 semillas, PAREADO ------------------------------
    kf = KFold(n_splits=5, shuffle=True, random_state=RS)
    folds = list(kf.split(a))
    medidas = {"A": [], "B": []}
    for nombre, cats in (("A", CAT_A), ("B", CAT_B)):
        X = a[NUM + cats]
        for s in SEEDS:
            for k, (tr, va) in enumerate(folds):
                m = evaluar(pipe(cats, s), X.iloc[tr], y[tr], X.iloc[va], y[va])
                m.update(seed=s, fold=k)
                medidas[nombre].append(m)

    for nombre in ("A", "B"):
        d = medidas[nombre]
        res["cv"][nombre] = {
            "n_medidas": len(d),
            "media": {m: float(np.mean([x[m] for x in d])) for m in ("MAE", "RMSE", "R2")},
            "std": {m: float(np.std([x[m] for x in d])) for m in ("MAE", "RMSE", "R2")},
            "detalle": d,
        }

    # Diferencias pareadas: mismo fold, misma semilla.
    pares = []
    for xa, xb in zip(medidas["A"], medidas["B"]):
        assert xa["seed"] == xb["seed"] and xa["fold"] == xb["fold"]
        pares.append({m: xa[m] - xb[m] for m in ("MAE", "RMSE")} |
                     {"R2": xb["R2"] - xa["R2"], "seed": xa["seed"], "fold": xa["fold"]})
    # Signo: positivo = B mejor (menos error, mas R2)
    res["pareado"] = {
        "n_pares": len(pares),
        "delta_MAE_media": float(np.mean([p["MAE"] for p in pares])),
        "delta_MAE_std": float(np.std([p["MAE"] for p in pares])),
        "delta_RMSE_media": float(np.mean([p["RMSE"] for p in pares])),
        "delta_R2_media": float(np.mean([p["R2"] for p in pares])),
        "veces_B_mejor_MAE": int(sum(p["MAE"] > 0 for p in pares)),
        "pct_MAE": float(np.mean([p["MAE"] for p in pares]) /
                         res["cv"]["A"]["media"]["MAE"] * 100),
    }
    return res


# ---------------------------------------------------------------- fase 3
def fase3(df, config):
    cats = CAT_A if config == "A" else CAT_B
    a, b = df[df.Year == 2016].copy(), df[df.Year == 2017].copy()
    Xtr, ytr = a[NUM + cats], a["Price"].values
    Xte, yte = b[NUM + cats], b["Price"].values

    por_semilla = [evaluar(pipe(cats, s), Xtr, ytr, Xte, yte) for s in SEEDS]
    nuevos_sub = ~b["Suburb"].isin(set(a["Suburb"])).values
    return {
        "config_elegida": config,
        "features_cat": cats,
        "n_train_2016": int(len(a)), "n_test_2017": int(len(b)),
        "pct_test_suburbio_nuevo": round(float(nuevos_sub.mean() * 100), 2),
        "por_semilla": por_semilla,
        "media": {m: float(np.mean([d[m] for d in por_semilla])) for m in ("MAE", "RMSE", "R2")},
        "std": {m: float(np.std([d[m] for d in por_semilla])) for m in ("MAE", "RMSE", "R2")},
        "benchmark_previo": {
            "fuente": "09_RESULTADOS/resultados_temporal.json",
            "modelo": "HistGradientBoosting | log",
            "MAE": 188217.69851223598, "R2": 0.757,
        },
    }


def guardar(clave, payload):
    try:
        with open(OUT, encoding="utf-8") as f:
            doc = json.load(f)
    except FileNotFoundError:
        doc = {"experimento": "CouncilArea: aporta senal?",
               "fecha": date.today().isoformat(),
               "semillas": SEEDS, "random_state": RS,
               "features_num": NUM, "cat_A": CAT_A, "cat_B": CAT_B,
               "modelo": "HistGradientBoostingRegressor(max_iter=500, lr=0.05, "
                         "max_leaf_nodes=31, l2=1.0) sobre log1p(Price)"}
    doc[clave] = payload
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f"\n-> guardado en {OUT} [{clave}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fase", choices=["fase1", "fase3"])
    ap.add_argument("--config", choices=["A", "B"])
    args = ap.parse_args()

    df = cargar()

    if args.fase == "fase1":
        falt = analisis_faltantes(df)
        print("=== FASE 4 · faltantes de CouncilArea ===")
        print(json.dumps(falt, ensure_ascii=False, indent=1))
        guardar("fase4_faltantes", falt)

        print("\n=== FASE 1 · solo 2016 ===")
        r = fase1(df)
        h, c, p = r["holdout"], r["cv"], r["pareado"]
        print(f"\nHoldout {h['A']['n_train']} train / {h['A']['n_validation']} validation "
              f"({len(SEEDS)} semillas)")
        for n in ("A", "B"):
            m, s = h[n]["media"], h[n]["std"]
            print(f"  {n}: MAE {m['MAE']:>10,.0f} (±{s['MAE']:,.0f})   "
                  f"RMSE {m['RMSE']:>10,.0f}   R2 {m['R2']:.4f}")
        print(f"\nCV 5-fold x {len(SEEDS)} semillas = {c['A']['n_medidas']} medidas")
        for n in ("A", "B"):
            m, s = c[n]["media"], c[n]["std"]
            print(f"  {n}: MAE {m['MAE']:>10,.0f} (±{s['MAE']:,.0f})   "
                  f"RMSE {m['RMSE']:>10,.0f}   R2 {m['R2']:.4f}")
        print(f"\nDiferencias pareadas (positivo = B mejor), n={p['n_pares']}")
        print(f"  delta MAE  : {p['delta_MAE_media']:>10,.0f} AUD  "
              f"(±{p['delta_MAE_std']:,.0f})  = {p['pct_MAE']:.2f}%")
        print(f"  delta RMSE : {p['delta_RMSE_media']:>10,.0f} AUD")
        print(f"  delta R2   : {p['delta_R2_media']:>+.5f}")
        print(f"  B gana en  : {p['veces_B_mejor_MAE']}/{p['n_pares']} comparaciones")
        guardar("fase1_solo_2016", r)
        print("\n2017 NO fue tocado en esta fase.")

    else:
        if not args.config:
            sys.exit("fase3 exige --config A|B: la decision se toma antes de mirar 2017.")
        print(f"=== FASE 3 · test temporal 2017, config {args.config} ===")
        r = fase3(df, args.config)
        m, s = r["media"], r["std"]
        print(f"  MAE  {m['MAE']:>10,.0f} (±{s['MAE']:,.0f})")
        print(f"  RMSE {m['RMSE']:>10,.0f}")
        print(f"  R2   {m['R2']:.4f}")
        bm = r["benchmark_previo"]
        print(f"\n  benchmark previo: MAE {bm['MAE']:,.0f}  R2 {bm['R2']}")
        print(f"  diferencia MAE  : {bm['MAE'] - m['MAE']:>+,.0f} AUD")
        guardar("fase3_test_2017", r)


if __name__ == "__main__":
    main()
