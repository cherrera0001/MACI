# Specification Quality Checklist: MACI 1.0 — Plataforma Termito

**Purpose**: Validate specification completeness and quality before proceeding to planning
**Created**: 2026-10-17
**Feature**: [spec.md](../spec.md)

## Content Quality

- [x] No implementation details (languages, frameworks, APIs) — verificado: ninguna
  mención a Python/Ollama/FastAPI; las restricciones de archivos legibles y offline son
  requisitos del dominio provenientes de la constitución, no decisiones de implementación.
- [x] Focused on user value and business needs — verificado: cada historia declara el
  valor (Why this priority) desde la perspectiva del estudiante.
- [x] Written for non-technical stakeholders — verificado: lenguaje pedagógico; la única
  tabla técnica (paridad competitiva) está redactada en términos de producto.
- [x] All mandatory sections completed — User Scenarios & Testing, Requirements, Success
  Criteria completos; Key Entities incluido (la feature involucra datos).

## Requirement Completeness

- [x] No [NEEDS CLARIFICATION] markers remain — 0 marcadores; las decisiones delegadas
  se documentaron en Assumptions (idioma primero, un curso = un directorio, LLM local por
  defecto, tests incluidos en backlog).
- [x] Requirements are testable and unambiguous — cada FR tiene verificación asociada en
  quickstart.md o en los invariantes de contracts/api.md.
- [x] Success criteria are measurable — SC-001 a SC-008 con métricas (30 min, 100%, 0
  violaciones, <10 s no aplica; tiempos y porcentajes explícitos).
- [x] Success criteria are technology-agnostic — ningún SC menciona tecnología.
- [x] All acceptance scenarios are defined — 4 escenarios por historia P1, 2 por P2/P3.
- [x] Edge cases are identified — 7 edge cases explícitos (PDF escaneado, fuera de
  alcance, insistencia en la respuesta, LLM ausente, edición que rompe, cierre
  accidental, Termitos solapados).
- [x] Scope is clearly bounded — sección "Fuera del MVP" + Assumptions.
- [x] Dependencies and assumptions identified — Assumptions completo; dependencia del
  curso v0.0.1 como criterio de aceptación (SC-007) y de Ollama/modelo local documentada
  en quickstart.md.

## Feature Readiness

- [x] All functional requirements have clear acceptance criteria — mapeo FR → escenarios
  → contratos (api.md/cli.md) trazable.
- [x] User scenarios cover primary flows — construir (US1), conversar (US2), evaluarse
  (US3), ciclo de vida (US4); secundarios: grafo (US5), familia (US6), portabilidad (US7).
- [x] Feature meets measurable outcomes defined in Success Criteria — quickstart.md
  define cómo verificar cada SC-00x de extremo a extremo.
- [x] No implementation details leak into specification — consistente con el primer ítem.

## Validación ejecutada

- Iteración 1 (2026-10-17): sección competitiva pendiente de la Fase 0 → resuelta al
  integrar `docs/investigacion/estado-del-arte.md` (12 competidores) y `patrones.md`.
- Iteración 2: revisión completa post-integración — sin fallos.
- Marcadores [NEEDS CLARIFICATION]: 0 (límite permitido: 3).

## Notes

- Items marked incomplete require spec updates before `/speckit-clarify` or `/speckit-plan`
- Los headers de plantilla se conservan en inglés por compatibilidad con las
  herramientas Spec Kit; todo el contenido está en español según instrucción del dueño.
