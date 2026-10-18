# Implementation Plan: MACI 1.0 — Plataforma de tutores agenticos personalizados (Termito)

**Branch**: `001-termito-platform` | **Date**: 2026-10-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-termito-platform/spec.md`

**Note**: Template resolution ejecutada manualmente (sin PowerShell en este entorno);
la capa activa es el template de proyecto `.specify/templates/plan-template.md`.

## Summary

Construir la plataforma MACI 1.0 que permite a cualquier estudiante crear su propio
tutor agentico ("Termito") a partir de los materiales reales de un curso, conversar con
él con evidencia citada y lucha productiva, ser evaluado por distinciones conceptuales y
cerrar el ciclo de vida conservando su registro. Enfoque técnico: aplicación local en
Python (servidor ligero + interfaz web servida en localhost), LLM local por defecto
con capa de abstracción para nube opcional, orquestación determinista sobre el LLM para
garantizar evidencia y lucha productiva, y todo el estado en archivos versionables
(YAML/Markdown/JSON) con directorio autocontenido por curso. Migración incremental
sobre el sitio estático v0.0.1, sin reescritura big-bang.

## Technical Context

**Language/Version**: Python 3.12 (ya es el runtime del repositorio; evita introducir
una segunda pila). Interfaz: web estática (HTML/JS) servida localmente.

**Primary Dependencies**:
- Servidor local: FastAPI + uvicorn (o módulo `http.server` de stdlib si se prefiere
  cero dependencias en el MVP — decisión en research.md).
- LLM local: Ollama (HTTP en localhost) con modelo abierto pequeño/mediano.
- Embeddings locales: fastembed o sentence-transformers vía Ollama.
- Ingesta: pypdf (PDF), python-pptx (ya usado en el repo), trafilatura (web),
  whisper.cpp opcional (video; el MVP acepta transcripciones ya provistas).

**Storage**: archivos versionables como fuente de verdad (YAML/Markdown/JSON). Índice
vectorial como artefacto derivado regenerable (caché, nunca fuente primaria).

**Testing**: `unittest` del stdlib, coherente con la convención existente del repo
(`04_CODIGO/test_*.py`). Runner: `python -m unittest discover`.

**Target Platform**: Linux/macOS/Windows de escritorio; servidor local en
`localhost`, uso mediante navegador. Sin despliegue remoto requerido.

**Project Type**: aplicación local (local web app) con CLI auxiliar.

**Performance Goals**: primera respuesta del tutor <10 s en hardware modesto (CPU);
ingesta de un curso típico (<200 páginas, <10 fuentes) <5 min; apertura del panel
de dominio <2 s.

**Constraints**: 100% funcional sin conexión (FR-020); datos solo en la máquina del
usuario (FR-021); creación de Termito <30 min de trabajo activo (FR-006); memoria
en uso <4 GB con modelo local pequeño.

**Scale/Scope**: un usuario (personal), decenas de cursos, materiales de tamaño de
un curso universitario real; no multi-tenant en el MVP.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principio | Decisión de diseño que lo satisface | Estado |
|---|---|---|
| I. Estudiante diseña el agente | Constructor de 8 componentes + prompt siempre visible y editable (FR-003–FR-005) | ✅ |
| II. Evidencia citada o silencio | Capa de orquestación exige cita a fragmento ingerido por afirmación; "sin fuente" explícito (FR-007, FR-011) | ✅ |
| III. Lucha productiva | Máquina de estados de interacción (pista → intento → revisión) implementada fuera del LLM, no delegada al prompt (FR-008) | ✅ |
| IV. Ciclo de vida | Estados de Termito (activo/cerrado) + registro íntegro conservado al cerrar (FR-015, FR-016) | ✅ |
| V. Distinciones | Generador de ítems a partir de pares de conceptos vecinos del grafo (FR-012–FR-014) | ✅ |
| VI. Materiales como verdad | Retrieval solo sobre fragmentos ingeridos; conocimiento general marcado "fuera del curso" (FR-011) | ✅ |
| VII. Offline-first | LLM local por defecto, embeddings locales, cero llamadas de red en uso normal (FR-020, FR-021) | ✅ |
| VIII. Multilenguaje | Cadenas de UI externalizadas desde el día 1; contenido del Termito en el idioma del estudiante (FR-022) | ✅ |
| IX. Familia independiente | Un curso = un directorio autocontenido; sin estado compartido (FR-018, FR-019) | ✅ |
| X. Personalización radical | Componentes 4 y 6 (estilos) condicionan guiones de interacción y son editables (FR-003, FR-005) | ✅ |

Re-check post-Phase 1: sin violaciones. Las restricciones técnicas de la constitución
(archivos legibles, migración incremental, español primero) se reflejan en la sección
Project Structure y en data-model.md.

## Project Structure

### Documentation (this feature)

```text
specs/001-termito-platform/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
15_TERMINITO/                  # Plataforma MACI 1.0 (siguiente número disponible)
├── src/
│   ├── termito/             # Paquete principal
│   │   ├── config.py        # Rutas derivadas de __file__, settings
│   │   ├── ingestor/        # Extracción por tipo de fuente (pdf, pptx, web, video)
│   │   ├── indice/          # Fragmentación, embeddings, búsqueda (artefacto derivado)
│   │   ├── constructor/     # Wizard de 8 componentes + generador/versionado de prompt
│   │   ├── tutor/           # Orquestación: evidencia, lucha productiva, memoria
│   │   ├── evaluador/       # Ítems de distinción, calificación, estado de dominio
│   │   ├── ciclo_vida/      # Notas como retroalimentación, cierre de curso
│   │   ├── grafo/           # Grafo de prerrequisitos + estado de dominio
│   │   ├── familia/         # Panel multi-Termito
│   │   ├── portabilidad/    # Exportar/importar paquete de curso
│   │   ├── i18n/            # Cadenas es/en
│   │   ├── api.py           # Servidor local (endpoints, contrato en contracts/api.md)
│   │   └── cli.py           # Comandos (contrato en contracts/cli.md)
│   └── web/                 # UI estática servida en localhost (español primero)
├── tests/                   # unittest (convención del repo)
├── cursos/                  # Un directorio autocontenido por Termito (datos de usuario)
└── README.md
```

**Structure Decision**: estructura de proyecto único en `15_TERMINITO/` (siguiente
número disponible de la convención 00–14 del repo; el hueco `12_` queda reservado).
Cada instancia de curso/Termito es un directorio autocontenido bajo `cursos/<slug>/`
(materiales, prompt versionado, índice, registro, grafo, progreso), que satisface a la
vez los principios VII (datos del usuario en su máquina), IX (independencia) y la
historia US7 (portabilidad: mover el directorio = exportar). La migración incremental
desde v0.0.1 adapta `07_DATITO/` y `03_SCRIPTS/construir_navegacion.py` como fuentes de
la primera instancia (ver research.md R6). No se modifica código existente hasta la fase
de migración explícita del MVP.

## Complexity Tracking

> Sin violaciones de la constitución que justificar. Decisiones con alternativas
> rechazadas documentadas en research.md (servidor stdlib vs FastAPI, índice vectorial
> vs búsqueda por palabras clave, unittest vs pytest).
