# 04Clase Fundamentos en Ciencia de Datos 17 Julio.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:32:18
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:00:08]** Hola, ¿eh? ¿Me escuchan? Hola, hola, buenas. ¿Me escuchan o no? Sí. ¿Me escuchan? Sí. Ya, súper.

**[0:00:27]** Voy a buscar el audífono y vení a escucharlo. ¿Puedes alguien hablar, por favor? Hola.

**[0:01:46]** ¿Cómo están? Todo bien. Bien, gracias. Aún.

**[0:01:54]** Espero que no haya sido muy terrible. No sé si fue o no terrible, pero espero que no.

**[0:02:02]** Y espero que hayamos, que no tengan problemas para conectarse hoy día, que fue una de las preguntas que me hicieron.

**[0:02:08]** Bueno, los que están acá, sumo que no tuvieron problemas para conectarse. De todas formas, la clase va a quedar grabada, así que...

**[0:02:25]** Profe. Profe.

**[0:02:29]** Si no es mucha morecha, o se podría hablar un poquito más fuerte, porque se escucha abajo.

**[0:02:36]** ¿Escucha todo bajo? O sea, yo lo escucho bien.

**[0:02:44]** ¿Me pueden decir si todos escuchan bajo? O sea, alguien más escucha abajo.

**[0:02:49]** Yo escucho bien, pero eso es muy importante.

**[0:02:55]** No, puede ser el internet. Igual está pasando muy bien.

**[0:03:02]** Bueno, vamos a comenzar con la clase de hoy. Ah, antes de comenzar con la clase, dejé un anuncio en Canvas para que llenen un...

**[0:03:17]** Un buen to meet para tener un horario de consultas.

**[0:03:22]** Entonces, le explico un poco cómo funciona esto.

**[0:03:25]** Nos vamos a poner de acuerdo en un horario donde todos podamos, o la gran mayoría en general, no todos podamos.

**[0:03:31]** Y ustedes me tienen que mandar un correo el día anterior, diciendo que van a asistir al horario de consultas,

**[0:03:40]** y nos juntamos online y Armando el link, y nos juntamos online.

**[0:03:43]** Por si tienen preguntas acerca de cualquier cosa, en particular de los proyectos.

**[0:03:48]** Generalmente, el horario de consultas podemos hablar en detalle de sus proyectos, de sus avances,

**[0:03:54]** si van bien o si necesitan ayuda, como lo podemos testrabar.

**[0:03:58]** Entonces, les pido, no sé si lo quieren hacer ahora, que llenan algo en to meet,

**[0:04:05]** o lo hacen después, pero que no pase de, digamos, el lunes,

**[0:04:09]** porque si no, no podemos quedar sin horario de consultas la próxima semana.

**[0:04:14]** Pero solo una consulta, es que, bueno, yo estoy en el diplomado.

**[0:04:18]** No sé si los grupos del proyecto ya se conformaron o no.

**[0:04:22]** O sea, si se conformaron no tengo a nadie con quien hacer el proyecto.

**[0:04:26]** Aún no, porque aún no subió el listado de proyectos.

**[0:04:30]** Después de la clase de hoy, podemos empezar a hablar de los proyectos,

**[0:04:33]** porque además es lo último que necesitan para empezar a trabajar en sus proyectos.

**[0:04:37]** Ah, sí, muchas gracias.

**[0:04:49]** Ok, vamos a comenzar con la clase.

**[0:04:52]** Entonces, voy a compartir la pantalla.

**[0:04:57]** ¿Están viendo la clase?

**[0:05:04]** Sí, se ve.

**[0:05:08]** Un momento que yo los perdí ahora porque cambió el zoom, pero no hablaste.

**[0:05:13]** Ya, súper.

**[0:05:20]** Ok, hoy día vamos a ver exploración de datos.

**[0:05:24]** Vamos a partir hablando acerca de cómo podemos describir los datos

**[0:05:28]** previamente a hacer el modelamiento exacto.

**[0:05:31]** Vamos a hablar acerca de distintas herramientas de visualización.

**[0:05:35]** Y vamos a ver un par de ejemplos de cómo podemos generar hipótesis de trabajo

**[0:05:41]** a partir de la descripción de los datos y de la visualización de los datos.

**[0:05:46]** Es muy importante al momento de decidir qué tipo de modelos

**[0:05:51]** voy a usar más adelante, qué tipo de modelos predictivos

**[0:05:56]** para poder trabajar con los datos y sacar valor desde estos datos.

**[0:06:01]** Entonces, esto ya lo vimos, ¿sí?

**[0:06:03]** Una consulta, disculpe que me interrumpa.

**[0:06:06]** ¿Usted tiene información acerca de si vamos a recuperar la clase

**[0:06:09]** que se perdió el viernes pasado?

**[0:06:12]** Ya la recuperamos. La recuperamos en el miércoles.

**[0:06:18]** Ah, se recuperó.

**[0:06:20]** Bueno, me llegó una. Yo soy del diplomado.

**[0:06:24]** ¿Alunos del diplomado no tienen acceso al Canvas?

**[0:06:32]** No, yo tengo acceso a Canvas.

**[0:06:35]** Sí, yo también tengo.

**[0:06:37]** Estas lo publican en Canvas.

**[0:06:40]** Sí, igual tengo acceso a Canvas, pero la verdad es que no lo reíso de manera...

**[0:06:44]** Sí, igual reíen esa encuesta para ver cuándo había disponibilidad

**[0:06:49]** y yo no podía almiencorar personalmente, pero eso.

**[0:06:53]** No sé qué va a pasar ahí con la asistencia,

**[0:06:55]** si cuesta como obligatorio igual.

**[0:06:57]** No, acá no hay asistencia obligatoria.

**[0:06:59]** Ah, ya, ¿qué?

**[0:07:01]** Así que no hay problema con eso.

**[0:07:02]** ¿Está la grabación, entonces, que es lo más importante al final?

**[0:07:05]** Es una buena pregunta. No lo he revisado.

**[0:07:08]** Yo grabé. No sé si lo subió la persona encargada.

**[0:07:12]** No sé si lo revisaba alguien.

**[0:07:15]** Yo lo puedo revisar y lo llevo.

**[0:07:18]** Voy a revisar y volver. Gracias.

**[0:07:20]** Gracias.

**[0:07:21]** Profesor, ¿y si hay que no está la grabación?

**[0:07:23]** ¿La PPT que presentó estaba ahí en Canvas?

**[0:07:26]** La PPT no está, esa la tengo que subir.

**[0:07:31]** Gracias.

**[0:07:32]** La voy a subir al fin de semana.

**[0:07:36]** Creo que no está, no lo recuerdo bien.

**[0:07:38]** Creo que no la subí, no lo recuerdo bien.

**[0:07:44]** ¿Alguna otra pregunta administrativa?

**[0:07:47]** Ya. Ok.

**[0:07:53]** Entonces, bueno, la clase pasada y la clase antepasada,

**[0:07:59]** hablamos del ciclo de la ciencia de datos,

**[0:08:03]** de un proyecto de ciencia de datos

**[0:08:05]** y hablamos de que partimos con requerimiento de preguntas,

**[0:08:08]** después tenemos que recolectar los datos,

**[0:08:10]** después limpiámonos datos.

**[0:08:11]** La clase pasada hablamos de recolección y limpieza

**[0:08:14]** y hoy lo que vamos a hablar es de exploración de los datos.

**[0:08:18]** Ok.

**[0:08:20]** Entonces, vamos a partir describiendo datos.

**[0:08:24]** Tenemos que de alguna forma entender qué son estos datos

**[0:08:27]** sin tener que entrar a leer cada uno de los datos

**[0:08:29]** porque pueden ser millones de datos

**[0:08:31]** y pueden ser miles de atributos

**[0:08:33]** y no vamos a poder verlos uno a uno.

**[0:08:37]** Entonces, alguna forma tenemos que sacar información

**[0:08:40]** y generar hipótesis de trabajo desde los datos.

**[0:08:43]** Entonces, básicamente lo que nos gustaría hacer

**[0:08:47]** es tener, calcular de alguna forma algo,

**[0:08:50]** alguna cantidad que pueda resumir

**[0:08:53]** y darnos alguna intuición de qué es lo que son estos datos.

**[0:08:56]** Tipo de cosas que nos gustaría saber

**[0:08:59]** son los valores típicos de nuestras variables o atributos.

**[0:09:02]** O sea, si yo estoy hablando, por ejemplo, de alturas de personas

**[0:09:06]** y dice que la media o la mediana es de 1,8 metros,

**[0:09:16]** ¿qué es lo que les dice eso a usted?

**[0:09:19]** Si yo digo que estoy midiendo personas

**[0:09:26]** y en el primer dataset,

**[0:09:29]** la medición de las personas tiene un promedio

**[0:09:32]** de 1,8 metros de altura.

**[0:09:34]** ¿Qué les dice eso a usted?

**[0:09:36]** O digamos lo siguiente.

**[0:09:38]** Quizás que son adultos.

**[0:09:40]** Eso, que son adultos, ¿certo?

**[0:09:42]** Si después yo digo voy a medir personas

**[0:09:44]** y la mediana o el promedio de estas personas,

**[0:09:48]** de la altura de estas personas es de, no sé,

**[0:09:51]** 0,9 metros.

**[0:09:53]** ¿Qué es lo que les dice eso a usted?

**[0:09:56]** Que podrían ser niños o quizás personas con elanismo.

**[0:10:00]** No sé.

**[0:10:01]** Eso puede ser.

**[0:10:02]** Entonces, podrían ser niños.

**[0:10:04]** Fíjense que de inmediato

**[0:10:06]** los números en nuestra cabeza

**[0:10:08]** tenemos una intuición de qué es lo que son los datos.

**[0:10:10]** Y podemos generar un hipótesis.

**[0:10:12]** Y acabamos de generar dos hipótesis

**[0:10:14]** que Hayden generó dos hipótesis.

**[0:10:16]** Una es que el primer dataset eran adultos.

**[0:10:19]** La segunda es que el segundo dataset eran niños.

**[0:10:22]** Esa es una hipótesis.

**[0:10:24]** Yo digo el primer dataset

**[0:10:27]** corresponde a un dataset de alturas de adultos.

**[0:10:32]** Eso es una hipótesis.

**[0:10:34]** Yo no lo sé porque no sé qué midió esto

**[0:10:36]** ni si son adultos o no.

**[0:10:39]** Pero es una hipótesis.

**[0:10:41]** Además nos dicen qué tan representativos

**[0:10:45]** son estos valores típicos.

**[0:10:47]** Entonces, es distinto que si yo les dijera,

**[0:10:49]** mira, estos son mediciones de personas

**[0:10:53]** y en promedio son 1,8 metros de altura

**[0:10:58]** pero van entre 0,3 metros

**[0:11:02]** y 2,5 metros.

**[0:11:04]** Es distinto que le diga eso

**[0:11:06]** a que yo les diga,

**[0:11:08]** estos son promedio de la altura de personas

**[0:11:11]** pero van la altura entre 1,60 metros

**[0:11:15]** y 1,90 metros.

**[0:11:18]** Entonces, eso lo que me está diciendo

**[0:11:21]** es este promedio que yo calculé

**[0:11:24]** qué tan representativo es de los datos.

**[0:11:28]** Vamos a hablar un poquito más de esto más adelante.

**[0:11:32]** Vamos a hacer un ejemplo.

**[0:11:34]** Entonces, digamos que estamos trabajando

**[0:11:37]** y tenemos una máquina

**[0:11:39]** donde estamos midiendo varias variables,

**[0:11:41]** están muy sensorizadas

**[0:11:43]** y en particular tenemos, no sé,

**[0:11:45]** por ejemplo, voltaje, presión, rotación

**[0:11:47]** y vibración, tenésensores

**[0:11:49]** que pueden medir esa parte

**[0:11:51]** en las distintas componentes de la máquina.

**[0:11:53]** Y tenemos la fecha

**[0:11:56]** de la mantención

**[0:11:58]** y la fecha de las fallas.

**[0:12:00]** Entonces, imagínense que

**[0:12:02]** en este gráfico estoy mostrando

**[0:12:04]** en el eje X la fecha

**[0:12:06]** y en el eje Y la vibración de uno de los sensores.

**[0:12:09]** Y fíjense que va vibrando

**[0:12:11]** y de repente sube, de repente baja

**[0:12:13]** y sube y baja y sube y baja.

**[0:12:16]** Y acá hubo una falla

**[0:12:18]** y acá hubo otra falla.

**[0:12:20]** La máquina falló.

**[0:12:22]** A mí lo que me gustaría sería de alguna forma

**[0:12:24]** prevenir la falla

**[0:12:26]** antes de que falle, porque imagínense que

**[0:12:28]** si la máquina falla se puede romper

**[0:12:30]** alguna componente y entonces

**[0:12:32]** quiere decir que yo tengo que invertir

**[0:12:34]** y prepararla y demora más tiempo

**[0:12:36]** mientras que si yo sé que va a fallar

**[0:12:38]** puedo tratar de tomar alguna

**[0:12:40]** medida antes de que eso ocurra.

**[0:12:42]** Entonces

**[0:12:45]** mi pregunta para ustedes es

**[0:12:47]** ¿qué les dice este gráfico?

**[0:12:54]** Voy a llamar a alguien

**[0:12:56]** a Jason.

**[0:13:00]** La gráfica mostraría

**[0:13:02]** en cuando tuvo mayor

**[0:13:04]** mayor vibración

**[0:13:06]** quizá

**[0:13:08]** cuando falló

**[0:13:10]** como cerca de fallar

**[0:13:12]** por alta y alta.

**[0:13:14]** Ahí va, ahí va.

**[0:13:16]** Tratemos de generar un hipótesis

**[0:13:18]** desde este gráfico.

**[0:13:20]** Entonces Jason, dime

**[0:13:22]** qué es lo que tú crees que puede estar pasando.

**[0:13:24]** Yo la veo estable

**[0:13:27]** la tendencia

**[0:13:29]** básicamente está bien estable

**[0:13:31]** pero hay momentos en los que tiene una alta vibración

**[0:13:33]** por ejemplo cuando destaca

**[0:13:35]** la línea roja de la derecha

**[0:13:37]** no es probable que en ese momento

**[0:13:39]** haya una falla o algo que haya generado

**[0:13:41]** alta vibración en el motor.

**[0:13:44]** Entonces tú lo que estás diciendo es

**[0:13:46]** cada vez que hay una falla

**[0:13:48]** hay una

**[0:13:50]** alza en la vibración, eso.

**[0:13:52]** Sí

**[0:13:54]** una perturbación

**[0:13:56]** o no tan solo falla

**[0:13:58]** puede ser algo no malo

**[0:14:00]** pero en sí la tendencia

**[0:14:02]** muestra aquí bien estable.

**[0:14:04]** Ya, pero estamos tratando

