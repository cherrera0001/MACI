# Feature Specification: MACI 1.0 — Plataforma de tutores agenticos personalizados (Datito)

**Feature Branch**: `001-datito-platform`

**Created**: 2026-10-17

**Status**: Draft

> **Nota de nombre (2026-10-18)**: "Datito" es el nombre oficial del producto
> (heredado de la v0.0.1 del curso); "Termito" fue el prototipo del ejemplo del
> profesor Parada Daza y así aparece en partes del historial. Este documento usa
> "Datito" en adelante; la rama real sigue siendo `001-termito-platform` y el
> código vive en `15_TERMINITO/src/datito/` (rename de producto, no de disco).

**Input**: User description: "MACI 1.0: plataforma para construir tutores agenticos personalizados ('Datito') diseñados por el propio estudiante a partir de los materiales reales de lo que quiere aprender. El estudiante crea un Datito por curso/materia. El prompt del agente se construye desde 8 componentes: (1) Rol y dominio, (2) Misión, (3) Funciones, (4) Estilo de enseñanza, (5) Contexto del curso, (6) Estilo de aprendizaje del estudiante, (7) Restricciones, (8) Relación temporal. Ingesta de materiales (PDFs, presentaciones, videos, evaluaciones pasadas, bibliografía, sitios web), constructor de identidad, diálogo continuo con memoria, evaluación adaptativa por distinciones, panel de dominio sobre grafo curricular, registro de dudas, exportación portable y familia de Datitos. Diferenciadores: el estudiante diseña el agente; materiales reales como fuente de verdad; evaluación por distinciones; ciclo de vida completo con retroalimentación de notas; 100% offline posible."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Construir un Datito desde los materiales reales del curso (Priority: P1)

Una persona que va a tomar un curso (universitario o de cualquier ámbito) reúne los
materiales reales del curso —programa, presentaciones, evaluaciones pasadas,
bibliografía, videos, sitios web— y los entrega al sistema. El sistema extrae y
estructura el contenido (texto, temas, referencias). Luego un asistente paso a paso le
ayuda a definir los 8 componentes del Datito (rol y dominio, misión, funciones, estilo
de enseñanza, contexto del curso, estilo de aprendizaje del estudiante, restricciones,
relación temporal). Al finalizar, el sistema genera el prompt del Datito, lo muestra
completo y editable, y el Datito queda listo para usar. Todo el proceso debe tomar
menos de 30 minutos de trabajo activo del estudiante.

**Why this priority**: es la puerta de entrada a toda la plataforma y el diferencial
central frente al mercado (nadie más deja al estudiante diseñar su agente). Sin esta
historia no existe producto.

**Independent Test**: se puede probar completamente entregando los materiales de un curso
real, completando el asistente de 8 componentes y verificando que el Datito resultante
conversa usando solo contenido de los materiales. Entrega valor: un tutor propio,
construido en <30 minutos.

**Acceptance Scenarios**:

1. **Given** un estudiante con los materiales de un curso real, **When** los sube al
   sistema, **Then** el sistema extrae el contenido, lo estructura y le muestra un
   resumen navegable de lo que "sabe" el Datito (con conteo de fuentes por tipo).
2. **Given** el contenido ya ingerido, **When** el estudiante completa el asistente de
   8 componentes, **Then** el sistema genera un prompt completo del Datito que refleja
   fielmente las decisiones del estudiante y se lo muestra íntegro para edición.
3. **Given** un Datito creado, **When** el estudiante edita cualquier componente,
   **Then** el cambio queda versionado y tiene efecto desde la siguiente interacción,
   sin necesidad de recrear el Datito.
4. **Given** materiales de baja calidad (PDF escaneado sin texto), **When** el
   estudiante los sube, **Then** el sistema lo advierte explícitamente y le indica qué
   fuentes quedaron sin extraer.

---

### User Story 2 - Conversar con el Datito con evidencia citada y lucha productiva (Priority: P1)

