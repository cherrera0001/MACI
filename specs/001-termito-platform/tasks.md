# Tasks: MACI 1.0 — Plataforma Datito

**Input**: Design documents from `/specs/001-datito-platform/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: INCLUIDOS — el spec (Assumptions) y la constitución exigen tests para nueva lógica. Se escriben primero y deben FALLAR antes de la implementación.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Alcance del backlog: SOLO hasta el hito **MVP = un curso real migrado a Datito funcional, evaluándose por distinciones, offline, con ciclo de vida completo** (US1–US4 + fase de migración). US5–US7 quedan fuera de este backlog (post-MVP, ver Notes).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project: `15_TERMINITO/src/datito/`, `15_TERMINITO/tests/` at repository root (estructura fijada en plan.md)
- Una instancia de curso: `15_TERMINITO/cursos/<slug>/` (layout fijado en data-model.md y contracts/formato-curso.md)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Estructura del paquete, dependencias, i18n y CLI esqueleto

- [ ] T001 Create project structure per plan.md: `15_TERMINITO/src/datito/{ingestor,indice,constructor,tutor,evaluador,ciclo_vida,grafo,familia,portabilidad,i18n}` y `15_TERMINITO/tests/`
- [ ] T002 [P] Create `15_TERMINITO/pyproject.toml` with dependencies: fastapi, uvicorn, pydantic, pyyaml, pypdf, python-pptx, trafilatura, fastembed, numpy, openai (SDK compatible Ollama), python-multipart
- [ ] T003 [P] Create i18n string files `15_TERMINITO/src/datito/i18n/es.json` and `en.json` (principio VIII; SC-006) con todas las cadenas de UI y de CLI
- [ ] T004 [P] Create `15_TERMINITO/.env.example` (OLLAMA_HOST, TERMITO_MODELO, TERMITO_PUERTO) and install section in `15_TERMINITO/README.md`
- [ ] T005 Implement CLI skeleton `15_TERMINITO/src/datito/cli.py` with all commands from contracts/cli.md returning "no implementado" and correct exit codes (0/1/2)
- [ ] T006 Smoke test `15_TERMINITO/tests/test_cli.py`: `datito --help` and unknown command exit codes (unittest)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Infraestructura núcleo que bloquea TODAS las historias: rutas, modelo Curso, LLM, índice

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Implement `15_TERMINITO/src/datito/config.py`: all paths derived from `__file__` (RAIZ, DIR_CURSOS, DIR_TESTS); reads `.env` from repo root, never hardcodes machine paths (lección EVALUACION.md C1)
- [ ] T008 [P] Implement `15_TERMINITO/src/datito/curso.py`: create/load `curso.yaml` with fields and validation rules from data-model.md (slug kebab-case único, estados configurando→listo→activo→cerrado)
- [ ] T009 [P] Implement `15_TERMINITO/src/datito/esquemas.py`: YAML validators for grafo.yaml (sin ciclos, ids únicos) and dudas.yaml (toda duda resuelta tiene ≥1 fid existente)
- [ ] T010 Implement `15_TERMINITO/src/datito/tutor/llm.py`: `LLMProvider` interface + Ollama provider (localhost) + `modo_exploracion` fallback when unreachable (research.md R2; contract api.md /api/salud)
- [ ] T011 [P] Implement `15_TERMINITO/src/datito/indice/vector.py`: fastembed embeddings + numpy cosine search + `.indice/manifest.json` + `vectores.npy` (reglas de data-model.md; índice regenerable)
- [ ] T012 [P] Implement `15_TERMINITO/src/datito/indice/fragmentos.py`: fragmentation 150–400 palabras with stable `fid` (`<fuente-id>#<n>`) and direccionable reference (page or timestamp)
- [ ] T013 Implement `15_TERMINITO/src/datito/indice/buscar.py`: top-k retrieval with metadata filter, the only channel through which course content reaches the tutor (research.md R5)
- [ ] T014 [P] Unit tests `15_TERMINITO/tests/test_indice.py`: fragmentation stability, fid format, round-trip index/regenerate
- [ ] T015 [P] Unit tests `15_TERMINITO/tests/test_llm.py`: Ollama provider with mocked HTTP; exploración mode on connection failure
- [ ] T016 [P] Unit tests `15_TERMINITO/tests/test_curso.py`: slug validation, duplicate rejection, state transitions

**Checkpoint**: Foundation ready — reindexar sobre fixture de prueba funciona; `python -m unittest discover -s 15_TERMINITO/tests` en verde

