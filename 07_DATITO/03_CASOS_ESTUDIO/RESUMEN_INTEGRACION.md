# 📊 RESUMEN: Integración Caso Cáncer de Mama + Herramientas Dinámicas

## Lo que hemos construido

### 1️⃣ Caso Completo: Cáncer de Mama

**Carpeta**: `F:\MACI\07_DATITO\casos_estudio\cancer_mama\`

**Contenido**:

| Archivo | Tipo | Propósito |
|---------|------|----------|
| `README.md` | Resumen | Por qué este caso, estructura, cifras |
| `INDICE.md` | Navegación | Índice completo de todos los materiales |
| `analisis_exploratorio_RESUMEN.md` | Guía | Hito 1: EDA, tamaño de efecto, correlación |
| `matriz_confusion_interpretacion_RESUELTO.md` | Educativo | Paso a paso: construcción, métricas, interpretación |
| `matriz_confusion_interpretacion_VACIO.md` | Ejercicio | 8 preguntas para resolver (con solución al lado) |
| 3 PDFs | Referencia | Preinforme Hito 1 + Hito 2 + Presentación |

---

### 2️⃣ Herramientas Dinámicas (NUEVO - Lo que pediste)

Tres formas de experimentar con Eje X → Procesamiento → Eje Y:

#### A) HTML Interactivo (Recomendado para empezar)

**Archivo**: `matriz_confusion_dinamica.html`

```
✨ SIN INSTALAR NADA
✨ SIN CÓDIGO
✨ Offline (funciona sin internet)
```

**Cómo funciona**:
1. Abre en navegador
2. Ingresa 4 números: TP, TN, FP, FN
3. Haz clic en "Calcular"
4. **Al instante**: Accuracy, Precision, Recall, F1, FPR, etc.
5. Heatmap se redibuja automáticamente

**Experimenta con**:
- Cáncer de Mama (predefinido): TP=39, TN=72, FP=0, FN=3
- COVID-19 (predefinido): TP=38, TN=50, FP=5, FN=7
- Tus propios números

**Pregunta reflexiva**: ¿Qué cambia si aumentas FN de 3 a 10? ¿Y FP de 0 a 5?

#### B) Python Script (Para automatizar)

**Archivo**: `matriz_confusion_generador.py`

**Instalación**:
```bash
pip install matplotlib seaborn
```

**Uso**:
```bash
# Línea de comandos
python matriz_confusion_generador.py --tp 39 --tn 72 --fp 0 --fn 3

# Con ejemplos
python matriz_confusion_generador.py --ejemplo cancer
python matriz_confusion_generador.py --ejemplo covid

# Con gráficos
python matriz_confusion_generador.py --ejemplo cancer --graficar

# Exportar
python matriz_confusion_generador.py --ejemplo cancer --guardar-json salida.json
```

**Usa en Python**:
```python
from matriz_confusion_generador import ConfusionMatrixVisualizer

