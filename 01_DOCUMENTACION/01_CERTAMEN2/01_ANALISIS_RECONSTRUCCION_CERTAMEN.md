# Reconstrucción del proceso de estudio — Certamen 2, Fundamentos de Ciencia de Datos (T2-2026)

**Pregunta que este documento intenta responder:**
¿Puede reconstruirse, a partir del material local de `F:\MACI`, un proceso de comprensión que explique cómo se resolvieron las preguntas del Certamen 2?

**Respuesta global: PARCIALMENTE, con base más amplia de lo que este informe sostuvo en su primera versión.** El detalle, pregunta por pregunta, está en la Fase 2; los límites y contradicciones, en la Fase 5. Este documento no intenta demostrar ausencia de uso de IA ni ausencia de copia. No se modificó ningún archivo original.

---

## Fe de erratas (léase primero)

La primera versión de este informe (15-09-2026) afirmó, en su Fase 1.1 y en su Fase 5.2:

> *"En todo `F:\MACI` no existe ningún otro archivo que mencione la palabra 'certamen'. No hay guía de estudio del certamen… Nada en `F:\MACI` fue producido para preparar este certamen."*

**Esa afirmación era falsa.** Existe `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx`, una guía de estudio activa de 246 párrafos que cubre los diez conceptos evaluados. No apareció en el primer barrido porque no estaba en el directorio en ese momento.

Se corrigen en consecuencia: la Fase 1.1, la Fase 1.2 (nueva entrada M0), la nueva Fase 1.5, las fichas de las preguntas 4 a 9, la Fase 5.2 y la clasificación de la Fase 5.7. **La conclusión global sigue siendo "parcialmente", pero por razones distintas y con tres preguntas menos en el nivel más bajo.**

Se deja constancia del error en vez de reescribir el informe en silencio. Es la misma práctica que el propio expediente valora en `README_POR_QUE_OBSOLETO.md` y en el §0 del informe del Proyecto 3; aplicarla aquí y no allá sería incoherente.

---

## FASE 1 — Material identificado

Barrido completo de `F:\MACI` (`.docx`, `.md`, `.txt`, `.py`, `.ipynb`, `.json`, `.pdf`, `.pptx`, `.html`).

### 1.1 Archivo que contiene las preguntas y las respuestas

