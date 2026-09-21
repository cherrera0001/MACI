# 2026-09-04T22_05_05Z Fundamentos en Ciencia de Datos.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 3:06:52
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:20:41]** ¿Me escuchan?

**[0:20:42]** Sí, grosor. Hola, buenas tardes.

**[0:20:44]** Hola, profe.

**[0:20:45]** Hola, profe.

**[0:20:47]** No alcanza a llegar a la casa a tiempo.

**[0:20:50]** Ya, vamos a empezar entonces con las presentaciones.

**[0:21:01]** Deme un minuto, por favor, a organizar acá la planía.

**[0:21:12]** Profe, nosotros como grupo queríamos pasar primero,

**[0:21:15]** no sé si con Germán y Rodolfo, no sé si es posible.

**[0:21:36]** Yo creo que sí, si es que nadie supone.

**[0:23:13]** Ya.

**[0:23:14]** Ok, ¿qué grupo son ustedes?

**[0:23:17]** No sé qué número de grupos somos, profe, pero...

**[0:23:21]** Germán Enriquez, Rodolfo Sañarto, Francisco Flores.

**[0:23:28]** Predicción de porcentaje de Síliz en concentrado.

**[0:23:32]** Ya, son el grupo dos.

**[0:23:34]** Ya.

**[0:23:38]** Dános más pancho.

**[0:23:41]** Comparto.

**[0:23:48]** Y ahí me confirman si es que se ve.

**[0:23:52]** Sí, se ve bien, bien.

**[0:23:55]** Ya, profe, usted nos dice.

**[0:23:57]** Entonces Germán Enriquez, Rodolfo Sañarto y Francisco Flores.

**[0:24:02]** Francisco Flores.

**[0:24:04]** Ya, dale.

**[0:24:06]** No se tienen 10 minutos y yo la hizo cuando se le va a acabar el tiempo, ¿qué?

**[0:24:11]** Poco, ya ok.

**[0:24:13]** ¿Iniciamos, no?

**[0:24:14]** Sí, perdón.

**[0:24:16]** Ya.

**[0:24:16]** Bueno, buenas tardes, profesor, compañeros.

**[0:24:19]** Ya sé que somos el grupo dos.

**[0:24:22]** Así que está compuesto como comentábamos por Germán, Rodolfo Sañarto y quien le habla

**[0:24:27]** Francisco Flores.

**[0:24:30]** El problema o el proyecto que nosotros tomábamos, ¿cierto?

**[0:24:34]** Que fueron dentro de los que compartió el profesor.

**[0:24:36]** Tiene que ver con el desafío o con el análisis, ¿cierto?

**[0:24:40]** De la predicción de porcentaje de Síliz en concentrado.

**[0:24:45]** Ya, en elito uno, nosotros...

**[0:24:48]** Ahí sí, ya, en elito uno, ¿cierto?

**[0:24:51]** ¿A qué nos dedicamos, ¿cierto?

**[0:24:53]** A limpiar los datos, a entender los datos y a ordenarlos de manera o temporalmente correcto,

**[0:25:02]** de acuerdo al análisis que estuvimos haciendo y una de las grandes insight que sacábamos,

**[0:25:09]** ¿cierto?

**[0:25:10]** Es que la Síliz no parece depender de una sola variable, sino que en realidad su comportamiento

**[0:25:16]** tiene que ver con distintos tipos de variables, ya sea por la alimentación dentro del proceso

**[0:25:24]** de flotación de minería.

**[0:25:25]** Bueno, me faltó decir eso, que esto se marca dentro de un proceso minero, ya que se llama

**[0:25:32]** flotación, ya en donde desde ahí se extrae un mineral, en donde que en este caso es

**[0:25:39]** concentrado de hierro y lo que buscábamos, ¿cierto?

**[0:25:41]** Es predecir el porcentaje de Síliz, el cual mientras menor se hace porcentaje, mejor es

**[0:25:48]** la calidad, ¿cierto?

**[0:25:49]** del producto final.

**[0:25:50]** Entonces, como les decía, estuvimos entendiendo los datos de que se trataban y una de las

**[0:25:55]** cosas que vimos es que depende de otras variables como son los procesos de alimentación, los

**[0:26:01]** datos de los reactivos que se agregan y también datos de la operación misma.

**[0:26:06]** Y en este segundo hito, ¿cierto?

**[0:26:08]** El foco estuvo en predecir valores futuros de Síliz usando variables también del proceso

**[0:26:13]** que se había encontrado que eran relevantes, ¿cierto?

**[0:26:15]** Y también considerando estas variables de lo que iba pasando o de lo que va pasando anterior

**[0:26:21]** al proceso.

**[0:26:22]** Una de las cosas relevantes que encontramos, ya lo primero que se analizó fue que la

**[0:26:30]** Síliz se presenta memoria temporal, ¿qué quiere decir esto?

**[0:26:34]** Que el valor actual, ¿cierto?

**[0:26:36]** Depende de lo que venía ocurriendo en el proceso en horas anteriores, ¿ya?

**[0:26:42]** Dentro de la análisis hicieron dos cosas, una fue una autocorrelación simple en donde

**[0:26:47]** se vio de que existía inercia en este proceso, ¿ya?

**[0:26:51]** Se ve una fuerte correlación, finalmente en que las horas anteriores al valor X que

**[0:26:56]** nosotros queremos predecir estaban fuertemente correlacionadas y en el gráfico del

**[0:27:00]** lado izquierdo se hizo una correlación parcial en donde se muestra, ¿cierto?

**[0:27:05]** Que el lag de las primeras tres horas ya es muy relevante para predecir, ¿cierto?

**[0:27:10]** El valor de la Síliz.

**[0:27:13]** Dentro de las características de ingeniería o la ingeniería de características, perdón,

**[0:27:18]** una de las cosas que hicimos en este análisis muy relevantes, una fue crear estas variables

**[0:27:23]** de los lag de las horas anteriores, tanto para el lag de una hora de dos horas

**[0:27:29]** y de tres horas y también se crearon variables que tenían que ver, ¿cierto?

**[0:27:35]** Con los procesos de los reactivos que se agregaban a este proceso, ¿ya?

**[0:27:41]** Y además se utilizó una, se calcularon, digamos, el top 15 de variables, ¿cierto?

**[0:27:50]** Que influían más en la predicción de este porcentaje de Síliz en concentrado.

**[0:27:57]** Todo el entrenamiento y validación de datos.

**[0:28:03]** Una de las cosas relevantes es que usitilizó Time Series Split, que esto es como no utilizamos

**[0:28:11]** una validación cruzada tradicional como puede ser el Key Fold, ¿ya?

**[0:28:19]** Que es lo que hace el Key Fold, toma observaciones de manera aleatoria para validar, ¿cierto?

**[0:28:25]** El modelo.

**[0:28:26]** Aquí el Time Series, el matiz que tiene es que no solamente toma, o sea, no es que tome

**[0:28:32]** variables de manera aleatoria tan solo, sino que sí o sí toma variables anteriores para

**[0:28:38]** validar, ¿cierto?

**[0:28:40]** El valor futuro.

**[0:28:41]** ¿Y esto por qué?

**[0:28:42]** Porque como decíamos anteriormente, el lag de las horas anteriores dentro del proceso

**[0:28:47]** tiene mucha correlación para la predicción de Síliz.

**[0:28:54]** También se utilizó un Random Size Search para ver la búsqueda dipper parámetros y también

**[0:28:59]** se utilizó una estrategia distinta al Exhibus que se utiliza tradicionalmente, sino que se

**[0:29:06]** hizo una estrategia de ocupar los delta que podrían ir dando estos valores, lo cual se

**[0:29:12]** va a explicar más adelante en la presentación.

**[0:29:14]** Bueno, para continuar con el análisis, en primer lugar exploramos un modelo que

**[0:29:20]** sería como nuestra línea base.

**[0:29:23]** Esto previo a evaluar como modelos más predictivos, más complejos, y tenía por objetivo tener

**[0:29:27]** una referencia simple.

**[0:29:29]** Para eso utilizamos este modelo, un modelo naive, que básicamente supone que el próximo valor

**[0:29:34]** de la Sílice será igual al último valor observado.

**[0:29:38]** Como vemos en el gráfico, vemos ambos datos representados, línea negra a los datos reales,

**[0:29:45]** línea roja vendría siendo el naive, y como se puede observar son muy similares

**[0:29:49]** solamente que están desplazados en una hora.

**[0:29:52]** Esto puede parecer una estrategia súper básica y como sencilla, pero debido a la fuerte autocorrelación

**[0:29:58]** como mencionaba Francisco, esta sí es un benchmark como bastante útil.

**[0:30:04]** Simplemente repetir el valor anterior, ya nos puede entregar una predicción razonable.

**[0:30:08]** Obviamente un modelo más sofisticado solo tiene sentido si logra mejorar esta línea

**[0:30:12]** base.

**[0:30:13]** Ahora pasando la comparación de modelos, comparamos distintas alternativas.

**[0:30:19]** Francisco las está proyectando.

**[0:30:21]** Usted utilizamos la misma metodología de validación y aquí están enumeradas las 5.

**[0:30:26]** Podemos ver modelos rich, random forest, ex-g-boost clásico, ex-g-boost delta predictor, y también

**[0:30:32]** está nuestro modelo naive.

**[0:30:34]** El principal criterio de comparación fue la recuadrado, que obviamente explica que

**[0:30:38]** también el modelo puede predecir el comportamiento de la Sílice.

**[0:30:43]** Además, revisamos los errores medios absolutos, entonces podemos observar que efectivamente

**[0:30:48]** el ex-g-boost delta predictor tiene un mayor re-cuadrado y también tiene un menor error

**[0:30:55]** medio absoluto.

**[0:30:56]** Así que en términos generales era el mejor modelo que podíamos presentar.

**[0:31:02]** La lamina siguiente, aparecen los valores más en detalle y ahora Germán continúa con

**[0:31:09]** el modelo y el resto de resultados.

**[0:31:12]** Gracias Rodolfo.

**[0:31:15]** Bueno, como Rodolfo mencionó anteriormente, nosotros utilizamos un modelo ex-g-boost.

**[0:31:19]** Aquí cuando le pusimos delta, nos referimos a que este modelo, en vez de calcular el valor

**[0:31:24]** absoluto siguiente, calcula la variación.

**[0:31:26]** Por lo tanto, el valor final es el valor actual más la predicción y obtuvimos la curva azul

**[0:31:34]** acá.

**[0:31:35]** Si se ve igual, hay un problema de que se ve un poquito desplazada, debido a la fuerte

**[0:31:39]** inercia del proceso.

**[0:31:40]** Pero sin embargo, es un poco mejor que el modelo base, eso evidentemente que el recuadrado

**[0:31:45]** es un tanto superior.

**[0:31:47]** Sí, Iván Sandu, por favor.

**[0:31:50]** Bueno, sobre la memoria del proceso que hemos mencionado anteriormente.

**[0:31:53]** Aquí no solo viendo los fichos más relevantes para el modelo, aquí ex-g-boost tiene

**[0:31:58]** la ventaja de que saber la relevancia y los tributos es muy sencillo.

**[0:32:02]** Podemos determinar que los lag definitivos de uno a dos horas son los que más pesan.

**[0:32:07]** Aquí como comentario aparte, se intentó con un modelo que no tenía las variables

**[0:32:09]** layas y el recuadrado era menor a un 0,1.

**[0:32:12]** Entonces tenemos que considerar sí o sí las variables anteriores.

**[0:32:15]** Por otro lado, hay variables como el pH, el ratio entre aminicilis, el flujo de amina y

**[0:32:22]** dosias específicas entre otros que nosotros creamos que desde un punto disto metalúrgico

**[0:32:26]** tienen sentido porque son variables que dominan el proceso de rotación.

**[0:32:29]** Sí Iván Sandu, por favor.

**[0:32:33]** Entonces aquí nosotros pensamos, tenemos este modelo que es un tanto mejor que simplemente

**[0:32:38]** tomar el valor anterior para que nos sirva esto.

**[0:32:41]** Aquí la aplicación industrial más clásica es un sistema alerta temprana.

**[0:32:45]** Aquí nosotros lo que podríamos decir es que nosotros estimamos que para uno a dos horas

**[0:32:48]** adelante, yo no, este modelo no es capaz de hacer peticiones para más de dos horas por

**[0:32:51]** su caso, tal cosa podría ocurrir.

**[0:32:54]** Entonces intenta adelantarte de eso y es algo un cambio operacional, es algo un cambio de

**[0:32:58]** variable, un variable objetivo o incluso pensando en la imagen grande, este modelo

**[0:33:02]** se podría combinar junto con un optimizador y directamente dictar variables operacionales.

**[0:33:08]** Sin embargo, como dijimos, le recuerdo a este modelo que no es tan alto.

**[0:33:12]** Entonces tenemos la limitación con los datos.

**[0:33:13]** Normalmente minería, el proceso anterior importa mucho y el origen terminal también.

**[0:33:17]** Hay características mineralógicas que en este momento nosotros no tenemos y también no

**[0:33:21]** tenemos detalles del proceso anterior de molienda.

**[0:33:23]** Si tuviéramos detalles de molienda, quizás podríamos tener una mayor predicción de

**[0:33:27]** lo que se ve en el futuro.

**[0:33:29]** La siguiente, por favor.

**[0:33:32]** Y bueno, ¿qué concluimos de acá?

**[0:33:35]** Solo pasamos desde un análisis descriptivo hasta un modelo predictivo interpretable.

**[0:33:39]** En primer lugar, tenemos a mejora modelada su modelo naive.

**[0:33:41]** ¿Es mejor que predicir que entregar para anterior?

**[0:33:44]** Sí, no es tanto, pero algo es mejor.

**[0:33:47]** El espacio para mejorar mineralogía, molienda, granulometría, origen terminal, todo eso

**[0:33:51]** nos podría ayudar a tener un modelo de mayor calidad, porque esos son variables que

**[0:33:54]** desde la literatura y la investigación sabemos que afectan mucho la flotación.

**[0:33:57]** ¿Y qué existe un potencial valor en un modelo de este estilo?

**[0:33:59]** Que puedas situar una mejor interpretación.

**[0:34:02]** Mejor, pero mejor indicar el rendimiento.

**[0:34:06]** Si es que serviría para hacer un sistema de alerta temprana.

**[0:34:12]** Eso sería.

**[0:34:12]** Muchas gracias.

**[0:34:16]** Gracias.

**[0:34:19]** OK, un par de preguntas.

**[0:34:22]** La primera pregunta va para Francisco.

**[0:34:27]** OK.

**[0:34:29]** ¿Los datos?

**[0:34:32]** ¿En qué rangos venían y a qué rangos llegaron?

**[0:34:35]** Me explico.

**[0:34:35]** O sea, usted mostró un gráfico de una hora, ¿certo?

**[0:34:39]** Donde salen los datos en periodos de una hora.

**[0:34:46]** Entonces, ¿en qué rangos venían o cuál eran las diferencias temporales?

**[0:34:50]** ¿Cuánto era entre una misión y la otra, en la original?

**[0:34:55]** La mayor granularidad estaba por...

**[0:35:01]** Por ahora, si mal no recuerdo, sí, está en...

**[0:35:04]** Por ahora esa era la granularidad, yo.

**[0:35:10]** Pero no había datos, ni el de minutos.

**[0:35:17]** En el target no.

**[0:35:20]** No.

**[0:35:22]** El target es la Silice, en realidad.

**[0:35:26]** Si, el target estaba acá una hora.

**[0:35:27]** Entonces, al final eso no restringía la granularidad de los datos que pudimos usar,

**[0:35:31]** porque había otros datos que se notaban que en el sensor está incluso cada 20 segundos.

**[0:35:34]** Pero el target que es de la Silice estaba acá una hora.

**[0:35:37]** Ah, ya.

**[0:35:38]** OK, perfecto.

**[0:35:41]** Otra pregunta, digamos para Germán.

**[0:35:44]** Si tuvieran que continuar con este proyecto, ¿cuál sería el siguiente paso?

**[0:35:49]** Como dije aquí, sería intentar no tener más información,

**[0:35:52]** porque en este momento puedes poner el rol,

**[0:35:54]** fue la imagen con la comparación de los modelos.

**[0:35:56]** O sea, el gráfico del delacere tiempo.

**[0:36:01]** Aquí como vemos, igual la capacidad de situación no está tan buena.

**[0:36:05]** ¿Es mejor que el modelo del valor anterior?

**[0:36:08]** Sí, pero tampoco es tanto mejor.

**[0:36:09]** Entonces, aquí hay que agregar variables que se pueden anticipar.

**[0:36:13]** Como mencioné aquí, si pudiera agregar variables de moliendo,

**[0:36:15]** o incluso de geología, esto mejoraría arto de la capacidad del modelo.

**[0:36:19]** Y si con eso mejoramos las métricas de rendimiento del modelo,

**[0:36:22]** y como les había mencionado,

**[0:36:23]** eventualmente quizás hasta podría meterle un optimizador al modelo,

**[0:36:27]** definirse estas variables operacionales como las variables de optimizar,

**[0:36:30]** y eventualmente hacer un recomendador.

**[0:36:31]** Si así podríamos avanzar con esto y tendríamos un impacto muy claro.

**[0:36:35]** Y Rodolfo, en términos de modelos predictivos, ¿qué podrían hacer?

**[0:36:42]** ¿Se te ocurra algo que podrían cambiar?

**[0:36:49]** Estoy pensando porque nosotros también vimos en clases y también lo intentamos,

**[0:36:54]** y lo discutimos en el grupo sobre las redes neuronales.

**[0:36:58]** Pero la verdad, no voy a ser sincero, yo no las testíe, las testíe German,

**[0:37:04]** pero llegamos rápidamente a la conclusión de que no funcionaban.

**[0:37:09]** Por eso seguimos insistiendo con el XGBoost,

**[0:37:12]** y de hecho llegamos ahí al Delta Predictor, que era mejor que el clásico.

**[0:37:19]** Desconozco si es que además de la red neuronal y estos modelos de árboles,

**[0:37:24]** podemos aplicar otra alternativa,

**[0:37:31]** pero por lo menos este de árbol era el que mejor rendimiento tenía.

**[0:37:36]** ¿El resto no se le ocurra algo más que podrían haber hecho?

**[0:37:40]** O que podrían hacer a futuro, en realidad, no que podrían haber hecho así.

**[0:37:44]** Está bien lo que hice.

**[0:37:47]** No, y la verdad, probar estos modelos,

**[0:37:50]** aquí estábamos mostrando 5, pero realmente como 15 modelos distintos,

**[0:37:53]** con distintas especificaciones, también no sé cómo se llaman,

**[0:37:57]** esta normalización de los datos, y la verdad, eso fue lo mejor que alcanzamos.

**[0:38:02]** Probábamos también la red neuronal con el long-charton memory,

**[0:38:05]** que es típico para hacer esto de tiempo, y de hecho lo recuadraron,

**[0:38:07]** nos vio como 0,5, entonces, y la debería de tener ellos que faltan datos,

**[0:38:11]** que eran un poco de datos, suele pasar por la red neuronal,

**[0:38:14]** pero más allá de eso, no sé qué se podría hacer,

**[0:38:17]** que en mi experiencia nosotros vamos a ver XGBoost en producción para problemas así,

**[0:38:23]** y por eso nos quedamos después con la conclusión de quizás más variables al modelo,

**[0:38:26]** quizás es mejor que buscar otro modelo de inteligencia.

**[0:38:30]** Pásima grande de datos también, quizás eso podría ayudar a la proyectilidad.

**[0:38:35]** Ya, ok, muchas gracias.

**[0:38:41]** Valencia.

**[0:38:42]** ¿Alguien sufre ese siguiente?

**[0:38:45]** Sí, profe, nosotros.

**[0:38:48]** Segundo, a ver, para, dice segundo grupo, Jorge Pucci, Valentina Jara,

**[0:38:54]** eso a usted?

**[0:38:56]** Sí.

**[0:38:57]** Ya, ¿sabes?

**[0:39:25]** Sí, ¿sabes?

**[0:39:29]** Ya, bueno, buenas tardes.

**[0:39:31]** Nuestro grupo va a presentar clasificación de tumores mamarios mediante análisis

**[0:39:35]** muy fológico de vio, no sé qué grupo somos,

**[0:39:38]** pero está conformado por Yodari, Jorge, Cristian y yo, Valentina.

**[0:39:45]** Bueno, como introducción, el problema es la alta incidencia del cáncer de mama,

**[0:39:52]** que es una necesidad de diagnósticos rápidos y certeros.

**[0:39:55]** Esto también tiene una relevancia operacional que es reducir la subjetividad

**[0:39:58]** de la persona que en el fondo diagnostica o revisa el examen

**[0:40:02]** y optimizar tiempos en detectar patología.

**[0:40:06]** Entonces, acá vamos a ver un resumen del análisis exploratorio

**[0:40:11]** que en el fondo vimos la clase anterior

**[0:40:14]** y el data set que nosotros teníamos eran 569 registros,

**[0:40:19]** 62.7% benignos y el resto malignos.

**[0:40:23]** No habían ID duplicados o filas con información repetida,

**[0:40:26]** no habían valores nulos.

**[0:40:28]** Y lo que nos dábamos cuenta es que los 10 parámetros

**[0:40:30]** que caracterizaban los núcleos celulares en los tumores malignos

**[0:40:34]** presentaban valores significativamente mayores que los benignos

**[0:40:37]** en variables geométricas como radioperimetroaria

**[0:40:40]** y también en irregularidad del contorno, o sea, la concavidad.

**[0:40:44]** Entonces, bueno, ahí en los boxplots se puede ver que en puntos concavo,

**[0:40:50]** perímetro, radio, área, en los malignos,

**[0:40:52]** estos datos eran mucho más grandes que los benignos

**[0:40:55]** y por ende llegamos a la hipótesis de que los tumores mamarios malignos

**[0:40:59]** presentan valores significativamente mayores que los benignos

**[0:41:02]** y entonces podríamos o esto podría permitir clasificar la naturaleza del tumor

**[0:41:06]** mediante algoritmos de aprendizaje y supervisión.

**[0:41:10]** Entonces, modelamiento.

**[0:41:13]** Acá estamos frente a un problema de clasificación

**[0:41:16]** porque la idea es clasificar si el tumor es maligno o benigno.

**[0:41:20]** Entonces, los modelos que nosotros proponimos que vamos a probar

**[0:41:23]** va a ser regresión logística, SVM o support vector machine

**[0:41:27]** y random forest.

**[0:41:28]** ¿Por qué estos tres modelos?

**[0:41:30]** Bueno, primero porque con 569 muestras no alcanza para,

**[0:41:34]** por ejemplo, probar una red neuronal.

**[0:41:38]** Aparte que la regresión logística es simple,

**[0:41:41]** quizás random forest y SVM son un poco más complejos,

**[0:41:44]** pero vamos a ver si podemos obtener mejores médicas

**[0:41:46]** y por otro lado, todos entregan probabilidades.

**[0:41:48]** Por lo tanto, podríamos construir la curva rock,

**[0:41:51]** ver con qué un brail funciona mejor o también poder en el fondo

**[0:41:57]** definir cuál es el punto de operación mejor para este caso.

**[0:42:04]** ¿Yodadi?

**[0:42:05]** Ahora bien, la elección de los tres modelos no fueron

**[0:42:09]** arbitrarias, que responden a una necesidad de cubrir

**[0:42:13]** tres razones principales de clasificación sin sesgal

**[0:42:16]** el análisis hacia un solo enfoque.

**[0:42:19]** Como dijo Lavalle, la regresión logística representa

**[0:42:22]** el extremo lineal, como vamos a usarlo como una línea de base.

**[0:42:26]** El random forest se incluye porque, como vimos en el análisis

**[0:42:29]** exploratorio, existen correlaciones fuertes entre

**[0:42:32]** el variable y el support vector machine se dirige porque

**[0:42:36]** en la fase anterior de exploratorio mostró que la

**[0:42:40]** separación entre clases, si bien clara, no es perfecta.

**[0:42:44]** Ya.

**[0:42:45]** Y siguiente, por favor.

**[0:42:48]** En cuanto a la metodología de ajuste,

**[0:42:52]** el procesamiento contempló la eliminación de la columna ID,

