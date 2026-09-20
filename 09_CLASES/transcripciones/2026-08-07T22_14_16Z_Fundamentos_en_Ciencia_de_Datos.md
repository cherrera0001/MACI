# 2026-08-07T22_14_16Z Fundamentos en Ciencia de Datos.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:37:17
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:00:09]** La semana pasada vimos regresión, que es cuando queremos predecir una etiqueta que tiene un

**[0:00:32]** valor continuo o un valor numérico. Hoy día vamos a ver clasificación que es cuando queremos

**[0:00:37]** predecir una etiqueta que tiene un valor categórico, o sea que es una categoría. Entonces acá

**[0:00:43]** como a modo de resumen siempre me gusta participar por este mono para nunca olvidarlo. El ciclo de

**[0:00:50]** la ciencia de datos comienza con un requerimiento pregunta, después recolectamos datos, limpiamos

**[0:00:56]** los datos, exploramos, modelamos, visualizamos de alguna forma los resultados de nuestro modelo

**[0:01:02]** y somos capaces de comunicarlo para luego tomar decisiones. Y finalmente el modelo se pone en

**[0:01:07]** marcha y después volvemos al requerimiento pregunta. Y como siempre decimos la flechita

**[0:01:12]** para nace a los dos lados porque a veces uno está modelando y de repente se cuenta que el modelo

**[0:01:17]** no funciona bien y tiene que volver a explorar los datos. Hoy día vamos a seguir en la parte

**[0:01:22]** de modelamiento, pero vamos a hablar de clasificación. Otra cosa que vimos en la clase pasada es que

**[0:01:29]** el aprendizaje de máquina, el estudio de algoritmos que mejoran su rendimiento en alguna

**[0:01:33]** tarea con la experiencia y una tarea de aprendizaje bien definida tiene que tener

**[0:01:38]** estos tres componentes. Y como vimos también la clase pasada, a la máquina se le enseña

**[0:01:47]** desde la experiencia y la experiencia viene desde los datos. Entonces los datos son como

**[0:01:51]** experiencia previas, datos que yo ya tenía antes y que le enseño, le entrego a la máquina

**[0:01:56]** para que aprenda a resolver alguna tarea en particular, la máquina en general intenta

**[0:02:01]** reducir algún error relacionado con esta tarea y después de eso yo puedo hacerle

**[0:02:08]** una pregunta y entonces la máquina me responde. El ejemplo que vimos y decir el año pasado. La semana

**[0:02:16]** pasada es que queremos predecir por ejemplo el peso de un árbol en función del radio del tronco

**[0:02:23]** y tenemos todos estos datos de árboles que yo corté y para los cuales yo sé cuál es su

**[0:02:29]** peso y también el radio de su tronco y entonces después puedo ajustar un modelo. Ahora el

**[0:02:36]** modelo podría ser un modelo de regresión lineal que como vimos la clase pasada es lineal en los

**[0:02:42]** parámetros a ajustar y podría uno pensar un polinomio por ejemplo de grado 1, un polinomio de grado 2,

**[0:02:49]** un polinomio de grado 10, un polinomio de grado P y una de las preguntas que teníamos era cómo

**[0:02:54]** definimos qué tan complejo tiene que ser el modelo. Entonces un modelo con poco parámetros

**[0:02:59]** como este acá es un modelo simple que tiene solamente dos parámetros y un modelo muy complejo

**[0:03:04]** como este acá que de grado 10 tiene muchos parámetros. Entonces cómo yo puedo saber cuántos

**[0:03:09]** parámetros son los correctos. Si se fijan si solo me dedico a mirar el error del modelo en función

**[0:03:18]** del conjunto de datos con el cual lo ajuste o no entrené. Entonces el problema que tenemos

**[0:03:23]** es que este modelo acá se tiende a sobreajustar pasa perfectamente por todos los datos pero el

**[0:03:29]** problema es que no es capaz de generalizar y es y entramos entonces al concepto de

**[0:03:33]** generalización. Y cómo podemos nosotros medir si es que el modelo está generalizando correctamente

**[0:03:38]** o no? ¿Quién me puede decir? ¿Para acceder con un set de datos de prueba que no haya sido usado

**[0:03:48]** durante el entrenamiento? Exacto y eso es lo que nosotros llamamos variación cruzada y vimos

**[0:03:54]** varias estrategias de variación cruzada la semana pasada. Variación cruzada en general uno

**[0:04:00]** lo usa casi siempre yo diría que siempre ok y se usa para cualquier tarea de aprendizaje ya sea

**[0:04:10]** supervisada no supervisada uno trata de asegurarse que el modelo sea capaz de generalizar correctamente.

**[0:04:20]** Entonces la clase de hoy vamos a hacer algo muy parecido a la clase pasada pero en vez de

**[0:04:26]** hablar de regresión vamos a hablar de clasificación y vamos a ver los distintos componentes que

**[0:04:31]** habíamos visto la clase pasada para la regresión pero lo vamos a ver para clasificación ahora ok.

**[0:04:36]** Clasificación es muy parecido a regresión y le recuerdo que cuando aparezca este simbolito

**[0:04:42]** quiere decir que hay un poco de matemática más densa y eso quiere decir que aún cuando no

**[0:04:48]** se va a preguntar en el certamen si usted tiene un background matemático entonces pueden prestar

**[0:04:57]** entonces vamos a hacer un ejemplo digamos que yo tengo animales y quiero clasificar a los animales

**[0:05:05]** y entonces yo mío algunos atributos de los animales y entonces digamos que yo estoy midiendo

**[0:05:10]** el tamaño del animal y el tamaño de las orejas por decir algo entonces voy a tomar un animal

**[0:05:16]** cualquiera como está acá y este es un perro que es un perro grande y que tiene orejas

**[0:05:22]** grandes ¿no? después voy a tomar otro animal como está acá que es un perro pequeño pero que

**[0:05:29]** tiene orejas grandes y después tomo otro animal como está acá que es un perro grande pero que tiene

**[0:05:35]** orejas comparativamente pequeñas y así sureciamente yo puedo tomar más y más perro y van a ver

**[0:05:40]** perros medianos y perros grandes con orejas grandes y pequeñas y etcétera etcétera

**[0:05:45]** ¿no? entonces ahí tengo fíjense que hay un color alrededor de la imagen eso hay el color

**[0:05:51]** me dice que de qué clase es el animal y en este caso es perro y ahora entonces digamos que yo quiero

**[0:05:58]** clasificar entre perro y gato y entonces tomo un gato como este que es un gato pequeño pero con orejas

**[0:06:04]** grandes y ahora tomo otro gato como este que es un gato grande pero con orejas pequeñas

**[0:06:09]** cualquier similitud con algún ser humano que ustedes conozcan es solo coincidencia y después

**[0:06:16]** de eso tomo más gato y más gato y entonces relleno acá ya que tengo un gato pequeño con

**[0:06:20]** orejas pequeñas un gato mediano con orejas medias entonces imagínense que ustedes van y

**[0:06:25]** empezan a tomar medidas de gato y perro y empiezan a pesarlo o a ver qué tan grande y también su oreja

**[0:06:32]** fíjense que los gatos tienen una etiqueta que está demarcada por un color verde alrededor

**[0:06:40]** entonces esto es supervisado porque yo sé qué es lo que es cada animal dentro de mi conjunto de

**[0:06:46]** datos o de mi conjunto de entrenamiento y yo quiero después ajustar un modelo que digamos que podría

**[0:06:52]** hacer algo como esto es digo todo lo que está hacia arriba es perro y todo lo que está hacia abajo

**[0:06:57]** es gato entonces con este modelo yo después podría tener otro animal que yo no sé si es perro gato

**[0:07:02]** y veo qué tan grande el tamaño del animal veo el tamaño de su oreja y si es muy grande la

**[0:07:08]** oreja son muy grande seguramente hace perro si es muy grande es perdón muy pequeño entonces

**[0:07:12]** seguramente hacer gato va a estar por acá abajo ok esto un modelo de clasificación lineal porque

**[0:07:18]** es una línea recta vencerlo así por ahora después vamos a definir un poco más lo que quiere decir

**[0:07:24]** como lo que hicimos con el modelo como yo dije perdón me confundí de que tenía el

**[0:07:36]** micrófono abierto y efectivamente lo tenías abierto entonces decía que esto un modelo lineal

**[0:07:46]** y básicamente que separa linealmente entre las dos clases entonces esto es como lo que uno

**[0:07:51]** quiere hacer ahora por supuesto no va a tener dos parámetros y seguramente los parámetros que

**[0:07:55]** voy a tener no van a ser los tamaños de la oreja y los tamaños del animal voy a tener

**[0:07:59]** otro tipo de parámetro y las tareas pueden ser tan complejas como uno quiera y uno puede

**[0:08:03]** empezar a complejizar el modelo también ¿saburan que vimos la definición de aprendizaje

**[0:08:10]** supervisado la semana pasada? decíamos que se utiliza un conjunto entrenamiento que está compuesto

**[0:08:16]** por atributos que son los de aquí que en el caso anterior son el tamaño del animal y el tamaño

**[0:08:23]** de la oreja del animal eso serían los atributos y tenemos las etiquetas y griega y que en el

**[0:08:28]** caso anterior era perro o gato son etiquetas yo sé que los datos vienen con esa etiqueta

**[0:08:34]** entonces después el objetivo es determinar una función que tome los atributos y prediga la etiqueta

**[0:08:40]** entonces esto es y gorro va a ser igual a f de x quiero una función que tome cualquier valor de x

**[0:08:46]** que son tamaños de oreja y tamaños de animal y me prediga un y que es la etiqueta me prediga

**[0:08:52]** la etiqueta y si recuerdan de la clase pasada le ponemos un gorrito cuando decimos que es una

**[0:08:58]** estimación de la etiqueta entonces básicamente es la predicción del modelo no es la etiqueta

**[0:09:02]** real cuando no tiene gorritos estamos hablando de los datos reales todo esto que acabo de mostrar

**[0:09:08]** acá es exactamente lo mismo que vimos la semana pasada con regresión pero ahora la diferencia

**[0:09:15]** si la etiqueta es una categoría entonces lo llamamos clasificación entonces qué me puede decir cuál

**[0:09:22]** la diferencia entre una variable categórica y una variable numérica alguien se acuerda voy a decir

**[0:09:35]** un nombre la sal hernan si no profe que no no recuerdo eso no respondo que me voy a decir la

**[0:09:49]** diferencia entre una variable categórica y una variable numérica parece que la categórica me

**[0:09:54]** de cualidades y no porque pueden haber cualidad en numérica que se mide en numérica pero categóricas

**[0:10:03]** fíjense lo que de dónde viene la palabra categórico viene de categorías versus numérico que

**[0:10:09]** viene de números alguien sabe cuál la diferencia entre categorico y numérico entonces una categoría

**[0:10:20]** es perro gato conejo un número es 1 2 3 4 5 6 entonces cuál la diferencia entre perro gato

