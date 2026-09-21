# 03Ayundatía Fundamentos en Ciencia de Datos 11 Julio.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:44:46
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:00:25]** Hola, luego. Hola.

**[0:00:31]** Hola, sí.

**[0:00:58]** Antes no, no, no había en clases teóricas hoy, o el profesor se

**[0:01:04]** se olvidó, o no le pasó algo.

**[0:01:06]** ¿Cómo?

**[0:01:08]** Aquí estábamos como todos conectados al acción cuarto, pensando

**[0:01:12]** que ya era una clase teórica, pero no, no, no, no sabemos

**[0:01:16]** si estaba programado de antemano así o fue por un error.

**[0:01:21]** Ehh, déjame mirar la fotito.

**[0:01:29]** Yo soy don Arabo, o debería haber clases teóricas que yo

**[0:01:37]** necesito ahora, porque vamos a ver calidad de datos y debería haber

**[0:01:41]** visto una clase de calidad de datos.

**[0:01:44]** Voy a preguntar, déjame dos minutitos.

**[0:01:50]** Toco, toco, toco, toco.

**[0:01:52]** Voy a ver si en el canvas está la info de la clase por ahora

**[0:02:21]** para ver si puedo hacer un mini repaso yo.

**[0:02:23]** A la mala, ¿no más?

**[0:02:51]** ¿Cuál fue la última diapo que vieron?

**[0:02:59]** Porque veo que tienen una que se llama intro, otra que se

**[0:03:02]** llama ciencia de datos y otra que se llama ciencia de

**[0:03:04]** datos en la práctica.

**[0:03:11]** Intro.

**[0:03:12]** ¿Sólo la intro?

**[0:03:19]** Ah, no, el que nos abrece en canvas es el 4321001,

**[0:03:33]** fundamentos de ciencia de datos, perdón, mi yoye.

**[0:03:36]** Pero me refiero a que en clases no le salen tres PDFs,

**[0:03:49]** vieron los tres en clase ya o solo vieron con el que hago

**[0:03:53]** algo pendiente.

**[0:03:55]** Me doy el segundo, creo.

**[0:03:58]** Sí, el primer segundo.

**[0:04:00]** Hoy en día deben haber visto el tercero.

**[0:04:03]** Incluso parece que el tercero, no sé si todo.

**[0:04:06]** Recibe que el tercero igual.

**[0:04:09]** Dice ciencia de datos en la práctica.

**[0:04:13]** No hace el tercero igual.

**[0:04:16]** Entonces quizás deberíamos haber, deberían haber visto

**[0:04:20]** como más o menos la idea de calidad de datos, quizás.

**[0:04:23]** Sí, eso también lo iba exagerizando.

**[0:04:26]** Quizás no hay problema en que yo pase el lab,

**[0:04:29]** o cuando no hubo clase hoy día, no entiendo muy bien

**[0:04:33]** qué onda la planificación.

**[0:04:44]** Hoy día es 10.

**[0:04:46]** Hoy día es 10, yo no estoy con nada malo aquí.

**[0:04:49]** Hoy día es, no mentira, hoy día es 7.

**[0:04:51]** No mentira, hoy día es 10.

**[0:04:53]** Hoy día es 10, Alejandra.

**[0:04:54]** Hoy día es 10, desde el 7, está naranjo,

**[0:04:57]** me toca y hasta todo viene entonces.

**[0:05:00]** Nadie me dice así como no, no hagas la práctica en el lab,

**[0:05:04]** pero tampoco me dicen que undibuy otro de la clase,

**[0:05:08]** así que creo que eso va a quedar pendiente

**[0:05:10]** y voy a tratar de seguir con la práctica en nuestro caballí día,

**[0:05:14]** pero si es que hay algo que no entiendan,

**[0:05:16]** así como, oye, ese concepto no lo vimos,

**[0:05:18]** aunque no es mucho del concepto,

**[0:05:20]** podemos repasarlo así como ahora,

**[0:05:24]** a medida que vayamos viendo las cosas.

**[0:05:27]** Ya, entonces empecemos con la práctica

**[0:05:29]** como para no estar tan en el limbo, no más.

**[0:05:31]** Recordemos que la práctica pasada nos quedó algo pendiente

**[0:05:36]** y también la práctica pasada,

**[0:05:38]** bueno, la práctica pasada fue como una introducción

**[0:05:40]** a una librería que se llamaba Pandas, ¿no es cierto?

**[0:05:43]** Donde vimos cómo manipular tablas.

**[0:05:46]** Esa es como la gran idea que tiene la librería Pandas,

**[0:05:50]** que yo puedo manipular los datos tabulares,

**[0:05:53]** recordemos que son datos tabulares,

**[0:05:55]** yo puedo hacer consultas, hacer alguna limpieza,

**[0:06:00]** como ver los datos mediante esta librería

**[0:06:04]** y habíamos visto como distintas funciones,

**[0:06:07]** si no mal recuerdo, no sé, compartiendo.

**[0:06:10]** Primero, ahí estoy yo, ya ahí, ahora soy vista.

**[0:06:14]** Y ahora tengo que compartir la práctica.

**[0:06:17]** Te voy a decir que no estaba compartiendo.

**[0:06:19]** O sí, o sí.

**[0:06:21]** Y me falta compartirme a mí misma.

**[0:06:24]** Me voy a tener la respuesta de los laboratorios abiertos

**[0:06:35]** por si acaso, por si no mando alguna cuestión,

**[0:06:39]** porque yo siempre me puedo equivocar,

**[0:06:41]** aquí me voy en directo y si entro en pánico,

**[0:06:43]** tengo la respuesta del lado,

**[0:06:45]** porque cuando entro en pánico de repente no programamos.

**[0:06:48]** Ya.

**[0:06:51]** Aquí estoy.

**[0:06:53]** Me dijeron la vez pasada que si ponía

**[0:06:55]** compartir esto con las camaritas tapabas,

**[0:06:58]** así que ya no voy a poner las camaritas

**[0:07:00]** para quedar chiquititos.

**[0:07:02]** Ya.

**[0:07:04]** O sea, ahí ven mi pantalla y deberíamos estar aquí en el uno.

**[0:07:07]** ¿No es cierto? Vimos esta práctica la vez pasada.

**[0:07:10]** Laboratorio de pandas, vacío, no es cierto?

**[0:07:13]** Y vimos que era una serie, que era una tabla en este caso.

**[0:07:17]** O sea, que era una serie, que era un data frame,

**[0:07:19]** vimos cómo mostrarlo, cómo acceder,

**[0:07:21]** el halo, que el look, cómo agregar filas,

**[0:07:24]** cómo agregar columnas, cómo eliminar, cómo recorrer.

**[0:07:27]** Y estábamos viendo cómo hacer consultas,

**[0:07:30]** cómo filtrar datos, y nos quedaron algunas operaciones

**[0:07:33]** pendientes.

**[0:07:36]** Porque nos quedamos sin tiempo en la última parte.

**[0:07:42]** Entonces, yo les enví el vacío y al final

**[0:07:44]** habían algunos ejercicios.

**[0:07:47]** Y esos ejercicios ya están con respuesta,

**[0:07:50]** porque yo subí las respuestas de los ejercicios.

**[0:07:54]** La idea es que ustedes quieren practicar

**[0:07:56]** que los intenten por su cuenta

**[0:08:00]** para aflojar un poco esto,

**[0:08:03]** porque a veces uno le cuesta como recordar las cosas

**[0:08:06]** y la mejor forma es como aplicarlas.

**[0:08:08]** Y aplicarlas uno solito de buenas a primeras,

**[0:08:10]** y ya después uno ve si es que ocupa

**[0:08:13]** alguna herramienta que lo ayude a programar después.

**[0:08:16]** Ah, y el ejercicio en conjunto, este ejercicio uno,

**[0:08:19]** lo hicimos en conjunto, valga la redunda.

**[0:08:22]** Así que sí lo hicimos, pero el otro,

**[0:08:24]** el ejercicio dos, es el que nos quedó pendiente.

**[0:08:28]** Ya, no me acuerdo muy bien en qué nos quedamos.

**[0:08:32]** Nos quedamos en filtrar datos, no es cierto,

**[0:08:34]** en hacer consultas, como por aquí.

**[0:08:36]** ¿Vamos?

**[0:08:42]** ¿Vamos?

**[0:08:44]** Creo que estamos viendo un poco la estadística

**[0:08:46]** de la información que venía, los cuerpos,

**[0:08:49]** las columnas, las cantidades.

**[0:08:52]** Sí, pero yo recuerdo que vimos consultas,

**[0:08:56]** porque recuerdo haber dicho cuál era el I y cuál era el O.

**[0:08:59]** Entonces recuerdo haber dicho que este es el O

**[0:09:02]** y este es el I, entonces habíamos visto,

**[0:09:04]** alcanzamos a ver el filtrado de datos.

**[0:09:07]** Pero no me acuerdo si alcanzamos a ver la operación.

**[0:09:10]** No creo que esta liye lo más de lo que me acuerdo.

**[0:09:12]** Entonces llegamos a ver filtrado de datos, ya.

**[0:09:15]** Es, obviamente, si yo corro esta celda,

**[0:09:17]** como no he corrido ninguna de las interiores,

**[0:09:19]** esto me va a dar error, ¿no es cierto?

**[0:09:21]** Así que me voy a poner aquí,

**[0:09:23]** me voy a ir en torno a ejecución,

**[0:09:25]** me voy a poner con ejecutar anteriores,

**[0:09:27]** con ejecutar todo para arriba,

**[0:09:29]** para que ya cargue los datos y haga toda la cuestión.

**[0:09:32]** Ya.

**[0:09:33]** Entonces por mientras que eso se ejecuta,

**[0:09:35]** recordemos un poquito que nosotros estábamos viendo,

**[0:09:38]** si esto no se queda pegado,

**[0:09:40]** que nosotros estábamos viendo

**[0:09:42]** ya operaciones un poquito más complejas.

**[0:09:44]** Entonces, por ejemplo,

**[0:09:46]** nosotros estábamos jugando acá arriba.

**[0:09:50]** Yo les dije cómo cargar y guardar tablas,

**[0:09:52]** no es cierto, con el read y con el tu.

**[0:09:55]** No es cierto, el read, ccb y el tu ccb.

**[0:09:57]** En este caso el ccb es un formato,

**[0:09:59]** un formato de texto.

**[0:10:01]** Qué fácil de leer, fácil de ocupar, no pesa mucho.

**[0:10:03]** Pero también se puede, por ejemplo,

**[0:10:05]** si quieren leer un excel y después hacer consultas para acá,

**[0:10:07]** se puede poner un read excel o un tu excel, etcétera, etcétera.

**[0:10:10]** Y habíamos estado jugando

**[0:10:13]** con, como ejemplo,

**[0:10:15]** que yo había puesto manualmente,

**[0:10:17]** que eso no era tan entretenido

**[0:10:19]** porque no son tablas tan grandes,

**[0:10:21]** yo veo al tiro lo que tienen,

**[0:10:23]** entonces como que no es tan real.

**[0:10:26]** Entonces aquí lo que habíamos hecho es

**[0:10:28]** ocupando estos read ccb

**[0:10:30]** y algunas cositas extras,

**[0:10:32]** estábamos cargando

**[0:10:34]** como un dataset

**[0:10:36]** real y existente.

**[0:10:38]** No es cierto que era el moving lens

**[0:10:40]** que tenía informaciones de reviews,

**[0:10:42]** de películas, de distintos usuarios

**[0:10:44]** y esto ya está anonimizado.

**[0:10:46]** ¿No es cierto?

**[0:10:49]** Y lo que habíamos hecho es que había una tabla

**[0:10:51]** había una tabla con la descripción de los usuarios,

**[0:10:53]** había una tabla con las películas

**[0:10:55]** y había una tabla con las calificaciones

**[0:10:57]** pero nosotros queríamos tener todo en su conjunto

**[0:10:59]** así que empezamos a ocupar

**[0:11:01]** nuestra primera como función nueva

**[0:11:03]** que era el merge.

**[0:11:05]** Que el merge es una función que me permite

**[0:11:07]** combinar tablas

**[0:11:09]** bajo cierto criterio.

**[0:11:11]** En este caso tienen que tener una columna en común.

**[0:11:13]** Ok, y esa es la columna en común

**[0:11:16]** que se utiliza para hacer este

**[0:11:18]** merge o este join

**[0:11:20]** o esta combinación de las tablas,

**[0:11:22]** de la información de las tablas.

**[0:11:24]** Yo me salte esta partecita

**[0:11:26]** que explicaba

**[0:11:28]** cómo afectaba

**[0:11:30]** el distinto tipo de merge

**[0:11:32]** a la tabla que se forma

**[0:11:34]** y yo les dije que esto lo podían correr.

**[0:11:37]** ¿Cómo?

**[0:11:39]** Yo expliqué que esto lo podían

**[0:11:41]** correr ustedes

**[0:11:43]** aparte para ver cómo cambiaba

**[0:11:45]** la tabla resultante

**[0:11:47]** dependiendo del tipo de merge

**[0:11:49]** que yo ocupaba.

**[0:11:52]** No sé si hay alguna duda.

**[0:11:55]** Ya.

**[0:11:57]** Entonces cargamos

**[0:11:59]** las tablas, las combinamos

**[0:12:01]** y tuvimos un gran dataset

**[0:12:03]** que tenía la información de la persona

**[0:12:05]** que hizo la review

**[0:12:07]** la...

**[0:12:09]** la persona que hizo la review

**[0:12:11]** el movie ID

**[0:12:14]** que sería como

**[0:12:16]** la película

**[0:12:18]** que calificó

**[0:12:20]** el movie ID

**[0:12:22]** del nombre de la película

**[0:12:24]** y en qué año se estrenó la película

**[0:12:26]** y aquí está la calificación

**[0:12:28]** y una información como temporal

**[0:12:30]** de cuándo fue hecha esta calificación.

**[0:12:32]** Entonces esta es toda la tabla combinada.

**[0:12:34]** Entonces tengo muchas calificaciones.

**[0:12:36]** ¿Qué es cada fila?

**[0:12:38]** Cada fila es la calificación

**[0:12:40]** que hizo un usuario específico

**[0:12:42]** a una película específica.

**[0:12:44]** Eso es cada fila.

**[0:12:46]** Yo tengo que tener muy en claro

**[0:12:48]** cuando estoy trabajando con datos

**[0:12:50]** qué significa una fila

**[0:12:52]** o cada dato.

**[0:12:55]** Ok, habíamos visto cómo describir los datos

**[0:12:57]** usando el info, el describe

**[0:12:59]** que se podía hacer el describe tipo object

**[0:13:01]** para dar algunos estadísticos

**[0:13:03]** de cosas que fueran como

**[0:13:05]** categóricas, creo que se llama.

**[0:13:10]** Vimos cómo filtrar datos

**[0:13:12]** y aquí nos quedamos.

**[0:13:14]** ¿Cómo hacer consultas sobre los datos?

**[0:13:16]** Recuerdan que yo tenía que poner el nombre

**[0:13:18]** de la tabla, los operadores

**[0:13:20]** que son los corchetes

**[0:13:22]** y dentro ahí tenía que poner mi consulta

**[0:13:24]** y estas consultas es

**[0:13:26]** como que la podemos pensar en lenguaje natural

**[0:13:28]** y después pasarlo

**[0:13:30]** a consulta que no es tan difícil.

**[0:13:32]** Por ejemplo, yo quiero, en este caso habíamos dicho

**[0:13:34]** yo quiero obtener

**[0:13:36]** todas las filas

**[0:13:38]** que sean calificaciones

**[0:13:40]** con un puntaje mayor a 3.

**[0:13:42]** Teniendo eso en lenguaje natural

**[0:13:44]** yo ya lo puedo pasar.

**[0:13:46]** Entonces quiero toda la fila

**[0:13:48]** entonces tengo que acceder a la tabla

**[0:13:50]** y dentro pongo los corchetes

**[0:13:52]** va mi consulta.

**[0:13:54]** Entonces ¿Qué es lo que quiero observar?

**[0:13:56]** Quiero observar las calificaciones

**[0:13:58]** porque me interesa que las calificaciones

**[0:14:00]** tengan un puntaje mayor a 3.

**[0:14:02]** Entonces accedo a la columna califications

**[0:14:04]** que contienen las calificaciones

**[0:14:06]** y que quiero que sean

**[0:14:08]** mayores a 3.

**[0:14:10]** Entonces pongo el signo de mayor

**[0:14:12]** y pongo un 3 y ahí está mi consulta.

**[0:14:14]** Son una consulta bastante simple

**[0:14:16]** pero nosotros podemos complejizar esto, no es cierto?

**[0:14:18]** Agregándole

**[0:14:20]** más de una condición.

**[0:14:22]** Por ejemplo aquí yo decía

**[0:14:24]** quiero obtener la tabla con personas

**[0:14:26]** que sean del sexo masculino

**[0:14:28]** o que sean mayores a 30.

**[0:14:30]** Y ahí hay dos consultas técnicamente

**[0:14:32]** o que sean del sexo masculino

**[0:14:34]** o que sean personas con edad

**[0:14:36]** mayor a 30.

**[0:14:38]** Entonces ahí tengo dos consultas

**[0:14:40]** cada vez que tengo más de una consulta

**[0:14:42]** tengo que poner cada consulta entre paréntesis

**[0:14:44]** o si no me puede dar error

**[0:14:46]** dependiendo de la versión de pandas

**[0:14:48]** y si es que yo digo

**[0:14:51]** o el lenguaje natural

**[0:14:53]** o sea es la una

**[0:14:55]** o la otra

**[0:14:57]** tengo que poner este palito

**[0:14:59]** y si es que yo digo

**[0:15:01]** mi condición es un i

**[0:15:03]** como por ejemplo quiero a

**[0:15:05]** y quiero b

**[0:15:07]** que se cumplan las dos

**[0:15:09]** entonces si es que digo i en lenguaje natural

**[0:15:11]** tengo que usar el ampersand

**[0:15:13]** o como lo llaman ustedes pero es ese símbolo

