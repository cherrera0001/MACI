/* i18n.js — ES/EN del interfaz (FR-022). Diccionario + toggle que persiste.
El cambio de idioma recarga la pagina: simple y sin estado fantasma. El
contenido generado por el Datito respeta el idioma del estudiante por regla
del system prompt (identidad.py) y de la plantilla de generacion (tutor.py). */
const I18N = {
  es: {
    /* comunes */
    "c_chat": "Chat", "c_eval": "Evaluarme", "c_dominio": "Dominio",
    "pill_tutor": "modo tutor",
    "pill_exploracion": "modo exploración (sin Ollama: cita evidencia, no genera)",
    "pill_caido": "servidor no responde",
    "cerrar": "Cerrar", "cargando": "cargando…",
    "lang_boton": "EN",
    /* index */
    "ix_titulo": "Tus Datitos",
    "ix_sub": "Un Datito por curso: diseñado por ti, con los materiales reales. Todo en tu máquina.",
    "ix_crear": "＋ Crear Datito",
    "ix_vacio": "Todavía no tienes Datitos. Crea el primero: toma menos de 10 minutos.",
    "ix_chat": "Chatear",
    "ix_caido": "El servidor local no responde. Arranca Datito con <code>start.py</code>.",
    "ix_que_es": "<b>¿Qué es un Datito?</b> Un tutor que tú construyes: le entregas el programa, las clases y los certámenes de tu curso, defines quién es y cómo enseña, y conversa contigo citando la fuente de cada afirmación. Cuando el curso termina, desaparece; tu conocimiento se queda contigo.",
    /* wizard */
    "wz_h1": "Construyamos tu Datito",
    "wz_sub": "Una decisión por pantalla. Enter no existe aquí: tú eliges todo.",
    "wz_p0_h": "Primero: ¿qué curso vas a aprender?",
    "wz_p0_p1": "Escribe el nombre (el slug se genera solo).",
    "wz_nombre_ph": "Fundamentos de Ciencia de Datos",
    "wz_p0_p2": "Ahora <b>los materiales reales</b>: programa, presentaciones, transcripciones, certámenes pasados, PDF de clases. Puedes subirlos ahora o después (desde la carpeta <code>materiales/</code> del curso).",
    "wz_siguiente": "Siguiente →", "wz_atras": "Atrás", "wz_usarla": "usarla",
    "wz_sugerencia": "sugerencia:",
    "wz_tu_respuesta": "Tu respuesta…",
    "wz_generar": "Generar mi Datito ✨",
    "wz_final_h": "Así quedó tu Datito",
    "wz_final_p": "Este es el system prompt completo — tu agente, tu diseño, siempre editable en <code>prompt/actual.md</code> (cada cambio queda versionado).",
    "wz_confirmar": "✓ Confirmar y empezar", "wz_volver": "Volver",
    "wz_construyendo": "Construyendo: parseando materiales e indexando evidencia…",
    "wz_listo": "Listo: {f} fuentes, {fr} fragmentos indexados con referencia citable.",
    "wz_nombre_falta": "Escribe el nombre del curso.",
    "wz_subidos": "{n} archivo(s) subido(s).",
    "wz_dist_h": "¿Qué distinciones debe dominar quien estudie esto?",
    "wz_dist_p": "Una <b>distinción</b> separa dos conceptos vecinos: elige al menos 2 del grafo y escribe la pregunta que los separa. Puedes crearlas ahora o después en <code>evaluaciones/</code>.",
    "wz_dist_pregunta": "Pregunta que obliga a separar los conceptos…",
    "wz_dist_criterios": "Criterios de la rúbrica, uno por línea (todos deben cumplirse para «logrado»)…",
    "wz_dist_pasos": "Pasos de ayuda para la lucha productiva, uno por línea (opcional)…",
    "wz_dist_solucion": "Solución modelo, se revela solo tras el intento (opcional)…",
    "wz_dist_guardar": "＋ Guardar distinción",
    "wz_dist_saltar": "Saltar →",
    "wz_dist_guardada": "Distinción guardada ({n}). Puedes agregar otra o continuar.",
    "wz_dist_faltan": "Elige al menos 2 conceptos y escribe la pregunta y un criterio.",
    /* eval: procedural (H-8.2) */
    "ev_procedural": "Distinción procedural: pega tu script. Los pasos se verifican por la traza de la corrida real (marca pasos con print(\"#@nombre\")).",
    "ev_ph_codigo": "Pega aquí tu script Python. Marca los pasos con print(\"#@brecha\"), print(\"#@etiquetar\")…",
    "ev_traza": "Traza:",
    /* evidencia viva (H-8.1) */
    "evv_h1": "La brecha train-test, vista en una corrida real",
    "evv_sub": "No es un ejemplo inventado: es la ejecución real de tres modelos sobre datos sintéticos (semilla 42). El formato es el del profesor: <b>primero la brecha, después la etiqueta</b>.",
    "evv_ref_h": "1 · La evidencia capturada",
    "evv_ref_p": "Traza de referencia, capturada el 2026-10-29 con REA (evidence <code>84b485dd…</code>, journal ordenado). Mírala paso a paso:",
    "evv_re_h": "2 · Re-ejecutar y comprobar",
    "evv_re_p": "La misma corrida vuelve a correr en tu máquina (sandbox, sin red). Con la misma semilla deben reproducirse los mismos números:",
    "evv_btn": "↻ Re-ejecutar con semilla 42",
    "evv_semilla": "semilla",
    /* guia Ollama (D-7.1) */
    "guia_t": "Sin Ollama, el Datito cita evidencia pero no genera explicaciones.",
    "guia_instala": "Para el modo tutor, instala Ollama y el modelo:",
    "guia_reinicia": "al terminar, recarga la página: la guía desaparece sola.",
    "guia_cerrar": "entendido",
    "w_c1p": "¿Quién es tu tutor y en qué materia?",
    "w_c1s": "Tutor experto en fundamentos de ciencia de datos",
    "w_c2p": "¿Para qué existe en este curso?",
    "w_c2s": "Acompañarme hasta el certamen final, amplificando mi esfuerzo",
    "w_c3p": "¿Qué debe hacer? (explicar, ejercicios, corregir…)",
    "w_c3s": "Explicar con ejemplos reales, proponer ejercicios, corregir con evidencia citada",
    "w_c4p": "¿Cómo enseña? (socrático, directo, con ejemplos…)",
    "w_c4s": "Socrático: pregunta de activación, pistas graduadas, nunca la solución antes del intento",
    "w_c5p": "Contexto del curso (programa, nº de clases, evaluaciones…)",
    "w_c5s": "Curso universitario de un semestre, 23 clases, evaluación por distinciones",
    "w_c6p": "¿Cómo aprendes TÚ? (paso a paso/desafío, texto/ejemplos…)",
    "w_c6s": "Paso a paso, con ejemplos concretos y tablas de datos",
    "w_c7p": "Reglas que no debe romper jamás",
    "w_c7s": "No inventar información del curso; fomentar razonamiento crítico",
    "w_c8p": "¿Por cuánto tiempo te acompaña?",
    "w_c8s": "Todo el semestre, recibiendo mis notas como retroalimentación",
    /* chat */
    "ch_sub": "Cada afirmación del tutor lleva su fuente: tócala para ver el fragmento.",
    "ch_ph": "Pregunta lo que quieras del curso… o trae un ejercicio para practicar.",
    "ch_enviar": "Enviar",
    "ch_ayuda": "<b>Registrar duda:</b> escríbela y usa el botón ✏️ que aparece junto a cada respuesta con fuente. Las dudas quedan en <code>dudas.yaml</code> con su procedimiento. En ejercicios: tu intento primero; «pista» muestra un paso; la solución solo con tu consentimiento, queda registrada.",
    "ch_pensando": "pensando…",
    "ch_duda": "✏️ registrar como duda",
    "ch_duda_ok": "✓ duda registrada",
    "ch_no_curso": "⚠ No encuentro ese curso. Vuelve a la lista y elige uno.",
    /* eval */
    "ev_h1": "Evaluación por distinciones",
    "ev_sub": "Separar conceptos vecinos, no recitar definiciones. Responde con tus palabras; el tutor evalúa con la rúbrica del curso.",
    "ev_micro": "Distinciones de esta sesión: {l}/{n}",
    "ev_vacio": "Este curso aún no tiene distinciones. Añade ítems en <code>evaluaciones/*.yaml</code>.",
    "ev_siguiente": "Siguiente distinción →",
    "ev_ver_dominio": "Ver mi dominio",
    "ev_ph": "Tu respuesta, con tus palabras…",
    "ev_responder": "Responder",
    "ev_de": "de",
    "ev_conceptos": "conceptos en juego:",
    /* panel */
    "pn_h1": "Dominio del curso",
    "pn_sub": "Cada cadena es un camino de prerrequisitos. Los nodos se revelan conforme estudias (patrón de los mejores cursos adaptativos).",
    "pn_toggle": "Mostrar todo el mapa (incluye lo no desbloqueado)",
    "pn_leyenda": "<b>Leyenda:</b> ● dominado · ◑ comprendido · ◐ en estudio · ○ no estudiado. El estado sale de tus respuestas en la evaluación por distinciones (<code>grafo/dominio.yaml</code>).",
    /* familiar (D-14.2) */
    "fm_top": "🏡 Datito · Panel de bienestar",
    "fm_sub": "Cómo está su familiar, de un vistazo y con respeto.",
    "fm_imprimir": "🖨️ Imprimir libro",
    "fm_volver": "Volver",
    "fm_pulso": "💗 Pulso del vínculo",
    "fm_dias": "días seguidos activa/o",
    "fm_sesion": "sesión de conversación",
    "fm_sesiones": "sesiones de conversación",
    "fm_mensaje": "mensaje intercambiado",
    "fm_mensajes": "mensajes intercambiados",
    "fm_recuerdo": "recuerdo guardado",
    "fm_recuerdos": "recuerdos guardados",
    "fm_taller": "taller práctico completado",
    "fm_talleres": "talleres prácticos completados",
    "fm_sin_conversacion": "aún no conversa",
    "fm_ultima": "Última conversación:",
    "fm_ok_t": "Bienestar sin alertas.",
    "fm_ok_p": "El guardián no ha registrado señales de riesgo ni de emergencia.",
    "fm_alerta": "alerta registrada",
    "fm_alertas": "alertas registradas",
    "fm_alertas_nota": "Por privacidad solo se muestran fecha y categoría:",
    "fm_libro": "📖 Libro de Historias de Vida",
    "fm_sobre": "Sobre",
    "fm_otras": "Otras historias",
    "fm_sin_historias": "Aún no hay historias de vida registradas.",
  },
  en: {
    /* common */
    "c_chat": "Chat", "c_eval": "Quiz me", "c_dominio": "Mastery",
    "pill_tutor": "tutor mode",
    "pill_exploracion": "exploration mode (no Ollama: cites evidence, no generation)",
    "pill_caido": "server not responding",
    "cerrar": "Close", "cargando": "loading…",
    "lang_boton": "ES",
    /* index */
    "ix_titulo": "Your Datitos",
    "ix_sub": "One Datito per course: designed by you, from the real course materials. Everything on your machine.",
    "ix_crear": "＋ Create Datito",
    "ix_vacio": "No Datitos yet. Create the first one: it takes under 10 minutes.",
    "ix_chat": "Chat",
    "ix_caido": "The local server is not responding. Start Datito with <code>start.py</code>.",
    "ix_que_es": "<b>What is a Datito?</b> A tutor you build: you give it your course syllabus, classes and past exams, define who it is and how it teaches, and it chats with you citing the source of every claim. When the course ends, it disappears; the knowledge stays with you.",
    /* wizard */
    "wz_h1": "Let's build your Datito",
    "wz_sub": "One decision per screen. No defaults here: you choose everything.",
    "wz_p0_h": "First: what course are you going to learn?",
    "wz_p0_p1": "Write the name (the slug is generated automatically).",
    "wz_nombre_ph": "Fundamentals of Data Science",
    "wz_p0_p2": "Now <b>the real materials</b>: syllabus, slides, transcripts, past exams, class PDFs. You can upload them now or later (into the course's <code>materiales/</code> folder).",
    "wz_siguiente": "Next →", "wz_atras": "Back", "wz_usarla": "use it",
    "wz_sugerencia": "suggestion:",
    "wz_tu_respuesta": "Your answer…",
    "wz_generar": "Generate my Datito ✨",
    "wz_final_h": "This is your Datito",
    "wz_final_p": "This is the full system prompt — your agent, your design, always editable in <code>prompt/actual.md</code> (every change is versioned).",
    "wz_confirmar": "✓ Confirm and start", "wz_volver": "Back",
    "wz_construyendo": "Building: parsing materials and indexing evidence…",
    "wz_listo": "Done: {f} sources, {fr} fragments indexed with citable references.",
    "wz_nombre_falta": "Write the course name.",
    "wz_subidos": "{n} file(s) uploaded.",
    "wz_dist_h": "Which distinctions should whoever studies this master?",
    "wz_dist_p": "A <b>distinction</b> separates two neighboring concepts: pick at least 2 from the graph and write the question that tells them apart. You can create them now or later in <code>evaluaciones/</code>.",
    "wz_dist_pregunta": "Question that forces separating the concepts…",
    "wz_dist_criterios": "Rubric criteria, one per line (all must hold for «logrado»)…",
    "wz_dist_pasos": "Productive-struggle hint steps, one per line (optional)…",
    "wz_dist_solucion": "Model solution, revealed only after the attempt (optional)…",
    "wz_dist_guardar": "＋ Save distinction",
    "wz_dist_saltar": "Skip →",
    "wz_dist_guardada": "Distinction saved ({n}). Add another or continue.",
    "wz_dist_faltan": "Pick at least 2 concepts and write the question and one criterion.",
    /* eval: procedural (H-8.2) */
    "ev_procedural": "Procedural distinction: paste your script. Steps are verified from the real run's trace (mark steps with print(\"#@name\")).",
    "ev_ph_codigo": "Paste your Python script here. Mark steps with print(\"#@brecha\"), print(\"#@etiquetar\")…",
    "ev_traza": "Trace:",
    /* evidencia viva (H-8.1) */
    "evv_h1": "The train-test gap, seen in a real run",
    "evv_sub": "Not a made-up example: the real execution of three models on synthetic data (seed 42). The format is the professor's: <b>the gap first, the label after</b>.",
    "evv_ref_h": "1 · The captured evidence",
    "evv_ref_p": "Reference trace, captured on 2026-10-29 with REA (evidence <code>84b485dd…</code>, ordered journal). Step through it:",
    "evv_re_h": "2 · Re-run and verify",
    "evv_re_p": "The same run executes again on your machine (sandbox, no network). With the same seed the same numbers must reproduce:",
    "evv_btn": "↻ Re-run with seed 42",
    "evv_semilla": "seed",
    /* guia Ollama (D-7.1) */
    "guia_t": "Without Ollama, Datito cites evidence but doesn't generate explanations.",
    "guia_instala": "For tutor mode, install Ollama and the model:",
    "guia_reinicia": "when done, reload the page: the guide goes away on its own.",
    "guia_cerrar": "got it",
    "w_c1p": "Who is your tutor and in what subject?",
    "w_c1s": "Expert tutor in fundamentals of data science",
    "w_c2p": "Why does it exist in this course?",
    "w_c2s": "To accompany me until the final exam, amplifying my effort",
    "w_c3p": "What must it do? (explain, exercises, grade…)",
    "w_c3s": "Explain with real examples, propose exercises, correct with cited evidence",
    "w_c4p": "How does it teach? (socratic, direct, with examples…)",
    "w_c4s": "Socratic: activation question, graduated hints, never the solution before the attempt",
    "w_c5p": "Course context (syllabus, number of classes, assessments…)",
    "w_c5s": "One-semester university course, 23 classes, assessment by distinctions",
    "w_c6p": "How do YOU learn? (step by step/challenge, text/examples…)",
    "w_c6s": "Step by step, with concrete examples and data tables",
    "w_c7p": "Rules it must never break",
    "w_c7s": "Never invent course information; foster critical reasoning",
    "w_c8p": "How long does it accompany you?",
    "w_c8s": "The whole semester, receiving my grades as feedback",
    /* chat */
    "ch_sub": "Every claim from the tutor carries its source: tap it to see the fragment.",
    "ch_ph": "Ask anything about the course… or bring an exercise to practice.",
    "ch_enviar": "Send",
    "ch_ayuda": "<b>To log a doubt:</b> write it and use the ✏️ button next to any sourced answer. Doubts land in <code>dudas.yaml</code> with their resolution procedure. For exercises: your attempt first; «hint» shows one step; the solution only with your consent, and it is recorded.",
    "ch_pensando": "thinking…",
    "ch_duda": "✏️ log as doubt",
    "ch_duda_ok": "✓ doubt logged",
    "ch_no_curso": "⚠ I can't find that course. Go back to the list and pick one.",
    /* eval */
    "ev_h1": "Assessment by distinctions",
    "ev_sub": "Separate neighboring concepts, don't recite definitions. Answer in your own words; the tutor grades with the course rubric.",
    "ev_micro": "Distinctions this session: {l}/{n}",
    "ev_vacio": "This course has no distinctions yet. Add items in <code>evaluaciones/*.yaml</code>.",
    "ev_siguiente": "Next distinction →",
    "ev_ver_dominio": "See my mastery",
    "ev_ph": "Your answer, in your own words…",
    "ev_responder": "Answer",
    "ev_de": "of",
    "ev_conceptos": "concepts at play:",
    /* panel */
    "pn_h1": "Course mastery",
    "pn_sub": "Each chain is a prerequisite path. Nodes unlock as you study (pattern from the best adaptive courses).",
    "pn_toggle": "Show the whole map (including locked content)",
    "pn_leyenda": "<b>Legend:</b> ● mastered · ◑ understood · ◐ studying · ○ not studied. The state comes from your answers in the distinction assessment (<code>grafo/dominio.yaml</code>).",
    /* familiar (D-14.2) */
    "fm_top": "🏡 Datito · Wellness panel",
    "fm_sub": "How your loved one is doing, at a glance and with respect.",
    "fm_imprimir": "🖨️ Print life story",
    "fm_volver": "Back",
    "fm_pulso": "💗 Bond pulse",
    "fm_dias": "active days in a row",
    "fm_sesion": "conversation session",
    "fm_sesiones": "conversation sessions",
    "fm_mensaje": "message exchanged",
    "fm_mensajes": "messages exchanged",
    "fm_recuerdo": "memory kept",
    "fm_recuerdos": "memories kept",
    "fm_taller": "practical workshop completed",
    "fm_talleres": "practical workshops completed",
    "fm_sin_conversacion": "no conversations yet",
    "fm_ultima": "Last conversation:",
    "fm_ok_t": "Wellness without alerts.",
    "fm_ok_p": "The guardian has logged no risk or emergency signals.",
    "fm_alerta": "alert logged",
    "fm_alertas": "alerts logged",
    "fm_alertas_nota": "For privacy, only date and category are shown:",
    "fm_libro": "📖 Book of Life Stories",
    "fm_sobre": "About",
    "fm_otras": "Other stories",
    "fm_sin_historias": "No life stories recorded yet.",
  },
};

