# Target C — Century Tech: BLOQUEADO (B2B) + sustituto Mathigon

**Fecha**: 2026-10-17 · **Método**: REA CLI `capture-browser-scenario` · **Estado**:
Century **descartado como inspección de producto** (autenticación institucional
inalcanzable); evidencia sustituta de Mathigon (frontend accesible) incorporada.

## Century Tech: veredicto de bloqueo (evidenciado)

- `https://app.century.tech/` → el shell de la app **carga pero queda vacío**
  (`app-shell.century-tech.json`; `screenshot-02-app-shell-vacia.png`, 4 KB = viewport
  esencialmente en blanco).
- `https://app.century.tech/login/` → la pantalla de login **no monta**
  (`app-login-no-monta.century-tech.json`; `screenshot-03-app-login-no-monta.png`, 4 KB).
  Consola: solo warnings de "Service Worker registration blocked by Playwright" — sin
  errores de app, es decir, el cliente espera credenciales/contexto institucional que
  un usuario anónimo no tiene.
- Conclusión: **producto 100% B2B cerrado**. El estudiante individual no puede ni
  entrar. Esto es en sí un hallazgo estratégico: confirma el diferencial de Termito
  (diseñado por y para el estudiante).

### Century — marketing (etiquetado: NO es inspección de producto)

`screenshot-05-marketing-dashboard-progreso.png` y `marketing-*.json` (landing pública):

- Dashboard con tarjetas de métricas: **"16 nuggets attempted"**, **"2hr 41m time spent
  studying"**, **"142 questions answered"**, **"LONGEST STREAK 1 week"**, avatar con
  nivel "3", badges con candado (gamificación por desbloqueo).
- La unidad de contenido se llama **nugget** (micro-lección); combinaciones de
  slideshow + video + ejercicios de opción múltiple con feedback "Correct Answer".
- Copy orientado a padres/docentes ("dashboard can be shared with parents").

Uso permitido: vocabulario de métricas y lenguaje de visualización. Nada de lo
mostrado está verificado contra producto real.

## Sustituto inspeccionado: Mathigon (mathigon.org) — evidencia real

Cursos interactivos abiertos, sin login. Evidencia en `mathigon/`:

| Archivo | Contenido |
|---|---|
| `mathigon-leccion3-flujo.json` (8 pasos) | lección con skips y pasos |
| `math3_0.png` … `math3_7.png` | estados de la lección |

### Hallazgos Mathigon

1. **Path lineal de pasos con nodos** (`math3_1.png`): sidebar izquierda con la
   secuencia vertical de la lección (Introduction → The Bridges of Königsberg →
   Handshakes and Dating → …), cada paso es un nodo en la línea. No es un grafo de
   prerrequisitos: es un *stepper* narrativo.
2. **Content gating explícito** (`math3_1.png`, burbuja del tutor "Archie"): *"Our
   content is divided into small steps. You have to complete the activities to reveal
   what's next."* El avance está bloqueado por completar actividades; existe "Reveal
   all steps" como escape.
3. **Tiempo de lectura estimado por unidad**: "Reading time: ~10 min" visible arriba.
4. Hosts de red limpios (`mathigon.org` ×51 + fuentes): coherente con una app sin
   tracking masivo — contraste directo con Duolingo (H3 allí).

## Implicancias para MACI/Termito

1. **Gating por progreso en el panel US5**: revelar conceptos del grafo conforme se
   completa lo previo (Mathigon), no mostrar todo de golpe — con "revelar todo" como
   escape para el estudiante que quiere el mapa completo.
2. **Tiempo estimado por unidad** en el panel de dominio (micro-copy que reduce
   ansiedad ante el grafo).
3. **Métricas tipo Century** (intentos, tiempo, preguntas, racha) como contadores en
   `progreso.yaml` — ver P4 en `sintesis-arquitectura.md`.
4. La visualización de Century/Mathigon es **lineal**; el diferencial del grafo de
   prerrequisitos de Termito (US5) queda reforzado: nadie inspeccionado lo hace.
