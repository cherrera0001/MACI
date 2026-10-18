# Síntesis de arquitectura — lo que la evidencia REA cambia en MACI 1.0

**Fecha**: 2026-10-17 · **Base**: `khan.md`, `duolingo.md`, `century.md` (evidencia
canónica con sha256 en esta carpeta). Principio rector: **la evidencia REA manda sobre
el análisis de marketing** (`estado-del-arte.md`) donde se contradicen.

## 1. Patrones de implementación que MACI debe adoptar

### P1. Feedback de error como ACCIÓN graduada, no solo mensaje (Khan — H3)
Tras un intento fallido: "Not quite yet…" + botones **"Show a step"** y **"Try again"**.
La pista es un paso del procedimiento, no la solución. Estado: cada error ofrece una
transición explícita. **Adopción**: refuerza R4; nuevo comportamiento en el orquestador
(ver T065 en tasks.md).

### P2. La solución vive en el cliente y eso está bien (Khan — H2)
Khan precarga la solución completa (0 requests en hints) y aun así sostiene la lucha
productiva con fricción + feedback. Conclusión: **en software educativo local, la
defensa pedagógica es diseño de interacción + registro auditable, no secreto**.
Elimina de raíz cualquier tentación de "proteger" las respuestas de evaluación en
Termito (cifrado, ofuscación): sería complejidad sin beneficio.

### P3. Onboarding narrativo, una decisión por pantalla (Duolingo — H1)
Primera sesión = conversación con la mascota + CONTINUE. **Adopción**: el wizard de 8
componentes (US1) se diseña como diálogo guiado de baja fricción (FR-003/FR-006).

### P4. Contadores de adopción desde el día 1, sin terceros (Duolingo — H2, Century)
Metas/leaderboards/logros se instrumentan antes de la primera lección; Century
condensa el vocabulario: intentos, tiempo, preguntas, racha. **Adopción**:
`progreso.yaml` incorpora `metricas` (sesiones, mensajes, evaluaciones_completadas,
tiempo_minutos, racha_dias) — ajuste mínimo al data model (ver §3). Nada de
leaderboards ni ads: principio VII.

### P5. Content gating + tiempo estimado por unidad (Mathigon)
Pasos bloqueados hasta completar la actividad previa, con "Reveal all steps" como
escape y "Reading time ~10 min". **Adopción**: panel US5 revela el grafo por dominio,
con escape a mapa completo y tiempo estimado por unidad.

### P6. Micro-progreso siempre visible (Khan — H5)
"Do 7 problems" + puntos por unidad corta. **Adopción**: en evaluación y chat, mostrar
unidades cortas de avance (3 distinciones de esta sesión, etc.).

### P7. Fricción mínima pre-evaluación (Khan — H4)
Botón Check deshabilitado hasta input válido. **Adopción**: trivial, UI.

## 2. Antipatrones confirmados por evidencia

### A1. "Seguridad por oscuridad" en el cliente (Khan — H2)
Intentar que el estudiante "no pueda ver" la respuesta en su propia máquina es falsa
seguridad. Documentado como decisión: Termito no oculta soluciones; audita su revelación
(registro de consentimiento, research R4).

### A2. Tracking masivo de terceros desde el primer segundo (Duolingo — H3)
30+ hosts en onboarding. Incompatible con principio VII. No copiar jamás.

### A3. B2B cerrado como único acceso (Century)
El producto no monta sin credenciales institucionales. El diferencial de Termito
(estudiante como diseñador) queda reforzado con evidencia, no solo con opinión.

## 3. Cruce con data-model.md (Fase 1.2)

El modelo actual **soporta** P1 (Mensaje/estado_interaccion), P5 (estado_dominio por
nodo) y P6 (progreso derivado). Ajustes mínimos propuestos (refinamiento, no
reescritura — quedan para la Fase 2 del plan, no para tocar ahora el spec aprobado):

1. `progreso.yaml`: añadir `metricas` {sesiones, mensajes, evaluaciones_completadas,
   tiempo_minutos, racha_dias} — habilita P4.
2. Mensaje: añadir `pasos_revelados` (entero) y permitir `estado_interaccion:
   "paso_mostrado"` entre "pista" y "revision" — habilita P1 con granularidad de
   "mostrar un paso".
3. Curso: añadir `tiempo_estimado_min` por unidad opcional (para P5 en el panel).

Ninguno rompe compatibilidad con contracts/formato-curso.md (campos opcionales
aditivos).

## 4. Decisiones de spec cruzadas (resumen; detalle en research.md §Validación REA)

- **R4 (lucha productiva determinista)**: CONFIRMADA Y REFORZADA por P1/A1.
- **R9 (UI vanilla sin build)**: CONFIRMADA (Mathigon renderiza lecciones ricas con JS
  server-rendered; el valor está en el patrón, no en el framework).
- **R5 (grounded generation), R1–R3, R6–R8, R10**: sin evidencia REA directa
  (los targets no exponen su pipeline de IA/ingesta); se mantienen por rationale
  original. R5 mantiene su limitación honesta ya documentada.

## 5. Lo que quedó NO VERIFICADO (hipótesis, prohibido afirmarlo como hecho)

- Interior de lección de Duolingo (estado, corazones, y si la respuesta correcta
  viaja al frontend) — requiere cuenta; pendiente para una iteración futura.
- Khanmigo (interfaz del tutor IA de Khan) — requiere login.
- Cuerpos de respuesta GraphQL de Khan — Playwright no los retuvo.