**[0:10:28]** conejo y 1 2 3 4 5 6 para mí la imagen mental que tengo yo de eso es que una que una variable

**[0:10:35]** numérica tiene sentido interpolarla mientras una categorica no tiene sentido por ejemplo entre

**[0:10:40]** 1 y 2 puede decir que hay 1.5 pero entre perro y gato no hay nada no tendría sentido como

**[0:10:43]** se pregunta estás muy cerca está al lado lo la diferencia es que la variable categórica no tiene

**[0:10:52]** una noción de orden entonces si digo perro gato conejo yo no puedo decir el perro viene antes

**[0:10:59]** que el gato o después del gato y el conejo antes o después del perro no tiene una noción de

**[0:11:04]** orden una categoría las variables numéricas si tienen una noción de orden el 1 es menor

**[0:11:10]** que el 2 y el 2 es menor que el 3 el 4 es mayor que el 3 yo no puedo decir el perro es mayor que el

**[0:11:16]** gato o el gato es mayor que el conejo si una es cualitativa y la otra es cuantitativa no necesariamente

**[0:11:24]** no necesariamente porque si tú por ejemplo dices voy a observar un paisaje y le voy a

**[0:11:31]** asignar un número de 1 a 5 de acuerdo a qué tan bonito el paisaje es un numérico y es

**[0:11:39]** cualitativo no ven cuantitativo sería como algo que yo mido cualitativo es como una

**[0:11:46]** cualidad que yo signo como como humano se entiende la diferencia categorica sería como

**[0:11:55]** saber si la categoría por ejemplo no sé adulto mayor adulto es joven

**[0:12:03]** abresente como diferente como rango de eso está un poco como en una zona gris porque en el

**[0:12:13]** fondo tú puedes asignar categorías pero esas categorías que tú me acabas de decir están

**[0:12:19]** asociadas una variable numérica entonces si pueden la variable real que está midiendo adulto mayor

**[0:12:26]** o adulto joven es la edad y la edad yo sí la puedo ordenar entonces no no se comporta

**[0:12:33]** como una variable categorica es una discretización de una variable numérica entonces sigue siendo

**[0:12:41]** sigue teniendo una noción de orden no tiene que tener orden por ejemplo hombre mujer o hombre

**[0:12:50]** mujer no tiene orden hombre mujer no tiene orden que otra cosa no tiene orden no sé árbol planta

**[0:12:59]** eso no tiene orden no hay yo no puedo ordenarlos o sea uno podría decir voy a ordenarlo en

**[0:13:06]** función de su altura pero ahí lo que tú estás ordenando es la altura no el árbol o la planta

**[0:13:12]** el concepto de árbol o planta por dentro de sí mismo no tiene una noción de orden

**[0:13:18]** y cómo pasaría para los grados por ejemplo midiendo la temperatura el cómo aplicaría por

**[0:13:25]** ejemplo 10 grados celsius 20 grados celsius porque como que mide también una supongo una

**[0:13:32]** categoría pero no es no es como el doble de la temperatura sino que está haciendo otro

**[0:13:39]** tipo de medición pero cuál es la categoría o qué es lo que está midiendo la temperatura

**[0:13:45]** está midiendo puedo tomar la temperatura y ordenarla o sea si día día 20 grados y mañana

**[0:13:53]** y 25 puedo decir hoy hay menos más que ayer o sea que mañana si los por ordenar entonces

**[0:14:02]** en numérico o sea son son números que por ordenar y si fuera profa de la categoría

**[0:14:08]** frío templado caliente sería como una categoría pero lo pudiese ordenar como me lo imagino como

**[0:14:17]** una recta entre frío mediano caliente o sea el mismo que hayamos hablado antes frío mediano

**[0:14:25]** caliente está asociado a una temperatura como la altura entonces una categoría tienen que pensar

**[0:14:35]** en cosas que tienen cierta cierta categoría ciertas clases y esas clases no están asociadas

**[0:14:43]** una variable numérica pero antes al principio había dicho otra definición había dado una

**[0:14:55]** definición como que no tenían orden la la categorica o no si si exacto hay más preguntas respecto

**[0:15:10]** estaría mal dar un valor numérico una variable categorica es una buena pregunta yo no puedo

**[0:15:22]** a un modelo matemático entregarle una variable categorica cierto un modelo matemático no

**[0:15:30]** entiende lo que es perro gato entonces tengo transformarlo un número y esto es lo que hablábamos

**[0:15:34]** la la vez pasada que se llama hacer el one hot encoding entonces se acuerdan una vez más

**[0:15:41]** un vector control del tamaño de todas las categorías y le ponía un uno a la categoría a la cual

**[0:15:48]** representaba el objeto y ceros al resto se acuerdan de eso si es importante que intentamos esto otra

**[0:15:59]** categoría que podría ser que que sea distinta es como el círculo cuadrado triángulo son yo no

**[0:16:08]** puedo decir un círculo es mayor que un cuadrado un cuadrado es mayor que un triángulo son

**[0:16:16]** categorías si ok entonces digamos que nosotros queremos clasificar digamos que tengo acá

**[0:16:35]** estos objetos que son de alguna clase que le voy a llamar triángulos y estos objetos acá que son

**[0:16:42]** de otra clase que lo voy a llamar círculos ok digamos que yo mío atributos de esta de esta

**[0:16:48]** variable es perdón de estos objetos entonces digamos que por ejemplo esto acá hay que uno es como

**[0:16:54]** el equivalente a lo que habíamos dicho antes que puede ser el tamaño del animal y x2 podría

**[0:16:58]** ser el tamaño de la oreja del animal y yo quiero de alguna forma dividir estos dos estos

**[0:17:04]** dos conjuntos de datos y entonces uno podría decir voy a hacer una línea recta y esto un modelo

**[0:17:10]** lineal aquí me refiero con que es lineal a que depende linealmente de x1 y de x2 si se acuerdan

**[0:17:17]** la vez pasada nosotros hicimos un modelo de regresión lineal que era también un modelo

**[0:17:23]** lineal al igual que lo que en regresión no puede tener modelos lineales que no sean lineales en

**[0:17:29]** x1 y en x2 pero que sí son lineales los parandro ok entonces digamos que yo separo esto así que les

**[0:17:38]** parece les parece bien o les parece mal está separando bien está separando mal qué bien

**[0:17:46]** cumple está bien está haciendo lo que debería estar haciendo no así yo lo mío digo bueno

**[0:17:52]** pero qué pasa con ese está haciendo lo que debería estar haciendo también cumple también cumple

**[0:18:01]** también está haciendo lo que yo le di quisiera y qué pasa con este está separando no está

**[0:18:07]** separando a los filo pero está como que no sé quién lo dijo pero dijo cumple este cumple

**[0:18:19]** también ahora la pregunta es cuál modelo le gusta más a ustedes y por qué sea al ojo y sólo

**[0:18:34]** con esos datos disponibles yo miría por el naranjo pero la verdad y para mí el azul y el naranjo

**[0:18:40]** son bien en cuenta bien similares habría alguna médica error pero yo miría por el naranjo así

**[0:18:44]** bien al ojo ya por qué hay por qué por qué no el verde por qué no el verde porque está más

**[0:18:51]** pecado un conjunto de datos sí siento que está más está más sesgado que a clasificar sobre el

**[0:18:57]** rojo en ese caso ya que como que les pasa que alir como más grande eso es como entre mí no más

**[0:19:00]** como al ojo matemáticamente debería ser explicarse de otra forma en la cercanía el fallo de la distancia

**[0:19:09]** contra la recta muy baja posible que se equivoque eso está muy muy bueno muy bueno muy buena intuición

**[0:19:17]** si ustedes piensan el verde ya imagínense que yo tengo un objeto por acá voy para atrás

**[0:19:23]** como como para imagínense que yo tengo un objeto por acá ven mi mouse cierto si qué tipo

**[0:19:33]** objeto debería ser esto creen ustedes dónde está mi mouse circulo azul debería ser un

**[0:19:40]** círculo cierto por qué porque debería ser un círculo y no un triángulo por anda por anda por anda

**[0:19:45]** por la tendencia por lo que está más cerca tal vez como se ha ido clasificando porque está más

**[0:19:53]** cerca porque está más cerca de los azules cierto entonces si yo hago eso y pongo el verde

**[0:20:00]** el verde como que está cometiendo un error acá porque los objetos más cerca de los azules no están

**[0:20:06]** siendo clasificados como azules sino que están siendo clasificados como triángulos como triángulos

**[0:20:10]** rojos no es entonces el verde creo que estamos claros y tienen la una relación de cercanía con

**[0:20:20]** los datos a los cuales estábamos que tenemos dentro de nuestro conjunto de entrenamiento

**[0:20:26]** si entonces empieza uno empieza a pensar ya cercanía distancia tienen que estar cerca

**[0:20:32]** cierto voy a ir atrás y ahora yo les pregunto cuál es mejor el naranjo o el azul el azul

**[0:20:41]** porque es súper similario ya mira si voy a hacer algo imagínense que usted tenga un objeto acá en

**[0:20:52]** esta zona acá que es como me digo bien entonces voy a dejar el mouse ahí y voy para atrás qué

**[0:20:59]** tipo objeto debería ser eso claro y debería ser azul ahí te más sentido debería ser azul porque

**[0:21:05]** estaba cerca de los azules el naranjo lo clasificaría como azul el azul lo clasificaría como triángulo

**[0:21:14]** como triángulo rojo cierto entonces lo que ocurre es que uno empieza a pensar y entonces

**[0:21:22]** tiene que ver con una una noción de cercanía entre los objetos que son clasificados de

**[0:21:28]** la misma forma y eso es súper importante o sea lo que usted para tomar la decisión de cuál de los

**[0:21:35]** modelos lineales más o millas convenientes es el que me permita clasificar más sin sin hacer

**[0:21:43]** como esta distinción entre uno y otro el que me deje más espacio esa clasificación por ejemplo

**[0:21:47]** yo hoy dije el azul anteriormente pero el azul no me permite seguir clasificando comillas más

**[0:21:52]** modelos o sea más intersección azules pero si el naranjo me permitiría para ambos casos seguir

**[0:21:58]** en la clasificación si que se aproximan a lo que ya a lo que ya viene viene mostrándola el modelo

**[0:22:08]** tiene tiene relación con con que el modelo de alguna forma tiene que representar la realidad y en

**[0:22:19]** este caso lo que nosotros decimos que en la realidad los objetos más cercanos generalmente

**[0:22:25]** son de la misma clase generalmente siempre hay cosas rara que ocurren podrías tener un

**[0:22:32]** perro pequeño no sé un chihuahua por ejemplo podría ser clasificado como gato pero eso es un

**[0:22:39]** error y los modelos como yo les decía la primera clase o la segunda clase los modelos nunca son

**[0:22:44]** perfectos entonces los modelos un modelo de 100% perfecto yo al tiro dudo de ese modelo porque

**[0:22:52]** ningún modelo 100% perfecto hay algo raro si un modelo 100% perfecto hay algo raro

