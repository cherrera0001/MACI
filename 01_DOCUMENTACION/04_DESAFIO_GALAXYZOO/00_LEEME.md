# Desafío Galaxy Zoo — Auditoría, reproducción y mejora

Ubicación: `..\..\Fundamentos de ciencia de datos\Desafio\`
Informe completo: `..\..\Fundamentos de ciencia de datos\Desafio\REPORT.md`

Clasificación multiclase de galaxias SDSS/Galaxy Zoo. Métrica oficial: **F1-score macro**.

| Clase | Significado | n (train) | % |
|---|---|---|---|
| 0 | no decidible / votación ambigua | 96 | 9,6 |
| 1 | espiral | 227 | 22,7 |
| 2 | elíptica | 677 | 67,7 |

El encargo no era hacer funcionar el notebook, sino **auditarlo, reproducirlo, validarlo y mejorarlo**.

---

## Por qué este desafío importa para el expediente del Certamen 2

Es la **única fuente local** de varios conceptos que el certamen evalúa:

| Concepto del certamen | Dónde aparece aquí |
|---|---|
| Diversidad de ensambles (P1) | `src\08_ensemble.py`: *"Primero mide DIVERSIDAD de errores entre modelos (si dos modelos fuertes fallan en las mismas filas, promediarlos no puede aportar)"*. Calcula `jaccard_error` y `desacuerdo_pred` por par de modelos |
| Matriz de confusión (P8) | `REPORT.md` §5: matriz 3×3 con filas = real, columnas = predicho, más precision/recall/F1 por clase |
| AUC (P4, P9) | `REPORT.md` §8.3: techo de AUC marginal univariada 0,754 para 0-vs-resto frente a 0,9041 para 1-vs-2, calculado **sin clasificador**, solo con los datos |
| Umbral y regla de decisión (P9) | `src\05_decision_rule.py` y §10.1: *"Cualquier cifra obtenida tuneando y reportando sobre el mismo OOF está inflada"* |
| Sobreajuste en clasificación (P3) | §10.1, misma cita: sobreajuste a la regla de decisión, no al modelo |

**Advertencia de trazabilidad temporal:** este material es del 12 de septiembre de 2026, **posterior** al certamen (28 de agosto). Evidencia que el autor comprende estos conceptos; no evidencia que los comprendiera al rendir. Así queda declarado en la Fase 5.1 del análisis del certamen.

---

## Estructura del desafío

| Ruta | Contenido |
|---|---|
| `src\00_audit.py` | Auditoría de columnas: constantes, MAD = 0, correlaciones extremas, outliers |
| `src\01_repro_notebook.py` | Reproducción del notebook original con CV estratificada |
| `src\02_ablation_features.py` | Ablación de grupos de features |
| `src\03_model_comparison.py` | Comparación de modelos |
| `src\04_class0_analysis.py` | Análisis geométrico de la clase 0 |
| `src\05_decision_rule.py` | Búsqueda de pesos de decisión sobre probabilidades OOF |
| `src\06_hierarchical.py` | Clasificador jerárquico |
| `src\07_final_train.py` | Entrenamiento final |
| `src\08_ensemble.py` | Ensamble con medición previa de diversidad |
| `src\09_catboost_tuning.py` | Ajuste de CatBoost |
| `analysis\` | Salidas: auditoría por columna, geometría de clase 0, frente de Pareto, búsqueda de pesos |

---

## Hallazgos conceptuales destacados

**1. La clase 0 no es un tipo de galaxia.** Es un estado del proceso de votación: *"ningún bando alcanzó mayoría"*. Esto condiciona todo el resto del análisis y explica por qué ninguna feature individual la detecta bien.

**2. Techo estructural, no falla del modelo.** Ninguna feature supera AUC 0,754 para 0-vs-resto, y la dispersión estandarizada de la clase 0 (1,229) es la mayor de las tres: es una mezcla, no un grupo.

**3. Autocrítica estadística.** §11: *"la desviación entre folds (0,022–0,038) es mayor que casi todas las diferencias que se quieren medir, por lo que la mayoría de las comparaciones de modelos no son concluyentes."* Declarar esto es más valioso que reportar un ganador.

**4. Auditoría de fuga: revisada y no encontrada.** Siete riesgos auditados uno por uno —preprocesamiento antes de la CV, selección global de features, escalado global, imputación global, oversampling antes de los folds, reutilización del test, ingeniería de features— cada uno con su veredicto.