Ambos en `01_DOCUMENTACION\01_CERTAMEN2\fuentes\`.

| Archivo | Contenido |
|---|---|
| `Certamen2_Respuestas_Finales (Recuperado automáticamente).docx` | **El certamen resuelto.** 11 preguntas con enunciado resumido + respuesta + justificación. 1.293 palabras. |
| `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` | **Guía de estudio activa.** 246 párrafos. Diez secciones, una por concepto evaluado, con estructura pedagógica fija. Analizada en la Fase 1.5 |

**Lo que sigue faltando:** no hay borradores de respuestas, ni apuntes de clase, ni bancos de preguntas, ni transcripciones de conversación. La cadena documental del certamen tiene dos eslabones —guía y respuestas— y no los pasos intermedios entre uno y otro.

**Advertencia de dirección, decisiva para interpretar la guía.** La propia guía declara en su primer párrafo:

> *"Esta guía toma las preguntas del Certamen 2 como puntos de partida para aprender."*

Es decir: **la guía se construyó a partir del certamen**, no al revés. Eso significa que evidencia un proceso de comprensión sobre el contenido evaluado, pero **no establece qué se comprendía el 28 de agosto al rendir**. Sus metadatos no ayudan a fecharla: `created` marca 2013-12-23 (valor de plantilla), sin autor y sin fecha de modificación. Esta distinción se mantiene en todo el resto del informe y no debe borrarse al citarlo.

### 1.2 Material que sí constituye trabajo conceptual propio

| # | Archivo | Tipo | Qué aporta conceptualmente |
|---|---|---|---|
| **M0** | `01_DOCUMENTACION\01_CERTAMEN2\fuentes\Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` | **Guía de estudio activa** | Los diez conceptos del certamen, cada uno con analogía cotidiana, traducción técnica, tres ejemplos, preguntas de reflexión, ejercicio de transferencia y conclusión. Ver Fase 1.5 |
| M1 | `08_PROYECTO_FCD/Hito1/Corrección/.../V2_Trabajo_N1_FUNDAMENTOS_(C_ABRIGO_C_HERRERA_K_URBINA).ipynb` | Notebook EDA (Hito 1, Trabajo 1) | Calidad de datos, faltantes, duplicados, rangos inválidos, distribución sesgada, varianza como estadístico descriptivo, comparación 2016 vs 2017 |
| M2 | `.../2° Trabajo _FUNDAMENTOS/V1_Trabajo_N2_FUNDAMENTOS_(...).ipynb` y su `.py` | Notebook de modelamiento (Hito 1, Trabajo 2) | Partición temporal, *leakage*, pipeline, jerarquía baseline→lineal→árbol→RF→GB, CV K=5, brecha train/test, GridSearchCV, importancia por **reducción de impureza** |
| M3 | `_obsoleto_split_aleatorio/JUSTIFICACION_MODELO_MACI_FCD.md` | Informe de justificación (versión temprana, luego invalidada) | Tabla explícita **R² train vs R² test vs brecha → "sobreajuste"**; criterio "menor brecha = mejor generalización"; "Suburb con 311 categorías = sobreajuste" |
| M4 | `_obsoleto_split_aleatorio/README_POR_QUE_OBSOLETO.md` | Autocorrección | Declara que sus propias cifras anteriores **no fueron calculadas** y las invalida |
| M5 | `INFORME_MODELO_FCD_P3.md` | Informe final generado desde código (04-09-2026) | Ensambles vs árbol simple, selección por CV sin mirar el test, divergencia de Ridge, `l2_regularization`, bootstrap pareado con IC 95 %, brecha train/test documentada |
| M6 | `Fundamentos de ciencia de datos/Desafio/` (`REPORT.md`, `src/01..09`) | Desafío de **clasificación** Galaxy Zoo (12-09-2026) | Matriz de confusión, precision/recall/F1, AUC 0-vs-resto, OOF, umbrales de decisión, y **diversidad de errores entre modelos de un ensamble** |
| M7 | `.cursor/agents/puente-hito.md`, `.cursor/rules/maci-coherencia-hitos.mdc` | Reglas de trabajo propias | Regla explícita de "no inventar cifras"; fuente de verdad `anclaje.json` |
| M8 | `PITCH_HITO2_REVISION.md`, `Pitch_Hito2_v2.pptx/pdf` | Presentación Hito 2 | Cierre narrativo del proyecto |

### 1.3 Clasificación pedida en Fase 1

1. **Preguntas originales:** solo la versión *resumida* dentro del `.docx`. Los enunciados completos y las figuras de las preguntas 7, 8, 9 y 10 **no están en el directorio**.
2. **Respuestas:** el mismo `.docx`.
3. **Material de estudio:** M1, M2, M3, M5, M6 — todos de proyecto, ninguno preparado para el certamen.
4. **Explicaciones y razonamientos:** M2 (celdas markdown "¿Qué? / ¿Por qué?"), M5 (§3 "Lecturas", §7 "Decisión y justificación"), M6 (§3.1, §8, §11).
5. **Correcciones y reformulaciones:** M4 (invalida M3), `INFORME_MODELO_FCD_P3.md` §0 "Fe de erratas", `_obsoleto_split_aleatorio/` como carpeta-cementerio deliberada.

### 1.4 Advertencia metodológica sobre falsos positivos

Una búsqueda ingenua por palabras clave produce coincidencias engañosas que **descarté**:

- "agente" en `guia_fcd_texto.txt` → *"Agente de bienes raíces"* (columna `SellerG`). **No** es evidencia sobre agentes de IA.
- "pureza" en `guia_fcd_texto.txt` → *"% de Silica (impureza)"*. **No** es evidencia sobre ganancia de pureza.
- "diversidad" en el notebook de EDA → *"gran diversidad de precios"*. **No** es evidencia sobre diversidad de ensambles.

La única evidencia real sobre esos tres conceptos está en otros archivos, y se cita como tal más abajo.

---

### 1.5 Análisis de la guía de estudio (M0)

#### Estructura

La guía no es un resumen de respuestas. Cada una de sus diez secciones repite la misma secuencia de seis pasos:

1. **Pregunta que queremos ser capaces de responder** — el problema, no la respuesta.
2. **Primero: una historia común** — analogía cotidiana (tres médicos, un guardia, cinco chinches en una tabla, un detector de humo, un auto eléctrico y la carretera).
3. **Ahora traduzcamos la historia a Ciencia de Datos** — formulación técnica.
4. **Ejemplos para pensar** — tres casos de dominios distintos.
5. **Detente y razona** — tres preguntas abiertas sin respuesta dada.
6. **Cámbiame el ejemplo** — ejercicio de transferencia a un contexto nuevo.
7. **Lo que deberías poder concluir** — el cierre.

Cierra con un **mapa de conexión** entre los diez conceptos, una **autoevaluación de cuatro criterios** y una **mini interrogación integradora** de siete preguntas.

#### Qué tipo de material es

El diseño es de **aprendizaje activo**, y lo declara explícitamente en su encabezado y en su regla de uso:

> *"Comprender con ejemplos, historias, gráficos y ejercicios — no memorizar respuestas."*
> *"Regla práctica: antes de leer la solución de un ejemplo, intenta explicarlo en voz alta. Si puedes explicar el porqué sin repetir una frase de memoria, estás procesando el concepto."*

Y su criterio de cierre exige cuatro capacidades, no el recuerdo de una frase:

> *"Marca un concepto como comprendido solo si puedes hacer las cuatro cosas: explicarlo sin usar la definición textual de esta guía; inventar un ejemplo cotidiano distinto; resolver un ejemplo con números o datos nuevos; explicar qué error cometería alguien que confundiera el concepto."*

Ese es exactamente el criterio que una defensa oral aplica. El material está construido para sobrevivir a una repregunta, que es lo contrario de un machote de respuestas.

#### Cobertura: guía → certamen

| Sección de la guía | Pregunta | Cobertura |
|---|---|---|
| 1. Ensambles: ¿por qué varios modelos pueden ser mejores? | **P1** | Completa. Tres termómetros descalibrados +2 °C; crédito bancario; Galaxy Zoo |
| 2. Sobreajuste y generalización | **P2** | Completa. Memorizar 100 preguntas; R² train 0,95 / test 0,60 |
| 3. Complejidad, variables y sobreajuste | **P3** | Completa. Identificador único de casa; número de fila del correo; código interno de paciente |
| 4. Validación cruzada: probar sin gastar el examen final | **P3** | Completa. K-fold; el ejemplo de Melbourne; la analogía del jurado |
| 5. Métricas de clasificación | **P4** | Completa, incluida FPR y la exclusión explícita de la varianza |
| 6. Matriz de confusión: convertir una figura en números | **P8** | Completa, **con los conteos exactos del certamen** |
| 7. ROC y AUC: el efecto de mover el umbral | **P9** | Parcial: cubre umbral, intercambio y dominancia. **No contiene las cifras de AUC** |
| 8. Regresión polinomial | **P7** | Completa. Cinco chinches y una cinta flexible |
| 9. LLM y agente: modelo versus sistema | **P5** | Completa. Asesor con teléfono, calendario y permisos |
| 10. Redes neuronales: causa versus infraestructura | **P6** | Completa. El auto eléctrico y la carretera |

Diez de las once preguntas tienen sección propia. La P10 no (dependía de una figura) y la P11 no es de contenido.

#### Los dos hallazgos que esta guía obliga a registrar

**a) La guía es la fuente de los conteos de la Pregunta 8.** Su sección 6 contiene:

> *"Ejemplo 1 — Conteo 12/3/4/31. VP=12, FN=3, FP=4, VN=31. Total=50. Accuracy=(12+31)/50=86%. Precision=12/(12+4)=75%. Recall=12/(12+3)=80%. FPR=4/(4+31)=11,4%."*

Son los mismos cuatro conteos y las mismas cuatro métricas de la respuesta del certamen. Eso hace **trazable** una cifra que la primera versión de este informe marcó como [NO EVIDENCIADO]. Pero la trazabilidad es **circular a efectos probatorios**: si la guía se construyó a partir del certamen, entonces el conteo pasó del certamen a la guía, no de la guía al certamen. Lo que sí queda establecido es que el procedimiento está comprendido y es reproducible con otros números — la propia guía lo ejercita: *"Construye mentalmente una matriz para 20 casos: 5 positivos reales; detectas 4; además acusas erróneamente a 3 negativos."*

**b) La guía NO explica las cifras de AUC de la Pregunta 9, y enseña el método correcto.** Su sección 7 no menciona 0,78 ni 0,68 en ninguna parte. Lo que enseña es precisamente el argumento de dominancia:

> *"Ejemplo 3 — Dos modelos. Si en varios umbrales A logra más TPR y menos FPR que B, A domina en esos puntos."*

Es decir: el material de estudio contiene el razonamiento correcto —el mismo que la Fase 5.3 verifica independientemente— y **no** contiene las dos cifras que resultan inconsistentes. La contradicción de la P9 no solo sobrevive a la aparición de la guía: queda más aislada, porque ahora se sabe que esos números no vienen ni de la tabla del certamen ni del material de estudio.

#### Un detalle que conviene no omitir

La **mini interrogación integradora** final tiene siete preguntas, cada una seguida de un campo `Respuesta propia: ____`. **Los siete campos están en blanco.** El ejercicio de recuperación activa que la propia guía propone como prueba de comprensión no fue completado en este archivo. Puede haberse hecho en otro soporte; en este documento no hay traza de ello.

---

## FASE 2 — Reconstrucción pregunta por pregunta

Convención de etiquetas:
**[EVIDENCIA]** = está explícitamente en un archivo, con cita. **[INFERENCIA]** = se deriva razonablemente del contenido. **[NO EVIDENCIADO]** = no puede sostenerse con el material.

---

### Pregunta 1 — Ensambles y diversidad

**PREGUNTA ORIGINAL:** V/F. *"Utilizar un modelo compuesto por varios modelos exactamente iguales y que predicen exactamente lo mismo suele predecir mejor que cada modelo por separado."*

**RESPUESTA ENTREGADA:** Falso. Un ensamble mejora cuando sus modelos aportan predicciones diferentes y sus errores no coinciden por completo; si son idénticos no se reduce la varianza.

**1. ¿Qué evalúa?** El mecanismo por el cual un ensamble funciona: **descorrelación de errores**, no acumulación de modelos. Es una pregunta sobre la *causa* de la mejora, no sobre la definición de ensamble.

**2. ¿Qué había que entender?**
- Que promediar reduce varianza solo si las componentes promediadas no están perfectamente correlacionadas.
- Que "más modelos" no es una cantidad que mejore por sí misma.
- Que el error de un ensamble depende del error individual **y** del grado de acuerdo entre modelos.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA]** — `Fundamentos de ciencia de datos/Desafio/src/08_ensemble.py`, docstring de cabecera:
> *"Primero mide DIVERSIDAD de errores entre modelos (si dos modelos fuertes fallan en las mismas filas, promediarlos no puede aportar)."*

Esta frase es, literalmente, el contenido de la Pregunta 1 en su forma general. El script además la **operacionaliza**: calcula `ambos_fallan`, `alguno_falla`, `jaccard_error` y `desacuerdo_pred` para cada par de modelos, y selecciona el par candidato ordenando por `jaccard_error` ascendente (menor solapamiento de errores = mayor diversidad).

**[EVIDENCIA]** — `INFORME_MODELO_FCD_P3.md` §3: los tres ensambles (RF, GB, HGB) superan claramente al árbol simple (MAE 245.393 → 185.449), con jerarquía documentada.

**[INFERENCIA]** — De M2 y M5 se deriva que el autor distingue "ensamble" de "modelo mejor": en `INFORME_MODELO_FCD_P3.md` Random Forest es a la vez ensamble **y** el modelo con mayor brecha train/test, lo que impide la lectura simplista "ensamble = siempre mejor".

**[LÍMITE]** `08_ensemble.py` es posterior al certamen (ver Fase 5.1). Lo que sostiene es que el concepto está comprendido y operacionalizado por el autor, no que lo estuviera el 28 de agosto.

**4. Deconstrucción del razonamiento**

1. La afirmación propone: N copias idénticas > 1 copia.
2. Primer paso: preguntar *por qué* un ensamble mejora. No mejora por ser "varios": mejora por promediar.
3. Segundo paso: ¿qué hace el promedio? Reduce varianza. Pero la varianza del promedio de N variables idénticas es la varianza de una sola — no baja nada, porque la correlación entre ellas es 1.
4. Tercer paso: si los N modelos son exactamente iguales, sus errores coinciden fila por fila. El conjunto `ambos_fallan` es igual al conjunto `alguno_falla`; el `jaccard_error` vale 1; la diversidad es cero.
5. Por tanto el ensamble degenera: su predicción es idéntica a la de un miembro. No es peor, es **equivalente** — y la afirmación decía "suele predecir mejor".
6. Respuesta: Falso.

**5. Punto de confusión**
La trampa es la palabra **"varios"**. La intuición de curso ("los ensambles predicen mejor") es correcta como regla general y empuja a marcar Verdadero. Lo que cambia la respuesta es el calificativo **"exactamente iguales y que predicen exactamente lo mismo"**: ese calificativo anula precisamente la condición que hace útil al ensamble. Quien responda sobre el enunciado general sin leer la condición particular, falla.

**6. Contrafactual**
*Si se interpretara "ensamble" como "cantidad de modelos" en lugar de "combinación de modelos con errores distintos", se respondería Verdadero. Esa interpretación falla porque el promedio de N señales perfectamente correlacionadas tiene exactamente la misma varianza que una sola: no hay información nueva que agregar, y el resultado es numéricamente idéntico al de un modelo individual.*

**7. Respuesta razonada (reconstruida)**
Falso. Un ensamble aporta cuando sus miembros se equivocan en filas distintas: ahí el promedio cancela parte del error. Si todos los modelos son idénticos, se equivocan en las mismas filas, el promedio devuelve el mismo número y no se gana nada. Lo que se necesita es **diversidad**, y por eso los ensambles reales la fuerzan: bagging cambia las muestras, Random Forest además cambia las variables candidatas en cada corte, boosting entrena cada modelo sobre los errores del anterior.

**8. Prueba de comprensión**
- *P: ¿Cómo mediría si dos modelos son suficientemente diversos para combinarlos?* → R: Comparo dónde fallan. Calculo la fracción de filas en que fallan ambos sobre la fracción en que falla alguno (un Jaccard de errores); si se acerca a 1, combinarlos no aporta. También mido el desacuerdo de predicciones.
- *P: ¿Entonces siempre conviene maximizar la diversidad?* → R: No. Hay un compromiso: puedo obtener diversidad altísima agregando modelos malos, y eso empeora el ensamble. Se necesita diversidad **entre modelos que individualmente sean fuertes**.

---

### Pregunta 2 — Sobreajuste y generalización

**PREGUNTA ORIGINAL:** V/F. *"El sobreajuste ocurre cuando el modelo predice correctamente sobre el conjunto de entrenamiento, pero no es capaz de generalizar para datos que no ha visto antes."*

**RESPUESTA ENTREGADA:** Verdadero. El modelo aprende particularidades y ruido del entrenamiento; alto desempeño en train, bajo en validación o test.

**1. ¿Qué evalúa?** La definición operativa de sobreajuste y, con ella, la distinción entre **ajustar** y **generalizar**.

**2. ¿Qué había que entender?**
- Que el desempeño en entrenamiento no es una medida de calidad del modelo.
- Que la única evidencia de generalización proviene de datos no usados para ajustar.
- Que el sobreajuste es un **síntoma comparativo** (brecha), no un valor absoluto.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA]** — `_obsoleto_split_aleatorio/JUSTIFICACION_MODELO_MACI_FCD.md`, sección "Análisis de Overfitting": tabla con columnas `R² Train | R² Test | Brecha | Interpretación`, y las interpretaciones escritas a mano: `-0.0030 → No sobreajuste`, `+0.0180 → Ligero sobreajuste`, `+0.0110 → Menor sobreajuste`. El concepto está usado como **instrumento de decisión**, no como definición recitada.

**[EVIDENCIA]** — `V1_Trabajo_N2...ipynb`, celda markdown "Paso 7":
> *"La complejidad solo se justifica si mejora el test 2017 de forma material, **no porque el R² de entrenamiento se vea alto**."*

**[EVIDENCIA]** — `INFORME_MODELO_FCD_P3.md` §6:
> *"Brecha R² train-test = +0.176. Parte es sobreajuste y parte es el shift 2016→2017 (el baseline también empeora); se documenta, no se oculta."*

Esta última frase es la más valiosa del expediente para esta pregunta: distingue dos causas de caída de desempeño (sobreajuste vs. cambio de distribución) y usa el baseline como control para separarlas. Está por encima del nivel que la pregunta exige.

**4. Deconstrucción del razonamiento**

1. La afirmación describe un patrón: alto en train, bajo fuera de train.
2. ¿Es ese *el* sobreajuste, o solo una consecuencia? Hay que comprobar que la afirmación no esté confundiendo el fenómeno con otro que produce el mismo patrón.
3. Candidato a confusión: un modelo puede caer fuera de muestra por *covariate shift* sin haber sobreajustado. Pero la afirmación no dice "toda caída es sobreajuste"; dice que el sobreajuste **ocurre cuando** se da ese patrón. Esa dirección sí es correcta.
4. Mecanismo: con capacidad suficiente, el modelo ajusta ruido —variación no reproducible— y el ruido no se repite en datos nuevos.
5. Por tanto la afirmación describe correctamente el fenómeno. Respuesta: Verdadero.

**5. Punto de confusión**
Confundir **error alto** con **sobreajuste**. Un modelo que anda mal en train y peor en test está *subajustado*, no sobreajustado. El sobreajuste exige la combinación: bueno adentro, malo afuera. La segunda confusión, más fina, es atribuir toda la brecha a sobreajuste cuando parte puede ser cambio de distribución.

**6. Contrafactual**
*Si se interpretara "predice correctamente en entrenamiento" como condición suficiente de mal modelo, se podría responder Falso alegando que "un buen modelo también predice bien en entrenamiento". Esa interpretación falla porque el enunciado no afirma que buen desempeño en train sea malo: afirma la conjunción con la incapacidad de generalizar, y esa conjunción es exactamente la definición.*

**7. Respuesta razonada (reconstruida)**
Verdadero. Sobreajustar es memorizar en vez de aprender: el modelo captura detalles del conjunto con que se entrenó —incluido el ruido— que no se repiten afuera. Se detecta comparando dos números, no mirando uno: desempeño en entrenamiento contra desempeño en datos no vistos. En mi propio proyecto la brecha de R² del Random Forest fue +0,231 y la del árbol simple +0,145, y eso fue un argumento en contra del RF pese a que su R² de entrenamiento era 0,946.

**8. Prueba de comprensión**
- *P: Si un modelo tiene R² 0,95 en train y 0,93 en test, ¿sobreajusta?* → R: No hay evidencia de sobreajuste relevante: la brecha es pequeña. Sobreajuste no es "R² alto", es "R² alto adentro y bajo afuera".
- *P: ¿Toda caída entre train y test es sobreajuste?* → R: No. Si la distribución cambió entre los dos conjuntos, el modelo puede caer sin haber memorizado. Para separarlo miro si un baseline trivial también empeora: si empeora, parte de la caída es del problema, no del modelo.

---

### Pregunta 3 — Causas y consecuencias del sobreajuste

**PREGUNTA ORIGINAL:** Selección múltiple sobre afirmaciones de sobreajuste. Respuesta entregada: correctas 2, 3, 4 y 5; incorrecta la 1 (aumentar el número de atributos evitaría el sobreajuste).

**RESPUESTA ENTREGADA (contenido):** más complejidad → más riesgo de sobreajuste; la validación cruzada permite detectar la brecha; el sobreajuste causa fallas en producción; ocurre en clasificación y regresión; agregar atributos no lo evita por sí solo.

**1. ¿Qué evalúa?** Cuatro afirmaciones independientes que solo se resuelven bien si se maneja el sobreajuste como *fenómeno con causas, diagnóstico, consecuencias y alcance*, no como una definición.

**2. ¿Qué había que entender?**
- Complejidad ↔ capacidad de ajustar ruido.
- Para qué sirve realmente la validación cruzada (estimar desempeño fuera de muestra, no "mejorar el modelo").
- Que el costo del sobreajuste se paga en despliegue.
- Que el fenómeno es del **aprendizaje**, no del tipo de tarea.
- Que más variables aumentan la dimensión del espacio de hipótesis: si no traen señal, solo traen riesgo.

**3. ¿Dónde está ese conocimiento en el material?** Esta es la pregunta con la evidencia local más densa.

| Afirmación | Evidencia |
|---|---|
| Más complejidad → más sobreajuste | **[EVIDENCIA]** `INFORME_MODELO_FCD_P3.md` §5, réplica DashAI: `DecisionTreeRegression` con `R² train = 1.000` y `R² test = 0.468`. Un árbol sin poda memoriza el train por completo. También §3: RF R² train 0,946 vs test 0,715 |
| La CV detecta la brecha / evalúa generalización | **[EVIDENCIA]** `V1_Trabajo_N2...ipynb` Paso 8: *"Validación cruzada K=5 dentro de 2016… La CV no sustituye al test temporal."* Y `INFORME_MODELO_FCD_P3.md` §1.2: *"Selección de modelo sin mirar 2017: validación cruzada 5-fold dentro de 2016; el ranking de CV decide, no el test."* |
| Problemas en producción | **[EVIDENCIA]** `INFORME_MODELO_FCD_P3.md` §2 y §3: 29,1 % de las filas de 2017 caen en suburbios inexistentes en 2016; el modelo Ridge **diverge** (MAE 9,79e+08) ante combinaciones no vistas. Es un caso real de "funcionó con históricos, falla con datos nuevos" |
| Ocurre en clasificación y en regresión | **[EVIDENCIA]** regresión en M5; clasificación en `Desafio/REPORT.md` §10.1: *"Cualquier cifra obtenida tuneando y reportando sobre el mismo OOF está inflada"* — sobreajuste a la regla de decisión en un problema de clasificación multiclase |
| Más atributos no evita sobreajuste | **[EVIDENCIA]** `JUSTIFICACION_MODELO_MACI_FCD.md`: *"NO usar 'Suburb' (311 categorías = sobreajuste); SÍ usar 'Regionname' (8 categorías = generalizable)"*. Y `INFORME_MODELO_FCD_P3.md` §6: `Bedroom2` tiene importancia por permutación +0,0009 — *"no aporta nada más allá de Rooms"* |

**4. Deconstrucción del razonamiento**
Cada afirmación se evalúa por separado; no hay un razonamiento único.

- *Complejidad:* un modelo con más capacidad puede representar más funciones, incluidas las que pasan por el ruido. Es una afirmación sobre el espacio de hipótesis, y es correcta como tendencia.
- *Validación cruzada:* el paso no obvio es que la CV **no arregla** el sobreajuste, lo **estima**. Sirve porque cada fold evalúa sobre datos que ese modelo no vio. Por eso la afirmación dice "permite detectar", que es la formulación correcta.
- *Producción:* el punto decisivo es que los datos de producción no son una muestra del conjunto histórico. Un modelo que memorizó el histórico no tiene por qué sobrevivir al cambio.
- *Clasificación y regresión:* el sobreajuste proviene de ajustar parámetros con datos finitos. Nada en ese mecanismo depende de si la salida es categoría o número.
- *Atributos:* aquí está la única afirmación falsa, y es la más tentadora. Agregar variables amplía el espacio de búsqueda. Si la variable no correlaciona con la señal, el modelo tiene una vía más para ajustar ruido. La afirmación invierte la relación real.

**5. Punto de confusión**
La afirmación 1 explota la intuición "más datos ayudan". Hay que distinguir **más filas** de **más columnas**. Más observaciones sí reducen el sobreajuste (más evidencia por parámetro). Más atributos hacen lo contrario: aumentan parámetros sin aumentar evidencia. Confundir estas dos direcciones del "más datos" es el error que la pregunta busca.

**6. Contrafactual**
*Si se interpretara "aumentar el número de atributos" como "enriquecer el conjunto de datos", se marcaría la afirmación 1 como correcta. Esa interpretación falla porque enriquecer en la dimensión de las filas y en la de las columnas tienen efectos opuestos sobre la razón evidencia/parámetros: n crece frente a p en el primer caso, p crece frente a n en el segundo.*

**7. Respuesta razonada (reconstruida)**
Son correctas las cuatro afirmaciones sobre complejidad, validación cruzada, producción y alcance en ambos tipos de tarea. La afirmación sobre agregar atributos es falsa: en mi proyecto descarté `Suburb` justamente porque sus 311 categorías daban al modelo 311 maneras de memorizar barrios en vez de aprender ubicación, y `Bedroom2` quedó con importancia prácticamente nula, o sea que solo agregaba dimensión sin aportar señal.

**8. Prueba de comprensión**
- *P: ¿Por qué la validación cruzada detecta sobreajuste si al final el modelo igual se entrena con todos los datos?* → R: Porque en cada fold el modelo se evalúa sobre el trozo que no usó para entrenar. Ese número es una estimación de desempeño fuera de muestra; si está muy por debajo del desempeño en entrenamiento, hay sobreajuste.
- *P: Deme un caso donde agregar una variable sí reduzca el sobreajuste.* → R: Si la variable explica parte de la varianza que el modelo estaba capturando con combinaciones ruidosas de otras, puede simplificar el ajuste. Pero eso ocurre porque la variable trae señal, no porque sea una variable más.

---

### Pregunta 4 — Métricas de clasificación

**PREGUNTA ORIGINAL:** Indicar cuáles se usan en clasificación: AUC, varianza, ganancia de pureza, FPR, exactitud.

**RESPUESTA ENTREGADA:** AUC, ganancia de pureza, FPR y exactitud. La varianza no es una métrica de rendimiento de clasificación.

**1. ¿Qué evalúa?** Discriminar entre **métrica de rendimiento de un clasificador**, **criterio interno de entrenamiento** y **estadístico descriptivo**. La pregunta mezcla deliberadamente las tres categorías.

**2. ¿Qué había que entender?**
- Qué mide cada cantidad y en qué momento del ciclo aparece.
- Que "ganancia de pureza" es un criterio de **construcción** de árboles (elegir el corte), no de evaluación del modelo terminado — y que aun así pertenece al dominio de la clasificación.
- Que la varianza es un estadístico de dispersión de una variable, presente en todo el análisis de datos pero no como medida de acierto.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA] — ganancia de pureza:** `V1_Trabajo_N2...ipynb`, Paso 11:
> *"Top 10 del Random Forest por **reducción de impureza**. Para el oral: qué usa el modelo. No es un efecto causal ni se usa para reelegir variables mirando 2017."*

El autor usa el criterio de impureza y además marca su alcance correcto (interpretación, no causalidad, no selección post-hoc).

**[EVIDENCIA] — AUC:** `Desafio/REPORT.md` §8.3:
> *"Techo de AUC marginal univariada: 0.754 para 0-vs-resto, frente a 0.9041 para 1-vs-2."*

Uso no trivial: AUC como cota de separabilidad calculada **sin clasificador**, solo con los datos. Eso solo se hace entendiendo que el AUC mide capacidad de ordenamiento, no acierto a un umbral.

**[EVIDENCIA] — exactitud, precision, recall, F1:** `Desafio/src/gz_lib.py`, `01_repro_notebook.py` y `03_model_comparison.py` calculan `f1_score`, precision, recall y matriz de confusión; `REPORT.md` reporta la tabla por clase.

**[EVIDENCIA] — varianza como estadístico, no como métrica:** `V2_Trabajo_N1...ipynb`, celda de precios: `price_stats` incluye `"varianza": price.var()` **junto a** media, mediana, Q1, Q3, IQR — es decir, la varianza aparece en el material exactamente en el rol que la respuesta del certamen le asigna: descripción de una distribución.

**[EVIDENCIA] — FPR y la taxonomía completa (guía de estudio, sección 5):**
> *"Accuracy pregunta por el total. Precision mira las predicciones positivas. Recall/Sensibilidad mira los positivos reales. FPR mira los negativos reales. AUC evalúa el ordenamiento a través de umbrales. Varianza, en cambio, es un estadístico general y no una métrica de rendimiento de clasificación."*

La guía resuelve la pregunta completa, incluida la exclusión de la varianza, y la ejercita con un caso numérico distinto: *"Imagina 100 correos: 10 spam y 90 legítimos. Un sistema identifica 8 spam pero también marca 12 legítimos como spam. ¿Qué preguntas responderían recall, precision y FPR?"* También plantea la distinción exacta que la pregunta evalúa: *"¿Varianza describe el clasificador o puede existir sin clasificación?"*

**4. Deconstrucción del razonamiento**

1. Clasificar cada término por *qué objeto describe*: AUC describe un clasificador; FPR describe un clasificador a un umbral; exactitud describe un clasificador; ganancia de pureza describe un **corte candidato** dentro de un árbol; varianza describe una **variable**.
2. La pregunta pide "las que se utilizan en clasificación". Cuatro de los cinco términos solo tienen sentido dentro de un problema de clasificación.
3. La varianza es el único que existe con total independencia de que haya clases: se calcula sobre el precio de una casa igual que sobre cualquier otra cosa.
4. Punto fino: la ganancia de pureza no evalúa el modelo terminado, pero sí es específica de clasificación (mide cuán homogéneas quedan las clases tras un corte). Por eso entra.
5. Respuesta: AUC, ganancia de pureza, FPR y exactitud.

**5. Punto de confusión**
Dos trampas superpuestas. La primera: la varianza *aparece* constantemente en ciencia de datos —incluida la descomposición sesgo–varianza, que sí es de modelos—, lo que invita a incluirla. Hay que distinguir "concepto que se usa al analizar modelos" de "métrica que mide el rendimiento de un clasificador". La segunda: la ganancia de pureza podría descartarse por no ser una métrica de evaluación, y sería un descarte por la razón equivocada, porque el enunciado dice "se utilizan en clasificación", no "evalúan el desempeño final".

**6. Contrafactual**
*Si se interpretara la lista como "métricas de evaluación del modelo terminado", se dejaría fuera la ganancia de pureza y se respondería solo AUC, FPR y exactitud. Esa interpretación falla porque el enunciado pregunta por uso en clasificación, no por uso en la fase de evaluación; la ganancia de pureza es un criterio propio de clasificadores basados en árboles y por tanto pertenece al dominio.*

**7. Respuesta razonada (reconstruida)**
AUC, ganancia de pureza, FPR y exactitud. La exactitud es la proporción total de aciertos; la FPR es cuántos negativos reales marqué como positivos; el AUC resume la calidad del ordenamiento del clasificador sobre todos los umbrales posibles; la ganancia de pureza es lo que un árbol optimiza al elegir cada corte — de hecho es lo mismo que usé para leer la importancia de variables de mi Random Forest. La varianza es un estadístico de dispersión: la calculé sobre el precio de las propiedades en el EDA, y ahí no había ninguna clase que predecir.

**8. Prueba de comprensión**
- *P: ¿La exactitud es una buena métrica siempre?* → R: No. Con clases desbalanceadas es engañosa: en mi desafío de galaxias la clase 0 era 9,6 % del total, y un modelo que nunca la predijera tendría exactitud alta y sería inútil. Por eso ahí la métrica oficial era F1-macro.
- *P: ¿En qué se diferencia el AUC de la exactitud?* → R: La exactitud se calcula fijando un umbral; el AUC recorre todos los umbrales y mide si el clasificador ordena bien los positivos por encima de los negativos. Un modelo puede tener buen AUC y mala exactitud si el umbral está mal elegido.

---

### Pregunta 5 — LLMs y agentes

**PREGUNTA ORIGINAL:** Seleccionar la afirmación correcta sobre LLMs y agentes.

**RESPUESTA ENTREGADA:** La correcta señala que un agente puede usar herramientas, almacenar conocimiento y ejecutar acciones, mientras un LLM se orienta al procesamiento de información y la generación de texto. Las demás fallan porque: un LLM no garantiza acceso a hechos recientes sin recuperación externa; los agentes sí pueden colaborar con personas u otros agentes; y entrenar un LLM sí requiere grandes volúmenes de datos y cómputo.

**1. ¿Qué evalúa?** La distinción entre **modelo** (una función que produce texto) y **sistema agente** (un bucle que percibe, decide, usa herramientas y actúa). También el límite de conocimiento de un LLM sin recuperación.

**2. ¿Qué había que entender?**
- Que el LLM es un componente del agente, no su sinónimo.
- Que las herramientas, la memoria y la ejecución de acciones son lo que convierte un modelo en agente.
- Que el conocimiento de un LLM está congelado en su entrenamiento salvo que se le dé acceso externo.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA] — guía de estudio, sección 9 "LLM y agente: modelo versus sistema":**
> *"Un LLM procesa contexto y genera una salida. Un sistema agente puede envolver ese modelo con herramientas, estado/memoria, reglas y un ciclo: decidir → actuar → observar → decidir nuevamente."*

Con la analogía del asesor al que se le da teléfono, calendario, buscador, archivos y permiso para ejecutar tareas; tres ejemplos (viaje, código, datos recientes); y el ejercicio de transferencia: *"Un chatbot puede responder 'crea una reunión a las 15:00'. ¿Qué capacidades adicionales necesita para que la reunión realmente aparezca en un calendario?"* Cubre además el distractor de los hechos recientes: *"Un modelo sin fuente externa no obtiene mágicamente un hecho posterior a su conocimiento; un sistema puede buscarlo y entregárselo como contexto."*

**[NO EVIDENCIADO]** en material del curso: no hay apuntes de clase ni notebooks sobre el tema. La cobertura proviene íntegramente de la guía.

**[INFERENCIA, débil]** El directorio contiene `.cursor/agents/puente-hito.md` y `.cursor/rules/maci-coherencia-hitos.mdc`: definiciones de un agente con rol, instrucciones, una fuente de verdad externa (`anclaje.json`) y reglas de no-invención. Esto evidencia que el autor **construyó y operó** un agente con herramientas y conocimiento anclado, que es exactamente la distinción que la respuesta enuncia. Pero es evidencia de práctica instrumental, no de estudio del concepto, y no puede presentarse como más que eso.

**4. Deconstrucción del razonamiento**

1. Las cuatro alternativas se resuelven por eliminación, no por reconocimiento de la correcta.
2. "Un LLM garantiza acceso a hechos recientes" → falso por construcción: el modelo aprende de un corpus con fecha de corte; sin recuperación externa no puede saber lo posterior.
3. "Los agentes no pueden colaborar" → falso: la colaboración con personas y con otros agentes es un patrón estándar, no una excepción.
4. "Entrenar un LLM no requiere grandes volúmenes de datos ni cómputo" → falso: la escala es precisamente lo que define a esta familia de modelos.
5. Queda la afirmación sobre la diferencia funcional, que además se verifica positivamente: un agente añade al modelo un bucle de acción, herramientas y estado.

**5. Punto de confusión**
Tratar "LLM" y "agente" como sinónimos porque en la práctica se accede a ambos por una interfaz de chat. La distinción decisiva es si el sistema puede **ejecutar acciones y observar su resultado**. Un LLM puro produce texto y termina; un agente encadena decisiones sobre el mundo.

**6. Contrafactual**
*Si se interpretara que un LLM "sabe" cosas del mundo actual porque responde sobre temas actuales, se marcaría como correcta la alternativa del acceso a hechos recientes. Esa interpretación falla porque el modelo reproduce lo que estaba en su corpus de entrenamiento; para hechos posteriores necesita un mecanismo de recuperación o búsqueda que le entregue el dato como entrada.*

**7. Respuesta razonada (reconstruida)**
La correcta es la que separa funciones: un LLM es un modelo que procesa y genera texto; un agente es un sistema construido alrededor de un modelo que además usa herramientas, mantiene conocimiento o memoria y ejecuta acciones. Las otras tres se caen: un LLM sin búsqueda externa no tiene hechos recientes, los agentes sí colaboran, y entrenar un modelo de esa escala es intensivo en datos y cómputo.

**8. Prueba de comprensión**
- *P: ¿Qué le falta a un LLM para ser un agente?* → R: Un bucle: capacidad de invocar herramientas, recibir el resultado y decidir el siguiente paso, más algún estado que persista entre pasos.
- *P: Si un LLM responde sobre un hecho de esta semana, ¿qué explica eso?* → R: O el hecho estaba en su entrenamiento, o alguien se lo entregó como contexto —búsqueda, RAG, un documento adjunto—. No es conocimiento propio del modelo.

---

### Pregunta 6 — Revoluciones recientes en inteligencia artificial

**PREGUNTA ORIGINAL:** Cuáles están entre las revoluciones recientes impulsadas por redes neuronales: PLN, computación en la nube, bases de datos relacionales, detección de objetos en imágenes.

**RESPUESTA ENTREGADA:** PLN y detección de objetos. La nube es infraestructura habilitante, no técnica de IA; las bases de datos relacionales son tecnología de almacenamiento, no una revolución reciente de redes neuronales.

**1. ¿Qué evalúa?** Distinguir **técnica de IA** de **infraestructura habilitante** y de **tecnología de datos preexistente**. Es una pregunta sobre causalidad tecnológica, no sobre memoria de fechas.

**2. ¿Qué había que entender?** Qué avance es atribuible a redes neuronales profundas y qué avance simplemente las hizo posibles o convivió con ellas.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA] — guía de estudio, sección 10 "Redes neuronales: causa versus infraestructura":**
> *"Un automóvil eléctrico necesita carreteras. Eso no significa que la carretera sea una tecnología de automóvil eléctrico. De la misma manera, la nube puede proporcionar cómputo para entrenar redes, pero no es una red neuronal."*

La guía plantea la distinción exacta que la pregunta evalúa —*"¿Qué significa que algo sea 'causa' frente a 'condición habilitante'?"*, *"¿Una GPU es una red neuronal?"*, *"¿Que una tecnología sea usada por IA la convierte en una técnica de IA?"*— y la transfiere: *"Una fábrica necesita electricidad para producir medicamentos. ¿Dirías que la electricidad es una técnica farmacológica?"*

**[NO EVIDENCIADO]** fuera de la guía: no hay ningún otro archivo sobre panorama de IA, y el proyecto completo no contiene una sola red neuronal.

**4. Deconstrucción del razonamiento**

1. Preguntar de cada ítem: ¿qué lo hizo avanzar?
2. PLN: el salto en traducción, comprensión y generación viene de arquitecturas neuronales (redes recurrentes y luego transformers). Atribuible.
3. Detección de objetos: el salto viene de redes convolucionales profundas. Atribuible.
4. Computación en la nube: es capacidad de cómputo alquilable. Habilita el entrenamiento, pero su existencia no depende de redes neuronales y no es una técnica de IA. No atribuible.
5. Bases de datos relacionales: modelo formalizado en los años 70. Ni reciente ni neuronal. No atribuible.

**5. Punto de confusión**
Confundir **causa** con **condición de posibilidad**. La nube es indispensable para entrenar modelos grandes, y eso hace tentador incluirla. Pero la pregunta dice "revoluciones **impulsadas por** redes neuronales": la dirección de la flecha es la que decide. La nube impulsa a las redes, no al revés.

**6. Contrafactual**
*Si se interpretara "revoluciones recientes en IA" como "tecnologías sin las cuales la IA moderna no existiría", se incluiría la computación en la nube e incluso las bases de datos. Esa interpretación falla porque convierte una condición habilitante en un resultado; bajo ese criterio habría que incluir también los semiconductores.*

**7. Respuesta razonada (reconstruida)**
PLN y detección de objetos en imágenes. Las dos son áreas donde el salto de desempeño se produjo por arquitecturas neuronales profundas. La nube es donde se entrenan esos modelos, no una técnica de IA, y las bases de datos relacionales son de los años 70 y no tienen relación con redes neuronales.

**8. Prueba de comprensión**
- *P: ¿Por qué el PLN es una "revolución" y no simplemente un área que mejoró?* → R: Porque cambió el tipo de tarea que se puede resolver: se pasó de sistemas de reglas y estadística de n-gramas a modelos que generalizan a tareas para las que no fueron programados.
- *P: ¿Podría haber ocurrido el aprendizaje profundo sin la nube?* → R: Más lento y con menos actores, pero el mecanismo es el hardware paralelo (GPU), del que la nube es una vía de acceso. La nube democratizó el acceso; no inventó la técnica.

---

### Pregunta 7 — Regresión polinomial y sobreajuste

**PREGUNTA ORIGINAL:** Evaluar si el ajuste polinomial de una curva a cinco árboles es correcto y proponer mejoras.

**RESPUESTA ENTREGADA:** Si la curva pasa exactamente por los cinco puntos con oscilaciones pronunciadas, el ajuste no es adecuado (grado alto, memoriza). Mejoras: bajar el grado, recolectar más observaciones, usar validación cruzada para comparar grados, y regularizar (Ridge o Lasso).

**1. ¿Qué evalúa?** Reconocer sobreajuste **visualmente** y proponer remedios ordenados por su mecanismo: reducir capacidad, aumentar evidencia, medir honestamente, penalizar coeficientes.

**2. ¿Qué había que entender?**
- Que un polinomio de grado n−1 puede interpolar exactamente n puntos, y que error de entrenamiento cero no es una virtud.
- Que con n = 5 la evidencia es mínima y cualquier modelo flexible va a memorizar.
- Que la regularización ataca el problema por otra vía: no reduce el grado nominal, reduce la magnitud efectiva de los coeficientes.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA] — guía de estudio, sección 8 "Regresión polinomial: una curva bonita también puede engañar":**
> *"Conecta cinco chinches sobre una tabla usando una cinta extremadamente flexible. Puedes hacer que la cinta toque todas las chinches, pero entre ellas puede formar curvas absurdas."*
> *"Reducir grado, aumentar observaciones y regularizar son mecanismos distintos para controlar la flexibilidad."*

La guía cubre los tres remedios y plantea explícitamente la distinción fina que separa dos de ellos: *"¿Bajar el grado y Ridge hacen exactamente lo mismo?"*. Sus tres ejemplos (crecimiento, ventas, temperatura) son de dominios distintos al del certamen, lo que ejercita transferencia y no reconocimiento.

**[NO EVIDENCIADO] — en el código:** cero coincidencias de "polinomi" en los scripts y notebooks de `F:\MACI`. No hay ningún ajuste polinomial ejecutado.

**[EVIDENCIA] — los cuatro remedios, cada uno por separado:**

- *Preferir el modelo más simple:* `V1_Trabajo_N2...ipynb` Paso 7 — *"La complejidad solo se justifica si mejora el test 2017 de forma material"*; `INFORME_MODELO_FCD_P3.md` §7 mantiene Gradient Boosting como alternativa aceptable por tener **menor brecha** train-test (+0,143 vs +0,176) aunque su error sea levemente mayor.
- *Validación cruzada para comparar candidatos:* `INFORME_MODELO_FCD_P3.md` §1.2 y §3, ranking por CV dentro de 2016.
- *Regularización:* `modelamiento_temporal.py` usa `Ridge`; el modelo final es `HistGradientBoostingRegressor(..., l2_regularization=1.0)` (§7). Y §3 documenta el fracaso de Ridge con target log: *"un modelo lineal extrapola sin límite ante combinaciones de variables no vistas"*.
- *Más observaciones:* `INFORME_MODELO_FCD_P3.md` §6 marca como límite de uso las regiones con `n < 60` (Eastern Victoria n = 53, MAPE 59,3 %; Western Victoria n = 32, MAPE 37,7 %). Es exactamente el argumento de "pocos datos → estimación no confiable", medido.

**[INFERENCIA]** El conjunto de remedios que la respuesta propone coincide, uno a uno, con los mecanismos que el autor aplicó en su proyecto sobre un problema distinto. El razonamiento es transferible y está documentado; el objeto concreto (polinomio de grado alto sobre 5 puntos) no lo está.

**4. Deconstrucción del razonamiento**

1. Observación: la curva pasa por los cinco puntos exactamente → error de entrenamiento cero.
2. Primera pregunta: ¿es eso bueno? No, es sospechoso. Con 5 puntos, un polinomio de grado 4 siempre puede interpolarlos exactamente, sin importar si hay o no una relación real.
3. Segunda observación: oscilaciones pronunciadas entre los puntos. Eso es lo diagnóstico: la función hace cosas violentas donde no hay datos que la restrinjan.
4. Contraste con el fenómeno: el volumen de un árbol frente a su diámetro o altura es una relación monótona y suave. Una curva que sube y baja entre observaciones contradice el fenómeno, no lo describe.
5. Conclusión: el ajuste captura ruido de medición de cinco árboles, no la ley que los relaciona.
6. Remedios por mecanismo: **bajar el grado** reduce capacidad; **más árboles medidos** aumentan la evidencia que restringe la curva; **validación cruzada** permite elegir el grado sin autoengañarse con el error de ajuste; **Ridge/Lasso** penalizan coeficientes grandes, que son la firma matemática de las oscilaciones.

**5. Punto de confusión**
Creer que un ajuste que pasa por todos los puntos es el mejor ajuste. Es el error central de la pregunta: confunde **error de entrenamiento** con **calidad del modelo**. La segunda confusión es pensar que la solución es siempre bajar el grado; con n = 5 el problema de fondo es la cantidad de datos, y ningún grado arregla del todo la falta de evidencia.

**6. Contrafactual**
*Si se interpretara "buen ajuste" como "mínimo error sobre los datos disponibles", se respondería que el ajuste es correcto e incluso óptimo. Esa interpretación falla porque con cinco puntos siempre existe un polinomio de grado 4 con error exactamente cero: el criterio no discrimina entre un modelo que aprendió la relación y uno que la memorizó, por lo que no puede usarse para juzgar el ajuste.*

**7. Respuesta razonada (reconstruida)**
No es un buen ajuste. Que la curva toque los cinco puntos no prueba nada: con cinco puntos siempre puedo construir un polinomio de grado 4 que los toque todos. Lo que delata el problema son las oscilaciones entre puntos, porque la relación entre las dimensiones de un árbol y su volumen debería ser suave y creciente. Para mejorarlo: bajar el grado hasta el modelo más simple que siga la tendencia, medir más árboles, comparar grados con validación cruzada en vez de mirar el error de ajuste, y si hace falta regularizar con Ridge o Lasso para penalizar coeficientes grandes. En mi proyecto usé estas mismas ideas: elegí modelo por CV dentro de 2016 sin mirar 2017, dejé `l2_regularization` en el modelo final y marqué como no confiables las regiones con menos de 60 observaciones.

**8. Prueba de comprensión**
- *P: ¿Qué grado elegiría y cómo lo justifica?* → R: No lo elijo a ojo: ajusto grados 1, 2 y 3 y comparo su error en validación cruzada. Con cinco puntos probablemente sea leave-one-out. Me quedo con el grado más bajo cuyo error de validación no sea materialmente peor.
- *P: ¿Ridge le baja el grado al polinomio?* → R: No. Deja los mismos términos pero encoge sus coeficientes, así que la curva resultante es más suave. Bajar el grado elimina términos; regularizar los amortigua.

---

### Pregunta 8 — Matriz de confusión y métricas

**PREGUNTA ORIGINAL:** Para el modelo representado por una línea verde punteada, calcular matriz de confusión, exactitud, precisión, TPR y FPR, explicando los supuestos.

**RESPUESTA ENTREGADA:** Supuestos declarados (círculos = positivos, triángulos = negativos, lado izquierdo = predicción positiva). VP = 12, FN = 3, FP = 4, VN = 31. Exactitud 86 %, precisión 75 %, TPR 80 %, FPR 11,4 %, TNR 88,6 %.

**1. ¿Qué evalúa?** Construir una matriz de confusión a partir de una frontera de decisión geométrica y derivar métricas sabiendo **sobre qué denominador** se calcula cada una.

**2. ¿Qué había que entender?**
- Qué es VP, FN, FP, VN respecto de una clase declarada positiva.
- Que precisión y TPR comparten numerador (VP) pero tienen denominadores distintos: precisión divide por lo **predicho** positivo; TPR divide por lo **real** positivo.
- Que la elección de clase positiva es una convención que hay que declarar, porque invierte todas las métricas asimétricas.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA] — matriz de confusión y métricas por clase:** `Desafio/REPORT.md` §5 presenta una matriz 3×3 con filas = real y columnas = predicho, junto a precision/recall/F1 por clase. `Desafio/src/gz_lib.py` y `01_repro_notebook.py` la calculan con `confusion_matrix` y `classification_report`.

**[EVIDENCIA] — verificación aritmética independiente.** Recalculé los cinco valores a partir de los conteos declarados: exactitud (12+31)/50 = 86,0 %; precisión 12/16 = 75,0 %; TPR 12/15 = 80,0 %; FPR 4/35 = 11,43 %; TNR 31/35 = 88,57 %. **Todas exactas**, y la tabla cierra por filas (15, 35), columnas (16, 34) y total (50). La aritmética y la estructura de la matriz son internamente consistentes y correctas.

**[EVIDENCIA] — guía de estudio, sección 6 "Matriz de confusión: convertir una figura en números":** contiene el procedimiento (*"Primero fijo la clase positiva. Después cruzo Real +/− con Predicho +/−"*), la analogía del guardia que decide quién entra, y **los conteos exactos del certamen**: *"Ejemplo 1 — Conteo 12/3/4/31… Accuracy=(12+31)/50=86%. Precision=12/(12+4)=75%. Recall=12/(12+3)=80%. FPR=4/(4+31)=11,4%."* Plantea además las dos confusiones críticas: *"¿Por qué precision y recall pueden ser distintos aunque comparten VP en el numerador?"* y *"¿FPR es 1-precision? Explica mirando los denominadores."*

**[RESERVA] — circularidad.** Como la guía declara haberse construido a partir de las preguntas del certamen, el conteo pasó del certamen a la guía y no al revés. La cifra queda **trazable**, no **derivada**. Lo que sí queda establecido es el dominio del procedimiento, que la guía ejercita con números nuevos: *"Construye mentalmente una matriz para 20 casos: 5 positivos reales; detectas 4; además acusas erróneamente a 3 negativos."* La figura original del certamen sigue sin estar en el directorio.

**4. Deconstrucción del razonamiento**

1. Antes de contar nada, fijar la convención: qué clase es positiva y qué lado de la línea predice positivo. Sin eso, "falso positivo" no significa nada.
2. Con la línea fijada, cada punto cae en una de cuatro casillas: círculo a la izquierda (VP), círculo a la derecha (FN), triángulo a la izquierda (FP), triángulo a la derecha (VN).
3. Contar da la matriz. Las marginales son controles: los círculos totales (15) y los triángulos totales (35) deben coincidir con lo que se ve en la figura.
4. Las métricas salen de elegir el denominador correcto:
   - Exactitud: aciertos sobre todo → (VP+VN)/N.
   - Precisión: de lo que **dije** positivo, cuánto acerté → VP/(VP+FP).
   - TPR: de lo que **era** positivo, cuánto capturé → VP/(VP+FN).
   - FPR: de lo que **era** negativo, cuánto marqué mal → FP/(FP+VN).
5. Lectura final en lenguaje del problema, no en fórmulas.

**5. Punto de confusión**
Confundir **precisión** con **exactitud**, y **precisión** con **sensibilidad**. Los tres comparten la palabra "acertar" en lenguaje corriente. La distinción operativa es el denominador: exactitud mira todo el conjunto; precisión mira solo las predicciones positivas; TPR mira solo los casos realmente positivos. Aquí precisión (75 %) y TPR (80 %) difieren justamente porque FP ≠ FN.

La segunda confusión, específica de esta pregunta: **FPR no es 1 − precisión**. FPR divide por los negativos reales (35), no por las predicciones positivas (16).

**6. Contrafactual**
*Si se interpretara que los triángulos son la clase positiva, se obtendría VP = 31, FN = 4, FP = 3, VN = 12: la exactitud seguiría siendo 86 %, pero la precisión pasaría a 91 %, la TPR a 89 % y la FPR a 20 %. Esa interpretación no es incorrecta en sí, pero sin declararla la respuesta sería irreproducible — por eso la convención debe explicitarse antes de calcular. La exactitud es simétrica; el resto no.*

**7. Respuesta razonada (reconstruida)**
Primero declaro la convención: círculos son la clase positiva y el lado izquierdo de la línea es la predicción positiva. Con eso, cada punto cae en una de cuatro casillas y cuento: 12 círculos bien clasificados, 3 círculos que se me escaparon, 4 triángulos que llamé círculo, 31 triángulos bien clasificados. De ahí: acierto en 43 de 50 casos, o sea 86 % de exactitud. Cuando digo "círculo", acierto 12 de 16, o sea 75 % de precisión. De los 15 círculos que existían, encontré 12, o sea 80 % de sensibilidad. Y de los 35 triángulos, marqué 4 como círculos por error: 11,4 % de falsas alarmas. La lectura es que el modelo es conservador con los círculos: falla más al declararlos que al encontrarlos.

**8. Prueba de comprensión**
- *P: Si mueve la línea a la derecha, ¿qué le pasa a la TPR y a la FPR?* → R: Ambas suben. Declaro más casos positivos, así que capturo más círculos reales pero también marco más triángulos. Es el compromiso que la curva ROC dibuja.
- *P: ¿Por qué precisión y sensibilidad dan distinto si el numerador es el mismo?* → R: Porque el denominador cambia de universo: precisión divide por lo que predije positivo, sensibilidad por lo que realmente era positivo. Con 16 predicciones positivas y 15 positivos reales, los cocientes no pueden coincidir salvo por casualidad.

---

### Pregunta 9 — Curva ROC y comparación de modelos

**PREGUNTA ORIGINAL:** Calcular TPR y FPR para dos modelos con distintos umbrales y determinar cuál es mejor.

**RESPUESTA ENTREGADA:** Tabla de TPR/FPR por umbral para Modelo 1 (0,95/0,34; 0,80/0,14; 0,45/0,03) y Modelo 2 (0,88/0,51; 0,70/0,23; 0,38/0,06). Modelo 1 preferible: curva más cerca de la esquina superior izquierda, **AUC ≈ 0,78 frente a 0,68**.

**1. ¿Qué evalúa?** Leer una curva ROC como familia de operaciones del mismo modelo a distintos umbrales, y comparar dos clasificadores sin fijar un umbral.

**2. ¿Qué había que entender?**
- Que un punto ROC no caracteriza un modelo: lo caracteriza la curva completa.
- Que subir el umbral baja TPR y FPR simultáneamente.
- Que la comparación válida es "a igual FPR, ¿quién tiene más TPR?" — o, mejor, dominancia en todos los puntos.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA] — umbrales y reglas de decisión:** `Desafio/src/05_decision_rule.py`, `analysis/decision_rule.csv`, la búsqueda de pesos `w0, w1, w2` sobre probabilidades OOF y la advertencia de `REPORT.md` §10.1 de que optimizar y reportar el umbral sobre el mismo OOF infla las cifras. Eso es comprensión avanzada del vínculo umbral–métrica.

**[EVIDENCIA] — AUC como capacidad de ordenamiento:** `REPORT.md` §8.3 y §11 (techo AUC 0,754 para 0-vs-resto).

**[EVIDENCIA] — guía de estudio, sección 7 "ROC y AUC: el efecto de mover el umbral":** cubre el intercambio con la analogía del detector de humo, la definición (*"ROC representa TPR/Recall frente a FPR para distintos umbrales. Un punto no representa todo el modelo"*), y **el argumento de dominancia**: *"Si en varios umbrales A logra más TPR y menos FPR que B, A domina en esos puntos."* Incluye las tres preguntas de control: *"¿Por qué TPR=1 y FPR=1 no es un gran clasificador?"*, *"¿Qué significa aproximadamente AUC=0,5?"*, *"¿Puede un modelo con buen AUC tener un umbral operativo malo?"*

**[NO EVIDENCIADO] — los conteos y umbrales de la pregunta.**

**[CONTRADICCIÓN QUE PERSISTE] — las cifras de AUC.** La guía **no contiene** 0,78 ni 0,68. Enseña el método correcto (dominancia) y omite justamente los dos números que resultan inconsistentes con la tabla del certamen. Ver Fase 5.3: la aparición de la guía no resuelve este punto, lo aísla más.

**4. Deconstrucción del razonamiento**

1. Cada fila de la tabla es el **mismo** modelo operando a un umbral distinto. Bajar el umbral mueve el punto hacia arriba y a la derecha; subirlo, hacia abajo y a la izquierda. La tabla es internamente coherente con eso en ambos modelos.
2. Para comparar, no sirve comparar filas sueltas: son regímenes distintos.
3. La comparación correcta es punto a punto por umbral comparable, o por área bajo la curva.
4. Comparando umbral a umbral: bajo 0,95/0,34 contra 0,88/0,51; medio 0,80/0,14 contra 0,70/0,23; alto 0,45/0,03 contra 0,38/0,06. En los tres, el Modelo 1 tiene **mayor TPR y menor FPR**.
5. Eso es **dominancia estricta**: no hay compromiso que negociar, el Modelo 1 es mejor en todo el rango observado. Es un argumento más fuerte que el AUC, porque no depende de cómo se interpole entre puntos.
6. Respuesta: Modelo 1.

**5. Punto de confusión**
Elegir el modelo por un solo punto de operación —típicamente el de mayor TPR— ignorando el costo en FPR. También, tratar la curva ROC como si midiera exactitud: no lo hace, es independiente de la prevalencia de clases y del umbral.

**6. Contrafactual**
*Si se interpretara "mejor modelo" como "el que alcanza la TPR más alta", se elegiría el Modelo 1 por su 0,95 — respuesta correcta por una razón incorrecta. La interpretación falla porque esa TPR se obtiene a FPR 0,34; sin mirar el par completo, el mismo criterio elegiría un clasificador que declara todo positivo (TPR = 1, FPR = 1), que es inútil.*

**7. Respuesta razonada (reconstruida)**
El Modelo 1. Y no hace falta el AUC para decirlo: comparando los dos modelos umbral por umbral, el Modelo 1 tiene más TPR **y** menos FPR en los tres casos. Cuando un modelo domina al otro en todos los puntos de operación, su curva ROC queda íntegramente por encima y más cerca de la esquina superior izquierda, así que su área también es mayor. Si tuviera que dar la cifra, la calcularía por trapecios sobre los puntos disponibles más (0,0) y (1,1).

**[NOTA HONESTA]** Al hacer ese cálculo con los puntos de la tabla, el AUC trapezoidal da **≈ 0,894 para el Modelo 1 y ≈ 0,785 para el Modelo 2**, no 0,78 y 0,68 como afirma el documento. La conclusión sobre cuál modelo es mejor no cambia, pero las dos cifras de AUC del documento **no son derivables de su propia tabla**. Si el profesor lo pregunta, la respuesta honesta es: la tabla sostiene la dominancia; esas cifras de AUC no las puedo reproducir desde la tabla.

**8. Prueba de comprensión**
- *P: ¿Puede un modelo con mayor AUC ser peor en la práctica?* → R: Sí. Si el punto de operación que necesito está en una zona donde el otro modelo es superior, o si el costo de un FP es muy distinto del de un FN, el AUC promedia regiones que a mí no me interesan.
- *P: ¿Qué significa AUC = 0,5?* → R: Que el modelo ordena al azar: la probabilidad de asignar mayor puntaje a un positivo que a un negativo es la de una moneda.

---

### Pregunta 10 — Punto base

**PREGUNTA ORIGINAL:** Seleccionar la alternativa correspondiente al punto base.

**RESPUESTA ENTREGADA:** *"No es posible establecer una respuesta definitiva porque las alternativas de la figura no están disponibles en el material recibido. Esta pregunta debe completarse revisando las opciones mostradas en Canvas."*

**1. ¿Qué evalúa?** No evaluable: el enunciado depende de una figura ausente.

**3. ¿Dónde está ese conocimiento?** **[NO EVIDENCIADO]** y no evaluable.

**4–7. Observación de proceso.** Esta "no respuesta" es, paradójicamente, uno de los rastros más informativos del documento. El autor **declara la ausencia de información en vez de producir una respuesta plausible**. Ese comportamiento tiene un antecedente documentado y sistemático en el material del proyecto:

**[EVIDENCIA]** `V2_Trabajo_N1...ipynb` imprime la cadena literal `"NO VERIFICABLE CON LOS DATOS DISPONIBLES"` en **más de una docena de celdas**, como rama `else` sistemática cuando el CSV no está cargado.

**[EVIDENCIA]** `.cursor/agents/puente-hito.md`: *"Si un número no está ahí ni en la salida ejecutada del notebook, recálculalo o márcalo como pendiente. Nunca redondees de memoria."*

**[EVIDENCIA]** `INFORME_MODELO_FCD_P3.md` §0 "Fe de erratas" y `README_POR_QUE_OBSOLETO.md`: el autor invalida por escrito sus propias cifras anteriores por no haber sido calculadas.

La Pregunta 10 aplica esa misma regla dentro del certamen. Es un patrón de conducta metodológica consistente y anterior al documento de respuestas, no una frase aislada.

**8. Prueba de comprensión**
- *P: ¿Por qué dejó esta pregunta sin responder?* → R: Porque la alternativa correcta depende de una figura que no tenía a la vista, y elegir una opción sin verla sería adivinar. Prefiero declarar el vacío a rellenarlo.

---

### Pregunta 11 — Comentarios y supuestos

**PREGUNTA ORIGINAL:** Ingrese cualquier comentario o supuesto realizado.

**RESPUESTA ENTREGADA:** Declara los supuestos de interpretación de figuras (clases y lados de la línea), advierte que los conteos y umbrales de las preguntas 8 y 9 **deben verificarse con la figura original**, explica el criterio usado en la 7, y cierra: *"Estos supuestos permiten explicar el procedimiento, pero no reemplazan la lectura directa de las figuras del certamen."*

**1. ¿Qué evalúa?** Honestidad metodológica: capacidad de separar lo que se calculó de lo que se supuso.

**3. ¿Dónde está ese conocimiento en el material?**

**[EVIDENCIA]** El mismo patrón citado en la Pregunta 10, más:

- `INFORME_MODELO_FCD_P3.md` §5: *"los modelos corren con sus hiperparámetros por defecto de DashAI… por lo que las cifras no son idénticas a las del pipeline local, pero permiten verificar el ordenamiento"* — declaración explícita del límite de una comparación.
- §6: *"Parte es sobreajuste y parte es el shift…; se documenta, no se oculta."*
- §6: sección *"Lo que el modelo **no** hace"*, dedicada a los límites de uso.
- `Desafio/REPORT.md` §11: once limitaciones enumeradas, incluida *"la desviación entre folds es mayor que casi todas las diferencias que se quieren medir, por lo que la mayoría de las comparaciones de modelos no son concluyentes"*.

**4. Deconstrucción.** El razonamiento aquí no es conceptual sino epistémico: separar tres capas —lo medido, lo supuesto y lo no disponible— y hacerlas visibles al evaluador para que pueda verificar el procedimiento aun si discrepa del supuesto.

**5. Punto de confusión.** Creer que declarar supuestos debilita la respuesta. Es al revés: una respuesta numérica sin supuesto declarado es irreproducible, y en las preguntas 8 y 9 la convención de clase positiva cambia todos los resultados asimétricos.

**7. Respuesta razonada (reconstruida)**
En las preguntas con figura tuve que fijar una convención para poder calcular: círculos como clase positiva y el lado izquierdo de la línea como predicción positiva. Los conteos que uso dependen de leer bien la figura, así que los declaro como supuesto y no como dato verificado. En la 7 el criterio fue que una curva muy ondulada sobre cinco puntos es indicio de sobreajuste. Todo esto explica el procedimiento; si el conteo de la figura fuera otro, el procedimiento sigue siendo el mismo y los números se recalculan.

---

## FASE 3 — Correspondencias entre material de proyecto y certamen

No busco similitud textual, sino **transformación conceptual**: casos donde un principio aplicado en el proyecto a un problema de regresión inmobiliaria debe reinterpretarse para responder una pregunta de clasificación o de teoría.

| # | Concepto en mi material | Pregunta del certamen | Operación conceptual necesaria |
|---|---|---|---|
| T1 | *"si dos modelos fuertes fallan en las mismas filas, promediarlos no puede aportar"* (`08_ensemble.py`) | P1 | De **medir** diversidad de errores entre modelos reales → a **razonar sobre el caso límite** de diversidad cero. Requiere ver que "modelos idénticos" es el extremo del eje que el script mide, no un caso nuevo |
| T2 | Tabla `R² Train / R² Test / Brecha / Interpretación` (M3, M5) | P2 | De **usar** la brecha como criterio de selección → a **enunciar** qué fenómeno la produce. Pasar de instrumento a definición |
| T3 | `Suburb` con 311 categorías descartado "= sobreajuste"; `Bedroom2` con importancia +0,0009 | P3, afirmación 1 | De un **caso particular** (dos variables descartadas por alta cardinalidad e irrelevancia) → a la **regla general** "más atributos no evita el sobreajuste". Generalización inductiva, no cita |
| T4 | *"La CV no sustituye al test temporal"* (M2, Paso 8) | P3, afirmación 2 | Distinción fina: la CV **estima** generalización, no la **garantiza**. El certamen pregunta si sirve para *detectar*, formulación más débil que la que el material maneja |
| T5 | Ridge diverge en 2017 con MAE 9,8e+08 ante zonas nuevas (M5 §3) | P3, afirmación 3 (producción) | De un **fallo medido** de extrapolación → a la afirmación general "puede fallar ante datos reales nuevos". El caso local es incluso más extremo que la afirmación |
| T6 | `HistGradientBoostingRegressor(..., l2_regularization=1.0)`; uso de `Ridge` (M5 §7) | P7, remedio 4 | De **regularización aplicada** en un ensamble de árboles y un lineal → a **regularización propuesta** para un polinomio. Requiere entender que la penalización actúa sobre la magnitud de coeficientes/hojas, transversal al tipo de modelo |
| T7 | Regiones con `n < 60` marcadas como no confiables (MAPE 59,3 %) (M5 §6) | P7, remedio 2 (más datos) | De **cuantificar** la falta de evidencia en subgrupos pequeños → a **proponer** más observaciones para un ajuste con n = 5. Mismo principio, tres órdenes de magnitud abajo |
| T8 | *"Top 10 del Random Forest por reducción de impureza"* (M2, Paso 11) | P4, ganancia de pureza | De **leer** importancias basadas en impureza → a **clasificar** la ganancia de pureza como concepto propio de clasificación por árboles. Requiere saber qué optimiza el árbol al cortar |
| T9 | `price_stats` con `"varianza": price.var()` junto a media, mediana, IQR (M1) | P4, varianza | De **usar** la varianza como descriptor de una distribución → a **excluirla** como métrica de rendimiento. La transformación es una negación fundada: el material la usa exactamente en el rol que el certamen dice que tiene |
| T10 | Matriz de confusión 3×3 + precision/recall/F1 por clase (`Desafio/REPORT.md` §5) | P8 | De **multiclase** a **binaria**: reducir la matriz 3×3 a las cuatro casillas VP/FN/FP/VN, lo que exige declarar cuál clase es positiva |
| T11 | *"optimizar y reportar el umbral sobre el mismo OOF infla las cifras"* (§10.1) | P9 | De **umbral como objeto de tuning riesgoso** → a **umbral como eje de la curva ROC**. Es la misma variable vista desde dos roles distintos |
| T12 | `"NO VERIFICABLE CON LOS DATOS DISPONIBLES"`, "Fe de erratas", regla de no-invención | P10, P11 | De una **práctica** en el manejo de datos → a una **conducta declarativa** dentro de una evaluación |

**Correspondencias que NO existen:** P5 (LLMs/agentes) y P6 (revoluciones de IA) no tienen ningún antecedente en el material. No hay transformación conceptual que reconstruir, porque no hay origen local.

---

## FASE 4 — Conocimiento, razonamiento, redacción y apoyo de IA

Separación por pregunta. La columna D no afirma qué hizo la IA; afirma **qué parte del resultado no queda explicada por el material local** y podría razonablemente corresponder a estructuración, explicación o mejora lingüística externa.

| Preg. | A. Conocimiento necesario | B. Razonamiento decisivo | C. Redacción | D. Qué no explica el material local |
|---|---|---|---|---|
| 1 | Mecanismo de reducción de varianza por promediado | Ver que "idénticos" = diversidad cero = ensamble degenerado | Compacta, técnica, sin ejemplo propio | La formulación general y abstracta. El material contiene el principio en forma **operacional** (código que mide diversidad), no como enunciado teórico. El paso de uno a otro es genuino, pero la redacción final es de manual |
| 2 | Definición operativa de sobreajuste | Distinguir brecha de error absoluto | Definición correcta y neutra | Poco. El material sostiene este contenido con holgura, incluso por encima (separa sobreajuste de covariate shift, cosa que la respuesta no menciona) |
| 3 | Cinco afirmaciones independientes | Evaluar cada una por su mecanismo; detectar la inversión filas/columnas | Enumeración ordenada | Poco en contenido. La **estructura** de la respuesta (bullets paralelos) es propia de redacción asistida; los cinco contenidos tienen anclaje local |
| 4 | Taxonomía: métrica / criterio de entrenamiento / estadístico | Clasificar por el objeto que cada cantidad describe | Precisa, una frase por término | La FPR no aparece en ningún archivo local. Su inclusión y su definición correcta no son reconstruibles desde el material |
| 5 | LLM vs agente; límite de conocimiento del modelo | Eliminación de tres distractores | Correcta y ordenada | **Casi todo.** No hay material de estudio sobre el tema. Solo existe evidencia de uso práctico de agentes (`.cursor/agents/`), que no es lo mismo que evidencia de estudio del concepto |
| 6 | Qué avance atribuir a redes neuronales | Distinguir causa de condición habilitante | Correcta y ordenada | **Todo.** No hay material local sobre IA, redes neuronales, visión ni PLN |
| 7 | Interpolación, capacidad, regularización | Leer sobreajuste en una figura y proponer remedios por mecanismo | Lista de cuatro mejoras | El **caso polinomial** (cero apariciones en el directorio). Los cuatro remedios sí tienen anclaje individual documentado. La respuesta es una transferencia válida a un objeto que el material nunca trata |
| 8 | VP/FN/FP/VN y denominadores | Fijar convención antes de contar; elegir denominador por métrica | Tablas, correcta y bien presentada | Los **conteos** (12/3/4/31). La aritmética sobre ellos es verificablemente exacta; su origen no es local. El propio documento declara este límite en P11 |
| 9 | ROC, umbral, AUC | Comparar umbral a umbral; dominancia | Tabla + conclusión | Los conteos, los umbrales y **las cifras de AUC, que además son inconsistentes con la propia tabla** (Fase 5.3). Es la respuesta con menor trazabilidad del documento |
| 10 | — | — | Declaración de imposibilidad | Nada que explicar: no hay respuesta |
| 11 | Epistemología del supuesto | Separar medido / supuesto / no disponible | Párrafo declarativo | Poco. Es el ítem con el rastro conductual más consistente en el material previo |

**Lectura de la Fase 4.** El documento no es homogéneo. Hay un bloque (P1, P2, P3, P7, P10, P11 y parcialmente P4) donde el conocimiento y el razonamiento tienen anclaje documental sólido en trabajo propio, y donde el aporte externo más plausible es de **forma**: ordenar, condensar y dar registro académico. Hay otro bloque (P5, P6, y los números de P8 y P9) donde el material local **no sostiene** el contenido, y donde no hay base para afirmar que el razonamiento fue reconstruido por el autor.

Una respuesta bien redactada no prueba comprensión; y haber usado IA para redactarla tampoco prueba ausencia de comprensión. Lo que sí se puede afirmar es lo anterior: dónde hay huella de proceso propio y dónde no la hay.

---

## FASE 5 — Revisión adversarial

### 5.1 La mayor parte del material conceptual es posterior al certamen

El certamen es del **28 de agosto de 2026**; el documento de respuestas fue creado el **29 de agosto** y modificado por última vez el **31 de agosto**. Los archivos con la evidencia conceptual más fuerte son posteriores:

| Material | Fecha | Relación con el certamen |
|---|---|---|
| Notebooks Hito 1 (Trabajo 1 y 2) | presentación del 14 de agosto según la guía del curso | **Anterior** |
| `_obsoleto_split_aleatorio/` (M3, M4) | 04-09-2026 (mtime) | Archivo posterior; su contenido corresponde a trabajo previo al Hito 2 |
| `INFORME_MODELO_FCD_P3.md` | 04-09-2026 | **Posterior** |
| `Fundamentos de ciencia de datos/Desafio/` | 12-09-2026 | **Posterior** |

Consecuencia: `08_ensemble.py` (diversidad de errores, P1), la matriz de confusión y el AUC del Desafío (P4, P8, P9) evidencian que el autor **comprende** esos conceptos, pero **no** que los comprendiera al rendir. La evidencia estrictamente anterior al certamen se reduce a los notebooks del Hito 1: partición temporal, leakage, jerarquía de modelos, CV, brecha train/test e importancia por reducción de impureza. Ese subconjunto sostiene P2, P3 y parte de P4 y P7 — no P1 en su forma medida, ni P8, ni P9.

No uso las fechas como argumento sobre integridad académica. Las señalo porque omitirlas convertiría este informe en el tipo de documento que dice más de lo que su evidencia permite: exactamente lo que `README_POR_QUE_OBSOLETO.md` le reprocha a su propia versión anterior.

### 5.2 Sí existe material de estudio, pero se construyó a partir del certamen

*(Sección corregida. La versión anterior afirmaba que no existía material de estudio. Ver la fe de erratas al inicio.)*

La guía de estudio (M0) cubre diez de las once preguntas con estructura de aprendizaje activo. Eso desmiente la afirmación original. Pero hay tres límites que no desaparecen:

1. **Dirección de la construcción.** La guía declara en su primer párrafo haberse construido *"tomando las preguntas del Certamen 2 como puntos de partida"*. Evidencia comprensión **del contenido evaluado**; no establece qué se comprendía al momento de rendir. Sus metadatos no permiten fecharla (`created` = 2013-12-23, valor de plantilla; sin autor; sin fecha de modificación).
2. **Faltan los eslabones intermedios.** Hay una guía y hay un documento de respuestas. No hay borradores, ni apuntes de clase, ni las respuestas propias a los ejercicios que la guía plantea. Los siete campos `Respuesta propia: ____` de su mini interrogación final están **en blanco**.
3. **La guía no explica todo el documento de respuestas.** En particular, no contiene las cifras de AUC de la P9 (ver 5.3).

Las dos afirmaciones que sí se sostienen, y conviene no mezclar:

- **Se puede reconstruir** un dominio conceptual sobre sobreajuste, validación, jerarquía de modelos, ensambles y métricas, con doble anclaje: trabajo aplicado propio (M1–M6) **y** material de estudio explícito (M0).
- **No se puede reconstruir** la secuencia temporal del estudio: qué se leyó, cuándo, y en qué orden respecto del certamen.

### 5.3 Contradicción numérica en la Pregunta 9

El documento afirma AUC ≈ 0,78 (Modelo 1) y ≈ 0,68 (Modelo 2). Calculando el AUC trapezoidal sobre los propios puntos de la tabla del documento, más (0,0) y (1,1):

- Modelo 1: puntos (0,03; 0,45), (0,14; 0,80), (0,34; 0,95) → **AUC ≈ 0,894**
- Modelo 2: puntos (0,06; 0,38), (0,23; 0,70), (0,51; 0,88) → **AUC ≈ 0,785**

Las cifras del documento no se derivan de su propia tabla. La conclusión (Modelo 1 mejor) es correcta y de hecho **demostrable por dominancia**: el Modelo 1 tiene mayor TPR y menor FPR en los tres umbrales, argumento más fuerte que cualquier AUC. Pero las dos cifras de AUC son un cuerpo extraño: no se calcularon a partir de lo que el documento muestra. Es la señal más clara de todo el expediente de contenido incorporado sin verificación.

### 5.4 Conceptos sin anclaje fuera de la guía

*(Sección corregida.)* Tras la aparición de M0, estos conceptos **sí** tienen material que los explica, pero **únicamente** en la guía de estudio — no en el código, los notebooks ni los informes del proyecto:

- **FPR** (P4, P8, P9): guía sección 5. Cero apariciones en código o notebooks.
- **Regresión polinomial / grado del polinomio** (P7): guía sección 8. Cero apariciones de "polinomi" en el código.
- **LLM, agente, PLN, detección de objetos** (P5, P6): guía secciones 9 y 10. Cero apariciones como contenido en el resto del repositorio.

La distinción importa: para el bloque de sobreajuste, validación y ensambles hay **doble anclaje** (guía + trabajo propio ejecutado). Para estos tres, el anclaje es **simple**: solo la guía.

### 5.5 Elaboración proporcionada al material, con una salvedad

*(Sección corregida.)* La Pregunta 8 produce una matriz completa con marginales y cinco métricas tabuladas. La aritmética es impecable y **ahora tiene respaldo**: la guía resuelve ese mismo ejercicio paso a paso, con los mismos conteos, y propone una variante con números distintos.

La salvedad es la circularidad ya señalada: si la guía se construyó desde el certamen, no puede usarse para explicar el origen de los conteos del certamen. Explica el dominio del procedimiento; no el origen del dato.

### 5.6 Evidencia de comprensión parcial o desplazada

En la P4 la respuesta clasifica la ganancia de pureza como "se usa durante la construcción de árboles de decisión", lo cual es correcto y más preciso que llamarla métrica. Pero no explicita por qué entonces cuenta como "usada en clasificación": deja implícita la distinción entre criterio de entrenamiento y métrica de evaluación, que es justamente la parte conceptualmente interesante. Es comprensión correcta, expresada sin desplegar el paso que la justifica.

### 5.7 Clasificación por pregunta

*(Clasificación actualizada tras la incorporación de la guía de estudio. Entre paréntesis, el nivel de la primera versión del informe.)*

| Pregunta | Nivel | Anclaje | Fundamento |
|---|---|---|---|
| P1 Ensambles y diversidad | **FUERTE** (=) | Doble | Guía §1 (tres termómetros, crédito, Galaxy Zoo) + `08_ensemble.py`, que lo operacionaliza midiendo `jaccard_error` |
| P2 Sobreajuste (definición) | **FUERTE** (=) | Doble | Guía §2 + brecha train/test usada como criterio en tres documentos, incluido material anterior al certamen |
| P3 Causas y consecuencias | **FUERTE** (=) | Doble | Guía §3 y §4 + las cinco afirmaciones con anclaje en cifras propias del proyecto |
| P4 Métricas de clasificación | **FUERTE** (era PARCIAL) | Doble | Guía §5 resuelve la taxonomía completa, FPR incluida y varianza excluida + reducción de impureza y `price_stats` en notebooks |
| P5 LLMs y agentes | **PARCIAL** (era INSUFICIENTE) | Simple | Guía §9, completa y con transferencia. Sin ningún otro anclaje en el repositorio |
| P6 Revoluciones en IA | **PARCIAL** (era INSUFICIENTE) | Simple | Guía §10, con la distinción causa / condición habilitante. Sin ningún otro anclaje |
| P7 Regresión polinomial | **FUERTE** (era PARCIAL) | Doble | Guía §8 (cinco chinches; *"¿Bajar el grado y Ridge hacen lo mismo?"*) + los cuatro remedios aplicados y medidos en el Proyecto 3 |
| P8 Matriz de confusión | **PARCIAL** (=) | Doble, con circularidad | Guía §6 con el procedimiento y los conteos exactos; aritmética verificada. Pero la guía deriva del certamen: la cifra es trazable, no derivada |
| P9 Curva ROC | **PARCIAL** (era INSUFICIENTE) | Simple, con contradicción | Guía §7 cubre umbral y dominancia. **Las cifras de AUC siguen sin explicación y contradicen la propia tabla** |
| P10 Punto base | No evaluable (=) | — | Sin respuesta. La no-respuesta sí tiene patrón antecedente documentado |
| P11 Comentarios y supuestos | **FUERTE** (=) | Proyecto | Patrón declarativo sistemático en material anterior al certamen |

**Resumen: 6 fuertes, 3 parciales, 0 insuficientes, 1 no evaluable** (antes: 4 / 3 / 3 / 1).

La columna "anclaje" es la que conviene mirar en una discusión académica. **Doble** significa que el concepto aparece tanto en material de estudio como en trabajo propio ejecutado y verificable. **Simple** significa que solo lo cubre la guía, cuya dirección de construcción está declarada y acotada en 5.2.

**Esta clasificación no determina si hubo o no una infracción académica. Mide una sola cosa: cuánto de cada respuesta puede reconstruirse desde los archivos de este directorio.**

---

## Conclusión

**¿Puede reconstruirse, a partir del material local, un proceso de comprensión que explique cómo se resolvieron las preguntas del certamen? — Parcialmente.**

Lo que el material **sí** sostiene:

1. **Existe material de estudio del certamen**, y su diseño es de comprensión y no de memorización: analogía cotidiana, traducción técnica, tres ejemplos por concepto, preguntas de reflexión sin respuesta dada, ejercicio de transferencia obligatorio, y una autoevaluación cuyo criterio es *"explicarlo sin usar la definición textual de esta guía"* e *"inventar un ejemplo cotidiano distinto"*. Cubre diez de las once preguntas.
2. Un dominio aplicado y documentado del bloque *sobreajuste / generalización / validación / selección de modelos / ensambles*, ejercido sobre un problema real con cifras propias, y sometido por el autor a autocorrección explícita (`README_POR_QUE_OBSOLETO.md`, "Fe de erratas").
3. Un patrón metodológico estable de **declarar supuestos y vacíos en vez de rellenarlos**, anterior al certamen, que reaparece literalmente en las preguntas 10 y 11.
4. Correspondencias no textuales sino de **transformación conceptual** entre principios aplicados a regresión inmobiliaria y preguntas formuladas sobre clasificación y teoría (Fase 3, doce casos).
5. **Doble anclaje** —guía de estudio más trabajo propio ejecutado— en seis de las once preguntas.

Lo que el material **no** sostiene:

6. **La secuencia temporal del estudio.** La guía declara haberse construido a partir de las preguntas del certamen y sus metadatos no permiten fecharla. Evidencia comprensión del contenido; no establece qué se comprendía el 28 de agosto.
7. **Los eslabones intermedios.** No hay borradores ni respuestas propias a los ejercicios que la guía plantea; sus siete campos `Respuesta propia: ____` están en blanco.
8. **El origen de los conteos de la pregunta 8.** La guía los contiene, pero deriva del certamen: la cifra queda trazable, no derivada.
9. **Las cifras de AUC de la pregunta 9.** No están en la tabla del certamen, no están en la guía, y **contradicen** la propia tabla que las acompaña (0,78 / 0,68 declarados frente a ≈ 0,894 / ≈ 0,785 calculados). La aparición de la guía no resuelve este punto: lo aísla, porque ahora se sabe que el material de estudio enseña el método correcto —dominancia— y omite justamente esos dos números.

La lectura honesta del expediente, tras la corrección, es que el sustrato de comprensión es **más amplio y mejor documentado** de lo que la primera versión de este informe sostuvo: hay material de estudio real, con diseño pedagógico orientado a la transferencia, y hay trabajo propio ejecutado y verificable que lo respalda en seis de las once preguntas. Sigue habiendo dos zonas que el material no explica —la secuencia temporal y las cifras de la pregunta 9—, y este informe no las disimula. Esa es la única razón por la que sus conclusiones positivas pueden tomarse en serio.
