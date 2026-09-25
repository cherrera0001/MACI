# 03Clase Recuperación Fundamentos en Ciencia de Datos 15 julio_.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:18:42
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:00:19]** ok. Hoy día en la clase vamos a hablar acerca de datos, en particular vamos a

**[0:00:29]** hablar acerca de qué es lo que es un dato, qué tipos de datos hay y en particular

**[0:00:34]** también de la calidad de datos. Entonces este monito que está acá,

**[0:00:40]** ¿usted lo vieron en la clase con mano del correcto?

**[0:00:46]** decir que sí o que no? Sí. Ya, súper. Entonces esto acá es lo que nosotros llamamos el ciclo de la

**[0:00:57]** ciencia de datos, lo voy a repasar rápidamente y básicamente todo parte con un requerimiento

**[0:01:02]** pregunta, sin el requerimiento o pregunta no tiene ningún sentido hacer ciencia de

**[0:01:08]** datos ni inteligencia artificial. Entonces después de que nosotros tenemos este requerimiento o

**[0:01:14]** pregunta lo que hacemos es buscar datos, buscar datos que puedan ayudarnos a responder esa pregunta

**[0:01:20]** y como vieron la clase pasada recolectamos muchos datos y generalmente muchos estos datos vienen sucios

**[0:01:27]** y viene toda esta etapa de limpieza. Después de la etapa de limpieza cuando ya tengo los datos limpios

**[0:01:33]** viene la etapa de exploración que es cuando me pongo a revisarse que los datos que yo obtuve

**[0:01:39]** son correctos y si me ayudan a resolver el problema o no. Una vez que yo logro hacer eso también genero

**[0:01:45]** hipótesis entonces un hipótesis por ejemplo sería utilizando estos datos yo soy capaz de responder

**[0:01:54]** a la pregunta. Eso es el tipo de hipótesis que queremos generar. Después de eso viene la etapa

**[0:01:59]** de modelamiento que es donde hacemos todos los modelos predictivos, la etapa de visualización

**[0:02:04]** y comunicación que es cuando nosotros tenemos que reportar de alguna forma que también lo hizo

**[0:02:10]** nuestros modelos predictivos o nuestros modelos de inteligencia artificial y después de eso una

**[0:02:15]** vez que tú reportas ya sea a los tomadores de decisiones puede hacer un reporte interno para tu

**[0:02:20]** equipo tienes que poner los modelos en marcha y después volvemos a otro requerimiento o pregunta.

**[0:02:26]** Ahora lo que ocurre es que estas si se fijan desde un paso a otro hay flechitas que apuntan

**[0:02:33]** en las dos direcciones ¿recuerdan por qué las flechitas apuntan las dos direcciones? Sí porque

**[0:02:41]** si en algún momento no se visualiza lo que uno quiere uno tiene que retroceder y ver dónde está

**[0:02:47]** cómo lo es. Claro o sea muchas veces esto es un proceso donde uno avanza y después tiene que

**[0:02:55]** retroceder por ejemplo yo podría hacer la recolección de los datos y cuando lo estoy

**[0:02:59]** limpiando me doy cuenta de que hay datos que fueron mal recolectados y tengo que volver a

**[0:03:03]** recolectarlo o puede ser que yo esté en la etapa de modelamiento y veo que el modelo predictivo

**[0:03:10]** que supuestamente va a predecir lo que yo quiero que el sistema haga no funciona y entonces tengo

**[0:03:18]** que volver atrás a la etapa de exploración para tratar de entender por qué el sistema no está

**[0:03:22]** haciendo lo que lo que yo esperaría que haga. Hoy día mismo tuvimos una reunión respecto a eso.

**[0:03:27]** De hecho les voy a contar una historia les voy a contar la historia de lo que pasó hoy día.

**[0:03:31]** Teníamos el modelo en marcha. Básicamente un modelo que tenemos dentro de Alerze que es un sistema

**[0:03:39]** que se conecta a los telescopios del peor del mundo y que trata de clasificar todo lo que

**[0:03:46]** va encontrando en el universo y dentro de eso teníamos un modelo que está en marcha y

**[0:03:53]** estaba andando, estaba en producción y de repente nos dimos cuenta que en producción

**[0:04:00]** tenía peor calidad que el modelo anterior que habíamos puesto en producción. Entonces ya estaba

**[0:04:06]** en marcha. Entonces volvimos a la etapa de visualización y en la etapa de visualización vimos

**[0:04:11]** los gráficos que ya habíamos generado para entender cómo funcionaba más o menos el modelo y

**[0:04:16]** nos dimos cuenta de que estos gráficos habían algunas cosas que seguían como raras un par de

**[0:04:20]** cositas que seguían reales. Entonces volvimos atrás de la etapa de modelamiento y dijimos

**[0:04:24]** a ver cuál es el modelo que nosotros estábamos usando y cuando vimos los modelos nos

**[0:04:27]** dimos cuenta de que básicamente eran los mismos modelos o muy parecidos, pero la diferencia es que

**[0:04:33]** hayan sido entrenados con datos distintos. Entonces volvimos a la etapa de exploración de los datos

**[0:04:37]** y hoy día estuvimos haciendo toda la exploración de nuevo de digamos por supuesto ahora con el

**[0:04:44]** insight, con la edición de lo que ya estaba pasando en marcha con el modelo en producción y

**[0:04:50]** nos dimos cuenta de que hayan cosas que no calzan bien y no entendemos bien todavía porque

**[0:04:55]** no calzan bien. Entonces lo más probable o sea tuvimos que hacer ahora estamos haciendo la siguiente

**[0:05:01]** etapa de exploración nos quedamos acá en la etapa de exploración para tratar de entender qué es

**[0:05:05]** lo que está pasando y lo más probable es que en el momento de recolectar los datos que fueron usados

**[0:05:10]** para ajustar este modelo algo hicimos mal que no sabemos exactamente qué pero en la etapa

**[0:05:15]** de exploración somos capaces de ver qué es lo que pudimos haber hecho mal. Entonces esto

**[0:05:20]** pasa constantemente o sea fíjense que hoy día en un día pasamos de la puesta en marcha nos

**[0:05:26]** devolvimos hacia la exploración de nuevo y seguramente mañana bueno mañana no porque es

**[0:05:31]** frío el viernes vamos a seguramente darnos cuenta que es lo que espero darnos cuenta que es lo que

**[0:05:37]** está pasando y volver a la etapa de recolectión en caso que haya que recolectar los datos de

**[0:05:41]** nuevo a lo mejor es simplemente un problema en la limpieza que también puede ser que cuando

**[0:05:45]** hicimos la limpieza de los datos eliminamos cosas que no deberíamos haber eliminado o a lo

**[0:05:49]** mejor deberíamos haber eliminado cosas que no eliminamos. Entonces como le digo esto es un

**[0:05:58]** ciclo iterativo pero que va en ambas direcciones y uno de los grandes problemas de cuando uno

**[0:06:04]** trabaja en un proyecto de ciencia de datos es que es muy difícil al momento que tú tienes el

**[0:06:08]** requerimiento pregunta de saber cuánto te vas a demorar y cuántos recursos vas a necesitar

**[0:06:13]** para llegar a la puesta en marcha porque tú puedes ir y volver y volver y puedes estar

**[0:06:18]** varias veces yendo y volviendo. Generalmente una cosa que yo me hago cuenta es que uno pasa

**[0:06:24]** aproximadamente el 80% del tiempo entre recolectión limpieza y exploración. La mayor parte del tiempo

**[0:06:30]** se va acá una vez que ya tienes todos los datos limpiecitos y listos para trabajar con el modelo

**[0:06:36]** el modelamiento es relativamente simple y rápido pero lo más difícil es la recolectión limpieza

**[0:06:41]** y exploración. ¿No sí tienen preguntas respecto de esto? Ya. Ok. Entonces hoy día vamos a hablar un

**[0:06:55]** poco de los datos. Entonces qué vamos a hablar acerca de cómo se obtienen los datos y también de

**[0:07:03]** cómo uno tiene que explorar los datos y hay distintos tipos de forma de explorar los datos.

**[0:07:11]** Algunos de estos es estadística descriptiva pero también uno muy importante es la visualización

**[0:07:17]** de los datos. Cuando digo estadística descriptiva son promedio de piacen estándar y cosas de

**[0:07:22]** ese estilo y cuando hablo de visualización de los datos es cosas tipo histogramas, corner plots,

**[0:07:29]** no sé gráficos de serie de tiempo y cosas de ese estilo. Ahora ¿qué es un dato? ¿alguien de

**[0:07:38]** ustedes tiene alguna noción de lo que es un dato? ¿Qué es un dato? Yo creo que todos hemos

**[0:07:47]** trabajado con datos o hemos visto datos incluso uno ver datos en las noticias pero es algún hecho

**[0:07:55]** que no necesariamente es un número por ejemplo una foto también es un puede ser un dato si el

**[0:07:59]** final es un hecho de algo. Ya. Ok. Es un hecho pero por ejemplo es difícil pero no sé cómo.

**[0:08:09]** Es el registro es el registro quizás complementando lo que dice German que

**[0:08:15]** es el registro de un hecho. De un hecho. Ahora ¿cómo define un hecho?

**[0:08:22]** Es algo que si sale una medición no más o que se tenga que capturar porque hay algún

**[0:08:28]** interés hay un dato no necesariamente de interés pero asumamos que hay algún interés detrás

**[0:08:32]** de eso. Ya está bien mira ahí está creo que dijiste la palabra clave que es se puede capturar

**[0:08:41]** es algo que uno captura ¿certo? Ahora un dato es una medición de algo en una escala que sea

**[0:08:50]** comprensible tanto para quien registra eso como para el lector para quien lo leen. Entonces el

**[0:08:56]** dato tiene solo sentido si es que al momento de tú registrarlo tiene un significado que es el

**[0:09:04]** mismo significado para otra persona que lo pueda tomar después más adelante. Entonces voy

**[0:09:09]** a partir por algo simple y después voy a ir algo más complejo. Digamos primero la altura de una

