# Ingeniería inversa — Duolingo (duolingo.com): lección activa y gamificación

**Fecha:** 2026-10-17/18 · **Herramienta:** REA CLI v6.5.0 (`rea-agents capture-browser-scenario`) con Chromium headless (Playwright) · **Modo:** sin cuenta de usuario (flujo anónimo) · **Alcance:** onboarding, una lección activa del curso Spanish↔English, feedback de error/acerto, trazas de red con cuerpos de respuesta, localStorage.

Toda afirmación de este informe cita el archivo de evidencia correspondiente en `docs/investigacion/rea-evidencia/duolingo/`.

## 1. URLs inspeccionadas

| URL | Qué se hizo | Evidencia |
|---|---|---|
| `https://www.duolingo.com/` | Carga homepage sin sesión | `01-homepage.json/png` |
| `https://www.duolingo.com/register` | Selector "I want to learn…" (tarjetas de idioma) | `02-register-selector-idioma.json/png` |
| `https://www.duolingo.com/welcome` | Funboarding animado ("Hi there! I'm Duo!") | `03-onboarding-duo.json/png` |
| `https://www.duolingo.com/welcome` (paso posterior) | "How did you hear about Duolingo?" (opción obligatoria) | `04-onboarding-how-did-you-hear.json/png` |
| `https://www.duolingo.com/learn` (con curso anónimo ya elegido) | "How much Spanish do you know?" (5 niveles, role=radiogroup) | `05-funboarding-nivel.json/png` |
| `https://www.duolingo.com/learn` | "Now let's find the best place to start!" → Start from scratch / Find my level | `06-funboarding-start-from-scratch.json/png` |
| `https://www.duolingo.com/lesson` | **Lección activa** (ejercicios de vocabulario) | `07-`, `08-`, `09-…` |

**Sin CAPTCHA/Cloudflare en ningún paso** del flujo anónimo (el único reCAPTCHA observado es invisible/enterprise al crear el usuario anónimo, vía token en body de POST — ver §5). La detección por texto del DOM dio un falso positivo inicial ("challenge" en copy de marketing); los screenshots lo descartan.

## 2. Escenarios REA por captura

Todos los escenarios usaron el esquema ya validado: `capture-browser-scenario "$(cat escenario.json)" --format json`, browser launch headless con Chromium-1234, `capture.at_end: [screenshot, dom, url, storage]`, `after_each_step: [screenshot]` en los de lección, y `events: [network, page-errors]` con `network.request_body/response_body/header_values: true` en las capturas de lección.

1. `01` — carga homepage (4 s).
2. `02` — carga `/register` (selector de idioma).
3. `03` — `/register` + clic en `[data-test="flag-spanish language-card"]` → `/welcome`.
4. `04` — funboarding: 2× `[data-test="funboarding-continue-button"]`; el 2º CONTINUE cae en pantalla con opciones obligatorias (clic en CONTINUE deshabilitado = espera de actionability que cancela el escenario; **limitación de REA**: los clicks que no resuelven cuelgan hasta el timeout global en vez de fallar rápido).
5. `05` — atajo: tras elegir idioma, `goto /learn` → pantalla de nivel ("How much Spanish do you know?").
6. `06` — clic en 1ª opción de nivel (`ul.sEiMT > div:first-child [data-test="prior-proficiency-card"]` por strict-mode de Playwright con 5 coincidencias) + CONTINUE → "Start from scratch".
7. `07` — clic en `[data-test="start-basics"]` + CONTINUE final → **URL `/lesson` con ejercicio activo** ("Which one of these is 'cat'?" con corazones y barra de progreso). Cero requests nuevos a duolingo.com durante toda la transición a la lección.
8. `08` — respuesta **incorrecta**: clic en 1ª opción (primer `div[role=radio]` del radiogroup `aria-label="choice"`) → `[data-test="player-next"]` (botón CHECK) → feedback de error con modal de corazones.
9. `09` — respuesta **correcta**: `[data-test="challenge-choice"]:has-text("gato")` → CHECK → feedback verde "Nice!".
10. `10` — flujo con SKIP: primer ejercicio omitido → solución revelada + modal de corazones → KEEP GOING → CONTINUE → ejercicio 2 ("Which one of these is 'dog'?", `10-leccion-skip-y-ejercicio2.json`).

## 3. Hallazgos técnicos

### 3.1 Estructura DOM de la lección (componentes y selectores)

Del DOM de la lección (`07-leccion-carga-sin-request.json`, paso final):