**[0:22:56]** porque la naturaleza no es 100% perfecta hay perros que parecen gatos hay gatos que

**[0:23:03]** parecen perros hay árboles que parecen plantas y hay plantas que parecen árboles si entonces en

**[0:23:13]** el fondo pero en general los objetos que están cerca pertenecerán a las mismas clases entonces

**[0:23:21]** tiene relación con la noción de cercanía que eso está asociado a la distancia no fue me

**[0:23:26]** acuerdo de un modelo veo que es el KNN puede ser algo de los vecinos vecinos

**[0:23:36]** claro que por cercanía y ahí si se clasificaban o se etiquetaban igual de la misma manera

**[0:23:45]** si entonces el KNN son los cada vecinos más cercanos y los cada vecinos más cercanos lo que

**[0:23:53]** hacen es que buscan cada vecino más cercano y tú defines K a priori y tú podrías decir K igual a 3

**[0:23:59]** por ejemplo y busco los tres vecinos más cercanos y aso y asigno una etiqueta relacionada con esos

**[0:24:07]** vecinos entonces por ejemplo mi mouse digamos que nuevamente el punto que quiero clasificar si

**[0:24:14]** estoy acá los tres vecinos más cercanos serían este este y este y en este caso lo que

**[0:24:20]** estoy diciendo entonces hay tres triángulos 100 por ciento probabilidad que sea triángulo y si yo

**[0:24:26]** quiero después clasificar algo por acá y digo tres los tres más cercanos serían este este y este y

**[0:24:32]** son hay son tres círculos entonces hay un cien por ciento probabilidad de ser círculo ahora lo que

**[0:24:37]** ocurre es que pasa cuando uno está al medio y si yo estuviese por acá digamos por acá

**[0:24:42]** para que sea un poco más fácil yo digo bueno los tres más cercanos de un círculo y dos

**[0:24:48]** triángulos y en ese caso lo que uno dice es bueno hay una probabilidad de dos de tres o sea un 66

**[0:24:56]** coma 6 periódico por ciento de probabilidad de que sea un triángulo y hay un 33,333 por ciento

**[0:25:05]** de probabilidad de que sea un círculo ese un vecino son los modelos de vecinos más cercanos

**[0:25:11]** ahora vamos a ir con los modelos lineales por ahora que creo que son muy intuitivos porque

**[0:25:22]** básicamente están pidiendo el espacio 2 entonces el modelo lineal como por excelencia más famoso

**[0:25:30]** es lo que se llama el support vector machine que quiere decir máquina de soporte vectorial y lo

**[0:25:37]** que hace que define ciertos vectores o ciertos puntos cuando digo un vector estoy hablando como un

**[0:25:42]** punto en el espacio parámetro entonces define algunos estos puntos como vectores de soporte y

**[0:25:49]** en la práctica lo que hace es que define digamos que este es el modelo lineal y busca el triángulo

**[0:25:54]** más cercano y el círculo más cercano entonces para hacer eso primero a uno de los objetos le

**[0:26:01]** ponemos la etiqueta más uno y a la otra etiqueta al otro objeto le pongo la etiqueta menos uno

**[0:26:08]** entonces esto es solamente una como se dice una herramienta matemática para poder ajustar el

**[0:26:16]** modelo entonces si yo pongo los círculos como más uno y los triángulos como menos uno después

**[0:26:22]** lo que trato a hacer es buscar cuáles son los puntos que son círculos y perdón el círculo más

**[0:26:29]** cercano y el triángulo más cercano que sería hasta acá y entonces lo que hago es que calculo

**[0:26:36]** las distancias desde el modelo lineal que está acá hacia esos círculos hacia esos vectores

**[0:26:45]** de soporte perdón entonces hacia el círculo y hacia el triángulo y hago como una hago como un plano

**[0:26:52]** paralelo a ese como está acá y está acá y hago otro plano paralelo que está acá al al al modelo

**[0:26:59]** lineal hasta acá se entiende todavía no sé porque estoy haciendo esto pero le voy a explicar al

**[0:27:08]** tiro entonces pues lo que uno hace es que calculo el margen que cuánto cuánto es cuál es la distancia

**[0:27:18]** entre los dos planos definidos por los vectores de soporte esto de acá ok y lo que trato a hacer

**[0:27:25]** es de maximizar esa distancia ok quiero que esa distancia sea lo más grande posible ok antes

**[0:27:33]** de ir a la matemática quiero que piensen por ejemplo si tuviéramos el modelo verde o el

**[0:27:39]** modelo azul el modelo azul es más fácil el modelo azul la distancia es menor a su potencial

**[0:27:45]** de vectores soporte este sería uno de los vectores soporte del modelo azul este acá y esta acá sería

**[0:27:52]** el otro vector de soporte y la distancia si yo dibujara los planos acá que no sé si sume

**[0:27:57]** permite dibujar ya entonces si yo calcular a los planos acá sería uno así y el otro sería

**[0:28:13]** como así cierto más o menos y esta distancia es más pequeña que voy a hacer otro que está acá

**[0:28:29]** que está acá no es esa distancia más pequeña que está acá entonces el fondo uno puede mostrar

**[0:28:42]** matemáticamente que al maximizar la el margen esta distancia entre las entre las dos distintas

**[0:28:51]** entre los dos planos definió por los por los vectores soporte al maximizar esa distancia

**[0:28:57]** entonces lo que hace es que divide el espacio tal forma que los puntos más cercanos que

**[0:29:03]** en al aire que las coordenadas más cercanas del espacio se acerquen correspondan a las clases

**[0:29:12]** más cercanas podría podría decir profesor que es como es como un barrio y los azules son

**[0:29:20]** casas los rajos son casas y lo que está entremedio una calle que separa ambos barrios y si quiero volver

**[0:29:25]** a construir una una casa tengo que esperar a que el espacio sea igual o el margen sea igual para separar

**[0:29:31]** ambos barrios eso es como el esperado haciendo una analogía muy parecido es muy parecido a esa

**[0:29:36]** la es una muy buena analogía y ahora no sé cómo correr estas muy así ya ok juan tiene la

**[0:29:52]** mano en alta si profesor me escucha si me queda una duda respecto a lo que habíamos visto en

**[0:30:03]** principio que era de la variable numérica y variables categóricas en este caso estaríamos

**[0:30:08]** hablando de variables categóricas cierto si y si es así no sé si lo vamos a ver más adelante como

**[0:30:15]** es que uno puede ajustar un modelo lineal por ejemplo en este caso cuáles son las consideraciones que

**[0:30:20]** uno podría tener para poder decir ya está pendiente la amarilla por ejemplo está siendo

**[0:30:27]** aplicada la la puedo hacer visualmente elegir un punto no en general es concepto de un ejemplo

**[0:30:37]** como para poder mostrar de manera pictórica lo que lo que hace el algoritmo por detrás pero en general

**[0:30:43]** yo no tengo dos atributos sino que tengo no sé 100 atributos entonces no puedo graficar así de

**[0:30:49]** que uno que 2 x 3 y 4 y 5 y 6 hasta x 100 hay técnicas de reducción de dimensionalidad que

**[0:30:57]** van a ver más adelante que te ayudan a hacer ese tipo de cosas pero en la práctica si yo quiero ajustar

**[0:31:03]** el modelo no puedo ajustarlo así no más entonces lo que uno hace por ejemplo en el caso del

**[0:31:08]** support vector machine es que transformo las categorías un número que el más uno y el menos

**[0:31:13]** uno categoría numérica sin pero después les voy a mostrar es o sea cinco minutos les

**[0:31:22]** voy a mostrar cómo sé por qué hago eso no solamente es que no para mí no es como muy

**[0:31:30]** intuitivo por ejemplo si yo tengo un grupo de menos uno asociado acá como el eje x digamos tiene

**[0:31:36]** ya por ciento valores en el espacio entonces como que no me calza el lo uno agrupado en una

**[0:31:45]** parte lo menos un agrupado en otra parte y con el eje x entonces no me imagino cómo uno puede hacer

**[0:31:49]** una justicia y la de ese tipo de distribución en el plano eso es lo que hay en este caso lo

**[0:31:58]** que estamos viendo acá son tres valores estamos viendo el valor de x1 ese uno el valor de x2

**[0:32:06]** es el segundo y hay un tercer valor que es la etiqueta que está representada con un más uno y un

**[0:32:11]** menos uno todo estos son valores numéricos actualmente en esto que estamos viendo aquí

**[0:32:19]** y lo que dice es que la cuando hablo de categorías variables categorías estoy diciendo que lo que

**[0:32:24]** quiero predecir es una variable categóricas entonces quiero predecir un triángulo y un

**[0:32:31]** círculo pero no estoy diciendo que x1 x2 sean categorías en este caso son numéricas

**[0:32:39]** aclaro hay un poco más entonces claro la la el ajuste es el lineal que estamos viendo no

**[0:32:49]** vemos función de la variable x1 y x2 sino que de lo entonces lo que tengo que hacer de

**[0:33:00]** alguna forma es calcular esta distancia entre estos dos entre estos dos hiperplano

**[0:33:06]** en realidad son en este caso son lineas rectas pero cuando uno habla de múltiples dimensiones son

**[0:33:12]** planos en alta dimensionalidad y eso uno le llamo un hiperplan entonces ahora le voy a explicar

**[0:33:18]** más o menos la matemática detrás de esto y básicamente lo primero que uno hace dice este

**[0:33:24]** va a ser un modelo lineal y acá estoy hablando de variables vectoriales entonces x que está

**[0:33:32]** como negrita es x1 y x2 y doble de es un vector de parámetro de dos dimensiones doble de

**[0:33:40]** un y doble de dos y los múltiples le hago el producto punto y le resto una variable constante un

**[0:33:47]** valor constante que es b y esto acá está como la forma genérica para definir un hiperplano porque

**[0:33:53]** si lo defiero así x puede tener cualquier dimensionalidad y doble puede tener cualquier

**[0:33:58]** dimensionalidad lo que hago es que defino también al mismo tiempo este hiperplano acá

**[0:34:06]** como doble de por x menos b que tiene que ser igual a uno y el de acá defino que doble de por x

**[0:34:14]** menos b igual a menos uno en realidad doble de punto x porque son vector y acá lo que hice fue definir

**[0:34:23]** trae hiperplano que pueden ser de cualquier dimensión que uno quiera actualmente son

**[0:34:27]** de dos dimensiones porque tengo aquí uno y aquí todo ok y entonces lo que hago es súper simple

**[0:34:34]** trato de medir la distancia entre este plano acá y este plano acá puedo calcular la distancia y

**[0:34:41]** esta distancia la distancia entre dos planos paralelo es dos sobre el módulo doble de ok

**[0:34:48]** y entonces lo que yo quiero hacer es transformar esto en un problema de optimización y lo que hago

**[0:34:54]** es maximizar dos sobre el módulo doble de o sea trato de maximizar esta distancia y eso

