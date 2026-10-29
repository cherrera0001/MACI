"""Escenario vivo de la brecha train-test (H-8.1): la corrida real del caso
del certamen (d1-brecha-r2), ejecutada en el sandbox con marcadores de paso.

La lección «Evidencia viva» (src/web/evidencia-brecha.html) embebe una
captura de referencia y ofrece re-ejecutar esta función con la misma semilla:
los números deben reproducirse exactos (escenario determinista: random.seed).
"""
from __future__ import annotations

from . import sandbox

ESCENARIO = '''
import random
random.seed({semilla})
N = 200
x = [random.uniform(0, 10) for _ in range(N)]
ruido = [random.gauss(0, 0.6) for _ in range(N)]
y = [2.0 * xi + 1.0 + r for xi, r in zip(x, ruido)]

def r2(real, pred):
    media = sum(real) / len(real)
    ss_res = sum((a - b) ** 2 for a, b in zip(real, pred))
    ss_tot = sum((a - media) ** 2 for a in real)
    return 1 - ss_res / ss_tot

def ajustar_lineal(xs, ys):
    n = len(xs)
    xm, ym = sum(xs) / n, sum(ys) / n
    b = sum((xi - xm) * (yi - ym) for xi, yi in zip(xs, ys)) / \\
        sum((xi - xm) ** 2 for xi in xs)
    return ym - b * xm, b

x_tr, x_te = x[:160], x[160:]
y_tr, y_te = y[:160], y[160:]
memoria = dict(zip(x_tr, y_tr))
media_tr = sum(y_tr) / len(y_tr)
predA_tr = [memoria[xi] for xi in x_tr]
predA_te = [memoria.get(xi, media_tr) for xi in x_te]
c0, c1 = ajustar_lineal(x_tr, y_tr)
predB_tr = [c0 + c1 * xi for xi in x_tr]
predB_te = [c0 + c1 * xi for xi in x_te]
constante = sum(y_tr) / len(y_tr)
predC_tr = [constante] * len(x_tr)
predC_te = [constante] * len(x_te)
modelos = {{"A": (r2(y_tr, predA_tr), r2(y_te, predA_te)),
           "B": (r2(y_tr, predB_tr), r2(y_te, predB_te)),
           "C": (r2(y_tr, predC_tr), r2(y_te, predC_te))}}

print("#@paso-1-rendimiento")
for nombre, (r_tr, r_te) in modelos.items():
    print(f"  {{nombre}}: R2 train={{r_tr:.2f}} test={{r_te:.2f}}")
print("#@paso-2-brechas")
for nombre, (r_tr, r_te) in modelos.items():
    print(f"  {{nombre}} brecha={{r_tr - r_te:+.2f}}")
print("#@paso-3-etiquetado")
print("  A sobreajusta (memoriza train, falla test)")
print("  C subajusta (malo en ambos)")
print("  B generaliza (brecha ~0 con buen rendimiento)")
'''


def correr(semilla: int = 42) -> dict:
    """Corre el escenario con la semilla dada y devuelve la traza completa."""
    traza = sandbox.ejecutar(ESCENARIO.format(semilla=semilla), timeout=20)
    return {
        "semilla": semilla,
        "eventos": [e.nombre for e in traza.eventos],
        "salida": traza.salida,
        "codigo_salida": traza.codigo_salida,
        "timeout": traza.timeout,
    }
