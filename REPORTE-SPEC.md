# REPORTE-SPEC — MACI 1.0 (Plataforma Termito)

**Fecha**: 2026-10-17 · **Ciclo**: specify → plan → tasks (Spec Kit) · **Estado**: ✅ completo y validado, listo para implementar

---

## 1. Resumen ejecutivo

Se especificó, planeó y taskificó MACI 1.0: la plataforma con la que cualquier persona
construye su propio tutor agentico ("Termito") a partir de los materiales reales de lo
que va a aprender. El backlog cubre **solo hasta el hito MVP**: un curso real migrado
(Fundamentos de Ciencia de Datos actual) a un Termito funcional, evaluándose por
distinciones conceptuales, 100% offline, con ciclo de vida completo (nace, evoluciona
con notas reales, muere conservando el registro).

Artefactos entregados:

| Artefacto | Ubicación | Estado |
|---|---|---|
| Constitución v1.0.0 (10 principios I–X) | `.specify/memory/constitución.md` | ✅ ratificada 2026-10-17 |
| Spec (7 historias, 22 FRs, 8 SCs, análisis competitivo) | `specs/001-termito-platform/spec.md` | ✅ validado, checklist en verde |
| Plan técnico + research (10 decisiones R1–R10) | `specs/001-termito-platform/plan.md`, `research.md` | ✅ gate constitucional en verde |
| Data model + 3 contratos + quickstart | `specs/001-termito-platform/data-model.md`, `contracts/`, `quickstart.md` | ✅ |
| Backlog 64 tareas (8 fases, tests incluidos) | `specs/001-termito-platform/tasks.md` | ✅ MVP = fases 1–7 |
| Investigación de mercado (12 competidores, citada) | `docs/investigacion/estado-del-arte.md`, `patrones.md` | ✅ integrada al spec |

## 2. Decisiones tomadas y por qué

1. **Arquitectura**: servidor local Python (FastAPI) + UI web estática vanilla, sin
   build. Porque: coherencia con el repo (ya es Python), offline-first sin toolchain.
2. **LLM local por defecto** (Ollama, modelo abierto 3–8B) con interfaz `LLMProvider`
   que también admite nube opcional. Porque: principio VII; un solo punto de cambio.
3. **Lucha productiva como máquina de estados determinista en código**, no como
   instrucción de prompt. Porque: SC-003 ("0 soluciones antes del intento") solo es
   auditable/testeable si la lógica no la decide el modelo.
4. **Evidencia citada por generación anclada a fragmentos** (el tutor responde solo
   desde fragmentos recuperados con fid estables; sin fragmento → "sin fuente"). Porque:
   convierte SC-002 en propiedad estructural, no promesa del LLM (une a Jill Watson con
   NotebookLM, hueco que nadie cubre).
5. **Un curso = un directorio autocontenido** (`15_TERMINITO/cursos/<slug>/`) con todo
   el estado en YAML/Markdown y el índice vectorial como caché regenerable. Porque:
   portabilidad (US7), independencia (US9) y la restricción constitucional de archivos
   legibles, de un solo golpe.
6. **Migración incremental**: adaptador `legacy_maci.py` que convierte `07_DATITO/`
   en la primera instancia; el sitio estático v0.0.1 nunca se toca. Porque: la
   constitución prohíbe big-bang y SC-007 exige cero regresiones.
7. **`15_TERMINITO/`** como carpeta de la plataforma (siguiente número de la
   convención 00–14). Porque: respeta la numeración existente sin tocar código activo.
8. **Versionado del prompt en archivos planos** (`prompt/versions/` + manifest), sin
   requerir git al estudiante. Porque: FR-005 exige reversibilidad para cualquier
   persona, no solo técnicas.
9. **unittest** (no pytest) y **video por transcripciones provistas** (whisper
   opcional). Porque: convención del repo y MVP sin modelos pesados.
10. **Backlog solo hasta el MVP**; US5–US7 (grafo visual, familia, portabilidad) quedan
    especificadas pero fuera del tasks.md, por condición explícita del dueño.
11. **Headings de plantilla Spec Kit en inglés, contenido 100% en español**: las
    herramientas del flujo (analyze/implement) reconocen la estructura original.
