# Plan de Iteración: Certamen 3 FCD 2026
## Elevación de calidad a estándar P1a_roc_detallado.html

---

## INVENTARIO ESTADO ACTUAL

### HTML Actual: certamen3_examen_fcd2026.html (1015 líneas)
- ✓ Estructura base (10 subpreguntas)
- ✗ Usa CDN (Chart.js) → ELIMINAR
- ✗ Details muy cortos (5-10 líneas máximo)
- ✗ Falta "¿Qué pasó?" explicativo para cada subpregunta
- ✗ No tiene tablas con números/cálculos
- ✗ Falta contexto matemático
- ✗ Checklists mínimos o ausentes
- ✗ Errores comunes superficiales

### Referencia P1a_roc_detallado.html
- ✓ Sin CDN (Canvas 2D local)
- ✓ Estructura clara: ¿Qué pasó? + Cómo se resuelve + Detalles + Respuesta correcta + Errores + Checklist
- ✓ Tablas con datos completos
- ✓ Gráficos con Canvas 2D
- ✓ Explicaciones contextuales
- ✓ Errores típicos documentados

---

## ESPECIFICACIÓN 6 BLOQUES POR SUBPREGUNTA

### Bloque 1: Enunciado Literal
- Texto exacto del PDF
- Puntaje visible
- Contexto del problema

### Bloque 2: ¿Qué Pasó?
- Qué datos/gráficos proporciona el examen
- Qué variables están involucradas
- Tablas de lecturas si es necesario
- Contexto del problema real

### Bloque 3: Cómo Se Resuelve (Pasos 1...N)
- Pasos numerados y claros
- Fórmulas cuando aplique
- Ejemplos numéricos
- Orden lógico

### Bloque 4: Detalles en <details> (Educativo)
- Definiciones de conceptos
- "¿Por qué?" responder dudas comunes
- Analogías si ayudan
- Referencias a conceptos previos

### Bloque 5: <details class="resp"> Respuesta Correcta
- Respuesta esperada completa
- Pasos de resolución detallados
- Error típico más común (etiqueta G4)
- Cómo evitarlo

### Bloque 6: Errores Comunes + Checklist
- ≥3 errores típicos con explicación
- Checklist de verificación (5-8 items)
- "¿Tu respuesta es correcta?" → validación

---

## PLAN POR SUBPREGUNTA

### P1a: Dibujar Curva ROC del Modelo 1 (0.5 pts)

**OBJETIVO:** Estudiante dibuja curva ROC usando datos confusos de dos gráficos

**REPRESENTACIÓN FALTANTE:**
- Tabla lectura α → VP, FN, FP, VN completa
- Tabla cálculo TPR, FPR para cada α
- Gráfico ROC dibujado con Canvas 2D
- Referencia diagonal (clasificador aleatorio)

**MATEMÁTICA:**
- TPR = VP / (VP + FN)
- FPR = FP / (FP + VN)

**GRAFO:**
- Scatter plot (FPR, TPR)
- Línea conectando puntos en orden α
- Diagonal de referencia

**EVIDENCIA DE COMPRENSIÓN:**
- Lee correctamente 2 gráficos
- Normaliza por totales
- Grafica en ejes correctos
- Interpreta (0,0), (1,1), (0,1)

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Dos gráficos de entrada + tabla lecturas
3. ✓ 4 pasos: ROC def → cálculo TPR/FPR → tabla → graficar
4. ✓ Details: qué es ROC, ejes, puntos especiales, lectura AUC
5. ✓ Respuesta: tabla completa + gráfico + etiqueta G4
6. ✓ 4 errores + checklist

---

### P1b: ¿Qué Modelo Es Mejor? (0.5 pts)

**OBJETIVO:** Comparar Modelo 1 vs Modelo 2 (curva ROC dada) mediante AUC e interpretación

**REPRESENTACIÓN FALTANTE:**
- Curva ROC ambos modelos superpuestos
- Área bajo cada curva (AUC visual o numérico)
- Tabla comparativa: AUC, complejidad, interpretación

**MATEMÁTICA:**
- AUC es el área entre curva y diagonal
- Modelo con AUC mayor es mejor
- Pero considerar contexto (sensibilidad vs especificidad)

**GRAFO:**
- Ambas curvas ROC en mismo gráfico
- Diagonal de referencia
- Sombreado del área bajo la curva

