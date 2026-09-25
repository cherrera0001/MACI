# Proyecto 3 FCD 2026-2 — ¿Cuál es el mejor modelo para predecir el precio de propiedades en Melbourne 2017 entrenando con 2016?

**Generado programáticamente** el 2026-09-15 por `generar_informe.py` desde `resultados_temporal.json`, `comparacion_estadistica.json` y `dashai_resultados.json`. Ningún número fue escrito a mano.

## 0. Fe de erratas (léase primero)

Los documentos que ahora están en `_obsoleto_split_aleatorio/` usaban un split aleatorio 80/20 y contenían cifras **no calculadas** (brechas train-test, porcentajes de importancia, un R² de 0,7842). Quedan invalidados. Todo lo que sigue proviene de código ejecutado y es reproducible con semillas fijas.

## 1. Instrucción del curso y protocolo de evaluación

La guía (*Proyectos FCD 2026-2*, Proyecto 3) es explícita: *"entrenar un modelo predictivo con datos del 2016, y luego predecir y evaluar su modelo sobre las propiedades del año 2017"*. El Hito 2 evalúa Modelamiento (15 %) y Resultados (15 %). Protocolo aplicado:

1. **Partición temporal estricta**: train = ventas 2016 (n = 6,336), test = ventas 2017 (n = 7,244). El test se usa **una sola vez**, al final.
2. **Selección de modelo sin mirar 2017**: validación cruzada 5-fold **dentro de 2016**; el ranking de CV decide, no el test.
3. **Jerarquía**: baseline (mediana) → lineal (Ridge) → árbol → ensambles (Random Forest, Gradient Boosting, HistGradientBoosting).
4. **Sin fuga de información**: imputación, escalado y one-hot aprendidos solo en train (`sklearn.Pipeline`); categorías nuevas de 2017 → `handle_unknown='ignore'`.
5. **Estabilidad**: 5 semillas ([0, 1, 2, 3, 4]) para modelos estocásticos; se reporta media ± sd.
6. **Dos targets**: precio crudo y `log1p(precio)` (distribución con cola derecha; mediana 2016 = 900,000, 2017 = 910,000).

## 2. Datos y desplazamiento de distribución (covariate shift)

2017 no es una muestra aleatoria del mismo universo que 2016: **29.1 % de las filas de 2017 están en suburbios que no existen en 2016** (172 suburbios nuevos), 26,7 % en códigos postales nuevos, y `CouncilArea` pasa de 0 % a 18,9 % de nulos. Consecuencias de diseño:

- **Excluidas**: Suburb, Postcode, Address, SellerG, CouncilArea, Date, BuildingArea, YearBuilt (identificadores de alta cardinalidad que no generalizan a zonas nuevas, o con calidad inconsistente entre años).
- **Numéricas** (9): Rooms, Distance, Bedroom2, Bathroom, Car, Landsize, Lattitude, Longtitude, Propertycount — imputadas con mediana de 2016 + indicador de faltante (BuildingArea 43 % nulo en 2016 / 51 % en 2017; YearBuilt 35 % / 44 %).
- **Categóricas** (3): Type, Method, Regionname — baja cardinalidad, estables entre años.
- La geografía se captura con variables **continuas** (Distance, Lattitude, Longtitude) que sí existen para suburbios nuevos.

## 3. Resultados de la jerarquía de modelos (target log, evaluación en 2017)

| Modelo | MAE CV-5 en 2016 (selección) | MAE test 2017 (± sd semillas) | RMSE 2017 | R² 2017 | R² train 2016 | Brecha R² | MAE sub. nuevo / conocido |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline (mediana) | 449,160 | 431,649 ± 0 | 654,393 | -0.080 | -0.071 | +0.009 | 308,196 / 482,352 |
| Ridge (lineal) | 235,857 | 275,806 ± 0 | 2,671,847 | -17.003 | 0.645 | +17.648 | 207,728 / 303,766 |
| Arbol de decision | 219,821 | 246,568 ± 0 | 392,077 | 0.612 | 0.752 | +0.140 | 257,462 / 242,094 |
| Random Forest | 170,467 | 206,843 ± 316 | 338,593 | 0.711 | 0.942 | +0.231 | 227,081 / 198,531 |
| Gradient Boosting | 161,499 | 192,441 ± 886 | 316,960 | 0.747 | 0.886 | +0.139 | 198,666 / 189,884 |
| HistGradientBoosting | 159,777 | 188,218 ± 0 | 310,329 | 0.757 | 0.927 | +0.170 | 193,462 / 186,064 |

Mismos modelos con target crudo (referencia):

