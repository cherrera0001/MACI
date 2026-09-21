# 06Ayudantia Fundamentos en Ciencia de Datos 31 Julio.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:37:51
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:00:00]** No, ahí no grabamos, súper.

**[0:00:04]** Ya.

**[0:00:05]** Hola, en tanto tiempo, porque no nos habíamos visto desde hace

**[0:00:08]** como dos semanas, tengo que empezar con algo que nos

**[0:00:15]** quedamos pendiente de la clase pasada.

**[0:00:17]** No sé si se acuerdan que la clase pasada vimos un poquito de

**[0:00:21]** una librería que se llama Nampi, para hacer como descripción

**[0:00:27]** general de los datos, sacar algunos estadísticos que ya

**[0:00:29]** habíamos visto en el Describe de Pandas.

**[0:00:33]** Y vimos un poquito de introducción a cómo se hacen los

**[0:00:35]** gráficos, con una, grabó chiquito,

**[0:00:41]** con una librería que se llama Matplotlib.

**[0:00:44]** Y debíamos haber quedado como...

**[0:00:50]** Creo que aquí, creo que en tipos de gráficos.

**[0:00:53]** Creo que quedamos aquí.

**[0:00:54]** Creo que llegué a terminar de decir qué cosa hace cada

**[0:00:59]** gráfico, así como cómo se pone el título,

**[0:01:02]** cómo se cambian los colores, cómo se cambia la opacidad,

**[0:01:05]** etcétera, etcétera.

**[0:01:07]** ¿Sí?

**[0:01:08]** ¿Recordamos eso más o menos?

**[0:01:13]** Sí.

**[0:01:16]** Ya.

**[0:01:16]** Entonces, voy a ponir un par de anteriores, por si acaso,

**[0:01:21]** porque tenía el entorno prendido, pero no me acuerdo.

**[0:01:24]** Entonces vimos cómo ocupar Nampi para hacer muchas de las

**[0:01:28]** operaciones que hace el Describe.

**[0:01:30]** Pero qué pasa si yo quiero hacer alguna modificación o

**[0:01:32]** quiero hacer esto a mano o quiero hacer alguna cosa un

**[0:01:35]** poquito más detallada.

**[0:01:36]** Por eso necesito ver cuáles son las funciones que se ocupan

**[0:01:39]** debajo y por qué Nampi, porque es mucho más rápido que hacerlo

**[0:01:45]** directamente con Python nativo, ¿OK?

**[0:01:47]** Y es lo que ocupa pandas también por detrás cuando está

**[0:01:50]** haciendo, por ejemplo, cosas como el Describe.

**[0:01:53]** Y después habíamos visto Matplotlib,

**[0:01:54]** que era esta librería para hacer los gráficos.

**[0:01:57]** Y en estas cosas básicas, en esta partecita que hice

**[0:01:59]** cosas básicas, habíamos visto cada una de las cosas de poner

**[0:02:03]** colores, poner un histogramo.

**[0:02:06]** O sea, un gráfico sobre otro, poner las labels,

**[0:02:11]** que serían como las etiquetas del gráfico,

**[0:02:16]** ponerle nombres a los ejes, etcétera, etcétera.

**[0:02:19]** Pero yo lo había explicado solamente con un histograma,

**[0:02:22]** que eran estos de aquí.

**[0:02:24]** Entonces faltaba explicar qué otros tipos de gráficos nos

**[0:02:27]** podíamos encontrar.

**[0:02:28]** Y obviamente hay un montón de tipos de gráficos y

**[0:02:32]** depende mucho con los tipos de datos con los que yo estoy

**[0:02:34]** trabajando, pero siempre voy a ocupar, por ejemplo,

**[0:02:36]** lo típico es ver un histograma, un gráfico de barras,

**[0:02:39]** un gráfico de dispersión.

**[0:02:41]** Y ya cuando necesito gráficos más difíciles,

**[0:02:45]** igual siempre está la documentación, por si acaso,

**[0:02:47]** siempre siempre está la documentación.

**[0:02:50]** Entonces para mostrar algunos tipos de gráficos de aquí en

**[0:02:53]** este ejemplo, vamos a ocupar este dataset que nos habla,

**[0:02:56]** solamente mide una variable que sería la calidad de aire.

**[0:03:00]** Y es solamente este valor, pero para distintas como

**[0:03:04]** instantes en el tiempo y está medido en tres estaciones de

**[0:03:09]** metro de París.

**[0:03:12]** Entonces es solamente un dato, es bastante sencillo,

**[0:03:15]** solamente que tiene temporalidad.

**[0:03:17]** Ya.

**[0:03:18]** Entonces, por ejemplo, vamos a ver el tipo de gráfico.

**[0:03:21]** Aquí yo pongo DF, que es el nombre del data frame de

**[0:03:25]** pandas, con el que yo instancia como los datos,

**[0:03:29]** es la tabla.

**[0:03:30]** Pero por debajo lo que está pasando está ocupando

**[0:03:33]** matplotlib.

**[0:03:34]** Entonces, todo lo que yo haga aquí,

**[0:03:36]** que lo haga con esta sintaxis, también lo puedo hacer con

**[0:03:39]** matplotlib, ¿OK?

**[0:03:40]** Y se llama parecido el plot, también se llama plot en matplotlib,

**[0:03:44]** el histograma aquí se llama inst, y también se llama inst

**[0:03:46]** en matplotlib, y así.

**[0:03:48]** Entonces, el plot es un gráfico de líneas,

**[0:03:51]** pero que no borrela.

**[0:03:52]** No, no borrela.

**[0:03:54]** Ya lo vamos a ver al mismo tiempo.

**[0:03:55]** El plot es un gráfico de líneas y en este caso nos

**[0:03:58]** sirve para ver el comportamiento de una variable en el

**[0:04:00]** tiempo, ¿OK?

**[0:04:02]** Día DF mundo plot y me muestro.

**[0:04:05]** Por defecto, como ya está puesto,

**[0:04:07]** simplemente aquí le estoy pasando la tabla entera,

**[0:04:11]** me está mostrando las tres estaciones.

**[0:04:14]** Pero yo podría decirle que me filtrara por cierta columna,

**[0:04:18]** por ejemplo, porque aquí los valores de las estaciones están

**[0:04:22]** en las columnas, entonces podría filtrar solamente

**[0:04:25]** porque me quedara con esta columna.

**[0:04:27]** Y así simplemente hago eso en el plot y solo me sale.

**[0:04:32]** Porque aquí, por ejemplo, la que es en azul está un poco

**[0:04:35]** aplastada.

**[0:04:35]** Eso también lo puedo solucionar con algunas de las herramientas que

**[0:04:37]** mismo antes, por ejemplo, la alfa, etcétera, etcétera.

**[0:04:41]** Otro es el histograma que me muestra la frecuencia.

**[0:04:44]** Yo puedo ver la distribución de los datos.

**[0:04:47]** Entonces, me muestra la frecuencia de distribución de

**[0:04:48]** los datos.

**[0:04:48]** Me quiero ver más o menos cómo se está comportando una

**[0:04:51]** variable, si es que la distribución está cegada,

**[0:04:54]** dónde están como los pics, así como los valores que más

**[0:04:57]** se repiten, si es uniforme, entre otros.

**[0:05:00]** Entonces, para esto, yo voy a seleccionar, como dije,

**[0:05:03]** podemos seleccionar una columna para hacer estas operaciones.

**[0:05:05]** Entonces, voy a seleccionar una columna específica,

**[0:05:08]** que sería una estación específica, y hago punto Isto.

**[0:05:12]** Y eso es muy parecido al histograma que hicimos en

**[0:05:14]** mat.lib, en el primer ejemplo que poníamos plet.ist.

**[0:05:17]** Aquí pongo el dataframe.ist.

**[0:05:20]** Y me muestra un histograma.

**[0:05:22]** Entonces, aquí vemos el comportamiento de los valores,

**[0:05:27]** pero con respecto en sí a cómo se comporta la variable.

**[0:05:30]** Entonces, puedo ver, por ejemplo, que el valor más repetido

**[0:05:33]** está entre 20 y 40, porque aquí veo la frecuencia.

**[0:05:36]** Y puedo ver, porque puedo ver el rango en el que se mueve la

**[0:05:38]** variable.

**[0:05:39]** Entonces, puedo decir que ya va entre 0 y yo mirando el gráfico

**[0:05:43]** aquí muy visual, diría que va entre 0 y 70,

**[0:05:47]** pero el gráfico me está mostrando hasta 100.

**[0:05:50]** Esto que significa que aquí, de forma muy pequeñita,

**[0:05:53]** hay un par de datos que están entre 80 y 100,

**[0:05:56]** pero son muy pocos casos de los registrados.

**[0:06:01]** Luego tengo los scatter, que son gráficos de dispersión,

**[0:06:04]** y me permiten mostrar relación entre dos variables,

**[0:06:07]** cómo se comporta una variable versus la otra, ¿OK?

**[0:06:09]** Entonces, aquí con este gráfico normalmente puedo encontrar

**[0:06:13]** tendencias, ¿OK?

**[0:06:17]** Entonces, aquí tengo un scatter,

**[0:06:19]** este se hace con df.plot.scatter y en mat.lib es

**[0:06:23]** simplemente .scatter.

**[0:06:25]** Y le indicó lo que quiero que estén el eje X y lo que

**[0:06:28]** quiero que estén el eje Y.

**[0:06:29]** Y en este caso, normalmente, cuando estamos haciendo un

**[0:06:31]** scatter, ocupamos el alfa.

**[0:06:33]** ¿Por qué?

**[0:06:34]** Porque normalmente muchos puntos van a quedar sobre otros,

**[0:06:38]** y para poder ver dónde se concentran más los puntos,

**[0:06:42]** dónde está la tendencia, necesitamos el alfa.

**[0:06:45]** ¿Dónde estén más cargado el color?

**[0:06:49]** Significa que hay más puntos.

**[0:06:52]** También tenemos un boxplot.

**[0:06:54]** Esto es muy útil para ver cómo se están comportando

**[0:06:58]** también las variables, sus valores como por donde se

**[0:07:02]** mueven, sus valores típicos y, por ejemplo,

**[0:07:04]** si es que habrían outliers, una buena forma de visualizar eso,

**[0:07:08]** cómo se están moviendo distintas variables al mismo

**[0:07:10]** tiempo.

**[0:07:11]** Entonces, este típico gráfico de caja donde aquí esto se

**[0:07:13]** consideraría como el outlier, que está la mediana,

**[0:07:16]** etcétera, etcétera.

**[0:07:19]** Después tenemos, por ejemplo, un gráfico de área y esto

**[0:07:22]** normalmente se utiliza en series de tiempo cuando se

**[0:07:24]** quiere observar como un todo, ¿OK?

**[0:07:27]** Entonces, básicamente, estoy viendo como cada uno de los

**[0:07:31]** datos está contribuyendo a mirar los datos totales.

**[0:07:35]** Entonces, esto se hace con df.plot.area y aquí lo puedo hacer

**[0:07:38]** simplemente, pasándole el data desde este caso entero.

**[0:07:45]** No me salto, no me faltan dos.

**[0:07:48]** Después tenemos el típico gráfico de barras y normalmente

**[0:07:51]** aquí estamos graficando valores.

**[0:07:53]** Entonces, ¿qué pasa cuando tenemos categorías?

**[0:07:56]** Bueno, el gráfico de barras es el que nos viene útil aquí

**[0:07:59]** cuando yo quiero mostrar las distintas variables

**[0:08:02]** categóricas, cada una la voy a representar con una bar, ¿OK?

**[0:08:06]** Así que quiero hacer alguna, por ejemplo,

**[0:08:08]** la distribución de las clases, por ejemplo,

**[0:08:11]** o la distribución de cierto tipo de datos que yo sé que es una

**[0:08:14]** variable categórica, no le puedo hacer un histogramo.

**[0:08:17]** Entonces, típicamente se le hace un gráfico de barras para

**[0:08:20]** mostrar esta información.

**[0:08:21]** Entonces, en este caso, una variable que yo sé que es

**[0:08:24]** categórica es el tipo de colisión.

**[0:08:29]** Y lo vamos a hacer y aquí no lo hago directamente con df.bar,

**[0:08:33]** pero le estoy agregando varias cosas para que se vea bonito, ¿OK?

**[0:08:38]** Entonces, la típica sintaxis que habíamos visto sería esta, ¿OK?

**[0:08:45]** Con respecto al ejemplo que vimos de la histograma,

**[0:08:48]** la clase pasada.

**[0:08:49]** Entonces, en vez de histograma, como aquí es un gráfico de

**[0:08:51]** barras, le pongo plt.bar.

**[0:08:53]** ¿Y qué le pongo?

**[0:08:54]** Lo que quiero que esté en el eje x y lo que quiero que esté

**[0:08:57]** en el eje y, en ese orden, primero el x, después el.

**[0:09:02]** Esto tiene muchos más parámetros con los que puedo

**[0:09:04]** jugar.

**[0:09:05]** ¿Y qué significa todo esto?

**[0:09:06]** Bueno, estos tres ya los habíamos visto.

**[0:09:09]** Uno está poniéndole el título, otro está asignando el valor,

**[0:09:13]** o sea, el título al eje x y el título al eje.

**[0:09:17]** Este type layout es básicamente para que el gráfico esté

**[0:09:20]** compactado después y que yo lo quiero guardar,

**[0:09:23]** que no tenga tanto espacio en blanco.

**[0:09:26]** Y el pelote.john, que yo lo habíamos mostrado,

**[0:09:28]** que es cuando yo quiero explícitamente decirle,

**[0:09:30]** muéstrame el gráfico.

**[0:09:33]** Y estos tics son para indicar lo que está en el eje x, aquí.

**[0:09:41]** Esto normalmente va a salir o de lado, la típica de lado.

**[0:09:45]** Y de repente, cuando están todos horizontales,

**[0:09:48]** se pueden ver mal, en especial cuando las categorías son como

**[0:09:51]** varias palabras o palabras muy grandes.

**[0:09:53]** Le podría cambiar el tipo de letra, pero si es que le

**[0:09:56]** achico el tipo de letra, voy a tener problemas para

**[0:09:57]** visualizarlo.

**[0:09:59]** Entonces, lo que podemos hacer es ocupar este x tics para

**[0:10:02]** indicar estos valores en el eje x y decirles que tengan una

**[0:10:06]** rotación, ¿ok?

**[0:10:08]** Y le ponemos una rotación de 45 para evitar que se vayan

**[0:10:11]** chocando.

**[0:10:12]** Si es que no le pongo nada van a estar horizontal,

**[0:10:15]** veis que eso no se chocan en la visualización que yo hago,

**[0:10:18]** no hay problema.

**[0:10:21]** Y estos son barras, pero también se pueden hacer

**[0:10:23]** barras horizontales.

**[0:10:24]** Y eso es lo mismo, solamente que en vez de poner bar,

**[0:10:27]** pongo barh, indicando bar horizontal.

**[0:10:31]** Y por último tenemos, bueno, es que hay muchos más, pero bueno,

**[0:10:39]** tenemos, por ejemplo, el gráfico de tort,

**[0:10:41]** que yo sé que este es como muy utilizado como en informes.

**[0:10:46]** Esto tiene un poquito más de cosas más difícil hacerlo,

**[0:10:51]** codearlo, porque hay que ver mucho manejo de lo que quiero

**[0:10:56]** que muestre.

**[0:10:57]** Por ejemplo, quiero que muestre las etiquetas de cada

**[0:10:59]** categoría, el porcentaje de cada categoría,

**[0:11:01]** en qué formato, etcétera, etcétera.

**[0:11:03]** Entonces, un poquito, un poquito más difícil.

**[0:11:06]** Entonces, aquí como lo estoy haciendo,

**[0:11:07]** aquí estoy con la tabla.

**[0:11:09]** Esto es toda la tabla.

**[0:11:10]** Esto es lo mismo que poner DF.

**[0:11:12]** Solamente que estoy haciéndole algunas modificaciones

**[0:11:15]** de esta tabla.

**[0:11:15]** Entonces, esto sería el DF.

**[0:11:17]** Y estoy poniendo punto plot, punto pi,

**[0:11:19]** como gráfico de tort.

**[0:11:21]** Y le estoy diciendo que el formato que tenga los

**[0:11:24]** numeritos sea esto.

**[0:11:26]** No hay mucho que pescar ahí.

**[0:11:28]** Lo importante es que le estoy diciendo,

**[0:11:29]** forma todos los numeritos.

**[0:11:32]** Y que tenga un título y que en realidad no tenga título en

**[0:11:36]** LG.

**[0:11:36]** No me interesa que tenga título en LG.

**[0:11:40]** Y aquí tenemos el gráfico de tort.

**[0:11:42]** Y dice que quisiera agregarle esto.

**[0:11:44]** Entonces, si se acuerdan del legend,

