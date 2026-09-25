"""
Genera el dataset SINTETICO de la prueba de transferencia de Datito.

Dominio: logistica de ultima milla. Predecir las horas que tarda una entrega.
Nada que ver con precios de vivienda: el objetivo es comprobar si Cristobal
transfiere el razonamiento sobre train/validation/test a un problema nuevo.

DATOS SINTETICOS. No son reales. El proceso generador queda documentado aqui
para que el experimento sea auditable despues de que el alumno responda.

Semilla fija: reproducible.
"""
import numpy as np
import pandas as pd

RNG = np.random.default_rng(20260918)
OUT = r"F:\MACI\07_DATITO\transferencia"

COMUNAS_2024 = ["Concepcion", "Talcahuano", "San Pedro de la Paz", "Chiguayante",
                "Hualpen", "Penco", "Coronel", "Lota", "Tome", "Hualqui",
                "Santa Juana", "Florida"]
COMUNAS_NUEVAS_2025 = ["Arauco", "Curanilahue", "Lebu", "Los Angeles",
                       "Nacimiento", "Cabrero", "Yumbel", "Laja"]

VEHICULOS = ["moto", "furgon", "camion_ligero"]
VEL = {"moto": 38.0, "furgon": 30.0, "camion_ligero": 24.0}


def generar(n, comunas, anio, pct_gps_faltante):
    com = RNG.choice(comunas, size=n)
    veh = RNG.choice(VEHICULOS, size=n, p=[0.35, 0.45, 0.20])

    # Distancia: las comunas nuevas de 2025 estan mas lejos del centro de
    # distribucion. Esto es lo que hace que 2025 sea un problema mas duro.
    base = np.array([18.0 if c in COMUNAS_2024 else 62.0 for c in com])
    distancia = np.clip(RNG.normal(base, base * 0.35), 2, None)

    peso = np.clip(RNG.gamma(2.2, 9.0, n), 0.5, None)
    n_paq = RNG.integers(1, 9, n)
    hora_salida = RNG.integers(6, 20, n)

    # Congestion: salir en hora punta penaliza.
    congestion = np.where(np.isin(hora_salida, [7, 8, 9, 17, 18, 19]), 1.35, 1.0)

    # Calidad de ruta del GPS: senal real, reduce el tiempo cuando es alta.
    score_gps = np.clip(RNG.normal(0.62, 0.17, n), 0, 1)

    velocidad = np.array([VEL[v] for v in veh])
    horas = (distancia / velocidad) * congestion
    horas += 0.045 * n_paq + 0.0035 * peso
    horas *= (1.25 - 0.40 * score_gps)          # el GPS aporta senal de verdad
    horas += RNG.normal(0, 0.16, n)
    horas = np.clip(horas, 0.15, None)

    # Costo de combustible: se registra AL CIERRE de la entrega, por lo que
    # depende del tiempo efectivamente empleado.
    costo_combustible = horas * RNG.normal(4200, 260, n) + RNG.normal(0, 600, n)

    df = pd.DataFrame({
        "id_entrega": [f"{anio}-{i:05d}" for i in range(n)],
        "fecha": pd.to_datetime(f"{anio}-01-01") + pd.to_timedelta(RNG.integers(0, 365, n), "D"),
        "comuna_destino": com,
        "tipo_vehiculo": veh,
        "distancia_km": distancia.round(2),
        "peso_kg": peso.round(2),
        "n_paquetes": n_paq,
        "hora_salida": hora_salida,
        "score_gps_ruta": score_gps.round(4),
        "costo_combustible_clp": costo_combustible.round(0),
        "horas_entrega": horas.round(3),
    })

    # El sensor de ruta se reconfiguro: en 2025 parte de la flota dejo de
    # reportarlo. El faltante NO es aleatorio, se concentra en las comunas
    # incorporadas ese anio.
    if pct_gps_faltante > 0:
        lejano = ~df.comuna_destino.isin(COMUNAS_2024)
        p = np.where(lejano, 0.72, 0.16)
        df.loc[RNG.random(len(df)) < p, "score_gps_ruta"] = np.nan

    return df.sort_values("fecha").reset_index(drop=True)


if __name__ == "__main__":
    d24 = generar(1200, COMUNAS_2024, 2024, 0.0)
    d25 = generar(1400, COMUNAS_2024 + COMUNAS_NUEVAS_2025, 2025, 0.4)
    d24.to_csv(f"{OUT}/entregas_2024.csv", index=False, encoding="utf-8")
    d25.to_csv(f"{OUT}/entregas_2025.csv", index=False, encoding="utf-8")

    for n, d in (("2024", d24), ("2025", d25)):
        print(f"{n}: {len(d)} filas | comunas {d.comuna_destino.nunique()} | "
              f"gps faltante {d.score_gps_ruta.isna().mean()*100:.1f}% | "
              f"horas media {d.horas_entrega.mean():.2f}")
    nuevas = set(d25.comuna_destino) - set(d24.comuna_destino)
    print("comunas nuevas en 2025:", len(nuevas))
