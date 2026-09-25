# 06Clase Fundamentos en Ciencia de Datos 31 de julio.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:31:09
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:00:09]** Ya, hoy día vamos a empezar a ver lo que es aprendizaje automático, que es como la base

**[0:00:15]** de la inteligencia artificial que tenemos hoy en día. Vamos a ver un par de clases donde

**[0:00:22]** vamos a pasar los fundamentos, que es como la base sobre la cual se construye cualquier

**[0:00:29]** modelo de inteligencia artificial hoy día. Y lo vamos a ver de una forma muy simple

**[0:00:34]** con un modelo muy simple, pero que todos los conceptos que vamos a ver van a ser,

**[0:00:39]** son directamente aplicables a la inteligencia artificial que tenemos hoy. Entonces vamos a

**[0:00:49]** partir hableando de regresión, que yo creo que algunos de ustedes ya han visto lo que es

**[0:00:53]** regresión, pero siempre puedo recordarlo porque hay conceptos fundamentales que se aplican en

**[0:01:01]** regresión y después se aplican en clasificación y después se aplican así sucesivamente a

**[0:01:05]** distintos modelos de inteligencia artificial. Entonces como siempre partimos viendo el ciclo de la

**[0:01:13]** ciencia de datos y nosotros dijimos que partíamos de una pregunta o requerimiento,

**[0:01:18]** después recolectábamos los datos, después hacemos la limpieza, la exploración, el modelamiento,

**[0:01:26]** vemos qué es lo que obtienen nuestros modelos, los comunicamos y pues ponemos en marcha.

**[0:01:30]** Hoy día lo que vamos a ver es el modelamiento. Recuerden siempre que puede ser que yo estuvieran

**[0:01:35]** haciendo el modelamiento y me de cuenta de que hay algo que no funciona, que no me calza bien,

**[0:01:40]** y entonces tengo que volver atrás a la fase exploración y seguramente hay algún dato que

**[0:01:45]** fue mal limpiado o mal recopilado y entonces tengo que volver hacia atrás. Hoy día vamos a ver

**[0:01:53]** aprendizaje automático que es machine learning, gran parte, si no, no sé, yo diría que un 90,

**[0:02:01]** 95% de la inteligencia artificial que tenemos hoy día se debe a este subconjunto de algoritmos

**[0:02:08]** que son de aprendizaje automático y vamos a ver qué es lo que significa el aprendizaje automático.

**[0:02:14]** Después de eso vamos a empezar con regresión, vamos a ir viendo lo que es generalización y

**[0:02:19]** cómo hacer que nuestro algoritmo nos aprenda los datos de memoria y sea capaz de generalizar a otros

**[0:02:25]** datos que no han visto antes. Para el final terminar viendo la técnica más importante yo creo de quizás

**[0:02:32]** toda la inteligencia artificial que es la variación cruzada. Y si es que aparece este símbolo en

**[0:02:38]** las slides quiere decir que voy a entrar un poco en las matemáticas y que es importante que presten

**[0:02:44]** atención a las matemáticas si no lo logran entender porque no vienen de un background

**[0:02:48]** matemático no es tan terrible ok, lo importante es que aprendan la parte más conceptual del curso.

**[0:02:54]** Entonces ¿qué es el aprendizaje automático? El aprendizaje automático es el estudio de

**[0:03:01]** algoritmos que mejoran su rendimiento en alguna tarea con la experiencia y entonces cualquier

**[0:03:08]** tarea de aprendizaje bien definida tiene estos tres conceptos, el rendimiento, la tarea y la

**[0:03:17]** experiencia. Entonces si ustedes piensan por ejemplo en si yo quiero clasificar entre perro y gato por

**[0:03:26]** decir algo tengo que de alguna forma medir que también lo está haciendo el algoritmo tengo que

**[0:03:32]** de alguna forma decir medir el rendimiento del algoritmo que también lo está haciendo si

**[0:03:37]** yo estoy pensando en por ejemplo mostrarle a usted las películas de netflix que más le

**[0:03:43]** va a gustar de alguna forma tengo que medir si es que lo estoy haciendo bien o mal ok. Está asociado

**[0:03:51]** una tarea que puede ser por ejemplo clasificación y los algoritmos tienen que aprender con la

**[0:03:56]** experiencia ok. Entonces digamos que esté en nuestra máquina que nosotros le queremos enseñar

**[0:04:02]** generalmente lo que hace el aprendizaje automático es que la experiencia se la damos desde los

**[0:04:07]** datos entonces le entregamos muchos datos y a partir de estos datos la máquina es capaz

**[0:04:14]** de aprender a realizar alguna tarea en particular después de eso una vez que ya aprendió yo le

**[0:04:20]** puedo hacer una pregunta y la máquina me esperaría que me respondiera fíjense que hay algo muy importante

**[0:04:26]** acá la máquina aprende desde los datos si es que hay datos que yo no tengo incluido o que yo no

**[0:04:31]** le entrega la máquina la máquina no aprender esos datos por ejemplo si yo estoy clasificando

**[0:04:37]** entre perro conijo y ratón y le entre lo le entrego puro perro y conejo no aprender a

**[0:04:42]** instigir un ratón ok se le ocurre por ejemplo si que estamos hablando de una LLM ¿sabes lo que una

**[0:04:51]** LLM? ChatGPT no es una LLM no que PT es la LLM. Ah claro la marca claro. ChatGPT no ChatGPT es un

**[0:05:04]** sistema multiagente que lo vamos a ver en la última clase es un sistema multiagente pero

**[0:05:08]** que por detrás tiene una LLM ¿Qué una LLM que me puede explicar? O sea sé que la sigla

**[0:05:16]** significa modelo de lenguaje large language model que al final es como es que depredís el toque

**[0:05:22]** en siguiente a partir del a partir del contexto anterior eso es como la idea. Claro. Entonces muy bien

**[0:05:27]** entonces una LLM viene como decía Germán de la es la sigla de large language model y lo que

**[0:05:35]** hace esta LLM es que predice la siguiente palabra un modelo muy grande de lenguaje entonces

**[0:05:44]** large language model es como modelo grande de lenguaje es un modelo muy grande de lenguaje que lo

**[0:05:52]** que hace es que predice la siguiente palabra entonces yo le digo hola cómo estás y con ese texto predice

**[0:05:59]** la siguiente palabra que la siguiente palabra sería por ejemplo muy y después toma ese muy y predice

**[0:06:04]** la siguiente palabra dice bien y después toma ese bien y predice la siguiente junto con todo

**[0:06:09]** el resto de las palabras dice y tú y así sucesivamente solamente predice la siguiente palabra

**[0:06:13]** un modelo como lo que tenemos hoy en día los modelos de los grandes modelos de lenguaje que

**[0:06:20]** tenemos hoy en día como los que usan yemina o gpt o todo esto son modelos que fueron entrenados

**[0:06:27]** básicamente con todo el texto que pudieron sacar de internet entonces el aprendizaje la

**[0:06:34]** experiencia voy atrás la experiencia es viene desde todo el texto que nosotros como humanidad hemos

**[0:06:44]** generado cuál es la tarea decir la siguiente palabra el toque no sé escribir reaktar leer

**[0:07:00]** es la tarea es predecir la siguiente palabra solamente eso lo único que quiere que el modelo

**[0:07:08]** hace que suena súper simple es predecir una palabra una a la vez ya y como yo mío el

**[0:07:15]** rendimiento al insuburrador con el titulado de usuario me imagino por qué uno le pudo poner

**[0:07:22]** un dedito para arriba abajo no sé me imagino me imagino que respuestas como que hay en tiempo

**[0:07:31]** de respuesta no no es tiempo yo quiero saber el tiempo no está casi se fijan el rendimiento está

**[0:07:37]** pensando en que también lo hace el algoritmo en la tarea que le estoy pidiendo no estoy

**[0:07:43]** hablando de tiempo acá que cuál cuál sería la calidad de respuesta la calidad de respuesta

**[0:07:50]** pero estoy solamente prediciendo la siguiente palabra entonces tengo una palabra como mi hora

**[0:07:54]** calidad de esa palabra que el de correlación tiene con lo que viene anterior conexiones no mira

**[0:08:06]** yo voy a explicar lo que nace lo que nace que yo le paso una oración completa por ejemplo hola

**[0:08:12]** mi nombre Guillermo y estoy muy feliz y le digo predice la siguiente palabra desde hola soy

**[0:08:19]** Guillermo y entonces el el lm tiene que predecir estoy si es que no la punto estoy entonces no

**[0:08:28]** lo está prediciendo bien y entonces pero soy capaz de esa forma de medir su rendimiento que

**[0:08:34]** también lo está haciendo imagínense que yo digo hola mi nombre Guillermo y en vez de decir

**[0:08:41]** estoy dice y perro entonces no le apuntó la palabra estoy y entonces no lo hizo bien

**[0:08:49]** pero eso eso como o sea porque claro en ese ejemplo quizá es fácil identificarlo pero

**[0:08:56]** hay algún indicador o hay alguna medida específica que que mida valga la redundancia

**[0:09:05]** el rendimiento si hay una forma de medirlo y es básicamente tú puedes medir cuánto

**[0:09:12]** le va apuntando a las palabras y tú le puedes entre comillas lo vamos a ver la próxima clase

**[0:09:16]** porque eso es esto que estamos hablando un problema clasificación y hoy día vamos a hablar

**[0:09:19]** de regresión pero en clasificación tú lo que hace es que tienes una función de costo que

**[0:09:26]** te dice que también la puntaste a las palabras lo vamos a ver la próxima la le puedo adelantar

**[0:09:37]** en particular el GPT lo que usa es la entropía cruzada esa es como la la la es la

**[0:09:45]** gran función de costo de que uno utiliza el clasificar christian

**[0:09:55]** entonces cuando habla de predecir la siguiente palabra se refiere a que aquí

**[0:10:04]** decir la siguiente palabra como del usuario de la misma inserción que quiere hablar entre

**[0:10:10]** comillas como esta que está escribiendo el texto la inteligencia artificial va a escribir una

**[0:10:18]** palabra y tú lo comparas con la palabra que debería seguir de acuerdo a la oración que tú le pasaste

**[0:10:29]** ya pero uno le hace una pregunta normalmente uno quiere como que diga lo mismo

**[0:10:37]** claro lo que ocurre es que estamos hay dos etapas hay una etapa que es el entrenamiento que

**[0:10:43]** cuando tú entrenas el modelo y hay otra etapa cuando que se llama la etapa de inferencia que es

**[0:10:49]** cuando tú usas el modelo cuando tú lo entrenas le vas diciendo el modelo lo que quieres que

**[0:10:56]** prediga cuando tú lo usas cuando ustedes usan por ejemplo el chat GPT o clodo yemina y nos están

**[0:11:04]** entrenando el modelo el modelo ya está entrenado el modelo simplemente responde ya está listo el

**[0:11:09]** modelo ok vamos a considerar un ejemplo más simple que en particular un modo un modelo de

**[0:11:26]** regresión considero una planta de evaporación para la cual usted quiere determinar la

**[0:11:30]** cantidad de agua evaporada entonces tiene una planta de evaporación y quieren calcular cuál