**[0:09:16]** persona. Yo puedo decir tomo a una persona no sé tomo a Fernanda la mía y digo mí de tantos

**[0:09:22]** metros ya y lo noto en un papelito ok. Después puedo pasar eso a Caden y Caden lo toma y dice

**[0:09:31]** ah yo lo entiendo o yo se lo puedo decir y Caden no entiende ok. Entonces es algo que tú

**[0:09:41]** mides ya en una escala entonces yo te digo 1,65 metros o algo de ese estilo. Inmediatamente

**[0:09:49]** cuando digo 1,65 metros todos los que conocemos lo que es 1,1, 1,65 metros entendemos de

**[0:09:57]** inmediato lo que significa. Incluso yo podría imaginarme que es lo que quiere decir este 1,65

**[0:10:04]** metros ok. Ahora vamos a algo un poco más complejo que mencionado recién no me acuerdo que lo mencionó

**[0:10:13]** pero es una imagen. Una imagen es una medición de algo. Si es la respuesta de la luz en los

**[0:10:25]** píxeles del sensor. Si al final es una matriz de tres dimensiones. Entonces se entiende.

**[0:10:33]** Alguien quería decir algo. Alguien quería decir algo parece como que se ha metido una meta. Caden o no?

**[0:10:45]** No no o sea que dije exacto o sea iba a mencionar eso que al final en una cámara en el sensor lo

**[0:10:53]** que se captura son mediciones no sé me la imagino como una matriz unos y ceros dependiendo de la

**[0:11:01]** intensidad de luz del color de todo entonces el pixel es como esa unidad de datos. Exacto. Entonces

**[0:11:11]** por ejemplo si yo tomo acá la letra u por decir algo acá y hago una imagen cierto y lo transformo

**[0:11:18]** en píxeles entonces algunos píxeles van a ser blancos y otros van a ser negros cierto. Entonces

**[0:11:26]** generalmente eso se representa con una escala entre 0 y 255. Saben en eso cierto que los píxeles de la

**[0:11:33]** imagen van entre 0 y 255. Entonces en este caso en blanco y negro yo podría decir que lo que está

**[0:11:40]** en blanco va a ser 255 y lo que está en negro va a ser 0 y entonces cuando yo tengo la imagen

**[0:11:47]** digamos que es una imagen de 16 por 16 píxeles algunos de esos píxeles van a ser ceros y otros van

**[0:11:53]** a ser 255 y yo en realidad lo que le estoy pasando son los 0 y los 255. Ese es el dato en los 0 y los

**[0:12:01]** 255. Después ustedes transforman eso en información y esa información sería lo que es una u.

**[0:12:08]** Cuando estamos hablando de imágenes en RGB que son como los tres filtros que se usan en los computadores

**[0:12:20]** ahí se transforma en un dato de tres dimensiones porque vamos a tener para cada píxel tres dimensiones

**[0:12:29]** el r, el u, el gr, el g y el v. Entonces un dato es algo que yo mido es una medición de algo que en

**[0:12:42]** alguna escala que sea comprensible tanto para mí que lo estoy midiendo como para alguien a quien yo

**[0:12:46]** se lo pase. Y así como uno podría pensar bueno pero entonces como que todo es dato o no. Hay

**[0:12:54]** algo que no es dato porque al final nosotros como seres humanos nos comunicamos unos con otros.

**[0:13:01]** Es que básicamente al menos en computación todo un dato porque al final son todos unos 0 en algún

**[0:13:05]** disco entonces ya la descripción sería así dato me sirve para algo porque por ejemplo voy a estrenar

**[0:13:10]** no sé el icono de Windows que tienen casi todos los computadores pero y para mí quizás no me

**[0:13:16]** interesa. Pero si yo digo por ejemplo así acá hablando mientras estamos hablando yo digo la

**[0:13:24]** palabra perro ese es un dato. Depende del contexto porque si es el resultado de un

**[0:13:31]** clasificador por ejemplo sí puede ser relevante pero la palabra por sí sola en el vacío quizás no.

**[0:13:35]** Entonces mirá vamos para la definición yo digo la palabra perro acá la digo frente a usted y

**[0:13:43]** primero es una medición de algo está una escala que sea comprensible para ustedes como para mí.

**[0:13:51]** Una escala de nombre de animal. La que podemos categorizar así.

**[0:14:01]** Es que falta el contexto.

**[0:14:04]** Para que pueda ser información útil se requiere el contexto porque si tú me dices perro solo por decirme

**[0:14:11]** perro. O sea yo puedo saber que es un perro pero sin el contexto no significa nada.

**[0:14:18]** Ya pero mira estamos hablando de dato versus información acá. Cuando tú dices el

**[0:14:24]** contexto estoy tratando de transformar el dato en información en algo es como de hecho

**[0:14:31]** la información son los datos dentro de un contexto pero yo estoy hablando del dato el

**[0:14:38]** dato yo digo solamente la palabra perro mide algo no solo especifica que es un perro que lo que

**[0:14:48]** sea es perro. A ver mira vamos por lo más fácil yo digo perro. Ustedes entienden qué es lo que

**[0:14:55]** estoy diciendo. Sí sí entonces está en una escala que sea comprensible tanto para mí como

**[0:15:09]** para ustedes y ahora yo creo que la pregunta es entonces yo creo que yo digo perro y estamos de

**[0:15:20]** acuerdo en que es comprensible tanto para ustedes como para mí ahora la pregunta es mide algo la

**[0:15:26]** palabra perro si yo digo la palabra perro mide algo. Yo sé lo que va pero no es adelantar

**[0:15:42]** un poquitito. La palabra es simple esto no mide nada pero por ejemplo eso puede ser un dato

**[0:15:51]** categoría también. Entonces ahí donde no es un poquito de ruido entonces entiendo el punto.

**[0:15:56]** Para allá voy. Pero no es un poco de ruido igual. Sí pues hace ruido porque nosotros estamos

**[0:16:01]** acostumbrados a trabajar con los datos en un computador en una planilla excel no sea algo

**[0:16:05]** así pero sí que yo hablo de perro perro como tú decía ahí es una variable categórica

**[0:16:11]** mide una categoría. Entonces si yo pusiera perro dentro una planilla excel usted me dirían

**[0:16:19]** ah sí es un dato yo tengo una planilla excel donde son puros animales y en una columna tengo

**[0:16:25]** la raza y sale perro gato. Entonces para ustedes es obvio que es un dato porque está en una

**[0:16:31]** planilla excel pero si yo lo digo no más está midiendo algo. Entonces en el fondo sí lo

**[0:16:40]** está midiendo está midiendo la categoría de algo de un animal y todos sabemos que está

**[0:16:47]** midiendo la categoría de un animal todos sabemos que perro es un animal. Entonces en el fondo

**[0:16:52]** es como como que al final uno empieza a sentir que todo lo que uno hace son datos todo lo que

**[0:17:00]** está alrededor de uno son datos y nosotros nos comunicamos y nos transferimos estos datos de

**[0:17:05]** una forma o otra ya sea de la conversación o un mensaje whatsapp o lo que sea. Ahora de

**[0:17:14]** dónde vienen los datos hay distintas fuentes de datos hay fuentes internas que son los

**[0:17:21]** datos que ya están recopilados que son parte de alguna organización y hay fuentes externas

**[0:17:27]** que ya existen que generalmente se pueden acceder de manera gratuita o pagada pero

**[0:17:36]** también existen fuentes externas que para transformarlo en datos útiles para mí tienen que

**[0:17:42]** tengo que hacer cierto procedimiento. Entonces por ejemplo imaginemos que yo estoy en alguna

**[0:17:47]** empresa y tengo digamos trabajo en recursos humanos y tengo los datos de todo el personal

**[0:17:54]** que trabaja en la empresa. Eso es un fuente interna son datos que ya están recopilados

**[0:18:00]** o sea cuando alguien entra a trabajar seguramente tu firmó un contrato y alguien pasa esos datos

**[0:18:05]** a algún sistema y eso es en alguna baseato y que es en esa baseato tu datos. Entonces cuando yo

**[0:18:12]** tengo una planilla con todos los trabajadores generalmente vienen desde esa baseato. Ahora también

**[0:18:20]** existen fuentes externas entonces yo pongo con los datos de mi organización sé que están

**[0:18:26]** bien organizados y tienen su buena arquitectura de datos y etcétera etcétera que vamos a

**[0:18:30]** hablar un poquito después. Entonces yo puedo usar esos datos y es relativamente simple para

**[0:18:37]** mí trabajar con los datos de fuente interna porque simplemente lo uso. Para la fuente externas

**[0:18:45]** existen muchos datos que son gratuitos y hay datos que son pagados. En general estos datos

**[0:18:53]** vienen ya estructurados o sea vienen con su buena estructura y uno puede descargarlo y

**[0:18:59]** usarlos o pagar y te dar acceso a ello y usarlo. Pero hay algunas veces que yo necesito conectarme

**[0:19:07]** a la fuente externa y desde la fuente externa empezar a procesar estos datos y así lo transformo

**[0:19:15]** en datos que sean útiles para mí. Entonces voy a darle algunos ejemplos. Fuente internas,

**[0:19:22]** datos centrado en el negocio que están disponibles en la base de datos de la organización

**[0:19:26]** eso es muy parecido a lo que les dije antes y se pueden usar para operaciones diarias o para

**[0:19:31]** operaciones periódicas mensuales lo que sea. También hay a veces cuando yo realizo experimento

**[0:19:38]** dentro de mi organización. Imaginemos que estoy en una farmacéutica o en una empresa del

**[0:19:45]** rubro forestal o minera. Yo puedo hacer experimentos y a partir de esos experimentos

**[0:19:50]** genero datos y estos datos después lo uso para mi experimento pero generalmente los guardo

**[0:19:55]** también en caso de que alguien quiera usarlos después más adelante. Fuente externa existente,

**[0:20:02]** bueno hay muchas bases de datos gubernamentales que son públicas. Hay muchos datos de mercado

