# Research: MACI 1.0 — Plataforma Datito

**Fecha**: 2026-10-17 · **Feature**: `specs/001-datito-platform` · **Estado**: completo
(sin marcadores NEEDS CLARIFICATION pendientes)

Resolución de las decisiones técnicas abiertas del plan. Formato por decisión:
Decisión / Rationale / Alternativas consideradas.

---

## R1. Servidor local: FastAPI + uvicorn

- **Decisión**: API local con FastAPI, servida por uvicorn en `127.0.0.1`.
- **Rationale**: validación automática de esquemas (contratos testeables), soporte async
  (llamadas al LLM local en paralelo con la interfaz), documentación OpenAPI generada
  que alimenta `contracts/api.md`. La UI sigue siendo HTML/JS estático servido por el
  mismo proceso: coherente con el sitio estático actual y sin paso de build.
- **Alternativas consideradas**: `http.server` stdlib (cero dependencias pero sin
  validación, más código manual y errores); Flask (síncrono, menos estructura de
  contratos). Descartadas por costo de mantenimiento.

## R2. Runtime de LLM: Ollama (local por defecto)

- **Decisión**: Ollama como runtime por defecto, vía su API HTTP en `localhost:11434`
  (compatible con el SDK de OpenAI, que se usa también para el modo nube opcional).
- **Rationale**: gestión de modelos multiplataforma, modelo abierto pequeño/mediano
  (orden de 3–8B cuantizado) que corre en CPU con <4 GB; un solo punto de cambio si el
  estudiante configura nube (mismo SDK). El sistema detecta si Ollama no está y entra
  en "modo exploración de materiales" (edge case del spec).
- **Alternativas consideradas**: llama.cpp directo (más bajo nivel, más fricción de
  gestión de modelos); LM Studio (excelente GUI pero poco scriptable). El contrato
  `LLMProvider` aísla el runtime: cambiar no afecta al resto del sistema.

## R3. Embeddings e índice: fastembed + numpy, índice como caché regenerable

- **Decisión**: embeddings con fastembed (modelos ONNX en CPU, sin torch, offline) y
  búsqueda por similitud coseno en numpy. Los vectores se guardan en un manifiesto
  JSON + `.npy` dentro de `cursos/<slug>/.indice/`, regenerables desde los fragmentos.
- **Rationale**: para corpus de tamaño curso universitario (<50k fragmentos), búsqueda
  exhaustiva en numpy es suficiente (<100 ms) y elimina una dependencia pesante
  (FAISS/Chroma). La fuente de verdad son los fragmentos en Markdown; el índice es un
  artefacto derivado, coherente con la restricción constitucional de archivos legibles
  (nada opaco como almacenamiento primario).
- **Alternativas consideradas**: sentence-transformers (mejor calidad pero +1 GB de
  dependencias); FAISS/Chroma (dependencia extra innecesaria a esta escala);
  búsqueda por palabras clave sin embeddings (no captura sinonimia ni parafraseo, y la
  calidad de la evidencia es crítica para el principio II).

## R4. Lucha productiva: máquina de estados en código, no en el prompt

- **Decisión**: el comportamiento "pista → intento → revisión → (revelación solo con
  consentimiento informado)" se implementa como máquina de estados determinista en la
  capa de orquestación (`tutor/`), no como instrucción del prompt. El LLM genera
  pistas y retroalimentación, pero la decisión de revelar la solución la toma el
  código, que además registra cada excepción.
- **Rationale**: los principios III y II son auditables y testeables solo si la lógica
  es determinista. Un prompt puede ser ignorado por el modelo; una transición de
  estado no. Esto hace SC-003 verificable.
- **Alternativas consideradas**: confiar en el system prompt (no auditable, falla
  silenciosamente); hardcodear pistas en la ingesta (rompe la adaptación al estilo,
  principio X).

## R5. Evidencia citada: generación anclada a fragmentos (grounded generation)