**[0:11:35]** la cantidad de agua evaporada para esto quieren entrenar una máquina que sea capaz de predecir este

**[0:11:41]** valor en función de un conjunto de parámetros que usted puede controlar entonces imagínense que tiene

**[0:11:46]** una planta que este caso es un caso real que en algún momento trabajamos y yo lo que quiero

**[0:11:52]** saber es predecir cuánta agua va a evaporar la planta y yo puedo mover perillas dentro de

**[0:11:59]** la máquina y de acuerdo a las perillas que yo mueva puede ser que la planta evapore más agua o menos

**[0:12:06]** agua entonces yo quiero alguna forma que el modelo prediga cuánto va voy a evaporar si es que yo

**[0:12:14]** muevo estas perillas entonces a forma yo podría poner eso podría optimizar la cantidad de agua

**[0:12:22]** evaporada de utilizando este modelo porque puedo saber cómo tengo que mover las perillas para

**[0:12:27]** que va a poner más o menos agua se entendió entonces fíjense que hay en aprendizaje automático

**[0:12:37]** hay dos enfoque principales uno y ahí tiene relación con esta pregunta tenemos algunos datos ya

**[0:12:45]** etiquetados que quiere decir tener datos etiquetados sé que yo estoy haciendo por ejemplo clasificación

**[0:12:51]** de perro y gato datos etiquetados quiere decir que yo tengo imágenes de perro y de

**[0:12:55]** gato con su etiqueta que dice este imagen es un perro este imagen es un gato en el caso de la de

**[0:13:02]** la planta de evaporación lo que quería decir es yo tengo valores de evaporación que quiero que la

**[0:13:09]** máquina siga si yo tengo datos etiquetados lo que hacemos es aprendizaje supervisado y qué tipo

**[0:13:16]** aprendizaje supervisado hay una clasificación y hay distinto algoritmo de clasificación y

**[0:13:24]** hay otro algoritmo que son los algoritmos de regresión clasificación es cuando tú querés

**[0:13:29]** estimar una clase una categoría entonces perro gato conejo regresión es cuando quieres estimar un

**[0:13:36]** valor numérico como por ejemplo 0,2 o un 5 por ciento ahí lo que uno hace es regresión

**[0:13:43]** si es que no tenemos datos etiquetados acá se complejiza un poco más la cosa porque no

**[0:13:52]** sabemos qué es lo que queremos que obtenga es como que yo le pasé muchos animales a la máquina

**[0:13:56]** sin nadie sin que nadie sepa qué tipo animales son y que la máquina prenda y extinguirlo

**[0:14:02]** automáticamente y que mira que hay un tipo animal y por acá hay otro tipo de animales eso es que

**[0:14:07]** acabo de decir es clustering que es básicamente tomar el conjunto de datos y hacer grupos de

**[0:14:15]** datos que los que se parecen más los dejamos en un lado los que no se parecen tanto los

**[0:14:19]** dejamos en otro lado pero que los que están dentro cada uno estos grupos se parezcan entre

**[0:14:23]** sí pero son distintos a los otros que sería como por ejemplo los gatos con los gatos y los

**[0:14:28]** conejos con los conejos aún cuando yo nunca le dije a la máquina que gana del gato y conejo otra

**[0:14:36]** cosa que uno hace estimación de densidad estimación de densidad es algo que de hecho

**[0:14:41]** llamimos como por ejemplo con los histograma uno trata de ver dónde están los datos ubicados

**[0:14:47]** dentro de un espacio parámetro y de eso uno puede sacar como probabilidad de que lo de que

**[0:14:52]** hayan datos en cierta zona o datos en cierta otra zona hay distinto para cada una de estas tareas

**[0:14:59]** fíjense que acá yo definí cuatro tareas cada una de estas una tarea clasificación de una

**[0:15:04]** tarea regresión de otra tarea clas teniendo otra tarea y estimación de densidad de otra

**[0:15:10]** tarea y para cada una de estas tareas hay distintos tipos de modelos entonces hay por

**[0:15:17]** ejemplo redes neuronales artificiales su port vector machines para clasificación árboles de decisión

**[0:15:23]** clasificadores vallesiano vecinos más cercanos etcétera para regresión está la regresión

**[0:15:29]** lineal los random forest la regresión por kernel y hay varias otras más en clustering uno puede

**[0:15:37]** hacer las k-medias agrupación jerárquica diviscan etcétera y en estimación de densidad uno

**[0:15:44]** puede hacer histogramas puede ser estimación de densidad por kernels mezclas de gaussiana

**[0:15:49]** y así varias cosas más hoy en día hoy en día cada una de estas tareas se están teniendo

**[0:15:59]** fuertemente con redes neuronales hay redes neuronales para clasificación hay redes neuronales

**[0:16:05]** para regresión hay redes neuronales para clustering hay redes neuronales para estimaciones

**[0:16:10]** para estimación de densidad vamos a hablar de aprendizaje supervisado ahora ya el aprendizaje

**[0:16:19]** supervisado utiliza un conjunto entrenamiento y esto es super importante los modelos cuando

**[0:16:26]** uno habla de aprendizaje automático se entrenan como qué quiere decir que se entrenan que yo le

**[0:16:31]** voy pasando datos para que el modelo vaya aprendiendo desde estos datos como que vaya entrenándose

**[0:16:36]** desde los datos los datos que yo le paso en aprendizaje supervisado son atributos

**[0:16:44]** y etiquetas entonces cuando yo estoy hablando de aprendizaje supervisado son le entrego atributos

**[0:16:50]** como habíamos visto anteriormente en las clases pasadas se acuerdan que habíamos visto que la tabla

**[0:16:55]** tenía columne cada una de esas columnas una tributo ya le entrego atributos y además le entrego

**[0:17:00]** una etiqueta en general las tablas cuando uno ve las tablas la etiqueta es parte de los

**[0:17:05]** atributos pero tú sabes que es el etiqueta y el el objetivo que tu modelo tiene que

**[0:17:11]** decir el objetivo en el aprendizaje supervisado es determinar una función que tome estos atributos

**[0:17:21]** y los transforme en una etiqueta entonces la práctica lo que uno hace es que yo tengo una

**[0:17:27]** función f de x que toma x que son los atributos y predice la etiqueta y regalo en como como

**[0:17:37]** estándar vamos a usar durante el curso que cuando tiene un gorrito quiere decir que es predicho la

**[0:17:44]** y sin gorrito quiere decir que es dato real si la etiqueta predecir es un valor real entonces

**[0:17:52]** estamos hablando de regresión pregunta hasta que nos suelta el porque se le llama supervisado

**[0:18:05]** porque yo lo estoy supervisando le estoy diciendo esto es lo que tú tienes que predecir

**[0:18:11]** claro porque en el fondo el algoritmo lo vamos a ver un poquito más delante pero el algoritmo va a

**[0:18:19]** decir este es el valor para este x este es el y y yo voy a tener la la y el y griega real y le voy

**[0:18:30]** a decir para ese griega que tú predijiste el real era este entonces lo estoy supervisando

**[0:18:36]** estoy enseñando directamente de la etiqueta por eso se llama supervisado si tengo etiquetas

**[0:18:42]** es supervisado porque le voy le voy le voy corrigiendo mía que va entrando ya vamos a dar un

**[0:18:53]** ejemplo de regresión considera la estimación del peso un árbol en función de su radio a una

**[0:18:58]** altura definida entonces digamos que acá yo tengo en el eje x el radio del tronco y en el eje y tengo

**[0:19:04]** el peso del árbol me gustaría saber más menos cuál es el peso del árbol sin tener que

**[0:19:10]** cortarlo entonces porque de esa forma yo podría encontrar el punto óptimo el cual cortar el árbol

**[0:19:18]** ok pero no quiero estar cortando todos los árboles para medir sus pesos porque bueno después no lo

**[0:19:24]** puedo volver a pegar con con la fría o bueno a lo mejor si podría pegarlo con con la fría pero

**[0:19:29]** no no funcionaría muy bien ok entonces yo lo que hago es que tengo datos histórico y lo

**[0:19:35]** voy poniendo acá en el eje x tengo el radio del tronco en el eje y el peso y yo ya corté

**[0:19:40]** estos árboles y sé que para este radio este el peso y que para este radio acá este el peso y

**[0:19:47]** para este radio acá este el peso este árbol fíjense que hay ruido cierto porque no todos los árboles

**[0:19:53]** son iguales hay algunos árboles que tienen el mismo radio pero tienen distinto peso pero uno

**[0:19:58]** ve una tendencia si yo veo que a medida que el radio del tronco va aumentando el peso

**[0:20:04]** también va aumentando entonces a mí me gustaría encontrar un modelo que fuese algo más o menos

**[0:20:13]** como esto digamos que yo digo mira este el modelo esto acá que está línea roja el modelo estamos

**[0:20:21]** modelando el problema y si que yo tuviese este modelo entonces para cualquier radio yo puedo

**[0:20:26]** tomar un radio cualquiera digamos este que está acá y voy a poder obtener cuál va a ser su peso

**[0:20:33]** para cualquier x yo veo poder obtener un y esto acá se llama un modelo de regresión y se llama

**[0:20:40]** regresión solamente porque está calculando un valor real vamos a partir hablando de la

**[0:20:49]** regresión lineal la regresión lineal es uno de los modelos más simples pero al hablar de la

**[0:20:55]** selección de la regresión lineal con con este modelo tan simple podemos tocar todos los temas

**[0:21:00]** que importan en todos los problemas más complejos con todos los modelos más complejos

**[0:21:06]** vamos a partir por un modelo lineal entonces digamos que yo tengo un modelo lineal como éste

**[0:21:12]** y digo el y a gorro recuerden que el gorro es destimado entonces voy a estimar el y

**[0:21:18]** como una variable teta 0 más una variable teta 1 multiplicado por x así de siempre entonces

**[0:21:27]** digo tengo un valor de x cualquiera y voy a estimar el y a gorro multiplicando este

**[0:21:33]** x por este teta 1 y sumándolo un teta 0 y eso queda algo como esto una línea recta

**[0:21:42]** pregunta si yo tengo este modelo entonces para puedo hacer una pregunta y decir para este radio

**[0:21:52]** cuál es el valor del y y hago lo mismo entonces ahora tomo éste bueno aquí un poquito más

**[0:21:57]** abajo pero para éste x es el valor de y que me va a dar entonces digamos que yo tengo este

**[0:22:08]** modelo lineal y ahora digo bueno pero por qué se mueve el lineal por qué no ese por ejemplo

**[0:22:15]** por qué no éste que me puede decir por qué por qué el rojo por qué el azul o por qué el naranjo

**[0:22:23]** con cuál me que me diría que porque el que minimiza los mínimos cuadráticos creo que

**[0:22:28]** era el que son los mínimos cuadrados una medida de error al final porque también puede ser el

**[0:22:38]** más hay un otro tipo de medidas para el final el tema es tener alguna alguna medida de error que

**[0:22:43]** minimizar entonces yo creo que la palabra clave es error entonces cuál creen ustedes que tienen menor

**[0:22:52]** error de estos tres rojo el rojo pareciera tener menor error no entonces la pregunta es la máquina

**[0:23:05]** como sabe que el rojo tiene menor error bueno lo calculamos por entonces digamos que yo tengo