viz = ConfusionMatrixVisualizer(tp=39, tn=72, fp=0, fn=3)
viz.mostrar_metricas()
viz.graficar()
```

**Calcula** 16 métricas automáticamente.

#### C) Documentación

**Archivo**: `QUICK_START_DINAMICAS.md`
- Cómo usar en 5 minutos (paso a paso)
- Tabla de cuándo usar cada herramienta

**Archivo**: `HERRAMIENTAS_DINAMICAS.md`
- Explicación conceptual: Eje X → Procesamiento → Eje Y
- 3 escenarios de experimentación
- Cómo escalar a 1000 pacientes (tu pregunta de certamen)

---

## Estructura de carpetas

```
F:\MACI\07_DATITO\casos_estudio\
├── cancer_mama/                           ← Tu caso principal
│   ├── README.md                          (resumen)
│   ├── INDICE.md                          (navegación)
│   ├── analisis_exploratorio_RESUMEN.md   (Hito 1)
│   ├── matriz_confusion_interpretacion_RESUELTO.md    (solución)
│   ├── matriz_confusion_interpretacion_VACIO.md       (ejercicio)
│   │
│   ├── matriz_confusion_dinamica.html     ⭐ (abre en navegador)
│   ├── matriz_confusion_generador.py      (Python script)
│   ├── QUICK_START_DINAMICAS.md           (guía rápida)
│   ├── HERRAMIENTAS_DINAMICAS.md          (conceptual)
│   │
│   ├── pre_informe_hito1_cancer_mama-v02.pdf
│   ├── preinforme_hito2_v02.pdf
│   └── Presentacion_Hito2_v2_2.pdf
│
├── entregas/                              (deja aquí tus respuestas)
│   └── (vacío, para que guardes ejercicios)
│
└── RESUMEN_INTEGRACION.md                 (este archivo)
```

---

## Mapeo al Curriculum de Datito

Hemos actualizado `curriculum.yaml` para vincular el caso del cáncer en **5 conceptos**:

| Concepto | Nuevo material | Pregunta de diagnóstico |
|----------|---|---|
| **11 · Matriz de confusión** | RESUELTO + VACIO + Dinámicas | "¿Cuál error (FN vs FP) es más grave?" |
| **12 · Métricas de clasificación** | Comparación 3 modelos | "¿Por qué recall > accuracy en medicina?" |
| **13 · ROC y AUC** | Curvas reales (0.995 RF, 0.922 DT) | "¿Qué explica la diferencia?" |
| **14 · Árboles de decisión** | Decision Tree: recall 0.881 | "¿Por qué peor generalizacion?" |
| **15 · Random Forest** | RF ganador (39 TP, 3 FN) | "¿Qué hace RF que no hace árbol?" |

---

## Flujo de uso recomendado

### Fase 1: Entender (Teórico)
1. Lee `README.md` (5 min)
2. Lee `analisis_exploratorio_RESUMEN.md` (10 min)
3. Lee `matriz_confusion_interpretacion_RESUELTO.md` (30 min)

### Fase 2: Experimentar (Dinámico)
1. Abre `matriz_confusion_dinamica.html` en navegador
2. Carga "Cáncer de Mama"
3. Cambiar valores, observa cambios
4. Lee `HERRAMIENTAS_DINAMICAS.md` mientras experimentas

### Fase 3: Resolver (Práctico)
1. Intenta `matriz_confusion_interpretacion_VACIO.md` (8 preguntas)
2. Usa el HTML para verificar tus cálculos
3. Guarda solución en `entregas/`

### Fase 4: Transferir (Tu certificado)
1. Aplica la lógica a **tu pregunta de certamen** (1000 pacientes)
2. Modela con el HTML: TP=344, TN=599, FP=31, FN=26
3. Interpreta los resultados

---

## Preguntas clave que puedes responder AHORA

### Con el HTML dinámico

**P1**: Si el modelo tiene Recall=0.929 con 42 malignos en test,
¿cuántos enfermos no detecta?
- Respuesta: 42 × (1-0.929) = 3 no detectados

**P2**: Si escalamos a 1000 pacientes con 37% positivos,
¿cuántos falsos negativos tendríamos con recall=0.93?
- Respuesta: 370 × (1-0.93) = 26 no detectados

**P3**: ¿Es mejor tener Precision=0.95 o Recall=0.95 en diagnóstico?
- Respuesta: **Recall > Precision** (better to alarm than miss)

**P4**: ¿Qué sucede a las métricas si cambias FN de 3 a 10?
- Usa el HTML, cambia, observa qué baja

**P5**: ¿Qué sucede a las métricas si cambias FP de 0 a 5?
- Usa el HTML, cambia, observa qué baja

---

## Checklist: ¿Qué dominas?

- [ ] Puedo construir una matriz de confusión desde predicciones
- [ ] Entiendo TP, TN, FP, FN conceptualmente
- [ ] Puedo calcular Accuracy, Precision, Recall sin error
- [ ] Sé cuándo Recall importa más que Accuracy
- [ ] Entiendo por qué FN es más grave que FP en medicina
- [ ] Puedo comparar dos modelos por recall/FPR
- [ ] Puedo escalar de 100 a 1000 pacientes mentalmente
- [ ] Puedo usar el HTML para verificar mis cálculos
- [ ] Puedo usar el Python script para automatizar
- [ ] Puedo responder tu pregunta de certamen (doctor + 1000 pacientes)

---

## Próximo paso

### Opción 1: Visual (Recomendado si eres nuevo)
```
1. Abre matriz_confusion_dinamica.html
2. Carga "Cáncer de Mama"
3. Cambia FN a 10, observa Recall
4. Lee HERRAMIENTAS_DINAMICAS.md
```

### Opción 2: Teórico
```
1. Lee matriz_confusion_interpretacion_RESUELTO.md completamente
2. Intenta VACIO.md
3. Compara con el HTML
```

### Opción 3: Práctico
```
1. python matriz_confusion_generador.py --ejemplo cancer
2. python matriz_confusion_generador.py --ejemplo cancer --graficar
3. Modifica código para tus propios valores
```

---

## Contacto / Dudas

Si tienes dudas:
```
/datito
"Explícame matriz de confusión con el ejemplo del cáncer de mama"

Datito te hará preguntas y te guiará.
```

O intenta con las herramientas dinámicas y mira si la pregunta se responde sola.

---

## Resumen ejecutivo

✅ **Caso integrado**: Cáncer de mama (114 test, Random Forest)
✅ **Herramientas dinámicas**: HTML + Python script + docs
✅ **Curriculum actualizado**: 5 conceptos ahora referencian este material
✅ **Escalable**: De 100 a 1000 pacientes (tu pregunta de certamen)
✅ **Listo para usar**: Abre el HTML, ingresa números, calcula

**Tiempo para dominar**: 2-3 horas (lectura + experimentación)
**Aplicación**: Tu pregunta de certamen sobre doctor + matriz de confusión
