<!--
SYNC IMPACT REPORT — 2026-10-17
- Version change: (sin versión previa, template sin rellenar) → 1.0.0
- Modified principles: ninguna (adopción inicial; 10 principios nuevos I–X)
- Added sections: "Restricciones Técnicas y de Datos", "Flujo de Trabajo de Desarrollo", "Governance"
- Removed sections: ninguna
- Deferred TODOs: ninguno. Todos los placeholders reemplazados.
- Nota: ratificación 2026-10-17 aprobada explícitamente por el dueño del proyecto en la
  solicitud que ordenó crear esta constitución (10 principios indicados como obligatorios).
-->

# MACI Constitution

## Core Principles

### I. El estudiante diseña el agente (soberanía del diseño)
El sistema facilita la construcción del tutor; NUNCA impone un agente genérico. El
estudiante define rol, misión, funciones, estilo, contexto, restricciones y relación
temporal de su Datito, y puede editar cualquiera de estos componentes en cualquier
momento. Rationale: según Víctor Parada, el estudiante diseña su propio proceso de
aprendizaje; un agente impuesto por plataforma convierte al estudiante en consumidor.

### II. Evidencia citada o silencio (trazabilidad)
Toda afirmación del tutor debe enlazar a su fuente en los materiales del curso (lámina,
transcripción con timestamp, sección de bibliografía o evaluación). Si no existe fuente,
el tutor debe declararlo explícitamente en vez de responder sin respaldo. Rationale: la
credibilidad del tutor depende de la verificabilidad; una respuesta sin fuente es opinión
del modelo, no enseñanza.

### III. Lucha productiva (nunca la respuesta sin intento)
El tutor nunca entrega la respuesta final de un ejercicio antes de que el estudiante
intente resolverlo. Debe guiar con preguntas socráticas, pistas graduadas y contraejemplos,
y revelar la solución solo después del intento del estudiante o cuando el estudiante lo
exija de manera explícita e informada. Rationale: el aprendizaje profundo exige esfuerzo
desirable; el tutor que resuelve por el estudiante lo deshabilita.

### IV. Ciclo de vida del agente (nacimiento, evolución, desaparición)
Todo Datito nace al iniciarse el aprendizaje de un curso, evoluciona con la
retroalimentación continua del estudiante (notas de evaluaciones, dudas, preferencias) y
desaparece cuando el curso termina. Al desaparecer, el estudiante conserva su conocimiento
y su registro de progreso y dudas resueltas. Rationale: el agente es un andamiaje temporal
(ZPD); si no desaparece, se convierte en muleta, no en medio.

### V. Evaluación por distinciones (no repetición)
El sistema evalúa la capacidad del estudiante de separar conceptos vecinos y distinguir
casos límite, no de repetir definiciones. La evaluación mide comprensión, criterio y
capacidad de modelar problemas. Rationale: reproducir contenido es señal débil de
aprendizaje; la discriminación entre conceptos próximos evidencia comprensión real y no
puede simularse con memoria.

### VI. Materiales del curso como fuente de verdad absoluta
Los materiales reales del curso (programa, presentaciones, evaluaciones pasadas,
bibliografía, videos) son la única fuente de verdad. El modelo de lenguaje NUNCA inventa
información sobre el curso: si algo no está en los materiales, el tutor lo dice. Rationale:
la alucinación en contexto educativo es dañina y erosiona la confianza; el contrato es
que el Datito solo sabe lo que los materiales sostienen.

### VII. Offline-first y soberanía de datos
Todo el ciclo de aprendizaje debe funcionar sin conexión: diálogo, evaluación, grafo y
registro de dudas. Los datos del estudiante (progreso, conversaciones, dudas, notas)
permanecen en su máquina en archivos que él controla. La nube es opcional y nunca
requerida para operar. Rationale: la dependencia de red es una falla de diseño para
estudiantes con conectividad limitada y una amenaza de privacidad para todos.

