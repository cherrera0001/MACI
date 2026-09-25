# 04Ayudantía Fundamentos en Ciencia de Datos 17 Julio.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:32:27
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:00:25]** Hola. Hola, hola. Hola, tuvieron su recreo, ¿verdad? O no. No, mira, la verdad, estábamos... O sea,

**[0:00:38]** estábamos tratando de ver si teníamos clase de práctica o no, porque el profe con la teoría

**[0:00:45]** no nos quedó claro si íbamos a tener práctica o no. Entonces creo que nos quedamos todos pegados

**[0:00:55]** tratando de ver si sí o si no, no sé, había como mucha confusión. Ah, ok, ya, está la mayoría de la

**[0:01:02]** gente aquí, ¿ustedes tienen un chat entre ustedes? ¿Dónde se... daten las noticias? Claro, tenemos

**[0:01:10]** un Whatsapp por ahí que volvió la clase. Ah, ya, entonces, ¿no tuvieron recreo? ¿No tuvieron

**[0:01:16]** tiempo como para irse a hacer un tecito o ir al baño o algo así? No, parece que no.

**[0:01:21]** Pero más de... más de confusión que de hacer algo. Ya, entonces, empecemos a las 8-10,

**[0:01:27]** le doy 9 minutitos así flash para que tengan un mini recreo como para, no sé, hacer senté o

**[0:01:32]** cualquier cosa, ¿ya? ¿Lo pueden avisar también en el chat general? Por favor, que tenga. Ya,

**[0:01:37]** yo me voy a quedar aquí conectada, pero la clase oficial empezaría a las 8-10. Eso.

**[0:01:45]** Hola, hola. Hola, tengo gente. Hola. Entonces, vamos empezando con tiempo para que la gente se vaya

**[0:10:01]** incorporando también para volver como del mini recreo improvisado. Entonces, para empezar por

**[0:10:10]** mientras podemos partir hablando de la clase anterior, no de materia nueva. Entonces,

**[0:10:16]** la clase anterior vimos, bueno, en nuestro laboratorio se llamaba calidad de DAB y estuvimos

**[0:10:23]** viendo algunas nuevas funciones de esta librería pandas que habíamos visto para poder limpiar

**[0:10:31]** datos tabulares, ¿no es cierto? Para eliminar datos no útiles, eliminar tal vez o tratar

**[0:10:38]** inconsistencias y también tratar, por ejemplo, datos duplicados. Y habíamos quedado con un

**[0:10:45]** ejercicio donde estoy acá, creo. Soy esto, no soy esto. Uf, tengo dos pestañas y estoy confundida

**[0:11:00]** cuando tengo un partido, creo que es... TV o no sé. TV. TV. Ok. Entonces, esta era la práctica

**[0:11:19]** que habíamos visto la clase pasada. Va a ser un poco extraño para mí estar mostrando la pantalla

**[0:11:28]** porque no estoy con mi configuración de siempre. Entonces, no estoy con el mouse. Entonces,

**[0:11:34]** me voy a tardar un poquito en hacer las cosas. Ya, pero esto era lo que habíamos visto. Y había

**[0:11:40]** quedado un ejercicio, ejercicio del cual todavía no subo las respuestas. Entonces, quería,

**[0:11:46]** primero, hablar un poco del ejercicio y hablar de alguna parte que les haya como costado y también

**[0:11:53]** ver cómo las respuestas en vivo y en directo, de manera rápida que ya la hicieron y de manera

**[0:11:59]** lenta, así es que les costó. Entonces, el ejercicio era tomar esta tabla, que era de la información

**[0:12:07]** de vos, esponja de Wikipedia, creo que no mal, sino mal recuerdo, de los capítulos de vos,

**[0:12:11]** esponja de Wikipedia, hace mucho tiempo, que puede haber cambiado. Y había que

**[0:12:15]** hacer toda esta instrucción. Había que hacer que esta tabla de juguete contenga solo los datos

**[0:12:22]** de las temporadas. O sea, que había que eliminar las películas. Había que eliminar duplicados. Había

**[0:12:28]** que reemplazar los valores NAND por Tobias, o TVA. Dejar todas las fechas solo con el año,

**[0:12:34]** eliminar las temporadas que tengan más de 30 capítulos y después ordenar la tabla por

**[0:12:39]** número de temporada. Entonces, me voy a ejecutar la anterior. Por mientras, lo primero era eliminar

**[0:12:54]** los duplicados. Entonces, ¿cómo hacíamos eso? Voy a estar moviéndome con el mouse tan raro.

**[0:13:08]** Ahí está mi tabla. Entonces, ¿cómo, cómo elimino duplicados aquí en esta tabla?

**[0:13:14]** Entonces, aquí si es que hago el drop duplicates, me va a dar a eliminar los duplicados que tengan la

**[0:13:35]** fila tal cual igual. Creo que era sin considerar el ID, porque el ID no se considera como parte de la fila.

**[0:13:41]** Entonces, hacer un drop duplicates. Recordar que también cuando ocupo el drop duplicates,

**[0:13:48]** si es que hay algo que sea como un ID, puedo utilizar el ID para ver si es que hay duplicados.

**[0:13:55]** Entonces, en este caso, si es que existe un ID, puedo ocupar la columna ID y si es que no existe un

**[0:14:02]** ID, puedo ocupar lo que yo. Habla.dropduplicates. Ok. Entonces, voy a copiar lo que me mandaron

**[0:14:19]** en el chat y me voy a demorar porque esto es un trabajo en proceso porque mi mouse está raro.

**[0:14:25]** Ahí ven lo que estoy compartiendo porque, por ejemplo, ahora yo estoy viendo otro notebook. ¿Lo ven o lo

**[0:14:34]** ven en blanco o no ven nada? No, en este momento está el notebook el que está compartiendo al

**[0:14:39]** principio y aparece un mensaje que dice favor a alejar esta ventana de la aplicación compartida.

**[0:14:44]** Pero está como pegado así.

**[0:14:46]** Ah, ok. Raro. Bueno, hacemos un drop duplicates. Con mi ventana original, por favor.

**[0:14:58]** Ahí. Eso es lo que me habían escrito y esto se llama tabla. Así que debería ser legal.

**[0:15:04]** Ahí tengo un drop duplicates. Ok. Entonces, esto en teoría debería funcionar. ¿No es cierto?

**[0:15:14]** Y no tengo inspección visual. Parece que no tengo como nada, nada repetido. Ya, me parece.

**[0:15:26]** Si es que una cosa, si es que yo quisiera usar un ID, por ejemplo, un ID en este caso podría

**[0:15:33]** ser la columna temporada. ¿Por qué? Porque solo puede haber una temporada 5, una temporada 1 o

**[0:15:40]** una película que se llama, no se, me voy a esponjar la película. No puede haber otro

**[0:15:45]** poco de esponja en la película. Entonces, si es que yo miro la tabla, podría identificar que

**[0:15:50]** estas temporadas podría ser un ID o simplemente eliminó ocupando drop duplicates y que me busque

**[0:15:56]** exactamente el match de toda, toda, toda la info. Ok, ¿Ambas insorables? Sí.

**[0:16:03]** Nada, consulta. ¿Y por qué tenías dos temporadas 7? En vivo una tenías 7 temporadas 7,

**[0:16:08]** episodios 26 y otra temporada 7, episodios 50.

**[0:16:11]** Ah, ya. Entonces, ya hay que usar el ID de temporada. Está haciendo inspección visual y no lo vi.

**[0:16:17]** Pensé que era el 5 el que tenía el problema y no vi la colisión. Aquí hay una temporada 7 y acá

**[0:16:22]** hay una temporada 7. Entonces, aquí tengo un problema y aquí yo tengo que tomar una decisión.

**[0:16:26]** Entonces, la ideal es simplemente tomar la decisión de ocupar temporada como ID y ocuparla

**[0:16:35]** para hacer el drop. Y aquí uno podría decir, bueno, ¿con cuál me quedo? Pero nosotros no

**[0:16:41]** vamos a tomar decisiones difíciles y simplemente vamos a ocupar el drop duplicates de temporada,

**[0:16:45]** o sea, sin drop duplicates y que ocupa temporada para buscar los duplicados. Y nos vamos a quedar

**[0:16:53]** con la primera que encuentre, ok, la primera como la original. Y con esa nos vamos a quedar con

**[0:16:58]** el orden que estaba la tabla. Simplemente así y así nos quitamos ese ese problema dense.

**[0:17:03]** Entonces, lo que tenemos que hacer es ocupar el drop duplicates, pero ocupando el subset.

**[0:17:13]** No sé si se acuerdan. Y voy a hacer un lindo copypasteo porque les quiero empezar a escribir

**[0:17:18]** en este tenglado y equivocarnos. Entonces sería el drop duplicates, el mismo de arriba,

**[0:17:22]** solamente que vamos a indicar el subset y le vamos a poner temporada. Y ahora en este resultante

**[0:17:31]** era la 7 y la colisión 7. Aquí está la 7 y ahora no hay otra 7. Entonces, eso no se

**[0:17:40]** elimina el problema de la colisión. Ahora, ¿qué pasa? ¿Qué tabla? Si aquí yo no le pongo

**[0:17:45]** in place o algo así, no se va a actualizar. Entonces, para que se actualice de verdad tengo

**[0:17:50]** poner tabla igual a tabla drop duplicates, pero si no la tabla original no cambia. Y ahora sí,

**[0:18:00]** mi tabla original ya no tiene los duplicados. Ok, ya. Luego viene, sé que sigue en el orden

**[0:18:12]** que ya les puse, dice reemplazar valores NAN por TBA. Y esto es una función que habíamos

**[0:18:19]** visto o se puede hacer fácil con una función que habíamos visto en la yoantía. No sé si

**[0:18:28]** se acuerdan que hay una función específica que reemplaza los NAN. ¿No?

**[0:18:52]** Los clientes. Ah, perdón, perdón, perdón. Ah, ya. Filna, ya. Es esa. Es la que se

**[0:18:59]** llama filna. Entonces nosotros habíamos visto que existe el drop NAN para eliminar

**[0:19:04]** los NAN, el isna para ver si algo es NAN y también está el filna para reemplazar los

