# 07 · DATITO — Tutor personal de Fundamentos de Ciencia de Datos

Datito **no explica conceptos: entrena resolución de problemas.** La prueba es
escrita, sin Internet, y el criterio de avance es cuántos problemas resuelves
**solo** — no cuánto contenido se te explicó.

Contrato completo y garantías verificables: [`../spec.md`](../spec.md).

---


> **¿Quieres entender cómo está construido, no cómo se usa?**
> [`ARQUITECTURA.md`](ARQUITECTURA.md) — componentes, los tres planos de
> datos, qué invariantes lo sostienen y qué cuesta cada decisión.

## Cómo se usa

Abre Claude Code en `F:\MACI` y habla:

```
Datito, quiero entender validación cruzada
```

| Comando | Qué hace | Dónde corre |
|---|---|---|
| `/datito` | Sesión de estudio: problema → tu respuesta → diagnóstico | Conversación |
| `/datito-progreso` | Informe de estado. Solo lectura | Conversación |
| `/datito-visual <concepto>` | HTML **solo** desde `_TEMPLATE_CANONICO.html` | Aislado |
| `/datito-loop` | Aprende de errores de construcción (keep/discard) | Aislado |
| `/datito-corregir` | Corrige un lote de respuestas escritas | Aislado |

Template canónico y learning loop: `07_DATITO/07_BITACORA/learning_loop/WORKFLOW_VISUAL.md`.

### Por qué dos corren aislados y dos no

El tutor **no puede** ser un subagente: un subagente no sabe pausar y esperar tu
respuesta, y ese es su núcleo. En cambio corregir un lote y construir un
artefacto no necesitan esperarte, así que corren en contexto propio y no gastan
el de la sesión.

---

## Estructura

```
07_DATITO/
├── 00_INICIO/               bienvenida, arquitectura, estado, curriculum
│   ├── 00_LEEME.md              este archivo
│   ├── ARQUITECTURA.md           componentes, planos de datos, invariantes
│   ├── datito.config.yaml        DATOS del alumno. Las reglas viven en la skill
│   ├── curriculum.yaml           21 conceptos: orden, prerrequisitos, material
│   ├── clases.yaml               22 clases, unidades, cierre de aprendizaje
│   ├── progreso.yaml             estado y cadena de evidencia ← lo escribe Datito
│   ├── errores_conceptuales.yaml errores observados ← ídem
│   ├── estado.md                 resumen autogenerado, se inyecta en sesión
│   ├── dudas.yaml                respuestas de Datito, se renderizan en visuales
│   └── grafo.yaml                relaciones conceptuales
│
├── 01_CONCEPTOS/            los 21 conceptos en orden del curriculum
│   └── visual/                   HTML interactivos (01_fundamentos.html → 19_deep_learning.html)
│       └── 00_index.html         portada: 22 clases, navegación, síntesis
│
├── 02_REFERENCIA/           fuentes, documentación, material externo
│   ├── fuentes.md               jerarquía de prioridad, etiquetado, NotebookLM
│   ├── material.md              prácticos, certámenes, proyectos Melbourne/Galaxy Zoo
│   ├── memoria.md               estados, cadena de evidencia, qué y dónde escribir
│   └── clase6_regresion.html    material adicional de referencia
│
├── 03_CASOS_ESTUDIO/        aplicaciones con herramientas dinámicas
│   ├── cancer_mama/             diagnóstico de mama: matriz confusión real, 3 modelos
│   ├── RESUMEN_INTEGRACION.md   síntesis de cómo integran caso y concepto
│   └── [futuros casos]
│
├── 04_EJERCICIOS/           problemas, certámenes, entregas
│   ├── cuadernillos/            problemas CON solución — enseñan
│   ├── guias/                   material escrito: temas claves
│   ├── certamenes/              certámenes sin solución — miden
│   ├── entregas/                donde dejas respuestas para corregir
│   └── *.html                   dinamicos: triaje, simuladores, certámenes HTML
│
├── 05_TRANSFERENCIA/        datasets y scripts de otro dominio
│   ├── generar_dataset.py       generador sintético de problemas
│   ├── 00_CONTEXTO.md           definición y uso
│   └── entregas_*.csv           datasets de años anteriores
│
├── 06_AUDITORIAS/           verificación pedagógica, artefactos
│   ├── auditoria_pedagogica.md      checklist de enseñanza
│   ├── auditoria_adversarial.md     casos extremos de fuga, overfitting
│   ├── auditoria_artefactos.md      validación de los HTML visuales
│   └── patron_evaluacion.md         cómo evalúa el profesor desde sus certámenes
│
├── 07_BITACORA/             una entrada por sesión
│   └── YYYY-MM-DD-concepto.md
│
├── 08_SCRIPTS/              scripts centralizados (si existen)
│
└── 09_PERSONAL/             datos del alumno, OSINT, investigación privada
    └── osint_*.md               investigación de fuentes públicas (en pausa)
```

---

## Lo que ya puedes abrir

### Visuales interactivos — `01_CONCEPTOS/visual/`

