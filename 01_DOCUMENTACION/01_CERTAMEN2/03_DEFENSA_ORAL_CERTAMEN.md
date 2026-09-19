# Defensa oral — Certamen 2, Fundamentos de Ciencia de Datos

**Qué es esto:** una guía para demostrar dominio académico hablando, no un texto para memorizar. Si una frase suena a recitado, cámbiala por tus palabras: lo que importa es que el razonamiento sea tuyo y sobreviva a una repregunta.

**Cómo usarla:** cada pregunta tiene un concepto central, una respuesta corta, un razonamiento de ~30 segundos, un ejemplo de tu propio proyecto, el error conceptual a evitar, y una repregunta probable con su respuesta.

**Tres reglas para la instancia oral:**
1. Si no sabes un dato, dilo. Tienes un historial documentado de hacerlo (`README_POR_QUE_OBSOLETO.md`, la propia pregunta 10 del certamen); ser consistente con eso vale más que improvisar.
2. Cuando puedas, aterriza el concepto en el Proyecto 3 (Melbourne 2016→2017) o en el desafío Galaxy Zoo. Un ejemplo con cifras propias es difícil de fingir.
3. Hay **dos puntos débiles reales** en el documento de respuestas: las cifras de AUC de la pregunta 9 y los conteos de las preguntas 8 y 9. Están señalados abajo. No los escondas: llévalos preparados.

---

## Pregunta 1 — Ensambles y diversidad

> *"Un modelo compuesto por varios modelos exactamente iguales, que predicen exactamente lo mismo, suele predecir mejor que cada modelo por separado."*

**Concepto central:** un ensamble funciona por **descorrelación de errores**, no por cantidad de modelos.

**Respuesta corta:** Falso.

**Razonamiento en 30 segundos:**
"Un ensamble mejora porque promedia. Y promediar solo reduce varianza si las cosas que promedio no están perfectamente correlacionadas. Si los modelos son exactamente iguales, sus errores caen en las mismas filas: el promedio devuelve exactamente el mismo número que uno solo. No es peor, es idéntico. Y el enunciado decía 'suele predecir mejor', así que es falso. Lo que hace útil a un ensamble es la diversidad, y por eso bagging cambia la muestra, Random Forest además cambia las variables candidatas en cada corte, y boosting entrena cada modelo sobre los errores del anterior."

**Ejemplo propio:**
"En el desafío de Galaxy Zoo, antes de combinar dos modelos medí dónde fallaba cada uno: la fracción de filas en que fallaban ambos sobre la fracción en que fallaba alguno. Si ese cociente se acerca a 1, los modelos fallan en el mismo lugar y combinarlos no aporta nada. Ese número es exactamente lo que esta pregunta pone en su caso extremo."

**Error conceptual a evitar:**
Leer "varios modelos" y responder con la regla general ("los ensambles mejoran"). El calificativo *"exactamente iguales"* es lo que cambia todo: anula la condición que hace útil al ensamble.

**Repregunta probable:** *"¿Y entonces conviene siempre maximizar la diversidad?"*
**Respuesta:** "No. Puedo conseguir diversidad enorme metiendo modelos malos, y eso empeora el ensamble. Lo que se necesita es diversidad **entre modelos que individualmente sean fuertes**. Es un compromiso: fuerza individual y desacuerdo en los errores."

---

## Pregunta 2 — Sobreajuste y generalización

> *"El sobreajuste ocurre cuando el modelo predice correctamente en entrenamiento pero no generaliza a datos nuevos."*

**Concepto central:** sobreajuste es una **brecha entre dos mediciones**, no un valor alto ni un valor bajo.

**Respuesta corta:** Verdadero.

**Razonamiento en 30 segundos:**
"El modelo tiene capacidad suficiente para ajustar no solo la señal sino también el ruido del conjunto con que lo entrené. El ruido, por definición, no se repite en datos nuevos. Entonces aparece el patrón característico: excelente adentro, mediocre afuera. Lo importante es que el sobreajuste no se mide con un número, se mide comparando dos: desempeño en entrenamiento contra desempeño en datos que el modelo no vio."

