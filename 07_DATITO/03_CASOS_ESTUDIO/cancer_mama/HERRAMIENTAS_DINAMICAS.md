# Herramientas Dinámicas: Matriz de Confusión con Entrada de Datos

## ¿Qué significa "dinámico"?

**Estático**: Guía PDF con números fijos (39, 72, 0, 3). Lees una vez.
**Dinámico**: Herramienta que **responde a tus inputs**. Cambias un número, todas las métricas se recalculan.

---

## 🎯 Los tres ejes de entrada

Cualquier matriz de confusión es un **espacio de 4 números**:

```
Entrada (eje de datos):
    TP (True Positive)   ← Puedo cambiar
    TN (True Negative)   ← Puedo cambiar
    FP (False Positive)  ← Puedo cambiar
    FN (False Negative)  ← Puedo cambiar

Salida (automática):
    Accuracy
    Precision
    Recall
    Specificity
    F1-Score
    FPR, FNR, etc.
```

**Lo "dinámico" es**: cambias **entrada** → recalcula **salida** al instante.

---

## Herramienta 1️⃣: HTML Interactivo (Sin código)

**Archivo**: `matriz_confusion_dinamica.html`

### Cómo usarla

1. Abre el archivo en tu navegador
2. Verás 4 campos de entrada:
   ```
   TP (Verdadero Positivo): [___]
   TN (Verdadero Negativo): [___]
   FP (Falso Positivo):     [___]
   FN (Falso Negativo):     [___]
   ```
3. Cambia cualquier número
4. Haz clic en "📊 Calcular Métricas"
5. **Al instante**:
   - Tabla actualizada
   - Heatmap redibujado
   - Todas las métricas recalculadas

### Ejemplos predefinidos

- Botón "Cáncer de Mama": TP=39, TN=72, FP=0, FN=3
- Botón "COVID-19": TP=38, TN=50, FP=5, FN=7

### Preguntas que puedes responder

**P1**: ¿Qué pasa si cambio FN de 3 a 10?
- Recall baja de 0.929 a 0.795
- Balanced Accuracy baja
- FNR sube

**P2**: ¿Y si cambio FP de 0 a 5?
- Precision baja de 1.000 a 0.886
- Specificity baja de 1.000 a 0.933
- FPR sube

**P3**: ¿Cuál cambio es más grave en diagnóstico médico?
- Aumentar FN (miss enfermos) es más crítico que aumentar FP

---

## Herramienta 2️⃣: Python Script (Máximo control)

**Archivo**: `matriz_confusion_generador.py`

### Instalación

```bash
# Opción 1: Línea de comandos
python matriz_confusion_generador.py --tp 39 --tn 72 --fp 0 --fn 3

# Opción 2: Con ejemplos
python matriz_confusion_generador.py --ejemplo cancer
python matriz_confusion_generador.py --ejemplo covid
python matriz_confusion_generador.py --ejemplo doctor_1000

# Opción 3: Con gráficos
python matriz_confusion_generador.py --tp 39 --tn 72 --fp 0 --fn 3 --graficar

# Opción 4: Exportar
python matriz_confusion_generador.py --ejemplo cancer --guardar-json salida.json
```

### Uso en Python (dentro de un Notebook)

```python
from matriz_confusion_generador import ConfusionMatrixVisualizer

# Crear visualizador
viz = ConfusionMatrixVisualizer(
    tp=39, tn=72, fp=0, fn=3,
    nombre_positivo="Maligno",
    nombre_negativo="Benigno",
    nombre_modelo="Random Forest - Cáncer"
)

# Ver resultados
viz.mostrar_matriz()      # Tabla
viz.mostrar_metricas()    # Todas las métricas
viz.graficar()            # Gráficos (matplotlib)

# Obtener como diccionario
resultados = viz.resumen_ejecutivo()
print(f"Accuracy: {resultados['metricas_principales']['accuracy']}")

# Exportar
viz.exportar_json("resultados.json")
viz.exportar_csv("matriz.csv")
```

### Estructura interna (Eje X y Eje Y)

**Entrada (Input Space)**:
```python
TP, TN, FP, FN  ← Tus 4 números
```

**Procesamiento**:
```python
def accuracy():
    return (TP + TN) / (TP + TN + FP + FN)

def precision():
    return TP / (TP + FP) if (TP + FP) > 0 else 0

def recall():
    return TP / (TP + FN) if (TP + FN) > 0 else 0

... (más 13 métricas)
```

**Salida (Output Space)**:
```python
{
  "accuracy": 0.974,
  "precision": 1.000,
  "recall": 0.929,
  "specificity": 1.000,
  "f1_score": 0.963,
  "fpr": 0.000,
  "fnr": 0.071,
  "balanced_accuracy": 0.964,
  ...
}
```

---

## Herramienta 3️⃣: Plantilla en Jupyter Notebook

*(Próximamente)* - Notebook que combine entrada dinámica + visualización + explicación.

---

## Pensando en Ejes: Entrada → Procesamiento → Salida

### Eje X: Entrada (que tú controlas)

```
TP ←─── (0 a ∞)
TN ←─── (0 a ∞)
FP ←─── (0 a ∞)
FN ←─── (0 a ∞)
```

Estos 4 números define **completamente** el desempeño de un modelo.

### Eje Y: Salida (calculada)

```
Accuracy     ←─── f(TP, TN, FP, FN)
Precision    ←─── f(TP, FP)
Recall       ←─── f(TP, FN)
Specificity  ←─── f(TN, FP)
F1-Score     ←─── f(Precision, Recall)
FPR          ←─── f(FP, TN)
FNR          ←─── f(FN, TP)
...
```

Cada métrica es una **función determinista** de los 4 inputs.

---

