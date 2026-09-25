#!/usr/bin/env python3
"""
anclaje.py — Congela el estado numerico del Hito 1.

Lee housing_data.csv desde disco local (sin red), verifica identidad por SHA-256
y emite anclaje.json. Ninguna cifra del deck ni del dossier se escribe a mano:
todas se leen de una clave de este archivo.
"""
import hashlib, json, sys
import numpy as np
import pandas as pd

RUTA = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/uploads/housing_data.csv"
SHA_ESPERADO = "3e449c3e95088da8a3a6b10331a5703f2c951d0740f317f97ed9baf0db1fd9f8"
SEMILLA = 20260810

COLUMNAS = ['Suburb','Address','Rooms','Type','Price','Method','SellerG','Date',
            'Distance','Postcode','Bedroom2','Bathroom','Car','Landsize',
            'BuildingArea','YearBuilt','CouncilArea','Lattitude','Longtitude',
            'Regionname','Propertycount']


def sha256(ruta, bloque=1 << 20):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for chunk in iter(lambda: f.read(bloque), b""):
            h.update(chunk)
    return h.hexdigest()


A = {}

# ── GL1 · PROCEDENCIA ────────────────────────────────────────────────────────
sha_obs = sha256(RUTA)
assert sha_obs == SHA_ESPERADO, f"INSUMO DISTINTO: {sha_obs}"

df = pd.read_csv(RUTA)
idx = [c for c in df.columns if str(c).startswith("Unnamed") or not str(c).strip()]
if idx:
    df = df.drop(columns=idx)

assert df.shape == (13580, 21), f"FORMA: {df.shape}"
assert list(df.columns) == COLUMNAS, "COLUMNAS INESPERADAS"

fecha = pd.to_datetime(df["Date"], dayfirst=True, errors="raise")
A["procedencia"] = {
    "archivo": "housing_data.csv",
    "sha256": sha_obs,
    "bytes": 2091239,
    "filas": int(df.shape[0]),
    "columnas": int(df.shape[1]),
    "columna_indice_arrastrada": idx,
    "fecha_min": fecha.min().strftime("%Y-%m-%d"),
    "fecha_max": fecha.max().strftime("%Y-%m-%d"),
    "duplicados_fila_completa": int(df.duplicated().sum()),
    "snapshot_kagglehub_filas": 18396,
    "semilla": SEMILLA,
}
df["_fecha"] = fecha
df["_anio"] = fecha.dt.year

# L-10 · formato de fecha
dia = df["Date"].str.split("/").str[0].astype(int)
A["L10_fecha"] = {
    "filas_dia_mayor_12": int((dia > 12).sum()),
    "rango_dayfirst": [fecha.min().strftime("%Y-%m-%d"), fecha.max().strftime("%Y-%m-%d")],
}
f_mes = pd.to_datetime(df["Date"], dayfirst=False, errors="coerce")
A["L10_fecha"]["rango_mesprimero"] = [
    f_mes.min().strftime("%Y-%m-%d"), f_mes.max().strftime("%Y-%m-%d")]
A["L10_fecha"]["nat_mesprimero"] = int(f_mes.isna().sum())
cnt_mes = f_mes.dt.year.value_counts().sort_index().to_dict()
A["L10_fecha"]["mezcla_mesprimero"] = {str(int(k)): int(v) for k, v in cnt_mes.items()}

# ── PARTICION TEMPORAL ───────────────────────────────────────────────────────
n16 = int((df["_anio"] == 2016).sum())
n17 = int((df["_anio"] == 2017).sum())
A["particion"] = {
    "n_2016": n16, "n_2017": n17,
    "pct_2016": round(100 * n16 / len(df), 1),
    "pct_2017": round(100 * n17 / len(df), 1),
}
mensual = df.groupby([df["_fecha"].dt.year, df["_fecha"].dt.month]).size()
A["particion"]["mensual"] = {f"{a}-{m:02d}": int(v) for (a, m), v in mensual.items()}
meses_2016 = sorted(m for (a, m) in mensual.index if a == 2016)
meses_2017 = sorted(m for (a, m) in mensual.index if a == 2017)
A["particion"]["meses_presentes_2016"] = meses_2016
A["particion"]["meses_presentes_2017"] = meses_2017
A["particion"]["meses_ausentes_2016"] = [m for m in range(1, 13) if m not in meses_2016]
A["particion"]["meses_ausentes_2017"] = [m for m in range(1, 10) if m not in meses_2017]