**[0:14:07]** de prevenir la falla, ese es nuestro objetivo.

**[0:14:09]** Entonces voy a pedirle a otra persona

**[0:14:11]** digamos Daniel

**[0:14:14]** Daniel, ¿tiene algo más que puedes decir

**[0:14:16]** de esto en términos de que queremos predecir la falla?

**[0:14:18]** Daniel Cisternas

**[0:14:26]** vamos con otra persona entonces

**[0:14:31]** ¿Victor?

**[0:14:37]** Es que estaba mirando y como que no...

**[0:14:39]** O sea, la línea roja es buena de falla

**[0:14:41]** pero por ejemplo

**[0:14:43]** ahí tiene una cierta cantidad de vibración

**[0:14:45]** y después en la fecha

**[0:14:47]** del

**[0:14:49]** si no me equivoco

**[0:14:51]** de julio y el 15 de julio

**[0:14:53]** tiene como una vibración es como parecía

**[0:14:55]** y ahí no falla

**[0:14:57]** pero no...

**[0:14:59]** Entonces claro después falla al final

**[0:15:01]** porque la vibración es super alta pero

**[0:15:03]** la verdad que no...

**[0:15:05]** es el primer caso, o sea el primer al que

**[0:15:07]** funcione a hacer esto entonces

**[0:15:09]** como que no se me ocurre más que decir

**[0:15:11]** pero yo creo que

**[0:15:13]** los dos le dieron al clavo

**[0:15:15]** entonces lo primero que la primera hipótesis

**[0:15:17]** que yo puedo generar

**[0:15:19]** es decir, cada vez que falla

**[0:15:22]** la máquina

**[0:15:24]** hay una alza en las vibraciones, ¿certo?

**[0:15:26]** pero además

**[0:15:28]** puedo hacer la segunda hipótesis que es que

**[0:15:30]** no siempre

**[0:15:32]** que...

**[0:15:36]** hay como una raya...

**[0:15:38]** Perdón, perdón, pero

**[0:15:40]** está yo anotando

**[0:15:42]** para ver si hay un patrón pero

**[0:15:44]** pensaba que era solo para mí

**[0:15:46]** Ah, ya lo vemos todo

**[0:15:48]** mire

**[0:15:50]** no sabía que podían hacer eso

**[0:15:52]** podían hacer cosas terribles

**[0:15:54]** con esa nueva herramienta

**[0:15:56]** bueno...

**[0:15:58]** bueno, lo que les decía

**[0:16:00]** es que la segunda hipótesis

**[0:16:02]** es que no siempre que hay una alza

**[0:16:04]** en vibraciones la máquina falla

**[0:16:06]** entonces son cosas distintas

**[0:16:09]** siempre que hay una falla

**[0:16:11]** hay una alza en vibraciones

**[0:16:13]** pero no siempre que hay una alza en vibraciones

**[0:16:15]** es la máquina falla, ¿ok?

**[0:16:17]** y entonces un hipótesis

**[0:16:19]** uno podría tener inicialmente

**[0:16:21]** como hipótesis ya para pensando

**[0:16:23]** en algún modelo predictivo que pueda predecir

**[0:16:25]** cuando venga las fallas

**[0:16:27]** uno podría decir

**[0:16:30]** la vibración

**[0:16:32]** me ayuda a detectar las fallas

**[0:16:34]** pero no es suficiente

**[0:16:36]** necesito algo más

**[0:16:39]** ¿me siguen?

**[0:16:43]** entonces fíjense que

**[0:16:45]** esto

**[0:16:47]** es una hipótesis que yo puedo

**[0:16:49]** utilizar después para un modelo predictivo

**[0:16:51]** y voy a hacer un modelo predictivo

**[0:16:53]** que detecte las fallas

**[0:16:55]** antes de que ocurran

**[0:16:57]** y una de las variables que va a necesitar

**[0:16:59]** uno de los atributos que va a necesitar es la vibración

**[0:17:02]** seguramente va a necesitar más

**[0:17:04]** y tengo que buscar cuáles van a ser los siguientes

**[0:17:06]** pero este uno es lo importante

**[0:17:09]** ¿preguntas?

**[0:17:16]** me llama la atención la falla

**[0:17:18]** es la fecha

**[0:17:20]** porque el tema de la mantención

**[0:17:22]** son cada 15 días

**[0:17:24]** pero tiene que haber algo

**[0:17:26]** que haga que exista esa vibración alta

**[0:17:28]** y por ejemplo la fecha de la mantención

**[0:17:30]** ya no sería como algo a considerar

**[0:17:32]** o yo estoy con

**[0:17:34]** o estoy mal

**[0:17:36]** me llaman la atención eso

**[0:17:38]** yo no dije que las mantenciones

**[0:17:40]** son cada 15 días

**[0:17:42]** de hecho no están marcas las mantenciones

**[0:17:44]** pero efectivamente

**[0:17:46]** la fecha de la mantención

**[0:17:48]** debería ser relevante

**[0:17:50]** creo que es una buena hipótesis

**[0:17:52]** la fecha de la mantención debería ser relevante

**[0:17:54]** para determinar

**[0:17:56]** cuando una máquina va a fallar o no

**[0:17:58]** yo pensé que la fecha

**[0:18:00]** ahí era la mantención

**[0:18:02]** no no no

**[0:18:04]** esa es la fecha es solo para marcar

**[0:18:06]** lo que da en el efecto

**[0:18:08]** yo creo que por ahí podríamos tratar

**[0:18:10]** de también comprender el tema de la falla

**[0:18:12]** si es un periodo

**[0:18:14]** antes de hacer la mantención

**[0:18:16]** o es

**[0:18:18]** algo propio de la máquina

**[0:18:20]** porque pasa por algún lugar

**[0:18:22]** específico

**[0:18:24]** pensando que no sé si en mi negra

**[0:18:26]** porque tampoco tenemos ese dato

**[0:18:28]** como para poder ser

**[0:18:30]** es verdad no tenemos

**[0:18:32]** el dato exacto

**[0:18:34]** esto es un ejemplo como para mostrar

**[0:18:36]** como uno puede empezar a generar hipótesis

**[0:18:41]** una de las primeras cosas que uno hace

**[0:18:43]** o que gráfica son las distribuciones

**[0:18:45]** la distribución

**[0:18:47]** de alguna variable es una función

**[0:18:49]** que asigna a cada suceso posible

**[0:18:51]** la probabilidad de que dicho suceso

**[0:18:53]** ocurra

**[0:18:55]** entonces déjame tratar de explicarlo

**[0:18:57]** un poco más

**[0:18:59]** en chileno

**[0:19:03]** digamos que yo tomo todos los datos

**[0:19:05]** de vibración que están en el gráfico anterior

**[0:19:07]** los pongo acá en lgx

**[0:19:09]** los valores fíjense quedan entre 30 y 60

**[0:19:11]** si hoy acá

**[0:19:13]** van como más o menos entre 30 y 60

**[0:19:15]** los datos

**[0:19:17]** y lo que hago es que

**[0:19:20]** en caso que no lo conozcan lo que es un histograma

**[0:19:22]** lo que hago es que hago como cajitas

**[0:19:24]** acá en lgx

**[0:19:26]** como cortecitos

**[0:19:28]** y voy cada vez que aparece

**[0:19:30]** un valor lo voy metiendo dentro de la cajita

**[0:19:32]** correspondiente a ese valor

**[0:19:34]** entonces por ejemplo acá

**[0:19:36]** si me sale un 29

**[0:19:38]** el 29 seguramente entraría en esta cajita

**[0:19:40]** si me sale un 31

**[0:19:42]** el 31 entraría en esta cajita

**[0:19:44]** entonces voy

**[0:19:46]** contando la frecuencia

**[0:19:48]** ocurrencia de cada uno de los valores

**[0:19:50]** dentro de estos rangos

**[0:19:52]** ¿Ya?

**[0:19:55]** la forma como les decía

**[0:19:57]** más fácil y simple

**[0:19:59]** y que todo el mundo seguramente alguna vez ha usado

**[0:20:01]** es lo que se llama el histograma

**[0:20:03]** que le estoy mostrando ahora

**[0:20:05]** pero en la práctica lo que está mostrando

**[0:20:07]** esto es

**[0:20:10]** lo que está mostrando es

**[0:20:12]** cuál es la frecuencia

**[0:20:14]** de ocurrencia de ciertos efectos

**[0:20:16]** o de ciertas valores de variables

**[0:20:18]** una cosa que yo puedo ver acá

**[0:20:20]** es que por ejemplo acá hay una cola hacia la derecha

**[0:20:22]** que hay poquitos valores que son altos

**[0:20:24]** ¿Ya?

**[0:20:26]** eso es lo que me quiere decir a mí

**[0:20:28]** es que son valores anómalos

**[0:20:30]** son valores que no son muy probables de que ocurran

**[0:20:32]** pero a veces ocurren

**[0:20:34]** y si voy atrás al gráfico que les había mostrado antes

**[0:20:36]** son justamente estos valores de alta duración

**[0:20:38]** que aparecen acá

**[0:20:41]** entonces son poco probables de que ocurran

**[0:20:43]** pero a veces ocurren

**[0:20:45]** y esto es lo que uno llama como

**[0:20:47]** valores anómalos o valores

**[0:20:49]** fuera de la distribución

**[0:20:54]** un número

**[0:20:56]** que uno puede calcular y que es fácil

**[0:20:58]** que te sirve para entender

**[0:21:00]** la distribución de los datos

**[0:21:02]** es el promedio

**[0:21:04]** que también se le llama la media

**[0:21:06]** entonces el promedio es como lo que todos

**[0:21:08]** conocemos y que seguramente no enseñaron

**[0:21:10]** en el colegio creo

**[0:21:12]** básicamente tomo todos los valores

**[0:21:14]** y los divido por el número de valores

**[0:21:16]** que yo promedí

**[0:21:19]** entonces esta forma

**[0:21:21]** ¿Qué es lo que estoy viendo?

**[0:21:23]** la centralidad de la distribución

**[0:21:25]** ¿Dónde está el medio de la distribución?

**[0:21:27]** entonces si esta es la distribución

**[0:21:29]** veo así como justo

**[0:21:31]** ¿Dónde está acá el medio?

**[0:21:33]** y esa forma es como que me dicen el centro

**[0:21:35]** y es como ¿cuál es el valor más típico

**[0:21:37]** o cerca de dónde están los valores más típicos?

**[0:21:39]** que es como lo que habíamos hablado al principio

**[0:21:41]** de la altura de un 80

**[0:21:43]** básicamente nos dice

**[0:21:45]** la mayor parte de la gente

**[0:21:47]** está dentro

**[0:21:49]** cercano al metro 80

**[0:21:51]** en este caso lo que estoy diciendo

**[0:21:53]** es la mayor

**[0:21:55]** parte de la vibración

**[0:21:57]** está cercano a este valor acá que no se cuenta

**[0:21:59]** pero es el 41

**[0:22:01]** o algo así

**[0:22:03]** entonces

**[0:22:05]** la media nos dice cuál es el valor

**[0:22:07]** más típico o el valor central de la distribución

**[0:22:09]** al mismo tiempo existe

**[0:22:13]** la mediana

**[0:22:15]** la mediana

**[0:22:17]** se calcula en la siguiente forma

**[0:22:19]** ordeno todos los datos de menor a mayor

**[0:22:21]** y busco el número al medio

**[0:22:23]** si es que el número de datos

**[0:22:25]** es impar

**[0:22:27]** entonces es exactamente el número al medio

**[0:22:29]** porque hay un solo número al medio

**[0:22:31]** si es que el número de datos es par

**[0:22:33]** hay dos valores que están al medio

**[0:22:35]** y entonces lo que hago es calcular

**[0:22:37]** el promedio entre esos dos valores

**[0:22:39]** y entonces

**[0:22:42]** hay una pequeña diferencia entre el promedio

**[0:22:44]** que es la media

**[0:22:46]** y la mediana

**[0:22:48]** la mediana te da exactamente el valor del medio

**[0:22:50]** el promedio te da

**[0:22:52]** el promedio

**[0:22:54]** la media te da como el promedio

**[0:22:56]** cada punto vale lo mismo

**[0:22:58]** para aportar al promedio

**[0:23:02]** ahora

**[0:23:05]** si nosotros estamos hablando de centralidad

**[0:23:07]** la media es más sensible

**[0:23:09]** a valores anómalos

**[0:23:12]** aquí me refiero con eso

**[0:23:14]** imagínense que acá yo tengo

**[0:23:16]** estos cinco valores

**[0:23:18]** tengo el valor 1, el 2, el 3, el 4

**[0:23:20]** y el 5

**[0:23:22]** distribuido uniformemente

**[0:23:24]** la media y la mediana me dan exactamente el mismo valor

**[0:23:26]** 3

**[0:23:29]** pero si voy al valor

**[0:23:31]** a los datos que están abajo

**[0:23:33]** y tengo el valor 1, el 2, el 3, el 4

**[0:23:35]** y el 9

**[0:23:37]** que está por acá

**[0:23:39]** lo que ocurre es que

**[0:23:41]** la media está en 3

**[0:23:43]** porque el punto en medio

**[0:23:45]** pero el promedio

**[0:23:47]** perdón

**[0:23:49]** la mediana está en 3

**[0:23:51]** o en 4

**[0:23:53]** entonces qué es lo que hace que se mueva

**[0:23:55]** hacia los valores anómalos

**[0:23:57]** el promedio

**[0:23:59]** o la media se mueve hacia los valores anómalos

**[0:24:01]** si yo tengo un valor muy muy muy grande

**[0:24:03]** la mediana no se va a mover mucho

**[0:24:05]** pero el promedio sí se va a mover

**[0:24:07]** preguntas hasta acá

**[0:24:16]** ok voy a la siguiente

**[0:24:20]** la media es más sensible

**[0:24:22]** a las asimetrías de la distribución

**[0:24:24]** entonces en este caso

**[0:24:26]** que la distribución es bastante simétrica

**[0:24:28]** qué quiere decir que sea asimétrica

**[0:24:30]** que básicamente se ve

**[0:24:32]** en la misma forma

**[0:24:34]** si yo la he vivido en la mitad

**[0:24:36]** se ve más o menos de la misma forma

**[0:24:39]** entonces en este caso

**[0:24:41]** que la distribución es simétrica

**[0:24:43]** la media y la mediana te dan más o menos parecido

**[0:24:45]** pero cuando la distribución es asimétrica

**[0:24:47]** como esta acá

**[0:24:49]** y esta acá es un ejemplo donde hay una cola grande

**[0:24:51]** entonces lo que ocurre

**[0:24:53]** es que la media, el promedio

**[0:24:55]** se empieza a mover hacia los valores anómalos

**[0:24:57]** lo que les desea antes

**[0:24:59]** y entonces empieza a mover

**[0:25:01]** hacia donde hay valores

**[0:25:03]** que no representan necesariamente

