# -*- coding: utf-8 -*-
"""
Tubería cruda vs vista imputada de DashAI (dataset 22).

(a) Descriptivo: este archivo. Cero imputación, cero dropna global, cero drop IQR.
(b) Correlación del explorador: anclaje.json → correlacion_dashai (no se recalcula aquí).
(c) Modelo Hito 1: BuildingArea y YearBuilt fuera; split 2016/2017.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd

CSV = Path(
    r"F:\MACI\08_PROYECTO_FCD\Hito1\Corrección"
    r"\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
)
ANCLAJE = Path(r"F:\MACI\08_PROYECTO_FCD\Hito1\anclaje.json")
SHA_ESPERADO = "3e449c3e95088da8a3a6b10331a5703f2c951d0740f317f97ed9baf0db1fd9f8"
SALIDA = Path(r"F:\MACI\09_RESULTADOS\auditoria_dashai_vs_crudo.json")


def sha256(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def cargar_crudo(ruta: Path = CSV) -> pd.DataFrame:
    sha = sha256(ruta)
    if sha != SHA_ESPERADO:
        raise SystemExit(f"INSUMO DISTINTO: {sha}")
    df = pd.read_csv(ruta)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    if df.shape != (13580, 21):
        raise SystemExit(f"Forma inesperada: {df.shape}")
    return df


def iqr_outliers(s: pd.Series) -> dict:
    q1, q3 = float(s.quantile(0.25)), float(s.quantile(0.75))
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    n = int(((s < lo) | (s > hi)).sum())
    return {
        "n": n,
        "q1": q1,
        "q3": q3,
        "lo": lo,
        "hi": hi,
        "mediana": float(s.median()),
        "media": float(s.mean()),
    }


def auditoria_dashai_vs_crudo(df: pd.DataFrame) -> dict:
    nulos = {
        "Car": int(df["Car"].isna().sum()),
        "BuildingArea": int(df["BuildingArea"].isna().sum()),
        "YearBuilt": int(df["YearBuilt"].isna().sum()),
        "CouncilArea": int(df["CouncilArea"].isna().sum()),
    }
    dup_total = int(df.duplicated().sum())
    dup_sin_date = int(df.drop(columns=["Date"]).duplicated().sum())

    ba_crudo = iqr_outliers(df["BuildingArea"].dropna())
    ba_imp = iqr_outliers(df["BuildingArea"].fillna(df["BuildingArea"].median()))
    yb_crudo = iqr_outliers(df["YearBuilt"].dropna())
    yb_imp = iqr_outliers(df["YearBuilt"].fillna(df["YearBuilt"].median()))

    tabla = [
        {
            "indicador": "Filas duplicadas (todas las columnas)",
            "dashai": 19,
            "crudo": dup_total,
            "veredicto": "artefacto" if dup_total == 0 else "real",
            "nota": f"sin Date: {dup_sin_date} (DashAI 19; pandas 18). No borrar. Reventas en anclaje.",
        },
        {
            "indicador": "Valores faltantes",
            "dashai": "0 (informe de calidad)",
            "crudo": nulos,
            "veredicto": "artefacto",
            "nota": "Si DashAI ve 0 nulos, la vista ya está imputada.",
        },
        {
            "indicador": "BuildingArea atípicos IQR",
            "dashai": 5565,
            "crudo": ba_crudo["n"],
            "veredicto": "artefacto",
            "nota": f"imputado-mediana = {ba_imp['n']}; Q1/Q3 crudo {ba_crudo['q1']:.0f}/{ba_crudo['q3']:.0f} vs {ba_imp['q1']:.2f}/{ba_imp['q3']:.2f}",
        },
        {
            "indicador": "YearBuilt atípicos IQR",
            "dashai": 3975,
            "crudo": yb_crudo["n"],
            "veredicto": "artefacto",
            "nota": f"imputado-mediana = {yb_imp['n']}; crudo mediana {yb_crudo['mediana']:.0f} vs imputada {yb_imp['mediana']:.0f}",
        },
        {
            "indicador": "Propertycount alta cardinalidad",
            "dashai": "categórica, 311 niveles",
            "crudo": int(df["Propertycount"].nunique()),
            "veredicto": "no actuar",
            "nota": "Entero (Cantidad_Propiedades). No one-hot. Suburb=314 y Postcode=198 sí son cardinalidad de OHE.",
        },
        {
            "indicador": "log(Price) / recorte IQR Price",
            "dashai": "skew 2.24; 612 atípicos; 'aplica log'",
            "crudo": f"skew {df['Price'].skew():.2f}; IQR n={iqr_outliers(df['Price'])['n']}",
            "veredicto": "real / no actuar",
            "nota": "Asimetría real. No log-target ni borrar cola. RF Hito 1 en Precio original.",
        },
        {
            "indicador": "IQR Rooms / geo",
            "dashai": "Rooms 682; Lat 262; Long 408; Dist 411",
            "crudo": {
                "Rooms": iqr_outliers(df["Rooms"])["n"],
                "Lattitude": iqr_outliers(df["Lattitude"])["n"],
                "Longtitude": iqr_outliers(df["Longtitude"])["n"],
                "Distance": iqr_outliers(df["Distance"])["n"],
            },
            "veredicto": "real / no actuar",
            "nota": "5–10 habitaciones y coordenadas son válidas. No drop.",
        },
        {
            "indicador": "Distance / Price skew (crudo)",
            "dashai": "Distance 1.68; Price 2.24",
            "crudo": {
                "Distance": round(float(df["Distance"].skew()), 2),
                "Price": round(float(df["Price"].skew()), 2),
            },
            "veredicto": "real",
            "nota": "Describir. No transformar el target para 'arreglar' DashAI.",
        },
    ]

    if ba_imp["n"] != 5565 or yb_imp["n"] != 3975:
        raise SystemExit(
            f"No clava el artefacto: BuildingArea imputado {ba_imp['n']} (esp. 5565), "
            f"YearBuilt imputado {yb_imp['n']} (esp. 3975)"
        )
    if ba_crudo["n"] != 353 or yb_crudo["n"] != 6:
        raise SystemExit(
            f"No clava el crudo: BuildingArea {ba_crudo['n']} (esp. 353), "
            f"YearBuilt {yb_crudo['n']} (esp. 6)"
        )
    if dup_total != 0 or dup_sin_date != 18:
        raise SystemExit(f"Duplicados: total {dup_total} (esp. 0), sin Date {dup_sin_date} (esp. 18)")
    if nulos != {"Car": 62, "BuildingArea": 6450, "YearBuilt": 5375, "CouncilArea": 1369}:
        raise SystemExit(f"Nulos distintos: {nulos}")

    return {
        "sha256": SHA_ESPERADO,
        "n_filas": int(len(df)),
        "nulos_crudo": nulos,
        "duplicados_fila_completa": dup_total,
        "duplicados_sin_Date": dup_sin_date,
        "desfase_dashai_duplicados": "DashAI=19; pandas sin Date=18. No redondear a 19.",
        "buildingarea": {"crudo": ba_crudo, "imputado_mediana": ba_imp},
        "yearbuilt": {"crudo": yb_crudo, "imputado_mediana": yb_imp},
        "tabla": tabla,
    }


if __name__ == "__main__":
    df = cargar_crudo()
    out = auditoria_dashai_vs_crudo(df)
    SALIDA.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print("AUDITORÍA DASHAI vs CRUDO  n =", out["n_filas"])
    print("duplicados fila completa:", out["duplicados_fila_completa"], "| sin Date:", out["duplicados_sin_Date"])
    print("nulos:", out["nulos_crudo"])
    print(
        "BuildingArea IQR crudo/imputado:",
        out["buildingarea"]["crudo"]["n"],
        "/",
        out["buildingarea"]["imputado_mediana"]["n"],
    )
    print(
        "YearBuilt IQR crudo/imputado:",
        out["yearbuilt"]["crudo"]["n"],
        "/",
        out["yearbuilt"]["imputado_mediana"]["n"],
    )
    print()
    print(f"{'indicador':<42} {'dashai':<28} {'crudo':<22} veredicto")
    for row in out["tabla"]:
        crudo = row["crudo"]
        if isinstance(crudo, dict):
            crudo = ", ".join(f"{k}={v}" for k, v in crudo.items())
        print(f"{row['indicador']:<42} {str(row['dashai']):<28} {str(crudo):<22} {row['veredicto']}")
    print("\nGuardado:", SALIDA)