---

## Phase 3: User Story 1 - Construir un Datito desde los materiales reales (Priority: P1) 🎯 MVP

**Goal**: Un estudiante con materiales de un curso real obtiene un Datito funcional en <30 min de trabajo activo (FR-001–FR-006)

**Independent Test**: Escenario 1 de quickstart.md: `datito nuevo` + `ingestar` + `construir` + `prompt ver` produce un curso verificable y un prompt íntegro editable

### Tests for User Story 1

- [ ] T017 [P] [US1] Ingesta tests in `15_TERMINITO/tests/test_ingesta.py`: PDF/PPTX/TXT fixtures → fragmentos con referencia; PDF escaneado → advertencia `estado_extraccion=parcial` (spec escenario 4)
- [ ] T018 [P] [US1] Constructor tests in `15_TERMINITO/tests/test_constructor.py`: 8 componentes completos/incompletos (`completo: bool`, `faltantes`); generación de prompt refleja cada componente (spec escenario 2)
- [ ] T019 [P] [US1] Versioning tests in `15_TERMINITO/tests/test_versionado_prompt.py`: editar componente → nueva versión en `prompt/versions/` con manifest; `revertir` restaura; edición directa marca `prompt_editado_manual: true` (FR-005; research R7)

### Implementation for User Story 1

- [ ] T020 [P] [US1] PDF ingestor in `15_TERMINITO/src/datito/ingestor/pdf.py` (pypdf; page-level references)
- [ ] T021 [P] [US1] PPTX ingestor in `15_TERMINITO/src/datito/ingestor/pptx.py` (python-pptx; slide-level references)
- [ ] T022 [P] [US1] Text/transcription ingestor in `15_TERMINITO/src/datito/ingestor/texto.py` (txt/md/srt/vtt; timestamp references per research R10)
- [ ] T023 [P] [US1] Web ingestor in `15_TERMINITO/src/datito/ingestor/web.py` (trafilatura; URL as source)
- [ ] T024 [US1] Ingestion summary in `15_TERMINITO/src/datito/ingestor/resumen.py`: fuentes procesadas, fragmentos por fuente, advertencias legibles (FR-002)
- [ ] T025 [US1] 8-component wizard in `15_TERMINITO/src/datito/constructor/componentes.py` (interactive CLI + validation API; FR-003)
- [ ] T026 [US1] Prompt generator in `15_TERMINITO/src/datito/constructor/prompt.py` (FR-004; template with slots for the 8 components)
- [ ] T027 [US1] Prompt versioning in `15_TERMINITO/src/datito/constructor/versiones.py` (FR-005; research R7)
- [ ] T028 [US1] Wire CLI commands `nuevo/ingestar/construir/prompt` in `15_TERMINITO/src/datito/cli.py` per contracts/cli.md
- [ ] T029 [US1] API endpoints `POST /api/cursos`, `POST /api/cursos/{slug}/fuentes`, `PUT /api/cursos/{slug}/componentes`, `POST /api/cursos/{slug}/construir` in `15_TERMINITO/src/datito/api.py` per contracts/api.md
- [ ] T030 [US1] Builder UI in `15_TERMINITO/src/web/construir.html` + `15_TERMINITO/src/web/static/app.js` (upload, resumen de ingesta, wizard de 8 pasos, prompt preview editable)

**Checkpoint**: US1 funcional de extremo a extremo; medir y registrar tiempo de trabajo activo del escenario 1 (<30 min, SC-001)

---

## Phase 4: User Story 2 - Conversar con evidencia citada y lucha productiva (Priority: P1) 🎯 MVP

**Goal**: Diálogo persistente donde toda afirmación lleva evidencia y la solución nunca precede al intento (FR-007–FR-011)

**Independent Test**: Escenario 2 de quickstart.md: explicación con evidencia clickeable; "dame la respuesta" sin intento → pista; corrección con evidencia deja duda registrada

### Tests for User Story 2

- [ ] T031 [P] [US2] Grounded generation tests in `15_TERMINITO/tests/test_orquestador.py`: toda afirmación resuelve a fid existente o `sin_fuente: true` (SC-002 invariante, research R5)
- [ ] T032 [P] [US2] State machine tests in `15_TERMINITO/tests/test_lucha_productiva.py`: transiciones pista→esperando_intento→revisión; revelación solo consentida y registrada; 0 soluciones antes del intento (SC-003; research R4)
- [ ] T033 [P] [US2] Memory/dudas tests in `15_TERMINITO/tests/test_dudas.py`: duda resuelta exige evidencia ≥1 fid; sesiones apend-only; reactivación de duda