### VIII. Multilenguaje desde el diseño
Las interfaces, los contenidos generados y el propio prompt del agente deben soportar
cualquier idioma desde la arquitectura, no como traducción posterior. El español es el
idioma primero del producto. Rationale: el mercado de tutores IA está dominado por el
inglés; multilenguaje nativo es ventaja estructural, no cosmética.

### IX. Familia de agentes independientes
El estudiante puede tener múltiples Datitos (uno por curso o materia), cada uno con su
propia identidad, materiales, grafo, progreso y ciclo de vida. Ningún Datito comparte
estado con otro salvo decisión explícita del estudiante. Rationale: el conocimiento está
compartimentado por disciplina; un tutor monolítico mezcla contextos y degrada la
precisión de la evidencia.

### X. Personalización radical del estilo de aprendizaje
El agente se adapta al estilo del estudiante: intuitivo vs. formal, paso a paso vs.
desafío directo, texto vs. ejemplos vs. imágenes. La personalización es observable y
editable por el estudiante, no un perfil opaco. Rationale: la adaptación al estilo es la
promesa central de un tutor personal; si el estudiante no puede verla ni cambiarla, no
existe.

## Restricciones Técnicas y de Datos

- Migración incremental desde el sitio estático v0.0.1; NUNCA reescritura big-bang. Cada
  incremento debe dejar el sistema operativo y verificable.
- Estado, evidencias, grafo y progreso se almacenan en archivos versionables
  (YAML/Markdown/JSON) legibles por humanos; las bases de datos opacas están prohibidas
  como almacenamiento primario.
- El modelo de lenguaje se ejecuta local por defecto; el uso de modelos en nube debe ser
  una opción explícita del estudiante, nunca obligatoria ni silenciosa.
- Los secretos y credenciales NUNCA se versionan; viven en `.env` (ignorado) en la máquina
  del usuario.
- Todo contenido del producto se escribe en español salvo decisión explícita en contrario.
- Los agentes v0.0.1 intocables como propósito (trazabilidad, grafo, taxonomía Bloom,
  distinciones, registro de dudas, offline, materiales como fuente de verdad) se conservan
  y se extienden; ningún incremento puede debilitarlos.

## Flujo de Trabajo de Desarrollo

- Toda feature sigue el ciclo Spec Kit: `/speckit-specify` → `/speckit-plan` →
  `/speckit-tasks` → `/speckit-implement`, con `/speckit-analyze` para consistencia cruzada
  antes de implementar.
- Ninguna tarea de implementación se ejecuta sin `spec.md`, `plan.md` y `tasks.md`
  completos y consistentes entre sí.
- Las violaciones a esta constitución detectadas durante el flujo se corrigen en el
  diseño o se elevan al dueño del proyecto con justificación escrita; no se ignoran.
- Antes de publicar el curso, `verificar_todo.py` y la suite de tests deben estar en verde.
- Toda definición de hecho (PR) exige: tests verdes, documentación actualizada y
  cumplimiento explícito de los principios I–X.

## Governance

Esta constitución tiene precedencia sobre cualquier otra práctica del repositorio. Las
enmiendas requieren: (1) justificación escrita, (2) aprobación del dueño del proyecto,
(3) incremento de versión según semántica: MAJOR si se elimina o redefine un principio,
MINOR si se agrega un principio o sección, PATCH si es clarificación o redacción. Todo PR
debe verificar el cumplimiento de los principios I–X y de las restricciones técnicas; la
duda se resuelve a favor de la constitución. El compliance se revisa al inicio de cada
fase del flujo Spec Kit y al cierre de cada MVP.

**Version**: 1.0.1 | **Ratified**: 2026-10-17 | **Last Amended**: 2026-10-18

> **Nota de nombre (2026-10-18)**: "Datito" es el nombre oficial del producto,
> heredado de la v0.0.1 del curso. "Termito" fue solo el nombre del prototipo
> tomado del ejemplo del profesor Parada Daza (termodinámica); el MVP lo adoptó
> provisionalmente y hoy se unifica todo a "Datito". Quedan con el nombre viejo,
> por no romper rutas ni historial: el directorio `15_TERMINITO/`, la rama
> `001-termito-platform` y los reportes históricos.
