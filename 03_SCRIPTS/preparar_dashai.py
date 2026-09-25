"""
Prepara un dataset 100% numerico para DashAI usando SOLO estadisticas de 2016 (train).
- Orden de filas identico al CSV original (los indices de split se calculan sobre ese orden).
- Imputacion con mediana 2016 + indicador de faltante.
- One-hot de Type/Method/Regionname con categorias vistas en 2016 (nuevas en 2017 -> todo 0).
- Excluye Suburb/Postcode/Address/SellerG/CouncilArea (covariate shift: 29% filas 2017 en suburbios nuevos).
Salidas: housing_dashai_2016_2017.csv, dashai_split_indices.json
"""
import json
import numpy as np, pandas as pd

CSV = r"F:\MACI\02_PROYECTO_FCD\Hito1\Corrección\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
df = pd.read_csv(CSV)
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
year = df["Date"].dt.year
is_tr = (year == 2016).values

# Hito 1: BuildingArea y YearBuilt fuera (nulos, no IQR). Propertycount numérica.
NUM = ["Rooms", "Distance", "Bedroom2", "Bathroom", "Car", "Landsize",
       "Lattitude", "Longtitude", "Propertycount"]
CAT = ["Type", "Method", "Regionname"]

out = pd.DataFrame(index=df.index)
for c in NUM:
    med = df.loc[is_tr, c].median()           # mediana SOLO de 2016
    if df[c].isna().any():
        out[f"{c}_missing"] = df[c].isna().astype(int)
    out[c] = df[c].fillna(med)
for c in CAT:
    cats = sorted(df.loc[is_tr, c].dropna().unique())   # categorias SOLO de 2016
    for k in cats:
        out[f"{c}_{k}".replace(" ", "_").replace("-", "_")] = (df[c] == k).astype(int)
out["Price"] = df["Price"]

out.to_csv(r"F:\MACI\04_DATOS\housing_dashai_2016_2017.csv", index=False)
# DashAI exige validation no vacio: 10% de 2016 como hold-out (nunca de 2017)
rng = np.random.default_rng(42)
idx2016 = np.where(is_tr)[0]; rng.shuffle(idx2016)
n_val = int(round(len(idx2016) * 0.10))
idx = dict(train=sorted(int(i) for i in idx2016[n_val:]), validation=sorted(int(i) for i in idx2016[:n_val]),
           test=[int(i) for i in np.where(~is_tr)[0]])
json.dump(idx, open(r"F:\MACI\05_RESULTADOS\dashai_split_indices.json", "w"))
print("filas", len(out), "columnas", out.shape[1], "| train2016", len(idx["train"]), "val2016", len(idx["validation"]), "test2017", len(idx["test"]))
print("columnas:", list(out.columns))
print("NaN restantes:", int(out.isna().sum().sum()))
