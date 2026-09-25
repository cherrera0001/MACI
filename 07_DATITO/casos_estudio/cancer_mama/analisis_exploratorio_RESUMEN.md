# Análisis Exploratorio: Cáncer de Mama (Hito 1) — RESUMEN

## Contexto

El Hito 1 del proyecto de cáncer de mama es un **análisis exploratorio puro**: no se entrena modelo, solo se observan diferencias entre grupos.

569 muestras:
- 357 benignas (62.7%)
- 212 malignas (37.3%)

30 características morfométricas de células nucleares:
```
10 características (radio, textura, perímetro, área, suavidad, compacidad,
concavidad, puntos cóncavos, simetría, dimensión fractal)
× 3 resúmenes cada una (mean, se, worst)
= 30 columnas totales
```

---

## Pregunta del Hito 1

**"¿Qué características morfométricas se diferencian entre tumores benignos y malignos? ¿Cuáles repiten la misma señal?"**

Esto es **análisis exploratorio**, no predicción. No se divide train/test. Solo se observan.

---

## Métodos utilizados

### 1. Tamaño de efecto (Cohen's d)

Para cada característica, se calculó:

$$d = \frac{\mu_{\text{maligno}} - \mu_{\text{benigno}}}{\sigma_{\text{pooled}}}$$

**Resultado**: Las variables con mayor separación fueron:
- **puntos_cóncavos** (concave points)
- **perímetro** (perimeter)
- **radio** (radius)
- **área** (area)
- **concavidad** (concavity)
- **compacidad** (compactness)

**Interpretación**: Tumores malignos tienen **núcleos más grandes y contornos más irregulares** que benignos.

### 2. Correlación de Spearman

Para detectar redundancia entre características:

**Hallazgo clave**: Radio, perímetro y área están **altamente correlacionados** (r > 0.95 en muchos casos).

**Por qué?**: Las tres miden la misma cosa: **tamaño geométrico**. Un núcleo más grande tendrá:
- Radio mayor → Perímetro mayor → Área mayor

---

## Hipótesis confirmada

**Hipótesis inicial**: "Los tumores malignos presentan núcleos de mayor tamaño y contornos más irregulares que los benignos."

**Evidencia**:
- Tamaños de efecto elevados en variables de tamaño y forma ✓
- Correlación altísima entre radio, perímetro, área (3 medidas del mismo fenómeno) ✓
- Esperanza confirmada: "la selección secuencial conserva variables de mayor efecto" ✓

---

## Decisión sobre variables redundantes

**Pregunta**: "¿Debería eliminar radius, perimeter y area porque están correlacionados?"

**Respuesta del Hito 1**: No se decide aquí. El análisis exploratorio **reporta** la redundancia. **Quién decide si eliminarla es el modelador**, y eso va en el Hito 2.

**Nota en el Hito 2**: "Las 30 variables se mantuvieron porque el Hito 1 no estableció un criterio predictivo para eliminarlas."

**Importante para tu comprensión**: 
- Análisis ≠ Decisión de modelado
- EDA describe qué hay
- Selección de variables es una decisión del modelo

---

## Vinculación a tu curriculum de Datito

Este análisis cubre:

| Concepto | Dónde se ve | Pregunta diagnóstico |
|----------|-------------|----------------------|
| **EDA** | Cálculo de media, desviación, distribuciones | ¿Cuál es la media de radio en benignos vs malignos? |
| **Limpieza** | Auditoría inicial: sin datos faltantes, sin duplicados | Auditaste calidad de datos. ¿Qué habría hecho diferente si hubiera 50 valores faltantes en una característica? |
| **Correlación** | Correlación de Spearman entre 30 características | Si dos variables están correlacionadas r=0.97, ¿cuál debería elegir para el modelo? |
| **Generalización** | Selección explorativa vs selectiva de variables | El Hito 1 exploró. El Hito 2 decidió. ¿Cuál permite reproducibilidad mejor? |

---

## Cifras clave para recordar

```
569 observaciones
357 benignas / 212 malignas
30 predictores
Cohen's d mayor: concave points ≈ 2.0
Correlación máxima: r(radius, perimeter) ≈ 0.997
```

---

## Lectura recomendada

Para profundizar en el análisis exploratorio del Hito 1:

1. **Pre-informe Hito 1 (sección 3)**: Inspección inicial y calidad de datos
   - Dimensiones, tipos de datos, valores ausentes
   - Filas duplicadas, columnas vacías

2. **Pre-informe Hito 1 (sección 4-5)**: Análisis de diferencias y redundancia
   - Cálculo de tamaño de efecto
   - Matriz de correlación de Spearman
   - Decisión sobre selección secuencial

[FUENTE · Clase 5 — Análisis exploratorio, FCD-2026-2_05_AnalisisExploratorio.pdf: EDA, correlación]  
[FUENTE · Repo: 07_DATITO/casos_estudio/cancer_mama/pre_informe_hito1_cancer_mama-v02.pdf, §4-5: Hito 1]  
[FUENTE · UCI ML: Breast Cancer Wisconsin (Diagnostic), DOI: 10.24432/C5DW2B]

---

## Próximo paso: Hito 2

Una vez entendido "qué características diferencian", el Hito 2 pregunta:

**"¿Podemos predecir el diagnóstico de una muestra nueva?"**

Eso requiere:
- Partición train/test
- Validación cruzada
- Ajuste de hiperparámetros
- Evaluación final

**Continuaremos en el módulo de Matriz de Confusión y Métricas.**