**[0:15:16]** y eso habíamos dicho sobre filtrar

**[0:15:18]** bastante rápido resumen

**[0:15:20]** de lo que no habíamos quedado la vez pasada

**[0:15:22]** y nos había quedado

**[0:15:24]** operaciones sobre los datos

**[0:15:26]** ya entonces

**[0:15:31]** la primera operación es bastante

**[0:15:33]** básica pero es que pasa si es que yo quisiera

**[0:15:35]** por ejemplo cambiarle los nombres

**[0:15:37]** a las columnas

**[0:15:39]** entonces podemos hacerlo con un rename

**[0:15:41]** y pasándole un diccionario

**[0:15:43]** que tenga el nombre original de la columna

**[0:15:45]** y el nombre al cual yo lo quiero cambiar

**[0:15:47]** en este caso no lo encontramos

**[0:15:49]** como súper súper útil porque

**[0:15:51]** lo mejor es dejarlo todo en el mismo formato

**[0:15:53]** en este caso ninguna tiene

**[0:15:55]** espacios tenían como

**[0:15:57]** yon bajo y eso significa que puedo utilizar

**[0:15:59]** para acceder a cada columna

**[0:16:01]** o las comillas dobles o el punto

**[0:16:03]** porque no había espacio

**[0:16:05]** espacio entre los nombres pero en el caso

**[0:16:07]** de que quisiera tenerla todo en español

**[0:16:09]** lo puedo hacer con un rename por ejemplo

**[0:16:13]** ok entonces ahí me cambian de nombre

**[0:16:15]** después otra operación

**[0:16:17]** era poner punto

**[0:16:19]** valius

**[0:16:21]** el nombre de la tabla punto valius

**[0:16:23]** o puede ser una columna también punto valius

**[0:16:25]** o una subtabla punto valius

**[0:16:27]** aunque no la serie punto valius no me sirve tanto

**[0:16:29]** puedo poner por ejemplo mi tabla

**[0:16:31]** se llama tabla completa y puedo poner

**[0:16:33]** punto valius y lo que hace es que

**[0:16:35]** me entrega

**[0:16:37]** toda la tabla pero ya no como

**[0:16:39]** un tipo

**[0:16:41]** dataframe no es cierto porque vimos el tipo

**[0:16:43]** de datos dataframe ahora me lo entrega

**[0:16:45]** como un arreglo

**[0:16:47]** como un numpy array

**[0:16:50]** ok entonces aquí yo ya puedo hacer operaciones

**[0:16:52]** de numpy sin tener problemas de formato

**[0:16:54]** ni nada así

**[0:16:56]** también tengo la operación

**[0:16:59]** que se llama value counts

**[0:17:01]** ok y esto me

**[0:17:03]** cuenta

**[0:17:05]** cuantas veces

**[0:17:07]** aparece cada valor

**[0:17:09]** no es cierto? creo que no hemos visto el unic

**[0:17:11]** todavía y va a comentar el unic

**[0:17:13]** esto me cuenta cuantas veces aparece

**[0:17:15]** cada valor del unic

**[0:17:17]** color único

**[0:17:19]** que tenga no es cierto la columna

**[0:17:21]** va a

**[0:17:23]** agrupar por ese valor único y va a contar

**[0:17:25]** cuantas veces se repite

**[0:17:27]** en cada no se cuántas filas

**[0:17:29]** tienen este valor

**[0:17:31]** entonces por ejemplo yo puedo hacer

**[0:17:34]** para una columna especifica

**[0:17:36]** puedo poner tabla completa

**[0:17:38]** puedo hacer por ejemplo la columna titulo

**[0:17:40]** o sea los titulos de las películas

**[0:17:42]** y le voy a poner punto value counts

**[0:17:44]** y cuando haga esto

**[0:17:47]** me va a dar

**[0:17:49]** todos los titulos

**[0:17:51]** bueno no se ven porque sería muy muy largo

**[0:17:53]** son 1664 titulos

**[0:17:55]** ok todos los titulos

**[0:17:57]** y cuantas veces

**[0:17:59]** aparece cada titulo o sea que a star wars

**[0:18:01]** le hicieron 583

**[0:18:03]** reviews

**[0:18:05]** o calificaciones la calificaron

**[0:18:07]** 583 veces

**[0:18:09]** a la película contact la calificaron

**[0:18:11]** 509 veces

**[0:18:13]** a la película

**[0:18:15]** la calificaron solamente una vez

**[0:18:17]** tiene solamente una review en nuestra tabla

**[0:18:19]** ok entonces eso hace

**[0:18:21]** el value counts

**[0:18:25]** también puedo obtener los valores

**[0:18:27]** únicos o sea

**[0:18:29]** si es que quiero ver como todos los valores

**[0:18:31]** posibles que hay en una columna

**[0:18:33]** de mi tabla puedo ocupar

**[0:18:35]** algo que se llama el iunic

**[0:18:37]** entonces accedo a mi tabla

**[0:18:39]** accedo a la columna de interés

**[0:18:41]** y pongo punto iunic

**[0:18:43]** y esto me da los valores únicos

**[0:18:45]** por ejemplo yo aquí me voy a poner en la columna ocupación

**[0:18:47]** que es una

**[0:18:49]** un dato de los usuarios

**[0:18:51]** me dan como la ocupación

**[0:18:53]** que tiene el usuario que hizo

**[0:18:55]** la review

**[0:18:57]** entonces aquí me dice que puede ser

**[0:18:59]** un escritor, un administrador, un estudiante

**[0:19:01]** un abogado etc etc

**[0:19:03]** entonces estos son todos los

**[0:19:05]** valores

**[0:19:07]** que tiene esa columna

**[0:19:09]** y además del iunic

**[0:19:12]** que me da exactamente los valores únicos

**[0:19:14]** yo puedo preguntarme cuántos valores únicos

**[0:19:16]** posee una columna

**[0:19:18]** y eso se hace con el

**[0:19:20]** iunic, o sea tomo el iunic

**[0:19:22]** y le pongo una n al principio

**[0:19:24]** se llama iunic

**[0:19:26]** y esto me dice básicamente es hacerle como un lend

**[0:19:28]** a el iunic

**[0:19:30]** porque me cuenta la cantidad de valores únicos

**[0:19:32]** en este caso

**[0:19:34]** yo voy a acceder a la columna calificación

**[0:19:36]** y voy a hacer un iunic

**[0:19:38]** entonces me dice que calificación tiene solamente

**[0:19:40]** 5 valores

**[0:19:42]** la calificación puede ser entre

**[0:19:44]** 0 y 5

**[0:19:46]** 1 y 5

**[0:19:50]** y bueno

**[0:19:52]** eso con algunas operaciones

**[0:19:54]** sobre los datos

**[0:19:56]** luego

**[0:19:59]** tenemos operación

**[0:20:01]** para ordenar los datos

**[0:20:03]** aquí podemos ordenar los datos

**[0:20:05]** si es que quisiera ponerlo como algún orden

**[0:20:07]** y existe

**[0:20:09]** oh se me olvida

**[0:20:11]** el sort values tiene un

**[0:20:13]** parámetro

**[0:20:15]** un imperparámetro aquí

**[0:20:17]** que yo le puedo poner, no me acuerdo si era ascending

**[0:20:19]** que le puedo poner que me dé el orden al revés

**[0:20:21]** por defecto

**[0:20:23]** si es que

**[0:20:25]** yo lo ordeno

**[0:20:27]** y son números, me lo va a ordenar

**[0:20:29]** del más pequeño al más grande

**[0:20:31]** pero yo puedo

**[0:20:33]** ponerle con este parámetro, creo que lo tengo que poner en true

**[0:20:35]** que se haga al revés

**[0:20:39]** entonces por ejemplo aquí voy a hacer tabla completa

**[0:20:41]** y como los ordeno con esta función

**[0:20:43]** que se llama sort values

**[0:20:45]** sort que en bajo values

**[0:20:47]** y en el buy tengo que indicarle

**[0:20:49]** la columna por la cual quiero

**[0:20:51]** que se ordene

**[0:20:53]** y yo le puedo poner más de una

**[0:20:55]** y el orden en que ponga las columnas importa

**[0:20:57]** si por favor

**[0:20:59]** como? una duda

**[0:21:04]** disculpe, Christian tenía la mano a levantar

**[0:21:07]** si

**[0:21:09]** tiene una duda que

**[0:21:11]** antes cuando estaba como el

**[0:21:13]** occupation

**[0:21:15]** se está como el nombre punto

**[0:21:17]** occupation, eso es porque

**[0:21:19]** ese es el nombre

**[0:21:21]** de la columna tal cual

**[0:21:23]** se llama así, no? se llama occupation

**[0:21:25]** y eso es porque

**[0:21:27]** está usando como

**[0:21:29]** el numpy ahí o no

**[0:21:31]** la lluviería numpy

**[0:21:35]** el occupation

**[0:21:38]** o el unit

**[0:21:40]** que yo nunca había visto

**[0:21:42]** eso de que uno puede

**[0:21:44]** poner punto en el nombre

**[0:21:46]** si directo de

**[0:21:48]** de cada columna se acerca

**[0:21:50]** como los datos de la columna

**[0:21:52]** si, se puede, cuando yo estoy

**[0:21:54]** accediendo a una columna creo que lo vimos

**[0:22:00]** yo estaba acostumbrado a usar los porchetes

**[0:22:04]** cuando dije hacer una columna

**[0:22:07]** aquí tengo que acceder a las filas

**[0:22:09]** debe ser más bajito

**[0:22:12]** mentí

**[0:22:14]** me recuerdo mi propia práctica

**[0:22:16]** me acuerdo que cuando comenté

**[0:22:18]** que podíamos acceder a las columnas

**[0:22:20]** hay dos formas de acceder a las columnas

**[0:22:22]** una es con los porchetes y otra es con el punto

**[0:22:24]** y dentro de los porchetes

**[0:22:26]** tienes que poner el nombre de la columna

**[0:22:28]** entre comillas, que pueden ser comillas dobles o simples

**[0:22:30]** aquí da lo mismo

**[0:22:32]** pero el punto sólo

**[0:22:34]** lo puedo ocupar cuando el nombre

**[0:22:36]** de la columna no tiene espacios

**[0:22:39]** es súper importante

**[0:22:42]** esa es como la diferencia

**[0:22:44]** entonces yo puedo ocupar el punto

**[0:22:46]** pero

**[0:22:48]** la forma universal como que siempre me va a servir

**[0:22:50]** en todos los casos serían los porchetes

**[0:22:52]** y solamente si es que la columna

**[0:22:54]** no tiene en el nombre

**[0:22:56]** espacios en blanco puedo ocupar el punto

**[0:22:59]** esa es la forma

**[0:23:01]** y no sé dónde está, pero esta vaya arriba

**[0:23:03]** no me acuerdo exactamente

**[0:23:05]** entendiendo

**[0:23:10]** gracias a ti por preguntar

**[0:23:14]** me quedé en el sort values

**[0:23:16]** ya como dije

**[0:23:18]** esto se va a ordenar por

**[0:23:20]** la columna que yo indicó acá en el bay

**[0:23:22]** en este caso voy a ocupar moviaid

**[0:23:24]** y esto lo corría

**[0:23:26]** entonces si vemos

**[0:23:30]** se ordena por moviaid

**[0:23:32]** y primero me va a aparecer las calificaciones

**[0:23:34]** que se hicieron a la película con moviaid 1

**[0:23:36]** que sería Toy Story

**[0:23:38]** y se van ordenando así para abajo

**[0:23:40]** ya

**[0:23:43]** entonces como dije se puede

**[0:23:45]** poner más de una columna

**[0:23:47]** de las columnas importan

**[0:23:49]** porque

**[0:23:51]** básicamente si yo le pongo más de una columna

**[0:23:54]** si se dan cuenta aquí

**[0:23:56]** por ejemplo todas estas

**[0:23:58]** películas

**[0:24:00]** no mentira cada fila es una calificación

**[0:24:02]** hecha por un usuario

**[0:24:04]** cada calificación hecha por un usuario

**[0:24:06]** puede tener en común el moviaid

**[0:24:08]** entonces aquí por ejemplo hay una

**[0:24:10]** colisión

**[0:24:12]** básicamente estas dos filas

**[0:24:14]** tienen el mismo moviaid

**[0:24:16]** que se van ordenando

**[0:24:18]** entonces por qué criterio las voy a ordenar

**[0:24:20]** como

**[0:24:22]** cual va primero y cual va después

**[0:24:24]** si mi único criterio para ordenar es el moviaid

**[0:24:26]** y ambas tienen el mismo moviaid

**[0:24:28]** bueno aquí lo hacen el orden en que las va encontrando

**[0:24:30]** me solamente eso

**[0:24:32]** como la que aparezca primero

**[0:24:34]** con el moviaid 1

**[0:24:36]** pero por eso me importa

**[0:24:38]** si es que yo pongo más de una

**[0:24:40]** columna para ordenar

**[0:24:42]** por qué

**[0:24:44]** qué ordeno por edad, luego por ocupación

**[0:24:46]** y luego por moviaid

**[0:24:48]** qué significa este es el orden en el que voy a priorizar

**[0:24:50]** como ordenar cuando hay una colisión

**[0:24:52]** es decir

**[0:24:54]** si es que encuentro una colisión

**[0:24:56]** hay dos filas que estoy encontrando que tienen la misma edad

**[0:24:58]** como voy a proceder en el orden ahí

**[0:25:00]** bueno voy a priorizar después

**[0:25:02]** en este caso las voy a ordenar

**[0:25:04]** esas que tienen colisión o que tienen el problema

**[0:25:06]** las voy a ordenar por ocupación

**[0:25:08]** y qué pasa si hay dos elementos que tienen

**[0:25:10]** la misma ocupación

**[0:25:12]** en este caso voy a proceder a ordenar por moviaid

**[0:25:14]** entonces esto va

**[0:25:16]** el orden de prioridad es el orden en el que están

**[0:25:18]** escritas las columnas por las cuales

**[0:25:20]** yo voy a ordenar

**[0:25:22]** por eso si yo cambio el orden de las columnas

**[0:25:24]** aquí en esta consulta

**[0:25:26]** el resultado de la tabla

**[0:25:28]** o la tabla resultante va a ser diferente

**[0:25:30]** aquí entonces por eso

**[0:25:32]** me importa el orden

**[0:25:34]** porque es el orden que voy a ocupar para trabajar

**[0:25:36]** con las colisiones

**[0:25:38]** es como una análisis encajada

**[0:25:40]** de otra y así consecutivamente

**[0:25:42]** literal es lo mismo

**[0:25:45]** y si

**[0:25:47]** entonces es muy fácil entender

**[0:25:49]** cómo se ordenan las cosas cuando yo estoy trabajando

**[0:25:51]** con números por ejemplo en edad

**[0:25:53]** o moviaid

**[0:25:55]** que esos son números pero por ejemplo ocupación

**[0:25:57]** es algo que es un string

**[0:25:59]** que son letras, son caracteres

**[0:26:01]** entonces como ordeno caracteres

**[0:26:03]** bueno eso lo hago en orden alfa numérico

**[0:26:05]** ustedes saben que cada carácter

**[0:26:07]** en realidad tiene como una representación numérica

**[0:26:09]** entonces podrían considerarlo como que sería

**[0:26:11]** que se ordena por orden alfabetico

**[0:26:13]** pero tengo que tener cuidado

**[0:26:15]** porque en realidad orden alfabetico

**[0:26:17]** no tanto

**[0:26:19]** en este caso por ejemplo

**[0:26:21]** si es que yo le preguntara

**[0:26:23]** hiciera esta consulta de

**[0:26:25]** ese chiquita es mayor

**[0:26:27]** que ese grande

**[0:26:29]** me va a dar que es verdad

**[0:26:31]** ok entonces el valor

**[0:26:34]** cuando yo mapeo de un carácter

**[0:26:36]** a un número

**[0:26:38]** el valor que tiene ese chiquita

**[0:26:40]** es más grande que el valor que tiene ese grande

**[0:26:42]** entonces si es que yo ordeno

**[0:26:44]** por orden alfabetico

**[0:26:46]** de menor a mayor

**[0:26:48]** primero van a aparecerlas con ese grande

**[0:26:50]** y después van a aparecerlas con ese chiquita

**[0:26:53]** o sea no son iguales además

**[0:26:55]** porque uno es mayor que la otra

**[0:26:57]** para el computador una S mayúscula

**[0:26:59]** y una S minúscula no son la misma letra

**[0:27:04]** y llegamos a la que es como

**[0:27:06]** más complicada que es el group by

**[0:27:08]** el group by lo que hace

**[0:27:10]** me permite agrupar

**[0:27:12]** por valores

**[0:27:14]** de las columnas que yo quiera

**[0:27:16]** entonces básicamente si le digo

**[0:27:18]** quiero agrupar por esta columna

**[0:27:20]** no se por ocupación

**[0:27:22]** va a ver la tabla

**[0:27:24]** y va a ver por cada

**[0:27:26]** valor único de ocupación no se por ejemplo

**[0:27:28]** por cada estudiante va a tomar

**[0:27:30]** todos los estudiantes y los va a agrupar

**[0:27:32]** los va a agrupar va a tomar todo ese conjunto

**[0:27:34]** de filas

**[0:27:36]** que tienen ocupación estudiante

**[0:27:38]** que hago con eso porque

**[0:27:40]** si es que las agrupos estoy aplanando la información

**[0:27:42]** como que la combino toda entonces por eso

**[0:27:44]** cuando hago group by además

**[0:27:46]** necesito una operación

**[0:27:48]** matemática que hacer con respecto

**[0:27:50]** a eso para que me pueda entregar

**[0:27:52]** algún resumen

**[0:27:54]** de la información que agrupó

**[0:27:56]** entonces puede ser por ejemplo el promedio

**[0:27:58]** puede ser un camp, puede ser sumar

**[0:28:00]** puede ser un mínimo, un máximo

**[0:28:02]** etcétera etcétera

**[0:28:04]** entonces de repente