**[0:20:08]** también que uno puede descargar directamente. No sé por ejemplo para el COVID estaban los

**[0:20:19]** datos epidemiológicos disponibles para que cualquier persona pudiese descargarlo. Hay

**[0:20:28]** algunos datos públicos que sirven para la investigación. Por ejemplo Kaggle o Seno. ¿Conocen

**[0:20:35]** Kaggle o Seno? ¿Tiengan deditos para arriba? Si lo conocen deditos para abajo si no lo conocen.

**[0:20:42]** Ya hay dos deditos para arriba eso es todo lo que ves. Mira les voy a agarrar. Kaggle esta

**[0:21:00]** vagina web es un servicio que básicamente originalmente almacenaba desafíos entonces podía

**[0:21:08]** llegar por ejemplo Google y decir quiero que alguien resuelva este problema y el que resuelva

**[0:21:13]** este problema le doy no sé 10.000 dólares. O podían llegar no sé podían llegar ustedes y

**[0:21:22]** decirle y decir saben que tengo este data set y quiero responder esta pregunta desde este

**[0:21:27]** data set y el que mejor lo haga se lleva solamente el honor pero a mí me sepa. Entonces a ver si

**[0:21:36]** que están los desafíos acá. Entonces si tú te metes a haga competitions también do mi Kaggle

**[0:21:41]** ¿Cierto? Sí. Acá están las competencias las competencias que están actualmente en Kaggle.

**[0:21:51]** Hay hackathones mira acá hay un premio de Pokémon Company hay una mira 240.000 dólares

**[0:22:05]** 240 millones de pesos que ganan esto y de qué se trata de hacer una IA que sea capaz de ganar

**[0:22:12]** en el Pokémon de eso se trata y tú te puedes meter acá y acá está el de qué se trata de

**[0:22:22]** hecho si te quieren participar de esto yo creo que sería una muy buena idea. Aún cuando no

**[0:22:26]** ganen es buena idea porque te entrenate te presiona para tener algo. Entonces la idea es tratar de

**[0:22:34]** ganar a ser una gente de inteligencia artificial que gane en Pokémon en train card game en las

**[0:22:40]** cartas de Pokémon. Ustedes pueden ver acá que está el overview que como resumen están los

**[0:22:46]** datos. Entonces acá están los datos que tú puedes descargar. Entonces tú puedes descargar los datos

**[0:22:56]** hay que sign in para obtener los datos. Muy buena mucho pero podéis descargar los datos y después de que

**[0:23:09]** descarga los datos puedes trabajar con ellos y después tú lo que haces es que puedes mandar

**[0:23:17]** tu resultado a Kaggle y se empiezan a comparar contra todos los del mundo y el que tenga el mejor

**[0:23:24]** score gana y no solamente te hace millonario en este caso sino que además te da fama. Yo creo

**[0:23:37]** que eso es lo más importante por eso lo hace la mayor parte de la gente te da mucha fama. De hecho

**[0:23:42]** generalmente los que ganan cualquiera de estas competencias son reclutados de inmediato por Google

**[0:23:48]** o por OpenAI o lo que sea para trabajar con ellos. Ahora es súper difícil porque todo el mundo está

**[0:23:55]** o sea hay expertos de todo el mundo participando en esto. Entonces tienen las competencias que

**[0:24:01]** ya la vimos este era uno que había. Hay otros mira que hay uno de 850 millones que es el

**[0:24:07]** ARK price que no sé qué es lo que hace. Hay varios ARK prices a ver qué es lo que son porque

**[0:24:19]** está el doy y el tres. Es resolver hacer inteligencia artificial que resuelva tareas que nunca antes

**[0:24:27]** nadie haya resuelto. Eso es difícil por eso te dan tanta plata porque son tareas muy complejas.

**[0:24:34]** Pero hay unos más chiquitos como estos de acá que son de 50.000. Estos de acá te dan

**[0:24:39]** swag que así como no sé si saben lo que es su acto. Y bueno hay varios más. Hay unos de

**[0:24:51]** mil. Hay unos de 20.000 de 3000. Así que eso. Pero además de tener las competencias miren

**[0:25:04]** ganas de verlas todas para que se puedan participar en una. Pero además de estas competencias están

**[0:25:10]** los benchmarks. Los benchmarks son como datos donde tú tienes un conjunto de datos. De hecho

**[0:25:17]** tú puedes poner acá en search y déjame algo y te apuestre que van a encontrar datos de eso que

**[0:25:24]** le interesaría. Déjame una o dos palabras. Déjame algo. No sé Fernanda. Fernanda cartes. Dime

**[0:25:41]** algo que te interesaría en lo que te gustaría trajar. Fernanda está acá. Ya vamos con

**[0:25:55]** la otra Fernanda. Entonces Fernanda Quijón. Pero cualquier cosa. Cualquier cosa. Así como un dato,

**[0:26:04]** un dato que te gustaría trajar de lo que sé. No sé las series más vistas. De serie de TV.

**[0:26:13]** Sí o anime a ver más complejo. A anime. De estar lleno de anime. Mira acá encontramos entonces un

**[0:26:24]** notebook. O sea esto es como para trabajar. Usted ya conoce los Jupyter notebooks. Y entonces hay un

**[0:26:30]** notebook donde puedes trabajar directamente. Acá tienes otro notebook. A ver busquemos por

**[0:26:38]** datos. Hackathon Project Completed Solution Projects. A ver voy a tomar uno. A ver el que tenga más.

**[0:26:51]** Es un sistema recomendador para anime. Entonces tú puedes ver acá que alguien generó esto. Y acá

**[0:27:06]** está el dataset. Y tienes el ID del anime. El nombre del anime. El género. El tipo. Cuantos

**[0:27:13]** episodios tiene. El rating en los miembros. Y si ustedes ven acá tienes todo. Tiene el Jupyter

**[0:27:20]** notebook completo. O sea puedes descargar esto y empezar a trabajar con él directamente. Y empieza

**[0:27:25]** a hacer cosas como análisis descriptivos. Empieza a sacar los gráficos. Y creo que al final de

**[0:27:31]** tener algo de modelo preáctil. Ah, acá hay un recomendador. Entonces puedes ver acá que existe

**[0:27:39]** un recomendador. Entonces dame la recomendación de Naruto. Ah, sé que a mí me gusta Naruto. A ver

**[0:27:46]** qué hice. Un nombre de la serie que le gustan a Naruto. Entran otras recomendaciones de milares.

**[0:27:57]** Claro, tú dices me gustan a Naruto y dicen entonces te gustar to love root darkness. No tengo idea

**[0:28:04]** qué es eso. Hamburg, Natsuki, Garno, Boru, No Boru, Sora. Maishime, Doraemon. Doraemon lo

**[0:28:15]** conozco. Boru and Genshin también lo conozco. Bueno, eso. Entonces si ustedes ven acá

**[0:28:24]** pueden descargar datos, notebooks que están listos para trabajar y además pueden participar de

**[0:28:28]** competencia. Eso es Kaggle. Entonces tú puedes volviendo a lo que estamos hablando antes. Tenemos

**[0:28:34]** fuente externa que ya existen como Kaggle. También está Seno. Seno son más datos científicos.

**[0:28:41]** Entonces tú te metes acá Seno y esto es un repositorio de datos. Entonces generalmente

**[0:28:46]** cuando tú escribas un artículo científico y tienes que liberar los datos, generalmente

**[0:28:52]** serían al red de Seno. Entonces voy a agarrar uno a cualquiera random. NASA, PDs, Register,

**[0:28:58]** API. Ah, no, pero software esto. No necesito datos. Acá hay un data. Tabla dos, un updated

**[0:29:09]** data on LeapDopterna from the white carrion stage H. No tengo idea qué es eso. Pero acá también

**[0:29:18]** pueden encontrar datos de varias cosas. Entonces busquemos anime, a ver si hay algo de anime.

**[0:29:23]** Esto no sé porque acá generalmente son más científicos. Acá hay una tesis, hay un artículo,

**[0:29:29]** acá hay un dataset anime, dataset y un cc. Ah, acá está el dataset.

**[0:29:37]** Seno. Aquí. Ah, y mira, es el mismo dataset del que vimos recién. Entonces el dataset está

**[0:29:49]** en Seno y el user notebook está en Kaggle. Ya. Ok. Ups. Entonces en el fondo hay fuentes

**[0:30:07]** externas de datos donde uno puede descargar datos de casi cualquier cosa o India y también hay fuentes

**[0:30:15]** externas que requieren algún procesamiento. Entonces a veces uno quiere por ejemplo obtener

**[0:30:22]** datos desde, desde algún, desde alguna fuente, desde alguna fuente donde no tengo el acceso directo

**[0:30:30]** a los datos, pero puedo ir y sacarlos directamente. Y creo que esto lo vieron usted en la ayuntía,

**[0:30:34]** ¿no? Cómo acceder a datos directamente de una página web. Todavía no creo.

**[0:30:45]** Hemos visto cómo se limpian los datos, cómo se estructuran o también cómo podemos ver

**[0:30:51]** qué es lo que tiene la base de datos. Estadística, etcétera, eso es lo que hemos visto. Ya. Cuando los

**[0:30:58]** datos están alojados online hay distintas formas de acceder a ello. La forma así como

**[0:31:05]** más importante de hoy día es a través de la API, que son Application Programming Interfaces o

**[0:31:10]** eso es, y que básicamente es un conjunto de funciones que son predefinidas por los

**[0:31:16]** quienes están entregando los datos y que a las cuales tú te conectas es como un

**[0:31:21]** pedazo de código, una función de código que tú te conectas y eres capaz de descargar datos desde

**[0:31:27]** esta API. Normalmente el acceso a esta API se paga. Entonces cuando alguien desarrolla un API,

**[0:31:35]** por ejemplo Twitter tenía un API o IndiaX o Facebook tiene un API o Google Maps tiene un API,

**[0:31:46]** entonces tú puedes acceder a los datos a través de una función y eso es lo que se llama un API.