**[0:19:13]** valores que son NAN. Entonces sería tabla, punto, y aquí voy a copypaster del chat,

**[0:19:20]** sobre lo más grande del chat, punto filna y le ponemos TBA. Y aquí sí es que no, no.

**[0:19:27]** Hay un problema con eso sí, que ahí te lleno, bueno aquí no sé si,

**[0:19:32]** la verdad no me fijé en los datos, la verdad, pero te voy a llenar todos los NAN con el TBA

**[0:19:36]** que quizás no sea las columnas que estemos buscando. No sé si son todas las verdad las que hay que

**[0:19:39]** hacer eso. Aquí yo puse a reemplazar valores NAN, entonces no especificé el columna,

**[0:19:44]** así que se asume que son todos, no más. Ah, ya, no, no, me refiero para el contexto los datos.

**[0:19:49]** Ah, no, no, vamos a poner TBA en general, no, no me compliques tanto con el ejercicio. En este

**[0:19:55]** caso, cuando hacemos filna con toda la tabla, tomamos todas las columnas,

**[0:20:00]** si es que quisieras solamente una columna especificada, le especifico que solamente en esa columna,

**[0:20:04]** pero aquí si lo hago global, se hace global. Y esto tampoco le hace in place, o sea,

**[0:20:10]** no modifica la tabla original, entonces para que se modifique la tabla original tengo poner TAB,

**[0:20:14]** igual la tabla firma. Y así quedaría con lo indicado. Y así solamente eso es reemplazar

**[0:20:24]** valores NAN. No me complique mucho con la idea. Esto podría ser un poquito más complicado,

**[0:20:30]** porque aquí hay muchas maneras de resolver esto, de dejar todas las fechas solo con el año, porque

**[0:20:36]** las fechas vienen con la descripción del día y del mes y a veces vienen de esta manera. Vienen,

**[0:20:46]** en vez de decir 16 de agosto, vienen por ejemplo 30 guión, marzo guión. Y ahí tengo un problema.

**[0:20:52]** Ok, entonces tengo que encontrar alguna manera de limpiar esto y quedarme solo con el año,

**[0:20:58]** porque en este caso el ejercicio dice solo con el año. Yo podría quedarme solo con el día o quisiera,

**[0:21:05]** no sé, dejarlo en otro formato, etcétera. Entonces aquí no especifica... Ah, no mentira,

**[0:21:11]** si especifica. Dice que las tengo que dejar en stream. Ok, no me dice que las dejen tipo

**[0:21:17]** daytime o time delta o lo que sea. Me dice en stream. Entonces hay muchas formas de resolver esto,

**[0:21:22]** lo puedo manejar como si fuera el año y después pasarlo stream o manejarlo como stream.

**[0:21:35]** ¿Tablas replays en Epenant TV? Sí, también se puede ocupar un replays. No hay problema con

**[0:21:43]** ocupar el replay, también se considera valio. Entonces, ¿cómo atacamos el problema de las fechas?

**[0:21:50]** Creo que la manera más fácil es el manejo de stream, porque ya las fechas ya están en stream,

**[0:21:59]** por ejemplo aquí tengo la embarrada. No hay que arreglar el nombre de las columnas.

**[0:22:12]** Los nombres de las columnas yo no pedí, ¿qué los arreglaran? ¿Qué pasa con los nombres de las

**[0:22:18]** columnas? Me puede haber equivocado en alguna columna. Necesito explicación porque no entendí el 100%

**[0:22:36]** de la pregunta, por favor. Hay que, como la columna tiene espacio, entonces cuando uno empieza

**[0:22:47]** a escribir la columna dice que no se reconoce esa columna. Entonces yo lo que hice volve a

**[0:22:53]** escribir los columnas, pero con guión bajo, en vez de espacio puse guión bajo en los nombres.

**[0:23:02]** No podías acceder a las columnas porque las columnas tenían espacios en los nombres. Bueno,

**[0:23:07]** eso lo hablé en un momento que aquí voy a ocupar el tabla .columns que ya lo vimos,

**[0:23:14]** lo vimos creo que la primera llanta para acceder a los nombres de las columnas de la tabla,

**[0:23:18]** ok. Entonces aquí están todos los nombres de las columnas y por ejemplo aquí dice comienzo

**[0:23:23]** a Estados Unidos y tiene espacios entre ellos. Entonces ¿Qué significa que tengo un espacio?

**[0:23:27]** Que yo no puedo hacer tabla .comienzo Estados Unidos por ejemplo, porque eso me va a dar error.

**[0:23:35]** Entonces cuando yo quiero acceder a una columna que en el nombre tiene espacios puedo ocupar los

**[0:23:40]** operadores que son los corchetes. Y ahí tengo que poner el nombre entre comillas que pueden

**[0:23:46]** ser comillas simples o comillas dobles, espero haberlo escrito bien. Y ahí yo puedo

**[0:23:51]** acceder a los datos de eso. Entonces si es que a mí me molesta ocupar esta forma,

**[0:23:59]** puedo cambiarle los nombres. Pero no es que esté incorrecto sino que es una forma distinta. Si es

**[0:24:06]** que yo quisiera para manejarlo todo con el operador .le puedo cambiar los nombres a los

**[0:24:10]** columnas y no hay problema. Pero que tengan un espacio no me impide tratarlas. La sigo

**[0:24:17]** podiendo como manejar y acceder. Solamente tengo que ocupar los operadores que son los corchetes.

**[0:24:29]** Esto podría ser un poquito más complicado porque no tengo que acceder a una segunda columna sino que

**[0:24:44]** tengo que acceder a hartas. Entonces puedo acceder a cada columna a mano o puedo hacer algún foro.

**[0:24:49]** Y qué es lo que tengo que hacer. Uy alguien me escribió en el chat y no lo mire. Usaría reggae,

**[0:24:58]** pero no es lo más práctico. Puede ser una expresión regular pero pueden no ser lo más

**[0:25:03]** Entonces lo que tenía antes para acceder a la tabla me voy a colar de aquí.

**[0:25:08]** Si yo quiero acceder tendría que hacer un str, ¿se acuerdan? str para poder acceder y hacer operaciones

**[0:25:16]** de string. Bueno lo primero es que me tengo que si o si como por por medida de seguridad tendría

**[0:25:24]** que hacerle un strip. No sé si se acuerdan del strip. Elimina como los espacios de más que

**[0:25:29]** hay al principio del string y al final del string. Solo por si acaso. Ok eso es lo único que hace si

**[0:25:37]** es que hubiera espacios al principio y al final. Entonces aquí yo tengo que empezar a pensar en

**[0:25:43]** patrones. ¿Qué me pasa? Que los strings aunque tengan o los datos aunque tengan distinto formato

**[0:25:52]** por ejemplo aquí uno de mayo y aquí 19 guión julio guión no sé cuánto. Lo que tienen es que

**[0:25:57]** el año está siempre al final. Ok eso es como una forma fácil de de identificarlo. El año está

**[0:26:04]** siempre al final. Entonces el año está siempre al final y siempre son cuatro números. Ok entonces

**[0:26:11]** una forma fácil de acceder al año sería simplemente hacerle un strip para ver que no tenga

**[0:26:19]** espacios de más en blanco al final o sea saber que al final si o si haciéndole un strip al

**[0:26:25]** final sé que sí o si tiene que estar el año y no hay espacios en blanco y acceder a los últimos

**[0:26:31]** cuatro elementos. Entonces como accedo a los últimos cuatro elementos serían menos cuatro desde el menos

**[0:26:38]** cuatro en adelante yo quiero todo el string. ¿Tiene sentido? Debería. Vamos a correrlo para ver si

**[0:26:45]** está bien. Ok entonces funciona. Si se dan cuenta me funciona con el comienzo de Estados Unidos.

**[0:26:50]** Entonces si yo le hago string punto strip y después string y hago esta operación que es el slice de

**[0:26:57]** string me quedo con los años y esto lo puedo hacer. Bueno tengo que reemplazarlo para que me quede todo

**[0:27:03]** igual y esto lo puedo hacer para cada columna a mano o sea tabla comienzo de Estados Unidos tabla

**[0:27:07]** final de Estados Unidos. No acuerdo los nombres que les puse. Para tabla comienzo de Estados

**[0:27:17]** Unidos final Estados Unidos comienzo de Hispanoamérica final Hispanoamérica comienzo de España y final

**[0:27:21]** España. Lo puedo hacer a mano escribiéndolo o puedo hacer un for. Ok for y in alguna tabla o sea

**[0:27:32]** alguna lista que contenga todos los nombres y luego hacer la operación y escribirla. Ok pero la

**[0:27:38]** operación bueno una forma de hacerlo se les ocurre otra también debería estar correcta o

**[0:27:44]** sea que llegan a la misma resultado. Una forma de hacerlo es así. Solamente quedan agregando un for.

**[0:27:57]** El extract es que si le pones de cuatro quizás debería funcionar no estoy tan segura porque

**[0:28:09]** quizás te funcionan pero va a buscar números seguidos pero te puede generar problemas o te

**[0:28:17]** puede generar un resultado distinto con un string que tiene el string que tiene la embarra que tiene

**[0:28:26]** como muchas fechas pegadas como toda seguida. Ahí te puede generar quizás un error pero una buena

**[0:28:32]** forma podría hacer ocupar el extract. Estoy hablando de la persona que me está escribiendo en el chat.

**[0:28:38]** Se supone que consideraba los últimos cuatro dígitos. Sí. Sí.

**[0:28:50]** Entonces esto para escribir el for en rápido me lo voy a copiar. Me lo voy a copiar y lo voy a

**[0:29:06]** copiar acá abajo. Entonces lo mismo que hicimos en la celda arriba lo voy a hacer en un for.

**[0:29:13]** Así. Entonces hago un for que tenga una variable cualquiera aquí le pueden poner el nombre que

**[0:29:19]** quieran un for normal y que dentro y tere con los nombres de las columnas que yo quiero modificar

**[0:29:26]** y luego que acceda esa columna y la haga igual a la operación que teníamos acá arriba. Esa es

**[0:29:33]** la operación que escribimos en la celda arriba sea tabla nombre de la columna punto str punto