**Ejemplo propio:**
"En el Proyecto 3 el Random Forest tenía R² de 0,946 entrenando con 2016 y 0,715 prediciendo 2017: brecha de +0,231. El árbol simple tenía brecha +0,145. Ese fue un argumento en contra del Random Forest, aunque su R² de entrenamiento se viera espectacular. Y en la réplica en DashAI el árbol de decisión sin podar llegó a R² train = 1,000 con R² test = 0,468: memorización pura."

**Error conceptual a evitar:**
Confundir **error alto** con **sobreajuste**. Un modelo malo en train y peor en test está *subajustado*. El sobreajuste exige la conjunción: bueno adentro, malo afuera.

**Repregunta probable:** *"¿Toda caída entre train y test es sobreajuste?"*
**Respuesta:** "No, y esto lo tuve que separar en mi propio proyecto. Entre 2016 y 2017 la distribución cambió: el 29 % de las propiedades de 2017 está en suburbios que no existían en 2016. Parte de la caída es del modelo y parte es del problema. Para separarlos miro si un baseline trivial —predecir la mediana de 2016— también empeora. Si el baseline también cae, esa parte de la brecha no es sobreajuste, es cambio de distribución."

---

## Pregunta 3 — Causas y consecuencias del sobreajuste

**Concepto central:** el sobreajuste tiene causas (complejidad), diagnóstico (validación), consecuencias (producción) y alcance (cualquier tarea supervisada).

**Respuesta corta:** Son correctas las afirmaciones sobre complejidad, validación cruzada, fallas en producción y presencia tanto en clasificación como en regresión. Es **incorrecta** la que dice que aumentar el número de atributos evita el sobreajuste.

**Razonamiento en 30 segundos:**
"Las cuatro correctas van por caminos distintos. Más complejidad significa más capacidad para ajustar ruido. La validación cruzada no arregla el sobreajuste, lo *estima*: cada fold evalúa sobre datos que ese modelo no vio. En producción el problema es que los datos nuevos no son una muestra del histórico, así que un modelo que memorizó el histórico no tiene por qué sobrevivir. Y el mecanismo del sobreajuste es ajustar parámetros con datos finitos: nada de eso depende de si la salida es una clase o un número. La falsa es la de los atributos, y es la más tentadora."

**Ejemplo propio:**
"Descarté `Suburb` justamente por eso: 311 categorías le daban al modelo 311 maneras de memorizar barrios en lugar de aprender ubicación. Usé `Regionname`, con 8 categorías, más `Distance` y las coordenadas, que son continuas y existen también para barrios nuevos. Y `Bedroom2` quedó con importancia por permutación de +0,0009: agregaba dimensión y cero señal."

**Error conceptual a evitar:**
Confundir **más filas** con **más columnas**. Más observaciones sí ayudan: suben la evidencia por parámetro. Más atributos hacen lo contrario: suben los parámetros sin subir la evidencia.

**Repregunta probable:** *"Si la validación cruzada detecta el sobreajuste, ¿por qué después entrena con todos los datos?"*
**Respuesta:** "Porque son dos cosas distintas. La CV la uso para **decidir**: comparar modelos y estimar cuánto van a generalizar. Una vez decidido, entreno con todos los datos disponibles porque más datos dan mejor ajuste. Lo que nunca hago es usar el test para decidir. En el Proyecto 3 elegí el modelo por CV 5-fold dentro de 2016 y solo después toqué 2017, una sola vez. De hecho el ranking de la CV coincidió con el ranking del test: esa coincidencia es la señal de que la selección fue honesta."

---

## Pregunta 4 — Métricas de clasificación

> AUC, varianza, ganancia de pureza, FPR, exactitud: ¿cuáles se usan en clasificación?

**Concepto central:** distinguir **métrica de evaluación**, **criterio interno de entrenamiento** y **estadístico descriptivo**.

**Respuesta corta:** AUC, ganancia de pureza, FPR y exactitud. La varianza no.