- **Decisión**: el tutor genera sus respuestas **solo** a partir de los fragmentos
  recuperados por el índice; cada fragmento tiene identificador estable y referencia
  direccionable (fuente + página/timestamp). La respuesta se estructura como
  afirmación + lista de ids de fragmento que la sustentan. La capa de orquestación
  verifica que toda afirmación sobre el curso cite ids existentes antes de renderizar;
  si la recuperación no arroja fragmentos, el tutor responde con la plantilla
  "sin fuente en los materiales" (o marca "fuera del curso" si el estudiante lo pide).
- **Rationale**: convierte SC-002 (100% de afirmaciones con evidencia o declaración
  explícita) en una propiedad estructural del sistema y no en una promesa del modelo.
- **Alternativas consideradas**: pedir al LLM que "cite sus fuentes" en texto libre
  (alucina citas plausibles, inaceptable bajo el principio VI); post-validación por
  segundo LLM (costo, latencia y un segundo modelo que también puede fallar).
- **Limitación honesta**: la pertinencia de la evidencia (que el fragmento cite
  realmente sustente la afirmación) depende del modelo; se mitiga con recuperación
  top-k estricta y con que las referencias siempre existen y son verificables por el
  estudiante con un clic.

## R6. Migración incremental desde v0.0.1: adaptador, no reescritura

- **Decisión**: un adaptador de importación (`ingestor/legacy_maci.py`) convierte los
  artefactos actuales (`07_DATITO/clases.yaml`, `grafo.yaml`, bitácoras, visuales y
  transcripciones) en una instancia `cursos/fundamentos-ciencia-datos/`. El sitio
  estático actual y `publicar_sitio.mjs` siguen intactos y operativos durante toda la
  migración; el primer Datito real se construye sobre los mismos YAML.
- **Rationale**: la constitución prohíbe big-bang y exige que cada incremento deje el
  sistema operativo. SC-007 (cero regresiones en funcionalidades v0.0.1) se verifica
  corriendo la verificación existente (`verificar_todo.py`) antes y después.
- **Alternativas consideradas**: reescribir el curso a mano (error-prone, rompe la
  fuente única); hacer que el runtime lea directamente `07_DATITO/` para siempre
  (acopla la plataforma al layout de un solo curso y viola IX).

## R7. Versionado del prompt: archivos planos con manifiesto

- **Decisión**: cada versión del prompt se guarda en
  `cursos/<slug>/prompt/versions/YYYYmmdd-HHMMSS.md` con un manifiesto YAML (qué
  componentes cambiaron, motivo). Revertir = copiar una versión anterior como actual.
- **Rationale**: el estudiante no debe saber git para recuperar su agente; los archivos
  diffs-eables cumplen la restricción de archivos legibles y versionables.
- **Alternativas consideradas**: git programático sobre el directorio del curso (fricción
  y sorpresas para usuarios no técnicos); un solo archivo con historial embebido
  (difícil de revisar y restaurar).

## R8. Testing: unittest (convención del repo)

- **Decisión**: tests con `unittest` del stdlib, descubribles por
  `python -m unittest discover -s 15_TERMINITO/tests`, integrables a la CI existente
  sin cambios.
- **Rationale**: coherencia con `04_CODIGO/test_*.py` y con el único workflow de CI
  actual (instala solo pyyaml hoy; pytest sería dependencia nueva). La constitución
  exige tests para nueva lógica, no un framework específico.
- **Alternativas consideradas**: pytest (más ergonomía, pero nueva dependencia de
  desarrollo; unittest cubre el alcance).

## R9. UI: HTML/JS estático sin build, español primero

- **Decisión**: interfaz web en HTML + JavaScript vanilla servida por la API local,
  cadenas externalizadas en `i18n/es.json` e `i18n/en.json`. Sin framework, sin
  bundler.
- **Rationale**: coherencia con el sitio v0.0.1 (offline-first, autocontenido),
  cero toolchain nuevo, cumplimiento directo del principio VIII.