**[0:23:11]** este modelo ya y acá viene el concepto función de costo la función de costo es cuánto me cuesta el

**[0:23:17]** utilizar este modelo que es como el equivalente al error entonces yo podría decir voy a tomar un punto

**[0:23:23]** este punto acá y este punto acá va a ser el punto y y voy a tomar su valor en x entonces su valor

**[0:23:29]** en x es x y y después tomo su valor en y el valor ni de este punto que el y rega y ya y

**[0:23:38]** entonces tengo este punto x y y y y entonces bueno y ahí me da este este par de coordenadas y y y y

**[0:23:48]** y entonces ahora yo puedo calcular el error del modelo porque tengo para este x y puedo calcular

**[0:23:54]** la función evaluada en ese punto de x y y y eso sería el y griega gorro acuérdense que ahora

**[0:24:01]** está estimado el y griega sin gorro el real el verdadero el con gorro el estimado el

**[0:24:07]** y griega estimado para el x y entonces yo sé que este es el valor real porque lo estoy haciendo de

**[0:24:14]** manera supervisada yo le estoy diciendo que la etiqueta real en el algoritmo yo sé que este

**[0:24:19]** es el valor real y entonces lo que hago es que calculo cuál es la diferencia entre lo que

**[0:24:24]** estima mi modelo y el valor real y entonces la diferencia va a ser y griega gorro de

**[0:24:31]** aquí menos y griega y entonces lo que yo hago es que me genero esta función de costo que

**[0:24:42]** está acá generalmente le pongo l a la función de costo por la l del los y esta l como rarita que

**[0:24:50]** es como la l de función de costo y lo que hago es que voy a empezar a sumar los errores de

**[0:24:56]** cada uno de los puntos entonces acá tengo el error del primer punto acá tengo el error del

**[0:25:02]** segundo punto y así sucesivamente hasta que tenga n puntos y esto errores lo elevo al cuadrado

**[0:25:09]** por qué lo elevo al cuadrado para eliminar los negativo para eliminar lo negativo

**[0:25:18]** claro se podría hacer que este me dé menos 100 y hasta acá más 100 y si yo no lo pongo al

**[0:25:23]** cuadrado podrían podrían restarse y te queda error 0 parecía como que el modelo es perfecto

**[0:25:32]** pero no entonces es una razón para eliminar el negativo pero por qué no le pongo un valor

**[0:25:37]** absoluto no más es que igual depende de las escalas pero si tienes mayores errores mayores o

**[0:25:43]** sea si la escala es mayor a 1 entonces amplifica más el error en cambio los valores entre 0 y 1

**[0:25:48]** como igual te los minimiza un poco pero igual depende mucho de las escalas de los datos como

**[0:25:53]** no entendí lo que tiene la escala sino lo que pasa es que si en este en este caso estamos

**[0:26:00]** prediciendo entre mames entre 1 51 85 si al ojo no perdón perdón perdón entre entre 0 y 6

**[0:26:07]** perdón disculpa me confundí con la colegia entonces si el error si el error es uno más al

**[0:26:12]** ser al cuadrado crece mucho más que si fuera entre 1 entre 1 y 0 se va chicando entre y entre 1 y 6

**[0:26:18]** como que crece crece más grande entonces el error como que te castiga lo las diferencias más grandes

**[0:26:23]** es el número más grande eso me refiero eso entonces si el error se escapa mucho entonces

**[0:26:29]** el error al cuadrado va a ser más grande que un error que se escapa poco en comparativamente

**[0:26:34]** la función del cuadrado hace que lo penaliza más fuerte a los valores que son más extremos

**[0:26:40]** ok hay otra razón más probabilista que la voy a mencionar pero no no es importante para este

**[0:26:50]** curso que es que el error cuadrático asume que el ruido de los datos es de si una distribución

**[0:26:59]** normal porque lo que uno hace que calcula la distribución normal le saca el logaritmo

**[0:27:05]** y el logaritmo te queda los valores al cuadrado ok una forma de escribir esto es con este símbolo

**[0:27:16]** acá que yo imagino que varios de ustedes lo conocen pero seguramente no todos y este símbolo

**[0:27:21]** acá es la sumatoria entonces la sumatoria lo que está haciendo es sumando cada uno estos

**[0:27:25]** términos y lo que voy haciendo es que tomo el valor y desde 1 hasta n y sumo esto con

**[0:27:32]** esos valores entonces sumo con el igual uno entonces me queda y de y1 menos y1 al cuadrado

**[0:27:41]** que este término acá y después lo paso al 2 y entonces me queda este término acá y así sucesivamente

**[0:27:47]** entonces ya tenemos dos componentes uno es la experiencia la experiencia en los datos

**[0:28:00]** dos podemos ver la performance que también lo está haciendo el modelo y eso lo podemos

**[0:28:05]** hacer utilizando algo como el error cuadrático medio es la función de costo ya ahora lo que

**[0:28:11]** me está lo que es lo que me está faltando el modelo en sí como la modelo en sí cierto

**[0:28:23]** necesito que aprenda con esto con estos ingredientes necesito que el modelo aprenda

**[0:28:27]** ya entonces cómo hago que el modelo aprenda bueno lo que uno hace es tratar de minimizar

**[0:28:35]** este error ok entonces si que yo por ejemplo vuelvo a estos puntos que a estas modelos

**[0:28:44]** que habíamos visto antes yo lo que podría hacer en principio si yo tengo estos estos

**[0:28:49]** tres modelos es medir su error puedo medir el error cuadrático que está acá puedo

**[0:28:54]** medir el error cuadrático y entonces puedo calcular cuál es el que tiene mayor o menor

**[0:28:58]** error en la práctica lo que lo que uno hace es que minimizo el error

**[0:29:07]** entonces generalmente el error tiene parámetros el error tiene los parámetros del modelo

**[0:29:13]** ok entonces sí que y fíjense que ahora está el signo acá de exclamación entonces mi modelo

**[0:29:19]** que está acá tiene dos parámetros el parámetros teta 0 y el parámetros teta 1 y esto importante

**[0:29:27]** para todos es un modelo de dos parámetros ok entonces si yo tuviese dos parámetros después

**[0:29:33]** tengo encontrar los valores de estos parámetros que minimice este error entonces si usted pensamos

**[0:29:41]** que tuviese solo un parámetro para el efecto gráfico en general los modelos tienen no idea

**[0:29:45]** billones de parámetros pero pensemos que que tiene solamente un parámetro imagínense

**[0:29:51]** que el teta 0 no existe que sólo fuese teta por x ya la función de costo sería algo

**[0:29:57]** como esto y lo que ocurre es que yo tengo que encontrar de alguna forma el valor mínimo de

**[0:30:04]** la función de costo que el que está acá entonces encuentro el teta que lo llamar teta

**[0:30:10]** gorro para el cual se minimiza la función de costo y después entonces lo que hago es que

**[0:30:20]** uso este teta gorro dentro de mi modelo para minimizar una función lo que uno trata de hacer es

**[0:30:27]** hacer que el gradiente sea 0 que quiere decir esto que las derivadas sean 0 no sé cuántos de acá se

**[0:30:34]** acuerdan de lo que una derivada ni cuántos de acá derivaron la semana pasada pero en general lo que

**[0:30:41]** uno trata de hacer la derivada es la pendiente entonces yo tengo la función de costo que esta

**[0:30:45]** la pendiente acá va hacia abajo hacia abajo hacia abajo y después empieza a subir la pendiente

**[0:30:51]** yo quiero que la pendiente sea 0 entonces quiero que las derivadas sean 0 en el caso en

**[0:30:59]** particular de un modelo lineal tú puedes derivar e igualar a 0 y llega a una solución

**[0:31:06]** analítica y esta es la solución analítica que es básicamente la covarianza para el teta 1 que

**[0:31:11]** está acá es la covarianza entre x y partido por la varianza de x y para el teta 0 uno llega

**[0:31:18]** a algo como esto que es el promedio de y menos teta 1 gorro por el promedio de x ok entonces

**[0:31:27]** en un modelo lineal así simplista como el que estamos viendo ahora yo puedo llegar directamente al

**[0:31:32]** valor óptimo de la función de costo y es simplemente derivar igualar a 0 y ustedes lo pueden hacer en

**[0:31:40]** su casa si quieren yo no se lo voy a pedir para ningún certamen es solamente para que entiendan

**[0:31:44]** conceptualmente lo que estamos haciendo estamos minimizando una función de costo y queremos

**[0:31:49]** básicamente que las derivadas sean 0 preguntas profe sería válido si yo llevo la analogía a otro

**[0:32:00]** contexto en donde yo digo lo que estoy buscando por ejemplo yo empresa presento presupuesto y lo que

**[0:32:06]** busco es que después de 100 presupuestos voy a hacer un presupuesto con menos errores posible y voy

**[0:32:12]** a cometer los menos errores posibles enviando ese presupuesto quizá los primero me voy a

**[0:32:16]** equivocar voy a cobrar lo que no debía y falle re re re este que en algún momento logro el falle más

**[0:32:23]** cercano a 0 y digo ahora si se hace por supuesto ahora si cobro correctamente y no por ejemplo iba

**[0:32:29]** incluido sin fin de cosa o no me equivoco considerando valores específicos eso es lo que de alguna

**[0:32:35]** forma busca uno en el aprendizaje me cuesta un poco asimilarlo con el tema de la madera porque

**[0:32:41]** no conozco mucho el contexto pero trataba de entender mientras iba escribiendo y preguntando

**[0:32:45]** por el lado pero sería eso lo que uno busca de alguna manera y bajar a 0 porque creo igual voy a

**[0:32:49]** seguir cometiendo errores pero van a ser cada vez menos claro mira es súper buena tu analogía por

**[0:32:56]** se me ocurren como distintas formas de tomar tu analogía y llevarla a este caso en el caso en

**[0:33:03]** particular de esto que estamos viendo ahora es como que tú no eres óptimo inicialmente en el

**[0:33:10]** ejecución en la definición de los presupuestos y entonces está como por acá y entonces de

**[0:33:17]** repente tú ya el presupuesto y te equivocaste dramáticamente y entonces tú dices chuta me

**[0:33:22]** equivocé dramáticamente pero sepa dónde me equivoqué yo qué sé que tengo que ir hacia

**[0:33:28]** allá y entonces avanza hacia y después dice de nuevo te volviste a hacer otro presupuesto

**[0:33:36]** mejor el segundo año y aprendiste y entonces dice ya ahora voy a voy a ahora que ya aprendí igual

**[0:33:43]** me equivoqué pero no tanto y entonces ahora tengo que hacer un poquito más hacia y empieza a

**[0:33:47]** optimizarte y de repente te voy a pasar por otro lado no se podría haber sobreestimado por acá

**[0:33:53]** podría estar sobreestimando y de repente te pasáis su estima y es como chuta no me pasé

**[0:33:58]** para el otro entonces tengo que ir hacia el otro lado eso que tú estás diciendo se llama

**[0:34:03]** aprendizaje por gradiente que básicamente tú sabes cuán más o menos para dónde tendrías que

**[0:34:09]** ir apuntado y avanza en esa dirección. Muchas gracias.

**[0:34:20]** Sí me dudas entonces ahí por qué no es profunda hacer la derivada de la función de costo