**[0:29:38]** str punto str y acceder a la posición que yo quiero y eso me cambia mi tabla tabla ya eso con

**[0:30:02]** eso después dice eliminar películas y temporadas de más de 30 capítulos. Entonces tengo que eliminar

**[0:30:10]** las películas y también las temporadas. Entonces como hago eso aquí como digo no hay una sola

**[0:30:20]** respuesta correcta esto se puede hacer de muchas maneras o puedo buscar algún patrón que me sirva

**[0:30:26]** para todo. Ahí me escriben el chat parece. Bueno una forma de buscar un patrón por ejemplo aquí

**[0:30:46]** viendo esta tabla particularmente para el caso esta tabla si me doy cuenta aquí tengo el nombre de

**[0:30:51]** la temporada y tengo los episodios de cada temporada. Entonces las temporadas tienen aquí

**[0:30:56]** les podría sacar la media si quisiera pero visualmente las temporadas que no son películas si o si tienen

**[0:31:03]** más de un capítulo o más de un episodio por ejemplo la temporada 5 tiene 20 la temporada 10

**[0:31:08]** tiene solo 11 capítulos la temporada 13 tiene muchos pero si se dan cuenta todas las temporadas

**[0:31:14]** tienen al menos 10 capítulos. ¿Qué pasa en el caso de las películas? Como las películas son

**[0:31:21]** solamente una película no son varios episodios el número de episodios siempre es 1 para las

**[0:31:28]** películas. Entonces aquí notando este patrón una forma fácil de hacer esto para eliminar las

**[0:31:35]** películas es decir voy a eliminar las filas que tengan solamente un episodio porque si solamente

**[0:31:41]** tienen un episodio son una película. Y además voy a eliminar las filas que tengan un solo

**[0:31:49]** episodio o que tengan más de 30 episodios. ¿Por qué? Porque ese es el otro criterio que me pidieron

**[0:31:58]** eso es una forma y eso lo podemos hacer con los filtros que habíamos visto antes entonces bueno

**[0:32:04]** esto se puede hacer de más manita se puede hacer también buscando números en la tabla de o

**[0:32:11]** sea letras en la tabla de temporada pero lo podemos hacer con las consultas que habíamos visto

**[0:32:21]** entonces me meto a tabla punto episodios y tengo que aquí lo hice al revés tengo que

**[0:32:26]** decir que tenga más de un episodio si o si estas son las con las que me quiero quedar me quiero

**[0:32:31]** quedar con las que tengan más de un episodio porque así sé que no son una película y

**[0:32:36]** como que como quiero eliminarlas de que tengan más de 30 capítulos me quiero quedar con las

**[0:32:40]** que tengan menor o igual que 30. Esas son las que quiero conservar. Ok tengo un problema no

**[0:32:55]** lo puedo tratar como número ¿Por qué será? Debe ser porque si hago tabla punto describe o tabla

**[0:33:01]** punto info bueno tabla punto info ¿Qué pasó? Episodios no está como número está como

**[0:33:11]** objeto o sea que estoy teniendo problemas entonces nosotros esto ya lo vimos de cómo

**[0:33:17]** enfrentarlo qué pasa si tengo un tipo de dato que no me está funcionando nosotros vimos que se

**[0:33:22]** podía hacer as type si se acuerdan para cambiar el tipo de datos de una columna entonces lo que

**[0:33:28]** tengo que hacer es poner tabla punto episodios que es la columna que yo quiero modificar tiene

**[0:33:37]** que ser igual a tabla punto episodios punto as type y aquí le puedo poner un tipo que puede

**[0:33:42]** ser numérico puede ser entero puede ser flotante pero aquí están con puros enteros no es

**[0:33:47]** como que yo tenga 0,5 episodios ok entonces le voy a poner que sean enteros entonces corriendo

**[0:33:54]** esto ahora la columna es de enteros entonces ahora sí puedo hacer consultas haciendo que

**[0:34:00]** sea mayor que uno y menor igual que 30 ok ahora funciona ¿Por qué no funcionaba antes? Porque

**[0:34:07]** tenía estaba como puesto como que los tipos de datos no eran numérico entonces no podía

**[0:34:12]** hacer la consulta tabla entonces ahí me quedo y la última creo que no no pude lo desortear

**[0:34:29]** ya la última era desortear o sea de ordenar no es cierto si no va el recuerdo dónde está la

**[0:34:42]** última instrucción aquí ordenar la tabla por un número de temporada como se hace eso estoy

**[0:34:53]** bajando para buscar una celda al final no es por si acaso me faltó poner esa instrucción aquí

**[0:34:58]** mal a mí no quiero escribir porque se mueve todo el notebook si escribo entonces alguien se le ocurre

**[0:35:16]** con mordeno estoy viva no si esto me escuchan verdad si se escucha ah ya supe ya por 5 segundos

**[0:35:42]** me asusté que como saqué las camaritas para que no vean como el trocito como negro que me

**[0:35:48]** decía que se veía o gris ya no veo si que hay interacción entonces ya entonces lo que nos queda

**[0:35:56]** es ordenar la tabla por número de temporada no se se acuerdan pero creo que fue la primera clase

**[0:36:03]** vimos una función que era para ordenar la tabla que se llama el sort values si era sort values

**[0:36:18]** entonces el sort values es el que nos sirve aquí pero no nos sirve el sort values solito sino que hay

**[0:36:24]** que pasarle la columna por la cual nosotros queremos tener el criterio para ordenar y en este caso el

**[0:36:32]** criterio es temporada porque nos dijeron que ese era el criterio explícitamente en el ejercicio

**[0:36:37]** entonces tengo que poner tabla punto sort values porque si se llama la función tengo

**[0:36:44]** que ponerle bye porque así se llamaba el parámetro y tengo que ponerle temporada

**[0:36:53]** temporada esto me puede dar error porque a mí todo me puede dar error no me dijeron y ahí está ordenada

**[0:37:02]** por número de temporada si no se ordenará bien por orden numérico puede ser porque temporada puede

**[0:37:12]** estar con otro tipo de dato podría estar por ejemplo con el tipo de dato string y tal vez ahí tendría

**[0:37:18]** problemas para ordenar pero en este caso se está ordenando bien entonces no necesito cambiar el tipo

**[0:37:25]** de datos el que tuviera problemas puede ser por cambiar el tipo de dato y ahí tendría que simplemente

**[0:37:30]** cambiar ok entonces ese era el ejercicio y vimos como la solución aquí paso a paso alguna duda

**[0:37:38]** con esto porque era solamente ocupar creo las funciones que vimos pero si hubo algo desconocido

**[0:37:45]** mejor que me lo pregunten ahora no hay dudas con esto todo claro una consulta tengo la duda en la

**[0:38:14]** primera que pasa si los dos puntos se pone antes del menos cuatro no acá sino que en el ejercicio

**[0:38:23]** en lo cosita del estingo no

**[0:38:30]** aquí si ahí qué pasa si ponen los dos puntos antes de menos cuatro los dos puntos antes del menos

**[0:38:39]** cuatro eso significa que yo voy a el operador slice tiene inicio dos puntos final entonces

**[0:38:48]** aquí le estoy diciendo que empieces desde el menos cuatro hasta el final entonces si yo hago lo

**[0:38:55]** contrario le pondría inicio 2 puntos menos 4 entonces le estaría diciendo que quiero todo el

**[0:39:03]** string menos el año eso es lo que me daría te doy el ejemplo le podemos pasar 16 de abril de

**[0:39:17]** 1990 y le voy a poner menos 4 no me dijiste 2 puntos menos 4 entonces debería darme todo el string

**[0:39:29]** excepto el año y te da cuenta me da todo el string menos los últimos cuatro caracteres que justo

**[0:39:38]** aquí son el año de nada recordar que siempre el operador slice tiene inicio dos puntos final si

**[0:39:53]** le quieres poner algo más fácil es dos puntos salto pero nosotros normalmente no ocupamos esto

**[0:39:59]** entonces si es que yo omito algunos de estos números va a tomar que es desde el inicio del

**[0:40:06]** string si yo mito el final va a decir que del inicio hasta el final del string o sea si yo

**[0:40:11]** pongo nada dos puntos nada me va a dar todo el string y si es que yo aquí estoy poniendo como

**[0:40:17]** por ejemplo numeritos me daría desde la tercera posición hasta el final del string desde la

**[0:40:23]** tercera posición hasta la quinta posición y así ya con esto entonces puedo cambiar de puedo ver

**[0:40:36]** la materia de hoy entonces voy a cambiar de algo de algo extra pero siento que no vale la pena tanto

**[0:40:56]** discutiendo y si ya que técnicamente cuando nosotros trabajamos con datos tabulares una

**[0:41:06]** forma como correcta de manejar los datos es siempre no tener valores en las columnas entonces por

**[0:41:14]** ejemplo en las columnas están los valores estados unidos hispanoamérica y españa pero esos no

**[0:41:19]** son esos son valores ok entonces ahí no deberían estar en los nombres entonces deberían ir debería

**[0:41:29]** existir una columna de lugar y ahí deberían estar los valores estadounidenses entonces un ejemplo

**[0:41:39]** era como o sea un ejercicio extra era como se podía ordenar la tabla en esto no me quiero

**[0:41:46]** detener tanto tanto aquí entonces les aconsejo como si es que les interesa este ejercicio ver la

**[0:41:52]** solución cuando la suba que debería subir después de la clase o si es que me queda tiempo al final de

**[0:41:58]** la clase podemos ver esto porque es un poco difícil es un poco más complicada de explicar la

**[0:42:03]** solución no la voy a tratar ahora pero si les interesa me pueden preguntar al final de la

**[0:42:08]** clase por ejemplo eso me va a quedar pendiente por ahora entonces lo de hoy día cambiando de

**[0:42:15]** tema y lo que tenemos que ver hoy día es esta que la subí hace poco hace como 40 minutos de que

**[0:42:25]** debería estar disponible en el campo una cosa y esta es un poquito más extensa pero debería

**[0:42:33]** haber materia que ya conocen entonces pues debería poder saltármela debería primero voy a encender

**[0:42:40]** el notebook porque se nos está encendido el otro sí que tenemos que ver la práctica se llama en la