### Implementation for User Story 2

- [ ] T034 [US2] Grounded orchestrator in `15_TERMINITO/src/datito/tutor/orquestador.py`: generate ONLY from retrieved fragments; verify citation ids before render; plantilla "sin fuente"; marca `fuera_del_curso` (FR-007, FR-011)
- [ ] T035 [US2] Interaction state machine in `15_TERMINITO/src/datito/tutor/estados.py` (FR-008; determinista, no delegada al LLM; research R4)
- [ ] T036 [US2] Duda registry in `15_TERMINITO/src/datito/tutor/dudas.py` (FR-010; data-model rules)
- [ ] T037 [US2] Session memory in `15_TERMINITO/src/datito/tutor/memoria.py` (FR-009; sesiones/<fecha>.md apend-only)
- [ ] T038 [US2] API endpoints `POST /api/cursos/{slug}/mensajes` and `POST .../mensajes/{id}/revelar` in `15_TERMINITO/src/datito/api.py` per contracts/api.md invariants
- [ ] T039 [US2] Chat UI in `15_TERMINITO/src/web/chat.html` with evidence panel (fid, fuente, página/timestamp, click-to-source) and explicit "revelar solución" consent flow
- [ ] T040 [US2] Streaming responses from LLM provider through API (performance goal <10 s first token)

**Checkpoint**: US1+US2 funcionan juntas; escenarios de SC-002/SC-003 verificados contra un curso real

---

## Phase 5: User Story 3 - Ser evaluado por distinciones conceptuales (Priority: P1) 🎯 MVP

**Goal**: Ítems que exigen separar conceptos vecinos, con criterios explícitos y actualización de dominio (FR-012–FR-014)

**Independent Test**: Escenario 3 de quickstart.md: `datito evaluar --tema X` genera solo ítems de distinción y actualiza el dominio en grafo.yaml

### Tests for User Story 3

- [ ] T041 [P] [US3] Item generator tests in `15_TERMINITO/tests/test_items.py`: todo ítem tiene ≥2 conceptos con relación de vecindad del grafo; rechazo si no (principio V)
- [ ] T042 [P] [US3] Grading tests in `15_TERMINITO/tests/test_calificacion.py`: criterios explícitos derivados de fragmentos; resultado actualiza estado de dominio del nodo (FR-014)

### Implementation for User Story 3

- [ ] T043 [US3] Distinction item generator in `15_TERMINITO/src/datito/evaluador/items.py` (FR-012; from grafo + fragmentos via índice)
- [ ] T044 [US3] Grader with explicit criteria in `15_TERMINITO/src/datito/evaluador/calificar.py` (FR-013; feedback nombra la frontera conceptual fallada, patrón 4 de patrones.md)
- [ ] T045 [US3] Domain state updater in `15_TERMINITO/src/datito/grafo/dominio.py` (FR-014; transiciones sin_empezar→en_progreso→dominado y retorno por duda reactivada, per data-model)
- [ ] T046 [US3] API endpoints `POST /api/cursos/{slug}/evaluaciones` and `POST .../evaluaciones/{id}/respuestas` in `15_TERMINITO/src/datito/api.py`
- [ ] T047 [US3] CLI command `evaluar` in `15_TERMINITO/src/datito/cli.py` per contracts/cli.md
- [ ] T048 [US3] Evaluation UI in `15_TERMINITO/src/web/evaluar.html` (ítem → respuesta abierta → feedback con frontera conceptual → actualización visible)

**Checkpoint**: US1–US3 forman el núcleo pedagógico; "evaluándose por distinciones" del hito MVP cumplido

---

## Phase 6: User Story 4 - Ciclo de vida: notas como retroalimentación y cierre (Priority: P1) 🎯 MVP

**Goal**: El Datito evoluciona con notas reales y muere con el curso conservando el registro íntegro (FR-015, FR-016)

**Independent Test**: Escenario 4 de quickstart.md: nota registrada genera ajustes; `cerrar` deja Datito inactivo con dudas.yaml íntegro y consultable

### Tests for User Story 4