**[0:42:57]** la codificación binaria del diagnóstico,

**[0:43:00]** que sea como cero para benigno y uno para maligno,

**[0:43:05]** y la estandarización de todas las variables mediante

**[0:43:08]** ¿Por qué lo estandalizamos?

**[0:43:10]** Que en los dos modelos que vamos a usar,

**[0:43:13]** de los tres, hay dos que son más sensibles a la escara.

**[0:43:17]** Entonces ahí, por lo tanto, vamos a estandarizar los datos.

**[0:43:21]** Ya y los datos se dieron de forma estratégica,

**[0:43:25]** 80% para entrenamiento, que son más o menos 455 observaciones,

**[0:43:30]** y 20% para prueba, que son más o menos 114 observaciones.

**[0:43:34]** Y cada modelo fue validado con cinco paticiones

**[0:43:37]** de validación cruzada, usando el mismo número de participación

**[0:43:41]** para evitar y para poder obtener una muy buena comparación

**[0:43:44]** y que sea más equitativo al momento de hacer la comparación.

**[0:43:48]** Siguiente, por favor.

**[0:43:52]** Ya.

**[0:43:53]** Como resultado de fase 1, que vamos a usar como fase de comparación,

**[0:43:57]** que es como usamos por defecto un umbral de decisión de 0,5.

**[0:44:03]** Por lo tanto, como resultado, las matrices de confusión reveran

**[0:44:06]** un hallazgo consistente entre los tres modelos donde,

**[0:44:09]** sin excepción, cada uno comete exactamente un falso negativo.

**[0:44:14]** Ese falso negativo significa que está clasificando como un maligno

**[0:44:18]** como un benigno.

**[0:44:19]** De esos 42 casos malignos en el conjunto de pruebas que usamos.

**[0:44:24]** Mientras que los falso positivos varían entre 2 y 5

**[0:44:28]** según el algoritmo.

**[0:44:30]** Lo que va a hacer en ese momento,

**[0:44:32]** ya vamos a considerar el siguiente paso que es la siguiente fase

**[0:44:36]** que va a hacer ajustar el umbral para eliminar por completo

**[0:44:40]** los falso negativos.

**[0:44:43]** Siguiente.

**[0:44:45]** Sí.

**[0:44:46]** Bueno, respecto a las métricas de los tres modelos,

**[0:44:51]** observamos que los tres modelos, el recall y el auce,

**[0:44:57]** son muy parecidos, lo cual indica que los desempeños parecidos

**[0:45:04]** a los modelos, pero varían en la exactitud y la precisión.

**[0:45:09]** Ahí el reelección logística tiene el mejor desempeño

**[0:45:14]** y el peor desempeño es random forest.

**[0:45:18]** Y siguiente, por favor.

**[0:45:23]** Y respecto a la curva rock, viendo el desempeño de los tres

**[0:45:27]** modelos, observamos que prácticamente las curvas se

**[0:45:32]** sobreponen.

**[0:45:33]** Entonces, esto nuevamente indica un desempeño muy parecido y,

**[0:45:39]** bueno, y ligeramente mayor en el caso del Superfactor Machine,

**[0:45:45]** el auce, pero es prácticamente despreciable la diferencia.

**[0:45:51]** Y, bueno, todas tienen, los modelos tienen una tasa de

**[0:45:54]** verdadero positivo muy alta y falso positivo baja.

**[0:46:01]** Y siguiente.

**[0:46:05]** Y bueno, y como hay algo de esta fase 1 en el que todos tenían

**[0:46:10]** el mismo umbral, los tres modelos dejan pasar un,

**[0:46:16]** exactamente un tumor maligno como benigno,

**[0:46:20]** que era lo que mostró mi compañero al comienzo.

**[0:46:23]** Y esto es inaceptable porque no puede a un paciente con un

**[0:46:29]** tumor maligno decirle que es benigno,

**[0:46:31]** o sea, un falso negativo.

**[0:46:33]** Entonces, la siguiente fase, lo que se va a hacer es modificar

**[0:46:37]** este umbral de decisión para que así el recall lleve un 100%

**[0:46:44]** o sea que todos los, los verdaderos positivos sean igual a los

**[0:46:49]** positivos.

**[0:46:50]** Sigamente.

**[0:46:53]** Ya.

**[0:46:53]** Entonces, como comentaba mi compañero, en la fase 1 se

**[0:46:56]** definió un umbral por defecto 05.

**[0:46:59]** Igual se gráficó la curva ROG y el área bajo la curva para

**[0:47:02]** generalizar.

**[0:47:03]** Pero acá lo que se va a hacer, el fondo, como es un caso médico y

**[0:47:09]** a una persona que tiene cáncer se le está diciendo que no tiene.

**[0:47:12]** Como comentaron mis compañeros, vamos a ajustar el recall a 100%

**[0:47:15]** para que los detecte todos.

**[0:47:16]** Entonces, en el fondo, lo que se hace es sacar la probabilidad

**[0:47:19]** para los tres modelos de esa muestra que está difícil de

**[0:47:24]** en el fondo de clasificar como maligno y bajar el umbral.

**[0:47:27]** Al bajar el umbral quizás va a tener un costo porque van

**[0:47:32]** a entrar cosas que quizás son benignas y las va a considerar

**[0:47:35]** como malignos.

**[0:47:36]** Entonces, en el fondo, lo que se ve acá es que en la fase 2,

**[0:47:40]** donde se ajusta el recall, ya no hay falsos negativos,

**[0:47:43]** sin embargo, la precisión cae demasiado entre 042.

**[0:47:47]** y 033, donde el que menor cae o el que menos cae es el random

**[0:47:51]** force.

**[0:47:52]** Entonces, si vemos de nuevo los matices de confusión,

**[0:47:55]** ahora detecta todo lo maligno.

**[0:47:58]** ¿En qué tanto minuto?

**[0:47:59]** Ya, detecta todo lo maligno, pero el problema está arriba.

**[0:48:02]** O sea, en el fondo, en la regresión logística,

**[0:48:05]** a 37 personas se les está diciendo que tienen cáncer

**[0:48:07]** cuando en verdad no lo tienen.

**[0:48:09]** Y el menor de estos casos es el random force.

**[0:48:13]** Entonces, ajustando el recall, el mejor modelo sería el random

**[0:48:17]** force.

**[0:48:18]** Entonces, como conclusión, ningún modelo es perfecto.

**[0:48:21]** Con umbral 05, los tres modelos cometen al menos un

**[0:48:23]** falso negativo.

**[0:48:26]** Si la decisión clínica exige el recall al 100%,

**[0:48:29]** entonces nos va a costar puntos de precisión y bastantes

**[0:48:31]** puntos de precisión.

**[0:48:33]** Pero, por otro lado, también se confirma la hipótesis que

**[0:48:35]** teníamos al principio de este proyecto,

**[0:48:38]** que es que, en el fondo, estas variables geométricas o de

**[0:48:42]** contorno podrían servir para poder clasificar la naturaleza del

**[0:48:46]** tumor mediante algoritmos de aprendizaje supervisados.

**[0:48:50]** Sin embargo, como no es perfecto,

**[0:48:52]** quizás mucha gente va a tener que volver a repetirse el

**[0:48:54]** examen.

**[0:48:55]** Eso.

**[0:48:56]** Muchas gracias.

**[0:49:05]** Está silenciado, profe, por eso.

**[0:49:09]** Ya, gracias.

**[0:49:11]** Entonces, no me escucharon cuando les dije que le quedan dos

**[0:49:12]** minutos.

**[0:49:13]** No, sí, eso sí.

**[0:49:15]** También.

**[0:49:16]** Ya.

**[0:49:19]** Partamos por Cristian.

**[0:49:22]** ¿Y si lo buscaba hiperparámetro en los modelos?

**[0:49:25]** Perdón.

**[0:49:29]** Sí, si lo hiperparámetro, sí.

**[0:49:32]** ¿Suscubieron?

**[0:49:34]** ¿Qué hiperparámetro buscaron y cómo lo hicieron?

**[0:49:38]** Por ejemplo, bueno, ahí la redición logística,

**[0:49:43]** ahí en este caso tenemos una redición logística o no,

**[0:49:51]** acuerdo, ¿cuál es hiperparámetro ahora?

**[0:49:54]** Mismo.

**[0:49:58]** Se tendría que volver a.

**[0:50:01]** ¿Cómo?

**[0:50:02]** Ahí puedo complementar.

**[0:50:04]** Sí, sí.

**[0:50:06]** Que en el fondo, en el estudio.

**[0:50:13]** Así, ahí había que se indicaba.

**[0:50:22]** Ya, aquí en el fondo con variación cruzada y con grit search,

**[0:50:27]** buscábamos los hiperparámetros o la combinación,

**[0:50:31]** la mejor combinación de hiperparámetros para no

**[0:50:33]** tener sobreajuste.

**[0:50:35]** Y en el fondo definíamos el C y el GAM para support vector

**[0:50:39]** machine y para el otro definimos max features,

**[0:50:49]** mean sample, split, mean sample, leap.

**[0:50:54]** Pero en el fondo con variación cruzada intentábamos jugar

**[0:50:58]** con las combinaciones para el fondo no caer en el sobreajuste.

**[0:51:04]** Ya, y Valentina, ¿qué quiere decir, por ejemplo,

**[0:51:07]** un número de árboles profundidad,

**[0:51:09]** mínimo de muestra, por hoja, división?

**[0:51:14]** O sea, yo lo entiendo como que random forest ocupa

**[0:51:16]** demasiado árboles.

**[0:51:17]** Entonces, según hiperparámetros,

**[0:51:19]** definir cuántos árboles vamos a usar para quien en

**[0:51:21]** el fondo decida, decida.

**[0:51:26]** Ya, otros hiperparámetros, es decir, por ejemplo,

**[0:51:29]** ¿cuánto voy a penalizar algo malo en el caso de support vector

**[0:51:39]** machine?

**[0:51:41]** Eh, yeah.

**[0:51:44]** En el caso de support vector machine hay que una que la

**[0:51:47]** regularización, que usamos el C para la regularización,

**[0:51:50]** y gama como para alcanzar de cada, para ver cada soporte.

**[0:51:54]** Y en ese caso, como ambos controlan la complejidad del

**[0:51:58]** modelo, y así se evita el riesgo de sobreajuste.

**[0:52:03]** ¿Qué creo que gama, Jodady?

**[0:52:06]** Es el alcance de los vectores del soporte.

**[0:52:12]** ¿Por qué dice que en el RBF hay?

**[0:52:15]** ¿Qué pasó?

**[0:52:17]** ¿Por qué dice que en el RBF?

**[0:52:23]** ¿Darred de F?

**[0:52:25]** ¿Dice gama, que en el RBF?

**[0:52:28]** Porque en el fondo no ocupamos un modelo lineal.

**[0:52:35]** O sea, en el fondo de la frontera, no es genial.

**[0:52:38]** ¿Ya hay el gama que es?

**[0:52:42]** El gama es el...

**[0:52:48]** El que controla como el tradeoff, entre la máxima,

**[0:52:52]** va a separación y que como un tradeoff el gama,

**[0:52:55]** usamos el gama como un tradeoff para...

**[0:52:58]** Ese es el C, ese es el C.

**[0:53:03]** ¿El gama es como el alcance de cada punto?

**[0:53:11]** Como tú decía, Valentina, el truco para el supervector machine

**[0:53:16]** para que no sea lineal, es cambiarle el kernel.

**[0:53:20]** Esto cambia un kernel que es la forma en la cual mide las distancias

**[0:53:23]** y hace que esta forma sea no lineal

**[0:53:26]** y de esa forma básicamente el plano se dobla.

**[0:53:30]** ¿Y el gama tiene relación con qué tan ancho ese kernel?

**[0:53:36]** Los 4, ya.

**[0:53:40]** Para decir como está más arriba.

**[0:53:44]** ¿Cómo eso? Para determinar como en caso de que cuando está más arriba

**[0:53:48]** del culva del modelo de ROG,

**[0:53:52]** ese es el gama.

**[0:53:54]** No, el gama lo que hace...

**[0:53:57]** El supervector más chino es un modelo lineal, ¿certo?

**[0:54:00]** Sí.

**[0:54:01]** Entonces tú lo que hace es que hace una transformación del espacio

**[0:54:05]** y entonces como que doblas todo el espacio

**[0:54:08]** y dentro de eso también dobla el plano separado.

**[0:54:11]** Y para hacer ese doblez, tú lo que tienes que hacer

**[0:54:15]** es cambiarle una transformación a las coordenadas.

**[0:54:20]** Y esa transformación se hace a través de un truco que se llama el truco del kernel

**[0:54:24]** que lo que hace es que para calcular distancias

**[0:54:28]** entre un punto y otro en vez de hacer una distancia lineal

**[0:54:32]** tú lo que hace es que usamos un kernel para calcular la distancia

**[0:54:36]** que en este caso es una radiación kernel gaussiano

**[0:54:39]** y lo que hace es que como que dobla el espacio para que tú puedas

**[0:54:44]** para que tú puedas calcular...

**[0:54:47]** En realidad dobla indirectamente el espacio

**[0:54:50]** pero el truco es que las distancias las calculan de otra forma

**[0:54:53]** a través de un kernel en este caso gaussiano

**[0:54:57]** y el gama en este caso es el ancho de la gaussiana

**[0:55:02]** entonces mientras más ancho

**[0:55:07]** la gaussiana más se aparecerá a una cosa lineal

**[0:55:11]** y si es chiquitito dobla mucho el espacio.

**[0:55:18]** Una pregunta ahora me falta Jorge

**[0:55:22]** Jorge, pueden poner el gráfico?

**[0:55:25]** Sí, es un tema...

**[0:55:28]** Sí, tengo que haberlo mencionado desde un comienzo

**[0:55:30]** pero el Jorge tenía un vuelo

**[0:55:33]** y por eso no se pudo presentar

**[0:55:36]** pero ahí decimos su parte con la Valentina

**[0:55:41]** ¿Y le mando un correo?

**[0:55:43]** Eso, comento que le había mandado un correo

**[0:55:45]** visando de su situación, trabajado en el norte

**[0:55:48]** Ya, ya.

**[0:55:50]** Ok, entonces dejémelo hasta acá.

**[0:55:53]** Ya, gracias.

**[0:55:56]** Gracias.

**[0:55:58]** ¿Y quién es el siguiente grupo en el chat?

**[0:56:01]** Vengo yo.

**[0:56:02]** ¿Hay un cuarto pero no un tercero?

**[0:56:05]** Vengo yo.

**[0:56:07]** Ah, ya.

**[0:56:08]** Ya.

**[0:56:11]** Compartó.

**[0:56:14]** ¿Te ves?

**[0:56:28]** Sí, se ve.

**[0:56:30]** Pero se ve en modo edición.

**[0:56:32]** Ya.

**[0:56:40]** Vamos a ver esto.

**[0:56:43]** Ya.

**[0:56:52]** ¿Sabe bien o no?

**[0:56:55]** Sí, ya.

**[0:56:57]** Perdón.

**[0:56:59]** Buenas tardes a todos.

**[0:57:02]** A mí, mi proyecto se trata de una prueba de concepto

**[0:57:06]** ya para ver la posibilidad de poder detectar

**[0:57:10]** tempranamente la probabilidad de que un estudiante

**[0:57:13]** pueda o no reprobar una asignatura

**[0:57:16]** antes del inicio de clases del primer semestre

**[0:57:19]** estudiante de pregrado.

**[0:57:23]** Vamos a hacer un resumen sobre elito 1

**[0:57:26]** ya que teníamos una hipótesis 0, una hipótesis 1.

**[0:57:30]** La hipótesis 0 es que las variables de pre-ingreso

**[0:57:35]** no nos permiten adecuadamente

**[0:57:39]** poder tener un modelo de referencia

**[0:57:42]** que podamos tener la probabilidad

**[0:57:45]** de predecir si un estudiante

**[0:57:47]** va a reprobar o no va a reprobar

**[0:57:49]** esta asignatura.

**[0:57:51]** Y la hipótesis 1 en la que yo quiero demostrar

**[0:57:54]** es que decir que con las variables de pre-ingreso

**[0:57:57]** que yo escoja, podemos predecir

**[0:58:00]** que un estudiante sí va a...

**[0:58:03]** va a tener o sea, podemos ver la probabilidad

**[0:58:06]** de que un estudiante pueda reprobar esta asignatura.

**[0:58:09]** Ya, asiento como un recordatorio,

**[0:58:12]** yo recibí un data set de 5.091 datos,

**[0:58:15]** elegí 7 programas

**[0:58:18]** que tenían esta nueva asignatura en común

**[0:58:21]** y son programas que son carreras de ingeniería

**[0:58:24]** que tuvieron pruebas de administración.

**[0:58:28]** Hice la limpieza y me quedé con 1.300 datos

**[0:58:31]** ya sin duplicados

**[0:58:34]** y un umbral institucional de aprobación

**[0:58:37]** de esta asignatura

**[0:58:39]** de 55 o mayor a 55.

**[0:58:42]** Al final nos quedamos con 809 aprobados,

**[0:58:45]** 492 reprobados

**[0:58:48]** y tenemos un de balanceo mediano.

**[0:58:54]** Ya, acá un poquito al contexto del estudio

**[0:58:57]** ya que habla como de lo mismo

**[0:59:00]** de lo que le había comentado anteriormente

**[0:59:03]** y tenemos también

**[0:59:06]** la variable numérica y la variable escatególica

**[0:59:09]** ya que consideramos

**[0:59:12]** en esta prueba concepto.

**[0:59:17]** Y las asociaciones lineales, ya con la nota de la asignatura

**[0:59:20]** y las variables, acá tenemos solamente

**[0:59:23]** variables numéricas, ya utilizamos la correlación de parsos

**[0:59:26]** más cercanas a uno, tiene una mayor correlación

**[0:59:29]** y como son carreras de ingeniería M1

**[0:59:32]** nos dio una correlación más alta, pero aún así

**[0:59:35]** el puntaje de ciencia, igual, llama bastante la atención.

**[0:59:38]** Ya.

**[0:59:40]** Y compresión lectora que va por debajo de ciencias.

**[0:59:43]** Eso sería como la correlación.

**[0:59:47]** Y ahora entramos al modelamiento

**[0:59:50]** 2 para el entrenamiento,

**[0:59:53]** la validación y el test.

**[0:59:56]** Ya nos quedamos con 1301 datos,

**[0:59:59]** ya separamos 80 y 20, dejamos 1040

**[1:00:02]** datos para entrenamiento y validación y dejamos

**[1:00:05]** 201 datos para test. Esos 201 datos nunca lo tocamos

**[1:00:08]** y lo dejamos fuera de la muestra para el entrenamiento

**[1:00:11]** y para la validación. Acá está. Un poquito

**[1:00:16]** del diseño instrumental. Acá donde ya le hablaba

**[1:00:19]** 80%, 1040, reserva 20, que fueron

**[1:00:22]** 261. Nuestra clase 0,

**[1:00:25]** yo la determiné como

**[1:00:27]** reprobado la clase 1 como

**[1:00:30]** aprobar. Ya.

**[1:00:32]** ¿Qué utilizamos acá?

**[1:00:34]** Esto fue aleatorio, ya.

**[1:00:36]** Pero como igual,

**[1:00:38]** hay un depalanceo, había que hacer una proporción

**[1:00:41]** entre aprobado y reprobado

**[1:00:44]** y, perdón, entre el

**[1:00:46]** desarrollo y la reserva y para eso

**[1:00:49]** utilicé stratificación

**[1:00:52]** para dejar proporcionalmente lo mayor

**[1:00:55]** posible entre

**[1:00:58]** ambos conjuntos de datos, tanto para el entrenamiento

**[1:01:00]** como para el test. Ya para

**[1:01:03]** las variables numérica

**[1:01:06]** a, utilicé una semilla 42,

**[1:01:09]** el 42 no tiene ninguna referencia, ninguna

**[1:01:12]** no afecta al modelo ni la probabilidad, solamente una semilla

**[1:01:15]** para que si otra persona ocupa este modelo

**[1:01:17]** se haga y tiene que empezar con esto porque puede

**[1:01:19]** empezar con otra y ahí no le va a dar

**[1:01:21]** exactamente lo mismo. Nuestras

**[1:01:24]** clases de interés es 0, que es reprobado

**[1:01:26]** y

**[1:01:28]** ya.

**[1:01:30]** En la reserva la nota

**[1:01:32]** de la asignatura no se va a utilizar como

**[1:01:34]** aquí vamos

**[1:01:38]** con la preparación y la

**[1:01:40]** validación. Bueno, las 7

**[1:01:42]** variables numéricas

**[1:01:44]** utilicen la mediana y standard

**[1:01:46]** standard para instutar los faltantes

**[1:01:48]** porque

**[1:01:50]** teníamos none y

**[1:01:52]** no todos los estudiantes dieron todas

**[1:01:54]** las pruebas, algunos dieron ciencias

**[1:01:56]** y otros dieron historias

**[1:01:58]** y para las categoricas

**[1:02:00]** utilicé la moda, one foot

**[1:02:02]** and coin, ya, para igual porque teníamos

**[1:02:04]** teníamos

**[1:02:06]** none, entonces

**[1:02:08]** para instutar los faltantes

**[1:02:10]** y para la otra parte utilicé

**[1:02:12]** cinco force para sobre

**[1:02:14]** los 1.040 estudiantes

**[1:02:16]** y esto quiere decir que

**[1:02:18]** todos los datos se evaluan, no

**[1:02:20]** hay ningún dato que quedó fuera

**[1:02:22]** de la evaluación

**[1:02:24]** y la métrica principal es f1

**[1:02:26]** que es reprobado, ya que

**[1:02:28]** precisión con

**[1:02:30]** pecal.

**[1:02:32]** Y la validación cruzada

**[1:02:34]** quedó completamente fuera

**[1:02:36]** de la reserva externa que es sólo

**[1:02:38]** 161 datos

**[1:02:41]** que vamos a usar para exceso

**[1:02:44]** y aquí vimos tres modelos

**[1:02:46]** ya y con balanceo

**[1:02:48]** y sin balanceo

**[1:02:50]** ya

**[1:02:52]** utilizamos, vi la regresión

**[1:02:54]** logística, ganónfoes

**[1:02:56]** y el árbol de decisión

**[1:02:58]** ya

**[1:03:00]** y el que tuvo

**[1:03:02]** mayor

**[1:03:04]** métrica como se puede decir

**[1:03:07]** o sea, fue

**[1:03:09]** regresión logística

**[1:03:11]** es importante mencionar

**[1:03:13]** que aquí ante el balanceo

**[1:03:15]** con regresión logística

**[1:03:17]** activó ahí como dice 0.622

**[1:03:19]** y pasó a 0.661

**[1:03:21]** tampoco digamos que

**[1:03:23]** tan grande la diferencia

**[1:03:25]** ya, pero

**[1:03:27]** con el balanceo a los jacals tuvo

**[1:03:29]** 0.702

**[1:03:31]** ya

**[1:03:34]** el balanceo

**[1:03:37]** no crea nuevos datos

**[1:03:39]** pero sí hace

**[1:03:41]** que se balanceen los pesos de los datos

**[1:03:43]** cuando uno hace este entrenamiento

**[1:03:45]** ya, le asigna

**[1:03:47]** a los datos que tiene

**[1:03:49]** menor cantidad de peso

**[1:03:51]** le asigna un poquito mayor peso

**[1:03:54]** sí, vamos

**[1:03:56]** y aquí yo utilice

**[1:03:58]** el hiperparámetro en C

**[1:04:00]** ya, aquí hay estas cositas

**[1:04:02]** voy a empezar explicando

**[1:04:04]** para qué utilice esto

**[1:04:06]** esto lo utilice para que

**[1:04:08]** cuando yo ingrese nuevos datos a este modelo

**[1:04:10]** ya no se me desajusta

**[1:04:12]** yo elegí una grilla de 5 C

**[1:04:14]** que son estos

**[1:04:16]** y estos números lo elegí yo

**[1:04:18]** y recuerdo que yo dije que

**[1:04:20]** habíamos elegido 5 F

**[1:04:22]** entonces, cada uno de estos C

**[1:04:24]** pasó por estos 5 F

**[1:04:26]** y esto es como

