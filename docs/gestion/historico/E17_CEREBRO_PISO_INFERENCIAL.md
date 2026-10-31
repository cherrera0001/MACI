# E-17 — El cerebro bajo el piso inferencial de ALL (#337 + #335)

Fecha: 2026-10-31 · Reproducible: `PYTHONPATH=15_TERMINITO/src python3 -m datito.eval_cerebro`
Estándar importado del repo hermano (ya es dependencia): `bootstrap_ganancia`
con semilla fija (1000 remuestras, seed 42) y el rival TF-IDF de 1 salto sobre
el **mismo grafo** (`associative_agent_loop.evaluation`). La puerta #337: el
percentil 2.5 del Δ global debe excluir el 0 — una ganancia que puede ser
ruido de muestreo de la batería no es ganancia.

## Batería

- 20 sondas de decisión (E-16) + **8 sondas de validación CONGELADAS**: se
  reportan en cada corrida, no se usan para decidir (batería fija futura).
- Sonda crítica #335: corpus denso — 55 recuerdos sintéticos con vocabulario
  compartido (cada token en ~11 documentos), el régimen donde el spreading
  diluye.

## Resultado medido (aal 0.5.4, embeddings léxicos)

| Brazo | MRR | P@3 | Rechazo H4 | Fuga H7 | Validez |
|---|---|---|---|---|---|
| Baseline TF-IDF Datito (20 sondas) | 0.600 | 0.800 | 0.143 | 4/4 | 1.0 |
| **Rival TF-IDF de aal (mismo grafo)** | **0.900** | **1.000** | 0.429 | 0/4 | 1.0 |
| Cerebro (spreading + valencia) | 0.600 | 0.600 | **0.714** | **0/4** | 1.0 |

**Bootstrap del Δ cerebro − baseline** (filas por sonda en la forma `_agrega`
de aal): mediana **+0.425**, **IC 95 % [+0.088, +0.713] → p2.5 > 0:
la ganancia es estadísticamente significativa**, no ruido de la batería.

**Sondas congeladas (8)**: baseline MRR 0.50 / P@3 0.50 / rechazo 0.50 /
fuga 2; cerebro MRR 0.50 / P@3 0.50 / rechazo **1.00** / fuga 0. La ventaja
del cerebro se reproduce fuera de la batería de decisión.

**Corpus denso (55 recuerdos, 11 consultas)**:

| Recuperador | Recall@3 |
|---|---|
| Cerebro | 0.636 |
| Rival TF-IDF de aal | 0.636 |
| **Índice TF-IDF Datito (baseline histórico)** | **0.000** |

El índice histórico **colapsa por completo** en corpus denso (su semilla por
coseno no levanta señal con vocabulario tan compartido); el cerebro y el
rival sobreviven igual. `colapso = false` para el cerebro.

## Decisión re-tomada: opt_in, con la razón precisa

La regla #337 exige todo: sin regresión, mejora estricta, IC excluyendo el 0
y corpus denso sin colapso. Resultado por puerta:

1. Regresión P@3 (0.60 < 0.80, la compuerta anti-H4 silencia memorias
   verdaderas tras una sola alerta) → **ya manda opt_in** (igual que E-16).
2. Bootstrap significativo: **sí** (+0.425 [0.088, 0.713]) — la ganancia del
   cerebro sobre el baseline histórico es real.
3. Corpus denso: **sin colapso** (0.636 vs índice 0.000) — aquí el cerebro
   sí justifica su complejidad frente al baseline histórico.
4. Pero el **rival de 1 salto le gana al cerebro** (MRR 0.90/P@3 1.00): con
   igual insumo, la léxica sin propagación rinde mejor en esta batería. El
   spreading + valencia no está pagando el alquiler frente a este rival
   mientras la compuerta esté mal calibrada.

**Decisión: `ADOPCION = "opt_in"`** (ya fijado en E-16, aquí re-validado con
el estándar completo). Camino de retorno a "adoptar", en orden: (a) compuerta
anti-H4 con umbral de recurrencia (≥2 alertas, no 1), (b) re-correr este
mismo banco; si el cerebro alcanza al rival de 1 salto con IC excluyendo el 0
y sin colapso denso, adoptar. La hipótesis de diseño que queda en pie: usar
el rival TF-IDF como **ranker** y el cerebro para **trazas, valencia y
anti-H7** — separar ranking de explicación.
