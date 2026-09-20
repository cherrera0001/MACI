# Proyecto 3 — Predicción del valor de propiedades (Melbourne 2016 → 2017)

Proyecto semestral de Fundamentos de Ciencia de Datos. Autores: C. Abrigo · C. Herrera · K. Urbina.

**Instrucción del curso (literal):** *"usar las ventas de propiedades para entrenar un modelo predictivo con datos del 2016, y luego predecir y evaluar su modelo sobre las propiedades del año 2017."*

Esa frase gobierna todas las decisiones de diseño: obliga a una partición **temporal**, no aleatoria.

---

## Hito 1 — Análisis exploratorio y modelamiento inicial

Ubicación: [`../../02_PROYECTO_FCD/Hito1/`](../../02_PROYECTO_FCD/Hito1/)

| Archivo | Contenido |
|---|---|
| `Corrección\Documentos Originales\V2_Trabajo_N1_FUNDAMENTOS_(...).ipynb` | **Trabajo 1 — EDA.** Calidad de datos, faltantes, duplicados, rangos inválidos, distribución de precios, comparación 2016 vs 2017 |
| `Corrección\Trabajo N°1 _ FINAL\2° Trabajo _FUNDAMENTOS\V1_Trabajo_N2_FUNDAMENTOS_(...).ipynb` | **Trabajo 2 — Modelamiento.** Partición temporal, pipeline sin leakage, jerarquía baseline→lineal→árbol→RF→GB, CV K=5, GridSearchCV, importancia por reducción de impureza |
| `anclaje.json` / `anclaje.py` | Fuente de verdad de las cifras del proyecto, con hash SHA-256 del dataset |
| `Presentacion_Hito1_prediccion_precios.pptx` | Presentación oral del Hito 1 |

**Cifras ancla del Hito 1:** 13.580 filas · 2016 = 6.336 (46,7 %) / 2017 = 7.244 (53,3 %) · mediana de precio 900k → 910k (+1,11 %) · 172 suburbios nuevos en 2017 (29,1 % de las filas) · baseline MAE 2016→2017 = 431.649 AUD.

---

## Hito 2 — Modelamiento final, comparación estadística y réplica

Capa ejecutable: scripts en `03_CODIGO/`, ejecutar **desde `F:\MACI`**. Orden:

| # | Script | Salida | Qué hace |
|---|---|---|---|
| 1 | `03_CODIGO/modelamiento_temporal.py` | `05_RESULTADOS/resultados_temporal.json` | Seis modelos × dos targets (crudo y `log1p`) × cinco semillas. CV 5-fold dentro de 2016; test 2017 una sola vez |
| 2 | `03_CODIGO/bootstrap_comparacion.py` | `05_RESULTADOS/comparacion_estadistica.json`, `predicciones_2017.csv` | Bootstrap pareado IC 95 % sobre 2017, segmentos, permutación |
| 3 | `03_CODIGO/preparar_dashai.py` + `dashai_driver.py all` | `04_DATOS/housing_dashai_2016_2017.csv`, `05_RESULTADOS/dashai_*.json` | Réplica independiente en DashAI |
| 4 | `03_CODIGO/generar_informe.py` | `06_ENTREGABLES/INFORME_MODELO_FCD_P3.md` | Informe final. **Ningún número escrito a mano** |
| 5 | `03_CODIGO/generar_pitch_v2.py` | `06_ENTREGABLES/PITCH_HITO2_REVISION.md`, `Pitch_Hito2_v2.pptx` | Revisión lámina por lámina y presentación |
| — | `03_CODIGO/housing_visualizations.py` | `06_ENTREGABLES/visualizaciones/viz_*.html` | Visualizaciones interactivas |
| — | `auditoria_dashai_vs_crudo.py`, `correlacion_dashai.py` | `05_RESULTADOS/auditoria_*.json`, `correlacion_*.json` | Controles de consistencia |

---

## Protocolo de evaluación aplicado

1. **Partición temporal estricta:** train = 2016 (n = 6.336), test = 2017 (n = 7.244). El test se usa **una sola vez**.
2. **Selección sin mirar el test:** validación cruzada 5-fold dentro de 2016; el ranking de CV decide.
3. **Jerarquía:** baseline (mediana) → lineal (Ridge) → árbol → ensambles (RF, GB, HistGB).
4. **Sin fuga de información:** imputación, escalado y one-hot aprendidos solo en train; `handle_unknown='ignore'` para categorías nuevas de 2017.
5. **Estabilidad:** cinco semillas para modelos estocásticos; se reporta media ± sd.

---

## Resultado

**Modelo elegido: `HistGradientBoostingRegressor` sobre `log1p(Price)`** con `max_iter=500, learning_rate=0.05, max_leaf_nodes=31, l2_regularization=1.0`.

| Métrica en 2017 | Valor |
|---|---|
| MAE | 185.449 AUD |
| RMSE | 305.329 |
| R² | 0,765 |
| MAPE | 16,8 % |
| Brecha R² train-test | +0,176 |

El ranking por CV dentro de 2016 **coincide** con el ranking en el test de 2017: la selección honesta eligió el mismo modelo que resultó mejor fuera de muestra.

**Límites declarados:** el error crece en el cuartil alto de precio, en suburbios nuevos (MAPE 22,5 % vs 14,5 %) y en regiones no metropolitanas con n < 60. El modelo no predice cambios macro del mercado.

---

## Hallazgo metodológico central

**Covariate shift medido:** el 29,1 % de las filas de 2017 pertenece a suburbios que no existen en 2016, y el 26,7 % a códigos postales nuevos. Consecuencia directa: se excluyeron `Suburb`, `Postcode`, `Address`, `SellerG`, `CouncilArea` y `Date` (alta cardinalidad o calidad inconsistente entre años), y la geografía se capturó con variables **continuas** (`Distance`, `Lattitude`, `Longtitude`) que sí existen para zonas nuevas.

**El caso más ilustrativo:** Ridge con target logarítmico **diverge** en 2017 (MAE ≈ 9,8e+08). Un modelo lineal extrapola sin límite ante combinaciones no vistas y `expm1` amplifica el error. Es un ejemplo real y medido de un modelo que funciona con datos históricos y falla con datos nuevos — el contenido exacto de la pregunta 3 del certamen.

---

## Documentos de lectura

| Documento | Ubicación |
|---|---|
| Informe final del modelamiento | [`../../06_ENTREGABLES/INFORME_MODELO_FCD_P3.md`](../../06_ENTREGABLES/INFORME_MODELO_FCD_P3.md) |
| Revisión del pitch | [`../../06_ENTREGABLES/PITCH_HITO2_REVISION.md`](../../06_ENTREGABLES/PITCH_HITO2_REVISION.md) |
| Presentación Hito 2 | [`../../06_ENTREGABLES/Pitch_Hito2_v2.pptx`](../../06_ENTREGABLES/Pitch_Hito2_v2.pptx) / `.pdf` |
| Versión invalidada y su corrección | [`../05_HISTORICO/00_LEEME.md`](../05_HISTORICO/00_LEEME.md) |