**[0:31:53]** Ah, bueno, acá hay ejemplo justo. Google Maps, Facebook y Twitter. Cuando Twitter era Twitter y no

**[0:32:01]** era X, la API de Twitter era gratuita y tú podías acceder directamente a los datos de Twitter y

**[0:32:08]** hacer consultas directas sobre los datos de Twitter dentro de un periodo de tiempo acotado.

**[0:32:15]** No sé si ustedes saben la historia de que cuando Elon Musk compró Twitter y lo transformó en X,

**[0:32:24]** Elon Musk como condición ante comprar Twitter dijo, esperen, esperen, antes de yo comprar Twitter

**[0:32:29]** quiero que ustedes me aseguren de que no hay datos falsos en Twitter, que todo es real en Twitter,

**[0:32:36]** eso es lo que dijo. Y Twitter lo que les dijo es, mira, eso ni siquiera nosotros lo podemos

**[0:32:42]** hacer, pero si tú quieres te damos acceso a todos los datos de Twitter y le dieron, le generaron un API

**[0:32:48]** para que se conectara a todos los datos de Twitter para que él revisara que todo era, si todo era

**[0:32:53]** verdad o falso, era imposible porque eran demasiados datos, entonces Elon Musk al final no lo pudo

**[0:32:59]** hacer tampoco. Están los RSS que son los Rigside Summaries y que resume el contenido

**[0:33:09]** actualizado frecuentemente en formato estándar. Ay, y es gratis que el sitio lo tiene en general,

**[0:33:15]** entonces estos son los RSS es un resumen de lo que ha pasado dentro de tu sitio web y generalmente

**[0:33:24]** tú lo entregas de manera gratuita para que la gente se conecte, esto se cuanta. A ti te sirve

**[0:33:29]** que la gente saque datos desde tu sitio web. ¿Se le ocurre? ¿A quién le podría interesar esto?

**[0:33:37]** ¿Qué quiere que la gente se conecte a su sitio web? Ese es el típico de las páginas de noticias

**[0:33:45]** para tener más tráfico. Las páginas de noticias, entonces cuando tú publica algo, por ejemplo,

**[0:33:51]** la BBC publica algo, quiere que la gente se meta y saque esa información y después los cite,

**[0:33:59]** porque así ellos tienen más público que los lee, entonces en general las páginas de noticias,

**[0:34:06]** los blogs que están de vuelta, los blogs en algún momento desaparecieron y ahora están de vuelta.

**[0:34:11]** Y lo otro que uno puede hacer es hacer web scrapping que es, usa un software, un pedazo de software

**[0:34:18]** que va, que se mete a la página web y empieza a extraer datos de manera automática.

**[0:34:23]** Pero es una consulta, los RSS también se nos conectamos a través de funciones,

**[0:34:30]** no sé, por Python o algo así. Sí, en general, en realidad el RSS es como la forma en la cual

**[0:34:39]** se te entregan los datos, tú te puedes conectar a través de Python, pero en general te puedes conectar

**[0:34:44]** a través de otro software también si quisiera. Ok. Ya, quiero que hablemos un poquito web

**[0:34:56]** scrapping que creo que es relevante y básicamente web scrapping es cuando tú generas un pedazo de

**[0:35:08]** código que se mete dentro una página web y empieza a sacar información automáticamente. Ok.

**[0:35:15]** Entonces, ¿por qué uno haría web scrapping? Bueno, hay algunas páginas antiguas de

**[0:35:21]** gobierno, algunos sitios de distintas cosas, blogs o cosas antiguas que no tienen APIs. Y al

**[0:35:32]** momento de acceder a los datos, tú quieres acceder a los datos y no existe forma de acceder directamente

**[0:35:37]** a los datos. Entonces, otra opción que tú podrías decir, bueno, no quiero pagar por la API o no

**[0:35:45]** quiero pagar por acceso a la base de datos. Entonces yo voy a generar un clóler que se

**[0:35:50]** meta directamente y saque los datos sin que yo tenga que pagar. Entonces acá viene como un problema

**[0:35:56]** un poco ético. O sea, para hacerlo, existen liderías para extraer los datos de archivos HTML y

**[0:36:02]** XML, por ejemplo, BeautifulSoup, que es como el que más se usa. Pero más que el por qué hacerlo

**[0:36:12]** o el cómo se hace, creo que una pregunta importante es si deberías hacerlo. Y si solo

**[0:36:20]** quieres explorar, así como que yo quiero saber qué es lo que hay en esta página web y quiero sacar

**[0:36:24]** datos. Hay que hacerse un par de preguntas. Primero, ¿estamos violando los términos de servicio?

**[0:36:28]** ¿Existen problemas de privacidad para el sitio web y sus clientes? Sé que yo descargo estos datos.

**[0:36:34]** Imagínense que el dato son datos de un hospital, por decir algo, y que yo pudiese ir y sacar

**[0:36:41]** los datos o el dato de una linea, los datos de una linea. La otra pregunta es si quieres

**[0:36:55]** publicar tu análisis o producto, ¿tienes una API o una tarifa que estás evitando? ¿Estás dispuesto

**[0:37:02]** a compartir esta información? ¿Estás violando los términos de servicio? Fíjense que hay una

**[0:37:08]** palabra o un concepto acá que son los términos de servicio. Y lo otro es si hay problemas de

**[0:37:13]** privacidad, a lo mejor tú al sacar los datos está haciendo algo complejo, algo que no deberías estar

**[0:37:20]** haciendo. Son preguntas que uno se tiene que hacer, ¿ok? Sí. Yo quizás aquí voy a dar un punto

**[0:37:32]** completamente distinto para en general, lo que han dicho las cortes gringas y bales europeas. Es que

**[0:37:37]** los términos de servicio son como básicamente, con respecto a eso es una sugerencia porque si yo

**[0:37:41]** tengo acceso legal a los datos, si no estoy distribuyéndolo de forma ilegal, como que sea más

**[0:37:46]** violación de derechos de autor, diciendo que estoy en el buen ese lado, y si no estoy usando,

**[0:37:50]** por ejemplo, agrenciales, que no sean mis agrenciales falsos, yo puedo intentar,

**[0:37:56]** puedo intentar lo que sea el sitio y lo más probable es que intente bloquearme algo así,

**[0:37:59]** pero si lo logro, no estoy cometiendo nada mal y no puedo decir ya es cuestionable y todo,

**[0:38:04]** pero uno puede hacerlo básicamente. Tú lo estás llevando a la área legal.

**[0:38:11]** Si, claro que yo que tengo acceso a los datos y los quiero sacar, uno los puede sacar,

**[0:38:20]** no más que sea fácil o no, ya es un tema aparte, pero deberías hacerlo, mi respuesta

**[0:38:25]** personal sería, si lo necesito, sí, listo. Es complejo, mira, voy a discutir esto un

**[0:38:34]** poco más delante, pero les quería mostrar que en general, por ejemplo, esta es la página de

**[0:38:38]** Johnson's y tú puedes ver que en la propiedad de la página web dice, adicionalmente usted se compromete

**[0:38:45]** a no usar ningún robot, spider u otro dispositivo automático, proceso o medio para acceder a

**[0:38:52]** esta web para cualquier propósito, incluyendo el scrapping, la minería de datos, la monitorización

**[0:38:58]** o copia cualquier material de esta web, entonces en general en los términos y

**[0:39:02]** servicios te dicen esto. Ahora estamos en una área super gris acá, esa es la verdad.

**[0:39:12]** Yo una vez estuve almorzando con un tipo que es billonario, tiene mucho dinero, que es de Estados

**[0:39:22]** Unidos y me dijo, me preguntó acerca de qué es lo que yo enseñaba en las clases y yo le

**[0:39:28]** decía no, ya voy a esto, enseño esto y esto y esto. Y le conté que yo enseñaba web scrapping y que

**[0:39:36]** le explicaba cómo se hacía y todo eso y me dijo, yo le dije pero por supuesto les digo que tienen

**[0:39:44]** que tener cuidado porque pueden haber consecuencias legales o hay consecuencias éticas que hay cosas

**[0:39:50]** que a lo mejor uno no debería hacer web scrapping. Y él me dijo, si Google hubiese

**[0:39:57]** pensado así hoy día no tendríamos Google. De hecho, si OpenJay hubiera pensado así,

**[0:40:02]** hoy día no tendríamos ChatGPT tampoco porque ChatGPT es conocido por comerse toda la información que

**[0:40:08]** está en internet. Bueno y entró a ver que todas esas compañías nos ven así. Exacto, exacto,

**[0:40:14]** entonces yo creo que es una área que lice y cada uno puede tener su propia opinión y la

**[0:40:23]** pregunta es, no sé, por ejemplo, ¿te gustaría un mundo sin ChatGPT o prefiero un mundo con ChatGPT?

**[0:40:28]** ¿Cuál es el costo de tener ChatGPT? O sea, el costo es que ellos acceden a todos nuestros datos,

**[0:40:37]** sin peirnos a autorización. ¿Cuál es el costo de tener algo como Google, como Gmail, el mismo,

**[0:40:44]** que ellos tienen acceso a todos nuestros emails y ya como que perdemos nuestra prioridad? Pero

**[0:40:52]** prefieres tener, y hay personas que prefieren una cosa u otra, pero la pregunta es prefieres tener

**[0:40:58]** algo como Google o como ChatGPT y renunciar a tu prioridad o prefieres mayor prioridad pero renunciar

**[0:41:08]** a cosas como ChatGPT y Google. Esa es como la pregunta que tendríamos que hacernos. Y no

**[0:41:14]** necesito que me den su opinión ahora, pero es una pregunta, una pregunta relevante.

**[0:41:20]** Pero por ahí no sé si usted ha escuchado, yo creo que lo escuché, no me sé el caso,

**[0:41:27]** como también, pero entiendo que en Chile hay una página que se llama solo todo,

**[0:41:35]** que no sé si todos lo ubican, que tiene que ver con que si te queréis comprar un PC y cachar

