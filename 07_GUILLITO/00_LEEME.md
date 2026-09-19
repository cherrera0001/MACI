# 07 · GUILLITO — Tutor personal de Fundamentos de Ciencia de Datos

Guillito enseña los 21 conceptos del programa usando **el material de esta
asignatura**: el cuaderno de NotebookLM, los documentos del curso, y los
proyectos Melbourne Housing y Galaxy Zoo como casos prácticos.

No es un chatbot que responde preguntas. Es un ciclo: diagnostica, explica,
pregunta, **espera de verdad**, analiza el razonamiento, reexplica por otra vía
si hace falta, verifica transferencia y registra lo aprendido.

---

## Cómo se usa

Abre Claude Code en `F:\MACI` y habla con él:

```
Guillito, quiero aprender validación cruzada
```

También responde a `explícame overfitting`, `no entiendo ROC`, `repasemos
regresión`, o al comando directo:

| Comando | Qué hace |
|---|---|
| `/guillito` | Abre sesión de estudio |
| `/guillito-progreso` | Informe de estado. Solo lectura, no enseña |

La primera vez ejecuta un diagnóstico de 8 preguntas repartidas por los 21
conceptos, para no perder tiempo enseñando lo que ya sabes.

---

## Estructura

```
07_GUILLITO/
├── 00_LEEME.md                 este archivo
├── curriculum.yaml             ESTÁTICO — 21 conceptos, orden, prerrequisitos, material
├── progreso.yaml               DINÁMICO — estado y cadena de evidencia
├── errores_conceptuales.yaml   errores observados + patrones a vigilar
└── bitacora/                   una entrada por sesión

.claude/skills/guillito/            el ciclo pedagógico
.claude/skills/guillito-progreso/   informe de estado
CLAUDE.md                            hace que Claude Code reconozca a Guillito
.mcp.json                            conexión a NotebookLM
```

La separación entre `curriculum.yaml` y `progreso.yaml` es deliberada: el plan no
cambia con el uso, así una sesión no puede corromperlo.

---

## Estudiado no es comprendido

Seis estados:

| Estado | Significado |
|---|---|
| `NO_ESTUDIADO` | No visto |
| `EN_ESTUDIO` | Guillito lo explicó. Nada verificado aún |
| `COMPRENSION_PARCIAL` | Lo explicas, pero con huecos |
| `COMPRENDIDO` | Explicas y aplicas correctamente |
| `DOMINADO` | Explicas, aplicas **y transfieres** |
| `REQUIERE_REPASO` | Lo sabías y fallaste en una re-verificación |

### La cadena de evidencia

```
EXPLICAR  →  APLICAR  →  TRANSFERIR
```

| Evidencia | Se cumple cuando |
|---|---|
| `EXPLICAR` | Lo explicas con tus palabras, sin leer |
| `APLICAR` | Resuelves un caso del mismo dominio, sin recibir la respuesta |
| `TRANSFERIR` | Resuelves un caso de **otro dominio** que no habías visto |

**`DOMINADO` exige las tres.** Decir "entendí" no es evidencia de nada, y
Guillito tiene instrucción explícita de no aceptarlo. Tampoco cuenta repetir su
explicación con otras palabras, ni acertar después de una pista muy fuerte, ni
acertar por el motivo equivocado.

Además, cada concepto guarda `ultima_verificacion`: al abrir sesión Guillito
re-pregunta uno antiguo, y si fallas pasa a `REQUIERE_REPASO`. Es lo que impide
que el registro solo suba.

---

## Errores conceptuales

`errores_conceptuales.yaml` separa dos cosas que no deben mezclarse:

- **`observados`** — errores que cometiste de verdad, con fecha, qué dijiste,
  cuál es la confusión de fondo y qué explicación funcionó para desmontarla.
  Si uno reaparece, sube el contador `veces`.
- **`patrones_vigilados`** — confusiones frecuentes en estos temas que Guillito
  anticipa. **No son errores tuyos.** Vienen sembrados: R² leído como porcentaje
  de aciertos, MAE juzgado sin escala, accuracy con clases desbalanceadas, AUC
  confundido con accuracy, split aleatorio en datos temporales, y otros.