- **Alternativas consideradas**: React/Vue con build (paso de compilación, node_modules,
  fragilidad offline); TUI en terminal (menor accesibilidad para usuarios no técnicos).

## R10. Video y transcripción: transcripciones provistas + whisper opcional

- **Decisión**: el MVP acepta transcripciones en `.txt/.srt/.vtt` asociadas a cada
  video, con timestamps preservados para la evidencia. Si el usuario tiene whisper.cpp
  instalado, el sistema puede transcribir localmente; si no, lo indica en el resumen
  de ingesta.
- **Rationale**: embeber un modelo de transcripción multiplica el peso de la
  instalación (~1.5 GB+) y no es esencial para el MVP (SC-001–SC-005 no dependen de
  ello). El edge case del spec (video sin transcripción) queda explícito.
- **Alternativas consideradas**: whisper vía Ollama (modelo grande para CPU modesta);
  servicio de transcripción en nube (viola VII por defecto).

## Síntesis de riesgos técnicos

| Riesgo | Mitigación |
|---|---|
| Calidad del modelo local pequeño en español | Elegir modelo con fuerte soporte es (evaluar en quickstart.md); nube opcional como válvula |
| Recuperación de evidencia poco relevante | Top-k estricto, fragmentos pequeños, metadatos de tema; el estudiante verifica con un clic |
| Latencia en CPU modesta | Modelo 3–4B cuantizado Q4; streaming de respuestas; objetivo <10 s primera respuesta |
| Pérdida de portabilidad por artefactos derivados | Todo derivado se regenera con un comando (`datito reindexar`) |
| Ollama no instalado | Modo degradado explícito de exploración de materiales + instrucciones de instalación |


---

## Validación REA (2026-10-17) — cruce de decisiones R1–R10 con evidencia técnica

Evidencia: `docs/investigacion/rea-evidencia/` (khan.md, duolingo.md, century.md,
sintesis-arquitectura.md). Regla: la evidencia REA manda sobre este documento donde se
contradigan.

| Decisión | Veredicto | Base |
|---|---|---|
| R1 FastAPI + servidor local | Sin evidencia REA directa (los targets no exponen su backend); el patrón API+SPA cliente es consistente con lo observado en Khan (`/api/internal/graphql`) y Duolingo (`excess.duolingo.com`). Se mantiene. | khan.md H1; duolingo.md H2 |
| R2 Ollama local por defecto | Sin evidencia REA (ningún target es local-first). Se mantiene por principio VII. | — |
| R3 fastembed + numpy | Sin evidencia REA. Se mantiene. | — |
| R4 Lucha productiva como máquina de estados determinista | **CONFIRMADA Y REFORZADA.** Khan implementa exactamente eso: feedback post-error con acciones "Show a step"/"Try again" = transiciones explícitas; y su defensa anti-trampa es interacción + registro, no secreto (A1). | khan.md H2/H3; sintesis P1/P2 |
| R5 Grounded generation anclada a fragmentos | Sin evidencia REA directa (ningún target citó fuentes; Khan no cita). Se mantiene con su limitación honesta. | — |
| R6 Migración incremental v0.0.1 | Sin evidencia REA. Se mantiene. | — |
| R7 Versionado de prompt en archivos planos | Sin evidencia REA. Se mantiene. | — |
| R8 unittest | Sin evidencia REA. Se mantiene. | — |
| R9 UI vanilla HTML/JS sin build | **CONFIRMADA.** Mathigon entrega lecciones interactivas y gating con JS sobre contenido server-rendered; el valor pedagógico está en los patrones (P1/P5), no en el framework. | century.md §Mathigon; sintesis P5 |
| R10 Video por transcripciones provistas | Sin evidencia REA. Se mantiene. | — |

**Corrección derivada de la evidencia** (no contradice R1–R10, las refina): los
patrones P1 (feedback-acción), P4 (contadores), P5 (gating) y P6 (micro-progreso)
quedan incorporados al backlog como T065–T068 (ver impacto-tasks.md) y a los ajustes
de contratos/quickstart de esta misma fecha.