El estudiante conversa con su Datito para aprender: pide explicaciones, propone
respuestas a ejercicios, recibe correcciones. Cada afirmación del tutor enlaza a su
fuente en los materiales (lámina, transcripción con timestamp, sección bibliográfica).
Cuando el estudiante intenta un ejercicio, el tutor nunca entrega la respuesta final sin
antes proponer pistas graduadas y contraejemplos; revela la solución solo tras el
intento o si el estudiante la exige de forma explícita e informada. Cada duda resuelta
queda registrada con su procedimiento y su referencia al material fuente, y alimenta las
próximas conversaciones. La conversación es persistente: el Datito recuerda sesiones
previas, dudas resueltas y preferencias.

**Why this priority**: es la experiencia de uso cotidiana y concentra dos activos
intocables de MACI (evidencia citada, lucha productiva) más el registro de dudas.
Junto con US1 y US3 forma el núcleo del MVP.

**Independent Test**: se puede probar conversando con el Datito de un curso real y
verificando que (a) toda afirmación trae evidencia enlazada o una declaración de
ausencia de fuente, (b) ante un ejercicio nuevo el tutor ofrece pistas antes que la
solución, y (c) las dudas resueltas aparecen en un registro consultable.

**Acceptance Scenarios**:

1. **Given** una conversación abierta, **When** el Datito explica un concepto,
   **Then** cada afirmación muestra su evidencia (fuente + ubicación) o declara
   explícitamente que no tiene fuente en los materiales.
2. **Given** un ejercicio propuesto por el Datito, **When** el estudiante pide "dame
   la respuesta" sin haber intentado, **Then** el tutor ofrece una pista adicional y
   solicita un intento antes de revelar la solución.
3. **Given** un estudiante que responde mal un ejercicio, **When** el Datito corrige,
   **Then** la corrección enlaza a la evidencia que la sustenta y la duda queda
   registrada con su procedimiento de resolución.
4. **Given** una sesión terminada, **When** el estudiante vuelve días después,
   **Then** el Datito recuerda dudas previas y no vuelve a explicar lo ya dominado
   salvo petición.

---

### User Story 3 - Ser evaluado por distinciones conceptuales (Priority: P1)

El Datito evalúa al estudiante con ítems que exigen separar conceptos vecinos
(p. ej. "¿en qué se diferencia X de Y y cuándo usar cada uno?"), no repetir
definiciones. Las evaluaciones se generan desde los materiales y el grafo de
prerrequisitos, se adaptan al estado de dominio y miden comprensión, criterio y
capacidad de modelar problemas. El resultado actualiza el estado de dominio de los
nodos del grafo, que alimenta qué explicar y qué evaluar después.

**Why this priority**: es el segundo diferencial central (la evaluación por
distinciones no existe en el mercado) y cierra el ciclo pedagógico: el MVP exige "un
curso real evaluándose por distinciones".

**Independent Test**: se puede probar solicitando una evaluación sobre un tema del curso
y verificando que todos los ítems exigen discriminación entre conceptos próximos (no
recitación) y que el resultado se refleja en el panel de dominio.

**Acceptance Scenarios**:

1. **Given** un tema con conceptos vecinos en los materiales, **When** el estudiante
   pide evaluarse, **Then** el Datito genera ítems de distinción y califica con
   criterios explícitos derivados de los materiales.
2. **Given** una evaluación en curso, **When** el estudiante no logra distinguir dos
   conceptos, **Then** el Datito lo detecta y propone reforzar justamente esa frontera
   conceptual.
3. **Given** resultados de evaluación, **When** el estudiante abre su panel, **Then**
   ve el estado de dominio actualizado por concepto del curso.

---

### User Story 4 - Alimentar el ciclo de vida: notas como retroalimentación y cierre del curso (Priority: P1)

Durante el curso, el estudiante registra las notas/resultados de sus evaluaciones
reales y el Datito las usa como retroalimentación para ajustar su enseñanza (qué
reforzar, qué cambiar de estilo). Al terminar el curso, el Datito "desaparece": deja
de estar activo como agente, pero el estudiante conserva íntegro su registro —progreso,
dudas resueltas con su procedimiento, evaluaciones y evidencias— en archivos suyos y
portables.

**Why this priority**: completa el ciclo de vida completo que exige el MVP (nace,
evoluciona con retroalimentación, desaparece conservando el aprendizaje). Es la
manifestación directa del principio constitucional IV.