**[0:42:48]** librería nampa más análisis descriptivo pero según entendí han visto harto de python y también

**[0:42:55]** hemos visto sin querer harto de nampa y entonces hay muchas cosas que creo que puedo omitir si es

**[0:43:01]** que en algún momento se pierden porque yo omití algo que ustedes no saben me detienen me

**[0:43:07]** dieron al tiro y me dicen oye eso yo no lo sé por favor menciona yo ya vamos al momento entonces

**[0:43:16]** nampa y es una librería como pandas no es cierto que básicamente lo importante es que es eficiente

**[0:43:22]** porque porque python es muy lento por cómo está construido entonces nampa es un paquete diseñado

**[0:43:29]** para computación científica y también conocido como computación orienta arreglos y lo importante

**[0:43:34]** es que nos permite hacer operaciones de forma eficiente si yo trato de hacer operaciones las mismas

**[0:43:39]** operaciones con python nativo versus con nampa y con nampa y va a ser mucho mucho más rápido y eso

**[0:43:46]** es súper importante cuando estamos tratando de analizar datos en especial gran cantidad de datos

**[0:43:51]** porque necesitamos tener los análisis pero también queremos que esto sea rápido no

**[0:43:56]** cierto no queremos que se demore una hora en analizar 100 mil datos no es la idea entonces

**[0:44:03]** como funciona nampa y bueno aquí lo importamos ya lo importaba en otros notebooks porque lo hemos

**[0:44:09]** ocupado sin querer y la la típica convención que se tiene es importarlo y ponerle el sobrenombre de

**[0:44:17]** np entonces nampa y haz np ella la libre ella existe y esto trabaja con un tipo de datos que

**[0:44:26]** se llaman arreglos entonces normalmente como defino los arreglos yo pongo np punto array y adentro

**[0:44:32]** normalmente le paso una lista una lista de python y esto se va a transformar en un arreglo y eso es un

**[0:44:39]** tipo de dato de nampa entonces si yo pongo print type npa ray y le paso una lista con algo me va a decir el

**[0:44:46]** tipo de dato entonces me dice me dice que el tipo de dato es nampa y punto n de array entonces un

**[0:44:55]** arreglo multidimensional de nampa entonces yo puedo definir arreglos como dije con np punto

**[0:45:02]** array utilizando listas entonces le paso a la función una lista y esta lista puede ser una

**[0:45:08]** lista de listas o una lista simple y sean a construir estos arreglos entonces normalmente cuando yo

**[0:45:14]** imprimo una lista de python están separadas por copas los números como los elementos cuando

**[0:45:23]** yo imprimo una regla así como ver lo fácil una regla de nampa y otro tipo no sea un tensor

**[0:45:29]** u otros tipos de datos están separados por espacio si se dan cuenta de una forma visual de ver que eso

**[0:45:35]** no es una lista de python algunas cosas como características o cosas tipos de datos dimensiones

**[0:45:44]** que le puedo sacar fácilmente algo que yo sé que es un arreglo de nampa y le puedo sacar la

**[0:45:49]** invención le puedo sacar el tipo de dato le puedo sacar el shape la forma que ya habíamos visto

**[0:45:54]** que era cuando trabajamos con una tabla y también le puedo trabajar le puedo sacar el número de elemento

**[0:46:00]** recordemos que el shape es la forma entonces me va a dar el número de filas el número de columnas o si

**[0:46:09]** tuviera más dimensiones las otras dimensiones entonces por ejemplo aquí el n es una básicamente

**[0:46:16]** algo parecido una lista y el m es una matriz una matriz de dos filas y tres columnas entonces

**[0:46:24]** la el shape o la forma de n simplemente me da 3, nada porque técnicamente es un vector plano

**[0:46:33]** un cierto solamente que tiene tres columnas tiene tres elementos así que se toma como tres tres

**[0:46:39]** columnas en sí y esto es una matriz y tiene dos filas y tres columnas entonces me está diciendo

**[0:46:45]** que son dos filas tres columnas cuando está así yo sé que es un vector planito y cuando

**[0:46:52]** ya tiene más de una dimensión yo ya sumo que es una matriz trimencional y ya va a tener la idea de

**[0:46:57]** que primero son las filas y a posar las columnas recordar que como esto es un tipo de dato que

**[0:47:08]** tiene un orden es ordenable no es cierto le puedo sacar y también como si tiene un orden y

**[0:47:14]** agrupa de elementos le puedo aplicar el len que una operación de python que me dice el

**[0:47:19]** tamaño y el len siempre va a ser igual al primer elemento del shape ok el primer elemento de la

**[0:47:27]** forma bueno en un arreglo similar a lo que le pasa con pandas el tipo de dato es el tipo de

**[0:47:38]** dato que engloba a la mayoría ok o sea el tipo de dato que puede englobar a todos los datos

**[0:47:43]** entonces por ejemplo si yo tengo un arreglo que tiene puros enteros sea va a decir que es de

**[0:47:49]** tipo entero pero luego si es que yo le agrego un elemento que es de tipo flotante el tipo de

**[0:47:57]** datos del arreglo va a cambiar va a cambiar a flotante porque porque necesita un tipo de

**[0:48:02]** dato para englobar todo lo que tiene o si no va a dar problema entonces todos los datos de

**[0:48:06]** adentro van a pasar a flotante entonces si yo me creo el arreglo normal tengo un 2 3

**[0:48:13]** 4 y se ven como enteros y luego se agrega un flotante después todos pasan a flotante

**[0:48:19]** porque se le ven ahí el puntito ya y como dije como como creo arreglos de nampa y vimos que podemos

**[0:48:28]** crearlo con np.array y le pasamos simplemente una lista pero también hay unas funciones

**[0:48:33]** útiles para crear algunos ya con ciertas características por ejemplo ceros crea un

**[0:48:39]** arreglo de ceros y esto tiene un tamaño y se lo puede pasar acá dentro once crea un

**[0:48:45]** arreglo lleno de unos arrange crea un arreglo contenido se parece al se parece un 4 crea un

**[0:48:54]** arreglo conteniendo los números entre a y b menos 1 con un aumento de c y el line space el

**[0:49:02]** lint space crea un arreglo de n valores entre a y b y esta es como la la el esquema de los

**[0:49:11]** parámetros como el orden en que van los parámetros a b y c en el arrange y lint space a b y n donde a y b

**[0:49:19]** delimitan como el el rango no es cierto y en este caso en el arrange el c es el salto y el en el caso

**[0:49:26]** de lint space este tercer elemento es el número de valores o sea aquí tengo ejemplos para once

**[0:49:33]** para ceros y para un random que no lo menciona aquí que es random punto random int o sea va a

**[0:49:38]** ser un una matriz al azar de números enteros entonces me crea mi matriz de unos mi matriz de

**[0:49:48]** ceros y mi matriz con números al azar ok entonces aquí con número al azar va a tener más argumentos

**[0:49:56]** como que yo le doy el el rango en el que quiero los números y en este caso le voy a dar la forma

**[0:50:03]** de la matriz y acá si se dan cuenta yo también en el once y en el ceros dentro de los paréntesis

**[0:50:08]** el argumento que le doy es la forma que te quiero que tenga el arreglo de salida el arreglo que se

**[0:50:14]** produzca de esto a los arreglos se le puede modificar la dimensión simplemente con un reshape ok pero

**[0:50:26]** tengo que tener cuidado con que siempre el shape coincida con el número total de elementos que

**[0:50:33]** posee por ejemplo si yo tengo un un arreglo con 10 elementos y le quiero hacer un reshape

**[0:50:40]** para que sea una matriz de tres por tres eso no me cabe porque en una matriz de tres por tres no

**[0:50:47]** me caben los 10 elementos que tengo entonces ahí eso me va a dar error entonces tengo que tener

**[0:50:51]** cuidado con entonces aquí tengo mi arreglo a que es básicamente un vector de puros unos y

**[0:51:00]** mi arreglo b que es una matriz de tres por dos y lo que voy a hacer es que al a le voy a

**[0:51:06]** cambiar el shape estas son dos formas de cambiar la cambiar la forma le voy a decir que el shape de

**[0:51:12]** a va a ser igual a 5,2 y el b le voy a hacer un reshape a 6 entonces lo que era un vector lo

**[0:51:21]** voy a pasar una matriz y lo que era una matriz lo voy a pasar un vector y este es el resultado y

**[0:51:27]** si ustedes descomentan esta línea y la corren como b tiene más de dos elementos esta línea

**[0:51:34]** les va a dar un error porque porque es una forma incompatible con el número de elementos que tiene

**[0:51:42]** b aquí está un ejemplo para el arrange que insisto funciona como un formato y el linspace para mostrar

**[0:51:53]** que generan también arreglos y me sirve cuando necesito como arreglos como con números para no

**[0:51:57]** sé recorrer alguna cantidad específica de números o para tener un conjunto de números que sigan

**[0:52:03]** unas reglas específicas me sirven esto pero eso no más forma como alternativa de crear arreglos

**[0:52:11]** luego me quedan las operaciones con arreglos entonces por ejemplo yo tengo dos arreglos ahí b me lo

**[0:52:21]** estoy creando aquí a mano y ahí tengo su size tengo a size y b size y me doy cuenta que tienen

**[0:52:29]** el mismo número de elementos entonces los arreglos tienen ciertas propiedades si es que yo sumo a

**[0:52:38]** b lo que va a pasar es que se va a hacer la suma por la posición entonces la suma elemento

**[0:52:45]** elementos los elementos que están en la posición 0 se van a sumar los dos elementos que están

**[0:52:49]** chinos se van a sumar los dos elementos que están en la posición 2 y así una suma elemento

**[0:52:55]** el elemento y va a pasar lo mismo con la multiplicación y lo mismo con la resta

**[0:53:00]** Entonces todo esto me va a dar un arreglo de 8, porque como dije la operación se

**[0:53:09]** realiza elemento-elemento. ¿Qué pasa por ejemplo si tengo un arreglo que tiene una

**[0:53:17]** dimensión distinta? Si es que yo trato por ejemplo este arreglo que es c, que solamente