**[0:28:06]** dependiendo de la

**[0:28:08]** versión de pandas

**[0:28:10]** me puede dar

**[0:28:12]** problemitas con la tabla resultante

**[0:28:14]** si es que yo

**[0:28:17]** tengo muchos datos y trato de

**[0:28:19]** agrupar por alguna tabla

**[0:28:21]** trato de sacar el promedio

**[0:28:23]** y tengo

**[0:28:25]** columnas no numéricas

**[0:28:27]** ahí me puede dar algún problemita

**[0:28:29]** así que ahora por ejemplo vamos a

**[0:28:31]** obtener una sub tabla

**[0:28:33]** que solo tenga

**[0:28:35]** id, edad, ocupación

**[0:28:37]** y calificación

**[0:28:39]** porque id, edad y calificación

**[0:28:41]** son números

**[0:28:43]** solo por eso y yo quiero sacar

**[0:28:45]** un valor que solamente se puede aplicar

**[0:28:47]** a números no es cierto información numérica

**[0:28:49]** que es la media

**[0:28:51]** y vamos a ocupar ocupación que no es

**[0:28:53]** numérica pero la puedo ocupar

**[0:28:55]** porque voy a agrupar por ella

**[0:28:57]** entonces como se ocupa el group by

**[0:29:00]** tomo mi tabla

**[0:29:02]** en este caso todo esto sería mi tabla

**[0:29:04]** el operador punto y luego pongo

**[0:29:06]** esta palabra que es group by

**[0:29:08]** que sería la función group by

**[0:29:10]** y dentro le voy a poner el nombre

**[0:29:12]** de la columna por la cual yo quiero agrupar

**[0:29:14]** porque eso es por columna

**[0:29:16]** entonces va a tomar cada valor

**[0:29:18]** de la columna ocupación

**[0:29:20]** y por cada valores que combine

**[0:29:22]** les va a sacar la media

**[0:29:26]** entonces ahora ocupación

**[0:29:28]** si se dan cuenta ya no está en el mismo formato

**[0:29:30]** que id, edad y calificación

**[0:29:32]** porque ocupación pasa a ser

**[0:29:34]** id de la tabla

**[0:29:36]** ok el id de la tabla

**[0:29:38]** ahora el id ya no tengo el id numérico

**[0:29:40]** sino que tengo un id que es una palabra

**[0:29:42]** que en este caso sería cada valor en ocupación

**[0:29:44]** entonces agrupa todos los administradores

**[0:29:46]** y saca el promedio de los id

**[0:29:48]** el promedio de la edad

**[0:29:50]** y el promedio de la calificación

**[0:29:52]** porque está agrupando todos esos valores

**[0:29:54]** y le estoy pidiendo el promedio

**[0:29:56]** y las justo las columnas que tengo

**[0:29:58]** son las que yo selecciono aquí

**[0:30:00]** me saca el promedio de cada columna

**[0:30:03]** entonces puedo saber por ejemplo

**[0:30:05]** la edad promedio

**[0:30:07]** de todos los usuarios

**[0:30:09]** o de técnicamente

**[0:30:11]** la edad promedio

**[0:30:13]** de las calificaciones

**[0:30:15]** que fueron hechas

**[0:30:18]** por ejecutivos

**[0:30:20]** o por profesionales de la sala

**[0:30:22]** porque aquí como

**[0:30:24]** son calificaciones

**[0:30:26]** se me puede repetir la misma persona

**[0:30:28]** más de una vez así que no sería como la edad

**[0:30:30]** promedio de los usuarios

**[0:30:32]** la promedio

**[0:30:34]** de las calificaciones

**[0:30:36]** una consulta

**[0:30:39]** si

**[0:30:41]** por ejemplo cuando lo agrupas

**[0:30:43]** que pasa si

**[0:30:45]** la ocupación

**[0:30:47]** no la coloca

**[0:30:49]** o tiene que estar si o si

**[0:30:51]** porque se está agrupando

**[0:30:53]** en torno a eso por ejemplo

**[0:30:55]** ahí sale tal la completa

**[0:30:57]** si es que yo tratará

**[0:30:59]** hacer un group by por una columna

**[0:31:01]** no va a dar error porque esa columna

**[0:31:03]** tiene que estar si o si

**[0:31:05]** esa columna tiene que existir si o si

**[0:31:07]** en la tabla que les estoy pasando

**[0:31:09]** hacer el filtro primero

**[0:31:11]** hago el filtro primero a grupo

**[0:31:13]** y después hago la operación

**[0:31:20]** entonces aquí

**[0:31:22]** aquí estoy haciendo aquí

**[0:31:24]** estoy haciendo exactamente lo mismo de antes

**[0:31:26]** si ven como que tomo esto

**[0:31:28]** y lo copio aquí

**[0:31:30]** es lo mismo

**[0:31:32]** si se dan cuenta por ejemplo yo podría no querer

**[0:31:34]** el ID y no querer la edad

**[0:31:36]** y se me olvido como filtrarla

**[0:31:38]** entonces también la puedo filtrar al final

**[0:31:40]** porque técnicamente esto que es resultante

**[0:31:42]** es una tabla

**[0:31:44]** entonces también puedo hacerle operaciones

**[0:31:46]** a la tabla después

**[0:31:48]** entonces yo puedo simplemente acceder a la columna

**[0:31:50]** que yo quisiera

**[0:31:53]** entonces ahí tengo por ejemplo la calificación

**[0:31:55]** promedio

**[0:31:57]** por estas ocupaciones

**[0:32:03]** bueno y ahí solo le puedo sacar por ejemplo

**[0:32:05]** la calificación máxima porque como dije

**[0:32:07]** esto que sigue siendo el resultado

**[0:32:09]** de un group buy sigue siendo

**[0:32:11]** una tabla entonces igual yo puedo

**[0:32:13]** hacerle operaciones de tabla

**[0:32:15]** entonces no se le puedo sacar el máximo

**[0:32:17]** el ARMAX, el IDMAX etc etc

**[0:32:19]** entonces me dice

**[0:32:23]** que la calificación máxima

**[0:32:25]** está dada por

**[0:32:27]** bueno la calificación promedio

**[0:32:29]** máxima la calificación promedio más alta

**[0:32:31]** está dada por

**[0:32:33]** ese numerito

**[0:32:35]** y el índice es el 12

**[0:32:37]** pero aquí no tengo el índice

**[0:32:39]** así que cuál es

**[0:32:41]** justo la 9

**[0:32:43]** los que no marcaron ocupación

**[0:32:45]** que fome

**[0:32:47]** ya

**[0:32:52]** y por si acaso

**[0:32:54]** yo aquí agrupe solamente por

**[0:32:56]** una columna pero yo puedo agrupar

**[0:32:58]** por más de una columna

**[0:33:00]** por ejemplo puedo hacer un group buy

**[0:33:02]** y si es que agrupo por más de una columna

**[0:33:04]** lo tengo que pasar como si fuera una lista

**[0:33:06]** ok

**[0:33:08]** entonces aquí puedo agrupar por ejemplo por

**[0:33:10]** edad y por ocupación

**[0:33:12]** y sacar la media y ver la tabla resultante

**[0:33:14]** el punto es que la tabla resultante

**[0:33:16]** lo que va a pasar con las columnas

**[0:33:18]** que yo ocupé para agrupar

**[0:33:20]** esas columnas se van a transformar como

**[0:33:22]** en un ID

**[0:33:24]** y va a ser un ID

**[0:33:27]** múltiples por decirlo así

**[0:33:30]** ok se dan cuenta que H

**[0:33:32]** y Occupation están como más abajitos

**[0:33:34]** las palabras que ID y calificación

**[0:33:36]** es porque ID y calificación son

**[0:33:38]** columnas y en cambio

**[0:33:40]** H y Occupation

**[0:33:42]** son los índices

**[0:33:44]** son los índices de cada fila

**[0:33:46]** porque ya no dejaron de ser columnas

**[0:33:48]** yo no las puedo acceder como columnas

**[0:33:50]** son el índice de cada fila

**[0:33:52]** entonces como agrupe por 2

**[0:33:54]** obviamente voy a tener como un doble índice

**[0:33:56]** entonces por ejemplo

**[0:33:58]** va a tomar cada valor de edad

**[0:34:00]** y después va por cada valor de edad

**[0:34:02]** a agrupar por ocupación

**[0:34:04]** por ejemplo tengo

**[0:34:06]** la edad 7 que tiene estudiantes

**[0:34:08]** la edad 10 que tiene también

**[0:34:10]** estudiantes la edad 11 que tiene non

**[0:34:12]** la edad 13 que tiene non

**[0:34:14]** y la edad 13 ahí

**[0:34:16]** puede ser ocupación non

**[0:34:18]** o puede ser ocupación otros

**[0:34:20]** hay edades que tienen varias ocupaciones

**[0:34:22]** por ejemplo la edad 70

**[0:34:24]** cuando yo la intento agrupar tiene varias ocupaciones

**[0:34:26]** así que me va a salir la ocupación administrador

**[0:34:28]** la ocupación ingeniero

**[0:34:30]** y la ocupación retida

**[0:34:32]** finalmente cada vez que ocupe el group by

**[0:34:34]** con alguna de las columnas

**[0:34:36]** pasaría a ser como un índice

**[0:34:38]** y no, claro, no podría tocarlas

**[0:34:40]** más como columnas

**[0:34:42]** si, exactamente

**[0:34:44]** se vuelven

**[0:34:50]** como multi index

**[0:34:53]** y ahí el reset index

**[0:34:55]** no me acuerdo aquí si esto va a dar error

**[0:34:57]** no, no debería

**[0:34:59]** el reset index es lo que hace que vuelvan

**[0:35:01]** a ser columnas

**[0:35:03]** si se dan cuenta, si yo le hago un reset index

**[0:35:05]** significa que

**[0:35:07]** quiero que vuelva a tener índice numérico

**[0:35:09]** el índice por defecto

**[0:35:11]** entonces estos índices

**[0:35:13]** que eran palabras y que eran información

**[0:35:15]** lo que hace es transformarlos en columnas

**[0:35:17]** de nuevo y transformarlos como

**[0:35:19]** pero no vuelvo a la tabla original por si acaso

**[0:35:21]** la tabla original no es esto

**[0:35:23]** sino que esto

**[0:35:25]** el índice

**[0:35:27]** lo vuelve columna

**[0:35:29]** pero no hace la operación inversa

**[0:35:31]** no hace como un desgroup by

**[0:35:33]** sino que esta tabla me la transforma

**[0:35:35]** simplemente esto en una columna

**[0:35:37]** y esto también en una columna iterable

**[0:35:39]** y el índice se transforma

**[0:35:41]** simplemente de 0 al número

**[0:35:43]** pero en ese caso a, si vuelve a ser

**[0:35:45]** a es que a nunca fue eso

**[0:35:47]** no, a no

**[0:35:49]** no es la tabla original

**[0:35:51]** es la tabla después del group by

**[0:35:53]** entonces yo aquí no es la tabla original

**[0:35:55]** pero aquí ya puedo entrar

**[0:35:57]** a hacer operaciones por ejemplo sobre la columna edad

**[0:35:59]** sabiendo que esta edad

**[0:36:01]** es la edad después de hacer la

**[0:36:03]** si la agrupación

**[0:36:05]** ya

**[0:36:12]** eso era lo que nos había quedado pendiente

**[0:36:14]** porque el group by es la última operación

**[0:36:16]** entonces el ejercicio 1

**[0:36:18]** yo sé que lo hicimos en conjunto

**[0:36:20]** llegamos hasta el final

**[0:36:22]** si llegamos hasta el final

**[0:36:24]** hasta el 1.4 lo hicimos en conjunto

**[0:36:26]** la clase pasada

**[0:36:28]** porque, porque ninguna de estas

**[0:36:31]** ninguna de estas cosas

**[0:36:33]** que preguntaba

**[0:36:35]** si requiere el group by

**[0:36:37]** o alguna cosa como más

**[0:36:39]** compleja

**[0:36:41]** de las que no habíamos visto

**[0:36:43]** pero en cambio el ejercicio 2

**[0:36:45]** si requiere estas cosas como más complejas

**[0:36:47]** alguna pregunta

**[0:36:49]** si yo si va a requerir un group by

**[0:36:51]** a menos de que se les ocurra una manera

**[0:36:53]** de hacerlo sin eso

**[0:36:55]** porque aquí no hay una respuesta

**[0:36:57]** en concreto correcta

**[0:36:59]** hay múltiples formas de llegar a la respuesta

**[0:37:01]** por si acaso

**[0:37:03]** no me ocurrió a mí

**[0:37:05]** pero con tal de que la salida coincida

**[0:37:07]** estaba todo bien

**[0:37:09]** entonces estos ejercicios 2

**[0:37:11]** ya son, pueden

**[0:37:13]** puedo pedirles que ocupen por ejemplo

**[0:37:15]** el value count o el group by

**[0:37:17]** o algún filtro

**[0:37:19]** que son como operaciones más complejas

**[0:37:21]** como la segunda parte de la práctica

**[0:37:24]** pero eso va a quedar pendiente

**[0:37:26]** para ustedes

**[0:37:28]** entonces dudas sobre esta materia

**[0:37:30]** porque si no ya voy a pasar a la otra

**[0:37:36]** con una parte y salía un non

**[0:37:38]** creo que un poquito más arriba

**[0:37:40]** más

**[0:37:43]** aquí este

**[0:37:45]** esa parte

**[0:37:47]** no entendí bien como se calculó

**[0:37:49]** me lo salté mucho pero

**[0:37:51]** básicamente yo estoy haciendo 3 operaciones

**[0:37:53]** que no son de

**[0:37:55]** como de nampa y más que de

**[0:37:58]** pandas que yo estoy haciendo un max

**[0:38:00]** para ver el valor

**[0:38:02]** máximo en este caso va a tomar

**[0:38:04]** la columna y va a ver cuál es el valor

**[0:38:06]** más alto

**[0:38:08]** después estoy haciendo un arc max

**[0:38:10]** y eso es básicamente

**[0:38:12]** el argumento del máximo

**[0:38:14]** y en este sería el índice

**[0:38:16]** del valor máximo

**[0:38:18]** que puede ser un poquito al revés que aquí

**[0:38:20]** ok, es el

**[0:38:24]** número o la posición

**[0:38:26]** en la cual se encuentra el valor máximo

**[0:38:28]** y este id xmax

**[0:38:30]** lo que me entrega es el índice

**[0:38:32]** de la tabla

**[0:38:34]** es donde se encuentra el valor máximo

**[0:38:36]** ok

**[0:38:39]** entonces el índice de la tabla

**[0:38:41]** es básicamente como aquí tenemos el id

**[0:38:43]** de ocupación

**[0:38:45]** el índice de la tabla es la ocupación

**[0:38:47]** que tiene el máximo

**[0:38:49]** promedio en calificación

**[0:38:51]** entonces por eso me dan

**[0:38:53]** si, la posición 12 pero aquí me da

**[0:38:55]** el valor del id en la posición

**[0:38:57]** 12, entonces este me da el número

**[0:38:59]** y este me da su valor

**[0:39:01]** si

**[0:39:06]** por ejemplo tuvieran el índice numérico

**[0:39:08]** los dos serían iguales

**[0:39:10]** ah, si, si estos fueran números serían iguales

**[0:39:12]** bueno

**[0:39:14]** si estos fueran números y no siguieran

**[0:39:16]** el orden podría ser cualquier cosa

**[0:39:18]** por ejemplo si estos fueran 20.000

**[0:39:20]** me daría 20.000 en vez de 9

**[0:39:22]** porque recordemos que

**[0:39:25]** los id

**[0:39:28]** pueden tener cualquier número

**[0:39:30]** esto me está dando la posición

**[0:39:32]** ah, si, pero si fueran como los índices

**[0:39:34]** normales 0 1

**[0:39:36]** ahi si

**[0:39:38]** si

**[0:39:40]** de nada

**[0:39:43]** alguna otra duda

**[0:39:45]** de la práctica en general

**[0:39:47]** puede ser de también lo que vimos la clase pasada

**[0:39:57]** ya, parece que no

**[0:39:59]** eh

**[0:40:01]** que me metí al red

**[0:40:04]** no, me metí a este el base

**[0:40:06]** entonces vamos a cambiar a la de hoy día

**[0:40:08]** que la subí reciente

**[0:40:10]** o sea, no recién ya pasó un rato

**[0:40:12]** porque vimos la clase pero la subí como

**[0:40:14]** casi a las 8

**[0:40:16]** si dicen de dónde sacaste eso

**[0:40:18]** bueno, la subí a las 8

**[0:40:20]** así que si revisan el canva

**[0:40:22]** de la asignatura debería estar ya

**[0:40:24]** que es calidad de datos y subí

**[0:40:26]** el vacío, siempre al principio

**[0:40:28]** de la clase le voy a subir el vacío y después ya después

**[0:40:30]** harto después le voy a subir

**[0:40:32]** la respuesta así es que

**[0:40:34]** dejo algún ejercicio

**[0:40:37]** entonces el contenido que tenemos

**[0:40:39]** que ver hoy día es calidad de datos

**[0:40:41]** y esto tiene que ver

**[0:40:43]** con básicamente

**[0:40:45]** no es tan fácil, fácil de explicar

**[0:40:47]** porque depende mucho

**[0:40:49]** del conjunto de datos que yo tenga

**[0:40:51]** como puedo ver si el conjunto de datos es bueno

**[0:40:53]** o malo y como le puedo hacer una

**[0:40:55]** limpieza para que

**[0:40:57]** sea útil para mi modelo

**[0:40:59]** o sea útil para mi análisis

**[0:41:01]** entonces vamos a ver algunas cosas que nos pueden servir

**[0:41:03]** pero

**[0:41:05]** la forma de limpiar

**[0:41:07]** un data set depende mucho del tipo

**[0:41:09]** de data set, yo no les puedo decir

**[0:41:11]** esto es sí o sí lo que hay que hacer

**[0:41:13]** siempre tiene que hacer esto