# ── AUSENCIAS ────────────────────────────────────────────────────────────────
nulos = df[COLUMNAS].isna().sum()
A["ausencias"] = {
    "por_columna": {k: int(v) for k, v in nulos.items() if v > 0},
    "columnas_completas": int((nulos == 0).sum()),
}
for c in ["Car", "CouncilArea", "YearBuilt", "BuildingArea"]:
    a16 = df.loc[df["_anio"] == 2016, c].isna().mean() * 100
    a17 = df.loc[df["_anio"] == 2017, c].isna().mean() * 100
    A["ausencias"].setdefault("tasa_por_anio", {})[c] = {
        "2016": round(a16, 1), "2017": round(a17, 1),
        "n_2016": int(df.loc[df["_anio"] == 2016, c].isna().sum()),
        "n_2017": int(df.loc[df["_anio"] == 2017, c].isna().sum()),
    }

# Cascada
def fila_cascada(nombre, sub):
    d = df.dropna(subset=sub) if sub else df
    m16 = d.loc[d["_anio"] == 2016, "Price"].median()
    m17 = d.loc[d["_anio"] == 2017, "Price"].median()
    a, b = int((d["_anio"] == 2016).sum()), int((d["_anio"] == 2017).sum())
    return {"politica": nombre, "filas": int(len(d)), "n_2016": a, "n_2017": b,
            "pct_2016": round(100 * a / len(d), 1), "pct_2017": round(100 * b / len(d), 1),
            "mediana_2016": int(m16), "mediana_2017": int(m17)}

geo = ["Price", "Rooms", "Type", "Distance", "Regionname", "Propertycount"]
A["cascada"] = [
    fila_cascada("(0) sin politica", []),
    fila_cascada("(b1) subset geo-estructural", geo),
    fila_cascada("(b2) + Car", geo + ["Car"]),
    fila_cascada("(b3) + CouncilArea", geo + ["Car", "CouncilArea"]),
    fila_cascada("(b4) + YearBuilt", geo + ["Car", "CouncilArea", "YearBuilt"]),
    fila_cascada("(a) global = (b5)", COLUMNAS),
]

# ── IDENTIDAD DE PROPIEDAD (SUPERSEDE de L-03) ───────────────────────────────
def identidad(cols):
    llave = df[cols].astype(str).agg("|".join, axis=1)
    vc = llave.value_counts()
    rep = vc[vc > 1]
    filas_rep = int(rep.sum())
    g = df.assign(_k=llave).groupby("_k")["_anio"].nunique()
    cruzan = g[g > 1]
    filas_cruzan = int(df.assign(_k=llave).loc[llave.isin(cruzan.index)].shape[0])
    dup = df.assign(_k=llave).duplicated(subset=["_k", "Date", "Price"], keep=False)
    return {"llave": "+".join(cols), "propiedades_repetidas": int(len(rep)),
            "filas_repetidas": filas_rep, "propiedades_cruzan_corte": int(len(cruzan)),
            "filas_cruzan_corte": filas_cruzan,
            "filas_duplicado_exacto": int(dup.sum())}

A["identidad"] = {
    "con_Address": identidad(["Address"]),
    "con_Suburb_Address": identidad(["Suburb", "Address"]),
    "con_Suburb_Address_Postcode": identidad(["Suburb", "Address", "Postcode"]),
}
A["identidad"]["sobreconteo_pct_propiedades"] = round(
    100 * (A["identidad"]["con_Address"]["propiedades_repetidas"] /
           A["identidad"]["con_Suburb_Address"]["propiedades_repetidas"] - 1), 0)
A["identidad"]["sobreconteo_pct_cruce"] = round(
    100 * (A["identidad"]["con_Address"]["propiedades_cruzan_corte"] /
           A["identidad"]["con_Suburb_Address"]["propiedades_cruzan_corte"] - 1), 0)

# Reventas que cruzan el corte, con identidad corregida
llave = df[["Suburb", "Address"]].astype(str).agg("|".join, axis=1)
d = df.assign(_k=llave)
g = d.groupby("_k")["_anio"].nunique()
cruzan = set(g[g > 1].index)
sub = d[d["_k"].isin(cruzan)].sort_values(["_k", "_fecha"])
revalor = []
for k, grp in sub.groupby("_k"):
    p = grp["Price"].tolist()
    if len(p) >= 2 and p[0] > 0:
        revalor.append(100 * (p[-1] - p[0]) / p[0])