**[0:25:05]** el centro de la distribución

**[0:25:07]** la mediana es menos sensible

**[0:25:09]** a esta asimetría en la distribución

**[0:25:11]** ahora

**[0:25:17]** para variables categóricas

**[0:25:19]** estos son valores, variables numéricas

**[0:25:21]** cuando hablamos de la distribución como

**[0:25:25]** como un histograma o algo de ese estilo

**[0:25:27]** son variables numéricas

**[0:25:29]** pero para variables categóricas

**[0:25:31]** no tenemos

**[0:25:33]** una noción de orden, entonces no las puedo ordenar

**[0:25:35]** y entonces no puedo calcular el histograma

**[0:25:39]** entonces lo que se hace

**[0:25:41]** es que se calcula la moda

**[0:25:43]** que es el valor que aparece más seguido

**[0:25:46]** entonces por ejemplo en este gráfico

**[0:25:48]** que está acá a la derecha

**[0:25:50]** estoy diciendo cuál es la componente que falló

**[0:25:52]** de la máquina

**[0:25:54]** y las componentes no están ordenados

**[0:25:56]** tienen una noción de orden

**[0:25:58]** 1, la 2, la 3 y la 4

**[0:26:00]** y entonces lo que estoy diciendo

**[0:26:02]** es que en términos de frecuencia

**[0:26:04]** la componente 2

**[0:26:06]** fue la que más falló

**[0:26:08]** después la componente 1

**[0:26:10]** después la componente 4 y finalmente la componente 3

**[0:26:12]** fíjense

**[0:26:14]** que no hay una noción de orden

**[0:26:16]** y lo que estoy diciendo es que la que más falló

**[0:26:18]** fue la componente 2

**[0:26:20]** ¿se entiende lo que acabo de decir?

**[0:26:23]** esto es una variable categórica

**[0:26:25]** yo podría haber puesto acá perros y gatos

**[0:26:27]** pero el final es como que no lo puedo ordenar

**[0:26:29]** entonces no puedo calcular un histograma

**[0:26:31]** pero sí puedo calcular

**[0:26:33]** la moda

**[0:26:35]** ¿preguntas? ok, seguimos

**[0:26:43]** ya

**[0:26:45]** entonces nosotros ya tenemos como una idea

**[0:26:47]** de centralidad, de dónde está el centro

**[0:26:49]** de los datos y estamos todos felices y contentos

**[0:26:51]** a su modo de que sabemos más o menos

**[0:26:53]** en torno a qué valor

**[0:26:55]** se mueven los datos

**[0:26:57]** pero no nos basta solamente

**[0:26:59]** con saber en qué en torno a qué valor

**[0:27:01]** se mueven los datos sino que además

**[0:27:03]** a mí me gustaría saber

**[0:27:05]** qué tanto se parece

**[0:27:07]** o sea acerca de mi distribución

**[0:27:09]** a ese valor céntrico que definimos

**[0:27:11]** Priscila

**[0:27:25]** en la clase pasada vimos que había variables

**[0:27:27]** numéricas y variables categóricas

**[0:27:29]** las variables numéricas

**[0:27:31]** tienen una noción de orden

**[0:27:33]** si yo digo 1, 2, 3, 4

**[0:27:35]** yo sé que el 2 es más alto que el 1

**[0:27:37]** y es más bajo que el 4

**[0:27:39]** por decir algo, entonces tiene una noción de orden

**[0:27:41]** cuando yo tengo una noción de orden

**[0:27:43]** puedo hacer un histograma como este

**[0:27:45]** y puedo calcular la media

**[0:27:48]** pero hay variables que no tienen

**[0:27:50]** una noción de orden

**[0:27:52]** como conejo, gato, perro

**[0:27:54]** o nitorrinco

**[0:27:56]** yo no puedo decir

**[0:27:58]** el nitorrinco viene antes que el conejo

**[0:28:00]** no hay una noción de orden

**[0:28:02]** entonces para ese tipo de variables

**[0:28:04]** que son las variables categóricas

**[0:28:06]** yo no puedo calcular un histograma

**[0:28:08]** tal cual como lo vimos delante

**[0:28:10]** donde voy haciendo cajitas

**[0:28:12]** por

**[0:28:14]** por rangos de valores

**[0:28:16]** pero lo que sí puedo hacer es calcular

**[0:28:18]** la frecuencia que ocurra cada una de estas variables

**[0:28:20]** y esa frecuencia

**[0:28:22]** que ocurra cada una de las variables

**[0:28:24]** entonces sobre ella yo puedo calcular

**[0:28:26]** lo que se llama la moda

**[0:28:28]** es el valor que aparece más seguido

**[0:28:30]** entonces en este caso la moda sería componente 2

**[0:28:32]** que es el que aparece más seguido

**[0:28:37]** muchas gracias

**[0:28:42]** entonces como les decía

**[0:28:47]** muchas veces yo no solamente quiero saber

**[0:28:49]** cuál es el valor central de la distribución

**[0:28:51]** sino que quiero además saber este valor

**[0:28:53]** central

**[0:28:55]** qué tan representativo es de la distribución

**[0:28:57]** entonces para eso yo trato

**[0:28:59]** de medir qué tan ancha es la distribución

**[0:29:01]** y una forma de hacer esto es con el rango

**[0:29:03]** el rango equivale al valor máximo

**[0:29:05]** menos al valor mínimo

**[0:29:07]** eso solamente

**[0:29:09]** y fíjense que en la primera distribución

**[0:29:11]** que vimos está acá

**[0:29:14]** el rango es de 43,46

**[0:29:16]** entonces la variable

**[0:29:18]** se mide en un rango de 43,46

**[0:29:20]** en

**[0:29:22]** en vibración

**[0:29:24]** ok

**[0:29:26]** en cambio en la segunda el rango es

**[0:29:28]** de 2,97,24

**[0:29:30]** entonces con esto yo ya sé

**[0:29:32]** imagínense que yo tuviese exactamente la misma

**[0:29:34]** mediana

**[0:29:36]** aun cuando yo tuviese exactamente la misma mediana

**[0:29:38]** yo puedo saber ahora

**[0:29:40]** que la primera, la mediana sobre

**[0:29:42]** la primera distribución es más representativa

**[0:29:44]** de la centralidad

**[0:29:46]** que sobre la segunda distribución

**[0:29:48]** y eso quiere decir que la segunda distribución es mancha

**[0:29:50]** o sea puedo tener valores mucho más grandes

**[0:29:52]** que para la primera

**[0:29:57]** ahora una de las cosas que generalmente

**[0:29:59]** usamos todos

**[0:30:01]** creo que la mayoría acá

**[0:30:03]** que lo usa alguna vez es lo que se llama la varianza

**[0:30:05]** entonces la varianza

**[0:30:07]** mide en promedio

**[0:30:09]** cuánto se desvían los valores

**[0:30:11]** desde la media, esa es como la idea que trata

**[0:30:13]** de calcular la varianza

**[0:30:15]** entonces

**[0:30:17]** lo que hago es que primero calculo el promedio

**[0:30:19]** entonces este es el promedio

**[0:30:21]** y después calculo para cada uno los datos

**[0:30:23]** X y, la diferencia

**[0:30:25]** entre el promedio y ese dato

**[0:30:27]** X y

**[0:30:29]** y entonces después lo que hago es que lo elevo al cuadrado

**[0:30:31]** y al elevarlo al cuadrado

**[0:30:33]** después puedo sumarlos

**[0:30:35]** y los promedio

**[0:30:37]** hay un par de cosas acá

**[0:30:39]** importantes, la primera

**[0:30:41]** es que

**[0:30:43]** hay un cuadrado acá

**[0:30:45]** ¿por qué va un cuadrado?

**[0:30:48]** ¿por qué va el cuadrado?

**[0:30:52]** ¿por qué estoy calculando el promedio al cuadrado?

**[0:30:54]** ¿por qué no el promedio en valor absoluto y chau?

**[0:30:56]** ¿alguien sabe?

**[0:31:01]** ¿por qué no escuché?

**[0:31:05]** no escuché

**[0:31:09]** alguien habló pero no escuché que dijo

**[0:31:11]** yo lo voy a decir porque lo elevamos al cuadrado

**[0:31:20]** lo primero

**[0:31:22]** es que yo quiero medir como la distancia

**[0:31:24]** al promedio

**[0:31:26]** entonces para medir esta distancia

**[0:31:28]** tiene que ser un valor

**[0:31:30]** tiene que ser un valor

**[0:31:32]** un valor positivo

**[0:31:35]** entonces por eso primero

**[0:31:37]** es como una excusa para elevarlo al cuadrado

**[0:31:39]** porque todos los valores del cuadrado son positivos

**[0:31:41]** si yo tengo menos 1 por menos 1

**[0:31:43]** es 1, si yo tengo menos 2 por menos 2

**[0:31:45]** es 4

**[0:31:47]** para eso va el cuadrado

**[0:31:49]** ahora uno podría decir

**[0:31:52]** bueno ok, si muy bien guille

**[0:31:54]** te felicito, pero podríamos

**[0:31:56]** simplemente poner el valor absoluto

**[0:31:58]** medir exactamente la distancia

**[0:32:00]** y la razón por la cual

**[0:32:02]** se le va el cuadrado

**[0:32:04]** es que es para hacerla más sensible

**[0:32:06]** outliers

**[0:32:08]** entonces la

**[0:32:10]** si tú tienes un valor anómalo

**[0:32:12]** y estás promediando

**[0:32:14]** la distancia entre el promedio

**[0:32:16]** y este valor anómalo

**[0:32:18]** esa distancia al cuadrado es mucho más grande

**[0:32:20]** que la distancia por sí sola

**[0:32:22]** entonces comparativamente con el resto de los valores del cuadrado

**[0:32:24]** esta va a ser más alta

**[0:32:26]** y entonces va a ser lo más sensible outliers

**[0:32:28]** ahora, por qué

**[0:32:31]** esta que estoy mostrando acá es la varianza muestral

**[0:32:33]** por qué estamos dividiendo por n menos 1

**[0:32:35]** si estoy calculando un promedio

**[0:32:37]** me voy a estar dividiendo por n

**[0:32:39]** ¿alguien sabe?

**[0:32:44]** ni un matemático en la sala

**[0:32:52]** y le voy a decir

**[0:32:54]** lo que pasa es que si tú divides por n

**[0:32:56]** entonces este estimador

**[0:32:58]** que es la varianza

**[0:33:00]** se sesga

**[0:33:02]** qué quiere decir que se sesgue

**[0:33:04]** que básicamente empieza a moverse

**[0:33:06]** desde su valor original

**[0:33:08]** tú lo puedes demostrar del valor real

**[0:33:10]** tú lo puedes demostrar matemáticamente

**[0:33:12]** que se produce un sejo

**[0:33:14]** si es que tú divides por n

**[0:33:16]** entonces la varianza muestral

**[0:33:19]** se calcula siempre dividiendo por n menos 1

**[0:33:21]** ahora

**[0:33:24]** soy consulta

**[0:33:26]** pero eso es como hacer

**[0:33:28]** más grande conforme n es más pequeño

**[0:33:30]** porque si n es muy grande

**[0:33:32]** ese menú 1 no va a hacer nada

**[0:33:34]** si

**[0:33:36]** si tienes razón

**[0:33:38]** para n pequeño

**[0:33:40]** la varianza

**[0:33:42]** pero incluso tú podrías tener n

**[0:33:44]** no más

**[0:33:46]** si tienes el menú 1

**[0:33:49]** y si tú tuvieses n

**[0:33:51]** y divides por 1

**[0:33:53]** imagínate que tiene un solo dato

**[0:33:55]** y es por 1

**[0:33:57]** entonces lo que va a ocurrir

**[0:33:59]** es que va a tener un valor solamente

**[0:34:01]** de la varianza que no va a ser un muy buen valor

**[0:34:03]** de la varianza

**[0:34:05]** lo que uno esperaría es que cuando n

**[0:34:07]** se vaya infinito

**[0:34:09]** entonces este es el valor real de la varianza

**[0:34:12]** pero no te da el valor real

**[0:34:14]** si es que tú no le pones el menú 1

**[0:34:18]** se entiende

**[0:34:20]** osea al final lo que entiendo es que

**[0:34:22]** como n es más grande

**[0:34:24]** la muestra es más representativa a la población

**[0:34:26]** entonces por ejemplo la varianza es como más cierta

**[0:34:28]** por eso decirlo

**[0:34:30]** porque es mostrarlo

**[0:34:32]** entonces en general lo que uno hace

**[0:34:34]** es que

**[0:34:36]** es una súper buena pregunta

**[0:34:38]** y está un poco fuera del ámbito

**[0:34:40]** de este curso

**[0:34:42]** pero lo que ocurre es que

**[0:34:44]** esto acá es un estimador de la varianza

**[0:34:46]** no es la varianza real

**[0:34:48]** es un estimador de la varianza que uno

**[0:34:50]** estima la varianza de manera mostrar

**[0:34:52]** que es lo que quiere decir eso

**[0:34:54]** que yo estoy en vez como no puedo calcular la varianza

**[0:34:56]** no tengo exceso a la varianza real

**[0:34:58]** entonces tengo que de alguna forma calcular la varianza

**[0:35:00]** desde los datos

**[0:35:02]** y entonces lo que hago es que

**[0:35:04]** saco datos

**[0:35:06]** que siguen cierta distribución de probabilidad

**[0:35:08]** saco estos datos y a partir de estos datos

**[0:35:10]** trato de estimar la varianza

**[0:35:13]** esto es la estimación de la varianza

**[0:35:15]** que se va infinito o sea cuando tengo datos infinito

**[0:35:17]** converge a la varianza real

**[0:35:19]** pero si yo no le pongo el menos uno

**[0:35:21]** entonces se sesga y aun cuando yo

**[0:35:23]** lleve en infinito

**[0:35:25]** entonces no voy a llegar a la varianza real

**[0:35:27]** ahora hay

**[0:35:34]** un problema acá

**[0:35:36]** o no sé si es un problema

**[0:35:38]** esta es la varianza no mano

**[0:35:40]** no sé si sería un problema

**[0:35:42]** pero hay algo acá que

**[0:35:44]** complejiza un poco el análisis

**[0:35:46]** y es que la varianza

**[0:35:48]** no tiene las unidades

**[0:35:50]** de la variable que estoy midiendo

**[0:35:52]** no se si lo ven

**[0:35:55]** si no tiene la unidad de la variable

**[0:35:57]** del cuadrado

**[0:36:00]** porque esta suma se hace sobre

**[0:36:02]** la diferencia del cuadrado

**[0:36:05]** entonces imagínense que yo calculo el promedio

**[0:36:07]** el promedio es uno

**[0:36:09]** por decir algo

**[0:36:11]** y tomo un dato

**[0:36:13]** y el dato me da tres

**[0:36:15]** entonces hago tres menos uno