**[0:41:40]** donde está más barato, te mete a la página y dice, miren, Falavela está en, no sé,

**[0:41:45]** 700 mil pesos, acá está en 650, que es yo. Entiendo que ellos hacen web scrapping y por ahí

**[0:41:52]** fue demandado por Falavela y quizá alguna otra grande del retail y entiendo que los dueños,

**[0:42:00]** por eso digo, no me acuerdo bien dónde lo leí, quizá quedo con la tarea de estudiarlo bien y

**[0:42:05]** quizá compartirlo o buscar la noticia, pero leía que el tipo de solo todo se sentó con el

**[0:42:11]** retail y finalmente es como, oye, gracias a mí y quizás gracias solo todo, te están yendo a

**[0:42:18]** comprar computadores, ¿cacháis? Entonces, si me hace mucho sentido lo que usted decía, eso de la

**[0:42:24]** como la materia gris que hay en esto, porque va a depender casi por la conveniencia que te

**[0:42:30]** entregue el web scrapping. Claro, exacto. Miren, acá me metí a ver a cuánto me metí a solo todo

**[0:42:38]** y podéis ver que efectivamente tienen los datos de distintas empresas y es básicamente,

**[0:42:45]** mira, y me metí a la de PC Factory, no sé por qué. Claro, porque te da el link, te da todo,

**[0:42:51]** caché, entonces por ahí entiendo que hubo un tema judicial con esta página y era un caso

**[0:42:58]** relevante de web scrapping, pero lo voy a buscar mejor para, no, pero tenía que ver con esto,

**[0:43:04]** con justo lo que estamos conversando. Ok, entonces la pregunta es, primero, o sea, bueno,

**[0:43:14]** ya sabemos básicamente dónde obtien los datos, pero el siguiente tema que quiero tratar es cómo se

**[0:43:20]** ven, entre comillas, los datos. Hay distintos tipos de datos y es súper importante entender cómo

**[0:43:26]** se llama, o sea, primero entender qué tipo de datos hay y cómo se llaman esos distintos

**[0:43:32]** tipos de datos, porque después todo lo que hagamos, que construyamos sobre esto va a tener relación

**[0:43:37]** con esa pregunta. Entonces, primero, ¿qué tipo de valores contienen tus datos? Esa es la pregunta

**[0:43:43]** número uno que yo tengo que hacerme. Y esto es como de qué tipo son tus datos,

**[0:43:48]** cuál es el tipo de estos datos. Entonces, hay datos primero que son simples o también se

**[0:43:53]** le llama atómicos y pueden ser los datos, como por ejemplo, un número. Entonces, un número

**[0:44:01]** es un dato simple, es un solo valor, ¿cierto? Y pueden ser enteros o pueden ser números con

**[0:44:09]** decimales, pueden ser distintos tipos. Hay datos bulianos que son los datos que son binarios,

**[0:44:16]** que son como o es verdadero o es falso. Y están también las palabras que son secuencias de símbolos.

**[0:44:26]** Entonces, una palabra, por ejemplo, podría ser, no sé, perro y es una P-E-R-R-O. Y la P se codifica

**[0:44:35]** con un número, la E se codifica con un número, la R con un número y la O con otro número.

**[0:44:41]** Entonces, es una secuencia de símbolos. Hay datos que están compuestos y que mezclan distintos

**[0:44:51]** tipos de datos. Entonces, por ejemplo, la fecha yora es un dato compuesto. Tiene una

**[0:44:57]** estructura específica que todos nosotros entendemos y que básicamente tiene fecha que son día,

**[0:45:06]** mes y año. O la hora, que son hora, minuto, segundo. Están las listas, que son las secuencias de

**[0:45:15]** valores. Entonces, yo puedo tener una lista de 5 número o una lista de 10 número o de 15

**[0:45:21]** número. Y están los diccionarios. Los diccionarios, ¿saben lo que son los diccionarios? Los diccionarios son

**[0:45:31]** básicamente conjuntos de pares donde uno tiene una clave y un valor o un key, una llave y un valor,

**[0:45:40]** ok? Entonces, generalmente, lo que yo digo es, por ejemplo, yo digo nombre, nombre es la

**[0:45:51]** key y valor puede ser Guillermo. Entonces, lo que estoy diciendo es que el nombre de esta persona es

**[0:45:58]** Guillermo, ok? Hago un ejemplo de diccionarios, solo para quienes no conocen los diccionarios.

**[0:46:08]** Digamos que tenemos el expediente de un estudiante. Entonces, podría decir nombre Guillermo.

**[0:46:13]** ¿Ya? Apellido, cabrera. Entonces, fíjense que acá tenemos el nombre y el apellido. ¿Y qué es

**[0:46:20]** lo que es el nombre y qué es el apellido? ¿Qué tipo de datos son nombre y apellido? ¿Quién me puede decir?

**[0:46:30]** Cadenas. Son cadenas, ¿sabto? Lo acabamos de decir. Una palabra es una cadena de símbolos. Y yo podría

**[0:46:45]** tener, por ejemplo, las clases que yo he tomado. Entonces, estas son las tres clases que yo he

**[0:46:49]** tomado. ¿De qué tipo es clases? Entonces, fíjense que hay tres clases. Voy a ir atrás.

**[0:47:03]** Ya. ¿Es un dato compuesto? A ver, primero. ¿Es un dato compuesto o un dato atómico?

**[0:47:08]** Compuesto. Compuesto, ¿cierto? Entonces, vamos a los datos compuestos. ¿Qué están los datos

**[0:47:19]** compuestos? ¿Qué es? ¿Es un diccionario? ¿Es una lista? ¿Qué es? ¿Una lista? ¿Es una lista? ¿Están

**[0:47:29]** de acuerdo? Yo estoy de acuerdo, pero quiero saber si están todos de acuerdo. Entonces,

**[0:47:34]** fíjense que acá yo tengo un diccionario que hay pares ya ve valor donde pueden ser el valor

**[0:47:42]** puede ser una cadena o el valor puede ser una lista. Ahora, ¿de qué tipo de forma nosotros

**[0:47:53]** almacenamos los datos? Hay distintos tipos de forma de guardarlo. Uno es con datos tabulares y un

**[0:48:00]** dato tabular o tabulado es cuando uno genera una tabla. Entonces, yo creo que esa es la

**[0:48:06]** mayor parte de los datos con los que todo hemos trabajado. Uno tiene una tabla. Entonces, tú

**[0:48:11]** tienes una tabla donde se mide en distintas cosas, ¿cierto? Y generalmente, esto se guardan,

**[0:48:17]** si ustedes han trabajado con Excel o con Google Sheets, tú podrías pensar en guardarlo en formato

**[0:48:24]** de KLSX o algo así, pero también hay distinto, hay otros tipos de formatos como el CSV,

**[0:48:29]** que es como de ASCII o puede ser un parquet o algo de otro estilo. Eso son los datos estructurados.

**[0:48:42]** Ahora, hay datos semiestructurados donde no todos los registros están representados por el mismo

**[0:48:50]** conjunto de claves y algunos registros no están representados con estos tipos para clave de

**[0:48:57]** valor. Entonces, les quiero mostrar un ejemplo. Vean esto acá. Esto es un ejemplo de datos tabulado.

**[0:49:07]** ¿Qué es lo que está representando este dataset? ¿Quién me dice? Yo voy a preguntar a alguien.

**[0:49:22]** Francisco, ¿qué representa este dataset, este conjunto de datos?

**[0:49:29]** Vamos mostrando como características de, no sé, galón de gal o algo así.

**[0:49:35]** Ya, puede ser, puede ser. Pero ¿qué es lo que representa? Por ejemplo, dime cuántos,

**[0:49:43]** si fueran galones de gas, cuántos son? Son dos. ¿Y qué características se están

**[0:49:52]** guardando de estos datos? Como dimensiones, digamos, altura, radio. Y el me gusta o no,

**[0:50:02]** no sea que se referida como me gusta, sino es como me va a gustar 100. Si me gusta el tipo de gas,

**[0:50:10]** no sé, algo así. ¿Puede ser? Pues sí. Ok. Fíjense que yo te hice dos preguntas y la respondiste

**[0:50:18]** inmediato. Que una es, ¿qué es lo que representa cada uno de estos objetos? ¿Y qué se está midiendo

**[0:50:25]** de cada uno de estos objetos? ¿Y esto es porque los datos tabulares nos permiten de inmediato

**[0:50:31]** entender qué son los objetos que estoy midiendo? ¿Qué es lo que estoy midiendo? ¿Y además qué es

**[0:50:37]** lo que estoy midiendo de cada uno de estos objetos? Entonces, cuando los datos están bien estructurados,

**[0:50:44]** uno espera que cada registro o observación represente las medidas de un solo objeto o evento.

**[0:50:52]** Entonces, en este caso, cada uno de estos es un objeto o evento. Cada una de las medidas que

**[0:51:00]** yo hago sobre cada uno de estos objetos o eventos, se les llama una variable o atributo. Entonces,

**[0:51:05]** cada vez que yo hable de variable o atributo, voy a estar hablando de lo mismo. Ok. Exactamente lo

**[0:51:10]** mismo. Entonces, por ejemplo, en este caso, lo que estoy midiendo de cada uno es los cilindros.

**[0:51:16]** Es la altura, el radio y si me gusta o no. Ok. Y fíjense que cada uno de esos va en una columna

**[0:51:24]** Yo creo que esto que yo le estoy mostrando suena súper obvio o no. Es como obvio. ¿Están de acuerdo?

**[0:51:31]** Así como obvio. Pero yo les aseguro que más de alguna vez no les ha tocado los datos así. Y

**[0:51:39]** ustedes han tenido que transformar los datos en algo así o les va a tocar. Si no les ha tocado,

**[0:51:43]** les va a tocar. Porque cuando la gente nota los datos, en general, muchas veces se guarda

**[0:51:51]** de manera no estructurada. El número de atributos que yo tenga, en este caso tres,

