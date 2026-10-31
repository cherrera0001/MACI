# E-16 — Banco D-15.3 ampliado (6 → 20 sondas) y re-decisión del cerebro

Fecha: 2026-10-31 · Reproducible: `PYTHONPATH=15_TERMINITO/src python3 -m datito.eval_cerebro`
Contexto: E-15 midió al cerebro (aal) con 6 sondas y decidió **adoptar** como
default en modo compañía. E-16 amplía el banco a 20 sondas y aplica la misma
regla pre-registrada, sin tunear el sistema para ganar.

## Banco de 20 sondas

- **10 objetivo** (recuerdo correcto esperado): rufo, videollamadas, tejer,
  sopaipillas, patio, canto, invierno/Chillán + 3 de paráfrasis.
- **6 señuelos H4**: guía anti-estafa con vocabulario colisionante, guía de
  videollamada, y 3 memorias contradictorias (rufo-gato, videollamadas-lunes,
  lluvia-rencor), dos de ellas **nuevas** y entrenadas con alerta.
- **4 cross-domain H7**: consultas académicas (regresión, matriz de confusión,
  Melbourne, splits) cuyo fid existe en el índice (valida con la evidencia) y
  vive en el grafo con `domain="academico"`: solo el filtro de dominio del
  cerebro puede rechazarlo. La fuga se mide en **ambos** recuperadores.

## Resultado medido

| Métrica | Baseline TF-IDF | Cerebro aal |
|---|---|---|
| MRR (10 objetivo) | 0.6000 | 0.6000 |
| Precisión@3 | **0.8000** | **0.6000** |
| Rechazo de señuelos H4 | 0.1429 | 0.7143 |
| Fuga de dominio H7 | **4 / 4** | **0 / 4** |
| Validación de evidencia | 1.0000 | 1.0000 |
| Historia repetida 12× | — | sin duplicados (nodo nuclear único) |

## La regla manda: ADOPCION pasa a "opt_in"

Con 6 sondas el cerebro no regresaba en nada y mejoraba el rechazo → adoptar.
Con 20 aparece una **regresión real en P@3** (0.60 < 0.80). Diagnóstico por
sonda:

| Sonda perdida | Causa |
|---|---|
| "las videollamadas con sus nietas" | La memoria verdadera fue recuperada durante la alerta de "videollamadas los lunes" y la compuerta anti-H4 (valencia ≤ −0.5) la silenció |
| "aprendió a tejer con su madre" | Co-ocurrió con la alerta "lluvia de Chillán" (menciona Chillán) → misma compuerta |
| "los inviernos de Chillán con lluvia" | Menciona lluvia+Chillán: recuperada en la misma alerta → silenciada |

**Hallazgo de diseño**: la compuerta de bienestar castiga memorias verdaderas
tras **una sola** co-ocurrencia con una alerta. Es demasiado agresiva: en la
vida real bajar el ranking tiene sentido; silenciar para siempre (la arista
no decae con uso) no. Corrección propuesta para una épica futura (no aplicada
aquí para no p-hackear el experimento): exigir ≥2 alertas asociadas, o
amortiguar la compuerta con el recuento de usos exitosos (nuclear ya guarda
`usos`).

## Estado final

- `cerebro.ADOPCION = "opt_in"` en código, con este documento como evidencia.
- El cerebro sigue disponible por curso con `cerebro: aal` (y es la vía que
  usan los evaluadores y los tests E-15/E-16).
- El default del modo compañía vuelve al índice TF-IDF (E-12/E-14), que en el
  banco amplio mantiene MRR 0.60 y P@3 0.80 pero sufre **4/4 fugas H7** y
  rechaza solo 1/7 señuelos: la motivación del cerebro sigue viva, y su
  adopción queda condicionada a corregir la compuerta.
- Si la compuerta se corrige y el banco de 20 sondas gana pareado con
  regresión cero, la regla exige volver a "adoptar" y documentarlo aquí.
