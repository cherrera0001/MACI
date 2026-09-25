# Índice: Caso de Diagnóstico de Cáncer de Mama

## Para empezar: LEE ESTO PRIMERO

**Vinculado a**: [Clase 7 — Clasificación](../../11_PRESENTACIÓN/FCD-2026-2_07_Clasificacion.pdf)

[`README.md`](README.md) — Resumen del proyecto, por qué importa para tu certamen, estructura de datos, fuentes verificadas.

---

## Materiales de referencia (PDFs)

| Archivo | Descripción | Secciones clave |
|---------|-------------|-----------------|
| `pre_informe_hito1_cancer_mama-v02.pdf` | Análisis exploratorio: EDA, tamaño de efecto, correlación | §1-5: Hipótesis, datos, inspección inicial, análisis de diferencias |
| `preinforme_hito2_v02.pdf` | Modelamiento predictivo: Datos, métodos, resultados | §1-8: Intro, formulación, modelos, metodología, métricas, resultados, discusión |
| `Presentacion_Hito2_v2_2.pdf` | Presentación visual del Hito 2 | Diapositivas 1-21: Resumen ejecutivo, comparación de modelos, matrices |

---

## 🔧 Herramientas Dinámicas (NUEVO)

### Para jugar con los números (Eje X → Procesamiento → Eje Y)

[`matriz_confusion_dinamica.html`](matriz_confusion_dinamica.html) ⭐ **SIN INSTALAR**
- Abre en navegador
- Ingresa TP, TN, FP, FN
- Calcula automáticamente todas las métricas
- Visualiza heatmap
- Botones de ejemplo: Cáncer, COVID

[`matriz_confusion_generador.py`](matriz_confusion_generador.py)
- Script Python reutilizable
- Calcula 16 métricas diferentes
- Genera gráficos (matplotlib)
- Exporta JSON/CSV
- Usa: `python matriz_confusion_generador.py --ejemplo cancer`

[`QUICK_START_DINAMICAS.md`](QUICK_START_DINAMICAS.md)
- Cómo usar las herramientas en 5 minutos
- Guía paso a paso

[`HERRAMIENTAS_DINAMICAS.md`](HERRAMIENTAS_DINAMICAS.md)
- Concepto completo: Eje X, procesamiento, Eje Y
- 3 escenarios de experimentación
- Cómo escalar a 1000 pacientes

---

## Guías de estudio

### Análisis exploratorio (Hito 1)

[`analisis_exploratorio_RESUMEN.md`](analisis_exploratorio_RESUMEN.md)
- Resumen ejecutivo del Hito 1
- Métodos: tamaño de efecto, correlación, redundancia
- Hipótesis y hallazgos clave
- Vinculación a conceptos de Datito: EDA, correlación, calidad de datos

**Conceptos del curriculum que refuerza**:
- `eda` (3): Centralidad, extensión, distribución, correlación
- `limpieza_preparacion` (4): Auditoría de calidad
- `datos_features_target` (2): Selección de características

---

### Matriz de confusión (Hito 2)

[`matriz_confusion_interpretacion_RESUELTO.md`](matriz_confusion_interpretacion_RESUELTO.md) ← **SOLUCIÓN CON EXPLICACIÓN**

Cálculo y interpretación de:
- TN, TP, FN, FP desde la matriz real (114 pacientes)
- Accuracy, Precision, Recall, Specificity, FPR
- Trade-offs entre tipos de error
- Comparación de tres modelos (SVM, Decision Tree, Random Forest)
- Conexión a tu pregunta de certamen (doctor + 1000 pacientes)

[`matriz_confusion_interpretacion_VACIO.md`](matriz_confusion_interpretacion_VACIO.md) ← **EJERCICIO PARA RESOLVER**

8 preguntas progresivas sobre matriz de confusión. Entrega en `../entregas/`.

**Conceptos del curriculum que refuerza**:
- `matriz_confusion` (11): Construcción, nomenclatura, interpretación
- `metricas_clasificacion` (12): Accuracy, precision, recall, F1
- `roc_auc` (13): Interpretación de AUC y trade-offs

---

## Notebooks (generados)

*(En desarrollo - se generarán próximamente)*

