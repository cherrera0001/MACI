# 🚀 Quick Start: Herramientas Dinámicas

## En 5 minutos: Eje X → Procesamiento → Eje Y

### Paso 1️⃣: Abre el HTML

```
F:\MACI\07_DATITO\casos_estudio\cancer_mama\matriz_confusion_dinamica.html
```

Doble clic → Se abre en tu navegador.

### Paso 2️⃣: Verás 4 campos

```
┌─────────────────────────────────────────┐
│ TP (Verdadero Positivo):    [___39___]  │  ← Eje X entrada
│ TN (Verdadero Negativo):    [___72___]  │
│ FP (Falso Positivo):        [____0___]  │
│ FN (Falso Negativo):        [____3___]  │
└─────────────────────────────────────────┘
```

Estos 4 números son tu **entrada (eje X)**.

### Paso 3️⃣: Haz clic en "📊 Calcular Métricas"

Al instante ves:

```
┌──────────────────────────────────────────────┐
│ Accuracy ........... 0.974  (Eje Y salida)   │
│ Precision .......... 1.000  ↑                │
│ Recall ............ 0.929   │                │
│ Specificity ....... 1.000   │                │
│ F1-Score .......... 0.963   │                │
│ FPR ............... 0.000   │                │
│ FNR ............... 0.071   │                │
│ Balanced Acc ...... 0.964   │                │
└──────────────────────────────────────────────┘
```

Estas son tus **salidas (eje Y)**.

### Paso 4️⃣: Experimenta

**Cambio 1: Aumenta FN de 3 a 10**
```
Antes:  Recall=0.929
Después: Recall=0.795  ← ¡Baja!
```
¿Por qué? Porque detecta menos enfermos.

**Cambio 2: Aumenta FP de 0 a 5**
```
Antes:  Precision=1.000
Después: Precision=0.886  ← ¡Baja!
```
¿Por qué? Porque hay más falsos positivos.

### Paso 5️⃣: Botones de ejemplo

```
Botón "Cáncer de Mama (114 test)"
  ↓ Carga automáticamente
TP=39, TN=72, FP=0, FN=3

Botón "COVID-19 (100 pacientes)"
  ↓ Carga automáticamente
TP=38, TN=50, FP=5, FN=7
```

---

## Opción 2: Python Script

### Instalación (1 comando)

```bash
pip install matplotlib seaborn
```

### Uso (3 formas)

**Forma A: Línea de comandos**
```bash
cd F:\MACI\07_DATITO\casos_estudio\cancer_mama
python matriz_confusion_generador.py --tp 39 --tn 72 --fp 0 --fn 3
```

**Forma B: Con gráficos**
```bash
python matriz_confusion_generador.py --ejemplo cancer --graficar
```

**Forma C: Exportar resultados**
```bash
python matriz_confusion_generador.py --ejemplo cancer --guardar-json salida.json
```

---

## Opción 3: Python Notebook (más interactivo)

En un Jupyter Notebook:

```python
from matriz_confusion_generador import ConfusionMatrixVisualizer

# Crear
viz = ConfusionMatrixVisualizer(
    tp=39, tn=72, fp=0, fn=3,
    nombre_positivo="Maligno",
    nombre_negativo="Benigno"
)

# Ver resultados
viz.mostrar_matriz()
viz.mostrar_metricas()
viz.graficar()
```

---

## El "Eje X" y "Eje Y" (Conceptualmente)

### Entrada (Eje X) - Lo que CONTROLAS

```
4 números que DEFINES:
├─ TP: Cuántos enfermos detectó bien
├─ TN: Cuántos sanos clasificó bien
├─ FP: Cuántos sanos clasificó como enfermos
└─ FN: Cuántos enfermos clasificó como sanos
```

### Procesamiento (La Caja Negra)

```
TP, TN, FP, FN  ──┐
                 └─→ [FÓRMULAS] ──→ Accuracy, Precision, etc.
```

Ejemplo:
```python
Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
```

### Salida (Eje Y) - Lo que RESULTA

```
16 métricas calculadas automáticamente:
├─ Accuracy, Precision, Recall, Specificity
├─ F1-Score, Balanced Accuracy
├─ FPR, FNR, FDR, FOR
├─ PPV, NPV
└─ Matthews Correlation Coefficient
```

---

## Tabla: ¿Cuál herramienta usar?

| Necesidad | Herramienta | Ventaja |
|-----------|-------------|---------|
| Rápido, visual, sin instalar | HTML | Abre en navegador, offline |
| Integrar en scripts | Python script | Importable, automatizable |
| Explorar + visualizar | Notebook | Interactivo, gráficos |
| Graficar matrices | Python (--graficar) | Matplotlib + Seaborn |
| Exportar datos | Python (--guardar-json) | JSON para otros usos |

---

## Escenario: Tu pregunta de certamen

**Enunciado**: "Doctor recibe 1000 pacientes, ~370 enfermos..."

**Cómo resolverlo con la herramienta**:

1. Abre el HTML
2. Ingresa (escenario probable):
   ```
   TP = 344  (93% de 370 detectados)
   TN = 599  (95% de 630 clasificados bien)
   FP = 31   (5% falsos positivos)
   FN = 26   (7% falsos negativos)
   ```
3. Calcula
4. Lee el resultado:
   ```
   Accuracy = 0.943
   Recall = 0.930  ← Esto es lo crítico
   Precision = 0.917
   ```
5. Responde: "¿Qué tipo de error es peor?"

---

## Primeros pasos

### Opción A: Visualista (recomendado para empezar)
```
1. Abre matriz_confusion_dinamica.html
2. Carga "Cáncer de Mama"
3. Cambia 3 a FN
4. Observa que baja Recall
5. Lee HERRAMIENTAS_DINAMICAS.md para entender por qué
```

### Opción B: Programador
```bash
1. cd F:\MACI\07_DATITO\casos_estudio\cancer_mama
2. python matriz_confusion_generador.py --ejemplo cancer
3. Lees la salida de texto
4. Luego: python ... --graficar
```

### Opción C: Notebook científico
```python
1. Abre Jupyter
2. Copia el código del ejemplo
3. Ejecuta interactivamente
4. Modifica TP, TN, FP, FN en vivo
```

---

## FAQ Rápido

**P: ¿Necesito instalar algo para el HTML?**
R: No. Solo abrelo en el navegador.

**P: ¿Necesito instalar para Python?**
R: Sí, pero solo: `pip install matplotlib seaborn`

**P: ¿Los números son reales?**
R: Sí. Cáncer de Mama es real (114 test, Random Forest). COVID es ejemplo.

**P: ¿Puedo usar mis propios números?**
R: Totalmente. Cualquier TP, TN, FP, FN válido.

---

## Siguiente paso

👉 Lee: `HERRAMIENTAS_DINAMICAS.md` para entender el concepto.

Luego:
1. Abre el HTML
2. Intenta los 3 escenarios ("¿Qué cambia si...?")
3. Compara con las fórmulas
4. Responde: ¿Cuál error (FP vs FN) es más grave en medicina?