- Contenedor ejercicio: `[data-test="challenge challenge-select"]` (varía por tipo de ejercicio).
- Encabezado/pregunta: `h1[data-test="challenge-header"]` ("Which one of these is “cat”?").
- Tag de contexto: "NEW WORD" con icono (spans animados letra a letra).
- Opciones: `div[role="radio"][data-test="challenge-choice"]` dentro de `div[role="radiogroup"][aria-label="choice"]`; cada tarjeta lleva número de teclado (1/2/3), imagen (background-image de CloudFront) y texto con `lang="es"`.
- Footer del jugador: `div#session/PlayerFooter` con:
  - `[data-test="player-skip"]` ("Skip", botón blanco).
  - `[data-test="player-next"]` — **doble función**: etiquetado "Check" antes de responder (`aria-disabled="true"` hasta elegir) y "Continue" tras el feedback.
- Barra de progreso: barra superior (verde sobre gris) que avanza por ejercicio (visible en comparación `08` vs `09`).
- Corazones: contenedor con `img` (SVG hearts de CloudFront) + `span` con el número (5 al inicio, 4 tras un error).
- Botón salir: `[data-test="quit-button"]` (X esquina superior izquierda).
- Feedback de error: `[data-test="blame blame-incorrect"]` en el footer con `h2 "Correct solution:"` + la solución en `div[lang=es]`, y botones de utilidad `aria-label="Too easy" / "Too difficult" / "Report"`.
- Feedback correcto: footer verde con check "Nice!" (mismos botones de utilidad + Continue).
- Modal de corazones (tras primer error): `[data-test="hearts-intro-continue-button"]` ("KEEP GOING") sobre `[data-test="drawer-backdrop"]`.

### 3.2 Mecánicas de gamificación observadas (sin cuenta)

- **Corazones (vidas):** 5 al inicio de la lección; cada error −1 (verificado: 5→4 tras responder mal, `08-leccion-feedback-error-corazones.png`). Modal pedagógico al primer descuento: "Each mistake costs 1 heart! Stay sharp and focused to keep your hearts. You got this!".
- **Barra de progreso de la lección:** avance visible por respuesta.
- **Topbar de la app** (ya presente en `/learn` anónimo, DOM de `05-funboarding-nivel.json`): `streak-menu`/`streak-stat`, `lingot-menu`/`lingot-stat`, `hearts-menu`, `quests-nav`, `leaderboard-nav`, `shop-nav`, `profile-tab`, `create-profile-juicy`, `sign-in-juicy`.
- **"NEW WORD" badge** y animaciones Lottie por tarjeta.
- **SKIP** disponible en cada ejercicio (renuncia con solución mostrada).
- **Funboarding gamificado:** mascota con diálogos ("Hi there! I'm Duo!", "Let's get this party started!"), barra de progreso del onboarding, tarjetas ilustradas, una sola pregunta de marketing obligatoria ("How did you hear…").
- No se alcanzó a observar streak freeze ni pantalla final de lección (ver Limitaciones).

### 3.3 Comportamiento ante error — lucha productiva

- Al fallar: **se muestra la respuesta correcta inmediatamente** ("Correct solution: gato", footer rojo) y **no se permite reintentar la misma pregunta**; el único camino es CONTINUE. El error tiene costo (corazón) pero el feedback es informativo, no punitivo-puro.
- No hay "ver la respuesta" aparte: el propio error la revela. El SKIP produce equivalente (solución mostrada, sin intento).
- El modal "KEEP GOING" refrasea la pérdida como motivación ("You got this!") — retención emocional en el momento de mayor frustración.

### 3.4 Trazas de red relevantes

Endpoints reales observados durante onboarding + lección (sin responder aún):

- `GET /api/1/courses/list` — catálogo de cursos (2×).
- `POST /2023-05-23/users?fields=id` — **creación de usuario anónimo**; request body con `distinctId` + token reCAPTCHA enterprise (`siteKey 6LcLOdsj…`, ~2.8 KB). Response: solo `{"id": ...}` (22 bytes).
- `GET /2023-05-23/users/{id}?fields=acquisitionSurveyReason,adsConfig,…` — perfil/config masiva del usuario anónimo.
- `GET /2023-05-23/config?fields=…clientExperiments…` — configuración y experimentos.
- `GET /2023-05-23/shop-items`, `GET /2023-05-23/words-list/supported-courses`, `GET /v2/mistakes/users/{id}/courses/DUOLINGO_ES_EN/count`, `GET /users/{id}/streak-goal-current|next-options`, `GET /2017-06-30/friends/users/{id}/profile|recommendations`, `GET /users/{id}/avatar-builder-config` (49 KB), `GET /duolingo-achievements-prod.duolingo.com/users/{id}/achievements`, `GET /goals-api.duolingo.com/users/{id}/quests`.
- Analytics: `POST excess.duolingo.com/batch` (Mixpanel: `course_picker_tap`, `course_selected`, `click`, `time_spent`, `abuse_req_cls_init_success`…) y Sentry.