| Modelo | MAE CV-5 en 2016 (selección) | MAE test 2017 (± sd semillas) | RMSE 2017 | R² 2017 | R² train 2016 | Brecha R² | MAE sub. nuevo / conocido |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline (mediana) | 449,160 | 431,649 ± 0 | 654,393 | -0.080 | -0.071 | +0.009 | 308,196 / 482,352 |
| Ridge (lineal) | 270,617 | 294,789 ± 0 | 455,623 | 0.476 | 0.624 | +0.148 | 330,817 / 279,992 |
| Arbol de decision | 224,982 | 250,771 ± 0 | 393,542 | 0.609 | 0.765 | +0.155 | 279,021 / 239,169 |
| Random Forest | 174,525 | 216,400 ± 546 | 347,038 | 0.696 | 0.949 | +0.253 | 262,825 / 197,333 |
| Gradient Boosting | 169,034 | 204,348 ± 2,057 | 329,030 | 0.727 | 0.905 | +0.178 | 226,832 / 195,114 |
| HistGradientBoosting | 165,064 | 196,287 ± 0 | 319,565 | 0.742 | 0.942 | +0.200 | 212,079 / 189,801 |

Lecturas:

- El **baseline** (predecir la mediana de 2016) tiene R² negativo en 2017: cualquier modelo útil debe superarlo ampliamente; todos lo hacen salvo en la medida en que Ridge-log diverge.
- **Ridge con target log diverge en 2017** (MAE ≈ 2.8e+05): un modelo lineal extrapola sin límite ante combinaciones de variables no vistas (regiones nuevas, Landsize extremos) y `expm1` amplifica el error. Con target crudo Ridge llega solo a R² = 0.476. Conclusión: la relación es fuertemente no lineal y el problema tiene shift; los lineales no son candidatos.
- Los tres **ensambles** están claramente por encima del árbol simple. Random Forest queda detrás de ambos boosting y además muestra la **mayor brecha train-test** (R² train 0.942 vs test 0.711).
- El **ranking por CV en 2016** (sin ver 2017) es: HistGradientBoosting < Gradient Boosting < Random Forest < Arbol de decision < Ridge (lineal) < Baseline (mediana). El ranking en test 2017 es: HistGradientBoosting < Gradient Boosting < Random Forest < Arbol de decision < Ridge (lineal) < Baseline (mediana). **Coinciden**: la selección hecha honestamente dentro de 2016 elige el mismo modelo que resulta mejor fuera de muestra.

## 4. ¿La diferencia entre modelos es real? Bootstrap pareado sobre las 7.244 propiedades de 2017

| Comparación (A − B) | Δ MAE 2017 | IC 95 % bootstrap pareado | P(A mejor) | Significativo |
|---|---:|---:|---:|:--:|
| HistGradientBoosting - Gradient Boosting | -2,816 | [-4,470, -1,110] | 1.000 | sí |
| HistGradientBoosting - Random Forest | -18,420 | [-21,152, -15,678] | 1.000 | sí |
| Gradient Boosting - Random Forest | -15,605 | [-18,508, -12,680] | 1.000 | sí |

HistGradientBoosting supera a Gradient Boosting por 2,816 AUD de MAE (IC 95 % excluye 0) y ambos superan a Random Forest por 15,605–18,420 AUD. La ventaja HGB–GB es estadísticamente significativa pero **pequeña en términos prácticos** (~1.5 % del MAE); la ventaja de boosting sobre Random Forest es sustantiva (~8.9 %).

## 5. Réplica en DashAI (http://localhost:8000, dataset preparado id 23, sesión con split manual)

Se subió a DashAI el mismo conjunto de variables (imputación y one-hot calculados **solo con 2016**, orden de filas intacto) y se creó una *model session* `RegressionTask` con `splitType: "manual"`: train = 5.702 filas de 2016, validation = 634 filas de 2016 (DashAI exige un conjunto de validación no vacío), test = 7.244 filas de 2017. Los modelos corren con sus **hiperparámetros por defecto** de DashAI y target crudo (DashAI no transforma el target), por lo que las cifras no son idénticas a las del pipeline local, pero permiten verificar el *ordenamiento* en una herramienta independiente.

| Run DashAI | Componente | MAE test 2017 | RMSE 2017 | R² 2017 | R² train | Estado |
|---|---|---:|---:|---:|---:|---|
| 01 Lineal (OLS) | LinearRegression | 297,317 | 457,460 | 0.472 | 0.626 | finished |
| 02 Ridge | RidgeRegression | 295,983 | 454,472 | 0.479 | 0.626 | finished |
| 03 Arbol de decision | DecisionTreeRegression | 286,088 | 466,126 | 0.452 | 1.000 | finished |
| 04 Random Forest (default) | RandomForestRegression | 218,986 | 354,664 | 0.683 | 0.973 | finished |
| 05 Gradient Boosting (default) | GradientBoostingR | 212,760 | 338,848 | 0.710 | 0.821 | finished |
| 06 HistGradientBoosting (default) | HistGradientBoostingRegression | 202,177 | 324,404 | 0.735 | 0.914 | finished |

Mejor run en DashAI por MAE 2017: **06 HistGradientBoosting (default)**.

## 6. Diagnóstico del modelo elegido: HistGradientBoosting (target log)

- MAE 2017 = **188,218 AUD**, RMSE = 310,329, R² = 0.757, MAPE = 16.8 %.
- Predicciones dentro de ±10 % del precio real: 38.9 %; dentro de ±20 %: 70.7 %. Dentro de ±100 k AUD: 44.2 %; ±200 k: 69.9 %.
- Brecha R² train-test = +0.170. Parte es sobreajuste y parte es el shift 2016→2017 (el baseline también empeora); se documenta, no se oculta.