**Razonamiento en 30 segundos:**
"Clasifico cada término por qué objeto describe. La exactitud, la FPR y el AUC describen un clasificador: proporción de aciertos, proporción de negativos reales que marqué mal, y calidad del ordenamiento sobre todos los umbrales. La ganancia de pureza describe un corte dentro de un árbol: es lo que el árbol optimiza al elegir dónde partir, y solo tiene sentido si hay clases. La varianza es el único que describe una **variable**, no un modelo: existe igual aunque no haya nada que clasificar."

**Ejemplo propio:**
"La varianza la calculé en el EDA sobre el precio de las propiedades, junto con media, mediana e IQR: era descripción de una distribución, no medida de acierto. Y la ganancia de pureza la usé sin nombrarla así: la importancia de variables del Random Forest del Hito 1 es exactamente reducción de impureza acumulada."

**Error conceptual a evitar:**
Incluir la varianza porque suena estadística y porque aparece en la descomposición sesgo–varianza. Una cosa es un concepto que se usa al analizar modelos; otra es una métrica que mide el rendimiento de un clasificador.

**Repregunta probable:** *"¿La exactitud sirve siempre?"*
**Respuesta:** "No, y tengo el caso a mano. En Galaxy Zoo la clase 0 era el 9,6 % de los datos. Un modelo que nunca predijera esa clase tendría exactitud alta y sería inútil para lo que interesaba. Por eso la métrica oficial ahí era F1-macro, que promedia el F1 de cada clase y no deja que la clase mayoritaria tape el resultado."

---

## Pregunta 5 — LLMs y agentes

**Concepto central:** un LLM es un **modelo**; un agente es un **sistema** construido alrededor de un modelo.

**Respuesta corta:** la correcta es la que dice que un agente puede usar herramientas, almacenar conocimiento y ejecutar acciones, mientras un LLM se orienta al procesamiento y generación de texto.

**Razonamiento en 30 segundos:**
"Las descarto por eliminación. Un LLM no garantiza hechos recientes: aprende de un corpus con fecha de corte, y para saber algo posterior necesita que alguien se lo pase como entrada, con búsqueda o recuperación. Los agentes sí colaboran, con personas y entre ellos: es un patrón estándar. Y entrenar un modelo de esa escala sí requiere volúmenes enormes de datos y cómputo, es prácticamente su definición. Queda la que separa funciones, y esa se verifica sola: lo que convierte un modelo en agente es el bucle de acción —invocar una herramienta, ver el resultado, decidir el paso siguiente— más algún estado que persista."

**Ejemplo propio:**
"En mi propio proyecto definí un agente con un rol acotado y una regla dura: cualquier cifra tenía que salir de `anclaje.json` o de una salida ejecutada del notebook, nunca de memoria. Eso es justamente la diferencia: el modelo genera texto; el sistema que lo rodea le da herramientas, una fuente de verdad externa y restricciones sobre qué puede afirmar."

**Error conceptual a evitar:**
Tratar LLM y agente como sinónimos porque a ambos se les habla por chat. La prueba es si el sistema puede **actuar y observar el resultado de su acción**.

**Repregunta probable:** *"Si un LLM le responde sobre algo que pasó esta semana, ¿qué significa?"*
**Respuesta:** "Que o el hecho estaba en su entrenamiento, o alguien se lo entregó como contexto: una búsqueda, un documento, un sistema de recuperación. No es conocimiento propio del modelo."

---

## Pregunta 6 — Revoluciones recientes en IA

**Concepto central:** distinguir **causa** de **condición habilitante**.

**Respuesta corta:** procesamiento del lenguaje natural y detección de objetos en imágenes.

**Razonamiento en 30 segundos:**
"Me pregunto de cada ítem qué lo hizo avanzar. En lenguaje natural el salto vino de arquitecturas neuronales: primero redes recurrentes, después transformers. En detección de objetos vino de redes convolucionales profundas. La computación en la nube es capacidad de cómputo alquilable: permite entrenar esos modelos, pero no es una técnica de IA y su existencia no depende de las redes neuronales. Las bases de datos relacionales son de los años 70: ni recientes ni neuronales."

