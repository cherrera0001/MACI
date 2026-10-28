# Tasks: Evolución de MACI a aplicación con tutor personalizado

**Input**: Design documents from `/specs/002-evolucion-app-tutor/` (spec.md, plan.md)

**Prerequisites**: spec.md ✔ · plan.md ✔ · research.md / data-model.md / contracts/ — pendientes, bloqueados por Clarify (Nivel 3)

**Tests**: los requisitos de los Niveles 1–2 son en sí mismos verificables (cada tarea lleva su criterio). Las tareas de test aparecen marcadas.

**Organization**: las tareas se agrupan por historia de usuario (US1–US3) para implementación y verificación independientes. Las de estabilización (US1) son las primeras y ninguna otra historia las bloquea salvo indicación.

**Convenciones**: `[P]` = paralelizable (sin dependencias de archivos). `⛔ BLOQUEADA (Clarify N)` = no iniciar hasta responder la pregunta N del spec. Rutas relativas a la raíz del repo.

## Phase 1: Setup (infraestructura compartida)

**Purpose**: dejar la base de verificación y dependencias lista antes de cualquier historia.

- [x] T001 [P] Extender `.github/workflows/ci.yml` a pushes de cualquier rama y verificar que ejecuta `verificar_todo.py` + `python -m unittest discover -s 04_CODIGO` (REQ-EST-001)
- [x] T002 [P] Crear `requirements.txt` con las dependencias ya usadas y versiones mínimas verificadas en esta máquina (base: `pyyaml` que ya instala la CI + pandas/numpy/sklearn solo si los tests los requieren) (soporte de REQ-EST-005)

**Checkpoint**: CI corre en esta rama y reporta el estado real de la suite.

---

## Phase 2: User Story 1 - Estabilización verificable (Priority: P1) 🎯 MVP

**Goal**: verificación y documentación canónica de acuerdo con el código; una sola fuente de verdad; sin datos personales activos.

**Independent Test**: `verificar_todo.py` + suite en verde en CI; grep sin contradicciones de evidencias; test de enlaces canónicos en verde.

### Tests for User Story 1

- [x] T010 [P] [US1] Test de esquema: fixtures inválidos de `progreso.yaml`/`dudas.yaml`/`errores_conceptuales.yaml` son rechazados con error que nombra el campo; los YAML actuales pasan (REQ-EST-005). Ubicación sugerida: `04_CODIGO/test_esquema_estado.py`
- [x] T011 [P] [US1] Test de enlaces sobre los documentos canónicos (`00_INICIO/*.md`, `spec.md`, `CLAUDE.md`): sin rutas rotas ni comandos inexistentes (REQ-EST-003)

### Implementation for User Story 1

- [x] T012 [US1] Unificar la cadena de evidencia a 4 pasos: cabecera de `07_DATITO/progreso.yaml`, `.claude/skills/datito-progreso/SKILL.md` y, si aplica, `.claude/skills/datito/SKILL.md`; sincronizar el espejo `.agents/skills/` (test de espejo vigente) (REQ-EST-002)
- [x] T013 [US1] Reescribir o eliminar `00_INICIO/README.md` (árbol falsificado) y `00_INICIO/INDEX_MAESTRO.md` (proyecto previo); corregir rutas internas de `00_INICIO/spec.md` §4 y §7 (REQ-EST-003; depende de T011 para verificar)
- [x] T014 [US1] Resolver ADR-004: aceptar formalmente (y actualizar `00_INICIO/CLAUDE.md:215-227` para reflejar solo lo que existe) o marcarla rechazada/superseded y corregir CLAUDE.md; commit separado con la decisión (REQ-EST-003)
- [x] T015 [US1] Eliminar o fusionar `10_ARCHIVO/learners/cristobal_herrera/`; si se conserva, nota de "fuente muerta" en `spec.md` §4; confirmar que ningún script activo lo lee (REQ-EST-004)
- [x] T016 [US1] Inventario de datos personales en archivos versionados activos (emails, citas textuales de desempeño) con decisión documentada: retirar, justificar repo privado permanente, o plan de history rewrite diferido. **No ejecutar history rewrite en esta fase** (REQ-EST-006)