**[0:11:46]** tendría que especificarle el layout de manera explícita,

**[0:11:52]** pasándole el index de la tabla.

**[0:11:55]** Y se acuerdan que dije que el legend se podía mover.

**[0:11:58]** Me acuerdo, había unos parámetros para moverlo.

**[0:12:01]** Es el lock.

**[0:12:02]** Eso indica dónde se va a poner el legend.

**[0:12:05]** Entonces, si es que yo le pongo right,

**[0:12:07]** se va a ir a la esquina derecha.

**[0:12:09]** Si es que le pongo led.

**[0:12:10]** O sea, top right, se va a ir a la esquina derecha de arriba y

**[0:12:15]** así.

**[0:12:15]** Entonces, puedo jugar, no puedo forzar a dónde quiero que

**[0:12:17]** esté.

**[0:12:18]** Por defecto, se supone que se pone en la posición donde no

**[0:12:21]** molesta, donde no tapa la mayoría de la información.

**[0:12:26]** Creo que ni corríes.

**[0:12:28]** Ya veo.

**[0:12:29]** Ahí está.

**[0:12:31]** Y nos habíamos quedado con ejercicios pendientes.

**[0:12:35]** Pero no sé si voy a alcanzar a ver los ejercicios uno a uno.

**[0:12:40]** Sin, porque me da miedo que esto igual sea como harta

**[0:12:45]** información.

**[0:12:47]** Entonces, quieren que hagamos uno en conjunto y después pasamos

**[0:12:52]** a la otra clase o prefieren, porque este que ya subí,

**[0:12:55]** ya tiene las respuestas.

**[0:12:56]** Prefieren simplemente hacerlo después con las respuestas

**[0:12:59]** y cada uno en su casita, por ejemplo.

**[0:13:13]** Prefiero hacer un ejercicio ahora o prefiero que continuemos con

**[0:13:17]** la clase y cada uno hace los ejercicios en su caso.

**[0:13:19]** Una gote.

**[0:13:23]** Quisiera coger alguno de esos ejercicios,

**[0:13:25]** que sea el más completo.

**[0:13:27]** El más completo.

**[0:13:29]** Más completo de lo que venga, o sea.

**[0:13:33]** Estoy mostrando la respuesta que te reglean.

**[0:13:34]** Le voy a dar el pausa.

**[0:13:35]** Jajaja.

**[0:13:37]** Eh, calpa y así.

**[0:13:43]** Es más interesante que tú veas que puede ser relevante como va.

**[0:13:49]** Podemos hacer esto, pero no es como tan, tan, tan interesante,

**[0:13:52]** sino que requiere como no llegar y plotear,

**[0:13:56]** sino que requiere hacer algo.

**[0:14:01]** Le voy a sacar la respuesta y la voy a copiar en la cosa de

**[0:14:04]** abajo.

**[0:14:11]** Y listo.

**[0:14:14]** Y la respuesta está ahí abajo.

**[0:14:15]** La respuesta está ahí abajo, no la borre.

**[0:14:18]** El problema 3 dice filtrar los accidentes con más de un

**[0:14:21]** peatón involucrado.

**[0:14:23]** Luego muestra un gráfico de barras que indique cuántos de

**[0:14:25]** esos accidentes ocurrieron en cada condición de iluminación.

**[0:14:29]** Indico cuál es esa columna.

**[0:14:33]** Entonces, ¿qué es lo que tendría que hacer aquí?

**[0:14:53]** ¿Alguna idea?

**[0:14:54]** Bueno, el mismo denunciado me dice que primero me da la

**[0:15:00]** instrucción de filtrar los accidentes con más de un peatón

**[0:15:03]** involucrado.

**[0:15:05]** Entonces, yo tengo mitad de la que se llama accidentes y

**[0:15:11]** debe haber alguna, ah, ahí está.

**[0:15:15]** No, me lo está poniendo.

**[0:15:17]** ¿Por qué tiene?

**[0:15:17]** Ah, debe ser que está copiando el de abajo.

**[0:15:20]** Ya, debe haber alguna columna que me indique cuántos peatones

**[0:15:26]** hay involucrados en cada accidente, ¿no es cierto?

**[0:15:29]** Entonces, si nosotros recordamos la tabla había una

**[0:15:31]** que se llamaba como pedestrian count.

**[0:15:33]** O sea, contador de peatones.

**[0:15:36]** Y como cada fila es un accidente, es el contador

**[0:15:38]** de peatones en el accidente.

**[0:15:39]** Contador de peatones involucrados en el accidente.

**[0:15:42]** Entonces, me voy a...

**[0:15:45]** ¿Me vas a pet count?

**[0:15:48]** Aquí me gustaría que tuviera el...

**[0:15:52]** Por favor, el auto completará aquí.

**[0:15:57]** Pet count.

**[0:16:01]** Y que esto fuera con más de un peatón.

**[0:16:04]** No, yo no.

**[0:16:10]** Sí, guarda.

**[0:16:21]** ¿Se entiende eso?

**[0:16:22]** ¿Se entiende lo que hice ahí?

**[0:16:24]** Habrá de que lo haya hecho mal, que siempre puede pasar.

**[0:16:31]** Me entregó una tabla, entonces tal vez no lo hice mal.

**[0:16:34]** ¿Se entiende por qué hice esto?

**[0:16:38]** Sí, no, quizá.

**[0:16:47]** Alguien no entiende, necesito que me diga.

**[0:16:56]** No te digo nada.

**[0:16:58]** Ya.

**[0:16:59]** Entonces, después me hice luego un maestro en gráfico de barras

**[0:17:02]** que indique cuántos de esos accidentes ocurrieron

**[0:17:04]** en cada condición de iluminación.

**[0:17:07]** Entonces, necesito contar, en esta tabla ya filtrada,

**[0:17:10]** necesito contar cada fila, pero por la cantidad de iluminación.

**[0:17:17]** Y aquí se puede hacer de varias maneras, ¿no es cierto?

**[0:17:20]** Pero hay una operación que me hace esto.

**[0:17:26]** Y no sé si se acuerdan de cuál es esa operación.

**[0:17:31]** Como digo, se puede hacer de otras maneras.

**[0:17:33]** También se puede hacer con un grupa o algo así.

**[0:17:36]** Pero hay una que me sale más natural a mí porque hay una

**[0:17:41]** operación de la cual vimos que hace más o menos esto.

**[0:17:52]** No sé si se acuerdan.

**[0:17:53]** No sé si se acuerdan de otra manera.

**[0:18:10]** Entonces, ahí está mi tabla filtrada

**[0:18:12]** y están todas las condiciones de iluminación.

**[0:18:14]** Y me dicen que yo tengo que hacer un gráfico de barras

**[0:18:20]** que básicamente me indique cuántas veces,

**[0:18:22]** cuántas veces aparece este valor.

**[0:18:25]** Cuántas veces aparece este valor.

**[0:18:27]** Cuántas veces aparece...

**[0:18:29]** No hay más valor.

**[0:18:33]** ¿Cuántas veces aparece ese valor?

**[0:18:35]** ¿Cuántas veces aparece ese otro valor?

**[0:18:37]** ¿Cuántas... No, vamos demostrando una espuela.

**[0:18:39]** Te mostrando la solución.

**[0:18:45]** Entonces, ¿se le ocurre qué operación que vimos?

**[0:18:49]** No me acuerdo si fue la clase de pandas o en la clase...

**[0:18:52]** ¿Verdad si era la clase de pandas?

**[0:18:54]** ¿Qué me haga esto?

**[0:18:55]** ¿Cuántas veces aparece cada valor en la tabla?

**[0:19:01]** ¿Cuántas veces aparece cada valor único?

**[0:19:03]** El value counts.

**[0:19:05]** El value counts, súper.

**[0:19:16]** Entonces, ahí lo tengo, si se dan cuenta.

**[0:19:18]** Entonces, lo que hace esto es contar cuántas filas hay

**[0:19:22]** que tengan esto, el light count en este volar.

**[0:19:26]** Cuántas filas hay que tengan el light count en este otro valor.

**[0:19:29]** Y así, así, así.

**[0:19:31]** Entonces, me dicen que esto tiene que estar en un gráfico de barras.

**[0:19:35]** Entonces, el gráfico de barras necesita...

**[0:19:37]** Uy, necesita algo para el eje X y para el eje Y.

**[0:19:41]** Para el de barras era plt.bar, ¿no es cierto?

**[0:19:44]** Es lo primero que tengo que acordarme, ¿cómo se hacía?

**[0:19:46]** Con plt.bar.

**[0:19:47]** Entonces, necesito el eje X y el eje Y.

**[0:19:50]** Y en el eje X tendrían que ir las categorías, ¿no es cierto?

**[0:19:55]** Entonces, esto me lo voy a guardar en...

**[0:20:00]** No sé, me voy a poner Vista.

**[0:20:03]** Vista igual a eso.

**[0:20:05]** Entonces, vamos a poner Vista.index.

**[0:20:07]** ¿Por qué? Porque necesito las categorías y las categorías

**[0:20:10]** están en el index, aquí.

**[0:20:12]** En el index de esta tablita.

**[0:20:14]** Y luego, necesito el valor para la frecuencia.

**[0:20:17]** Y la frecuencia o cantas veces aparece cada fila

**[0:20:19]** en esta condición.

**[0:20:20]** Entonces, esto sería ya simplemente los valores

**[0:20:23]** que me entrega la tablita Vista.

**[0:20:26]** Sería Vista.value, o Vista.no.

**[0:20:30]** No acuerdo, voy a mirar la solución.

**[0:20:32]** Sería punto values.

**[0:20:34]** Punto values.

**[0:20:36]** ¿Ya? Entonces, ¿por qué aquí el index?

**[0:20:40]** Porque necesito las etiquetas para el eje X.

**[0:20:42]** Y aquí punto values, porque necesito simplemente el valor para el eje.

**[0:20:47]** Bueno, veamos si nos da, porque no puede fallar.

**[0:20:49]** Y ahí estamos.

**[0:20:51]** Y si se dan cuenta, me pasa lo que yo mencioné acá abajo.

**[0:20:55]** Si acuerdan que yo dije que a veces,

**[0:20:57]** como van a estar en horizontal,

**[0:20:59]** se van a chocar entre sí las etiquetas

**[0:21:01]** y no se van a ver bien.

**[0:21:03]** Bueno, aquí está.

**[0:21:04]** Entonces, ¿cómo solucionó esto con el tix

**[0:21:07]** que habíamos mencionado? ¿No es cierto?

**[0:21:09]** Entonces, plt, y quiero ocupar un tix.

**[0:21:11]** En este caso, en el eje X.

**[0:21:13]** Entonces, X tix.

**[0:21:16]** Y voy a poner rotation.

**[0:21:20]** Rotation y le pongo un outer.

**[0:21:22]** Y aquí le puedo poner más,

**[0:21:24]** si quiero que se rote por otro lado.

**[0:21:29]** Ah, y para que no me aparezca este texto aquí.

**[0:21:32]** plt.

**[0:21:38]** Ya.

**[0:21:39]** Y ahí estoy.

**[0:21:40]** Entonces, ahí tengo el gráfico que me fue pedido.

**[0:21:44]** ¿Qué pasa en la solución de abajo?

**[0:21:45]** En la solución de abajo yo lo pongo más bonito

**[0:21:47]** porque le puse título,

**[0:21:49]** bueno, le puse título al gráfico,

**[0:21:51]** le puse título al eje X y al eje Y.

**[0:21:53]** Lo más probable.

**[0:21:54]** Pero la lógica de cómo se crea el gráfico

**[0:21:57]** son estas tres líneas.

**[0:22:00]** La verdad, porque esto también es como

**[0:22:02]** para que se vea mejor.

**[0:22:04]** Entonces, la lógica del gráfico

**[0:22:06]** serían solamente estas tres líneas.

**[0:22:08]** ¿Alguna duda con esas tres líneas?

**[0:22:13]** Cualquiera.

**[0:22:18]** Todo claro.

**[0:22:19]** Todo claro.

**[0:22:20]** Ya supe.

**[0:22:21]** Entonces, no sé si me faltó algo en la solución.

**[0:22:23]** Ya, la solución está exactamente igual

**[0:22:27]** solo que le puse otros nombres

**[0:22:29]** porque no me acordaba,

**[0:22:30]** pero miren, esto es de puro de bonito,

**[0:22:32]** que es la etiqueta al eje X,

**[0:22:34]** la etiqueta al eje Y, el título

**[0:22:36]** y el tix, que si lo alcanzamos a poner.

**[0:22:38]** Ya.

**[0:22:41]** Entonces, ahí tienen,

**[0:22:43]** más o menos, como resolver uno rápido.

**[0:22:46]** Y los otros,

**[0:22:48]** ya tienen la solución aquí

**[0:22:50]** porque esto ya se lo subí,

**[0:22:52]** pero la idea es que si quieren practicar

**[0:22:54]** para soltar la mano

**[0:22:55]** y para acordarse cuando ocupar cada gráfico,

**[0:22:57]** aunque creo que yo menciono,

**[0:22:59]** así como hago un gráfico de dispersión,

**[0:23:01]** hago un gráfico de no sé qué,

**[0:23:03]** hago un histogram.

**[0:23:05]** Igual es importante

**[0:23:07]** como para reforzarlo aprendido.

**[0:23:09]** Ok.

**[0:23:11]** Entonces,

**[0:23:12]** hasta ahí quedamos con A.

**[0:23:14]** Y al final, al final de esto,

**[0:23:16]** que yo recuerdo,

**[0:23:18]** están estos,

**[0:23:20]** la segunda a mí no va a funcionar

**[0:23:22]** porque estoy en un navegador que se llama Brave

**[0:23:24]** y creo que es incompatible con esto,

**[0:23:26]** pero si es que lo abren en Chrome

**[0:23:28]** o en Edge

**[0:23:30]** o creo que hasta en Opera,

**[0:23:32]** demás que le resulta.

**[0:23:34]** Pero esto es una librería,

**[0:23:36]** aparte,

**[0:23:38]** existen como muchas librerías para hacer gráfico.

**[0:23:40]** Estamos ocupando

**[0:23:42]** matplotlib, pero por ejemplo

**[0:23:44]** hay una que se ocupa más porque

**[0:23:46]** de manera más sencilla para hacer gráficos

**[0:23:48]** como más coloridos,

**[0:23:50]** o más complejos que se llama Seaborn,

**[0:23:52]** pero Seaborn también está

**[0:23:54]** construida en base a matplotlib.

**[0:23:56]** Entonces, si es que hago un gráfico en Seaborn

**[0:23:58]** y después pongo alguna lógica de matplotlib

**[0:24:00]** va a funcionar igual,

**[0:24:02]** por si acaso, y ahí está la documentación de sí.

**[0:24:04]** Entonces existen muchas librerías

**[0:24:06]** y algunas pueden ser, por ejemplo, para generar gráficos

**[0:24:08]** un poco más interactivos, porque estos gráficos

**[0:24:10]** son planos, ¿no?

**[0:24:12]** No les puedo hacer zoom o algo así.

**[0:24:14]** Entonces, por ejemplo, hay una librería

**[0:24:16]** que se llama Plotlib, que está así

**[0:24:18]** y me permite tener gráfico interactivo

**[0:24:20]** en donde yo les puedo hacer zoom al gráfico,

**[0:24:22]** le puedo sacar algún pantalla,

**[0:24:24]** etcétera, etcétera.

**[0:24:26]** O puedo poner el mouse y que me muestre algún valor.

**[0:24:30]** Y aquí

**[0:24:32]** deberías también verse un Scatter

**[0:24:34]** o sea, un gráfico de dispersión de puntos por puntos.

**[0:24:36]** Entonces, si yo me meto dentro del punto

**[0:24:38]** me va a decir el valor de X y el valor de Y

**[0:24:40]** pero en este navegador no sé por qué no...

**[0:24:42]** Bueno, en este navegador

**[0:24:44]** no va a funcionar.

**[0:24:46]** Y aquí tienen dos links

**[0:24:48]** aparte

**[0:24:50]** como tips

**[0:24:52]** para cuando se hagan gráficos

**[0:24:54]** y también tipos de gráficos.

**[0:24:56]** Entonces, este mismo BlaBla que yo dije

**[0:24:58]** aquí también existe así.

**[0:25:00]** ¿Cuándo ocupa un gráfico de área?

**[0:25:02]** ¿O para qué me sirve el gráfico de área?

**[0:25:04]** Entonces, aquí como un artículo

**[0:25:06]** que más o menos menciona

**[0:25:08]** para que me sirve cada uno

**[0:25:10]** por si se les olvide

**[0:25:12]** o por si quieren como complementar la info.

**[0:25:14]** ¡Ya!

**[0:25:18]** Eso con

**[0:25:20]** los gráficos.