**Error conceptual a evitar:**
Incluir la nube porque "sin ella no habría IA moderna". El enunciado dice revoluciones **impulsadas por** redes neuronales. La flecha va al revés: la nube impulsa a las redes. Con ese criterio laxo habría que incluir también los semiconductores.

**Repregunta probable:** *"¿Por qué habla de 'revolución' y no simplemente de mejora?"*
**Respuesta:** "Porque cambió el tipo de tarea resoluble, no solo el porcentaje de acierto. En lenguaje se pasó de sistemas de reglas y estadística de n-gramas a modelos que resuelven tareas para las que nadie los programó explícitamente. Eso es un cambio de categoría, no un incremento."

---

## Pregunta 7 — Regresión polinomial y sobreajuste

> Curva polinomial ajustada a cinco árboles: ¿es correcto el ajuste?

**Concepto central:** error de entrenamiento cero no es evidencia de nada cuando el modelo tiene capacidad suficiente para interpolar.

**Respuesta corta:** no es un buen ajuste. Bajar el grado, medir más árboles, comparar grados con validación cruzada y, si hace falta, regularizar con Ridge o Lasso.

**Razonamiento en 30 segundos:**
"Con cinco puntos siempre existe un polinomio de grado 4 que pasa exactamente por todos. Así que tocar los cinco puntos no prueba nada: cualquier conjunto de cinco puntos se puede interpolar. Lo que delata el problema son las oscilaciones entre puntos, donde no hay datos que restrinjan la curva. Y contrasto con el fenómeno: la relación entre las dimensiones de un árbol y su volumen debería ser suave y creciente. Una curva que sube y baja entre observaciones contradice el fenómeno en vez de describirlo. Está capturando ruido de medición de cinco árboles."

**Las cuatro mejoras, cada una por su mecanismo:**
- Bajar el grado → reduce capacidad.
- Medir más árboles → aumenta la evidencia que restringe la curva.
- Validación cruzada entre grados → permite elegir sin autoengañarse con el error de ajuste.
- Ridge o Lasso → penalizan coeficientes grandes, que son la firma matemática de las oscilaciones.

**Ejemplo propio:**
"Estos cuatro mecanismos son los que usé en el Proyecto 3. Elegí modelo por CV dentro de 2016 sin mirar 2017. El modelo final lleva `l2_regularization`. Y marqué como no confiables las regiones con menos de 60 observaciones: Eastern Victoria tenía 53 casos y un error porcentual de 59 %, contra 14–17 % en las zonas con miles de observaciones. Ese es el mismo problema que tiene un ajuste con n = 5, tres órdenes de magnitud más arriba."

**Error conceptual a evitar:**
Creer que el ajuste que pasa por todos los puntos es el mejor. Y la trampa secundaria: pensar que basta bajar el grado. Con cinco observaciones el problema de fondo es la falta de datos, y ningún grado lo resuelve del todo.

**Repregunta probable:** *"¿Ridge le baja el grado al polinomio?"*
**Respuesta:** "No. Ridge deja los mismos términos pero encoge sus coeficientes, así que la curva sale más suave. Bajar el grado elimina términos; regularizar los amortigua. Son dos formas de reducir la capacidad efectiva, no la misma."

**Repregunta probable 2:** *"¿Qué grado elegiría?"*
**Respuesta:** "No lo elijo a ojo. Ajusto grado 1, 2 y 3 y comparo su error en validación cruzada; con cinco puntos sería leave-one-out. Me quedo con el grado más bajo cuyo error de validación no sea materialmente peor que el del mejor."

---

## Pregunta 8 — Matriz de confusión y métricas

**Concepto central:** cada métrica es un cociente, y lo que la distingue es **el denominador**.

**Respuesta corta:** con círculos como clase positiva y el lado izquierdo como predicción positiva: VP 12, FN 3, FP 4, VN 31. Exactitud 86 %, precisión 75 %, sensibilidad 80 %, FPR 11,4 %, especificidad 88,6 %.

