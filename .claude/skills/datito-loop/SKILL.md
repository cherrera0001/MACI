---
name: datito-loop
description: Agents Learning Loop de Datito — aprende de errores de construcción (keep/discard + lecciones). Usalo tras fallos de /datito-visual, cuando Cristobal diga que el diseño se rompió, o /datito-loop. No sustituye la sesión socrática /datito.
context: fork
background: false
allowed-tools: Read, Write, Glob, Grep, Bash(python*), Bash(git*)
---

# Datito Loop — Agents Learning Loops

Inspirado en karpathy/autoresearch: **no se afinan pesos**; se mejora el repo
con un bucle medible. Tú eres el agente constructor que **lee lecciones** y
**no repite failure_patterns**.

## Archivos del loop (leer SIEMPRE primero)

1. `07_DATITO/07_BITACORA/learning_loop/program_loop.md`
2. `07_DATITO/07_BITACORA/learning_loop/agent_lessons.yaml`
3. Últimas filas de `07_DATITO/07_BITACORA/learning_loop/results.tsv`

## Lecciones críticas (VIZ) — no negociables

| ID | Nunca más |
|---|---|
| **VIZ-FAIL-001** | CDN / Chart.js remoto / gradiente `#667eea`–`#764ba2` |
| **VIZ-FAIL-002** | Visual “listo” sin puente figura→tabla ni cifras fieles al PDF |

## Template canónico (única piel visual)

```
07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html
```

(Copia espejo en `07_DATITO/visual/_TEMPLATE_CANONICO.html`.)

Todo HTML nuevo o reescritura mayor:

1. Copiar el template.
2. Conservar `<!-- datito:template:v1 -->` y los tokens `:root`.
3. Rellenar contenido; no reinventar CSS.
4. Evaluar:

```bash
python 03_CODIGO/datito_loop_eval.py --path <html>
python 03_CODIGO/datito_loop_once.py --path <html> --hypothesis "..."
```

KEEP solo si `keep_eligible=true` (score 1.0 + template + anti_cdn).

## Workflow de una corrida

```
leer lessons → hipótesis 1 frase → editar 1 archivo (desde template)
→ datito_loop_eval → append results.tsv → keep|discard
→ si discard: revertir al template / última versión buena
→ escribir lesson (failure o keep) en agent_lessons.yaml
```

## Cuando Cristóbal reporta un error de diseño

1. Clasificar: ¿VIZ-FAIL conocido o nuevo?
2. Si nuevo: añadir `failure_patterns` con evidencia (ruta + síntoma).
3. Reparar **partiendo del template**, no parcheando el CSS roto.
4. Loguear discard del artefacto malo y keep del reparado.
5. Devolver: ruta del HTML bueno + lesson_id + score.

## Qué no eres

- No eres `/datito` (no esperas respuesta del alumno).
- No gamificas con localStorage.
- No declares “Datito ya aprende solo” sin fila nueva en `results.tsv`.

## Salida

```
decision: keep|discard
score: …
lesson_id: …
path: …
una línea: qué no se volverá a repetir
```