12. **REA MCP (Fase 0.4)**: no disponible en este entorno; anotado y continuado sin
    inspección técnica de competidores (la evidencia vino de fuentes públicas citadas).

## 3. Hallazgos clave del estado del arte (fuente: docs/investigacion/)

- **Nadie deja al estudiante diseñar su agente.** Todo el mercado (Jill Watson, Khanmigo,
  Duolingo Max, Century, Squirrel AI, LearnLM, Study Mode, Claude for Education,
  NotebookLM, Jotform) entrega un tutor diseñado por la plataforma o la institución.
- **La paridad mínima creíble ya estaba contemplada** en el spec: tutoría socrática
  (Khanmigo/Study Mode), grounding en materiales con citas (Jill Watson + NotebookLM —
  Termito une ambos), evaluación formativa de respuesta abierta (Cognii), calibración por
  nivel (Century). Ninguna historia nueva fue necesaria.
- **Lecciones duras del mercado adoptadas**: Khanmigo tuvo solo ~15% de uso real → el
  registro de sesiones de Termito instrumenta adopción desde el día 1 (patrón 7);
  Riiid pivotó → la evaluación por comprensión (distinciones) es la apuesta correcta.
- **Tesis confirmada**: "El mercado ofrece consumo; Termito ofrece arquitectura del
  aprendizaje."

## 4. Riesgos top 5 con mitigación

| # | Riesgo | Mitigación en diseño |
|---|---|---|
| 1 | Modelo local pequeño con español débil | Evaluación de modelos en T058/quickstart; `LLMProvider` permite cambiar modelo o usar nube sin tocar el sistema |
| 2 | Evidencia recuperada poco relevante (afirmación mal sustentada) | Top-k estricto, fragmentos pequeños con tema, verificación humana de 1 clic sobre cada cita (research R5, limitación honesta documentada) |
| 3 | Latencia en CPU modesta | Modelo 3–4B Q4, streaming, objetivo <10 s primera respuesta; medición obligatoria en T062 |
| 4 | Los 30 min de construcción no se cumplen si la ingesta fricciona | Ingesta con resumen claro y advertencias (FR-002), wizard de 8 pasos reanudable; SC-001 se mide en T030 checkpoint |
| 5 | Migración con baseline roto (verificar_todo ya falla por rutas F:\, EVALUACION.md C1) | T057 compara "no empeorar", no "sanar deuda previa"; la deuda F:\ queda fuera del alcance de este feature |

## 5. Comandos exactos para retomar mañana

```bash
# 1. Ver el backlog y empezar a implementar (fases 1–2 primero):
cat specs/001-termito-platform/tasks.md

# 2. Con Kimi Code, retomar el flujo con el skill:
#    /speckit-implement
#    (lee .specify/feature.json → specs/001-termito-platform/, ejecuta T001 en adelante)

# 3. Preparar el entorno antes de implementar:
uv venv 15_TERMINITO/.venv && uv pip install -r 15_TERMINITO/pyproject.toml  # tras T002
ollama pull qwen2.5:3b    # o modelo es→en evaluado en T058

# 4. Verificación de consistencia de artefactos en cualquier momento:
#    /speckit-analyze

# 5. Validación del MVP al terminar la Fase 7:
#    escenarios 1–6 de specs/001-termito-platform/quickstart.md
#    (offline, con evidencia en specs/001-termito-platform/evidencias-mvp.md)
```

**Recordatorio de alcance**: no se escribió código de producto. Lo único creado fuera de
`specs/` y `.specify/` son los dos documentos de investigación en `docs/investigacion/`
(solicitados explícitamente en la Fase 0).

## 6. Preguntas críticas de Parada — dónde responde el spec

a) Construir un Termito en <30 min → US1 + FR-006 + quickstart escenario 1.
b) Evidencia citada en cada respuesta → FR-007/FR-011 + research R5 + panel de evidencia.
c) Evaluar sin trampas → FR-008 + máquina de estados determinista (R4) + SC-003.
d) Editar el prompt en cualquier momento → FR-005 + contrato CLI `prompt ver|editar|revertir` + R7.
e) Progreso preservado al "desaparecer" → FR-016 + formato-curso.md regla 7 + SC-005.