**Independent Test**: se puede probar registrando una nota baja real, verificando que el
Datito adapta su enseñanza, y luego cerrando el curso y confirmando que el registro
completo queda disponible y el Datito queda inactivo.

**Acceptance Scenarios**:

1. **Given** el estudiante registra una nota con observaciones, **When** la guarda,
   **Then** el Datito incorpora esa retroalimentación y ajusta próximos ejercicios y
   explicaciones.
2. **Given** un curso terminado, **When** el estudiante cierra el ciclo, **Then** el
   Datito queda inactivo y no genera nuevas interacciones como tutor activo.
3. **Given** un Datito cerrado, **When** el estudiante consulta su registro,
   **Then** accede al 100% de dudas resueltas, evaluaciones, progreso y evidencias.

---

### User Story 5 - Visualizar el dominio sobre el grafo de prerrequisitos (Priority: P2)

El estudiante ve un mapa del curso: nodos de conceptos conectados por prerrequisitos,
coloreados por estado de dominio (sin empezar, en progreso, dominado, con dudas
activas). Puede navegarlo, ver qué desbloquea qué y elegir dónde concentrarse.

**Why this priority**: el grafo ya existe en MACI v0.0.1 (`grafo.yaml`) y potencia la
evaluación adaptativa (US3), pero su visualización interactiva no es estrictamente
necesaria para el MVP.

**Independent Test**: se puede probar abriendo el mapa de un curso real y verificando
que el estado de dominio mostrado coincide con los resultados de las evaluaciones
realizadas en US3.

**Acceptance Scenarios**:

1. **Given** un curso con evaluaciones realizadas, **When** el estudiante abre el mapa,
   **Then** cada nodo muestra su estado de dominio consistente con esas evaluaciones.
2. **Given** un nodo con prerrequisitos, **When** el estudiante lo selecciona,
   **Then** ve qué conceptos lo anteceden y cuáles desbloquea.

---

### User Story 6 - Gestionar la familia de Datitos (Priority: P2)

El estudiante con varios cursos ve un panel con todos sus Datitos activos: uno por
curso/materia, cada uno con su propia identidad, materiales, grafo, progreso y ciclo de
vida independiente. Desde ahí crea nuevos Datitos, archiva los terminados y navega
entre ellos.

**Why this priority**: es el principio constitucional IX y escala el producto, pero el
MVP se demuestra con un solo Datito.

**Independent Test**: se puede probar con dos cursos reales, verificando que cada
Datito solo usa sus propios materiales y que archivar uno no afecta al otro.

**Acceptance Scenarios**:

1. **Given** un estudiante con dos Datitos, **When** abre el panel, **Then** ve ambos
   con su estado (activo, curso terminado) y progreso resumido.
2. **Given** dos Datitos activos, **When** pregunta a cada uno sobre su curso,
   **Then** cada respuesta usa exclusivamente los materiales de su propio curso.

---

### User Story 7 - Exportar y portar un curso completo (Priority: P3)

El estudiante exporta un curso completo (materiales, Datito, progreso, dudas, grafo)
como paquete portable y lo abre en otro dispositivo, donde funciona offline sin pérdida
de historial.

**Why this priority**: garantiza la soberanía de datos (principio VII) y es coherente
con el diseño offline-first, pero se puede demorar sin comprometer el MVP.

**Independent Test**: se puede probar exportando un curso con historial, abriéndolo en
otro dispositivo sin red y verificando que conversación, dudas y dominio están íntegros.

**Acceptance Scenarios**:

1. **Given** un curso con historial, **When** el estudiante lo exporta, **Then**
   obtiene un paquete autocontenido que incluye materiales, Datito, progreso y dudas.
2. **Given** el paquete en otro dispositivo, **When** lo abre sin conexión,
   **Then** el Datito conversa y muestra el progreso completo.

---

### Edge Cases

- Materiales sin texto extraíble (PDF escaneado, video sin transcripción): el sistema
  advierte qué quedó fuera y ofrece caminos (transcripción manual, omisión explícita).
- Pregunta del estudiante fuera del alcance de los materiales: el tutor declara que no
  tiene fuente y no inventa; puede ofrecer responder claramente marcado como
  "fuera del curso".