**EVIDENCIA:**
- Reconoce AUC > 0.5 = mejor que aleatorio
- Compara posición de curvas
- Justifica según contexto clínico

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Dos gráficos ROC (Modelo 1 del paso anterior, Modelo 2 del PDF)
3. ✓ Pasos: definir AUC → calcular o estimar → comparar → justificar
4. ✓ Details: AUC significa qué, área bajo curva visual, interpretación
5. ✓ Respuesta: "Modelo 2 es mejor porque AUC > AUC_modelo1" + explicación
6. ✓ 3 errores (confundir AUC con exactitud, ignorar contexto, etc) + checklist

---

### P1c: Umbral α Para Detectar 100% Enfermos (0.5 pts)

**OBJETIVO:** Seleccionar α minimizando falsos positivos manteniendo TPR = 1.0

**REPRESENTACIÓN FALTANTE:**
- Tabla de TPR por α
- Tabla de FP mensuales por α
- Visualización del umbral en la curva ROC

**MATEMÁTICA:**
- TPR = 1.0 requiere α ≥ 2 (del PDF)
- FP mensuales = FP × (1000 - 200) / (FP + VN) × (1000 - 200)
  O más directo: si hay FP en gráfico, escalar a 1000 pacientes

**CONTEXTO CLÍNICO:**
- 1000 pacientes/mes
- 200 enfermos realmente
- 800 sanos
- Queremos sensibilidad = 100% (detectar todos los 200)
- Minimizar falsos positivos entre los 800

**EVIDENCIA:**
- Identifica α donde TPR es máximo
- Calcula FP totales
- Justifica trade-off sensibilidad/especificidad

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts) con contexto clínico
2. ✓ Tabla valores α con TPR (de P1a)
3. ✓ Pasos: buscar TPR=1, mínimo FP, justificar
4. ✓ Details: por qué importa TPR=1 en medicina, sensibilidad vs especificidad
5. ✓ Respuesta: α=2 es óptimo, TPR=1, FP mínimo
6. ✓ Errores: ignorar TPR, elegir α con mayor AUC pero TPR<1, etc

---

### P1d: Falsos Positivos Mensuales en Ese Umbral (0.5 pts)

**OBJETIVO:** Cuantificar pacientes sanos etiquetados como enfermos a escala mensual

**MATEMÁTICA:**
- α = 2: FP = 2, VN = 3 (del gráfico)
- Total de sanos = 1000 - 200 = 800
- Escalar FP: si en muestra hay 5 totales (FP+VN), en 1000 pacientes:
  FP_escalado = 2 × 800 / 5 = 320
  
  O si los números del gráfico ya están escalados a los 800 sanos:
  FP_escalado = 2 × 800 / 5 = 320

**EVIDENCIA:**
- Entiende el escalamiento
- Usa la métrica correcta
- Contextualiza en el problema real

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Datos de α=2 (FP=2, VN=3, total sanos=800)
3. ✓ Pasos: identificar FP en umbral → escalar a población → calcular
4. ✓ Details: por qué escalar, qué significa "320 pacientes etiquetados falsamente"
5. ✓ Respuesta: 320 pacientes (o cálculo que llevó a ese número)
6. ✓ Errores: olvidar escalar, confundir con TP, etc

---

### P2a: ¿Usar Grado 10? (0.5 pts)

**OBJETIVO:** Reconocer overfitting por brecha RMSE entrenamiento vs prueba

**REPRESENTACIÓN FALTANTE:**
- Tabla RMSE para todos los grados
- Gráfico RMSE_train vs RMSE_test por grado (líneas o barras)
- Visualización del gap

**MATEMÁTICA:**
- Gap = RMSE_prueba - RMSE_entrenamiento
- Grado 10: gap = 79 - 6 = 73 (enorme) → overfitting
- Grado 3: gap = 30 - 27 = 3 (mínimo)

**CONCEPTO CLAVE:**
- RMSE bajo en entrenamiento no garantiza buen desempeño futuro
- Buscar modelo que generalice bien (validación fuera de muestra)

**EVIDENCIA:**
- Reconoce la trampa: buen RMSE entrenamiento ≠ buen modelo
- Usa RMSE prueba para decidir
- Identifica overfitting por brecha

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Tabla RMSE entrenamiento y prueba para grados 1-10
3. ✓ Pasos: leer RMSE_entrenamiento (6) → leer RMSE_prueba (79) → comparar → conclusión
4. ✓ Details: overfitting, validación cruzada, por qué brecha = problema
5. ✓ Respuesta: NO, grado 10 overfitting, gap enorme (79-6=73)
6. ✓ Errores: elegir por RMSE bajo sin ver prueba, confundir "bajo" con "bueno"

---

### P2b: Qué Grado Elegir Para Predicciones Futuras (0.5 pts)

**OBJETIVO:** Seleccionar grado minimizando RMSE de prueba (mejor generalización)