**[0:25:22]** Creo que termine con este tema.

**[0:25:25]** Entonces, ahora comenzaríamos con

**[0:25:27]** ya la clase de hoy que debería ser este.

**[0:25:29]** ¿Un alzón?

**[0:25:32]** Ya.

**[0:25:34]** Entonces, hoy día

**[0:25:36]** me tocaría regresión.

**[0:25:38]** Ustedes ya tuvieron la clase...

**[0:25:40]** supone que vivía mismo.

**[0:25:42]** Tuvieron la clase de teorías de regresión.

**[0:25:44]** ¿No es cierto?

**[0:25:46]** Entonces, ya entendieron más o menos

**[0:25:48]** la regresión lineal que yo tengo como un BlaBla

**[0:25:50]** explicándola pero

**[0:25:52]** ya la deberían tener más o menos

**[0:25:55]** en la mente, ¿no es cierto?

**[0:25:58]** Entonces, más o menos

**[0:26:00]** ¿Cuándo ocupamos una regresión lineal?

**[0:26:02]** La regresión lineal.

**[0:26:09]** No tenemos datos etiquetados y generalmente

**[0:26:11]** son numéricos.

**[0:26:14]** Me sirve.

**[0:26:16]** Ya super, entonces tenemos la información super fresca.

**[0:26:19]** Ya, sí.

**[0:26:21]** Entonces, me sirve nuestro modelo.

**[0:26:23]** Siempre son modelos predictivos.

**[0:26:25]** Entonces, yo quiero predecir algo.

**[0:26:27]** Entonces, la regresión lineal

**[0:26:29]** es cuando yo quiero

**[0:26:31]** construir una función

**[0:26:33]** que me prediga

**[0:26:35]** la salida de nuevos datos.

**[0:26:37]** Con los que yo voy a ajustar

**[0:26:39]** esta función, tienen que estar

**[0:26:41]** etiquetados. O sea, necesito datos

**[0:26:43]** y una etiqueta, un X y un Y.

**[0:26:45]** Y cuando el Y,

**[0:26:47]** cuando nuestro modelo predictivo va

**[0:26:49]** el Y es un número, ¿ok?

**[0:26:51]** No es una clase, un número.

**[0:26:53]** Ahí tenemos una regresión.

**[0:26:55]** Y en este caso, regresión lineal.

**[0:26:57]** ¿Por qué? Porque

**[0:26:59]** nuestros parámetros son

**[0:27:01]** lineales con respecto al X.

**[0:27:03]** Entonces, nuestro valor,

**[0:27:06]** cuando nuestro valor predicho

**[0:27:08]** es un número continuo, tengo una

**[0:27:10]** regresión. Que es que fuera una clase

**[0:27:12]** y ahí pasa a ser clasífica.

**[0:27:14]** Entonces, la regresión sigue

**[0:27:16]** una formulita que el profesor se las

**[0:27:18]** ha demostrado de ver si parecía

**[0:27:20]** a esto. No es cierto, yo tengo un Y.

**[0:27:22]** Y la formulita en la que

**[0:27:24]** voy a basar de la regresión es que

**[0:27:26]** para cada X, yo lo voy a multiplicar

**[0:27:28]** por un parámetro. Bueno, para cada

**[0:27:30]** columna. Voy a tener

**[0:27:33]** un parámetro distinto.

**[0:27:35]** Y la etiqueta real va a ser

**[0:27:37]** mi predicción más un error.

**[0:27:39]** ¿No es cierto? Porque puede haber

**[0:27:41]** a menos de que sea exacto.

**[0:27:43]** Siempre voy a asumir que hay un

**[0:27:45]** un error.

**[0:27:47]** Para el valor real.

**[0:27:49]** Ahora el valor predicho es simplemente

**[0:27:51]** esto. Tiene el error.

**[0:27:54]** Entonces, ¿cómo definimos una

**[0:27:56]** regresión lineal? Para eso, vamos a

**[0:27:58]** ocupar una librería que se llama

**[0:28:00]** sqlearn.

**[0:28:03]** Y voy por esto.

**[0:28:05]** Y lo bonito que tiene es que me

**[0:28:07]** permite tener

**[0:28:09]** construir este paso

**[0:28:11]** o este modelo que se entrena.

**[0:28:13]** De manera que yo no lo tengo que programar directamente

**[0:28:15]** sino que yo solamente lo tengo que ocupar.

**[0:28:17]** Entonces, tiene un montón

**[0:28:19]** de funcionalidades que yo puedo ocupar.

**[0:28:21]** La primera que vamos a ocupar es para

**[0:28:23]** crearnos un data set de juguete.

**[0:28:25]** Entonces, aquí tiene una función

**[0:28:27]** que se llama make regression

**[0:28:29]** que es para construir datos

**[0:28:31]** muestraos como de una regresión.

**[0:28:33]** Ok?

**[0:28:41]** Entonces, estos datos básicamente

**[0:28:43]** son sacados de una línea

**[0:28:45]** solamente que les pusimos ruido.

**[0:28:47]** Ok?

**[0:28:49]** Entonces, no es que pasen todos por la línea

**[0:28:51]** sino que tienen ahí una dispersión, una

**[0:28:53]** varianza. Ok?

**[0:28:55]** Entonces, con esto me genero mis X

**[0:28:57]** y me genero mis I de juguete.

**[0:28:59]** Con lo que vamos a empezar a prediciar.

**[0:29:01]** Entonces, algo súper

**[0:29:06]** importante cuando yo empiezo a entrenar modelos

**[0:29:08]** además de fijarme que todos los datos sean numéricos

**[0:29:10]** porque si no voy a tener

**[0:29:12]** tengo que empezar a jugar con informatos

**[0:29:14]** es las dimensiones.

**[0:29:16]** Entonces, el X

**[0:29:18]** que son nuestros datos

**[0:29:20]** necesitamos que básicamente

**[0:29:22]** tenga la forma de una tabla, no es cierto?

**[0:29:24]** Con M filas y N columnas

**[0:29:26]** M la cantidad de datos

**[0:29:28]** y N la cantidad como de atributos.

**[0:29:30]** O sea, M la cantidad

**[0:29:32]** de datos y N la cantidad de atributos

**[0:29:34]** que tiene cada dato.

**[0:29:38]** Y el arreglo I, básicamente

**[0:29:40]** cuando nosotros queremos prediciar sólo una

**[0:29:42]** debe tener una sola dimensión.

**[0:29:44]** Aquí digo M filas y una columna

**[0:29:46]** pero en realidad es una dimensión.

**[0:29:48]** Entonces, nuestro

**[0:29:51]** X

**[0:29:53]** tiene

**[0:29:55]** mil filas

**[0:29:57]** y en este caso una sola columna

**[0:29:59]** y esto tiene sentido

**[0:30:01]** porque aquí estoy haciendo que cada

**[0:30:03]** dato se lo tenga un atributo

**[0:30:05]** que sería el valor NX

**[0:30:07]** aquí. Aquí sería el valor NX

**[0:30:09]** y yo quiero predecir su valor en I.

**[0:30:13]** Y, el I

**[0:30:15]** simplemente tiene una sola dimensión

**[0:30:17]** que es lo que yo necesito

**[0:30:19]** para entrenar una regresión lineal

**[0:30:21]** o para ajustar una regresión lineal.

**[0:30:23]** Ahora, ¿cómo ocupo

**[0:30:26]** una regresión lineal? ¿Cómo como modelo

**[0:30:28]** de regresión lineal en esta librería?

**[0:30:30]** Bueno, yo simplemente la voy a importar

**[0:30:32]** porque los modelos ya están ahí

**[0:30:34]** programados. Entonces, yo puedo llegar y ocuparlos.

**[0:30:36]** Entonces, ¿de dónde?

**[0:30:38]** De scikitlearn.linearmodel

**[0:30:40]** porque son modelos lineal

**[0:30:42]** vamos a importar linear regression.

**[0:30:44]** Con eso, ya podemos

**[0:30:46]** ocupar ese

**[0:30:48]** extracto de código.

**[0:30:50]** Y aquí siempre seguimos como el mismo formato

**[0:30:52]** primero yo tengo que crearme una instancia

**[0:30:54]** del model.

**[0:30:56]** Ok, y me la guardo en algún nombre

**[0:30:58]** de alguna variable que yo quiero.

**[0:31:00]** Entonces, el modelo se llama linear regression.

**[0:31:02]** ¿No es cierto? Entonces, me creo

**[0:31:04]** una instancia de ese modelo. Lo llamo.

**[0:31:06]** Ahora, normalmente aquí hay un paréntesis

**[0:31:08]** y ahí yo voy a poder jugar

**[0:31:10]** con los distintos hiperparámetros

**[0:31:12]** que tenga el modelo.

**[0:31:14]** Ok, pero aquí vamos a dejar todo por defecto.

**[0:31:16]** Entonces, por eso

**[0:31:19]** dejamos los paréntesis sin nada.

**[0:31:21]** Ok, ahí se abre como la documentación

**[0:31:23]** y me muestra como algunos hiperparámetros

**[0:31:25]** que tienen el init.

**[0:31:27]** Pero no los vamos a tocar, los vamos a dejar

**[0:31:29]** todo por defecto.

**[0:31:31]** Con eso, ya nos creamos un modelo.

**[0:31:33]** El modelo existe, pero

**[0:31:35]** nos ha ajustado a nuestros datos.

**[0:31:37]** Entonces, si nosotros los ocupáramos para predecir,

**[0:31:39]** nos predeciría cosas que yo espero que sean

**[0:31:41]** muy incorrectas.

**[0:31:43]** Uy, mi mano levantaba, me acabo de dar cuenta.

**[0:31:45]** Perdón.

**[0:31:47]** ¿Qué pasó?

**[0:31:50]** Me han dos personas levantando la mano,

**[0:31:52]** pero no sé cómo ver quiénes son.

**[0:31:55]** Yo tengo una duda con el tema

**[0:31:57]** de ahí cuando calcula

**[0:31:59]** el shape

**[0:32:01]** de I y de I.

**[0:32:03]** Sí, y esperaría obtener

**[0:32:05]** mil

**[0:32:07]** y solamente en mil

**[0:32:09]** y con el shape de I

**[0:32:11]** tenía

**[0:32:13]** una sola columna, no?

**[0:32:15]** Entonces, uno solamente.

**[0:32:17]** Pero ahí sale

**[0:32:20]** con el shape de I sale

**[0:32:22]** de mil.

**[0:32:24]** ¿Por qué me preguntas?

**[0:32:26]** ¿Por qué?

**[0:32:28]** Porque ocupamos esta función

**[0:32:30]** que por defecto ya me lo deja

**[0:32:32]** en las dimensiones que yo necesito

**[0:32:34]** para ocupar estos datos en una regresión linea.

**[0:32:36]** Y como dije, cuando yo estoy ocupando

**[0:32:38]** cómo sería el formato

**[0:32:40]** de los datos para pasárselo a un modelo

**[0:32:42]** de regresión lineal de Scikit-learn

**[0:32:44]** para que funcione, que en el caso

**[0:32:46]** de la matriz X, que serían los datos,

**[0:32:48]** yo necesito M filas y N columnas.

**[0:32:50]** O sea, necesito dos dimensiones.

**[0:32:52]** Y en el caso del I

**[0:32:54]** necesito que sea una sola dimensión.

**[0:32:56]** Entonces, por eso me lo hace.

**[0:33:00]** Pero ahí

**[0:33:03]** no debería ser shape de I

**[0:33:05]** uno solamente. ¿Por qué sale

**[0:33:07]** mil al imprimir?

**[0:33:09]** No, no, no, pero es que el shape

**[0:33:11]** me da

**[0:33:13]** técnicamente

**[0:33:15]** es una sola dimensión porque es

**[0:33:17]** solamente

**[0:33:19]** aquí solamente me muestra

**[0:33:21]** un valor.

**[0:33:23]** Entonces solamente tengo una dimensión.

**[0:33:25]** Pero

**[0:33:28]** imaginemos que la dimensión son el número

**[0:33:30]** de filas. Entonces técnicamente tengo mil filas.

**[0:33:32]** Tengo mil datos.

**[0:33:34]** Por eso es el mil.

**[0:33:39]** ¿Y en el del X?

**[0:33:41]** El del X son dos dimensiones.

**[0:33:43]** Ok?

**[0:33:47]** Tengo mil filas

**[0:33:50]** una columna.

**[0:33:56]** Porque son mil datos y cada uno tiene solamente

**[0:33:58]** una columna.

**[0:34:02]** Ah, ya.

**[0:34:04]** Ya.

**[0:34:08]** Otra manito levanta, pero no me puedo ver el nombre

**[0:34:10]** de la persona, me salí grandos.

**[0:34:12]** Pero la bajo, ya no la tienes levantada.

**[0:34:19]** Ah, buchi, ya.

**[0:34:21]** Ok, perdón.

**[0:34:23]** La puedes volver a levantar y me quieras preguntar.

**[0:34:25]** Lo siento, no me cuento.

**[0:34:27]** Eh, donde me quedes?

**[0:34:29]** Precisamente.

**[0:34:33]** Yo creo mi instancia de modelo

**[0:34:35]** de regresión línea.

**[0:34:37]** Como dije, cuando yo lo creo

**[0:34:39]** el modelo no está ajustado,

**[0:34:41]** no está entrenado.

**[0:34:43]** Puede estar inicializado con valores por defecto.

**[0:34:45]** Entonces yo puedo llegar

**[0:34:47]** y ocuparlo. Puedo llegar y predecir

**[0:34:49]** datos, no cierto.

**[0:34:51]** Pero, lo que me va a pasar

**[0:34:53]** es que, lo más probable

**[0:34:55]** es que la predicción sea muy alejada

**[0:34:57]** del valor que yo quiero, porque no está

**[0:34:59]** ajustado, no está entrenado.

**[0:35:01]** Entonces, ¿cómo lo entreno?

**[0:35:03]** ¿Cómo lo ajusto a los datos?

**[0:35:05]** Bueno, para entrenar el modelo,

**[0:35:07]** yo tengo que tener mi instancia de modelo

**[0:35:09]** que lo guarde en esta variable.

**[0:35:11]** Entonces pongo el nombre de la variable

**[0:35:13]** y pongo punto fit. Y esa sería la

**[0:35:15]** función que

**[0:35:17]** está dada para ajustar

**[0:35:19]** este modelo. Y por eso, yo le tengo que pasar

**[0:35:21]** mis datos de entrenamiento

**[0:35:23]** y también la etiqueta.

**[0:35:25]** En este caso, no dividí nada

**[0:35:27]** de mi conjunto, así que vamos a llegar

**[0:35:29]** y vamos a pasarle de X y el Y directamente.

**[0:35:31]** Porque es un ejemplo de juguete.

**[0:35:33]** Porque estamos empezando recién.

**[0:35:35]** Entonces, yo le paso mi X y mi.

**[0:35:38]** Y solo con eso, mi modelo

**[0:35:40]** ya se ajustó a los datos.

**[0:35:42]** Ok. Ya calculó

**[0:35:44]** valores para

**[0:35:46]** los parámetros, tal que

**[0:35:48]** yo disminuyo el error.

**[0:35:50]** Es decir, en la clase deberían haber

**[0:35:52]** más o menos visto el concepto de cómo se entrena

**[0:35:54]** esto. ¿No es cierto? Yo estoy disminuyendo el error.

**[0:35:56]** Ya.

**[0:35:59]** Entonces, ahora que ya tengo

**[0:36:01]** una regresión lineal, entrenada

**[0:36:03]** con los datos, yo puedo llegar

**[0:36:05]** y hacer alguna predicción.

**[0:36:07]** Entonces, lo que voy a hacer, aquí hice aleatorios

**[0:36:09]** pero en realidad no son aleatorios.

**[0:36:11]** Vamos a crear datos que estén

**[0:36:13]** en el rango en que se mueven

**[0:36:15]** mis datos normales, o sea entre menos

**[0:36:19]** me los voy a crear con un Arrange.

**[0:36:21]** Está funcionando en Amp y que habíamos visto

**[0:36:23]** entonces me va a crear menos 3, menos todo, menos

**[0:36:25]** y así. Y ese va a

**[0:36:27]** ser mi test.

**[0:36:29]** Por realidad no es un test

**[0:36:31]** porque son valores de juguete.

**[0:36:33]** Y son simplemente menos 3,

**[0:36:35]** menos 2, menos 1, 0 y así.

**[0:36:37]** Pero me los voy a crear para predecir

**[0:36:40]** algo nuevo. Entonces, para hacer

**[0:36:42]** predicciones, tengo que recordarme

**[0:36:44]** que esto necesita una sola dimensión

**[0:36:46]** y que el X necesita dos dimensiones,

**[0:36:48]** etcétera, etcétera. Entonces, para que

**[0:36:50]** el test aquí

