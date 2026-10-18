# Estado del arte: tutores de IA (2024–2026)

**Fecha:** 2026-10-17 (estrategia) · **Actualización:** 2026-10-17 (capa de evidencia técnica REA en `rea-evidencia/`)
**Contexto:** investigación competitiva para MACI 1.0 / "Termito", plataforma personal de tutoría con IA en la que el estudiante construye su propio agente tutor a partir de los materiales reales de su curso (programa, presentaciones, evaluaciones pasadas, bibliografía, videos). Diferenciales evaluados en cada competidor: diseño del agente por el estudiante, uso de materiales propios, evidencia citada en cada respuesta, grafo de prerrequisitos, evaluación por distinciones conceptuales, modo offline y ciclo de vida del agente (muere al terminar el curso).

**Capa de evidencia:** este documento es el análisis estratégico (fuentes públicas citadas). La evidencia técnica de implementación real (ingeniería inversa con REA: DOM, trazas de red, screenshots) vive en `rea-evidencia/` (khan.md, duolingo.md, century.md y `sintesis-arquitectura.md`). Donde un dato de esta ficha se contradiga con la evidencia REA, manda la evidencia REA.

Regla de citación: cada dato lleva la URL de su fuente. Cuando un dato no pudo confirmarse, se indica **"no verificado"**.

---

## 1. Georgia Tech — Jill Watson / AI-TA

