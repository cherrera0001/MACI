# Mapa del proceso de estudio — Certamen 2, Fundamentos de Ciencia de Datos

Matriz transversal de las 11 preguntas y análisis de patrones globales. Complementa a `01_ANALISIS_RECONSTRUCCION_CERTAMEN.md`, que contiene el desarrollo completo de cada ficha.

> **Actualizado.** Este mapa incorpora la guía de estudio `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` (M0), que no estaba disponible en el primer barrido. Ver la fe de erratas y la Fase 1.5 del análisis.

---

## 1. Matriz pregunta a pregunta

### P1 — Ensambles y diversidad

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Mecanismo de mejora de un ensamble: descorrelación de errores |
| **Qué tuve que comprender** | Que promediar reduce varianza solo si las componentes no están perfectamente correlacionadas |
| **Distinción conceptual clave** | Número de modelos **≠** diversidad de modelos |
| **Evidencia en mis materiales** | `Desafio/src/08_ensemble.py`: *"si dos modelos fuertes fallan en las mismas filas, promediarlos no puede aportar"*, con cálculo de `jaccard_error` y `desacuerdo_pred` por par. `INFORME_MODELO_FCD_P3.md` §3: los tres ensambles superan al árbol simple |
| **Cómo se deriva la respuesta** | Modelos idénticos → errores idénticos → diversidad cero → el promedio devuelve el mismo valor → equivalente a un modelo, no mejor → Falso |
| **Nivel de evidencia** | **FUERTE** (reserva: el archivo es posterior al certamen) |

### P2 — Sobreajuste y generalización

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Definición operativa de sobreajuste |
| **Qué tuve que comprender** | Que el desempeño en entrenamiento no mide calidad; solo datos no vistos la miden |
| **Distinción conceptual clave** | Sobreajuste (bueno adentro, malo afuera) **≠** subajuste (malo en ambos) **≠** error alto |
| **Evidencia en mis materiales** | `JUSTIFICACION_MODELO_MACI_FCD.md`: tabla `R² Train / R² Test / Brecha / Interpretación`. `V1_Trabajo_N2` Paso 7: *"no porque el R² de entrenamiento se vea alto"*. `INFORME_MODELO_FCD_P3.md` §6: separa sobreajuste de covariate shift usando el baseline como control |
| **Cómo se deriva la respuesta** | El patrón descrito (alto en train, bajo fuera) es exactamente el síntoma de ajustar ruido → Verdadero |
| **Nivel de evidencia** | **FUERTE** |

### P3 — Causas y consecuencias del sobreajuste

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Causas, diagnóstico, consecuencias y alcance del sobreajuste |
| **Qué tuve que comprender** | Complejidad ↔ capacidad de ajustar ruido; para qué sirve la CV; costo en producción; independencia del tipo de tarea; efecto de agregar columnas |
| **Distinción conceptual clave** | **Más filas** (reduce sobreajuste) **≠ más columnas** (lo aumenta si no traen señal) |
| **Evidencia en mis materiales** | Árbol DashAI `R² train 1.000 / test 0.468`; CV 5-fold dentro de 2016 como criterio de selección; Ridge diverge en 2017 (MAE 9,8e+08); `Suburb` descartado por "311 categorías = sobreajuste"; `Bedroom2` con importancia +0,0009 |
| **Cómo se deriva la respuesta** | Cada afirmación se evalúa por su mecanismo propio; la de los atributos invierte la relación evidencia/parámetros → es la incorrecta |
| **Nivel de evidencia** | **FUERTE** |

### P4 — Métricas de clasificación

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Taxonomía: métrica de evaluación / criterio de entrenamiento / estadístico descriptivo |
| **Qué tuve que comprender** | Qué objeto describe cada cantidad y en qué momento del ciclo aparece |
| **Distinción conceptual clave** | Cantidad que describe un **clasificador** **≠** cantidad que describe una **variable** |
| **Evidencia en mis materiales** | `V1_Trabajo_N2` Paso 11: importancia por **reducción de impureza**. `V2_Trabajo_N1`: `price_stats` con `"varianza": price.var()` junto a media/mediana/IQR. `Desafio/REPORT.md` §8.3: AUC como techo de separabilidad. **Sin evidencia local de FPR** |
| **Cómo se deriva la respuesta** | Cuatro términos solo existen dentro de un problema de clasificación; la varianza existe con o sin clases → se excluye |
| **Nivel de evidencia** | **PARCIAL** |

