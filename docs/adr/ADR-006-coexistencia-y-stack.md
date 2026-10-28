# ADR-006 — La skill y la app coexisten sobre un mismo contrato; el stack se queda

**Fecha:** 2026-10-28 · **Estado:** aceptado · **Decide:** el dueño (único alumno y desarrollador)

## Contexto
- MACI tiene un solo usuario: su creador, que también es el alumno (Clarify 1, respuesta del 2026-10-28).
- Hay dos tutores: la skill `/datito` (Claude Code) y la política de `15_TERMINITO/src/datito/socratico.py` (app local).
- `specs/002` dejó bloqueadas la coexistencia (Clarify 9) y la Opción B multiusuario (Clarify 1, 2, 3, 7, 8).

## Decisión
1. **Coexisten.** La skill es el tutor de uso diario. La política es el motor de la app y el **oráculo determinista** del harness (`--generador socratico`). Ninguna reemplaza a la otra.
2. **Un solo contrato.** Ambas se miden con las mismas reglas de `04_CODIGO/harness_escenarios/harness.py`. `harness.py --comparar socratico,claude` lista dónde divergen. Una divergencia es un defecto de una de las dos, no una diferencia de diseño.
3. **El stack no cambia.** Front en HTML y JS sin framework (`15_TERMINITO/src/web/`). API con `http.server` de la stdlib más MCP por stdio. Motor en Python 3.12. Datos en YAML. LLM local con Ollama.
4. **La Opción B queda descartada** mientras haya un solo usuario. Se reabre con un ADR nuevo si: (a) aparece un segundo alumno real → SQLite y auth; (b) la app debe publicarse → auth y hosting; (c) mediciones de latencia muestran que `ThreadingHTTPServer` no alcanza → FastAPI con el mismo contrato `/api`.

## Consecuencias
- T030 cerrada; T034–T038 quedan fuera de alcance, no bloqueadas.
- Hoy la política diverge del contrato solo en G6: no modela la degradación de fuentes. Es trabajo pendiente del motor, no del contrato.