**[1:04:28]** se suma

**[1:04:30]** cada uno de estos y se divide por 5

**[1:04:32]** y este es el dato que nota

**[1:04:34]** el 0.655

**[1:04:37]** ya

**[1:04:39]** ¿sí? ¿se entiende cierto?

**[1:04:41]** sí

**[1:04:43]** entonces, ¿cuál es el edad de esto?

**[1:04:45]** esto es que el modelo

**[1:04:47]** evitar el sobreajuste del modelo

**[1:04:49]** incluso cuando reciba nuevos datos

**[1:04:51]** ya

**[1:04:55]** ahí está todo

**[1:04:57]** ¿esto todo?

**[1:05:02]** la selección de modelo final

**[1:05:04]** ya

**[1:05:06]** aquí

**[1:05:08]** seleccione

**[1:05:10]** la dirección logística

**[1:05:13]** acá, yo considero

**[1:05:15]** que me dio excelente resultado

**[1:05:17]** esto, estoy muy contenta porque

**[1:05:19]** es una corte, es un 1.300

**[1:05:21]** un dato

**[1:05:23]** y me detectó

**[1:05:25]** 7 de 10

**[1:05:27]** o sea

**[1:05:30]** me detectó 7 estudiantes

**[1:05:32]** que sí, realmente voy a probar

**[1:05:34]** y sigamos

**[1:05:38]** que me llamo un minuto

**[1:05:40]** aquí hay un poquito más de detalle

**[1:05:42]** entonces, ¿qué queríamos saber si el modelo funcionaba?

**[1:05:44]** acá, senablemente bien

**[1:05:46]** que no participaron en su desarrollo

**[1:05:48]** y estos son los resultados de

**[1:05:50]** el TES, que fue el 261

**[1:05:52]** que el modelo nunca en el entrenamiento

**[1:05:54]** los vio

**[1:05:57]** y me vio

**[1:05:59]** a ciertos totales

**[1:06:01]** o sea, ¿cuántos precifico correctamente?

**[1:06:03]** me entregó

**[1:06:05]** ¿cuántos dijo que reprobó

**[1:06:07]** y tuvo razón?

**[1:06:09]** un recal de 0.707

**[1:06:11]** ya

**[1:06:13]** que son totalmente cuántos detectó

**[1:06:15]** un equilibrio de

**[1:06:17]** 0.645

**[1:06:19]** y un rock out de 7.68

**[1:06:21]** ya

**[1:06:23]** esto, ¿qué quiere decir? ¿qué?

**[1:06:25]** acá está

**[1:06:27]** recordando que la clase de interés has reprobado

**[1:06:29]** este de 0.50

**[1:06:31]** que es normal que se utiliza

**[1:06:33]** siempre como el medio ya

**[1:06:35]** y fueron 118

**[1:06:37]** estudiantes fueron calificados

**[1:06:39]** como reprobados y 143

**[1:06:41]** como aprobados y ahora lo vamos a ver

**[1:06:43]** el matriz de confusión

**[1:06:47]** y aquí está

**[1:06:49]** y aquí nos dice

**[1:06:52]** o sea, en la variación

**[1:06:54]** del TES, de los 99 estudiantes

**[1:06:56]** que el TES

**[1:06:58]** teníamos como reprobados

**[1:07:00]** reconoció 79

**[1:07:02]** y 48

**[1:07:04]** fueron los

**[1:07:06]** los alertados

**[1:07:08]** pero que sí aprobaron

**[1:07:10]** 29 no

**[1:07:13]** me reconoció el modelo

**[1:07:15]** por eso dice que el modelo detecta aproximadamente

**[1:07:17]** 7 de cada 10 estudiantes

**[1:07:19]** y después vamos

**[1:07:21]** ah, y esto está bueno también

**[1:07:23]** ya aquí vamos un solapamiento

**[1:07:25]** y son todos estos que el modelo

**[1:07:27]** ya

**[1:07:30]** estos fueron como los que

**[1:07:32]** no debió haber

**[1:07:34]** me debía haber detectado pero no me detectó

**[1:07:36]** ya y todo esto sí

**[1:07:38]** detectó y aquí tenemos el del

**[1:07:40]** y esta línea es

**[1:07:43]** una línea que divide en dos

**[1:07:45]** y esto significa que

**[1:07:47]** tan bueno que ya puedes generalizar mi modelo

**[1:07:49]** y aquí está la variación cruzada

**[1:07:54]** en las clases de interés

**[1:07:56]** ya

**[1:07:59]** se acabó el tiempo preciera

**[1:08:01]** pero termina el ratito

**[1:08:03]** y ya, no sí, esto

**[1:08:05]** quería mostrar esto

**[1:08:07]** un poquitito

**[1:08:09]** que ahí hice una prueba en diferentes umbrales

**[1:08:11]** ya y en el 0.2

**[1:08:13]** es el mejor que me dio

**[1:08:16]** el 0.8 es como dejar como

**[1:08:18]** decir saben que mejor

**[1:08:20]** ventan todos los estudiantes

**[1:08:22]** y los dejo a todos como retrobados

**[1:08:24]** pero eso no es la idea

**[1:08:28]** y...

**[1:08:30]** y ahí sería

**[1:08:32]** ya, gracias

**[1:08:35]** una pregunta

**[1:08:37]** de acuerdo a tus métricas

**[1:08:39]** que pueden ser estas mismas de acá

**[1:08:41]** mi pregunta es

**[1:08:43]** que harías tú

**[1:08:46]** con este modelo ahora

**[1:08:48]** en la práctica

**[1:08:50]** y de acuerdo a tus métricas

**[1:08:52]** cuáles son las consecuencias

**[1:08:54]** de tomar esas decisiones

**[1:08:57]** hay aquí

**[1:08:59]** dos cosas

**[1:09:01]** una, es que lo que diría yo

**[1:09:03]** yo seguiría explorando

**[1:09:05]** porque también hice un experimento

**[1:09:07]** sin movilidad

**[1:09:09]** que eso me falta mencionar que

**[1:09:11]** estos datos tienen movilidad

**[1:09:13]** o sea, está considerando variables

**[1:09:15]** de muy, no sé si

**[1:09:17]** lo tengo ahí

**[1:09:19]** y sin movilidad

**[1:09:21]** pero como que detecto como lo mismo

**[1:09:23]** pero la diferencia es que con movilidad

**[1:09:25]** el entrenamiento

**[1:09:27]** versus el test, han tuvieron

**[1:09:29]** reintentos casi iguales

**[1:09:32]** pero qué es lo que haría yo

**[1:09:34]** yo que haría primero

**[1:09:36]** estudiaría las variables

**[1:09:38]** porque también es importante el peso

**[1:09:40]** de cada variable

**[1:09:42]** y también

**[1:09:44]** ver que estos datos

**[1:09:46]** son de una sola corte

**[1:09:48]** y eso tendría que ingresar más patos

**[1:09:50]** para ver si el modelo puede mejorar

**[1:09:52]** los patas que tiene

**[1:09:54]** indican que sí puede mejorar

**[1:09:56]** pero para mí

**[1:09:58]** pregunta ya para otro lado

**[1:10:00]** asumen que

**[1:10:02]** tú quieres usar este modelo

**[1:10:05]** ¿ya?

**[1:10:07]** ¿cómo lo usarías

**[1:10:09]** en la práctica?

**[1:10:11]** imagínate que el ricor Luis

**[1:10:13]** llega a un 95

**[1:10:15]** o da 90

**[1:10:17]** ¿cómo lo usarías en la práctica?

**[1:10:19]** ¿y

**[1:10:21]** ¿cuáles serían las consecuencias

**[1:10:23]** de usarlo de esa forma de acuerdo a tus métricas?

**[1:10:25]** ya

**[1:10:28]** acá el solapamiento

**[1:10:30]** que es súper importante porque lo pensé

**[1:10:32]** y lo conversamos

**[1:10:34]** a ver ¿cómo lo usaría?

**[1:10:36]** para mí esto es una probabilidad

**[1:10:38]** que un estudiante pueda reprobar

**[1:10:40]** entonces la idea

**[1:10:42]** esto es que del día 1

**[1:10:44]** el coordinador

**[1:10:47]** académico, el jefe carrera

**[1:10:49]** pueda tener estos datos

**[1:10:51]** y el mismo pueda definir

**[1:10:53]** porque igual estoy viendo una herramienta

**[1:10:55]** un BI donde pueda definir

**[1:10:57]** qué acción tomar con este estudiante

**[1:10:59]** y nosotros siempre tenemos los

**[1:11:01]** acompañamientos estudiantiles

**[1:11:03]** entonces podemos desde el día 1

**[1:11:05]** y no esperar las primeras 8 semanas

**[1:11:07]** que viene el primer certamen 1

**[1:11:09]** entonces ahí aparecen como las primeras alertas

**[1:11:11]** y que te dice

**[1:11:13]** este estudiante

**[1:11:15]** si no sé al datae

**[1:11:17]** a reforzar un poco

**[1:11:19]** matemática

**[1:11:21]** sincia básica

**[1:11:23]** claro pero en el fondo

**[1:11:25]** para eso lo utilizaría

**[1:11:27]** o sea como para

**[1:11:29]** apoyar al estudiante

**[1:11:31]** que el modelo mentique la probabilidad

**[1:11:33]** de que pueda reprobar esta asignatura

**[1:11:35]** claro entonces

**[1:11:37]** pero mi pregunta es imagínate que llegue

**[1:11:39]** un estudiante que el modelo le dice

**[1:11:41]** que tiene un 90% probabilidad

**[1:11:43]** de reprobar la asignatura

**[1:11:45]** y lo que

**[1:11:47]** qué decisión debería tomar a alguien

**[1:11:49]** con esto y cuál sería la implicancia

**[1:11:51]** bueno es que eso

**[1:11:54]** ya

**[1:11:56]** salía del área de mi expertise

**[1:11:58]** porque no

**[1:12:00]** ahí hay personas que

**[1:12:02]** que manejan esos temas

**[1:12:04]** o sea

**[1:12:06]** no no pero te digo

**[1:12:08]** la intención de poder ayudar

**[1:12:10]** pero ahí tenemos que ver

**[1:12:12]** totalmente diferente usted sabe

**[1:12:14]** pero yo estoy tratando

**[1:12:16]** recordar que nosotros vivíamos el ciclo

**[1:12:18]** de la ciencia de datos

**[1:12:20]** y que había una parte donde había

**[1:12:22]** visión

**[1:12:24]** y ahí los tomadores de decisiones

**[1:12:26]** tomaban decisiones

**[1:12:28]** la pregunta es cuál es la decisión que deberían

**[1:12:30]** tomar con este modelo y cuál sería la implicancia

**[1:12:32]** de acuerdo a tus métricas

**[1:12:34]** entonces déjame contar tu ejemplo

**[1:12:36]** si es que tú decís

**[1:12:38]** no sé tenía un precision de un 70%

**[1:12:40]** que era más o menos

**[1:12:42]** perdón un recall de un 70%

**[1:12:44]** aún un real de 0,050

**[1:12:46]** que es la mitad

**[1:12:48]** qué quiere decir eso en la práctica

**[1:12:50]** cuando tú se lo tengas que mostrar a alguien

**[1:12:52]** cómo se lo explicas y cómo le explicas

**[1:12:54]** cuáles son las consecuencias

**[1:12:56]** de tomar las decisiones que fallen a tomar

**[1:12:58]** es que

**[1:13:03]** yo no he ido tan allá

**[1:13:05]** porque como digo yo no es mi expertise

**[1:13:07]** y usted dio el ejemplo

**[1:13:09]** de no sé un 99%

**[1:13:11]** que los estudiantes detectan el modelo

**[1:13:13]** pero también ahí es que tenés como

**[1:13:15]** déjame dar tu ejemplo

**[1:13:17]** por eso no me voy mayor de 0,45

**[1:13:19]** pero déjame dar tu ejemplo

**[1:13:21]** porque esto es súper importante

**[1:13:23]** como es de tener y lo voy a hacer

**[1:13:25]** imagínate que yo estoy

**[1:13:27]** detectando

**[1:13:29]** comida en mal estado

**[1:13:31]** y yo tengo

**[1:13:33]** un 70% de recall

**[1:13:35]** eso quiere decir

**[1:13:38]** que yo soy capaz de captar

**[1:13:40]** un 70% de la comida que está en mal estado

**[1:13:42]** y un 30% se pasa

**[1:13:44]** ¿certo?

**[1:13:46]** y entonces cuando yo muestro esto

**[1:13:48]** frente a los productores de pescado

**[1:13:50]** por decir algo

**[1:13:52]** le voy a decir mira

**[1:13:54]** tengo este modelo

**[1:13:56]** si ustedes lo aplicaran

**[1:13:58]** podrían detectar correctamente un 70%

**[1:14:00]** de los pescados que se echan a perder

**[1:14:02]** pero van a perder un 30%

**[1:14:04]** entonces

**[1:14:06]** ustedes pueden tomar las decisiones que quieran

**[1:14:08]** pero podrían

**[1:14:10]** tener que eliminar

**[1:14:12]** un 70% de los pescados

**[1:14:14]** que aparecen como malos pero sin embargo

**[1:14:16]** el precision

**[1:14:18]** es de un 80%

**[1:14:20]** digamos

**[1:14:22]** entonces esto quiere decir que todo lo que el modelo detecta como malo

**[1:14:24]** un 80% verdad

**[1:14:26]** entonces si tú tomas el modelo y llegas y lo aplicas

**[1:14:28]** lo que va a pasar es que

**[1:14:30]** va a perder un 30%

**[1:14:32]** de pescados malos que van a pasar

**[1:14:34]** y va a perder

**[1:14:36]** un 20% de pescados buenos

**[1:14:38]** que ellos tienen que votar

**[1:14:40]** ya pero acá

**[1:14:42]** el tema es el siguiente

**[1:14:44]** bueno

**[1:14:47]** es como

**[1:14:49]** los exámenes

**[1:14:51]** cuando hablaba la compañera del cáncer

**[1:14:53]** el positivo negativo es mejor tener

**[1:14:55]** un falso positivo

**[1:14:57]** en este caso

**[1:14:59]** que realmente

**[1:15:01]** no va a aceptar

**[1:15:03]** no ver la probabilidad que el estudiante

**[1:15:06]** si pueda reprobar

**[1:15:08]** podemos

**[1:15:10]** tener las primeras 8 semanas al estudiante

**[1:15:12]** que tiene la probabilidad de reprobar

**[1:15:14]** pero realmente no va a reprobar

**[1:15:16]** pero

**[1:15:18]** yo creo que no

**[1:15:20]** va a ser tan duro

**[1:15:22]** no se si me doy entender

**[1:15:25]** osea es que

**[1:15:27]** mi mirada es reprobar

**[1:15:29]** solamente el que reproba

**[1:15:31]** esa es mi variable de interés

**[1:15:33]** los que aprobaron y son tan poco

**[1:15:35]** y el modelo

**[1:15:37]** que dice

**[1:15:39]** reprobaron

**[1:15:41]** son 8 semanas

**[1:15:43]** no es una vida entera

**[1:15:45]** no se si

**[1:15:47]** me doy entender

**[1:15:49]** pero que pasaría si tú dijera

**[1:15:53]** ya voy a tener un recall del 100%

**[1:15:55]** pero es que

**[1:15:58]** esa es una suposición

**[1:16:00]** pero que puedo moverlo acá

**[1:16:02]** voy a moverlo acá en la curva roca

**[1:16:04]** pero es que claro

**[1:16:06]** no puedo hacer lo que quiera acá y decir

**[1:16:08]** yo quiero tenerlo a todo

**[1:16:10]** pero la idea de esto es llegar

**[1:16:12]** realmente a lo cierto

**[1:16:14]** entonces por eso ni siquiera me quiero mover

**[1:16:17]** al 3.045

**[1:16:19]** y después meterle más datos

**[1:16:21]** para llegar a una precisión realmente correcta

**[1:16:23]** ya, ok

**[1:16:26]** vamos con el siguiente grupo

**[1:16:29]** que ahora si creo que es el

**[1:16:31]** el que decía cuarto

**[1:16:33]** que es Fernanda

**[1:16:35]** y Carolina

**[1:16:37]** si hola profe

**[1:16:39]** ya voy a convertir

**[1:16:45]** voy a convertir

**[1:16:49]** bueno si

**[1:17:02]** ya creo que se ve en modelos de presentación

**[1:17:04]** cierto?

**[1:17:07]** Peño dale

**[1:17:09]** entonces buenas tardas a todos

**[1:17:11]** hoy día con Carolina le vamos a presentar

**[1:17:13]** la segunda parte de nuestro proyecto

**[1:17:15]** en donde delito 1 hicimos este análisis

**[1:17:17]** clavectorio de los datos y ahora

**[1:17:19]** es como el paso clave

**[1:17:21]** a construir estos modelos predictivos

**[1:17:23]** de clasificar

**[1:17:25]** automáticamente en este caso tumores

**[1:17:27]** en donde nuestro objetivo principal no es acertar

**[1:17:29]** sino que detectar

**[1:17:31]** la mayor cantidad posible de tumores malignos

**[1:17:33]** bueno, por favor

**[1:17:35]** trabajamos con alrededor de

**[1:17:37]** 569 muestras

**[1:17:39]** donde había un 67%

**[1:17:41]** benigno y un 37%

**[1:17:43]** maligna

**[1:17:45]** 30 variales numéricas del tumor

**[1:17:47]** y por lo mismo codificamos

**[1:17:49]** benigno como ser maligno como uno

**[1:17:51]** muy simple

**[1:17:53]** vamos a ocupar en modelos matemáticos

**[1:17:55]** entonces se entiende el número y al hacer esto

**[1:17:57]** podemos calcular

**[1:17:59]** diferentes métricas como por ejemplo

**[1:18:01]** lorical que están enfocadas directamente

**[1:18:03]** en detectar lo que es la clase maligna

**[1:18:05]** y que es lo que no interesa

**[1:18:07]** Contenida por favor

**[1:18:11]** en resumen las variables más destacadas del

**[1:18:13]** lipo 1 fueron el radio, el perímetro, el área

**[1:18:15]** y lo que es con cavidad

**[1:18:17]** que nos mostraron

**[1:18:19]** diferencias claras entre

**[1:18:21]** tumores benigno y maligno

**[1:18:23]** porque en este caso modelo de clasificación

**[1:18:25]** aprenda a partir de patrones

**[1:18:27]** los datos y estas variables ya se

**[1:18:29]** separaban como naturalmente

**[1:18:31]** entre los benignos

**[1:18:33]** y los malignos

**[1:18:35]** entonces en este caso podíamos usarlas

**[1:18:37]** como base para tomar decisiones

**[1:18:39]** acertadas, son variables

**[1:18:41]** que en realidad nos dan información

**[1:18:43]** valiosa para poder diferenciar

**[1:18:45]** correctamente en este caso

**[1:18:47]** caso nuevo

**[1:18:49]** y continuamos

**[1:18:53]** separamos los datos en tres conjuntos en este caso

**[1:18:55]** primero el modelamiento en el 60%

**[1:18:57]** y el final es solamente para entender

**[1:18:59]** los datos, las correlaciones

**[1:19:01]** poder definir diferentes hiperparámetros

**[1:19:03]** que vamos a probar

**[1:19:05]** después el entrenamiento

**[1:19:07]** 20% donde aplicamos

**[1:19:09]** la variación cruzada

**[1:19:11]** y el 3 al final que queda completamente

**[1:19:13]** aislado y se usa

**[1:19:15]** la vamos a ocupar como solamente al final

**[1:19:17]** para saber si el modelo realmente aprendió

**[1:19:19]** con de más

**[1:19:22]** también ocupamos como decía la variación cruzada

**[1:19:24]** donde ocupamos el

**[1:19:26]** dividimos los datos en cinco partes

**[1:19:28]** entrenamos cuatro pero a vos con una

**[1:19:30]** después eso lo fuimos requiriendo cinco veces

**[1:19:32]** tratando de mantener como la misma

**[1:19:34]** proporción entre benigno

**[1:19:36]** y maligno y aplicamos también

**[1:19:38]** hiperparámetros según el recal

**[1:19:40]** de la clase de maligna

**[1:19:42]** porque en medicina por ejemplo

**[1:19:44]** no detectar un cáncer es mucho peor

**[1:19:46]** que una falsa alarma

**[1:19:48]** y bueno el primero modelo que

**[1:19:51]** vamos a ver es el

**[1:19:53]** super vector machine que en realidad lo que

**[1:19:55]** busca es la frontera óptima

**[1:19:57]** de separación entre benigno y maligno

**[1:19:59]** tenemos el árbol de decisión que funciona

**[1:20:01]** como con reglas jeráticas

**[1:20:03]** es como más fácil de

**[1:20:05]** interpretar y tenemos

**[1:20:07]** el random Fourier que combina mucho

**[1:20:09]** de esto al bolito y promedía sus

**[1:20:11]** predicciones y poder decir que es

**[1:20:13]** como más profundo y por qué estas tres

**[1:20:15]** porque representa como

**[1:20:17]** familias como distintas o sea

**[1:20:19]** unos geométricos, unos reglas,

**[1:20:21]** unos ensambles, entonces nos permite

**[1:20:23]** comparar y ver cuál

**[1:20:25]** funciona mejor.

**[1:20:28]** Bueno el primer modelo es

**[1:20:30]** el super vector machine

**[1:20:32]** es como un modelo

**[1:20:34]** que separa los tumores como

**[1:20:36]** buenos pelos malos

**[1:20:38]** y busca dejar como un espacio

**[1:20:40]** entre ambos grupos

**[1:20:42]** y si no se puede por ejemplo

**[1:20:44]** con una línea recta lo vamos a hacer

**[1:20:46]** con una línea curva para poder separar lo mejor

**[1:20:48]** y por lo mismo

**[1:20:50]** cuando hicimos la variación cruzada

**[1:20:52]** se detectó un 97 como

**[1:20:54]** más 78%

**[1:20:56]** tumores malignos

**[1:20:58]** es decir por ejemplo que de 100 malignos

**[1:21:00]** atrapó casi el 98

**[1:21:02]** y en el test

**[1:21:04]** detectó un 88.10%

**[1:21:06]** o sea

**[1:21:08]** bajó un poco pero

**[1:21:11]** es normal porque los datos

**[1:21:13]** así y el modelo

**[1:21:15]** nunca había visto estos datos

**[1:21:17]** entonces eso reservamos ese

**[1:21:19]** 20% que le había dicho anteriormente

**[1:21:21]** porque se podría decir que

**[1:21:23]** detecta 9

**[1:21:25]** de cada 10 tumores más lindos

**[1:21:27]** en datos nuevos

**[1:21:29]** con un 91.23%

**[1:21:31]** de aciertos totales

**[1:21:33]** ¿Continúa Carmen

**[1:21:35]** con los demás?

**[1:21:37]** El segundo modelo que utilizamos

**[1:21:39]** fue de árbol de decisión

**[1:21:41]** los

**[1:21:43]** los hiberparámetros que se utilizaron

**[1:21:45]** y con los cuales configuramos

**[1:21:47]** son los que aparecen ahí

**[1:21:49]** de los cuales bueno voy a destacar

**[1:21:51]** solo dos el criterio

**[1:21:53]** de Ginny que nos permite

**[1:21:55]** medir las impurezas

**[1:21:57]** de los nodos para generar subconjuntos

**[1:21:59]** y que estos subconjuntos

**[1:22:01]** sean lo más equitativo posible

**[1:22:03]** que no haya muchos por ejemplo

**[1:22:05]** benignos y muy poquitos malignos

**[1:22:07]** ni viceversa

**[1:22:10]** dentro de las otras de los otros hiberparámetros

**[1:22:12]** a destacar por ejemplo

**[1:22:14]** maxDip que dice igual a 5

**[1:22:16]** evita que

**[1:22:18]** con este número evita que se vuelve

**[1:22:20]** accesivamente complejo

**[1:22:22]** y se ajuste demasiado

**[1:22:24]** a los datos de entrenamiento

**[1:22:26]** acá se obtuvo un recall

**[1:22:28]** promedio de

**[1:22:30]** 90.83

**[1:22:32]** recordemos que además

**[1:22:34]** recall es una métrica que nos indica