revalor = np.array(revalor)
A["reventas"] = {
    "propiedades": int(len(cruzan)),
    "filas": int(len(sub)),
    "filas_en_2017": int((sub["_anio"] == 2017).sum()),
    "pct_de_2017": round(100 * (sub["_anio"] == 2017).sum() / n17, 2),
    "revalorizacion_mediana_pct": round(float(np.median(revalor)), 1),
    "revalorizacion_media_pct": round(float(revalor.mean()), 1),
    "revalorizacion_min_pct": round(float(revalor.min()), 0),
    "revalorizacion_max_pct": round(float(revalor.max()), 0),
    "n_2017_depurado": n17 - int((sub["_anio"] == 2017).sum()),
}

# ── COTA TRIVIAL ─────────────────────────────────────────────────────────────
p16 = df.loc[df["_anio"] == 2016, "Price"]
p17 = df.loc[df["_anio"] == 2017, "Price"]
med16, med17 = float(p16.median()), float(p17.median())
mae = lambda y, c: float(np.abs(y - c).mean())
por_type = df[df["_anio"] == 2016].groupby("Type")["Price"].median()
pred_type = df.loc[df["_anio"] == 2017, "Type"].map(por_type)
mae_type = float((p17 - pred_type).abs().mean())

A["cota"] = {
    "mediana_2016": int(med16), "mediana_2017": int(med17),
    "deriva_mediana_pct": round(100 * (med17 - med16) / med16, 2),
    "mae_const2016_sobre2017": round(mae(p17, med16), 0),
    "mae_oraculo2017_sobre2017": round(mae(p17, med17), 0),
    "mae_const2016_sobre2016": round(mae(p16, med16), 0),
    "mae_por_Type_sobre2017": round(mae_type, 0),
    "media_2016": int(p16.mean()), "media_2017": int(p17.mean()),
    "desv_2017": int(p17.std()),
    "price_min": int(df["Price"].min()), "price_max": int(df["Price"].max()),
}
A["cota"]["brecha_oraculo_pesos"] = round(
    A["cota"]["mae_const2016_sobre2017"] - A["cota"]["mae_oraculo2017_sobre2017"], 0)
A["cota"]["brecha_oraculo_pct"] = round(
    100 * A["cota"]["brecha_oraculo_pesos"] / A["cota"]["mae_const2016_sobre2017"], 3)
A["cota"]["mejora_Type_pct"] = round(
    100 * (1 - mae_type / A["cota"]["mae_const2016_sobre2017"]), 1)

# ── NIVELES NO VISTOS (L-04) ─────────────────────────────────────────────────
def no_vistos(col):
    v16 = set(df.loc[df["_anio"] == 2016, col].dropna().unique())
    s17 = df.loc[df["_anio"] == 2017, col]
    nuevas = set(s17.dropna().unique()) - v16
    filas = int(s17.isin(nuevas).sum())
    return {"niveles_2016": len(v16), "niveles_2017": int(s17.nunique()),
            "niveles_nuevos": len(nuevas), "filas_2017_afectadas": filas,
            "pct_2017": round(100 * filas / n17, 1)}

A["no_vistos"] = {c: no_vistos(c) for c in
                  ["Suburb", "SellerG", "CouncilArea", "Postcode", "Regionname", "Type"]}

v16 = set(df.loc[df["_anio"] == 2016, "Suburb"].unique())
m16 = df["_anio"] == 2016
m17 = df["_anio"] == 2017
nuevo = m17 & ~df["Suburb"].isin(v16)
A["no_vistos"]["Suburb"]["mediana_precio_visto"] = int(df.loc[m17 & df["Suburb"].isin(v16), "Price"].median())
A["no_vistos"]["Suburb"]["mediana_precio_nuevo"] = int(df.loc[nuevo, "Price"].median())
A["no_vistos"]["Suburb"]["distancia_mediana_visto"] = round(float(df.loc[m17 & df["Suburb"].isin(v16), "Distance"].median()), 1)
A["no_vistos"]["Suburb"]["distancia_mediana_nuevo"] = round(float(df.loc[nuevo, "Distance"].median()), 1)
A["no_vistos"]["Suburb"]["total_suburbios"] = int(df["Suburb"].nunique())