**REPRESENTACIÓN FALTANTE:**
- Gráfico RMSE_prueba vs grado
- Tabla con grados 1-10, RMSE_entrenamiento, RMSE_prueba, brecha
- Marcación del punto óptimo

**MATEMÁTICA:**
- Grado 3: RMSE_prueba = 30 (mejor)
- Grado 2: RMSE_prueba = 43
- Grado 1: RMSE_prueba = 62
- Grado 5: RMSE_prueba = 34 (peor que 3)
- Grado 10: RMSE_prueba = 79 (peor aún)

**TRADE-OFF:**
- Sesgo: modelo simple (grado 1) no captura patrón → RMSE alto
- Varianza: modelo complejo (grado 10) overfits → RMSE prueba alto
- Punto óptimo: grado 3 (Bias-Variance trade-off)

**EVIDENCIA:**
- Compara RMSE_prueba solo (no entrenamiento)
- Justifica con sesgo-varianza
- Entiende el trade-off

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Tabla completa con todos los grados
3. ✓ Pasos: revisar RMSE_prueba para c/grado → identificar mínimo → justificar
4. ✓ Details: bias-variance trade-off, underfitting vs overfitting, validación
5. ✓ Respuesta: grado 3 (RMSE_prueba=30, menor que otros)
6. ✓ Errores: elegir por entrenamiento, no considerar prueba, confundir brecha

---

### P2c: Interpretar Media, Desv.Std, RMSE Para Grado 3 (1 punto)

**OBJETIVO:** Explicar qué significa cada métrica en contexto de consumo eléctrico

**DATOS PARA GRADO 3:**
- RMSE entrenamiento: 27 kWh
- RMSE prueba: 30 kWh
- Media del error: 3 kWh
- Desv.Std del error: 30 kWh

**REPRESENTACIÓN FALTANTE:**
- Definición de cada métrica
- Tabla con interpretación contexto (kWh)
- Distribución de errores (gráfico o descripción)
- Ejemplo: "Si consumo real = 100 kWh, predicción promedio = 103 kWh"

**MATEMÁTICA:**
- RMSE = √(promedio(error²)) = medida de dispersión en escala original
- Media = sesgo sistemático (¿predice más o menos?)
- Desv.Std = variabilidad de los errores (¿predice consistentemente?)

**INTERPRETACIÓN CONTEXTO:**
- Media=3: modelo subestima 3 kWh en promedio (sesgo)
- Desv.Std=30: ±30 kWh de variación alrededor de esa media (incertidumbre)
- RMSE=30: error típico = 30 kWh (raíz de media de errores al cuadrado)

**EVIDENCIA:**
- Diferencia entre media (sesgo) y desv.std (variabilidad)
- Relación media² + desv.std² ≈ RMSE² (Var = E[X²] - E[X]²)
- Contextualiza en consumo eléctrico (kWh)

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (1 punto, peso mayor)
2. ✓ Tabla valores + definiciones formales
3. ✓ 3 pasos: explicar media → explicar desv.std → explicar RMSE
4. ✓ Details: relación media-varianza, RMSE vs MAE, sesgo sistemático
5. ✓ Respuesta: contexto claro para cada métrica en kWh
6. ✓ Errores: confundir media con RMSE, ignorar desv.std, no contextualizar

---

### P3a: Dos Conclusiones Adopción IA (0.5 pts)

**OBJETIVO:** Leer gráfico McKinsey e interpretar brecha adopción-integración

**REPRESENTACIÓN FALTANTE:**
- Gráfico Original: McKinsey IA adoption (2017-2025)
- Dos líneas: "Uso de IA en ≥1 función" (88% en 2025) y "Uso de IA generativa" (33 en 2024, 65 proyectado 2025)
- Barra de desglose 2025: 7% completamente desplegada, 31% escalando, 30% pilotos, 32% experimentando

**CONCLUSIONES ESPERADAS:**
1. Adopción crece: 20% (2017) → 88% (2025) pero...
2. Integración baja: solo 7% completamente integrada en 2025
   → Brecha: muchos usan IA superficialmente, pocos la han integrado

**MATEMÁTICA SIMPLE:**
- 88% - 7% = 81% no está completamente integrada
- Implicación: la mayoría está en pilotos, experimentación, escalamiento

**EVIDENCIA:**
- Lee números del gráfico
- Interpreta la brecha
- Contextualiza en empresa del caso (mantenimiento de maquinaria)

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Gráfico McKinsey (descripción o recreación)
3. ✓ Pasos: lectura primer número → lectura segundo número → comparación → conclusión
4. ✓ Details: qué significa "completamente desplegada", por qué brecha, fases de adopción
5. ✓ Respuesta: dos conclusiones claras (crecer + brecha integración)
6. ✓ Errores: confundir dos líneas, ignorar barra desglose, solo mencionar crecimiento