**[1:22:36]** que también el modelo

**[1:22:38]** puede o logra detectar

**[1:22:40]** los casos que realmente pertenecen a esa clase

**[1:22:42]** en este caso lo que más nos interesa

**[1:22:44]** es

**[1:22:46]** el recall m que se encuentra

**[1:22:48]** en la parte inferior

**[1:22:50]** destacado ahí con un

**[1:22:52]** remarcador en rojo

**[1:22:54]** de todos los tumores que realmente

**[1:22:56]** eran malignos cuántos logró detectar

**[1:22:58]** ese es el fondo como la traducción

**[1:23:00]** más entendible

**[1:23:02]** ahí bueno se ve que se evaluaron

**[1:23:04]** después o que evaluamos

**[1:23:06]** estos resultados en el conjunto

**[1:23:08]** de test en donde obtuvimos

**[1:23:10]** este recall para los tumores

**[1:23:12]** malignos de un 83.33

**[1:23:14]** por ciento

**[1:23:16]** el rock a hook es de

**[1:23:18]** 89.32

**[1:23:20]** indica que el modelo sí tiene una buena

**[1:23:22]** capacidad para distinguir entre los tumores

**[1:23:24]** malignos y benignos

**[1:23:26]** pero es inferior al que anteriormente

**[1:23:28]** presentó fernanda

**[1:23:30]** y lo que se destaca ahí también

**[1:23:32]** es que con el signo como de advertencia

**[1:23:34]** existen 7 falsos negativos

**[1:23:36]** o sea 7 tumores malignos fueron

**[1:23:38]** clasificados como

**[1:23:40]** benignos

**[1:23:43]** el siguiente modelo que utilizamos

**[1:23:45]** fue random forest

**[1:23:47]** ya sabemos que es un muy grande rago

**[1:23:49]** un conjunto de árboles de decisión

**[1:23:51]** para seleccionar la configuración

**[1:23:53]** del modelo también utilizamos

**[1:23:55]** validación cruzada de 5 fold

**[1:23:57]** buscando maximizar el recall

**[1:23:59]** de la clase maligna como en el anterior

**[1:24:01]** recordemos que

**[1:24:03]** en el fondo esto de 5 fold

**[1:24:05]** pide en 4 partes para entrenar

**[1:24:07]** y una para validar y esto se repite

**[1:24:09]** 5 veces

**[1:24:11]** con esta configuración obtuvimos un

**[1:24:13]** recal promedio de 93.05

**[1:24:15]** durante la validación cruzada

**[1:24:17]** y después al evaluar esto en conjunto

**[1:24:19]** de test

**[1:24:21]** obtuvimos en el recal

**[1:24:23]** para malignos un 90.48%

**[1:24:27]** si miramos la matriz de confusión

**[1:24:29]** lo más importante es que solamente

**[1:24:31]** tenemos 4 falsos negativos

**[1:24:33]** es decir solamente 4 tumores

**[1:24:35]** que realmente eran malignos

**[1:24:37]** fueron clasificados erróneamente

**[1:24:39]** como benignos

**[1:24:41]** hasta acá el mejor desempeño

**[1:24:43]** lo presenta random forest

**[1:24:45]** acá hay una tabla comparativa

**[1:24:49]** sobre los resultados

**[1:24:51]** en el conjunto de test

**[1:24:53]** nos permite evaluar cómo se comportan estos modelos

**[1:24:55]** frente a datos que no fueron usados

**[1:24:57]** durante el entrenamiento

**[1:24:59]** y por otro lado también

**[1:25:01]** en el lado derecho se muestran las curvas rock

**[1:25:03]** en donde acá podemos presidenciar

**[1:25:05]** que la que está en verde

**[1:25:07]** hay una flecha que les apunta

**[1:25:09]** es la respectiva y la que corresponde

**[1:25:11]** a random forest

**[1:25:13]** si se fijan también

**[1:25:15]** el área bajo la curva obviamente

**[1:25:17]** es mayor para este model

**[1:25:19]** acá bueno como se le dice

**[1:25:22]** siempre el criterio clínico que tenemos

**[1:25:24]** que tener en cuenta por el tipo de caso

**[1:25:26]** que tenemos es

**[1:25:28]** minimizar falsos negativos

**[1:25:30]** o sea malignos clasificados como benignos

**[1:25:36]** comparativo aquí de las matrices de confusión

**[1:25:38]** que ya fuimos viendo en cada una de las

**[1:25:40]** diapositivas anteriores

**[1:25:42]** falsos negativos para

**[1:25:44]** el primer modelo sm5

**[1:25:46]** árbol de decisión 7 y random forest

**[1:25:48]** de 4

**[1:25:50]** la matriz de confusión

**[1:25:52]** no solamente nos permite ver cuántos casos

**[1:25:54]** clasificamos correctamente

**[1:25:56]** sino también que tipo de errores

**[1:25:58]** estamos cometiendo

**[1:26:00]** en este caso ya hemos visto

**[1:26:02]** y por las métricas anteriores

**[1:26:04]** random forest sería como el que más nos acomoda

**[1:26:06]** y como conclusión final

**[1:26:09]** vimos que se compararon

**[1:26:11]** los modelos de sm árbol de decisión

**[1:26:13]** random forest mediante

**[1:26:15]** variación cruzada

**[1:26:17]** de 5 false y selección por recall

**[1:26:19]** el modelo seleccionado fue

**[1:26:21]** random forest ya que fue el

**[1:26:23]** que tuvo un mejor

**[1:26:25]** valor en lo que era

**[1:26:27]** o mejor resultado mejor dicho

**[1:26:29]** en la prueba en el conjunto

**[1:26:31]** de test

**[1:26:33]** ofrece un mejor equilibrio entre lo

**[1:26:35]** que es discriminación en rock

**[1:26:37]** y lo que es detección de malignidad

**[1:26:39]** que lo vimos con el recall m

**[1:26:41]** y quedando como segunda alternativa

**[1:26:43]** sm

**[1:26:45]** y desde el punto de vista clínico

**[1:26:47]** el modelo final presenta 4

**[1:26:49]** falsos negativos de 42 casos

**[1:26:51]** malignos en test

**[1:26:53]** es el menor número de los 3

**[1:26:55]** aún cuando sigue presentando

**[1:26:57]** un cierto porcentaje mínimo de error

**[1:26:59]** y además obviamente

**[1:27:01]** con todo lo anteriormente visto

**[1:27:03]** podemos validar la utilidad práctica

**[1:27:05]** del aprendizaje automatizado

**[1:27:07]** en oncología

**[1:27:14]** muchas gracias

**[1:27:16]** pueden poner la matriz

**[1:27:18]** osea la tablita

**[1:27:20]** ponen el recall

**[1:27:22]** y el precision

**[1:27:24]** entonces

**[1:27:26]** voy a hacer la misma pregunta que hice en antes

**[1:27:28]** si que ustedes eligieron por ejemplo

**[1:27:30]** ahí el punto donde está

**[1:27:32]** primero, antes elegí el segundo

**[1:27:34]** vamos con

**[1:27:36]** primero calorina

**[1:27:38]** si ustedes eligen

**[1:27:40]** los valores que están en la tabla

**[1:27:42]** ya

**[1:27:44]** y en vez de elegir el random forest

**[1:27:46]** elijo el árbol de decisión

**[1:27:48]** ok

**[1:27:51]** entonces que quiere decir en la práctica

**[1:27:53]** que yo uso ese árbol de decisión

**[1:27:55]** el árbol de decisión

**[1:27:59]** con los valores que se presentan

**[1:28:01]** bueno uno que tiene

**[1:28:03]** menos precisión

**[1:28:05]** menos precisión para detectar

**[1:28:07]** los malignos o para diferenciar

**[1:28:09]** malignos bebenignos

**[1:28:11]** y también

**[1:28:13]** tiene

**[1:28:15]** menor poder discriminatorio

**[1:28:17]** entre los tipos de tumores que hay

**[1:28:19]** en el accuracy se puede ver eso

**[1:28:21]** y

**[1:28:23]** lo que más nos

**[1:28:25]** llama la atención o lo que más nos importaba

**[1:28:27]** en el fondo es el recall

**[1:28:29]** m que en este caso

**[1:28:31]** está muy por debajo del

**[1:28:33]** sdm y del random forest

**[1:28:35]** con un 83,3%

**[1:28:37]** pero no quiero

**[1:28:40]** saber del modelo imagínate que

**[1:28:42]** yo soy un médico y tú me quieres decir

**[1:28:44]** que

**[1:28:46]** cuáles son las consecuencias de usar este modelo

**[1:28:49]** hay una mayor probabilidad

**[1:28:51]** de detectar

**[1:28:53]** muchos más falsos negativos

**[1:28:55]** por ejemplo de

**[1:28:57]** que aparezca un tumor maligno

**[1:28:59]** y que no se detecte a tiempo porque

**[1:29:01]** fue clasificado como benigno

**[1:29:03]** ya

**[1:29:06]** digamos que yo te digo miras ahí que

**[1:29:08]** yo soy un médico

**[1:29:10]** un colo

**[1:29:12]** y de cada 100 pacientes

**[1:29:14]** que yo atiendo

**[1:29:16]** 20 tienen realmente cáncer

**[1:29:19]** yo pasaría si usar este modelo

**[1:29:21]** al momento de atender a estos pacientes

**[1:29:23]** de cada 100 pacientes que yo atiendo

**[1:29:25]** 20 tienen cáncer

**[1:29:33]** si ese fuera como el conjunto

**[1:29:35]** de datos para entrenar el modelo

**[1:29:37]** con árbol de decisión

**[1:29:39]** no, no, no, no es el conjunto

**[1:29:41]** de datos para entrar en el modelo

**[1:29:43]** tú me estás diciendo mirá

**[1:29:45]** está este modelo

**[1:29:47]** que funciona así con estos números

**[1:29:49]** que están acá

**[1:29:51]** y yo digo de cada 100 pacientes

**[1:29:53]** que yo generalmente veo

**[1:29:55]** y a los cuales le voy a aplicar este modelo

**[1:29:57]** 20 realmente tienen cáncer

**[1:29:59]** y yo le aplico este modelo

**[1:30:03]** que es lo que pasaría

**[1:30:05]** que deberían haber más pacientes con cáncer

**[1:30:07]** no solo 20

**[1:30:10]** no, pero yo te digo yo ya sé

**[1:30:12]** no sé porque

**[1:30:14]** mi experiencia me lo dice que llegaba a 100

**[1:30:16]** 20 efectivamente realmente tienen cáncer

**[1:30:18]** y yo le aplico este modelo

**[1:30:21]** no sé si me entiendes

**[1:30:24]** entonces la pregunta que te estoy diciendo es

**[1:30:26]** yo le aplico el modelo

**[1:30:29]** cuántas veces

**[1:30:31]** usando el árbol de decisión

**[1:30:33]** cuántos pacientes me saldrían

**[1:30:35]** que tienen cáncer y cuántos de esos son verdad

**[1:30:37]** entonces yo te estoy diciendo

**[1:30:42]** los verdaderos positivos

**[1:30:44]** y los perdón

**[1:30:46]** yo te estoy diciendo el número total de positivos

**[1:30:48]** y el número total de negativos

**[1:30:50]** y yo quiero que me transforme eso

**[1:30:52]** usando estas métricas

**[1:30:54]** a cuántos

**[1:30:56]** número de pacientes que de verdad

**[1:30:58]** van a ser positivos

**[1:31:00]** o de verdad van a ser negativos

**[1:31:07]** cuántos van a ser los verdaderos positivos

**[1:31:09]** cuántos van a ser los verdaderos negativos

**[1:31:11]** de verdad van a ser los falsos positivos

**[1:31:15]** voy a retroceder una diapositiva

**[1:31:19]** bueno

**[1:31:25]** no pero mira es mucho más fácil

**[1:31:27]** anda a la siguiente slide

**[1:31:31]** entonces imaginemos que yo uso el random forest

**[1:31:33]** y yo te digo

**[1:31:35]** yo estoy seguro que los positivos

**[1:31:37]** son 20 y los negativos

**[1:31:39]** son 80

**[1:31:41]** es el número total de positivos

**[1:31:43]** y negativos de verdad

**[1:31:45]** así que si yo le hago un examen

**[1:31:47]** me salen efectivamente

**[1:31:49]** si

**[1:31:51]** entonces tú me dices la precisión

**[1:31:53]** es de un 100%

**[1:31:55]** si

**[1:31:57]** que quiere decir que la precisión es de un 100%

**[1:32:00]** que esos 80 negativos efectivamente

**[1:32:02]** son

**[1:32:04]** tumores malignos y los 20 son efectivamente

**[1:32:06]** tumores benignos

**[1:32:10]** no

**[1:32:13]** yo le voy a aplicar el modelo

**[1:32:15]** a estos 20

**[1:32:17]** y 80

**[1:32:19]** y tú me estás diciendo

**[1:32:21]** y tú me estás diciendo la precisión

**[1:32:23]** va a ser de un 100%

**[1:32:25]** si

**[1:32:29]** si tú me dijeras

**[1:32:31]** el recall

**[1:32:33]** es de un 100%

**[1:32:35]** y la precisión es de un 100%

**[1:32:37]** entonces el recall de un 100%

**[1:32:39]** te diría que

**[1:32:41]** voy a detectar siempre esos 20

**[1:32:43]** ah claro siempre los 20

**[1:32:45]** los 20 siempre van a salir como

**[1:32:47]** tu modelo siempre te dice que

**[1:32:49]** son positivos

**[1:32:51]** con precisiones que están confiables

**[1:32:53]** es en el fondo que sean

**[1:32:55]** malignos o benignos

**[1:32:57]** si tú me dices

**[1:33:00]** que la precisión es de un 100%

**[1:33:02]** lo que me estás diciendo

**[1:33:04]** que cada vez que el modelo me diga

**[1:33:06]** que

**[1:33:08]** es positivo o sea que hay cáncer

**[1:33:10]** le voy a apuntar en un cáncer

**[1:33:12]** si

**[1:33:14]** si el recall es de un 100%

**[1:33:16]** lo que me está diciendo es que

**[1:33:18]** va a recuperar a todos

**[1:33:20]** los pacientes con cáncer

**[1:33:22]** los va a etiquetar como que tienen cáncer

**[1:33:24]** si?

**[1:33:27]** por favor escúchenme todo porque se los puede empezar

**[1:33:29]** a preguntar a todos ya

**[1:33:31]** entonces ahora que

**[1:33:33]** yo sé

**[1:33:35]** que si fuese un 100% precisión

**[1:33:37]** y un 100% recall

**[1:33:39]** entonces efectivamente

**[1:33:41]** me estás devolviendo a todos

**[1:33:43]** que pasa si el recall es de un 90%

**[1:33:48]** que es lo que está en el random forza

**[1:33:51]** que pasa si el recall es de un 90%

**[1:33:57]** si el recall

**[1:34:01]** que parece ahí es del 90,5

**[1:34:03]** que parece

**[1:34:05]** digamos 90% para que sea más fácil

**[1:34:07]** porque si le ponís 90,5 te agosta más el cálculo

**[1:34:09]** pero digamos que te da un recall de 90%

**[1:34:15]** logra detectar en un 90%

**[1:34:17]** los

**[1:34:19]** que son verdaderamente malignos

**[1:34:21]** eso y yo te estoy diciendo

**[1:34:23]** cuando son 20

**[1:34:25]** si, entonces detectaría como

**[1:34:27]** 18

**[1:34:29]** detectaría 18

**[1:34:31]** entonces eso quiere decir

**[1:34:33]** que tu modelo perdería cuántos?

**[1:34:35]** 2

**[1:34:37]** perdería 2

**[1:34:41]** y qué querría decir entonces

**[1:34:43]** que la precisión sea de un 100%

**[1:34:45]** y el recall de un 90%

**[1:34:47]** sé que yo tengo esto 80 y 20

**[1:34:49]** o sea la precisión clasifica

**[1:34:52]** bien los que están como

**[1:34:54]** malignos

**[1:34:56]** y benignos pero

**[1:34:58]** aún les falta al recall

**[1:35:00]** un

**[1:35:02]** 20%

**[1:35:04]** para que seas

**[1:35:06]** como 100% seguro de que el tumor

**[1:35:08]** es

**[1:35:10]** maligno

**[1:35:13]** y ahora

**[1:35:16]** una pregunta para

**[1:35:18]** Fernanda

**[1:35:23]** hay una flechita marcando ahí

**[1:35:29]** digamos que esa flechita esté

**[1:35:31]** una tasa de verdaderos positivos de 1

**[1:35:33]** y una tasa de falso positivos

**[1:35:35]** de 0,2

**[1:35:38]** la misma pregunta para Fernanda

**[1:35:40]** yo sé como médico

**[1:35:42]** que me llegan

**[1:35:44]** no sé, se van al mento

**[1:35:46]** 20 pacientes que son positivos

**[1:35:48]** 80 que son negativos

**[1:35:50]** qué quiere decir ese 1

**[1:35:52]** y 0,2

**[1:35:58]** es igual como que en realidad esas preguntas

**[1:36:00]** son las preguntas más importantes

**[1:36:02]** no hay ninguna pregunta más importante

**[1:36:04]** que les estoy haciendo

**[1:36:06]** de esos 20

**[1:36:08]** en realidad serían

**[1:36:10]** de esos 20 en realidad serían los que

**[1:36:12]** realmente tienen cáncer

**[1:36:15]** qué quiere decir la tasa de falso positivo

**[1:36:20]** si quieres puedo buscarlo

**[1:36:36]** cómo se calcula la tasa de falso positivo

**[1:36:44]** no sé

**[1:36:56]** el número de falso positivo

**[1:37:00]** dio por el número de positivos reales

**[1:37:02]** perdón, de negativos reales

**[1:37:04]** los falsos positivos

**[1:37:06]** los benignos que se interpretan como malignos

**[1:37:12]** entonces

**[1:37:14]** la tasa de falso positivos

**[1:37:20]** es el porcentaje

**[1:37:22]** de los negativos

**[1:37:24]** que fueron seleccionados como positivos

**[1:37:29]** entonces

**[1:37:32]** qué quiere decir que hay un 20%

**[1:37:34]** los negativos cuánto eran

**[1:37:38]** si yo te digo hay 20 y 80

**[1:37:44]** 20 con cáncer

**[1:37:46]** 80 sin cáncer

**[1:37:48]** cuánto son los negativos

**[1:38:03]** ¿tú sabes Carolina?

**[1:38:08]** si eran 20 con cáncer, 80 sin cáncer

**[1:38:10]** ¿cuánto son los negativos?

**[1:38:12]** ¿cuál es el número de negativos?

**[1:38:14]** le voy a la oportunidad

**[1:38:24]** de subir la nota a Priscila

**[1:38:26]** pero porque

**[1:38:32]** yo no la entendí la pregunta

**[1:38:34]** tengo 20

**[1:38:36]** pacientes, yo sé que el número de pacientes

**[1:38:38]** con cáncer real

**[1:38:40]** 20 y el número de pacientes

**[1:38:42]** sin cáncer

**[1:38:44]** real es 80

**[1:38:46]** ¿cuánto es el número de negativos?

**[1:38:57]** yo sé que el número de pacientes

**[1:38:59]** con cáncer

**[1:39:01]** real es 20

**[1:39:03]** el número de pacientes sin cáncer

**[1:39:05]** real es 80

**[1:39:07]** ¿cuánto es el número

**[1:39:09]** de negativos?

**[1:39:13]** el número real con cáncer

**[1:39:15]** 80

**[1:39:17]** el número real con cáncer

**[1:39:19]** real es 80

**[1:39:21]** sin cáncer real es 80

**[1:39:23]** ¿cuánto es el número de negativos?

**[1:39:26]** hay una diferencia de 60

**[1:39:28]** ¿cuánto es el número de negativos?

**[1:39:31]** ¿los falsos negativos?

**[1:39:34]** no, número de negativos

**[1:39:36]** ¿cómo los números?

**[1:39:40]** ya, ya

**[1:39:42]** voy a pasar al siguiente

**[1:39:44]** no se va a entender bien

**[1:39:46]** como que no se va a entender

**[1:39:48]** estoy diciendo

**[1:39:50]** el número de negativos

**[1:39:52]** ¿cuánto es?

**[1:39:54]** 1, 2, 3, 4, 10, 20, 30

**[1:39:56]** pero si tiene 20

**[1:39:58]** me dijo que tenía 20

**[1:40:00]** me estaba preguntando algo

**[1:40:02]** que ni yo estudiaba

**[1:40:04]** es un 20 negativo

**[1:40:06]** no te preocupes, vamos con Cristian

**[1:40:08]** por ejemplo, los estudiantes

**[1:40:10]** si volvemos los estudiantes no podrías responder

**[1:40:12]** ya, está bien, Cristian, ¿tú sabes?

**[1:40:14]** era

**[1:40:17]** la pregunta me la rubiste una vez más

**[1:40:19]** ya he estado anotando y todo

**[1:40:21]** ¿quién no está atento?

**[1:40:23]** ¿quién está atento a lo que yo estoy hablando?

**[1:40:25]** aparte es Hernández y Carolina

**[1:40:27]** que espero que sea la pregunta

**[1:40:29]** porque si no ya

**[1:40:31]** alguien sabe la respuesta a la pregunta

**[1:40:33]** pero digo 80

**[1:40:35]** ¿quién dijo eso?

**[1:40:38]** yo

**[1:40:40]** Jason

**[1:40:43]** fue Jason?

**[1:40:45]** bien, son 80

**[1:40:47]** ¿qué es lo que es un positivo?

**[1:40:49]** ¿qué es lo que es un negativo?

**[1:40:51]** el positivo

**[1:40:53]** son los pacientes con cáncer

**[1:40:55]** el negativo son los pacientes

**[1:40:57]** sin cáncer

**[1:41:02]** entonces

**[1:41:04]** la pregunta ahora de fondo

**[1:41:06]** que era la que le estaba haciendo a Fernanda

**[1:41:08]** ¿tú ya sabes cuántos son los negativos?

**[1:41:10]** ¿sierto cuántos son Fernández los negativos?

**[1:41:12]** 80

**[1:41:15]** 80

**[1:41:17]** ¿qué quiere decir

**[1:41:19]** que la pregunta de falsos positivos

**[1:41:21]** es de ser comodos

**[1:41:26]** que dos no tienen cáncer

**[1:41:29]** ¿qué con? ¿cómo?

**[1:41:31]** de esos ocheros

**[1:41:36]** o sea en ese caso si

**[1:41:38]** se equivocó en esos dos casos o no

**[1:41:40]** en dos casos

**[1:41:43]** ¿por qué en dos casos?

**[1:41:46]** Carolina ¿tú sabes?

**[1:41:50]** por ciento de los casos

**[1:41:52]** el culpa que me toma esto

**[1:41:58]** pero esto es demasiado importante

**[1:42:00]** creo que es lo más importante el curso

**[1:42:02]** entonces si no lo están entendiendo más de la mitad del curso

**[1:42:04]** estoy preocupadísimo

**[1:42:08]** se despeja de las fórmulas nuevas ¿no?

**[1:42:10]** lo voy despejar

**[1:42:12]** de las fórmulas ¿si?

**[1:42:14]** 16

**[1:42:16]** 16 por ¿qué quiere decir ese 16?

**[1:42:18]** ¿qué son esos 16?

**[1:42:21]** los falsos negativos

**[1:42:23]** ¿ya? y ¿qué quiere decir

**[1:42:26]** los falsos negativos Cristian?

**[1:42:29]** significa de que

**[1:42:31]** el modelo

**[1:42:33]** está prediciendo

**[1:42:36]** de que

**[1:42:38]** de que es negativo

**[1:42:40]** y si equivocó

**[1:42:42]** eso

**[1:42:44]** está prediciendo que

**[1:42:46]** es negativo o que es positivo

**[1:42:48]** o sea

**[1:42:51]** porque son las tasas de falsos positivos

**[1:42:54]** son falsos positivos

**[1:42:56]** si, falsos positivos

**[1:43:00]** así, acá estamos viendo las falsas

**[1:43:03]** positivos

**[1:43:05]** entonces esos 16

**[1:43:18]** predijo que era positivo

**[1:43:20]** y no era negativo