**[0:41:15]** porque siempre hay un

**[0:41:17]** depende, siempre puede

**[0:41:19]** depender de algo, por ejemplo en el caso de

**[0:41:21]** valores fuera de rango

**[0:41:23]** como yo sé que un valor está fuera de rango

**[0:41:25]** depende del problema, depende

**[0:41:27]** de la columna, siempre es un depende

**[0:41:29]** entonces yo les entrego como las herramientas

**[0:41:31]** en general que se pueden como ir

**[0:41:33]** adaptando y ya después

**[0:41:35]** ustedes tienen que ver según su

**[0:41:37]** según su problema

**[0:41:39]** que puede ser útil para

**[0:41:41]** ustedes y como lo pueden ir adaptando para eso

**[0:41:43]** entonces, hay veces

**[0:41:46]** en que mis datos siempre vamos a estar

**[0:41:48]** hablando de datos tabulares aquí

**[0:41:50]** en que mis datos pueden estar incompletos

**[0:41:52]** pueden estar ruidosos

**[0:41:54]** o pueden ser como inconsistentes

**[0:41:56]** pueden tener valores

**[0:41:58]** nada que ver, entonces

**[0:42:00]** qué hago si es que tengo duplicados

**[0:42:02]** qué hago si tengo valores fuera de rango

**[0:42:04]** qué hago si tengo valores faltantes

**[0:42:06]** o qué pasa si tengo símbolos extraños

**[0:42:08]** o valores null o null

**[0:42:10]** útiles, entonces cosas

**[0:42:12]** que me dificultan en las análisis de los datos pueden ser

**[0:42:14]** índices poco significativos

**[0:42:16]** columnas con tipo de dato incorrecto

**[0:42:18]** o índices repetidos

**[0:42:20]** o también datos repetidos

**[0:42:22]** entonces, primero voy

**[0:42:25]** tengo ejecutado

**[0:42:28]** esto, ¿por qué tengo ejecutado esto?

**[0:42:30]** qué mentira, voy a correr esto

**[0:42:32]** voy a importar las librerías y me voy a creer

**[0:42:34]** un lindo dataset de

**[0:42:36]** juguete, que ya casi ni me acuerdo

**[0:42:38]** de qué se trata esto porque hace tiempo

**[0:42:40]** que no lo ve, entonces lo vamos a crear

**[0:42:42]** como data frame

**[0:42:44]** porque normalmente cuando cargamos un dato

**[0:42:46]** un conjunto de datos lo vamos a cargar así

**[0:42:48]** y vamos a ver qué tiene

**[0:42:50]** porque de verlo así

**[0:42:52]** yo típicamente cuando cargo

**[0:42:54]** un conjunto de datos lo primero que tengo que hacer es

**[0:42:56]** ver cómo es

**[0:42:58]** para entender más o menos con lo que estoy trabajando

**[0:43:00]** entonces con el head

**[0:43:03]** que ya habíamos visto en la clase pasada

**[0:43:05]** un head, un tail, un describe

**[0:43:07]** un info, cualquiera de eso, solamente

**[0:43:09]** para ver los datos, para yo poder entender

**[0:43:11]** con lo que estoy trabajando es

**[0:43:13]** una buena práctica, primero

**[0:43:15]** si es que me pasa en una tabla, yo tengo que ver

**[0:43:17]** más o menos qué contiene, entonces

**[0:43:19]** tengo el ID

**[0:43:21]** de por sí de la tabla y también tengo un ID aparte

**[0:43:23]** como columna, hay un código

**[0:43:25]** asociado, hay una entidad

**[0:43:27]** que hice full cargo

**[0:43:29]** hay una calle y un número, asumimos

**[0:43:31]** que es una dirección, también puede tener

**[0:43:33]** algo adicional para esta dirección

**[0:43:35]** tiene una comuna, más info

**[0:43:37]** de una dirección, y tiene

**[0:43:39]** día, dice día inicio, día y fin

**[0:43:41]** hora inicio, hora fin, carga máxima, carga mínima

**[0:43:43]** y

**[0:43:45]** este norte longitud el latitud, entonces

**[0:43:47]** esto los vamos a subir como

**[0:43:49]** coordenadas, tiene como

**[0:43:51]** coordenadas asociadas al lugar

**[0:43:53]** tiene una dirección

**[0:43:55]** asociada al lugar y también tiene

**[0:43:57]** días y horas

**[0:43:59]** ok, entonces

**[0:44:01]** ah, y también tiene cantidades

**[0:44:03]** por carga máxima y carga mínima

**[0:44:05]** y ya solamente viendo esta tabla

**[0:44:07]** vemos algo extraño, que

**[0:44:09]** carga mínima

**[0:44:11]** tiene valores y carga máxima

**[0:44:13]** también tiene valores, pero

**[0:44:15]** carga mínima no tiene el puntito

**[0:44:18]** y

**[0:44:20]** carga mínima tampoco tiene el signo peso

**[0:44:22]** que algunos valores que se ven en carga máxima

**[0:44:24]** carga máxima si lo tienen, entonces ya aquí

**[0:44:26]** ya veo, solamente mirando veo una inconsistencia

**[0:44:28]** tiene valor negativo también

**[0:44:30]** hay valores negativos

**[0:44:32]** como signos de 100.000

**[0:44:35]** ah, perdón, no la he visto

**[0:44:37]** aquí veo algo extraño, aquí veo un valor

**[0:44:39]** negativo que dependiendo

**[0:44:41]** de lo que yo estoy trabajando puede ser un error

**[0:44:43]** o algo extraño, dependiendo

**[0:44:45]** siempre depende y también veo valores

**[0:44:47]** vacíos, porque aquí no hay nada

**[0:44:49]** aquí no hay nada, aquí no hay nada, aquí no hay nada

**[0:44:51]** aquí no hay nada, etcétera

**[0:44:53]** hay mucho de nada adicional, por ejemplo que no hay nada

**[0:44:55]** y ya, entonces puedo hacer

**[0:44:57]** también un info para que me diga

**[0:44:59]** y miren, no me dice

**[0:45:01]** dice que hay 24 filas

**[0:45:03]** 24 entradas y todos

**[0:45:05]** me dicen que hay 24 nonulos

**[0:45:07]** entonces

**[0:45:09]** esto no es un nan sino que

**[0:45:11]** es como si es que en el excel no hubieran puesto nada

**[0:45:13]** es un espacio en blanco

**[0:45:15]** literal es un espacio en blanco

**[0:45:17]** entonces le puedo hacer un describe

**[0:45:19]** para que me diga que onda

**[0:45:21]** en este caso, nosotros ya vimos

**[0:45:23]** que si yo hago un describe por defecto

**[0:45:25]** me voy a mostrar la información

**[0:45:27]** de los datos que son numéricos

**[0:45:29]** y si yo le hago un include

**[0:45:31]** object, me voy a mostrar información

**[0:45:33]** de los datos que no son numéricos

**[0:45:35]** y si yo le pongo un all

**[0:45:37]** que creo que no lo vimos, me da todo

**[0:45:39]** lo malo es que aquí voy a ver

**[0:45:41]** datos nan porque no le puedo sacar

**[0:45:43]** la media a datos que no son numéricos

**[0:45:45]** y no le puedo sacar por ejemplo

**[0:45:47]** el top o si

**[0:45:49]** ah no, un top, ya no he dicho

**[0:45:51]** pero voy a ver muchos nan porque tengo muchas

**[0:45:53]** si vemos aquí

**[0:45:55]** tengo muchas columnas que son de tipo object

**[0:45:57]** que no son número

**[0:45:59]** y eso que hay una columna que se llama num

**[0:46:01]** y no es de tipo número

**[0:46:03]** raro

**[0:46:06]** también las coordenadas

**[0:46:08]** no son tipo número, son objeto

**[0:46:10]** más raro todavía

**[0:46:12]** entonces aquí más o menos puedo ver

**[0:46:14]** por ejemplo habíamos visto que la carga mínima

**[0:46:16]** tenía algo raro

**[0:46:19]** no es cierto porque vivimos

**[0:46:21]** que tenía un valor negativo

**[0:46:23]** entonces le voy a ver el mínimo

**[0:46:25]** y es un valor negativo

**[0:46:27]** al menos la carga mínima

**[0:46:29]** está como numérico

**[0:46:31]** está como numérico

**[0:46:33]** lo raro es que la carga máxima no

**[0:46:35]** bueno no tan raro porque vi que tenía un signo peso

**[0:46:37]** pero no está como numérico

**[0:46:39]** y quizás sería más fácil verlo como numérico

**[0:46:41]** para análisis y todo eso

**[0:46:43]** entonces hay muchas cosas con las que trabajar aquí

**[0:46:45]** yo podría mejorar dependiendo de mi tipo de análisis

**[0:46:47]** por ejemplo

**[0:46:49]** simplemente viendo el tipo de dato de carga máxima

**[0:46:51]** yo ya no la podrían analizar como número

**[0:46:53]** porque está de tipo objeto

**[0:46:55]** ya veo un problema

**[0:46:57]** la carga mínima tengo valores negativos

**[0:46:59]** tengo hartos nan, kevi, etc

**[0:47:01]** etc

**[0:47:03]** muchas cosas que hacer

**[0:47:05]** solamente ganando esta información

**[0:47:07]** solamente mirando los datos

**[0:47:10]** nada del otro mundo

**[0:47:12]** todo el info, el describe, el head

**[0:47:14]** ya lo habíamos visto

**[0:47:16]** muchas veces vamos a trabajar con las cosas que ya vimos

**[0:47:18]** la clase pasa

**[0:47:20]** pero el duplicate

**[0:47:22]** primero duplicados

**[0:47:24]** puede ser que yo tenga valores

**[0:47:26]** repetidos, entonces tengo una columna

**[0:47:28]** que me dice que tengo 1000 valores

**[0:47:30]** cuando en realidad no es así

**[0:47:32]** pueden ser muchos valores que esté duplicados

**[0:47:34]** y en realidad eso no me aporta información nueva

**[0:47:36]** no me sirven de nada, estoy ocupando espacio

**[0:47:38]** en cosas que no me sirven técnicamente

**[0:47:40]** entonces para revisarse una tabla

**[0:47:42]** tiene filas duplicadas

**[0:47:44]** podemos usar la función que se llama duplicator

**[0:47:46]** y para eliminar los duplicados hay una función

**[0:47:48]** para eso que se llama drop duplicates

**[0:47:50]** entonces por ejemplo

**[0:47:52]** mi tabla se llama ejemplo

**[0:47:54]** por ejemplo yo puedo poner el nombre de la tabla

**[0:47:56]** los corchetes

**[0:47:58]** y después le pongo ejemplo.duplicator

**[0:48:00]** porque duplicates me da

**[0:48:02]** una salida

**[0:48:04]** que es un bool

**[0:48:06]** un true, un false

**[0:48:08]** un verdadero un falso indicándome si cada

**[0:48:10]** fila está repetida o no

**[0:48:12]** entonces si es que yo hago

**[0:48:17]** ejemplo, corchetitos

**[0:48:19]** esta tabla que tiene verdadero falso

**[0:48:21]** me voy a mostrar las que tienen verdadero

**[0:48:23]** es decir me voy a mostrar

**[0:48:25]** las filas

**[0:48:27]** que están repetidas

**[0:48:29]** entonces me dice que estas filas

**[0:48:31]** exactamente

**[0:48:33]** están repetidas en su totalidad

**[0:48:35]** en su totalidad

**[0:48:40]** pero puede pasar

**[0:48:42]** que yo no necesite

**[0:48:44]** tener duplicados de una columna específica

**[0:48:46]** sino que no puedo tener duplicados

**[0:48:48]** por ejemplo en el id

**[0:48:50]** si nos dimos cuenta

**[0:48:53]** hay una columna que se llama id

**[0:48:55]** no debería tener duplicados ahí

**[0:48:57]** porque no puedo tener dos operaciones con el mismo id

**[0:48:59]** asumiendo que esta es una operación así

**[0:49:01]** entonces puedo pedirle

**[0:49:03]** que me revise los duplicados de esa columna específica

**[0:49:05]** simplemente

**[0:49:07]** accediendo a la columna específica

**[0:49:09]** y haciendo la misma operación duplicate

**[0:49:11]** entonces me dice que

**[0:49:15]** todos estos

**[0:49:17]** están repetidos

**[0:49:19]** cada uno parece solo una vez eso

**[0:49:21]** pero están repetidos

**[0:49:23]** me refiero que cada uno tiene solamente una repetición

**[0:49:25]** entonces

**[0:49:28]** yo podría por ejemplo

**[0:49:30]** setear

**[0:49:32]** una nueva tabla

**[0:49:34]** que tenga este índice id

**[0:49:36]** que está malito

**[0:49:38]** para poder como darles el ejemplo de que paso

**[0:49:40]** si yo tuviera índices duplicados

**[0:49:42]** cuál es el problema de tener índices duplicados

**[0:49:44]** bueno si es que yo tengo

**[0:49:46]** índices duplicados

**[0:49:48]** se acuerdan que nosotros podíamos acceder

**[0:49:50]** a las posiciones con lock

**[0:49:52]** y iLock

**[0:49:54]** con la posición relativa en la tabla

**[0:49:56]** y lock era con el índice

**[0:49:58]** bueno cuando yo hago operaciones con lock

**[0:50:00]** normalmente espero que solamente tengan

**[0:50:02]** si es que yo le pongo un solo índice

**[0:50:04]** espero que me llegue un solo resultado

**[0:50:06]** entonces puedo

**[0:50:08]** hacer alguna consulta en que yo espere

**[0:50:10]** un solo resultado

**[0:50:12]** y cuando me de como te... si yo tuviera

**[0:50:14]** índices repetidos eso no va a pasar

**[0:50:16]** si yo tuviera índices repetidos y hago un lock

**[0:50:18]** me va a dar múltiples resultados

**[0:50:20]** entonces mi código puede fallar

**[0:50:22]** o puedo tener cosas con distintos

**[0:50:24]** como con un comportamiento que yo no esperaba

**[0:50:26]** entonces lo ideal es que el

**[0:50:28]** índice no esté repetido

**[0:50:30]** entonces por ejemplo aquí

**[0:50:32]** que se tiene el index

**[0:50:34]** a esta nueva tabla con algo que yo sé

**[0:50:36]** que está repetido que algo que se está malo

**[0:50:38]** hago el ejemplo a hacerle un lock

**[0:50:40]** y cuando yo esperaría solamente

**[0:50:42]** una fila

**[0:50:44]** un dato aquí me da dos

**[0:50:46]** entonces aquí tengo un problema

**[0:50:48]** entonces yo

**[0:50:51]** para cambiar el índice

**[0:50:53]** puedo hacer un set index

**[0:50:55]** ok puedo cambiar el índice a una columna

**[0:50:57]** que yo sé que si o si

**[0:50:59]** no tiene que tener repetidos

**[0:51:01]** por ejemplo si fueran personas podría poner

**[0:51:03]** no sé

**[0:51:06]** podría poner el root

**[0:51:08]** podría poner el root por ejemplo

**[0:51:10]** o alguna cosa así o el número

**[0:51:12]** de documento alguna cosa

**[0:51:14]** alguna cosa así

**[0:51:16]** y también si es que quiero sacar este índice

**[0:51:18]** simplemente tengo que hacer el reset index

**[0:51:20]** si es que quiero hacer

**[0:51:22]** la operación

**[0:51:24]** que reemplace la tabla original recordemos que tener

**[0:51:26]** la opción de inplace to

**[0:51:30]** así saco ese índice

**[0:51:32]** y ya después empiezo como a

**[0:51:34]** a sacar los duplicados

**[0:51:36]** bueno primero a verlos con esta forma

**[0:51:38]** que les mostré y ahora vamos a ver como sacarlos

**[0:51:44]** ya como lo saco

**[0:51:46]** con esta forma que yo les dije que se llama

**[0:51:48]** drop duplicates

**[0:51:50]** el drop duplicates sin argumentos

**[0:51:52]** me va a sacar todas las filas

**[0:51:54]** que sean exactamente iguales

**[0:51:56]** exactamente iguales

**[0:51:58]** una copia la misma que la otra

**[0:52:00]** en su totalidad

**[0:52:02]** sin contar el índice

**[0:52:04]** entonces si yo hago ejemplo

**[0:52:06]** que es el nombre de la tabla punto drop duplicates

**[0:52:09]** me va a dar una tabla en donde

**[0:52:11]** borró los duplicados

**[0:52:13]** ok

**[0:52:15]** entonces como yo veo que borró los duplicados

**[0:52:17]** normalmente debería haber un salto en los índices

**[0:52:19]** pero yo no creo que los ve aquí

**[0:52:21]** debería haber sido los duplicados que agreguemos

**[0:52:23]** después

**[0:52:25]** ay porque le hizo un reset índice

**[0:52:27]** así que no creo que los ve

**[0:52:29]** y si es que

**[0:52:31]** yo quisiera

**[0:52:34]** solamente tener en cuenta

**[0:52:36]** los duplicados de una columna específica

**[0:52:38]** por ejemplo asumiendo que estoy trabajando con personas

**[0:52:40]** y no puedo tener dos personas con el mismo root

**[0:52:42]** entonces hago un drop duplicates por

**[0:52:44]** root específico si yo quiero indicar eso

**[0:52:46]** tengo que meterme al drop duplicates

**[0:52:48]** y ponerle un valor

**[0:52:50]** en este parámetro que se llama subset

**[0:52:52]** y dentro de subset tengo que poner el nombre

**[0:52:54]** de las columnas que puede ser más de una

**[0:52:56]** en este caso vamos a poner el id

**[0:52:58]** porque vamos a asumir que ese es el valor

**[0:53:00]** único

**[0:53:02]** de cada fila aquí, de cada descripción

**[0:53:04]** vamos a asumir que ese es como su root

**[0:53:06]** y con eso

**[0:53:11]** yo ya debería haber iluminado todos

**[0:53:13]** las filas que tuvieran el id duplicado

**[0:53:15]** entonces ahora puedo simplemente

