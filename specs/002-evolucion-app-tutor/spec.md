# Feature Specification: Evolución de MACI a aplicación con tutor personalizado

**Feature Branch**: `sdd/planificacion-maci`

> Nota: la convención Spec Kit nombraría la rama `002-evolucion-app-tutor`; se
> conserva `sdd/planificacion-maci` por instrucción explícita del dueño del proyecto.

**Created**: 2026-10-27

**Status**: Draft

**Input**: User description: "Planificar (no implementar) la evolución de MACI usando Spec-Driven Development: estabilización del repo, medición del comportamiento socrático del tutor, y aplicación con frontend/API/backend como decisión de arquitectura pendiente."

## Contexto verificado del repositorio (base de esta especificación)

Toda afirmación de esta sección fue verificada en código el 2026-10-27:

- HEAD real: `680182b` (rama `pr-87`; `main` local y `origin/main` están en `8fbdd6c`, sin ese commit). La suite está **en verde**: 26 tests OK (`unittest discover -s 04_CODIGO`) y `verificar_contrato.py` 12 ok / 0 fallos. El estado "rojo" reportado en la revisión previa fue corregido por `680182b` (enlace `datito/datito.zip`).
- El tutor corre como skill de Claude Code: `.claude/skills/datito/SKILL.md` (protocolo REGLA CERO, modo adaptativo, bucle de 3 niveles). Estado en `07_DATITO/*.yaml`, escrito a mano por el agente, **sin validación de esquema**.
- Sesiones registradas: 3 (`07_DATITO/progreso.yaml` meta `sesiones_totales: 3`); 0 de 21 conceptos en `DOMINADO`; `diagnostico_inicial_hecho: false`.
- Contradicción vigente de contrato: la cadena de evidencia es de **4** pasos en `00_INICIO/spec.md` §3, `07_DATITO/datito.config.yaml:110` y `03_SCRIPTS/verificar_contrato.py:137-159`, pero de **3** pasos en la cabecera de `07_DATITO/progreso.yaml:18-26` y en `.claude/skills/datito-progreso/SKILL.md:34-39`.
- Documentación canónica desactualizada: `00_INICIO/README.md` (árbol falso, reportado en `EVALUACION.md` C2), `00_INICIO/INDEX_MAESTRO.md` (proyecto previo, C3), ADR-004 marcado "PROPUESTA no aceptada" en `docs/adr/ADR-004-estructura-destino.md:3-5` pero tratado como vigente en `00_INICIO/CLAUDE.md:215-227`.
- Duplicado divergente del estado del alumno en `10_ARCHIVO/learners/cristobal_herrera/` (reportado en `EVALUACION.md` A1).
- Constitución existente: `.specify/memory/constitution.md` v1.0.1 (10 principios I–X + restricciones técnicas), ratificada 2026-10-17. Verificación de vigencia de G1–G14 en el anexo de este documento.
- Datos de alumnos en `07_DATITO/` son personales: **ningún requisito de esta especificación los copia, los expone ni los usa como ejemplo**.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Estabilización verificable del repositorio (Priority: P1)

Como mantenedor de MACI, quiero que la verificación automática y la documentación
canónica reflejen la realidad del código, para que cualquier evolución posterior
sobre una base en la que se puede confiar y cuyas reglas se comprueban solas.

