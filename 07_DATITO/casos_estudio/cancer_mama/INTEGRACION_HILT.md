# Integración: Wisconsin Diagnostic ↔ Clase 7 (HILT)

## Mapeo: Láminas → Caso práctico

| Concepto HILT | Lámina | Qué cubre | Dónde en cancer_mama |
|---|---|---|---|
| **Clasificación binaria** | Clase 7, lámina ~3-5 | Definición y problema | README.md, analisis_exploratorio_RESUMEN.md |
| **Matriz de confusión** | Clase 7, lámina ~10-12 | TP/TN/FP/FN | matriz_confusion_interpretacion_RESUELTO.md, matriz_confusion_dinamica.html |
| **Accuracy, Precision, Recall** | Clase 7, lámina ~13-15 | Métricas derivadas | matriz_confusion_interpretacion_RESUELTO.md, metricas_clasificacion.html |
| **F1-Score, Balanced Accuracy** | Clase 7, lámina ~16-18 | Promedios | HERRAMIENTAS_DINAMICAS.md |
| **Comparación de modelos** | Clase 7, lámina ~19-21 | SVM vs Decision Tree vs Random Forest | preinforme_hito2_v02.pdf, Presentacion_Hito2_v2_2.pdf |

---

## Fuentes verificadas

### Dataset
- **Fuente oficial**: UCI ML Repository, dataset #17
- **DOI**: 10.24432/C5DW2B
- **URL UCI**: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- **URL Kaggle**: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
- **Paper**: Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993)

### Clase HILT
- **Fuente**: Clase 7 — Clasificación
- **Archivos**:
  - `F:\MACI\11_PRESENTACIÓN\FCD-2026-2_07_Clasificacion.pdf`
  - `F:\MACI\11_PRESENTACIÓN\_markdown\FCD-2026-2_07_Clasificacion.md`
- **Mención de matriz/confusión**: 17 referencias confirmadas

### Caso de estudio
- **Hito 1**: Análisis exploratorio (diferencias entre benignos/malignos)
- **Hito 2**: Modelamiento predictivo (Random Forest ganador)
- **Autores**: Luis Jara, Hernán Leiva, Víctor Mardones, Juan Garcés
- **Fecha**: Agosto 2026

---

## Etiquetación de fuentes

**Todos los archivos deben usar**:
- `[FUENTE · Clase 7]` → cuando está en láminas de clasificación
- `[FUENTE · UCI ML]` → cuando proviene del dataset
- `[FUENTE · Repo: preinforme_hito2_v02.pdf]` → cuando está en PDFs
- `[DATITO]` → explicación pedagógica original (solo con justificación)

---

## Checklist final

- [x] Dataset Wisconsin (Diagnostic) verificado: 569 obs, 30 features
- [x] Clase 7 (HILT) menciona matriz de confusión: 17 refs
- [x] PDFs coinciden con dataset: ✓ (357/212, 62.7%/37.3%)
- [ ] **Re-etiquetar TODO con [FUENTE · Clase 7]**
- [ ] **Crear referencias cruzadas README → láminas**
- [ ] **Validar que cada número es trazable**

---

## Próxima acción

**ANTES de abrir matriz_confusion_dinamica.html**:

1. Re-etiqueta los 7 archivos .md con referencias correctas
2. Agrega en README.md un párrafo: "Vinculado a Clase 7 (HILT): [URL a lámina]"
3. Cierra este checklist
4. ENTONCES: abre el HTML y comienza experimentos