**[0:53:17]** revisar con el duplicates

**[0:53:19]** de nuevo para ver si me sale algo

**[0:53:21]** si no me sale nada

**[0:53:23]** significa que yo no hay filas con el id

**[0:53:25]** repetido

**[0:53:27]** y porque esto me elimina las filas

**[0:53:29]** que había visto al principio

**[0:53:31]** se acuerdan cuando hicimos un duplicates

**[0:53:33]** del ejemplo entero

**[0:53:35]** aquí

**[0:53:37]** aquí me muestro si

**[0:53:39]** cuando dice eliminarlo duplicado

**[0:53:41]** se refiere a que quita las columnas

**[0:53:43]** que tienen igual descando una

**[0:53:45]** si

**[0:53:47]** si

**[0:53:49]** yo tuviera por ejemplo este duplicates

**[0:53:51]** no me está mostrando dos filas

**[0:53:53]** iguales sino que nos está mostrando

**[0:53:55]** las que están

**[0:53:57]** duplicadas o sea no me muestra la original

**[0:53:59]** hay una original que dejo tranquila

**[0:54:01]** voy a tomar como la primera coincidencia

**[0:54:04]** como la original y después

**[0:54:06]** cuando ya encuentro algo que

**[0:54:08]** ya vi lo tomo como repetido

**[0:54:10]** y es lo que muestro en el duplicates

**[0:54:12]** y es lo que se elimina con el drop duplicates

**[0:54:14]** si aplicó el drop duplicates

**[0:54:17]** no voy a eliminar

**[0:54:19]** la información

**[0:54:22]** única

**[0:54:24]** si o si me voy a quedar con al menos una

**[0:54:26]** representación de los datos que yo considero duplicados

**[0:54:30]** ahí tienen que estar todas las columnas iguales

**[0:54:32]** o sea es como que

**[0:54:34]** la fila se repite exactamente

**[0:54:36]** para todas las columnas igual

**[0:54:38]** más de una vez

**[0:54:40]** si, si, si

**[0:54:42]** entonces como ya había hecho antes

**[0:54:44]** ejemplo punto duplicates

**[0:54:46]** significa que el id también estaba repetido

**[0:54:48]** duplicates, considerando el id

**[0:54:50]** estoy diciendo que ya la elimine

**[0:54:53]** así es fácil

**[0:54:55]** y entonces ya no debería tener

**[0:54:57]** una consulta y ahí el duplicates

**[0:54:59]** entonces se repite

**[0:55:01]** por la misma fila

**[0:55:03]** 3 o 4 de eso

**[0:55:05]** más de 2

**[0:55:07]** y también

**[0:55:09]** nos muestra o no? si, me voy a salir más pc

**[0:55:11]** me voy a salir más pc

**[0:55:15]** gracias

**[0:55:17]** ya, así quito

**[0:55:20]** duplicados

**[0:55:22]** una forma super

**[0:55:24]** como fácil

**[0:55:26]** de medir como la calidad de los datos

**[0:55:28]** de siempre buscar duplicados

**[0:55:30]** porque es fácil de ver, simplemente

**[0:55:32]** trato de ir o hago un duplicated

**[0:55:34]** para toda la tabla

**[0:55:36]** o identifico cuál sería

**[0:55:38]** como el índice

**[0:55:40]** de mis datos o el id

**[0:55:42]** de mis datos

**[0:55:44]** y reviso si es que esos tienen algún duplicado

**[0:55:46]** y como dije, esto siempre depende

**[0:55:48]** de lo que tenga

**[0:55:50]** por ejemplo

**[0:55:53]** para los usuarios

**[0:55:55]** en la tabla que me hemos visto antes de películas

**[0:55:57]** cada usuario tenía un id específico

**[0:55:59]** entonces si yo podría ir a la tabla de usuarios

**[0:56:01]** y ver si es que hay algún duplicator

**[0:56:03]** del id

**[0:56:05]** que hay un duplicator del id tengo un usuario varias veces

**[0:56:07]** eso es extraño

**[0:56:09]** cosas

**[0:56:11]** entonces tengo que identificar cuál sería

**[0:56:13]** como la

**[0:56:15]** columna que sí o sí es única

**[0:56:17]** y esa es la que debo revisar

**[0:56:19]** y depende de mi problema

**[0:56:21]** a veces esa columna puede que no exista

**[0:56:23]** ya

**[0:56:25]** eso con duplicados

**[0:56:27]** luego valores fuera de rango, aquí también

**[0:56:29]** depende de mucho

**[0:56:31]** con lo que yo esté trabajando

**[0:56:33]** por ejemplo

**[0:56:35]** un valor fuera de rango puede ser edades negativas

**[0:56:37]** según dependiendo como si tuviera datos de personas

**[0:56:39]** yo no debería tener edades negativas

**[0:56:41]** mediciones negativas

**[0:56:43]** o valores que yo sé que son imposibles

**[0:56:45]** estoy trabajando en una

**[0:56:47]** planta y sé que

**[0:56:49]** cierta temperatura

**[0:56:51]** debe ir en un rango entre

**[0:56:53]** 0 y

**[0:56:55]** 0 y 120 y veo un 5000

**[0:56:57]** y ahí veo que hay un error

**[0:56:59]** de sensor y ese dato no me sirve

**[0:57:01]** para analizar el comportamiento por ejemplo normal

**[0:57:03]** entonces ese debería eliminar

**[0:57:05]** siempre depende

**[0:57:08]** de mi

**[0:57:10]** de mi problema

**[0:57:12]** una forma más fácil de ver esto

**[0:57:14]** es cuando la columna es numérica

**[0:57:16]** porque cuando la columna es numérica

**[0:57:18]** fácilmente cuando hay un valor fuera de rango

**[0:57:20]** es numérica y simplemente tengo que ver

**[0:57:22]** el rango y para ver el rango

**[0:57:24]** imprimo el mínimo y imprimo el máximo

**[0:57:26]** entonces accedo a la columna

**[0:57:28]** y ocupo punto min

**[0:57:30]** y punto max

**[0:57:33]** y si

**[0:57:35]** entonces en carga mínima tengo valores negativos

**[0:57:37]** no debería ser así

**[0:57:39]** ya no debería tener valores negativos

**[0:57:41]** y para ver esto de mínimo y máximo

**[0:57:43]** fácilmente para todas las columnas numéricas

**[0:57:45]** ocupamos el describe

**[0:57:47]** en este caso

**[0:57:49]** se lo tengo dos columnas numéricas

**[0:57:51]** también es extraño

**[0:57:54]** pero bueno las columnas que están netamente numéricas

**[0:57:56]** aquí para analizar son simplemente

**[0:57:58]** carga mínima y el id

**[0:58:00]** y el id yo asumo que no puede ser negativo

**[0:58:02]** entonces le miro el mínimo es 1

**[0:58:04]** tiene sentido

**[0:58:06]** la carga mínima yo también voy a asumir que no puede ser negativa

**[0:58:08]** tiene menos 1000

**[0:58:10]** es raro

**[0:58:13]** entonces veo que eso es raro

**[0:58:15]** tengo que tomar una decisión

**[0:58:17]** siempre tengo que tomar una decisión puede ser

**[0:58:19]** cambio algún

**[0:58:22]** valor lo cambio como por la centralidad

**[0:58:24]** puede ser no se reemplazo

**[0:58:26]** de los valores negativos por la media

**[0:58:28]** o por la mediana

**[0:58:30]** elimino los valores negativos

**[0:58:32]** o se cambia por el mínimo permitido

**[0:58:34]** ok

**[0:58:37]** o por tener alguna

**[0:58:39]** otro protocolo que me diga que debo hacer

**[0:58:41]** pero siempre depende de

**[0:58:43]** como que tengo que tomar una decisión así

**[0:58:45]** no hay un camino que yo diga ya

**[0:58:47]** esto es negativo si o si hay que hacer esto

**[0:58:49]** siempre depende

**[0:58:51]** en este caso una forma fácil es

**[0:58:53]** asumir que es un error de tipeo

**[0:58:55]** y se pasó a

**[0:58:57]** como a digitar un menos

**[0:58:59]** cuando en realidad el valor real

**[0:59:01]** es el valor

**[0:59:03]** sin el signo menos

**[0:59:05]** entonces el valor en este caso el valor correcto

**[0:59:07]** sería el valor absoluto

**[0:59:09]** entonces es fácil de reemplazar

**[0:59:11]** a la columna

**[0:59:13]** y decir oye tu valor en realidad

**[0:59:15]** es tu valor absoluto para hacer el valor absoluto

**[0:59:17]** hay una operación que se llama

**[0:59:19]** punto apps de absolute

**[0:59:21]** y eso me obtiene el valor absoluto

**[0:59:23]** y esto me va a tirar un warning

**[0:59:25]** a no mentira

**[0:59:27]** a veces va a tirar un warning

**[0:59:29]** pero con eso yo ya cambié

**[0:59:31]** el valor

**[0:59:33]** por su valor absoluto

**[0:59:36]** yo puedo hacer un log también

**[0:59:38]** por ejemplo para obtener

**[0:59:40]** es que tengo muchas alternativas aquí

**[0:59:42]** yo puedo

**[0:59:44]** con un log acceder

**[0:59:46]** a todos los ejemplos que tengan carga mínima

**[0:59:48]** menor a cero

**[0:59:50]** acceder a su valor carga mínima y no sé

**[0:59:52]** poner

**[0:59:55]** aquí estoy haciendo lo mismo

**[0:59:57]** estoy accediendo a exactamente el mismo valor

**[0:59:59]** y multiplicándolo por menos uno

**[1:00:01]** o sea literal

**[1:00:03]** esto negativo lo estoy multiplicando por menos uno

**[1:00:05]** lo estoy haciendo positivo es lo mismo que hacer apps

**[1:00:07]** aquí tengo otra alternativa para hacer eso mismo

**[1:00:09]** y aquí tengo otra alternativa para hacer eso mismo

**[1:00:11]** esto ocupando una función

**[1:00:13]** lambda

**[1:00:15]** creo que no la vamos a ver

**[1:00:17]** en este curso

**[1:00:19]** creo quizá en un curso de python ya la vieron

**[1:00:21]** pero ahí está de ejemplo

**[1:00:23]** y también aquí está con una función

**[1:00:25]** de numpy que se llama where

**[1:00:27]** le puedo poner

**[1:00:29]** un

**[1:00:32]** como una condición

**[1:00:34]** de cuando esto pase

**[1:00:36]** lo que quiero hacer cuando es verdad

**[1:00:38]** y lo que quiero hacer cuando no se cumple

**[1:00:40]** entonces

**[1:00:42]** cuando se cumple que este valor es menor que cero

**[1:00:44]** cuando sí se cumple eso

**[1:00:46]** reemplázalo por el valor

**[1:00:48]** multiplicado por menos uno

**[1:00:50]** y cuando no se cumple eso reemplázalo por el

**[1:00:52]** valor origino

**[1:00:55]** distinta alternativa para hacer exactamente

**[1:00:57]** esto mismo

**[1:00:59]** recuerdan que les dije que no hay una respuesta correcta

**[1:01:01]** para hacer algo bueno

**[1:01:03]** cuando yo hago algo en código

**[1:01:05]** ustedes lo pueden pensar de otra manera

**[1:01:07]** con todas las funciones que hemos aprendido

**[1:01:09]** o con funciones extra

**[1:01:11]** por ejemplo funciones de nampa

**[1:01:13]** o función lambda etc

**[1:01:15]** eso es por ejemplo

**[1:01:19]** con valores fuera de rango

**[1:01:21]** que pasa si tengo valores faltantes

**[1:01:23]** cuando tengo valores faltantes

**[1:01:25]** normalmente yo veo un nan o un null

**[1:01:27]** y tengo funciones específicas

**[1:01:29]** para ver cuando algo es nan o null

**[1:01:31]** entonces para nan

**[1:01:33]** normalmente

**[1:01:35]** aquí bueno esto disminuyó porque

**[1:01:37]** eliminé lo negativo

**[1:01:39]** antes había 24 horas y 19

**[1:01:41]** me dice que está todo bien

**[1:01:43]** que tengo 19 datos en cualquier columna

**[1:01:45]** entonces si yo le hago un isna

**[1:01:47]** que como dije cuando hay nan

**[1:01:50]** hay operaciones especiales

**[1:01:52]** para ver cuando algo es nan

**[1:01:54]** para nan está el isna

**[1:01:56]** y esto me da true

**[1:01:58]** si es que el valor tiene

**[1:02:00]** si es que la columna

**[1:02:02]** si es que la fila posee

**[1:02:04]** algún nan y me da false

**[1:02:06]** y yo puedo sumarlos

**[1:02:08]** mentira es en la columna

**[1:02:13]** es en la columna

**[1:02:15]** lo está haciendo por columna

**[1:02:17]** entonces me dice que no hay nada que sea un nan

**[1:02:19]** o sea

**[1:02:21]** estoy teniendo un problema porque yo vi unos valores vacíos

**[1:02:23]** pero están registrados como por alguna cuestión

**[1:02:25]** entonces lo que pasa

**[1:02:27]** es que muchos valores nan

**[1:02:29]** se han puesto como espacio en blanco en las celdas

**[1:02:31]** entonces aquí yo puedo utilizar

**[1:02:33]** una función que se llama replace

**[1:02:35]** y que no es una función

**[1:02:37]** en este caso sí es una función de pandas

**[1:02:39]** pero se parece a la función de strings

**[1:02:41]** de python cuando yo quiero

**[1:02:43]** reemplazar un carácter por algún otro

**[1:02:45]** en python y aquí se está haciendo lo mismo

**[1:02:47]** yo quiero reemplazar un espacio en blanco

**[1:02:49]** por

**[1:02:51]** np.nan

**[1:02:53]** que sería la forma de

**[1:02:55]** un nan aquí numéricamente

**[1:02:57]** y aquí yo le podría pasar

**[1:03:00]** simplemente el espacio en blanco

**[1:03:02]** así

**[1:03:04]** o así, o así, o así

**[1:03:06]** dependiendo de la forma que tenga el espacio en blanco

**[1:03:08]** pero también le puedo pasar

**[1:03:10]** una expresión regular

**[1:03:12]** ok

**[1:03:14]** y si es que yo le paso una expresión regular

**[1:03:16]** en rigex

**[1:03:18]** tengo que ponerle true

**[1:03:20]** si es que no fuera una expresión regular

**[1:03:22]** tengo que ponerle false

**[1:03:24]** creo que por defecto está en false

**[1:03:26]** así que por defecto asume que no le pasó una

**[1:03:29]** pero en este caso le vamos a pasar una expresión regular

**[1:03:31]** ooo

**[1:03:33]** que pasa si hago el info

**[1:03:35]** no me cambia y en adicional

**[1:03:37]** tengo 4 valores nonulos

**[1:03:39]** en este tengo 6 valores nonulos

**[1:03:41]** en norte tengo 16 valores nonulos

**[1:03:43]** entonces algo cambió

**[1:03:45]** y ahora si hago el isna.zoom

**[1:03:47]** ahora si

**[1:03:50]** me salen nans aquí

**[1:03:52]** me salen nans aquí y me salen nans aquí

**[1:03:54]** entonces mi función

**[1:03:56]** de reemplazo funciona

**[1:03:58]** y ahora hubo ocupar el isna de manera fácil

**[1:04:00]** para ver porque yo los quiero pasar a nan

**[1:04:02]** ah también puedo preguntar

**[1:04:05]** adicionalmente

**[1:04:07]** cuáles no son nan

**[1:04:09]** con not na

**[1:04:11]** tengo el isna

**[1:04:13]** para saber cuando algo es

**[1:04:15]** vacío y tengo el not na

**[1:04:17]** para saber cuando algo no es vacío

**[1:04:19]** técnicamente

**[1:04:21]** ya

**[1:04:23]** entonces los valores nonulos los puedo dejar

**[1:04:25]** eliminar en plaza

**[1:04:27]** y esto depende otra vez

**[1:04:29]** siempre depende con los datos con los que yo estoy trabajando

**[1:04:31]** entonces por qué los quiero pasar a nan

**[1:04:33]** porque como dije hay funciones

**[1:04:35]** especiales para poder trabajar con esto

**[1:04:37]** puedo por ejemplo

**[1:04:39]** sacar la media

**[1:04:41]** y

**[1:04:43]** ignorar los que son nan

**[1:04:45]** por ejemplo puedo hacer operaciones matemáticas

**[1:04:47]** y hay algunas operaciones matemáticas

**[1:04:49]** que hoy yo les pongo un argumento

**[1:04:51]** o la función se llama de manera especial

**[1:04:53]** de tal manera que me calcule

**[1:04:55]** esa operación ignorando los nan

**[1:04:57]** porque a veces si es que yo tengo un nan

**[1:04:59]** y hago una suma

**[1:05:01]** o saco alguna estadística

**[1:05:03]** lo que pasa si hay un nan

**[1:05:05]** es que todo el resultado se me va a nan

**[1:05:07]** y me arruina todo

**[1:05:09]** de manera segura yo puedo sacar como una media

**[1:05:11]** ignorando los nan poniéndole un argumento

**[1:05:13]** ocupando una función especial

**[1:05:15]** y también

**[1:05:17]** tengo por ejemplo la función

**[1:05:19]** fil na

**[1:05:21]** que es para reemplazar los valores

**[1:05:23]** los llenas

**[1:05:27]** entonces vimos que la columna

**[1:05:29]** esta columna que se llama este

**[1:05:31]** tiene valores nan

**[1:05:33]** entonces yo puedo

**[1:05:35]** ver que valores típicos

**[1:05:37]** tiene esto para ver como los voy a reemplazar

**[1:05:43]** entonces lo primero que voy a ver

**[1:05:45]** es que tipo de dato es

**[1:05:47]** es de tipo de dato object

**[1:05:49]** por lo cual yo podría insertar números

**[1:05:51]** insertar strings, insertar lo que yo quiera

**[1:05:53]** bueno inserto un número

**[1:05:55]** no se como lo vaya a interpretar

