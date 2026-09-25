# Matriz de Confusión: Cáncer de Mama — EJERCICIO

## Contexto

Un modelo Random Forest fue entrenado para clasificar muestras de tumores de mama como benignos (B) o malignos (M).

**Conjunto de test**: 114 muestras
- 72 tumores realmente benignos
- 42 tumores realmente malignos

El modelo entrenado predice: benigno o maligno para cada una.

**Matriz de confusión observada** (resultado del modelo):

```
                   Predicción
                   Benigno  Maligno
Verdad  Benigno      72        0
        Maligno       3        39
```

---

## Preguntas

### Pregunta 1: Nomenclatura

Rellena la tabla con los valores de TN, TP, FN, FP:

| Celda | Símbolo | Significado | Valor |
|-------|---------|-------------|-------|
| Fila B, Col B | ? | Benigno predicho como benigno | ? |
| Fila B, Col M | ? | Benigno predicho como maligno | ? |
| Fila M, Col B | ? | Maligno predicho como benigno | ? |
| Fila M, Col M | ? | Maligno predicho como maligno | ? |

---

### Pregunta 2: Exactitud (Accuracy)

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

Calcula la exactitud del modelo. ¿Es un buen resultado? ¿Por qué no es suficiente solo con el accuracy?

---

### Pregunta 3: Precisión

$$\text{Precision} = \frac{TP}{TP + FP}$$

¿Cuál es la precisión del modelo para la clase "maligno"?

¿Qué significa este número? (Pista: "De las muestras que el modelo dice que son malignas, ¿cuántas realmente lo son?")

---

### Pregunta 4: Sensibilidad / Recall

$$\text{Recall} = \frac{TP}{TP + FN}$$

¿Cuál es el recall del modelo para la clase "maligno"?

¿Qué significa? (Pista: "De los 42 tumores realmente malignos, ¿cuántos detectó el modelo?")

¿Cuántos tumores malignos fueron no detectados?

---

### Pregunta 5: Especificidad

$$\text{Specificity} = \frac{TN}{TN + FP}$$

¿Cuál es la especificidad del modelo?

¿Qué significa?

---

### Pregunta 6: El error crítico

Tienes dos tipos de error:
- **Falso Negativo (FN)**: 3 casos — tumores malignos clasificados como benignos
- **Falso Positivo (FP)**: 0 casos — tumores benignos clasificados como malignos

¿Cuál es más grave en un contexto clínico? ¿Por qué?

---

### Pregunta 7: Comparación con otros modelos

Se entrenaron otros dos modelos en el mismo test. Sus matrices fueron:

**SVM lineal**:
```
           Predicción
           Benigno  Maligno
Verdad  B    72        0
        M     4        38
```

**Decision Tree**:
```
           Predicción
           Benigno  Maligno
Verdad  B    71        1
        M     5        37
```

Llena esta tabla:

| Modelo | Accuracy | Recall (M) | FN | FP |
|--------|----------|------------|----|-----|
| SVM | ? | ? | ? | ? |
| DecTree | ? | ? | ? | ? |
| RandFor | ? | ? | ? | ? |

¿Cuál modelo tiene mejor recall? ¿Por qué eso importa más que accuracy en un diagnóstico médico?

---

### Pregunta 8: Conexión a tu certamen

Tu examen pedía interpretar una matriz de confusión de un doctor que recibe pacientes, algunos diagnosticados.

Usando **esta** matriz de cáncer como referencia:
- Si 1000 pacientes llegan al doctor y 370 realmente tienen cáncer, ¿cuántos falsos negativos tendrías si el modelo tiene recall = 0.929?
- ¿Cuántos pacientes enfermos no serían detectados?

---

## Envío

Una vez resuelto, guarda este archivo en:

```
F:\MACI\07_DATITO\casos_estudio\entregas\
cancer_matriz_confusion_[TU_NOMBRE].md
```

Y envíamelo para corregir.