### P5 — LLMs y agentes

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Modelo vs sistema agente; límite de conocimiento de un LLM |
| **Qué tuve que comprender** | Que el LLM es un componente del agente; que las herramientas y el bucle de acción son lo distintivo |
| **Distinción conceptual clave** | Generar texto **≠** ejecutar acciones y observar su resultado |
| **Evidencia en mis materiales** | **[NO EVIDENCIADO]** como estudio. Solo `.cursor/agents/puente-hito.md`: un agente propio con rol, herramientas y fuente de verdad anclada — evidencia de práctica, no de estudio |
| **Cómo se deriva la respuesta** | Eliminación de los tres distractores (hechos recientes, colaboración, escala de entrenamiento) |
| **Nivel de evidencia** | **INSUFICIENTE** |

### P6 — Revoluciones recientes en IA

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Atribución causal de avances tecnológicos |
| **Qué tuve que comprender** | Qué avance es producto de redes neuronales y qué avance solo las habilita |
| **Distinción conceptual clave** | **Causa** (redes neuronales → PLN, visión) **≠ condición habilitante** (nube → entrenamiento) |
| **Evidencia en mis materiales** | **[NO EVIDENCIADO]**. No hay una sola red neuronal en todo el código del repositorio |
| **Cómo se deriva la respuesta** | Preguntar de cada ítem qué lo hizo avanzar; la dirección de la flecha decide |
| **Nivel de evidencia** | **INSUFICIENTE** |

### P7 — Regresión polinomial y sobreajuste

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Diagnóstico visual de sobreajuste y remedios por mecanismo |
| **Qué tuve que comprender** | Que un polinomio de grado n−1 interpola n puntos siempre; que error de entrenamiento cero no es evidencia |
| **Distinción conceptual clave** | **Error de entrenamiento** **≠ calidad del modelo**. Y: bajar el grado (elimina términos) **≠** regularizar (los amortigua) |
| **Evidencia en mis materiales** | Los cuatro remedios anclados por separado: simplicidad (`V1_Trabajo_N2` Paso 7; GB preferible por menor brecha), CV (§1.2, §3), regularización (`Ridge`, `l2_regularization=1.0`), más datos (regiones con n < 60 marcadas no confiables, MAPE 59,3 %). **El objeto polinomial: cero apariciones en el repositorio** |
| **Cómo se deriva la respuesta** | Interpolación exacta + oscilaciones + contraste con un fenómeno que debe ser suave → sobreajuste → cuatro remedios por mecanismo |
| **Nivel de evidencia** | **PARCIAL** |

### P8 — Matriz de confusión y métricas

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Construcción de matriz de confusión y derivación de métricas |
| **Qué tuve que comprender** | Que cada métrica es un cociente y lo distintivo es el denominador |
| **Distinción conceptual clave** | Precisión (÷ predichos positivos) **≠** sensibilidad (÷ positivos reales) **≠** exactitud (÷ total). Y: **FPR ≠ 1 − precisión** |
| **Evidencia en mis materiales** | `Desafio/REPORT.md` §5: matriz 3×3 con precision/recall/F1 por clase; `gz_lib.py` y `01_repro_notebook.py` la calculan. **Aritmética verificada independientemente: las cinco cifras son exactas y la tabla cierra en filas, columnas y total.** Los conteos (12/3/4/31) **no son derivables** de ningún archivo |
| **Cómo se deriva la respuesta** | Declarar convención → contar cuatro casillas → verificar marginales → elegir denominador por métrica → interpretar en lenguaje del problema |
| **Nivel de evidencia** | **PARCIAL** (método correcto y verificado; datos de entrada no trazables) |

### P9 — Curva ROC y comparación de modelos

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Lectura de una curva ROC; comparación de clasificadores sin fijar umbral |
| **Qué tuve que comprender** | Que un modelo es una curva, no un punto; que subir el umbral baja TPR y FPR a la vez |
| **Distinción conceptual clave** | Comparar **punto de operación** **≠** comparar **modelo**. La comparación limpia es dominancia o área |
| **Evidencia en mis materiales** | `Desafio/src/05_decision_rule.py` y `REPORT.md` §10.1: el umbral como objeto de tuning y el riesgo de optimizar y reportar sobre el mismo OOF. AUC en §8.3. **Conteos y umbrales: no derivables. Cifras de AUC: contradicen la tabla del propio documento** |
| **Cómo se deriva la respuesta** | Comparar umbral a umbral → el Modelo 1 domina en los tres (mayor TPR y menor FPR) → su curva está enteramente por encima → Modelo 1 |
| **Nivel de evidencia** | **INSUFICIENTE** |