---

### P3b: Problema Calidad de Datos - Histograma (0.5 pts)

**OBJETIVO:** Reconocer calibración de sensores por histograma bimodal

**REPRESENTACIÓN FALTANTE:**
- Histograma con dos picos (Proveedor 1 y Proveedor 2)
- Tabla de estadísticos por proveedor
- Explicación visual de "calibración diferente"

**PROBLEMA IDENTIFICABLE:**
- Pico 1: centrado en ~60°C (Proveedor 1, sensor frío)
- Pico 2: centrado en ~140°C (Proveedor 2, sensor caliente)
- Bimodal = dos distribuciones diferentes

**CAUSA RAÍZ:**
- Sensores de distintos proveedores miden diferente
- Calibración offset diferente entre proveedores
- Al integrar en una BD sin corrección, dos distribuciones

**CÓMO COMPROBAR:**
- Separar datos por proveedor
- Comparar estadísticos (media, desv.std por proveedor)
- Gráfico de densidad por proveedor

**CÓMO CORREGIR:**
1. Estandarizar dentro de cada proveedor (restar media de proveedor)
2. O calibrar sensores vs referencia
3. O usar factores de corrección por proveedor

**EVIDENCIA:**
- Identifica causa (origen de los datos)
- Propone comprobación (separación por proveedor)
- Sugiere corrección (estandarización o calibración)

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Histograma bimodal + etiquetas "Proveedor 1" y "Proveedor 2"
3. ✓ Pasos: identificar dos picos → reconocer proveedores → hipótesis calibración
4. ✓ Details: qué es calibración, offset de sensores, por qué integración crea bimodal
5. ✓ Respuesta: "Calibración diferente entre proveedores" + comprobación + corrección
6. ✓ Errores: pensar que es ruido, ignorar origen, no proponer corrección

---

### P3c: Limitaciones LLM + Modelo Alternativo (0.5 pts)

**OBJETIVO:** Comparar LLM aislado vs LLM + herramientas (Agentes)

**LIMITACIONES LLM AISLADO:**
1. Solo genera texto basado en patrón entrenado
2. No puede acceder a datos reales (sensores, manuales, BD)
3. No puede ejecutar acciones (generar orden de inspección)
4. Riesgo de alucinaciones (inventa información)
5. No tiene retroalimentación sobre calidad de respuesta

**MODELO ALTERNATIVO:**
- **Agente basado en LLM** (agentic architecture)
- LLM como "cerebro" + herramientas externas como "brazos/ojos"
- Puede: razonar, acceder a datos, ejecutar acciones, iterar

**FUNCIONAMIENTO AGENTE:**
```
LLM lee instrucción 
  → decide qué herramienta usar 
  → ejecuta herramienta 
  → obtiene resultado real 
  → actualiza razonamiento 
  → repite hasta completar tarea
```

**EVIDENCIA:**
- Identifica ≥2 limitaciones de LLM
- Propone arquitectura alternativa
- Explica cómo resuelve limitaciones

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts)
2. ✓ Tabla: LLM aislado (limitaciones) vs Agente (ventajas)
3. ✓ Pasos: definir limitación 1 → definir limitación 2 → introducir agente → explicar solución
4. ✓ Details: qué es un agente, herramientas externas, loop de razonamiento, RAG
5. ✓ Respuesta: dos limitaciones + "Agentes LLM" como solución + arquitectura
6. ✓ Errores: confundir LLM con agente, mencionar solo 1 limitación, no proponer solución

---

### P3d: Por Qué Agente > LLM Aislado + Secuencia de Acciones (0.5 pts)

**OBJETIVO:** Justificar agente en contexto de "revisar sensores, detectar anomalía, consultar manual, generar orden"

**INSTRUCCIÓN DEL CASO:**
> "Revisa las mediciones actuales del sensor de temperatura y, si detectas un valor anómalo, consulta el manual del equipo y genera una orden de inspección."

**ESTO REQUIERE:**
1. **Acceso a datos:** lectura sensor en tiempo real
2. **Razonamiento:** detectar anomalía (¿qué es "anómalo"?)
3. **Acceso a referencias:** buscar manual
4. **Generación de artefactos:** crear orden de inspección

**LLM AISLADO NO PUEDE:**
- Leer sensor en tiempo real (no tiene conexión)
- Buscar manual en BD (no tiene herramientas)
- Garantizar que la orden de inspección se genere (solo texto)

