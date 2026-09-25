# Caso: Diagnóstico de Cáncer de Mama

## Resumen ejecutivo

**569 muestras de células de tumores mamarios** clasificadas como benignas (357) o malignas (212).

**Vinculado a**: Clase 7 — Clasificación (FCD-2026-2_07_Clasificacion.pdf)  
**Dataset**: Breast Cancer Wisconsin (Diagnostic) — UCI ML Repository, DOI: 10.24432/C5DW2B  
**Paper**: Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993)

**30 características morfométricas** derivadas de imágenes digitalizadas: radio, textura, perímetro, área, suavidad, compacidad, concavidad, puntos cóncavos, simetría y dimensión fractal. Cada una se resume en tres formas: media (mean), error estándar (se) y extremo superior (worst).

**Dos hitos**:
- **Hito 1**: Análisis exploratorio. ¿Qué características diferencian tumores benignos de malignos? ¿Cuáles son redundantes?
- **Hito 2**: Modelamiento predictivo. ¿Podemos predecir el diagnóstico de una muestra nueva? ¿Qué modelo generaliza mejor?

---

## Estructura del dataset

```
569 observaciones = 357 benignas (62.7%) + 212 malignas (37.3%)
30 predictores numéricos
1 variable objetivo: diagnosis (B/M)
```

**Partición (Hito 2)**:
- Train: 455 observaciones (285 benignas, 170 malignas)
- Test: 114 observaciones (72 benignas, 42 malignas)

---

## Resultados finales (Hito 2)

**Modelo ganador: Random Forest**

Hiperparámetros: 100 árboles, profundidad máxima = 5

| Métrica | Valor |
|---------|-------|
| Accuracy (test) | 0.974 |
| Precision (maligno) | 1.000 |
| Recall (maligno) | 0.929 |
| FPR | 0.000 |
| ROC-AUC | 0.995 |
| Falsos negativos | 3 |

**Matriz de confusión (test, Random Forest)**:
```
           Predicción
           Benigno  Maligno
Verdad  B    72         0
        M     3        39
```

---

## Por qué es importante para tu certamen

Tu pregunta de certamen fue sobre un doctor que recibe 1000 pacientes, de los cuales ~200 tienen diagnóstico positivo. Tu pregunta pedía **leer correctamente una matriz de confusión** e interpretar:

- **Falsos negativos**: pacientes enfermos que el test clasifica como sanos
- **Falsos positivos**: pacientes sanos que el test clasifica como enfermos
- **Por qué el cost o no es simétrico**: un falso negativo (enfermo no detectado) tiene consecuencias distintas que un falso positivo

**Este caso es idéntico en estructura pero con números reales de un problema actual.**

---

## Archivos

- `pre_informe_hito1_cancer_mama-v02.pdf` — Análisis exploratorio: EDA, tamaño de efecto, redundancia
- `preinforme_hito2_v02.pdf` — Modelamiento: SVM, Decision Tree, Random Forest, validación cruzada, resultados
- `Presentacion_Hito2_v2_2.pdf` — Presentación visual del Hito 2

---

## Material pedagógico (generado)

- `cancer_mama_hito2_RESUELTO.ipynb` — Notebook con el análisis completo paso a paso
- `cancer_mama_hito2_VACIO.ipynb` — Ejercicio: reproducir el análisis
- `matriz_confusion_cancer.md` — Guía para leer e interpretar la matriz de confusión

---

## Dónde va en Datito

Conceptos del curriculum que refuerza:

- **11 · Matriz de confusión**: Construcción a partir de predicciones reales
- **12 · Métricas de clasificación**: Accuracy, precision, recall, FPR, specificity
- **13 · ROC y AUC**: Curva ROC calculada para tres modelos competidores
- **15 · Random Forest**: Primer ensemble, comparación con SVM y Decision Tree

**Nota**: Este caso es de **transferencia**. No es el tuyo (Melbourne es regresión, Galaxy Zoo es multiclase), pero comparte los métodos de clasificación binaria con tu dominio.