**[1:05:57]** no se como si lo va a guardar como número

**[1:05:59]** entonces yo podría reemplazarlo

**[1:06:01]** con un 0 sin ningún problema

**[1:06:03]** tengo que ver el tipo de dato porque si es que fuera

**[1:06:05]** solo numérico y yo lo quiero reemplazar

**[1:06:07]** con un no aplica

**[1:06:09]** por ejemplo eso me va a romper la lógica

**[1:06:11]** de la

**[1:06:13]** de la columna

**[1:06:15]** primero tengo que ver qué tipo de dato es

**[1:06:17]** entonces yo puedo poner

**[1:06:19]** fil na le paso el valor

**[1:06:21]** que yo quiero reemplazar

**[1:06:23]** y el in place es para

**[1:06:25]** simplemente reemplazar la tabla original

**[1:06:27]** con esta

**[1:06:29]** con la nueva tabla que se origina

**[1:06:31]** con esta operación

**[1:06:33]** eso es lo que hace el in place

**[1:06:36]** se me va a decir cuidado

**[1:06:38]** pero bueno

**[1:06:41]** y simplemente me va a quedar

**[1:06:43]** se me dan a reemplazar los valores na

**[1:06:45]** y le voy a poner un 0 y eso es todo lo que hace

**[1:06:47]** y si es que quiero volver a ponerla

**[1:06:49]** puedo usar por ejemplo el replay

**[1:06:51]** el replay también lo puedo ocupar

**[1:06:53]** para volver de un valor al otro

**[1:06:55]** no hay problema

**[1:06:58]** yo quiero reemplazar con un valor

**[1:07:00]** fil na

**[1:07:02]** que pasa si yo los quiero eliminar

**[1:07:04]** tengo un drop especial para la columna que se llama

**[1:07:06]** drop na

**[1:07:09]** sin argumentos esta función

**[1:07:11]** elimina cualquier fila que contenga

**[1:07:13]** un nan en alguna parte

**[1:07:15]** da lo mismo me elimina la fila entera

**[1:07:17]** entonces yo tengo que tener cuidado

**[1:07:19]** con esto

**[1:07:21]** porque qué pasa si yo tengo una columna

**[1:07:23]** inutil una columna

**[1:07:25]** que no me sirve en realidad

**[1:07:27]** si yo hago un drop na

**[1:07:29]** voy a eliminar

**[1:07:31]** muchas filas

**[1:07:33]** que podrían ser útiles pero que tienen un na

**[1:07:35]** en esa columna inútil

**[1:07:37]** en esa columna inútil entonces voy a perder mucho de uso

**[1:07:39]** entonces tengo que tener cuidado con esto

**[1:07:41]** entonces por ejemplo

**[1:07:44]** adicional

**[1:07:46]** que es como una información adicional

**[1:07:48]** de la dirección

**[1:07:50]** en realidad quizá no es tan necesaria

**[1:07:52]** y tiene muchos nan

**[1:07:54]** entonces si yo eliminara

**[1:07:56]** por adicional

**[1:07:58]** voy a estar perdiendo mucha info

**[1:08:00]** por una columna quizá inútil

**[1:08:02]** entonces tengo que tener cuidado con eso

**[1:08:05]** qué pasa si es que yo

**[1:08:07]** quisiera hacer un drop na

**[1:08:09]** pero solamente mirando una columna en específico

**[1:08:11]** tengo que ponerle un subset

**[1:08:13]** lo mismo que en el drop duplicate

**[1:08:15]** entonces lo tengo que usar como

**[1:08:17]** el nombre de mi tabla punto drop na

**[1:08:19]** le paso en subset el nombre de una columna

**[1:08:21]** que puede ser más de una

**[1:08:23]** en este caso

**[1:08:25]** bueno ejemplo vamos a eliminar

**[1:08:27]** todas las

**[1:08:29]** filas

**[1:08:31]** que en la columna este

**[1:08:33]** tengan un nan

**[1:08:37]** y me va a dar

**[1:08:39]** una tabla muy chiquita

**[1:08:41]** porque hay hartos nan aquí

**[1:08:43]** entonces pierdo muchos datos

**[1:08:45]** entonces tengo que mirar realmente

**[1:08:47]** si esa columna es de interés o no

**[1:08:49]** y si hiciera un ejemplo punto drop na

**[1:08:53]** así entero

**[1:08:55]** me queda solamente una fila

**[1:08:57]** esa columna no va

**[1:08:59]** las columnas que tienen nan no vale tanto

**[1:09:01]** la pena mantenerla

**[1:09:03]** porque estoy perdiendo mucha información

**[1:09:05]** tratando de mantener esa columna

**[1:09:07]** en mi tabla

**[1:09:09]** entonces aquí tendría que tomar decisiones sobre

**[1:09:11]** qué quiero mantener

**[1:09:13]** entonces como pierdo

**[1:09:15]** muchos datos eliminando estos valores nulos

**[1:09:17]** tengo que ver si es que

**[1:09:19]** estas columnas que tienen hartos valores nulos

**[1:09:21]** son útiles o no

**[1:09:23]** o si es que de verdad los quiero eliminar

**[1:09:25]** pero también reemplazarlos no se conoce

**[1:09:27]** cero o algo así

**[1:09:31]** si hasta aquí todo bien

**[1:09:38]** una pregunta tenía

**[1:09:40]** un poquito más arriba

**[1:09:42]** cuando estaba

**[1:09:44]** tratando de

**[1:09:46]** te aparecieron esos trece esta cuerda

**[1:09:48]** pusiste un carácter raro una error

**[1:09:50]** con un gato o hasta el disco

**[1:09:52]** no entendí bien por qué

**[1:09:54]** esto es una expresión

**[1:09:56]** es una expresión regular

**[1:09:58]** no creo

**[1:10:00]** no sé si la vieron antes

**[1:10:02]** no sé si es necesario tanto verlas

**[1:10:04]** pero

**[1:10:06]** lo que pasa

**[1:10:08]** es que yo puedo

**[1:10:10]** tener muchas formas

**[1:10:12]** de tener un carácter

**[1:10:14]** un carácter

**[1:10:16]** en blanco por ejemplo puedo tener un espacio

**[1:10:18]** o puedo tener dos espacios

**[1:10:20]** o puedo tener tres espacios

**[1:10:22]** o puedo tener un tab

**[1:10:24]** hay muchas formas de tener un carácter en blanco

**[1:10:26]** y todo eso yo los voy a ver como algo

**[1:10:28]** vacío

**[1:10:30]** entonces qué pasa si quiero reemplazarlos

**[1:10:32]** todos

**[1:10:34]** lo que voy a decirle

**[1:10:36]** a mi replays es que

**[1:10:38]** voy a ocupar una expresión regular

**[1:10:40]** le estoy diciendo oye todo lo que sea

**[1:10:43]** un carácter en blanco

**[1:10:45]** eliminámelo eso es lo que está diciendo la expresión regular

**[1:10:47]** en vez de decirle

**[1:10:49]** solamente este

**[1:10:51]** reemplazalo con un nan

**[1:10:53]** le estoy diciendo oye no es sólo este

**[1:10:56]** sino que este también

**[1:10:58]** y este también

**[1:11:00]** y este también

**[1:11:02]** todo eso lo estoy diciendo

**[1:11:05]** con la expresión regular

**[1:11:07]** no, parece que no lo han visto antes

**[1:11:09]** pero

**[1:11:12]** no creo que entremos tanto

**[1:11:14]** en detalle con eso

**[1:11:17]** no crees sencillamente entenderlo un poquito

**[1:11:19]** de todo lo que mencionaste

**[1:11:21]** me he quedado volvido

**[1:11:23]** la expresión regular

**[1:11:25]** aquí estoy diciendo el inicio de la expresión

**[1:11:27]** y aquí estoy diciendo el final de la expresión

**[1:11:29]** es un backslash

**[1:11:31]** un backslash ese

**[1:11:33]** es el carácter en blanco

**[1:11:36]** y el asterisco estoy diciendo que aparezca

**[1:11:38]** una vez

**[1:11:40]** que aparezca cero veces o muchas veces

**[1:11:42]** entonces es como que sólo haya un carácter en blanco

**[1:11:44]** porque aquí empieza la expresión y aquí está el final

**[1:11:46]** entonces que sólo haya un carácter en blanco

**[1:11:48]** que sólo contenga carácter en blanco

**[1:11:50]** y que aparezca o cero

**[1:11:52]** o infinito a veces

**[1:11:54]** todos esos son los carácteres que estoy tomando en cuenta

**[1:11:56]** para reemplazarlos por esto

**[1:11:58]** por eso es muy útil como la expresión regular aquí

**[1:12:00]** gracias

**[1:12:02]** ya

**[1:12:07]** igual creo que vamos a ver un poquito

**[1:12:09]** operaciones de string más abajo

**[1:12:11]** pero quizás ya las vieron, si ya las vieron las podemos saltar

**[1:12:18]** me quedé aquí

**[1:12:20]** ya y eso es con datos

**[1:12:22]** nan o nul

**[1:12:24]** para nul también

**[1:12:26]** hay un isnul

**[1:12:28]** etcétera etcétera

**[1:12:31]** los datos no útiles

**[1:12:33]** esto depende demasiado

**[1:12:35]** de el data set con el que estoy trabajando

**[1:12:37]** cuando tengo datos no útiles

**[1:12:39]** simplemente yo puedo

**[1:12:41]** eliminarlos sin que me afecten

**[1:12:43]** todo el data set

**[1:12:45]** entonces yo dije que si elimino

**[1:12:47]** todos los nan que tiene la columna este

**[1:12:49]** y todos los nan por ejemplo

**[1:12:51]** que tienen la columna adicional

**[1:12:53]** en realidad estoy perdiendo mucha información

**[1:12:55]** y quizás esto no es

**[1:12:57]** importante para el problema

**[1:12:59]** porque yo quiero analizar

**[1:13:01]** entonces en ese caso

**[1:13:03]** vamos a asumir que estas columnas

**[1:13:05]** son info que no es útil

**[1:13:07]** ok

**[1:13:11]** entonces lo que podemos hacer

**[1:13:13]** es con una función que nosotros ya vimos

**[1:13:15]** que es el drop

**[1:13:17]** podemos simplemente eliminar estas columnas

**[1:13:19]** cuando nosotros vimos como eliminar

**[1:13:21]** filas o columnas, vimos el drop

**[1:13:23]** y cuando quiero eliminar columnas simplemente hago

**[1:13:25]** columns y pongo el nombre

**[1:13:27]** de las columnas

**[1:13:29]** entonces ahora que yo ya eliminé

**[1:13:31]** estas columnas

**[1:13:33]** que yo consideraba no útiles

**[1:13:35]** ahora puedo hacer un análisis de decir bueno

**[1:13:37]** si es que me quedan nulos

**[1:13:39]** que hago con esos nulos, los reemplazas

**[1:13:41]** etc etc

**[1:13:43]** entonces la idea sería primero ver

**[1:13:45]** que datos no son útiles

**[1:13:47]** y después ver

**[1:13:49]** ya cuáles son los nulos

**[1:13:51]** entonces

**[1:13:54]** con este drop ya ejemplo

**[1:13:56]** me queda así

**[1:14:01]** hacer un punto info

**[1:14:06]** para que veamos que como boté

**[1:14:08]** estas tres columnas que yo no consideré útiles

**[1:14:10]** ahora ya no tengo nans

**[1:14:12]** de nuevo, entonces ya no tengo que hacer una

**[1:14:14]** una cosa muy compleja

**[1:14:17]** ve una manito

**[1:14:19]** ahora me parece una notificación

**[1:14:22]** si, una consulta

**[1:14:24]** cuando comentaste recién

**[1:14:26]** los datos y el no sé qué

**[1:14:28]** y el plurrora, ¿a qué te agarías con eso?

**[1:14:30]** que es ahí como

**[1:14:32]** que

**[1:14:34]** no sé qué quieres decir

**[1:14:36]** con

**[1:14:38]** todo lo que sigue

**[1:14:40]** por favor

**[1:14:42]** lo que estoy diciendo aquí

**[1:14:44]** es que al menos lo que entiendo

**[1:14:46]** que es la pregunta es que yo dije

**[1:14:48]** que estoy sacando

**[1:14:50]** estas columnas

**[1:14:52]** que tenían muchos valores nulos

**[1:14:54]** y yo asumí

**[1:14:56]** que estas columnas no eran útiles

**[1:14:58]** entonces

**[1:15:00]** esta decisión

**[1:15:02]** debería analizarla

**[1:15:05]** primero, antes

**[1:15:07]** de eliminar valores nulos

**[1:15:09]** antes de eliminar valores nulos, yo primero debería

**[1:15:11]** definir

**[1:15:13]** cuáles columnas son útiles

**[1:15:15]** o cuál la información es útil

**[1:15:17]** y cuál es inútil

**[1:15:19]** porque si es que yo hubiera hecho un dropna

**[1:15:21]** general

**[1:15:23]** estas columnas me hubieran dejado con solamente una fila

**[1:15:25]** lo cual me hace

**[1:15:27]** perder demasiada información

**[1:15:29]** primero debería decir

**[1:15:31]** si o si me sirven

**[1:15:33]** y después empiezo a hacer todo este análisis

**[1:15:35]** de si es que tienen valores nulos

**[1:15:37]** si es que no tienen valores nulos

**[1:15:39]** y qué hago a partir de los valores nulos

**[1:15:41]** si es que los reemplazo, si es que los elimino

**[1:15:43]** si es que ya elimino la columna

**[1:15:45]** no más, etc

**[1:15:47]** creo que eso era lo que quise decir

**[1:15:49]** sí, se entendió

**[1:15:51]** muchas gracias

**[1:15:53]** ya

**[1:15:55]** entonces yo eliminar estas tres columnas

**[1:15:57]** ya no me queda ni un nan

**[1:15:59]** con respecto a eso

**[1:16:01]** estamos más o menos tranquilos

**[1:16:03]** ahora tengo que ver otras inconsistencias

**[1:16:05]** que haya en los datos

**[1:16:07]** entonces

**[1:16:10]** aquí vamos a ver algunas cositas de strings

**[1:16:12]** aunque si ya las conocen

**[1:16:14]** me dicen que lo podemos saltar

**[1:16:16]** pero operaciones sobre strings

**[1:16:18]** qué me pasa con la tabla

**[1:16:20]** que la tabla a veces presenta inconsistencias

**[1:16:22]** en datos que son de tipo objeto

**[1:16:24]** o que sean un string

**[1:16:26]** que son palabras

**[1:16:28]** que podemos usarlo todo en el mismo formato

**[1:16:30]** por ejemplo aquí si vemos

**[1:16:32]** la columna calle

**[1:16:34]** yo tengo que aquí esto está en mayúscula

**[1:16:36]** esto está en minúscula

**[1:16:38]** esto está en minúscula y esto está en mayúscula

**[1:16:40]** o sea tengo

**[1:16:43]** a veces sí, a veces no

**[1:16:45]** una inconsistencia

**[1:16:47]** entonces si es que yo hiciera alguna

**[1:16:49]** consulta sobre esto

**[1:16:51]** y ocupara solo mayúsculas

**[1:16:53]** las que están en minúscula no me las encontraría

**[1:16:55]** aquí entonces tengo un problema

**[1:16:57]** en los datos porque voy a hacer consultas

**[1:16:59]** que no me van a dar toda la información

**[1:17:01]** que yo requiero

**[1:17:04]** entonces yo puedo pasar

**[1:17:06]** un string de mayúscula

**[1:17:08]** a minúscula o de minúscula a mayúscula

**[1:17:10]** de forma fácil

**[1:17:12]** con estas operaciones de python

**[1:17:14]** que se llaman upper y lower

**[1:17:16]** entonces upper para arriba

**[1:17:18]** entonces me la voy a poner todo en mayúscula

**[1:17:20]** entonces si yo le paso un string

**[1:17:22]** que sea hola y hago la punto upper

**[1:17:24]** me voy a devolver el hola en mayúscula

**[1:17:26]** mayúscula y si yo le paso un hola

**[1:17:28]** punto lower

**[1:17:30]** lower para abajo entonces en minúscula

**[1:17:32]** entonces me la devolver todo esto en minúscula

**[1:17:35]** ok, entonces upper

**[1:17:37]** mayúsculas lower minúsculas

**[1:17:39]** y así

**[1:17:41]** una forma fácil de eliminar esta inconsistencia

**[1:17:43]** inconsistencia

**[1:17:45]** qué pasa cuando yo tengo espacios en blanco

**[1:17:47]** me puedes pasar por ejemplo que tengo este string

**[1:17:49]** que tiene uno espacio en blanco aquí

**[1:17:51]** y después dice hola como estás

**[1:17:54]** yo podría tener aquí

**[1:17:56]** pero yo creo que lo puse en algún momento

**[1:17:58]** porque fui mala

**[1:18:00]** alguna de estas debe tener algún espacio en blanco

**[1:18:02]** o al principio o al final

**[1:18:04]** que debo haberlo puesto por ahí

**[1:18:06]** entonces qué pasa si es que yo tuviera

**[1:18:08]** un nombre de alguien

**[1:18:10]** no se

**[1:18:12]** Fernando

**[1:18:14]** y al principio tiene un espacio en blanco

**[1:18:16]** o al final tiene un espacio en blanco

**[1:18:18]** entonces hago buscar coincidencias

**[1:18:20]** que sea exactamente Fernando

**[1:18:22]** la palabra Fernando tiene un espacio en blanco

**[1:18:24]** al final y sin espacio al principio

**[1:18:26]** no voy a encontrar la palabra Fernando

**[1:18:28]** que tiene un espacio en blanco al principio

**[1:18:30]** tiene un espacio en blanco al final

**[1:18:32]** voy a tener problemas con eso

**[1:18:34]** por esto espacio en blanco que yo no veo

**[1:18:36]** entonces puedo hacer un punto

**[1:18:39]** strip

**[1:18:41]** un punto strip me quita los espacios en blanco

**[1:18:43]** que están al principio y al final

