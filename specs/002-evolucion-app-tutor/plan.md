# Implementation Plan: Evolución de MACI a aplicación con tutor personalizado

**Branch**: `sdd/planificacion-maci` | **Date**: 2026-10-27 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-evolucion-app-tutor/spec.md`

**Note**: documento de planificación. No implementa código de aplicación; fija
requisitos de arquitectura, opciones con costo y recomendación. Las decisiones
marcadas NEEDS CLARIFICATION en el spec bloquean solo el Nivel 3.

## Summary

Tres frentes ordenados por valor y riesgo: (1) **Estabilización** — poner la
verificación y la documentación canónica de acuerdo con el código, con
contradicciones cerradas (cadena de evidencia 4-vs-3, docs falsos, duplicado
divergente, datos personales inventariados); (2) **Medición del tutor** —
harness de escenarios socráticos con resultado esperado, métricas de sesión,
diagnóstico inicial, evaluación a ciegas y re-verificación; (3) **Aplicación** —
frontend + API + backend como decisión de arquitectura: se especifican los
requisitos y las opciones aquí; el stack se congela solo después de responder
las preguntas de Clarify del spec. Enfoque de extensión incremental del
motor existente (`15_TERMINITO/`) hacia una API, preservando el curso
estático y los YAML como fuente de verdad primaria.

## Technical Context

**Language/Version**: Python 3.12.3 (verificado en el entorno). Backend en
Python (coherente con `15_TERMINITO`, `03_SCRIPTS/`). Frontend: HTML/JS
vanilla ya usado por el curso generado; framework de UI: NEEDS CLARIFICATION.

**Primary Dependencies**: NEEDS CLARIFICATION a nivel de versión. Anclajes
verificados: índice TF-IDF propio y LLM vía Ollama ya integrados en
`15_TERMINITO` (README: `qwen2.5:3b` como referencia); sin manifiesto de
dependencias en el repo (deuda conocida, `EVALUACION.md` A2) — la
estabilización (REQ-EST) es el lugar de nacer de un `requirements.txt`.

**Storage**: archivos legibles versionables (YAML/Markdown/JSON) como
almacenamiento primario — obligatorio por constitución ("las bases de datos
opacas están prohibidas como almacenamiento primario"). Base de datos
relacional/embedded solo como caché indexado con exportación íntegra a YAML.

**Testing**: `unittest` (convención vigente del repo, 26 tests en verde en
`680182b`); `pytest` disponible como runner. Harness de tutor (REQ-TUT-001)
como suite más ejecutor propio (el comportamiento esperado no es aserción de
función sino de diálogo).

**Target Platform**: Linux/WSL (Ubuntu 24.04 verificado) como primera
plataforma; despliegue de la API: NEEDS CLARIFICATION (local/VPS/nube).

**Project Type**: web-service + static-site companion + CLI heredado.

**Performance Goals**: NEEDS CLARIFICATION (depende de usuarios concurrentes;
ver Clarify 1–2). No hay objetivos de concurrencia que justifiquen números hoy.

**Constraints**: offline-first (constitución VII); LLM local por defecto
(restricciones técnicas); español como idioma primario; migración incremental
nunca big-bang; secretos jamás versionados; el curso estático debe seguir
generándose y sirviéndose sin la app (REQ-APP-006).

**Scale/Scope**: NEEDS CLARIFICATION (número de usuarios reales en el primer
semestre; ver Clarify 1).

## Constitution Check

*GATE: pasado antes de cualquier decisión de arquitectura. Re-chequeo tras la recomendación.*

| Principio / restricción | ¿La especificación y la recomendación cumplen? | Nota |
|---|---|---|
| I. El estudiante diseña el agente | Sí | REQ-APP y opciones preservan identidad editable del tutor (heredado de Termito) |
| II. Evidencia citada o silencio | Sí | sin cambios; el harness puede verificar etiquetas G4 |
| III. Lucha productiva | Sí | REQ-TUT-001/002 lo miden por primera vez |
| V. Evaluación por distinciones | Sí | REQ-TUT-004 la instrumenta contra certámenes reales |
| VII. Offline-first y soberanía de datos | Sí en Opciones A y D; **parcial en B** (exige LLM local en el servidor y exportación); **incumplida en C** | ver Opciones |
| Restricción: archivos legibles como almacén primario | Sí | REQ-APP-005 lo hace criterio de aceptación |
| Restricción: LLM local por defecto | Sí en A y D; condicional en B; no en C | C queda descartada por esto |
| Restricción: migración incremental | Sí | la fase de estabilización precede a todo |
| Restricción: secretos nunca versionados | Sí | REQ-EST-006 inventaria y decide |

Re-chequeo post-recomendación: la recomendación (A ahora, B después, C
descartada, D evolución) cumple todos los principios con una condición
explícita en B. Sin violaciones que justificar.

## Opciones de arquitectura (front / API / backend)

Estado verificado que condiciona las opciones: el sitio estático ya se genera
con `03_SCRIPTS/construir_navegacion.py` y se publica en Vercel
(`publicar_sitio.mjs`, `vercel.json`); `15_TERMINITO/` tiene ya el motor del
tutor (índice TF-IDF sobre los materiales, evidencia citada, evaluación por
distinciones, panel de dominio, web vanilla de 5 pantallas, paquete
distribuible) con LLM local vía Ollama; la skill de Claude Code conserva el
protocolo pedagógico maduro que el motor aún no tiene.

### Opción A — Extender el motor local (Termito) como app de escritorio/navegador local

- **Descripción**: evolucionar `15_TERMINITO/` (Python + web vanilla + LLM
  local) hasta ser la app del estudiante: portar el protocolo de la skill
  (REGLA CERO, cadena de 4 evidencias, G11), añadir persistencia de sesión
  con métricas y validación de esquema. Sin servidor remoto.
- **Pros**: cumple íntegro la constitución (offline-first, LLM local, archivos
  legibles, soberanía de datos); reutiliza el 80% del motor existente; costo
  de infraestructura cero; sin superficie de ataque remota; el paquete
  distribuible ya existe (`dist/datito.zip`).
- **Contras**: un usuario por máquina (sin cuentas ni sincronización);
  requiere que el estudiante instale Python/Ollama; sin acceso desde el móvil
  fuera de la máquina.
- **Costo**: bajo — horas de desarrollo sobre código propio; cero infra.

### Opción B — Aplicación web multiusuario: front estático + API propia con LLM en el servidor

- **Descripción**: el generador actual sigue produciendo el curso estático;
  una API (Python, stack a congelar tras Clarify) expone sesiones/progreso
  con validación de esquema y aislamiento por usuario; el LLM corre en el
  servidor (Ollama en VPS) con opción explícita de nube; almacén primario en
  archivos exportables.
- **Pros**: multiusuario real con cuentas; acceso desde cualquier
  dispositivo; progreso centralizado pero exportable (cumple VII con la
  condición de exportación y nube-opt-in); el front estático ya existe.
- **Contras**: exige hosting (costo y decisión pendientes), operación de un
  servidor, y endurecimiento de privacidad (datos de menores si algún día
  aplica: fuera de alcance hoy pero a diseñar); riesgo de "creeping
  big-bang" que la constitución prohíbe — mitigar con migración incremental
  (REQ-APP-005).
- **Costo**: medio — VPS (~US$5–20/mes según GPU/CPU para LLM local; NEEDS
  CLARIFICATION presupuesto), más horas de desarrollo de auth y aislamiento.

### Opción C — Serverless sobre el despliegue actual (Vercel/Cloudflare)

- **Descripción**: API como funciones serverless junto al sitio estático ya
  servido en Vercel.
- **Pros**: despliegue existente, sin servidor que mantener, escalado gratis.
- **Contras**: **incumple la restricción "LLM local por defecto"** (no hay GPU
  en serverless; la nube sería obligatoria, no opt-in); estado efímero vs.
  archivos versionables como fuente primaria; datos del estudiante en infra
  de terceros. Requiere enmienda constitucional ratificada.
- **Costo**: bajo en dinero; alto en excepciones de gobernanza.

### Opción D — PWA offline-first con sincronización opcional

- **Descripción**: app web instalable que corre el tutor en local (WASM o
  backend embebido) y sincroniza cuando hay red.
- **Pros**: máximo cumplimiento offline-first; acceso móvil; la sincronización
  puede ser "exportación/importación de archivos" (compatible con la
  constitución) antes que sync automático.
- **Contras**: complejidad de conflicto de estado entre dos máquinas; auth
  sigue sin resolver; es evolución de A, no punto de partida.
- **Costo**: medio-alto en complejidad; bajo en infra.

### Recomendación justificada

**Ahora (sin dependencias de Clarify): Opción A.** Es la única que cumple la
constitución sin condiciones y reutiliza el motor existente; además los
Niveles 1–2 del spec (estabilización y medición del tutor) son agnósticos al
stack y se hacen igual con A.

**Después (condicionada a Clarify 1–2–3): Opción B como contrato, no como
código.** Se redacta `contracts/api.md` (REQ-APP-002) y se implementa solo
cuando haya respuestas sobre usuarios y alojamiento, con LLM en el servidor
(local) y exportación YAML como criterio de aceptación. Esto evita construir
multiusuario para usuarios que quizá no existan (riesgo confirmado por la
propia historia del repo: el andamiaje multi-curso de `context_manager.py`
se archivó sin llegar a tener un segundo usuario real).

**Descartada: Opción C** por conflicto constitucional documentado (solo
vuelve con enmienda ratificada). **Diferida: Opción D** como evolución futura
de A si se prioriza el móvil.

**Compatibilidad garantizada en cualquier opción**:
- El curso estático sigue generándose desde `clases.yaml` con
  `construir_navegacion.py` y sirviéndose sin la app (REQ-APP-006; la Opción B
  lo sirve tal cual; A y D lo empaquetan).
- Los YAML de `07_DATITO/` son la fuente de verdad primaria en A; en B se
  importan con migración idempotente y exportación íntegra (REQ-APP-005). La
  app nunca exige reescribirlos.

## Project Structure

### Documentation (this feature)

```text
specs/002-evolucion-app-tutor/
├── spec.md              # Este flujo: qué y por qué (3 niveles, REQ, SC)
├── plan.md              # Este archivo: opciones y recomendación
└── tasks.md             # Lista ordenada con dependencias y bloqueos
# contracts/             # Pendiente: contrato API (REQ-APP-002), post-Clarify
# data-model.md          # Pendiente: entidades del Nivel 3, post-Clarify
# research.md            # Pendiente: spike de stack, post-Clarify
```

### Source Code (repository root) — destino, no se crea en esta etapa

Estructura de destino sugerida (a confirmar con el stack elegido; la
estabilización no la requiere):

```text
# Extensión del motor existente (Opción A) — preliminar
15_TERMINITO/src/datito/    # motor existente (índice, evidencia, evaluador…)
15_TERMINITO/src/datito/socratico/   # NUEVO: protocolo portado de la skill
15_TERMINITO/src/datito/metrics/     # NUEVO: métricas de sesión (REQ-TUT-002)
15_TERMINITO/src/datito/validacion/  # NUEVO: esquemas YAML (REQ-EST-005)
tests/                      # suite existente + harness de escenarios (REQ-TUT-001)
```

La estructura del front/API/back de la Opción B no se fija en esta etapa:
depende de las respuestas de Clarify y se documentará en
`data-model.md` + `contracts/` cuando existan.

**Structure Decision**: se mantiene la estructura actual del repo; se agregan
solo los artefactos de esta feature en `specs/002-evolucion-app-tutor/` y, en
la fase de estabilización, validadores dentro de `03_SCRIPTS/` y `04_CODIGO/`
(convenciones vigentes), sin tocar `07_DATITO/` salvo correcciones de
documentación (cabecera de `progreso.yaml`) decididas en REQ-EST-002.

## Complexity Tracking

Sin violaciones de la constitución en la ruta recomendada (A → B condicionada;
C descartada). Dos tensiones documentadas, resueltas sin excepción:

| Tensión | Resolución |
|---|---|
| Opción B centraliza datos en un servidor (principio VII) | Cumple con dos condiciones de aceptación explícitas: LLM local en servidor + exportación íntegra por usuario (REQ-APP-005/008). Si las condiciones no se aceptan, B se descarta y queda A |
| El harness de tutor evalúa diálogo, no funciones | No es violación; es una suite con ejecutor propio (documentado en Technical Context > Testing) |
