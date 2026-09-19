# -*- coding: utf-8 -*-
"""
BLOQUE CANÓNICO DE CORRELACIÓN — réplica del CorrelationMatrixExplorer de DashAI (dataset 22).

Calidad / nulos / IQR: ver auditoria_dashai_vs_crudo.py (CSV crudo, sin imputar).
Este archivo solo replica el heatmap del explorador; no es la tubería de calidad ni del modelo.

(a) HALLAZGO DESCRIPTIVO (Pearson, DashAI):
    - Solo las 8 columnas que DashAI tipó numéricas: BuildingArea, Distance, Landsize,
      Lattitude, Longtitude, Price, Rooms, YearBuilt.  (Lattitude/Longtitude: nombres del CSV, no se corrigen.)
    - NO entran (DashAI las tipó Categorical/Text): Bathroom, Bedroom2, Car, Propertycount, Postcode,
      Suburb, Type, Method, Regionname, CouncilArea, Date, Address, SellerG.
    - Todas las 13.580 filas; sin escalar; sin one-hot; sin train_test_split.
    - Manejo de nulos: el backend de DashAI está compilado. Verificado empíricamente contra la matriz
      del explorador: Pearson "pairwise" puro NO la reproduce (falla en las 6 celdas que tocan
      BuildingArea/YearBuilt); sí la reproduce (±0,0005) Pearson sobre todas las filas con los nulos de
      BuildingArea y YearBuilt sustituidos por la MEDIA SIN OUTLIERS de la columna (cercas de Tukey
      Q1-1.5·IQR / Q3+1.5·IQR, las mismas que DashAI guarda en numeric_stats.lower_bound/upper_bound).
      Cualquier constante en BuildingArea∈[110,132] y YearBuilt∈[1963,5;1965,5] da la misma matriz a 3 decimales.
      Este bloque se AUTOVERIFICA contra las 15 celdas de aceptación y aborta si no calza.
    - Umbral "fuerte" de DashAI: |r| > 0,5. Ninguna celda fuera de la diagonal lo cumple.

(b) DECISIÓN DE MODELO (Hito 1, no se mezcla con (a)):
    - Modelo: Random Forest. Split temporal: train 2016 / test 2017 (no se cambia).
    - Fuera del modelo: BuildingArea (47,5 % nulos) y YearBuilt (39,6 % nulos) — por NULOS, no por r≈0
      (YearBuilt–Price = −0,262 es la 2.ª |r| con Precio); CouncilArea (nulos + niveles nuevos);
      Barrio one-hot (172 barrios nuevos en 2017).
    - Entran: Distancia, Latitud, Longitud, Habitaciones (+ Tipo/Región categóricas, no van en Pearson).
"""
import json, sys
import numpy as np, pandas as pd

CSV = r"F:\MACI\02_PROYECTO_FCD\Hito1\Corrección\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
COLS_DASHAI = ["BuildingArea", "Distance", "Landsize", "Lattitude", "Longtitude", "Price", "Rooms", "YearBuilt"]
FUERA_PEARSON = ["Bathroom", "Bedroom2", "Car", "Propertycount", "Postcode", "Suburb", "Type", "Method",
                 "Regionname", "CouncilArea", "Date", "Address", "SellerG"]
UMBRAL_FUERTE = 0.5
# Matriz de aceptación (explorador DashAI, dataset 22) — 3 decimales
ACEPTACION = {("Price", "Rooms"): 0.497, ("Price", "YearBuilt"): -0.262, ("Price", "Lattitude"): -0.213,
              ("Price", "Longtitude"): 0.204, ("Price", "Distance"): -0.163, ("Price", "BuildingArea"): 0.070,
              ("Price", "Landsize"): 0.037, ("Lattitude", "Longtitude"): -0.358, ("Rooms", "Distance"): 0.294,
              ("Distance", "Longtitude"): 0.239, ("Distance", "YearBuilt"): 0.193, ("BuildingArea", "Landsize"): 0.094,
              ("BuildingArea", "Rooms"): 0.093, ("Landsize", "Distance"): 0.025, ("YearBuilt", "Rooms"): -0.052}


def r3(x) -> float:
    """3 decimales redondeados (así muestra DashAI: 0.4966->0.497, -0.2129->-0.213). Única celda en frontera:
    Price–Landsize = 0.03750745 (float64 -> 0.038; DashAI muestra 0.037 y su splits.json guarda 0.0375). Se documenta, no se fuerza."""
    return round(float(x), 3)