**Tras responder (correcta o incorrecta): ningún request a duolingo.com** — ni POST de grading, ni PUT de resultado, ni nada (`08-leccion-respuesta-incorrecta.json`, pasos 14–17 del scenario; idéntico en `09`). La única red es analytics.

### 3.5 VEREDICTO — ¿la respuesta correcta viaja al frontend antes del intento?

**Sí: antipatrón confirmado, con matices que lo vuelven razonable.**

- **No viaja por la red en este flujo:** en la carga de la lección no hay ninguna petición que entregue ejercicios (0 requests a duolingo.com en los pasos que abren `/lesson`, `07-…json`; ningún cuerpo de respuesta contiene ejercicios ni soluciones — se revisaron los 124 cuerpos capturados con `response_body: true`).
- **La corrección es 100% del lado del cliente:** existe la clave `duo.clientSideGradingConfig` (+ `.timestamp`) en localStorage en todas las capturas post-onboarding (`05`, `07`, `08`, `09`), y responder no genera tráfico de grading. Los ejercicios de esta lección "Start from scratch" se materializan en el cliente (bundle/config, no observable en red).
- **El DOM visible no delata la solución:** 0 coincidencias de `correct|solution|graded` en el DOM antes de responder (`07`); solo aparece `Correct solution:` después del CHECK, dentro de `[data-test="blame blame-incorrect"]`.
- **Conclusión:** la solución está en el cliente por diseño (client-side grading), accesible a quien inspeccione el estado de la app, aunque no se transmite por la red ni se pinta en el DOM. Para MACI (single-player, sin anti-trampas críticas) esto es un **patrón a copiar**, no un antipatrón grave: ahorra latencia y permite offline; el riesgo (trampas) se mitiga porque el valor pedagógico no está en la evaluación sino en la práctica.

### 3.6 localStorage (valores hasheados por REA — estructura sí visible)

Claves tras el onboarding/lección (`09-leccion-respuesta-correcta.json`, `artifacts.storage`):

- `duo.state` — estado principal de la app (Redux persistido), presente desde la homepage.
- `duo.clientSideGradingConfig` + `duo.clientSideGradingConfig.timestamp` — config de corrección en cliente (ver §3.5).
- `duo.delphi.history.{userId}.DUOLINGO_ES_EN` — historial por curso (motor "delphi").
- `duo.dailyQuests`, `duo.avatarsIntro`, `duo.ageRestrictedLeaderboards`, `duo.sentryThrottling`, `duo.postedAdjustWebUuid`.
- `_grecaptcha`, `adjust-sdk.p`, `_gcl_ls`, `lastExternalReferrer(Time)` — terceros.
- Cookies relevantes: `logged_out_uuid`, `wuuid`, `lu`, `lang`, `tsl` (identificación anónima cross-session).

Los valores los entrega REA como `value_sha256` (redacción por defecto); la estructura de claves es la evidencia útil. El corazón/puntaje en vivo viaja en el estado de la sesión (no en localStorage visible entre pasos).

## 4. Screenshots clave

- `01-homepage.png` — landing sin sesión ("Get started").
- `02-register-selector-idioma.png` — tarjetas de idiomas con data-test.
- `04-onboarding-how-did-you-hear.png` — única pantalla con opción obligatoria.
- `05-funboarding-nivel.png` — radiogroup de nivel.
- `06-funboarding-start-from-scratch.png` — selección de punto de partida.
- `07-leccion-primera-pregunta.png` — **primera pregunta, 5 corazones, barra de progreso, SKIP/CHECK**.
- `08-leccion-opcion-seleccionada.png` — opción elegida, CHECK habilitado.
- `08-leccion-feedback-error-corazones.png` — **feedback de error: "Correct solution: gato", corazón 5→4, modal "Each mistake costs 1 heart!"**.
- `09-leccion-opcion-correcta.png` — opción correcta elegida.
- `09-leccion-feedback-correcto.png` — **feedback "Nice!", barra avanzada, corazones intactos**.
- `10-leccion-skip-solucion-modal.png` — **SKIP: solución revelada ("Correct solution: gato") + modal "Each mistake costs 1 heart!"**.
- `10-leccion-ejercicio2-dog.png` — ejercicio 2 ("dog") tras KEEP GOING + CONTINUE.