**[0:35:00]** es equivalente a minimizar el módulo doble o sea si estoy maximizando uno sobre el módulo

**[0:35:06]** doble de exactamente lo mismo que minimizar el módulo doble de ok y entonces minimizo el módulo

**[0:35:14]** doble de pero fíjense esta restricción para lo que recuerdan algo de optimización en alguna

**[0:35:21]** parte tengo que poner una restricción y la restricción es que esto tiene que estar

**[0:35:26]** sujeto a que y por doble de por x y menos b sea mayor igual que uno qué quiere decir

**[0:35:34]** esta restricción no se lo pudo fíjense que x y es cada uno de los puntos acá de todo acá y

**[0:35:45]** esto de acá entonces lo que estoy diciendo es que acá en esta zona doble por x menos b va a ser

**[0:35:54]** igual a cero en esta zona doble por si por este plano doble por x menos b va a ser igual a uno

**[0:36:02]** cierto entonces lo que estoy diciendo es que si yo no no mirar a este y de allí primero lo que

**[0:36:09]** estoy diciendo es que para todos los círculos doble punto x y menos b tiene que ser mayor

**[0:36:15]** igual que uno entonces estoy diciendo que aquí pa ya si yo evaluó doble por el punto x y menos b

**[0:36:25]** me tiene que dar mayor que uno entonces básicamente lo que estoy diciendo de aquí para ya al aplicar

**[0:36:31]** el modelo todo tiene que ser mayor que uno y qué pasa al otro lado al otro lado yo digo doble

**[0:36:40]** punto x y menos b por y ahí tiene que ser mayor igual que uno pero y ahí que es la etiqueta acá es

**[0:36:49]** menos uno entonces qué estoy diciendo con esto si esto es menos uno qué estoy diciendo con esto

**[0:36:55]** como que tienen que estar realmente agrupados como cada categoría si pero matemáticamente

**[0:37:09]** qué es lo que tiene que pasar acá tiene que ser que tiene que ser negativo

**[0:37:14]** entonces lo que estoy diciendo es de aquí hacia allá todo tiene que ser negativo de aquí hacia

**[0:37:21]** acá todo tiene que ser positivo entonces si yo tengo este modelo ajustado que es básicamente un

**[0:37:28]** problema optimización lo optimizo y obtengo los doble si yo tengo este modelo ajustado

**[0:37:34]** entonces lo único que tengo que hacer es poner calcular doble de punto x menos b si es mayor que

**[0:37:42]** uno es de la clase positiva entre mí y si es menor que uno es de la clase negativa si lo de

**[0:37:50]** en centro lo de en medio fuera un caudal diría como ninguna casa se puede construir cerca del

**[0:37:56]** caudal del río una cosa así como vamos a construir casa en el caudal del río no te

**[0:38:02]** preocupa vamos para allá vamos a construir casa y cristian hace una duda entonces y ahí

**[0:38:14]** el la b que era un valor de un valor constante es para poder mover digamos el plano porque si

**[0:38:24]** no te ha quedado siempre en el en el origen y lo calcula entonces bueno el punto punto en doble

**[0:38:36]** y aquí eran como los vectores directores de directores de esos planos no doble de doble de

**[0:38:48]** esos los parámetros que quiero ajustar se acuerdan cuando ajustamos la regresión teníamos

**[0:38:51]** de tabul de tabula acá los doble son esos parámetros que hay que ajustar

**[0:38:58]** pero tienen que ver con la con algo de la recta

**[0:39:04]** lo que pasa es que está a ver voy a escribir un poquito

**[0:39:13]** entonces lo que pasa lo que estoy haciendo acá cuando yo digo doble de punto x esto es lo

**[0:39:22]** que lo que estoy diciendo es que voy a tener un parámetro o sea un vector lo voy a poner esto como

**[0:39:27]** para que se vean que son victoria esa flechita ría entonces estoy diciendo que voy a tener doble de

**[0:39:31]** uno y digamos que en este caso son dos son dos dimensiones y doble de 2 punto x1 y 2 y el

**[0:39:46]** producto punto lo que me haré doble de uno por x1 más doble de dos por x2 si y si se fijan esto

**[0:40:04]** acá es un modelo lineal ahora le sumo el b por acá bueno en alguna parte que pone hay que sumarle

**[0:40:11]** el b entonces voy a poner por acá b más esto y entonces acá me suma un b y acá también suma

**[0:40:19]** un b y entonces esto me hace un modelo lineal en este caso es un modelo lineal entre x1 y x2

**[0:40:28]** porque lo que voy a hacer es quédense que esta línea de acá la línea sólida hace doble por x

**[0:40:35]** menos b e igual a cero y entonces yo digo esto e igual a cero y entonces tengo dos variables x1

**[0:40:45]** y x2 y estoy diciendo que son igual a cero entonces me hace una línea recta se entiende

**[0:40:53]** ahora esto lo hice en dos dimensiones acá como les decía para mostrarlo de manera

**[0:41:00]** pictórica pero en la práctica yo lo esto mismo lo puedo hacer en n dimensiones no puedo hacer en 100

**[0:41:06]** dimensiones mil dimensiones si quiero rofe y que depende del problema que usted utilice más

**[0:41:18]** dimensiones de la complejidad las dimensiones son el número de atributos que uno tenga

**[0:41:23]** a claro que estoy midiendo no sé imagínense vamos a los perre los gatos que para mí es fácil

**[0:41:30]** tengo el tamaño del animal y tengo el tamaño de la oreja pero podría decir no sé el color podría

**[0:41:37]** decir la altura el peso no sé el tamaño de las piernas puedo empezar a ponerle más y más atributos

**[0:41:47]** y a medida que le voy poniendo más y más atributos entonces se empieza a ser

**[0:41:53]** se empieza a crecer la dimensionalidad del problema

**[0:41:55]** hay más preguntas

**[0:42:07]** pero se yo tenía una consulta volviendo al ahorita cuando hablaba hablores

**[0:42:13]** de que esta línea finalmente buscan maximizar la distancia entre las coordenadas

**[0:42:24]** y esto en este caso más cortana entre las diferentes clases entonces claro el súper

**[0:42:34]** perfecto en la mente se basa en que entre más grandes la distancia el modelo mejor ahí metió

**[0:42:42]** si cuando se puede mostrar matemáticamente que no lo vamos a hacer en esta clase pero se puede

**[0:42:49]** mostrar matemáticamente que bajo cierto supuesto de la distribución de los datos

**[0:42:53]** ok cuando tú tienes cuando maximiza este margen el equivalente a que los puntos más cercanos

**[0:43:03]** del espacio parámetro estén o sea que los puntos todos los puntos del espacio parámetros estén

**[0:43:08]** divididos de tal forma que estén más cerca de su clase entonces básicamente lo que hace que

**[0:43:17]** si yo tengo un punto por acá lo más probable es que sea círculo porque porque está más cerca a la

**[0:43:25]** distribución de los círculos y si tengo un punto que está por acá lo más probable es que sea

**[0:43:31]** triángulo porque está más cerca la distribución de los triángulos el supo del vector machina

**[0:43:39]** así como para darle un poco de historia así como el era como el modelo matemático más

**[0:43:49]** utilizado alrededor del año 2000 yo iría y es porque matemáticamente es muy puro es fácil de

**[0:43:56]** demostrar cosas con ellos con el supo del vector machina y además es fácil de ajustar es rápido

**[0:44:01]** no uno ajusta rápidamente porque solamente tiene que resolver este problema de optimización que

**[0:44:08]** en la práctica se se resuelve de manera numérica sobre todo cuando aún no se reclusan los datos

**[0:44:15]** cuando como alguien decía uno construye una casa al río ya entonces ahora imagínense que ustedes

**[0:44:25]** tienen su modelo ya pero yo quiero evaluarlo quiero saber que también lo hace mi modelo entonces pueden

**[0:44:32]** pasar cosas como esta miren lo que pasó acá tenemos dos triángulos que están en la zona de los

**[0:44:39]** círculos y un círculo que está en la zona de los triángulos en principio yo podría decir ya

**[0:44:48]** ok lo vamos a ver después pero le voy a dar un spoiler yo podría decir bueno pero que

**[0:44:54]** ese modelo no es muy bueno yo iría a hacer algo como así y así iría a hacer mi modelo

**[0:45:02]** pero hay un problema acá cuál problema de este modelo lo vamos a ver más adelante pero

**[0:45:09]** quiero ver si alguien tiene la intuición no generaliza no generaliza exacto si me aparece algo

**[0:45:15]** acá va a decir mi modelo que un triángulo y entonces de alguna forma lo por eso yo les decía

**[0:45:22]** los modos siempre no tener errores ok y de alguna forma yo tengo que medir esos errores

**[0:45:30]** entonces para medir los errores uno generalmente lo que hace es que parte diciendo uno de los

**[0:45:40]** objetos los voy a llamar positivos y los otros objetos los voy a dar los voy a llamar

**[0:45:45]** negativos y no es que a mí me gustan más los círculos que los triángulos es como la convención

**[0:45:50]** y uno y si uno dice bueno los positivos van a hacer ahora los triángulos y los negativos los círculos

**[0:45:56]** también funciona todo funciona perfecto son son un día las mismas conclusiones

**[0:46:02]** entonces si yo digo que los círculos son positivos los triángulos son negativos

**[0:46:06]** yo puedo decir tengo los positivos reales primero que lo voy a llamar p en este en este

**[0:46:13]** caso cuántos p cuántos cuántos el número de positivos reales

**[0:46:24]** siete siete exacto son hay siete círculos los negativos reales lo voy a llamar n cuántos

**[0:46:33]** son los negativos reales acá los verdaderos positivos voy a llamar a los positivos que

**[0:46:49]** fueron correctamente clasificados como positivos cuántos son los verdaderos positivos

**[0:46:58]** entonces yo miro qué es lo que clasificó el modelo como positivos clasificó todo esto

**[0:47:05]** acá como positivos y cuáles de esos son verdaderos positivos son 1 2 3 4 5 6 los verdaderos

**[0:47:15]** negativos son los negativos correctamente clasificados cuántos son 7 7 1 2 3 4 5 6 7

**[0:47:25]** los falsos positivos son los negativos que fueron incorrectamente clasificados como positivos

**[0:47:35]** cuántos negativos clasificados como positivos también está haciendo así 2 yo pensé que está

**[0:47:45]** haciendo amor y paz y los falsos negativos son los positivos que fueron clasificados

**[0:47:52]** correctamente como negativo y es uno solo que sería está acá entonces ahora que ya

**[0:48:00]** sabemos todo esto nos vamos a mariar un poco más y vamos a medir distintos tipos de cosas sobre el

**[0:48:06]** modelo entonces lo primero son es la exactitud la exactitud del porcentaje de objetos que fueron

**[0:48:12]** clasificados correctamente en otras palabras son los verdaderos positivos más los verdaderos

**[0:48:18]** negativos divididos por los positivos negativos entonces eso es como lo obvio así como voy