**[1:43:22]** en realidad

**[1:43:24]** eso significa falsos negativos

**[1:43:26]** entonces

**[1:43:28]** ¿qué es lo que pasa?

**[1:43:30]** para que lo vayamos

**[1:43:32]** cerrando ya porque esto es súper importante

**[1:43:34]** si tú tomas el modelo

**[1:43:36]** esa flechita

**[1:43:39]** de los 80

**[1:43:41]** que no tenían cáncer

**[1:43:43]** va a tomar 16

**[1:43:45]** y va a decir que sí tuvieron cáncer

**[1:43:48]** entonces

**[1:43:50]** si tienen el reporte

**[1:43:52]** le van a llegar 16 pacientes que el doctor valerio

**[1:43:54]** va a decir si tiene cáncer

**[1:43:58]** ¿se entienden?

**[1:44:01]** ahora Fernanda ¿qué quiere decir que la tasa

**[1:44:03]** de verdaderos positivos sea 100

**[1:44:05]** si es que el número

**[1:44:08]** de pacientes realmente con cáncer

**[1:44:10]** son 20

**[1:44:12]** y realmente sin cáncer son 80

**[1:44:14]** ¿qué quiere decir que sea 1?

**[1:44:16]** la tasa de verdaderos positivos

**[1:44:19]** es súper perdida

**[1:44:21]** ¿alguien sabe

**[1:44:25]** qué es lo que quiere decir?

**[1:44:27]** todo lo ha hecho

**[1:44:29]** a todos los modelos

**[1:44:31]** a todos los positivos

**[1:44:33]** efectivamente eran positivos

**[1:44:35]** todos los que tenían

**[1:44:37]** todos los que el modelo perijo como con cáncer

**[1:44:39]** de verdad tenían cáncer

**[1:44:41]** entonces al final el doctor

**[1:44:43]** Cristian ¿cuánto

**[1:44:45]** ¿cuánto pacientes con

**[1:44:47]** el informe con cáncer le va a dar?

**[1:44:49]** ahí les será los mismos 20

**[1:44:53]** no porque

**[1:44:55]** son acuerdas de que tenían los falsos positivos también

**[1:44:57]** ah este es el punto de la flecha

**[1:45:01]** era 0,9 entonces

**[1:45:03]** 18

**[1:45:06]** no 36

**[1:45:08]** 36

**[1:45:11]** entonces de los 100 pacientes

**[1:45:13]** 36 el modelo le va a decir que tiene cáncer

**[1:45:15]** aun cuando en realidad sólo 20

**[1:45:18]** tiene cáncer ¿entienden?

**[1:45:23]** si

**[1:45:26]** le sumó los 16 a los 20

**[1:45:28]** es más fácil verlo en una matriz

**[1:45:30]** no porque la matriz de confusión

**[1:45:33]** sólo tiene los datos de tu conjunto de test

**[1:45:35]** no tiene los datos de la realidad

**[1:45:39]** ya ok

**[1:45:42]** estamos

**[1:45:45]** gracias vamos con

**[1:45:47]** el siguiente grupo y prepárense para la

**[1:45:49]** misma pregunta

**[1:45:51]** a menos que sea regresión

**[1:45:53]** pero le voy a hacer otra pregunta

**[1:45:55]** parecía regresión

**[1:45:57]** ¿por qué hice la animotecnia?

**[1:46:03]** la segunda palabra dice el predicho

**[1:46:09]** ah está explicando ya

**[1:46:11]** alguien más tiene

**[1:46:13]** tiene

**[1:46:15]** tiene ganas de presentar ahora

**[1:46:17]** o el hijo yo

**[1:46:21]** creo que nadie está con ganas

**[1:46:23]** después de esto

**[1:46:25]** creo que

**[1:46:27]** me siento con cáncer en este momento

**[1:46:31]** por Dios

**[1:46:33]** te voy a impunar por ese tipo de declaraciones

**[1:46:37]** vamos con el grupo 5

**[1:46:39]** que son

**[1:46:41]** Caden

**[1:46:43]** Cristóbal

**[1:46:45]** y Camilo

**[1:46:48]** ¿lo vas a faltar ahí?

**[1:46:51]** no

**[1:46:57]** lo que dije no, el resto así como en general

**[1:46:59]** alguien estaba pendiente

**[1:47:01]** por lo que empezaba a preguntarme

**[1:47:04]** pero de qué estamos hablando

**[1:47:06]** es que la sigla

**[1:47:08]** y los números

**[1:47:10]** es diferente que lo conversemos

**[1:47:12]** hay que estemos con un papel

**[1:47:14]** creo que falta prácticas

**[1:47:16]** sí, también puede ser

**[1:47:18]** pero

**[1:47:20]** es súper importante

**[1:47:22]** interpretar los números

**[1:47:24]** no se trata solamente de tener el número

**[1:47:26]** decir un 90%

**[1:47:28]** es súper importante entender

**[1:47:30]** qué quiere decir en la práctica ese número

**[1:47:33]** es lo que pasa

**[1:47:35]** es igual profesores que

**[1:47:37]** con este tipo de

**[1:47:39]** nosotros tenemos el mismo caso

**[1:47:41]** como un grupo que estudiamos lo mismo

**[1:47:43]** y a mí al menos lo personal

**[1:47:45]** cuando se asocia los tumores malignos con positivos

**[1:47:47]** y los benignos con negativos

**[1:47:49]** y además se genera todas

**[1:47:51]** las preguntas no se uno ya atiende

**[1:47:53]** confundirse

**[1:47:55]** me ha gustado entender eso de los falsos positivos

**[1:47:57]** de manera tan intuitiva o fácil

**[1:47:59]** requiere un poco de práctica

**[1:48:01]** entonces se le pregunta a gente que no ha visto el tema

**[1:48:03]** y quizás se le haga más complejo

**[1:48:05]** pero es un tema

**[1:48:07]** pero por esta confusión

**[1:48:09]** de

**[1:48:11]** cómo se denomina el más positivo

**[1:48:13]** maligno, negativo, benigno

**[1:48:16]** era lo mismo, yo podría hacer exactamente

**[1:48:18]** el mismo argumento dando vuelta

**[1:48:20]** maligno y benigno

**[1:48:22]** podría decir que los benignos son negativos

**[1:48:24]** y los malignos son positivos

**[1:48:26]** y puedo tener la misma discusión

**[1:48:28]** exactamente la misma discusión

**[1:48:30]** hay que ser consultores

**[1:48:34]** ya vamos a ver cómo nos parecen

**[1:48:37]** con las predicciones

**[1:48:39]** con las predicciones de

**[1:48:41]** propiedad ya

**[1:48:43]** cuando quieran

**[1:48:47]** y se ve

**[1:48:49]** bueno

**[1:48:51]** vamos a ver

**[1:48:54]** el problema de las predicciones de

**[1:48:56]** Melbourne 2016-2017

**[1:48:58]** usamos los datos para el entrenamiento

**[1:49:00]** del año 2016

**[1:49:02]** y para probarlo con el tercio del año 2017

**[1:49:06]** bueno

**[1:49:10]** el problema

**[1:49:12]** nosotros tuvimos

**[1:49:14]** el modelo entrenado sólo

**[1:49:16]** de las transacciones del año 2016

**[1:49:18]** estimar los precios del 2017

**[1:49:20]** entonces hicimos dos hipótesis

**[1:49:22]** una hipótesis primera

**[1:49:24]** que finalmente concluimos que no

**[1:49:26]** que las relaciones observadas entre las características

**[1:49:28]** las propiedades y sus precios del 2016

**[1:49:30]** no se mantienen suficientemente

**[1:49:32]** el año 2017

**[1:49:34]** por esa razón el 2016

**[1:49:36]** no permite predecir los precios del 2017

**[1:49:38]** de una manera solamente

**[1:49:40]** con una estimación básica

**[1:49:42]** y le puedo decir uno

**[1:49:44]** que precisamente se nos dio correcta

**[1:49:46]** que las características de propiedad observada del año 2016

**[1:49:48]** como cantidad de habitaciones

**[1:49:50]** tipo de propiedad y la ubicación

**[1:49:52]** mantienen una relación suficiente

**[1:49:54]** estable respecto al precio del año 2017

**[1:49:56]** por lo que es posible

**[1:49:58]** dar esos datos del 2016

**[1:50:00]** para predecir los mejores precios del 2017

**[1:50:02]** ya primero hicimos

**[1:50:04]** el análisis exploratorio

**[1:50:06]** después entrenamos

**[1:50:08]** el modelo con los datos del año 2016

**[1:50:10]** y finalmente ocupamos como

**[1:50:12]** los datos del 2017

**[1:50:15]** en total de la base data

**[1:50:17]** eran 13.000 observaciones

**[1:50:19]** 21 atributos en columna

**[1:50:21]** y vimos los requerimientos

**[1:50:23]** de predecir los precios de la vivienda

**[1:50:25]** la recolección de la data

**[1:50:27]** tuvimos que también hacer limpieza la data

**[1:50:29]** porque había información que estaba nula

**[1:50:31]** nos estaba completada

**[1:50:33]** y

**[1:50:35]** nos fuimos dando cuenta

**[1:50:37]** del precio que era nuestro target

**[1:50:39]** dimensiones físicas que eran importante

**[1:50:41]** en el modelo como la habitación

**[1:50:43]** en los baños

**[1:50:45]** y también el tema de las ubicaciones

**[1:50:47]** eso afectaba bastante al precio

**[1:50:49]** y lo que nos percatamos también

**[1:50:51]** es que habían precios muy disparados

**[1:50:53]** entonces esos precios disparados también

**[1:50:55]** podían ensuciar un poco

**[1:50:57]** el modelo

**[1:50:59]** y acá básicamente

**[1:51:01]** el building area

**[1:51:03]** year build y console area

**[1:51:05]** eran las columnas

**[1:51:07]** que tenían

**[1:51:09]** mayor cantidad de información

**[1:51:11]** nula

**[1:51:13]** entonces también fuimos sacándose

**[1:51:15]** y retiramos esa información

**[1:51:17]** antes de empezar a utilizar

**[1:51:19]** el análisis para los modelos

**[1:51:22]** y acá un poco

**[1:51:24]** no sé si nos puede completar acá esta parte

**[1:51:26]** si bueno y para continuar

**[1:51:28]** un poco lo que menciona Camilo

**[1:51:30]** nosotros que esto también lo hablamos

**[1:51:32]** la última presentación que tuvimos

**[1:51:34]** dentro del análisis exploratorio

**[1:51:36]** lo que rescatábamos para recordar

**[1:51:38]** y la presentación de este modelo

**[1:51:40]** es que

**[1:51:42]** nosotros vemos

**[1:51:44]** una clara

**[1:51:46]** relación de la importancia que tiene

**[1:51:48]** el número de habitaciones

**[1:51:50]** dentro de la influencia que puede tener en el precio

**[1:51:52]** como ven si vemos

**[1:51:54]** a medida de que

**[1:51:56]** aumentan el número de habitaciones

**[1:51:58]** la mayoría de los datos hay un incremento

**[1:52:00]** en los precios exceptuando

**[1:52:02]** algunas casos bordes

**[1:52:04]** que observamos

**[1:52:06]** que no cumple

**[1:52:08]** con esta condición sin embargo la mayoría

**[1:52:10]** sí lo boom

**[1:52:12]** el otro punto era el tipo de vivienda

**[1:52:14]** también claramente las casas

**[1:52:16]** son mucho más costosas que el

**[1:52:18]** casas pariadas y los duplex

**[1:52:20]** y como parte de este análisis

**[1:52:22]** también vimos

**[1:52:24]** cuáles eran las correlaciones de los precios

**[1:52:26]** y bueno acá claramente identificamos

**[1:52:28]** que hay una correlación

**[1:52:30]** positiva en lo que son

**[1:52:32]** las habitaciones

**[1:52:34]** y los baños

**[1:52:36]** como parte explicando

**[1:52:38]** lo que mencionó Camilo

**[1:52:40]** como parte de las variables espaciales

**[1:52:42]** que influye

**[1:52:44]** en el comportamiento del precio

**[1:52:46]** entonces finalmente

**[1:52:48]** para concluir las habitaciones

**[1:52:50]** sí aportan

**[1:52:52]** digamos

**[1:52:54]** aportan al precio el tipo de vivienda

**[1:52:56]** y bueno existen

**[1:52:58]** también

**[1:53:00]** la distancia por ejemplo

**[1:53:02]** tiene menor impacto

**[1:53:04]** sin embargo después

**[1:53:06]** cuando trabajamos

**[1:53:08]** en el modelo

**[1:53:10]** nos dimos cuenta de que si recoge

**[1:53:12]** información relevante

**[1:53:14]** pasando a la siguiente

**[1:53:16]** nosotros antes de modelar

**[1:53:18]** lo que hicimos fue separar

**[1:53:20]** las bases

**[1:53:22]** básicamente separamos todo lo que era

**[1:53:24]** 2016

**[1:53:26]** esta era la base que íbamos a utilizar

**[1:53:28]** para el entrenamiento

**[1:53:30]** después todo lo que es 2017

**[1:53:32]** íbamos a usar

**[1:53:34]** esa base para comenzar a hacer el testeo

**[1:53:36]** y aquí nos dimos cuenta

**[1:53:38]** de esta diferencia

**[1:53:40]** que habían 172 barrios nuevos

**[1:53:42]** dentro de la data del 2017

**[1:53:44]** que nos estaba en el 2016

**[1:53:46]** bueno como mencionó Camilo

**[1:53:49]** aquí también hicimos una limpieza

**[1:53:51]** de datos, eliminamos los datos

**[1:53:53]** que habían datos nulos

**[1:53:55]** y que tampoco tenía mayor relevancia

**[1:53:57]** dentro del modelo

**[1:53:59]** el área de construcción

**[1:54:01]** el año de construcción

**[1:54:03]** acá comenzamos a

**[1:54:05]** también a hacer

**[1:54:07]** recodificación del tipo de propiedad

**[1:54:09]** y el método de venta

**[1:54:11]** para que sea un poco más uniforme

**[1:54:13]** y más entendible

**[1:54:15]** también convertimos fechas para poder aislar

**[1:54:17]** cuáles eran los años 2016-2017

**[1:54:19]** y bueno también

**[1:54:21]** dentro del modelo

**[1:54:25]** revisamos

**[1:54:27]** la conexión temprana de barrios

**[1:54:29]** de 2017

**[1:54:31]** que no estaban dentro del 2016

**[1:54:33]** lo cual podría

**[1:54:35]** ser algún riesgo

**[1:54:37]** en el modelo

**[1:54:39]** para la generalización geográfica

**[1:54:46]** y acá bueno, Camilo

**[1:54:48]** perdón Cristóbal, no sé si quieres

**[1:54:50]** comentar algo acá

**[1:54:54]** Sí, por supuesto

**[1:54:56]** en este caso

**[1:54:58]** en el slide nosotros lo que

**[1:55:00]** determinamos fueron los modelos principales

**[1:55:02]** que decidimos revisar

**[1:55:04]** que fue el modelo random forest

**[1:55:06]** y gradient boosting

**[1:55:08]** al principio nos costó mucho

**[1:55:10]** determinar cuál elegir

**[1:55:12]** pero nos quedamos con el modelo

**[1:55:14]** gradient boosting

**[1:55:16]** utilizando la validación cruzada

**[1:55:18]** el objetivo no era simplemente

**[1:55:20]** encontrar un modelo más complejo

**[1:55:22]** que otro sino comprobar

**[1:55:24]** cuál reducía mejor el error

**[1:55:26]** y conseguía un mejor resultado

**[1:55:28]** según error

**[1:55:31]** la operación random forest

**[1:55:33]** y gradient boost fueron los modelos

**[1:55:35]** más competitivos por eso los destacamos

**[1:55:37]** a pesar de que fueron 5

**[1:55:39]** los modelos

**[1:55:41]** o ahí están indicados los modelos

**[1:55:43]** evaluados

**[1:55:45]** 5 los modelos utilizados

**[1:55:47]** por favor continuar con la siguiente

**[1:55:49]** finalmente

**[1:55:53]** gradient boosting obtuvo

**[1:55:55]** el mejor desempeño

**[1:55:57]** en los datos de 2017

**[1:55:59]** alcanzó un aproximado de 072

**[1:56:01]** y un más de cercano a 210.000 dólares

**[1:56:03]** australiano

**[1:56:05]** frente al baseline

**[1:56:07]** cuyo más de cercano era de 432.000

**[1:56:09]** logramos reducir el error

**[1:56:11]** absoluto

**[1:56:13]** medio aproximado de 51.3%

**[1:56:15]** el resultado nos indica

**[1:56:17]** que existe una señal

**[1:56:19]** aprendible en los datos de 2016

**[1:56:21]** que logra generalizar

**[1:56:23]** razonablemente hacia 2017

**[1:56:25]** aquí cabe señalar

**[1:56:28]** que en todo el ejercicio intentamos

**[1:56:30]** también interpretar dentro de la

**[1:56:32]** limpieza de los datos

**[1:56:34]** si era factible o no completar

**[1:56:36]** otros antecedentes por ejemplo

**[1:56:38]** a través del postcode

**[1:56:40]** a través de la latitud

**[1:56:42]** la longitud pero veíamos que finalmente

**[1:56:44]** en este proceso de limpieza no era mucho

**[1:56:46]** el valor que sumábamos en el proceso

**[1:56:48]** sino que

**[1:56:50]** aunque uno pensara por lógica

**[1:56:52]** que la periferia o otros lugares

**[1:56:54]** de las zonas centrales

**[1:56:56]** o metropolitanas de la ciudad

**[1:56:58]** una diferencia importante en cuanto a

**[1:57:00]** precio no pudimos determinar lo que

**[1:57:02]** completando estos datos si realmente

**[1:57:04]** vamos a llegar a un indicador diferente

**[1:57:06]** el siguiente paso

**[1:57:08]** nosotros pensamos que sería analizar

**[1:57:10]** dónde este modelo finalmente

**[1:57:12]** se equivoca

**[1:57:14]** y por qué se equivoca y cómo afectan los cambios

**[1:57:16]** en la aparición de nuevos barrios

**[1:57:18]** ahí identificamos que en 2017 también

**[1:57:20]** encontramos nuevas comillas

**[1:57:22]** o así nosotros las mencionamos

**[1:57:24]** y estudiantes antecedentes también

**[1:57:26]** pensamos que iban a ser relevantes pero no era

**[1:57:28]** un dato compartido con el año 2016

**[1:57:30]** entonces no pudimos tampoco

**[1:57:32]** determinarlo

**[1:57:34]** eso para finalizar

**[1:57:38]** gracias

**[1:57:40]** ok

**[1:57:45]** Kevin

**[1:57:47]** voy a hacer la misma pregunta que hice

**[1:57:50]** antes

**[1:57:52]** ¿Qué quiere decir mirando esto en número?

**[1:57:55]** ¿Qué quiere decir en la práctica

**[1:57:57]** si tú pusieras este modelo

**[1:57:59]** en producción, si tú lo usaras

**[1:58:01]** ¿Qué quiere decir?

**[1:58:03]** Claro

**[1:58:05]** este modelo quería decir

**[1:58:07]** que por ejemplo

**[1:58:09]** si vemos el re-quadrado

**[1:58:11]** si usamos este modelo significa que

**[1:58:13]** el modelo puede predecir

**[1:58:15]** el 72% de

**[1:58:17]** los datos

**[1:58:19]** con el que nosotros trabajamos en 2016

**[1:58:21]** podría predecir los precios en 2017

**[1:58:26]** lo mismo pasa con

**[1:58:28]** el

**[1:58:30]** error medio absoluto

**[1:58:32]** que también

**[1:58:34]** nosotros vemos que

**[1:58:36]** y si quieres este pasas Camilo por favor

**[1:58:38]** a la

**[1:58:40]** a la línea anterior

**[1:58:42]** aquí nosotros vemos un comportamiento

**[1:58:44]** cuando hacemos la comparación de los modelos

**[1:58:46]** donde el error va reduciéndose

**[1:58:48]** dependiendo

**[1:58:50]** de este modelo y por ende

**[1:58:52]** va a explicar de mejor forma

**[1:58:54]** o va a mitigar

**[1:58:56]** el riesgo de

**[1:58:58]** predicción de algún precio

**[1:59:00]** lo cual pues

**[1:59:02]** significaría un riesgo

**[1:59:04]** para...

**[1:59:06]** quiero ponerlo en la práctica

**[1:59:08]** entonces imagínate

**[1:59:10]** que yo digo

**[1:59:12]** voy a predecir

**[1:59:14]** el valor de esta propiedad

**[1:59:16]** y para eso voy a usar

**[1:59:18]** el modelo que ustedes están proponiendo

**[1:59:21]** y yo voy a ir

**[1:59:23]** y voy a decir esta propiedad

**[1:59:25]** va a valer

**[1:59:27]** el próximo año tanto

**[1:59:29]** y entonces yo voy

**[1:59:31]** y digo a usted

**[1:59:33]** según el modelo a usted

**[1:59:35]** va a valer tanto

**[1:59:37]** entonces yo voy y la compro

**[1:59:39]** que quiere decir

**[1:59:41]** para efectos míos

**[1:59:44]** el haber usado su modelo

**[1:59:46]** cual la reconoce para mi

**[1:59:48]** por haber usado su modelo

**[1:59:50]** podría sobrevalorar

**[1:59:52]** o subvalorar en una propiedad

**[1:59:54]** y tomar decisiones

**[1:59:56]** de comprar o tomar

**[1:59:58]** o solicitar en un financiamiento

**[2:00:00]** menos precisa

**[2:00:02]** ¿Cuánto? ¿Cuánto puedo ganar

**[2:00:04]** o perder o qué me puede pasar?

**[2:00:06]** Complementando lo que dice Guyden

**[2:00:08]** podría potencialmente

**[2:00:10]** tener un ahorro de un 51,3%

**[2:00:12]** de lo que

**[2:00:14]** de lo que podría haber sido que no lo hago

**[2:00:16]** es no hubiese hecho esa prediction

**[2:00:18]** pero es solo un ahorro

**[2:00:22]** o puede ser que hay una pérdida

**[2:00:25]** o una pérdida

**[2:00:27]** porque está en el 51%

**[2:00:29]** por eso usamos ese indicador

**[2:00:33]** el del primer

**[2:00:35]** eso es lo que yo necesito que usted haga

**[2:00:37]** entonces en la práctica

**[2:00:39]** en la práctica yo podría

**[2:00:41]** ganar o perder

**[2:00:43]** ahora el problema del más

**[2:00:45]** es que te promedia

**[2:00:47]** dar lo mismo si es para arriba o abajo

**[2:00:49]** hay alguna forma

**[2:00:51]** que tenga de saber si es que le voy a apuntar

**[2:00:53]** o si se va a ir para arriba o abajo

**[2:00:55]** mencionaba

**[2:00:57]** de lo que estuvimos analizando

**[2:00:59]** hablaba sobre que

**[2:01:01]** podría escogerse una segmentación

**[2:01:03]** del modelo de las casas

**[2:01:05]** de lujo que le llaman

**[2:01:07]** hacer una categoría de lujo

**[2:01:09]** y en esa categoría de lujo hacer una segmentación

**[2:01:11]** separada de ese mundo

**[2:01:13]** para apuntarle mejor

**[2:01:15]** a ese parámetro

**[2:01:17]** porque si uno efectivamente como da lo mismo

**[2:01:19]** si es negativo o positivo

**[2:01:21]** va a dar un brazo

**[2:01:23]** es un poco lo que investigamos de esa parte

**[2:01:26]** Cristóbal tengo una pregunta para ti

**[2:01:28]** pueden ir a

**[2:01:30]** donde muestre

**[2:01:32]** a este gráfico

**[2:01:34]** Cristóbal

**[2:01:36]** ¿cuál es la diferencia entre el azul y el naranjo?

**[2:01:38]** la cantidad en dinero

**[2:01:45]** miles de dinero

**[2:01:47]** cuanto al modelo de

**[2:01:49]** de regresión

**[2:01:51]** te digo hay una barrita azul y una barrita naranja

**[2:01:53]** ¿cuál es la diferencia

**[2:01:55]** entre la barrita azul y la barrita naranja?

