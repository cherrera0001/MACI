# Workflow visual Datito (canónico + learning loop)

## Por qué existe

Se rompió el diseño **dos veces** al generar Certamen 3:

1. **VIZ-FAIL-001** — CDN Chart.js + gradiente púrpura ajeno al sistema Datito  
2. **VIZ-FAIL-002** — “Listo” con details cortos y tabla que no salía de la figura del PDF  

Este workflow hace imposible un KEEP sin pasar por el template y la métrica.

## Piezas

| Pieza | Ruta |
|---|---|
| Template único | `07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html` |
| Espejo | `07_DATITO/visual/_TEMPLATE_CANONICO.html` |
| Skill generación | `.claude/skills/datito-visual/SKILL.md` → `/datito-visual` |
| Skill aprendizaje | `.claude/skills/datito-loop/SKILL.md` → `/datito-loop` |
| Protocolo | `learning_loop/program_loop.md` |
| Lecciones | `learning_loop/agent_lessons.yaml` |
| Log | `learning_loop/results.tsv` |
| Eval | `03_CODIGO/datito_loop_eval.py` |
| Una iteración | `03_CODIGO/datito_loop_once.py` |

## Flujo (obligatorio)

```
/datito-visual  o  pedido de HTML nuevo
        │
        ├─► leer agent_lessons.yaml
        ├─► COPIAR _TEMPLATE_CANONICO.html
        ├─► rellenar contenido (sin tocar :root / sin CDN)
        ├─► python 03_CODIGO/datito_loop_eval.py --path …
        │         │
        │         ├─ keep_eligible=true  → datito_loop_once (KEEP) → listo
        │         └─ false               → DISCARD → /datito-loop repara desde template
        └─► append results.tsv siempre
```

## Comandos

```bash
# Evaluar un visual (exit 1 = discard)
python 03_CODIGO/datito_loop_eval.py --path 07_DATITO/visual/certamen3_p1a_roc_detallado.html

# Loguear decisión
python 03_CODIGO/datito_loop_once.py --path 07_DATITO/visual/foo.html --hypothesis "partir de template v1"

# Tras keep de curso: regenerar nav si aplica
python 03_CODIGO/construir_navegacion.py
```

## Criterio KEEP (todos)

- `<!-- datito:template:v1 -->` presente  
- Cero CDN / Chart.js remoto  
- Cero `#667eea` / `#764ba2`  
- CSS embebido; canvas/SVG local si hay gráfico  
- Si es certamen: Qué pasó (lectura de figura) + pasos + `details.resp` + errores  

## Relación con el alumno

| Loop | Quién aprende | Dónde |
|---|---|---|
| 1 Alumno | Cristóbal | progreso / evidencias |
| 2 Tutor→alumno | explicaciones | errores conceptuales → mejor visual |
| 3 Agente→Datito | el constructor | **este** learning_loop |

El loop 3 no sustituye G1 (esperar al alumno). Corre en fork (`datito-loop` / post-visual).
