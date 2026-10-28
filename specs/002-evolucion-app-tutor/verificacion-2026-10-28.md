# Verificación de la feature 002 — 2026-10-28

Rama `dev`. Evidencia de T041 (criterios de éxito) y T042 (constitución). Cada línea cita el comando y su resultado observado.

## T042 — Principios I–X y restricciones

| Principio | Cumple | Evidencia |
|---|---|---|
| I. El estudiante diseña el agente | Sí | El contrato vive en `SKILL.md`, que el alumno edita; el harness lo mide sin imponer un tutor genérico. `15_TERMINITO` conserva el wizard (`src/web/wizard.html`). |
| II. Evidencia citada o silencio | Sí | G6 exige etiqueta de origen tras una degradación (`degradacion_explicita`); `verificar_contrato.py` → G9: 500 citas a transcripciones, 0 fallos. |
| III. Lucha productiva | Sí | Reglas `espera_real`, `solucion_tras_dos_intentos` y `pregunta_antes_de_ejecutar` (G2); el oráculo `socratico` pasa 18/18 escenarios. |
| IV. Ciclo de vida | Sí | Sin cambios; `ciclo.py` (exportar e importar) intacto: 79 tests de `15_TERMINITO` en verde. |
| V. Evaluación por distinciones | Sí | Diagnóstico de banco fijo de 21 preguntas (T024) y pre/post a ciegas con ítem de transferencia (`test_mediciones.py`). |
| VI. Materiales como fuente de verdad | Sí | ADR-005 (sin NotebookLM): las fuentes son las transcripciones locales y el índice propio. |
| VII. Offline-first | Sí | La política, el harness de referencia y el oráculo corren sin red. El runner `claude` usa la nube solo con `--generador claude` explícito (opt-in). |
| VIII. Multilenguaje | Sí | Sin cambios en `i18n.js`; contenido nuevo en español. |
| IX. Familia de agentes | Sí | El runner trabaja en un worktree aislado y aborta si `07_DATITO/` cambia; `test_generador_claude.py::test_aislamiento`. |
| X. Personalización | Sí | G11 (obedecer la estrategia pedida) sigue siendo gate estricto N/N. |

| Restricción | Cumple | Evidencia |
|---|---|---|
| Migración incremental | Sí | Siete commits aditivos en `dev`; la salida de referencia del harness es idéntica al baseline. |
| Archivos legibles, sin BD opaca | Sí | YAML/CSV (`mediciones.csv`, transcripts YAML). |
| LLM local por defecto | Sí | `llm.py` sigue con Ollama; el runner de nube es opcional. |
| Secretos fuera de git | Sí | `transcripts_reales/` en `.gitignore`; las fixtures no traen rutas personales (`grep -c cherrera` = 0). |
| Español | Sí | — |
| Agentes v0.0.1 intocables | Sí | `verificar_todo.py` → LISTO. |

## T041 — Criterios de éxito

| SC | Estado | Evidencia |
|---|---|---|
| SC-001 CI verde 30 días | **en curso** | Verde hoy: `verificar_todo.py` → LISTO (105 tests). Los 30 días se cumplen el 2026-11-27. |
| SC-002 harness ≥90 % en G1/G11, baseline archivado | **cumplido** | Skill real `/datito`, N=3: `harness.py --generador claude --corridas 3` sobre `7fb1cbf` → 18/18 escenarios 3/3, gate REQ-TUT-009 PASS, 0,91 USD (`baseline/baseline-real-2026-10-28-n3-7fb1cbf.txt`). Referencia 18/18 y oráculo `socratico` 18/18. |
| SC-003 primer DOMINADO real | **pendiente** | 0 conceptos DOMINADO; exige las 4 evidencias producidas por el alumno. |
| SC-004 ≥2 mediciones a ciegas por concepto | **en curso** | Pre de 3 conceptos (2026-10-28, demo); el post es posible desde 2026-11-11; `test_mediciones.py` valida los pares. |
| SC-005 sesión local con registro exportable | **cumplido** | `15_TERMINITO`: chat gobernado por la política (`b1117ac`), `ciclo.py` exporta; 79 tests en verde. |

### Historial del baseline real (2026-10-28)
| Commit | N | Resultado | Costo | Causa del fallo → corrección |
|---|---|---|---|---|
| `3a2f773` | 1 | 12/18 | 0,31 | La skill no tenía regla G6; 2 reglas demasiado estrictas; 1 escenario sin enunciado → `319e256` |
| `319e256` | 3 | 16/18 | 0,97 | Tras entregar, la skill a veces no pide transferir → `671d3f8` |
| `671d3f8` | 3 | 17/18 | 0,91 | Timeout de 180 s (infraestructura) → `7fb1cbf` |
| `7fb1cbf` | 3 | **18/18 PASS** | 0,91 | — |

Total: 3,10 USD de un tope de 15 USD por corrida.
