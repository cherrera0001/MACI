# Cruce del glosario de referencia contra las 23 clases (T-1.2.1, H-1.2)

Referencia: `11_GOOGLE/Glosario.docx` («Google Data Analytics», 403 términos, en inglés).
Curso: las 23 clases de `07_DATITO/clases.yaml`. Glosario resultante: `07_DATITO/glosario.yaml`.

## Mapa inglés → español y cobertura

| Término del curso (es) | En la referencia (en) | Clase | Estado |
|---|---|---|---|
| Ciencia de datos | Data analysis | 1 | cubierto |
| Escala data-driven | — | 1 | **ausente en referencia** |
| Feature (variable de entrada) | — | 2 | **ausente** |
| Target (variable objetivo) | — (Target population es otra cosa) | 2 | **ausente** |
| Fuga de información | — | 2 | **ausente** |
| Atípico (outlier) | Outliers | 3 | cubierto |
| Correlación | Correlation | 3 | cubierto |
| Distribución normal | Normal distribution | 3 | cubierto |
| Binning | Binning | 4 | cubierto |
| Dato faltante | Missing data | 4 | cubierto |
| Regresión lineal | Linear regression | 5 | cubierto |
| Mejor recta | Best fit line | 5 | cubierto |
| MSE | MSE (Mean Squared Error) | 6 | cubierto |
| MAE | MAE (Mean Absolute Error) | 6 | cubierto |
| R² | Adjusted R² (parcial: la referencia no trae R² solo) | 6 | parcial |
| Train / validation / test | Model validation (parcial) | 7 | parcial |
| Hiperparámetro | Hyperparameters | 7 | cubierto |
| Validación cruzada | — | 8 | **ausente** |
| Generalización | — | 9 | **ausente** |
| A/B testing | A/B testing | 19 | cubierto |
| Overfitting | Overfitting | 10 | cubierto |
| Underfitting | — | 10 | **ausente** |
| Compromiso sesgo-varianza | Bias-variance trade-off | 10 | cubierto |
| Clasificación | — | 11 | **ausente** |
| Regresión logística | Logistic regression | 11 | cubierto |
| Supervisado / no supervisado | Supervised machine learning / Unsupervised model | 11 | cubierto |
| Matriz de confusión | Confusion matrix | 12 | cubierto |
| Exactitud | Accuracy | 13 | cubierto |
| Precisión | Precision | 13 | cubierto |
| Sensibilidad (recall) | Recall | 13 | cubierto |
| Teorema de Bayes | Bayes' theorem | 13 | cubierto |
| ROC y AUC | — | 14 | **ausente** |
| Umbral (threshold) | — (los «threshold» de la referencia son de clustering) | 14 | **ausente** |
| Árbol de decisión | Tree-based learning (parcial) | 15 | parcial |
| Random Forest | Random forest | 16 | cubierto |
| Gradient boosting | Gradient boosting | 16 | cubierto |
| Ensamble | Ensemble learning | 16 | cubierto |
| Red neuronal | — | 17 | **ausente** |
| Deep learning | — | 18 | **ausente** |
| Modelo de lenguaje (LLM) | Large Language Model (LLM) | 18 | cubierto |
| Agente | — | 18 | **ausente** |

**Resumen**: 42 términos del curso — 25 cubiertos, 3 parciales, 14 ausentes en la
referencia. Los ausentes son precisamente el núcleo del curso (validación,
generalización, ROC/AUC, umbral, redes y agentes): el glosario del curso no puede
copiarse de la referencia; la definición de esos términos sale de las clases.

## Términos pertinentes de la referencia que el curso no enseña (ausencias de cobertura)

| Término de la referencia | Por qué queda fuera |
|---|---|
| Clustering (Agglomerative, K-means), ANOVA, MANOVA | No hay unidad de aprendizaje no supervisado ni inferencia clásica en el plan |
| Naive Bayes | El curso cita Bayes solo como base conceptual (clase 13) |
| XGBoost, AdaBoost | El curso llega a Gradient Boosting (clase 16); los variantes quedan para después |
| Tableau, Dashboard, Action, Story | Herramientas de visualización de negocio; el curso visualiza con HTML propio |
| Funciones de pandas y Python (agg(), append(), merge()) | El curso no enseña sintaxis; enseña criterio de análisis |
| ARIMA, Series temporales | Fuera del alcance del semestre |

Conclusión: la referencia cubre el vocabulario de análisis de datos básico y sirve
de respaldo para el 60 % del glosario; el 40 % restante se redactó desde las
transcripciones y fichas de las clases (fuente citada en `glosario.yaml`).
