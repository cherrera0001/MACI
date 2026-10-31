# E-15 — Experimento D-15.3: ¿el cerebro (aal) mejora al índice TF-IDF?

Fecha: 2026-10-31 · Épica E-15 (issues #211–#227) · Reproducible:
`PYTHONPATH=15_TERMINITO/src python3 -m datito.eval_cerebro`

## Método

Mismo índice, mismas 6 sondas, dos recuperadores cara a cara:

- **Baseline**: `Indice.buscar_asociativo` (E-12/E-14, memoria actual).
- **Cerebro**: `cerebro.Cerebro.recuperar` sobre grafo aal entrenado con 3
  episodios previos + 12 repeticiones de una historia (recall con trazas,
  valencia contextual, filtro duro de dominio/kind).

Escenarios adversarios heredados del repo hermano Agents_Learning_Loops:
señuelo léxico contradictorio (H4), señuelo de guía anti-estafa (H4),
contaminación cruzada académico↔compañía (H7), historia repetida N veces.

## Resultado medido (aal 0.5.4, embeddings léxicos)

| Métrica | Baseline TF-IDF | Cerebro aal |
|---|---|---|
| MRR (5 sondas con objetivo) | 1.0000 | 1.0000 |
| Precisión@3 | 1.0000 | 1.0000 |
| Rechazo de señuelos (H4) | 0.0000 | **1.0000** |
| Fuga de dominio (H7) | 0 | 0 |
| Validación evidencia | 1.0000 | 1.0000 |
| Historia repetida 12× | — | sin duplicados, Rufo único |

Detalle: el baseline mezcla guías con memorias (devuelve la guía anti-estafa
ante "claves banco teléfono") y no tiene mecanismo para down-rankear el
recuerdo contradictorio ligado a una alerta. El cerebro rechaza ambos
señuelos gracias al filtro de kind y a la compuerta de bienestar
(valencia ≤ −0.5 ⇒ no se evoca de forma proactiva).

## Decisión aplicada (regla D-15.3)

`ADOPCION = "adoptar"` en `src/datito/cerebro.py`:

- Sin regresión en MRR/P@3 y mejora estricta en rechazo de señuelos
  (0.0 → 1.0) ⇒ **default en modo compañía** cuando aal esté instalado.
- Sin aal instalado: degradación limpia (D-15.1); el índice TF-IDF sigue
  siendo la única memoria. Paquete zip, CI y tests base no instalan aal.
- Opt-out por curso: `cerebro: off` en curso.yaml. Opt-in forzado:
  `cerebro: aal`. La preferencia `auto` (default) sigue la adopción.

## Honestidad científica

Si una futura versión del experimento empata sin mejora estricta, o regresa
en cualquiera de las tres métricas ante cambios de aal o del índice, la
regla exige cambiar `ADOPCION` a `"opt_in"` y documentarlo aquí.
La memoria puede empeorar (lecciones H4/H7 del repo hermano): por eso la
adopción se mide con señuelos y nunca por impresión.