**[1:18:45]** de cada frase

**[1:18:47]** no los que están entre

**[1:18:49]** caracteres así como normales

**[1:18:51]** sino los que están al principio

**[1:18:53]** y los que están al final

**[1:18:55]** que tampoco aportan nada

**[1:18:59]** este ola como estas que tenía mucho espacio al principio

**[1:19:01]** y un espacio inútil al final

**[1:19:03]** me lo devolvió con cero espacio al principio

**[1:19:05]** y cero espacio al final

**[1:19:07]** también está el replays

**[1:19:09]** el replays yo aquí pongo

**[1:19:11]** lo que quiero reemplazar

**[1:19:13]** que puede ser una expresión regular

**[1:19:15]** pero aquí vamos a poner un carácter simple

**[1:19:17]** y por lo que

**[1:19:19]** por lo que quiero reemplazar

**[1:19:21]** entonces aquí podría poner una contilde

**[1:19:23]** la quiero reemplazar por una cintilde

**[1:19:25]** una eñe la quiero reemplazar por una n

**[1:19:27]** cosas así

**[1:19:29]** entonces aquí estoy poniendo ejemplo que un espacio en blanco

**[1:19:31]** lo quiero reemplazar por

**[1:19:33]** nada

**[1:19:35]** osea voy a eliminar el espacio en blanco

**[1:19:37]** entonces ola como estas

**[1:19:40]** me va a quedar sin el espacio en blanco así

**[1:19:42]** ola como estas todo apretado

**[1:19:44]** esos son ejemplos como fáciles

**[1:19:46]** de manipulación

**[1:19:48]** de strings

**[1:19:50]** de palabras, de caracteres

**[1:19:53]** y aquí estoy mostrando

**[1:19:59]** estoy mostrando aquí un for

**[1:20:01]** con los valores únicos

**[1:20:03]** de cada columna

**[1:20:05]** entonces para mostrar como los valores únicos

**[1:20:07]** que tiene cada costumbre

**[1:20:09]** entonces por ejemplo ID

**[1:20:11]** tiene numeritos, código

**[1:20:13]** no es algo numérico

**[1:20:15]** está en objeto pero tiene puros números

**[1:20:17]** entidad solo tiene un valor

**[1:20:19]** tiene full carga

**[1:20:21]** que no me está portando nada porque todo tiene el mismo valor

**[1:20:23]** por ejemplo

**[1:20:26]** en calle tenemos este ejemplo

**[1:20:28]** inconsistencia que algunas están en minúsculas

**[1:20:30]** y en mayúsculas

**[1:20:32]** en comuna tengo el ejemplo

**[1:20:34]** ah la puse en comuna, si se dan cuenta

**[1:20:36]** aquí licura tiene un espacio en blanco al final

**[1:20:38]** eso es un tab

**[1:20:40]** tiene un espacio en blanco

**[1:20:42]** entonces ahí tengo un problemita

**[1:20:45]** tengo por ejemplo

**[1:20:47]** la florida con un espacio

**[1:20:49]** y después la florida sin el espacio

**[1:20:51]** entonces ahí tengo otro ejemplo

**[1:20:53]** otro problema

**[1:20:55]** tengo puente alto en mayúscula

**[1:20:57]** y después tengo puente alto en minúscula

**[1:20:59]** entonces aquí tengo mucha inconsistencia

**[1:21:01]** por ejemplo aquí en día inicio

**[1:21:03]** tengo lunes

**[1:21:05]** y tengo lunes

**[1:21:07]** tengo muchas inconsistencias de string

**[1:21:09]** en carga máxima teníamos los signos pesos

**[1:21:11]** que a veces aparecían al principio y al final

**[1:21:13]** tengo hasta un negativo

**[1:21:15]** tengo muchas inconsistencias de string

**[1:21:17]** entonces como puedo ir trabajando

**[1:21:19]** con estas operaciones de string

**[1:21:21]** no creo que las veamos toda

**[1:21:23]** pero como les doy las herramientas

**[1:21:25]** para que ataquen esto

**[1:21:28]** bueno, con estas operaciones

**[1:21:30]** que vimos

**[1:21:32]** yo puedo fácilmente resolver el problema

**[1:21:34]** de las mayúsculas y minúsculas

**[1:21:36]** también puedo

**[1:21:38]** eliminar los espacios

**[1:21:40]** que están al principio y al final

**[1:21:42]** y con un replay también puedo eliminar

**[1:21:44]** los espacios que están entre medio

**[1:21:46]** entonces todo lo puedo dejar en el mismo formato

**[1:21:48]** para yo poder hacer consultas

**[1:21:50]** y que la información

**[1:21:52]** que me retorna

**[1:21:54]** la consulta es la información que yo necesito

**[1:21:56]** porque no habrían inconsistencia

**[1:21:58]** en los datos

**[1:22:00]** entonces como hago todas estas operaciones

**[1:22:02]** no puedo llegar a hacerlas

**[1:22:04]** porque si es que yo accedo a la columna

**[1:22:06]** me va a dar error

**[1:22:08]** para trabajar sobre string

**[1:22:10]** entonces lo que tengo que hacer es

**[1:22:12]** acceder a la tabla, acceder a la columna

**[1:22:14]** y poner punto str

**[1:22:16]** como a los datos de string

**[1:22:18]** y ahí poder hacer toda la operación

**[1:22:20]** entonces una fácil

**[1:22:24]** es lunes

**[1:22:26]** y lunes

**[1:22:28]** si se dan cuenta podemos dejarlo todo en el mismo formato

**[1:22:30]** si es que solo obtenemos

**[1:22:32]** las primeras tres letras de cada día

**[1:22:34]** porque si vemos en el día fin

**[1:22:36]** tienen solamente

**[1:22:38]** tres letras de cada día

**[1:22:40]** ¿tienen sap, viern, domi?

**[1:22:42]** bueno sap, viern, dom

**[1:22:44]** que serían las primeras tres letras de cada día

**[1:22:46]** entonces para acceder a las primeras tres letras

**[1:22:48]** simplemente

**[1:22:50]** hacemos como un slice del string

**[1:22:52]** considerando solamente las primeras

**[1:22:54]** tres letras de cada día

**[1:22:56]** entonces por ejemplo aquí

**[1:22:58]** si yo hago ejemplo, punto, di, inicio, punto

**[1:23:00]** str

**[1:23:02]** si no lo hago en str no me va a salir

**[1:23:04]** para acceder a la operación

**[1:23:06]** a los strings

**[1:23:08]** y pongo el operador de slice

**[1:23:10]** y le digo que quiero todo hasta el

**[1:23:12]** segundo carácter

**[1:23:15]** entonces me va a dar todo esto

**[1:23:17]** y así voy a perder

**[1:23:19]** esto que estaba distinto

**[1:23:21]** entonces sabiendo que esta operación

**[1:23:23]** hace lo que yo quiero

**[1:23:25]** simplemente reemplazo

**[1:23:27]** oye esta columna y todos sus valores

**[1:23:29]** reemplazalo por la operación que había hecho

**[1:23:31]** antes que me da lo que quiero

**[1:23:34]** ya

**[1:23:37]** para las calles y la comuna

**[1:23:39]** vamos a eliminar los espacios en blanco

**[1:23:41]** y lo vamos a dejar todo en mayúscula

**[1:23:43]** entonces para acceder a la comuna

**[1:23:45]** para poder hacer la operación

**[1:23:47]** de string yo tengo que hacer str

**[1:23:49]** operación de string

**[1:23:51]** str, operación de string

**[1:23:53]** porque si no me va a dar de error

**[1:23:55]** y voy a obtener los values

**[1:23:57]** solo para mostrarlo

**[1:24:03]** maravilloso

**[1:24:07]** recordemos que tenía el problema de la florida

**[1:24:09]** y eso tiene que hacerlo con un lindo

**[1:24:11]** replays

**[1:24:13]** no es cierto se va a resolver con un replays

**[1:24:15]** para poder reemplazar

**[1:24:17]** comuna y calle haciendo

**[1:24:19]** operaciones de string que es con el strip

**[1:24:21]** y con el uppercut

**[1:24:26]** cuál es el problema de carga máxima

**[1:24:28]** son los

**[1:24:30]** los signos peso y los puntos

**[1:24:32]** ok tengo unos signos peso

**[1:24:34]** y tengo unos puntos que quiero eliminar

**[1:24:36]** para poder tratarlo todo como número

**[1:24:38]** hay uno que tiene un signo peso al final la Emma

**[1:24:40]** si, tiene un signo peso

**[1:24:42]** me asusté

**[1:24:44]** tiene un signo peso al final

**[1:24:46]** que hago para poder reemplazar algo

**[1:24:48]** y acceder al string

**[1:24:50]** cuando quiero reemplazar algo

**[1:24:52]** tengo que poner en la tabla

**[1:24:54]** el nombre de la columna

**[1:24:56]** la palabra está especial

**[1:24:58]** str y luego el replays

**[1:25:00]** ya no puedo poner simplemente solo replays

**[1:25:02]** porque si no así me va a encontrar la coincidencia tal cual

**[1:25:04]** entonces si yo le

**[1:25:06]** le saco este str

**[1:25:08]** y solo le pongo un punto replays así

**[1:25:10]** va a tratar de buscar

**[1:25:12]** en esa columna exactamente

**[1:25:14]** una palabra

**[1:25:16]** no el

**[1:25:18]** va a tratar de buscar la palabra

**[1:25:20]** que sea solamente el signo peso

**[1:25:22]** y eso es lo que va a reemplazar con nada

**[1:25:24]** entonces eso no me sirve

**[1:25:26]** yo necesito acceder al string

**[1:25:28]** y que en el string busque

**[1:25:30]** en cada string busque este signo peso

**[1:25:32]** y lo reemplace con nada

**[1:25:34]** y lo busque en cualquier parte

**[1:25:36]** si, en cualquier parte

**[1:25:38]** y si está repetido también

**[1:25:41]** si, si está repetido también

**[1:25:43]** este replays aquí

**[1:25:45]** lo vamos a mostrar como la salida

**[1:25:47]** y si se dan cuenta

**[1:25:49]** no me acuerdo cual era el que tenía dos

**[1:25:51]** el 100,000 tienes dos signo peso

**[1:25:53]** uno adelante y uno al final

**[1:25:55]** y este replays los elimina los dos

**[1:25:57]** porque busca todos

**[1:25:59]** en todos los strings busca cada vez que aparece

**[1:26:01]** y lo reemplaza con

**[1:26:03]** lo saca básicamente

**[1:26:05]** entonces

**[1:26:07]** podemos hacer lo mismo con este puntito

**[1:26:09]** o pasarlo a numerico

**[1:26:11]** podría hacerle un replays

**[1:26:13]** para que saque el signo peso

**[1:26:15]** y un replays para que saque el puntito

**[1:26:17]** y eso después simplemente

**[1:26:19]** lo

**[1:26:22]** lo reemplazo

**[1:26:24]** por los valores de la columna original

**[1:26:26]** y eso es simplemente

**[1:26:28]** con operaciones de string

**[1:26:30]** me voy a quedar un valor negativo

**[1:26:32]** que ustedes después multiplican pero

**[1:26:34]** esto es solamente para ver operaciones de string

**[1:26:36]** para reemplazar todo esto

**[1:26:38]** obteniendo

**[1:26:40]** como concatenando todas las dos operaciones

**[1:26:42]** haciéndole que saca el signo peso

**[1:26:44]** y haciéndole que saca el puntito

**[1:26:46]** ahora todo me queda como número

**[1:26:48]** número número número número

**[1:26:50]** si yo quisiera sacar este signo menos

**[1:26:52]** ahora sabiendo que esto es un string

**[1:26:54]** también podría ponerle un str

**[1:26:56]** le pongo el guión del signo menos

**[1:26:58]** y lo reemplazo con nada

**[1:27:00]** y también me voy a quitar este signo menos

**[1:27:02]** problemático antes de que yo lo pase a número

**[1:27:04]** entonces

**[1:27:08]** es que ahí cuando

**[1:27:10]** entendí muy bien

**[1:27:12]** esa cuando no está el str

**[1:27:14]** como que es lo que hace

**[1:27:16]** si no está el str

**[1:27:18]** va a buscar la palabra que sea exactamente

**[1:27:20]** solo un signo peso

**[1:27:22]** la coincidencia exacta no me va a buscar

**[1:27:24]** dentro del string sino que va a decir

**[1:27:26]** el string es un signo peso

**[1:27:28]** entonces por eso yo tengo que

**[1:27:30]** hacer la operación dentro del string

**[1:27:32]** por eso lo tengo para el punto str

**[1:27:38]** y aquí tengo algo

**[1:27:41]** el contains pero no sé si es tan necesario

**[1:27:43]** pero

**[1:27:45]** puede ser

**[1:27:47]** puede puede ser

**[1:27:49]** que pasa si yo quisiera hacer

**[1:27:51]** una consulta

**[1:27:53]** sobre los strings

**[1:27:55]** no sé sobre los valores de una tabla

**[1:27:57]** y

**[1:27:59]** quisiera la consulta es

**[1:28:01]** dentro del string

**[1:28:03]** contiene este

**[1:28:05]** substring básicamente es eso

**[1:28:07]** porque ahora no les he dicho como

**[1:28:09]** buscar un substring

**[1:28:11]** les he dicho así como cuando filtramos es

**[1:28:13]** este valor es igual

**[1:28:15]** igual a no sé ocupación

**[1:28:17]** estudiante

**[1:28:19]** pero no les he dicho como buscar

**[1:28:21]** un substring dentro de un string

**[1:28:23]** eso no se vio para los filtros

**[1:28:25]** entonces lo agrego aquí como de información extra

**[1:28:27]** por si la necesitaran alguna cosa

**[1:28:29]** que quieran hacer

**[1:28:31]** existe el contains

**[1:28:33]** y el contains es eso

**[1:28:35]** buscar algo

**[1:28:37]** una frasecita dentro de

**[1:28:39]** algún string

**[1:28:41]** entonces en este caso por ejemplo yo ahora que cambié las calles

**[1:28:43]** y ya tienen un formato

**[1:28:45]** casi perfecto

**[1:28:47]** que falta la cuestión de la florida que no me ha acordado

**[1:28:49]** dónde está

**[1:28:51]** veo que tienen algunas que son avenidas

**[1:28:53]** ok

**[1:28:56]** veo que tienen algunas que son avenidas

**[1:28:58]** y yo podría decir oh quiero saber

**[1:29:00]** cuántas son avenidas

**[1:29:02]** o cuáles de las filas contienen una avenida

**[1:29:04]** bueno entonces para ustedes

**[1:29:06]** deberían que hacer un filtro que sea

**[1:29:08]** ya

**[1:29:10]** en la columna calle

**[1:29:12]** que esto sea igual igual

**[1:29:14]** a avenida walker martínez

**[1:29:16]** o igual igual a avenida

**[1:29:18]** santa rosa o igual igual

**[1:29:20]** a avenida provi... y así

**[1:29:22]** con todos los valores

**[1:29:24]** pero se puede hacer más fácil con un contains

**[1:29:26]** yo simplemente puedo acceder

**[1:29:28]** a la columna calle

**[1:29:30]** hacer operación de string

**[1:29:32]** y puedo hacer un contains

**[1:29:34]** la

**[1:29:36]** como los caracteres

**[1:29:38]** a b y un buntito

**[1:29:40]** porque eso define como avenida

**[1:29:42]** y aquí le pongo que la expresión

**[1:29:44]** no es una expresión regular porque el punto

**[1:29:46]** también se usa en la expresión irregular

**[1:29:48]** entonces puede pasar algo raro ahí

**[1:29:50]** le pongo que no es una expresión regular

**[1:29:52]** sino que me busque el string

**[1:29:54]** tal cual yo lo estoy poniendo

**[1:29:56]** entonces con eso puedo obtener

**[1:29:58]** aquí me va a dar como true false

**[1:30:00]** ok

**[1:30:03]** me va a dar un true cuando

**[1:30:05]** esta fila si contiene

**[1:30:07]** una avenida y un false cuando no

**[1:30:09]** y yo simplemente

**[1:30:11]** pasándole esto a un log

**[1:30:13]** como argumento

**[1:30:15]** y pidiéndole que me dé la calle y me va a dar los valores

**[1:30:17]** que se dan cuenta

**[1:30:19]** y me va a pasar todas las avenidas

**[1:30:21]** y eso es para lo que sirve el contains

**[1:30:23]** no es muy útil a buenas a primeras

**[1:30:25]** pero para que sepan que existe

**[1:30:27]** porque en algún momento puede querer hacer una consulta

**[1:30:29]** donde puede ser

**[1:30:31]** que les sirvan como varios strings

**[1:30:33]** entonces un contents

**[1:30:35]** es más fácil que estar escribiendo no se

**[1:30:37]** 3 o 4

**[1:30:39]** como condiciones anidadas

**[1:30:41]** ok solamente para que sepan que existen

**[1:30:43]** ay ya me queda poquito

**[1:30:47]** queda solamente columnas

**[1:30:49]** con tipo de dato incorrecto

**[1:30:51]** ok entonces primero dudas

**[1:30:54]** hasta aquí porque igual operaciones de strings

**[1:30:56]** no se si habían visto

**[1:30:58]** se entendió todo esto

**[1:31:00]** yo te quería hacer una consulta

**[1:31:04]** pero si bien estos

**[1:31:06]** substring o el contents

**[1:31:08]** ve

**[1:31:10]** finalmente igual claro

**[1:31:12]** ve todo lo que contenga

**[1:31:14]** a b punto en este caso

**[1:31:16]** pero hay alguna

**[1:31:18]** no se si hay tipo de librería

**[1:31:20]** o algo que ve a carácteres

**[1:31:22]** por ejemplo

**[1:31:24]** no lo he buscado todavía

**[1:31:26]** pero se me ocurrió

**[1:31:28]** no se de repente tenemos tema en el trabajo

**[1:31:30]** que nos vienen

**[1:31:32]** en glosas de bancos cartolas

**[1:31:34]** ponte tu root