- Estudiante que insiste en obtener la respuesta sin intentar: el tutor revela tras una
  advertencia informada y registra la excepción.
- Modelo de lenguaje local no disponible o no instalado: el sistema indica cómo
  habilitarlo y queda en modo "exploración de materiales" (sin tutor) hasta entonces.
- Edición del prompt que rompe el comportamiento esperado: el sistema ofrece volver a
  cualquier versión previa del prompt (versionado).
- Cierre de curso por accidente: el cierre requiere confirmación y queda reversible por
  un período.
- Dos Datitos con materiales solapados: cada uno sigue usando solo sus propios
  materiales; no hay mezcla de evidencias.

## Requirements *(mandatory)*

### Functional Requirements

**Construcción del Datito (US1)**

- **FR-001**: El sistema MUST aceptar materiales de un curso en formatos documento
  (PDF, presentaciones), video, texto y referencias web, y extraer de ellos contenido
  estructurado con su origen identificable.
- **FR-002**: El sistema MUST presentar al estudiante un resumen de la ingesta (fuentes
  procesadas, contenido extraído por fuente, advertencias de lo no extraíble) antes de
  construir el Datito.
- **FR-003**: El sistema MUST guiar al estudiante en la definición de los 8 componentes
  del Datito: rol y dominio, misión, funciones, estilo de enseñanza, contexto del
  curso, estilo de aprendizaje del estudiante, restricciones y relación temporal.
- **FR-004**: El sistema MUST generar el prompt completo del Datito a partir de los 8
  componentes y mostrarlo íntegro y editable al estudiante.
- **FR-005**: El estudiante MUST poder editar el prompt de su Datito en cualquier
  momento; cada versión MUST quedar registrada y reversible.
- **FR-006**: El proceso de creación de un Datito funcional MUST tomar menos de 30
  minutos de trabajo activo del estudiante con materiales ya reunidos.

**Diálogo con evidencia y lucha productiva (US2)**

- **FR-007**: Toda afirmación del tutor sobre el contenido del curso MUST enlazar a su
  fuente en los materiales o declarar explícitamente la ausencia de fuente.
- **FR-008**: El tutor MUST ofrecer pistas y guía socrática antes de revelar la
  solución de un ejercicio, y solo puede revelarla tras un intento del estudiante o una
  petición explícita e informada de éste.
- **FR-009**: El sistema MUST mantener memoria de la conversación: dudas resueltas,
  temas explicados, preferencias de estilo y resultados de ejercicios previos.
- **FR-010**: Cada duda resuelta MUST quedar registrada con su procedimiento de
  resolución y la referencia al material fuente que la sustenta.
- **FR-011**: Cuando una pregunta no tiene respaldo en los materiales, el tutor MUST
  declararlo; si responde desde conocimiento general, MUST marcarla visiblemente como
  fuera del curso.

**Evaluación por distinciones (US3)**

- **FR-012**: El sistema MUST generar ítems de evaluación que exijan distinguir
  conceptos vecinos o casos límite, derivados de los materiales y del grafo de
  prerrequisitos.
- **FR-013**: La calificación MUST usar criterios explícitos derivados de los
  materiales y MUST producir retroalimentación que identifique la frontera conceptual
  fallada.
- **FR-014**: Los resultados de evaluación MUST actualizar el estado de dominio de los
  conceptos del curso.

**Ciclo de vida (US4)**

- **FR-015**: El estudiante MUST poder registrar notas y observaciones de evaluaciones
  reales, y el Datito MUST usarlas para ajustar su enseñanza.
- **FR-016**: Al terminar el curso, el Datito MUST quedar inactivo y el estudiante
  MUST conservar íntegro su registro (progreso, dudas, evaluaciones, evidencias).

**Grafo (US5) y familia (US6)**

- **FR-017**: El sistema MUST visualizar el grafo de prerrequisitos del curso con el
  estado de dominio por nodo, consistente con las evaluaciones.
- **FR-018**: El sistema MUST permitir gestionar múltiples Datitos independientes
  (uno por curso), sin compartir materiales, evidencias ni estado entre ellos.

**Portabilidad (US7)**

- **FR-019**: El sistema MUST poder exportar un curso completo (materiales, Datito,
  progreso, dudas, grafo) como paquete portable y reabrirlo en otro dispositivo
  funcionando sin conexión.