function langDatito() {
  const g = localStorage.getItem("datito-lang");
  if (g === "es" || g === "en") return g;
  return (navigator.language || "es").toLowerCase().startsWith("en") ? "en" : "es";
}

function t(clave, vars) {
  let s = (I18N[langDatito()] || {})[clave] ?? I18N.es[clave] ?? clave;
  if (vars) for (const k in vars) s = s.replace("{" + k + "}", vars[k]);
  return s;
}

function aplicarIdioma() {
  const l = langDatito();
  document.documentElement.lang = l;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    el.textContent = t(el.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-html]").forEach(el => {
    el.innerHTML = t(el.dataset.i18nHtml);
  });
  document.querySelectorAll("[data-i18n-ph]").forEach(el => {
    el.placeholder = t(el.dataset.i18nPh);
  });
}

function insertarBotonIdioma() {
  document.querySelectorAll(".top").forEach(top => {
    if (top.querySelector(".lang-switch")) return;
    const b = document.createElement("button");
    b.className = "boton alt lang-switch";
    b.style.cssText = "padding:.35rem .7rem;font-size:.82rem";
    b.textContent = t("lang_boton");
    b.title = "idioma / language";
    b.onclick = () => {
      localStorage.setItem("datito-lang", langDatito() === "es" ? "en" : "es");
      location.reload();
    };
    top.insertBefore(b, top.querySelector(".estado-motor"));
  });
}

document.addEventListener("DOMContentLoaded", () => {
  aplicarIdioma();
  insertarBotonIdioma();
});