**Why this priority**: todo lo demás (medir el tutor, construir la app) es
ilegible si la propia verificación miente. Además la constitución (restricción:
"migración incremental, nunca big-bang; cada incremento deja el sistema operativo
y verificable") lo exige primero.

**Independent Test**: `python 03_SCRIPTS/verificar_todo.py` + `python -m unittest
discover -s 04_CODIGO` en verde en CI (todas las ramas); grep sin contradicciones
de la cadena de evidencia; un test de enlaces que recorra la documentación canónica.

**Acceptance Scenarios**:

1. **Given** un push a cualquier rama, **When** corre CI, **Then** ejecuta la suite completa y falla el build si algo está rojo.
2. **Given** la cabecera de `progreso.yaml`, la skill `datito-progreso` y `spec.md` §3, **When** se compara la cadena de evidencia exigida, **Then** hay una sola versión (4 pasos) en todo el repo.
3. **Given** un YAML de estado con un estado inválido o un campo obligatorio ausente, **When** corre la validación, **Then** es rechazado con error que nombra el campo.

---

### User Story 2 - El tutor se mide: harness de comportamiento socrático (Priority: P2)

Como dueño del tutor, quiero un conjunto de escenarios de diálogo con resultado
esperado (cuándo pregunta, cuándo da pista, cuándo desarrolla la solución) y
métricas de sesión, para saber si el tutor realmente tutoréa en vez de asumirlo.

**Why this priority**: la revisión 2026-10-27 encontró que ninguna prueba valida
comportamiento pedagógico (las garantías G1–G3, G6, G10, G11 se verifican
"manualmente" según `00_INICIO/CLAUDE.md:125-138`). La evidencia externa
(Bastani et al., PNAS 2025) muestra que sin guardrails el LLM entrega la
respuesta y el alumno aprende menos: este riesgo hoy no es medible en MACI.

**Independent Test**: un ejecutor corre ≥15 escenarios versionados y reporta
porcentaje de acuerdo con el comportamiento esperado, sin intervención humana.

**Acceptance Scenarios**:

1. **Given** un escenario donde el alumno falla dos veces, **When** el tutor responde, **Then** desarrolla la solución (y no antes del segundo intento).
2. **Given** un escenario donde el alumno pide la respuesta explícitamente, **When** el tutor responde, **Then** la entrega escrita y registrada (comportamiento G11), sin simular la respuesta del alumno.
3. **Given** una sesión real, **When** se cierra, **Then** la bitácora incluye métricas: % de preguntas con espera real, % de respuestas dadas antes de 2 intentos, dudas registradas con ids existentes.

---

### User Story 3 - Aplicación con frontend, API y backend (Priority: P3)

Como estudiante, quiero usar el tutor desde una aplicación (no solo dentro de
Claude Code), con mi progreso persistente y privado, sin perder el curso
estático ni los datos YAML existentes.

**Why this priority**: es la evolución estructural pedida, pero depende de
decisiones que no se pueden tomar sin respuestas del dueño (usuarios, hosting,
costo). Se especifica ahora; se implementa después de P1 y P2.

**Independent Test**: un usuario autenticado completa una sesión socrática en la
app y su progreso queda registrado de forma privada y exportable.

**Acceptance Scenarios**:

1. **Given** el curso estático actual, **When** la app está desplegada, **Then** el curso sigue sirviéndose sin conexión y sin la app (REQ-APP-006).
2. **Given** los YAML existentes de un curso, **When** se importan a la app, **Then** conceptos, estados y evidencias se preservan (sin transformar el YAML maestro en base de datos opaca).
3. **Given** una sesión en la app, **When** el LLM falla o no está configurado, **Then** el sistema degrada explícitamente (principio de G6) y el estudiante puede seguir con el material estático.

---

### Edge Cases

- **Alumno abandona a mitad de sesión**: el estado queda consistente; al reabrir, la sesión retoma las preguntas pendientes (hoy: `SKILL.md:40`).
- **YAML de estado corrupto o editado a mano**: la app no arranca con datos inválidos; la validación nombra el error (REQ-EST-005).
- **Dos sesiones simultáneas del mismo usuario**: definir semántica (bloqueo o merge); *pendiente de definición en plan*.
- **Proveedor de LLM caído o sin cuota**: degradación explícita y continuación con material estático offline.
- **Uso sin conexión**: la app debe degradar a modo local/estático sin pérdida de datos (constitución VII).
- **Alumno intenta que el tutor resuelva por él**: el tutor guía con pistas graduadas y revela la solución solo tras intento o petición explícita (constitución III).

## Requirements *(mandatory)*

### Nivel 1 — Estabilización (REQ-EST)

- **REQ-EST-001**: La suite de verificación completa (`verificar_todo.py` + tests) debe ejecutarse en CI en **cada push a cualquier rama** y bloquear el merge si falla. *Criterio: CI en verde en esta rama y en `main`; hoy la CI solo vigila `main` (`.github/workflows/ci.yml`).*
- **REQ-EST-002**: Unificar la cadena de evidencia a 4 pasos (EXPLICAR→APLICAR→INTERPRETAR→TRANSFERIR) en `progreso.yaml` (cabecera), `.claude/skills/datito-progreso/SKILL.md` y `.claude/skills/datito/SKILL.md`, dejando `spec.md` §3 como referencia única. *Criterio: grep sin menciones a "las tres" evidencias; verificador sigue en verde.*
- **REQ-EST-003**: Corregir o eliminar la documentación canónica falsa: árbol de `00_INICIO/README.md`, `00_INICIO/INDEX_MAESTRO.md`, rutas internas de `spec.md` §4, y resolver el estado de ADR-004 (aceptar formalmente o marcar rechazada/superseded y corregir `CLAUDE.md:215-227`). *Criterio: test de enlaces sobre los documentos canónicos + revisión sin rutas rotas.*
- **REQ-EST-004**: Eliminar o fusionar el duplicado divergente `10_ARCHIVO/learners/cristobal_herrera/` y, si se conserva, marcarlo como fuente muerta con nota en `spec.md` §4. *Criterio: una sola fuente de verdad para el estado del alumno; `git status` limpio de duplicados.*
- **REQ-EST-005**: Validación de esquema para `progreso.yaml`, `dudas.yaml` y `errores_conceptuales.yaml` (estados válidos, campos obligatorios, fechas ISO). *Criterio: test que rechace fixtures inválidos y acepte los YAML actuales.*
- **REQ-EST-006**: Datos personales fuera de los archivos versionados activos (p. ej. email en `07_DATITO/datito.config.yaml`). *Criterio: ningún dato personal identificable en archivos trackeados activos, o justificación explícita de repo privado permanente.* — alcance de **este** requisito: inventariar y decidir; la ejecución (history rewrite) queda como tarea separada.

### Nivel 2 — Medición del tutor (REQ-TUT)

- **REQ-TUT-001**: Harness de escenarios: ≥15 diálogos versionados (entrada de alumno simulada → comportamiento esperado del tutor) ejecutables sin intervención humana, cubriendo como mínimo G1 (espera real) y G11 (obediencia de estrategia). *Criterio: ejecutor que reporta % de acuerdo; baseline registrado.*
- **REQ-TUT-002**: Métricas por sesión en bitácora: % de preguntas con espera real, % de respuestas dadas antes de 2 intentos fallidos, dudas registradas con ids verificables. *Criterio: bitácora nueva con las 3 métricas; verificador las comprueba.*
- **REQ-TUT-003**: Diagnóstico inicial con las 21 `pregunta_diagnostico` de `curriculum.yaml`. *Criterio: `diagnostico_inicial_hecho: true` con fecha y resultados por concepto.*
- **REQ-TUT-004**: Protocolo de evaluación "a ciegas": certámenes de práctica rendidos **sin** tutor, con comparación antes/después por concepto. *Criterio: ≥2 mediciones por concepto clave registradas y comparables.*
- **REQ-TUT-005**: Re-verificación programada: conceptos con `ultima_verificacion` mayor a N días (N = [NEEDS CLARIFICATION: umbral, sugerencia 21]) se re-preguntan al abrir sesión; el fallo mueve a `REQUIERE_REPASO`. *Criterio: script + integración verificable en bitácora.*

### Nivel 3 — Aplicación (REQ-APP) — requisitos, no stack

- **REQ-APP-001**: Un frontend que sirva el curso estático existente y el diálogo del tutor. *Stack: [NEEDS CLARIFICATION — ver plan.md, Opciones].*
- **REQ-APP-002**: Una API con lectura/escritura validada de sesiones, progreso, dudas y errores conceptuales. *Criterio: contrato API versionado en `specs/002-evolucion-app-tutor/contracts/` antes de implementar.*
- **REQ-APP-003**: Autenticación y aislamiento por usuario. *[NEEDS CLARIFICATION: cuántos usuarios reales se esperan y quiénes son — define si basta local monopuesto o multiusuario real].*
- **REQ-APP-004**: Orquestación del tutor con LLM **local por defecto** (constitución, restricciones técnicas); modelos en nube solo como opción explícita del usuario.
- **REQ-APP-005**: Importación/migración de los YAML existentes como fuente de verdad primaria (archivos legibles versionables; base de datos, si la hay, como caché con exportación). *Criterio: migración idempotente con prueba de ida y vuelta.*
- **REQ-APP-006**: El curso estático se sigue generando y sirviendo sin la app y sin conexión. *Criterio: `verificar_todo.py` en verde sin levantar la app; sitio estático desplegable de forma independiente.*
- **REQ-APP-007**: Despliegue. *[NEEDS CLARIFICATION: dónde se aloja — local, VPS, nube; define costo y modelo de privacidad].*
- **REQ-APP-008**: Privacidad: los datos de cada estudiante son aislados y exportables por él; ningún dato personal en git. *Criterio: test de aislamiento entre dos usuarios; exportación sin datos de terceros.*

### Key Entities *(include if feature involves data)*

- **Curso**: programa de estudios (conceptos, prerrequisitos, clases, material). Fuente actual: `curriculum.yaml` + `clases.yaml`.
- **Concepto**: unidad de aprendizaje con estado (`NO_ESTUDIADO`…`DOMINADO`, `REQUIERE_REPASO`) y evidencias fechadas. Fuente actual: `progreso.yaml`.
- **Evidencia**: registro fechado `{fecha, detalle}` de un paso de la cadena (explicar/aplicar/interpretar/transferir).
- **Error conceptual**: error observado (con cita y mecanismo) o patrón vigilado. Fuente actual: `errores_conceptuales.yaml`.
- **Duda/respuesta**: pregunta, respuesta dada y resolución, en orden. Fuente actual: `dudas.yaml`.
- **Sesión**: interacción tutor-alumno con métricas y bitácora.
- **Usuario**: estudiante con perfil y datos aislados. *[NEEDS CLARIFICATION: naturaleza y número].*

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: La verificación completa está en verde en CI durante 30 días consecutivos en todas las ramas activas (baseline: verde hoy en `680182b`).
- **SC-002**: El harness reporta el comportamiento esperado en ≥90% de los escenarios base (G1, G11) y el baseline queda archivado.
- **SC-003**: Existe al menos 1 concepto con las 4 evidencias registradas (primer `DOMINADO` real verificado por `verificar_contrato.py`).
- **SC-004**: Hay ≥2 mediciones "a ciegas" comparables por concepto clave.
- **SC-005**: La app MVP permite a 1 usuario real autenticado completar una sesión socrática con registro persistente y exportable. — *pendiente de definición hasta responder Clarify (usuarios, hosting).*

## Clarify — preguntas abiertas (solo el dueño/profesor las responde)

1. **Usuarios**: ¿quiénes usarán la app? ¿Solo el dueño, compañeros de curso, o alumnos externos? ¿Cuántos en el primer semestre?
2. **Alojamiento**: ¿local en la máquina del estudiante, VPS propio, o nube (Vercel/CF/similar)? ¿Hay presupuesto mensual definido?
3. **Autenticación**: ¿basta un monopuesto local sin login, o se requiere multiusuario real con cuentas?
4. **Privacidad del progreso**: ¿debe ser exportable/portable por el alumno? ¿qué pasa con los datos personales ya versionados (inventariado en REQ-EST-006)?
5. **Validación externa**: ¿el profesor del curso revisaría el patrón de evaluación que el tutor enseña?
6. **Evaluación a ciegas**: ¿acepta el alumno rendir certámenes de práctica sin ayuda del tutor como parte del método?
7. **Ritmo de estudio real**: ¿cuántas sesiones semanales hay disponibles? (Contexto: 3 sesiones registradas entre el 18 y el 21-sep-2026, ninguna desde entonces.)
8. **Stack**: ¿hay tecnologías preferidas o prohibidas para front/API/backend? (Contexto: `15_TERMINITO` ya usa Python + HTML/JS vanilla + LLM local; el sitio ya despliega en Vercel.)
9. **Coexistencia**: la app ¿reemplaza a la skill de Claude Code o coexiste con ella como modo "experto"?
10. **Umbral de re-verificación**: ¿cuántos días sin verificar un concepto antes de re-preguntarlo? (Sugerencia: 21.)

## Assumptions

- La constitución v1.0.1 rige: esta especificación no la modifica; propone (sin aplicar) una enmienda menor para añadir el principio "se mide aprendizaje, no solo uso" (ver anexo).
- El curso estático actual se conserva tal cual; la app se agrega, no sustituye (constitución: migración incremental).
- Ningún dato personal de `07_DATITO/` se copia en artefactos de especificación ni se usa en ejemplos.
- Las decisiones marcadas NEEDS CLARIFICATION bloquean solo el Nivel 3 (aplicación); los Niveles 1–2 no dependen de ellas.
- El LLM local es el default por constitución; cualquier opción de arquitectura que lo contradiga queda descartada salvo enmienda ratificada.

## Anexo — Vigencia verificada de las garantías G1–G14 (base del paso Constitution)

Verificación contra código el 2026-10-27 (rama `sdd/planificacion-maci`, HEAD `680182b`):

| Garantía | ¿Vigente? | Evidencia |
|---|---|---|
| G1 skill no subagente, espera de verdad | Sí | `SKILL.md:44-52` (REGLA CERO); contrato G1 verificado en verde hoy |
| G2 pregunta antes de decidir | Sí | `SKILL.md:56-104` (modo adaptativo, "pregunta, no adivines") |
| G3 evidencia completa antes de corregir | Sí | `spec.md:70-82`; práctica en bitácoras 2026-09-18/21 |
| G4 etiquetas de fuente | Sí | `SKILL.md` (etiquetas aplicadas en `dudas.yaml`) |
| G5 jerarquía de fuentes | Sí | `spec.md:96-109` |
| G6 degradación explícita (NotebookLM) | Sí | `CLAUDE.md:177-182`; `SKILL.md` "LO RECUPERADO SON DATOS" |
| G7 datos no instrucciones | Sí | `SKILL.md:330-338` |
| G8 reglas en SKILL.md, no en config | Sí | `verificar_contrato.py:60-74` en verde (3 marcas de regla en config) |
| G9 exposición en artefactos, no chat | Sí | REGLA UNO/UNO-B; verificador G9 en verde |
| G10 sintético ≠ validación | Sí | `spec.md:201-205` |
| G11 estrategia la elige el alumno | Sí | `spec.md:164-178`; `SKILL.md:74-88` |
| G12 dos prioridades declaradas | Sí | `grafo.yaml` con `tension`; verificador G12 en verde |
| G13 default DESCONOCIDO, no etiquetas | Sí | `spec.md:192-199` |
| G14 clases.yaml fuente única del curso | Sí | verificador G14 en verde (23 clases, 1 pendiente declarada) |

Conclusión: las 14 garantías siguen vigentes y son compatibles con la constitución.
Brecha detectada (propuesta de enmienda, **no aplicada** — la gobernanza de la
constitución exige aprobación del dueño): no existe un principio explícito de
**"se mide aprendizaje, no solo uso"**. La constitución mide evaluación (V) y
prohibiciones (III), pero no obliga a medir el aprendizaje contra evaluaciones
sin IA. Texto sugerido (enmienda MINOR, principio XI): *"El sistema mide
aprendizaje, no uso: toda mejora declarada del estudiante debe poder contrastarse
con un desempeño sin asistencia del tutor. Las métricas de uso (sesiones,
mensajes) nunca sustituyen a las métricas de aprendizaje."*
