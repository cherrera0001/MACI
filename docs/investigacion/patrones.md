# Patrones de diseño para MACI 1.0 — aprendizajes del estado del arte

**Fecha:** 2026-10-17
**Base:** hallazgos de `estado-del-arte.md` (mismas fuentes citadas). Cinco a ocho patrones a adoptar y tres antipatrones a evitar, cada uno con quién lo ejecuta bien y por qué importa para Termito.

---

## Patrones a adoptar

### 1. Tutoría socrática con "no" a la respuesta directa
**Quién lo hace bien:** Khanmigo (guía con preguntas en vez de soluciones), ChatGPT Study Mode (preguntas guía + andamiaje por secciones) y Claude Learning Mode ("¿cómo abordarías este problema?") ([rankncompare.com](https://www.rankncompare.com/tools/khanmigo), [openai.com](https://openai.com/index/chatgpt-study-mode/), [anthropic.com](https://www.anthropic.com/news/introducing-claude-for-education)).
**Por qué importa:** es el consenso pedagógico del mercado 2025-2026: el valor del tutor no es el contenido sino la lucha productiva que induce. Para Termito esto valida su bucle socrático y sugiere hacer explícita la política de "negarse a entregar la respuesta" como feature comunicable.

### 2. Grounding restricto en materiales del curso, con verificación
**Quién lo hace bien:** Jill Watson, que solo responde cuando hay material verificado del curso y chequea cada salida con entailment textual (accuracy 75-97% vs ~30% del assistant genérico); NotebookLM, que cita inline el pasaje exacto de la fuente ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748), [skywork.ai](https://skywork.ai/blog/doc/notebooklm-guide-2025-how-to-use-googles-ai-for-study-and-research)).
**Por qué importa:** son los dos extremos que Termito debe unir — la restricción dura de Jill (no responder sin evidencia) y la citabilidad de NotebookLM (timestamp por respuesta). El mercado demuestra que ambas son técnicamente viables; nadie las combina con tutoría socrática.

### 3. Pedagogía explícita basada en ciencia del aprendizaje, publicada y medida
**Quién lo hace bien:** Google con LearnLM — cinco principios pedagógicos, informes técnicos periódicos, RCT pre-registrado en Sierra Leona (percentil 50→64 en mates) y métricas de error factual (0,1%) ([cloud.google.com/solutions/learnlm](https://cloud.google.com/solutions/learnlm?hl=es-419)).
**Por qué importa:** la credibilidad de un tutor se construye publicando cómo enseña y midiendo efecto, no con claims de marketing. Termito debería documentar su marco pedagógico (grafo de prerrequisitos, distinciones conceptuales) y medir resultados desde el primer prototipo, aunque sea con n pequeño.

### 4. Evaluación formativa de respuesta abierta con feedback inmediato
**Quién lo hace bien:** Cognii, cuyo núcleo es que el estudiante responde con sus propias palabras y la IA evalúa comprensión en diálogo, no opción múltiple ([walturn.com](https://www.walturn.com/insights/top-20-genai-products-for-education), [meratutor.ai](https://www.meratutor.ai/lms/blog/5-best-ai-tutors-for-education-that-empower-self-learning-and-independent-study/)).
**Por qué importa:** valida la apuesta de MACI por evaluar "distinciones conceptuales" en lugar de repetición. El patrón concreto a copiar: pedir respuesta abierta → evaluar contra la distinción esperada → feedback que nombra el concepto confundido, todo en la misma conversación.

### 5. Calibración por nivel y metacognición, no solo por contenido
**Quién lo hace bien:** ChatGPT Study Mode calibra preguntas según objetivo y nivel del usuario, gestiona carga cognitiva con secciones y promueve auto-reflexión; Century Tech usa insights de neurociencia y alertas de intervención ([openai.com](https://openai.com/index/chatgpt-study-mode/), [century.tech](https://www.century.tech/)).
**Por qué importa:** el grafo de prerrequisitos de Termito debe alimentar no solo qué enseñar sino *cómo* preguntar: el mismo concepto se pregunta distinto según el nivel detectado, y el tutor verbaliza su estrategia ("noto que dominas X, tu brecha está en Y").

### 6. Proactividad: el tutor inicia, no solo responde
**Quién lo hace bien:** el rediseño 2026 de Khanmigo incluye "proactive tutor nudges" — el tutor empuja al estudiante en vez de esperar preguntas; los dashboards de Century disparan intervenciones del docente ([collegehobbies.com](https://collegehobbies.com/article/khanmigo-public-launch-july-2026/), [century.tech](https://www.century.tech/)).
**Por qué importa:** la lección dura de Khanmigo (solo 15% de uso con acceso disponible) muestra que un tutor pasivo muere de desuso. Termito debería planificar sesiones y retomar hilos pendientes ("seguimos con la distinción sesgo-varianza que quedó abierta") como comportamiento por defecto.

### 7. Medir adopción como métrica de producto, no solo aprendizaje
**Quién lo hace bien:** Khan Academy detectó el 15% de uso real y rediseñó el producto completo en 2026 en vez de defender el lanzamiento ([rctrl.com](https://rctrl.com/blog/aeo-edtech-ai-tutor-recommendations), [collegehobbies.com](https://collegehobbies.com/article/khanmigo-public-launch-july-2026/)).
**Por qué importa:** para un agente de un solo curso con fecha de muerte, la retención semanal del estudiante es la señal temprana de que la arquitectura del tutor está bien. Instrumentar uso desde el primer día es más barato que descubrir al final del semestre que nadie conversó con Termito.

### 8. Modos múltiples sobre un mismo motor pedagógico
**Quién lo hace bien:** Jotform AI Tutor ofrece practice/guided/contest; Duolingo Max separa Roleplay, Video Call y Explain My Answer sobre GPT-4 ([jotform.com/ai/ai-tutor](https://www.jotform.com/ai/ai-tutor/), [duoplanet.com](https://duoplanet.com/duolingo-max-review/)).
**Por qué importa:** el mismo grafo de prerrequisitos y banco de distinciones de Termito puede servir modos distintos (sesión socrática, autoevaluación, simulacro de certamen) sin reescribir el núcleo; el estudiante diseña el agente también eligiendo qué modos incluir en su ciclo de vida.

---

## Antipatrones a evitar

### 1. La máquina de respuestas: entregar la solución sin lucha productiva
**Evidencia:** Duolingo Max es criticado porque Explain My Answer puede alucinar o explicar la parte equivocada, y sus propias funciones no sustituyen interacción real; el reporte educativo de Anthropic encontró que casi la mitad de los chats universitarios buscaban respuestas directas, no aprendizaje ([duoplanet.com](https://duoplanet.com/duolingo-max-review/), [academyforeducationalstudies.org](https://academyforeducationalstudies.org/wp-content/uploads/2025/09/watkins-monroe-final-1.pdf)).
**Riesgo para Termito:** un modo "dame la respuesta" siempre disponible corrompe el contrato pedagógico en una sesión. Regla sugerida: la respuesta completa solo es accesible después de un intento del estudiante, y el tutor explica por qué.

### 2. Dependencia total de la nube
**Evidencia:** todos los competidores requieren conexión — Khanmigo, LearnLM/Guided Learning, ChatGPT Study Mode, Claude for Education, NotebookLM, Jotform; incluso Duolingo Max limita sus funciones AI a online aunque sus lecciones básicas tengan offline ([rankncompare.com](https://www.rankncompare.com/tools/khanmigo), [completeaitraining.com](https://completeaitraining.com/news/googles-free-gemini-ai-tutor-guided-learning-promises/), [talkpal.ai](https://talkpal.ai/how-much-is-duolingo-max-ultimate-pricing-guide-2025/)).
**Riesgo para Termito:** si Termito cede y adopta un backend en nube "por simplicidad", pierde su diferencial más barato de mantener. El patrón offline-first no es solo feature: es la única propuesta del mercado que garantiza que el tutor del curso sigue vivo sin conectividad (biblioteca, campus remoto, viaje).

### 3. Evaluación de repetición en vez de comprensión
**Evidencia:** Duolingo monetiza rachas y drills gamificados; Squirrel AI descompone todo en micro-puntos con muestreo repetitivo orientado a examen — y Riiid, pionero serio del knowledge tracing, terminó pivotando su negocio a Socra AI ([duoplanet.com](https://duoplanet.com/duolingo-max-review/), [time.com](https://time.com/collections/best-inventions-2025/7318298/squirrel-ai-intelligent-adaptive-learning-system/), [riiid.co](https://www.riiid.co/)).
**Riesgo para Termito:** caer en generar quizzes de "recuerda la fórmula" desde los materiales subidos. La apuesta de MACI — evaluar si el estudiante distingue conceptos que suelen confundirse (sesgo vs varianza, correlación vs causalidad) — es justo lo que el mercado no hace, y el pivote de Riiid sugiere que la vía puramente adaptativa sin comprensión no sostiene producto.