**[0:51:57]** altura, radio y me gusta o no, es lo que se le llama la dimensión de los datos. Entonces,

**[0:52:03]** en este caso son tres dimensiones. Entonces, estos son datos tridimensionales. Ya. Ahora,

**[0:52:19]** hay variables cuantitativas que son las variables numéricas y pueden ser discretas. ¿Qué

**[0:52:26]** quiere decir discreto? Que puede tener un número finito de valores en cualquier intervalo. O sea,

**[0:52:33]** que lo que estoy diciendo es una variable discreta, sé que yo pongo cualquier intervalo y dentro de

**[0:52:39]** este intervalo hay un número finito de valores. Entonces, por ejemplo, si yo digo número de

**[0:52:45]** hijos, yo puedo poner un intervalo cualquiera. Digamos, voy a poner entre cero y cinco.

**[0:52:52]** Dentro de entre cero y cinco hay un número finito de valores. Está el cero, un, dos, tres,

**[0:52:58]** cuatro, cinco. Y nadie más. Por ejemplo, un número de hermano, una variable discreta. Una variable

**[0:53:06]** continua es cuando dentro de un intervalo pueden haber valores infinitos. Por ejemplo,

**[0:53:13]** temperatura. Entonces, si yo digo temperatura, ¿qué valor puede tener de temperatura entre cero

**[0:53:21]** y cinco? Infinitos. Puede ser uno, puede ser uno coma uno, puede ser uno coma uno o uno,

**[0:53:27]** o puede ser uno coma dos. Entonces, tengo infinitos valores de temperatura dentro de un rango de

**[0:53:35]** finito. ¿Se entiende? Entonces, es súper importante porque cuando nosotros trabajemos en

**[0:53:41]** el modelamiento, vamos a trabajar con modelamiento de variables continuas y discretas de forma

**[0:53:47]** distinta. Las variables categóricas son variables que no tienen un orden inherente entre sus

**[0:53:57]** distintos valores. Entonces, por ejemplo, ¿qué tipo de mascota tienes? Es una variable categórica,

**[0:54:04]** porque yo podría decir gato y ustedes podrían decir perro, ya alguien podría decir conejo,

**[0:54:09]** ya alguien podría decir hornito rinco. Entonces, cada una de estas variables no tienen un orden,

**[0:54:15]** no es como que haya o que gato es menor que perro y es mayor que hornito rinco. No, porque no existe un

**[0:54:22]** orden inherente dentro de los valores. ¿Se entiende? Las variables cuantidadivas sí tienen un orden,

**[0:54:30]** ¿ok? Y generalmente se lee, bueno, casi siempre es usando un número. Entonces, tú le dices,

**[0:54:39]** dice, este es el número, la temperatura es tanto y le asignan un número. Las variables

**[0:54:44]** categóricas no tienen orden. En una variable continua, por ejemplo, en la temperatura yo sé que 2 es

**[0:54:52]** mayor que 1. Pero entre perro y gato yo no puedo ordenar. ¿Pregunta hasta acá? Sí, yo tengo una

**[0:55:06]** consulta prefe. ¿En las variables categóricas para poder trabajar con ellas se aconseja asignarles

**[0:55:13]** un valor numérico? Sí. En general, tú no puedes trabajar con las variables categóricas sin transformarlas

**[0:55:23]** de alguna forma en un valor numérico. Ok, gracias. Y les puedo explicar al tiro si quieren cómo

**[0:55:31]** se hace eso. Entonces, lo que generalmente tú no haces es, estoy buscando, ah, pero creo que,

**[0:55:48]** entonces lo que generalmente tú no haces es que imagínense que yo tengo la categoría animal,

**[0:55:55]** y tengo perro, gato y ornitorrinco. Ok. Entonces, en mi dataset, ¿sabe algo como así? No me gusta

**[0:56:04]** ese color. En mi dataset, ¿sabe algo como así? Y en alguna parte de mi dataset va a aparecer acá

**[0:56:15]** animal, animal, muy horrible. Y podría decir que para este registro es perro y para este gato y para este

**[0:56:34]** otro registro es ornitorrinco. Elegí una palabra muy larga, así que voy a poner ornino. Entonces,

**[0:56:42]** lo que uno hace es que dice, ya, yo no puedo trabajar, mi modelo no puede trabajar directamente

**[0:56:48]** con palabras. Tengo que transformar de alguna forma esta, esta, esta palabra en un dato numérico,

**[0:56:55]** pero que no tenga orden. ¿Cierto? Entonces, lo que uno hace es lo que se llama one-hot encoding,

**[0:57:02]** que básicamente yo digo, si tengo tres categorías, ¿no más? Yo digo perro, va a ser un vector,

**[0:57:10]** o ustedes pueden pensarlo como una lista, ¿no? Donde voy a tener un 1 acá, un 0 acá y un 0 acá,

**[0:57:23]** y puedo decir gato es otro vector, o es otra lista donde voy a decir este 0, este 1 y este 0.

**[0:57:36]** Y después digo ornit, para no tener que escribir toda la palabra. ¿Va a ser otro vector? ¿Qué

**[0:57:44]** cómo va a ser? ¿Cómo se le ocurre que hacer? 001. 001, bien. Entonces, fíjense, yo creo que ya te

**[0:57:52]** diste cuenta que lo que estoy representando con esto es, en el primer valor es como decir es perro,

**[0:58:00]** fíjense que será forma como una variable binaria, es como es perro, si es perro le pongo un 1,

**[0:58:06]** si no es perro le pongo un 0, en la segunda es gato, si es gato, entonces le pongo un 1,

**[0:58:15]** si no es gato le pongo un 0, y en la tercera es eornito rinco, ¿lo ven? Entende lo que estoy haciendo.

**[0:58:22]** Entonces, en el fondo lo que hago es que acá en la tabla, al final, voy a hacer como más o menos la

**[0:58:28]** misma tabla, ¿no? Donde decía perro, esto se transforma en 3 columnas, ¿no? Y esto va a tener

**[0:58:40]** un 1, un 0 y un 0, la siguiente va a tener un 0, un 1 y un 0, y la siguiente va a tener un 0,

**[0:58:52]** un 0 y un 1. ¿Se entiende? Esa es la forma más básica de hacer esto, y como en realidad

**[0:59:02]** con la que generalmente uno hace. Hay otra forma más compleja, mucho más compleja, pero esto es

**[0:59:09]** como lo que uno generalmente hace, y esto se llama one-hot encoding, one-hot codificación uno caliente,

**[0:59:23]** no sé si suena tan bien eso, generalmente le decimos one-hot encoding, ¿no? ¿Hay más preguntas?

**[0:59:41]** Vamos entonces ahora a hablar un poquito de calidad y limpieza de datos, ¿ok? Entonces,

**[1:00:00]** la pregunta que nos queremos hacer es, recuerda que primero tenemos que recolectar los datos y

**[1:00:04]** después tenemos que limpiar los datos, yo me tengo que preguntar, ¿estos datos son lo

**[1:00:09]** suficientemente buenos? Entonces hay algunos problemas típicos con los datos, valores faltantes,

**[1:00:15]** ¿no? Y la pregunta que yo me tengo que hacer es ¿qué hago para completar esos datos o los

**[1:00:21]** completos o los eliminos? ¿Qué es lo que me conviene hacer con los valores faltantes? Hay valores

**[1:00:27]** que son incorrectos, ¿cómo detecto si es que los valores son incorrectos y cómo nos puedo corregir?

**[1:00:32]** Entonces yo creo que hay algunos valores incorrectos que son como medio obvio, como por ejemplo si yo

**[1:00:37]** estoy midiendo, no sé, peso y me da un valor negativo, yo sé que dentro de los datos hay un

**[1:00:42]** valor negativo y yo sé que ese valor negativo está mal, ¿no? Entonces tengo que alguna forma

**[1:00:47]** encontrar la forma de corregirlo. Y el que más me gustaría enfocarme ahora es el del formato

**[1:00:54]** desordenado. Yo en antes les dije, mira, así es como deberían ser las tablas y es como obvio

**[1:00:58]** que deberían ser así, no siempre hace. Y hay datos que simplemente no los puedo usar,

**[1:01:05]** que son datos que no me sirven para responder a la pregunta que quiero, que me implanté inicialmente.

**[1:01:12]** Entonces, miremos este data set de acá, esta tabla contabiliza la entrega de productos durante

**[1:01:20]** un fin de semana, ¿lo ven? Entonces ¿qué me puede decir más o menos algo respecto a esta

**[1:01:26]** tabla? Víctor, ¿qué me puedes decir de esta tabla?

**[1:01:31]** De producto, de siguiente tabla contabiliza la entrega. O sea, esa es la entrega de los

**[1:01:39]** productos del bienesado domingo y el logrario de mañana, tarda y noche, no fin de semana.

**[1:01:45]** ¿Te acordáis de cómo habíamos dicho que debería ser una tabla?

**[1:01:50]** Es que me conecté un poquito más tarde porque no me hayan fijado que haríamos clases.

**[1:01:57]** Ok, ya lo voy a preguntar a otra persona. Camilo, ¿sí?

**[1:02:06]** Sí. ¿Te acuerdas de cómo habíamos dicho que debería ser una tabla? Una tabla bien estructura?

**[1:02:12]** Sí, que tenía que tener variables, dimensiones y atributos.

**[1:02:18]** Ya, súper. Entonces, ¿cuáles son las variables en este conjunto de datos?

**[1:02:24]** La variable es el momento del día, mañana, tarde, noche, los días de la semana y una

**[1:02:35]** dimensión en la cantidad de esa combinación. Ya, pero está bien. ¿Diste dos variables

**[1:02:42]** súper buenas? ¿Te faltó una variable? ¿Cuál es la tercera variable? ¿Dijiste el momento

**[1:02:50]** del día y te faltó? Y cuántas veces, por ejemplo, me imagino que se me cortó cuando

**[1:03:01]** estás explicando el concepto, eso a la mina. La siguiente está la cantidad de producto.

**[1:03:06]** Ah, los productos. Entregas. La cantidad de producto o la cantidad de producto.

