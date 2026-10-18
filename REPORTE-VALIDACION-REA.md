# REPORTE-VALIDACION-REA — Iteración de validación técnica de la spec MACI 1.0

**Fecha**: 2026-10-17 · **Método**: ingeniería inversa con REA (`rea-agents` CLI,
evidencia canónica con sha256) sobre Khan Academy, Duolingo y Century/Mathigon ·
**Alcance**: validar/refinar la spec existente en `specs/001-termito-platform/`
(sin reescribirla) · **Estado**: ✅ condición de parada cumplida

## (a) Qué descubrió REA que web search no podía haber descubierto

Web search da marketing y papers; REA da **implementación real**. Cinco cosas que solo
se ven abriendo el producto:

1. **Los clicks en "Hint" de Khan Academy generan cero requests de red** — la solución
   completa viaja precargada al frontend (evaluación 100% client-side en Perseus).
   Ninguna reseña lo dice; es verificable solo con traza de red.
2. **El feedback de error de Khan es una máquina de estados de UI**: toast "Not quite
   yet…" con botones "Show a step" / "Try again" — la lucha productiva como transición
   explícita, no como tono del mensaje.
3. **Duolingo enciende metas, leaderboards y logros (APIs dedicadas) antes de la
   primera lección** — la retención se instrumenta desde el onboarding, no desde el
   contenido.
4. **La app de Century no monta sin credenciales institucionales** (shell vacío,
   login ausente) — el "B2B cerrado" deja de ser opinión y pasa a ser evidencia
   screenshotteada.
5. **Mathigon bloquea el contenido por progreso** ("complete the activities to reveal
   what's next", dicho por su propio tutor en pantalla) con "Reveal all steps" como
   escape — el content gating como patrón, no como promesa.

## (b) Hallazgos técnicos top 3 (con evidencia)

**H1 — La respuesta correcta vive en el cliente y Khan lo sabe.**
Trazas: `docs/investigacion/rea-evidencia/khan/04-hints-escalera.json` (steps 6–13:
0 requests durante 4 clicks de hint) y `khan/07-flujo-completo.json` (22 pasos, sin
llamadas tras la carga). Renderer Perseus identificado en el DOM
(`khan/dom-ejercicio.html`, clases `perseus-renderer`/`perseus-container`).

**H2 — "Show a step": pista graduada como acción post-error.**
Screenshot `khan/06-feedback-incorrecto.png` (toast "Not quite yet…" + "Show a step" +
"Try after") y DOM `khan/06-feedback-dom.html` (textos confirmados). Es el patrón P1
de `sintesis-arquitectura.md`.

**H3 — Content gating + tiempo estimado + path lineal con nodos.**
`century/mathigon/math3_1.png` (sidebar de pasos con línea de nodos, "Reading time
~10 min", burbuja del tutor "you have to complete the activities to reveal what's
next") + `century/mathigon/mathigon-leccion3-flujo.json` (8 pasos, red limpia:
`mathigon.org` ×51, sin tracking masivo — contraste con `duolingo/03-onboarding-duo.json`:
30+ hosts terceros).

## (c) Decisiones de spec corregidas o reforzadas

| Artefacto | Cambio | Estado |
|---|---|---|
| research.md R4 (lucha productiva determinista) | **Reforzada** por H2/H1; añadida tabla de validación REA de R1–R10 al final del archivo | ✅ editado |
| research.md (nuevo criterio A1) | Corrección de enfoque: no gastar esfuerzo en ocultar respuestas al estudiante en su propia máquina; la defensa es fricción + registro auditable | ✅ añadido en síntesis |
| tasks.md | T065 (mostrar un paso), T066 (micro-progreso), T067 (contadores de adopción), T068 (gating del grafo) | ✅ añadidos |
| contracts/api.md | `estado_interaccion` gana `paso_mostrado` + campo `paso{numero,total}` (aditivo) | ✅ editado |
| quickstart.md | Escenarios 1–2 incorporan onboarding narrativo y feedback-acción graduado | ✅ editado |
| data-model.md | Propuesta mínima documentada en `sintesis-arquitectura.md` §3 (`metricas`, `pasos_revelados`, `tiempo_estimado_min`) — se aplica en la fase de diseño, no ahora | 📋 propuesta |
| R9 (UI vanilla) | **Confirmada** (Mathigon) | ✅ |
| research.md R1–R3, R5–R8, R10 | Sin evidencia REA directa; se mantienen por rationale original | ✅ documentado |

Detalle del cruce: `docs/investigacion/rea-evidencia/sintesis-arquitectura.md` §4 y
`research.md` §Validación REA.

## (d) Riesgo #1 revelado por REA y cómo lo evita MACI

**Riesgo**: la tentación de "proteger" las respuestas de evaluación del estudiante
(ocultarlas, cifrarlas, servirlas solo al calificar). REA demuestra que en el modelo
client-side esto es **falsa seguridad**: Khan —con decenas de millones de usuarios—
entrega la solución completa con el ejercicio y aun así sostiene la lucha productiva,
porque su defensa es el **diseño de interacción** (un paso por click, feedback
inmediato, reintento) y la **auditabilidad** (uso de hints registrado), no el secreto.

**Cómo lo evita MACI**: Termito adopta el mismo modelo de confianza (las soluciones
viven en los archivos del curso del estudiante) y concentra el esfuerzo donde REA
demostró que funciona: máquina de estados determinista (R4 + T065), revelación
consentida registrada (FR-008), y registro de dudas con evidencia (FR-010). Cero
complejidad criptográfica; máxima auditabilidad. Coherente con la constitución
(principio III y VII).

## Evidencia no obtenida (marcada "no verificado — hipótesis", prohibido afirmarla)

- Interior de lección de Duolingo (corazones/racha/respuesta-en-frontend) — requiere
  cuenta. Pendiente iteración futura.
- Khanmigo — requiere login.
- Cuerpos de respuesta GraphQL de Khan — Playwright no los retuvo (limitación).

## Comandos exactos para retomar mañana

```bash
# El backlog ya incluye los refinamientos REA (T065–T068): implementar en orden,
# con T065 junto a la fase 4 (es el refuerzo pedagógico más valioso de esta iteración):
grep -n "T065" specs/001-termito-platform/tasks.md

# Ver la evidencia REA de un hallazgo concreto (ej. H2):
#   docs/investigacion/rea-evidencia/khan/06-feedback-incorrecto.png
# Re-ejecutar una captura REA si se necesita verificación adicional:
#   npx rea-agents capture-browser-scenario "$(cat escenario.json)" --format json > ev.json

# Flujo normal Spec Kit:
#   /speckit-implement        (lee .specify/feature.json → specs/001-termito-platform/)
#   /speckit-analyze          (consistencia cruzada tras los edits de hoy)
```

**Resumen**: la spec se refinó sin reescribirse; lo que cambió es dónde poner el
esfuerzo pedagógico (interacción auditable, no secreto) y cuatro tareas concretas
(T065–T068) respaldadas por evidencia técnica real.