**[0:36:17]** me da dos y lo lego al cuadrado

**[0:36:19]** entonces no estoy midiendo

**[0:36:21]** como la distancia

**[0:36:23]** a la media

**[0:36:25]** entonces lo que

**[0:36:27]** uno hace

**[0:36:29]** es calcular la raíz

**[0:36:31]** de la varianza

**[0:36:33]** y eso es lo que se llama la despiación standard

**[0:36:35]** entonces de esta forma este es como un trucaso

**[0:36:37]** solamente para que tenga las mismas unidades

**[0:36:39]** de la variable que yo estoy midiendo

**[0:36:41]** y entonces ahora si

**[0:36:43]** me da hace más sentido

**[0:36:46]** la despiación

**[0:36:49]** estándar si tiene las mismas unidades

**[0:36:51]** que la variable que yo estoy midiendo

**[0:36:53]** entonces acá tengo

**[0:36:56]** por ejemplo los mismas distribuciones que teníamos

**[0:36:58]** antes

**[0:37:00]** y veo que

**[0:37:02]** en el primer gráfico estoy graficando

**[0:37:04]** el rango con el amarillo

**[0:37:06]** el rojo está midiendo la media

**[0:37:08]** y el azul

**[0:37:10]** está mostrando

**[0:37:12]** una varianza

**[0:37:14]** una despiación estándar desde la media

**[0:37:16]** hacia cada lado

**[0:37:19]** ahora yo digo la despiación estándar

**[0:37:21]** es de 5,97

**[0:37:23]** y si hago lo mismo al otro lado

**[0:37:25]** la despiación estándar es de 32,47

**[0:37:27]** entonces

**[0:37:29]** yo podría tener el mismo promedio

**[0:37:31]** en la

**[0:37:33]** toda distribución

**[0:37:35]** pero solamente la varianza

**[0:37:37]** me dice a la derecha

**[0:37:39]** o la despiación estándar

**[0:37:41]** me dice en el gráfico de la derecha

**[0:37:43]** que tengo mucha menos certeza

**[0:37:45]** de este promedio que estoy midiéndose

**[0:37:47]** cerca o lejos de este promedio

**[0:37:53]** otra forma de medir la extensión

**[0:37:55]** son los presentiles

**[0:37:57]** y los presentiles son súper útiles

**[0:37:59]** porque te dice

**[0:38:01]** la enviación estándar no te dice hacia que lado

**[0:38:03]** esta

**[0:38:05]** va la simetría

**[0:38:07]** de la distribución

**[0:38:09]** o sea no me dice tengo una cola más larga hacia la derecha

**[0:38:11]** o hacia la izquierda

**[0:38:13]** porque no me dice eso porque el promedio

**[0:38:15]** de las diferencias entre

**[0:38:17]** la media y los datos

**[0:38:20]** es lo que uno si puede hacer

**[0:38:22]** es calcular los presentiles

**[0:38:24]** y los presentiles es una idea bastante simple

**[0:38:26]** ordeno

**[0:38:28]** desde menor a mayor

**[0:38:30]** los datos

**[0:38:32]** y después de eso lo que digo es

**[0:38:34]** que porcentaje de los datos

**[0:38:36]** están bajo o sobre

**[0:38:38]** cierto valor

**[0:38:40]** en realidad

**[0:38:42]** que porcentaje de los datos

**[0:38:44]** está debajo de cierto valor

**[0:38:46]** ok

**[0:38:48]** en esta distribución la que está a la izquierda

**[0:38:50]** tenemos

**[0:38:52]** el promedio que está acá el medio

**[0:38:54]** y

**[0:38:56]** yo podría preguntarme cuál es el presentil

**[0:38:58]** 5

**[0:39:00]** y digo bueno tengo que

**[0:39:02]** calcular el punto

**[0:39:04]** donde si yo me paro ahí

**[0:39:06]** en ese punto de ahí hacia abajo

**[0:39:08]** está el 5% los datos

**[0:39:10]** entonces si yo me pongo acá

**[0:39:12]** de aquí hacia abajo está el 5% los datos

**[0:39:14]** acá

**[0:39:18]** ahora

**[0:39:20]** yo podría decir lo mismo y calcular

**[0:39:22]** el presentil 95

**[0:39:24]** el presentil 95 me dice

**[0:39:26]** que está acá me dice

**[0:39:28]** desde aquí hacia abajo

**[0:39:30]** está el 95% los datos

**[0:39:32]** ok

**[0:39:36]** fíjense ahora el gráfico de la derecha

**[0:39:38]** el gráfico de la izquierda no se ve tanto la diferencia

**[0:39:40]** porque es una

**[0:39:42]** distribución relativamente simétrica

**[0:39:44]** pero vamos al gráfico de la derecha

**[0:39:46]** de hecho si se ve miren

**[0:39:48]** que entre la desviación

**[0:39:50]** y el presentil 5

**[0:39:52]** hay menor distancia que entre

**[0:39:54]** la desviación y el presentil 95

**[0:39:56]** ¿no ven?

**[0:39:58]** acá está un poquito más largo, más grande

**[0:40:00]** que esto y eso básicamente

**[0:40:02]** lo que me está diciendo es que hay una cola

**[0:40:04]** que es esta cola que habíamos hablado al principio

**[0:40:06]** que es la cola con los valores anúmalos

**[0:40:08]** que eran los valores de alta vibración

**[0:40:10]** entonces esto ya me dice

**[0:40:13]** desde los datos, desde el número

**[0:40:15]** mismo me dice que

**[0:40:17]** estamos moviéndonos que mi distribución

**[0:40:19]** tiene algunos valores anúmalos

**[0:40:21]** ahora si voy al gráfico de la derecha

**[0:40:23]** veo que

**[0:40:25]** la desviación

**[0:40:27]** está muy cercana al presentil 5

**[0:40:29]** digamos la media menos la desviación

**[0:40:31]** está muy cercano al presentil

**[0:40:33]** 5

**[0:40:35]** pero la media más la desviación

**[0:40:37]** está muy lejana

**[0:40:39]** del presentil 95

**[0:40:41]** y esto lo que me dice es lo mismo

**[0:40:43]** que este tiene valores mucho más anómalos

**[0:40:45]** que el data set del izquierdo

**[0:40:47]** preguntas

**[0:40:51]** yo les tengo una pregunta a ustedes

**[0:40:56]** ¿qué presentil es la mediana?

**[0:41:00]** 50

**[0:41:05]** ya, gracias

**[0:41:08]** el presentil 50 es la mediana

**[0:41:10]** justo el valor que está en el

**[0:41:12]** bueno acá hay otro ejemplo

**[0:41:17]** de presentil, acá está el presentil 5

**[0:41:19]** el 25, el 50, el 75 y el 95

**[0:41:21]** y una al hacer este tipo

**[0:41:23]** de cálculo

**[0:41:25]** ver dónde están los presentiles tú puedes ver

**[0:41:27]** rápidamente como que tan simétrica

**[0:41:29]** o asimétrica es la

**[0:41:31]** la distribución

**[0:41:35]** ok, entonces ya podemos saber

**[0:41:37]** con todo esto que acabamos de ver

**[0:41:39]** dónde está el centro de la distribución

**[0:41:41]** y también

**[0:41:43]** qué tan representativo es este centro

**[0:41:45]** de la distribución completa

**[0:41:47]** pero ahora vamos a ver algunas herramientas

**[0:41:49]** de visualización

**[0:41:52]** entonces, tenemos este data set

**[0:41:54]** este data set se llama el cuarteto

**[0:41:56]** de anscombe

**[0:41:58]** porque el promedio son

**[0:42:00]** cuatro data sets, el data set 1

**[0:42:02]** el data set 2, el data set 3

**[0:42:04]** y el data set 4

**[0:42:06]** y cada uno de estos data sets tiene dos

**[0:42:08]** variables, la variable x y la variable y

**[0:42:10]** la variable x y la variable y

**[0:42:12]** la variable x y la variable y

**[0:42:14]** y fíjense que si yo calculo

**[0:42:16]** el promedio, el promedio

**[0:42:18]** de los cuatro

**[0:42:20]** data sets es exactamente el mismo

**[0:42:22]** para cada una de las variables

**[0:42:24]** entonces acá 9

**[0:42:26]** 9, 9

**[0:42:28]** para y 7,5 y 7,5

**[0:42:30]** 7,5 y 7,5

**[0:42:32]** y la distribución estándar

**[0:42:34]** es la misma también

**[0:42:36]** entonces en el eje x

**[0:42:38]** la distribución estándar es de 3,32

**[0:42:40]** para y es 2,03

**[0:42:42]** 3,32, 2,03

**[0:42:44]** 3,32, 2,0

**[0:42:46]** entonces pareciera que los cuatro

**[0:42:48]** data sets son los mismos

**[0:42:51]** pero si yo los grafico ahora

**[0:42:53]** resulta que los data sets son totalmente

**[0:42:55]** correctos, fíjense que este acá

**[0:42:58]** van como en una línea recta

**[0:43:00]** pero con ruido, con acto de ruido

**[0:43:02]** este acá no va en una línea recta

**[0:43:04]** ok, este acá

**[0:43:06]** de repente tiene un valor anómalo

**[0:43:08]** y este acá tiene

**[0:43:10]** el mismo valor en X

**[0:43:13]** ok, entonces

**[0:43:15]** que lo que estoy diciendo con esto es que

**[0:43:17]** la media, la mediana, la distribución estándar

**[0:43:19]** los presentiles si nos ayudan

**[0:43:21]** pero no son suficientes como para

**[0:43:23]** darnos un contexto real de lo que

**[0:43:25]** estamos midiendo

**[0:43:30]** otro ejemplo, si yo les digo que el consumo

**[0:43:32]** medio de gasolina de los camiones de la compañía

**[0:43:34]** es de 1,440 litros

**[0:43:36]** pero los camiones que usted administra

**[0:43:38]** gastan sobre 2,500 litros

**[0:43:40]** ¿qué es lo que les estoy sugiriendo con esto?

**[0:43:42]** este sobre la media

**[0:43:48]** o quizás estoy

**[0:43:50]** estoy como dato anómalo

**[0:43:52]** soy una persona anómala, pero con su bien

**[0:43:54]** claro, entonces yo podría ir y decirle

**[0:43:56]** oye pero ¿cómo es posible que sus

**[0:43:58]** camiones consuman tanta gasolina?

**[0:44:00]** y ustedes van a venir y van a decir

**[0:44:02]** espera, espera, espera

**[0:44:04]** porque si nosotros hacemos el gráfico

**[0:44:06]** de la distribución

**[0:44:08]** entonces nos damos cuenta

**[0:44:10]** de que hay un valor

**[0:44:12]** hay un valor anómalo muy grande acá

**[0:44:14]** entonces hay muchos ceros

**[0:44:16]** ¿qué es lo que puede significar esto?

**[0:44:19]** muchos camiones inactivos

**[0:44:23]** muchos camiones inactivos

**[0:44:25]** entonces es como jefe

**[0:44:27]** está calculando al promedio

**[0:44:29]** fíjense que eso lo puedo hacer

**[0:44:31]** lo puedo hacer solamente

**[0:44:33]** de manera gráfica

**[0:44:35]** o en este caso lo hice de manera gráfica

**[0:44:37]** pero fíjense en la potencia

**[0:44:39]** que tiene el poder hacer un gráfico

**[0:44:41]** solamente un gráfico

**[0:44:45]** ¿para qué sirve la visualización

**[0:44:47]** de los datos? son buenas prácticas

**[0:44:49]** para analizar

**[0:44:51]** ¿a qué me refiero en esto? que yo gráfico

**[0:44:53]** para verlo yo primero

**[0:44:55]** y de esa forma puedo identificar ciertos patrones

**[0:44:57]** que pueden no verse directamente

**[0:44:59]** desde las estadísticas

**[0:45:01]** Cristian

**[0:45:03]** me ayuda a formular hipótesis

**[0:45:05]** por ejemplo recién acaban de formular un hipótesis

**[0:45:07]** que hay muchos camiones inactivos

**[0:45:09]** ayuda a determinar

**[0:45:11]** el siguiente paso de análisis o de modelamiento

**[0:45:13]** entonces yo podría decir

**[0:45:15]** o el jefe podría decirle

**[0:45:17]** pero si no hay ningún camión inactivo

**[0:45:19]** bueno entonces algo está pasando

**[0:45:21]** a lo mejor la gente no está reportando

**[0:45:23]** el consumo de gasolina

**[0:45:25]** algo raro está pasando

**[0:45:28]** entonces el siguiente paso podría

**[0:45:30]** ir y ver quién anotó los datos

**[0:45:32]** o podríamos ver quién

**[0:45:34]** qué es lo que está pasando, dónde están los camiones

**[0:45:36]** cuánto es tan inactivo

**[0:45:38]** ese tipo de cosas, entonces no ayuda

**[0:45:40]** a determinar cuál es el siguiente paso

**[0:45:43]** pero además la visualización de datos sirve mucho

**[0:45:45]** para comunicar

**[0:45:47]** entonces ahora en este mismo ejemplo

**[0:45:49]** que vimos yo comuniqué

**[0:45:51]** a usted me comunicaron a mí

**[0:45:53]** que algo pasa

**[0:45:55]** algo raro pasaba

**[0:45:57]** te sirve para proveer

**[0:45:59]** evidencia pero muy importante

**[0:46:01]** muy muy muy importante

**[0:46:03]** te sirve para influenciar

**[0:46:05]** y persuadir

**[0:46:07]** y esto vamos a tener un poco acá

**[0:46:09]** porque

**[0:46:11]** podrían utilizarlo

**[0:46:13]** para persuadir

**[0:46:15]** y para influenciar

**[0:46:17]** pero también usted podría ser

**[0:46:19]** alguien podría tratar de influirlo a usted

**[0:46:21]** y ustedes tienen que estar muy atentos

**[0:46:23]** siempre en este tipo de cosas

**[0:46:25]** y no lo estoy diciendo de manera negativa

**[0:46:27]** siendo que uno siempre tiene que ser crítico

**[0:46:29]** con el trabajo que hace

**[0:46:33]** existe el criterio de Tufte

**[0:46:35]** que básicamente apunta

**[0:46:37]** hacia la excelencia gráfica

**[0:46:39]** y lo que Tufte decía es

**[0:46:41]** tenemos que tratar de transmitir

**[0:46:43]** el mayor número de ideas

**[0:46:45]** en el menor tiempo

**[0:46:47]** usando la menor cantidad de tinta

**[0:46:49]** en el menor espacio

**[0:46:51]** entonces cuando uno genera un gráfico

**[0:46:53]** en realidad yo me quedo acá principalmente

**[0:46:55]** con mayor número de ideas en el menor tiempo

**[0:46:57]** la menor cantidad de tinta

**[0:46:59]** en el menor espacio se supone que apunta

**[0:47:01]** a

**[0:47:03]** a lo mismo, a tener mayor idea