**[2:01:57]** ¿qué dice la barrita azul y qué dice la barrita naranja?

**[2:02:01]** indica

**[2:02:03]** bueno

**[2:02:08]** el error de la predicción

**[2:02:10]** es lo que está indicando

**[2:02:13]** pero cuál es la diferencia por ejemplo

**[2:02:15]** yo estoy esperando que me digas

**[2:02:17]** la barrita azul es esto

**[2:02:19]** y la barrita naranja es esto

**[2:02:24]** el maya azul indica

**[2:02:26]** que se entrena con los datos

**[2:02:28]** del 2016

**[2:02:30]** y el otro indica que se entrena con los datos

**[2:02:32]** del 2017

**[2:02:35]** ¿qué hay dentro de estas de acuerdo?

**[2:02:37]** si, estoy de acuerdo

**[2:02:39]** ¿a mí y el otro estás de acuerdo?

**[2:02:43]** complementaría un poquito

**[2:02:45]** la

**[2:02:47]** no se me meto la

**[2:02:50]** la respuesta porque

**[2:02:52]** el maya normal

**[2:02:54]** el error absoluto medio

**[2:02:56]** es como

**[2:02:58]** como nos dice aquí

**[2:03:00]** de una distancia promedio

**[2:03:02]** en que se equivocan las predicciones

**[2:03:04]** sin importar si me paseo o me quede corto

**[2:03:06]** en cambio el maya se ve

**[2:03:08]** con la variación cruzada

**[2:03:10]** exactamente ese mismo error

**[2:03:12]** absoluto medio del maya

**[2:03:14]** pero calculo la variación cruzada

**[2:03:16]** y en este caso nosotros ocupamos

**[2:03:18]** como parte de esto el key fold

**[2:03:20]** le dimos un número

**[2:03:24]** pensando también que el modelo

**[2:03:27]** hay cosas o información

**[2:03:29]** que nunca antes había visto

**[2:03:31]** lo que comentábamos de estos barrios

**[2:03:33]** hay barrios que no estaban el año anterior

**[2:03:35]** que eran más de 170

**[2:03:37]** entonces un poco

**[2:03:39]** 174

**[2:03:41]** estoy de acuerdo con tu

**[2:03:43]** interpretación del azul

**[2:03:45]** pero no me quedo claro lo que dijiste el naranjo

**[2:03:47]** ¿qué es el naranjo?

**[2:03:50]** del naranjo por ejemplo si lo conecto

**[2:03:52]** con lo que vimos en lo que vimos en clase

**[2:03:54]** saca la diferencia

**[2:03:56]** de los valores absolutos

**[2:03:58]** represento una

**[2:04:00]** directamente cuando se alija

**[2:04:02]** esa observación del centro

**[2:04:04]** que podría ser considerada

**[2:04:06]** un poco más intuitiva

**[2:04:08]** y robusta frente

**[2:04:10]** al outlier que le llaman

**[2:04:12]** estos valores atípicos

**[2:04:14]** ya que no penaliza de una forma exagerada

**[2:04:16]** estos valores atípicos

**[2:04:20]** pero adicionalmente profesores

**[2:04:22]** que finalmente el naranjo se contrasta

**[2:04:24]** contra los datos del 2016

**[2:04:26]** como que volvemos a comparar

**[2:04:28]** finalmente lo que no

**[2:04:30]** utilizó para enfrentar este modelo

**[2:04:32]** ¿lo pueden ir más atrás?

**[2:04:34]** ¿qué es lo que están diciendo acá?

**[2:04:39]** el proceso es como el flujo

**[2:04:47]** nosotros tomamos los datos

**[2:04:49]** hicimos el proceso de limpieza

**[2:04:51]** el tema de las variables

**[2:04:53]** también como que

**[2:04:55]** reinterpretamos valores de variables

**[2:04:57]** ordenamos definimos también

**[2:04:59]** los datos que no eran numéricos

**[2:05:01]** y seleccionamos solamente los valores de un médico

**[2:05:03]** para lograr la regresión

**[2:05:05]** fuimos también haciendo ese proceso de filtro

**[2:05:07]** claro pero quizás ahora

**[2:05:09]** complementando por la pregunta

**[2:05:11]** se ocupó

**[2:05:13]** se segmentaron los años

**[2:05:15]** entonces de acuerdo al año 2016

**[2:05:17]** se utilizó como conjunto de entrenamiento

**[2:05:19]** y el año 2017

**[2:05:21]** se utilizó como conjunto de des

**[2:05:23]** y de esa forma

**[2:05:25]** y de esa forma y fuimos llegando

**[2:05:27]** a esas conclusiones teniendo presente además

**[2:05:29]** que

**[2:05:31]** aparecieron datos nuevos como estos 170 barrios

**[2:05:33]** que el día mañana

**[2:05:35]** vamos a hacer el siguiente slide

**[2:05:37]** y quizás profesor para complementar

**[2:05:39]** en eso que menciona

**[2:05:41]** parte de todo eso que nosotros

**[2:05:43]** utilizamos dentro

**[2:05:45]** dentro del entrenamiento

**[2:05:47]** o sea dentro de la prueba

**[2:05:49]** la validación cruzada era ver

**[2:05:51]** como se comportaba con los mismos datos del 2016

**[2:05:53]** por eso es que mencionaba

**[2:05:55]** antes de que la barrita azul

**[2:05:57]** significa es

**[2:05:59]** cuál es el resultado

**[2:06:01]** de ese modelo con la misma data

**[2:06:03]** del 2016

**[2:06:06]** ya, de antes

**[2:06:08]** listo al dijo

**[2:06:10]** entrenamos con datos del 2017

**[2:06:12]** no, ahí fue

**[2:06:15]** quizás se confundió

**[2:06:17]** no se entrenó con datos del 2017

**[2:06:19]** se utilizó como conjunto de test

**[2:06:21]** correcto, entonces vamos de vuelta

**[2:06:23]** al siguiente gráfico

**[2:06:25]** a la siguiente gráfica

**[2:06:27]** ah, perdón

**[2:06:29]** entonces ahora yo les pregunto

**[2:06:31]** de nuevo

**[2:06:34]** cómo interpretan la barrita laranja

**[2:06:36]** versus la barrita azul

**[2:06:39]** ¿por qué no se comporta

**[2:06:41]** la variación cruzada?

**[2:06:45]** porque uno hace la variación cruzada

**[2:06:47]** ¿por qué uno hace la variación cruzada?

**[2:06:49]** O sea uno hace la variación cruzada

**[2:06:52]** para

**[2:06:54]** finalmente

**[2:06:56]** para ver cómo se comporta

**[2:06:58]** tu modelo de entrenamiento

**[2:07:00]** si

**[2:07:04]** pero

**[2:07:06]** por qué uno todo se usa un conjunto de test

**[2:07:08]** si ya puedes saber

**[2:07:10]** cómo se comporta un conjunto de test

**[2:07:12]** diferentes. Claro, y es para estimar, para estimar finalmente para obtener un

**[2:07:17]** porcentaje. Si no contaminaríamos la nuestra evaluación final. Claro, lo que

**[2:07:22]** pasa es que parte de los datos del 2017 son datos que no estaban, que no fueron

**[2:07:26]** conocidos, no estaban, no eran datos conocidos del 2016. Entonces datos no

**[2:07:31]** van con el modelo. Y ahora miren la barrita azul y la barrita naranja de

**[2:07:35]** cada uno de estos. En particular del que ustedes eligieron que creo que

**[2:07:38]** fue el random forestal. ¿Qué les dice la barrita azul y la barrita naranja

**[2:07:44]** del reading boosting? ¿Por qué la barrita naranja un poco más grande? Porque tengo

**[2:07:57]** datos, por el gap de datos que tengo del modelo. Tengo más data que lo que tengo en

**[2:08:06]** el modelo del 2016 de los datos con los que se entrenó. Nos dice también que el

**[2:08:15]** error subió finalmente. O sea, cómo se comportó nuestro modelo en esa

**[2:08:20]** diferencia de los precios que teníamos. Pero también hubo un aumento de 216.000

**[2:08:28]** dólares. Eso es como australiano. Ya, no, yo les voy a decir lo que pasa. En el

**[2:08:39]** azul, ustedes entrenaron su modelo, hicieron la evaluación cruzada,

**[2:08:44]** ¿cierto? Y al momento de hacer la evaluación cruzada podrían haber elegido

**[2:08:49]** hiperparámetro. Entonces ustedes validaron con un subconjunto de

**[2:08:54]** datos, pero también tomaron decisiones con ese subconjunto de datos. Y después,

**[2:08:58]** cuando pasaron el 2017, ese modelo funciona un poco peor. Y es normal que

**[2:09:03]** funciona un poco peor porque los datos cambian un poco entre el 2016 y el

**[2:09:09]** 2017. Entonces el modelo está un poquito sobreajustado a los datos del

**[2:09:16]** 2016 y le cuesta un poco más predecir solo los datos del 2017, porque no lo

**[2:09:21]** ha visto antes. Ok. Ya, vamos con los siguientes. El grupo número uno, que son

**[2:09:34]** Daniel Fernanda y Jason. Hola, vamos a presentar ahora.

**[2:09:48]** Un segundito. ¿Me escucho? Sí. Ahí, ¿esto se ve la presentación? Se ve. Ya,

**[2:10:13]** super. Entonces vamos a comenzar. Buenas tardes, profesores y compañeros. Le vamos a

**[2:10:17]** presentar la segunda parte de nuestro proyecto. Bueno, nosotros con la

**[2:10:21]** retroalimentación igual hicimos hartos cambios desde el primerito ahora. Así

**[2:10:25]** que volvamos a definir una base como puntos claves más que nada para poder

**[2:10:29]** entender mejor el análisis. Nosotros conseguimos o obtuvimos el set de

**[2:10:35]** datos desde la ODPA, que es la Oficina de Estudios y Políticas

**[2:10:38]** Agrarias, que se encarga de entregar datos sobre los precios,

**[2:10:41]** producción y comercio del sector silva europecuario. Y también tomamos como

**[2:10:45]** referencia la canasta básica de alimentos, que la determina el Ministerio de

**[2:10:49]** Desarrollo Social y que refleja los hábitos de consumo de los hogares del

**[2:10:52]** país y que sirve para medir la línea de la pobreza. Acá la canasta básica de

**[2:10:57]** alimentos, la CBA calcula la cantidad de cada producto en base a la porte

**[2:11:02]** calórico, considerando que son 2000 calorías diarias por persona. Nosotros

**[2:11:06]** con esto definimos una canasta base, que es la que vamos a utilizar para

**[2:11:09]** este proyecto, con 24 productos que coinciden tanto en la ODPA como en la CBA

**[2:11:14]** y utilizamos igual el mismo criterio calórico. Que es lo que vamos a analizar,

**[2:11:19]** vamos a buscar predecir el precio promedio mensual futuro de la canasta

**[2:11:23]** base, que nosotros construimos a partir de los criterios de la CBA y los

**[2:11:27]** datos disponibles en la ODPA, utilizando el comportamiento histórico para

**[2:11:31]** posteriormente estimar la evolución del valor agregado de esta canasta

**[2:11:35]** durante los próximos 12 meses. Con diferentes parámetros igual decidimos

**[2:11:40]** como analizar. Bueno, ahora en la descripción de los datos, como comenté

**[2:11:50]** este set lo obtuvimos de la ODPA, pero lo conseguimos de la página

**[2:11:55]** gobierno abierto. Cuánta con datos desde el 2008 al 2026, ya se registra con

**[2:12:01]** una frecuencia semanal en la base de datos, pero nosotros lo utilizamos de

**[2:12:04]** manera mensual. Bueno, son más de un millón de datos, clasificado en siete

**[2:12:08]** grupos de productos y tomados de nueve regiones del país, desde el

**[2:12:12]** norte al sur de Chile. Contiene 10 variables, pero las que más destacamos son

**[2:12:16]** año, mes, región, producto y precio promedio.

**[2:12:27]** Para abordar los objetivos de proyectar el costo de la canasta, el

**[2:12:32]** primer paso fue garantizar la consistencia, limpieza y representatividad de la

**[2:12:37]** base histórica. Nuestra base proviene de gobierno abierto, recopilada

**[2:12:40]** mensualmente por lo recopilada semanalmente y luego tratada de forma

**[2:12:44]** mensual por lo ODPA, lo valioso a este registro de su profundidad que

**[2:12:48]** cubre casi dos décadas de seguimiento continuo en varias regiones y grupos

**[2:12:52]** de alimentos. Esto nos da una perspectiva de largo plazo fundamental para

**[2:12:55]** observar cómo se acumula la inercia de precios y no quedarnos solo con la

**[2:12:59]** coyuntura del último año. Pasando a la siguiente lámina, para

**[2:13:08]** convertir estos datos brutos en una serie económica consistente, aplicamos

**[2:13:12]** tres etapas de depuración. Primero, omitimos los registros nulos para

**[2:13:16]** evitar vacíos en las series de tiempo. Segundo, homologamos los nombres de

**[2:13:20]** los productos para consolidar las distintas variedades comerciales en

**[2:13:24]** los alimentos representativos. Y tercero, agrupamos las regiones en cuatro

**[2:13:28]** macrozonas homogéneas. El paso metodológico decisivo fue cruzar estos

**[2:13:33]** precios con las cantidades normativas del Ministerio de Desarrollo Social.

**[2:13:36]** Así pasamos de mirar precios aislados por kilo al costo efectivo que

**[2:13:41]** realmente asume una persona al mes para alimentarse. En la siguiente día

**[2:13:46]** positiva, a partir de la base construida definimos tres hipotecís

**[2:13:51]** operativas. Primero, que la canasta no se mueve por hacer, sino que tiene una

**[2:13:55]** inercia inflacionaria marcada y marcada y componentes cíclicos que hacen

**[2:14:00]** viable modelarla con series de tiempo. Segundo, que la predictibilidad es

**[2:14:04]** profundamente desigual la estabilidad logística de los alimentos procesados

**[2:14:07]** contrasta con la vulnerabilidad climática de los que son frescos. Y

**[2:14:12]** tercero, que existen brechas territoriales sistemáticas que se

**[2:14:14]** amplían con el tiempo. Lo que significa que con un único

**[2:14:18]** promedio país no alcanza para reflejar la realidad regional.

**[2:14:22]** Esta última hipótesis queda en evidencia al ver la distribución territorial a lo

**[2:14:30]** largo del tiempo. Al inicio de la serie histórica, las regiones se

**[2:14:33]** encontraron relativamente agrupadas y pagaban costos muy similares. Sin

**[2:14:37]** embargo, con el paso de los años, especialmente tras los choques

**[2:14:41]** inflacionarios recientes, la dispersión se abrió con mucha fuerza. La

**[2:14:46]** conclusión de este gráfico es que el costo de vida no subió al mismo

**[2:14:50]** ritmo en todo el territorio, sino que al analizar la canasta con un

**[2:14:53]** promedio nacional, esconde realidad locales en donde se castiga con mayor

**[2:14:57]** fuerza a las regiones más apartadas. Pasando a la siguiente lámina,

**[2:15:03]** para entender qué genera esa desigualdad geográfica, cruzamos los

**[2:15:07]** productos con cada macro zona. El análisis muestra que el factor

**[2:15:10]** logístico domina los pienes perecibles. La macro zona sur concentra

**[2:15:13]** de forma sistemática los precios más caros en frutas y verduras debido

**[2:15:17]** a la distancia de transporte y los fletes desde la zona central.

**[2:15:20]** Pero encontramos una excepción estructural clave en donde el pan

**[2:15:23]** corriente invierte completamente la dinámica. Es comparativamente más

**[2:15:28]** barato en el sur y el alimento más encarecido en el norte.

**[2:15:31]** Esto responde a la geografía productiva. El sur cuenta con la

**[2:15:35]** molienda triguera tradicional histórica, mientras que el norte

**[2:15:38]** debe asumir el costo de transportar la harina a lo largo de

**[2:15:41]** miles de kilómetros. Con la siguiente lámina,

**[2:15:47]** frente a esa brecha, de precios del dinero, evaluamos si los

**[2:15:54]** calendarios agrícolas también cambian con la latitud. Al contrastar

**[2:15:58]** la región metropolitana con el sur, la conclusión analítica es

**[2:16:01]** muy clara en que el nivel de precios varía por territorio.

**[2:16:05]** Pero el ciclo biológico de cosecha es exactamente el mismo en

**[2:16:08]** todo el país. En ambas zonas, los cítricos tocan su momento

**[2:16:11]** de mayor escasez y alzano toño. La manzana tiene su ciclo

**[2:16:15]** emberano y las hortalizas como el tomate presionan hacia fines de

**[2:16:20]** año. La biología rige independiente que sea regional,

**[2:16:26]** sino que se vea a nivel nacional. Con la siguiente lámina,

**[2:16:33]** al normalizar los datos para aislar el efecto de la

**[2:16:36]** inflación y mirar la amplitud estacional pura,

**[2:16:39]** evaluamos nuestra hipótesis de predictibilidad desigual.

**[2:16:42]** Los bienes procesados como harina, fideos, arroz o aceite

**[2:16:46]** son prácticamente planos a lo largo del año, dominados por una

**[2:16:49]** inercia muy estable. Los productos frescos, en cambio,

**[2:16:53]** sufren oscilaciones anuelles profundas entre abundancia y

**[2:16:57]** escasez. Y el factor analítico más crítico de toda la canasta

**[2:17:01]** es la papa. La papa combina un doble impacto entre la

**[2:17:05]** volatilidad estacional altísima, sumada a que es el

**[2:17:08]** segundo alimento con mayor consumo físico mensual en

**[2:17:10]** los hogares. Es el eslabón más difícil de anticipar

**[2:17:15]** con el yel que con mayor facilidad puede desviar cualquier

**[2:17:21]** proyección presupuestaria. Teniendo identificado este mapa,

**[2:17:26]** donde conviven inercia y los choques estacionales junto

**[2:17:31]** a las brechas territoriales. Ahora veremos los

**[2:17:35]** distintos modelos predictivos.

**[2:17:41]** Hablamos distintos modelos predictivos, tanto los comunes,

**[2:17:44]** lo más estandardes que hemos trabajado como modelos

**[2:17:48]** autoregresivos y modelos también, digamos, como delineabase.

**[2:17:55]** Y obtuvimos el resultado de que los modelos tradicionales,

**[2:17:57]** como Random Forest, que daban con un error cuadrático

**[2:18:02]** bastante alejado y lejano. Así que fueron, en este caso,

**[2:18:06]** descartados y nos quedamos con modelos que serían

**[2:18:09]** autoregresivos o delineabase, que serían un

**[2:18:12]** modelo que estaban presentando en esta siguiente Madrid

**[2:18:14]** de parámetros de métricas. En este caso,

**[2:18:17]** nuestros modelos que estamos utilizando, por ejemplo,

**[2:18:19]** es el KNIP, el cual busca básicamente mantener

**[2:18:23]** el último valor y lo mantiene pegado hasta los próximos meses.

**[2:18:29]** KNIP estacional que compara según cómo estuvo la predicción

**[2:18:35]** lo real en el período anterior. Y así mismo,

**[2:18:41]** lo otro modelo autoregresivo, como sería el Sarima,

**[2:18:44]** la cual está tomando imóviles, autoregresiones y así

**[2:18:49]** sucibamente. Y lo importante es que el error que vemos

**[2:18:52]** ahí en el ETS, que es el menor, está alcanzando

**[2:18:56]** un valor de 1,320 pesos, es cual sería nuestro

**[2:18:58]** valor mejor resultado que hemos obtenido.

**[2:19:01]** ¿Se siente la mirada? Se siente la mirada

**[2:19:05]** que muestra la tendencia real de la canasta básica,

**[2:19:09]** de la canasta donde la comparamos año a año

**[2:19:13]** con los datos hasta el año anterior.

**[2:19:15]** Ejemplo, estamos comparando los datos de la canasta

**[2:19:18]** hasta el año 2020 con los datos, con los datos hasta 2020

**[2:19:22]** para predecirlo hasta el 2021.

**[2:19:24]** Así es, año tras año buscando poder ver si

**[2:19:27]** que logramos tener una buena métrica.

**[2:19:30]** Y si comparamos los datos de los primeros años

**[2:19:32]** antes de la inflación en 2020 en adelante,

**[2:19:34]** vemos que la tendencia la sigue, la continúa.

**[2:19:38]** Pero cuando esta inflación que se generó esta

**[2:19:41]** alza, esta crisis, no la logró identificar

**[2:19:43]** y vemos que la tendencia sube y la previsión también sube,

**[2:19:47]** pero sin lograr predecirlo.

**[2:19:49]** ¿Se siente la mirada?

**[2:19:56]** Tomamos también el concepto del mape, que es en este caso

**[2:20:00]** el error absoluto, comparándolo con las distintas

**[2:20:05]** zonas que hemos comentado en las matrices anteriores

**[2:20:09]** y vemos cómo este error es muy alto

**[2:20:14]** a comparativa al resto de las zonas en la zona sube.

**[2:20:17]** Quiere decir esto, es que el valor predicho se aleja

**[2:20:20]** bastante del valor real en comparativa de nosotros

**[2:20:24]** y también este valor lo vemos en la segunda

**[2:20:27]** grafica que está ahí, que nos muestra de manera positiva.

**[2:20:31]** Tenemos un mayor valor en la zona sur a comparativa

**[2:20:34]** de las otras zonas que son errores bastante más notorios.

**[2:20:41]** ¿Consiguiente la mirada?

**[2:20:45]** Ya se la acabó el tiempo, pero terminen rápido.

**[2:20:50]** Y bajo este mismo concepto es que elegimos evaluar

**[2:20:53]** estas dos zonas que son como la más representativa

**[2:20:55]** que digamos, la que tiene un mayor error,

**[2:20:57]** la geometra paritana, evaluando también

**[2:21:00]** estos modelos predictivos que comentábamos anteriormente

**[2:21:03]** elegiendo estos tres mejores para así ver cómo se comportaba

**[2:21:06]** y también que en el global genera una tendencia

**[2:21:08]** relativamente normal hasta esta alza de la crisis

**[2:21:11]** que estábamos evaluando.

**[2:21:14]** Yo creo que saltemos la otra siguiente

**[2:21:16]** y basamos en una conclusión por tema de tiempo.

**[2:21:21]** Y entonces...

**[2:21:22]** ¿Vale? Te volvamos a un producto.

**[2:21:24]** Sí, en la anterior evaluábamos unos productos,

**[2:21:26]** pero bueno, la principal es conclusiones es que,

**[2:21:29]** bueno, la canasta tiene una mejor,

**[2:21:32]** como valor de predicción de manera agregada.

**[2:21:35]** Como prediciendo el valor de la canasta agregada,

**[2:21:37]** vamos a tener un menor porcentaje de error

**[2:21:39]** que es prediciendo los productos de manera desagregada,

**[2:21:42]** ya que el nivel de error de los productos desagregados

**[2:21:45]** va desde un 2,5% hasta un 22,6%.

**[2:21:48]** En cambio, con la canasta a nivel agregado,

**[2:21:50]** el modelo DTS logra un 31,1% de error.

**[2:21:54]** Lo otro es que el territorio igual importa.

**[2:21:56]** Un modelo único no es suficiente para analizar esta problemática,

**[2:21:59]** sino que el mejor modelo a utilizar va a cambiar

**[2:22:03]** según la zona.

**[2:22:04]** Y también pudimos concluir que los modelos no anticipan shocks.

**[2:22:07]** Es un límite estructural, ya que no logró predecir

**[2:22:09]** el alza inflación al que hubo de más de casi un 30%.

**[2:22:14]** Entonces fue subestimado por los modelos,

**[2:22:17]** entonces fue más que nada pronóstico,

**[2:22:18]** fue un piso, no un valor central.

**[2:22:21]** Eso se quedó. Muchas gracias.

**[2:22:24]** Ya, gracias.

**[2:22:26]** Ok, Jason, tengo la primera pregunta para ti.

**[2:22:30]** ¿Para qué usarían este modelo?

**[2:22:37]** ¿De qué es un modelo más grande?

**[2:22:40]** El modelo nos ayudaría a poder identificar

**[2:22:44]** cómo va a estar la canasta en el próximo estampa de tiempo.