**[0:36:52]** tiene solamente una dimensión.

**[0:36:54]** Entonces, para que no me rete

**[0:36:56]** el código de que hay algo incompatible

**[0:36:58]** yo tengo que asegurarme que tenga

**[0:37:00]** dos dimensiones. Entonces, por eso yo le voy a hacer

**[0:37:02]** un reshape. Y cuando hago

**[0:37:04]** menos 1, significa

**[0:37:06]** que mantenga

**[0:37:08]** la dimensión que calza

**[0:37:10]** aquí con menos 1. Y en el otro le voy

**[0:37:12]** a explicitar que solamente

**[0:37:14]** se vuelva dimensión 1

**[0:37:16]** las columnas.

**[0:37:20]** Entonces, ahí se transforma en 6,1.

**[0:37:22]** Paso de 6 de una sola dimensión

**[0:37:24]** a dos dimensiones.

**[0:37:26]** Entonces, ahora tengo 6 valores de X

**[0:37:28]** y se los voy a pasar al modelo

**[0:37:30]** para que haga una predicción. El modelo ya se

**[0:37:32]** entrenó, ok? Ya no lo ajusto más.

**[0:37:34]** Entonces, ahora lo que voy a hacer

**[0:37:36]** para predecir es ocupar otra vez

**[0:37:38]** esta variable que tiene mi modelo

**[0:37:40]** que ya se ajustó,

**[0:37:43]** punto predict. Y esa es

**[0:37:45]** la manera para hacer predicciones.

**[0:37:47]** ¿Qué hace el predic? Que yo le paso estos datos

**[0:37:49]** y los parámetros ya no se ajustan.

**[0:37:51]** Con el predic, los parámetros no se ajustan.

**[0:37:53]** Con el fit,

**[0:37:55]** con el fit, los parámetros

**[0:37:57]** sí se ajustan, calculo el error,

**[0:37:59]** calculo los gradientes y después

**[0:38:01]** ajusto estos parámetros que están aquí

**[0:38:03]** en la formulita, que serían estos.

**[0:38:06]** Esto es lo que ajusto.

**[0:38:08]** Cuando hago predic, no ajusto

**[0:38:10]** eso. Entonces, simplemente ocupo

**[0:38:12]** la fórmula interna que el modelo ya calcula.

**[0:38:14]** Entonces,

**[0:38:17]** vamos a predecir

**[0:38:19]** y este IPred me lo voy a

**[0:38:21]** guardar.

**[0:38:24]** Entonces, ahora voy a mostrar

**[0:38:27]** los datos originales.

**[0:38:29]** Voy a hacer una dispersión, un scatter

**[0:38:31]** con X y le voy a poner un alpha

**[0:38:33]** y también voy a

**[0:38:35]** plotear los datos

**[0:38:37]** de test que tenía con el valor predicho

**[0:38:39]** y también los voy a mostrar con un puntito.

**[0:38:41]** Quiero plotar una línea y también

**[0:38:43]** quiero plotarlos como un puntito.

**[0:38:46]** Se entiende, necesariamente, ya.

**[0:38:48]** Esto es lo que hago. Entonces, cada puntito

**[0:38:50]** lo estoy haciendo con forma de estrella

**[0:38:52]** y eso lo indique en este marker.

**[0:38:54]** El marker es la formita

**[0:38:56]** del puntito y aquí está el color

**[0:38:58]** que ya lo habíamos visto, que lo puedes especificar

**[0:39:00]** y ese

**[0:39:02]** si no me recuerdo era el tamaño

**[0:39:04]** pero no estoy 100% seguro.

**[0:39:08]** Entonces, con el scatter, con este scatter

**[0:39:10]** estoy haciendo estas marquitas

**[0:39:12]** que serían las estrellitas, los puntitos

**[0:39:14]** y para que se vea la línea

**[0:39:16]** estoy haciendo el plot

**[0:39:18]** con exactamente los mismos datos si se han puesto

**[0:39:20]** test X, test X y pred

**[0:39:22]** y pred

**[0:39:25]** y como yo sé cómo funciona la regresión lineal

**[0:39:27]** cuando yo dibujo una regresión lineal

**[0:39:29]** es una línea, lo que va a llegar

**[0:39:31]** la regresión lineal

**[0:39:33]** visualmente

**[0:39:35]** es que va a generar una línea

**[0:39:37]** que disminuye

**[0:39:39]** el error de reconstrucción entre los datos

**[0:39:41]** entonces básicamente va a ser una línea

**[0:39:43]** que pase como por la mitad

**[0:39:45]** de todo este rango de los datos

**[0:39:47]** entonces va a tomar el rango de acá

**[0:39:49]** y el rango de acá, así que tenemos

**[0:39:51]** la misma cantidad de datos, entonces voy a encontrar una línea

**[0:39:53]** que pase como por al medio de todo

**[0:39:55]** porque esa es la mejor predicción

**[0:39:57]** esa es la predicción que disminuye el error

**[0:39:59]** para todo esto

**[0:40:01]** mi línea

**[0:40:04]** ahora, cuando yo ya entren esto

**[0:40:06]** estos parámetros existen

**[0:40:08]** y tienen un valor fijo

**[0:40:10]** yo los puedo mirar, los puedo obtener

**[0:40:12]** entonces como esto es una línea

**[0:40:14]** o una recta

**[0:40:16]** nosotros como la dibujamos, como la graficamos

**[0:40:18]** tienen una pendiente

**[0:40:20]** y

**[0:40:22]** como se llama

**[0:40:24]** y un coeficiente de intersección creo que se llama

**[0:40:26]** entonces ahí tengo

**[0:40:28]** mis dos valores

**[0:40:30]** que no me acuerdo si siguen siendo los mismos de aquí

**[0:40:32]** entonces ahí tengo

**[0:40:35]** mi pendiente y mi B

**[0:40:38]** y en este caso

**[0:40:40]** es este B

**[0:40:42]** sería este theta sub 0

**[0:40:44]** que es el theta como

**[0:40:46]** el

**[0:40:48]** nosotros lo llamamos bayas a veces

**[0:40:50]** pero es el theta que está por defecto

**[0:40:52]** que no se multiplica por ninguna de las columnas

**[0:40:54]** y la pendiente sería el theta sub 1

**[0:40:56]** ok

**[0:40:58]** que sería este M

**[0:41:00]** que se está multiplicando por el

**[0:41:02]** el primer atributo de cada

**[0:41:04]** de cada dato, que sería el único

**[0:41:06]** porque solamente tenemos un atributo por dato

**[0:41:09]** ok, y entonces esto lo puedo hacer

**[0:41:11]** una función que me retorne eso

**[0:41:13]** una función que recibo en X

**[0:41:15]** recibo en M, recibo en B

**[0:41:17]** donde M es mi pendiente y B este es

**[0:41:19]** el coeficiente de intersección

**[0:41:21]** y que me devuelva X por

**[0:41:23]** M más B

**[0:41:25]** ok, entonces después puedo ocupar

**[0:41:29]** esa función

**[0:41:31]** y le puedo pasar mi test X

**[0:41:33]** le puedo pasar como M

**[0:41:35]** el coeficiente

**[0:41:37]** y como B

**[0:41:39]** el intercept

**[0:41:41]** que dijimos que son los valores que tiene por dentro

**[0:41:43]** y puedo plotar eso mismo

**[0:41:46]** y me va a dar lo mismo que tenía

**[0:41:49]** ok

**[0:41:51]** porque técnicamente lo que tiene esta regresión por dentro

**[0:41:53]** es calcular

**[0:41:55]** esta fórmula, esto es lo que está haciendo por dentro

**[0:41:57]** ok, tiene esa fórmula

**[0:42:00]** y cuál es el M

**[0:42:02]** el coefe, y cuál es el B

**[0:42:04]** el intercept

**[0:42:06]** lo aterrizamos porque uno puede llegar a ocuparla

**[0:42:08]** y decir que estará pasando por dentro

**[0:42:10]** bueno, simplemente está ajustándose

**[0:42:12]** disminuyendo el error y calculando estos dos valores

**[0:42:14]** ahora si yo tuviera más atributos

**[0:42:16]** tendría

**[0:42:18]** muchos más valores aquí en el coeficiente

**[0:42:20]** tendría 1 por

**[0:42:22]** cada atributo

**[0:42:24]** ¿cierto? siendo

**[0:42:27]** la fórmulita aquí

**[0:42:29]** yo tengo un parámetro

**[0:42:31]** un teta sub y

**[0:42:33]** por cada atributo

**[0:42:35]** que tenga mi dato

**[0:42:37]** pero si tengo 5 columnas voy a tener

**[0:42:39]** 5 coefe

**[0:42:45]** ya, entonces ahí es

**[0:42:47]** la forma más fácil de inicializar este modelo

**[0:42:49]** entrenarlo, predecir

**[0:42:51]** ocuparlo en general

**[0:42:53]** ahora, ¿cómo evalúo? que también lo hace

**[0:42:55]** bueno

**[0:42:57]** dependiendo del tipo de problema también

**[0:42:59]** cuando ya se complejizan hay distintas métricas

**[0:43:01]** de evaluación pero unas muy ocupadas

**[0:43:03]** en especial en regresión es el

**[0:43:05]** R cuadrado, el R cuadrado score

**[0:43:07]** que básicamente

**[0:43:09]** ahí está la fórmulita

**[0:43:11]** la fuente de Wikipedia y aquí está mi fórmulita

**[0:43:13]** del error cuadrático medio

**[0:43:15]** de la fuente de Wikipedia

**[0:43:17]** entonces estas son fórmulitas ya existen

**[0:43:19]** yo las podría programar porque simplemente

**[0:43:21]** calcular aquí estoy calculando

**[0:43:23]** la diferencia entre el valor real

**[0:43:25]** y el valor predicho ¿no cierto?

**[0:43:27]** y solo estoy elevando al cuadrado

**[0:43:29]** y eso me lo quedo y así

**[0:43:31]** puedo seguir esa fórmula y programarla

**[0:43:33]** pero esto ya está programado en scikit-learn

**[0:43:35]** ya existen, ¿ok? desde scikit-learn.metrics

**[0:43:37]** yo puedo

**[0:43:39]** instanciar estas dos

**[0:43:41]** que la fórmula ya existe

**[0:43:43]** o que sucede

**[0:43:45]** si, hola

**[0:43:47]** me quedo una duda respecto al plot anterior

**[0:43:49]** ¿podríamos revisar por favor?

**[0:43:51]** la línea maría

**[0:43:53]** y

**[0:43:55]** la estrellita de maría

**[0:43:57]** en que se diferenciaban al final

**[0:43:59]** con el plot anterior

**[0:44:01]** ah, ok

**[0:44:04]** lo que pasa es que aquí

**[0:44:07]** en este plot

**[0:44:09]** yo estoy ocupando este IPRED

**[0:44:11]** es que no les cambia el nombre

**[0:44:13]** de la construcción

**[0:44:15]** este IPRED yo lo saqué

**[0:44:17]** prediciendo con la función predict

**[0:44:19]** de mi regresión lineal

**[0:44:21]** yo tome mi regresión lineal y apliqué el predict

**[0:44:23]** el amarillo

**[0:44:25]** en cambio lo que hice es

**[0:44:27]** crear una función

**[0:44:29]** que tiene la fórmula

**[0:44:31]** por defecto que yo debería pensar

**[0:44:33]** que tiene la regresión lineal

**[0:44:35]** me creo una función que calcula esta fórmula

**[0:44:37]** esta es la fórmula literal

**[0:44:39]** le hicimos a mano

**[0:44:41]** lo que estoy haciendo es generarme este nuevo IPRED

**[0:44:43]** pasándole los datos de test

**[0:44:45]** y este M y este B

**[0:44:47]** o sea, esto yo no lo estoy haciendo

**[0:44:49]** con la regresión lineal

**[0:44:51]** lo estoy haciendo yo a manito

**[0:44:53]** con los parámetros de la regresión lineal

**[0:44:55]** exacto, con el mejor ajuste

**[0:44:57]** y para las contantes

**[0:44:59]** y los valores

**[0:45:01]** para la estrellita los da por defecto el plot

**[0:45:03]** cierto

**[0:45:05]** ahí veo que son para los números

**[0:45:07]** del eje de X

**[0:45:10]** es que el eje de X

**[0:45:12]** está en el test X

**[0:45:14]** el test X son puro número 20

**[0:45:16]** son menos 3, menos 2

**[0:45:19]** ahí está

**[0:45:21]** menos 3, menos 2, menos 1, 0, 0, 1

**[0:45:26]** qué raro que no está hasta el 2

**[0:45:30]** qué raro

**[0:45:32]** pero sí, y esto lo habíamos construido

**[0:45:34]** con

**[0:45:36]** mi arrange

**[0:45:38]** aquí lo construí

**[0:45:40]** que dije eran aleatorias pero realmente no son aleatorias

**[0:45:42]** porque toma

**[0:45:44]** más o menos el rango de los datos

**[0:45:46]** y me crea puntos equidistantes

**[0:45:48]** entre los rangos

**[0:45:50]** eso no

**[0:45:55]** gracias

**[0:45:58]** nos consulta ahí eso mismo

**[0:46:00]** del arrange

**[0:46:02]** aparte no lo han entendido bien

**[0:46:04]** qué hacía

**[0:46:07]** el arrange

**[0:46:09]** el arrange en sí

**[0:46:11]** o otra cosa

**[0:46:13]** el arrange en sí

**[0:46:15]** sí, ahí donde sale

**[0:46:17]** el arrange

**[0:46:19]** general como valor intermedial

**[0:46:21]** esperame

**[0:46:23]** es que estoy buscando

**[0:46:34]** no lo vimos

**[0:46:36]** debimos haberlo visto aquí

**[0:46:48]** me acuerdo que lo vimos en

**[0:46:50]** en la

**[0:46:52]** daré puro mintiendo

**[0:46:56]** acá está, ahí está

**[0:46:58]** perdón

**[0:47:00]** ahí va, vimos el arrange

**[0:47:02]** que tiene 3

**[0:47:04]** funciona como el 4

**[0:47:06]** funciona como el range que ocupamos

**[0:47:08]** en el 4, tiene 3 parámetros

**[0:47:10]** A, B y C

**[0:47:12]** y crea un arreglo conteniendo los números

**[0:47:14]** entre A y B-1 con un aumento de C

**[0:47:16]** ahí sí

**[0:47:20]** ahí salía

**[0:47:25]** arrojado un 6, me acuerdo

**[0:47:27]** porque

**[0:47:29]** me tira 6 valores

**[0:47:31]** me arroja

**[0:47:33]** el 6

**[0:47:36]** es el shape

**[0:47:38]** no me está mostrando

**[0:47:40]** cada valor, sino que yo le pedí el shape

**[0:47:42]** para saber cuántos valores eran

**[0:47:45]** y lo del reshape

**[0:47:47]** de...

**[0:47:49]** esto, allá

**[0:47:51]** lo que pasa es que

**[0:47:53]** esto lo quiero usar como

**[0:47:55]** datos para

**[0:47:57]** probar, se lo quiero pasar a la regresión lineal

**[0:47:59]** para que prediga

**[0:48:01]** dado estos X, cuál sería la etiqueta

**[0:48:03]** entonces como vimos antes

**[0:48:05]** cuando yo le paso a la regresión lineal

**[0:48:07]** los X, tienen que estar

**[0:48:09]** con M

**[0:48:11]** filas, tienen que tener dos dimensiones

**[0:48:13]** filas, columnas

**[0:48:15]** entonces si te das cuenta cuando yo le saco el shape aquí al X

**[0:48:17]** me da solamente una dimensión

**[0:48:19]** que son las filas

**[0:48:21]** entonces lo que yo estoy haciendo con el reshape

**[0:48:23]** es forzarlo a que tengas dos dimensiones explícitas

**[0:48:25]** filas y columnas

**[0:48:27]** ¿por qué el menos 1,1?

**[0:48:31]** el menos 1

**[0:48:33]** es para que mantenga

**[0:48:35]** la...

**[0:48:37]** la dimensión que ya contenía

**[0:48:39]** aquí, en este lugar

**[0:48:41]** y el 1 es forzarlo a que

**[0:48:43]** explícite una columna

**[0:48:47]** entonces, menos 1 es simplemente que mantenga

**[0:48:49]** el 6

**[0:48:52]** que yo no quiero sacarlo aquí

**[0:48:54]** si es que esto fuera 8

**[0:48:56]** el menos 1 también me va a funcionar, no tengo que poner yo

**[0:48:58]** 6, explícito

**[0:49:00]** porque si esto le pido más valores

**[0:49:02]** después de este 6 va a estar malo

**[0:49:04]** entonces prefiero ponerle menos 1

**[0:49:06]** para que sea dinámico

**[0:49:09]** y el 1 es que de una columna

**[0:49:11]** el 1 es porque solamente es una columna