**[0:47:05]** en la menor cantidad de tiempo

**[0:47:08]** y además esto fue hecho

**[0:47:10]** cuando lo gráfico se imprimía

**[0:47:12]** entonces la tinta

**[0:47:14]** hoy en día no sé si me importa tanto

**[0:47:16]** y tampoco menor espacio

**[0:47:18]** porque puedo abrir lo gráfico cerrando

**[0:47:20]** hacer lo que yo quiero

**[0:47:23]** este es un ejemplo

**[0:47:26]** de integridad visual

**[0:47:28]** está mostrando este gráfico

**[0:47:30]** lo que dice es la economía

**[0:47:32]** en gasolina

**[0:47:34]** para los distintos automóviles

**[0:47:36]** acá a la izquierda voy mostrando el año

**[0:47:38]** y a la derecha

**[0:47:41]** lo que voy mostrando

**[0:47:43]** es el número

**[0:47:45]** de millas por galón

**[0:47:47]** en función del año

**[0:47:49]** ok

**[0:47:51]** entonces fíjense que en 1978

**[0:47:53]** había 18 millas por galón

**[0:47:55]** y ya el 85

**[0:47:57]** había 27,12 millas por galón

**[0:47:59]** que les parece este gráfico

**[0:48:01]** como gráfico

**[0:48:05]** creativo

**[0:48:07]** bonito

**[0:48:11]** tiene un problema

**[0:48:14]** el problema es que

**[0:48:16]** acá es 18

**[0:48:18]** y acá es 27

**[0:48:20]** esto me induce a creer

**[0:48:22]** que este gráfico que está alineado acá

**[0:48:24]** que es como

**[0:48:26]** 10 veces más grande que está acá

**[0:48:28]** me induce a creer que el 85

**[0:48:30]** el año 85

**[0:48:32]** eran

**[0:48:35]** 10 veces más

**[0:48:37]** el número de millas por galón

**[0:48:39]** visualmente me induce a creer eso

**[0:48:41]** ok

**[0:48:44]** entonces

**[0:48:46]** pero en realidad no es así pues

**[0:48:48]** son 27 de 18

**[0:48:50]** más o 27

**[0:48:52]** no debería ser tan grande la diferencia en la línea

**[0:48:54]** ok

**[0:48:59]** otro ejemplo

**[0:49:01]** yo les digo

**[0:49:03]** que yo corro mucho más rápido que ustedes

**[0:49:05]** entonces yo voy a graficar

**[0:49:07]** el número de millas que corro

**[0:49:09]** por hora

**[0:49:11]** y este soy yo y este eres tú

**[0:49:13]** y miren fíjense

**[0:49:15]** yo corro mucho más rápido que ustedes

**[0:49:17]** y ustedes me dicen a ver pero

**[0:49:19]** que acá hay algo raro

**[0:49:21]** que hay de raro

**[0:49:23]** esto pareciera como si yo fuera flash

**[0:49:27]** la escala

**[0:49:29]** claro porque acá

**[0:49:31]** estamos entre 8,09

**[0:49:33]** y 8,1

**[0:49:35]** pero

**[0:49:37]** en la práctica esa es la diferencia muy poca

**[0:49:39]** todos esos términos podrían decir ya así

**[0:49:41]** pero no es para tanto

**[0:49:43]** es un poquito más no más

**[0:49:45]** y si tú lo graficaras correctamente sería algo como esto

**[0:49:51]** este otro ejemplo

**[0:49:53]** este es un ejemplo de casos reales

**[0:49:55]** donde pasó esto

**[0:49:57]** el termo que acabamos de darle

**[0:49:59]** entonces acá decía

**[0:50:01]** si expiran

**[0:50:03]** los cortes de impuestos

**[0:50:05]** ahora 35%

**[0:50:07]** y después en enero el 2013

**[0:50:09]** en este caso 39,6

**[0:50:11]** estos Fox News

**[0:50:13]** que no se decir conocen pero no tienen muy

**[0:50:15]** muy buena fama como noticia

**[0:50:17]** entonces esto salió realmente en las noticias

**[0:50:19]** en algún momento

**[0:50:21]** y en realidad tú decir bueno pero

**[0:50:23]** suena como que si fuera algo desastroso

**[0:50:25]** pero en realidad no es tanto

**[0:50:28]** si se fijan la diferencia

**[0:50:30]** no es tanta

**[0:50:33]** otro ejemplo

**[0:50:35]** en este caso acá sale el año en el eje X

**[0:50:37]** y en el eje I

**[0:50:39]** dice el número

**[0:50:41]** de empleos perdidos

**[0:50:43]** por cuartil

**[0:50:46]** dice 7,7

**[0:50:48]** millones

**[0:50:50]** 9 millones, 13,5 millones, 15 millones

**[0:50:52]** esto parece así como que vamos

**[0:50:54]** horrible hace arriba y no

**[0:50:56]** no vamos a tener nunca de nuevo Fox News

**[0:50:58]** pero en realidad estaba el hecho

**[0:51:00]** el gráfico

**[0:51:02]** el gráfico se vería algo como esto

**[0:51:04]** que va subiendo

**[0:51:06]** pero no es como que vamos subiendo sin parar

**[0:51:08]** pareciera como que hubo un alza grande

**[0:51:10]** entre septiembre del 2008

**[0:51:12]** y marzo del 2009

**[0:51:14]** pero después se atendió a bajar

**[0:51:16]** ¿recuerdan este gráfico?

**[0:51:20]** ah German

**[0:51:23]** no es que

**[0:51:25]** apagase con ese gráfico después con mi punto

**[0:51:27]** que ya tengo un punto muy interesante

**[0:51:29]** pero termine el gráfico no

**[0:51:31]** ¿recuerdan este gráfico?

**[0:51:37]** este gráfico se presentó

**[0:51:40]** durante la pandemia

**[0:51:42]** en cadena nacional

**[0:51:44]** cuando hablaron

**[0:51:46]** del porcentaje de vacunación en Chile

**[0:51:48]** ¿y entonces

**[0:51:51]** tú miras este gráfico y básicamente dijeron

**[0:51:53]** no, si vamos bien con la vacunación

**[0:51:55]** hemos seguido vacunando y no

**[0:51:57]** habíamos problemas y las tasas

**[0:51:59]** no han diminuido y bla bla bla

**[0:52:01]** y si tú miras el gráfico sin mirar

**[0:52:03]** nada más que la línea, tú dices ah

**[0:52:05]** si en realidad hubo como una bajita

**[0:52:07]** pues como que subió y ha bajado un poquito

**[0:52:09]** de abajo

**[0:52:12]** pero si tú graficas

**[0:52:14]** como alguien se lo cuenta

**[0:52:16]** la escala acá

**[0:52:18]** ¿está en qué tipo de escala?

**[0:52:20]** esa es el logarítmica o exponencial

**[0:52:22]** no sé que depende del ángulo

**[0:52:24]** escala logarítmica

**[0:52:26]** entonces en realidad

**[0:52:28]** entre este punto

**[0:52:30]** y este

**[0:52:32]** entre este y este

**[0:52:35]** hay un décimo

**[0:52:37]** de la distancia entre este y este

**[0:52:39]** graficas correctamente, que fue lo que yo hice

**[0:52:41]** básicamente lo que tú ves

**[0:52:43]** es algo de este estilo

**[0:52:45]** y entonces

**[0:52:48]** pareciera que en realidad

**[0:52:50]** en la práctica hubo una baja

**[0:52:52]** durante los últimos, no sé, desde

**[0:52:54]** marzo a abril, una baja en la tasa

**[0:52:56]** de vacunación de más o menos un 50%

**[0:52:58]** o sea estaba como

**[0:53:00]** en 1.5 y llegó como a 1.8

**[0:53:02]** casi un 50%

**[0:53:05]** entonces en realidad este gráfico

**[0:53:07]** primero fue presentado en el

**[0:53:09]** nacional por el gobierno de Chile

**[0:53:11]** tratando

**[0:53:13]** de

**[0:53:15]** de no influenciar

**[0:53:18]** de influir en la población

**[0:53:20]** pero siendo

**[0:53:22]** incorrecto en la forma en la cual

**[0:53:24]** está transmitiendo su mensaje

**[0:53:26]** o transmitiendo un mensaje incorrecto

**[0:53:30]** ¿alguien quería hacer una pregunta?

**[0:53:32]** si, no, yo quería mencionar algo que

**[0:53:34]** yo llegó un poquito tarde a la clase

**[0:53:36]** porque estaba sin luz, disculpa

**[0:53:38]** pero en justo cuando empezó

**[0:53:40]** a mostrar los gráficos

**[0:53:42]** y aparte de la forma visual

**[0:53:44]** que usted ya dijo los puntos

**[0:53:46]** también en el story de link

**[0:53:48]** también hay un tema de uno cómo dice la información

**[0:53:50]** sin más lejos, el día de la mañana

**[0:53:52]** vi una evaluación redes sociales

**[0:53:54]** que decía como que un 25%

**[0:53:56]** de los accidentes de trabajo

**[0:53:58]** se reportan un viernes o lunes

**[0:54:00]** en augustin así

**[0:54:02]** y es como

**[0:54:04]** yo me gusta pensar

**[0:54:06]** ¿cuánto pesa cada día?

**[0:54:08]** se sumemos que es como una distribución uniforme

**[0:54:10]** que no es así, pero sumamos

**[0:54:12]** realmente debería ser un 30%

**[0:54:14]** es decir 25% suena super al armista

**[0:54:16]** pero son 7 días a la semana y cada día

**[0:54:18]** aporta aproximadamente un 15%

**[0:54:20]** entonces igual está como la intención

**[0:54:22]** de la forma en que uno hizo las cosas

**[0:54:24]** entonces igual, aunque ahí no hubo gráficos

**[0:54:26]** fue una oración no más

**[0:54:28]** pero igual la forma que se planteó

**[0:54:30]** sonaba super al armista

**[0:54:32]** básicamente diciendo esperan el fin de semana

**[0:54:34]** para crear la licencia, básicamente

**[0:54:36]** por el de hecho el número, si uno lo pensaba un poco

**[0:54:38]** decía todo lo contrario

**[0:54:40]** claro, es igual que ese tema

**[0:54:42]** si, bueno ese es

**[0:54:44]** un problema comunicacional que

**[0:54:46]** existe no sólo de esa forma, existe de

**[0:54:48]** muchas formas

**[0:54:50]** y generalmente

**[0:54:53]** yo diría que nosotros tratamos

**[0:54:55]** de comunicar o de entender

**[0:54:57]** desde la ciencia de datos

**[0:54:59]** los datos de manera

**[0:55:01]** lo más correcta posible

**[0:55:03]** pero los periodistas en general

**[0:55:05]** en general no hay goto

**[0:55:07]** pero en general o varios

**[0:55:09]** digamos periodistas no tienen

**[0:55:11]** formación en ciencia de datos

**[0:55:13]** entonces simplemente tirar

**[0:55:15]** número y no se preocupan

**[0:55:17]** de la integridad de lo que están diciendo

**[0:55:19]** esto es más grave

**[0:55:21]** cuando uno habla de

**[0:55:23]** no sé si más grave, pero es grave también

**[0:55:25]** cuando uno habla de correlación

**[0:55:27]** versus causalidad

**[0:55:29]** no sé si saben de lo que estoy hablando

**[0:55:31]** pero básicamente

**[0:55:33]** es distinto que dos variables

**[0:55:35]** estén

**[0:55:37]** correladas o sea que al momento de subir

**[0:55:39]** una también sua la otra

**[0:55:41]** a decir que

**[0:55:43]** al decir que

**[0:55:45]** una variable impacta

**[0:55:47]** en que la otra suba

**[0:55:50]** entonces un ejemplo así muy burdo

**[0:55:52]** es como por ejemplo decir

**[0:55:54]** la temperatura

**[0:55:56]** cuando sube la temperatura

**[0:55:59]** se empiezan a vender más helado

**[0:56:01]** por decir algo

**[0:56:03]** y entonces alguien podría llegar y decir

**[0:56:05]** oye cada vez que se venden helado

**[0:56:07]** empieza a subir la temperatura

**[0:56:09]** entonces la causa de que haga calor

**[0:56:11]** hoy día es que hemos comprado mucho helado

**[0:56:13]** entonces paremos de comprar helado

**[0:56:15]** alguien podría decir algo así

**[0:56:17]** que suena estupido

**[0:56:19]** y en realidad es una mala interpretación

**[0:56:21]** de la correlación

**[0:56:23]** versus la causalidad

**[0:56:25]** o sea la causa

**[0:56:27]** o sea la venta helado está correlada

**[0:56:29]** con la temperatura

**[0:56:31]** pero no quiere decir que porque

**[0:56:33]** se vendan más helado

**[0:56:35]** va a subir la temperatura

**[0:56:37]** en este caso es súper burdo el ejemplo

**[0:56:39]** pero muchas veces

**[0:56:41]** muchas veces lo dicen en el noticiero

**[0:56:43]** tratan de interpretar

**[0:56:45]** una correlación como una causalidad

**[0:56:47]** dale german

**[0:56:50]** que a mí lo que me pasó ver también

**[0:56:52]** es que bueno que siempre que ocurre

**[0:56:54]** es que hay una correlación

**[0:56:56]** netamente hasta el punto matemático

**[0:56:58]** igual hay que buscar algún tipo de mecanismo

**[0:57:00]** es un tema

**[0:57:02]** y a mí me pasó que un análisis que hizo

**[0:57:04]** un colega anulice yo

**[0:57:06]** que le llegó un análisis y él dijo

**[0:57:08]** algo así como oye esto no tiene bien ni cabeza

**[0:57:10]** entonces lo que él hizo para destrozar el análisis

**[0:57:12]** fue que

**[0:57:14]** y de verdad yo lo encontré muy chistoso

**[0:57:16]** él se conectó a la base a todos los recursos humanos

**[0:57:18]** bajo el dígito verificador de todos los trabajadores

**[0:57:20]** y lo intentó correlacionar

**[0:57:22]** y el dígito verificador tenía más correlación

**[0:57:24]** que el análisis que había hecho otro ingeniero

**[0:57:26]** entonces básicamente

**[0:57:28]** lo que él básicamente decía

**[0:57:30]** decía ya contratemos más gente con estos dígitos verificadores

**[0:57:32]** y le dijo por qué eso está haciendo un análisis

**[0:57:34]** entonces

**[0:57:36]** lo que quería decir básicamente

**[0:57:38]** es que no había

**[0:57:40]** no había nada que conectar

**[0:57:42]** al scatter plot que la otra persona había dibujado

**[0:57:44]** eso era básicamente lo que quería decir

**[0:57:46]** y a veces pasa porque

**[0:57:48]** cuando tenemos muchos datos

**[0:57:50]** la probabilidad de que algo

**[0:57:52]** esté correlacionado solamente por azar