**[0:48:24]** a calcular qué porcentaje de objetos fueron correctamente clasificados el error es

**[0:48:30]** como un inverso entonces uno dice qué porcentaje fueron incorrectamente clasificados entonces son

**[0:48:36]** los falsos positivos más los falsos negativos sobre los positivos más los negativos los positivos

**[0:48:41]** más los negativos del total de objetos la tasa de verdaderos positivos que en inglés se le llama

**[0:48:48]** recall y que generalmente uno dice el recall porque cuando uno lo codea el librería está

**[0:48:56]** entonces uno se acostumbra a decirle recall la tasa de verdaderos positivos es los verdaderos

**[0:49:02]** positivos sobre los verdaderos positivos más los falsos negativos y se fijan los verdaderos

**[0:49:08]** positivos son estos acá los falsos negativos este acá entonces se fijan cuando digo los verdaderos

**[0:49:15]** positivos más los falsos negativos son los positivos totales entendieron lo que acabas

**[0:49:22]** entonces estoy diciendo de los positivos totales cuántos fueron correctamente clasificados la precisión

**[0:49:29]** es qué porcentaje de lo que fue clasificado como positivo realmente era positivo entonces son los

**[0:49:37]** verdaderos positivos sobre los verdaderos positivos más los falsos positivos entonces básicamente

**[0:49:44]** estoy diciendo todo lo que fue clasificado todo lo que está acá todo lo que fue clasificado

**[0:49:48]** acá como positivo qué porcentaje de eso es un verdadero positivo sermán si profesor puede

**[0:50:00]** que esté confundiendo concepto así que es para seguir de la udo más que nada que yo recuerdo que

**[0:50:06]** algún momento cuando vi cuando vi esto se hablaba de sensibilidad de especificidad y también

**[0:50:10]** salió en la medida de confusión eso es lo mismo son conceptos distintos está adelantando

**[0:50:15]** ya desculpe no la intención no se entiende la diferencia entre la tasa verdaderos positivos

**[0:50:27]** y la precisión creo que eso es súper importante porque mieden dos cosas distintas aunque se

**[0:50:33]** parecen mucho la precisión dice mi modelo me dijo que todo esto era positivo qué porcentaje lo

**[0:50:41]** que me dijo mi modelo que la positivo realmente es positivo el recall o la tasa verdaderos

**[0:50:46]** positivos me dice de todos los positivos que realmente eran positivos qué porcentaje fue

**[0:50:52]** capaz de recuperar mi modelo como positivo entonces voy a poner un ejemplo imaginemos que tenemos

**[0:51:02]** una máquina que está y tú que tiene un modelo que te hace detección de anomalías y te detecta

**[0:51:11]** anomalías la anomalía pasa un poquito o sea que detecta cuando la máquina va a fallar la

**[0:51:16]** cuando las fallas pasan poco de una cada mil emisiones de la máquina por decir algo

**[0:51:25]** entonces una de cada mil es una falla pero yo quiero predecirla entonces imagínense que ustedes

**[0:51:31]** tienen un recall del 100 por ciento pero tienen una precisión del 70 por ciento qué quiere decir

**[0:51:42]** eso yo voy a decir que la falla es positivo la falla cuando falla es positivo entonces tengo

**[0:51:51]** un recall del 100 por ciento qué quiere decir un recall del 100 por ciento todo lo que predice

**[0:52:02]** todas las fallas que predice son esos fallas reales todas las fallas que predice son fallas

**[0:52:12]** reales tan de acuerdo yo lo diría otra forma que se cruza los cales pero de que si si es positivo

**[0:52:28]** siempre decir que es positivo y si es positivo nunca decir que negativo realmente tan de acuerdo con

**[0:52:34]** eso entonces estoy diciendo el 100 por ciento de las veces esto es 100 por ciento igual entonces

**[0:52:46]** lo verdad es positivo igual en los positivos a siempre siempre es positivo de forma real

**[0:52:56]** nunca se equivocan a la predicción pero yo estoy diciendo que esto es igual aún cuánto

**[0:53:04]** dije 50 70 70 70 esto un 70 por ciento entonces lo que estoy diciendo que creo que van con una

**[0:53:19]** dirección correcta pero después se devuelven es que todas las fallas son correctamente predichas

**[0:53:31]** no en o sea cada una de las fallas siempre que hay una falla el modelo la encuentro

**[0:53:45]** cierto y ustedes pueden decir buenísimo vamos pero si yo le digo que hay una falla a cada mil

**[0:53:53]** entonces lo que estoy diciendo es que esto acá es igual a sobre uno es la falla

**[0:54:05]** cierto se encontré la falla ya pero yo le estoy diciendo que hay una falla cada mil no fallas

**[0:54:17]** o una falla dentro de mil entonces qué pasa con este con esta precisión qué quiere decir este 70

**[0:54:27]** por ciento profesor tal vez estoy confundiendo un poco pero yo estuve hoy revisando un poco y hay un

**[0:54:42]** modelo que se llama y me ha sentido con lo que está diciendo esto no sé si lo estoy pronunciando

**[0:54:46]** bien a cuas a cuasi algo así que por ejemplo tenemos 100 datos ya de esos 100 datos hay 20

**[0:55:01]** datos por ejemplo que no cumple pero un por un tema de desbalanceo y siempre va a decir

**[0:55:07]** que todo cumple es como eso algo parecido está está yendo mucho más adelante lo que lo

**[0:55:15]** que yo estoy preguntando mucho más simple eso es mucho más complejo lo vamos a hablar un poquito

**[0:55:22]** más adelante de las fallas que predigo son 100 por ciento cientos pero del total de fallas

**[0:55:32]** predigo un 70 por ciento porque lo que estoy diciendo es esto va a ser igual a uno sobre

**[0:55:41]** 7 y esto es igual el yo estoy diciendo los verdaderos positivos son 1 entonces esto quiere

**[0:55:51]** decir que hacer 1 sobre 1 más 6 y entonces estoy diciendo que aparecen 6 falsos positivos

**[0:56:02]** entonces de estos mil datos me aparecieron 6 falsos positivos entonces tuve yo el modelo

**[0:56:15]** me dijo va a fallar la máquina y yo freno la máquina y digo parem parem parem parem

**[0:56:20]** y el 20 y 6 de esas veces no es real sólo una en el entiendo lo que estoy diciendo pero lo que

**[0:56:35]** acaba de decir con el gráfico que estamos de los colores vendría haciendo los azules a ver los

**[0:56:44]** paré esas seis veces por ejemplo la azul que está en los negativos me equivocé perdón me

**[0:56:56]** quedó que me quedó que le hice al revés disculpa disculpa que me quedó que demasiado feo

**[0:57:06]** esto es 7 sobre 10 ahí sí me quedó que lo hice lo hice terrible perdón entonces lo que

**[0:57:20]** estoy diciendo es que sé que yo tuviese 7 falsos verdaderos positivos ya de esos van a

**[0:57:29]** ver 3 falsos positivos en este caso disculpa disculpa dije al re me equivocé creo que creo

**[0:57:42]** que francisco va a preguntar justo lo que voy a preguntar yo no sé si puede continuar

**[0:57:45]** ahí sí culpa francisco finalmente era si lo llevamos el graficito de los colores tendríamos

**[0:57:54]** tenemos 7 círculos azules que son los profirios uno está dentro los negativos por

**[0:58:04]** en esa falla hablábamos de lo que es del ejemplo vendría siendo ese azul que están los negativos

**[0:58:13]** pero que yo sabía que iba a estar allá yo predijo que estar ahí tú predijiste el modelo predijo

**[0:58:24]** que iba a estar acá claro que porque si ese azul hubiese sido un triángulo por ejemplo eso

**[0:58:35]** vendría siendo un falso negativo y ok si ok tengo que avanzar un poco más rápido pero en ese

**[0:58:52]** ejemplo cuáles cuáles son verdaderamente positivos los azules o los rojos acá estos todos los

**[0:59:00]** azules son positivos estos son los positivos o sea ahí en ese caso serían dos falsos dos falsos

**[0:59:07]** positivos eso es lo que está diciendo como los triángulos son dos falsos positivos exacto esto

**[0:59:13]** un falso positivo y es otro falso y como se lee el otro término que dijo verdaderos positivos

**[0:59:20]** en ese caso en ese ejemplo cuál sería un verdadero positivo que coincida otra vez un

**[0:59:25]** los verdaderos positivos son estos son los verdaderos positivos estos acá son los verdaderos

**[0:59:45]** negativos con rojo este acá es un falso negativo porque debería ser positivo pero falsamente se

**[0:59:58]** disfrazó de negativo y estos dos de acá son los falsos positivos la tasa de falsos positivos son

**[1:00:23]** los falsos positivos sobre los falsos positivos más los verdaderos negativos entonces lo que estoy

**[1:00:28]** diciendo es los falsos positivos que son estos acá más los verdaderos negativos que son los

**[1:00:35]** negativos entonces cuántos falsos positivos hay que sería está acá dentro del total de negativos o

**[1:00:43]** sea cuánto yo clasifique de negativo como del del total de negativo que falsamente aquí ahora

**[1:00:54]** entonces esto acá que alguien mencionó que creo que fue de priscila o alguien mencionó

**[1:01:04]** no no recuerdo que fue priscila no creo que no fue es lo que se llama la matriz de confusión

**[1:01:09]** la matriz de confusión yo creo que es una de las herramientas más útiles para saber cómo se está

**[1:01:15]** comportando mi modelo y lo que hago es que digo pongo en algunos otros ejes de lo mismo cual pongo

**[1:01:22]** cuál es la etiqueta real y cuál es la etiqueta predicha entonces lo primero que digo es la etiqueta

**[1:01:27]** real era círculo y la etiqueta predicha es círculo si yo veo acá deberían haber 1 2 3 4 5 6

**[1:01:35]** cerco entonces pongo acá y me haceis después digo la etiqueta real es un triángulo y la etiqueta

**[1:01:45]** predicha en un círculo entonces son triángulos que yo predije como círculo y son dos estos dos

**[1:01:51]** de acá cuántos hay acá en esta zona acá que me pude ser que número diría ir ahí

**[1:02:02]** cerco y quién número diría ir acá 2 7 7 7 porque son los triángulos que fueron predichos como

**[1:02:19]** triángulos fíjense que con esto yo inmediato puedo calcular todo lo que habíamos hablado en antes

**[1:02:25]** con esta matriz puedo calcular todo lo anterior ok el 6 y además lo que me dice es de inmediato

**[1:02:35]** yo entiendo la confusión si yo podría poner más clases acá podría poner no sé un rombo un

**[1:02:41]** cuadrado lo que sea y esto lo que me dice es qué se está confundiendo con qué cosa y me da una

**[1:02:48]** intuición de por qué podría hacer eso entonces seguramente los gatos van a confundir con los

**[1:02:54]** perros más que con una serpiente por ejemplo porque son más parecidos ok ahora vamos a

**[1:03:03]** hablar de los modelos más complejos y yo les decía el modelo lineal que vimos delante es un