## 5. Limitaciones

- Cada escenario REA lanza un browser nuevo: la sesión anónima no persiste entre capturas; cada lección costó repetir ~1 min de onboarding (mitigado con el atajo `/learn`).
- REA redacta (hashea) los valores de storage y headers por defecto: no se pudo inspeccionar el contenido de `duo.state` ni de `duo.clientSideGradingConfig`.
- Los clicks que no resuelven su locator cuelgan hasta el timeout global (600 s) y cancelan el resto del escenario — costó 3 escenarios fallidos (2 por CONTINUE deshabilitado/locator role, 1 por strict-mode). Los locators CSS con nth-child/has-text fueron estables.
- No se llegó a la pantalla final de lección (XP total, streak celebrado, prompt de registro): cada intento de cadena larga que incluía un locator por texto colgaba cuando la pregunta sorteada no lo contenía (el contenido de la primera pregunta varía por sesión: "cat"/"dog"), y 3 escenarios de este tipo se cancelaron por timeout. Los flujos con selectores estructurales (`player-skip`, `player-next`, `hearts-intro-continue-button`) fueron 100% estables.
- Dato no resuelto: tras SKIP + modal, el contador de corazones volvía a mostrar 5 en el ejercicio siguiente (`10-leccion-ejercicio2-dog.png`), mientras que tras un error real marcaba 4 (`08-leccion-feedback-error-corazones.png`). No se pudo determinar si el primer SKIP no descuenta corazón o el indicador se refresca tarde.
- No se observó "streak freeze" (requiere días de actividad) ni hearts refill (tienda, usuario anónimo limitado).
- El orden de las opciones varía por sesión (mamá/papá/gato vs papá/gato/agua vs gato/agua/mamá): la aleatorización es de posiciones, no de contenido.

## 6. Implicancias para MACI (qué copiar sin romper la lucha productiva)

**Copiar de la gamificación/retención:**
1. **Corazones con feedback emocional inmediato:** costo visible por error (−1 corazón con animación) + modal que refrasea ("You got this!") en el punto de máxima frustración. En Datito: un "foco/energía" por intento en evaluaciones, con mensaje de ánimo (no castigo) al perderlo.
2. **Feedback de error que ENSEÑA al instante:** mostrar la solución correcta inmediatamente tras fallar, con la opción de continuar (no reintentos infinitos que estiran la frustración). MACI ya lo hace bien en teoría: copiar el formato "Correct solution: X" sobrio, sin humillación (sin rojo agresivo, sin personaje triste).
3. **Barra de progreso por sesión:** avance visible en cada respuesta (la de Duolingo avanza por ejercicio, no por puntaje).
4. **SKIP explícito:** permitir saltar sin castigo oculto; mostrar la solución y seguir (evita el bloqueo "no sé qué hacer").
5. **Badge de novedad ("NEW WORD"):** marcar contenido nuevo vs repaso — reduce ansiedad y orienta el esfuerzo.
6. **Onboarding con mascota y diálogos cortos:** el funboarding de Duolingo es 100% navegable sin leer: una pregunta por pantalla, CONTINUE siempre en el mismo lugar, barra de progreso propia.
7. **Topbar de estado global:** streak, moneda (lingots), corazones y misiones visibles siempre (`quests-nav` en su topbar) — para MACI: racha de estudio diaria + "puntos Datito" persistentes.
8. **Corrección del lado del cliente (client-side grading):** copiar la arquitectura (cero latencia, offline-friendly), documentando la limitación de seguridad. Para un tutor educativo single-player el riesgo de trampas es aceptable y el beneficio de UX es grande.
9. **Utilidad "Too easy / Too difficult / Report" en cada ejercicio:** micro-feedback de dificultad que alimenta el sistema (en Duolingo va a analítica) — para Datito: señal de dificultad percibida por ejercicio para ajustar la ruta socrática.

**NO copiar:**
- Reintentos bloqueados sin opción (Duolingo fuerza CONTINUE tras error; en el bucle socrático de Datito el reintento guiado es el corazón pedagógico — mantenerlo).
- La solución inmediata sin elaboración: Duolingo muestra "la" respuesta; Datito debe mostrar la respuesta **y** una pista de por qué (la lucha productiva no muere, cambia de forma).