- `cancer_mama_hito2_RESUELTO.ipynb`
  - Carga de datos
  - Partición train/test estratificada
  - Validación cruzada 5-fold
  - Ajuste de hiperparámetros
  - Comparación de tres modelos
  - Matrices de confusión
  - Curvas ROC
  
- `cancer_mama_hito2_VACIO.ipynb`
  - Ejercicio: reproducir el análisis paso a paso
  - Usar los PDFs como referencia
  - Código con celdas vacías

---

## Entregas

Deja tus respuestas aquí:

```
../entregas/cancer_matriz_confusion_[TU_NOMBRE].md
../entregas/cancer_hito2_notebook_[TU_NOMBRE].ipynb
```

---

## Vinculación al curriculum de Datito

Actualización: El `curriculum.yaml` ahora referencia este material en los conceptos:

- **11 · Matriz de confusión**: Pregunta extendida con interpretación clínica
- **12 · Métricas de clasificación**: Comparación de modelos por recall vs accuracy
- **13 · ROC y AUC**: Curvas ROC de tres competidores, interpretación de AUC
- **14 · Árboles de decisión**: Por qué Decision Tree tiene peor generalizacion
- **15 · Random Forest**: Ganador del Hito 2, comparación directa

---

## Flujo de estudio recomendado

### Semana 1: Análisis Exploratorio (Hito 1)

1. Lee `README.md` (5 min)
2. Lee `analisis_exploratorio_RESUMEN.md` (10 min)
3. Consulta `pre_informe_hito1_cancer_mama-v02.pdf` para profundizar (30 min)
4. Pregúntale a Datito: "Explícame EDA con el caso del cáncer"

### Semana 2: Matriz de confusión (Hito 2)

1. Lee `matriz_confusion_interpretacion_RESUELTO.md` (20 min)
2. Haz el ejercicio en `matriz_confusion_interpretacion_VACIO.md` (30-40 min)
3. Consulta `preinforme_hito2_v02.pdf` si tienes dudas
4. Envía tu solución a `../entregas/`
5. Pregúntale a Datito: "Corrige mi solución de la matriz de confusión del cáncer"

### Semana 3: Modelos y métricas

1. Estudia los resultados comparativos en `Presentacion_Hito2_v2_2.pdf` (20 min)
2. Lee el notebook resuelto (cuando esté disponible)
3. Reproduce el análisis en el notebook vacío
4. Pregúntale a Datito: "¿Por qué Random Forest beat SVM en este dataset?"

---

## Verificación: ¿Qué deberías ser capaz de hacer?

- [ ] Construir una matriz de confusión desde predicciones y etiquetas reales
- [ ] Calcular TN, TP, FN, FP correctamente
- [ ] Interpretar accuracy, precision, recall como proporciones
- [ ] Explicar por qué un falso negativo es peor que un falso positivo en diagnóstico
- [ ] Calcular balanced accuracy como promedio de recall + specificity
- [ ] Comparar dos modelos por recall si tienen precisión igual
- [ ] Transferir esta lógica a otro problema médico (no solo cáncer de mama)

---

## FAQ

**P: ¿Por qué hay un caso de cáncer si ya tengo Melbourne y Galaxy Zoo?**
R: Porque tu pregunta de certamen fue sobre matriz de confusión en un problema médico. Este caso es idéntico en estructura pero con cifras reales modernas. Melbourne es regresión, Galaxy Zoo es multiclase. Aquí es clasificación binaria clara.

**P: ¿Debo memorizar los números?**
R: No. Usa los números para *entender el proceso*. ¿Cómo cambiaria recall si hubiera 5 falsos negativos en lugar de 3?

**P: ¿Está disponible el dataset de cáncer?**
R: Sí, es el Breast Cancer Wisconsin (Diagnostic) dataset, público en UCI ML Repository. Si lo necesitas, contacta.

**P: ¿Qué hago si no entiendo un concepto?**
R: Lee RESUELTO primero. Luego intenta VACIO. Luego pregúntale a Datito.

---

## Contacto

Si tienes dudas sobre este caso:
- Abre Claude Code en `F:\MACI`
- Escribe: `/datito`
- Pregunta: "Explícame [concepto] con el ejemplo del cáncer de mama"