- [ ] T049 [P] [US4] Feedback tests in `15_TERMINITO/tests/test_notas.py`: registrar nota produce `ajustes_derivados` visibles y rastreados (FR-015)
- [ ] T050 [P] [US4] Closure tests in `15_TERMINITO/tests/test_cierre.py`: cierre exige confirmación; estado cerrado bloquea conversación; 100% del registro íntegro y consultable (SC-005; FR-016)

### Implementation for User Story 4

- [ ] T051 [US4] Feedback module in `15_TERMINITO/src/datito/ciclo_vida/notas.py` (FR-015; cómo se incorpora al estilo del Datito queda registrado)
- [ ] T052 [US4] Course closure in `15_TERMINITO/src/datito/ciclo_vida/cerrar.py` (FR-016; reversible por período corto, edge case del spec)
- [ ] T053 [US4] API endpoints `POST /api/cursos/{slug}/notas`, `POST .../cerrar`, `GET .../registro` in `15_TERMINITO/src/datito/api.py`
- [ ] T054 [US4] UI for notes + closure in `15_TERMINITO/src/web/ciclo.html` (formulario de nota con vista de ajustes, flujo de cierre con confirmación y acceso al registro)

**Checkpoint**: "ciclo de vida completo" del hito MVP cumplido (nacer→evolucionar→desaparecer conservando)

---

## Phase 7: Migración del curso real v0.0.1 (cierre del hito MVP)

**Goal**: El curso Fundamentos de Ciencia de Datos actual migra como primer Datito real sin regresiones (SC-007; research R6)

**Independent Test**: Escenario 6 de quickstart.md: baseline y post de `verificar_todo.py` sin empeorar; el Datito migrado conversa con evidencia real

- [ ] T055 [P] Legacy adapter in `15_TERMINITO/src/datito/ingestor/legacy_maci.py`: `07_DATITO/clases.yaml`, `grafo.yaml`, bitácoras y transcripciones → instancia `cursos/fundamentos-ciencia-datos/` (research R6; sitio estático intacto)
- [ ] T056 Run migration to `15_TERMINITO/cursos/fundamentos-ciencia-datos/` and review extraction summary for completeness (programa, láminas, evaluaciones, bibliografía)
- [ ] T057 Regression guard: run `python3 03_SCRIPTS/verificar_todo.py` before and after migration; result must not worsen (SC-007; baseline con fallos conocidos documentados en EVALUACION.md C1)
- [ ] T058 MVP validation runbook: execute quickstart.md scenarios 1–5 offline against the migrated course and sign off each SC (SC-001–SC-006 evidence log in `specs/001-datito-platform/evidencias-mvp.md`)

**Checkpoint**: HITO MVP ALCANZADO — un curso real migrado a Datito funcional, evaluándose por distinciones, offline, con ciclo de vida completo

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Calidad transversal previa al cierre del MVP

- [ ] T059 [P] Offline verification: run full test suite and quickstart scenarios with network disabled; document zero outbound calls (SC-004; FR-020) in `15_TERMINITO/README.md`
- [ ] T060 [P] i18n completion: UI and CLI strings 100% from `i18n/es.json` and `en.json`; verify English mode end-to-end (SC-006)
- [ ] T061 [P] Package hygiene: add `15_TERMINITO/` to root `.gitignore` for `.indice/` and `cursos/*/sesiones/` if user decides (data ownership decision documented), update root README with platform section
- [ ] T062 [P] Performance pass: first response <10 s and index rebuild <5 min on modest CPU (plan.md goals); measure and record
- [ ] T063 Final constitution audit: checklist of principles I–X against shipped behavior; record in `specs/001-datito-platform/checklists/constitucion-mvp.md`
- [ ] T064 Run `/speckit-analyze` cross-artifact consistency check and fix any findings

### Refinamientos por validación REA (2026-10-17) — ejecutar en la fase indicada