**Empieza por [`01_CONCEPTOS/visual/00_index.html`](../01_CONCEPTOS/visual/00_index.html)**: la portada del curso.
Son 22 clases en 6 unidades, ordenadas por prerrequisitos (fuente única:
[`clases.yaml`](clases.yaml)); cada una abre con objetivo, ficha Bloom y
activación, y cierra con síntesis, procedimiento y pregunta final. Incluye el
repaso del certamen y las dudas resueltas. Todo abre con doble clic, sin Internet.

| # | Archivo | Concepto |
|---|---|---|
| 1 | `01_fundamentos.html` | Qué problema resuelve la ciencia de datos; data-driven; Big Data; el ciclo |
| 2 | `02_datos_features_target.html` | Fila, columna, feature, target, identificador y fuga de información |
| 3 | `03_eda.html` | Centralidad, extensión, distribución, correlación, integridad visual |
| 4 | `04_limpieza_preparacion.html` | Calidad de datos sobre la tabla real de la 9B; limpiar ≠ decidir modelado |
| 5 | `05_train_validation_test.html` | Los tres conjuntos y por qué el test se guarda |
| 6 | `06_validacion_cruzada.html` | Holdout, bootstrap, submuestreo y K-Fold |
| 7 | `07_generalizacion.html` | Datos no vistos: interpolar, extrapolar, cambio de distribución |
| 8 | `08_overfitting_underfitting.html` | La curva de complejidad y el diagnóstico por la brecha |
| 9 | `09_regresion.html` | La Clase 6 completa: la función de costo y MAE |
| 10 | `10_clasificacion.html` | Cuando la etiqueta no es un número |
| 11 | `11_matriz_confusion.html` | Construir y leer la matriz; el ejercicio de 100 pacientes del profesor |
| 12 | `12_metricas_clasificacion.html` | Exactitud, precisión, recall, F1: el denominador |
| 13 | `13_roc_auc.html` | Umbral, punto de operación, curva ROC y AUC |
| 14 | `14_arboles_decision.html` | Árboles de decisión, Random Forest, boosting y ensambles |
| 18 | `18_redes_neuronales.html` | Perceptrón y entrenamiento |
| 19 | `19_deep_learning.html` | Deep learning, LLM y agentes |

**Especiales** (en `04_EJERCICIOS/` y casos de estudio):
- `certamen_1.html` · `certamen_2.html` — Los certámenes auditados pregunta por pregunta
- `triaje_de_problemas.html` — Qué tipo de problema tengo delante
- `simulador_prediccion_falla.html` — Herramienta dinámica para explorar umbrales
- Caso estudio `cancer_mama/matriz_confusion_dinamica.html` — Matriz interactiva de 114 pacientes

Cada visual cita la clase donde se enseñó con ruta completa y marca de tiempo.
La barra superior de cada uno la genera `03_SCRIPTS/construir_navegacion.py`.

### Material escrito

- `04_EJERCICIOS/guias/overfitting_underfitting.md` — los dos criterios, la inversión de métrica, remedios por mecanismo, procedimiento de siete pasos
- `04_EJERCICIOS/cuadernillos/01_sobreajuste_y_calidad_de_datos.md` — nueve problemas con solución plegable, en los formatos del profesor

---

## Estudiado no es comprendido

Seis estados:

| Estado | Significado |
|---|---|
| `NO_ESTUDIADO` | No visto |
| `EN_ESTUDIO` | Datito lo explicó. Nada verificado |
| `COMPRENSION_PARCIAL` | Lo explicas con huecos, o el mecanismo incompleto |
| `COMPRENDIDO` | Explicas y aplicas correctamente |
| `DOMINADO` | Explicas, aplicas, interpretas **y** transfieres |
| `REQUIERE_REPASO` | Lo sabías y fallaste en una re-verificación |

### La cadena de evidencia

```
EXPLICAR  →  APLICAR  →  INTERPRETAR  →  TRANSFERIR
```

`DOMINADO` exige las cuatro. **Decir "entendí" no es evidencia de nada**, y
Datito tiene instrucción explícita de no aceptarlo. Tampoco cuenta repetir su
explicación, ni acertar tras una pista fuerte, ni acertar por el motivo
equivocado.

### Tres niveles de problema

| Nivel | Qué es | Acredita |
|---|---|---|
| 1 · Reconocimiento | Del mismo tipo que usa el profesor | — |
| 2 · Aplicación | Mismo concepto, cambian números o representación | `APLICAR` |
| 3 · Transferencia | Otro dominio, tú descubres qué aplica | `TRANSFERIR` |

---

## Cómo evalúa tu profesor

Detalle en [`06_AUDITORIAS/patron_evaluacion.md`](../06_AUDITORIAS/patron_evaluacion.md). El hallazgo central:

**Las 11 fichas del Certamen 2 comparten un mismo campo sin excepción:
*distinción conceptual clave*.** Cada pregunta se resuelve separando dos
conceptos vecinos — número de modelos ≠ diversidad, más filas ≠ más columnas,
precisión ≠ sensibilidad, comparar un punto ≠ comparar un modelo.

**No evalúa definiciones. Evalúa discriminación.**