**[0:34:26]** ahí me cuesta estar pensando como la derivada de las funciones normales ahí en este caso

**[0:34:34]** no serían puros datos el valor que he dicho con el original no estaría como derivando los números

**[0:34:41]** no lo que uno si no no eso porque como les decía la función de costo depende del modelo y el modelo

**[0:34:49]** depende de los parámetros entonces lo que uno hace es que pone esto aquí adentro y después que

**[0:34:57]** está acá adentro si puedes derivar con respecto a esto que está va a estar metido aquí adentro

**[0:35:05]** tenéis que desarrollar este cuadrado o de hecho bueno depende como lo queráis derivar pero

**[0:35:10]** podréis desarrollar este cuadrado y después te queda más fácil porque las sumas van a estar separadas

**[0:35:14]** y derivar. La forma sencilla es con las fórmulas de abajo de una estimar el parámetro óptimo.

**[0:35:24]** O sea si tú quieres derivar esto lo puedes hacer no es tan complejo porque son puras o sea

**[0:35:32]** son lineal y cuadráticos en teta entonces es fácil derivar ese tipo de cosas. Y la otra opción es

**[0:35:39]** con calcularlo para las fórmulas que están más abajo los parámetros sin tener que derivar. Esto

**[0:35:47]** de acá si tú llegas a este resultado si que deriva igual a hacer este resultado de estas

**[0:35:54]** derivadas. Alguien quería hacer una pregunta. Yo iba a hacer una pregunta pero me retracté así

**[0:36:05]** con la respuesta que dio. Entonces una vez que yo obtengo este teta 1 gorro y este teta 0

**[0:36:16]** gorro esos son los que yo uso en mi modelo. Ahora nosotros usamos un modelo lineal ya es un modelo

**[0:36:26]** lineal y es como un modelo superfome y yo podría decir ok este modelo lineal bien amigos

**[0:36:33]** estamos felices pero uno se podría preguntar pero por qué un modelo lineal por qué no un

**[0:36:39]** modelo cuadrático. O sea yo podría decir en vez de teta 0 más teta 1 por x podría decir bueno

**[0:36:46]** debería ser en realidad esto se ve como más cuadrático debería ser teta 0 más teta 1 por

**[0:36:49]** x más teta 2 por x cuadrado. No sé si están de acuerdo. Y entonces uno podría decir bueno

**[0:36:59]** veamos pues me damos el error y seguramente tú vas a decir el error del modelo cuadrático

**[0:37:06]** es menor. Y después yo puedo decir bueno pero por qué entonces no un modelo cúbico. O sea podríamos

**[0:37:15]** decir teta 0 más teta 1 por x más teta 2 por x cuadrado más teta 3 por x cubo. Y entonces hay

**[0:37:24]** un concepto fundamental que estamos haciendo que es que estamos complejizando el modelo. La

**[0:37:31]** complejidad del modelo tiene relación con el número de parámetros que tiene el modelo.

**[0:37:35]** Un modelo con menos parámetros es más simple. Tiene menos complejidad que un modelo con más

**[0:37:43]** parámetros. Un modelo con mucho parámetros es mucho más complejo que uno con poco parámetros.

**[0:37:49]** Entonces en realidad la regresión lineal se llama regresión lineal porque es lineal en

**[0:37:55]** los teta. No porque es lineal en los x. Y entonces en principio yo podría decir voy a

**[0:38:03]** hacer un modelo de regresión lineal polinomial y está bien sigue siendo lineal en los parámetros.

**[0:38:10]** Fíjense que acá yo los parámetros que tengo son teta 0 teta 1 teta 2 y teta 3.

**[0:38:19]** ¿Cierto? Estos parámetros son lineales. Esta función es lineal en teta. No es lineal en

**[0:38:27]** x. En x es cuiga pero en teta es lineal. Entonces yo podría tener un modelo de regresión lineal

**[0:38:35]** porque es lineal en los parámetros para de dimensión p donde tenga p parámetros que ajustar. En realidad

**[0:38:43]** en este caso son p más 1 porque acá tengo el teta 0. Y esto sigue siendo un modelo lineal

**[0:38:49]** en los parámetros. Incluso no podría decir voy a hacer algo mucho más complejo,

**[0:38:57]** entre comidas complejo. Y en vez de usar un polinomio puedo usar cualquier función de x.

**[0:39:03]** Puedo ponerle un logaritmo, puedo ponerle una exponencial, un seno, un coseno, lo que yo quiera.

**[0:39:10]** Y el modelo sigue siendo lineal en teta. No sé si lo ven. Sigue siendo lineal en teta.

**[0:39:17]** Hay un solo teta o sea cada teta parece una sola vez. Ok eso quiere decir que el lineal que

**[0:39:24]** en realidad no hay un teta al cuadrado ni un logaritmo de teta ni una exponencial de teta es que el teta

**[0:39:29]** parece cada teta parece por sí solo una vez. Ok y entonces yo podría hacer que cada una

**[0:39:38]** de estas funciones sean muy distintas pero sigue siendo un modelo lineal. Y la forma que uno

**[0:39:44]** escribió esto es de esta forma. El y agorro es la suma desde j igual 0 hasta p del teta j por

**[0:39:52]** el jj de x. Es lo mismo que habíamos escrito antes simplemente lo escribí con forma utilizando

**[0:39:58]** una sumatoria. ¿Pregunta hasta acá? Ok. Si yo hiciera algo como esto por ejemplo usar un modelo

**[0:40:15]** de regresión lineal pero con un polinomio. Si yo uso un polinomio de grado 1 así como teta 0 más

**[0:40:23]** teta 1 por x es un polinomio de grado 1 me ha quedado una línea recta. Si yo uso un polinomio

**[0:40:31]** de grado 2 teta 0 más teta 1 por x más teta 2 por x cuadrado complejizo el modelo y me queda algo

**[0:40:37]** como esto. Sé que yo voy aumentando el grado del polinomio el modelo se irá ajustando cada vez más

**[0:40:45]** a los datos. Entonces esto es un ejemplo de un polinomio de grado 10. Entonces yo podría tener un

**[0:40:51]** polinomio de grado 10 y fíjense que el modelo pasa muy cerca de todos los datos todos los

**[0:40:56]** datos. Entonces mi pregunta es ¿cuál de estos tres modelos es mejor y por qué? O sea el mejor

**[0:41:08]** si es el de grado 10 pero tal vez el sobre ajustado a los datos. Ah muy bien ¿qué quiere decir sobre

**[0:41:16]** ajustado a los datos? Que eso lo funciona con esos datos si no le pasa a otro tal vez no se ajusta

**[0:41:24]** Exacto. Entonces no nos basta. Que no generalizo. No generalizo. Entonces no nos basta con solamente

**[0:41:34]** tener un modelo que minimice el error sobre el conjunto entrenamiento. Imagínense que yo tengo este

**[0:41:42]** polinomio de grado 10 y lo ajusto a los datos y me queda esto y ahora yo pregunto por ejemplo

**[0:41:49]** este valor. Este valor de acá. El modelo me va a decir que el valor de griega este de por acá ría

**[0:41:56]** pero es raro que ese sea el valor de griega así como que no sigue la tendencia. Eso es lo que se llama

**[0:42:03]** sobre ajuste y el problema que tiene el modelo al estar sobre ajustado que no es capaz de generalizar.

**[0:42:10]** ¿Qué quiere decir generalizar? Que sea capaz de funcionar para datos que no ha visto antes.

**[0:42:16]** Que eso es lo que uno quiere que hagan los modelos. O sea si yo tengo un modelo que me

**[0:42:20]** predice cuando va a fallar una máquina por decir algo. No quiero que me prediga cuando

**[0:42:24]** falló la máquina. Quiero que me prediga cuando va a fallar el futuro y eso quiere

**[0:42:29]** decir que el modelo tiene que generalizar a datos que no ha visto antes. Tiene que ser general

**[0:42:34]** en ese sentido. ¿Pregunta hasta acá? Ya. Entonces ¿qué es la generalización? Es la

**[0:42:50]** capacidad de obtener buenos resultados con datos que nunca ha visto el modelo antes.

**[0:42:54]** Y entre comillas es como que la máquina no se aprenda de memoria los datos y no sea capaz de

**[0:43:01]** entender datos que nunca ha visto. Y acá pasa algo muy interesante que es que a medida que se

**[0:43:09]** complejiza el modelo tiende a sobreajustarse más. Pero si yo tengo un modelo muy simple,

**[0:43:16]** entonces lo que ocurre es que el modelo muy simple no va a ser capaz de predecir bien,

**[0:43:22]** que es como el modelo lineal que habíamos visto antes. Entonces hay un balance entre tener un modelo

**[0:43:28]** muy complejo y un modelo muy simple. ¿Cómo saber si estoy sobreajustado? Lo que generalmente

**[0:43:37]** uno hace es lo que se llama validación cruzada. Entonces generalmente yo le digo a todo mi alumno,

**[0:43:44]** si es que no saben la respuesta a algún problema, tienen como respuesta validación cruzada.

**[0:43:51]** Porque validación cruzada es la respuesta a la mayor parte de los problemas del aprendizaje

**[0:43:55]** automático. ¿Qué es la validación cruzada? La validación cruzada es que yo tomo mi conjunto de

**[0:44:03]** datos como este acá y defino tres subconjuntos. Uno es el conjunto de test, voy a partir al

**[0:44:12]** revés de abajo para arriba. El conjunto de test yo lo tomo y me lo guardo en el bolsillo. La

**[0:44:17]** máquina nunca lo es. Y lo que hace es que evalúa qué también lo haría el modelo sobre

**[0:44:24]** datos que no ha visto antes. Lo uso solamente para evaluar al final. Después de que entreno

**[0:44:29]** un modelo y hago todo lo que yo quiera, lo que hago es uso el conjunto de test. Además tengo un

**[0:44:36]** conjunto de entrenamiento que es con el que se ajuste el modelo y también tenemos un conjunto de

**[0:44:42]** validación. ¿Para qué sirve el conjunto de validación? Para evaluar cómo el modelo,

**[0:44:48]** para evaluar qué también lo hace el modelo para distintos hiperparámetros. Y acá introduce

**[0:44:54]** el concepto de hiperparámetro. Todos los modelos, la gran mayoría, creo que no se ocurre ninguno que

**[0:45:01]** no, tienen hiperparámetros. Los hiperparámetros son parámetros que se fijan antes de empezar

**[0:45:07]** a ajustar el modelo. Entonces, por ejemplo, en el caso del modelo de regresión lineal,

**[0:45:16]** un hiperparámetro sería el orden del polinomio. El orden del polinomio yo lo defino antes de

**[0:45:24]** ajustar el modelo. Entonces, yo defino un orden de polinomio, por ejemplo, no sé, polinomio de

**[0:45:30]** grado 3. Y lo que hago es que lo entreno con el conjunto de entrenamiento. Una vez que

**[0:45:39]** terminó de entrenar, lo evaluó con el conjunto de validación. Calcule la función de costo

**[0:45:44]** sobre el conjunto de validación. Debería generalizar bien al conjunto de validación.

**[0:45:49]** Pero después yo cambio el orden del polinomio y digo, voy a probar polinomio de grado 3.