**[0:53:23]** tiene dos elementos, si yo trato de hacer a más c, como tienen número incompatible

**[0:53:29]** de elementos, eso me va a dar error. Entonces tengo que tener cuidado cuando hagas

**[0:53:34]** ahora, eso es cuando yo sumo resto, multiplico algo, alguna operación entre

**[0:53:40]** dos elementos que son arreglos. ¿Qué pasa cuando le sumo una cantidad fija? Algo que

**[0:53:46]** no es un arreglo, así por ejemplo sumar un entero o multiplicar por un entero.

**[0:53:50]** Bueno lo que pasa es que si yo por ejemplo hago a más 5, este 5 se le va a

**[0:53:56]** sumar a cada elemento, o sea el elemento 0, al elemento 0 de a se le va a sumar 5, al

**[0:54:01]** elemento 1 de a también se le va a sumar 5, al elemento 2 de a, o sea, entonces a todo

**[0:54:06]** los elementos se le van a sumar 5 y eso va a pasar si es que yo hago una suma, si es que hago

**[0:54:11]** una resta, división, multiplicación, si es que lo elevo, etcétera, etcétera.

**[0:54:15]** Entonces bueno el mismo ejemplo de multiplicar yo tengo a que era 1.1, no me

**[0:54:26]** tiene la escuela, era 1, 2, 3 o no. El a era 0.1, 0.3, 2.4, etcétera y aquí le estoy

**[0:54:36]** sumando 5, entonces me queda 5.1, 5.3, ese elemento, elemento se le suma el 5 y al b

**[0:54:42]** cada elemento se multiplicó por 0,25. Otra operación es que pueda ser un

**[0:54:48]** ampy, es por ejemplo sacar la media de los valores, sumar los valores,

**[0:54:54]** multiplicar los valores, o sea como la multiplicación de todos los elementos,

**[0:54:58]** la suma de todos los elementos, la media, la desviación estándar, valor mínimo, no sé,

**[0:55:04]** valor máximo, también se puede pedir el mínimo y la posición en donde está el valor

**[0:55:10]** máximo, el argmax ya lo habíamos visto en una ayudante y no se demora nada, si esto

**[0:55:19]** lo hiciera con Python se demoraría más. También en algún momento si es que estoy

**[0:55:25]** trabajando con matrices, algo que hace ampy de manera fácil es sacar la

**[0:55:30]** transpuesta de una matriz, si es que yo tengo, ya es una matriz, yo puedo hacer apunto

**[0:55:37]** t y eso me saca la transpuesta, también puedo hacer sort para ordenar los elementos de

**[0:55:44]** un arreglo, y esto se hace a nivel, por ejemplo aquí, se hace a nivel de fila,

**[0:55:51]** no voy a tocar las demás filas, sino que dentro de cada fila ordeno, no voy a

**[0:55:58]** cambiar el orden de las filas. Ahora, todas estas operaciones que vi, por ejemplo

**[0:56:13]** sacar la media, sacar la desviación, sumar todos los elementos, multiplicar, sacar el

**[0:56:19]** máximo, los vimos solamente con arreglos de una dimensión, pero que pasa si yo

**[0:56:23]** tuviera arreglos de más de una dimensión, por ejemplo aquí, si aquí yo hiciera

**[0:56:28]** un A que fuera una matriz de 3,4, bueno que pasa ahí con la suma, o con el máximo,

**[0:56:34]** con el mínimo, bueno ahora puedo pedirle la suma de todos los números, o puedo hacer

**[0:56:39]** que haga las sumas por filas o por columnas, y eso tengo que agregarle un

**[0:56:43]** argumento que sería como la dimensión, entonces si yo quiero sumar las columnas,

**[0:56:46]** tengo que ponerle punto sum 0, y si yo quiero sumar las filas, punto sum 1,

**[0:56:52]** y esto es un argumento normalmente en las operaciones que se llama axis,

**[0:56:57]** entonces aquí es el primero, entonces no tengo que especificarlo, pero si es que

**[0:57:02]** tuviera alguna otra cosa y quiero hacerlo por filas o por columnas o por alguna

**[0:57:05]** otra dimensión, tengo que poner axis igual a la dimensión que quisiera

**[0:57:10]** especificar, entonces ahí tengo el arreglo original y estoy sumando con sum,

**[0:57:19]** sin ningún argumento adentro, estoy sumando todos los elementos, con 0 estoy

**[0:57:24]** sumando las columnas y con 1 estoy sumando las filas, como me doy cuenta

**[0:57:30]** fácilmente que aquí estoy sumando por columnas y aquí estoy sumando por filas

**[0:57:34]** por la forma del resultado, entonces aquí estoy sumando así como para abajo y

**[0:57:41]** aquí estoy sumando como así para el lado, y eso es fácil de ver porque tengo

**[0:57:45]** 3 filas y 4 columnas, y eso me va a pasar para todas las operaciones que

**[0:57:51]** lo puedo hacer globalmente para todo el arreglo o por alguna dimensión

**[0:57:58]** especifica, por ejemplo aquí estoy haciendo lo mismo pero con el mínimo, entonces puedo

**[0:58:02]** sacar el mínimo global, el mínimo por columnas o el mínimo por filas, ya esto

**[0:58:13]** creo que ya lo saben, no es cierto? todo lo de las posiciones de acceder a

**[0:58:18]** posiciones de elementos porque vieron python básico, no es cierto? esto de

**[0:58:25]** los índices y los corchetes, esto creo que me lo puedo saltar, no vi si alguien me había

**[0:58:32]** escrito en el chat, no veo quejas pero tampoco veo cosas positivas, ya, asumo que el operador

**[0:58:43]** de los corchetes y como funciona los elementos ya lo saben porque vieron

**[0:58:48]** python básico, entonces me lo voy a saltar pero si necesitan repasarlo

**[0:58:54]** avísenme, es importante, entonces me lo voy a saltar pero asumiendo que ya lo

**[0:59:00]** saben, el slicing, voy a asumir también que ya lo saben, o no, ya, solamente para

**[0:59:15]** saber si es que lo tienen más o menos claro, ahí está este arreglo o esta

**[0:59:23]** matriz A que es de tres dimensiones, entonces tengo una pregunta, necesito que

**[0:59:30]** me la respondan, como accedo al elemento, a este elemento, al que es un 4?

**[0:59:35]** Es de dos dimensiones, creo, entonces habría que venir los dos, a ver, 0, 1, ser 1,1 creo, no estoy seguro si

**[0:59:54]** 1,1? no, no, no, no, no, no, 1, 1 y 1 después, así como corchetes, corchetes?

**[1:00:01]** si, corchetes, corchetes, creo, no estoy seguro si, casi, ahi no, casi, ya hay un 0, es tres dimensiones,

**[1:00:11]** ay pensé que tanto, ya faltó el 0 ahí, con tres dimensiones y un 0 ya, ok, por qué, recordándolo

**[1:00:19]** así fácil por si acaso, por qué, por qué, esto es de tres dimensiones, aquí es la primera

**[1:00:25]** dimensión, entonces estoy haciendo que voy a acceder a la primera matriz, porque la como

**[1:00:31]** tengo estos tres dimensiones tengo tres matrices, así lo vamos a ver con la segunda parte del 0,

**[1:00:36]** ahi, perdón, que estoy accediendo a la segunda matriz, que estoy accediendo aquí, entonces ya,

**[1:00:40]** accedí a la segunda matriz, después tengo un 1 para la siguiente dimensión, entonces las matrices

**[1:00:45]** tienen filas columnas, entonces aquí estoy diciendo que voy a acceder a la segunda fila,

**[1:00:50]** o sea, aquí, y cuando ya estoy en la fila, en la tercera dimensión sería el elemento,

**[1:00:55]** o la columna de esto, o el elemento de la fila, entonces el 0 me está diciendo que

**[1:01:00]** voy a acceder al primer elemento de esta fila, y ese es el 4, y así funciona, entonces eso estuvo

**[1:01:11]** fácil, si alguien tiene dudas de por qué, que me diga ahora, para poder repasar lo fácil,

**[1:01:19]** o si no, seguimos, me da la manito. Constanta vamos a tener la grabación disponible para este

**[1:01:34]** fin de semana o no, para poderlo repasar. Esto se está grabando, no lo siento. No la pregunta,

**[1:01:44]** si, aparece que si. Ahi, entonces si, deberían tenerla, que yo no la subo, se suba automática.

**[1:01:49]** Ya, super. Ok, si, deberían estar con la grabación para esto, y recuerden que este

**[1:01:55]** notebook que yo estoy mostrando ustedes también lo tienen, y lo pueden correr ustedes,

**[1:01:59]** y lo pueden modificar, y no hay problema, porque lo van a tener para cada uno, entonces

**[1:02:03]** aquí pueden ponerle nos 300, y 50 mil, y ver qué pasa, pueden jugar con esto, no hay problema.

**[1:02:10]** La idea es que juegan con el código, para como soltar un poco el miedo a equivocarse o a programar.

**[1:02:20]** Ya, otra cosa que puedo hacer, es cómo paso de un data frame a un numpy array,

**[1:02:28]** y eso ya lo habíamos visto, y es con el punto values, pero también se puede hacer con un

**[1:02:32]** punto to numpy, y lo único que hago es simplemente que este data frame que yo construy aquí,

**[1:02:37]** lo voy a pasar a un numpy array. Ok, un lindo arreglo de numpy. Ya, y eso es numpy,

**[1:02:51]** y me quedan 20 minutos, igual no es tanto tanto tanto, quizás esto pueda quedar pendiente.

**[1:02:58]** Y lo otro que viene, la segunda parte que sería análisis descriptivo, pero vamos a ver como

**[1:03:04]** algunas operaciones de numpy, y después la idea es ver cómo hacer gráficos. Ok, como queremos sacar

**[1:03:11]** información, ok, sacar alguna información de alguna tabla, de algunos datos, pero también ser capaces de

**[1:03:16]** como sacar estadísticos que nosotros queramos, no simplemente sacar la media por variables,

**[1:03:22]** sino que quizás hacer algún análisis un poquito más profundo, y también ver cómo podemos

**[1:03:28]** mostrar de una manera como fácil la información que queremos como expresar, ok, si es que queremos

