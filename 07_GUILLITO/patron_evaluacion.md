# Patrón de evaluación del profesor

Reconstruido desde las evaluaciones **reales** del repositorio, no desde lo que
"suele" preguntarse en Ciencia de Datos.

**Fuente principal:** Certamen 2, 11 preguntas, con ficha completa en
`01_DOCUMENTACION/01_CERTAMEN2/02_MAPA_PROCESO_ESTUDIO.md`.
**Complementos:** guía de estudio del profesor, Trabajos 1 y 2, Desafío Galaxy
Zoo, y los 5 prácticos de `08_PRACTICA/`.

---

## 1 · La firma del profesor

Revisando las 11 fichas aparece **un mismo campo en todas**: *distinción
conceptual clave*. Sin excepción.

Cada pregunta del certamen se resuelve separando dos cosas que se parecen:

| Pregunta | La distinción que decide la respuesta |
|---|---|
| P1 | Número de modelos **≠** diversidad de modelos |
| P2 | Sobreajuste **≠** subajuste **≠** error alto |
| P3 | Más filas (reduce sobreajuste) **≠** más columnas (lo aumenta) |
| P4 | Cantidad que describe un **clasificador** **≠** que describe una **variable** |
| P5 | Generar texto **≠** ejecutar acciones y observar su resultado |
| P6 | **Causa** **≠** condición habilitante |
| P7 | Error de entrenamiento **≠** calidad del modelo · bajar grado **≠** regularizar |
| P8 | Precisión (÷ predichos) **≠** sensibilidad (÷ reales) **≠** exactitud (÷ total) · **FPR ≠ 1 − precisión** |
| P9 | Comparar **punto de operación** **≠** comparar **modelo** |
| P10 | Declarar un vacío **≠** producir una respuesta plausible |
| P11 | **Medido** / **supuesto** / **no disponible** |

**Consecuencia para el entrenamiento:** no evalúa si sabes una definición.
Evalúa si distingues dos conceptos vecinos bajo presión. Guillito debe entrenar
esa discriminación, no el recitado.

---

## 2 · Distribución temática

### Certamen 2 — modelamiento y evaluación

| Bloque | Preguntas | Peso |
|---|---|---|
| **Sobreajuste, generalización, validación, ensambles** | P1, P2, P3, P7 | **36 %** |
| **Métricas de clasificación y evaluación** | P4, P8, P9 | **27 %** |
| Panorama de IA: LLM, agentes, redes neuronales | P5, P6 | 18 % |
| Conducta metodológica: supuestos y vacíos | P10, P11 | 18 % |

Más de un tercio gira sobre sobreajuste y validación. Un cuarto, sobre métricas
de clasificación. Juntos: **63 %**.

### Certamen 1 — fundamentos, adquisición y calidad

Fuente: `01_DOCUMENTACION/06_CERTAMEN1/`. **Material de un compañero: los
enunciados son fiables, las respuestas NO están verificadas.** Ver el 00_LEEME
de esa carpeta.

| # | Formato | Pts | Tema |
|---|---|---|---|
| 1-4 | V/F con justificación | 0,5 c/u | Campo interdisciplinario · *data-driven* frente a *data-informed* · rol del líder · ciclo de vida iterativo |
| 5-8 | Selección múltiple | 0,5 c/u | Webscraping · tipo de problema · reclutamiento · Big Data (las "V") |
| 9A | Desarrollo con tabla | — | Calidad y estructura de datos tabulares |
| **9B** | **Desarrollo con tabla** | **2,0** | **Caso minero: consumo de combustible** |
| 10 | Retroalimentación | 0 | — |

**Dato que reordena las prioridades:** la 9B vale **2,0 puntos**, más que las
ocho preguntas cerradas juntas. El desarrollo de calidad de datos pesa mucho
más de lo que sugería el Certamen 2 por sí solo.

### Los dos certámenes juntos

| | Certamen 1 | Certamen 2 |
|---|---|---|
| Enfoque | Fundamentos, adquisición, calidad | Modelamiento, evaluación |
| Formato dominante | V/F + selección múltiple + **desarrollo con tabla** | V/F + selección múltiple + lectura de figuras |

Cubren bloques distintos y entre ambos mapean casi todo el curso.

---

## 3 · Formatos que usa

| Formato | Dónde aparece | Qué exige |
|---|---|---|
| Verdadero/falso con justificación | P1, P2 | Nombrar el mecanismo, no solo elegir |
| "Cuál de estas afirmaciones es incorrecta" | P3, P4, P5, P6 | Evaluar cada opción por su mecanismo propio |
| Diagnóstico desde una figura | P7, P10 | Leer un gráfico y nombrar el fenómeno |
| Cálculo desde matriz de confusión | P8 | Aritmética a mano y elección de denominador |
| Lectura y comparación de curvas ROC | P9 | Comparar modelos, no puntos |
| Declaración de supuestos | P11 | Separar medido de supuesto |

**Todo es resoluble a mano.** Ninguna pregunta exigió ejecutar código. Eso fija
el estándar de entrenamiento: cálculo manual, papel y lápiz.

---

## 4 · Errores típicos que el formato castiga

Deducidos de las distinciones que cada pregunta exige:

- Diagnosticar sobreajuste mirando un solo número en vez de la brecha
- Confundir "más datos" con "más columnas"
- Usar el denominador equivocado al calcular precisión o sensibilidad
- Creer que `FPR = 1 − precisión`
- Comparar dos clasificadores en un único umbral y concluir cuál es mejor
- Tratar el error de entrenamiento como evidencia de calidad
- Responder con algo plausible cuando el dato no está disponible

---

## 5 · Cruce con el progreso actual

| Concepto | Peso en los certámenes | Estado en `progreso.yaml` | Prioridad |
|---|---|---|---|
| `overfitting_underfitting` | C2: P2, P3, P7 — **3 preguntas** | `NO_ESTUDIADO` | **1** |
| `limpieza_preparacion` | C1: **9A + 9B, la 9B vale 2,0 pts** | `NO_ESTUDIADO` | **2** |
| `matriz_confusion` | C2: P8 — cálculo manual | `NO_ESTUDIADO` | **3** |
| `metricas_clasificacion` | C2: P4, P8 | `NO_ESTUDIADO` | **4** |
| `roc_auc` | C2: P9 | `NO_ESTUDIADO` | **5** |
| `ensembles` | C2: P1 | `NO_ESTUDIADO` | 6 |
| `fundamentos_ciencia_datos` | C1: P1-P4, P7 | `NO_ESTUDIADO` | 7 — conceptual, poco cálculo |
| `datos_features_target` | C1: P6, P9A | `NO_ESTUDIADO` | 8 |
| `generalizacion` | transversal | `COMPRENSION_PARCIAL` | prerrequisito cubierto |
| `train_validation_test` | transversal | `COMPRENDIDO` | prerrequisito cubierto |
| `llm`, `agentes_ia` | C2: P5, P6 | `NO_ESTUDIADO` | 9 — menos material propio |

`limpieza_preparacion` sube al segundo lugar por el peso de la 9B: dos puntos en
una sola pregunta de desarrollo, con la tabla a la vista y resoluble en papel.

### Por qué `overfitting_underfitting` va primero

1. **Mayor peso**: 3 de 11 preguntas, más que ningún otro concepto.
2. **Evidencia documentada de dificultad**: el error
   `sobreajuste_como_etiqueta_de_toda_degradacion` está registrado en
   `errores_conceptuales.yaml` — usó "sobreajuste" como etiqueta para cualquier
   empeoramiento, sin el mecanismo.
3. **Prerrequisitos cubiertos**: `train_validation_test` en `COMPRENDIDO` y
   `generalizacion` en `COMPRENSION_PARCIAL`.
4. **Material propio abundante**: los seis modelos de Melbourne tienen
   `train2016_R2`, `test2017_R2` y `brecha_R2_train_test` ya calculados.

---

## 6 · Niveles de entrenamiento

| Nivel | Qué es | Habilita |
|---|---|---|
| **1 · Reconocimiento** | Ejercicio del mismo tipo que usó el profesor | — |
| **2 · Aplicación** | Mismo concepto, cambian números, contexto o representación | `PUEDO RESOLVER SOLO` |
| **3 · Transferencia** | Problema nuevo donde hay que descubrir qué concepto aplica | `PUEDO TRANSFERIR` |

Regla: no marcar `PUEDO RESOLVER SOLO` sin superar el nivel 2 sin ayuda.

---

## 7 · Método de resolución por familia

### Diagnóstico de sobreajuste / subajuste

1. Localizar el par de números: rendimiento **dentro** y **fuera** del entrenamiento
2. Calcular la **brecha**, no mirar un solo valor
3. Clasificar: bueno dentro + malo fuera → sobreajuste · malo en ambos → subajuste · parecido y aceptable → ajuste razonable
4. Nombrar el **mecanismo**, no la etiqueta
5. Proponer remedio según causa: simplificar · regularizar · más filas · validación cruzada

### Matriz de confusión y métricas

1. Declarar cuál es la **clase positiva**
2. Localizar positivos reales (fila) y positivos predichos (columna)
3. Obtener TP, TN, FP, FN y **verificar que los marginales cierren**
4. Identificar qué métrica piden
5. Escribir la fórmula **antes** de sustituir
6. Sustituir, calcular, e **interpretar en palabras del problema**

Denominadores, que es lo que el profesor distingue:

```
Exactitud  = (TP+TN) / TOTAL           ÷ todo
Precisión  =  TP / (TP+FP)             ÷ predichos positivos
Sensibilidad (TPR) = TP / (TP+FN)      ÷ positivos reales
FPR        =  FP / (FP+TN)             ÷ negativos reales
F1         = 2·P·R / (P+R)             media armónica
```

### Comparación con ROC

1. Un modelo es una **curva**, no un punto
2. Comparar umbral a umbral: ¿uno tiene mayor TPR **y** menor FPR en todos?
3. Si domina en todos → su curva está por encima → es mejor sin ambigüedad
4. Si se cruzan → no hay ganador absoluto; depende del punto de operación

---

## 8 · Lo que este documento no hace

No inventa temas por pertenecer a Ciencia de Datos. Cada bloque listado está
anclado a una pregunta real del Certamen 2 o al material del curso.

Redes neuronales aparecen en P6, pero el expediente registra que **no hay una
sola red neuronal en el código del repositorio**: ahí el entrenamiento depende
de NotebookLM y del material de clase, no de trabajo propio.