**[0:57:54]** igual es harta

**[0:57:56]** el cuidado que hay que tener

**[0:57:59]** podemos hablar ampliamente de causalidad

**[0:58:01]** es uno de los temas que me apasiona

**[0:58:03]** pero creo que estamos saliendo en un poco del

**[0:58:05]** del curso

**[0:58:07]** pero si en la práctica

**[0:58:09]** uno puede calcular

**[0:58:11]** causalidad y hay contrafactual

**[0:58:13]** y cosas de ese estilo que son herramientas que uno usa

**[0:58:15]** para calcular la causalidad

**[0:58:17]** es mucho más complejo que calcular una correlación

**[0:58:19]** entonces todo el mundo calcula correlaciones

**[0:58:21]** porque son fáciles de calcular

**[0:58:23]** la causalidad es mucho más compleja

**[0:58:26]** y hay cosas que se llaman confusores

**[0:58:28]** que son variables que tú no mediste

**[0:58:30]** pero que pueden impactar en dos variables

**[0:58:32]** o más simultáneamente

**[0:58:34]** y hacen que se correlen

**[0:58:36]** y estos confusores son, puede ser

**[0:58:38]** la causa real

**[0:58:40]** pero tú no la ves

**[0:58:42]** y entonces solo ves que las dos suben

**[0:58:44]** por una tercera variable

**[0:58:46]** que no está inigiendo

**[0:58:51]** voy a darles un par de

**[0:58:53]** ejemplos de tipo de visualizaciones

**[0:58:55]** y como para entender

**[0:58:57]** a pasar a tratar de entender

**[0:58:59]** cómo

**[0:59:01]** cómo realizar una hipótesis

**[0:59:03]** que algo que nada tenga que hacer para su proyecto

**[0:59:05]** ok

**[0:59:08]** entonces para distribuciones

**[0:59:10]** lo primero es el histograma

**[0:59:12]** se acuerdan que hablamos de histograma

**[0:59:14]** entonces histograma es algo que nosotros podemos usar

**[0:59:16]** para calcular distribuciones

**[0:59:18]** pero también

**[0:59:20]** está la distribución acumulada

**[0:59:22]** que esto también es súper importante

**[0:59:24]** y básicamente lo que uno hace

**[0:59:26]** es que en vez de simplemente calcular

**[0:59:28]** para cada bin

**[0:59:30]** cuántos objetos van cayendo dentro

**[0:59:32]** lo que hago

**[0:59:34]** es que

**[0:59:36]** empiezo a mover la variable

**[0:59:38]** y voy calculando

**[0:59:40]** todo lo que va cayendo

**[0:59:42]** antes de ese umbral que estoy definiendo

**[0:59:44]** entonces por ejemplo cuando yo digo

**[0:59:46]** voy a calcular todo lo que está

**[0:59:48]** antes de un valor 30

**[0:59:50]** entonces

**[0:59:52]** lo que estoy diciendo es calculo

**[0:59:54]** un porcentaje

**[0:59:56]** de lo que está antes del 30

**[0:59:58]** cae acá

**[1:00:00]** un porcentaje de todo mis datos

**[1:00:02]** tiene un valor menor a 30

**[1:00:04]** ¿por qué me sirve esto?

**[1:00:06]** ¿por qué me sirve tanto para entender mi distribución?

**[1:00:08]** porque yo podría decir

**[1:00:10]** ¿y dónde está la mediana acá?

**[1:00:12]** ¿quién me puede decir dónde está la mediana en esta distribución?

**[1:00:14]** el percentil 50

**[1:00:20]** ¿si dónde está?

**[1:00:22]** ¿cuál es el valor de la mediana?

**[1:00:25]** más o menos

**[1:00:31]** 40

**[1:00:33]** entre 40 y 50

**[1:00:35]** claro, lo que seguramente usted

**[1:00:37]** dijeron acá

**[1:00:39]** voy a ir al 0,5

**[1:00:41]** y voy a calcular

**[1:00:43]** el valor

**[1:00:45]** al cual

**[1:00:47]** el 50% de los objetos se encuentra

**[1:00:49]** y ese valor está acá

**[1:00:51]** que es como 41

**[1:00:53]** y fíjense que yo puedo ver

**[1:00:55]** muchas más cosas, o sea puedo decir

**[1:00:57]** ¿y dónde está el 80%?

**[1:00:59]** bueno acá

**[1:01:02]** en este valor

**[1:01:04]** ¿y dónde está el 20? acá

**[1:01:06]** en este valor acá

**[1:01:08]** y nos sirve mucho porque

**[1:01:10]** yo puedo empezar a ver distribuciones que sean algunas más

**[1:01:12]** y otras más

**[1:01:14]** y entonces yo puedo empezar a generar hipótesis

**[1:01:16]** acerca de la distribución

**[1:01:20]** cuando tú tienes variables en dos dimensiones

**[1:01:22]** tú puedes hacer un histograma también

**[1:01:24]** en dos dimensiones

**[1:01:28]** scatter plots

**[1:01:30]** también te sirven para mostrar la distribución

**[1:01:32]** perdón

**[1:01:34]** un minuto

**[1:01:38]** y básicamente lo que yo hago

**[1:01:43]** es que si yo tengo dos variables

**[1:01:45]** grafico

**[1:01:48]** en el eje X una variable y en el eje Y otra variable

**[1:01:50]** uno puede hacer scatter plots

**[1:01:52]** que también muestren la distribución

**[1:01:54]** la distribución

**[1:01:56]** permiso, necesito un minuto

**[1:01:58]** voy a volver

**[1:02:28]** ya, perdón

**[1:02:30]** entonces les decía que el problema con los scatter plots

**[1:02:32]** es que a veces te caen muchos puntos

**[1:02:34]** uno arriba de otro y uno no sabe cómo están distribuidos

**[1:02:36]** entonces lo que uno puede hacer

**[1:02:38]** es pintar los colores

**[1:02:40]** de acuerdo al número de objetos que hay alrededor

**[1:02:42]** de ese punto

**[1:02:49]** los scatter plots

**[1:02:51]** nos sirven para

**[1:02:53]** medir

**[1:02:55]** o para entender relaciones

**[1:02:57]** entre dos variables

**[1:03:00]** entonces por ejemplo en este gráfico acá

**[1:03:02]** yo estoy mostrando en el eje X

**[1:03:04]** la altura y en el eje Y el peso

**[1:03:06]** y de inmediato puedo generar un hipótesis

**[1:03:10]** un hipótesis es que a medida que

**[1:03:12]** aumenta la altura de las personas

**[1:03:14]** aumenta el peso de las personas

**[1:03:16]** y entonces si yo quisiera

**[1:03:18]** estimar el peso de las personas

**[1:03:20]** podría tratar de hacerlo a través de la altura

**[1:03:22]** entonces podría generar un modelo

**[1:03:24]** que aprenda

**[1:03:26]** a distinguir el peso de las personas

**[1:03:28]** desde la altura

**[1:03:31]** los gráficos de torta

**[1:03:35]** nos ayudan también a

**[1:03:37]** distinguir eso si en este caso composición

**[1:03:39]** generalmente se usan para variables catégóricas

**[1:03:41]** entonces

**[1:03:43]** en este caso categorice una variable

**[1:03:45]** que era la edad

**[1:03:47]** y lo puse entre distintos rangos

**[1:03:49]** y nos muestran gráficamente

**[1:03:51]** podemos distinguir rápidamente

**[1:03:53]** cuáles son los porcentajes

**[1:03:55]** como se distribuían en distintos porcentajes

**[1:03:58]** también están estos gráficos apilados por área

**[1:04:00]** entonces acá lo que voy mostrando

**[1:04:02]** es en el eje X

**[1:04:04]** en el tiempo

**[1:04:06]** en el eje Y

**[1:04:08]** en miles de personas

**[1:04:10]** y yo lo que puedo ir viendo

**[1:04:12]** con estos gráficos es que no solamente

**[1:04:14]** tengo la distribución

**[1:04:16]** de personas por tiempo

**[1:04:18]** sino que además puedo dividirlo

**[1:04:20]** en distintos rangos

**[1:04:22]** y de hecho podría ser que esto fuesen

**[1:04:24]** hombres mujeres

**[1:04:26]** adultos niños

**[1:04:28]** que son variables que no son

**[1:04:30]** numéricas que son catégóricas

**[1:04:36]** los gráficos de barra se usan mucho

**[1:04:38]** para variables catégóricas

**[1:04:40]** es como el equivalente

**[1:04:42]** al listograma

**[1:04:44]** pero para variables catégóricas

**[1:04:46]** y acá lo que estoy mostrando son distintos grupos de personas

**[1:04:48]** entonces está el grupo 1

**[1:04:50]** el grupo 2, el grupo 3, el grupo 4 y el grupo 5

**[1:04:52]** y tengo

**[1:04:54]** en azul los hombres

**[1:04:56]** en naranjo las mujeres

**[1:04:58]** y acá mirándolo

**[1:05:00]** directamente

**[1:05:02]** el gráfico uno puede decir

**[1:05:04]** hay cosas que puedo entender

**[1:05:06]** porque en el grupo 4

**[1:05:08]** hay más hombres que mujeres

**[1:05:10]** pero no solo hay más hombres que mujeres

**[1:05:12]** porque eso lo podría haber sacado el número

**[1:05:14]** sino que no es...

**[1:05:16]** o sea, esta diferencia sólo ocurre en este grupo

**[1:05:18]** en los otros grupos no ocurre tan grandes

**[1:05:20]** o no veo

**[1:05:22]** una diferencia tan grande en los otros grupos

**[1:05:26]** y también uno puede hacer estos gráficos

**[1:05:28]** de barra pilado

**[1:05:30]** donde tenemos por ejemplo en este caso

**[1:05:32]** distintas tiendas

**[1:05:34]** y dice qué tipo de objetos están vendiendo

**[1:05:36]** entonces el azul

**[1:05:38]** es ropa

**[1:05:40]** el amarillo es equipamiento

**[1:05:42]** y el morado es accesorios

**[1:05:44]** y lo que podemos ver acá rápidamente

**[1:05:46]** así porque eso se trata

**[1:05:48]** en lo gráfico de entender rápidamente algo

**[1:05:50]** es que por ejemplo

**[1:05:52]** en Cherry Street es donde más se vende

**[1:05:54]** en esta tienda es donde más se vende por leco

**[1:05:56]** pero

**[1:05:58]** se vende menos accesorios

**[1:06:00]** que en Strawberry Mode

**[1:06:02]** ¿no ven?

**[1:06:04]** y uno los puede ver rápidamente

**[1:06:06]** y uno puede ver también que en Peach Street

**[1:06:08]** se vende más equipamiento que en ninguna otra tienda

**[1:06:14]** ahora gráficos de barras

**[1:06:16]** versus gráficos de líneas

**[1:06:18]** miren estos dos gráficos y díganme qué opinan

**[1:06:20]** lo que están mostrando acá es

**[1:06:22]** hombre-mujer

**[1:06:24]** acá hombre-mujer

**[1:06:26]** acá 12 años

**[1:06:28]** 12 años y 10 años

**[1:06:30]** 12 años y 10 años

**[1:06:32]** el de la derecha muestra lo mismo que el de la izquierda

**[1:06:34]** en los dos casos

**[1:06:38]** sin contextos un poquito difícil

**[1:06:40]** dar una opinión pero lo que sí puedo decir

**[1:06:42]** es que

**[1:06:44]** en el hombre-mujer

**[1:06:46]** está mejor el gráfico de barras

**[1:06:48]** que aparece en las edades

**[1:06:50]** está mejor en de líneas

**[1:06:52]** porque las barras son categóricas

**[1:06:54]** aquí no se puede interpolar

**[1:06:56]** en cambio en las edades sí se puede interpolar

**[1:06:58]** entonces tiene sentido que se haga una línea

**[1:07:01]** Exacto, súper bien

**[1:07:03]** entonces básicamente si yo miro el gráfico acá abajo

**[1:07:05]** de líneas

**[1:07:07]** dice acá hay 10 años y acá hay 12 años

**[1:07:09]** y acá está la

**[1:07:11]** altura y uno dice

**[1:07:13]** bueno en realidad uno mentalmente

**[1:07:15]** puede interpolar

**[1:07:17]** yo puedo pensar en alguien de 11 años y que debería

**[1:07:19]** estar como más o menos por ahí

**[1:07:21]** sin embargo

**[1:07:23]** yo no puedo hacer eso entre hombre y mujer

**[1:07:25]** entonces entre hombre y mujer

**[1:07:27]** no hay algo al medio

**[1:07:29]** bueno quizá hoy en día si no sé

**[1:07:31]** no quiero entrar en esos temas

**[1:07:33]** pero si estamos hablando de variables categóricas

**[1:07:35]** no deberían tener

**[1:07:37]** no se podrían interpolar

**[1:07:39]** entonces en este caso el gráfico de la izquierda

**[1:07:41]** es mejor

**[1:07:46]** algo que es súper útil

**[1:07:48]** cuando uno está haciendo clasificación

**[1:07:50]** y esto es súper importante

**[1:07:52]** clasificación es

**[1:07:54]** un gráfico de distribuciones

**[1:07:56]** para cada una de las clases

**[1:07:59]** entonces en este caso lo que estamos mostrando

**[1:08:01]** es la altura

**[1:08:03]** de las personas y tenemos las mujeres

**[1:08:05]** y los hombres

**[1:08:07]** entonces fíjense que hay dos distribuciones

**[1:08:09]** hombre y mujeres

**[1:08:11]** y estamos midiendo la altura tanto para los hombres como para las mujeres

**[1:08:13]** ¿Por qué este gráfico es tan importante?

**[1:08:16]** porque yo a través de este gráfico

**[1:08:18]** no más podría decir

**[1:08:20]** yo a través de la altura

**[1:08:22]** puedo clasificar a alguien

**[1:08:24]** entre hombre y mujer

**[1:08:27]** y entonces podría decir mirá si hay alguien con una altura de 62

**[1:08:33]** entonces lo más probable

**[1:08:35]** es que sea mujer

**[1:08:37]** y acá al medio

**[1:08:39]** es donde se complejiza un poco la cosa

**[1:08:42]** porque

**[1:08:44]** está como

**[1:08:46]** mitad y mitad

**[1:08:48]** pero

**[1:08:50]** una hipótesis de investigación

**[1:08:52]** súper importante que puedo sacar

**[1:08:54]** desde este gráfico

**[1:08:56]** hay peso

**[1:08:58]** perdón, dije altura

**[1:09:00]** no siento

**[1:09:02]** peso

**[1:09:04]** una hipótesis que puedo sacar

**[1:09:06]** pero lo importante de esto

**[1:09:08]** es que yo a partir del peso

**[1:09:10]** podría generar un modelo de clasificación

**[1:09:12]** entre hombre y mujer

**[1:09:15]** en este caso en particular no es muy útil