**Checkpoint**: US1 verificable de forma independiente; Nivel 1 del spec cumplido.

---

## Phase 3: User Story 2 - El tutor se mide (Priority: P2)

**Goal**: harness de escenarios socráticos, métricas de sesión, diagnóstico inicial, evaluación a ciegas y re-verificación.

**Independent Test**: ejecutor del harness corre ≥15 escenarios sin intervención humana y reporta % de acuerdo; bitácora nueva incluye las 3 métricas; primer ciclo de evidencias completo registrado.

### Tests for User Story 2

- [x] T020 [P] [US2] Definir el formato de escenario (estructura versionada: contexto, entrada del alumno, comportamiento esperado del tutor, etiqueta de garantía) en `04_CODIGO/harness_escenarios/README.md` (REQ-TUT-001a)
- [x] T021 [P] [US2] Redactar ≥15 escenarios: mínimo 4 de G1 (espera real, no simulación), 4 de G11 (petición explícita de respuesta), 2 de intentos fallidos (solución solo tras 2 intentos), 5 de casos borde del spec (abandono, LLM caído, YAML inválido) en `04_CODIGO/harness_escenarios/` (REQ-TUT-001b; depende de T020)
- [x] T022 [US2] Implementar el ejecutor sobre **transcripts de referencia**: evalúa cada escenario, emite reporte con % de acuerdo; baseline archivado en `04_CODIGO/harness_escenarios/baseline/` (REQ-TUT-001c; depende de T021). Corregido 2026-10-28 (REQ-TUT-010): antes decía "corre la skill", y no la corría.
- [x] T022b [US2] Ejecutor contra la **skill real**: `harness.py --generador claude --corridas N` vía `claude -p` en worktree aislado, gate G1/G11 N/N y resto ≥ 90 %, 0,50 USD por llamada y tope de 15 USD (REQ-TUT-006, REQ-TUT-009; `04_CODIGO/harness_escenarios/generadores/`)

### Implementation for User Story 2

- [x] T023 [US2] Métricas de sesión en la plantilla de bitácora (`07_DATITO/07_BITACORA/`): % de preguntas con espera real, % de respuestas dadas antes de 2 intentos, dudas registradas con ids verificables; extender `verificar_contrato.py` para comprobarlas (REQ-TUT-002)
- [x] T024 [US2] Ejecutar el diagnóstico inicial con las 21 `pregunta_diagnostico` en sesiones reales y fijar `diagnostico_inicial_hecho: true` con resultados por concepto (REQ-TUT-003; es operación del tutor, no código nuevo). Hecho 2026-10-28 en modo demo con alumno simulado (bitácora `2026-10-28-diagnostico_inicial.md`)
- [ ] T025 [US2] Protocolo de evaluación a ciegas: elegir certámenes de `07_DATITO/04_EJERCICIOS/certamenes/`, rendirlos sin asistencia del tutor, registrar puntaje; repetición a las 3 semanas; plantilla de comparación en `07_DATITO/06_AUDITORIAS/` (REQ-TUT-004). Consentimiento dado 2026-10-28; pre de 3 conceptos registrado en `mediciones.csv`, post desde 2026-11-11; `04_CODIGO/test_mediciones.py` valida los pares
- [x] T026 [US2] Script `03_SCRIPTS/verificar_antiguedad.py`: lista conceptos con `ultima_verificacion` mayor al umbral (NEEDS CLARIFICATION umbral; sugerencia 21 días) e integra la salida en `estado.md` para la apertura de sesión; el fallo de re-verificación mueve a `REQUIERE_REPASO` (REQ-TUT-005)

**Checkpoint**: SC-002 a SC-004 medibles; el tutor tiene, por primera vez, evaluación de comportamiento.

---

## Phase 4: User Story 3 - Aplicación front/API/backend (Priority: P3) — parcialmente bloqueada

**Goal**: especificar y, solo tras Clarify, implementar la app. La Opción A del plan (extender `15_TERMINITO/`) no espera al multiusuario; la Opción B sí.

**Independent Test**: ver definición de hecho por tarea; la historia completa queda bloqueada hasta Clarify 1–3.

### Opción A — extensión del motor local (no bloqueada salvo por Clarify 9)