- **Modelo de tutoría:** asistente docente virtual (TA) que responde preguntas de los estudiantes en foros tipo Piazza y en chat. Primera versión (2016) sobre IBM Watson; iteraciones con Google BERT (2019); versión actual integra ChatGPT pero **restringe las salidas a material validado del curso** y verifica cada respuesta con entailment textual. Arquitectura: base de conocimiento preprocesada + memoria MongoDB + pipeline que clasifica preguntas, recupera contenido relevante y modera respuestas; solo responde cuando hay material verificado suficiente ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748)). El agente maneja la rutina; el humano (profesor/equipo del curso) diseña el curso y la base de conocimiento.
- **¿Diseño por el estudiante?** No. Lo despliegan el DILab de Georgia Tech, el instituto NSF AI-ALOE y la editorial asociada (Wiley); el estudiante solo lo consume ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748)).
- **¿Materiales propios del curso?** Sí, es su núcleo: syllabus, Q&A históricos del foro, courseware, libros de texto y transcripciones de video del curso ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748)).
- **Evaluación integrada:** no evalúa al estudiante; la evaluación publicada es del sistema (accuracy 75–97% según fuente de contenido, frente a ~30% del Assistant de OpenAI; experimento A/B: más notas A, 66% vs 62%, y menos C, 3% vs 7%, en el curso OMSCS de IA con +600 estudiantes) ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748)).
- **Evidencia/citación:** respuestas *grounded* en material validado del curso, pero citación explícita con referencia navegable por respuesta: **no verificado** en el sentido que usa MACI.
- **Offline vs nube:** infraestructura propia institucional (MongoDB + pipeline); despliegue 100% offline del lado estudiante: **no verificado**.
- **Idiomas:** inglés (cursos desplegados en inglés) ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748)).
- **Precio/acceso:** no comercial; despliegue institucional (Georgia Tech OMSCS, Wiregrass Georgia Technical College; colaboración con John Wiley & Sons para escalar a cientos/miles de cursos) ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748)).
- **Debilidad más clara:** depende de que un equipo de curso construya y mantenga la base de conocimiento; no escalable ni configurable por el propio estudiante, y los resultados sobre presencia cognitiva (pensamiento crítico) siguen inconclusos ([ai.gatech.edu](https://ai.gatech.edu/taxonomy/term/748)).

## 2. Khan Academy — Khanmigo

- **Modelo de tutoría:** tutor conversacional socrático 24/7 + asistente docente. Guía al estudiante con preguntas en vez de dar la solución; integrado a la biblioteca de contenidos de Khan Academy (mates, ciencias, humanidades, código); incluye Writing Coach y herramientas de planificación para docentes ([rankncompare.com](https://www.rankncompare.com/tools/khanmigo), [is4.ai](https://is4.ai/blog/our-blog-1/top-10-ai-tutoring-systems-2026-learning-outcomes-208)).
- **¿Diseño por el estudiante?** No; personalización limitada según comportamiento del usuario.
- **¿Materiales propios del curso?** No; anclado al contenido cerrado de Khan Academy ([rankncompare.com](https://www.rankncompare.com/tools/khanmigo)).
- **Evaluación integrada:** práctica adaptativa y dashboards docentes; no hay evaluación documentada por distinciones conceptuales (**no verificado**).
- **Evidencia/citación:** "grounded in Khan Academy content", pero sin citas explícitas de fuente por respuesta (**no verificado**).
- **Offline vs nube:** nube; modo offline **no verificado**.
- **Idiomas:** principalmente inglés; hay despliegues localizados con contenido adaptado (p. ej. Pakistán) ([khanacademypakistan.org](https://khanacademypakistan.org/_us_news/khan-academy-pakistan-launched-brings-ai-powered-tutor-khanmigo-to-country/)). Soporte oficial de Khanmigo en español: **no verificado**.
- **Precio/acceso:** US$4/mes o US$44/año para estudiantes/padres (mayores de 18, EE.UU.); gratis para docentes K-12 verificados; licenciamiento por distrito escolar ([blog.khanacademy.org](https://blog.khanacademy.org/khanmigo-lite?37=), [edisonos.com](https://www.edisonos.com/alternatives/khan-academy-pricing), [rankncompare.com](https://www.rankncompare.com/tools/khanmigo)).
- **Debilidad más clara:** adopción real baja — solo ~15% de los estudiantes con acceso lo usaban regularmente (dato interno citado en 2025-2026) — lo que obligó a un rediseño completo con relanzamiento público en julio 2026 ([rctrl.com](https://rctrl.com/blog/aeo-edtech-ai-tutor-recommendations), [collegehobbies.com](https://collegehobbies.com/article/khanmigo-public-launch-july-2026/)); además, no trabaja sobre el material real del curso del estudiante.

## 3. Duolingo — Duolingo Max

- **Modelo de tutoría:** capa premium de IA (GPT-4) sobre la app gamificada de idiomas: Roleplay (conversación por texto con personajes), Video Call (llamada con el personaje Lily, desde 2024) y Explain My Answer (explicaciones de errores aciertos) ([duoplanet.com](https://duoplanet.com/duolingo-max-review/), [techcrunch.com](https://techcrunch.com/2023/03/14/duolingo-launches-new-subscription-tier-with-access-to-ai-tutor-powered-by-gpt-4/)). El agente practica conversación; el humano sigue la ruta de lecciones.
- **¿Diseño por el estudiante?** No.
- **¿Materiales propios del curso?** No; currículo propio de Duolingo.
- **Evaluación integrada:** quizzes de lección y reportes de Roleplay/Video Call con feedback; evaluación centrada en práctica y repetición, no en distinciones conceptuales.
- **Evidencia/citación:** no; Explain My Answer puede alucinar o explicar la parte equivocada (admitido en revisiones) ([duoplanet.com](https://duoplanet.com/duolingo-max-review/)).
- **Offline vs nube:** lecciones básicas con modo offline (Super), pero las funciones AI requieren conexión ([talkpal.ai](https://talkpal.ai/how-much-is-duolingo-max-ultimate-pricing-guide-2025/)).
- **Idiomas:** funciones completas en cursos español/francés para angloparlantes (iOS; Android parcial); parcial en alemán, italiano, portugués, japonés, coreano, chino ([duoplanet.com](https://duoplanet.com/duolingo-max-review/)).
- **Precio/acceso:** desde US$14/mes con plan anual (US$168/año) o US$30/mes mensual en EE.UU.; Family Plan ~US$200/año ([duoplanet.com](https://duoplanet.com/duolingo-max-review/)).
- **Debilidad más clara:** precio alto (doble que Super) por solo 3 funciones AI, disponibilidad limitada por plataforma/curso, y reconocimiento abierto de que no sustituye interacción humana ni logra fluidez por sí solo ([duoplanet.com](https://duoplanet.com/duolingo-max-review/)).

## 4. Century Tech

- **Modelo de tutoría:** plataforma adaptativa para escuelas (primaria, secundaria y post-16) que combina IA, ciencia del aprendizaje y neurociencia: miles de videos y preguntas con auto-corrección, rutas personalizadas por estudiante, y dashboards para docentes y apoderados con alertas de intervención ([century.tech](https://www.century.tech/), [sites.psu.edu](https://sites.psu.edu/leapforpit/artificial-intelligence/century-tech/)). El agente personaliza y marca; el docente interviene con los insights.
- **¿Diseño por el estudiante?** No; la configuran escuelas y docentes.
- **¿Materiales propios del curso?** Parcial — el contenido base es propio de Century; hasta qué punto un docente puede cargar su propio material de curso: **no verificado** en detalle.
- **Evaluación integrada:** sí — auto-marcación continua, diagnósticos y métricas de progreso en tiempo real ([century.tech](https://www.century.tech/), [g2.com](https://www.g2.com/products/century-tech/reviews)).
- **Evidencia/citación:** **no verificado** (no documentada).
- **Offline vs nube:** nube/SaaS; modo offline **no verificado**.
- **Idiomas:** inglés como idioma principal; usada en más de 70 países ([century.tech](https://www.century.tech/)); soporte multilingüe real: **no verificado**.
- **Precio/acceso:** licenciamiento institucional B2B; cifra pública **no verificado**.
- **Debilidad más clara:** modelo institucional cerrado: el estudiante individual no puede acceder ni configurar nada, y la lógica de personalización es una caja negra sin publicación técnica comparable a los informes de LearnLM o Jill Watson.

## 5. Squirrel AI

- **Modelo de tutoría:** tutoría adaptiva 1-a-1 basada en su "large adaptive model" (LAM): descompone materias en miles de micro-puntos de conocimiento, rastrea brechas y patrones cognitivos, y sirve el siguiente problema en tiempo real; operación híbrida con centros físicos propios donde maestros humanos apoyan ([time.com](https://time.com/collections/best-inventions-2025/7318298/squirrel-ai-intelligent-adaptive-learning-system/), [einpresswire.com](https://www.einpresswire.com/article/842853275/squirrel-ai-secures-5-papers-at-acl-2025-highlighting-breakthrough-in-ai-education)).
- **¿Diseño por el estudiante?** No.
- **¿Materiales propios del curso?** No; currículo propio K-12 (chino, matemáticas, inglés, física, química) ([linkedin.com/company/squirrelai](https://www.linkedin.com/company/squirrelai)).
- **Evaluación integrada:** sí — muestreo continuo de dominio, tests adaptativos y knowledge tracing ([time.com](https://time.com/collections/best-inventions-2025/7318298/squirrel-ai-intelligent-adaptive-learning-system/)).
- **Evidencia/citación:** **no verificado** (no documentada).
- **Offline vs nube:** hardware/software en centros conectados a su nube; modo offline **no verificado**.
- **Idiomas:** chino e inglés; expansión a EE.UU. en curso ([time.com](https://time.com/collections/best-inventions-2025/7318298/squirrel-ai-intelligent-adaptive-learning-system/), [forbes.com](https://www.forbes.com/sites/forbeschina/2025/02/18/derek-li-and-squirrel-ai-aim-to-lead-the-future-of-ai-driven-education/)).
- **Precio/acceso:** suscripción/pago por cursos en centros; más de 24 millones de estudiantes en China y 3.000+ ubicaciones ([time.com](https://time.com/collections/best-inventions-2025/7318298/squirrel-ai-intelligent-adaptive-learning-system/), [squirrelai.com](https://squirrelai.com/)); tarifa pública exacta **no verificado**.
- **Debilidad más clara:** opacidad — claims de efectividad difíciles de auditar externamente, orientación a entrenamiento para exámenes, y formato de centro físico que no escala al "sube los materiales de tu curso universitario" ([weforum.org](https://www.weforum.org/stories/education-and-skills/ai-tutor-china-teaching-gaps/)).

## 6. Riiid

- **Modelo de tutoría:** knowledge tracing profundo aplicado a preparación de exámenes: Santa TOEIC (lanzado 2017) genera la "ruta de aprendizaje más corta" por estudiante; mejora media de +124 puntos TOEIC tras 20 h de estudio ([prnewswire.com](https://www.prnewswire.com/news-releases/riiid-labs-launches-ai-education-solutions-in-america-301088205.html)), y +165 puntos con 20 min/día durante un mes según soporte oficial ([support.riiid.co](https://support.riiid.co/hc/en-us/articles/4402895958041-Riiid-Tutor-is-released-Try-it-for-free-now-21-06-28)). En 2023 lanzó R.test (assessment adaptativo SAT/ACT) y partnership con ALC para Japón ([beetroot.co](https://beetroot.co/edtech/top-12-rising-ai-education-startups-to-watch-in-2025/)). **Hallazgo 2026:** el sitio corporativo (riiid.co) ahora muestra **Socra AI**, un producto pivoteado hacia "aprender a juzgar entre respuestas de IA" (ask, not answer), señal de que la tutoría adaptiva pura no sostuvo el modelo de negocio ([riiid.co](https://www.riiid.co/)).
- **¿Diseño por el estudiante?** No.
- **¿Materiales propios del curso?** No; contenido de tests estandarizados (TOEIC, SAT, ACT) ([beetroot.co](https://beetroot.co/edtech/top-12-rising-ai-education-startups-to-watch-in-2025/)).
- **Evaluación integrada:** sí — assessment adaptativo y predicción de aciertos basada en estado de conocimiento del estudiante ([beetroot.co](https://beetroot.co/edtech/top-12-rising-ai-education-startups-to-watch-in-2025/)).
- **Evidencia/citación:** **no verificado**.
- **Offline vs nube:** apps móviles conectadas a nube; modo offline **no verificado**.
- **Idiomas:** coreano, japonés e inglés (TOEIC) ([beetroot.co](https://beetroot.co/edtech/top-12-rising-ai-education-startups-to-watch-in-2025/)).
- **Precio/acceso:** freemium/suscripción en app stores; cifra exacta **no verificado**.
- **Debilidad más clara:** hiper-nicho en tests estandarizados y pivote corporativo reciente que deja incierto el futuro del producto tutor original ([riiid.co](https://www.riiid.co/)).

## 7. Cognii

- **Modelo de tutoría:** Virtual Learning Assistant (VLA) conversacional cuyo diferencial es la **respuesta abierta** (constructed-response): el estudiante responde con sus propias palabras, la IA evalúa la comprensión, da feedback inmediato y tutoría 1-a-1 en diálogo; orientado a K-12, educación superior y capacitación corporativa ([walturn.com](https://www.walturn.com/insights/top-20-genai-products-for-education), [forwardfuture.com](https://forwardfuture.com/tools/details/cognii)).
- **¿Diseño por el estudiante?** No; lo despliegan instituciones.
- **¿Materiales propios del curso?** Parcial — el VLA se integra con contenido/plataformas del cliente mediante su tecnología de diálogo; si el estudiante final sube sus propios materiales: **no verificado**.
- **Evaluación integrada:** sí, es su núcleo — evaluación formativa de respuesta abierta con feedback inmediato y analytics docentes ([cloudassess.com](https://cloudassess.com/blog/best-ai-marking-tools/), [meratutor.ai](https://www.meratutor.ai/lms/blog/5-best-ai-tutors-for-education-that-empower-self-learning-and-independent-study/)).
- **Evidencia/citación:** **no verificado**.
- **Offline vs nube:** SaaS en nube; modo offline **no verificado**.
- **Idiomas:** inglés como mercado principal; multilingüe **no verificado**.
- **Precio/acceso:** institucional/SaaS; precio público **no verificado**.
- **Debilidad más clara:** tracción y prensa recientes escasas frente a los gigantes; el sitio oficial destaca premios de 2015-2016 más que casos 2025-2026 ([cognii.com](https://www.cognii.com/)), lo que sugiere estancamiento comercial.

## 8. Google — LearnLM / Gemini en educación

- **Modelo de tutoría:** familia de modelos ajustada específicamente para pedagogía (5 principios de ciencia del aprendizaje), integrada en Gemini como modo **Aprendizaje guiado (Guided Learning)** — lanzado el 6 de agosto de 2025, gratuito, con preguntas guía paso a paso — y en Classroom, YouTube y NotebookLM. Informes técnicos periódicos con evidencia: RCT en Sierra Leona (1.763 estudiantes, 12 h en 8 semanas) → salto del percentil 50 al 64 en matemáticas (1,8–2,5 años de progreso adicional); estudio con Eedi: 0,1% de mensajes con error factual y +5,5% de resolución de problemas nuevos vs solo tutores humanos ([cloud.google.com/solutions/learnlm](https://cloud.google.com/solutions/learnlm?hl=es-419), [completeaitraining.com](https://completeaitraining.com/news/googles-free-gemini-ai-tutor-guided-learning-promises/)).
- **¿Diseño por el estudiante?** No; configuración genérica (con "Gems" para instrucciones personalizadas).
- **¿Materiales propios del curso?** Parcial — Gemini puede trabajar sobre archivos que el usuario sube al chat, pero Guided Learning no está anclado por defecto al syllabus del curso del estudiante.
- **Evaluación integrada:** knowledge checks, quizzes y retroalimentación dentro del modo guiado ([openai.com no aplica]; ver [techlearning.com](https://www.techlearning.com/how-to/geminis-guided-learning-mode-from-google-ai-what-educators-need-to-know)).
- **Evidencia/citación:** citación cuando hay grounding con fuentes web; citación estructurada de materiales del curso del estudiante: **no verificado** (parcial).
- **Offline vs nube:** nube; requiere conexión y cuenta Google.
- **Idiomas:** multilingüe; India es el país líder en adopción con más de 2 millones de estudiantes usando Guided Learning ([testbook.com](https://testbook.com/question-answer/which-country-has-emerged-as-the-world-leader-in-adopting-google-gemini-s-guided-learning-ai-tutoring-feature-according-to-google-s-announcement-in-november-2025-)).
- **Precio/acceso:** gratuito con límites (cuenta Google); Google Workspace for Education con controles de admin para instituciones ([buildmvpfast.com](https://www.buildmvpfast.com/articles/best-llms-2026-guide/education-ai)).
- **Debilidad más clara:** genérico y atado al ecosistema Google — no nace de los materiales reales del curso del estudiante, y las políticas de datos de menores son un tema activo de regulación.

## 9. Anthropic — Claude for Education (Learning Mode)

- **Modelo de tutoría:** Claude con **Learning Mode**: guía el razonamiento del estudiante en vez de entregar respuestas — preguntas socráticas ("¿cómo abordarías este problema?"), énfasis en conceptos fundamentales, plantillas para trabajos; vive dentro de Projects (conversaciones organizadas por asignatura). Lanzado abril 2025 con acuerdos campus-wide (Northeastern, 50.000 personas; LSE; Champlain College) e integración con Canvas LMS (Instructure) vía Internet2 ([anthropic.com](https://www.anthropic.com/news/introducing-claude-for-education), [campustechnology.com](https://campustechnology.com/articles/2025/04/02/anthropic-launches-claude-for-education.aspx)).
- **¿Diseño por el estudiante?** No; se contrata/configura a nivel institución.
- **¿Materiales propios del curso?** Parcial — los estudiantes pueden subir documentos del curso a un Project como contexto, pero sin RAG curado ni verificación por curso (**no verificado** que exista grounding estructurado).
- **Evaluación integrada:** feedback sobre tesis y ensayos, rúbricas para docentes; sin evaluación de dominio integrada (**no verificado**).
- **Evidencia/citación:** puede redactar literature reviews "con citas", pero sin sistema de citación verificable contra fuentes del curso: **no verificado**.
- **Offline vs nube:** nube.
- **Idiomas:** multilingüe (incluye español) — capacidad del modelo Claude; alcance del producto educativo por idioma: **no verificado** específicamente.
- **Precio/acceso:** institucional (campus-wide); precio público **no verificado**. Claude individual tiene plan gratuito con límites.
- **Debilidad más clara:** no anclado a un curso específico y vulnerable al uso como atajo: el Anthropic Education Report (1 millón de chats) muestra que casi la mitad de los chats buscaban respuestas directas, no tutoría ([academyforeducationalstudies.org](https://academyforeducationalstudies.org/wp-content/uploads/2025/09/watkins-monroe-final-1.pdf)).

## 10. OpenAI — ChatGPT Study Mode

- **Modelo de tutoría:** modo de estudio dentro de ChatGPT (lanzado 29 de julio 2025): preguntas guía socráticas, andamiaje por secciones, calibración por objetivo y nivel, knowledge checks y quizzes con feedback personalizado; construido con instrucciones de sistema escritas con docentes y expertos en pedagogía (participación activa, gestión de carga cognitiva, metacognición, curiosidad). Disponible para usuarios logueados Free, Plus, Pro y Team (Edu semanas después) ([openai.com](https://openai.com/index/chatgpt-study-mode/), [cnbc.com](https://www.cnbc.com/2025/07/29/openai-announces-new-study-mode-product-for-students-.html)).
- **¿Diseño por el estudiante?** No; es un modo genérico que se activa/desactiva.
- **¿Materiales propios del curso?** Parcial — funciona sobre archivos que el usuario suba a la conversación, sin curaduría de curso ni citas; **no verificado** que exista grounding estructurado por materia.
- **Evaluación integrada:** quizzes y preguntas abiertas con feedback; seguimiento de progreso anunciado como roadmap, no como producto verificado ([openai.com](https://openai.com/index/chatgpt-study-mode/)).
- **Evidencia/citación:** **no verificado** (puede alucinar; sin citación estructurada).
- **Offline vs nube:** nube.
- **Idiomas:** multilingüe (capacidad de ChatGPT).
- **Precio/acceso:** gratis con límites (plan Free); Plus/Pro de pago ([technologyreview.com](https://www.technologyreview.com/2025/07/29/1120801/openai-is-launching-a-version-of-chatgpt-for-college-students/)).
- **Debilidad más clara:** OpenAI admite comportamiento inconsistente por ser instrucciones custom sobre el modelo base (no conducta entrenada), y su genéricidad lo deja desconectado del programa real del estudiante ([openai.com](https://openai.com/index/chatgpt-study-mode/)).

## 11. Google — NotebookLM (hoy Gemini Notebook)

- **Modelo de tutoría:** no es un tutor socrático sino un "cuaderno de fuentes": el usuario sube PDFs, Docs, URLs, videos de YouTube y audio; el chat responde **anclado a esas fuentes con citas inline al pasaje exacto**; genera Audio Overviews (podcast con dos voces), mapas mentales, study guides y flashcards. No entrena con los datos subidos ([skywork.ai](https://skywork.ai/blog/doc/notebooklm-guide-2025-how-to-use-googles-ai-for-study-and-research), [atlasworkspace.ai](https://www.atlasworkspace.ai/blog/notebooklm-for-students)). En 2026 se integra como "Gemini Notebook" ([atlasworkspace.ai](https://www.atlasworkspace.ai/blog/notebooklm-for-students)).
- **¿Diseño por el estudiante?** Parcial — el estudiante elige y sube sus fuentes (sus materiales), pero no configura el comportamiento pedagógico del agente.
- **¿Materiales propios del curso?** **Sí, es el núcleo del producto** ([skywork.ai](https://skywork.ai/blog/doc/notebooklm-guide-2025-how-to-use-googles-ai-for-study-and-research)).
- **Evaluación integrada:** flashcards, quizzes y study guides; sin evaluación formativa conversacional profunda (**no verificado** algo más avanzado).
- **Evidencia/citación:** **sí — citas inline a los pasajes exactos de las fuentes**, el estándar de mercado más cercano al diferencial de MACI "evidencia con timestamp" ([skywork.ai](https://skywork.ai/blog/doc/notebooklm-guide-2025-how-to-use-googles-ai-for-study-and-research)).
- **Offline vs nube:** nube; requiere conexión.
- **Idiomas:** multilingüe (responde en el idioma de las fuentes/del usuario); lista exacta de idiomas **no verificado**.
- **Precio/acceso:** gratis con límites (notebooks, fuentes); NotebookLM Plus ~US$20/mes con cuotas ampliadas ([solothinking.com](https://solothinking.com/notebooklm-complete-guide-2025-how-to-use-it-pricing-login-app-pdf-guide-download/), [tech-now.io](https://tech-now.io/en/blogs/google-notebooklm-guide-2025-the-ai-knowledge-companion-for-2025)).
- **Debilidad más clara:** entrega contenido (resúmenes, respuestas) en vez de forzar lucha productiva — no se niega a dar la respuesta — y sin grafo de prerrequisitos, evaluación de dominio ni modo offline.

## 12. Jotform AI Tutor (representante de la categoría "construye tu tutor con tus archivos")

- **Modelo de tutoría:** generador de tutores IA sin código: se crea un tutor a partir de un archivo subido o un prompt, y ofrece tres modos — contest (competencia en tiempo real), practice (conversación detallada) y guided (paso a paso sin revelar respuestas) ([jotform.com/ai/ai-tutor](https://www.jotform.com/ai/ai-tutor/), [jotform.com/ai/how-to-build-an-ai-tutor](https://www.jotform.com/ai/how-to-build-an-ai-tutor/)). Es el competidor más directo de la premisa "sube tus materiales → obtén un tutor", junto a ofertas similares de formularios/apps (TutorOcean, VEGA AI) ([jotform.com/ai/best-ai-tutor](https://www.jotform.com/ai/best-ai-tutor/), [tutorocean.com/ai](https://www.tutorocean.com/ai)).
- **¿Diseño por el estudiante?** Parcial — cualquier persona puede crear un tutor, pero la "configuración" es subir un archivo/elegir modo, no diseñar pedagogía, prerrequisitos ni evaluación.
- **¿Materiales propios del curso?** **Sí** ([jotform.com/ai/how-to-build-an-ai-tutor](https://www.jotform.com/ai/how-to-build-an-ai-tutor/)).
- **Evaluación integrada:** quizzes interactivos y modo concurso; evaluación adaptativa o por comprensión profunda: **no verificado**.
- **Evidencia/citación:** grounding en el archivo subido, pero sin citas con timestamp documentadas: **no verificado**.
- **Offline vs nube:** nube (servicio Jotform).
- **Idiomas:** multilingüe heredado de Jotform; cobertura exacta **no verificado**.
- **Precio/acceso:** freemium dentro de los planes de Jotform; cifra exacta **no verificado**.
- **Debilidad más clara:** herramienta de engagement de superficie — orientada a formularios y ejercicios rápidos, sin teoría pedagógica publicada ni evidencia de efecto en aprendizaje.

---

## Tabla comparativa

| Competidor | ¿Diseño por estudiante? | Materiales propios | Evidencia citada | Offline | Evaluación integrada | Precio |
|---|---|---|---|---|---|---|
| Georgia Tech (Jill Watson) | No (equipo de curso) | **Sí** (RAG sobre el curso) | Parcial (grounding verificado, sin citas navegables documentadas) | No verificado | No (evalúa al sistema, no al estudiante) | Institucional, sin precio público |
| Khanmigo (Khan Academy) | No | No (contenido Khan) | No verificado | No (nube) | Parcial (práctica adaptativa, dashboards) | US$4/mes estudiantes; gratis docentes; distritos por licencia |
| Duolingo Max | No | No | No (puede alucinar) | Lecciones sí, AI no | Sí (quizzes, reportes de conversación) | US$14–30/mes |
| Century Tech | No | Parcial (contenido Century) | No verificado | No verificado | Sí (auto-marcación, diagnósticos) | Institucional, no verificado |
| Squirrel AI | No | No (currículo propio) | No verificado | No verificado | Sí (knowledge tracing adaptativo) | No verificado (centros + suscripción) |
| Riiid / Socra AI | No | No (tests TOEIC/SAT) | No verificado | No verificado | Sí (assessment adaptativo) | Freemium, cifra no verificada |
| Cognii | No | Parcial (integración institucional) | No verificado | No verificado | **Sí** (respuesta abierta con feedback inmediato) | Institucional, no verificado |
| Google LearnLM / Guided Learning | No | Parcial (archivos al chat) | Parcial (con grounding web) | No (nube) | Sí (knowledge checks) | Gratis con límites; Workspace for Education |
| Claude for Education | No | Parcial (Projects con documentos) | No verificado | No (nube) | Parcial (feedback de ensayos) | Institucional, no verificado |
| ChatGPT Study Mode | No | Parcial (archivos al chat) | No verificado | No (nube) | Sí (quizzes, checks) | Gratis con límites; Plus/Pro |
| NotebookLM / Gemini Notebook | Parcial (sube sus fuentes) | **Sí** | **Sí (citas inline al pasaje)** | No (nube) | Parcial (flashcards, quizzes) | Gratis con límites; Plus ~US$20/mes |
| Jotform AI Tutor | Parcial (sube archivos, elige modo) | **Sí** | No verificado | No (nube) | Parcial (quizzes, modos) | Freemium, cifra no verificada |

## Síntesis: ¿qué hace único a MACI/Termito?

El mercado 2024-2026 resuelve la tutoría como **consumo**: el estudiante recibe un tutor que la plataforma (o la universidad, o la editorial) ya diseñó — Jill Watson groundea en el curso pero solo porque un equipo de Georgia Tech construyó la base de conocimiento; Khanmigo, Duolingo Max, Squirrel AI y Century traen su propio currículo; LearnLM, Study Mode y Claude for Education son capas pedagógicas genéricas sobre modelos de propósito general; NotebookLM acepta los materiales del estudiante pero para resumirlos y citarlos, no para enseñar con lucha productiva; Jotform convierte un archivo en quizzes sin teoría pedagógica. Ninguno permite que **el propio estudiante arquitecte su agente desde sus materiales reales** — programa, presentaciones, evaluaciones pasadas y videos de su curso concreto — con evidencia citada con timestamp en cada respuesta, grafo de prerrequisitos, evaluación por distinciones conceptuales (no repetición), funcionamiento 100% offline y un ciclo de vida que muere con el curso. **El mercado ofrece consumo; Termito ofrece arquitectura del aprendizaje**: el estudiante no es usuario de un tutor ajeno, es diseñador del suyo, y esa autoría sobre cómo se estructura su propio aprendizaje es el diferencial que ningún competidor cubre hoy.
