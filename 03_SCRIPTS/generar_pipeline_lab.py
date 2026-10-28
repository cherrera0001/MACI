"""
Rellena el explicador del pipeline Melbourne (22_pipeline_melbourne.html, REQ-TUT-020)
con datos reales del proyecto y las cifras esperadas que el JavaScript debe reproducir.

  housing_data.csv (13.580 ventas) -> año de Date -> 2016 train / 2017 test
  limpieza: BuildingArea y YearBuilt fuera (>40 % faltante); Car imputado con la mediana de 2016
  muestra: 1 de cada 2 ventas (orden estable por sha256 de Address|Date) para que la página pese poco
  modelo: regresión lineal por mínimos cuadrados (ecuaciones normales) sobre 6 variables

Python estándar, sin numpy: el mismo álgebra que corre en la página, para que la
paridad sea exacta (04_CODIGO/test_visual_v2.py la compara con node).

USO
  python 03_SCRIPTS/generar_pipeline_lab.py            # escribe
  python 03_SCRIPTS/generar_pipeline_lab.py --revisar  # codigo 1 si el HTML no coincide
"""
import csv
import hashlib
import json
import os
import re
import statistics
import sys
from pathlib import Path

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRUDO = os.path.join(RAIZ, "08_PROYECTO_FCD", "Hito1", "Corrección", "Trabajo N°1 _ FINAL",
                     "1° Trabajo _FUNDAMENTOS", "housing_data.csv")
TEMPORAL = os.path.join(RAIZ, "09_RESULTADOS", "resultados_temporal.json")
PROGRESO = os.path.join(RAIZ, "07_DATITO", "progreso.yaml")
PAGINA = os.path.join(RAIZ, "07_DATITO", "01_CONCEPTOS", "visual", "22_pipeline_melbourne.html")
DATOS = re.compile(r"(/\* datito:pipeline:datos:inicio \*/).*?(/\* datito:pipeline:datos:fin \*/)", re.S)

VARIABLES = ["Rooms", "Distance", "Bathroom", "Car", "Landsize", "es_casa"]
PRESETS = {"A": ["Rooms"], "B": ["Rooms", "Distance"], "C": ["Rooms", "Distance", "Bathroom", "es_casa"],
           "D": VARIABLES}
DEFECTO = {"preset": "C", "k": 5}
CONCEPTOS = ["eda", "limpieza_preparacion", "train_validation_test", "validacion_cruzada", "regresion",
             "overfitting_underfitting", "matriz_confusion", "roc_auc"]


# ---- algebra: identica a <script id="pipeline-modelo"> ---------------------
def resolver(a, b):
    """Gauss con pivoteo parcial sobre copias."""
    n = len(b)
    m = [fila[:] + [b[i]] for i, fila in enumerate(a)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(m[r][c]))
        m[c], m[p] = m[p], m[c]
        for r in range(c + 1, n):
            f = m[r][c] / m[c][c]
            for j in range(c, n + 1):
                m[r][j] -= f * m[c][j]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        s = m[r][n] - sum(m[r][j] * x[j] for j in range(r + 1, n))
        x[r] = s / m[r][r]
    return x


def ajustar(datos, cols, filas):
    p = len(cols) + 1
    xtx = [[0.0] * p for _ in range(p)]
    xty = [0.0] * p
    for i in filas:
        x = [1.0] + [datos[c][i] for c in cols]
        y = datos["Price"][i]
        for a in range(p):
            xty[a] += x[a] * y
            for b in range(p):
                xtx[a][b] += x[a] * x[b]
    return resolver(xtx, xty)


def predecir(beta, datos, cols, i):
    return beta[0] + sum(beta[j + 1] * datos[c][i] for j, c in enumerate(cols))


def mae(beta, datos, cols, filas):
    return sum(abs(predecir(beta, datos, cols, i) - datos["Price"][i]) for i in filas) / len(filas)


def cv(datos, cols, k):
    n = len(datos["Price"])
    folds = []
    for f in range(k):
        val = [i for i in range(n) if i % k == f]
        tr = [i for i in range(n) if i % k != f]
        folds.append(mae(ajustar(datos, cols, tr), datos, cols, val))
    return folds


def auc(scores, etiquetas):
    """Probabilidad de que una positiva puntúe sobre una negativa (empates = 1/2)."""
    orden = sorted(range(len(scores)), key=lambda i: scores[i])
    rangos = [0.0] * len(scores)
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and scores[orden[j + 1]] == scores[orden[i]]:
            j += 1
        for t in range(i, j + 1):
            rangos[orden[t]] = (i + j) / 2 + 1
        i = j + 1
    pos = sum(etiquetas)
    neg = len(etiquetas) - pos
    suma = sum(r for r, e in zip(rangos, etiquetas) if e)
    return (suma - pos * (pos + 1) / 2) / (pos * neg)


def confusion(scores, etiquetas, umbral):
    tp = sum(1 for s, e in zip(scores, etiquetas) if s > umbral and e)
    fp = sum(1 for s, e in zip(scores, etiquetas) if s > umbral and not e)
    fn = sum(1 for s, e in zip(scores, etiquetas) if s <= umbral and e)
    return {"tp": tp, "fp": fp, "fn": fn, "tn": len(scores) - tp - fp - fn}