**[1:31:36]** en medio de texto

**[1:31:38]** y cosas por el estilo entonces de repente queremos

**[1:31:40]** separar el root del text

**[1:31:42]** y cosas así pero claro

**[1:31:44]** no colocar el root hoy es busca

**[1:31:46]** este root en particular

**[1:31:48]** sino que existe algo

**[1:31:50]** que vea el tipo

**[1:31:52]** de carácter o no se voy a el

**[1:31:54]** xx.xx

**[1:31:56]** guion algo no se como estructura

**[1:31:58]** del

**[1:32:00]** de la palabra algo así

**[1:32:02]** eso es una expresión regular

**[1:32:04]** eso es lo que tu necesitas una expresión regular

**[1:32:06]** entonces

**[1:32:09]** tu puedes como

**[1:32:11]** no se puedes extraer por ejemplo

**[1:32:13]** hay un

**[1:32:15]** std.stract

**[1:32:17]** hay un std.stract

**[1:32:19]** en donde tu le puedes poner

**[1:32:21]** la expresión regular que tu necesitas

**[1:32:23]** y que te extraiga eso

**[1:32:25]** o lo puedes poner entre paréntesis

**[1:32:27]** para que te lo vayas separando en una tabla

**[1:32:29]** si tu quieres separar

**[1:32:31]** hay una función std.stract

**[1:32:33]** y lo que tu tendrías que pasar ahí es una expresión regular

**[1:32:35]** porque yo mostré una expresión regular

**[1:32:37]** arriba

**[1:32:39]** no me acuerdo donde

**[1:32:42]** acá

**[1:32:44]** aquí yo mostré una expresión regular para cosas en blanco

**[1:32:46]** pero yo puedo ponerle

**[1:32:48]** por ejemplo

**[1:32:50]** no se me ocurre

**[1:32:52]** yo he la expresión regular de hacerle porque no las veo

**[1:32:54]** pero le puedo decir así como oye

**[1:32:56]** un d es un digito

**[1:32:58]** entonces yo le puedo decir mira necesito

**[1:33:00]** por ejemplo

**[1:33:02]** esto también es una forma de ponerle dígitos

**[1:33:04]** así como ya necesito

**[1:33:06]** que si o si contengas

**[1:33:08]** dígitos aquí le estoy diciendo que si o si

**[1:33:10]** el texto contenga dígitos

**[1:33:12]** y que además contenga

**[1:33:14]** no se creo que este era para

**[1:33:16]** palabras para palabras

**[1:33:18]** y no se que

**[1:33:20]** entonces tu le puedes hacer al extract pedirle

**[1:33:22]** que te con

**[1:33:24]** en paréntesis pedirle que te saque los dígitos

**[1:33:26]** si

**[1:33:28]** pero el

**[1:33:30]** es tr

**[1:33:32]** como para estudiar eso

**[1:33:34]** y tendrías que pasarle

**[1:33:36]** una expresión regular

**[1:33:38]** si

**[1:33:40]** gracias

**[1:33:42]** eso también te sirve para validar

**[1:33:44]** con una expresión regular tu podrías validar por ejemplo

**[1:33:46]** que el rute este bien escrito

**[1:33:48]** tu sabes que tiene que tener dígitos

**[1:33:50]** y que después tiene que tener un guión

**[1:33:52]** y después tiene que tener un dígito

**[1:33:54]** en acá

**[1:33:56]** entonces eso también se puede hacer con una expresión regular

**[1:33:59]** y todas esas cosas

**[1:34:01]** pero eso era un poquito más complicado

**[1:34:03]** porque hay que ver como ya

**[1:34:05]** que significa tal cosito y tal cosito

**[1:34:07]** pero se puede

**[1:34:09]** ya gracias

**[1:34:12]** de nada

**[1:34:14]** alguna otra duda en general sobre strings

**[1:34:17]** porque no se si lo

**[1:34:19]** no me acuerdo si lo vieron en algún laboratorio

**[1:34:21]** de python general como operaciones

**[1:34:23]** en string

**[1:34:25]** en detalla o no

**[1:34:29]** no

**[1:34:32]** habíamos visto algunas cosas pero si están de allá

**[1:34:34]** como tú lo fuiste mostrando

**[1:34:36]** no me acuerdo

**[1:34:38]** pero al menos saben

**[1:34:40]** que esto es comparar strings

**[1:34:42]** que un string se compara así

**[1:34:44]** eso si

**[1:34:46]** no me refiero a algunas funcionalidades que tú pusiste

**[1:34:48]** tan buena por ejemplo

**[1:34:50]** el sub

**[1:34:52]** para filtrar el ab punto

**[1:34:54]** ah si

**[1:34:57]** super super

**[1:34:59]** si no hay dudas y me pueden preguntar al final

**[1:35:01]** vamos a pasar a la última cosa

**[1:35:03]** y el ejercicio lo voy a dejar como

**[1:35:05]** de tarea

**[1:35:07]** para no dejarlo con más

**[1:35:09]** tiempo

**[1:35:11]** para no quitarles más tiempo

**[1:35:13]** lo último que me queda son columnas

**[1:35:15]** con tipo de dato incorrecto

**[1:35:17]** entonces puede pasar a veces

**[1:35:19]** que las columnas tengan el tipo de dato incorrecto

**[1:35:21]** por ejemplo

**[1:35:23]** si yo tuviera algo que es numérico

**[1:35:25]** y lo tiene como tipo objeto

**[1:35:27]** cuando yo quisiera

**[1:35:29]** hacer alguna consulta le quiera sacar el máximo

**[1:35:31]** le quiera sacar el mínimo

**[1:35:33]** le quiera sacar la media

**[1:35:35]** o quiera sumar

**[1:35:37]** si es que la cosa está como tipo objeto

**[1:35:39]** me va a dar error en algunos casos

**[1:35:41]** entonces esto me va a impedir poder analizarlas

**[1:35:43]** correctamente

**[1:35:45]** entonces como le cambio el tipo de dato

**[1:35:47]** a una columna

**[1:35:50]** eso lo vamos a ver ahora

**[1:35:52]** entonces aquí habíamos visto con el info

**[1:35:54]** de tipo object

**[1:35:56]** cuando en realidad pueden ser de tipo entero

**[1:35:58]** o de tipo flowato

**[1:36:00]** por ejemplo carga máxima podría ser un entero

**[1:36:02]** entonces como lo hago

**[1:36:05]** bueno

**[1:36:07]** primero podría hacerle a cada

**[1:36:09]** si quiero ver una columna específica

**[1:36:11]** yo puedo acceder al d-type

**[1:36:13]** eso es si lo vimos

**[1:36:16]** cuando vimos series y todo

**[1:36:18]** pudimos ver que una característica de la serie

**[1:36:20]** era el tipo de dato

**[1:36:22]** entonces yo para acceder al tipo de dato

**[1:36:24]** una columna punto d-type

**[1:36:26]** y ahí veo el tipo de dato que tiene

**[1:36:28]** o hago punto info y lo miro aquí

**[1:36:30]** también puede ser

**[1:36:32]** entonces para cambiar el tipo de dato

**[1:36:34]** lo que puedo ocupar es un as-type

**[1:36:36]** también hay una función

**[1:36:38]** que se llama tu numeric

**[1:36:40]** y ahí tiene un argumento

**[1:36:42]** de que hacer en caso de que

**[1:36:44]** me salga un error

**[1:36:46]** porque puede tirar un warning

**[1:36:48]** o puede ignorarlo y

**[1:36:50]** si es que encuentro un error

**[1:36:52]** entonces hay un argumento ahí

**[1:36:54]** que creo que se llama course

**[1:36:56]** creo que sí

**[1:36:58]** que lo puedo dejar ahí para que en el caso

**[1:37:00]** de que me salga otro tipo de

**[1:37:02]** dato que no se pueda transformar

**[1:37:04]** que lo deje como non, se puede hacer

**[1:37:06]** pero el as-type me da el error

**[1:37:08]** si es que no puede

**[1:37:10]** me sirve

**[1:37:13]** entonces lo que yo puedo hacer

**[1:37:15]** es simplemente tomar la columna

**[1:37:17]** hacerla igual a

**[1:37:19]** la columna punto as-type

**[1:37:21]** echarle el tipo de dato que yo quiero

**[1:37:23]** que se transforme, puede ser entero

**[1:37:25]** puede ser flotante, puede ser object

**[1:37:27]** etc etc

**[1:37:31]** entonces aquí me cambia el tipo de dato

**[1:37:33]** si yo hago info de nuevo acá arriba

**[1:37:35]** aquí está, esto es la carga máxima

**[1:37:37]** carga máxima sale como objeto

**[1:37:40]** y ahora carga máxima me sale como float

**[1:37:42]** float64

**[1:37:44]** que significa ahora que puedo sumar

**[1:37:46]** esa columna con alguna cosa

**[1:37:48]** que le puedo restar

**[1:37:50]** que la puedo sumar con carga mínima

**[1:37:52]** y el tipo de dato que se llama

**[1:37:56]** date time

**[1:37:58]** también en algunos casos

**[1:38:00]** no vamos a trabajar tanto este tipo de

**[1:38:02]** dato, existe el tipo de dato que se

**[1:38:04]** llama date time

**[1:38:06]** por si acaso, cuando yo trabajo con

**[1:38:08]** horas, días, meses, años etc

**[1:38:10]** y quiero hacer consultas

**[1:38:12]** puedo trabajar con datos

**[1:38:14]** de tipo date time y ahí sería

**[1:38:16]** pd.date time

**[1:38:18]** no time delta como lo tengo acá

**[1:38:20]** date time

**[1:38:22]** puede acceder por ejemplo

**[1:38:24]** al año, al mes

**[1:38:26]** al día, de una fecha

**[1:38:28]** de forma fácil y también

**[1:38:30]** me permite restar fechas

**[1:38:32]** de forma fácil

**[1:38:34]** la puedo

**[1:38:36]** hacer un, no se, hora

**[1:38:38]** inicio menos hora fin

**[1:38:40]** si es que fueran date times

**[1:38:42]** hacerle las diferencias y eso me va a dar un time delta

**[1:38:44]** sería una diferencia de tiempo

**[1:38:47]** también existe el tipo de dato time delta

**[1:38:49]** que yo lo puedo transformar

**[1:38:51]** por ejemplo el hora inicio y el hora fin

**[1:38:53]** y eso me va a dar simplemente

**[1:38:55]** un tipo de dato distinto

**[1:38:57]** en el que va a tener un formato

**[1:38:59]** con las horas y con los días

**[1:39:01]** y con los minutos y con los segundos

**[1:39:03]** a los cuales yo también puedo acceder

**[1:39:05]** y también puedo por ejemplo

**[1:39:07]** restar estos time delta o sumar estos time delta

**[1:39:09]** o sacarle el mínimo y el máximo

**[1:39:11]** y que estos mínimo y máximo tengan

**[1:39:13]** sentido porque si saco el mínimo

**[1:39:15]** y el máximo de string

**[1:39:17]** me van a dar resultados raros

**[1:39:19]** en cambio si yo lo paso a tipo de dato

**[1:39:21]** date time o time delta

**[1:39:23]** el mínimo y el máximo van a tener sentido

**[1:39:25]** entonces se dan cuenta cuando yo lo paso

**[1:39:29]** tu time delta

**[1:39:31]** va a tener otro formato

**[1:39:33]** entonces se va a tener los días

**[1:39:35]** después las horas, después los minutos

**[1:39:37]** después los segundos

**[1:39:41]** y puedo transformar los dos

**[1:39:43]** y puedo por ejemplo sacar el máximo

**[1:39:45]** y me va a dar el máximo

**[1:39:47]** que tiene sentido porque si yo le saco el máximo

**[1:39:49]** cuando está con string

**[1:39:51]** me puede dar resultados

**[1:39:53]** que no tienen sentido numérico para mí

**[1:39:56]** y puedo acceder a los componentes

**[1:39:58]** por ejemplo

**[1:40:00]** yo accedo a la hora de inicio, le pongo puntos de T

**[1:40:02]** accedo a los componentes y puedo por ejemplo

**[1:40:04]** acceder a las horas, aquí estoy accediendo al primero

**[1:40:06]** pero si le saco el cero me va a dar la tabla

**[1:40:08]** completa, entonces típicamente

**[1:40:10]** son ocho horas y aquí hay un cinco

**[1:40:12]** y puedo acceder a los minutos

**[1:40:14]** etcétera

**[1:40:16]** y en el describe me van a dar

**[1:40:18]** voy a poder analizar

**[1:40:20]** estos tipos de datos ahora, está horrible este

**[1:40:22]** min, muy largo

**[1:40:24]** pero ahora como les cambié el tipo de

**[1:40:26]** datos, ahora son tipos numéricos

**[1:40:28]** porque el time data y el daytime también son numéricos

**[1:40:30]** le puedo sacar estos estadísticos

**[1:40:32]** que antes no se podía

**[1:40:34]** ok?

**[1:40:39]** si, quizás

**[1:40:42]** como digiendo

**[1:40:44]** pero como dije

**[1:40:46]** no hay como una

**[1:40:48]** receta paso a paso que van a tener que ocupar

**[1:40:50]** si o si siempre, sino que nosotros

**[1:40:52]** les damos la herramienta

**[1:40:54]** para que ustedes puedan adaptarla

**[1:40:56]** según las necesidades de su conjunto

**[1:40:58]** de datos o de lo que quieran analizar

**[1:41:00]** como dije, entonces aquí

**[1:41:02]** este ejercicio yo creo que

**[1:41:04]** como es igual

**[1:41:06]** lo podemos ver

**[1:41:08]** a la otra clase al principio

**[1:41:10]** ver la respuesta, ya? y es que yo les paso

**[1:41:12]** una tabla, aquí

**[1:41:14]** creo que es una tabla que saqué Wikipedia hace mucho

**[1:41:16]** con capítulos de voz esponja

**[1:41:18]** no, temporada de voz esponja

**[1:41:20]** y lo que le pido es que

**[1:41:22]** esta tabla de juguete

**[1:41:24]** contenga solo los datos de las temporadas de voz esponja

**[1:41:26]** porque tiene unas películas, y no las quiero

**[1:41:28]** dice eliminar las películas

**[1:41:30]** eliminar duplicados y reemplazar valores

**[1:41:32]** NAN por TVA

**[1:41:34]** que en inglés es como to be added

**[1:41:36]** reemplazarlos NAN por este string

**[1:41:38]** dejar todas las fechas solo

**[1:41:41]** con el año

**[1:41:43]** pueden verlo como lo hacen ustedes

**[1:41:45]** con manejo de string, manejo de daytime

**[1:41:47]** da lo mismo con tal de que la respuesta final

**[1:41:49]** es buena, eliminar las temporadas

**[1:41:51]** que tengan más de 30 capítulos

**[1:41:53]** y ordenar la tabla por número de temporada

**[1:41:55]** entonces la idea es que

**[1:41:57]** hagan todo esto sin tocarme esta celda

**[1:41:59]** esta celda que lo define mal

**[1:42:01]** esta no la pueden tocar

**[1:42:03]** sino que solamente con operaciones

**[1:42:05]** que vimos aquí de pandas y todo eso ya

**[1:42:07]** eso les quedaría como

**[1:42:09]** de tarea para practicar como limpiar una tabla

**[1:42:11]** que igual tiene sus cosas

**[1:42:13]** medio complicadas, si?

**[1:42:17]** ok, si

**[1:42:19]** si no hay más dudas

**[1:42:21]** como dije ojalá hagan este ejercicio

**[1:42:23]** en su tiempo libre para verlo

**[1:42:25]** la solución

**[1:42:27]** en la próxima clase

**[1:42:29]** me voy a quedar pendiente

**[1:42:32]** ver qué pasó con la clase

**[1:42:34]** les voy a tener que informar después

**[1:42:36]** con algún anuncio en el

**[1:42:38]** en el campus

**[1:42:40]** ahí voy a tener que preguntar

**[1:42:42]** qué onda porque por mientras no tengo información

**[1:42:44]** no sé si hay dudas

**[1:42:46]** sueltas en este momento

**[1:42:48]** pendientes de subir

**[1:42:50]** no sé, creo que ya se subió el sílabus y todo eso

**[1:42:52]** que me lo pidieron la vez pasada

**[1:42:54]** si, esto de lluviter

**[1:42:56]** es lo que cargaste al inicio de la clase

**[1:42:58]** si, eso está

**[1:43:00]** en el campus

**[1:43:02]** está el vacío eso si, no está en la respuesta

**[1:43:04]** la próxima clase

**[1:43:06]** yo creo que el mismo día de la próxima clase

**[1:43:08]** les voy a cargar la respuesta y la podemos comentar

**[1:43:10]** al inicio

**[1:43:12]** ya

**[1:43:18]** si no hay más dudas

**[1:43:20]** lo dejamos hasta aquí

**[1:43:22]** nos veríamos la otra semana

**[1:43:24]** no más

**[1:43:28]** muchas gracias que tengamos

**[1:43:30]** buena noche

**[1:43:32]** nos vemos

**[1:43:34]** nos vemos, chao

**[1:43:36]** que nada, chao

**[1:43:38]** como dejo de compartir

**[1:43:40]** me voy a quedar

**[1:43:44]** tres minutitos aquí por si alguien se quiere quedar

**[1:43:46]** para preguntarme algo por si acaso

**[1:44:01]** alguna duda, me estoy quedando aquí por dudas

**[1:44:03]** pero ustedes se pueden retirar ya

**[1:44:05]** no hay problema

**[1:44:07]** ya termino la clase, todo legal aquí

**[1:44:14]** alguna duda, alguna duda

**[1:44:19]** ya voy a dar las dos manitos

**[1:44:21]** voy a dar las dos manitos para ver si alguien

**[1:44:23]** no tiene alguna duda, si no ya termino

**[1:44:25]** la grabación

**[1:44:29]** ah, ya, ok, chao

**[1:44:39]** entonces parece que

**[1:44:41]** no hay dudas, entonces voy a dejar la clase

**[1:44:43]** hasta aquí
