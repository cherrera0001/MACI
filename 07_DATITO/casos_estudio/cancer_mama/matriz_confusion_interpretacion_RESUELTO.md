# Matriz de Confusión: Cáncer de Mama — RESUELTO

## Contexto

Un modelo Random Forest fue entrenado para clasificar muestras de tumores de mama como benignos (B) o malignos (M).

**Conjunto de test**: 114 muestras
- 72 tumores realmente benignos
- 42 tumores realmente malignos

**El modelo entrenado predice**: benigno o maligno para cada una.

---

## Paso 1: Armar la matriz de confusión

**Definición**: 
- Filas = clase verdadera (lo que realmente es)
- Columnas = clase predicha (lo que el modelo dice)
- Maligno = clase positiva (por importancia clínica)

```
                   Predicción
                   Benigno  Maligno
Verdad  Benigno      72        0       ← Todas benignas fueron identificadas correctamente
        Maligno       3        39      ← 39 correctas, 3 malignos clasificados como benignos
```

### Nomenclatura

| Celda | Símbolo | Significado | Fórmula |
|-------|---------|-------------|---------|
| Fila B, Col B | TN (True Negative) | Benigno predicho como benigno | 72 |
| Fila B, Col M | FP (False Positive) | Benigno predicho como maligno | 0 |
| Fila M, Col B | FN (False Negative) | Maligno predicho como benigno | 3 |
| Fila M, Col M | TP (True Positive) | Maligno predicho como maligno | 39 |

---

## Paso 2: Calcular métricas

### Exactitud (Accuracy)

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{39 + 72}{39 + 72 + 0 + 3} = \frac{111}{114} = 0.974$$

**Interpretación**: El modelo acertó el 97,4% de las clasificaciones.

**Pero espera**: 62.7% de las muestras son benignas. Un modelo que **siempre predice "benigno"** tendría:

$$\text{Accuracy}_{\text{dummy}} = \frac{72}{114} = 0.632$$

Entonces 0.974 vs 0.632 muestra que el modelo aprende algo real, no es solo el baseline.

---

### Precisión (Precision for class Maligno)

$$\text{Precision} = \frac{TP}{TP + FP} = \frac{39}{39 + 0} = 1.000$$

**Interpretación**: De las muestras que el modelo clasificó como "maligno", el 100% realmente eran malignas. **Cero falsos positivos.**

**Costo**: Si clasificas un benigno como maligno, el paciente se somete a tratamiento innecesario. Aquí eso no pasó.

---

### Sensibilidad / Recall (para clase Maligno)

$$\text{Recall} = \frac{TP}{TP + FN} = \frac{39}{39 + 3} = 0.929$$

**Interpretación**: De los 42 tumores realmente malignos, el modelo detectó 39. **Falló con 3.**

**Esto es lo más importante clínicamente**: 3 pacientes enfermos fueron clasificados como sanos. Pueden no recibir el tratamiento que necesitan.

---

### Especificidad (para clase Benigno, o equivalentemente, 1 - FPR)

$$\text{Specificity} = \frac{TN}{TN + FP} = \frac{72}{72 + 0} = 1.000$$

O equivalentemente:

$$\text{FPR} = \frac{FP}{TN + FP} = \frac{0}{72 + 0} = 0.000$$

**Interpretación**: De los 72 tumores realmente benignos, todos fueron identificados correctamente. No hay falsos alarmas.

---

## Paso 3: Interpretar el trade-off

### ¿Qué tipo de error es peor?

**Falso Negativo (3 casos)**: Maligno clasificado como benigno.
- Consecuencia: Paciente no recibe tratamiento urgente
- Riesgo: Enfermedad avanza sin intervención
- **Costo clínico: ALTO**

**Falso Positivo (0 casos)**: Benigno clasificado como maligno.
- Consecuencia: Paciente se somete a tratamiento innecesario
- Riesgo: Efectos secundarios, costos
- **Costo clínico: MEDIO**

### En este caso

El modelo tiene:
- **Precision = 1.000** (no hay falsos positivos, no hay alarmas falsas)
- **Recall = 0.929** (detecta casi todos los casos positivos, pero se pierde 3)

Esto es una **elección deliberada**: mejor dejar escapar un raro caso maligno que alarmar falsamente.

---

## Paso 4: Comparación con otros modelos

El Hito 2 comparó tres modelos en el mismo test de 114 muestras:

### SVM lineal