**[1:03:37]** mostrar tendencias, como lo vamos a hacer, etcétera, etcétera, por eso también me hemos graficado.

**[1:03:41]** Entonces, el tiempo que alcance nomás, vamos a utilizar un dataset que corresponde

**[1:03:47]** a un fragmento del dataset oficial de colisiones de Seattle, que contiene todas las colisiones

**[1:03:52]** proporcionadas por la policía de Seattle, y registrada por el departamento de registros de

**[1:03:56]** tráfico. Entonces, lo voy a abrir primero, porque vuelvo a importar, no me acuerdo. Ahí está el dataset,

**[1:04:17]** y tenemos varias, varias variables. Entonces, esto es de accidentes, de tráfico, se supone,

**[1:04:27]** porque son colisiones, bueno no puede ser tráfico porque hay bicicletas, pero de colisiones. Entonces,

**[1:04:33]** primero tiene columnas de Kiki para indicar el dónde fue la colisión, luego el tipo de colisión,

**[1:04:40]** luego una descripción de la ubicación general, luego tiene un código que corresponde a la gravedad

**[1:04:47]** de la coalición, donde tiene fatalidad, lesión grave, lesión como no grave, daño a la propiedad o

**[1:04:54]** cero desconocido. Después tiene una descripción detallada, ¿por qué? Ah, luego tiene como el

**[1:05:02]** severity code y el severity description, ok. Entonces, tiene esto que yo mismo, esto que estaba acá

**[1:05:09]** arriba también lo tiene, pero en inglés. Después tiene el número total de personas

**[1:05:15]** involucradas, y el número de peatones, el número de bicicletas y el número de vehículos

**[1:05:21]** involucrados. También tiene el número de total de personas lesionadas, número de lesiones graves,

**[1:05:27]** si es que hubieron muertes, la fecha, la hora, si la colisión fue causada por falta de atención,

**[1:05:34]** etcétera, etcétera, también la condición climática, etcétera, etcétera, etcétera. Entonces,

**[1:05:39]** es un data set real que habla como de accidentes de choques de la policía, que está registrado

**[1:05:47]** por la policía de Cierno, ok, anonimizado y todo eso. Está ahí disponible. Entonces, algo fácil

**[1:05:55]** que nosotros podemos hacer con el conocimiento que ya teníamos, simplemente cuando nosotros

**[1:06:00]** tenemos un nuevo data set, lo que les dije como buena práctica es siempre mirarlo, siempre mirarlo

**[1:06:06]** para entender más o menos con qué estoy trabajando. Si yo les hubiera mostrado solo este data set así,

**[1:06:13]** sin nada más, no sé si habríamos entendido tanto de qué se trata. Entonces la idea es mirarlo para

**[1:06:19]** entender con qué datos estoy trabajando, pero también si es que tengo alguna información del

**[1:06:24]** contexto de los datos, por ejemplo esto mismo, que sería la descripción del data set en palabras,

**[1:06:29]** también nos ayuda mucho más, mucho más a entender qué está pasando solamente si mirábamos la

**[1:06:35]** tabla vacía, o sea la tabla, simplemente. Pero igual mirar la tabla ayuda, porque a veces uno

**[1:06:41]** ve la descripción y no se imagina lo que tiene. Entonces siempre mirar la tabla es bueno como

**[1:06:46]** para entender con qué estoy trabajando. Luego buena práctica hacer un punto info para entender si es

**[1:06:52]** que, por ejemplo, cuántas columnas tengo, cuántos nulos, etcétera, etcétera. Entonces, como

**[1:06:58]** esto es una data set real, ya no es de juguete, vemos que tengo artos, por ejemplo, que es artos

**[1:07:05]** de elementos nulos, por ejemplo son casi 230.000 entradas y hay casi 10.000 en speeding, o sea,

**[1:07:17]** me faltan artas, hay artas que son nulas aquí. Para valores numéricos algo fácil que yo puedo

**[1:07:28]** sacar es la centralidad, es como un valor para representar, como definir la información de una

**[1:07:35]** columna, un solo valor, me sirve la centralidad. Y para eso podemos ocupar, por ejemplo, la media

**[1:07:42]** o la mediana. Y esto lo estamos haciendo por debajo, pero también lo podemos hacer directamente

**[1:07:50]** del data frame, como lo estamos haciendo aquí. Para, en este caso, nosotros estamos analizando

**[1:07:54]** la cuántas personas involucrajo en el accidente, no es cierto. Y podemos observar que la media y

**[1:08:04]** la mediana no son iguales, ok? Entonces, aquí podríamos medir si es Outlier, podríamos ver

**[1:08:11]** la extensión de los datos, etcétera, etcétera. Pero como centralidad no sirven artos, pero nos sirven

**[1:08:17]** para columnas que son numéricas. ¿Qué pasa cuando ya no tenemos columnas numéricas? O sea,

**[1:08:23]** para la variable categórica. En este caso, por ejemplo, tenemos el clima y el clima no

**[1:08:31]** está como un número. Debe tener algún código después, pero en la columna clima no está como

**[1:08:37]** un número, no le puedo sacar la mediana, porque no tengo números, ok? Entonces, una forma de

**[1:08:43]** representar esta columna con su centralidad, pues sería como su centralidad, sería el valor

**[1:08:50]** que más se repite y esa es la moda. Entonces, puedo acceder a esta columna y sacarle la moda.

**[1:08:55]** Y la moda me dice que es clear, o sea, como el cielo despejado. Ahora, si es que yo quisiera,

**[1:09:03]** por ejemplo, tener un poco más de información de ver cuántas filas o cuántas veces aparece

**[1:09:10]** cada valor, puedo utilizar esta función que nosotros habíamos visto, que es value counts,

**[1:09:14]** ok? Entonces, me dice cuántas veces aparecen el clear, el reining, ok? Entonces, hay 114.000

**[1:09:23]** filas, o sea, 114.000 accidentes registrados que estaban en un tiempo clear. Y yo esperaría

**[1:09:30]** que, así como sin haber visto la tabla, uno esperaría que la mayoría de los accidentes hayan sido,

**[1:09:37]** no sé, por condiciones climáticas, por ejemplo, entonces yo esperaría que la mayoría de los

**[1:09:40]** accidentes fueran en tiempos lluviosos, por ejemplo, en reining, pero veo que no. Viendo solamente la

**[1:09:48]** centralidad, por ejemplo, la centralidad de los dotos, veo que la mayoría de los accidentes

**[1:09:52]** no son cuando está lloviendo, sino que la mayoría de los accidentes fueron cuando el cielo

**[1:09:56]** estuvo despejado. Y eso simplemente lo obtengo haciendo esta operación. Bueno, la extensión en el caso

**[1:10:07]** numérico, ¿no es cierto? La extensión es ver más o menos el rango en el que se mueve una variable,

**[1:10:14]** en este caso numérica, porque para ver el rango en el que se mueve una variable categorica,

**[1:10:19]** tendría que ver como todos los valores que toma en el dato. Pero con variables numéricas es

**[1:10:26]** más fácil. Simplemente tengo que sacar el mínimo y el máximo para ver los valores extremos y ver

**[1:10:33]** dónde está el rango en el que se mueve esta variable. También le puedo sacar la varianza y la

**[1:10:39]** desviación estándar. Entonces si veo el mínimo a 0 y el máximo es 23, la varianza es 2.1 y la

**[1:10:50]** STD es 1.4. Entonces el rango es bastante extenso, muy superior a la media y la mediana,

**[1:10:58]** que la media y la mediana la sacamos antes, pero las vamos a sacarte nuevo para recordar.

**[1:11:01]** La media es 2.2, la mediana es 2.0 y el máximo es 93. Entonces debe haber un accidente como este

**[1:11:17]** 93 que es bastante alto, no es cercano a la mediana y a la media, vamos a asumir que hay

**[1:11:26]** algunos outliers que son bastante altos, pero no son tantos porque la media no está tanta movida de

**[1:11:34]** la mediana. Para entender si es solo un accidente el que involucra tantas personas o si son varios,

**[1:11:39]** podemos por ejemplo utilizar los percentiles o de manera visual lo podríamos ver en un gráfico.

**[1:11:45]** Entonces con los percentiles esto lo podemos hacer directamente con un AMPAI o con pandas,

**[1:11:51]** bueno técnicamente esto ocupan AMPAI por debajo que es el cuánta y el y aquí pongo el percentil

**[1:11:56]** que yo quiero mirar. Si se dan cuenta en el 25% es 2, en el 50% es 2, en el 75% es 3, entonces 75%

**[1:12:10]** de las colisiones involucra a 3 personas o menos y eso está muy lejos del máximo. Entonces vamos

**[1:12:18]** a ver otro cuántil y aquí vemos por ejemplo que el 95% involucra a 5 personas o menos. Entonces

**[1:12:25]** este 93 es un outlier, es la minoría de casos y por eso la media se corre un poco de la mediana,

**[1:12:36]** pero no tanto. Y todo esto que vimos lo podemos sacar con, bueno, la mayoría de las cosas que vimos lo

**[1:12:46]** podemos sacar con el describe cuando es una, como diríamos, cuando es una consulta fácil que

**[1:12:55]** quiero hacer una consulta a toda la columna, pero recordemos que a veces las cosas no son

**[1:13:02]** tan fáciles y yo quiero filtrar a veces, no es cierto? Entonces quisiera filtrar por algún, no

**[1:13:07]** sé, quisiera ver la media de personas involucradas cuando está lloviendo y además que las heridas

**[1:13:16]** hayan sido de tipo, no sé, grave. Entonces ahí el describe ya no me sirve tanto y lo que sí me

**[1:13:22]** sirve es lo que nosotros vimos durante las clases, o sea, filtrar y cómo sacó la media con estas

**[1:13:28]** operaciones que vimos acá, porque ustedes pueden decir, ah, el describe me saca todo lo que vimos antes,

**[1:13:34]** sí, pero de forma muy simple, esto analiza solamente la columna en general, pero si es que yo quisiera

**[1:13:42]** hacer un análisis como más en profundidad y necesito por ejemplo alguna otra cosa, ahora con