**[1:03:10]** Ya. Fíjense qué pasa algo. Yo les había dicho antes que las variables

**[1:03:16]** debían ser en columnas, ¿certo? Hay una columna por cada variable, pero en este caso

**[1:03:24]** no pasa eso. Las variables están distribuidas entre los nombres de las columnas, las

**[1:03:29]** filas y el, digamos, todo el resto de la tabla. ¿Qué objeto o evento estamos

**[1:03:39]** midiendo acá? Le voy a preguntar a Rodolfo. Rodolfo, Rodolfo, ¿estás ahí?

**[1:03:55]** ¿Cantidad de, perdón, disculpa, cantidad de las entregas durante los distintos momentos

**[1:04:03]** y días, momentos del día y días. Son las entregas, eso es lo que estamos midiendo,

**[1:04:10]** ¿cierto? Ya. Y las entregas, los objetos debían ser en las filas. Entonces,

**[1:04:16]** esto está malestructurado. Ya. Esto ya lo hablamos. Y entonces el problema que tiene

**[1:04:25]** esta tabla, así tal cual está, es que cada encabezado de la columna representa el valor

**[1:04:29]** de una variable y esto, estas encabezados de columnas ocultan, entre comillas,

**[1:04:34]** la variable día. Los valores de la variable número de producto no se registran

**[1:04:39]** tampoco en una sola columna. Todos estos deberían estar registrados en una sola columna,

**[1:04:43]** pero están distribuidas en distintas columnas y distintas filas.

**[1:04:46]** ¿OK? Uno debíes, en principio, hacer algo como este estilo.

**[1:04:50]** Tenemos, generalmente, esto ocurre muy a menudo. Uno tiene que reorganizar

**[1:04:54]** la información para hacer explícito el evento que está observando

**[1:04:59]** y sus variables asociadas. Fíjense que ahora yo tengo como el delivery, entre comillas,

**[1:05:04]** y tengo el delivery 1, el 2, el 3, el 4, el 5, el 6, el 7, el 8 y el 9.

**[1:05:09]** Y tengo el período, el período de la mañana, la tarde de la noche,

**[1:05:13]** el día y el número de producto. Tuve que reorganizar la tabla

**[1:05:18]** para poder dejarla en un formato que esté ordenado.

**[1:05:25]** Hay otra cosa muy importante acá, que yo le puse acá el delivery, ¿cierto?

**[1:05:32]** El delivery es una ID, es un identificador.

**[1:05:37]** ¿Se acuerdan en el ramo anterior de fundamento de algoritmo y datos, y estructura de datos?

**[1:05:43]** Los foreign key.

**[1:05:46]** ¿Ah?

**[1:05:47]** Los foreign key es key. OK. Los key y los foreign key.

**[1:05:50]** Son exactamente eso. O sea, las llaves, las llaves primarias

**[1:05:55]** son las llaves que te permiten identificar únicamente cada uno de los elementos.

**[1:06:00]** Y después puedes relacionarlos, ¿es la distinta base de datos por relacionales?

**[1:06:04]** Como un búsqued vene.

**[1:06:05]** Te podría relacionar, sí, exacto.

**[1:06:08]** Pero además, lo que ocurre es que cuando uno trabaja con muchos datos acá,

**[1:06:12]** por supuesto son poquitos, son nueve, yo los puedo mirar y más o menos entender,

**[1:06:15]** pero cuando tú trabajas con muchos datos,

**[1:06:17]** tú tienes que de alguna forma saber si es que, por ejemplo,

**[1:06:21]** si tú quieres saber cuándo tu modelo predice mal

**[1:06:24]** y tienes medidas cuáles son los objetos que predice mal,

**[1:06:26]** tienes que de alguna forma acceder a esos datos.

**[1:06:29]** Y la forma de acceder es a través de esto acá que se le llama un índice,

**[1:06:33]** ¿no?

**[1:06:34]** O una llave primaria entre una base de datos.

**[1:06:37]** ¿OK?

**[1:06:38]** ¿Preguntas hasta acá?

**[1:06:42]** Un comentario, brozo. De hecho, normalmente,

**[1:06:44]** ese ID o ese key, debería ser único.

**[1:06:47]** ¿No repetido?

**[1:06:48]** Sí.

**[1:06:49]** Es algo importante.

**[1:06:50]** Es único. Es muy importante.

**[1:06:52]** Gracias, gracias.

**[1:06:54]** Tiene que ser un identificador único.

**[1:06:57]** O sea, yo no le puedo poner este de Libre 1 y el siguiente de Libre 1

**[1:07:00]** porque entonces no puedo identificar exactamente cada uno de ellos.

**[1:07:03]** ¿OK?

**[1:07:07]** Entonces, acá hay un ejercicio.

**[1:07:09]** Fíjense, estos también son datos, son casos reales.

**[1:07:14]** Los siguientes son datos de consumo en cine a camiones.

**[1:07:18]** Y dice, consumo, el lunes, camión 1, camión 2, camión 3.

**[1:07:22]** El martes, camión 1, camión 2, camión 3.

**[1:07:25]** El miércoles, camión 1, camión 2, camión 3.

**[1:07:28]** Y después dice cantidad.

**[1:07:30]** Y acá está la cantidad que puede ser en cualquier unidad

**[1:07:32]** que ustedes creen que es relevante.

**[1:07:34]** Entonces, volvamos a hacer las mismas preguntas de antes.

**[1:07:38]** ¿Cuáles son las variables en este conjunto de datos?

**[1:07:49]** La fecha y el tipo de camión.

**[1:07:53]** Ya.

**[1:07:54]** El consumo de encina.

**[1:07:56]** El consumo de encina.

**[1:07:58]** La cantidad de camión y el día.

**[1:08:00]** No, no es la cantidad de camiones.

**[1:08:02]** Es el camión.

**[1:08:04]** Este es el camión 1, este es el camión 2 y este es el camión 3.

**[1:08:07]** Ah, perfecto.

**[1:08:08]** Entonces, tenemos 3.

**[1:08:10]** Tenemos el día, el camión y la cantidad.

**[1:08:14]** Y el consumo.

**[1:08:16]** ¿Ya?

**[1:08:19]** ¿Qué estamos midiendo?

**[1:08:22]** ¿Qué es lo que estamos midiendo?

**[1:08:25]** Estamos midiendo camiones.

**[1:08:27]** Consumo de encina.

**[1:08:29]** Consumo de encina.

**[1:08:31]** ¿Qué es lo más que eso?

**[1:08:33]** Porque estamos midiendo el consumo de encina

**[1:08:35]** por día y por camión.

**[1:08:37]** ¿Cierto?

**[1:08:39]** Entonces, cada fila

**[1:08:41]** debe ser el consumo de encina

**[1:08:43]** por día y por camión.

**[1:08:45]** Cada columna

**[1:08:47]** tiene que ser una de las variables.

**[1:08:49]** Que en este caso sería el día, el camión

**[1:08:51]** y la cantidad.

**[1:08:53]** ¿No es?

**[1:08:56]** Sí.

**[1:08:58]** Yo podría sacar esta ítica de cuál es el camión que más consume

**[1:09:00]** por ejemplo, del mayor consumo.

**[1:09:02]** Y empezar a estandarizar un poco el proceso de

**[1:09:04]** distribuir.

**[1:09:06]** Exacto.

**[1:09:08]** Piensen que usted estuviese en la tabla así

**[1:09:10]** y tienen que acceder a los datos

**[1:09:13]** y sacar eso que tocas decir.

**[1:09:15]** Digamos, yo quiero saber el consumo

**[1:09:17]** del camión 2

**[1:09:19]** en promedio durante la semana.

**[1:09:21]** Voy a empezar a recorrer esta tabla

**[1:09:23]** y me va a aparecer primero el lunes.

**[1:09:25]** ¿Qué quiere decir el lunes? ¿Es un camión?

**[1:09:29]** O sea, ¿estamos viendo acá camiones

**[1:09:31]** o qué estamos viendo? Fíjense que la variable

**[1:09:33]** o sea, hay una columna

**[1:09:35]** que tiene dos variables metidas dentro

**[1:09:37]** de la misma columna.

**[1:09:39]** Que en el día tiene sentido.

**[1:09:42]** ¿Debería abrirse como una especie de grubado?

**[1:09:45]** Podría ser.

**[1:09:47]** Pero en este caso estamos trabajando

**[1:09:49]** con un formato

**[1:09:51]** de datos no tabulares.

**[1:09:53]** Estamos trabajando con un formato diccionario.

**[1:09:55]** Pero eso que tú dijiste

**[1:09:57]** es como trabaja con datos en formato diccionario.

**[1:09:59]** O sea.

**[1:10:01]** El lunes, y el lunes

**[1:10:03]** pues decir dentro del lunes, decir

**[1:10:05]** hay camión 1 con sumo tanto.

**[1:10:07]** Camión 2 con sumo tanto y así sucesivamente.

**[1:10:09]** Y eso sería como abrirlos.

**[1:10:11]** O sea, yo he tenido que trabajar con Excel.

**[1:10:13]** Para mí es un copy page de un Excel.

**[1:10:15]** Yo los he visto en industria.

**[1:10:17]** Entonces

**[1:10:19]** aquí la verdad

**[1:10:21]** el procesamiento un poquito más complicado.

**[1:10:23]** Al final lo que no debería llegar sería tener

**[1:10:25]** el ID único obviamente.

**[1:10:27]** La fecha que me gustaría que fuera una fecha en vez de

**[1:10:29]** 3, sino que sea año mes día

**[1:10:31]** o horas si es que llega a ser relevante.

**[1:10:33]** En este caso no creo.

**[1:10:35]** El identificador del camión que sea 1, 2, 3

**[1:10:37]** de hecho yo lo sacaría la palabra camión ahí.

**[1:10:39]** Y finalmente

**[1:10:41]** lo consumí.

**[1:10:43]** Y ahí con eso sí se puede trabajar.