**[1:09:17]** pero esa es la idea

**[1:09:19]** o sea, si yo tengo varios de estos gráficos

**[1:09:21]** yo podría generar una hipótesis de investigación

**[1:09:23]** y decir

**[1:09:25]** estas variables sí me van a ayudar a clasificar

**[1:09:27]** vamos a hacer un gráfico

**[1:09:30]** vamos a hacer un ejemplo más delante

**[1:09:32]** tengo a cansar un poquito más rápido y de culto

**[1:09:34]** porque si no me alcanzará es lo que considero

**[1:09:36]** importante

**[1:09:38]** cuando tú tienes muchas variables

**[1:09:40]** lo que puedes hacer es lo que se llaman corner plots

**[1:09:42]** que son como gráficos de esquinas

**[1:09:44]** y lo que uno hace

**[1:09:46]** en este caso en particular tengo 3 variables

**[1:09:48]** tengo la variable m1, m2 y m3

**[1:09:50]** y lo que hago es que

**[1:09:52]** empiezo a generar gráficos en 2 dimensiones

**[1:09:54]** entre todas las variables

**[1:09:56]** entonces acá tengo la distribución de m1

**[1:09:58]** vs m3, acá m2 vs m3

**[1:10:00]** acá m1 vs m2

**[1:10:02]** y acá es generalmente

**[1:10:04]** lo que uno hace es que genera la distribución

**[1:10:06]** de cada variable por separado, entonces esta es la distribución

**[1:10:08]** de m3, si te fijan es m3 con m3

**[1:10:10]** entonces acá

**[1:10:12]** es la distribución solamente de m3

**[1:10:14]** acá la m2 y acá la m1

**[1:10:16]** esto te permite rabiamente

**[1:10:18]** entender las distribuciones

**[1:10:20]** las correlaciones entre las distintas clases

**[1:10:22]** entonces yo, perdón

**[1:10:24]** entre las distintas variables

**[1:10:26]** entonces por ejemplo acá yo podría ver

**[1:10:28]** que hay una anticorrelación

**[1:10:30]** entonces que a medida que yo voy aumentando m1

**[1:10:32]** bajando m2

**[1:10:34]** sin embargo a medida que yo voy aumentando m1

**[1:10:36]** va subiendo m3

**[1:10:39]** y a medida que yo voy aumentando m2

**[1:10:41]** va disminuyendo m3

**[1:10:43]** ok

**[1:10:47]** la matriz de correlación también es algo súper importante

**[1:10:49]** y básicamente

**[1:10:51]** lo que hago es que calculo correlaciones entre

**[1:10:53]** variables

**[1:10:55]** y lo agrego dentro de una matriz

**[1:10:57]** entonces este es el caso

**[1:10:59]** del dataset del titanic

**[1:11:01]** no sé si lo conocen pero es un dataset

**[1:11:03]** que van a jugar

**[1:11:05]** y que básicamente lo que te dice es

**[1:11:07]** tiene los datos de todos los pasajeros del titanic

**[1:11:09]** y dentro de eso

**[1:11:11]** tienen si que se murió o no se murió

**[1:11:13]** y tú tienes

**[1:11:15]** cosas como por ejemplo

**[1:11:17]** el tipo de pasajero

**[1:11:19]** primera clase, segunda clase, tercera clase

**[1:11:21]** el género, mujer

**[1:11:23]** y hombre, la edad

**[1:11:25]** el número de hermanos

**[1:11:27]** el número de padres

**[1:11:29]** y cuánto pagaron por su ticket

**[1:11:31]** ok

**[1:11:33]** entonces si yo miro esto

**[1:11:35]** y miro las correlaciones

**[1:11:37]** de inmediato no hay cuenta algo

**[1:11:39]** uno es muy correlado y menos uno

**[1:11:41]** es que tiene una correlación negativa

**[1:11:44]** entonces cosas que puedo ver rápidamente

**[1:11:46]** es que hay una, veamos

**[1:11:48]** quienes son los que más

**[1:11:50]** o los que hubiesen sobreivio

**[1:11:52]** entonces

**[1:11:54]** sexo

**[1:11:57]** tiene una correlación negativa

**[1:11:59]** de menos 54

**[1:12:01]** qué quiere decir este menos 54

**[1:12:03]** sé que cero es mujer

**[1:12:05]** y uno es hombre

**[1:12:08]** que sobrevieron más hombre o más mujer

**[1:12:12]** mujeres

**[1:12:14]** que sobrevieron más mujeres

**[1:12:18]** qué pasa

**[1:12:20]** sé que la correlación es positiva

**[1:12:22]** el valor del pasaje

**[1:12:24]** qué quiere decir

**[1:12:27]** mientras más caro era el pasaje

**[1:12:29]** más probable es sobrevivir

**[1:12:31]** entonces fíjense que eso

**[1:12:33]** tú lo podéis ver rápidamente

**[1:12:35]** en el gráfico no más

**[1:12:38]** fíjense también en esta correlación

**[1:12:40]** por ejemplo dado que vimos sexo

**[1:12:42]** y valor del pasaje es menos

**[1:12:44]** 0,18

**[1:12:46]** qué quiere decir eso

**[1:12:55]** es que es medio de 0,18 pero

**[1:12:57]** que las mujeres ponían el pago a más

**[1:12:59]** que en promedio

**[1:13:01]** las mujeres pagaron más que los hombres

**[1:13:03]** y acá podemos ver dos correlaciones grandes

**[1:13:05]** qué quieren decir estas dos correlaciones

**[1:13:07]** entonces tenemos acá

**[1:13:22]** el número de

**[1:13:24]** hermanos y esposas

**[1:13:26]** que están en el barco

**[1:13:28]** y parche el número

**[1:13:30]** de padres o hijos

**[1:13:32]** arriba del barco

**[1:13:35]** es más probable que

**[1:13:39]** también con los hijos

**[1:13:41]** claro

**[1:13:43]** entonces eran como grupos familiares

**[1:13:45]** los grupos familiares eran como de varios

**[1:13:47]** arriba del barco

**[1:13:50]** la matrita confusión es súper importante

**[1:13:52]** cuando uno quiere hacer por ejemplo regresión

**[1:13:54]** quiero predecir una variable

**[1:13:56]** numérica a partir de la otra variable

**[1:13:58]** puedo ver rápidamente qué variables

**[1:14:00]** tiene una correlación alta o baja

**[1:14:02]** y esa forma me ayudan a

**[1:14:04]** a calcular esto

**[1:14:06]** a generar un modelo

**[1:14:08]** de regresión que pudiese

**[1:14:10]** estimar la variable

**[1:14:12]** objetivo

**[1:14:16]** los box plots también son súper útiles

**[1:14:18]** ayudan a

**[1:14:20]** graficar variables

**[1:14:24]** valores para ciertas variables

**[1:14:26]** entonces por ejemplo acá

**[1:14:28]** yo tengo ciudades

**[1:14:30]** y esta es la temperatura

**[1:14:32]** cerca de la superficie para las distintas ciudades

**[1:14:34]** lo que hace un box plot

**[1:14:36]** es que grafica depende como usted lo usa

**[1:14:38]** en realidad lo pueden usar de distintas formas

**[1:14:40]** pero este es como en el clásico

**[1:14:42]** grafican una cajita

**[1:14:44]** y al medio ponen una línea

**[1:14:46]** la línea del medio

**[1:14:48]** que es la que está acá es la mediana

**[1:14:50]** la cajita

**[1:14:52]** te marca el cuartil 1

**[1:14:54]** o sea el presentil 25 y el 75

**[1:14:56]** y el bigote

**[1:14:58]** que se llama esto acá

**[1:15:00]** es 1,5

**[1:15:02]** por el rango intercuartil

**[1:15:04]** además los valores que salen

**[1:15:07]** fuera de este valor

**[1:15:09]** se grafican con puntitos como esto acá

**[1:15:11]** y esos son los valores anómalos

**[1:15:13]** entonces podemos ver que en Sydney

**[1:15:15]** por ejemplo la mediana

**[1:15:17]** de la temperatura es del orden de

**[1:15:19]** 18

**[1:15:21]** pero hay días muy calurosos

**[1:15:23]** que son estos acá

**[1:15:26]** mientras que el timbox 2

**[1:15:28]** la mediana es de 31

**[1:15:30]** más o menos

**[1:15:32]** y el rango intercuartil te llega hasta 40

**[1:15:34]** y 45

**[1:15:36]** creo

**[1:15:38]** entonces hace mucho más calor

**[1:15:40]** te ayuda a medir la distribución

**[1:15:42]** entonces tú puedes ver cuáles se parecen más a otros

**[1:15:44]** cuáles no

**[1:15:47]** bueno y para tendencias

**[1:15:49]** este es un gráfico de tendencias

**[1:15:51]** que hoy en día se usa mucho para

**[1:15:53]** ver si ese tipo de cosas

**[1:15:55]** mide como una variada le va cambiando en el tiempo

**[1:15:58]** ya quiero llegar

**[1:16:01]** a los ejemplos y acá me quiero detener un poco

**[1:16:03]** porque este es el tipo de cosas que yo espero que ustedes hagan

**[1:16:05]** en su análisis exploratorio

**[1:16:07]** que es lo primero que tienen que

**[1:16:09]** presentar en sus proyectos

**[1:16:11]** entonces le voy a dar dos ejemplos

**[1:16:14]** el primer ejemplo

**[1:16:16]** es de tipos de vinos

**[1:16:18]** tenemos un data set

**[1:16:20]** que son el resultado de un análisis químico de vinos

**[1:16:22]** cultivado en la misma región en Italia

**[1:16:24]** por tres cultivadores diferentes

**[1:16:26]** ya

**[1:16:28]** se toman 13 medidas diferentes

**[1:16:30]** para los diferentes componentes que se encuentran

**[1:16:32]** en los tres tipos de vinos

**[1:16:34]** entonces tenemos el cultivador cero

**[1:16:36]** el cultivador uno y el cultivador dos

**[1:16:38]** y los tres son como tres personas

**[1:16:40]** que fabrican vinos o tres empresas

**[1:16:42]** que fabrican vinos

**[1:16:44]** y nosotros medimos

**[1:16:46]** varias cosas dentro del vino

**[1:16:48]** imagínense

**[1:16:50]** que ustedes ponen una botella de vino al frente

**[1:16:52]** y tienen que probarla

**[1:16:54]** y decir de cual de los tres cultivadores

**[1:16:56]** es

**[1:16:58]** y seguramente yo no lo podría hacer

**[1:17:00]** no lo sé

**[1:17:02]** a lo mejor sí

**[1:17:04]** pero

**[1:17:06]** si ustedes tienen los datos

**[1:17:08]** a lo mejor podrían calcular los datos

**[1:17:10]** obtener los datos de esa copa de vino

**[1:17:12]** y a partir de eso generar un modelo predictivo

**[1:17:14]** que sea capaz de hacerlo

**[1:17:16]** entonces la pregunta es

**[1:17:18]** antes de generar el modelo predictivo

**[1:17:21]** tengo alguna certeza de que voy a poder

**[1:17:23]** generar algo de este estilo

**[1:17:25]** este modelo que desde el vino

**[1:17:27]** me estime

**[1:17:29]** quién es el cultivador

**[1:17:31]** de ese vino

**[1:17:33]** entonces lo primero que hago

**[1:17:35]** generalmente cuando una clasificación

**[1:17:37]** es calcular las distribuciones

**[1:17:39]** por distintos tipos de clases

**[1:17:41]** entonces en este caso tenemos cero

**[1:17:43]** uno y dos los distintos cultivadores

**[1:17:45]** y podemos ver que tenemos

**[1:17:47]** más datos del uno

**[1:17:49]** que del dos y que del cero

**[1:17:51]** y eso es importante porque los modelos tienden a

**[1:17:53]** sobreajustarse a los valores

**[1:17:55]** que son más representativos dentro de tu distribución

**[1:17:57]** acá lo que hice fue calcular

**[1:18:02]** la media, la eviación estándar

**[1:18:04]** el mínimo, el percentil 25

**[1:18:06]** el 50, el 75 y el máximo

**[1:18:08]** ok

**[1:18:11]** y entonces lo que puedo ver es que

**[1:18:13]** en principio el nivel de alcohol

**[1:18:15]** estos son para las distintas variables

**[1:18:17]** para las 13 variables

**[1:18:19]** entonces el

**[1:18:21]** nivel de alcohol tiene una media de

**[1:18:23]** 13, entonces como tiene

**[1:18:25]** en promedio 13 grados

**[1:18:27]** y la eviación estándar es de 0,8

**[1:18:29]** entonces ¿qué me está diciendo esto?

**[1:18:31]** me está diciendo que no sea

**[1:18:33]** leja, parece mucho

**[1:18:35]** del 13

**[1:18:37]** o sea es como puede ser 13,8

**[1:18:39]** o 12,2

**[1:18:41]** pero en promedio va a estar por ahí, cerca

**[1:18:43]** ahora ustedes podrían decir a él

**[1:18:45]** pero espera

**[1:18:48]** el rango, ¿dónde está esto?

**[1:18:50]** calculamos el percentil 25 y el 75

**[1:18:52]** y el percentil 50

**[1:18:54]** entonces veo que la mediana

**[1:18:56]** se parece a la media

**[1:18:58]** entonces al saber que la mediana se parece

**[1:19:00]** a la media, digo ah

**[1:19:02]** no hay colas grandes hacia un lado o hacia el otro

**[1:19:04]** se ve relativamente simétrica la distribución

**[1:19:06]** y el percentil 25

**[1:19:08]** y el 75 están

**[1:19:10]** más o menos a la misma distancia

**[1:19:12]** de la mediana, entonces es como ya

**[1:19:14]** una distribución simétrica

**[1:19:16]** ok, entonces

**[1:19:18]** yo podría seguir calculando esto para cada una

**[1:19:20]** de las variables y entonces puedo ir

**[1:19:22]** encontrando cada uno de los valores

**[1:19:24]** fíjense que acá ya se aleja

**[1:19:26]** en magnesio, entonces pareciera

**[1:19:28]** que en magnesio está un poquito corrido

**[1:19:30]** de la mediana

**[1:19:32]** y

**[1:19:34]** voy a ir al siguiente

**[1:19:36]** el percentil 50 acá

**[1:19:38]** está en 34 y esto es 36

**[1:19:40]** en non-flavanoid

**[1:19:42]** phenols, no sé qué es

**[1:19:44]** ok, pero

**[1:19:47]** fíjense en la intensidad del color

**[1:19:49]** la media está en 5,05

**[1:19:51]** y la mediana

**[1:19:53]** está en 4,69

**[1:19:55]** pareciera que como que se empieza

**[1:19:57]** que hay colores

**[1:19:59]** con valores más bajos

**[1:20:01]** ok, se entiende lo que estoy haciendo

**[1:20:04]** si, entonces a partir de esto

**[1:20:06]** calculando solamente promedio