**[0:49:13]** si fueran más columnas

**[0:49:15]** yo debería indicar, pero aquí yo sé

**[0:49:17]** explícitamente que es solo 1

**[0:49:20]** ahí ya

**[0:49:22]** ya

**[0:49:28]** las muertes de evaluación

**[0:49:30]** estaba por acá, no es cierto?

**[0:49:32]** bueno, para evaluar

**[0:49:34]** luego de entrenar yo quiero evaluarnos

**[0:49:36]** porque normalmente yo tengo mis conjuntos de entrenamiento

**[0:49:38]** y mi conjunto de

**[0:49:40]** validación o mi conjunto de tests

**[0:49:42]** y quiero ver que también lo hace

**[0:49:44]** en datos que el modelo

**[0:49:46]** no ocupó para entrenarse

**[0:49:48]** y también quiero de alguna manera

**[0:49:50]** cuantificar el error

**[0:49:52]** quiero ponerle un valor a ese error

**[0:49:54]** para después comparar modelos, cual lo hace mejor

**[0:49:56]** entonces las métricas de evaluación me ayudan

**[0:49:58]** definen una regla para cuantificar

**[0:50:00]** este error

**[0:50:02]** y en caso de la regresión igual es fácil

**[0:50:04]** porque tenemos números continuos

**[0:50:06]** de entrenar, tienen una espada, etc

**[0:50:08]** entonces tienen este tipo

**[0:50:10]** en distintas métricas dependiendo del problema

**[0:50:12]** y unas muy utilizadas son el error

**[0:50:14]** cuadrático medio, pero deben conocer que existen

**[0:50:16]** muchas más, por ejemplo el

**[0:50:18]** también existe el

**[0:50:20]** el MAE

**[0:50:22]** era mean absolute error

**[0:50:24]** el error

**[0:50:27]** medio absoluto

**[0:50:29]** algo así, el MAE

**[0:50:31]** también, como el mc, solamente que el MAE

**[0:50:33]** no está al cuadrado, sino que tiene el valor absoluto

**[0:50:35]** y también está el R cuadrado

**[0:50:37]** y el R cuadrado

**[0:50:39]** me dice cuánto de la varianza

**[0:50:41]** yo puedo explicar

**[0:50:43]** con este modelo cuánto de la varianza de los datos

**[0:50:45]** yo puedo explicar, entonces espero el

**[0:50:47]** R cuadrado está en 0 y 1

**[0:50:49]** y entre más cercano a uno mejor

**[0:50:51]** ok, entre más cercano a uno

**[0:50:53]** puedo explicar toda la

**[0:50:55]** la varianza de los datos

**[0:50:57]** estoy en 0.5 es lo mismo que

**[0:50:59]** básicamente predici... de la media

**[0:51:01]** por ejemplo

**[0:51:03]** y el mean square error

**[0:51:05]** me mide el cuánto

**[0:51:07]** yo me estoy equivocando con respecto

**[0:51:09]** aquí está mi valor predicho

**[0:51:11]** y mi valor real, entonces cuánto me estoy equivocando

**[0:51:13]** en promedio

**[0:51:15]** eh...

**[0:51:17]** básicamente, cuánto me estoy equivocando en promedio

**[0:51:19]** en la predicción

**[0:51:22]** entonces el mc no es que tengo un rango

**[0:51:24]** no es cierto, no es como el R cuadrado

**[0:51:26]** el R cuadrado tiene un rango, el mc no tiene un rango

**[0:51:28]** entonces el mc de solito

**[0:51:30]** me puede decir más o menos cuánto

**[0:51:32]** espero equivocarme

**[0:51:34]** pero yo tendría que tener

**[0:51:36]** conocimiento del problema para saber si ese valor

**[0:51:38]** es aceptable o no

**[0:51:40]** pero me sirve para comparar modelos

**[0:51:42]** porque ya cuando tengo dos

**[0:51:44]** R cuadrados medio ahí puedo saber

**[0:51:46]** cuál es menor, no es cierto? porque menor

**[0:51:48]** es mejor, porque esto te mide

**[0:51:50]** cuánto me equivoco, entonces entre más

**[0:51:52]** bajo me estoy equivocando menos

**[0:51:54]** no es cierto

**[0:51:56]** entonces como dije

**[0:52:00]** estas son fórmulas, yo podría llegar y programarlas

**[0:52:02]** pero no es necesario porque en scikit-learn

**[0:52:04]** ya están y yo simplemente las

**[0:52:06]** las puedo instanciar y ocupar

**[0:52:08]** son funciones

**[0:52:10]** entonces como indicó que las quiero ocupar

**[0:52:12]** yo quiero decir dónde están

**[0:52:14]** entonces las importo, desde

**[0:52:16]** sclearn.metrics, bastante intuitivo

**[0:52:18]** y las importo con el nombre

**[0:52:20]** mean, square, error o el

**[0:52:22]** ilr cuadrado, si es que yo quisiera

**[0:52:24]** más métricas, me puedo meter a la

**[0:52:26]** documentación de scikit-learn

**[0:52:28]** y buscar si es que hay alguna que yo necesite

**[0:52:30]** un tipo de problema, entonces

**[0:52:33]** para evaluar, yo simplemente necesito

**[0:52:35]** las etiquetas reales

**[0:52:37]** y etiquetas predichas, ok?

**[0:52:39]** entonces para evaluar

**[0:52:42]** necesito tener como dije los valores reales

**[0:52:44]** y ese y existe

**[0:52:46]** ah si

**[0:52:48]** entonces para

**[0:52:50]** compararlo aquí lo voy a hacer

**[0:52:52]** con los datos de entrenamiento

**[0:52:54]** esto técnicamente no se hace

**[0:52:56]** te voy a hacerlo con datos de test

**[0:52:58]** pero solamente por el ejemplo porque son datos de fuert

**[0:53:00]** entonces el y predicho

**[0:53:02]** voy a predecir directamente de mi

**[0:53:04]** regresión lineal, le voy a pasar el

**[0:53:06]** conjunto de datos que ocupamos para ajustar

**[0:53:08]** la que sería el x y luego

**[0:53:10]** voy a comparar el y

**[0:53:12]** que son las etiquetas reales con el

**[0:53:14]** y predicho que es la predicción

**[0:53:16]** que hizo mi regresión lineal y voy a

**[0:53:18]** ocupar las dos métricas, el mean

**[0:53:20]** square error y el ilr cuadrado

**[0:53:26]** ok?

**[0:53:29]** el ilr cuadrado me da bastante alto

**[0:53:34]** y el error cuadrático medio también

**[0:53:36]** bastante alto, entonces como el error

**[0:53:38]** cuadrático medio nos está ayudando tanto

**[0:53:40]** aquí a menos de que yo conozca

**[0:53:42]** la escala de los datos

**[0:53:44]** y conozca más o menos

**[0:53:46]** la naturaleza para saber

**[0:53:48]** por eso, cuánto es permitido que yo me equivoque

**[0:53:50]** porque 98 son a súper alto

**[0:53:52]** pero igual

**[0:53:54]** esto va entre menos

**[0:53:57]** 250

**[0:53:59]** y 250

**[0:54:01]** ok?

**[0:54:03]** entonces ahí tengo que ver

**[0:54:06]** efectivamente si eso me sirve o no

**[0:54:08]** o si necesito bajar

**[0:54:10]** ok?

**[0:54:14]** y aquí tenía un ejemplo y después

**[0:54:16]** tenía variación cruzada

**[0:54:18]** entonces aquí tenemos un ejemplo

**[0:54:20]** con un dataset real

**[0:54:23]** que se llama california housing

**[0:54:25]** y básicamente tiene los

**[0:54:27]** datos de viviendas

**[0:54:33]** en cada distrito

**[0:54:35]** y tiene como distintas variables

**[0:54:37]** que te describen la casa

**[0:54:39]** entonces, bueno, el valor de las viviendas

**[0:54:41]** en general, por ejemplo

**[0:54:43]** medias de años de antigüedad

**[0:54:45]** de las viviendas, número

**[0:54:47]** promedio de habitaciones por hogar

**[0:54:49]** entonces como quieres predecir cuánto vale

**[0:54:51]** una casa en el sector

**[0:54:53]** entonces promedio de dormitorios por hogar

**[0:54:55]** población total

**[0:54:57]** número promedio de habitantes por hogar

**[0:54:59]** la ubicación

**[0:55:01]** y después tiene la variable que queremos

**[0:55:03]** predecir que es el valor

**[0:55:05]** promedio de las viviendas del distrito

**[0:55:07]** ok? esta va a ser nuestra variable

**[0:55:09]** objetivo

**[0:55:12]** entonces vamos a cargar el dataset

**[0:55:14]** que está también en SecretLearn

**[0:55:17]** que maravilloso

**[0:55:19]** y aquí estoy cargando una función

**[0:55:21]** que vamos a ocupar arto

**[0:55:23]** que se llama trainTestSplit

**[0:55:25]** que es una función que me divide

**[0:55:27]** los datos

**[0:55:29]** de manera automática para que yo no tenga que hacerlo

**[0:55:31]** a manito

**[0:55:33]** y aquí hay como un sneak peek

**[0:55:35]** de la tabla del dataset

**[0:55:37]** entonces aquí tengo las distintas columnas que vimos

**[0:55:39]** y esta

**[0:55:41]** la última columna sería

**[0:55:43]** el valor que nosotros queremos predecir

**[0:55:45]** que es el valor medio

**[0:55:47]** de las casas del distrito

**[0:55:51]** yo podría sacarle correlaciones

**[0:55:53]** esto podría ser distintas cosas

**[0:55:55]** podría ser una análisis que quisiera

**[0:55:57]** aquí estoy ocupando ciborn

**[0:56:01]** por el caso

**[0:56:03]** podría hacer un hipmap

**[0:56:05]** aquí estoy haciendo un hipmap de las correlaciones

**[0:56:08]** entonces por ejemplo

**[0:56:10]** veo, esta es mi variable objetivo

**[0:56:12]** ¿recuerdan? midhouse value

**[0:56:14]** entonces veo que por ejemplo

**[0:56:17]** mi variable objetivo está bastante

**[0:56:19]** correlacionada con

**[0:56:21]** esto era

**[0:56:23]** el sueldo promedio de las personas del lugar

**[0:56:25]** ingreso medio de los hogares

**[0:56:27]** en decenas de millones de dólares

**[0:56:30]** entonces está bastante el precio de las casas

**[0:56:32]** en el distrito

**[0:56:34]** estaba bastante

**[0:56:36]** fuertemente correlacionado

**[0:56:38]** con la cantidad

**[0:56:40]** de dinero que ganan las personas

**[0:56:42]** en ese distrito

**[0:56:44]** por casa

**[0:56:46]** y también tiene un poquito de correlación

**[0:56:48]** en especial estas dos variables

**[0:56:50]** pero estas son correlaciones lineales

**[0:56:52]** recordemos y es de aparez

**[0:56:54]** lineales de aparez

**[0:56:56]** y veo como correlaciones entre

**[0:56:58]** mi variable objetivo y las demás

**[0:57:00]** y podría haber correlaciones entre las mismas variables

**[0:57:02]** para ver si alguna variable es bastante

**[0:57:04]** inútil por ejemplo

**[0:57:06]** y puedo hacer aquí

**[0:57:09]** distinto analisis de lo que quiera

**[0:57:11]** pero aquí no lo vamos a aceptar

**[0:57:13]** la verdad no le voy a poner

**[0:57:15]** tanto blablabla

**[0:57:17]** por el tiempo

**[0:57:20]** entonces aquí tengo mis columnas

**[0:57:22]** normalmente yo hago el punto columns

**[0:57:24]** para copiar y pegar esto

**[0:57:26]** cuando hago la división

**[0:57:28]** de los datos

**[0:57:30]** entonces el X

**[0:57:33]** van a ser

**[0:57:35]** en mi DF sería mi dataset

**[0:57:37]** todas estas columnas

**[0:57:39]** a excepción de la última

**[0:57:41]** porque la última la queremos usar como el valor

**[0:57:43]** que queremos predecir

**[0:57:46]** y el I va a ser solamente

**[0:57:48]** esa columna

**[0:57:51]** entonces con eso ya hago

**[0:57:53]** la división y explícito

**[0:57:55]** cuáles son mis datos

**[0:57:57]** y cuáles son mis etiquetas

**[0:57:59]** X datos y etiquetas

**[0:58:01]** y con el train test split

**[0:58:04]** podemos hacer la división

**[0:58:06]** como se hacen las buenas prácticas

**[0:58:08]** que yo debería tener un conjunto

**[0:58:10]** de entrenamiento

**[0:58:12]** un conjunto de test

**[0:58:14]** y un conjunto de validación

**[0:58:16]** si es que quisiera hacer ajuste y parámetro

**[0:58:18]** u otras cosas

**[0:58:21]** entonces el train test split lo que hace

**[0:58:23]** es que me divide los datos

**[0:58:25]** de manera ordenada y lo único que tengo que pasar

**[0:58:27]** son los datos originales

**[0:58:29]** y la cantidad

**[0:58:31]** o el tamaño que yo quiero

**[0:58:33]** para el...

**[0:58:35]** bueno si la proporcionalidad de los datos

**[0:58:37]** entonces yo quiero que...

**[0:58:39]** consulta

**[0:58:41]** va a ir a separar en

**[0:58:43]** datos de entrenamiento y datos de test

**[0:58:45]** cierto? si la primera si

**[0:58:47]** ya

**[0:58:49]** tengo una

**[0:58:51]** una consulta

**[0:58:54]** porque estuvo viendo

**[0:58:56]** que además

**[0:58:58]** del test y el entrenamiento y la devaliación

**[0:59:00]** si

**[0:59:03]** el devaliación

**[0:59:05]** fue una parte del

**[0:59:07]** entrenamiento, del test

**[0:59:09]** o hay que formarlo a parte igual

**[0:59:11]** eso depende

**[0:59:13]** de mi problema y de la cantidad de datos que yo

**[0:59:15]** tenga si es que tengo pocos

**[0:59:17]** datos

**[0:59:19]** entonces no me sale muy a cuenta tener

**[0:59:21]** un conjunto de validación

**[0:59:23]** porque estoy perdiendo esos datos

**[0:59:25]** para entrenar entonces puedo hacer

**[0:59:27]** validación cruzada

**[0:59:30]** y eso es

**[0:59:32]** entrenar varias veces

**[0:59:34]** variando el conjunto de validación

**[0:59:36]** tomándolo desde el conjunto de entrenamiento

**[0:59:38]** pero la forma más fácil, más sencilla

**[0:59:40]** es dividirlo en tres conjuntos

**[0:59:42]** distintos

**[0:59:45]** es la más fácil de entender, después

**[0:59:47]** abajito voy a hablar de un método de validación cruzada

**[0:59:49]** y este método extraño que

**[0:59:51]** se llama CAFOL, más abajo hay una

**[0:59:53]** hay una imagen pero por mientras

**[0:59:55]** los vamos a dividir en tres conjuntos

**[0:59:57]** distintos y cada uno tiene sus funciones

**[0:59:59]** el detrain es para ajustar el modelo

**[1:00:01]** el detest es para

**[1:00:03]** evaluar el modelo final o sea solamente se ocupa

**[1:00:05]** el final, no se ocupa para nada más

**[1:00:07]** y el de validación es para tomar

**[1:00:09]** decisiones sobre los hiperparámetros

**[1:00:11]** del modelo, o sea estos son

**[1:00:13]** parámetros del modelo que no se entrenan

**[1:00:15]** con los datos de entrenamiento, son decisiones que yo

**[1:00:17]** tendría que tomar desde antes

**[1:00:19]** de entrenar, si lo

**[1:00:22]** pensamos por ejemplo en

**[1:00:24]** estos modelos como más grandes, cuando no hice

**[1:00:26]** voy a entrenar, no sé

**[1:00:28]** una red neuronal

**[1:00:30]** bueno la cantidad de épocas podría ser

**[1:00:32]** un hiperparámetro, yo lo entreno por

**[1:00:34]** 20 épocas, 30 épocas

**[1:00:36]** 50 épocas

**[1:00:38]** y me desconecto

**[1:00:40]** esto que es terrible, no puedes

**[1:00:42]** ya

**[1:00:47]** voy a dejar que se ocorra para arriba

**[1:00:49]** y entonces aquí lo estamos haciendo

**[1:00:51]** de la manera como más fácil

**[1:00:53]** que es dividirlo en tres

**[1:00:55]** entonces voy a ocupar el train test

**[1:00:57]** 2 veces, primero

**[1:00:59]** voy a dividir en train

**[1:01:01]** y test y luego voy a tomar

**[1:01:03]** el train y también lo voy a partir

**[1:01:05]** y me voy a quedar con la partición como

**[1:01:07]** train y vale

