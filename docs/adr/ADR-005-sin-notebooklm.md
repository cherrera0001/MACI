# ADR-005: NotebookLM descartado como fuente del tutor

**Estado:** ACEPTADA · **Fecha:** 2026-10-28 · **Origen:** comentarios del dueño en #45 y #46

## Contexto

Desde el inicio, Datito usó un cuaderno de NotebookLM (66+ fuentes) vía un
servidor MCP propio (`notebooklm-py` sobre APIs internas no documentadas).
Costos reales observados:

- Integración frágil por diseño: cookies que caducan «cada pocas semanas»,
  APIs internas que «pueden romperse sin aviso» (lo decía el propio CLAUDE.md).
- Sin integración nativa con el agente: el MCP hacia Claude Code era
  incómodo de operar (experiencia del dueño, #46).
- Servicio de terceros de pago: riesgo de lock-in y costo recurrente (#45).

Mientras tanto, el reemplazo local ya existía y era mejor para el contrato:
las 15/15 sesiones transcritas en `05_CLASES/transcripciones/` con
`mapa_ensenanza.yaml` (rango + hablante + evaluabilidad) y el índice propio
del motor (`15_TERMINITO`, TF-IDF sobre los materiales del curso) cubren la
función «preguntar a las fuentes con cita» sin dependencias externas y
cumpliendo el principio de soberanía de datos (constitución VII).

## Decisión

1. **NotebookLM queda descartado** como fuente del tutor. Se elimina el
   servidor MCP del proyecto (`00_INICIO/.mcp.json` fuera, tools fuera de la
   skill) y toda referencia viva en configuración y contrato apunta aquí.
2. **Fuente de verdad jerárquica** (nueva G5):
   1. Material FCD del repositorio (`01_DOCUMENTACION/`, `06_LABORATORIOS/`,
      `05_CLASES/transcripciones/` con ruta + timestamp).
   2. Proyectos propios (Melbourne, Galaxy Zoo).
   3. Fuentes académicas externas, solo si lo anterior no alcanza.
3. **La consulta a fuentes** se resuelve con el índice local del motor
   (recupera fragmentos con cita `[fid]`) o, en sesiones de Claude Code, con
   lectura directa de las transcripciones (G5 ya lo exigía).
4. Las etiquetas `[FUENTE · NotebookLM: …]` pasan a ser históricas: en
   material nuevo se citan ruta de transcripción/lámina con marca de tiempo.

## Consecuencias

- Las bitácoras y auditorías históricas que citan NotebookLM NO se reescriben
  (son evidencia de su época).
- `03_SCRIPTS/integrar_clase.py` y `transcribir_clases.py` conservan su parte
  local (transcripción/indexación); su función de subida queda sin destino.
- `verificar_todo.py --en-linea` sigue siendo el control de publicación; la
  verificación ya no depende de ningún servicio externo.
- Si en el futuro se evalúa otra herramienta RAG, el criterio es: API
  documentada, ejecución local posible, y cumplimiento de la constitución
  (offline-first, datos del estudiante bajo su control).