**[1:20:08]** media de piano, puedo

**[1:20:10]** entenderle

**[1:20:12]** qué tipo de datos son los que yo tengo

**[1:20:14]** acá lo que estoy graficando

**[1:20:17]** es en el eje x el alcohol

**[1:20:19]** y en el eje y

**[1:20:21]** la frecuencia

**[1:20:23]** y entonces tengo un histograma

**[1:20:25]** pero lo estoy haciendo patre

**[1:20:27]** para los tres cultivadores distintos

**[1:20:30]** y fíjense que acá yo del primer gráfico

**[1:20:32]** obtengo algo rápidamente

**[1:20:34]** se le ocurre que es lo que estoy viendo

**[1:20:36]** que ven usted así directo

**[1:20:38]** el primer gráfico

**[1:20:40]** que el cultivador 1 suele hacer vinos

**[1:20:42]** con menor gradación alcohólica

**[1:20:44]** el cultivador 1

**[1:20:46]** vinos con menor gradación alcohólica

**[1:20:48]** entonces...

**[1:20:50]** pero que no puede diferenciar entre el 0 y el 2

**[1:20:52]** al menos no con el alcohol

**[1:20:55]** claro, pero esto quiere decir

**[1:20:57]** que si yo tengo un vino

**[1:20:59]** un vino nuevo y me piden clasificar de dónde viene

**[1:21:01]** yo puedo medirle el niel de alcohol

**[1:21:03]** imagínense que yo fuese muy bueno

**[1:21:05]** para medir el niel de alcohol en mi boca

**[1:21:07]** lo puedo sentir el niel de alcohol en mi boca

**[1:21:09]** y diría ah, es un niel de alcohol de 11,5

**[1:21:11]** está entre 11 y 12

**[1:21:13]** tiene que ser del cultivador 1

**[1:21:15]** es cierto?

**[1:21:17]** entonces esto es lo que me está diciendo

**[1:21:19]** es el niel de alcohol ya me ayuda

**[1:21:21]** a clasificar entre distintos v

**[1:21:23]** ok?

**[1:21:26]** en el gráfico de la derecha, Kevin

**[1:21:32]** déjenme preguntarle a alguien distinto

**[1:21:34]** Luis

**[1:21:41]** que veo en el

**[1:21:43]** 2

**[1:21:46]** menor 0 y el 1

**[1:21:48]** se parecen

**[1:21:50]** ya el 12

**[1:21:52]** tiene una distribución diferente

**[1:21:54]** claro

**[1:21:58]** eso es como principal

**[1:22:00]** entonces pareciera

**[1:22:02]** que yo podría usar estas dos variables

**[1:22:04]** y con estas dos variables ya puedo distinguirlas

**[1:22:06]** porque sé que yo tengo

**[1:22:09]** un

**[1:22:11]** malic acid, no sé qué es lo que es

**[1:22:13]** alguien de saber acá pero yo no

**[1:22:15]** de valor 4

**[1:22:17]** y tengo un niel de alcohol

**[1:22:19]** de 13,5

**[1:22:21]** lo más probable es que sea

**[1:22:23]** del cultivador 2

**[1:22:25]** entonces esto fíjense que

**[1:22:28]** con esto yo ya puedo generar una hipótesis

**[1:22:30]** y mi hipótesis acá

**[1:22:32]** es a partir de estas dos variables

**[1:22:34]** ya puedo clasificar

**[1:22:36]** la procedencia del vino

**[1:22:39]** y esa es una hipótesis de clasificación

**[1:22:42]** porque estoy clasificando

**[1:22:44]** estoy buscando la clase

**[1:22:46]** a la cual pertenece el vino

**[1:22:48]** ahora yo podría decir

**[1:22:51]** vamos un poquito más allá

**[1:22:53]** ya que hagamos un gráfico en 2 dimensiones

**[1:22:55]** entonces son exactamente los mismos valores

**[1:22:57]** de la clasificación

**[1:22:59]** el morado

**[1:23:01]** el cultivador 0

**[1:23:03]** el verde el 1

**[1:23:05]** y el amarillo el 2

**[1:23:08]** y fíjense que acá es mucho más claro

**[1:23:10]** y puedo decir, claramente puedo hacer una clasificación

**[1:23:12]** o sea es cosa que

**[1:23:14]** dibuje acá un circulito

**[1:23:16]** y todo esto

**[1:23:18]** viene de procedencia 2

**[1:23:20]** todo esto acá

**[1:23:22]** viene de procedencia 1

**[1:23:24]** y todo esto acá viene de procedencia 0

**[1:23:26]** pero con esto yo ya digo si

**[1:23:28]** voy a ser capaz de clasificar

**[1:23:30]** no a ser perfecto

**[1:23:32]** porque ningún modelo es perfecto nunca

**[1:23:34]** pero al menos soy capaz de clasificar

**[1:23:38]** vamos a otro ejemplo

**[1:23:40]** ejemplo 2, obesidad

**[1:23:43]** voy a leerlo, este conjunto de datos

**[1:23:45]** incluye datos sobre la dieta

**[1:23:47]** la actividad física

**[1:23:49]** y el peso de los adultos

**[1:23:51]** del sistema de vigilancia de factores

**[1:23:53]** de riesgo conductual

**[1:23:55]** estos datos se utilizan para la base de datos

**[1:23:57]** de datos

**[1:24:06]** estos datos se utilizan

**[1:24:08]** para la base de datos, tendencia y mapas

**[1:24:10]** de DNPAO que proporciona datos

**[1:24:12]** nacionales y estatales específicos sobre

**[1:24:14]** obesidad, nutrición, actividad física y lactancia

**[1:24:16]** y este data se lo saqué acá

**[1:24:18]** de Kaggle, ahí está el link

**[1:24:21]** entonces

**[1:24:23]** vamos a hablar ahora de taza obesidad

**[1:24:25]** imaginemos que yo quisiera

**[1:24:27]** predecir la taza obesidad

**[1:24:29]** ahora yo lo primero que hago

**[1:24:31]** es hago un histograma

**[1:24:33]** el histograma me muestra acá

**[1:24:35]** que la taza obesidad que el porcentaje

**[1:24:37]** de

**[1:24:40]** adultos

**[1:24:42]** obesos

**[1:24:44]** la mayoría

**[1:24:46]** está bajo

**[1:24:48]** el 70%

**[1:24:50]** si yo veo esta

**[1:24:53]** distribución primero veo que es asimétrica

**[1:24:55]** entonces hay un

**[1:24:57]** bajo número de personas muy obesas

**[1:24:59]** y hay

**[1:25:01]** un número de personas no obesas

**[1:25:03]** o eso

**[1:25:05]** sobre 30 o 40

**[1:25:07]** entonces con esto

**[1:25:09]** yo ya puedo ver más o menos cómo se comporta

**[1:25:11]** la variable

**[1:25:14]** me quedan 5 minutos

**[1:25:16]** pero lo otro que yo puedo ver

**[1:25:18]** son este tipo gráfico y acá lo que estoy

**[1:25:20]** viendo es

**[1:25:22]** estos son datos de estadounidense

**[1:25:24]** y entonces lo que estamos viendo

**[1:25:26]** es para cada uno de los estados

**[1:25:28]** cómo se comporta

**[1:25:30]** el rango obesidad

**[1:25:32]** estos son los 10 menos obesos

**[1:25:34]** y estos son los 10 más obesos

**[1:25:36]** y esto acá lo que está

**[1:25:38]** mostrando es la mediana

**[1:25:40]** entonces básicamente lo que estoy diciendo

**[1:25:42]** es hay estados

**[1:25:44]** donde hay mayor obesidad

**[1:25:46]** que en otros estados

**[1:25:50]** entonces si yo quiero

**[1:25:52]** por ejemplo

**[1:25:54]** calcular la taza obesidad

**[1:25:56]** dentro de un barrio

**[1:25:58]** quiero predecir la taza obesidad

**[1:26:00]** dentro de un barrio

**[1:26:02]** verdamente cuál es el estado

**[1:26:05]** ok

**[1:26:08]** lo otro que uno puede ver es la cantidad de

**[1:26:10]** income

**[1:26:12]** el ingreso

**[1:26:14]** el ingreso anual familiar

**[1:26:16]** y uno puede ver

**[1:26:18]** que dependiendo de cuánto

**[1:26:20]** cuánto dinero ingresa a la casa

**[1:26:22]** cómo impacta eso

**[1:26:24]** en la taza obesidad

**[1:26:26]** y se ve rápidamente

**[1:26:28]** que la gente que tiene menor ingreso

**[1:26:30]** son las que tienen mayor taza

**[1:26:32]** obesidad

**[1:26:34]** entonces con esto yo ya puedo decir

**[1:26:36]** si yo quiero calcular la taza

**[1:26:38]** obesidad de algún barrio o de alguna

**[1:26:40]** región puedo calcular

**[1:26:42]** por ejemplo los ingresos promedios

**[1:26:44]** de esas regiones

**[1:26:46]** y puedo calcular

**[1:26:48]** en qué estado está

**[1:26:50]** y con eso ya puedo de alguna forma

**[1:26:52]** estimar la taza obesidad

**[1:26:56]** ¿se entienden? este es el tipo

**[1:26:58]** de análisis que yo quiero

**[1:27:00]** que ustedes hagan para

**[1:27:02]** la presentación

**[1:27:04]** de la primera entrega de su proyecto

**[1:27:06]** eso

**[1:27:10]** ¿no sé si tienen alguna pregunta?

**[1:27:17]** ok

**[1:27:20]** entonces lo dejamos hasta acá

**[1:27:22]** y nos vemos

**[1:27:26]** ¿sí?

**[1:27:28]** ¿cómo? no escuché

**[1:27:30]** ¿sería posible contar con este material

**[1:27:32]** si

**[1:27:35]** lo voy a subir

**[1:27:38]** de hecho terminamos la clase

**[1:27:40]** y lo voy a subir

**[1:27:43]** yo tengo una pregunta sobre el certamen

**[1:27:46]** eso es la próxima semana

**[1:27:48]** eso va a ser

**[1:27:50]** durante la hora de clase

**[1:27:52]** o durante el día o como funciona

**[1:27:54]** durante la hora de clase

**[1:27:56]** empieza la serie cuarto

**[1:27:58]** el certamen a esa hora se abre

**[1:28:00]** y termina a las nueve

**[1:28:03]** entonces yo lo que les decía la otra vez

**[1:28:05]** es que

**[1:28:07]** son tres preguntas

**[1:28:11]** son tres conjuntos de preguntas

**[1:28:13]** una es verdadero falso

**[1:28:15]** con justificación

**[1:28:17]** la otra es de selección múltiple

**[1:28:19]** y la otra es algo que ya van a tener

**[1:28:21]** que ser de esa forma

**[1:28:23]** una perrita acá

**[1:28:25]** de unos minutos

**[1:28:29]** el certamen

**[1:28:42]** el certamen se hace por

**[1:28:46]** campas

**[1:28:48]** y se abre

**[1:28:50]** a las seis cuartos

**[1:28:52]** yo voy a estar acá con usted a las seis cuartos

**[1:28:54]** entonces si calienten algún problema

**[1:28:56]** lo que sea lo vamos a resolver

**[1:28:58]** tienen que tener las cámaras prendidas

**[1:29:02]** eso es importante durante el certamen

**[1:29:04]** nada más

**[1:29:12]** profesor consulta ese certamen va a ser más que nada teórico

**[1:29:14]** si, es solamente

**[1:29:19]** las clases teóricas

**[1:29:21]** entonces con ver las clases

**[1:29:24]** bastaría

**[1:29:26]** si

**[1:29:29]** la idea del curso es que el certamen

**[1:29:31]** evalúa las clases teóricas

**[1:29:33]** y el proyecto evalúa la parte más práctica

**[1:29:35]** Caden

**[1:29:39]** yo tengo una pregunta

**[1:29:42]** respecto al proyecto

**[1:29:44]** no estoy seguro

**[1:29:46]** pero al menos en campas

**[1:29:48]** no vi quizás

**[1:29:50]** cuáles son los lineamientos del proyecto

**[1:29:52]** los temas

**[1:29:56]** quizá estaría bueno

**[1:29:58]** que nos comentaran algo

**[1:30:02]** eso le había comentado al principio

**[1:30:04]** la clase

**[1:30:06]** la primera parte del proyecto

**[1:30:08]** es la situación con el análisis exploratorio

**[1:30:10]** entonces no lo había subido

**[1:30:12]** hasta que pasara esta clase

**[1:30:14]** pero ahora le voy a subir

**[1:30:16]** los lineamientos del proyecto

**[1:30:18]** y como les decía

**[1:30:20]** una cosa importante

**[1:30:22]** de los proyectos es que idealmente

**[1:30:24]** trabajen con datos

**[1:30:26]** que a ustedes les sirvan

**[1:30:28]** que después esto que vayan a hacer

**[1:30:30]** durante el proyecto lo vayan a extender

**[1:30:32]** durante las siguientes clases

**[1:30:34]** en los siguientes cursos

**[1:30:36]** lo vayan en su que hacer diario

**[1:30:39]** igual

**[1:30:41]** si que

**[1:30:43]** no tienen un dataset

**[1:30:45]** todavía no tienen claro que van a hacer

**[1:30:47]** más adelante

**[1:30:49]** tenemos un puñado de dataset

**[1:30:51]** que le vamos a pasar

**[1:30:53]** para que ustedes puedan trabajar con ellos

**[1:30:56]** perfecto y esto es individual o es grupal?

**[1:30:59]** es

**[1:31:03]** una buena pregunta

**[1:31:06]** todavía no está definido

**[1:31:09]** digamos así

**[1:31:12]** tiene una relación con cuántos alumnos

**[1:31:14]** son en el curso

**[1:31:16]** hay presentaciones orales

**[1:31:18]** y si son muchos alumnos

**[1:31:20]** necesitamos que

**[1:31:22]** pero si no puede ser indivíduo

**[1:31:24]** en todo caso

**[1:31:27]** una cosa que les dije en un principio

**[1:31:29]** es que si por alguna razón

**[1:31:31]** ustedes tienen

**[1:31:33]** algún problema

**[1:31:35]** para compartir los datos

**[1:31:37]** porque son exactamente

**[1:31:39]** o tienen problemas de privacidad

**[1:31:41]** o cosas de ese estilo

**[1:31:43]** o de

**[1:31:45]** que son estratégicos para el negocio

**[1:31:47]** donde ustedes trabajan

**[1:31:49]** entonces pueden hacerlo de manera individual

**[1:31:51]** y no hay problema pero me lo tienen que decir

**[1:31:53]** pero todo eso va a estar en la instrucción

**[1:31:55]** en que le voy a subir esta semana

**[1:31:58]** vale muchas gracias

**[1:32:09]** estamos entonces

**[1:32:12]** nos vemos que estén bien

**[1:32:16]** igual profesor