**[2:22:48]** Nosotros lo utilizamos para identificar una proyección hasta un año.

**[2:22:51]** Así que no ayudaría a poder saber si es que esto va a subir,

**[2:22:54]** si se va a mantener o...

**[2:22:56]** y el ideal sería una baja.

**[2:22:58]** Así que podría predecir esto y no se debe tomar un plan de acción.

**[2:23:01]** Me está respondiendo qué es lo que hace el modelo.

**[2:23:04]** Yo te estoy preguntando para qué sirve, a quién le sirve

**[2:23:07]** y qué es lo que podrían hacer con este modelo.

**[2:23:11]** El resultado nos ayudaría a tomar un plan de acción,

**[2:23:14]** si es que es una alza,

**[2:23:15]** poder tomar acciones correctivas, quizás,

**[2:23:19]** para evitar alguna crisis.

**[2:23:22]** ¿Quién?

**[2:23:23]** ¿Qué tomaría esas acciones?

**[2:23:26]** El gobierno.

**[2:23:28]** ¿Tú le entregaría este modelo al gobierno?

**[2:23:31]** ¿Sí?

**[2:23:33]** Ya.

**[2:23:34]** Fernanda.

**[2:23:36]** Entonces, ¿qué pasaría si es que

**[2:23:39]** tú le entrega a este modelo al gobierno?

**[2:23:40]** ¿Cómo se lo entrega?

**[2:23:41]** Así que le explicas qué es lo que hace el modelo

**[2:23:43]** y cuáles son sus cosas buenas y sus cosas malas.

**[2:23:47]** Bueno, yo les diría que este modelo igual sirve

**[2:23:50]** para hacer la predicción a un año

**[2:23:54]** del valor de la canasta base,

**[2:23:55]** igual a la salvedad de que es una canasta base.

**[2:23:58]** No es la canasta básica de alimentaria,

**[2:23:59]** que es la que utiliza el Mideso,

**[2:24:01]** pero igual pueden utilizarlo como complemento.

**[2:24:03]** Las cosas buenas es que igual tiene un error,

**[2:24:06]** una variación de 1.300 pesos si no me equivoco,

**[2:24:09]** entre como el valor real,

**[2:24:12]** pero igual la dificultad es que va a cambiar por zona.

**[2:24:15]** Entonces, tienen que tener la salvedad de que,

**[2:24:17]** dependiendo del territorio,

**[2:24:18]** igual el modelo a utilizar puede que varir.

**[2:24:21]** Entonces, es como una desventaja,

**[2:24:24]** tal vez, de la propuesta que tenemos nosotros

**[2:24:28]** como en el proyecto.

**[2:24:31]** Igual, obviamente, serviría para generar,

**[2:24:34]** como comentaba Jason, medidas preventivas

**[2:24:37]** o tomar acciones, por ejemplo,

**[2:24:39]** subsidios, ver dónde focalizar esta ayuda,

**[2:24:41]** dependiendo de cuánto va a subir.

**[2:24:43]** Obviamente, igual no está,

**[2:24:47]** no es la prueba de los chocs externos,

**[2:24:49]** por ejemplo, como la pandemia,

**[2:24:50]** igual causa un impacto de largo plazo.

**[2:24:52]** Entonces, igual sería como una salvedad.

**[2:24:56]** Igual, tal vez podría complementarse

**[2:24:58]** con más datos para que la predicción,

**[2:25:00]** con más antiguos todavía,

**[2:25:01]** para que la predicción pueda ser aún más acertada.

**[2:25:05]** Me gustaría llegar a números.

**[2:25:08]** Entonces, le voy a preguntar a Daniel ahora.

**[2:25:13]** Daniel, entonces, en términos de números,

**[2:25:15]** ¿qué es lo que querría decir si yo fui el gobierno

**[2:25:18]** y ustedes me quieren decir que use este modelo?

**[2:25:22]** ¿Qué quiere decir en términos de los números?

**[2:25:26]** Bueno, en teoría, en base al modelo,

**[2:25:30]** tendríamos un error de un 3,42% próximada.

**[2:25:34]** ¿Pueden poner el data?

**[2:25:38]** ¿Dónde sale ese 3.0 y tanto?

**[2:25:48]** ¿Dónde está ese 3.1?

**[2:25:50]** ¿De acuerdo o no?

**[2:25:57]** Disculpe.

**[2:25:58]** ¿Dónde está el 3.0 y tanto?

**[2:26:02]** Bueno, para este caso, por ejemplo,

**[2:26:03]** estaría en el, si no me lo recuerdo,

**[2:26:06]** o sea, si no me lo entiendo,

**[2:26:07]** en el de mape, en el modelo de TDS, por ejemplo.

**[2:26:15]** ¿Qué querés decir mape?

**[2:26:20]** Digamos que ya sabéis cómo te tienes que explicar esto.

**[2:26:22]** ¿Qué querés decir mape?

**[2:26:25]** ¿Qué querés decir un 3.1% de mape?

**[2:26:29]** Yo lo entendía de forma más global,

**[2:26:32]** más generalizada como el error que nos entrega el modelo.

**[2:26:37]** Ya. ¿Y qué querés decir ese 3.1?

**[2:26:41]** Bueno, ese 3.1,

**[2:26:43]** yo lo entiendo como que de lo que nosotros estamos prediciendo,

**[2:26:48]** o sea, en realidad de lo que el modelo está prediciendo,

**[2:26:51]** el 90 y algo, o sea, lo contrario del 3.17,

**[2:26:55]** sería de alguna forma tendría acertividad

**[2:26:58]** respecto al valor real que entregaría hacia el futuro.

**[2:27:03]** Por ejemplo, si tuviéramos datos hacia el 2023,

**[2:27:07]** desde el 2023 hacia adelante,

**[2:27:09]** tendríamos una prioridad de un 3.17

**[2:27:12]** entre arrojar un resultado lejano al punto real,

**[2:27:19]** que sería el error.

**[2:27:20]** Pero ¿cuál es la consecuencia de usar este modelo para mí

**[2:27:27]** como gobierno, asumiendo que yo soy el gobierno?

**[2:27:31]** ¿Cómo?

**[2:27:33]** ¿Cuál es la consecuencia?

**[2:27:34]** O sea, ¿qué gano, qué pierdo, que este 3.1,

**[2:27:40]** a qué período de tiempo es? ¿Me sirve o no me sirve?

**[2:27:45]** Ya comprendo.

**[2:27:46]** Bueno, en teoría, como vimos con los grupos anteriores,

**[2:27:49]** como el modelo se va alimentando con los mismos resultados

**[2:27:58]** que va prediciendo el mismo modelo,

**[2:28:00]** en teoría hacia el futuro se iría sobreajustando

**[2:28:04]** y por tanto el error se podría ir ampliando.

**[2:28:10]** ¿Y a qué tiempo me da este 3.1?

**[2:28:15]** Lo que logramos revisar fue desde el 2000 hasta,

**[2:28:20]** considerando datos hasta 2023 y probándolo desde 2023 hasta 2026.

**[2:28:25]** Creo que no me estoy explicando.

**[2:28:27]** Estoy preguntando, este modelo predice a que,

**[2:28:31]** ¿en qué horizonte de tiempo?

**[2:28:35]** En principio hacia un año.

**[2:28:38]** Hacia un año, entonces se equivoca un 3.1 en un año.

**[2:28:42]** Hacia un año, evidentemente.

**[2:28:45]** Pueden poner el gráfico de más adelante, por favor.

**[2:28:53]** ¿Tan de acuerdo que eso es un 3.1?

**[2:29:03]** Es como se calcula por ti, tú.

**[2:29:07]** Ay, de culpa.

**[2:29:08]** Vale, que hizo.

**[2:29:10]** Y producto de que en los primeros años,

**[2:29:14]** en horrores casi mínimos,

**[2:29:16]** genera que el promedio general de esto sea un 3.1.

**[2:29:22]** Ya.

**[2:29:23]** Entonces, si yo como gobierno quiero usar este modelo,

**[2:29:29]** yo digo esto es un desastre,

**[2:29:31]** porque veo ahí uno de horrores gigantes,

**[2:29:32]** mucho más de un 3.1.

**[2:29:34]** Entonces, digo, me están tratando de engañar.

**[2:29:38]** Claro, sin embargo, eso también es como lo vimos,

**[2:29:40]** como estaba Fernando, de que, claro,

**[2:29:42]** el modelo dentro de todo se va autoalimentando de alguna manera.

**[2:29:47]** Sin embargo, hay externalidades.

**[2:29:49]** Y, claro, y eso sería lo que no tomaría el modelo,

**[2:29:51]** que de alguna forma influiría en que haya un mayor

**[2:29:54]** rango de error, o sea, una mayor cantidad de error.

**[2:30:01]** Ya.

**[2:30:01]** Además, si comparamos el último abreccion del último año,

**[2:30:06]** la tendencia se acerca bastante de la realidad,

**[2:30:09]** donde si ocurre este valor disparaste,

**[2:30:12]** sería cuando ocurre esta gris y que sería de 2020 al 2023.

**[2:30:16]** Comitiendo eso, las tendencias predichas

**[2:30:19]** siguen bastante la línea real de lo que obtuvo la ganada.

**[2:30:24]** Ya.

**[2:30:25]** OK, gracias.

**[2:30:26]** Vamos con el último grupo, que es el grupo número 7.

**[2:30:31]** Que entiendo que son Luis, Hernán y Víctor.

**[2:30:40]** Hola, buenas tardes, ¿se escuchan?

**[2:30:43]** Se escuchan, sí.

**[2:30:44]** Ay, voy a esperar que comparte el compañero.

**[2:30:55]** Y, hola.

**[2:30:56]** No sé, no sé.

**[2:30:58]** Se está viendo.

**[2:31:06]** No lo veo, Luis.

**[2:31:08]** Mientras te hacen esto, yo voy con un vaso de agua y vuelvo ya.

**[2:31:12]** Vale.

**[2:31:14]** No se ve.

**[2:31:16]** No, yo no lo veo.

**[2:31:18]** No, no, están presentando.

**[2:31:19]** No se ve.

**[2:31:21]** Ah, sí.

**[2:31:22]** ¿Sí?

**[2:31:23]** Ya.

**[2:31:24]** Sí, se ve.

**[2:31:25]** No se ve.

**[2:31:26]** No se ve la portada.

**[2:31:29]** Sí, el mundo.

**[2:31:39]** Estábamos mejorsaltos.

**[2:31:40]** Luis.

**[2:32:15]** Sí.

**[2:32:16]** Está tratando de compartir.

**[2:32:19]** Ah, pensé que sí, que me dijeron se ve y no dejé de compartir.

**[2:32:25]** Me voy a ir a...

**[2:32:33]** ¿Me obra?

**[2:32:34]** Ahora sí.

**[2:32:35]** Está de...

**[2:32:36]** Sí, no dejaba de compartir.

**[2:32:39]** No se ve.

**[2:32:40]** No se ve.

**[2:32:41]** No se ve.

**[2:32:44]** No se ve.

**[2:32:45]** Ya.

**[2:32:55]** Ya, ya no sé.

**[2:32:56]** Listo.

**[2:32:57]** Empiecen cuando quieren.

**[2:32:58]** Ya.

**[2:32:59]** Buenas tardes, profesores.

**[2:33:00]** Buenas tardes, compañeros.

**[2:33:01]** Bueno, aquí nosotros vamos a mostrar el Lito 2, que es modelamiento preactivo y diagnóstico

**[2:33:05]** de cancer demado.

**[2:33:06]** Nuestro grupo es Luis Jara, Hernández Leyva, Juan Garcés y Víctor Mardón.

**[2:33:09]** La siguiente, por favor.

**[2:33:10]** Bueno, para refrescar la memoria, en el Lito 1 nos planteamos una pregunta

**[2:33:16]** exploratoria que dice qué características morfológicas se diferencian.

**[2:33:20]** ¿Qué características morfológicas se diferencian entre humoros benignos y malignos?

**[2:33:24]** Iguales repiten la misma señal.

**[2:33:26]** Y para el Lito 2, nos planteamos una pregunta sobre adecuidad que dice

**[2:33:29]** podemos predecir el diagnóstico de una muestra nueva.

**[2:33:32]** ¿Y con qué conjunto de variables se logra mejor equilibrio entre desempeño y simplicidad?

**[2:33:36]** Entonces, para guiarnos con esta pregunta, nos planteamos cuatro comparaciones

**[2:33:41]** que son las que nos está ahí la depositiva, que es la primera dice

**[2:33:44]** superan las variables morfológicas o una clasificación trivial.

**[2:33:48]** La pregunta número 2, las variables worse, aportan sobre las mean.

**[2:33:52]** La pregunta 3, las variables se justifican al modelo completo.

**[2:33:56]** Y la pregunta 4, ¿qué familia de modelo nos conviene, digamos, utilizar?

**[2:34:00]** La siento, por favor.

**[2:34:01]** Bueno, y el conjunto de datos tenía 569 observaciones.

**[2:34:07]** Eran 30 variables numéricas, una variable objetivo.

**[2:34:11]** El conjunto de datos estaba dividido entre 157 benignos y 212 malignos.

**[2:34:16]** Y la estructura del conjunto de datos es descaracterística para estos resúmenes

**[2:34:21]** en que cada imagen aporta mean, que es el comportamiento típico de la célula,

**[2:34:25]** SE, que es la variabilidad entre núcleos y worse, que son los núcleos más extremos.

**[2:34:30]** Y en cuanto a la calidad de los datos, sin valores nulos ni duplicados,

**[2:34:34]** se eliminó la columna ID y se eliminó la columna vacío que presentaba el archivo.

**[2:34:40]** La siento, por favor.

**[2:34:41]** Y bueno, la conclusión es que nosotros sacamos delito 1,

**[2:34:45]** que la mayor diferencia aparece en el punto concoz, perímetro, radio, área,

**[2:34:50]** compasidad.

**[2:34:51]** El punto 2, radio, perímetro y área forman un blog que es fuertemente correlacionada.

**[2:34:55]** Y los resúmenes de worse se paran mejor que las medias.

**[2:34:59]** Y el análisis descriptivo no mide desempeño predictivo.

**[2:35:02]** Eso es elito 2.

**[2:35:03]** Y para la hipótesis que nos planteamos para elito 2,

**[2:35:06]** que pone a prueba que si los worse se paran mejor,

**[2:35:09]** un modelo que las incluya debería parecer mejor que uno construye.

**[2:35:14]** Son lo con medias.

**[2:35:15]** Elito 2 pone a prueba ese hipótesis con lo que junto a BIC.

**[2:35:19]** Ya abre el cuento sobre nuestro flujo de trabajo de las 569 pacientes,

**[2:35:28]** apartamos el 20%, o sea, 114 casos, los cuales guardamos, sin tocarlo.

**[2:35:34]** Los 455 hicimos el entrenamiento, la validación y decidimos cuál era el mejor modelo.

**[2:35:41]** Para decidir, usamos la validación cruzada, partimos esos 455 casos en cinco grupos,

**[2:35:47]** por turno entrenamos con cuatro y volvamos con el que quedó fuera.

**[2:35:52]** Cada modelo además tiene perillas que hay que fijar al teletinar

**[2:35:56]** como que tan estricto es en el SVM con los errores

**[2:36:02]** y esto lo hicimos mediante GlitchRV,

**[2:36:08]** hicimos pruebas para todos los modelos, aplicando esa misma cinco ronda

**[2:36:13]** y que se quedara con el mejor, la mejor elección de los hiperparámetros.

**[2:36:18]** Esto también dentro siempre de los mismos 455.

**[2:36:22]** Recién con el modelo ya elegido y cerrado,

**[2:36:25]** abrimos el software de los casos de test, unas olaves.

**[2:36:29]** Teníamos dos preguntas.

**[2:36:34]** ¿Cuánta variable utilizar, qué modelo utilizar?

**[2:36:37]** Por el lado de las variables teníamos tres conjuntos,

**[2:36:40]** que podían ser solamente las variables mean,

**[2:36:43]** o a las mean le podríamos aportar o complementar con la box.

**[2:36:47]** Otra posibilidad también era utilizar toda la variable,

**[2:36:51]** era tren.

**[2:36:52]** Y por el lado de los modelos consideramos tres familias en tinta,

**[2:36:56]** las que el mismo en clase, el SVM lineal,

**[2:36:59]** árbol de decisión y random fault.

**[2:37:02]** Por tanto, nueve candidatos, todos compitiendo en igualdad de condiciones,

**[2:37:06]** mismo entrenamiento, mismas variaciones y mismas tométicas.

**[2:37:17]** Bueno, acá hay que considerar que para los modelos

**[2:37:20]** maligno es positivo, benigno es negativo.

**[2:37:23]** Los modelos tienen dos formas de equivocarse

**[2:37:25]** y no cuesta lo mismo.

**[2:37:27]** Por ejemplo, un falso positivo, decir que un tumor benigno,

**[2:37:30]** que se le dice maligno,

**[2:37:32]** si significa un susto, exámenes adicionales,

**[2:37:35]** en cambio, un falso negativo.

**[2:37:37]** Y lo contrario, significa que no se detecta un cáncer,

**[2:37:39]** es un error mucho más caro.

**[2:37:43]** No decidimos sobre el accuracy.

**[2:37:46]** Por ejemplo, si mirar la parte inferior,

**[2:37:49]** dice que un modelo que dijera siempre benigno,

**[2:37:54]** si mirar nada más, aceptaría en el 62,

**[2:37:57]** como a 7% los casos.

**[2:37:59]** ¿Cierto? Porque en el data set,

**[2:38:01]** en el data set hay ese porcentaje de tumores benignos.

**[2:38:05]** Esto parecería aceptable,

**[2:38:08]** pero no detectó ningún cáncer.

**[2:38:11]** Por lo tanto, la métrica a utilizar,

**[2:38:13]** que nos fijamos en el balance accuracy,

**[2:38:17]** que mide por separado

**[2:38:19]** cómo le va con cada clase,

**[2:38:21]** cómo le va con los benignos,

**[2:38:23]** y promede.

**[2:38:25]** Además, reportamos la sensibilidad de los falso negativos

**[2:38:28]** en casos concretos.

**[2:38:30]** Pasando a los resultados de la evaluación cruzada,

**[2:38:36]** podemos identificar un patrón claro

**[2:38:38]** de entre los distintos candidatos.

**[2:38:40]** Aquí tenemos a Tomatric y nos muestra

**[2:38:42]** los tres conjuntos de datos

**[2:38:43]** y los tres modelos que seleccionamos.

**[2:38:45]** Donde el conjunto A podemos ver

**[2:38:47]** que la variable min presenta

**[2:38:49]** de los tres conjuntos

**[2:38:51]** el menor desempeño general.

**[2:38:55]** Si nos pasamos al conjunto B

**[2:38:57]** podemos ver que la variable force

**[2:38:59]** presenta una mejora,

**[2:39:01]** por lo menos en Super Record Machine

**[2:39:03]** y en Random Forest.

**[2:39:05]** En cambio, el árbol es el que

**[2:39:07]** la decisión que prácticamente no mejora

**[2:39:09]** en los tres conjuntos que seleccionamos.

**[2:39:12]** Más que mirar solamente

**[2:39:14]** cuál es el modelo,

**[2:39:16]** que tiene el valor más alto,

**[2:39:18]** lo interesante es que acá estamos

**[2:39:20]** surfando cómo cambia el desempeño

**[2:39:22]** en adicional.

**[2:39:24]** En este caso, el más evidente es

**[2:39:26]** cuando pasamos del conjunto A

**[2:39:28]** y de las min y sumamos los force.

**[2:39:31]** En la siguiente depositiva

**[2:39:33]** podemos cuantificar un poco

**[2:39:35]** de mejor manera este efecto.

**[2:39:37]** Para el Super Record Machine

**[2:39:39]** pasamos de un balance a cuáles

**[2:39:41]** de 0,92 con el conjunto A

**[2:39:43]** o 0,96.

**[2:39:45]** Y la diferencia además

**[2:39:47]** es mayor que las barras,

**[2:39:49]** es mayor que las barras de error

**[2:39:51]** y exactamente claro como para considerar

**[2:39:53]** que la variable record si están aportando

**[2:39:55]** una información dedictiva adicional.

**[2:39:57]** Ahora cuando incorporamos las variabas

**[2:39:59]** ese que están en el conjunto C

**[2:40:01]** no es el comportamiento

**[2:40:03]** distinto y no es un cambio

**[2:40:05]** muy relevante por lo que podemos

**[2:40:07]** también asumir que no hay una evidencia

**[2:40:09]** concreta de que esto,

**[2:40:11]** esta variable que estamos dejando fuera

**[2:40:13]** si están aportando información predictiva.

**[2:40:16]** Siente de positiva por favor Luis.

**[2:40:18]** Entonces, para tener un criterio

**[2:40:20]** para poder seleccionar un modelo

**[2:40:22]** utilizamos un criterio donde

**[2:40:24]** vamos a analizar el modelo que presenta mayor

**[2:40:26]** balance a cuáles

**[2:40:28]** una media mayor

**[2:40:30]** si la diferencia entre estos modelos

**[2:40:32]** no es muy superior, nos vamos a hacer

**[2:40:34]** la sensibilidad y en caso de que persista

**[2:40:36]** valores similares

**[2:40:38]** no iremos por el modelo más

**[2:40:40]** menos complejo. En este caso

**[2:40:42]** el mejor desempeño lo obtenemos con

**[2:40:44]** Super Factor Machine Lineal

**[2:40:46]** utilizando el conjunto B

**[2:40:48]** de Works y con un hiper

**[2:40:50]** parámetro de 01 que seleccionamos

**[2:40:52]** mediante la función

**[2:40:54]** Grease Shirt. La

**[2:40:56]** avalización cruzada de este modelo alcanzó

**[2:40:58]** un balance a cuáles de 0.96

**[2:41:00]** más o menos

**[2:41:02]** 0.018 y una

**[2:41:04]** sensibilidad de 0.94 con un rock

**[2:41:06]** de 0.99

**[2:41:10]** Bueno, en esta parte final

**[2:41:12]** de la presentación vamos a

**[2:41:14]** mostrar la evaluación final del modelo

**[2:41:16]** seleccionado usando solamente

**[2:41:18]** un conjunto test que está formado por

**[2:41:20]** 114 muertes

**[2:41:23]** La matriz de confusión que estaba mostrando acá

**[2:41:25]** la podemos leer como ya hemos

**[2:41:27]** visto

**[2:41:29]** que es un diagnóstico real

**[2:41:31]** sí con un diagnóstico real en la fila

**[2:41:33]** y la edición en las columnias cierta

**[2:41:35]** en este caso tenemos que

**[2:41:37]** son sete de 2 velinos correctamente

**[2:41:39]** lasificando y 41 marinos correctamente

**[2:41:41]** detectados

**[2:41:43]** no hubo falsos positivos y hubo

**[2:41:45]** un solo falso negativo

**[2:41:47]** es decir un caso maligno en que el modelo

**[2:41:49]** lo clasificó como

**[2:41:51]** venido, ¿cierto?

**[2:41:54]** La siguiente, por favor

**[2:41:57]** acá nosotros tenemos una

**[2:41:59]** comparación de las matrices

**[2:42:01]** de confusión

**[2:42:03]** para los diferentes modelos, vemos que

**[2:42:05]** árbol, la edición árbol

**[2:42:07]** tiene 5 falsos negativos

**[2:42:09]** y 4 falsos positivos

**[2:42:11]** por lo que podríamos decir que uno

**[2:42:13]** de los modelos que mayor error

**[2:42:15]** comete y el para

**[2:42:17]** random forest, tenemos

**[2:42:19]** que no hay falsos positivos

**[2:42:21]** pero deja 4 malignos

**[2:42:23]** y detectar.

**[2:42:25]** Vamos a la última, por favor

**[2:42:28]** Bueno, respecto acá

**[2:42:30]** de estos plots

**[2:42:32]** de la Culver Rock

**[2:42:34]** lo que hemos visto ya

**[2:42:36]** que el eje X

**[2:42:38]** o el eje horizontal

**[2:42:40]** la tasa de falsos positivos es decir

**[2:42:42]** qué versión de los benignos

**[2:42:44]** están siendo clasificados

**[2:42:46]** correctamente como malignos y en el caso