### P10 — Punto base

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | No evaluable: depende de una figura ausente |
| **Qué tuve que comprender** | — |
| **Distinción conceptual clave** | Declarar un vacío **≠** producir una respuesta plausible |
| **Evidencia en mis materiales** | La *conducta* sí tiene evidencia: `"NO VERIFICABLE CON LOS DATOS DISPONIBLES"` repetido en más de una docena de celdas del notebook de EDA; regla *"Nunca redondees de memoria"* en `.cursor/agents/puente-hito.md`; "Fe de erratas" del informe final |
| **Cómo se deriva la respuesta** | No se deriva: se declara la imposibilidad |
| **Nivel de evidencia** | No evaluable (la no-respuesta sí tiene patrón antecedente documentado) |

### P11 — Comentarios y supuestos

| Campo | Contenido |
|---|---|
| **Concepto evaluado** | Honestidad metodológica: separar lo medido de lo supuesto |
| **Qué tuve que comprender** | Que un resultado numérico sin supuesto declarado es irreproducible |
| **Distinción conceptual clave** | **Medido** / **supuesto** / **no disponible** — tres capas que deben quedar visibles al evaluador |
| **Evidencia en mis materiales** | `INFORME_MODELO_FCD_P3.md` §5 (límites de la réplica en DashAI), §6 (*"se documenta, no se oculta"*, sección "Lo que el modelo **no** hace"); `Desafio/REPORT.md` §11 (once limitaciones, incluida la no-concluyencia de la mayoría de las comparaciones); `README_POR_QUE_OBSOLETO.md` |
| **Cómo se deriva la respuesta** | Enumerar el supuesto de cada pregunta con figura y declarar que los conteos dependen de lectura visual |
| **Nivel de evidencia** | **FUERTE** |

---

## 2. Síntesis cuantitativa

| Nivel de evidencia | Preguntas | Total | (1.ª versión) |
|---|---|---|---|
| **FUERTE** | P1, P2, P3, P4, P7, P11 | 6 | 4 |
| **PARCIAL** | P5, P6, P8, P9 | 4 | 3 |
| **INSUFICIENTE** | — | 0 | 3 |
| **No evaluable** | P10 | 1 | 1 |

*Actualizado tras la incorporación de la guía de estudio (M0). El desglose y las reservas están en la Fase 5.7 del análisis.*

**Distribución por bloque temático:**

| Bloque | Preguntas | Anclaje | Evidencia local |
|---|---|---|---|
| Sobreajuste, generalización, validación, ensambles | P1, P2, P3, P7 | **Doble** | Alta. Guía §1–§4 y §8, más el núcleo del trabajo propio del semestre |
| Métricas de clasificación y evaluación | P4, P8, P9 | Doble / simple | Media-alta en método (guía §5–§7 + Desafío). Los conteos son trazables pero circulares; las cifras de AUC de la P9 siguen sin explicación |
| Panorama de IA (LLMs, agentes, redes neuronales) | P5, P6 | **Simple** | Media. Guía §9 y §10 con transferencia. Ningún otro anclaje en el repositorio |
| Conducta metodológica (supuestos, vacíos) | P10, P11 | Proyecto | Alta y anterior al certamen |

---

## 3. Patrones globales: ¿aparece realmente un ciclo de estudio en los archivos?

El enunciado propone verificar si existe este patrón:

> pregunta → interpretación inicial → identificación del concepto → explicación → contraste → corrección → justificación → respuesta

**Veredicto: el patrón NO aparece aplicado al certamen, y SÍ aparece —completo y documentado— aplicado al proyecto del curso.**

### 3.1 Dónde no aparece

No existe en el repositorio ninguna traza de ese ciclo sobre las preguntas del certamen: no hay una interpretación inicial registrada, ni un contraste, ni una corrección, ni un borrador. Solo existe el documento de respuestas finales. Afirmar que ese ciclo ocurrió sería atribuir un pensamiento no documentado, que es exactamente lo que este análisis tiene prohibido hacer.

### 3.2 Dónde sí aparece, con las siete etapas identificables

El ciclo está documentado sobre la pregunta del Proyecto 3: *"¿los datos de 2016 sirven para predecir 2017?"*