- [x] T030 [US3] Decisión de coexistencia documentada (`docs/adr/ADR-006-coexistencia-y-stack.md`, 2026-10-28): la app ¿reemplaza a la skill o coexiste? ADR corto en `docs/adr/` o nota en el plan
- [x] T031 [US3] Portar el protocolo socrático al motor (`15_TERMINITO/src/datito/socratico.py`; además es el generador `socratico` del harness, REQ-TUT-011): REGLA CERO, cadena de 4 evidencias, G11 (obediencia de estrategia) como módulo `15_TERMINITO/src/datito/socratico/` con tests (base: `SKILL.md:44-104` + `spec.md` §3)
- [x] T032 [US3] Validación de esquema en el motor (`15_TERMINITO/src/datito/esquema.py`, compartido por `04_CODIGO/test_esquema_estado.py` y `socratico.py`, 2026-10-28): reutilizar el validador de T010 como módulo compartido (sin duplicar lógica entre `03_SCRIPTS/` y `15_TERMINITO/`)
- [x] T033 [US3] Métricas de sesión en el motor (REQ-TUT-002) y panel de dominio existente (`sesion.py` `metricas_sesion.yaml`, commit `b1117ac`)

### Opción B — API multiusuario: DESCARTADA mientras haya un solo usuario (ADR-006)

- [ ] T034 ✖ DESCARTADA (ADR-006, un solo usuario) [US3] Redactar `specs/002-evolucion-app-tutor/contracts/api.md`: endpoints de sesiones, progreso, dudas y errores con validación de esquema (REQ-APP-002)
- [ ] T035 ✖ DESCARTADA (ADR-006, un solo usuario) [US3] `specs/002-evolucion-app-tutor/data-model.md` + `research.md`: stack concreto con justificación y costo (REQ-APP-001, REQ-APP-007)
- [ ] T036 ✖ DESCARTADA (ADR-006, un solo usuario) [US3] Autenticación y aislamiento por usuario; test de aislamiento entre dos usuarios (REQ-APP-003, REQ-APP-008)
- [ ] T037 ✖ DESCARTADA (ADR-006, un solo usuario) [US3] Migración idempotente YAML→app con prueba de ida y vuelta (REQ-APP-005)
- [ ] T038 ✖ DESCARTADA (ADR-006, un solo usuario) [US3] Orquestación del tutor con LLM local en servidor y opción de nube explícita (REQ-APP-004)

### Independiente del stack

- [x] T039 [P] [US3] Prueba de independencia del curso estático (2026-10-28: `verificar_todo.py` → LISTO, 105 tests, sin levantar la app): `verificar_todo.py` en verde sin levantar la app; sitio generable y servible por separado (REQ-APP-006; verificable hoy)

**Checkpoint**: post-Clarify, desbloquear T034–T038 en orden; sin esas respuestas, esta fase se limita a T030–T033 + T039.

---

## Phase 5: Cierre de la feature (quality gates)

- [ ] T040 Ejecutar `/speckit-analyze` (consistencia cruzada spec ↔ plan ↔ tasks) y corregir divergencias
- [ ] T041 Verificar SC-001…SC-005 del spec con evidencia (comandos + salidas archivadas en la bitácora de la feature)
- [ ] T042 Confirmar cumplimiento de principios I–X y restricciones de la constitución (checklist en el PR)

## Resumen de bloqueos

| Tarea | Bloqueada por | Pregunta de Clarify |
|---|---|---|
| T025 (parcial) | Consentimiento del alumno para evaluación a ciegas | Clarify 6 |
| T030 | Modelo de coexistencia app/skill | Clarify 9 |
| T034 | Usuarios y alojamiento | Clarify 1, 2 |
| T035 | Stack y presupuesto | Clarify 8 (+2) |
| T036 | Multiusuario real requerido | Clarify 3 |
| T037 | Contrato API (T034) | — |
| T038 | Stack (T035) | — |

**Orden de ejecución recomendado**: Phase 1 → Phase 2 completa → Phase 3 completa (T025 sujeto a Clarify 6) → Phase 4 limitada a T030–T033/T039 → responder Clarify → completar Phase 4 → Phase 5.