**[1:03:09]** modelo relativamente simple pero yo podría en la práctica usar modelos mucho más complejos como

**[1:03:15]** por ejemplo una red neuronal la red neuronal es que son las que se usan hoy en día son muy complejas

**[1:03:21]** y entonces yo podría decir mira acá tengo mi modelo perfecto ok pero como lo vimos delante qué

**[1:03:29]** pasaría si que aparece un objeto por acá qué tipo objeto de ese ser un triángulo un círculo

**[1:03:34]** un círculo porque está más cerca los círculos entonces para medir cómo un modelo si un modelo

**[1:03:43]** está sobre ajustado no qué es lo que puedo hacer hay valer esa encruzada hay que guardar

**[1:03:51]** algunos datos es variación cruzada y hago exactamente lo mismo que hice con regresión tengo

**[1:03:59]** los distintos tipos de de variación cruzada que puede ser el k-fold el shuffle split y el bootstrapping

**[1:04:04]** y puedo medir todo lo que yo quiera de manera de saber si es que no es capaz el modelo generalizar

**[1:04:10]** generalizar en términos del precision o de la tasa falso positivo o en función de la exactitud

**[1:04:17]** o del error puedo medir todo eso usando variación cruzada otra cosa que uno hace mucho es que

**[1:04:25]** los modelos generalmente tienen cierto parámetro de sensibilidad el más clásico es cuando un

**[1:04:31]** modelo te predice una probabilidad entonces imagínate que te dice tengo una probabilidad de

**[1:04:35]** 0,9 por ciento de ser un perro y 0,10 por ciento es perdón 90 por ciento de ser un perro y un 10

**[1:04:43]** por ciento ser un gato que creen ustedes que es un perro un gato según el número que la probabilidad

**[1:04:57]** es mayor perro el perro tiene un 90 por ciento probabilidad de ser un o sea el animal tiene

**[1:05:07]** 90 por ciento de ser un perro entonces suena como razonable que 10 de tener que 10 de ser un perro

**[1:05:12]** ok ahora qué pasa si el modelo le dice tengo un 50 por ciento de ser un perro y un 50 por ciento

**[1:05:21]** de ser un gato qué es espero que gata la vez entonces fíjense que hay hay algo detrás de

**[1:05:39]** esto que le acabo de decir que cómo tomo yo la decisión de decir un perro un gato y en general

**[1:05:45]** uno dice bueno voy a general generar un umbral y el umbral es un 50 por ciento mi cabeza siempre

**[1:05:52]** el umbral como un 50 por ciento está mi perro reclamando porque le dije gato entonces el umbral

**[1:06:01]** siempre un 50 por ciento o en mi cabeza generalmente un 50 por ciento pero no tiene porque

**[1:06:08]** ser un 50 por ciento podría ser un 55 o un 60 y lo que ocurre es que este umbral me ayuda a mover

**[1:06:19]** el modelo y eso es lo que está representado acá imagínense que yo tengo este modelo acá y yo

**[1:06:24]** bajo el umbral de probabilidad o lo subo entonces empieza a moverse el modelo no empieza a moverse

**[1:06:30]** hacia un lado y el otro entonces yo podría hacer lo que podría hacer es calcular la tasa

**[1:06:37]** de verdadero positivo y la tasa de falsos positivos y por ejemplo si lo hago acá la tasa de verdadero

**[1:06:42]** positivo es de 0.3 y la tasa de falsos positivos de 0.0 entonces pareciera como que yo digo wow que

**[1:06:49]** buena tasa de falsos positivos o sea no tengo ningún falso positivo estupendo pero espérate yo

**[1:06:56]** digo pero la tasa de verdadero positivo no es muy buena porque se te está yendo el 70 por ciento

**[1:07:01]** de los positivos negativos entonces digo ya ok lo muevo un poquito más y ahora acá la tasa de verdadero

**[1:07:07]** positivo es de 0.6 y la tasa de falsos positivos es de 0 ok espérate que tengo que mi perro está

**[1:07:16]** ladrando acá al lado la tengo que ir a echar ya disculpa entonces acá yo diría cuál de los

**[1:07:40]** dos modelos está mejor bueno claramente el de la derecha porque la tasa de verdadero

**[1:07:45]** positivo es más alta que el de la izquierda y la tasa de falsos positivos se mantuvo igual

**[1:07:48]** entonces yo digo ya ahora sí me quedo con esto y digo bueno pero no me gusta tu tasa de verdadero

**[1:07:53]** positivo que era una mejor tasa de verdadero positivo entonces muevo de nuevo el umbral

**[1:07:57]** y ahora te queda una tasa de verdadero positivo de 0.8 y ahí ustedes me dicen bien

**[1:08:02]** tasa de verdadero positivo 0.8 esa es la que yo quería y le digo ya pero hay un problema que la

**[1:08:08]** tasa de falsos positivos empezó a aumentar ahora entonces tengo una mayor tasa de falsos

**[1:08:13]** positivos y ustedes dicen no no no pero pero ya no está terrible no está terrible el

**[1:08:18]** pero quiero una mayor tasa de verdadero positivo quiero llegar al 100% de la tasa de verdadero

**[1:08:23]** positivo entonces yo lo vuelvo a subir a cambiar el umbral y digo ya llegué a la tasa de verdadero

**[1:08:29]** positivo del 100% pero ahora la tasa de falsos positivos de 0.6 entonces si se fijan empieza

**[1:08:36]** uno como a balancear entre verdadero positivo y falsos positivos y empieza como a model

**[1:08:42]** el umbral y tiene que definir de alguna forma lo que se llama el punto de operación del modelo

**[1:08:46]** cuál es el umbral que tú vas a usar al momento de poner esto en producción y esto acá si se

**[1:08:53]** fijan estos numeritos de acá yo podría ser como un gráfico donde tenga la tasa de verdadero

**[1:08:58]** positivo en función de la tasa de falsos positivos y eso lo que se llama la curva rock que quiere

**[1:09:05]** decir receiver operating characteristic y entonces para estos mismos valores de acá si se fijan

**[1:09:12]** acá tengo el false positive rate la tasa de falsos positivos acá tengo la tasa de verdadero

**[1:09:17]** positivo y pongo gráficos estos mismos números entonces la tasa de verdadero positivo acá de 0.3

**[1:09:23]** está por ahí la tasa de falsos positivos está en cero y fíjense que empieza a ver como un trade

**[1:09:30]** off donde me gustaría estar a mí donde cual en qué parte de este gráfico quiero que esté

**[1:09:34]** mi modelo ahí no era el codo lo que se elegía estáis perdidos de nuevo pero asumamos

**[1:09:49]** que no tengo un modelo donde me gustaría que estuviese no te gusta y lo más cercano a cero

**[1:10:00]** cero y en el eje y lo más cercano uno y en el eje y lo más cercano uno ese es mi modelo perfecto

**[1:10:08]** ese es mi modelo perfecto pero como yo les decía los modelos nunca son perfectos ok entonces siempre

**[1:10:15]** se ve uno puede esta otra herramienta que uno suele usar para definir el punto de operación

**[1:10:20]** del modelo y siempre se ve como algo así ahora en la práctica yo podría tener podría

**[1:10:28]** cambiar el modelo en vez de usar digamos un supor vector machine yo podría decir voy a usar otro

**[1:10:33]** tipo de lo vamos a ver otro modelo ahora se ha alcanzado y entonces yo podría usar otro modelo

**[1:10:40]** que esta curva rock se ve ir algo como así qué modelo preferiría el naranjo o el rojo el rojo

**[1:10:53]** cierto porque está más cerca del uno y en la práctica lo que uno hace es que dice mira digamos que

**[1:11:02]** voy a volver acá digamos que este es mi modelo yo tengo que definir un punto de operación si para

**[1:11:07]** mí es muy importante que la tasa de falsos positivos sea muy baja entonces yo tengo que

**[1:11:14]** estar por acá cierto pero podría ser que para mí sea muy importante tener una tasa de verdadero

**[1:11:21]** positivo alta entonces tendría que estar por acá ok y entonces siempre hay un trade off y en algún

**[1:11:28]** momento tú tienes que hacer los números de así como lo hicimos de antes de cuántas veces falla

**[1:11:32]** en la máquina o lo que sea y con ese número tú defines el punto de operación del modelo

**[1:11:39]** pero yo tengo una pregunta porque ya podríamos irnos con estos porcentajes de falsos positivos

**[1:11:50]** y todo esto esto no viene a reemplazar el error del modelo si esto es recuadrado que hablábamos

**[1:11:55]** en la vía anterior como estimador de si es bueno o porque tan bueno es el modelo

**[1:12:03]** trayectivo en este caso de clasificación si el recuadrado es una métrica que uno usa para

**[1:12:10]** medir lo errores o el porcentaje de la varianza que representa un modelo de regresión el recuadrado

**[1:12:18]** uno lo usa para regresión en este caso estamos en clasificación entonces acá ha habido distintos

**[1:12:26]** tipos de errores german si profesor aquí para yo estoy pensando si estoy teniendo el concepto

**[1:12:35]** para llevar algo más entre comidas real pasa que típico por ejemplo el examen es médico

**[1:12:42]** voy a poner el ejemplo el examen el examen de h por dar un ejemplo no más ahí lo entiendo yo que

**[1:12:48]** lo que buscan más es que la tasa verdadera es positiva sea muy alta porque después una segunda

**[1:12:54]** prueba después se hace una segunda prueba después se hace con se puede hacer un cálculo

**[1:12:57]** entero y me vayas y todo eso pero eso es como el ese con el balance que usted dice que

**[1:13:01]** que buscar exacto o sea si tú quieres por ejemplo imagínate que tiene algún examen de

**[1:13:07]** alguna enfermedad muy grave como puede ser el VIH entonces tú lo que dice es no me quiero perder

**[1:13:12]** ninguno me da lo mismo equivocarme porque si me equivoco prefiero que alguien diagnosticar

**[1:13:18]** equivocadamente para que alguien se vaya a hacer un segundo examen el segundo examen le le salga

**[1:13:22]** bien entonces yo quiero estar por acá por acá ría camilo en camilo y en ese aspecto

**[1:13:35]** no existe como un óptimo o un óptimo global o algo o algo por el estilo pensando en lograr ese

**[1:13:43]** punto de equilibrio depende de lo que yo ando buscando o puede haber un óptimo el óptimo

**[1:13:50]** al cual tú te refieres está acá pero como yo te digo ningún modelo entonces nunca llegaste

**[1:13:57]** ya hay muchos modelos que hacen esto a proposición que hacen esto y pasan aquí al

**[1:14:01]** laito ok pero el el modelo en general nunca son perfectos incluso los modelos de inteligencia

**[1:14:09]** artificial más sofisticados de hoy en día así como los modelos de lenguaje se equivocan y eso

**[1:14:15]** lo que uno dice que alucinan entonces ningún modelo es perfecto en realidad si bueno uno

