# PRÓXIMA SESIÓN: Simulador de Predicción de Falla

## 📌 ESTADO ACTUAL

✅ **Completado**:
- Caso Wisconsin (Diagnostic) validado
- Conectado a Clase 7 (HILT)
- HTML simple creado
- Fuentes verificadas

⏸️ **PAUSADO**:
- Simulador interactivo de falla (vibración vs temperatura)

---

## 🎯 QUÉ CONSTRUIR EN PRÓXIMA SESIÓN

### HTML: `simulador_prediccion_falla.html`

**Ubicación**: `F:\MACI\07_DATITO\visual\simulador_prediccion_falla.html`

**Componentes necesarios**:

1. **Scatter plot** (Plotly o SVG)
   - Eje X: Vibración (0-10)
   - Eje Y: Temperatura (20-80°C)
   - Puntos rojos: FALLA real
   - Puntos verdes: NO FALLA real
   - LÍNEA DE DECISIÓN dinámica (ej: Vibración > 5.0 AND Temp > 60)

2. **Controles interactivos**
   - Slider: Umbral Vibración (0-10)
   - Slider: Umbral Temperatura (20-80)
   - Botón: "Actualizar predicción"

3. **Matriz de confusión EN VIVO**
   - Se actualiza conforme cambias umbrales
   - Muestra: TP, TN, FP, FN
   - Calcula: Recall, Precision, F1, AUC

4. **Histogramas**
   - Vibración (FALLA vs NO FALLA)
   - Temperatura (FALLA vs NO FALLA)
   - Superpuestos para ver separación

5. **Curva ROC dinámica**
   - TPR vs FPR
   - Se mueve conforme cambias umbrales
   - Muestra AUC

6. **Preguntas pedagógicas**
   - "¿Dónde hay mejor separación entre clases?"
   - "¿Qué error es más peligroso: FN o FP?"
   - "¿A qué umbral maxim iza el recall?"

---

## 📊 DATASET NECESARIO

Crear o usar dataset de vibración vs temperatura con:
- Mínimo 50-100 puntos
- Dos clases claramente separables
- Algo de solapamiento (realista)

Ejemplo estructura:
```
vibración,temperatura,falla
2.1,35,0
2.3,38,0
3.2,42,0
...
7.5,65,1
8.1,68,1
8.9,72,1
```

---

## 🎨 DISEÑO VISUAL

**Mantener coherencia con Datito**:
- Usar paleta CSS variables (--real, --error, --acierto)
- Layout .hoja (max-width 860px)
- Clases .caja, .peligro, .clave, .mini
- Tipografía consistente

**Inspiración**:
- `metricas_clasificacion.html` (estructura)
- `matriz_confusion_dinamica.html` (interactividad)

---

## 📚 FUENTES A VINCULAR

- [FUENTE · Clase 7 — Clasificación]
- [FUENTE · Mantenimiento Predictivo — análisis de vibración/temperatura]
- [FUENTE · Caso práctico del certamen]

---

## ✅ CHECKLIST FINAL

- [ ] HTML creado con scatter plot interactivo
- [ ] Controles de umbral funcionan
- [ ] Matriz de confusión se actualiza EN VIVO
- [ ] Histogramas muestran separación
- [ ] Curva ROC dinámica
- [ ] Preguntas de análisis integradas
- [ ] Etiquetado con fuentes HILT
- [ ] Probado con datos de ejemplo

---

## 🚀 PRÓXIMA SESIÓN

**Comienza con**:
```bash
# Abrir proyecto
cd F:\MACI
# Crear HTML en visual/
# Integrar dataset
# Probar interactividad
```

**Fin de sesión cuando**:
- HTML está listo
- Todos los gráficos funciona n
- Preguntas pedagógicas están integradas
- Cristobal puede USAR el simulador para aprender

---

## 💡 POR QUÉ ESTO IMPORTA

Este simulador enseña TODO lo que el profesor pregunta en certamen:
1. **Leer scatter plot** → ¿Dónde falla?
2. **Establecer umbral** → Línea de decisión
3. **Ver trade-off** → Matriz dinámnica
4. **Evaluar modelo** → ROC, recall, precision
5. **Transferir** → Cualquier problema clasificación

Es el puente entre **teoría (Clase 7)** y **práctica (certamen)**.

---

**Fecha propuesta**: Próxima sesión disponible

**Esfuerzo estimado**: 2-3 horas (construcción + pruebas)

**Producto final**: Herramienta de aprendizaje que Cristobal usa para DOMINAR clasificación binaria