# ── EFECTO DE COMPOSICION (hallazgo L-12) ───────────────────────────────────
comp = df["Suburb"].isin(v16)
y_comp = df.loc[m17 & comp, "Price"]
A["composicion"] = {
    "mediana_2016": int(df.loc[m16, "Price"].median()),
    "mediana_2017_total": int(df.loc[m17, "Price"].median()),
    "mediana_2017_comparable": int(y_comp.median()),
    "n_2017_comparable": int((m17 & comp).sum()),
    "deriva_agregada_pct": round(100 * (df.loc[m17, "Price"].median() /
                                        df.loc[m16, "Price"].median() - 1), 2),
    "deriva_comparable_pct": round(100 * (y_comp.median() /
                                          df.loc[m16, "Price"].median() - 1), 1),
    "distancia_mediana_2016": float(df.loc[m16, "Distance"].median()),
    "distancia_mediana_2017": float(df.loc[m17, "Distance"].median()),
    "por_tipo": {},
    "mix_tipo": {},
}
for t in ["h", "u", "t"]:
    a = df.loc[m16 & (df["Type"] == t), "Price"].median()
    b = df.loc[m17 & comp & (df["Type"] == t), "Price"].median()
    c = df.loc[m17 & (df["Type"] == t), "Price"].median()
    A["composicion"]["por_tipo"][t] = {
        "mediana_2016": int(a), "mediana_2017_comparable": int(b),
        "mediana_2017_total": int(c),
        "var_comparable_pct": round(100 * (b - a) / a, 1),
        "var_total_pct": round(100 * (c - a) / a, 1)}
for t in ["h", "u", "t"]:
    A["composicion"]["mix_tipo"][t] = {
        "pct_2016": round(100 * (df.loc[m16, "Type"] == t).mean(), 1),
        "pct_2017": round(100 * (df.loc[m17, "Type"] == t).mean(), 1)}

# ── PLAUSIBILIDAD (GL2) ──────────────────────────────────────────────────────
A["plausibilidad"] = {
    "YearBuilt_min": int(df["YearBuilt"].min()),
    "YearBuilt_max": int(df["YearBuilt"].max()),
    "YearBuilt_anteriores_1850": int((df["YearBuilt"] < 1850).sum()),
    "YearBuilt_posteriores_venta": int((df["YearBuilt"] > df["_anio"]).sum()),
    "Landsize_cero": int((df["Landsize"] == 0).sum()),
    "Landsize_cero_pct": round(100 * (df["Landsize"] == 0).mean(), 1),
    "Landsize_max": int(df["Landsize"].max()),
    "BuildingArea_cero": int((df["BuildingArea"] == 0).sum()),
    "BuildingArea_mayor_Landsize": int((df["BuildingArea"] > df["Landsize"]).sum()),
    "Bedroom2_cero": int((df["Bedroom2"] == 0).sum()),
    "Bathroom_cero": int((df["Bathroom"] == 0).sum()),
    "Rooms_distinto_Bedroom2": int((df["Rooms"] != df["Bedroom2"]).sum()),
    "Distance_nulos": int(df["Distance"].isna().sum()),
    "Distance_max": float(df["Distance"].max()),
}

# ── DESCRIPCION DE DATOS ─────────────────────────────────────────────────────
A["datos"] = {
    "tipos": {"h": int((df["Type"] == "h").sum()), "u": int((df["Type"] == "u").sum()),
              "t": int((df["Type"] == "t").sum())},
    "n_suburbios": int(df["Suburb"].nunique()),
    "n_regiones": int(df["Regionname"].nunique()),
    "n_vendedores": int(df["SellerG"].nunique()),
    "n_metodos": int(df["Method"].nunique()),
    "rooms_min": int(df["Rooms"].min()), "rooms_max": int(df["Rooms"].max()),
    "enunciado_declara_atributos": 21,
    "enunciado_enumera_atributos": 15,
}
reg = df.groupby("Regionname").agg(n=("Price", "size"), mediana=("Price", "median"))
reg = reg.sort_values("n", ascending=False)
A["datos"]["por_region"] = [{"region": i, "n": int(r.n), "mediana": int(r.mediana)}
                            for i, r in reg.iterrows()]

# Mediana mensual, para la lamina de deriva
serie = (df.groupby(df["_fecha"].dt.to_period("M"))["Price"]
           .agg(["median", "size"]).reset_index())
A["serie_mensual"] = [{"mes": str(r["_fecha"]), "mediana": int(r["median"]),
                       "n": int(r["size"])} for _, r in serie.iterrows()]

with open("anclaje.json", "w", encoding="utf-8") as f:
    json.dump(A, f, ensure_ascii=False, indent=2)

print("ANCLAJE EMITIDO — anclaje.json")
print(json.dumps({k: (v if not isinstance(v, (list, dict)) else f"<{type(v).__name__}>")
                  for k, v in A.items()}, ensure_ascii=False, indent=2))