**AGENTE PUEDE:**
```
1. LLM recibe instrucción
2. Llama herramienta: obtener_temperatura_actual()
   → Retorna: 180°C (normal: 50-150°C) ✓ Anómalo
3. LLM decide: consultar manual
4. Llama herramienta: buscar_manual("sensor temperatura")
   → Retorna: "Si T>160°C, inspeccionar bomba refrigerante"
5. LLM razona: condición cumplida
6. Llama herramienta: crear_orden_inspección(motivo="T anómala", equipo="bomba")
   → Retorna: Orden creada, ticket #12345
7. LLM reporta: "Orden generada: revisar bomba refrigerante"
```

**ROLES EN LA ARQUITECTURA:**
- **LLM:** Razonador, decisor, interpretador de contexto
- **Entorno/Datos:** Temperatura actual (lectura sensor)
- **Herramientas:** API sensores, BD manual, API órdenes

**EVIDENCIA:**
- Justifica por qué agente es superior
- Describe secuencia lógica de 3+ pasos
- Identifica papel de LLM, datos, herramientas

**BLOQUES NECESARIOS:**
1. ✓ Enunciado (0.5 pts) con instrucción completa
2. ✓ Tabla/diagrama: LLM vs Agente en este contexto
3. ✓ Pasos: lectura sensor → detección anomalía → consulta manual → generación orden
4. ✓ Details: loop de razonamiento, tool-use, retroalimentación, porqué agente es flexible
5. ✓ Respuesta: justificación clara + 4-5 pasos con roles identificados
6. ✓ Errores: confundir secuencia, omitir acceso a datos, no identificar herramientas

---

## RESUMEN: ESTRUCTURA FINAL POR SUBPREGUNTA

| Subpregunta | Enunciado | ¿Qué Pasó? | Pasos | Details | Respuesta | Errores+Checklist |
|--|--|--|--|--|--|--|
| P1a | ✓ | Tabla (α,VP,FN,FP,VN) | 4 pasos | ROC def, ejes, (0,0), AUC | Tabla+Gráfico | 4 errores |
| P1b | ✓ | 2 gráficos ROC | 3 pasos | AUC, área, contexto | Modelo 2 mejor, AUC > | 3 errores |
| P1c | ✓ | Tabla TPR por α | 2 pasos | Sensibilidad, especificidad | α=2, TPR=1, FP min | 3 errores |
| P1d | ✓ | Datos α=2 | 2 pasos | Escalamiento, contexto | 320 pacientes | 2 errores |
| P2a | ✓ | Tabla RMSE | 2 pasos | Overfitting, brecha | NO, gap=73 | 3 errores |
| P2b | ✓ | Tabla RMSE, gráfico | 2 pasos | Bias-Variance trade-off | Grado 3, RMSE=30 | 3 errores |
| P2c | ✓ | Tabla valores | 3 pasos | Media=sesgo, Std=variabilidad | Contexto kWh | 3 errores |
| P3a | ✓ | Gráfico McKinsey | 2 pasos | Adopción vs Integración | Brecha 88% vs 7% | 3 errores |
| P3b | ✓ | Histograma bimodal | 3 pasos | Calibración, offset | Proveedor 1 vs 2 | 3 errores |
| P3c | ✓ | Tabla comparativa | 3 pasos | Agente, tool-use | Agentes LLM, 2 lim. | 3 errores |
| P3d | ✓ | Instrucción caso | 5 pasos | Loop razonamiento | Secuencia + roles | 3 errores |

---

## ELIMINAR DEL BORRADOR SUPERFICIAL

1. ✗ CDN Chart.js → reemplazar con Canvas 2D local
2. ✗ Details de 5 líneas → expandir a 15-20 líneas contextuales
3. ✗ Sin tabla de lecturas → agregar tablas numéricas
4. ✗ Errores genéricos → errores específicos del PDF
5. ✗ Checklists mínimos → checklists de 6-8 items
6. ✗ Gráficos en HTML triviales → gráficos Canvas 2D interactivos

---

## CRITERIOS DE ÉXITO (GUARDAR)

- [ ] Alguien sin PDF entiende cualquier subpregunta solo con el HTML
- [ ] Cada subpregunta tiene 6 bloques claramente identificados
- [ ] Offline OK: sin CDN, sin fonts remotas
- [ ] Diff muestra ampliación real P1b-d, P2, P3 (>500 líneas nuevas)
- [ ] Python verify_visuales.py pasa (si existe)
- [ ] Lesson en agent_lessons.yaml agregada