**Razonamiento en 30 segundos:**
"Primero declaro la convención, porque sin eso 'falso positivo' no significa nada: círculos son positivos y el lado izquierdo de la línea predice positivo. Con eso, cada punto cae en una de cuatro casillas. Cuento y verifico las marginales: 15 círculos, 35 triángulos, 50 en total. Después cada métrica es elegir bien el denominador. Exactitud: aciertos sobre el total, 43 de 50, 86 %. Precisión: de lo que **dije** círculo, cuánto acerté, 12 de 16, 75 %. Sensibilidad: de lo que **era** círculo, cuánto encontré, 12 de 15, 80 %. Y FPR: de los 35 triángulos, cuántos marqué mal, 4, o sea 11,4 %."

**Lectura en lenguaje del problema:**
"El modelo es conservador con los círculos: falla más al declararlos que al encontrarlos."

**Error conceptual a evitar:**
Confundir precisión, exactitud y sensibilidad —las tres suenan a "acertar"—. Y en particular: **la FPR no es 1 menos la precisión**. La FPR divide por los 35 negativos reales; la precisión divide por las 16 predicciones positivas. Universos distintos.

**Punto que debes llevar preparado (honestidad):**
Los conteos 12/3/4/31 salen de leer la figura del certamen. La aritmética sobre ellos es exacta y verificable, pero si el profesor cuenta distinto en la figura, el procedimiento es el mismo y los números se recalculan. Tú ya declaraste este supuesto en la pregunta 11 del propio certamen; mantén esa línea.

**Repregunta probable:** *"Si mueve la línea a la derecha, ¿qué pasa con TPR y FPR?"*
**Respuesta:** "Suben las dos. Al declarar positivos más casos capturo más círculos reales, pero también marco más triángulos. No se puede subir una sin subir la otra: ese compromiso es exactamente lo que dibuja la curva ROC."

**Repregunta probable 2:** *"¿Por qué precisión y sensibilidad dan distinto si el numerador es el mismo?"*
**Respuesta:** "Porque el denominador cambia de universo. Tengo 16 predicciones positivas y 15 positivos reales; los cocientes solo coincidirían si FP y FN fueran iguales."

---

## Pregunta 9 — Curva ROC y comparación de modelos

**Concepto central:** un modelo no es un punto en el plano ROC, es una **curva**; y la comparación limpia es la dominancia.

**Respuesta corta:** el Modelo 1.

**Razonamiento en 30 segundos:**
"Cada fila de la tabla es el **mismo** modelo a un umbral distinto. Bajar el umbral mueve el punto arriba y a la derecha; subirlo, abajo y a la izquierda. Así que no puedo comparar filas sueltas de modelos distintos: son regímenes distintos. Comparo umbral con umbral. Umbral bajo: Modelo 1 da 0,95 de TPR con 0,34 de FPR; Modelo 2 da 0,88 con 0,51. Umbral medio: 0,80 con 0,14 contra 0,70 con 0,23. Umbral alto: 0,45 con 0,03 contra 0,38 con 0,06. En los tres el Modelo 1 tiene **más TPR y menos FPR**. Eso es dominancia: no hay compromiso que negociar, su curva está enteramente por encima y por tanto su área también es mayor."

**Por qué el argumento de dominancia es mejor que citar un AUC:**
No depende de cómo se interpole entre puntos ni de si tomé bien la cifra. Con tres puntos dominados, la conclusión es incontestable.

**Punto que debes llevar preparado (honestidad — el más importante de toda la defensa):**
El documento entregado afirma AUC ≈ 0,78 para el Modelo 1 y ≈ 0,68 para el Modelo 2. **Esas cifras no se derivan de la tabla del propio documento.** Calculando el área por trapecios sobre los puntos de la tabla, más (0,0) y (1,1), da ≈ 0,894 y ≈ 0,785. La conclusión no cambia, pero las cifras sí.

Si el profesor lo pregunta, la respuesta que corresponde es: *"La conclusión la sostengo por dominancia, que es verificable en la tabla. Las dos cifras de AUC que aparecen en mi documento no las puedo reproducir a partir de esa tabla; calculándolas por trapecios dan alrededor de 0,89 y 0,79."* No intentes defender los números. Ofrece el cálculo correcto: eso demuestra que entiendes qué es el AUC, que es lo que se está evaluando.