- [ ] T065 [US2] "Mostrar un paso" en el feedback de error: nuevo `estado_interaccion: "paso_mostrado"` en `15_TERMINITO/src/datito/tutor/estados.py`, pistas graduadas por procedimiento (patrón Khan, khan.md H3), registro de cada revelación. Tests en `15_TERMINITO/tests/test_lucha_productiva.py`: paso N exige N-1 pasos previos; 0 soluciones completas antes del intento. (Fase 4, junto a T035)
- [ ] T066 [US3] Micro-progreso visible en evaluación ("N distinciones de esta sesión" + puntos por ítem) en `15_TERMINITO/src/web/evaluar.html` (patrón Khan "Do 7 problems", khan.md H5). (Fase 5, junto a T045)
- [ ] T067 Contadores de adopción: `metricas` (sesiones, mensajes, evaluaciones_completadas, tiempo_minutos, racha_dias) en `progreso.yaml` + actualización en cada operación, en `15_TERMINITO/src/datito/grafo/dominio.py` (patrón Duolingo/Century sin terceros, sintesis P4). (Fase 2, junto a T007–T009)
- [ ] T068 [US5] Gating del panel de grafo: revelar nodos por dominio con escape "revelar mapa completo" + `tiempo_estimado_min` por unidad en `curso.yaml` (patrón Mathigon, sintesis P5), en `15_TERMINITO/src/datito/grafo/` y la UI del panel. (Fases 7–8)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — T001–T006 inmediatos
- **Foundational (Phase 2)**: Depends on Setup — BLOQUEA todas las historias (T007–T016)
- **User Stories MVP (Phases 3–6)**: Dependen de Foundational; entre sí secuenciales por dependencia funcional real (US2 necesita el prompt de US1; US3 necesita el índice de US1 y la memoria de US2 para adaptar; US4 necesita conversación y evaluación activas)
- **Migración (Phase 7)**: Depends on US1–US4 completos
- **Polish (Phase 8)**: Depends on Phase 7

### User Story Dependencies

- **US1 (P1)**: Foundational only — no dependencies on other stories
- **US2 (P1)**: Foundational + US1 (necesita Datito construido e índice)
- **US3 (P1)**: Foundational + US1 (+ US2 recomendado para adaptación, no bloqueante: la evaluación puede correr por CLI)
- **US4 (P1)**: US1 + US2 (la retroalimentación necesita interacciones que adaptar)

### Within Each User Story

- Tests MUST be written and FAIL before implementation (T017–T019 antes que T020–T030, etc.)
- Ingestores/construcción (T020–T027) antes que wiring CLI/API (T028–T029)
- Core logic (orquestador/estados) antes que endpoints y UI

### Parallel Opportunities

- T002/T003/T004 en paralelo; T008/T009/T011/T012 en paralelo; T014/T015/T016 en paralelo
- Tests de cada historia (T017–T019, T031–T033, T041–T042, T049–T050) en paralelo entre sí
- Ingestores T020–T023 en paralelo; T055 junto a Polish si hay capacidad
- Tras Foundational, US1 puede arrancar mientras se refinan contratos

---

## Parallel Example: User Story 1

```bash
# Tests primero, en paralelo:
Task: "Ingesta tests in 15_TERMINITO/tests/test_ingesta.py"
Task: "Constructor tests in 15_TERMINITO/tests/test_constructor.py"
Task: "Versioning tests in 15_TERMINITO/tests/test_versionado_prompt.py"

# Luego ingestores en paralelo:
Task: "PDF ingestor in 15_TERMINITO/src/datito/ingestor/pdf.py"
Task: "PPTX ingestor in 15_TERMINITO/src/datito/ingestor/pptx.py"
Task: "Text/transcription ingestor in 15_TERMINITO/src/datito/ingestor/texto.py"
Task: "Web ingestor in 15_TERMINITO/src/datito/ingestor/web.py"
```

---

## Implementation Strategy

### MVP First (hito según solicitud del dueño)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL — bloquea todo)
3. Complete Phase 3: US1 → validar escenario 1 (<30 min)
4. Complete Phase 4: US2 → validar SC-002/SC-003
5. Complete Phase 5: US3 → validar evaluación por distinciones
6. Complete Phase 6: US4 → validar ciclo de vida completo
7. Complete Phase 7: migración del curso real + runbook firmado
8. **STOP**: hito MVP alcanzado; US5 (grafo visual), US6 (familia) y US7 (portabilidad) se replanifican como backlog post-MVP

### Incremental Delivery

Cada fase deja el sistema operativo y verificable (restricción constitucional): tras US1
ya existe valor usable (constructor), tras US2 el diálogo, tras US3 la evaluación, tras
US4 el ciclo completo. Ninguna fase reescribe lo anterior.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- US5–US7 (grafo visual, familia, portabilidad) quedan FUERA de este backlog por
  condición explícita del dueño ("solo hasta el hito MVP"); sus specs ya están en
  spec.md y se taskifican en el siguiente ciclo
- Las rutas de todos los archivos usan el patrón derivado de `__file__` (T007); ninguna
  ruta absoluta de máquina se hardcodea (lección de EVALUACION.md C1)
- Verify tests fail before implementing; commit after each task or logical group