**[0:45:55]** Perdón, partí con grado 3. Voy a probar con polinomio de grado 10. Y entonces,

**[0:46:00]** ajusto el polinomio de grado 3 de grado 10, perdón, con el conjunto de entrenamiento. Y

**[0:46:07]** después de que terminó de ajustar, lo evaluó con el conjunto de validación. El conjunto de

**[0:46:13]** validación no lo vio durante el entrenamiento. Entonces, el polinomio, de acuerdo a lo que

**[0:46:18]** vimos antes, un polinomio de grado 3 debería evaluarse mejor sobre el conjunto de

**[0:46:23]** validación con polinomio de grado 10. Para este caso en particular, el que vimos recién.

**[0:46:29]** Y entonces, con eso, yo tomo una decisión y digo, no voy a usar un polinomio de grado 10,

**[0:46:36]** sino que voy a usar un polinomio de grado 3. Y después de que tomé esa decisión,

**[0:46:42]** el polinomio de grado 3, lo que hago es tomar, me saco del bolsillo o del cajón,

**[0:46:46]** no sé dónde lo guardaron, el conjunto de test y evaluo sobre el conjunto de test.

**[0:46:51]** Y esa es la última validación que hago y reporto las métricas sobre el conjunto de

**[0:46:55]** test. Digo que también lo hizo para generalizar al final sobre el conjunto de test. ¿Se entendió?

**[0:47:02]** Pregunta, ¿por qué entonces tengo que hacer conjunto de alineación y de test? ¿Por qué no

**[0:47:10]** uso solo uno? Para evaluar la generalización. Por el sobreajuste es lo que pasó con el polinomio,

**[0:47:17]** porque así sí tengo datos entre comidas escondidos. Después puedo comparar el... Es

**[0:47:23]** para enseñarte sobre el sobreajuste, porque si por ejemplo como un polinomio de

**[0:47:26]** grado muy alto, más que algo que voy a generalizar, me va a hacer una interpelación tan que pase por

**[0:47:33]** todos los puntos y los intermediados no se van a ver. Entonces con ese set de validación puedo ver

**[0:47:38]** que esas ondas que se hacen... Con eso voy a decir que esas ondas que se hacen en este caso en

**[0:47:44]** particular están mal. Y ahí puedo tener una métrica de error. Para qué usa el conjunto de alineación?

**[0:47:50]** Pero ¿por qué necesito 2? ¿Por qué necesito validación y test? Ah, porque si suelo

**[0:47:56]** complejizar el modelo, va a intentar pasar por esos puntos, en esos puntos en particular que están

**[0:48:00]** en el set de validación. Entonces si no están ahí los puedo comparar. Porque si tengo todos los

**[0:48:06]** puntos en el entrenamiento y tengo un polinomio de grado muy alto, el error me dar 0. Y no tengo

**[0:48:11]** cómo compararlo, porque no tengo otros puntos aparte. No sé si se entiende. No, no lo entiendo,

**[0:48:16]** porque en el fondo el conjunto de alineación no lo vio durante el entrenamiento. No, claro,

**[0:48:21]** porque ese es el caso si estaría. Pero en términos, sí es como que la máquina no me memorizo. No

**[0:48:28]** voy a memorizar números que no vio. Eso es como en palabras como más... En palabras como más día a día.

**[0:48:33]** Pero el conjunto de alineación no lo vio? Por eso. Si no vio el conjunto de alineación,

**[0:48:40]** entonces se suelo no sé para verificar qué puede generalizar. Lo que me acuerdo es que

**[0:48:48]** el validación... A ver, cuando uno toma datos o pruebas de test y después validación es un poco

**[0:48:55]** para ver cómo funciona con datos, como que los de validación pasan a ser datos nuevos por lo que me

**[0:49:03]** acuerdo. Entonces, claro, yo entreno al modelo con el testing y después el de validación viene

**[0:49:07]** a ver ya qué tal se comporta fuera de los datos que utilicé para entrenar, diga.

**[0:49:13]** Ya, por ahí va, por ahí va. Lo que ocurre, lo que podría ocurrir, que no necesariamente ocurre

**[0:49:20]** siempre, pero que yo haya escogido un modelo, un hiperparámetro que funcione muy bien para el

**[0:49:30]** conjunto de alineación. Que por chances, así como por azar, justo el conjunto de alineación funciona

**[0:49:38]** muy bien para un subconjunto o para un set de hiperparámetro, para un orden del polinomio.

**[0:49:44]** Entonces podría ser que justo el conjunto de alineación, si hubo una tendencia, no sé por decir,

**[0:49:50]** de un polinomio de orden 5, porque tuve mala suerte. Y entonces el problema que tenemos ahí es que se

**[0:49:59]** podría sobreajustar el conjunto de alineación. ¿Me entienden? Porque yo estoy tomando una

**[0:50:05]** decisión sobre el modelo, utilizando el conjunto de alineación. Aun cuando no son los TET,

**[0:50:11]** los parámetros del modelo, que es los parámetros del modelo se ajustan con el conjunto de entrenamiento.

**[0:50:15]** En el conjunto de alineación, yo estoy tomando, con el conjunto de alineación,

**[0:50:19]** yo estoy tomando una decisión y es cuál es el orden del polinomio en este caso.

**[0:50:25]** Entonces podría ser que el escoja justo el orden del polinomio que calza bien con el conjunto de

**[0:50:30]** alineación, pero que después no generaliza igual, a datos que no hay instantes. Entonces

**[0:50:35]** por eso la métrica final se mide sobre el conjunto de test. En general los errores sobre el conjunto

**[0:50:47]** de alineación son muy parecidos a los errores sobre el conjunto de test, en general. Pero hay

**[0:50:52]** ocasiones en las cuales uno ve que no ocurre eso. Y hay uno que tiene que entrar así como con mucho

**[0:50:58]** cuidado en qué es lo que está pasando. Rofe, pero si pasa eso que comenta de que justo con

**[0:51:05]** validación dio el polinomio perfecto, ¿cómo encuentro eso? Porque de alguna manera, claro,

**[0:51:14]** cuando uno ve curvas de testing y de validación, generalmente son como usted bien dice, como muy

**[0:51:22]** parecía las líneas, pero ¿cómo tomo esa decisión? O sea, ¿qué utilizo para contrastar en caso de

**[0:51:29]** que suceda eso que justo dio perfecto o dio bien el polinomio? Esto que yo le acabo de mostrar acá

**[0:51:38]** no es validación cruzada, esto es validación nomás. Y ahora le voy a explicar cómo se hace eso que

**[0:51:45]** tú dices Francisco, usando validación cruzada propiamente tal. La estrategia de validación

**[0:51:52]** cruzada hay distinta, pero una de esas es K-fold, otra de esas shuffle split y otra es bootstrapin y

**[0:51:59]** vamos a ver estas ahora. Alguien levantó la mano, pero no alcanzé a ver quién fue. Yo me quedé con una

**[0:52:06]** duda del conjunto de validaciones con lo hiperparámetro, ahí entonces como el conjunto de entrenamiento,

**[0:52:17]** ahí el modelo aprende, pero ahí no se viene que se refiere con eso, o sea, ya con lo hiperparámetro

**[0:52:23]** ya tengo el modelo en sí, se refiere como que decir para calcular los errores, ¿es cuál es el modelo

**[0:52:31]** de entrenamiento o qué se refiere con que el modelo aprenda? Ah ya, mira, es que el modelo aprende,

**[0:52:39]** ahí voy a ir para atrás, digamos este modelo acá, el modelo aprende cuando al momento de encontrar

**[0:52:52]** estos tetas, estos parámetros que son los parámetros del modelo, es el momento en el

**[0:52:56]** cual el modelo está aprendiendo, ok? Pero antes de que el modelo aprenda, yo tengo que fijar este 3,

**[0:53:04]** si yo no tengo este 3, el modelo no sabe cómo, qué es lo que tiene que ajustar,

**[0:53:13]** hasta ahí vamos bien, ¿cierto? O sea, y ahí con los grados, el grado del polinomio se

**[0:53:23]** refiere a que con hiperparámetro o los grados del polinomio, en este caso voy para acá, en este

**[0:53:29]** caso este P, el hiperparámetro, ah ya, y los otros son, ¿sería más como parámetros? Estos son parámetros,

**[0:53:39]** los tetas son parámetros, el P es hiperparámetro, ah ya, y ahí se determinan entonces con el

**[0:53:46]** entrenamiento de los parámetros. Entonces yo parto con un P que yo lijo, digamos 2, calculo los tetas

**[0:53:54]** sobre el conjunto entrenamiento y evaluo cómo le fue el modelo sobre el conjunto de alineación,

**[0:54:01]** entonces en principio estoy evaluando su capacidad de generalizar, entonces después lo que hago es

**[0:54:07]** tomo otro P y digo 10 y ajusto con el conjunto entrenamiento los parámetros tetas y después

**[0:54:16]** lo ajusto, evaluo sobre el conjunto de alineación, comparo cuál de los dos da mejor el conjunto de

**[0:54:24]** alineación, queda menor error en el conjunto de alineación y después de eso digo este es el modelo

**[0:54:31]** final, pero una vez que tengo el modelo final necesito ver su capacidad de generalizar y para eso

**[0:54:37]** tomo el conjunto de test que lo tenía guardado de antes y ahí con eso mido efectivamente que

**[0:54:42]** también le fue el modelo, ¿sí? Ay ya, sí, gracias. ¿Hay más preguntas? Ok, entonces qué estrategia hay de

**[0:55:04]** validación cruzada y ahora le voy a explicar lo que es la validación cruzada, uno de eso el método

**[0:55:10]** de retención que el que acabamos de ver que el holdout method que es como que básicamente

**[0:55:15]** guardo un subconjunto pero el problema que tenemos con eso es que tengo un solo valor y así

**[0:55:20]** como preguntaba Francisco es como bueno pero de qué me sirve es que el mono se ajustó y lo tengo

**[0:55:27]** validado sobre un solo valor, entonces hay otros métodos de validación cruzada que los vamos

**[0:55:32]** a ir viendo como el submostreo aleatorio, el key fold y bootstrap, el método de retención el que

**[0:55:39]** acabamos de ver que separa el conjunto de entrenamiento en dos conjuntos separados, se entrena sobre un

**[0:55:45]** conjunto y se valía sobre el otro y generalmente se usa dos tercios para entrenamiento y un

**[0:55:49]** tercio para validación, fíjense que lo que estoy diciendo acá el conjunto de test siempre se se

**[0:55:54]** para primero, esto es como yo hago la separación entre conjunto entrenamiento y validación y finalmente

**[0:56:01]** calculo después de que termino todo esto calculo el error sobre el conjunto de test, entonces tomo

**[0:56:06]** los datos esto es como lo mismo que hay a más laminante, tomo los datos, tomo el conjunto

**[0:56:13]** de entrenamiento, ajusto el modelo sobre el conjunto de entrenamiento, tomo el conjunto

**[0:56:17]** de validación, evaluo sobre el conjunto de validación y al final le evaluo sobre el conjunto de test,

**[0:56:21]** todos felices, todos contentos. Ahora bootstrap, lo que uno va a hacer es lo siguiente, genero