**Error por tipo de propiedad (2017)**

| Segmento | n | MAE | MAPE |
|---|---:|---:|---:|
| h | 5280 | 212,826 | 17.8 % |
| t | 578 | 145,332 | 13.5 % |
| u | 1386 | 97,884 | 14.5 % |

**Error según si el suburbio existía en 2016**

| Segmento | n | MAE | MAPE |
|---|---:|---:|---:|
| False | 5135 | 182,129 | 14.5 % |
| True | 2109 | 193,530 | 22.5 % |

**Error por cuartil de precio (2017)**

| Segmento | n | MAE | MAPE |
|---|---:|---:|---:|
| Q1 bajo | 1814 | 94,364 | 19.0 % |
| Q2 | 1819 | 126,638 | 16.3 % |
| Q3 | 1803 | 157,452 | 14.2 % |
| Q4 alto | 1808 | 363,922 | 17.9 % |

**Error por región (2017)**

| Segmento | n | MAE | MAPE |
|---|---:|---:|---:|
| Eastern Metropolitan | 989 | 224,154 | 19.7 % |
| Eastern Victoria | 53 | 393,637 | 59.3 % |
| Northern Metropolitan | 2014 | 141,069 | 14.4 % |
| Northern Victoria | 41 | 102,785 | 19.7 % |
| South-Eastern Metropolitan | 426 | 231,777 | 25.6 % |
| Southern Metropolitan | 2140 | 234,281 | 15.7 % |
| Western Metropolitan | 1549 | 134,276 | 15.5 % |
| Western Victoria | 32 | 138,085 | 37.7 % |

El error crece en el cuartil alto (propiedades > ~1,3 M AUD), en suburbios nuevos (MAPE 22.5 % vs 14.5 %) y en las regiones *Victoria* (n muy pequeño, fuera del área metropolitana). Son los límites de uso del modelo.

**Importancia por permutación (post-hoc, calculada en 2017, no usada para seleccionar variables):**

| Variable | Δ MAE (escala log) al permutar | sd |
|---|---:|---:|
| Distance | +0.1013 | 0.0017 |
| Type | +0.0774 | 0.0015 |
| Lattitude | +0.0600 | 0.0013 |
| Regionname | +0.0506 | 0.0014 |
| Landsize | +0.0496 | 0.0006 |
| Longtitude | +0.0454 | 0.0009 |
| Rooms | +0.0336 | 0.0009 |
| Bathroom | +0.0112 | 0.0005 |
| BuildingArea | +0.0106 | 0.0004 |
| Propertycount | +0.0066 | 0.0004 |
| YearBuilt | +0.0066 | 0.0004 |
| Method | +0.0058 | 0.0004 |
| Car | +0.0052 | 0.0003 |
| Bedroom2 | +0.0009 | 0.0003 |

Ubicación (Distance, Lattitude/Longtitude, Regionname), tipo de propiedad y tamaño del terreno explican la mayor parte de la señal; `Bedroom2` (scrapeada) no aporta nada más allá de `Rooms`.

## 7. Decisión y justificación

**Modelo recomendado: HistGradientBoostingRegressor sobre `log1p(Price)`** (`max_iter=500, learning_rate=0.05, max_leaf_nodes=31, l2_regularization=1.0`), con el preprocesamiento descrito en §2.

Justificación, en el orden de criterios de la metodología del curso:

1. **Menor error fuera de muestra (2017)** en MAE, RMSE y R², con la partición temporal exigida por la guía.
2. **Elegido sin mirar el test**: es también el mejor en CV 5-fold dentro de 2016.
3. **Diferencia estadísticamente significativa** frente a las alternativas (bootstrap pareado, IC 95 %).
4. **Robusto al covariate shift**: degradación moderada en suburbios nuevos; los lineales colapsan y Random Forest sobreajusta más.
5. **Reproducible**: semillas fijas, pipeline encapsulado, resultados en JSON; réplica independiente en DashAI.

Alternativa aceptable: **Gradient Boosting** (mismo preprocesamiento), a ~2,816 AUD de MAE, con menor brecha train-test (+0.139 vs +0.170). **No recomendados**: Random Forest (peor error y mayor sobreajuste), modelos lineales (inadecuados ante no linealidad y shift), y cualquier modelo que use `Suburb`/`Postcode` (no generaliza al 29 % de 2017 en zonas nuevas).

Lo que el modelo **no** hace: no predice cambios macro del mercado (solo aprende 2016), no es fiable en regiones no metropolitanas (n < 60) ni en el tramo > 2 M AUD, y su error típico (~17 %) debe declararse junto con cada predicción.

## Reproducir

```
python modelamiento_temporal.py    # jerarquía de modelos, 5 semillas, CV en 2016, test 2017 -> resultados_temporal.json
python bootstrap_comparacion.py    # bootstrap pareado, segmentos, permutación -> comparacion_estadistica.json, predicciones_2017.csv
python preparar_dashai.py && python dashai_driver.py all   # réplica en DashAI -> dashai_resultados.json
python generar_informe.py          # este informe
```