**Error conceptual a evitar:**
Elegir el modelo por el punto de mayor TPR. Con ese criterio ganaría un clasificador que declara todo positivo: TPR 1, FPR 1, inútil.

**Repregunta probable:** *"¿Puede un modelo con mayor AUC ser peor en la práctica?"*
**Respuesta:** "Sí. El AUC promedia el desempeño sobre todos los umbrales, incluidos los que yo nunca voy a usar. Si mi punto de operación está en una zona donde el otro modelo es mejor, o si un falso positivo me cuesta mucho más que un falso negativo, el AUC no es el criterio adecuado."

**Repregunta probable 2:** *"¿Qué significa AUC = 0,5?"*
**Respuesta:** "Que el modelo ordena al azar: la probabilidad de que le asigne mayor puntaje a un positivo que a un negativo es la de una moneda."

---

## Pregunta 10 — Punto base

**Concepto central:** declarar el vacío en vez de rellenarlo.

**Respuesta corta:** no la respondí porque dependía de una figura que no tenía a la vista.

**Razonamiento en 30 segundos:**
"Elegir una alternativa sin ver las opciones habría sido adivinar y presentarlo como respuesta. Prefiero declarar qué me faltaba. Es la misma regla que aplico en el trabajo: en el notebook del Hito 1 cada celda tiene una rama que imprime 'NO VERIFICABLE CON LOS DATOS DISPONIBLES' cuando el dato no está, en vez de producir un número plausible."

**Repregunta probable:** *"¿Y si le muestro ahora la figura?"*
**Respuesta:** Pídele verla y respóndela ahí mismo. Es la mejor demostración posible de que el vacío era de información, no de comprensión. Si el concepto de "punto base" en esa figura es el baseline —el modelo trivial contra el cual se compara todo lo demás—, tienes el ejemplo listo: *"en mi proyecto el baseline era predecir la mediana de 2016, con MAE de 431.649 AUD; cualquier modelo tenía que superarlo ampliamente para justificar su existencia."*

---

## Pregunta 11 — Comentarios y supuestos

**Concepto central:** separar lo medido, lo supuesto y lo no disponible.

**Respuesta corta:** declaré los supuestos de lectura de figuras y advertí que los conteos de las preguntas 8 y 9 dependían de mi lectura visual.

**Razonamiento en 30 segundos:**
"Una respuesta numérica sin supuesto declarado es irreproducible. En la pregunta 8, si en vez de círculos tomo triángulos como clase positiva, la exactitud sigue siendo 86 % pero la precisión salta a 91 % y la FPR a 20 %. O sea que el supuesto no es un detalle: determina cuatro de las cinco cifras. Por eso lo puse por escrito antes de calcular, para que el procedimiento pueda verificarse aunque alguien discrepe del supuesto."

**Ejemplo propio:**
"Es la misma práctica del informe del proyecto. Cuando repliqué el modelamiento en DashAI dejé escrito que los hiperparámetros eran los de fábrica y que por eso las cifras no iban a coincidir con las del pipeline local, pero que servían para verificar el ordenamiento. Y en la sección de diagnóstico separé explícitamente qué parte de la brecha era sobreajuste y qué parte era cambio de distribución, en vez de atribuirla toda a una causa."

**Error conceptual a evitar:**
Creer que declarar supuestos debilita la respuesta. Es al revés: la vuelve auditable.

**Repregunta probable:** *"¿No es una forma de cubrirse por si el resultado está mal?"*
**Respuesta:** "Es lo contrario: hace más fácil encontrarme el error. Si dejo escrito de dónde salió cada número, cualquiera puede revisar el paso donde me equivoqué. Lo hice también en mi proyecto: hay una carpeta marcada como obsoleta con un README donde declaro que mis propias cifras anteriores no habían sido calculadas y las invalido, y el informe final abre con una fe de erratas. Declarar supuestos y declarar errores es la misma disciplina."

---

## Cierre: si te preguntan directamente por el uso de IA

Esto no es un guion. Es lo que el expediente permite sostener, para que no digas ni más ni menos que eso:

**Lo que puedes afirmar con respaldo documental:**
- **Existe una guía de estudio** que cubre diez de las once preguntas, con diseño de comprensión y no de memorización: analogía cotidiana, traducción técnica, tres ejemplos por concepto, preguntas de reflexión sin respuesta dada, y un ejercicio de transferencia obligatorio ("cámbiame el ejemplo"). Su criterio de cierre es *explicarlo sin usar la definición textual de la guía* e *inventar un ejemplo cotidiano distinto*. Si el profesor te pide justamente eso en la oral, el material estaba construido para esa prueba.
- Trabajo propio, ejecutado y verificable, sobre sobreajuste, validación cruzada, jerarquía de modelos, ensambles y métricas, con cifras reproducibles desde código (`modelamiento_temporal.py`, `bootstrap_comparacion.py`, `INFORME_MODELO_FCD_P3.md`).
- **Doble anclaje** —guía más trabajo propio— en seis de las once preguntas.
- Una práctica documentada de autocorrección: invalidaste por escrito tus propias cifras anteriores cuando descubriste que no habían sido calculadas.
- Una práctica documentada de declarar vacíos en lugar de rellenarlos, anterior al certamen, que reaparece en las preguntas 10 y 11.

**Lo que no puedes afirmar, y conviene no intentar:**
- **Que la guía pruebe qué entendías el 28 de agosto.** Ella misma dice haberse construido *"tomando las preguntas del Certamen 2 como puntos de partida"*, y sus metadatos no permiten fecharla. Preséntala como lo que es: material de comprensión del contenido, no prueba de un estado mental en una fecha.
- Que los conteos de la pregunta 8 salgan de la guía. Están ahí, pero la guía deriva del certamen: es trazable, no derivado. Lo que sí dominas es el procedimiento, y eso se demuestra resolviendo una matriz con números nuevos delante del profesor.
- Que las cifras de AUC de la pregunta 9 sean tuyas y correctas. No son derivables de tu propia tabla **ni aparecen en la guía** — que, de hecho, enseña el método correcto: la dominancia.

Si te preguntan por ese último punto, la respuesta honesta —"ese número no lo puedo reproducir, y el cálculo correcto da otro; la conclusión la sostengo por dominancia"— demuestra más comprensión que cualquier defensa del número. Y es coherente con todo lo demás que has escrito.

---

## Apéndice: cómo usar la guía de estudio para practicar

`fuentes\Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` trae una **mini interrogación integradora** de siete preguntas con campos `Respuesta propia: ____` **en blanco**. Complétalos por escrito antes de la oral. Dos razones:

1. Es el ejercicio de recuperación activa que la propia guía define como prueba de comprensión, y es el formato más cercano a lo que el profesor va a hacerte.
2. Deja rastro de tu proceso: pasas de tener un material que *podrías* haber trabajado a tener uno que *trabajaste*.

Las siete preguntas, para que las tengas a mano:

| # | Pregunta | Concepto |
|---|---|---|
| 1 | Un modelo obtiene 0,92 en train y 0,90 en test. Otro 0,99 y 0,62. ¿Qué observas antes de elegir? | P2 |
| 2 | Dos modelos tienen F1 parecido. ¿Qué información adicional buscarías antes de combinarlos en un ensamble? | P1 |
| 3 | ¿Por qué usar repetidamente el test para elegir hiperparámetros termina contaminándolo? | P3 |
| 4 | En 200 transacciones hay 20 fraudes. Detectas 16 y bloqueas por error 18 compras legítimas. Construye la matriz y explica precision y recall. | P8 |
| 5 | Si bajas el umbral de fraude, ¿qué esperas que ocurra con TPR y FPR? | P9 |
| 6 | Una curva de grado 8 pasa por nueve observaciones. ¿Qué evidencia falta para afirmar que es buena? | P7 |
| 7 | ¿Cuál es la diferencia entre un modelo que redacta una acción y un sistema que realmente la ejecuta? | P5 |

La 4 es la más valiosa para practicar: son números distintos a los del certamen (VP=16, FN=4, FP=18, VN=162), así que resolverla demuestra el procedimiento y no el recuerdo.