**[0:56:31]** m subconjunto aleatorio de tamaño n' menor que n muestreando de los datos al azar con

**[0:56:38]** reemplazo, entonces qué es lo que estoy diciendo, voy a hacer el mismo ejercicio que hicimos

**[0:56:43]** antes pero lo voy a hacer varias veces, entonces para hacerlo varias veces, lo que hago es que

**[0:56:51]** imagínense que los datos estuvieran dentro de una bolita, cada uno de los datos dentro de una

**[0:56:56]** bolita y tengo un saco de bolitas y entonces lo que hago es que tomo un dato, lo miro, lo anoto

**[0:57:02]** y digo ya este es el dato que voy a usar para mi conjunto de entrenamiento y vuelvo a meter

**[0:57:07]** la bolita y después vuelvo a sacudir la bolsa y vuelvo a tomar otro dato y digo a este

**[0:57:12]** también lo voy a usar para mi conjunto de entrenamiento y vuelvo a meter la bolita y vuelvo a sacudir el saco,

**[0:57:18]** lo que estoy haciendo ahí es que a veces me podría salir dos veces el mismo dato,

**[0:57:27]** la gracia hacer esto es que puedo hacerlo varias veces, no sé si lo ven, lo puedo hacer varias

**[0:57:34]** veces, entonces después lo que hago es que todo lo que no está dentro del conjunto de

**[0:57:40]** entrenamiento pasa al conjunto de aliaciones, en promedio un conjunto de entrenamiento de

**[0:57:47]** tamaño n con bootstrap contiene el orden del 63,2% de los datos, entonces voy a hacer el dibujito

**[0:57:55]** como los datos, guardo el test, siempre parto guardando el test, eso que no se lo olvide nunca,

**[0:58:01]** guardar el test y después digo aleatoriamente saco datos del conjunto de entrenamiento y pueden

**[0:58:07]** ver datos repetidos dentro del conjunto de entrenamiento y después lo que no estuvo

**[0:58:11]** repetido lo paso al conjunto de aliación y después puedo volver a hacer lo mismo,

**[0:58:18]** puedo tomar mis datos, siempre tengo que usar el mismo conjunto de test que está guardado y ahora

**[0:58:28]** vuelvo a mostrar aleatoriamente y me salen otros datos para el conjunto de entrenamiento y otros

**[0:58:32]** datos para el conjunto de aliación, fíjense que si yo hago esto, lo que ocurre es que

**[0:58:38]** voy a tener varios valores de validación, entonces si ustedes están pensando por ejemplo en el error

**[0:58:44]** cuadrático que el que vimos recién, voy a tener varios errores cuadráticos para cada vez que yo

**[0:58:50]** haga uno de estos voy a tener un error cuadrático sobre el conjunto de aliación, entonces si yo tengo

**[0:58:55]** varios errores de esto que digamos que lo haga 10 pese o 50 pese o 100 pese o 1000 pese,

**[0:59:01]** da lo mismo, si yo lo hago varias pese entonces puedo saber más o menos la distribución

**[0:59:07]** del error, entonces sé que el error puede estar, va a estar entre este y este valor más o menos,

**[0:59:13]** le puedo calcular la media o la mediana y puedo calcular la deviación estándar o los percentiles,

**[0:59:18]** entonces de esa forma yo sé en qué rango se debería mover mi modelo y entonces empiezo como

**[0:59:26]** a medir estadísticamente como sea comportando el modelo y después al final lo aplico sobre

**[0:59:31]** el conjunto de test y en conjunto de test el error debiese caer dentro de los errores del

**[0:59:38]** conjunto de aliación dentro de la distribución de los errores del conjunto de aliación ¿Se entiende?

**[0:59:45]** ¿Tiene alguna pregunta? Hay en el conjunto de entrenamiento de susteniar los parámetros ¿verdad?

**[1:00:01]** Cada vez que yo muevo un parámetro tengo que hacer esto varias pese,

**[1:00:07]** a ver, levante la mano sé que entendieron, pero que hay una sola mano levanta. No sé cómo

**[1:00:29]** levanta la mano pero hay varias manos más leantas, ok, levante la mano si no entendieron,

**[1:00:44]** hay varias manos levantas también que no entendieron, voy a hacer un dibujo,

**[1:00:58]** ok, creo que eso siempre es yo. Déjenme sacar mi tal, déjenme un segundo por favor.

**[1:01:13]** Profes, una consulta, esta presentación ¿Usted no la puede compartir?

**[1:01:18]** Sí, sí por supuesto va a quedar en el campas, tengo un problema, me voy a conectar durante

**[1:01:32]** como 10 segundos pero que tengo que conectar el cable de red. Volví, ¿no escuchan?

**[1:01:49]** Sí, sí, sí. ¿Están viendo mi pantalla?

**[1:02:02]** Sí, se ve, se ve. Entonces, ¿imaginen que yo tengo por acá? Ah, no está escribiendo,

**[1:02:45]** imaginen que tengo acá hace tiempo que nos gusta, la función de costo, ok, esa es mi función de costo

**[1:03:08]** y yo tomo un polinomio de orden 1 y empiezo a calcular el error del polinomio orden 1,

**[1:03:19]** ok, entonces tomo el polinomio orden 1, hago esta variación cruzada, entonces saco un conjunto

**[1:03:26]** entrenamiento, un conjunto de aliación y calculo el error sobre el conjunto de aliación y vamos

**[1:03:32]** que me da acá, es el error y después lo que yo hago es, voy a tratar de poner un punto y después

**[1:03:41]** tomo otro punto, ya me da ahí, entonces ahora tomo, vuelvo a remostreo desde los datos para el conjunto

**[1:03:56]** entrenamiento y aliación, acuérdense que el conjunto de pruebas no se toca y calculo el error en

**[1:04:02]** conjunto de aliación y me da este punto acá y después lo vuelvo a hacer, vuelvo a remostrear y

**[1:04:08]** vuelvo a calcular el error sobre el conjunto de aliación y me da por acá, ok, entonces fíjense

**[1:04:14]** que yo sé que el error en el conjunto de aliación está como por ahí, ya, vamos a hacer esto un

**[1:04:19]** poquito al largo, vaya, digamos que por acá está el cero, ok, está quedando real, ahí está el cero,

**[1:04:30]** ya, entonces ahora esto es el polinomio de grado 1, cierto, bueno acá, grado 1, está quedando real,

**[1:04:46]** estoy haciendo lo mejor que puedo, ya, es 1, y ahora tomo un polinomio de grado 2 y hago lo

**[1:04:57]** mismo, entreno el modelo con el polinomio de grado 2 y calculo el conjunto de aliación y me da por acá

**[1:05:02]** y después de nuevo, entreno el modelo con el polinomio de grado 2 y lo calculo el error de

**[1:05:10]** variación y me da acá y así sucesivamente lo puedo hacer cuatro veces y el otro lo hice tres,

**[1:05:15]** bueno, da no bien, ok, entonces este es el de grado 2, sí, fíjense que lo que estoy viendo

**[1:05:28]** acá es que, ¿con cuál polinomio de qué grado me quería quedar con el polinomio de qué grado

**[1:05:36]** me quería quedar? Uno, ¿por qué? Porque tiene menor error, cierto, el error está más cercano a cero,

**[1:05:51]** entonces me quedo con el polinomio de grado 1, que esto fue evaluado sobre el conjunto de aliación,

**[1:05:57]** cierto, y entonces lo que hago es ahora sobre los distintos conjuntos de aliación,

**[1:06:03]** porque se han generando nuevos conjuntos de aliación, ahora tomo el conjunto de test y

**[1:06:09]** evaluo sobre el conjunto de test, el conjunto de test me diría quedar por acá el error,

**[1:06:15]** ¿cierto? Entonces por acá debería estar el error sobre el conjunto de test, más o menos,

**[1:06:22]** si no me queda ahí hay algo raro, ¿cierto? Entonces podría ser en general te queda ahí,

**[1:06:31]** pero si no quiere decir que tú hiciste algo raro, que el conjunto de los conjuntos de

**[1:06:35]** aliación nos representan correctamente al conjunto de test, y eso a veces ocurre porque el

**[1:06:40]** conjunto de test tiene alguna anomalía, por ejemplo, o porque artificialmente cogiste un conjunto de test

**[1:06:47]** que no es representativo del resto del conjunto de datos, eso también pasa cuando uno trabaja

**[1:06:52]** con series de tiempo, por ejemplo, y yo digo voy a considerar para el entrenamiento los datos

**[1:06:58]** hasta el año 2025, voy a usar como conjunto de aliación los datos del año 2025 al 2026,

**[1:07:05]** y voy a juntar en el conjunto de test todos los datos del año 2008, por decir algo. Entonces lo que

**[1:07:15]** pasa es que el conjunto de aliación está muy separado el conjunto de test, el conjunto de

**[1:07:22]** test no es representativo de lo que yo quiero que el modelo haga, ¿se entendió?

**[1:07:28]** Yo ahora sí, ahora se entendió, pero yo estoy con una duda de síctencia así, todo esto que

**[1:07:42]** estamos viendo, el dibujito es de la validación cruzada, no del primer entrenamiento que hicimos.

**[1:07:49]** Sí, es la validación cruzada, todos estos son puntitos del conjunto de aliación,

**[1:07:55]** más preguntas? Ya, y fíjense que en este método de bootstrap que uno de los métodos que uno puede

**[1:08:06]** usar, el conjunto de entrenamiento podría tener valores repetidos, pero no el conjunto de

**[1:08:12]** aliación, el conjunto de aliación no tiene valores repetidos. Ahora, ¿por qué uno usaría bootstrap?

**[1:08:22]** En general uno usa bootstrap que es como repetir datos del conjunto de entrenamiento,

**[1:08:27]** porque uno lo usa cuando tengo pocos datos, si tengo pocos datos y me saldría como entre comillas muy

**[1:08:36]** caros, usan muchos datos en el conjunto de entrenamiento, entonces lo voy a repetir. El submuestreo

**[1:08:43]** aleatorio que es lo que se llama random sub sampling en inglés, es básicamente la misma idea,

**[1:08:49]** pero sin reemplazo, o sea, muestreo sin reemplazo. Entonces dividido aleatoriamente los datos,

**[1:08:56]** conjunto de entrenamiento, conjunto de aliación, realizo el método de retención para cada división y

**[1:09:01]** el error se calcula como el promedio de lo error obtenido, que es lo mismo que hayamos visto. Entonces

**[1:09:06]** de nuevo guardo el conjunto de test, no se olviden de guardar el conjunto de test, el conjunto de test

**[1:09:10]** no cambia entre una iteración y otra, y después de eso digo aleatoriamente sacó parte del

**[1:09:17]** conjunto de datos como parte del conjunto de entrenamiento, aleatoriamente el resto lo

**[1:09:22]** pasó a aliación. Acá no hay repetición, el conjunto de entrenamiento no tiene datos

**[1:09:26]** repetidos, ok? Y después hago lo mismo otra vez y saco datos para el conjunto de entrenamiento y

**[1:09:33]** datos para el conjunto de aliación, ¿sí? Es la misma idea y después yo puedo calcular de

**[1:09:42]** nuevo lo error en el conjunto de aliación que voy a tener distintos valores para lo