**[2:42:48]** del eje Y tenemos la tasa

**[2:42:50]** de verdaderos positivos

**[2:42:55]** y idealmente acá lo que queremos

**[2:42:57]** es que el valor sea cercano a uno

**[2:42:59]** lo que significa una buena capacidad

**[2:43:01]** de precisión del valor cierto

**[2:43:03]** y 0.5 en este caso

**[2:43:05]** representa una selección al azate

**[2:43:07]** aquí están los comportamientos

**[2:43:09]** en el diagrama rock de los tres

**[2:43:11]** modelos que nosotros probamos

**[2:43:13]** y vemos que eso es del linear

**[2:43:15]** que tiene la mayor área bajo la curva

**[2:43:17]** la más cercana 1

**[2:43:20]** y para terminar como conclusión

**[2:43:24]** tenemos que las variables worse

**[2:43:26]** que una de las variables que consideramos

**[2:43:28]** en nuestra base de datos

**[2:43:30]** aportan también información efectiva clara

**[2:43:32]** sobre las variables mean

**[2:43:34]** pero nos produce una

**[2:43:36]** una mejora que

**[2:43:38]** consideremos

**[2:43:40]** importante

**[2:43:42]** el mejor candidato

**[2:43:44]** fue el super vector machine genial

**[2:43:46]** mal a 20 variables que consideran mean worse

**[2:43:53]** y fue seleccionado exclusivamente

**[2:43:55]** mediante la variación cruzada

**[2:43:57]** de los entrenamientos

**[2:43:59]** y con este reservado, que es decir

**[2:44:01]** con la muestra de 114 muestras

**[2:44:03]** se obtuvo un balance

**[2:44:05]** cercano a 1

**[2:44:07]** esto corresponde que de los 114

**[2:44:09]** casos el T produced un falso

**[2:44:11]** negativo

**[2:44:13]** cero falsos positivos

**[2:44:15]** eso, gracias

**[2:44:17]** ya, gracias

**[2:44:21]** apartamos con Luis

**[2:44:23]** Luis

**[2:44:25]** el mismo ejemplo de antes

**[2:44:29]** usted va en donde un médico ofrece

**[2:44:31]** un oncólogo

**[2:44:33]** y el oncólogo les dice

**[2:44:35]** saben que yo tengo

**[2:44:37]** del todo paciente que yo veo

**[2:44:39]** hay 20 pacientes

**[2:44:41]** que tienen cáncer

**[2:44:43]** de que yo le hago la piox

**[2:44:45]** y un 100% que

**[2:44:47]** perdón

**[2:44:49]** y 80% que no

**[2:44:51]** 80 pacientes que no tienen cáncer

**[2:44:54]** como interpreta eso

**[2:44:56]** que quiere decir eso al momento de que usted le pase

**[2:44:58]** en el modelo

**[2:45:03]** el modelo

**[2:45:05]** el 80

**[2:45:07]** que no tienen cáncer

**[2:45:11]** 80 no tienen cáncer

**[2:45:13]** 20 tienen cáncer

**[2:45:15]** y los 80

**[2:45:17]** que no se va en piox

**[2:45:21]** ¿por qué?

**[2:45:23]** ¿dónde lo ves?

**[2:45:26]** hasta le puedo ver por los

**[2:45:29]** falsos negativos

**[2:45:33]** en este caso

**[2:45:35]** los 80 se transportan en 72

**[2:45:37]** ahí se decidió

**[2:45:39]** que no tenían cáncer

**[2:45:41]** y el modelo hizo que no tenían cáncer

**[2:45:43]** ¿se entienden?

**[2:45:49]** si, en piox

**[2:45:51]** pero

**[2:45:53]** ese 80

**[2:45:55]** es el 72 para nosotros en esta matriz

**[2:45:57]** pero el cambio

**[2:45:59]** con los 20

**[2:46:01]** si se va a equivocar

**[2:46:04]** porque ese 20 se transforma en este 42

**[2:46:06]** y en estos 42 si tuvo

**[2:46:08]** un falso

**[2:46:10]** positivo

**[2:46:12]** ¿cuánto se va equivocar?

**[2:46:16]** ¿cuánto se va equivocar?

**[2:46:23]** bueno hay que sacar el calculado

**[2:46:25]** pero está el 0.90 y tanto era

**[2:46:27]** y lo que no se equivoca

**[2:46:33]** por ejemplo acá la probabilidad

**[2:46:39]** de ese modelo

**[2:46:41]** que suena a nosotros es 0.99

**[2:46:43]** que

**[2:46:45]** tiene probabilidad de acertar

**[2:46:47]** ese es 0.99

**[2:46:49]** la probabilidad de acertar

**[2:46:53]** si

**[2:46:58]** así luego

**[2:47:00]** pero 0.99 es cierto

**[2:47:02]** cuando le pasa una pareja de un negativo

**[2:47:04]** y un positivo

**[2:47:06]** me va a decir bien

**[2:47:08]** va a detectar quién es

**[2:47:10]** el mal himno

**[2:47:14]** el resto te acuerdo que ese 0.99

**[2:47:16]** es la probabilidad de acertar

**[2:47:26]** habría que ver la sensibilidad

**[2:47:28]** si

**[2:47:30]** la sensibilidad saliera

**[2:47:32]** que era del modelo que elegimos eran a

**[2:47:34]** 27.6%

**[2:47:36]** entonces la probabilidad

**[2:47:38]** o sea la tasa de falso negativo

**[2:47:40]** sería la resta del 2.4%

**[2:47:42]** y ese sería el 1

**[2:47:44]** y el caso

**[2:47:46]** de los 20 casos con cáncer

**[2:47:48]** ese sería el 1 de que lo estamos diciendo

**[2:47:50]** que está sano y realmente está con cáncer

**[2:47:52]** pues se dice un 4%

**[2:47:54]** de 20

**[2:47:58]** si

**[2:48:01]** en ese caso si

**[2:48:04]** sería 4%

**[2:48:06]** super

**[2:48:08]** que pasaría si que yo

**[2:48:10]** como médico

**[2:48:12]** les digo

**[2:48:14]** oye pero yo no soy médico

**[2:48:16]** a eso vemos que si

**[2:48:18]** se que yo como médico

**[2:48:20]** dijera

**[2:48:22]** oye pero yo no puedo fallar con ninguno

**[2:48:24]** que podrían hacer usted

**[2:48:27]** y déjame preguntarle a

**[2:48:29]** Víctor

**[2:48:32]** habría que buscar

**[2:48:36]** corregir mejorar el modelo

**[2:48:40]** si el modelo

**[2:48:42]** tiene cierto parámetro de error

**[2:48:44]** habría que buscar mejorarlo

**[2:48:46]** como lo mejoraría

**[2:48:51]** quizá buscando otro

**[2:48:53]** mejorar el hiper parámetro

**[2:48:58]** ya pero si yo te digo

**[2:49:00]** osea tu crees que hay un modelo perfecto

**[2:49:03]** osea no

**[2:49:05]** tengo claro que no hay un modelo perfecto

**[2:49:07]** pero habría que mejorarlo

**[2:49:09]** pero yo te digo yo necesito

**[2:49:11]** que no falle con ningún

**[2:49:13]** paciente con cáncer

**[2:49:16]** osea es como

**[2:49:18]** osea si tiene ningún modelo perfecto

**[2:49:20]** no se podría hacer

**[2:49:22]** siempre va a haber un

**[2:49:25]** un error

**[2:49:28]** la misma pregunta

**[2:49:34]** como podríamos mejorar el modelo

**[2:49:36]** yo digo yo no puedo hacer dejar

**[2:49:38]** pasar ningún paciente con cáncer

**[2:49:40]** tendríamos que

**[2:49:47]** tendríamos que llevar

**[2:49:51]** la tasa

**[2:49:53]** o el rical, la suicidía

**[2:49:55]** la tasa de falso de verdadero positivo

**[2:49:57]** lo más cercano

**[2:49:59]** a uno

**[2:50:02]** la tasa de verdadero positivo

**[2:50:04]** lo más cercano a uno

**[2:50:07]** eso

**[2:50:09]** ya y como las 10

**[2:50:16]** llevando la tasa de

**[2:50:21]** falso negativo

**[2:50:23]** osea el falso

**[2:50:25]** positivo a cero

**[2:50:31]** ya, la tasa de

**[2:50:33]** pero como lo harías en la práctica

**[2:50:37]** bueno acá lo que

**[2:50:41]** hicimos osea

**[2:50:43]** enteriendo que

**[2:50:46]** tratamos de hacer fue exactamente eso

**[2:50:48]** probamos diferentes modelos

**[2:50:50]** que solo sube el Tectromachy

**[2:50:52]** decisión fobresito

**[2:50:54]** y claro la idea era

**[2:50:56]** obtener la mayor

**[2:50:58]** tasa de verdaderos

**[2:51:01]** positivos

**[2:51:03]** justamente aplicando como una metodología

**[2:51:05]** similar ahora pero

**[2:51:08]** no se como llegar al modelo perfecto

**[2:51:10]** que no hay que llegar al modelo perfecto

**[2:51:13]** no

**[2:51:17]** no se como lo pueden hacer sin llegar

**[2:51:19]** al modelo perfecto pero yo no quiero perder ningún paciente

**[2:51:21]** con cáncer

**[2:51:24]** a ver lo que se me ocurre profe

**[2:51:26]** hay que responderle si el doctor

**[2:51:28]** sin decirle que

**[2:51:30]** que no existe el modelo perfecto sería forzada

**[2:51:32]** que el modelo

**[2:51:34]** clasifique algún

**[2:51:36]** tumor benigno como maligno

**[2:51:38]** osea si fuera el

**[2:51:40]** centrarnos solo en el modelo superfecto al machín

**[2:51:42]** disminuir el umplano acercándose a lo

**[2:51:44]** para que

**[2:51:46]** asegurarme que toma todos los malignos

**[2:51:48]** y si sacrificando la

**[2:51:50]** predicción de los benignos

**[2:51:52]** hace maligno

**[2:51:54]** pero tendría

**[2:51:56]** también le explicaría

**[2:51:58]** de que significa que

**[2:52:00]** osea que el modelo

**[2:52:03]** no está forzado

**[2:52:05]** osea no

**[2:52:08]** abordamos su requerimiento pero

**[2:52:10]** que entienda que no es

**[2:52:12]** un modelo tan realista osea pasar varios

**[2:52:14]** colapos

**[2:52:16]** ya perfecto

**[2:52:20]** estamos entonces

**[2:52:22]** creo no falta ningún grupo no

**[2:52:25]** no

**[2:52:29]** nos vemos entonces ah

**[2:52:31]** próxima semana

**[2:52:33]** sesión presencial

**[2:52:35]** yo no voy a poder estar porque voy a estar en estados

**[2:52:37]** unidos entonces

**[2:52:39]** Alejandra va a realizar la sesión presencial

**[2:52:46]** la sesión presencial

**[2:52:48]** porque acá igual la vemos alumnos de

**[2:52:50]** personalmente soy del diplomado

**[2:52:52]** no se si es para el diplomado

**[2:52:54]** al menos a mi no me ha llegado ninguna invitación

**[2:52:56]** hasta ahora

**[2:52:59]** la sesión presencial es del magister

**[2:53:01]** si te creen benigno hay problema

**[2:53:03]** lo alumno del diplomado que el benigno

**[2:53:05]** hay ningún problema

**[2:53:08]** si resulta bueno la vez pasada

**[2:53:10]** yo asistí a esa sesión personal pero

**[2:53:12]** claro había

**[2:53:14]** por ejemplo incluía almuerzo que teníamos

**[2:53:16]** que matricularse e inscribirme y todo

**[2:53:18]** ahora no se se hizo con alteraciones

**[2:53:20]** ahora estamos como super encima

**[2:53:22]** pero igual quería hablar de eso

**[2:53:24]** estaré con su integración igual

**[2:53:27]** y voy a pedirles que le den información ok

**[2:53:29]** eso una consulta

**[2:53:33]** con esto terminaríamos

**[2:53:35]** o es también es que enviarle un informe

**[2:53:37]** no con esto estamos listos

**[2:53:39]** ya

**[2:53:41]** una consulta

**[2:53:43]** lo que pasa es que en el documento

**[2:53:45]** Silavus hay un 20%

**[2:53:47]** como perdido

**[2:53:49]** ese se le suma las presentaciones o no

**[2:53:51]** porque es de un informe pero no ha habido informe

**[2:53:55]** ah

**[2:53:58]** fue un error mío en el Silavus

**[2:54:02]** pero para que del 100 entonces

**[2:54:04]** que se veinte a que cosa

**[2:54:06]** al proyecto

**[2:54:08]** son 30 y 30 entonces

**[2:54:10]** déjame revisar el Silavus

**[2:54:13]** dame un segundo

**[2:54:33]** si quieren pueden dejarte de presentar

**[2:55:20]** pero son clientes en la mano levantar

**[2:55:22]** si si pero estoy revisando

**[2:55:24]** no se lo voy a captar

**[2:55:27]** ya en el

**[2:55:30]** en las slides de la primera clase

**[2:55:32]** aparece el porcentaje correcto

**[2:55:34]** fue un error mío del Silavus

**[2:55:36]** entonces son 25% para la primera

**[2:55:39]** presentación y 35% para la segunda

**[2:55:41]** gracias

**[2:55:46]** ahora sí y Cristian, disculpe

**[2:55:48]** si no se preocupen

**[2:55:51]** hay que una pequeña consulta

**[2:55:53]** de

**[2:55:55]** la próxima sesión

**[2:55:57]** esta vez de casualidad que se va

**[2:55:59]** a hacer como dice

**[2:56:01]** sola materia o sorpresa

**[2:56:03]** la sesión presencial

**[2:56:06]** si

**[2:56:09]** si quieres saberlo

**[2:56:11]** o prefieres ser sorprendido

**[2:56:13]** es una sorpresa

**[2:56:16]** sorpresa porfa

**[2:56:18]** es una sorpresa

**[2:56:20]** es una sorpresa buena

**[2:56:22]** es una sorpresa buena

**[2:56:24]** vamos a

**[2:56:26]** vamos a hacer un

**[2:56:28]** un desafío

**[2:56:30]** entonces le vamos a pasar un dataset

**[2:56:32]** y se van a juntar en grupo

**[2:56:34]** y tienen que trabajar con el dataset

**[2:56:36]** y gana el equipo que lo saque más rápido

**[2:56:38]** perdón más rápido con mejor

**[2:56:40]** valores

**[2:56:42]** activo jacatón

**[2:56:44]** profesor, una consulta

**[2:56:47]** vamos a tener algún tipo de retroalimentación

**[2:56:49]** de todo esto, que la idea libre es

**[2:56:51]** yo en la presencia

**[2:56:53]** pero ya que no se va a poder

**[2:56:55]** como para saber qué tan

**[2:56:57]** tan propiedad más en nuestros proyectos

**[2:56:59]** y tal cosa

**[2:57:01]** yo le puedo decir al general

**[2:57:05]** yo creo que en general

**[2:57:09]** están bien

**[2:57:11]** pero les falta la interpretación

**[2:57:13]** y a todos les falta la interpretación

**[2:57:15]** a todos los grupos

**[2:57:17]** uno no hace un modelo por hacer un modelo

**[2:57:19]** uno hace un modelo porque quiere resolver algo

**[2:57:21]** y la pregunta es

**[2:57:24]** si tu modelo resolvió ese algo

**[2:57:26]** y uno tiene

**[2:57:28]** un montón de números

**[2:57:30]** que puede tener

**[2:57:32]** pero si esos números no los interpreto

**[2:57:34]** o no los transforma en realidad

**[2:57:36]** nos sirve mucho

**[2:57:40]** y a todos los grupos les falta la interpretación

**[2:57:42]** algunas personas

**[2:57:44]** de los grupos

**[2:57:46]** algunos integrantes

**[2:57:48]** de los grupos supieron interpretar

**[2:57:50]** pero en todos los grupos

**[2:57:52]** había al menos un integrante

**[2:57:54]** que no supo interpretar

**[2:57:57]** y eso es lo más importante

**[2:57:59]** o sea todo el resto está bien

**[2:58:01]** se necesita y todo lo que uno quiera

**[2:58:03]** pero si yo al final no puedo interpretarlo

**[2:58:05]** entonces no puedo saber

**[2:58:07]** si es que lo que tengo que hacer

**[2:58:09]** o sea si es que el modelo lo puedo usar o no

**[2:58:11]** tiene que estar el modelo matemático

**[2:58:14]** tiene que estar súper amarrado a la realidad

**[2:58:16]** y los resultados

**[2:58:18]** los números tienen que estar súper amarrado

**[2:58:20]** a la realidad

**[2:58:24]** y ver su experiencia

**[2:58:26]** esto es solo práctica de más estudios

**[2:58:28]** poner, meter más cabeza

**[2:58:30]** yo creo que es

**[2:58:32]** a mi también me pasó cuando yo aprendí

**[2:58:34]** me acuerdo ahora que ustedes me dijeron

**[2:58:36]** pero que es difícil

**[2:58:38]** yo me acordé que cuando yo lo aprendí

**[2:58:40]** me costó

**[2:58:42]** entender lo que eran los falsos positivos

**[2:58:44]** los verdaderos negativos

**[2:58:46]** toda esa tasa de falsos positivos

**[2:58:48]** pero en un momento me di cuenta

**[2:58:50]** de que no lo estaba entendiendo

**[2:58:52]** y me dediqué a entenderlo

**[2:58:54]** y estuve harto rato tratando de entenderlo

**[2:58:56]** así como de

**[2:58:58]** y que pasaría si es que

**[2:59:00]** no sé

**[2:59:02]** el recall sube un 10%

**[2:59:04]** qué quiere decir

**[2:59:06]** y como que me empezaba a pensar

**[2:59:08]** y a calcular y todo

**[2:59:10]** no tiene sentido

**[2:59:12]** y me tomó harto tiempo

**[2:59:14]** esa es la verdad porque como que lo entendía

**[2:59:16]** decía ya, a vacán lo entendí

**[2:59:18]** y después se me olvidaba al mes

**[2:59:20]** y al mes tenía que de nuevo hacer todo el ejercicio

**[2:59:22]** y agarrar a mi cuenito

**[2:59:24]** buscar lo que había notado y decía

**[2:59:26]** ay, a verdad y ahí lo entendía

**[2:59:29]** y ahora me sale como más natural

**[2:59:31]** yo creo porque

**[2:59:33]** lo veo como lo he visto mucho tiempo

**[2:59:35]** pero

**[2:59:37]** tienen que

**[2:59:40]** practicarlo

**[2:59:44]** Profesor, yo quería comentar algo

**[2:59:46]** y bueno

**[2:59:48]** primero agradecer

**[2:59:50]** de verdad todo el espacio porque

**[2:59:52]** al menos en mi caso que no vengo del mundo

**[2:59:54]** de la ingeniería ni de los datos

**[2:59:56]** ni

**[2:59:58]** me ha ayudado un montón en aprender

**[3:00:00]** estuve acuerdo

**[3:00:02]** que efectivamente

**[3:00:04]** yo creo que

**[3:00:06]** nos hizo falta

**[3:00:08]** y aquí quizás un poco el feedback

**[3:00:10]** no sé si algunos compañeros

**[3:00:12]** percibieron lo mismo

**[3:00:14]** pero

**[3:00:16]** desde mi punto de vista, yo creo que

**[3:00:18]** claro, las clases prácticas

**[3:00:20]** fueron muy enfocadas obviamente

**[3:00:22]** en la parte teórica

**[3:00:24]** muy enfocadas en lo teórico

**[3:00:26]** lo cual está bien

**[3:00:28]** pero yo al menos en particular siento

**[3:00:30]** que si hubo cierta desconexión

**[3:00:32]** en la parte práctica

**[3:00:34]** con la parte teórica

**[3:00:36]** sentir desconexión en el sentido

**[3:00:38]** que quizás nos íbamos también muy en lo técnico

**[3:00:40]** en Python

**[3:00:42]** en cómo hacer las cosas en Python

**[3:00:44]** y quizás no aterrizamos

**[3:00:46]** ejemplos más prácticos

**[3:00:48]** para que nosotros también pudiéramos

**[3:00:50]** empezar a

**[3:00:52]** entrenar este

**[3:00:54]** pensamiento más crítico

**[3:00:56]** entonces quizás como

**[3:00:58]** recomendación

**[3:01:00]** quizás integrar un poco mejor eso

**[3:01:02]** porque yo al menos sentía muchas veces en la parte práctica

**[3:01:04]** que era como estar en clases de Python

**[3:01:06]** para poder hacer

**[3:01:08]** random force

**[3:01:10]** y para poder hacer todo lo que nos han enseñado

**[3:01:12]** pero si no había

**[3:01:14]** casos específicos para desarrollar

**[3:01:16]** entonces eso yo creo que estaría bueno

**[3:01:18]** para

**[3:01:20]** para ayudarnos

**[3:01:22]** a entender de mejor forma

**[3:01:24]** en un caso como interpretar los datos

**[3:01:26]** eso

**[3:01:29]** ya, no estoy tomando

**[3:01:31]** de hecho lo estoy anotando

**[3:01:33]** o para considerar ese feedback

**[3:01:35]** para la próxima interacción

**[3:01:37]** te lo agradezco mucho que iden

**[3:01:39]** yo comparto igual como que iden

**[3:01:41]** porque

**[3:01:43]** desde lo que usted nos comenta

**[3:01:45]** claramente hay que darle como

**[3:01:47]** hacerle sentido más al dato

**[3:01:49]** al número a la interpretabilidad

**[3:01:51]** eso

**[3:01:55]** una consulta profe

**[3:01:58]** una prox

**[3:02:00]** las notas más o menos

**[3:02:02]** que notas tienes

**[3:02:04]** si cuando van a estar

**[3:02:06]** al menos la primera

**[3:02:08]** presentación

**[3:02:10]** las tengo acá

**[3:02:12]** y no la haya subido así que les pido disculpas

**[3:02:14]** se me olvido completamente de subirla

**[3:02:16]** lo siento

**[3:02:18]** es responsabilidad mía

**[3:02:21]** y de verdad lo lamento

**[3:02:23]** tengo las notas de la primera

**[3:02:25]** me importa si le coloca una décima va

**[3:02:27]** quedamos súper bien, todo

**[3:02:29]** por una décima

**[3:02:31]** no un punto

**[3:02:33]** claro

**[3:02:35]** por un asadito

**[3:02:37]** un asadito estaría bueno

**[3:02:39]** eso sí que se los daría pero

**[3:02:41]** pucho voy a estar en estados unidos

**[3:02:43]** así que no

**[3:02:45]** un asado virtual

**[3:02:47]** yo soy de sanctuario de la organiza

**[3:02:49]** pero si no

**[3:02:51]** para profe ya no tienes que regresar

**[3:02:53]** oye pero si quieren

**[3:02:55]** de verdad si quieren organizamos

**[3:02:57]** una saga

**[3:03:00]** si usted organiza una saga me invitan yo voy

**[3:03:02]** eso eso eso

**[3:03:04]** ya pues

**[3:03:06]** pero va a estar en estados unidos

**[3:03:08]** pero en otro momento

**[3:03:10]** ok no solamente

**[3:03:12]** pero bueno díselo con tiempo

**[3:03:14]** que yo estoy en santiago

**[3:03:16]** para la próxima presencial

**[3:03:18]** para la próxima presencial podría ser

**[3:03:22]** pero ellos no me toca

**[3:03:24]** porque no

**[3:03:26]** no hago el próximo trimestre ramos

**[3:03:28]** pero lo invitamos profe

**[3:03:31]** va como invitado

**[3:03:33]** es en un asado yo llevo

**[3:03:35]** ya

**[3:03:38]** ok le voy a subir

**[3:03:40]** las notas mañana por favor

**[3:03:42]** no se preocupen

**[3:03:44]** no se preocupen

**[3:03:46]** tengo la profesora que se demoramos

**[3:03:48]** así que dos días

**[3:03:50]** tres días

**[3:03:52]** hoy tengo acá todas las notas

**[3:03:54]** ya

**[3:03:56]** ok estamos

**[3:03:58]** gracias

**[3:04:00]** gracias

**[3:04:02]** chau
