# Índice general de la documentación

Guía paso a paso de todo el material del repositorio, ordenado por para qué sirve.
Si no sabes por dónde empezar, sigue las rutas de lectura del final.

---

## 01 · CERTAMEN 2 — Reconstrucción del proceso de estudio

Carpeta: [`01_CERTAMEN2\`](01_CERTAMEN2/)

| Orden | Documento | Qué contiene | Cuándo leerlo |
|---|---|---|---|
| 0 | [`00_LEEME.md`](01_CERTAMEN2/00_LEEME.md) | Qué es este expediente, qué afirma y qué no | Siempre primero |
| 1 | [`01_ANALISIS_RECONSTRUCCION_CERTAMEN.md`](01_CERTAMEN2/01_ANALISIS_RECONSTRUCCION_CERTAMEN.md) | Análisis completo en 5 fases: material identificado, ficha de cada una de las 11 preguntas, correspondencias, separación conocimiento/razonamiento/redacción, revisión adversarial | Documento principal. Largo, pero es el que sostiene todo lo demás |
| 2 | [`02_MAPA_PROCESO_ESTUDIO.md`](01_CERTAMEN2/02_MAPA_PROCESO_ESTUDIO.md) | Matriz transversal de las 11 preguntas + análisis de patrones globales del método de trabajo | Para tener la vista de conjunto en pocas páginas |
| 3 | [`03_DEFENSA_ORAL_CERTAMEN.md`](01_CERTAMEN2/03_DEFENSA_ORAL_CERTAMEN.md) | Guion de trabajo por pregunta: concepto, respuesta corta, razonamiento de 30 s, ejemplo propio, error a evitar, repregunta y respuesta | Para preparar una instancia oral |
| 4 | [`Certamen2_Reconstruccion_Completa.docx`](01_CERTAMEN2/Certamen2_Reconstruccion_Completa.docx) | **Los tres documentos anteriores consolidados en un solo Word**, con el mismo formato del documento de respuestas original | Si prefieres leerlo o imprimirlo como un solo documento |
| — | [`fuentes\`](01_CERTAMEN2/fuentes/) | Los dos originales intactos: `Certamen2_Respuestas_Finales (Recuperado automáticamente).docx` y `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` | Referencia |

**Conclusión del expediente, en una línea:** el material local permite reconstruir **parcialmente** un proceso de comprensión — con doble anclaje (guía de estudio + trabajo propio ejecutado) en seis de las once preguntas, anclaje solo en la guía en tres, y dos zonas que ningún archivo explica: la secuencia temporal del estudio y las cifras de AUC de la pregunta 9.

---

## 02 · CURSO — Enunciados y reglas de evaluación

Carpeta: [`02_CURSO\`](02_CURSO/)

| Archivo | Qué es |
|---|---|
| `Proyectos FCD 2026-2 (6).pdf` | Enunciado oficial de los proyectos del semestre |
| `guia_fcd_texto.txt` | Texto extraído del enunciado. Contiene la instrucción decisiva del Proyecto 3: *"usar las ventas de propiedades para entrenar un modelo predictivo con datos del 2016, y luego predecir y evaluar su modelo sobre las propiedades del año 2017"* |
| `Guia_metodologica_proyecto_FCD.docx` | Guía metodológica del proyecto |

Aquí también están los pesos de evaluación de ambos hitos. En el Hito 2: Modelamiento 15 %, Resultados 15 %, Presentación 20 %, **Preguntas 30 %**.

---

## 03 · PROYECTO MELBOURNE — Hito 1 y Hito 2

Índice: [`03_PROYECTO_MELBOURNE\00_LEEME.md`](03_PROYECTO_MELBOURNE/00_LEEME.md)

Predicción del precio de propiedades: entrenar con 2016, evaluar en 2017. Es el núcleo del trabajo propio del semestre y la fuente de casi toda la evidencia conceptual del expediente del certamen.

Resultado final: **HistGradientBoosting sobre `log1p(Price)`**, MAE 2017 = 185.449 AUD, R² = 0,765, seleccionado por CV dentro de 2016 sin mirar el test.

---

## 04 · DESAFÍO GALAXY ZOO — Clasificación

Índice: [`04_DESAFIO_GALAXYZOO\00_LEEME.md`](04_DESAFIO_GALAXYZOO/00_LEEME.md)

Clasificación multiclase de galaxias con auditoría adversarial del notebook original. Es la única fuente local de matriz de confusión, precision/recall/F1, AUC y diversidad de ensambles.

---

## 05 · HISTÓRICO — Lo que quedó invalidado y por qué

Índice: [`05_HISTORICO\00_LEEME.md`](05_HISTORICO/00_LEEME.md)

No es basura: es el registro de una corrección. Se conserva deliberadamente porque documenta el paso de una versión con cifras no calculadas a una versión reproducible.

---

## Rutas de lectura

**Si necesitas preparar una defensa oral del certamen (2–3 h):**
1. `01_CERTAMEN2\00_LEEME.md`
2. `01_CERTAMEN2\02_MAPA_PROCESO_ESTUDIO.md` — vista de conjunto
3. `01_CERTAMEN2\03_DEFENSA_ORAL_CERTAMEN.md` — trabajarlo pregunta por pregunta en voz alta
4. Del análisis completo, leer solo las fichas de P8 y P9, que son las que tienen puntos débiles

**Si necesitas entender el expediente completo:**
1. `01_CERTAMEN2\01_ANALISIS_RECONSTRUCCION_CERTAMEN.md` de principio a fin, o
2. el Word `Certamen2_Reconstruccion_Completa.docx`, que trae los tres documentos consolidados

**Si necesitas defender el Proyecto 3:**
1. `03_PROYECTO_MELBOURNE\00_LEEME.md`
2. `..\INFORME_MODELO_FCD_P3.md` (raíz)
3. `..\PITCH_HITO2_REVISION.md` (raíz)

**Si alguien cuestiona la reproducibilidad del proyecto:**
1. `05_HISTORICO\00_LEEME.md` — el error y su corrección documentada
2. `..\INFORME_MODELO_FCD_P3.md` §0 "Fe de erratas"
3. Ejecutar la secuencia de scripts del `README.md` raíz

---

## Convención de etiquetas usada en todo el expediente

| Etiqueta | Significado |
|---|---|
| **[EVIDENCIA]** | Está explícitamente en un archivo, con cita textual y ruta |
| **[INFERENCIA]** | Se deriva razonablemente del contenido, pero no está escrito |
| **[NO EVIDENCIADO]** | No puede sostenerse con el material disponible |

Esta convención no es decorativa: es la que permite que el expediente sea auditable por un tercero que discrepe de sus conclusiones.