**[1:09:48]** error en el conjunto de aliación y podría calcular media o mediana o cualquier cosa para

**[1:09:52]** saber más o menos dónde se mueven los errores. La validación cruzada con K-fold lo que uno hace

**[1:09:59]** es que dividió el conjunto de datos en K subconjuntos disjuntos. ¿Qué quiere decir eso? Que no se repiten

**[1:10:08]** dentro estos K conjuntos, no se repiten objetos en más de un conjunto. Dejo un subconjunto

**[1:10:15]** como conjunto de aliación y uso los otros K-1 para el entrenamiento. Y repito esto

**[1:10:21]** cada vez porque es el número de veces que lo puedo hacer usando cada subconjunto una vez para la

**[1:10:25]** validación. Entonces tengo mis datos, guardo siempre mi test y el resto de los datos lo que hago es que

**[1:10:33]** saco un subconjunto de aliación y el resto los dejo como conjunto de entrenamiento. Entonces en

**[1:10:40]** este caso dije K igual 4 porque tengo 4 subconjuntos, estos 4 acá, uno lo tomo como

**[1:10:46]** aliación y todo el resto entra el conjunto de entrenamiento. Entreno con este conjunto de

**[1:10:51]** entrenamiento y después valido con el conjunto de aliación. Y después lo que hago es que los subconjuntos

**[1:10:58]** se quedan fijos y cambio el conjunto de aliación. Entonces el conjunto de aliación ahora era

**[1:11:04]** antes era conjunto de entrenamiento pero ahora es conjunto de aliación y el conjunto de

**[1:11:07]** aliación pasa a ser parte del conjunto de entrenamiento. Y así sucesivamente lo voy

**[1:11:12]** haciendo y en este caso lo puedo hacer 4S porque dice K igual a 4. ¿Preguntas hasta acá?

**[1:11:25]** Dale Cristóbal, David, pregunto. No, no dale, tú dijiste primero. Que yo ya estoy pensando mientras

**[1:11:32]** va explicando profe, claro, ¿cuál es mejor? O sea, cuándo ocupo uno, cuándo ocupo otro y en alguna

**[1:11:40]** medida esas validaciones cruzadas quizá pueden dar métricas de validación no buenas, por ejemplo,

**[1:11:49]** ¿o cuáles serían esas? ¿Cómo se trabaja eso? O quizá me estoy adelantando. No, no, no, es una

**[1:11:56]** muy buena pregunta. En general todas estas convergen a los mismos resultados para datos infinitos,

**[1:12:02]** pero tú no tienes datos infinitos, nadie tiene datos infinitos. Si tú tuvieras datos infinitos

**[1:12:07]** converges básicamente al error real, ¿no? Pero como no tienes datos infinitos, va a

**[1:12:15]** depender mucho de la tarea que tú estás realizando y de lo que quieres hacer con esa tarea. Entonces,

**[1:12:21]** el problema de K Fold es que si tú no tienes muchos datos, no tienes muchas opciones para el K,

**[1:12:27]** así que yo tengo 100 datos, no puedo hacer K igual a 1000, por ejemplo. ¿Cierto? Si yo tengo 10

**[1:12:34]** datos, no puedo hacer K igual a 12. Entonces, lo que hay como un tradeoff entre una cosa y otra.

**[1:12:44]** La gracia, eso sí que tiene el K Fold, es que cada dato fue usado exactamente una vez para

**[1:12:52]** ser validado. Entonces, en principio yo tengo cada dato fue validado. Me imagino como que da

**[1:13:00]** vuelta al data set, claro, como bien dices, o sea, para probar todo lo que tengo en ese data set,

**[1:13:06]** algo así o cada X, pero cada predicción, digamos, y estimado. Claro, entonces yo podría tener una

**[1:13:15]** predicción para cada uno de los datos y podría entonces ver cómo se comporta el modelo para

**[1:13:19]** todos los datos. Ahora, para hacer esto, como les decía, tenéis que tener suficiente datos

**[1:13:26]** y para tener un K relativamente alta. La otra gracia que tiene, que también se puede hacer con

**[1:13:30]** lo otro, pero en este caso se suele hacer con este método, es que tú puedes usar, imagínate que tú

**[1:13:40]** quieres tratar 20 modelos, tú puedes usar exactamente la misma partición para estos 20 modelos que

**[1:13:48]** tú quieres probar. Ahora, tú también lo puedes hacer con el resto, con el anterior. Tú puedes

**[1:13:56]** acá primero muestrear y después de que yo muestreo de que tengo todas las muestras,

**[1:14:01]** empiezo a entrenar los modelos y me aseguro de que todos los modelos sigan exacta,

**[1:14:06]** sean evaluados sobre exactamente lo mismo. La misma muestra. En general, yo lo que digo es,

**[1:14:13]** o como yo lo uso, es si tienen mucho, mucho datos que hay ford está bien,

**[1:14:18]** porque cada uno de los subconjunto va a tener mucho, mucho datos. Ahora tú me

**[1:14:23]** voy a preguntar y ¿cuánto es mucho, mucho datos? Bueno, depende del problema, depende del problema.

**[1:14:30]** Si que yo quiero clasificar entre perro y gato, mucho, mucho datos no es tanto, porque necesito que me

**[1:14:36]** caigan, no sé, unos 50 gato acá y 50 perros en cada conjunto y con eso más o menos lo hago,

**[1:14:43]** porque con eso tengo una cierta precisión en las métricas que estoy evaluando.

**[1:14:51]** Sí, entiendo un poco. Ahora, si yo tengo muy pocos datos, ahí tenés que hacer

**[1:14:59]** bootstrapping porque no va a tener la capacidad para generar conjunto entrenamiento lo suficientemente

**[1:15:03]** grande. Gracias profe. Cristobal tenía una pregunta, ¿no? Sí, profe, tratando de entender este

**[1:15:16]** concepto, pero desde una arquitectura tecnológica, me refiero a una stack o estructura, yo tengo

**[1:15:22]** un modelo, una base de datos, no sé, corro algún script. Supongo cómo funciona esto en la práctica

**[1:15:29]** cuando ejecuto estos modelos de aprendizaje o cuando dejo entrenando. Eso es como un primer

**[1:15:34]** punto para tratar de materializarlo o bajarlo algo tangible. Y lo segundo es, en la actualidad

**[1:15:41]** los modelos tienen la capacidad realmente de auto aprendizaje. He visto hartos de artículos

**[1:15:46]** bien interesantes que sugieren que han logrado como el genia, de alguna forma o la capacidad

**[1:15:52]** generativa en donde podrían eventualmente con bajo costo estar generando algo similar

**[1:15:58]** al auto aprendizaje o a la inflexión o a la reflexión, como ella. Pero, y trae saber

**[1:16:06]** más que nada, porque si yo quisiera crear mi propio modelo, es costoso para mí en

**[1:16:11]** mi PC, en mi equipo, en mi casa hacer un ejercicio como este. ¿Pero cómo logró

**[1:16:16]** vencer estos gigantes como OpenI o Anthropic y comenzar a trabajar con mi propio modelo,

**[1:16:24]** no sé, pensando en algo específico? Porque usted dice, ¿se necesitan grandes pólúmenes

**[1:16:28]** de datos, parámetros y tal vez no voy a lograrlo hacerlo? O tal vez sí, no sé.

**[1:16:34]** Ya hiciste tres preguntas muy interesantes. La primera es cómo voy a poder hacer

**[1:16:41]** esto en la práctica dentro de mi arquitectura. Generalmente tú lo que haces es descargar

**[1:16:47]** los datos, entrenas el modelo y después cuando digamos que tú tienes una pipeline de

**[1:16:53]** procedimiento, lo que sea, sube el modelo y lo conecta a la pipeline y después con el

**[1:16:58]** modelo ya entrenado. El modelo no se reentrena mientras está en producción.

**[1:17:02]** En general, hay veces que uno no puede hacer. En la ayudantía, después de esto,

**[1:17:09]** en la clase práctica, van a ver cómo entrenar el modelo.

**[1:17:14]** La segunda pregunta era del auto aprendizaje ya. Hay auto aprendizaje que es como self-supervised,

**[1:17:22]** es cuando los modelos se entrenan para ser capaces de reconocer los datos por sí mismo.

**[1:17:29]** Entonces, ¿qué me refiero con esto? Sé que yo, por ejemplo, tengo una imagen de un

**[1:17:33]** perro y hago un recorte de la imagen del perro. Yo le enseño al modelo a aprender

**[1:17:41]** a predecir ese recorte y eso es, por ejemplo, un caso de in-painting que es cuando tú borra un

**[1:17:48]** pedazo de la imagen y le pides al modelo que la reconstruye. Eso es auto aprendizaje porque no

**[1:17:56]** tengo una etiqueta, así propiamente tal, que diga perro, pero sí tengo los mismos datos de

**[1:18:03]** entrada, los atributos, que son los píxeles de la imagen y entonces puedo verle al modelo

**[1:18:08]** que aprenda a reconocer sus propios atributos. Eso es auto aprendizaje, pero tú creo que digas

**[1:18:17]** en otra dirección que era cómo el modelo es capaz de corregirse a sí mismo y me imagino que

**[1:18:28]** está hablando un modelo de lenguaje o no. Pensando específicamente, le doy un poco más de

**[1:18:33]** contexto. Yo corro el script, corro ejecuciones, descubro orecha y trato de medir la ejecución,

**[1:18:40]** no sé, un pentes ejecutado agénticamente y tal vez mido cantidad de hallazgo versus el tiempo de

**[1:18:48]** ejecución. Próximo ciclo vuelvo a correr contra un mismo set de target y digo, bueno,

**[1:18:53]** en esta oportunidad demoró tal vez 15 minutos y descubrió más hallazgo. Entonces eso es

**[1:18:59]** como mis dos parámetros y para medirlo, pero mi orquestador sigue siendo antropic. Entonces

**[1:19:05]** de alguna forma, en ese contexto como que trato de yo decir, cómo me desagoplo de alguna forma

**[1:19:10]** antropic y cómo logro enterar mi propio modelo con todos los históricos que existen. Existen

**[1:19:15]** mucha fuente de información, pero no tengo la capacidad arquitectónica para lograr un centro

**[1:19:20]** de investigación en esa línea. Ya, sí, mirad, es complicado. En el fondo, hoy en día, los

**[1:19:29]** modelos de lenguaje están gobernados por... Son los dueños de estos modelos de lenguaje

**[1:19:35]** son las grandes empresas. No existe forma de competir con ellos. Tienen unos servidores

**[1:19:42]** gigantes, o sea, tienen unos datacenters gigantes distribuidos por todo el mundo donde

**[1:19:47]** entren estos modelos y tienen muchos recursos para entrenar estos modelos. Entonces hoy en día,

**[1:19:52]** tú no puedes competir con antropic, no hay a tener un chat GPT. Lo que sí puedes tener son modelos

**[1:19:59]** que no son tan tan buenos, pero tampoco son tan malos y que son abiertos. Entonces, por ejemplo,

**[1:20:06]** DeepSig tiene los modelos abiertos y tú puedes descargar el modelo y si tiene una GPU lo

**[1:20:12]** suficientemente poderosa, puedes usar esa GPU para correr el modelo en modo de inferencia.