Un error que vuelve tres veces no es un despiste: es un modelo mental
equivocado, y Guillito debe atacarlo de frente en vez de corregir el síntoma.

---

## De dónde sale cada afirmación

| Etiqueta | Origen |
|---|---|
| `[FUENTE · NotebookLM: <documento>]` | El cuaderno, citando el documento concreto |
| `[FUENTE · Repo: <ruta>]` | Tu material, con ruta verificable |
| `[INFERENCIA]` | Se deriva de lo anterior, pero no está escrito |
| `[GUILLITO]` | **Explicación pedagógica suya**: analogía, ejemplo inventado |

`[GUILLITO]` no es una etiqueta de segunda: una buena analogía es trabajo docente
legítimo. Pero queda marcada para que no atribuyas al syllabus algo que dijo él.

### Jerarquía de fuentes

1. Material FCD del repositorio
2. Cuaderno de NotebookLM
3. Proyectos propios (Melbourne, Galaxy Zoo)
4. Fuentes académicas externas, solo si lo anterior no alcanza

Dentro del cuaderno: material de la asignatura > documentos UdeC > libros y
papers > documentación técnica.

---

## Material propio por concepto

Hay material real para **17 de los 21** conceptos, con 37 rutas verificadas. Las
cifras de ejemplo salen de `05_RESULTADOS/resultados_temporal.json`: 6.336
propiedades de 2016 para entrenar, 7.244 de 2017 para evaluar, MAE 185.449 AUD,
R² 0,765, y **29,1% del test en suburbios que no existen en el train**.

Los tres recursos más valiosos:

- **`99_ARCHIVO/_obsoleto_split_aleatorio/`** — versión anterior que anunciaba
  *"81% Precisión"* con split aleatorio y fue invalidada por el split temporal.
  Un error real, propio y documentado: el mejor material posible para entender
  fuga de información y por qué un número más alto puede ser un modelo peor.
- **El 29,1% de suburbios nuevos** — generalización medida, no teórica.
- **`02_PROYECTO_FCD/Desafio/`** (Galaxy Zoo) — única fuente propia de matriz de
  confusión, precision/recall/F1, AUC y ensembles.

Para redes neuronales, deep learning, LLM y agentes no hay trabajo propio
ejecutado, pero **sí hay fuentes**: `FCD-2026-2_08_DL_LLMs_Agents.pdf`,
`Resumen_Clase8_DL_LLMs_Agentes.pdf` y el PDF de Deep Learning del Magíster.

---

## El cuaderno de NotebookLM

**66 fuentes**, todas procesadas: 32 páginas web, 29 PDF, 3 Word, 2 Markdown.

Incluye el material de la asignatura (`Syllabus Fundamentos de Ciencia de
Datos.docx`, presentaciones `FCD-2026-2_02` a `_08`, resúmenes de clase, dos
guías de autoestudio), documentos UdeC (tesis de detección de fraude, edad de
jubilación, XGBoost con SHAP, diploma de Ingeniería UdeC) y bibliografía de
referencia (ISLR, OpenIntro Statistics, el paper de XGBoost, *50 Years of Data
Science*, principios FAIR, guía de scikit-learn).

### Limitaciones que conviene conocer

Google **no ofrece API oficial de NotebookLM para cuentas personales** — solo
para *Gemini Notebook Enterprise*. La integración usa
[`notebooklm-py`](https://github.com/teng-lin/notebooklm-py) (MIT) sobre **APIs
internas no documentadas con cookies de sesión**. Por tanto:

- Google puede romperla sin aviso.
- Las cookies caducan cada pocas semanas.
- Aplican límites de uso.

Guillito **no depende** de ella: si falla, avisa, sigue con el material del
repositorio y etiqueta el resto. La degradación está diseñada.

Las credenciales viven en `C:\Users\herre\.notebooklm\`, **fuera del
repositorio**. Nunca deben entrar en Git.

Re-autenticar cuando caduque:

```bash
notebooklm login --browser msedge    # Playwright abre Edge con perfil aislado
notebooklm auth check --json         # debe devolver "status": "ok"
```

> Nota: importar cookies con `--browser-cookies edge` **no funciona**. Edge y
> Chrome cifran las cookies con App-Bound Encryption, que ata la clave al
> proceso del navegador. Usa siempre `--browser msedge`.