**[1:13:49]** las herramientas que yo tengo lo puedo hacer, eso es lo importante, que si es que quisieran hacer

**[1:13:53]** algo, ya tienen la idea general de cómo hacerlo. Ok, entonces el describe me saca de manera general

**[1:13:59]** lo que acabamos de ver para todas las columnas que sean de tipo numérico, no es cierto? Entonces

**[1:14:05]** me saca los percentiles, me saca el mínimo al máximo, se me saca la media y me saca la

**[1:14:11]** desviación y recordemos que esto también le podemos decir que sean los tipos object o también

**[1:14:18]** le podemos poner all para que sea todo, pero eso puede resultar en una tabla muy grande con muchos

**[1:14:25]** none, entonces por eso prefiero normalmente hacerlo separado. Y para los tipos object me va a dar los

**[1:14:31]** unique, la cantidad de valores únicos, la moda y la cantidad de veces que se repite la moda. Ok,

**[1:14:44]** ya, hasta aquí, estamos vivos, funcionamos? Funcionamos, ya, funcionamos, super. La media

**[1:14:56]** máquina pero funcionamos. Ya, entonces ahora comenzaríamos a ver los gráficos y yo creo que

**[1:15:04]** cuando lleguemos a tipos de gráficos me voy a detener porque igual es hard time. Entonces para

**[1:15:12]** hacer gráficos para poder como mostrar un poquito más de todo nuestro análisis es importante

**[1:15:17]** cómo mostramos, ok? De repente hay una forma más fácil para ser el espectador o al receptor

**[1:15:28]** entender nuestra información si nosotros tenemos como conocimiento de los gráficos y también hay

**[1:15:32]** que de repente queremos mostrar como algo específico, entonces tenemos que saber bien cómo mostrar

**[1:15:38]** esa información y cómo poner algo que podría ser básico, de cómo poner los títulos,

**[1:15:43]** de cómo poner títulos a los ejes, de si es que queremos dibujar algo en alguna parte,

**[1:15:47]** cómo cambiar el color, etcétera, etcétera. Entonces primero vamos a ver eso como operaciones

**[1:15:52]** chiquititas para poner el estándar de los gráficos y después tipos de gráficos. Para esto

**[1:15:58]** vamos a ocupar una librería que se llama matplotlib que podrían considerarla un poquito

**[1:16:03]** básica pero hay hartas librerías que se construyen a base de ésta y si es que ocupan otra

**[1:16:08]** librería de gráficos la sintaxis es parecida, entonces sí o sí sirve como aprender un poquito

**[1:16:15]** de ésta. Entonces para partir simple vamos a utilizar un histograma, vamos a importar matplotlib

**[1:16:21]** y lo vamos a llamar PLT, en algunos casos la llaman, creo que PL, en algunos casos lo llaman PI

**[1:16:31]** pero lo importante es que es matplotlib y ustedes le pueden poner el sobrenombre

**[1:16:35]** que quieran. Entonces cómo funciona esto, como lo llame PLT tengo que poner PLT y punto alguna

**[1:16:42]** función que yo quiera llamar, en este caso le vamos a decir que dibuje un histograma y le

**[1:16:47]** vamos a pasar un 1, el PLT.show es para que nos lo muestre, si es que yo mito el PLT.show

**[1:16:55]** me lo va a mostrar igual, por si acaso, pero el PLT.show es normalmente la forma de decir

**[1:17:00]** muéstrame el gráfico. Ok, entonces me hay a generar un histograma y me voy a generar

**[1:17:08]** un histograma que tiene un solo dato, su frecuencia es 1, entonces el 1 aparece 1, maravilloso.

**[1:17:18]** No nos interesa tanto, después vamos a pasar los datos más complejos, pero la idea es

**[1:17:22]** como ver el formato, como modifico esto para que se vea de la forma que yo quiero

**[1:17:27]** que se vea. Entonces por ejemplo aquí está el gráfico vacío, como le pongo nombre

**[1:17:32]** a los ejes como le pongo título, para esto vamos a ocupar PLT.title para el título y para

**[1:17:40]** los ejes, para ponerle el nombre a los ejes, para el eje X se llama X label y para el eje

**[1:17:46]** Y se llama Y label y dentro de los paréntesis yo simplemente con comillas simples o comillas

**[1:17:53]** dobles tengo que poner el nombre que quiero que tenga, entonces aquí el mismo gráfico

**[1:18:01]** de arriba, ahora con nombres en los ejes, eje Y, eje X y el título. ¿Qué pasa si es

**[1:18:10]** que yo tengo un gráfico? Y en realidad no quiero mostrar todo, quiero mostrar una parte

**[1:18:18]** o quiero hacerle zoom para concentrarme en un fenómeno ahí que pasa con los datos.

**[1:18:25]** Bueno, yo puedo limitar los ejes, puedo limitar el eje Y o el eje X, hacerle algún

**[1:18:29]** zoom o alejarlo un poco, etcétera, etcétera, para entender la información exacta que yo quiero

**[1:18:35]** mirar que yo quiero mostrar. Para esto tengo que agregar algo que se llama X lim, como limitar

**[1:18:42]** el eje X o Y lim para limitar el eje Y, yo simplemente tengo que ponerle, todo se

**[1:18:48]** puede hacer de distintas formas, pero para entenderlo más fácil le paso una lista

**[1:18:54]** que tenga el principio y el final. Quiero que muestres de aquí a acá, eso es todo, entonces

**[1:19:07]** si se dan cuenta antes mi gráfico en el eje X iba del 0 hasta el 1.6 aproximadamente y ahora

**[1:19:17]** yo le estoy diciendo que vaya del 0 al 10, o sea, técnicamente me estoy alejando, entonces

**[1:19:21]** esto se va a ver más flaquito y en el eje Y estoy diciendo que vaya, este va desde

**[1:19:27]** el 0 al 1 y estoy diciendo que vaya del 0 al 0.5, entonces lo estoy, entonces por eso cuando

**[1:19:35]** yo hago esta nueva visualización mi barra se ve como más, más pequeña del ladito, pero

**[1:19:44]** no alcanzo a ver al final, el final de la barra, no veo cuando termina porque yo limité

**[1:19:48]** el eje Y y justo en este rango la barra no está en su máximo, entonces no ha terminado,

**[1:19:55]** entonces sigue para arriba, pero yo solamente muestro este sector para mostrar alguna

**[1:19:58]** cosa de interés por ejemplo. Si es que si es que yo quisiera por ejemplo agregar más de

**[1:20:07]** una figura, simplemente tengo que ponerle no sé, peleté punto el gráfico que quiera, los

**[1:20:15]** datos que yo quiera, después peleté punto el gráfico que quiera, bueno el mismo gráfico

**[1:20:19]** con los mismos datos, si yo lo hago esto varias veces lo que va a pasar es que por

**[1:20:24]** defecto cada una se va a poner de un color distinto hasta que llegue al límite

**[1:20:28]** de colores y ya se van a empezar a repetir, entonces si se dan cuenta aquí está el 1,

**[1:20:38]** aquí está el 2 y aquí está el 3 que se repite dos veces, así que la frecuencia es 2, el 4

**[1:20:43]** y el 5, si se dan cuenta el 1 es de un color, el 2 es de otro color y este como está

**[1:20:50]** grupito de datos también es de otro color, pero como estaban todos agrupados en el

**[1:20:56]** mismo gráfico o en el mismo comando, todos son de un mismo color pero ese color es

**[1:21:02]** distinto de los demás, si es que yo quisiera especificar el color hay un

**[1:21:09]** parámetro que se llama color, ok y aquí le puedo poner distintas palabras, ahora

**[1:21:15]** lo importante es ir a la documentación para ver cuáles son las palabras válidas

**[1:21:20]** porque yo le podría poner no sé, azul en español, pero eso no es una

**[1:21:25]** palabra válida para la librería entonces me va a dar error, entonces tengo que buscar ahí en la

**[1:21:30]** documentación qué colores están disponibles, entonces por ejemplo aquí le

**[1:21:37]** cambié con ese, le puse tío creo que se llama y le cambió el color, entonces le

**[1:21:44]** podría cambiar el color a todo, le podría poner no sé, orange, red o a veces le

**[1:21:49]** puedo poner un código del color, dependiendo de si la librería me deja o

**[1:21:53]** no, aquí quiero mostrar este caso que me pasa que pongo estos gráficos, pongo un

**[1:22:04]** histograma con el 1, el histograma con el 2 y un histograma con muchas cosas y lo que

**[1:22:08]** pasa es que histograma 1 y el histograma 2 existen, pero este histograma lo está

**[1:22:13]** tapando, no me los muestra porque están encima y son más grandes, entonces no

**[1:22:18]** se ve, entonces lo que yo puedo hacer cuando tengo como datos y quisiera

**[1:22:23]** que tuvieran un poquito de transparencia, hay un parámetro que se llama alfa,

**[1:22:31]** por qué no lo tengo puesto aquí, ah, voy a mostrar el alfa al tiro primero, el alfa,

**[1:22:38]** que es este de aquí, el alfa, entonces van 3, 0 y 1 y entre más cercano a 0 más

**[1:22:45]** transparente es la figura, entonces aquí es transparente, lo que quería

**[1:22:49]** mostrar es que el orden importa, entonces si pongo la figura que me

**[1:22:54]** tapaba las cosas primero y después voy agregando las otras 2, estas se van a

**[1:22:59]** pintar o dibujar encima, porque el orden importa, el orden en que yo voy dando los

**[1:23:04]** camandos importa, entonces si se dan cuenta se van a pintar encima, pero igual no se

**[1:23:08]** ve tan bien, entonces agregar el alfa me ayuda en la visualización, esto me ayuda

**[1:23:13]** en especial cuando tengo gráficos de dispersión y quiero ver tendencias de

**[1:23:18]** los puntos, ahí me sirve mucho a agregar el alfa y también si es que yo quisiera

**[1:23:26]** agregar etiquetas, porque por ejemplo aquí tengo 3 gráficos de colores distintos, pero

**[1:23:31]** no estoy diciendo qué significa cada gráfico, por ejemplo esto puede ser una

**[1:23:35]** bodega, no sé, una bodega en san Carlos y esta puede ser una bodega en