**Transversales**

- **FR-020**: Todo el ciclo de uso (construir, conversar, evaluar, registrar notas,
  consultar progreso) MUST funcionar sin conexión a internet.
- **FR-021**: Todos los datos del estudiante MUST permanecer en su máquina en archivos
  legibles y versionables (no en un almacenamiento opaco).
- **FR-022**: Las interfaces del sistema MUST estar disponibles en español e inglés, y
  el contenido generado por el Datito MUST respetar el idioma que el estudiante use.

### Key Entities *(include if feature involves data)*

- **Curso**: unidad de aprendizaje del estudiante; agrupa materiales, grafo, Datito y
  registro. Atributos: nombre, período, estado (activo/cerrado).
- **Material/Fuente**: documento, video o referencia aportada por el estudiante.
  Atributos: tipo, identificador, contenido extraído, ubicaciones direccionables
  (página, timestamp).
- **Datito**: el agente tutor de un curso. Atributos: los 8 componentes, prompt
  versionado, estado (activo/inactivo).
- **Evidencia**: referencia direccionable a una parte de un Material que sustenta una
  afirmación del tutor.
- **Sesión/Mensaje**: interacción conversacional persistente.
- **Duda**: pregunta del estudiante resuelta; atributos: procedimiento de resolución,
  evidencia de respaldo, estado.
- **Ítem de distinción**: pregunta de evaluación que exige separar conceptos vecinos;
  atributos: conceptos involucrados, criterios de calificación, resultado.
- **Concepto/Nodo de grafo**: unidad del temario con prerrequisitos; atributos:
  estado de dominio, relaciones.
- **Retroalimentación de nota**: resultado real de evaluación aportado por el
  estudiante; alimenta la adaptación del Datito.
- **Paquete portable**: exportación autocontenida de un curso completo.

## Análisis competitivo y alcance del MVP *(Fase 0)*

**Fuentes**: investigación completa en `docs/investigacion/estado-del-arte.md` (12
competidores, 2024–2026, con URLs por dato) y patrones en
`docs/investigacion/patrones.md` (8 patrones a adoptar, 3 antipatrones a evitar).

### Síntesis del mercado

Ningún competidor permite que el propio estudiante arquitecte su agente desde los
materiales reales de su curso. Jill Watson (Georgia Tech) groundea en el curso pero la
base de conocimiento la construye un equipo docente; Khanmigo, Duolingo Max, Squirrel
AI y Century Tech traen currículo propio; LearnLM, ChatGPT Study Mode y Claude for
Education son capas pedagógicas genéricas en nube; NotebookLM cita los materiales del
estudiante pero para resumirlos, no para enseñar con lucha productiva; Jotform convierte
un archivo en quizzes sin teoría pedagógica. **El mercado ofrece consumo; Datito
ofrece arquitectura del aprendizaje.**

### Paridad — features que deben existir para ser credible (todas cubiertas por US1–US5)

| Paridad de mercado | Quién lo establece | Dónde vive en este spec |
|---|---|---|
| Tutoría socrática que se niega a dar la respuesta directa | Khanmigo, ChatGPT Study Mode, Claude Learning Mode | US2 + FR-008 (con enforce determinista, research R4) |
| Grounding restricto en materiales del curso con citas verificables | Jill Watson (responde solo con material validado) + NotebookLM (citas inline al pasaje) | US2 + FR-007/FR-011 + research R5 |
| Evaluación formativa de respuesta abierta con feedback inmediato | Cognii | US3 + FR-012/FR-013 |
| Calibración por nivel y estado de dominio | ChatGPT Study Mode, Century Tech | US3 + FR-014 + grafo en US5 |
| Panel de progreso visible | Century Tech, dashboards Khanmigo | US5 |
| Construcción de tutor desde archivos propios | Jotform AI Tutor, NotebookLM | US1 (superado: 8 componentes pedagógicos, no solo "sube un archivo") |

### Diferenciadores — lo que ningún competidor cubre (núcleo del MVP)

1. **Diseño del agente por el estudiante** (principio I): los 8 componentes visibles y
   editables en cualquier momento. Nadie en el mercado lo ofrece: o el agente es de la
   plataforma o es un archivo subido.