**[1:01:09]** todo lo que estoy haciendo aquí

**[1:01:12]** nada más, nada más

**[1:01:14]** lo importante es no cambiar los nombres

**[1:01:16]** aquí, porque esto te lo da

**[1:01:18]** en el orden que está explícito aquí

**[1:01:20]** o sea, primero te da los X

**[1:01:22]** primero del conjunto

**[1:01:24]** grande que sería el train

**[1:01:26]** porque pusiste test side 0.2

**[1:01:28]** después el X del test, después viene

**[1:01:30]** el ID del train y después viene el ID del test

**[1:01:32]** aunque yo cambie los nombres que quiera aquí

**[1:01:34]** la función

**[1:01:38]** devuelve ese orden

**[1:01:40]** o sea, aunque aquí le ponga

**[1:01:42]** ID test, aquí va a estar el X test

**[1:01:44]** porque la función la devuelve

**[1:01:46]** en ese orden

**[1:01:49]** así que cuidado con eso

**[1:01:51]** cuidado con los nombres

**[1:01:54]** y aquí puedo ver la cantidad de datos

**[1:01:56]** que me quedo para entrenar

**[1:01:58]** la cantidad de datos que me quedo para validar

**[1:02:00]** y la cantidad de datos de test

**[1:02:02]** entonces tengo 640, 160

**[1:02:04]** y yo digo, bueno

**[1:02:07]** entonces como vamos a ajustar nuestra linda

**[1:02:09]** regresión lineal

**[1:02:11]** como lo hicimos antes, instanciamos

**[1:02:13]** nuestro modelo de regresión lineal

**[1:02:15]** y luego para entrenar lo hacemos punto fit

**[1:02:17]** y pasamos el X train

**[1:02:19]** y el E train, o sea, los datos para entrenar

**[1:02:21]** y las etiquetas para entrenar

**[1:02:25]** y luego lo que podemos hacer es predecir

**[1:02:27]** porque quiero predecir para después evaluar

**[1:02:29]** entonces para predecir

**[1:02:31]** con esto que es el punto fit que no se demora nada

**[1:02:33]** porque son pocos dadas

**[1:02:35]** de toda la cuestión

**[1:02:37]** puedo hacer mi predict ya

**[1:02:39]** y aquí le paso el conjunto de test

**[1:02:41]** para eso lo hice

**[1:02:46]** recordar que el conjunto de test

**[1:02:48]** son datos que el modelo no ha visto

**[1:02:50]** nunca los ocupo para aprender

**[1:02:52]** entonces yo aquí estoy

**[1:02:54]** viendo con el conjunto de test

**[1:02:56]** como el modelo es capaz de generalizar

**[1:02:58]** como es capaz

**[1:03:00]** de que tanto predice bien

**[1:03:02]** para datos nuevos

**[1:03:04]** porque eso es lo importante, yo quiero que mi modelo

**[1:03:06]** tiene para datos que nunca haya visto

**[1:03:08]** por eso necesito el conjunto de test

**[1:03:10]** entonces aquí voy a hacer un

**[1:03:12]** scatter entre la etiqueta

**[1:03:14]** verdadera y lo que predijo mi modelo

**[1:03:16]** entrenar, entonces aquí tengo el valor

**[1:03:21]** real y aquí el valor predicho

**[1:03:23]** entonces yo cuando la predicción es

**[1:03:25]** muy parecía el valor real

**[1:03:27]** voy a ver como una línea

**[1:03:29]** normalmente yo espero ver una línea

**[1:03:31]** si tuviera todo muy

**[1:03:33]** desparramado eso significa que

**[1:03:35]** mi modelo no me está funcionando

**[1:03:37]** como yo esperaría

**[1:03:39]** y le puedo sacar el R2

**[1:03:41]** le puedo sacar el mc

**[1:03:43]** ahí está mi R2

**[1:03:49]** y ahí está mi mc

**[1:03:51]** igual mi error cuadrático medio

**[1:03:53]** recordemos que el cuadrático medio

**[1:03:55]** lo estoy elevando

**[1:03:57]** pero igual es

**[1:03:59]** alto

**[1:04:01]** pero no está tan alto y si le sacamos la

**[1:04:03]** si sacamos el Rmc

**[1:04:06]** el root mean square error

**[1:04:08]** que sería sacar la raíz y ahí vemos el valor real

**[1:04:10]** estoy equivocando más o menos

**[1:04:12]** bueno ahí es más aceptable

**[1:04:14]** he dado el rango, el rango por el que

**[1:04:16]** se mueven los valores

**[1:04:19]** y yo aquí podría hacer muchas cosas

**[1:04:23]** por ejemplo podría mirar

**[1:04:25]** los coeficientes

**[1:04:27]** de mi modelo porque

**[1:04:29]** aquí ya tenemos más de una columna

**[1:04:31]** entonces lo que

**[1:04:33]** me mostraron los coeficientes

**[1:04:35]** yo llame pendiente antes

**[1:04:37]** son más de uno porque

**[1:04:39]** es guat

**[1:04:45]** guat guat

**[1:04:50]** no calmación, paso aquí

**[1:04:52]** y hice mal

**[1:04:57]** algo hice mal, calmación

**[1:04:59]** estoy entrando en panico

**[1:05:02]** paso aquí, no hay sonido

**[1:05:08]** se me apagó el perno el nuevo

**[1:05:13]** que te paso aquí

**[1:05:15]** la rara mi vida

**[1:05:29]** ok me voy a quedar esto pendiente

**[1:05:35]** porque estoy entrando en panico

**[1:05:37]** lo vamos a dejar así

**[1:05:39]** voy a dejar esto pendiente, no sé qué está pasando aquí

**[1:05:41]** qué extraño

**[1:05:43]** ya pero

**[1:05:45]** superé por eso, sigamos con mi vida

**[1:05:47]** después mando un anuncio

**[1:05:49]** explicando qué me está pasando ahí

**[1:05:51]** porque ahora no tengo cabeza para

**[1:05:53]** de boogie, cuando entré en panico

**[1:05:57]** tengo mi modelo

**[1:05:59]** predige y evalué

**[1:06:01]** que es como el típico

**[1:06:03]** flujo que tengo con esto

**[1:06:05]** y normalmente instancia mi modelo

**[1:06:07]** lo entreno, si es que tengo algún hiperparámetro

**[1:06:09]** o algo con el conjunto de validación

**[1:06:11]** que vamos a ver un poquito más adelante

**[1:06:13]** y con el conjunto de test evalúo

**[1:06:15]** y ya con las métricas puedo ver

**[1:06:17]** que también lo hace mi modelo en estos datos nuevos

**[1:06:19]** o sea que también generaliza

**[1:06:21]** o también puedo ver qué modelo es mejor que otro

**[1:06:23]** porque me permito con las métricas

**[1:06:25]** poder comparar modelos

**[1:06:27]** lo importante cuando estoy comparando modelos

**[1:06:29]** es que calcule las métricas

**[1:06:31]** sobre el mismo conjunto de test

**[1:06:33]** ok eso es super importante

**[1:06:35]** si yo quiero comparar modelos lo importante es poner como

**[1:06:37]** hiperpar, o sea

**[1:06:39]** algún baseline y ocupar el mismo conjunto de test

**[1:06:41]** y ahí sacarlas métricas

**[1:06:43]** porque eso me permite comparar

**[1:06:46]** entonces muy importante

**[1:06:48]** si es que quiero como correr varios modelos

**[1:06:50]** guardar

**[1:06:52]** no cambiar el conjunto de test

**[1:06:54]** ok el conjunto de test tiene que ser igual

**[1:06:56]** para todos

**[1:06:59]** un poquito de miedo de esto, me voy a saltar

**[1:07:01]** ya

**[1:07:04]** lo otro, esa es regresión lineal

**[1:07:06]** regresión lineal

**[1:07:08]** la vainilla

**[1:07:11]** sin ninguna cosa extra

**[1:07:13]** ahora ustedes

**[1:07:15]** podemos como encontrar

**[1:07:17]** un poquito de problemas más complejos

**[1:07:19]** y podemos pasar

**[1:07:21]** a la regresión polinomial

**[1:07:23]** entonces la regresión lineal

**[1:07:25]** como dice su nombre

**[1:07:27]** solo puede modelar relaciones lineales

**[1:07:29]** entre las variables de entrada

**[1:07:31]** y la salida

**[1:07:33]** esta multiplicación que tengo aquí

**[1:07:35]** es una operación lineal

**[1:07:37]** si la relación real

**[1:07:41]** no es lineal

**[1:07:43]** podemos transformar las variables

**[1:07:45]** para que una regresión lineal

**[1:07:47]** pueda modelar

**[1:07:49]** entonces va a seguir siendo lineal

**[1:07:51]** con respecto a los parámetros

**[1:07:53]** si es que yo le hago una transformación

**[1:07:55]** no lineal a esto

**[1:07:57]** entonces nuestra formulita

**[1:07:59]** nuestra expresión que era esta

**[1:08:01]** vamos a pasarla a este

**[1:08:03]** X es el que se transforma

**[1:08:05]** entonces nuestra transformación va a llamarse

**[1:08:07]** y nuestro G

**[1:08:09]** no es lineal con respecto a X

**[1:08:11]** pero nuestra regresión

**[1:08:14]** sigue siendo lineal

**[1:08:16]** entonces

**[1:08:18]** para hacer una regresión polinomial

**[1:08:20]** nuestro G va a hacer

**[1:08:22]** calcular un polinomial

**[1:08:24]** entonces en el caso de la regresión polinomial

**[1:08:26]** la regresión queda como

**[1:08:28]** y voy a

**[1:08:30]** esta transformación es

**[1:08:32]** elevar como un grado

**[1:08:34]** por ejemplo tengo aquí

**[1:08:36]** elevado a 1

**[1:08:38]** después mi X elevado a 2

**[1:08:40]** y mi X elevado hasta K

**[1:08:42]** donde K va a ser el grado del polinom

**[1:08:46]** entonces antes yo solamente

**[1:08:48]** me preocupaba

**[1:08:50]** de que la cantidad

**[1:08:52]** de estos parámetros

**[1:08:54]** solo dependía de la cantidad de atributos

**[1:08:56]** o la cantidad de columnas

**[1:08:58]** que tenía mi conjunto de datos

**[1:09:00]** pero ahora tengo otra cosa

**[1:09:02]** que

**[1:09:05]** también me cambia el número de parámetros

**[1:09:07]** que me voy a preocupar del modelo

**[1:09:09]** que es el grado del polinomio

**[1:09:11]** ok?

**[1:09:13]** dependiendo del grado del polinomio

**[1:09:15]** me iba a tener más parámetros para el modelo

**[1:09:17]** entonces

**[1:09:19]** este parámetro

**[1:09:21]** del valor del polinomio en realidad no depende de los datos

**[1:09:23]** no es cierto?

**[1:09:26]** si se dan cuenta

**[1:09:28]** yo puedo decir ya voy a hacer una regresión polinomial

**[1:09:30]** de grado 3

**[1:09:32]** de grado 4

**[1:09:34]** de grado 5

**[1:09:36]** porque yo estoy entrenando porque ese parámetro

**[1:09:38]** no se ajusta con los datos

**[1:09:40]** no depende de los datos

**[1:09:42]** entonces al no depender de los datos

**[1:09:44]** se transforma en algo que llamamos

**[1:09:46]** hiperparámetro

**[1:09:48]** es distinto de

**[1:09:50]** estos

**[1:09:52]** estos se ajustan

**[1:09:54]** se entrenan

**[1:09:56]** el K se decide antes de entrenar

**[1:10:02]** entonces ahora vamos a ver

**[1:10:04]** de forma simple

**[1:10:06]** como hacemos esta transformación

**[1:10:08]** para

**[1:10:10]** para transformar valga la redundancia

**[1:10:12]** nuestro valor en un polinomio

**[1:10:14]** entonces aquí me voy a dibujar

**[1:10:17]** unos puntitos

**[1:10:21]** ahí existen

**[1:10:23]** si se dan cuenta algunos son más claritos

**[1:10:25]** que otros y es simplemente para

**[1:10:27]** demostrar que voy a tener

**[1:10:29]** unos x y unos y

**[1:10:31]** que voy a tomar como entrenamiento

**[1:10:33]** unos puntos que voy a tomar

**[1:10:35]** como entrenamiento y otros puntos

**[1:10:37]** que voy a tomar como validación

**[1:10:40]** claritos los voy a tomar como el entrenamiento

**[1:10:42]** sin normal recuerdo y los oscuritos

**[1:10:44]** los voy a tomar como validación

**[1:10:46]** entonces voy a entrenar una regresión

**[1:10:48]** lineal

**[1:10:51]** y voy a tratar de

**[1:10:53]** ajustar una regresión lineal

**[1:10:55]** a este tipo de datos

**[1:10:57]** que si yo los veo al ojo

**[1:10:59]** veo que no va a ser un buen ajuste

**[1:11:04]** si se dan cuenta aquí estoy ocupando los datos

**[1:11:06]** los datos claritos

**[1:11:08]** cuando el x y el y

**[1:11:10]** el x y el y

**[1:11:13]** estoy ocupando esto para ajustar

**[1:11:15]** y me doy cuenta que el ajuste no es muy bueno

**[1:11:17]** si se dan cuenta no estoy describiendo en realidad

**[1:11:19]** el comportamiento de los datos que yo visualmente

**[1:11:21]** veo con esa línea

**[1:11:23]** entonces aquí tenemos un problema porque la regresión lineal

**[1:11:25]** con una línea no voy a poder

**[1:11:27]** describir bien este comportamiento

**[1:11:30]** entonces vamos a utilizar una

**[1:11:32]** regresión polinomia

**[1:11:34]** como hacemos esta transformación vamos a ocupar

**[1:11:36]** una función de scikit learn

**[1:11:38]** polinomial features

**[1:11:41]** aquí

**[1:11:44]** entonces también es como una forma de

**[1:11:46]** procesar los datos lo vamos a importar

**[1:11:48]** desde scikit learn y lo vamos a ocupar

**[1:11:50]** como la instanciamos

**[1:11:52]** y aquí si le tenemos que poner

**[1:11:54]** algún valor no podemos usarla por defecto

**[1:11:56]** y el valor es el grado

**[1:11:58]** del polinomio que queremos

**[1:12:00]** entonces en este caso le voy a poner que es de grado 3

**[1:12:02]** y lo que va

**[1:12:05]** lo que va a hacer es que esto transforma los valores

**[1:12:07]** en nuestra g

**[1:12:09]** nuestra g de aquí

**[1:12:11]** entonces tomo los valores

**[1:12:13]** y le hago a mi polinomial features

**[1:12:15]** que lo llame transformer

**[1:12:17]** le voy a hacer transformer.fit

**[1:12:19]** y le paso mis x

**[1:12:21]** y después le hago transformer.transform

**[1:12:23]** y también le paso el x

**[1:12:25]** esto se puede

**[1:12:27]** hay un método

**[1:12:29]** que lo hace todo junto que se llama fit transform

**[1:12:31]** y estas dos líneas las transforman una

**[1:12:33]** y hace exactamente la misma

**[1:12:36]** entonces el transformado me lo voy a

**[1:12:38]** a guardar en un x yon bajo

**[1:12:40]** y el sin transformar

**[1:12:42]** es el x sin el yon

**[1:12:44]** voy a mostrar esto

**[1:12:46]** y mi x original es

**[1:12:48]** 1,3,6,10,20

**[1:12:50]** 22,26

**[1:12:52]** y 28

**[1:12:55]** entonces que es lo que hace esto

**[1:12:57]** porque yo le puse grado 3

**[1:12:59]** toma el 1 y lo eleva a 0

**[1:13:01]** después toma el 1

**[1:13:03]** y lo eleva a 1

**[1:13:05]** después toma el 1 y lo eleva a 2

**[1:13:07]** después toma el 1 y lo eleva a 3

**[1:13:09]** y todo eso me da puros 1

**[1:13:11]** después toma el segundo valor que es 3

**[1:13:13]** toma el 3 y lo eleva a 0

**[1:13:15]** después toma el 3 y lo eleva a 1

**[1:13:17]** que eso es 3

**[1:13:19]** después toma el 3 y lo eleva a 2

**[1:13:21]** que eso es 9

**[1:13:23]** después toma el 3 y lo eleva a 3

**[1:13:25]** que eso es 27

**[1:13:27]** y así con cada uno de los valores que están en x

**[1:13:29]** entonces lo que esta haciendo es

**[1:13:31]** elevarlos a cierta potencia

**[1:13:33]** hasta el grado que yo marque

**[1:13:35]** entonces con eso ya tenemos nuestra transformación

**[1:13:38]** ya podemos transformar nuestros datos

**[1:13:40]** entonces ahora

**[1:13:42]** tenemos que combinar

**[1:13:44]** la transformación

