# 07 · TUTOR — Agente personal de aprendizaje de Ciencia de Datos

Tutor que ensena los 21 conceptos del programa usando **el material de este
repositorio** y el cuaderno de NotebookLM *Fundamentals of Data Science
Syllabus* como fuentes citables.

No es un chatbot de preguntas y respuestas. Es un bucle: explica, pregunta,
espera, diagnostica el error, reexplica por otra via, y solo entonces avanza.

---

## Como se usa

| Comando | Que hace |
|---|---|
| `/tutor` | Abre sesion. La primera vez hace un diagnostico de 8 preguntas |
| `/tutor-progreso` | Informe de estado. Solo lectura, no ensena |

---

## Estructura

```
07_TUTOR/
├── 00_LEEME.md        este archivo
├── curriculum.yaml    ESTATICO — los 21 conceptos, orden, prerrequisitos, material
├── progreso.yaml      DINAMICO — el registro de dominio. Lo escribe el tutor
└── bitacora/          una entrada por sesion: preguntas, respuestas, errores

.claude/skills/tutor/            el bucle de ensenanza
.claude/skills/tutor-progreso/   informe de estado
.mcp.json                        conexion a NotebookLM
```

La separacion entre `curriculum.yaml` y `progreso.yaml` es deliberada: el plan no
cambia con el uso, y asi una sesion no puede corromperlo.

---

## Estudiado no es comprendido

Cinco estados por concepto:

| Estado | Significado |
|---|---|
| `pendiente` | No visto |
| `en_curso` | El tutor lo explico |
| `explicado` | Lo explicaste con tus palabras, correctamente |
| `en_duda` | Fallaste, y el error concreto quedo registrado |
| `dominado` | **Exige las dos evidencias** |

Un concepto llega a `dominado` solo si se cumplen ambas:

1. Lo explicaste con tus palabras, sin leer.
2. Resolviste un ejercicio nuevo **sin que el tutor te diera la respuesta**.

Una sola no basta. Ademas, cada `dominado` guarda `ultima_verificacion`: al abrir
sesion el tutor re-pregunta uno antiguo al azar, y si fallas vuelve a `en_duda`.
Es lo que impide que el registro solo suba.

---

## De donde sale cada afirmacion

Se reutiliza la convencion de etiquetas que este repositorio ya usa en el
expediente del Certamen 2:

| Etiqueta | Origen |
|---|---|
| `[EVIDENCIA · NotebookLM: <fuente>]` | Tu cuaderno, con la fuente que el propio NotebookLM cito |
| `[EVIDENCIA · Repo: <ruta>]` | Tu material, con ruta verificable |
| `[INFERENCIA]` | Se deriva de lo anterior, pero no esta escrito |
| `[GENERAL]` | Conocimiento del modelo, **sin respaldo en tus fuentes** |

La ultima es la que importa: si NotebookLM esta caido, lo veras marcado en
pantalla en lugar de recibir una afirmacion sin respaldo.

---

## Material propio por concepto

Hay material real en el repositorio para **17 de los 21** conceptos. Las cifras
usadas como ejemplo salen de `05_RESULTADOS/resultados_temporal.json`:
6.336 propiedades de 2016 para entrenar, 7.244 de 2017 para evaluar, MAE 185.449
AUD, R2 0,765, y **29,1% del test en suburbios que no existen en el train**.

Los tres recursos mas valiosos para ensenar:

- **`99_ARCHIVO/_obsoleto_split_aleatorio/`** — version anterior que anunciaba
  *"81% Precision"* con split aleatorio y fue invalidada por el split temporal.
  Un error real, propio y documentado: el mejor material posible para entender
  fuga de informacion y por que un numero mas alto puede ser un modelo peor.
- **El 29,1% de suburbios nuevos** — generalizacion medida, no teorica.
- **`02_PROYECTO_FCD/Desafio/`** (Galaxy Zoo) — unica fuente propia de matriz de
  confusion, precision/recall/F1, AUC y ensembles.

**Sin material local (4):** redes neuronales, deep learning, LLM y agentes de IA.
Ahi dependemos de NotebookLM y fuentes externas.

---

## Sobre la conexion con NotebookLM

Google **no ofrece API oficial de NotebookLM para cuentas personales** — solo
para *Gemini Notebook Enterprise* en Google Cloud. La integracion usa
[`notebooklm-py`](https://github.com/teng-lin/notebooklm-py) (MIT), que accede a
**APIs internas no documentadas mediante cookies de sesion**.

Consecuencias que conviene tener presentes:

- Google puede romperla sin aviso.
- Las cookies caducan cada pocas semanas y hay que re-autenticar.
- Aplican limites de uso.

Por eso el tutor **no depende** de NotebookLM: si falla, avisa, sigue con el
material del repositorio y etiqueta el resto como `[GENERAL]`.

Las credenciales viven en `C:\Users\herre\.notebooklm\`, **fuera de este
repositorio**. Nunca deben entrar en Git.

Re-autenticar cuando caduque:

```bash
notebooklm login --browser-cookies edge    # con Edge cerrado
notebooklm auth check --json               # debe devolver "status": "ok"
```
