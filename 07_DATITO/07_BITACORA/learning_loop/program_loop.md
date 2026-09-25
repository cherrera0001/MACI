# program_loop.md — Agents Learning Loop (constructor de Datito)
# Inspirado en karpathy/autoresearch: editar un artefacto → métrica fija → keep/discard → log.
# NO entrenar pesos. First-IA / spec-driven / data-driven.

## Antes de CADA corrida
1. Leer este archivo.
2. Leer `agent_lessons.yaml` (failure_patterns primero).
3. Leer la última fila de `results.tsv` si existe.
4. Elegir **una** hipótesis (1 frase) y **un** archivo objetivo.

## Superficies editables (una sola por experimento)
| family   | archivo permitido |
|----------|-------------------|
| visual   | un `*.html` bajo 07_DATITO/**/visual/ partido del `_TEMPLATE_CANONICO.html` |
| curriculum | `clases.yaml` o un concepto en curriculum |
| skill    | un SKILL.md (solo con ADR si toca garantías) |

## Protocolo (no preguntar “¿sigo?”)
1. Hipótesis + target_file
2. Copiar/respetar template v1 si family=visual
3. Editar solo lo necesario
4. Correr: `python 03_CODIGO/datito_loop_eval.py --path <archivo>`
5. Append fila a `results.tsv`
6. Si score mejora vs baseline de la familia → KEEP + lesson keep_patterns
7. Si igual/peor/crash → DISCARD (revertir diff) + failure_patterns
8. Siguiente iteración

## Métrica visual (val_bpb de Datito)
score = media de gates {0|1}:
- template_marker (`<!-- datito:template:v1 -->`)
- anti_cdn (0 http(s) a cdn/jsdelivr/unpkg/fonts.google/chart.js remoto)
- anti_ai_gradient (0 #667eea / #764ba2 / linear-gradient púrpura genérico)
- offline_canvas_ok (si hay gráfico: canvas/SVG local)
- profundidad_min (si es certamen: bloques Qué pasó / Pasos / details / resp)

KEEP solo si score == 1.0 (todos los gates).

## Prohibido
- Inventar CSS nuevo como “mejora”
- Declarar listo sin results.tsv
- Ignorar VIZ-FAIL-001 / VIZ-FAIL-002

## Workflow operativo
Ver `WORKFLOW_VISUAL.md` en esta misma carpeta. Una corrida tipica:

```bash
python 03_CODIGO/datito_loop_once.py --path <html> --hypothesis "..."
```