**[1:14:29]** podría pensar en algún modelo muy muy poco útil que sería perfecto pero en general no lo son

**[1:14:34]** porque si no no es desafiante el problema ok vamos a ver otro modelo que se llaman los árboles

**[1:14:43]** de decisión entonces los árboles de decisión básicamente yo tengo mi mi conjunto de datos

**[1:14:52]** y acá estoy representando el número de triángulo y de círculos que hay entonces se fijan acá hay

**[1:14:57]** nueve triángulos 1 2 3 4 5 6 7 8 9 y hay ocho círculos 1 2 3 4 5 6 7 8 y lo primero que

**[1:15:07]** hago es que elijo una de estos dos atributos y divido en dos así por ejemplo ahí hizo una

**[1:15:15]** edición en dos y digo todo lo que está cuento todo lo que está hacia un lado y cuento todo lo que

**[1:15:22]** está hacia el otro lado entonces trato de que todos los círculos que en como un lado y todos

**[1:15:26]** los triángulos que en al otro por supuesto no puedo en este caso en particular entonces hago

**[1:15:32]** eso y si se fijan a la izquierda hay un triángulo un triángulo y seis círculos a la derecha hay ocho

**[1:15:40]** triángulos y dos círculos y después elijo otro atributo que puede ser por ejemplo el x2 y vuelvo

**[1:15:48]** a dividir y ahora dividido y arriba hay un círculo y un triángulo y abajo hay cinco círculos y el

**[1:15:58]** otro subconjunto que está acá vuelvo a hacer lo mismo dividido y me queda que arriba hay un círculo

**[1:16:05]** y abajo hay ocho triángulos y un círculo esto acá una arbol de decisión y lo que uno hace es que

**[1:16:12]** después cuando cuando ya se como que separó todo el espacio de atributo cuando me aparece un

**[1:16:17]** nuevo objeto digamos que me aparece un objeto por acá no se me aparece un objeto por acá

**[1:16:22]** digo a a qué corresponde eso se corresponde a este subconjunto de datos de acá y ahí en esta

**[1:16:30]** cajita están hay puro círculo entonces este punto tiene un cien por ciento probabilidad de ser círculo

**[1:16:39]** y si voy por ejemplo a acá y tengo un objeto por acá digo a dónde está esto está acá

**[1:16:52]** cierto y son puro círculo entonces también un cien por ciento probabilidad de ser un círculo

**[1:16:56]** pero si me aparece algo digamos por acá entonces digo a dónde corresponde esto hay un círculo

**[1:17:08]** y un triángulo entonces un cincuenta por ciento probabilidad de ser un círculo

**[1:17:12]** si francisco no sé consulta en ese gráfico las decisiones que realizó son

**[1:17:24]** parámetros dentro de la fórmula voy para voy para ya voy para ya les voy a explicar cómo se hace

**[1:17:32]** estoy explicando como la idea general primero pero se entiende no tengo que dividir ahora la

**[1:17:39]** pregunta es cómo dividido eso es lo que tu pregunta francisco cierto que cómo el hijo

**[1:17:43]** dividir que para de meter elegir lo que sea bueno lo que uno hace primero cómo es cojo que atributo

**[1:17:54]** utilizar y donde lo que uno hace es que intenta de hacer divisiones de tal forma que los subconjunto

**[1:18:04]** que se generen sean lo más puros posibles o sea que hayan solo objeto ojalá solo círculo a la

**[1:18:10]** izquierda y solo triángulo a la derecha o que hayan poquito poca mezcla dentro de los subconjunto

**[1:18:17]** que el hijo sé que yo pude seguir de inmediato en que todos los círculos a la izquierda y todos los

**[1:18:22]** triángulos a la derecha entonces resolver el problema de una con una sola edición ok ahora

**[1:18:29]** para hacer esto tengo que medir de alguna forma la pureza entonces vamos que estos son mis datos

**[1:18:37]** y yo hago esta división los subconjunto los subconjunto son impuros porque tengo a la izquierda

**[1:18:46]** la mitad de triángulo y la mitad de círculo y a la derecha la mitad de triángulo y la mitad de

**[1:18:49]** círculo pero esta división hace que los conjuntos sean puros que tengo solo triángulo y solo

**[1:18:56]** círculo se entiende la idea ahora la pregunta es cómo mido la pureza entonces lo que uno

**[1:19:06]** hace es que hay distintas formas de medir la impureza la iguínea es como la una de las más

**[1:19:13]** famosas que mide el error esperado si escojo aleatoriamente un objeto y se predice la clase de

**[1:19:23]** todo el conjunto basado en él no sé si entendieron esto lo voy a pasar de nuevo mido el error

**[1:19:31]** esperado si escojo aleatoriamente un objeto entonces tengo un subconjunto de datos escojo

**[1:19:37]** aleatoriamente un objeto y predigo la clase de todo el conjunto basado en él entonces ejemplo número

**[1:19:44]** 1 tengo estos datos de acá ok la probabilidad de escoger un triángulo es de 3 octavos la probabilidad

**[1:19:56]** de escoger un círculo es de 5 octavos si escojo un triángulo y después digo voy a clasificar

**[1:20:08]** todo como un triángulo el error que voy a obtener es de 5 octavos porque voy a clasificar

**[1:20:15]** incorrectamente todos los círculos cierto hasta ahí vamos bien entonces yo voy a escoger escojo algo

**[1:20:24]** así como que no veo y saco un triángulo entonces el error de clasificado todo digo ya todo el

**[1:20:30]** triángulo el error que voy a que voy a obtener es de 5 octavos si escojo un círculo el error

**[1:20:38]** de clasificar todos los puntos como círculo es de 3 octavos entonces ahora lo que yo tengo que hacer

**[1:20:45]** es medir el error esperado si se escoge aleatoriamente un objeto y se predice la clase de todo el objeto

**[1:20:53]** basado en él entonces el error esperado es la probabilidad de escoger un triángulo que es 3

**[1:21:00]** octavos por el error por haber escogido 6 de triángulo que es de 5 octavos más la probabilidad

**[1:21:08]** de escoger un círculo por el error de haber escogido ese círculo y en este caso es como de

**[1:21:15]** 0.46 esto es un conjunto relativamente impuro ok esto acá como les decía es la probabilidad de

**[1:21:23]** elegir un triángulo y esto es la probabilidad de elegir un círculo vamos a poner un segundo

**[1:21:30]** ejemplo miren esto acá este un conjunto más puro va impuro que el anterior más puro

**[1:21:41]** cierto hay un solo triángulo entonces vuelvo a hacer lo mismo la probabilidad de escoger

**[1:21:46]** un triángulo en un octavos la probabilidad de escoger un círculo es 7 octavos se c Jieca un

**[1:21:52]** triángulo el error de clasificar todos los puntos como triángulos de 7 octavos y si Erm el

**[1:21:58]** error de clasificar todos los puntos como círculo en un octavos calculo exactamente lo

**[1:22:03]** mismo acá está la probabilidad de elegir un triángulo por el error asociado a elegir

**[1:22:09]** ese triángulo acá está la probabilidad de elegir un círculo por el error y elegir

**[1:22:15]** ese círculo y entonces ahora me da 0,21. Fíjense que lo que está midiendo esto es la impureza.

**[1:22:22]** Mientras más impuro, el dataset más alto va a ser esta impureza de Ginny. Esa es la idea detrás

**[1:22:31]** de esto. En general, la impureza de Ginny, yo tengo C clases, así muchas clases más de 2,

**[1:22:40]** es la suma desde igual 1 hasta C de el número de objetos de esa clase dividido por el número

**[1:22:47]** total de objetos por 1 menos el número de esa clase partido por el número total de objetos.

**[1:22:53]** Exactamente lo mismo que hicimos delante con los triángulos círculos, pero acá está como para

**[1:22:57]** muchas clases. Entonces en este caso, ya lo habíamos calculado, la impureza era de 0,46,

**[1:23:05]** en este caso también la habíamos calculado, que es de 0,21 o 0,22. Y en este caso,

**[1:23:12]** ¿cuánto me va a dar? ¿Y por qué? ¿Quién se lo cura? Esa es 0, pero ¿por qué? Que no hay otra

**[1:23:28]** categoría. O sea, pues asumamos que hay triángulos, asumamos que los triángulos existen. Bueno,

**[1:23:36]** la probabilidad de elegir un triángulo es 0, ¿certo? La probabilidad de elegir un círculo es 1,

**[1:23:44]** pero el error por el elegir un círculo es 0, porque no hay ningún triángulo que se

**[1:23:50]** pueda transformar. Entonces esto es 0. ¿OK? Hay distintos tipos de media impureza. La impureza

**[1:23:58]** y linea es una de varias. Pero existe, por ejemplo, la entropía, que es el promedio de la información,

**[1:24:06]** en la información en promedio que contiene el experimento de sacar un dato. Y existe el

**[1:24:15]** error de clasificación, que básicamente sé que yo clasifico todo de una cierta forma,

**[1:24:21]** ¿cuál va a ser ese error? Esperamos un poquito, Camilo. Déjame terminar con esto y estoy en la

**[1:24:30]** palabra. Este es un gráfico que muestra, acá en el eje X, muestra el número objeto de una clase sobre

**[1:24:36]** el número total de objetos. Entonces, 0 quiere decir que todos los objetos son de una clase,

**[1:24:41]** en 1 quiere decir que todos los objetos son de la otra clase. Entonces, el índice guini hace

**[1:24:48]** algo como esto, llega un máximo de 0,5, la entropía hace algo como esto, llega un máximo de 1 y el error

**[1:24:56]** de clasificación hace algo como esto. ¿OK? Camilo. Sí, quería preguntar, ¿en qué contexto conviene

**[1:25:05]** más usar o es más conveniente utilizar uno y otro? Ay, qué buena pregunta, qué buena pregunta.

**[1:25:11]** ¿Alguien tiene la respuesta? Yo sé, profesor, esto es más por el lado de computación que la

**[1:25:19]** entropía, es más costosa calcular porque tiene un logaritmo, pero una respuesta netamente por

**[1:25:25]** ciencia o no sabría darla. Fíjense que esto es algo que uno escoge antes de ajustar el modelo,

**[1:25:35]** ¿cómo se llama eso? ¿En serio? Cuando yo tengo algo que tengo que escoger antes de ajustar el

**[1:25:47]** modelo, ¿cómo se llama eso? ¿Como la etapa de exploración, no? No, no, no. Es un parámetro que

**[1:25:59]** uno tiene que escoger antes de ajustar el modelo, ¿cómo se llama eso? Como el orden del polinomio,

**[1:26:06]** ¿se acuerdan? ¿Estaba el entrenamiento para la validación? Es un hiperparámetro, Camilo. Entonces,

**[1:26:18]** tú lo tienes que elegir a priori y generalmente lo que uno hace es que lo elige usando validación

**[1:26:23]** cruzada. De acuerdense que si no saben la respuesta, digan validación cruzada. No, no siempre,