| Etapa | Evidencia en archivo |
|---|---|
| **Pregunta** | `V2_Trabajo_N1` celda 1: *"¿Qué características presentan los datos de propiedades de Melbourne y qué patrones permiten plantear una hipótesis razonable para predecir los precios de 2017 utilizando información de 2016?"* |
| **Interpretación inicial** | `_obsoleto_split_aleatorio/`: primera aproximación con split aleatorio 80/20 y conclusión "Gradient Boosting es el mejor" |
| **Identificación del concepto** | Lectura de la guía del curso: el Proyecto 3 exige partición **temporal**, no aleatoria. `INFORME_MODELO_FCD_P3.md` §1 cita textualmente la instrucción |
| **Explicación** | `V1_Trabajo_N2` Paso 5: *"Un split aleatorio mezclaría el futuro con el entrenamiento (data leakage)"* |
| **Contraste** | Reejecución completa con train = 2016 / test = 2017; comparación de la jerarquía de seis modelos con cinco semillas y bootstrap pareado con IC 95 % |
| **Corrección** | `README_POR_QUE_OBSOLETO.md`: *"contienen cifras que NO fueron calculadas… Fueron escritas a mano antes de ejecutar código"*. `INFORME_MODELO_FCD_P3.md` §0 "Fe de erratas": *"Quedan invalidados"* |
| **Justificación** | `INFORME_MODELO_FCD_P3.md` §7, cinco criterios ordenados, incluido *"elegido sin mirar el test"* |
| **Respuesta** | HistGradientBoosting sobre `log1p(Price)`, MAE 2017 = 185.449 AUD, con límites de uso declarados |

Este ciclo está **completo y es verificable**. Es el hallazgo más sólido del expediente.

### 3.3 Tres rasgos estables del método de trabajo

Aparecen de forma repetida y en archivos independientes, lo que los hace difíciles de atribuir a un episodio aislado:

**a) Anclaje obligatorio de cifras.**
`.cursor/agents/puente-hito.md`: *"Si un número no está ahí ni en la salida ejecutada del notebook, recálculalo o márcalo como pendiente. Nunca redondees de memoria."* Existe un archivo dedicado, `anclaje.json`, como fuente de verdad, con hash SHA-256 del dataset.

**b) Declaración sistemática de lo no verificable.**
La cadena `"NO VERIFICABLE CON LOS DATOS DISPONIBLES"` aparece como rama `else` en más de una docena de celdas del notebook de EDA. La misma conducta reaparece en la pregunta 10 del certamen.

**c) Autoinvalidación por escrito.**
El repositorio conserva deliberadamente una carpeta `_obsoleto_split_aleatorio/` con un README que explica por qué su contenido está mal y cuál es su reemplazo. No se borró el error: se dejó documentado. El informe final abre con una fe de erratas antes de presentar cualquier resultado.

### 3.4 El patrón que sí conecta el proyecto con el certamen

Lo que puede sostenerse no es que el ciclo de estudio se repitiera sobre las preguntas del certamen, sino algo más acotado y más verificable:

> El rasgo (b) —declarar el vacío en vez de rellenarlo— **cruza** del proyecto al certamen. Las preguntas 10 y 11 del certamen son la aplicación literal de una regla que el autor ya tenía escrita e implementada en su código antes de rendir.

Es una sola transferencia, pero es la única cuyo origen es **anterior** al certamen, está documentada en múltiples archivos y no requiere inferencia: la conducta es la misma, la formulación es la misma, el propósito es el mismo.

---

## 4. Lo que este mapa no puede afirmar

Para que el documento sea útil tiene que ser preciso también en sus límites:

1. **No hay material de preparación del certamen.** Ninguno. Lo que se reconstruye es dominio conceptual adquirido en trabajo de proyecto, no un proceso de estudio del certamen.
2. **La mayor parte de la evidencia conceptual es posterior al 28 de agosto de 2026.** La estrictamente anterior se reduce a los notebooks del Hito 1, que sostienen P2, P3 y parte de P4 y P7.
3. **Las preguntas 5 y 6 no tienen ningún antecedente local.**
4. **Las cifras de AUC de la pregunta 9 contradicen la tabla del propio documento** (0,78 / 0,68 declarados frente a ≈ 0,894 / ≈ 0,785 calculados por trapecios sobre sus propios puntos). Es la señal más clara de contenido incorporado sin verificación.
5. **Ninguna de estas observaciones determina si hubo o no una infracción académica.** Miden una sola cosa: cuánto de cada respuesta puede reconstruirse desde los archivos de este directorio.