def relleno_media_sin_outliers(s: pd.Series) -> float:
    q1, q3 = s.quantile(0.25), s.quantile(0.75); iqr = q3 - q1
    return float(s[(s >= q1 - 1.5 * iqr) & (s <= q3 + 1.5 * iqr)].mean())


def matriz_dashai(df: pd.DataFrame, cols=COLS_DASHAI):
    """Pearson estilo explorador DashAI sobre las columnas numéricas de DashAI. Devuelve (matriz, rellenos)."""
    d = df[cols].apply(pd.to_numeric, errors="coerce")
    rellenos = {}
    for c in cols:
        if d[c].isna().any():
            rellenos[c] = relleno_media_sin_outliers(d[c]); d[c] = d[c].fillna(rellenos[c])
    return d.corr(method="pearson"), rellenos


def verificar(m, tol=0.0006):
    desv = {f"{a}-{b}": round(float(m.loc[a, b] - v), 4) for (a, b), v in ACEPTACION.items() if abs(m.loc[a, b] - v) > tol}
    if desv:
        sys.exit(f"NO REPRODUCE LA MATRIZ DASHAI (tolerancia {tol}): {desv}")
    return True


if __name__ == "__main__":
    df = pd.read_csv(CSV)
    assert df.shape == (13580, 21), df.shape
    m, rellenos = matriz_dashai(df)
    verificar(m)
    ranking = m["Price"].drop("Price").reindex(m["Price"].drop("Price").abs().sort_values(ascending=False).index)
    fuertes = [(a, b, round(float(m.loc[a, b]), 3)) for i, a in enumerate(m.columns) for b in m.columns[i + 1:] if abs(m.loc[a, b]) > UMBRAL_FUERTE]

    print("MATRIZ PEARSON — método explorador DashAI (dataset 22), 8 columnas numéricas, n =", len(df))
    print(m.round(3).to_string())
    print("Nota: Price–Landsize = %.8f está en frontera de redondeo (DashAI muestra 0.037; float64 redondea a 0.038)." % m.loc["Price", "Landsize"])
    print(f"\nRellenos aplicados a nulos (media sin outliers, cercas de Tukey): { {k: round(v, 2) for k, v in rellenos.items()} }")
    print("\nRANKING |r| vs Price:")
    for k, v in ranking.items():
        print(f"  {k:13s} {r3(v):+.3f}")
    print(f"\nCeldas con |r| > {UMBRAL_FUERTE} fuera de la diagonal: {fuertes if fuertes else 'ninguna'}  "
          f"(la mayor es Price–Rooms = {m.loc['Price', 'Rooms']:.3f})")
    print("Fuera del heatmap (DashAI no las tipó numéricas):", ", ".join(FUERA_PEARSON))
    print("Autoverificación contra las 15 celdas de aceptación: OK")

    salida = {"metodo": "pearson; 8 columnas numericas DashAI; todas las filas; nulos BuildingArea/YearBuilt -> media sin outliers (Tukey)",
              "n_filas": int(len(df)), "columnas": COLS_DASHAI, "fuera_del_heatmap": FUERA_PEARSON,
              "rellenos_nulos": {k: round(v, 4) for k, v in rellenos.items()},
              "presentacion": "3 decimales redondeados (como DashAI). Celda en frontera: Price-Landsize=0.03750745 (DashAI muestra 0.037; splits.json de DashAI guarda 0.0375). 'matriz_6dec' conserva el valor completo",
              "matriz": {a: {b: r3(m.loc[a, b]) for b in m.columns} for a in m.index},
              "matriz_6dec": {a: {b: round(float(m.loc[a, b]), 6) for b in m.columns} for a in m.index},
              "ranking_abs_r_vs_Price": [{"variable": k, "r": r3(v)} for k, v in ranking.items()],
              "umbral_fuerte": UMBRAL_FUERTE, "pares_fuertes": fuertes, "verificado_contra_dashai": True}
    json.dump(salida, open(r"F:\MACI\05_RESULTADOS\correlacion_dashai.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print("\nGuardado: F:\\MACI\\05_RESULTADOS\\correlacion_dashai.json")