# ---- datos -----------------------------------------------------------------
def leer():
    with open(CRUDO, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    faltantes = {c: sum(1 for r in filas if not r[c].strip()) for c in ("BuildingArea", "YearBuilt", "Car")}
    por_anio = {"2016": [], "2017": []}
    for r in filas:
        por_anio[r["Date"][-4:]].append(r)
    mediana_car = statistics.median(float(r["Car"]) for r in por_anio["2016"] if r["Car"].strip())
    imputados = {a: sum(1 for r in rs if not r["Car"].strip()) for a, rs in por_anio.items()}

    def columnar(rs):
        rs = sorted(rs, key=lambda r: hashlib.sha256(f"{r['Address']}|{r['Date']}".encode()).hexdigest())[::2]
        d = {c: [] for c in VARIABLES + ["Price"]}
        for r in rs:
            d["Rooms"].append(int(r["Rooms"]))
            d["Distance"].append(round(float(r["Distance"]), 1))
            d["Bathroom"].append(int(float(r["Bathroom"])))
            d["Car"].append(int(float(r["Car"])) if r["Car"].strip() else int(mediana_car))
            d["Landsize"].append(int(float(r["Landsize"])))
            d["es_casa"].append(1 if r["Type"] == "h" else 0)
            d["Price"].append(int(round(float(r["Price"]) / 1000)))  # miles de AUD
        return d

    meta = {"n_crudo": len(filas), "n_2016": len(por_anio["2016"]), "n_2017": len(por_anio["2017"]),
            "faltantes": faltantes, "pct_faltante": {c: round(100 * v / len(filas), 1) for c, v in faltantes.items()},
            "mediana_car_2016": mediana_car, "car_imputados": imputados,
            "mediana_precio_2016": statistics.median(float(r["Price"]) for r in por_anio["2016"]) / 1000}
    return columnar(por_anio["2016"]), columnar(por_anio["2017"]), meta


def esperado(train, test, meta):
    cols = PRESETS[DEFECTO["preset"]]
    folds = cv(train, cols, DEFECTO["k"])
    todas = list(range(len(train["Price"])))
    beta = ajustar(train, cols, todas)
    tst = list(range(len(test["Price"])))
    scores = [predecir(beta, test, cols, i) for i in tst]
    etiq = [1 if p > meta["mediana_precio_2016"] else 0 for p in test["Price"]]
    med = statistics.median(train["Price"])
    return {"preset": DEFECTO["preset"], "k": DEFECTO["k"], "folds": folds, "cv": sum(folds) / len(folds),
            "train": mae(beta, train, cols, todas), "test": mae(beta, test, cols, tst),
            "beta": beta, "auc": auc(scores, etiq),
            "confusion": confusion(scores, etiq, meta["mediana_precio_2016"]),
            "baseline_cv": sum(abs(p - med) for p in train["Price"]) / len(train["Price"])}


def corpus():
    train, test, meta = leer()
    temporal = json.loads(Path(TEMPORAL).read_text(encoding="utf-8"))
    meta["pct_suburbio_nuevo_2017"] = round(temporal["meta"]["pct_test_suburbio_nuevo"], 1)
    meta["proyecto_ridge_cv_mae"] = round(temporal["resultados"]["Ridge (lineal) | raw"]["cv2016_MAE_mean"] / 1000)
    meta["proyecto_baseline_cv_mae"] = round(temporal["resultados"]["Baseline (mediana) | raw"]["cv2016_MAE_mean"] / 1000)
    prog = yaml.safe_load(Path(PROGRESO).read_text(encoding="utf-8"))
    estados = {c["id"]: c["estado"] for c in prog["conceptos"]}
    return {"variables": VARIABLES, "presets": PRESETS, "train": train, "test": test, "meta": meta,
            "progreso": {c: estados.get(c, "NO_ESTUDIADO") for c in CONCEPTOS},
            "esperado": esperado(train, test, meta)}


def renderizar(t):
    datos = json.dumps(corpus(), ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return DATOS.sub(lambda m: m.group(1) + datos + m.group(2), t, count=1)


def main():
    t = Path(PAGINA).read_text(encoding="utf-8")
    if not DATOS.search(t):
        sys.exit("22_pipeline_melbourne.html no tiene los marcadores datito:pipeline:datos")
    nuevo = renderizar(t)
    if "--revisar" in sys.argv:
        sys.exit(0 if nuevo == t else 1)
    if nuevo != t:
        Path(PAGINA).write_text(nuevo, encoding="utf-8")
    e = corpus()["esperado"]
    print(f"22_pipeline_melbourne.html: preset {e['preset']} K={e['k']} · CV MAE {e['cv']:.1f} · "
          f"train {e['train']:.1f} · test {e['test']:.1f} · AUC {e['auc']:.3f} (miles de AUD)")


if __name__ == "__main__":
    main()