## Ejercicio interactivo: ¿Qué cambia si...?

Usa `matriz_confusion_dinamica.html` para responder:

### Escenario 1: Mejoras el modelo (más TN)
```
Antes: TP=39, TN=72, FP=0, FN=3
Después: TP=39, TN=75, FP=0, FN=3  ← +3 en TN
```
**¿Qué cambia?** (Calcula ambos casos)
- [ ] Accuracy sube
- [ ] Precision no cambia (sigue siendo 1.000)
- [ ] Recall no cambia
- [ ] Specificity sube

### Escenario 2: Empeoras la detección (más FN)
```
Antes: TP=39, TN=72, FP=0, FN=3
Después: TP=39, TN=72, FP=0, FN=10  ← +7 en FN
```
**¿Qué cambia?** (Calcula ambos casos)
- [ ] Recall baja (crítico)
- [ ] FNR sube
- [ ] Balanced Accuracy baja
- [ ] Specificity no cambia

### Escenario 3: Más alarmas falsas (más FP)
```
Antes: TP=39, TN=72, FP=0, FN=3
Después: TP=39, TN=72, FP=5, FN=3  ← +5 en FP
```
**¿Qué cambia?** (Calcula ambos casos)
- [ ] Precision baja (importante)
- [ ] Specificity baja
- [ ] FPR sube
- [ ] Recall no cambia

---

## Escalabilidad: De 100 a 1000 pacientes

### Tu pregunta de certamen

"Un doctor recibe 1000 pacientes, 370 tienen la enfermedad..."

**Cómo modelarlo**:

Si el modelo tiene:
- Recall = 0.93 → detecta 370 × 0.93 = 344 enfermos
- FN = 370 - 344 = 26 no detectados
- FPR = 0.05 → 630 × 0.05 = 31 falsos positivos

Entonces en 1000 pacientes:
```
TP = 344
TN = 599
FP = 31
FN = 26
Total = 1000
```

**Cálculo**:
```
Accuracy = (344 + 599) / 1000 = 0.943
Recall = 344 / (344 + 26) = 0.930
Precision = 344 / (344 + 31) = 0.917
```

**Visualiza esto en el HTML**:
1. Ingresa TP=344, TN=599, FP=31, FN=26
2. Haz clic en "Calcular"
3. Observa cómo cambian las métricas

---

## Comparación de modelos

**¿Cómo comparar dos modelos dinámicamente?**

Abre DOS pestañas del HTML con:

**Pestaña 1** (Modelo A - SVM):
```
TP=38, TN=72, FP=0, FN=4
Accuracy=0.965, Recall=0.905
```

**Pestaña 2** (Modelo B - Random Forest):
```
TP=39, TN=72, FP=0, FN=3
Accuracy=0.974, Recall=0.929
```

**Pregunta**: ¿Cuál es mejor?
- RF ganó en Accuracy (+0.009)
- RF ganó en Recall (+0.024)
- RF detectó 1 maligno más

---

## API de la clase ConfusionMatrixVisualizer

### Métodos de entrada

```python
viz = ConfusionMatrixVisualizer(
    tp=39, tn=72, fp=0, fn=3,
    nombre_positivo="Maligno",
    nombre_negativo="Benigno"
)
```

### Métodos de salida

| Método | Retorna | Fórmula |
|--------|---------|---------|
| `accuracy()` | float | (TP+TN)/Total |
| `precision()` | float | TP/(TP+FP) |
| `recall()` | float | TP/(TP+FN) |
| `specificity()` | float | TN/(TN+FP) |
| `f1_score()` | float | 2×(P×R)/(P+R) |
| `false_positive_rate()` | float | FP/(FP+TN) |
| `false_negative_rate()` | float | FN/(FN+TP) |
| `balanced_accuracy()` | float | (Recall+Spec)/2 |
| `matthews_correlation_coefficient()` | float | Correlación (-1 a 1) |
| `resumen_ejecutivo()` | dict | Todas las métricas |

### Métodos de visualización

```python
viz.mostrar_matriz()       # Tabla de texto
viz.mostrar_metricas()     # Todas las métricas
viz.graficar()             # Matplotlib: heatmap + barras
viz.exportar_json(ruta)    # Guardar como JSON
viz.exportar_csv(ruta)     # Guardar matriz como CSV
```

---

## FAQ

**P: ¿Debo memorizar las fórmulas?**
R: No. La herramienta las calcula. Entiende **por qué** cada métrica importa.

**P: ¿Por qué 4 números definen todo?**
R: La matriz de confusión es una partición exhaustiva:
- Positivos reales = TP + FN
- Negativos reales = TN + FP
- Total = TP + TN + FP + FN

Cada métrica es una combinación de esos 4.

**P: ¿Puedo usar esto para mi dataset?**
R: Sí. Si tienes predicciones y etiquetas reales:
```python
from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
viz = ConfusionMatrixVisualizer(tp=tp, tn=tn, fp=fp, fn=fn)
viz.mostrar_metricas()
```

**P: ¿Hay versión online?**
R: Sí, el HTML funciona offline. Abrilo en cualquier navegador.

---

## Lectura recomendada

1. Abre `matriz_confusion_dinamica.html`
2. Carga "Cáncer de Mama"
3. Cambia FN de 3 a 10
4. Observa cómo baja Recall
5. Ahora cambia FP de 0 a 5
6. Observa cómo baja Precision
7. Pregúntate: ¿Cuál cambio es más grave en diagnóstico médico?
8. Lee `matriz_confusion_interpretacion_RESUELTO.md` para la respuesta

---

## Próximo paso

Una vez dominado el concepto con números pequeños (114 pacientes),
escala mentalmente a 1000 pacientes como en tu pregunta de certamen.

Las fórmulas no cambian. Solo los números.