**[1:26:31]** la mayor parte de las veces la respuesta es validación cruzada. Ok, se me está acabando el tiempo,

**[1:26:38]** pero quiero terminar con esto. Al final, la pregunta que sigue es, si yo ya sé dónde tengo que dividir,

**[1:26:45]** la pregunta es, entonces, ¿cómo sé cuando dejo dividir? Entonces, lo que uno tiene que

**[1:26:53]** hacer es que a medida que va dividiendo, va midiendo la ganancia de la pureza. ¿Cuánta pureza voy

**[1:26:59]** ganando a medida que voy dividiendo? Y entonces, lo que hay que comparar es la impureza al no padre,

**[1:27:05]** ¿se acuerdan que es un árbol, ¿está cierto? Entonces, la impureza al no padre en función

**[1:27:11]** contra la impureza de los no-dijo. Y esto es lo que se llama la ganancia a la impureza y que es,

**[1:27:16]** esta es la, si que yo tengo no a acá, no b acá y no c acá, es la impureza al no padre menos

**[1:27:26]** la impureza de los dos no-s hijos, pero esto está ponderado por el número de objetos que

**[1:27:32]** está en b sobre el número de objetos que está en a. O sea, si hay muchos objetos en un lado,

**[1:27:37]** esa impureza pesa más que la del otro. Ya, el algoritmo clásico de árboles de decisiones

**[1:27:50]** del C4.5 que lo que dice es, mientras no se cumpla algún criterio convergencia, para cada

**[1:27:57]** atributo calculo la ganancia de dividir en ese atributo, sea x el atributo con mayor ganancia,

**[1:28:02]** creo una decisión que separe con respecto a x y aplico este algoritmo a los subconjuntos creados

**[1:28:08]** al dividir por x. Y se converge, tú dices el algoritmo para cuando el no contiene solamente

**[1:28:17]** una clase, cuando el no contiene menos de un valor deseado de objetos, cuando se alcanza una

**[1:28:22]** altura máxima, cuando la pureza es suficiente o cuando se comienza a sobreajustar. Y ahí uno

**[1:28:28]** puede estar a media que empieza a dividir, pues están haciendo validación cruzada. Los árboles de

**[1:28:36]** decisión son, yo me tomé el tiempo de explicarlo y todo esto, pero son muy malos modelos, son como

**[1:28:43]** de los peores modelos que uno podría tener en la vida. Entonces, te van a decir, pero por qué

**[1:28:48]** me están enseñando esto? Entonces, yo les voy a decir, porque los árboles de decisión son

**[1:28:53]** la base de lo que se llaman los modelos basados en bosques y dentro de eso está el random

**[1:28:59]** forest, el exigibus, que a lo mejor les suena de alguna parte. Vamos a ver los random forest

**[1:29:05]** rápidamente, es súper simple si han entendido un árbol de decisión, esto se explica en

**[1:29:09]** 30 segundos, ¿no? Y la idea y el random forest fue como el modelo que lo hizo mucho mejor

**[1:29:18]** que el support vector machine por los años 2000, entre 2000 y el 2000D, fue como el

**[1:29:23]** que reemplazó el support vector machine. Y después de eso, esto fue reemplazado por

**[1:29:27]** la red neuronal. El random forest viene en la idea de la sabiduría de los grupos, que es

**[1:29:36]** una idea que básicamente lo que dice es, en general tú puedes demostrar matemáticamente

**[1:29:42]** que si es que la decisión de un individuo es peor que la decisión de un grupo de individuos

**[1:29:49]** siempre y cuando las decisiones no estén correladas, si no están correladas, entonces o que

**[1:29:55]** la correlación, perdón, siempre y cuando la decisión, si hay correlación, pero que esa

**[1:30:04]** correlación no sea muy alta. Y le voy a explicar cómo funciona esto. El random forest

**[1:30:10]** básicamente lo que hace es que son muchos árboles. Un árbol solo no predice muy

**[1:30:17]** bien, pero es muy rápido de ajustar. Entonces la idea es que utilicemos muchos árboles,

**[1:30:24]** pero para eso tenemos que asegurarnos de que no todos aprendan exactamente lo mismo. Así

**[1:30:28]** de la misma forma que yo les digo, si yo voy a tomar, le voy a pedir la decisión a Cristóbal.

**[1:30:33]** Cristóbal, ¿qué opinas de esto? Y después le pregunto a Daniel y le digo a Daniel, ¿qué

**[1:30:40]** opinas de esto? Y Daniel opina exactamente igual que Cristóbal, como que no me sirvió

**[1:30:45]** mucho el le preguntó a Daniel, pero generalmente lo que ocurre es que Daniel va a opinar

**[1:30:49]** distinto y Daniel va a ver cosas que Cristóbal no va a ver y Cristóbal va a ver cosas que

**[1:30:54]** Daniel podría potencialmente no ver. Entonces en el fondo es ajustar distintos árboles, pero

**[1:31:02]** que no todos aprendan exactamente lo mismo. Entonces algunos se han especializado en algunas

**[1:31:06]** cosas y otros se han especializado en otras. Ahora, ¿cómo se hace? Se hace de manera

**[1:31:11]** totalmente aleatoria. Entonces lo primero que digo voy a tener n árboles y para

**[1:31:16]** cada árbol voy a seleccionar aleatoriamente del conjunto de datos un subconjunto. Entonces

**[1:31:22]** cada árbol no he entrenado con exactamente los mismos datos, pero también le entrego un

**[1:31:28]** subconjunto los atributos. Entonces no solamente no tienen los mismos datos, sino que no tienen

**[1:31:32]** los mismos atributos. Entonces algunos árboles se especializan en algunos atributos y otros

**[1:31:37]** árboles se especializan en otros atributos que son seleccionados de manera aleatoria.

**[1:31:41]** Entonces hay solapamiento, hay cierta correlación. Y para predecir promedio la predicción hecha por

**[1:31:49]** todos los árboles, así es simple. O sea tengo cuatro árboles, le digo ¿qué opina usted? Yo digo

**[1:31:53]** que un perro. Le digo al segundo árbol ¿qué opina usted? Yo digo que un perro. Le pregunta al

**[1:31:58]** tercer árbol ¿qué opina usted? Yo creo que un gato. Le pregunto al último árbol le digo ¿qué

**[1:32:03]** opina usted? Yo creo que un perro. Entonces digo ¡ah! 75% probabilidad de que sea un perro.

**[1:32:09]** Entonces en el fondo lo que digo es la predicción es uno sobre n de la suma de las predicciones

**[1:32:14]** de cada uno de los árboles. Un gran número de árboles no correlados tienen mejor desempeño que

**[1:32:24]** cada uno de los modelos por separados, eso es lo que les decía. Y lo que ocurre es que los

**[1:32:28]** errores que comete un árbol pueden ser corregidos por los otros árboles. Y es uno de los

**[1:32:33]** algoritmos más certeros que hoy en día se conocen. De hecho en general uno comienza

**[1:32:39]** con un random forest y hay muchos problemas en los cuales un random forest lo hace mucho

**[1:32:46]** mejor que una red neuronal. Lo otro que es bueno es que permiten estimar la importancia de las

**[1:32:53]** variables y cómo es que tan importante es cada una de las variables que entra al árbol. ¿Y cómo

**[1:32:59]** lo puedo hacer? Bueno tengo que ver cuántas veces tengo que contar cuántas veces cada

**[1:33:04]** variable fue cogida por cada uno de los árboles como relevante al momento de separar. Entonces

**[1:33:09]** si hay una variable que ningún árbol escogió nunca para separar para dividir entonces esa variable

**[1:33:15]** es cero relevante y entonces no me sirve para clasificar el objeto. Pero si hay una variable

**[1:33:23]** que todos los árboles siempre la escogen entonces esa variable es muy importante. Resumen,

**[1:33:31]** clasificación e aprendizaje supervisado para categorías. Vimos un modelo lineal,

**[1:33:37]** el support vector machine. Vimos cómo se evalúa y cómo lo hacemos para asegurarnos de que generalice

**[1:33:43]** correctamente y también vimos modelos no lineales. Si se fijan el árbol de decisión no es lineal y

**[1:33:50]** por lo mismo el random forest tampoco es lineal. Ok, ahí estamos. No sé si hay preguntas,

**[1:33:58]** me pasé cinco minutos, les pido disculpa. Yo tengo una duda de lo último que dijo que

**[1:34:06]** cuando uno aplicaba estos modelos o los random forest ya hay distintas aisolapamientos,

**[1:34:15]** digamos de distintos atributos que se repiten y uno puede decir que dependiendo del resultado

**[1:34:21]** estas variables son súper importantes. Pero cómo eso conversa y me entró como la duda cuando

**[1:34:29]** uno hace el análisis exploratorio de los datos y hace correlación de variables es de las que

**[1:34:34]** tú eliges como que en virtud de estos análisis tú dices, hayas esta si elegiste, no sé,

**[1:34:40]** seis variables de estas seis al dos que son con la bomba para tu predicción, algo así.

**[1:34:46]** Es algo así, exactamente. Es como que estas seis variables siempre fueron elegidas, digamos que un,

**[1:34:55]** por decir algo, un 50% de las veces se coge una variable, la variable A. Un 20% de las veces

**[1:35:02]** se coge la variable B, un 10% la variable C y un 10% la variable D. Eso quiere decir que la variable A

**[1:35:10]** es muy relevante para clasificar. Entonces te da como una intuición de lo que los modelos están haciendo.

**[1:35:17]** Yo fui y una de las cosas que igual decía la vida, porque claro, uno de los modelos más

**[1:35:23]** importantes, si en qué caso es no, va a depender del problema que uno quiera desarrollar?

**[1:35:32]** Sí, sí, va a depender del problema, va a depender también mucho de los atributos,

**[1:35:42]** va a depender mucho de la cantidad de datos que tú tienes. En general, los modelos de

**[1:35:48]** deep learning, como los que usan la LLM y todo eso, son muy buenos porque son muy complejos y

**[1:35:56]** porque son entrenados con muchos datos, muchos extremadamente hartos datos. Entonces si tú no

**[1:36:05]** llegas a ese régimen en el cual tienes suficientes datos para que un modelo de deep learning le

**[1:36:10]** pueda vencer un modelo clásico como el random forest, entonces en general es mejor usar un modelo

**[1:36:15]** de deep learning. Pero no siempre es así, o sea, hay veces donde tú no tienes suficiente

**[1:36:22]** datos y suficiente datos es ambiguo, o sea, no hay un número, ya depende del problema,

**[1:36:29]** depende, pero hay momentos en los cuales tú entren a un random forest y entren a una

**[1:36:34]** red neuronal muy compleja y el random forest lo supera y pasa mucho más seguido lo que uno creería.

**[1:36:40]** ¿Hay más preguntas? Ok, dejamos la clase hasta acá entonces y nos vemos la próxima semana,

**[1:36:59]** la próxima semana tenemos presentación de proyectos. Ok, nos vemos.

**[1:37:12]** Chau, gracias.