2. **Evidencia citada con referencia direccionable** (principio II): timestamp/página
   verificable con un clic, como estructura del sistema y no como promesa del modelo.
3. **Evaluación por distinciones conceptuales** (principio V): separar conceptos
   vecinos, no recitar. El pivote de Riiid (knowledge tracing puro → Socra AI) sugiere
   que la vía adaptativa sin comprensión no sostiene producto.
4. **100% offline** (principio VII): ningún competidor funciona sin conexión.
5. **Ciclo de vida del agente** (principio IV): nace, evoluciona con notas reales y
   muere con el curso, conservando el registro del estudiante.
6. **Multilenguaje nativo** (principio VIII): el mercado es anglocéntrico; el español
   es idioma primero de Datito.

### Fuera del MVP (explícito)

- Proactividad del tutor ("nudges" que retoman hilos pendientes) y modos múltiples
  sobre el mismo motor (simulacro de certamen, autoevaluación rápida): patrones 6 y 8
  de `patrones.md`, candidatos naturales de la primera versión post-MVP porque el grafo
  y el banco de distinciones ya los soportan.
- Aplicaciones móviles nativas, multi-usuario/aula con roles docentes, analítica
  agregada institucional e integración LMS.
- Instrumentación de adopción (patrón 7): se diseña desde el MVP (contadores de
  sesiones ya existen en el registro) pero su tablero es post-MVP.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Un estudiante con los materiales reunidos construye un Datito funcional
  en menos de 30 minutos de trabajo activo.
- **SC-002**: El 100% de las afirmaciones del tutor sobre el curso llevan evidencia
  enlazada o una declaración explícita de ausencia de fuente (medido en auditoría de
  sesiones).
- **SC-003**: Cero revelaciones de solución antes del intento del estudiante en
  ejercicios de práctica (medido en sesiones observadas).
- **SC-004**: El ciclo completo de uso —construir, conversar, evaluarse, registrar
  notas, consultar progreso— funciona con la red desconectada, sin degradación de
  funcionalidad.
- **SC-005**: Tras cerrar un curso, el 100% del registro del estudiante (dudas,
  evaluaciones, progreso, evidencias) permanece consultable y portable.
- **SC-006**: Las interfaces y el contenido del Datito están disponibles en español y
  inglés desde el lanzamiento del MVP.
- **SC-007**: El curso real migrado desde MACI v0.0.1 conserva el 100% de sus
  funcionalidades actuales (trazabilidad, grafo, registro de dudas, offline) sin
  regresiones detectables por su verificación automatizada.
- **SC-008**: Una edición del prompt por parte del estudiante tiene efecto desde la
  siguiente interacción y es reversible a cualquier versión anterior.

## Assumptions

- **Idioma primero**: el producto se construye en español; el inglés se incluye desde
  el diseño pero puede llegar como segunda interfaz en el MVP.
- **Modelo de lenguaje local por defecto**: el sistema opera con un modelo ejecutado en
  la máquina del estudiante; el uso de modelos en nube será una opción explícita y
  configurable, nunca obligatoria (decisión documentada: coherencia con principio VII).
- **Un Datito = un curso = un directorio autocontenido**: materiales, prompt, grafo,
  registro y progreso viven juntos y son portables por diseño (decisión documentada:
  simplifica US6 y US7).
- **Curso de referencia**: el curso actual de MACI v0.0.1 (Fundamentos de Ciencia de
  Datos, con su `clases.yaml`, `grafo.yaml`, visuales y bitácoras) se migra como primer
  Datito real y criterio de aceptación del MVP (SC-007).
- **El prompt del Datito es siempre visible**: no hay configuración opaca del agente;
  todo componente es legible y editable (principios I y X).
- **Versionado del prompt**: cada Datito conserva el historial de versiones de su
  prompt en archivos dentro de su directorio.
- **Tests en el backlog**: la constitución exige tests para nueva lógica; se incluirán
  tareas de test en tasks.md aunque el spec no las detalle.
- **Fuera del MVP**: aplicaciones móviles nativas, uso multi-usuario/aula con roles de
  docente, analítica agregada para instituciones e integración con LMS institucionales.