**[1:10:45]** Porque esto es como que alguien escribió un Excel y lo mandó nomás.

**[1:10:47]** Exacto.

**[1:10:49]** Y esto es lo que yo les decía al principio.

**[1:10:51]** Que

**[1:10:54]** cuando yo les dije es obvio que uno tiene que trabajar con una tabla así.

**[1:10:56]** Cuando estamos viendo lo de los cilindros.

**[1:10:58]** En general

**[1:11:00]** no son así.

**[1:11:02]** A menos de que quien haya escrito la tabla haya

**[1:11:04]** pensado que después se va a querer

**[1:11:06]** usar para hacer algún tipo de análisis

**[1:11:08]** de este estilo.

**[1:11:10]** Pero generalmente es como que se lo pasa

**[1:11:12]** a un operador y el operador dice ya ok voy

**[1:11:14]** a empezar a escribirlo.

**[1:11:16]** Pero es totalmente desestructurado.

**[1:11:18]** Y tenemos que tratar

**[1:11:21]** de llevar los datos a un formato lo más

**[1:11:23]** estructurado posible.

**[1:11:28]** Entonces la respuesta a esto que ya la venimos

**[1:11:30]** discutiendo.

**[1:11:32]** Las variables en este conjunto de datos son día,

**[1:11:34]** camión y consumo.

**[1:11:36]** El objeto de evento que estamos midiendo

**[1:11:38]** es el consumo por día y por camión.

**[1:11:40]** Entonces uno podría tener algo

**[1:11:42]** como este estilo.

**[1:11:44]** Tú dijiste una muy buena idea.

**[1:11:46]** Que yo no la puse acá en el resultado.

**[1:11:48]** Pero es que en realidad

**[1:11:50]** el ID del camión debería ser

**[1:11:52]** un ID numérico.

**[1:11:54]** O un ID que después yo pueda asociar

**[1:11:56]** directamente con

**[1:11:58]** otra tabla donde aparezcan

**[1:12:00]** las descripciones del camión por ejemplo.

**[1:12:02]** Claro.

**[1:12:04]** Y de uno es

**[1:12:06]** un CAD 793F

**[1:12:08]** con tales condiciones

**[1:12:10]** y se ocupa en tal lugar.

**[1:12:12]** Y es una tabla de parte que no necesariamente

**[1:12:14]** está ahí porque sería demasiada información

**[1:12:16]** para juntarla todas.

**[1:12:18]** Aparte y tema de rendimiento cuando uno hace joins

**[1:12:20]** con strings versus joins con números.

**[1:12:22]** Pero eso es un tema de parte.

**[1:12:24]** Sí.

**[1:12:26]** Así que no vamos a dejar así.

**[1:12:30]** Y por ejemplo

**[1:12:39]** dejarlo se podría

**[1:12:41]** crear una

**[1:12:43]** nueva columna.

**[1:12:45]** O sea en la tabla original

**[1:12:47]** tener una columna

**[1:12:49]** columnas con los días sería como

**[1:12:51]** no sería lo óptimo.

**[1:12:53]** Con la ficha.

**[1:12:57]** Sí, por ejemplo

**[1:12:59]** que la columna baby lexel

**[1:13:01]** o sea la segunda

**[1:13:03]** para lunes, pues martes,

**[1:13:05]** martes, miércoles y

**[1:13:08]** si le tienen razón, hagámoslo.

**[1:13:10]** 15

**[1:13:12]** de julio del

**[1:13:14]** 2016.

**[1:13:21]** De hecho tienen toda la razón porque

**[1:13:23]** además, además

**[1:13:25]** hay muchos miércoles.

**[1:13:29]** No se siguen eso.

**[1:13:32]** Hay muchos miércoles.

**[1:13:34]** Entonces necesito saber cuál es el miércoles exacto

**[1:13:36]** en el cual estoy midiendo esto.

**[1:13:40]** Rofi igual esto es una pedantería mía

**[1:13:42]** no más por si acaso es una pelea personal

**[1:13:44]** que yo tengo.

**[1:13:46]** Pero yo para fecha en cuanto bien mejor el ISO

**[1:13:48]** 86.01 que es año, mes, día

**[1:13:50]** es una pedantería mía así.

**[1:13:52]** Yo sé que es una tontera pero igual es

**[1:13:54]** como me toca limpiar

**[1:13:56]** datos mucho, son peleas que suelo tener yo.

**[1:13:58]** Ya, así?

**[1:14:01]** Sí, porque

**[1:14:04]** los primeros días de los primeros meses uno lo sabe

**[1:14:06]** si está con fecha gringo, fecha

**[1:14:08]** de acá.

**[1:14:10]** Está bien, está bien.

**[1:14:16]** Ya.

**[1:14:23]** ¿Algo más que sugeren?

**[1:14:28]** Me gusta, me gusta que

**[1:14:30]** tengamos esta discusión.

**[1:14:33]** Y yo pensaba dejar como

**[1:14:35]** en vez de tener una columna a día

**[1:14:37]** tener varias columnas con

**[1:14:39]** días

**[1:14:41]** o sea, no se

**[1:14:43]** se entiende.

**[1:14:45]** Sí, eso en general no se hace.

**[1:14:47]** Eso en general no se hace porque existe la estructura

**[1:14:49]** de datos

**[1:14:51]** de fecha.

**[1:14:53]** Por ejemplo, cuando tú trabajas con

**[1:14:55]** bandas

**[1:14:57]** generalmente tú trabajas con

**[1:14:59]** el dato en fecha

**[1:15:01]** y hay operaciones específicas que

**[1:15:03]** funcionan para fechas.

**[1:15:06]** Ya.

**[1:15:13]** Ok, eso es la clase

**[1:15:15]** de hoy.

**[1:15:17]** La próxima semana lo que vamos

**[1:15:19]** la próxima semana, el viernes

**[1:15:21]** este viernes lo que vamos a ver

**[1:15:23]** es exploración de datos.

**[1:15:25]** Ok, ¿no se si tiene alguna otra pregunta

**[1:15:27]** relacionada con la clase de hoy?

**[1:15:31]** Sí, más que con la clase

**[1:15:33]** es porque la próxima semana

**[1:15:35]** se supone que el 24

**[1:15:37]** es nuestro primer certamen

**[1:15:39]** ¿cuándo podría entregar

**[1:15:41]** el temario o la forma

**[1:15:43]** la modalidad de las preguntas?

**[1:15:45]** Ah, se lo puedo explicar al tiro.

**[1:15:47]** El temario

**[1:15:50]** para verlo a usted.

**[1:15:52]** Sí, el temario

**[1:15:54]** entrato hasta

**[1:15:56]** la clase de el viernes.

**[1:15:58]** ¿Ya?

**[1:16:00]** Y lo que van a tener que hacer

**[1:16:02]** son cuatro preguntas

**[1:16:04]** ah, no, perdón, miento

**[1:16:06]** no son cuatro preguntas.

**[1:16:09]** Son tres grupos de preguntas

**[1:16:11]** ¿Ya? Y una de esta

**[1:16:13]** de este grupo de preguntas es verdadero o falso

**[1:16:15]** con justificación, la otra es

**[1:16:17]** selección múltiple y la última

**[1:16:19]** es de desarrollo

**[1:16:21]** donde van a tener que hacer algo como lo que acabamos

**[1:16:23]** de hacer, que básicamente

**[1:16:25]** le doy una tabla y le digo mira

**[1:16:27]** esta tabla presenta muchos problemas

**[1:16:29]** que presenta y cómo lo resolverían.

**[1:16:31]** Rafa, disculpe.

**[1:16:35]** La modalidad, la modalidad es online

**[1:16:37]** a través de campas.

**[1:16:39]** Ah, ok.

**[1:16:45]** ¿Había otra pregunta?

**[1:16:47]** Rafa, que yo no escuché.

**[1:16:49]** Dale, Camilo, dale.

**[1:16:51]** Disculpe, ¿se abre en algún horario

**[1:16:53]** o algún día en particular?

**[1:16:55]** Sí, empieza a

**[1:16:57]** a las seis y cuarto el próximo viernes.

**[1:16:59]** Ya es ahora

**[1:17:02]** se abre

**[1:17:04]** el set también.

**[1:17:06]** Nos vamos a juntar por zoom

**[1:17:08]** y

**[1:17:10]** les voy a pedir que prendan las cámaras

**[1:17:12]** y yo voy a estar acá conectado

**[1:17:14]** por si tiene alguna duda o lo que sea.

**[1:17:16]** Ah, es sin crónico.

**[1:17:18]** Ya, es sin crónico, sí.

**[1:17:20]** Ah, ya es perfecto.

**[1:17:22]** Y dura desde las seis y cuarto

**[1:17:24]** hasta las nueve.

**[1:17:29]** En general es mucho más corto

**[1:17:31]** pero le doy ese plazo porque a veces

**[1:17:33]** algunos alumnos requieren más plazo.

**[1:17:36]** Perfecto.

**[1:17:39]** Yo creo que tranquilamente lo pueden determinar

**[1:17:41]** a las ocho. ¿Hay alguna otra pregunta?

**[1:17:51]** Lo que usted no acaba de comentar

**[1:17:53]** igual nos va a llegar como

**[1:17:55]** algún, lo va a subir en campas

**[1:17:57]** o

**[1:17:59]** con esto queda como

**[1:18:01]** sanjado el temario.

**[1:18:04]** Creo que con esto queda sanjado

**[1:18:06]** una cosa que es importante

**[1:18:08]** es que

**[1:18:10]** no hay

**[1:18:12]** o sea, entre solo la parte teórica

**[1:18:14]** ¿A qué me refiero con eso?

**[1:18:16]** Entran solo mis clases.

**[1:18:18]** No entran las clases de Alejandra.

**[1:18:21]** Las clases de Alejandra se evaluan

**[1:18:23]** a través de los proyectos, la parte práctica.

**[1:18:25]** Ah, ya perfecto.

**[1:18:28]** Gracias.

**[1:18:39]** Ok, lo dejamos hasta acá entonces.