**[1:23:41]** wiki y esta puede ser otra bodega en otra parte, pero no lo estoy mostrando

**[1:23:46]** así, entonces me falta información, entonces una forma de mostrar eso es con

**[1:23:50]** etiquetas que se llaman labels, entonces yo aquí cuando estoy creando todo este

**[1:23:55]** gráfico acá adentro, le puedo poner además del color, además del alfa, le

**[1:23:59]** puedo poner un label y le puedo poner lo que yo quiera, aquí la estoy poniendo

**[1:24:04]** colores, lo importante es que la etiqueta no se va a mostrar a menos de que yo

**[1:24:08]** ponga de manera explícita que quiero que se muestre, le puedo poner los

**[1:24:13]** labels y si es que no le pongo explícitamente un comando para que

**[1:24:16]** se muestren no van a aparecer, cuál es este comando se llama plt.legend, como de

**[1:24:21]** leyenda, entonces ahora me aparece este cuadrito que me indica

**[1:24:28]** las palabras que yo puse aquí de argumento en el label para cada

**[1:24:33]** para cada color en este caso, entonces me va indicando qué es cada uno, si es que

**[1:24:40]** yo quisiera que este cuadrito aparezca en otra parte, le puedo poner la

**[1:24:44]** posición aquí, que no me acuerdo exactamente cuáles eran, pero lo

**[1:24:47]** puedo buscar la documentación, le puedo poner como center, creo, lo podemos intentar

**[1:24:52]** pero puede que no funcione, ah no se pone, ¿cuál era la, será position? no creo que no, ya no nos vamos a poner de esa

**[1:25:10]** pero hay un argumento para cambiarle la posición, que no me acuerdo cuál era,

**[1:25:13]** que lo podemos buscar la documentación que es para mover esto, que yo lo

**[1:25:16]** puedo mover al centro, lo puedo mover a las esquinas o lo puedo mover a los

**[1:25:20]** lados, hay una forma complicada de ponerlo afuera del gráfico, también, pero se

**[1:25:26]** puede, y lo último serían las líneas, a veces yo quiero como dibujar o dividir el

**[1:25:38]** gráfico y le puedo agregar estas líneas, pueden ser líneas horizontales o líneas

**[1:25:42]** verticales que se hacen con estos comandos, ok, entonces le puedo decir

**[1:25:46]** que yo quiero una línea horizontal y en el en el valor 1 o una línea

**[1:25:52]** vertical en el valor 4.5 y este LS es el line style y es el estilo de dibujo de la

**[1:26:00]** línea, si es que no le pongo nada va a aparecer una línea normal y en este caso

**[1:26:07]** es una línea apunteada y también hay más argumentos, si es que yo quisiera por

**[1:26:12]** ejemplo cambiarles el tamaño, también hay un argumento para el tamaño, si es

**[1:26:15]** que yo quisiera cambiar la letra de esto, el tipo de letra, también hay

**[1:26:18]** un argumento para eso, etcétera, etcétera, entonces ahí está mi línea vertical que

**[1:26:23]** está en el valor 4.5 porque aquí puse 4.5 y mi línea horizontal que

**[1:26:29]** ahí está mi 1 porque yo puse 1, eso, no vamos a alcanzar a ver los tipos de gráficos

**[1:26:35]** entonces voy a pasarlos la otra clase yo creo, entonces lamentablemente no

**[1:26:41]** van a poder hacerlos, o quizás sí, no, no van a poder hacer los ejercicios, pueden

**[1:26:46]** intentar hacerlos, si es que quieren, tratando de ver cómo se hacen los

**[1:26:52]** distintos gráficos ya en el tiempo fuera de la clase, pero si no podemos verlos muy

**[1:26:57]** muy rápido la próxima clase al principio, ya, entonces dejo estos últimos

**[1:27:03]** minutitos para dudas, dudas de lo que acabamos de ver, a mí me estresa mucho

**[1:27:23]** no estar, haberme caído y yo no lo sé, yo no lo sé, si se escucha el

**[1:27:27]** profesor, yo por lo tanto no tengo dudas, que entendí

**[1:27:32]** súper, si quieren, si quieren pueden como mirar esto igual porque aunque no van a

**[1:27:40]** tener mi bla bla, yo normalmente escribo como para que puedan mirar esto sin

**[1:27:45]** yo estar hablando entonces normalmente está, si ustedes corren esto les va a

**[1:27:50]** aparecer, bueno no corría el data, pero si ustedes corren esto les va a

**[1:27:53]** aparecer el dibujito del gráfico y también está una mini descripción del

**[1:27:57]** gráfico, además, viéndome muy para abajo, aquí hay algunos links, entonces si se

**[1:28:04]** mete por ejemplo aquí, que es este que debería verse porque te compartiendo toda

**[1:28:08]** la pestaña, hay un texto que va también explicando con información

**[1:28:14]** adicional de cuáles son los distintos tipos de gráfico y lo importante es como

**[1:28:19]** para qué sirven, cuando quiero ocupar este tipo de gráfico, para qué

**[1:28:22]** tipo de dato, cuando yo quiero mostrar esta, esta cosa o esta otra cosa se

**[1:28:27]** recomienda este gráfico o este otro gráfico y así, si es que quieren tener

**[1:28:32]** más información sobre eso, porque por ejemplo aquí hay algunos gráficos que yo

**[1:28:36]** no muestro acá, para ver cómo expandirlo, no sé si hay dudas, dudas de

**[1:28:45]** último minuto, parece que no, entonces esta material la vamos a dejar cortita para

**[1:28:55]** el inicio de la próxima clase, ahora son libres de descansar, se pueden

**[1:29:04]** retirar.

**[1:29:07]** Chavros, ahora gracias, que estén bien.

**[1:29:09]** Chav, que estén muy bien.

**[1:29:11]** Hola, gracias.

**[1:29:13]** Chavos.

**[1:29:15]** Gracias.

**[1:29:17]** Chavos, cómo vuelvo al zoom.

**[1:29:21]** Ah, gato.

**[1:29:23]** Me voy a quedar aquí por si hay dudas de la vida.

**[1:29:28]** Yo tengo una consulta, no sé si lo habrá mencionado a algún lado, pero

**[1:29:33]** el horario de consulta tiene como...

**[1:29:37]** Yo como ayudante creo que no, y el prefe no sé si le habrá dado uno.

**[1:29:42]** Ahora estamos como eligiendo uno, pero no sé si es como que ese es para todos,

**[1:29:46]** para los tres profesores del ramo o solo con él,

**[1:29:50]** entonces era mi consulta.

**[1:29:52]** Sí, justicia.

**[1:29:54]** Me sirve que me lo pregunte, lo agradezco mucho, porque la verdad es que no tenía

**[1:29:57]** ni idea, entonces lo voy a plantear con el prefe para ver si es que yo

**[1:30:01]** tengo que agregar así como un horario de consulta online para estar disponible

**[1:30:05]** o si es solo con el prefe.

**[1:30:07]** Sí.

**[1:30:09]** Ahora normalmente estoy respondiendo como en los correos, pero igual me demoro

**[1:30:12]** sus dos días hábiles en respuesta.

**[1:30:14]** Sí, usted entiende.

**[1:30:16]** Pero si es que tengo que poner un horario,

**[1:30:19]** un horario lo pondría, voy a hablar con el profesor a cargo,

**[1:30:22]** y si hay alguno lo voy a poner como en un anuncio,

**[1:30:26]** para que estén enteros.

**[1:30:28]** Si es que no se pudiera concretar eso, igual uno puede mandarlo un correo

**[1:30:32]** para coordinar alguna consulta pequeñita o algo así.

**[1:30:36]** Sí, si es que me dicen que no tengo que poner un horario de consulta,

**[1:30:39]** igual voy a subir un anuncio diciendo no hay un horario de consulta,

**[1:30:42]** pero se puede por correo.

**[1:30:44]** Sí.

**[1:30:46]** De los dos casos.

**[1:30:48]** Gracias.

**[1:30:50]** Buen fin de semana.

**[1:30:52]** Profesora.

**[1:30:57]** Hola.

**[1:30:59]** Hola.

**[1:31:01]** Quisiera hacerle una consulta, pero es como para el futuro.

**[1:31:04]** Yo soy profesor de Matemática.

**[1:31:06]** Estoy en la Océano del Biohíaco en Chile.

**[1:31:09]** Y ahora estoy cursando el diplomado.

**[1:31:12]** Entonces, o sea, si me falta esta parte del diplomado,

**[1:31:15]** porque como termina septiembre,

**[1:31:17]** entonces si lo llegase a aprobar,

**[1:31:19]** me gustaría después postular al Magister de Ciencedato.

**[1:31:23]** Entonces, mi consulta es que

**[1:31:25]** usted después realiza clases particulares,

**[1:31:28]** porque me gustaría, como el diplomado,

**[1:31:31]** después termina septiembre,

**[1:31:33]** como que alguien me guiará para seguir profundizando,

**[1:31:35]** porque si no sientas que después me voy a chunchear,

**[1:31:37]** o sea, voy a repasar las clases,

**[1:31:39]** pero para, como, seguir avanzando.

**[1:31:44]** No sé si usted...

**[1:31:46]** Suza, no me lo había planteado,

**[1:31:48]** porque nunca he realizado como clases particulares,

**[1:31:50]** no me lo había planteado.

**[1:31:52]** No me lo había planteado como ayudante

**[1:31:54]** como de los cursos específicos, no más.

**[1:31:56]** Y si en que traje el programa de Magister,

**[1:31:58]** quizás también nos veamos ahí.

**[1:32:00]** Sinceramente no lo he planteado,

**[1:32:02]** pero si es que termina el curso

**[1:32:04]** y si es como teniendo ganas de aprender,

**[1:32:06]** lo que te puedo mandar es como material adicional.

**[1:32:08]** Si no, si no hay ningún problema como en eso.

**[1:32:10]** Ah, ya, ya.

**[1:32:12]** Y así eso le quería consultar.

**[1:32:14]** Mucho gracias a todos.

**[1:32:16]** De nada, gracias a ti.

**[1:32:18]** Buen fin de semana.

**[1:32:20]** ¡Adiós!