Peso por bloque:

| Bloque | Peso |
|---|---|
| Sobreajuste, generalización, validación, ensambles | **36 %** |
| Métricas de clasificación | **27 %** |
| Panorama de IA: LLM, agentes, redes | 18 % |
| Conducta metodológica | 18 % |

Y en el Certamen 1, la pregunta 9B de calidad de datos **vale 2,0 puntos** por
sí sola: la mitad de lo que suman las ocho cerradas juntas (4,0) y la pregunta
individual de mayor puntaje.

---

## Fuentes

| Prioridad | Fuente |
|---|---|
| 1 | Laboratorios del curso — `06_LABORATORIOS/`, 12 de los 21 conceptos |
| 2 | Transcripciones de clase — `05_CLASES/` |
| 3 | Material FCD del repositorio |
| 4 | Cuaderno de NotebookLM |
| 5 | Proyectos propios: Melbourne, Galaxy Zoo |
| 6 | Fuentes académicas externas |

Toda afirmación lleva etiqueta: `[FUENTE · NotebookLM: …]`, `[FUENTE · Repo: …]`,
`[INFERENCIA]` o `[DATITO]` para explicación pedagógica propia.

Las transcripciones se citan con la ruta completa del `.md` y la marca de tiempo,
nunca el `_plano.txt`. Si contradicen una lámina o un práctico, manda el material
oficial. Y solo las clases del profesor titular entran al certamen: «Entran solo
mis clases. No entran las clases de Alejandra» (`05_CLASES/transcripciones/03Clase_Recuperación_…_15_julio.md`, 1:18:16).

### Material de terceros

`01_DOCUMENTACION/06_CERTAMEN1/` procede de un compañero. Los **enunciados** son
fiables; las **justificaciones no están verificadas** — el documento se titula
"Pauta Oficial" pero cierra con campos de plantilla sin rellenar.

---

## Mantenimiento

Tras cada sesión, Datito regenera el resumen que se inyecta la próxima vez:

```bash
python 03_SCRIPTS/datito_estado.py
```

Transcribir una clase nueva e integrarla a los visuales:

```bash
uv run --with faster-whisper python 03_SCRIPTS/transcribir_clases.py --listar
uv run --with faster-whisper python 03_SCRIPTS/transcribir_clases.py --todas
python 03_SCRIPTS/integrar_clase.py --sin-subir      # índice de menciones
# agregar la clase y sus tramos a 05_CLASES/mapa_ensenanza.yaml
python 03_SCRIPTS/construir_navegacion.py            # barras de navegación + index.html
python 03_SCRIPTS/verificar_visuales.py              # sin red, enlaces, citas
uv run --with playwright python 03_SCRIPTS/probar_visuales_offline.py   # prueba en Edge sin red
```

Reautenticar NotebookLM cuando caduque:

```bash
notebooklm login --browser msedge
notebooklm auth check --test --json     # debe devolver "status": "ok"
```

Datito **no depende** de NotebookLM: si falla, avisa, sigue con el material
local y etiqueta el resto.

---

## Para reutilizarlo en otro curso (ADR-001: Arquitectura Multi-Curso)

**Lectura recomendada:** [`01_DOCUMENTACION/ADR-001-multi-course.md`](../01_DOCUMENTACION/ADR-001-multi-course.md) — decisiones, tradeoffs, layout.

Datito se separó en **tres ámbitos**:
- **Motor** (`datito-core`): skills, scripts, verificadores — no cambian
- **Curso** (`courses/tu-ramo/`): curriculum, clases, material, visuales — lo llena el docente
- **Alumno** (`learners/tu-alumno/`): progreso, errores, estado, dudas — automático

### Quickstart (10 minutos)

```bash
# 1. Clona la plantilla
cp -r courses/_template courses/tu-ramo-2026-2
cd courses/tu-ramo-2026-2

# 2. Edita datito.config.yaml, curriculum.yaml, clases.yaml

# 3. Crea un alumno nuevo
python 03_SCRIPTS/datito_init_learner.py --course tu-ramo-2026-2 --learner juan_perez

# 4. Regenera
python 03_SCRIPTS/construir_navegacion.py
python 03_SCRIPTS/datito_estado.py

# 5. Abre Claude Code
/datito
```

### Layout

```
courses/
  fcd-2026-2/                     ← Fundamentos de Ciencia de Datos (default)
    datito.config.yaml
    curriculum.yaml
    clases.yaml
    visual/
    ...

learners/
  cristobal_herrera_fcd-2026-2/   ← Alumno 1
    progreso.yaml
    estado.md
    ...
  juan_perez_tu-ramo-2026-2/       ← Alumno 2 (otro curso)
    progreso.yaml
    ...
```

Las skills de `.claude/skills/` **no se tocan**: leen de `datito.config.yaml` para resolver rutas.

### Backward Compatibility

Si no hay `course_id` ni `learner_id` en `datito.config.yaml`, asumen:
```yaml
course_id: fcd-2026-2
learner_id: cristobal_herrera
```

Sesiones antiguas funcionan sin cambios.