```
           Predicción
           Benigno  Maligno
Verdad  B    72        0
        M     4        38
```

- Accuracy: 0.965
- Recall (M): 0.905 (36 de 42 detectados)
- FN: 4 casos

### Decision Tree

```
           Predicción
           Benigno  Maligno
Verdad  B    71        1
        M     5        37
```

- Accuracy: 0.939
- Recall (M): 0.881 (37 de 42 detectados)
- FP: 1 caso
- FN: 5 casos

### Random Forest (GANADOR)

```
           Predicción
           Benigno  Maligno
Verdad  B    72        0
        M     3        39
```

- Accuracy: 0.974
- Recall (M): 0.929 (39 de 42 detectados)
- FP: 0 casos
- FN: 3 casos

---

## Comparación visual

```
           Accuracy  Recall  FN  FP  Balanced Acc.
SVM        0.965     0.905   4   0   0.952
DecTree    0.939     0.881   5   1   0.894
RandFor    0.974     0.929   3   0   0.964
```

**Por qué ganó Random Forest**:
- Highest accuracy (97.4%)
- Highest recall para malignos (92.9% detecta casos positivos)
- Cero falsos positivos (máxima precisión)
- Highest balanced accuracy (0.964)

La métrica de selección fue **balanced accuracy** = (Recall + Specificity) / 2

---

## Paso 5: Conexión a tu pregunta de certamen

Tu pregunta fue: **"Un doctor recibe 1000 pacientes, 200 son diagnosticados... [tabla de confusión]. Interpreta qué significa cada celda."**

**Nuestra matriz simplificada** (si escalamos nuestro test):

```
1000 pacientes → ~630 sanos (62.7%) + ~370 enfermos (37.3%)
                   (similar a nuestro ratio 72:42)

Predicción del modelo:
           Sano  Enfermo
Verdad  S   72%    0%       ← TN=630, FP≈0
        E    3     39        ← FN≈30, TP≈340
```

**Lo que tu examen probablemente pedía**:

1. ¿Cuál es el TN, TP, FN, FP?
   - TN = Sanos clasificados correctamente
   - FP = Sanos clasificados como enfermos (falsa alarma)
   - FN = Enfermos clasificados como sanos (miss crítico)
   - TP = Enfermos clasificados correctamente

2. ¿Qué métrica importa más?
   - **Recall (sensibilidad)** para enfermedades graves: queremos detectar a casi todos los enfermos
   - **Precisión** cuando el tratamiento es agresivo: no queremos tratar a sanos

3. ¿Por qué no es suficiente accuracy?
   - Si 630/1000 son sanos, un modelo "dummy" que siempre dice "sano" tendría 63% accuracy
   - Pero false negative rate = 100% (todos los enfermos quedan sin tratar)

---

## Resumen

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué es TP en este caso? | 39 tumores malignos correctamente identificados |
| ¿Qué es FN en este caso? | 3 tumores malignos clasificados como benignos (CRÍTICO) |
| ¿Qué es FP en este caso? | 0 tumores benignos clasificados como malignos |
| ¿Qué es TN en este caso? | 72 tumores benignos correctamente identificados |
| ¿Qué métrica mide "de los enfermos, cuántos detectamos"? | Recall = TP / (TP + FN) = 0.929 |
| ¿Qué métrica mide "de los que diagnosticamos como enfermos, cuántos realmente lo son"? | Precision = TP / (TP + FP) = 1.000 |
| ¿Cuál es el error más crítico aquí? | FN: pacientes enfermos no detectados |
| ¿Por qué? | Pueden no recibir tratamiento urgente. La enfermedad avanza. |

---

## Referencias

[FUENTE · Clase 7 — Clasificación, FCD-2026-2_07_Clasificacion.pdf: matriz de confusión, métricas]  
[FUENTE · Repo: 07_DATITO/casos_estudio/cancer_mama/preinforme_hito2_v02.pdf, §6: resultados Hito 2]  
[FUENTE · Repo: 07_DATITO/casos_estudio/cancer_mama/Presentacion_Hito2_v2_2.pdf, Diapositiva 12-15: visualización]  
[FUENTE · UCI ML: Breast Cancer Wisconsin (Diagnostic), DOI: 10.24432/C5DW2B]  
[FUENTE · Paper: Street, Wolberg, Mangasarian (1993): "Nuclear Feature Extraction for Breast Tumor Diagnosis", SPIE 1905]
