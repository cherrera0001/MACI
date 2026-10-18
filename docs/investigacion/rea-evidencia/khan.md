# Target A — Khan Academy (khanacademy.org): práctica, hints y feedback

**Fecha**: 2026-10-17 · **Método**: REA CLI `capture-browser-scenario` (Playwright con
Chromium 151, evidencia canónica con sha256 por captura) · **Estado**: ✅ completo
(flujo de ejercicio sin login; Khanmigo no inspeccionado — requiere cuenta)

## URLs inspeccionadas

- `https://www.khanacademy.org/math/arithmetic/x18ca194a:1-digit-multiplication/...`
  (ejercicio interactivo, renderer Perseus)
- `https://www.khanacademy.org/math/arithmetic/x18ca194a:intro-to-multiplication/...`
  (mismo ejercicio tipo "elige 2 respuestas")

## Capturas (evidencia en esta carpeta)

| Archivo | Escenario | Contenido |
|---|---|---|
| `01-home.json` | home | carga portal |
| `04-hints-escalera.json` | 14 pasos | 4 clicks de hint con screenshot por paso |
| `05-dom-ejercicio.json` | 6 pasos | DOM completo del ejercicio (`dom-ejercicio.html`, 541 KB) |
| `06-respuesta-incorrecta.json` | 11 pasos | flujo respuesta incorrecta + trazas de red con cuerpos |
| `07-flujo-completo.json` | 22 pasos | error + escalera completa de 5 pasos de hint |
| PNGs | — | `06-feedback-incorrecto.png`, `shot-0*.png`, `05-matcher.png` |

## Hallazgos técnicos

### H1. El renderer de ejercicios es Perseus y evalúa en el cliente
El DOM del ejercicio está dominado por clases `perseus-renderer`, `perseus-container`,
`perseus-renderer-responsive`, `perseus-block-math` (extraídas de `dom-ejercicio.html`).
Los ejercicios se evalúan localmente en el navegador; la API principal es
`/api/internal/graphql` (15 llamadas en la captura 04) más beacons `_analytics` y `_bb`.

### H2. ANTIPATRÓN CONFIRMADO: la solución completa viaja al frontend
**Los clicks en "Hint" generan cero requests de red.** Verificado en `04-hints-escalera.json`
(steps 6–13: 0 requests cada uno) y consistente en `07-flujo-completo.json` (todo el flujo
error+hints sin llamadas tras la carga inicial). La escalera de pistas —que termina
revelando la solución paso a paso— ya está precargada en el cliente con el ejercicio.
Khan acepta que cualquiera con DevTools pueda leer la respuesta: su defensa anti-trampa
NO es el secreto, es la fricción por granularidad (un paso por click) más el feedback
inmediato. (Limitación: Playwright no retuvo los cuerpos de las respuestas GraphQL —
189 `unavailable` — así que la clave literal `"correct"` no es observable en las trazas;
la conclusión se sostiene por la ausencia total de red durante los hints y por la
arquitectura Perseus, pública y documentada.)

### H3. El feedback de error es una acción, no solo un mensaje
`06-feedback-incorrecto.png` + `06-feedback-dom.html`: al responder mal, un toast
embebido en la misma vista dice **"Not quite yet... Give it another try!"** con dos
botones: **"Show a step"** (pista graduada, no la solución completa) y **"Try again"**.
El DOM confirma los textos ("Not quite", "Show a step", "Try again"). La lucha productiva
está implementada como transición de estado explícita del UI post-error.

### H4. Fricción mínima antes de evaluar
El botón **Check** está deshabilitado (gris) hasta que el estudiante selecciona al menos
una opción (`05-matcher.png`): no se puede "enviar vacío".

### H5. Micro-progreso siempre visible
Barra inferior con **"Do 7 problems"** y 7 puntos que se van completando
(`shot-06-hint-1.png`), sidebar con estructura del curso (Unidad → Lección → Videos/
Ejercicios), botón "Skip" disponible. Progreso por unidades de esfuerzo cortas.

### H6. Cero errores de página
0 page-errors y 0 responses ≥400 en todas las capturas: el flujo anónimo es estable y
completamente usable sin cuenta.

## Trazas de red relevantes (captura 04, 198 requests)

- `khanacademy.org/api/internal/graphql` ×15 (datos de contenido/perfil)
- `khanacademy.org/api/internal/_analytics` ×6, `_bb` ×3
- Bundles: `cdn.kastatic.org/khanacademy/khanacademy.*.js`, `runtime.*.js`
- Anti-bot: challenge F5 (`_fs_ch-*`) presente pero no bloqueante para el flujo

## Limitaciones

- Khanmigo (el tutor IA) requiere login: **no inspeccionado**.
- No se capturó lección con input numérico/editor de expresiones (solo "elige N").
- Cuerpos de respuesta GraphQL no retenidos por la herramienta.

## Implicancias para MACI/Termito

1. **Copiar el patrón "mostrar un paso"**: tras un intento fallido, el feedback debe
   ofrecer una acción de pista graduada ("mostrar un paso") junto a "intentar de nuevo",
   no solo texto socrático (refuerza R4; tarea nueva en tasks.md).
2. **No gastar esfuerzo en ocultar respuestas**: en software educativo client-side la
   solución vive en la máquina del estudiante; la defensa es interacción + registro
   auditable, no criptografía (confirma que FR-008/R4 apuntan al lugar correcto).
3. **Check deshabilitado hasta input válido**: fricción de un click que evita envíos
   vacíos y "clicks de prueba".
4. **Progreso por unidades cortas visibles**: los puntos "Do N problems" son el
   equivalente micro del panel de dominio (US5) — vale para el quickstart.
5. Perseus es open-source: considerado como renderer de ejercicios para Termito;
   descartado para el MVP por ser React (incoherente con research R9 vanilla).