**[1:13:46]** con nuestra regresión linear

**[1:13:48]** tenemos que pegarlo

**[1:13:50]** para que yo después

**[1:13:52]** a esa cosa que ya esta conectada

**[1:13:54]** le pase los datos y los datos se transformen

**[1:13:56]** y se vayan a la regresión

**[1:13:58]** y yo no tengo que hacer nada

**[1:14:00]** no me preocupen

**[1:14:02]** entonces este pegamento para poder conectar estas dos cosas

**[1:14:04]** se llama make pipeline

**[1:14:06]** que básicamente conecta la salida de una cosa

**[1:14:08]** con la entrada de otra cosa

**[1:14:10]** como poner un tubito

**[1:14:14]** entonces vamos a crearnos una función

**[1:14:16]** que se llame polynomial regression

**[1:14:18]** y como argumento va a tener el grado

**[1:14:20]** y por defecto se lo voy a dejar como grado 2

**[1:14:22]** y que puede tener otros argumentos

**[1:14:24]** allí dice por defecto tendrá grado 0

**[1:14:26]** mentira tiene grado 2

**[1:14:28]** y lo que hago es

**[1:14:30]** retornar un make pipeline

**[1:14:32]** o sea crear esta conexión

**[1:14:34]** el polynomial features

**[1:14:36]** que tiene el degree que yo le paso aquí

**[1:14:38]** el grado que yo le paso aquí

**[1:14:40]** y una regresión linear

**[1:14:44]** entonces esto yo ya lo creé

**[1:14:46]** ya existe, ya funciona

**[1:14:48]** que sería mi regresión polynomial

**[1:14:50]** que hicimos más o menos a mano

**[1:14:52]** entonces ahora yo ya puedo llegar a ocuparla

**[1:14:54]** maravilloso

**[1:14:56]** entonces vamos a crear regresiones polynomiales

**[1:14:58]** del grado 2 al 7

**[1:15:00]** y voy a crear una regresión linear

**[1:15:03]** que sería de grado 0

**[1:15:05]** con mis datos

**[1:15:07]** me estoy pintando los datos

**[1:15:09]** y estoy cogiendo un color distinto para cada

**[1:15:11]** modelo

**[1:15:14]** y aquí estoy haciendo un ford para los distintos grados

**[1:15:16]** el 1, el 2 y hasta el 7

**[1:15:18]** luego creo mi modelo

**[1:15:20]** que en este caso se llama polynomial regression

**[1:15:22]** que es el que pusimos acá arriba

**[1:15:24]** luego le hago un pit

**[1:15:26]** y luego le hago un predict

**[1:15:28]** y

**[1:15:31]** estoy graficando lo que predigo

**[1:15:33]** entonces dibujo la predicción

**[1:15:35]** dibujo mi modelo en el espacio

**[1:15:37]** esto lo voy a correr porque visualmente

**[1:15:39]** se entiende mejor

**[1:15:42]** entonces ahí tengo mis datos de entrenamiento

**[1:15:44]** y ahí tengo los distintos grados

**[1:15:46]** y como se comporta

**[1:15:48]** como está describiendo

**[1:15:50]** el comportamiento de los datos cada

**[1:15:52]** regresión polynomial dado el grado

**[1:15:54]** entonces por ejemplo

**[1:15:56]** vemos la de grado 1 que es esa línea

**[1:15:58]** luego le vemos la de grado 2 que es como una curva

**[1:16:00]** una parábola

**[1:16:02]** una sonrisa

**[1:16:05]** pues vemos la de grado 3 que es un verde más clarito

**[1:16:07]** que va tratando como de

**[1:16:09]** seguir esta forma

**[1:16:11]** y ya entre más voy aumentando el grado

**[1:16:13]** más estoy pasando exactamente

**[1:16:15]** casi por los puntos

**[1:16:18]** entonces en este caso

**[1:16:20]** podemos observar que

**[1:16:22]** mientras más alto el grado del polynomial

**[1:16:24]** más flexible el modelo

**[1:16:26]** y por ende mejora el ajuste

**[1:16:28]** pero al aumentar arbitrariamente el grado del polynomial

**[1:16:30]** podemos sobreajustarnos

**[1:16:32]** a los datos

**[1:16:34]** que es el problema

**[1:16:37]** esto me lo voy a saltar por cosas de tiempo

**[1:16:39]** pero esto debería poder acceder

**[1:16:41]** que

**[1:16:43]** aquí hay distintas cosas que puedo acceder

**[1:16:45]** desde mi modelo que se llama polynomial feature

**[1:16:47]** si es que quisiera acceder

**[1:16:49]** al coeficiente

**[1:16:51]** si es que quisiera acceder al intercept

**[1:16:53]** si es que quisiera acceder al grado

**[1:16:55]** y aquí los coeficientes

**[1:16:57]** son más de 1

**[1:16:59]** porque necesito 1

**[1:17:01]** para cada

**[1:17:03]** elemento elevado

**[1:17:05]** a un grado

**[1:17:07]** necesito

**[1:17:09]** el que se le va al grado 0

**[1:17:11]** el que se le va al grado 1

**[1:17:14]** entonces aquí está tomando la polynomial feature

**[1:17:16]** el grado 7

**[1:17:18]** entonces debería tener 1 para

**[1:17:20]** grado 0, grado 1, 2, 3, hasta el 7

**[1:17:22]** y tengo mi bias

**[1:17:24]** ya esto lo escribí a manito pero no lo quiero

**[1:17:26]** así que me lo voy a saltar por tiempo

**[1:17:28]** entonces aquí me viene

**[1:17:30]** mi validación cruzada y mis cosas de sesgo

**[1:17:32]** y variance

**[1:17:35]** aquí voy a mostrar más o menos para que se entiende

**[1:17:37]** mucho más visualmente

**[1:17:40]** voy a hacer lo mismo aquí

**[1:17:42]** sé antes, pero un gráfico para cada uno

**[1:17:44]** voy a tomar

**[1:17:46]** la regresión polynomial

**[1:17:48]** de grado 4, de grado 7

**[1:17:50]** de grado 10 y de grado 13

**[1:17:52]** que están aquí y les voy a sacar

**[1:17:54]** el R cuadrado y el mce

**[1:17:56]** solo utilizando

**[1:17:58]** la diferencia con el mismo conjunto de datos

**[1:18:00]** que yo entrené

**[1:18:02]** a manito

**[1:18:08]** me pregunto si en este caso

**[1:18:10]** como podíamos discriminar por ejemplo

**[1:18:13]** de algún ajuste sinusoidal

**[1:18:15]** como?

**[1:18:18]** es que bueno

**[1:18:21]** con los polinomios igual se puede hacer

**[1:18:23]** más o menos un polinomio de grado

**[1:18:25]** alto y se ajustan bien por ejemplo

**[1:18:27]** el 4 o el 7

**[1:18:29]** pero en ese sentido

**[1:18:31]** como uno podría decir no sé

**[1:18:33]** discriminar entre estos

**[1:18:35]** un ajuste sinusoidal

**[1:18:37]** ah, ya

**[1:18:41]** ahí empezaría lo que necesitaría

**[1:18:43]** si me preguntas como qué pasa

**[1:18:45]** si yo hago esto a un modelo

**[1:18:47]** que

**[1:18:49]** como que describa esta forma sinusoidal

**[1:18:51]** original de los datos

**[1:18:53]** ahí simplemente puedes ajustar el modelo que tú quieras

**[1:18:55]** y medirle el error

**[1:18:57]** pero no medirle el error

**[1:18:59]** con respecto a lo que yo estoy haciendo aquí

**[1:19:01]** que serían los

**[1:19:04]** los datos de entrenamiento

**[1:19:06]** sino que tendrías que medirle el error

**[1:19:08]** o al test o a la validación

**[1:19:11]** si es tu modelo final

**[1:19:13]** y no vas a tomar ninguna más decisión

**[1:19:15]** lo tendrías que comparar el error con los

**[1:19:17]** datos de test

**[1:19:19]** y ahí tomas una decisión

**[1:19:23]** si porque

**[1:19:25]** bueno a fin

**[1:19:27]** de ejemplo me he visto

**[1:19:29]** regresar a línea y ahora polinomio

**[1:19:31]** pero existen también otras funciones que se pueden

**[1:19:33]** aplicar me imagino

**[1:19:35]** si pero

**[1:19:37]** esto es un ejemplo muy de juguete

**[1:19:39]** por eso es súper importante visualizar los datos

**[1:19:41]** para ver el comportamiento

**[1:19:43]** pero normalmente mis datos tienen múltiples dimensiones

**[1:19:45]** entonces quizá esta forma yo no la vea

**[1:19:47]** entonces ahí me queda solamente probar

**[1:19:52]** y ahí tendría que comparar y como te digo

**[1:19:54]** tendría que usar métricas

**[1:19:56]** normalmente en mi conjunto de test para ver qué modelo

**[1:19:58]** se ajusta mejor

**[1:20:05]** entonces aquí tengo

**[1:20:08]** 4

**[1:20:10]** de los distintos que ajusté con el mismo set

**[1:20:12]** de datos son los mismos datos que aquí

**[1:20:14]** se ven más chiquitos porque el gráfico está

**[1:20:16]** abarcando un rango mucho mayor

**[1:20:18]** aquí tengo un polinomio de grado 4

**[1:20:20]** grado 7 grado 10 de grado 13

**[1:20:22]** y estoy calculando cuánto es el error

**[1:20:24]** pero con los datos que yo ocupé para entrenar

**[1:20:26]** o sea estoy calculando el error

**[1:20:28]** en los datos de entrenamiento

**[1:20:30]** entonces si se dan cuenta el polinomio de grado 4

**[1:20:32]** lo hace bastante bien

**[1:20:34]** el polinomio de grado 7 pasa perfectamente

**[1:20:36]** por todos los puntos tiene un re-quadrado

**[1:20:38]** de grado 1 y un mc de 0

**[1:20:40]** entonces pasa perfectamente por cada punto

**[1:20:42]** si dan cuenta el de grado 10

**[1:20:44]** también pasa perfectamente por cada punto

**[1:20:46]** y el de grado 13 también pasa

**[1:20:48]** bueno casi perfectamente por cada punto

**[1:20:50]** se equivoca un poquito

**[1:20:52]** pero qué me pasa que el de grado 10

**[1:20:54]** hace locuras

**[1:20:56]** entre los puntos

**[1:20:58]** en cambio el de grado 7 sigue el comportamiento

**[1:21:00]** que yo esperaría

**[1:21:02]** y por qué me pasa porque aquí me estoy

**[1:21:04]** sobreajustando demasiado los datos

**[1:21:06]** qué me va a pasar que yo no voy a poder generalizar

**[1:21:08]** con este tipo de modelo

**[1:21:10]** entonces aquí tengo un problema de

**[1:21:12]** cómo escojo el grado del polinomio

**[1:21:14]** para escoger el grado del polinomio

**[1:21:16]** como dijimos que es un hiperparámetro

**[1:21:18]** necesita un conjunto de validación

**[1:21:21]** entonces voy a hacer exactamente esto mismo

**[1:21:23]** pero

**[1:21:25]** calculando el re-quadrado y el mc

**[1:21:27]** con esos datos que yo me quedé guardaditos

**[1:21:29]** que no ocupé para entrenar

**[1:21:31]** con esos datos que están más claritos aquí

**[1:21:37]** estos

**[1:21:39]** que no ocupas para entrenar

**[1:21:41]** entonces si yo ahí sacando el re-quadrado

**[1:21:43]** y el mc con respecto a esos datos

**[1:21:45]** ahí puedo mirar matemáticamente

**[1:21:47]** cuál modelo es mejor

**[1:21:49]** si se dan cuenta en este caso me quedaría

**[1:21:51]** fácil viendo esos

**[1:21:53]** solamente viendo esos números

**[1:21:55]** me quedaría con el de grado 7

**[1:21:57]** porque disminuye el mc y en cambio el de grado 10

**[1:21:59]** que lo hace súper bien porque pasa

**[1:22:01]** por cada punto en el entrenamiento

**[1:22:03]** en la validación lo hace mal

**[1:22:05]** y lo puedo mirar

**[1:22:07]** entonces

**[1:22:09]** como ajusto estos hiperparámetros

**[1:22:11]** yo ocupo mi conjunto de validación

**[1:22:13]** si es que quiero ajustar

**[1:22:15]** estos hiperparámetros

**[1:22:17]** que son una decisión que yo tomo

**[1:22:19]** que no se ajusta con los datos

**[1:22:21]** conjunto de validación

**[1:22:23]** porque el grado es

**[1:22:25]** una decisión que yo tomo

**[1:22:27]** del modelo

**[1:22:29]** técnicamente estoy ajustando el grado

**[1:22:31]** y lo estoy ajustando

**[1:22:33]** con el conjunto de validación

**[1:22:35]** y recuerden ¿por qué no puedo ocupar el conjunto de test?

**[1:22:37]** porque el conjunto de test

**[1:22:39]** no se puede ocupar

**[1:22:41]** para ajustar nada del modelo

**[1:22:43]** nada nada

**[1:22:45]** no se puede filtrar información

**[1:22:47]** del conjunto de test para alimentar al modelo

**[1:22:49]** entonces como el grado

**[1:22:51]** yo lo estoy ajustando con el conjunto de

**[1:22:53]** validación no puedo ocupar el conjunto de test

**[1:22:55]** por eso existe el de validación

**[1:22:57]** para estos casos

**[1:22:59]** porque estoy tomando una decisión con respecto al modelo

**[1:23:01]** para que funcione mejor

**[1:23:03]** entonces el de test

**[1:23:05]** no va el de test es al final

**[1:23:07]** al final cuando ya ajuste todo lo que tenía que ajustar

**[1:23:09]** ajuste parámetros a usted hiperparámetros

**[1:23:11]** ahí evalúa

**[1:23:13]** y como se cogieron los puntos

**[1:23:15]** para el test de validación

**[1:23:17]** es que la clase vimos

**[1:23:19]** por ejemplo

**[1:23:21]** busstra

**[1:23:23]** si

**[1:23:25]** no me acuerdo de los otros nombres pero si

**[1:23:27]** sería bueno como tener

**[1:23:30]** una idea de

**[1:23:32]** normalmente lo que se hace es

**[1:23:34]** simplemente yo

**[1:23:36]** si aquí ya tengo un data set

**[1:23:38]** yo les mostré esta función

**[1:23:40]** train-test-split

**[1:23:42]** entonces normalmente ocupo esa porque

**[1:23:44]** es a los desordena

**[1:23:46]** ¿cuál lo ocupaste?

**[1:23:48]** esta función

**[1:23:50]** train-test-split

**[1:23:52]** y eso simplemente reparte los datos

**[1:23:54]** de entrenamiento, validación o test

**[1:23:56]** según yo lo necesite cuántas veces la ocupa

**[1:23:59]** que derreli

**[1:24:01]** ah, esta aquí

**[1:24:03]** aquí hay un ejemplo de cómo ocupar

**[1:24:06]** y eso de los desordena

**[1:24:08]** porque si pueden tener un orden temporal

**[1:24:10]** y pueden tener correlaciones temporales

**[1:24:12]** es la idea de desordenar

**[1:24:15]** para el caso del ejemplo

**[1:24:17]** yo solamente tomé los datos que estaban al medio

**[1:24:19]** no me acuerdo

**[1:24:21]** el nombre de todos los métodos

**[1:24:23]** que mostró el profe en clase

**[1:24:25]** pero si alguno quiera el bootstrap

**[1:24:27]** que lo explicó

**[1:24:29]** para mostrar

**[1:24:31]** para mostrar

**[1:24:33]** pero igual se podía hacer como

**[1:24:35]** para seleccionar muestras de testeos

**[1:24:37]** por lo que tendríamos

**[1:24:40]** ¿puedo hacerlo pero normalmente uno lo ocupa

**[1:24:42]** como para hacer

**[1:24:44]** aumentación de datos?

**[1:24:46]** si hubo una ocupa bootstrap

**[1:24:51]** pero para hacer ajustes

**[1:24:53]** y sacar errores

**[1:24:55]** pero no lo había

**[1:24:57]** me pareció interesante también la aplicación

**[1:24:59]** para estos fines

**[1:25:01]** si

**[1:25:03]** simplemente la idea es seleccionar un conjunto

**[1:25:05]** y seleccionarlo de esta manera

**[1:25:07]** o seleccionarlo al azar

**[1:25:10]** para que sea igual representativo

**[1:25:12]** porque una cosa que me puede pasar

**[1:25:14]** que yo puedo decir

**[1:25:16]** me puedo sobreajustar

**[1:25:18]** el conjunto de validación

**[1:25:20]** o sea quizá hay un conjunto de validación mejor

**[1:25:23]** claro igual me imagina que cada vez

**[1:25:25]** tú puedes hacer miles de pruebas

