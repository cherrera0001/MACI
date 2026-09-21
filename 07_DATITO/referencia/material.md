# Referencia · Material disponible

Cargar al elegir ejemplos o ejercicios.

---

## Los prácticos de la asignatura

`08_PRACTICA/` — cinco laboratorios, cada uno en versión `(res)` resuelta y
`(vacio)` sin resolver. Mapeo completo en `curriculum.yaml`, sección `practicos`.

| | Tema | Cubre |
|---|---|---|
| P1 | Pandas | `datos_features_target`, `eda` |
| P2 | Calidad de Datos | `limpieza_preparacion` |
| P3 | Numpy y Análisis Descriptivo | `eda` |
| P4 | Regresión | `regresion`, `train_validation_test`, `validacion_cruzada`, `overfitting_underfitting` |
| P5 | Clasificación | `clasificacion`, `matriz_confusion`, `metricas_clasificacion`, `arboles_decision`, `random_forest` |

P4 trae el desarrollo formal de **sesgo y varianza**. P5, la definición
explícita de **TP, TN, FP, FN** con el ejemplo de la "Guitarra".

**Los `(vacio)` son la fuente de evidencia de APLICAR.** Nunca muestres el
`(res)` de un ejercicio antes de que lo intente.

---

## Ejercicios de los certámenes

### Certamen 1 — desarrollo con tabla

Dos casos reales, datos a la vista, resolubles en papel. Fuente:
`01_DOCUMENTACION/06_CERTAMEN1/`.

- **9A · Calificaciones** — 4 alumnos × 3 fechas, las fechas como encabezados de
  columna. `N/A` en texto mezclado con números, y `Matrícula` con valor `N/A`.
  A detectar: formato ancho frente a *tidy data*, tipos inconsistentes, clave
  primaria rota.
- **9B · Consumo minero (2,0 pts)** — la columna `CONSUMO` mezcla días, IDs de
  camiones y estados operativos. Centinela `-999` para mantenimiento, y un
  `2900` frente a `200` del resto. A detectar: sobrecarga semántica, centinelas
  que sesgan estadísticos, atípico, filas usadas como separadores.

**La 9B vale más que las ocho preguntas cerradas juntas.**

### Certamen 2 — modelamiento y evaluación

11 fichas -10 preguntas numeradas en Canvas mas un Espaciador de 0 puntos-
con ficha completa en
`01_DOCUMENTACION/01_CERTAMEN2/02_MAPA_PROCESO_ESTUDIO.md`.

---

## Melbourne Housing — regresión

`05_RESULTADOS/resultados_temporal.json`

- Train 6.336 propiedades de 2016 · test 7.244 de 2017
- Final: HistGradientBoosting sobre `log1p(Price)` — MAE 188.218 AUD, R² 0,757
- Mediana de precio 2017: 910.000 AUD
- **29,1 % del test son suburbios que no existen en el train**

Brechas train/test, útiles para enseñar sobreajuste con sus propios números:

| Modelo (log) | R² train | R² test | Brecha |
|---|---|---|---|
| Árbol de decisión | 0,7523 | 0,6123 | 0,1400 |
| Random Forest | 0,9423 | 0,7109 | **0,2314** |
| Gradient Boosting | 0,8858 | 0,7466 | 0,1392 |
| HistGradientBoosting | 0,9274 | 0,7571 | 0,1703 |

Ridge sobre log da R² **−17,0**: al deshacer el `expm1` sobre valores extremos
las predicciones se disparan.

### El error documentado

`99_ARCHIVO/_obsoleto_split_aleatorio/` anunciaba *"81 % Precisión"* con split
aleatorio y fue invalidado por el split temporal. Un error real, suyo y
documentado: el mejor material para enseñar fuga de información y por qué un
número más alto puede ser un modelo peor.

### Experimento CouncilArea

`05_RESULTADOS/experimento_councilarea_2026-09-18.json`. A vs B con una sola
variable de diferencia. B mejora 599 AUD (0,38 %) y gana 20/25 comparaciones
pareadas, **pero se conservó A**: `CouncilArea` tiene 0 % de nulos en 2016 y
18,9 % en 2017, más 14 categorías nuevas — el 28,5 % de las filas de 2017 no
aportan nada por esa columna.

---

## Galaxy Zoo — clasificación

`04_DATOS/GZ_mini_challenge_{train,test}.csv` · informe en
`02_PROYECTO_FCD/Desafio/REPORT.md` · detalle en `04_DATOS/00_LEEME.md`

Tres clases, métrica oficial **F1-macro**. Única fuente propia de matriz de
confusión, precision/recall/F1, AUC y ensembles.

### Cifras reales, verificadas sobre el CSV

```
train  1.000 × 90        test  10.000 × 86     cero nulos
```

| Clase | Qué es | Filas | % |
|---|---|---|---|
| 0 | No decidible · votación ambigua | 96 | **9,6 %** |
| 1 | Espiral | 227 | 22,7 % |
| 2 | Elíptica | 677 | **67,7 %** |

**Desbalance 7,1×.** Un modelo que responda siempre «elíptica» acierta el
67,7 % sin aprender nada — y ahí está la razón de que la métrica oficial sea
F1-macro y no exactitud. **Es el ejemplo real para enseñar métricas de
clasificación**, mejor que cualquiera inventado.

### Dos trampas reales en estos datos

**1 · Features que no existen al predecir.** `p_el` y `p_cs` —las fracciones de
voto humano— están en train y **no en test**:

| Clase | `p_el` | `p_cs` |
|---|---|---|
| 0 | 0,356 | 0,271 |
| 1 | 0,212 | **0,739** |
| 2 | **0,735** | 0,139 |

Son muy informativas y **no se pueden usar**: un modelo entrenado con ellas no
podría ejecutarse sobre el test. Mismo problema que `costo_combustible_clp` del
dataset sintético de transferencia, pero real.

**2 · Por qué la clase 0 es la difícil.** Sus dos medias son bajas: ninguna
domina. La clase 0 no es otro tipo de galaxia — es *«los humanos no se pusieron
de acuerdo»*. Reconocer **ausencia de consenso** es señal mucho más débil que
reconocer una forma, y con solo 9,6 % de representación es la clase que hunde
el F1-macro.

---

## Guías de estudio

`07_DATITO/guias/` — material escrito para leer sin agente.

- `overfitting_underfitting.md` — los dos criterios, la inversión de métrica,
  remedios por mecanismo, y un procedimiento de siete pasos