**[1:20:19]** Entrenarlo es mucho más difícil. O sea, pero puedes correr al menos el modelo en modo de inferencia,

**[1:20:26]** que es básicamente que predica la siguiente palabra y lo puedes tener tú localmente para evitar

**[1:20:31]** brechas de seguridad o lo que sea que te importe. Ahora, la respuesta a esto desde la

**[1:20:41]** comunidad inteligencia artificial es lo que se llaman los modelos fundacionales, que son modelos

**[1:20:46]** que como de uso general y que tú los puedes descargar y puedes hacer algunas cosas con ellos.

**[1:20:53]** Entonces hay cosas como lo que se llaman los low resolution adapters que son como modelos

**[1:20:59]** chiquititos que se conectan a los modelos fundacionales y que aprenden a hacer alguna

**[1:21:05]** cosa en particular usando este modelo, o sea, entrenando con tu tato. Entonces tú toda la maquinaria

**[1:21:13]** pesada se queda fija, pero tenés un modelo chiquitito que te ayude a hacer alguna cosita.

**[1:21:18]** Eso es una opción. La otra opción es simplemente poner un modelo que no sea un adaptador,

**[1:21:28]** pero obviamente tal. O sea, que no haga exactamente lo que el otro modelo hacía,

**[1:21:32]** pero que haga alguna tarea en particular. Entonces, en vez de, por ejemplo,

**[1:21:36]** estamos hablando de un chat GPT, en vez de predecir la siguiente palabra con un LORA,

**[1:21:40]** con un low resolution adapter, tú lo que podías hacer es ponerle, conectarle a un LLM al final

**[1:21:47]** algo, un clasificador, clasificador de sentimientos, por ejemplo, o algo de ese estilo. Pero,

**[1:21:54]** hoy en día lo que se hace que está muy de moda son los agentes. Entonces tú puedes usar agentes,

**[1:22:01]** pero tienes que tener la capacidad de correr los LLM, los modelos de lenguaje. Entonces los modelos

**[1:22:10]** de lenguaje generalmente como funciona o como yo uso los agentes, por lo menos que tengo varios

**[1:22:16]** proyectos con un agente. Lo que hago es uso como parte trasera, como backbone, alguna LLM pagada.

**[1:22:25]** Entonces yo pago Yeminai y pago todo, pero pago por el uso de Yeminai para conectar

**[1:22:34]** mi agente a Yeminai. ¿Por qué no lo hago en mi infraestructura local? Porque cuando uno

**[1:22:41]** trabaja con un agente necesita en general que la LLM responda rápido y la GPU así como las

**[1:22:47]** gamers no tienen una ancho de banda tan alto. Existen hoy en día GPU que tienen una ancho de

**[1:22:54]** banda alto, pero son carísimas, cuestan cientos de millones de pesos y donde tú puedes meterle un

**[1:22:59]** deep seek y que te corre más o menos en tiempo real. Pero a mí me sale más cuenta pagar

**[1:23:04]** a Yeminai para usar esa tarjera. Además que si yo compro, si comprar el hardware en un año más

**[1:23:11]** va a estar obsoleto. Entonces para qué voy a invertir tanta plata en algo que va a estar en un año

**[1:23:15]** obsoleto mientras que Yeminai, Google, OpenAI, Anthropic me los actualizan automáticamente.

**[1:23:21]** No sé si respondí todas las preguntas. Sí, por supuesto, por supuesto profesor,

**[1:23:26]** muchas gracias. ¿Hay más preguntas? Priscila parece que había hablado.

**[1:23:33]** Sí, yo tengo una pregunta relacionada a lo que dijo Francisco, así como más que de la clase.

**[1:23:41]** Cuando Francisco preguntó qué modelo elegir, mi pregunta es, usted dijo el modelo de acuerdo

**[1:23:50]** a la tarea que uno quiere hacer. Uno también puede apoyarse la literatura para elegir el

**[1:23:59]** mejor modelo, porque eso es lo que yo estoy haciendo. O sea, estoy revisando paper, estoy viendo,

**[1:24:06]** o sea, de acuerdo a lo que yo quiero hacer, los papers que están saliendo y ahí estoy como

**[1:24:11]** viendo el modelo o según mi hipótesis lo que quiero hacer. Entonces ¿es correcto eso? ¿poder

**[1:24:21]** no apoyar en la literatura? Sí, en general uno se apoya en la literatura y usa básicamente

**[1:24:28]** los modelos que funcionan bien para las tareas que uno quiere resolver. Sin embargo,

**[1:24:35]** siempre pueden evaluar más de un modelo. O sea, o en realidad uno puede sacar un modelo de la

**[1:24:41]** literatura y usarlo directamente, pero a veces no funcionan también, entonces uno tiene que evaluar

**[1:24:48]** más de un modelo. Y cuando uno evalúa más de un modelo, podría hacer que un modelo

**[1:24:52]** funcione mejor que otro. Entonces ¿cómo puedo hacer para saber cuál es el modelo

**[1:24:57]** que me diría que haga? Ya, muchas gracias. Pero era una pregunta. ¿Cómo elijo el modelo

**[1:25:09]** con el cual me diría que haga? ¿Quién sabe? Se quedó bajo tres modelos, ¿cómo se cual

**[1:25:15]** de los tres diría usar? Bueno, viendo lo más. ¿El que más es el que a cero? ¿Cómo?

**[1:25:22]** ¿El que de mejores métricas? ¿El que de mejores métricas? ¿Pero cómo miedo las

**[1:25:27]** métricas? El que más es el que a cero. El que más es el que a cero, pero con

**[1:25:32]** respecto a qué? O sea, a los errores. ¿Cómo? A los errores. ¿A los errores? ¿Aquí

**[1:25:48]** errores? Cuadrático. No, pero al final lo que uno tiene que hacer, acuérdense que si

**[1:25:59]** ustedes no saben la respuesta, tienen que responder validación cruzada. Lo que uno

**[1:26:03]** hace es validación cruzada. Entonces yo tengo que hacer validación cruzada con

**[1:26:08]** los tres modelos y me quedo con el de menor error, como decía Caden, sobre la

**[1:26:13]** validación cruzada. Oye, quizá ahí, no sé si quizá yo pregunté mal o no, pero yo en

**[1:26:23]** realidad más que preguntar qué modelo quizá lo que hablaba Priscila, me refería

**[1:26:29]** a qué tipo de validación usar. Quizá ahí yo me, cuando... Ah, no, pero eso lo respondí.

**[1:26:35]** Sí, sí, no, de acuerdo. Solo que me quedé marcando ocupado con con la pregunta de Priscila,

**[1:26:43]** porque yo entiendo cuando oye qué modelo elegimos, no estamos hablando... o

**[1:26:48]** bueno, quizá sí no, no sé, pero no estamos hablando de claro qué modelo

**[1:26:52]** ocupar de para predicción. Acá estamos hablando de formas para

**[1:26:56]** validación que es distinto, digo. Sí. Como para que quizá si hay alguna

**[1:27:02]** confusión, poder aterrizarla. Y respecto a lo otro, yo como que iba a

**[1:27:13]** responder, que claro, uno lo hace claro a través de validación cruzada, pero uno,

**[1:27:19]** cuando echa a andar estos modelos y de repente el código en Python que se yo

**[1:27:24]** empieza a analizar, claro, te entrega un porcentaje, un nivel de confianza, digamos,

**[1:27:29]** cuál tiene mayor nivel de confianza, digo, ah, y a este modelo anda mejor,

**[1:27:34]** digamos. Sí. Ok, yo le voy a hacer un ejemplo, le voy a mostrar este ejemplo,

**[1:27:44]** estamos un poco en contra del tiempo, lo voy a pasar rapidito. Básicamente, si se

**[1:27:49]** fijan lo que nosotros, lo que yo les digo que tenemos que hacer es etiquetado,

**[1:27:53]** entrenamiento, evaluación y al final predicción. Entonces, primero etiqueta uno,

**[1:27:58]** tiene etiquetas, cierto, que tiene que conseguirla de alguna parte. Después

**[1:28:03]** entra en el modelo y después de entrenado tengo que evaluarlo y después de

**[1:28:08]** que ya está evaluado y que yo sé que también lo está haciendo mi modelo,

**[1:28:10]** tengo que predecir, cierto. Este es un sistema que nosotros armamos para Arauco,

**[1:28:16]** donde básicamente ellos tenían drones que vuelan por los predios y querían contarle la

**[1:28:25]** cantidad de árboles, ese era como el objetivo principal, tenían muchas, muchas

**[1:28:29]** imágenes y entonces lo que nosotros hicimos fue que tomábamos estas imágenes y las

**[1:28:32]** dividíamos en grillas, entonces teníamos esta grilla y después tú podías etiquetar

**[1:28:38]** dentro de las grillas lo que tú quisieras. En principio esto sirva para cualquier cosa,

**[1:28:42]** podías etiquetar células o pese o lo que fuese. Entonces tú vas etiquetando cosas y

**[1:28:47]** después de que etiquetas las cosas se generan dentro de estas grillas, se separan

**[1:28:52]** las celditas en conjunto entrenamiento, aliación y test y después de eso uno

**[1:28:58]** entra en el modelo y después se evalúa sobre el conjunto de test y después se

**[1:29:04]** se predice con datos nuevo y en principio te permite etiquetar cualquier cosa.

**[1:29:10]** Es un problema clásico, ocurre todo el rato, siempre uno necesita etiquetas,

**[1:29:15]** siempre uno necesita la mayor cantidad de etiquetas que pueda, a veces las etiquetas son caras,

**[1:29:20]** entonces tú tienes que alguna forma generar modelos que hagan la validación cruzada con

**[1:29:25]** el número de etiquetas que tengas. Eso es todo, no sé si tiene alguna pregunta adicional de

**[1:29:33]** la materia. Profesor consulta, cuando hicieron la grilla de la imagen que estaba mostrando,

**[1:29:44]** la forestal, una etiqueta podría hacer árbol, la otra era suelo, algo así. Sí. O podría

**[1:29:53]** tener solo árbol. Ah y fíjense que esto es un problema de regresión porque lo que

**[1:29:57]** estábamos buscando eran o cajitas o un polígono. Entonces cuando yo quiero cajitas lo que

**[1:30:03]** estoy diciendo es necesito las esquinas y las esquinas son valores reales. Hay alguna pregunta

**[1:30:13]** adicional? Un tendí, perdón, no entendí eso último. Ah, que cuando se que cuando uno hace

**[1:30:21]** localización que básicamente tengo una imagen y quiero hacer una caja alrededor de algún objeto,

**[1:30:27]** digamos de un árbol, un perro, un taladro o lo que sea. Cuando hago una caja,

**[1:30:33]** la caja se define en general por dos puntos. Una esquina y otra esquina. Las coordenadas

**[1:30:39]** con una esquina y las coordenadas en otra. Las coordenadas son valores reales. Entonces es un

**[1:30:45]** problema de regresión porque tengo que estimar puede ser 0,2, 1, 5, puede ser 5, 2, 6, 8,

**[1:30:53]** ok. Entonces se transforma en un problema de regresión. Ok. Ok, entonces vamos a dejar la clase hasta acá.