**[1:25:27]** 10.000 pruebas y si se te ocurre

**[1:25:29]** y elegir diferentes

**[1:25:31]** muestras y hacer ajuste y comparar

**[1:25:33]** no se ver qué cual puede ser mejor

**[1:25:35]** ¿validación cruzada?

**[1:25:37]** creo que el profesor debió haberlo mencionado

**[1:25:39]** ¿validación cruzada?

**[1:25:41]** ya, ¿validación cruzada?

**[1:25:43]** hace que yo disminuya

**[1:25:45]** este pensamiento

**[1:25:47]** que yo me puedo sesgar por el conjunto de validación

**[1:25:49]** y con eso escojo varios conjuntos

**[1:25:51]** de validación

**[1:25:53]** perfecto

**[1:25:55]** gracias

**[1:25:57]** veo otra manito

**[1:26:00]** si yo

**[1:26:02]** una consulta

**[1:26:04]** ligaba a lo que está comentando el compañero

**[1:26:06]** y lo que recién nos mostraste

**[1:26:08]** lo que pasa es que yo tengo mi conjunto de datos

**[1:26:10]** y

**[1:26:12]** la variable

**[1:26:14]** como con la que

**[1:26:16]** pienso

**[1:26:19]** utilizar

**[1:26:21]** para mi hipótesis

**[1:26:23]** para es

**[1:26:25]** binaria

**[1:26:27]** entonces de este conjunto de datos

**[1:26:29]** voy a utilizar un 80%

**[1:26:31]** y el otro 20% para dejarlo como para validación

**[1:26:33]** así como

**[1:26:35]** entonces

**[1:26:37]** de ahí con lo que no indicaste

**[1:26:39]** para desordenar los datos

**[1:26:41]** porque yo estaba pensando

**[1:26:43]** mientras tú hablabas

**[1:26:45]** de cómo voy a utilizar mi conjunto de datos

**[1:26:47]** pero cómo elijo el 20%

**[1:26:49]** y

**[1:26:51]** cómo elijo el otro 80%

**[1:26:53]** de qué forma

**[1:26:55]** y también este viendo el modelo

**[1:26:57]** para ver si ocupo

**[1:26:59]** regresión logística o decisión

**[1:27:01]** gandalfores

**[1:27:03]** ya

**[1:27:06]** con respecto

**[1:27:08]** a tu duda

**[1:27:10]** normalmente tienes que ver

**[1:27:12]** por ejemplo si es que es clasificación

**[1:27:14]** binaria

**[1:27:16]** la típica decisión es toparlo

**[1:27:18]** al azar

**[1:27:20]** es hacer una división al azar

**[1:27:22]** que es lo que hace la función 30 split por defecto

**[1:27:24]** ahora lo que tú deberías fijarte

**[1:27:26]** como es básicamente

**[1:27:28]** clasificación tu problema

**[1:27:30]** es ver

**[1:27:32]** que

**[1:27:34]** el desbalanceo que hay presente

**[1:27:36]** y si es que hay desbalanceo

**[1:27:38]** quizás tienes que

**[1:27:40]** ocupar alguna técnica

**[1:27:42]** para muestrear

**[1:27:44]** para aumentar los datos que tienes para balancear

**[1:27:46]** o cortar o decir voy a trabajar

**[1:27:48]** con el desbalanceo y si quieres que

**[1:27:50]** se mantenga las proporciones

**[1:27:52]** de cada clase entre test

**[1:27:54]** y variación

**[1:27:56]** hay un argumento que tiene 30 split

**[1:27:58]** no me acuerdo exactamente como se llamaba

**[1:28:00]** pero tiene uno que las mantiene

**[1:28:02]** ahí está como en la

**[1:28:05]** documentación hay que ponerle como true

**[1:28:07]** las mantien

**[1:28:10]** pero porque quiero dejar

**[1:28:12]** el 20% del conjunto de los datos

**[1:28:14]** para la prueba final

**[1:28:16]** y ocupar el 80% que tengo

**[1:28:18]** para

**[1:28:20]** la validación actualmente como cruzada

**[1:28:22]** si

**[1:28:24]** si quieres ocupar

**[1:28:26]** validación cruzada

**[1:28:28]** o se puede aceptar

**[1:28:30]** y aquí

**[1:28:32]** este 30 split está partiendo en dos

**[1:28:34]** mi conjunto y el primer conjunto

**[1:28:36]** está el 80% de los datos

**[1:28:38]** y el segundo es el 20 porque

**[1:28:40]** yo le puse que el test size fuera el 20%

**[1:28:42]** y con este

**[1:28:44]** con este valor

**[1:28:46]** yo le estoy indicando el porcentaje de datos

**[1:28:51]** vamos a tener la clase grabada

**[1:28:53]** vamos a tener la clase grabada

**[1:28:55]** así está grabando

**[1:28:57]** y creo que me pase

**[1:28:59]** voy a decir algo chiquito

**[1:29:01]** al último

**[1:29:03]** y termino

**[1:29:05]** que creo que no alcanza

**[1:29:07]** gracias a ti

**[1:29:09]** creo que no alcanza a explicar validación cruzada

**[1:29:11]** enteramente en tres minutos porque sería el medio

**[1:29:17]** aquí estábamos explicando porque el conjunto

**[1:29:19]** de validación es útil

**[1:29:21]** que teníamos hiperparámetros

**[1:29:23]** y la manera a ajustarlos era ocupando el conjunto

**[1:29:25]** de validación y que conjunto de test

**[1:29:27]** no se podía ocupar para ajustar esto

**[1:29:29]** porque igual es ajuste del modelo

**[1:29:31]** que pasa

**[1:29:33]** yo puedo realizar validación cruzada

**[1:29:35]** validación cruzada significa

**[1:29:37]** tomar varias veces

**[1:29:39]** entrenar varias veces con distintos

**[1:29:41]** conjuntos de validación

**[1:29:43]** y eso los puedo definir yo

**[1:29:45]** o puedo

**[1:29:47]** hacer que se definan automáticamente

**[1:29:49]** ok

**[1:29:51]** y una forma

**[1:29:53]** de hacer que se elijan

**[1:29:55]** automáticamente

**[1:29:57]** que se sampleen automáticamente

**[1:29:59]** es con un método que se llama

**[1:30:01]** Calfold

**[1:30:03]** no sé si el profe lo explicó en clases

**[1:30:05]** pero si no lo vamos a explicar la próxima ayudantía

**[1:30:07]** de buenas a primeras

**[1:30:10]** pero aquí está la definición de cada conjunto

**[1:30:12]** su utilidad

**[1:30:14]** y aquí hay

**[1:30:16]** una imagen

**[1:30:18]** explicando cómo funciona el Calfold

**[1:30:20]** el Calfold lo que hace es

**[1:30:22]** dividir los datos en dos

**[1:30:24]** en entrenamiento y test

**[1:30:26]** y luego yo defino

**[1:30:28]** un número K

**[1:30:30]** pongámosle 5

**[1:30:32]** porque este el ejemplo tiene 5

**[1:30:34]** y lo que hago es de

**[1:30:36]** dividir mi conjunto de entrenamiento

**[1:30:38]** en 5

**[1:30:40]** y voy a entrenar 5 veces

**[1:30:42]** y estas 5 veces voy a

**[1:30:44]** variar mi conjunto de validación

**[1:30:46]** para qué? para no sobreajustarme

**[1:30:48]** a mi conjunto de validación

**[1:30:50]** entonces aquí tengo 5 folds

**[1:30:53]** y la primera vez que entreno

**[1:30:55]** que sería el split 1

**[1:30:57]** ocupo el fold 1 para validar

**[1:30:59]** y todo lo demás para entrenar

**[1:31:01]** la segunda vez que entreno

**[1:31:03]** una instancia distinta de modelo

**[1:31:05]** ocupo el fold 2 como validación

**[1:31:07]** y todos los demás para entrenar

**[1:31:09]** y así

**[1:31:11]** y después veo el mejor modelo en pre-med

**[1:31:13]** ahí como veo el mejor modelo

**[1:31:15]** que valúo en el texto

**[1:31:17]** entonces

**[1:31:19]** con esta fórmula

**[1:31:21]** que es el codito como de acá abajo

**[1:31:23]** aquí grande

**[1:31:25]** yo puedo hacer la búsqueda hiperparámetros

**[1:31:27]** automática

**[1:31:29]** no tengo que probar yo con grado 7

**[1:31:31]** grado 10 hacia mano

**[1:31:33]** sino que puedo decirle aquí

**[1:31:35]** con un diccionario de parámetros

**[1:31:37]** oye me codigo

**[1:31:39]** prueba tanto tanto tanto

**[1:31:41]** tantos datos con tantos tantos tantos

**[1:31:43]** creo que lo vamos a dejar pendiente

**[1:31:45]** para verlo en la próxima clase

**[1:31:47]** porque igual dejar todo codigo

**[1:31:49]** no creo que se entienda de buenas a primeras

**[1:31:52]** pero hay una forma de hacerlo

**[1:31:54]** automática

**[1:31:56]** pueden tener toda la lógica del modelo

**[1:31:58]** y después podemos ver el k fold más

**[1:32:00]** a detalle

**[1:32:02]** pero ahora ya saben más o menos cómo entrenar

**[1:32:04]** cómo predecir y cómo evaluar

**[1:32:06]** teniendo los conjuntos fijos

**[1:32:09]** ya

**[1:32:11]** lo dejamos hasta aquí porque ya me pasé

**[1:32:13]** para mostrar por si hay más dudas

**[1:32:15]** ok

**[1:32:17]** ay ya, yo tengo una

**[1:32:19]** para lo que recién estábamos viendo

**[1:32:21]** vale

**[1:32:23]** mil datos

**[1:32:25]** tengo 9

**[1:32:27]** 90 y 8 aproximadamente

**[1:32:29]** esa es

**[1:32:31]** esa es mi data

**[1:32:33]** entonces justo eso

**[1:32:35]** tengo que hacer cinco modelos

**[1:32:37]** lo que recién estabas comentando

**[1:32:39]** y el 20% lo voy a dejar

**[1:32:41]** lo otro

**[1:32:43]** entonces me sirven

**[1:32:46]** es un milo tiene que ser menos

**[1:32:48]** o más

**[1:32:51]** mil datos dependiendo

**[1:32:53]** de la cantidad de columnas que tengas

**[1:32:55]** puede ser harto o no

**[1:32:57]** y así

**[1:32:59]** con tanto

**[1:33:01]** sacando todo lo que es

**[1:33:03]** aula

**[1:33:05]** certamen este son alrededor

**[1:33:07]** de 16 columnas

**[1:33:10]** igual no

**[1:33:12]** un poco para apoblar el espacio

**[1:33:14]** pero igual el modelo va a aprender algo

**[1:33:16]** pero quizás no tenga la cantidad

**[1:33:18]** de datos para apoblar todo tu espacio

**[1:33:20]** porque 16 columnas igual es

**[1:33:22]** harta dimensión aliento

**[1:33:24]** estoy reciente viendo los esperantes

**[1:33:26]** estoy confirmando

**[1:33:28]** disculpe que me meta

**[1:33:32]** pero me imagino que igual

**[1:33:34]** debe haber una cierta correlación

**[1:33:36]** entre los datos que va a querer expresar

**[1:33:38]** entre la veje X y por ejemplo

**[1:33:40]** lo que estoy graficando

**[1:33:42]** no sé si uno puede acusar cosas

**[1:33:44]** como cualquier

**[1:33:46]** a cualquier conjunto de datos que uno tenga

**[1:33:48]** esperar ciertos comportamientos

**[1:33:50]** no sé si uno visualiza las cosas

**[1:33:52]** una disculpción

**[1:33:54]** que te permite una justelina

**[1:33:56]** cuadrático o de un polínome que sea

**[1:33:58]** si no soy dar

**[1:34:00]** pero si tienen que haber ciertas tendencias

**[1:34:02]** obvio

**[1:34:05]** el análisis como de correlaciones

**[1:34:07]** y de ver como tendencias

**[1:34:09]** yo lo hago antes de empezar a entrenar

**[1:34:11]** para que sea más útil

**[1:34:13]** entonces podría por ejemplo comparar

**[1:34:15]** dos instancias de modelo uno donde

**[1:34:17]** solamente entreno con

**[1:34:19]** las variables que yo opino que son las más críticas

**[1:34:21]** y después entregar con todo

**[1:34:23]** para comparar por ejemplo entre esas

**[1:34:25]** dos instancias de modelo

**[1:34:28]** si es que tengo el tiempo para probar

**[1:34:30]** sí

**[1:34:32]** por lo que

**[1:34:34]** claro

**[1:34:36]** es algo que me refiere a que posible

**[1:34:38]** quizás sea bueno visualizar las columnas

**[1:34:40]** y la grafica en función de

**[1:34:42]** no sé

**[1:34:45]** de las variables que ya quería que pueda generar cierta tendencia

**[1:34:47]** que lo más importante me imagino

**[1:34:49]** para poder hacer el modelo

**[1:34:51]** es que estamos grabando ¿no?

**[1:34:55]** estoy grabando no sé si se corta

**[1:34:57]** lo que pasa es que yo tengo

**[1:34:59]** mi hipótesi

**[1:35:01]** nula y mi hipótesi

**[1:35:03]** ya formulada

**[1:35:05]** ahí tengo el dataset

**[1:35:07]** me estoy basando en un paper

**[1:35:09]** que salió

**[1:35:11]** que se publicó el año pasado

**[1:35:13]** referente a la hipótesi

**[1:35:15]** si

**[1:35:17]** entonces que lo estoy haciendo

**[1:35:19]** yo estoy tomando lo que ya se hizo

**[1:35:21]** pero

**[1:35:23]** es como que ellos hicieron hasta el uno

**[1:35:25]** evaluaron desde el cero al uno

**[1:35:27]** y yo estoy evaluando desde el cero

**[1:35:29]** a menos uno

**[1:35:31]** yo sé que es difícil toda vez comprenderlo

**[1:35:33]** pero igual hay gente

**[1:35:35]** y los datos son de universidad no son sensible

**[1:35:37]** me quiero enterar mucho en detalles

**[1:35:39]** pero es como eso estoy tomando

**[1:35:41]** un paper publicado

**[1:35:43]** y de ahí estoy

**[1:35:45]** pero si ya es un paper

**[1:35:47]** puedes utilizar la misma limpieza

**[1:35:49]** o el mismo procesamiento que hacen ellos

**[1:35:51]** porque ellos también deben haber analizado

**[1:35:53]** los datos entonces tú puedes hacer exactamente

**[1:35:55]** el mismo análisis y ocupar las mismas razones

**[1:35:57]** para

**[1:35:59]** justificar quedarte con una variable o no

**[1:36:01]** lo típico cuando tengo clases

**[1:36:03]** es hacer gráficos de dispersión

**[1:36:05]** y colorear por clases

**[1:36:07]** para ver si las clases se separan

**[1:36:09]** que es que las clases se separan

**[1:36:11]** en algún gráfico

**[1:36:13]** o en los histogramas pues también

**[1:36:15]** pero no creo en gráficos de dispersión

**[1:36:17]** normalmente si las clases se separan

**[1:36:19]** esa es un atributo

**[1:36:21]** potencial candidato

**[1:36:23]** para ocupar en mi modelo

**[1:36:25]** porque me separan las clases

**[1:36:30]** estoy ocupando los mismos datos

**[1:36:32]** porque me hicieron la entrega de los datos

**[1:36:34]** también

**[1:36:36]** creo que en la clase de clasificación

**[1:36:38]** muestro como un gráfico

**[1:36:40]** de dispersión y lo pinto por clases

**[1:36:42]** y se muestra la separación

**[1:36:44]** voy a tratar de subirlo un poco

**[1:36:46]** antes para que tengan acceso por cierto

**[1:36:48]** ya te pasaste mucha gracia

**[1:36:50]** esa era como mi duda

**[1:36:52]** gracias

**[1:36:54]** que tenga buen fin de ir al cuidado

**[1:37:00]** que tenga buen fin de ir al cuidado

**[1:37:02]** igualmente, igualmente

**[1:37:04]** gracias por tu duda

**[1:37:06]** no sé si alguien más tiene dudas

**[1:37:08]** porque voy a acumular la gente

**[1:37:10]** no me alcanzaría a despedir

**[1:37:12]** no por el momento

**[1:37:17]** solo despedime, buenas noches

**[1:37:19]** ok, chao chao que estén muy bien

**[1:37:21]** si igual, gracias

**[1:37:23]** muy buena la gracia y la practica

**[1:37:25]** nos vemos entonces

**[1:37:27]** la próxima semana

**[1:37:29]** que estén muy muy bien

**[1:37:32]** chao igual

**[1:37:34]** gracias chao

**[1:37:36]** chao, muchas gracias

**[1:37:38]** chao chao
