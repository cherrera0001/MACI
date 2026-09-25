# 2026-08-07T23_57_03Z Fundamentos en Ciencia de Datos.mp4

> Transcripcion automatica con faster-whisper. **Puede contener errores**,
> sobre todo en terminos tecnicos y nombres propios. Contrastar con el
> material del curso antes de citarla como fuente.

- Duracion: 1:46:07
- Modelo: `small` · idioma detectado: `es` (confianza 1.00)

---

**[0:03:23]** Hola, ¿cómo estás? Bien, bien, ¿ustedes?

**[0:03:27]** Bien, también.

**[0:03:29]** Hola.

**[0:03:30]** Hola.

**[0:03:33]** ¡Tututututututututututututututututututututu!

**[0:03:39]** Ay, ¿cómo estás?

**[0:03:48]** ¿Cómo estás? Ahí estoy yo.

**[0:04:00]** Y voy a compartir...

**[0:04:02]** Ay, ya, ¿cómo le fue en la clase?

**[0:04:07]** Tú buena.

**[0:04:08]** Supe.

**[0:04:10]** Un poco difícil, pero bueno.

**[0:04:12]** Súper. Bueno, ¿te supone que ahora repasamos igual contenidos que vieron en clase?

**[0:04:17]** así que si es que algo quedó pendiente, igual lo podemos ver de nuevo, voy a compartir pantalla

**[0:04:29]** que es esto, voy a sacar esto porque si no lo me ven, y esto no lo saco, interesante, ya aquí

**[0:04:44]** tengo la clase de regresión y nos habíamos quedado en regresión polinomial sino mal

**[0:04:55]** no habíamos quedado, no habíamos quedado hasta aquí, bueno habíamos hablado de validación cruzada,

**[0:05:02]** ah creo que si, porque hablamos de un poco el sobreajuste y nos quedamos en esta imagen creo,

**[0:05:07]** ya pero partamos de aquí, la voy a ejecutar todas las anteriores por mientras, ya entonces

**[0:05:17]** porque estoy partiendo de regresión y no de clasificación que es la materia que vieron porque

**[0:05:21]** nos quedó un cachito del laboratorio de regresión pendiente de la clase pasada,

**[0:05:27]** yo ya subí esta respuesta la subí ayer, también lo de clasificación tanto vacío como respuesta

**[0:05:33]** también está subiendo en el campo, ya entonces habíamos estado hablando de regresión y que

**[0:05:40]** la regresión es básicamente cuando yo quiero entrenar un vapeo de variables a una etiqueta

**[0:05:49]** y en especial cuando yo quiero entrenar este mapa de variables de etiqueta y este etiqueta es un número,

**[0:05:58]** no es una clase, un valor, esto se llama regresión y habíamos visto cómo funcionaba la regresión

**[0:06:05]** lineal, no siento la fórmula que tenía internamente y nos dimos cuenta que a veces puede ser que lo

**[0:06:11]** que necesitemos no sea algo lineal con respecto a la variable pero sí lineal con respecto a los

**[0:06:18]** parámetros, entonces podíamos tener este truco cuando teníamos, cuando utilizamos por ejemplo una

**[0:06:24]** transformación, no es cierto esta transformación G, lo voy a hacer más grande, técnicamente es una

**[0:06:33]** regresión lineal con transformación polinomial, ¿por qué? porque los parámetros siguen siendo

**[0:06:38]** lineales, no es cierto, pero me pasa que la regresión lineal puede modelar relaciones lineales

**[0:06:47]** entre las variables de entrada y salida pero yo puedo hacer una transformación que es no lineal con

**[0:06:53]** respecto a X, entonces yo voy a transformar no linealmente la entrada, entonces eso es lo que

**[0:07:00]** hacíamos con la regresión polinomial, ¿no es cierto? nosotros ocupábamos una función de la

**[0:07:09]** librería que se llama polinomial features para elevar todas las variables a distintos

**[0:07:17]** grados de no sea elevar a 0, elevar a 1 y hasta así hasta el grado que yo escoja y luego esto como

**[0:07:24]** que lo pegaba con pegamento la salía de esto con la entrada de la regresión lineal y me creaba mi

**[0:07:30]** propia regresión polinomial a mal y podíamos hacer cosas como éstas, por ejemplo, ¿no es cierto?

**[0:07:35]** dado el grado del polinomio que está detrás de esta regresión polinomial, nosotros podíamos

**[0:07:43]** ir viendo cómo se ajustaba a unos datos de juguetes que nosotros habíamos hecho, entonces habíamos

**[0:07:50]** dicho que teníamos la situación de no saber qué grado es coger porque si es que aumentábamos el grado

**[0:08:00]** aquí visualmente en este gráfico si es que aumentábamos el grado entonces era mejor el ajuste

**[0:08:06]** nosotros podríamos decir bueno entonces entre más grande el grado siempre va a ser mejor el

**[0:08:11]** ajuste para mis datos pero eso no es tan así y tenemos que entender cuándo el ajuste deja de

**[0:08:17]** ser bueno y cómo hacemos eso y para eso mencionábamos bueno el prefe de haberme mencionado más en la

**[0:08:26]** clase que son los conceptos de sesgo y varianza y para eso necesito tener un conjunto de validación

**[0:08:33]** entonces nosotros agregaba primero veíamos ajustábamos distintos modelos y veíamos el

**[0:08:39]** error dado el conjunto de entrenamiento entonces calculamos nuestras dos métricas de error que

**[0:08:45]** ya habíamos visto que eran el mc y el r cuadrado dado este ajuste con respecto al conjunto de entrenamiento

**[0:08:52]** entonces aquí teníamos un polinomio de grado 4 de grado 7 de grado 10 y de grado 13 y veíamos

**[0:08:59]** que todos tenían bueno desde el grado 7 en adelante todos tenían un r cuadrado bastante

**[0:09:06]** alto casi cercano a uno el grado 13 se equivocaba un poquito y un mc bastante bajo pero por ejemplo el

**[0:09:11]** grado 7 y el grado 10 tenían las mismas métricas en entrenamiento sea que el ajuste por los puntos

**[0:09:18]** que yo estaba ocupando para entrenar era muy bueno pero qué pasaba visualmente con el grado 10 yo

**[0:09:23]** me doy cuenta que yo sé cuál es la tendencia real no es cierto que siguen los datos porque yo

**[0:09:29]** los muestre a tener una forma así entonces cuando veo el ajuste el grado 10 sé que en

**[0:09:33]** otros datos que el modelo no ha visto el modelo no va a poder generalizar no va a poder predecir

**[0:09:38]** bien para esos datos entonces cómo puedo saber esto desde antes sin tener que visualizar porque de repente

**[0:09:45]** no va a ser tan fácil o yo no voy a conocer realmente esta tendencia de los datos que hay por detrás

**[0:09:50]** entonces ahí decíamos que necesitamos agregar nuestro conjunto de validación no me acuerdo

**[0:09:57]** no me acuerdo cuando dije de que no me quede adecuera

**[0:10:06]** entonces lo que hacíamos es agregar un conjunto de validación había unos puntitos extra que yo me los

**[0:10:12]** había guardado y no los había ocupado para entrenar que son estos puntitos que están un poco

**[0:10:16]** más opacos y eso lo voy a ocupar de conjunto de validación entonces que voy a hacer voy a

**[0:10:21]** escoger mi polinomio lo voy a entrenar ocupando los datos que están más oscuros y con los

**[0:10:27]** datos que tienen menos opacidad voy a evaluar mi ajuste a esos datos que sería voy a evaluar

**[0:10:35]** mi ajuste en el conjunto de validación y evaluando el conjunto de validación nos damos cuenta que

**[0:10:40]** podemos ver con las métricas ya no tenemos que verlo visual podemos verlo con las métricas que

**[0:10:44]** el modelo que mejor se ajusta para estos datos es el grado 7 porque porque visualmente vemos

**[0:10:50]** que sigue la tendencia real que sabemos que está por detrás de los datos y aquí

**[0:10:55]** podemos cuantificar entonces necesitamos este conjunto de validación cuando tenemos estos

**[0:11:03]** hiperparámetros ok son parámetros pero que no se ajustan con los datos nosotros tenemos que

**[0:11:09]** tomar esta decisión antes de empezar a entrenar tenemos que escoger sus valores antes de empezar

**[0:11:13]** a entrenar o sea no dependen de los datos no los podemos ajustar en el entrenamiento de

**[0:11:18]** los dos entonces para eso nos sirve nuestro conjunto de validación y entonces podríamos

**[0:11:24]** decir que queríamos realizar validación cruzada y podríamos ocupar una herramienta y ocupando

**[0:11:30]** el método de cáfora y aquí están los las definiciones de los tres conjuntos de datos entonces

**[0:11:38]** al final yo voy a tener tres que sería el conjunto de entrenamiento con el que entrenó los parámetros

**[0:11:43]** internos del modelo no es cierto el conjunto de validación con el que yo voy a ocupar para

**[0:11:48]** ajustar los hiperparámetros ok y el conjunto de prueba que es el conjunto ya final que

**[0:11:55]** yo ocupo para evaluar que también lo hace el modelo en datos que no ha visto ya y hay un método que

**[0:12:03]** también lo puedo ocupar si es que no si es que no tengo un poco de datos de entrenamiento que se

**[0:12:06]** llamaba cáfor ya y esto hacía una división especial yo tengo todos mis datos y primero los divido

**[0:12:17]** una consulta cómo sabes qué porcentaje o qué tipo de de set de datos hubas para el entrenamiento

**[0:12:30]** para la aleación y para el test no tú tienes el conjunto de datos como voy a decir invento tengo

**[0:12:35]** 10 mil cuánto y cómo escojo cada uno de los tres set de datos pensando en llevarlo a lo práctico

**[0:12:43]** como cómo me doy cuenta cómo lo hago que hubo alguna metodología como lo hace que yo quiero

**[0:12:50]** hacer sampling normalmente se hace de manera aleatoria porque porque técnicamente aleatoriamente

**[0:12:56]** porque yo no puedo querer buscar cuál es el mejor conjunto de datos para entrenar necesito que

**[0:13:01]** él si yo tengo un conjunto de datos si lo sacó aleatorio se supone que siguiendo la aleatoria

**[0:13:06]** datos deberían seguir la misma distribución de datos ok si es que yo tuviera clases

**[0:13:11]** lo ideal sería mantener las proporciones de clases por ejemplo en todos los conjuntos para

**[0:13:20]** evaluar cada clase tal como se comporta no es esto porque si es que tengo en el conjunto de test por

**[0:13:26]** ejemplo tengo datos de perros gatos unicornios y en el conjunto de test no tengo datos de unicornios

**[0:13:33]** no voy a estar evaluando para todas las clases entonces es algo que me tengo que fijar por

**[0:13:37]** ejemplo por clases pero normalmente lo que uno hace es dividir aleatoriamente y en términos de

**[0:13:44]** porcentaje no hay como una regla escrita pero algo como lo que el ecosistema ocupó mucho el 80 20

**[0:13:52]** normalmente un porcentaje así 30 por ciento máximo para ocupar para testear o validar porque

**[0:14:01]** si no sacó mucho datos de entrenamiento que me pueden ser útiles para seguir ajustando el

**[0:14:05]** mucho gracias gracias a ti ya entonces siguiendo con el método del café yo tengo mis datos y los voy

**[0:14:17]** a dividir en dos en los datos de entrenamiento y los datos de test y luego lo que voy a hacer es

**[0:14:23]** definir un k también se podría considerar yo lo tengo que definir antes entonces vamos a

**[0:14:29]** asumir que este k es 5 que significa esto que los datos de entrenamiento se van a dividir

**[0:14:35]** en cinco pedacitos cinco pedacitos y de igual tamaño y lo que voy a hacer es entrenar cinco

**[0:14:42]** veces van a ser cinco instancias de modelo distintas entonces en el primer entrenamiento lo

**[0:14:49]** que voy a hacer es ocupar el primer fold o el primer pedacito para validación y los otros cuatro

**[0:14:56]** pedacitos los voy a ocupar para entrenar la segunda vez que entrene voy a ocupar el segundo

**[0:15:02]** pedazo para validar y todos los demás para entrenar y la tercera vez que entrene voy a ocupar el tercer

**[0:15:08]** pedacito para validar y todo lo demás para entrenar y así hasta que haya ocupado cada uno de los

**[0:15:13]** pedacitos para validar en un entrenamiento y el test no se toca y se ocupa para hacer una

**[0:15:22]** evaluación final entonces para realizar validación cruzada necesito definir qué

**[0:15:28]** hiperparámetros voy a ajustar y qué valores van a tomar los hiperparámetros entonces esto este

**[0:15:36]** este proceso de entrenar varias veces de escoger cada pedacito ya se ya está automático en

**[0:15:44]** cycling learning entonces nosotros podemos llegar y ocuparlo y funciona parecido a cómo funciona

**[0:15:49]** cuando entrenamos un modelo entonces lo primero que voy a hacer aquí para poder ocuparlo de

**[0:15:55]** forma ordenada es que mi método de regresión polinomial yo lo tenía escrito como una función pero

**[0:16:05]** para que me funcione bien yo necesito escribirlo como una clase así que lo único que estoy definiendo

**[0:16:09]** aquí es la regresión polinomial que ya conocíamos que es aquí con el make pay pipeline del pegamento

**[0:16:16]** entre polinomial features y línea regresión todo eso lo estoy definiendo como una clase

**[0:16:21]** pero no es nada de nada distinto lo que vimos antes de código solamente que le estoy diciendo que es

**[0:16:26]** una clase y le estoy definiendo sus distintos métodos entonces antes de realizar validación cruzada que

**[0:16:34]** necesito necesito saber qué voy a ajustar y los valores que voy a probar entonces nosotros al definir

**[0:16:41]** nuestra clase de regresión polinomial decimos que vamos a ajustar un parámetro en este

**[0:16:47]** caso va a ser el grado y se dan cuenta el grado existe aquí como parámetro o hiperparámetro de esta

**[0:16:54]** clase se llama grado entonces lo primero que tengo que saber es qué modelo estoy ocupando y cuáles son

**[0:17:01]** sus hiperparámetros que ustedes no se lo saben pueden ir a la documentación de la librería y

**[0:17:07]** ahí buscar cómo se llaman y qué valores pueden tener entonces en este caso nosotros queremos

**[0:17:14]** ocupar el grado y sabemos que el grado puede ser un número y queremos probar por ejemplo 4 7 10 y 13 por

**[0:17:21]** por poner y aquí yo puedo tengo dos maneras si es que yo ya tengo datos de validación definidos o si

**[0:17:32]** es que quiero ocupar el método de cafol y simplemente y simplemente definir conjunto de

**[0:17:37]** entrenamiento y test y que la validación se haga se saque sola de si es que yo ya tengo

**[0:17:44]** datos de validación definidos de antes simplemente por ejemplo ponga que yo ya tengo mi x que serían

**[0:17:56]** mis datos de entrenamiento y mi x extra que serían mis datos de validación lo que voy a hacer es juntarlos

**[0:18:02]** ok en un mismo arreglo primero lo tengo que juntar porque se lo tengo que pasar todos juntos y lo

**[0:18:10]** único que va a distinguir si algo es de entrenamiento o de validación es un índice que van a tener

**[0:18:16]** entonces voy a crear un índice que las primeras x posiciones que sería la cantidad del conjunto

**[0:18:25]** de entrenamiento tengan un menos uno y que luego las posiciones que debería estar el conjunto de

**[0:18:30]** validación tengan un c y esto se lo voy a pasar a una función que está aquí de model

**[0:18:36]** selección de scikit-learn que se llama predefined split y le voy a pasar test fault igual a split

**[0:18:43]** index y lo único que está haciendo esto es que se está creando un índice interno para saber

**[0:18:49]** dónde está en dónde están los datos que son de entrenamiento y donde están los datos que son

**[0:18:54]** de validación aquí entonces cómo ocupo este procedimiento para que haga todo esto para

**[0:19:03]** que entrene varias veces etcétera ya o para que entrene varias veces por cada configuración de

**[0:19:13]** parámetros para saber qué parámetros mejor entonces lo que tengo que hacer es muy parecido a crear un

**[0:19:18]** modelo ok vamos a ocupar algo que se llama gritserge cv que también es de model de model selección

**[0:19:25]** de scikit-learn entonces nosotros primero vamos a crear como cuando creamos la instancia de

**[0:19:30]** un modelo que nos vamos a guardar nuestro gritserge cv instanciando lo primero pero ahora ya no

**[0:19:37]** podemos ocupar los parámetros por defecto tenemos que pasarle valores y lo primero es que le vamos

**[0:19:41]** a pasar el modelo y hasta aquí creo mi instancia de modelo con todos los parámetros por defecto

**[0:19:48]** aquí aquí no ponemos nada se lo paso tal cual que yo estoy ocupando regresión polinomial

**[0:19:53]** regresión polinomial si es que estoy ocupando un random forest le pasa un random forest y

**[0:19:57]** así dependiendo del modelo que yo quiero ajuste después le paso el diccionario de los parámetros

**[0:20:03]** de los hiperparámetros que yo quiero ajustar y los valores donde está definido lo definimos acá

**[0:20:08]** arriba y se dan cuenta el único hiperparámetro que quería ajustar era el grado y están los

**[0:20:12]** valores que tiene que probar luego aquí de que ocupar a caffle tendría que pasarle un

**[0:20:18]** número sino como tengo mi conjunto de validación predefinido tengo que pasarle este objeto

**[0:20:24]** predefined split que ya creamos aquí en scoring tendría que explicarle cuál es la métrica que a mí

**[0:20:31]** me interesa para evaluar qué modelo es mejor que otro y un verbos que esto es para decir cuánto me

**[0:20:39]** habla el procedimiento si quiero que se calle creo que tengo para el 0 o 1 entonces yo quiero que

**[0:20:47]** me imprima todo lo que está pasando así que le doy un 3 y con esto creamos nuestra grilla

**[0:20:55]** y como funciona como modelo para que entrene todos los todos los entrenamientos que tiene

**[0:21:00]** que hacer internamente hay que hacerlo como si fuera un modelo cuando poníamos modelos punto fit bueno

**[0:21:05]** ahora vamos a poner el objeto de grilla un tofit y le pasamos los datos entonces si yo corro esto

**[0:21:16]** y acorde todo el anterior no es cierto si yo corro esto no se va a morar nada porque son

**[0:21:20]** poquitos y si se dan cuenta está fitiendo un solo fold para los cuatro candidatos porque

**[0:21:27]** ya no tiene que andar haciendo este proceso no tiene que andar definiendo que que saque

**[0:21:32]** conjunto de entrenamiento porque ya le definí o sea conjuntos de variación porque ya definí mi

**[0:21:37]** conjunto de validación entonces por cada combinación de modelo que yo quiero probar solo tienen

**[0:21:45]** que entrenar una vez entonces tiene que hacer un fold para los cuatro candidatos porque son

**[0:21:53]** cuatro candidatos porque yo solo quiero probar un hiperparámetro pero quiero probar cuatro valores

**[0:21:59]** entonces el primer entrenamiento va a ser la instancia del modelo pero que su grado sea 4 y se

**[0:22:06]** va a entrenar con lo que yo pase el segundo entrenamiento es lo mismo pero con grado 7 el

**[0:22:12]** tercero con grado 10 y el último con grado 13 y me está diciendo el score que saca que el score

**[0:22:18]** es la métrica que yo pase aquí y normalmente me da el tiempo y entonces si nos vamos dando cuenta

**[0:22:29]** que yo empezará de grados más bajos me daría cuenta que entre más aumento el grado así se le

**[0:22:34]** pongo grado 2 grado 3 grado 4 me daría cuenta que el ajuste se está haciendo mejor y después

**[0:22:40]** cuando ya me pasó del grado 7 que habíamos visto que era un buen fit un buen ajuste después me

**[0:22:47]** voy pasando el grado 7 y el ajuste empieza a empeorar y empeorar empeorar como vemos aquí que el grado

**[0:22:52]** 10 me da un score bajo y el grado 3 o sea un score que técnicamente bastante alto si no

**[0:22:58]** ramos el menos porque este es el negativo un score bastante alto del mc o sea un fit bastante

**[0:23:04]** malo y después aumenta el grado 13 y el fit muy muy grande no me sirve entonces si aquí hubiera

**[0:23:13]** mucho y yo me enredo un poco puedo simplemente obtener la combinación de parámetros que mejor

**[0:23:21]** se ajustó a los datos con y como accedó a eso tengo que poner la instancia de mi grilla debo ponerle

**[0:23:27]** punto best y un bajo params que un bajo y me da que el mejor modelo fue el de grado 7 con esto yo

**[0:23:37]** cojo los mejores parámetros pero no escojo el mejor modelo que ya está entrenado entonces

**[0:23:43]** como obtengo el modelo que ya está entrenado para yo llegar y ocuparlo tengo que acceder a la grilla y

**[0:23:48]** en vez de best params de parámetros tengo poner best estimator y bajo estimator y bajo y así obtengo

**[0:23:55]** esa instancia del modelo que es la mejor y que ya está entrenado y ya se ajustó entonces puedo

**[0:24:01]** llegar y ocuparla para predecir entonces yo aquí me lo guardé en esta variable que se llama

**[0:24:11]** mejor modelo o tomar datos me puedo crear un arrange para volar por aquí por ejemplo pero lo

**[0:24:19]** que voy a usar básicamente va a ser los datos de variación y voy a mostrar mi modelo ya ajustado

**[0:24:25]** a esos datos y ahí está el verdecito es mi modelo ya ajustado eso es utilizar variación

**[0:24:36]** cruzada y así yo no tengo que simplemente cojo los valores que yo quiero probar dejó que

**[0:24:43]** entrene todas las veces esto es como para hacer artos de entrenamiento de una que compare y después

**[0:24:49]** pedirle oye cuál fue el mejor bueno oye cuáles fueron los la combinación de parámetros que dio

**[0:24:54]** mejor resultado oye dame el mejor modelo qué pasa si es que yo no definí me con no tengo mi

**[0:25:02]** conjunto de variación definido sino que quiero ocupar el método de cafón bueno ocupamos la

**[0:25:08]** misma idea entonces tengo que tener mi conjunto de entrenamiento y test todo lo que necesito aquí

**[0:25:16]** como yo tengo entrenamiento y variación separados ahora los voy a juntar de nuevo pero si tengo

**[0:25:21]** solo el entrenamiento este paso y me lo salto entonces funciona muy parecido creo una instancia

**[0:25:28]** del modelo que quiero ajustar los distintos hiperparámetros tengo mi conjunto de entrenamiento

**[0:25:35]** y tengo que definir el número de fold este ca del café por defecto es cinco así que cinco es un buen

**[0:25:43]** número nosotros le vamos a poner tres tres fold y de nuevo volvemos a nuestra grilla veamos una

**[0:25:50]** instancia de la grilla como dije no la podemos dejar por defecto tenemos que pasarle el modelo

**[0:25:55]** nuestro diccionario con los hiperparámetros que queremos ajustar y los valores que queremos

**[0:26:01]** probar y en cb aquí ya no le vamos a pasar el los índices sino que le vamos a pasar el número

**[0:26:08]** de fold o sea aquí puede ser un tres un cinco uno ocho etcétera el scoring sigue siendo el mismo y el

**[0:26:15]** verbos también para que nos diga todo lo que está haciendo luego de crearnos la instancia de la

**[0:26:20]** grilla para que haga todos los entrenamientos tenemos que poner como si fuera un modelo punto

**[0:26:24]** fit y entre paréntesis pasarle los datos que us que tiene que usar para entrenarse

**[0:26:31]** voy a correr esto y esto igual no se demora tanto pero me está diciendo que son tres fold y tenemos

**[0:26:39]** cuatro candidatos entonces tenemos tres fold tengo solamente una un hiperparámetro pero quiero

**[0:26:46]** probarlo en cuatro valores entonces por cada modelo que yo quiero probar tengo que entrenar tres

**[0:26:52]** veces entonces por eso lo multiplico y me da dar que tengo que en realidad hacer doce doce

**[0:26:59]** entrenamientos que voy a hacer doce entrenamientos en total por eso esto se puede demorar un poquito

**[0:27:08]** más que yo tengo que probar hartos hiperparámetros entonces debería quizá para ver cuánto se

**[0:27:14]** demora ver cuánto se demora un entrenamiento y ahí escalar vamos a decir esto se puede demorar

**[0:27:19]** unos cinco minutos etcétera igual si no le pones verbos te va mostrando cuántos está

**[0:27:26]** demorando internamente ya entonces aquí me muestra por ejemplo los tres primeros entrenamientos que

**[0:27:34]** tiene que hacer para grado 4 los tres entrenamientos para grado 7 los tres entrenamientos para grado

**[0:27:41]** 10 y los tres entrenamientos para grado 13 entonces aquí debería sacar un promedio no

**[0:27:49]** cierto porque yo estoy sacando un fold pero técnicamente aquí estoy entrenando con distintos

**[0:27:57]** conjuntos de dato y validando con conjuntos de dato entonces estoy sacando básicamente la pérdida

**[0:28:01]** en promedio y de luego de eso saco cuál es el mejor estimado entonces por ejemplo aquí el grado 7

**[0:28:06]** lo hizo por aquí entonces luego le pido los mejores parámetros dado eso y el mejor el mejor modelo

**[0:28:17]** para aquí con los mejores parámetros cambió y fue el grado 4 quizás si hubiera probado con el

**[0:28:22]** grado 6 hubiera sido el grado 6 porque porque hay una parte de los datos que si yo les cojo como

**[0:28:29]** conjunto de validación mi grado 7 lo hace pésimo no tiene un buen ajuste justo para esos datos y luego

**[0:28:39]** tiene la misma lógica para sacar los mejores parámetros y también para el mejor modelo

**[0:28:44]** como dije cuando yo ya tengo el best estimator puedo llegar y predecir y ocupar ya hasta

**[0:28:55]** ahí lo que nos había quedado pendiente de la clase pasada que es cómo hacer validación cruzada

**[0:29:00]** se entiende alguna no solta si que ahí es indicador que negativo más negativo mejor

**[0:29:24]** tengo que fijarme en el valor absoluto porque es el mc si te acuerdas el mc mide que tanto me estoy

**[0:29:35]** equivocando al cuadrado entonces el valor que yo más quiero es cero si entonces este valor si es muy

**[0:29:46]** grande aunque sea negativo es muy grande el valor absoluto entonces significa que se está equivocando

**[0:29:51]** mucho entonces entre más cercano a cero mejor y ahí porque está negativo que hiciste porque

**[0:30:02]** está negativo porque el scoring en el grid search no no sé si habrá cambiado pero en la versión de

**[0:30:09]** en la versión de la que tenía creo que el año pasado no tenía mc positivo solamente tenía el

**[0:30:18]** negativo solamente por las médicas que tenía disponibles en este caso se lo tenía disponible

**[0:30:25]** y ya entonces si quedó esto listo acá abajo hay un ejercicio que lo pueden hacer después después

**[0:30:41]** ahora no para pasar por la parte de clasificación pero ya está la respuesta ya la subí más aquí

**[0:30:47]** debería estar porque este es el notebook de respuesta ahora me cambio de notebook y voy al otro ya

**[0:30:56]** cambios de contenido y ahora deberíamos ver el contenido que ya habían visto en clase que es

**[0:31:01]** clasificación entonces cuando hablamos de clasificación el primer desafío con el que nos encontramos es

**[0:31:13]** que nuestros valores ya no son numéricos tenemos strings por ejemplo tenemos caracteres tenemos

**[0:31:20]** palabras y si nosotros tratáramos de entrenar un modelo con esos datos tal cual tendríamos

**[0:31:27]** un problema el modelo nos daría error porque porque no entiende esos datos no entiende palabras

**[0:31:33]** entonces tenemos que codificarlas de alguna manera que el modelo las entiende me cree esto de juguete

**[0:31:49]** no es cierto entonces tenemos por ejemplo la variable que me indica los kilogramos la variable

**[0:31:55]** que me indica el tipo de fruta y la fruta es importada si o no y el precio entonces 2.5 1.8

**[0:32:03]** este que sería el como el peso ya está numérico entonces no debería provocarme problemas pero en

**[0:32:10]** cambio qué hago por ejemplo con la columna fruta qué hago con la columna importado estos dos no son

**[0:32:16]** números entonces necesito pasar la número de alguna manera para que mi modelo pueda entrenarse

**[0:32:24]** con estos datos estos datos no son utilizables así entonces cómo puedo codificarlas de alguna

**[0:32:30]** manera si que tengo pocas variables igual puedo realizar una transformación a mano como utilizando

**[0:32:36]** un diccionario y utilizando un replays que ya habíamos visto la función replays cuando

**[0:32:41]** estábamos tratando de jugar con con palabras con strings no sé cuando queríamos que el string

**[0:32:49]** fuera como en un formato usábamos esta función de replays entonces podemos crearnos un

**[0:32:55]** diccionario tal cual diría que y aquí le asignó un valor a cada palabra entonces digo que por

**[0:33:02]** ejemplo el plátano va a ser el valor 1 la manzana verde va a ser 2 y así entonces yo especifico las

**[0:33:08]** reglas a mano yo las escribo en un diccionario y luego lo único que tengo que hacer es tabla

**[0:33:14]** punto replays o si me preocupo de que sólo se aplica la columna que yo quiero tabla

**[0:33:20]** punto columna punto replays y le paso mi diccionario esto lo puedo hacer así crean un

**[0:33:27]** diccionario parte o puedo hacer el replays aquí aquí lo hago con la con la columna en específica

**[0:33:33]** tabla columna importado punto replays etcétera etcétera entonces aquí está y aquí paso la fruta

**[0:33:42]** a números y el importado también a números cada uno con un diccionario de forma manual

**[0:33:49]** ahora esto se puede hacer automático como por ejemplo existe en pandas la función que se llama

**[0:33:57]** get dummies y es una función que crea una columna booleana o sea como de verdadero falso para cada

**[0:34:05]** valor categórico técnicamente si tú unes como todo el código es un utiliza el método de

**[0:34:13]** one hot encode y entonces deja cero todas las posiciones y uno la posición que con que corresponde

**[0:34:21]** al valor que toma que tiene es ese como que representa mi valor en la posición se entiende más

**[0:34:32]** mirando entonces que pasa si yo tomo mi tabla uno y le a mi tabla no mi tabla se llama tabla que

**[0:34:42]** pasa si yo tomo mi tabla y le aplico esta función que se llama que pasa que pasa pasa algo raro con

**[0:34:52]** la tabla la tabla ya está modificado se crearon más columnas porque porque se crea una columna por

**[0:34:59]** cada valor que tiene mi columna básicamente entonces la columna fruta tenía por ejemplo el valor

**[0:35:07]** plátano el valor manzana verde manzana roja mandarina etcétera entonces se crea una por cada

**[0:35:14]** por cada valor o sea una para mandarina una para manzana roja una para manzana verde una para

**[0:35:19]** pera una para plátano etcétera y como son booleanas tienen verdadero falso entonces se dan cuenta

**[0:35:26]** para cada pila o registro que no sea mandarina se va a poner con falso y cuando cierra mandarina

**[0:35:36]** se va a poner con verdadero y qué va a pasar cuando es mandarina en todas las demás columnas

**[0:35:43]** que representan otro valor de fruta va a estar en falso entonces si es que nosotros miramos los falsos

**[0:35:50]** como cero y los tru como uno esto quedaría como un vector bueno un arreglo de ceros excepto en

**[0:35:59]** donde está la posición ok la posición indica que fruta es ok entonces sería 0 0 0 0 1 entonces

**[0:36:08]** a la última si en la última hay un uno significa que es un plátano si en la primera hay un uno significa

**[0:36:14]** que es una mandarina aquí entonces pasamos como a representarlo como un vector de ceros y uno

**[0:36:21]** y el importado le pasa lo mismo no es cierto importado no importado si tiene un tru y un

**[0:36:29]** falso pero en cambio para importado no es tan necesario porque importado podría ser simplemente

**[0:36:35]** lo podemos pasar a 0 y uno y que el cero significa que no y que el uno significa que si

**[0:36:40]** esto tener dos columnas para representarlo es innecesario porque es una variable binaria entonces

**[0:36:46]** si no es una si es si no es tru entonces fuese entonces como que es redundante tener dos columnas

**[0:36:53]** para esto porque binario qué pasa si hay un nan y yo lo quiero representar porque puede pasar

**[0:37:02]** puede pasar y va a ser un año y yo lo quiero representar normalmente lo que haría sería un

**[0:37:06]** manejo no es cierto de la tabla y tomar la decisión de qué hago con los nan antes de pero qué pasa si

**[0:37:12]** yo lo quiero representar específicamente en esta representación yo puedo obligar aquí estoy

**[0:37:21]** insertando un nan a propósito porque no tenía yo puedo obligar con el get dummies si aplicó

**[0:37:28]** el get dummies el nan no aparece el nan que está aquí que sería el último lo único que hace es tener

**[0:37:36]** todo en falso o sea que no forma parte de ninguno de los valores para frutas pero lo puedo forzar poniendo

**[0:37:44]** un dummy na igual a tru y ahí lo que va a pasar es que por cada columna que tenga esto de

**[0:37:53]** ser categoría categorica se se va a agregar la opción de nada no se va a crear un nan para

**[0:38:00]** fruta una columna nan para fruta y una columna nan para importado que esta columna es inútil porque

**[0:38:06]** está todo en falso entonces yo la podría borrar ya así sería automático también se puede automático

**[0:38:16]** a hacer lo que nosotros hicimos con el diccionario con algo que se llama label encoder que

**[0:38:22]** transforma los valores desde cero hasta el número de clases qué pasa con este label encoder o esta

**[0:38:28]** representación de 0 1 2 3 4 para los valores categóricos se aconseja utilizar solo en la variable

**[0:38:37]** objetivo por qué porque yo puedo crear un orden artificial de que los paso a número cuando las

**[0:38:46]** variables no son la variable objetivo por ejemplo si es que yo no quisiera predecir fruta y a la

**[0:38:51]** mandarina le pongo 1 a la roja le pongo a la manzana roja le pongo 2 a la manzana verde le

**[0:38:55]** pongo 3 a la fruta le pongo 4 el modelo quizás trate de encontrar alguna relación creciente que

**[0:39:04]** haya entre los valores cuando en realidad no es así no existe un orden para las frutas no

**[0:39:11]** cierto no existe un orden de pera manzana verde manzana roja la mandarina no sé debería

**[0:39:18]** tener un valor más grande que el pera o más grande que plátano no pasa eso siempre

**[0:39:22]** eso entre categoría entonces este label encoder que es e implícidamente le pone un orden

**[0:39:29]** cuando crea las etiquetas se aconseja utilizar solo solo en la variable que vamos a predecir

**[0:39:36]** que sería el objeto entonces como lo ocupó importó de saikidler de la parte de preprocesamiento

**[0:39:44]** de preprocesing lo importó lo creo y luego le le paso la columna en específico que yo quiero

**[0:39:53]** transformar entonces lo llamo aquí lo llame y como lo hago normalmente lo que hago es hacer

**[0:39:59]** un punto fit y después un punto transform que creo que lo vimos la ayudante a pasar laboratorio

**[0:40:06]** pasado yo les dije oigan hay una función que hace los dos de una que se llama fit transform

**[0:40:11]** ya este tal este también la tiene tiene un fit transform entonces lo que está haciendo es ver la

**[0:40:17]** ver la columna no cierto y ahí ve cuál es el número máximo de clases no cierto y después

**[0:40:23]** las transforma este fit transform hace todo de una del número de clases las transforma también en una

**[0:40:29]** sola pasa entonces aquí yo le estoy especificando la columna la columna fruta no más que solo

**[0:40:37]** cambia eso entonces ahora veo mi columna fruta modificada y ahora digo cómo cómo sé cuál es

**[0:40:47]** el valor original porque aquí no veo el diccionario interno que tiene no cierto no veo el diccionario

**[0:41:00]** interno que tiene solamente si lo llamo entonces puedo ocupar algo que se llama el inverse

**[0:41:07]** transform y el inverse transform lo que hace es tomar una etiqueta y tengo que ocupar el

**[0:41:12]** mismo que entrene y el mismo que se para transformar la misma instancia toma un número y devuelve la etiqueta

**[0:41:18]** categorica entonces no sé el uno representa manzana roja entonces yo puedo hacer esto para cada código

**[0:41:26]** y ahí está mi diccionario entonces el uno ignorar esta esta cosa ignorarlo primero ignorar

**[0:41:34]** el idea el uno representa manzana roja el cero representa mandarina el 3 representa pera por

**[0:41:40]** ejemplo y así entonces es la manera automática que tengo para pasar de valores categóricos a número

**[0:41:49]** si se entiende voy a sumer que no hay dudas pero me pueden interromper si quiero ya entonces esa

**[0:42:03]** era la primera el primero obstáculo que teníamos cuando nos cuando nos enfrentamos al problema

**[0:42:11]** de clasificación que puede ser bueno que lo primero es que nuestra etiqueta ya no era un

**[0:42:16]** número pero ahora ya resolvimos eso sabemos cómo va a hacerla a número me voy a saltar esto porque

**[0:42:23]** acabamos de ver la clase pero nosotros estamos en modelos discriminativos estamos en queremos aprender

**[0:42:29]** una función discriminativa bla bla bla donde tenemos k etiquetas bla bla bla o veo una manito si una

**[0:42:41]** duda que es eso de label encoder es lo mismo que son un replays para cambiar los valores

**[0:42:49]** categóricos por los numéricos que otro cuál es el otro replays si es lo mismo que hacer un replay

**[0:43:00]** solamente que con el replays yo tengo que ver los valores a mano y quizás a veces tengo muchas

**[0:43:07]** categorías entonces lo hace de forma automática si es que yo no quiero hacer la transcripción de

**[0:43:15]** cada categoría a mano y eso sí o sí es un paso necesario para el modelo de clasificación

**[0:43:26]** si es que yo tengo variables que tienen valores que no son numéricos no puedo entrenar el modelo

**[0:43:33]** si se lo intentas pasar te va a dar error porque no puede leer palabras no las va a entender

**[0:43:39]** bien gracias

**[0:43:47]** entonces otro obstáculo que tenemos al momento de trabajar con modelos de clasificación es que

**[0:43:54]** ya no podemos medir el error como lo mediamos con las métricas de antes porque si se acuerdan por

**[0:43:59]** ejemplo una métrica era el min square error el error cuadrático medio y eso me dice mide como

**[0:44:07]** la distancia la diferencia entre mi valor predicho y mi valor real no es cierto pero aquí en clasificación

**[0:44:18]** no tenemos esto ve una manito la tengo pendiente un segundo en clasificación no tenemos eso porque

**[0:44:26]** qué pasa por ejemplo aquí que tengo mi codificación de números qué pasa si la respuesta correcta

**[0:44:32]** era plátano y yo predije manzana roja ok mi respuesta correcta era 4 y yo predije 1 y tengo otro modelo

**[0:44:44]** que predice 3 si ocupáramos el error cuadrático medio me diría que el modelo que predice 3 está mejor

**[0:44:52]** que el modelo que predice 1 aún cuando la respuesta correcta es 4 porque porque 3 está más cercano

**[0:44:58]** pero eso no lo puedo aplicar a las categorías porque pera predicir pera y predicir manzana roja

**[0:45:04]** está igual de mal porque me equivoqué en la categoría entonces ya no puedo ocupar ese tipo de métricas

**[0:45:10]** porque no hay distancia lo importante es que me equivoqué de categoría no más entonces por eso

**[0:45:15]** necesitamos definir otras métricas que nos ayuden a cuantificar estas relaciones y ahora sí

**[0:45:22]** y por ejemplo el tema de los de los variables ahí no hay ningún problema si la letra como si por

**[0:45:35]** ejemplo manzana verde si en algunos casos dice verde beba yúscula el otro dice verde beba yuscula

**[0:45:41]** ahí no hay ningún pulmón si también más

**[0:45:52]** te me cuartaste un poquito pero creo que entendí de qué pasa si es que tengo manzana verde escritó

**[0:45:58]** de una manera y manzana verde escritos de otra manera o sea si tengo inconsistencia en la tabla

**[0:46:04]** básicamente si esa es más o menos tu la capte bien a lo no me estoy cayendo yo

**[0:46:33]** no se escucha a mí si me cae en internet

**[0:46:40]** pero tu duda es más o menos qué pasa si es que tengo inconsistencia en las etiquetas por ejemplo

**[0:46:46]** si es que tuviera manzana verde con mayúscula después con minúscula eso eso ya es que eso ya

**[0:46:53]** sería un paso anterior porque si te acuerdas nosotros primero limpiamos la base de datos

**[0:46:58]** y después hago el preprocesamiento y después entren y después hago todo eso entonces sería un paso

**[0:47:03]** antes de antes del preprocesamiento sería parte del preprocesamiento pero tendría que ver con la limpieza

**[0:47:09]** de los datos entonces ahí yo tengo las herramientas que vimos antes en limpieza que serían como para

**[0:47:16]** ponerlas toda por ejemplo podría poner todo en minúscula o todo en mayúscula eliminar los

**[0:47:21]** espacios de más eliminar tildes etcétera etcétera y luego cuando ya tengo todo limpio puedo

**[0:47:26]** hacer esto del label encoder o ocupar el diccionario

**[0:47:42]** ya voy a asumir que responde pero si no responde puedes volver a hablar voy a seguir con esto por

**[0:47:52]** el momento de nada gracias ya entonces como dije hay que cambiar las métricas porque ahora la

**[0:48:02]** forma de medir el error es diferente entonces para esto ocupamos estas letritas que ustedes

**[0:48:09]** debieron haber visto en clase no es cierto los tropos los verdaderos positivos verdaderos negativos

**[0:48:15]** falsos positivos y muy bien si lo dieron hoy día más o menos tienen el concepto no es cierto

**[0:48:25]** ok repasemos lo igual entonces qué significa cada uno vamos a pensar en un modelo binario

**[0:48:36]** y que nos vaya que reciba por ejemplo una imagen o algo y nos diga si la etiqueta es como guitarra y

**[0:48:45]** tiene que decir si o no así es guitarra ya es como guitarra o no guitarra y no va a quedar binario

**[0:48:51]** entonces si yo tengo una entrada x y yo considero guitarra como verdadero eso voy a guitarra es el

**[0:49:00]** el tru entonces si yo tengo una entrada x y esta es positiva no es cierto es guitarra puede suceder

**[0:49:08]** pueden suceder dos cosas que el modelo predijo guitarra ok entonces la etiquetara tru y un modelo

**[0:49:16]** predijo tru entonces ahí es un verdadero positivo porque mi guitarra es el positivo y el modelo

**[0:49:23]** predijo bien entonces verdadero positivo en el otro caso es que el modelo prediga que no era

**[0:49:28]** guitar básicamente no guitarra entonces la etiqueta verdadera sería un tru y un modelo dijo no entonces

**[0:49:39]** es un negativo pero es falso es un falso negativo ahora que pase yo tengo una entrada x y la etiqueta

**[0:49:47]** no es guitarra o sea no guitarra puede suceder dos cosas que el modelo prediga guitarra o que el

**[0:49:53]** modelo prediga no guitarra si el modelo predijo guitarra mi modelo dice que la muestra es positiva

**[0:50:02]** porque yo aquí estoy considerando guitarra como positivo entonces estoy diciendo que mi muestra

**[0:50:05]** es positiva pero me equivoqué entonces un positivo presta malo entonces es un falso positivo y ahora

**[0:50:13]** que pasa si es que en este caso predijo que no era guitarra recordemos que si guitarra

**[0:50:18]** es positivo no guitarra se consideraría negativo entonces mi modelo predijo negativo y la etiqueta

**[0:50:25]** real era negativa era no guitarra entonces un negativo y está bien entonces es un verdadero

**[0:50:32]** negativo ahora son las definiciones de verdadero positivo falso negativo falso positivo verdadero

**[0:50:38]** negativo ya teniendo esta definición ah esperen alguien se perdió aquí tú tú tú que como lo

**[0:50:47]** más difícil igual a mí de repente se me olvido y mal de repente ando sin

**[0:50:53]** ya parece que estamos bien igual si llega confusión pueden pueden preguntar entonces ya definiendo

**[0:51:08]** estos verdaderos positivo y todo esto estos cuatro yo defino todas las métricas están definidas

**[0:51:14]** en base a eso ok entonces por ejemplo tenemos el acura si o la exactitud que es para evaluar

**[0:51:22]** el clasificador y consiste la fórmula general el acura si es los tropos y bueno en español los

**[0:51:29]** verdaderos positivos más los verdaderos negativos partido por los verdaderos positivos más los

**[0:51:34]** verdaderos no más los falsos positivos más los verdaderos negativos más los falsos negativos

**[0:51:38]** si se dan cuenta los cuatro son la totalidad es mi universo entero porque no hay si yo predigo

**[0:51:47]** si tengo una etiqueta y esta tiene un valor y yo hago una predicción sólo puede ser uno

**[0:51:51]** de estos cuatro puede caer en una de estas cuatro cosas entonces si yo sumo las cuatro cosas este

**[0:51:56]** es mi universo entero y lo de arriba si se dan cuenta son los verdaderos positivos ok los que

**[0:52:04]** eran positivos mi modelo predijo positivo entonces mi modelo lo hizo bien y los verdaderos negativos

**[0:52:13]** donde mi modelo predijo negativo y mi modelo lo hizo bien entonces la acura si es lo lo que

**[0:52:21]** mi modelo predijo bien partido de todo toda toda la toda la predicción de la que me pasa con esto que

**[0:52:33]** si yo tengo datos desbalanceados esto no toma en cuenta el desbalance entonces existen algunas

**[0:52:39]** variaciones una de ellas es el balance acura si la exactitud balanceada que es esto mismo que tengo

**[0:52:48]** los casos positivos partido los casos totales y esto lo hago por cada k que k sería cada clase

**[0:52:56]** o sea el k sería el número total de clases y lo hago en este k chiquito que es cada

**[0:53:00]** clase esto lo hago por clases otras métricas que podemos utilizar por ejemplo es el f1 score

**[0:53:09]** muy muy utilizada el f1 score que es una media armónica una media entre una métrica

**[0:53:17]** que se llama precisión y otra que se llama record o no me acuerdo en español ya pero precisión

**[0:53:25]** y precisión y record y que es el precisión y que es el record veo una manito

**[0:53:36]** tengo una consulta porque justo estaba viendo este tema el día de hoy por el proyecto que

**[0:53:42]** en los datos que yo estoy trabajando y cuáles recomiendas tú porque yo la encontré como

**[0:53:51]** débil el el acuara si no sé no se lo no se la desculpa

**[0:53:56]** porque por ejemplo de 100 datos ya 20 me salen por ejemplo negativo 80 positivo pero aún

**[0:54:10]** cuanto se hace esto me van a dejar que los 100 son positivos porque es como que tiene un

**[0:54:16]** pequeño sesgo entonces como quien no no es muy recomendable utilizarlo entonces aparte de

**[0:54:22]** ese tenemos como los de abajo son más recomendables normalmente vamos a bajito vamos a ver algo que

**[0:54:32]** se llama classification report que saca artes métricas de una pero yo puedo sacar varias pero

**[0:54:37]** normalmente cuando si el número de clases o si hay desbalanceo lo que yo voy a ocupar es como

**[0:54:42]** el balance aquí ahora si pero una muy utiliza es el f1 score entonces ésta ésta es muy recomendada

**[0:54:52]** ahora que es que me interesa más hacerlo bien me da lo mismo en qué clase de la que ahora

**[0:55:01]** pero también lo puedo tener el balance aquí ahora si también hay otras formas de medirle

**[0:55:07]** el acuara si hay algunas variaciones pero como digo el f1 score es muy utilizado en especial

**[0:55:13]** porque usa estas dos estas dos métricas que voy a explicar ahorita gracias gracias a ti me sale

**[0:55:24]** más uno o sea que hay otra manito pero no es quiénes cuéntame cuéntame escucha si hayan que

**[0:55:37]** adua el número de clases no entiendo bien es que se refiere con el número de datos

**[0:55:44]** número de categoría número de categorías por ejemplo en la cosa de arriba

**[0:56:00]** y aquí aquí yo tengo cinco clases de la clase mandarina clase manzana roja clase manzana

**[0:56:06]** verdad clasa clase pera clase plata no entonces tengo cinco clases en total entonces mi casa sería cinco

**[0:56:13]** me pase entonces mi casa sería cinco entonces cuando caes cero o bueno dependiendo de cómo lo tome

**[0:56:23]** si mi casa es uno por ejemplo estoy evaluando mandarina por ejemplo la clase mandarina

**[0:56:31]** voy a sacar el balance aquí ahora si el sub uno para la clase mandarina el sub dos para la clase

**[0:56:39]** manzana del sub tres para y después lo divido en uno partió el número total de clases sería cinco

**[0:56:47]** pero hay como tomando en cuenta el número de datos está tomando en cuenta la número de clases

**[0:57:01]** de categorías pero no pensaba como que ese índice media como el número de datos

**[0:57:11]** el número de clases el número de clases y ahí como entonces mide como el desbalance

**[0:57:21]** es como que no me queda claro que podría tener como cinco clases todas con el mismo número de

**[0:57:34]** datos y no no no veo el desbalance no se explico quizá me queda pendiente te puedo explicar otra forma

**[0:57:47]** más adelante con con el classification report que me sé ese no me se va a lanzar poco pero podría

**[0:57:54]** fijarme quizás tengo la fórmula mala pero mejor mejor lo dejo pendiente lo dejo al final al final la

**[0:58:03]** busco y la al final de la clase ya ya gracias y ya entonces

**[0:58:15]** precision y record ahí me entonces tengo el f1 que es una media armónica entre precision y

**[0:58:22]** record tengo el recall y tengo el precision y aquí están por clase porque tienen el suca

**[0:58:27]** entonces yo puedo sacar el recall por clase y el precision por clase entonces todo este

**[0:58:31]** análisis de verdadero positivo va a ser por clase entonces tengo el recall que son los

**[0:58:36]** verdaderos positivos partido de los verdaderos positivos más los falsos negativos los verdaderos

**[0:58:44]** positivos son los que me modeló puedo puso dijo que eran positivos y están bien y los falsos

**[0:58:51]** negativos son los que mi modelo que dijo que eran negativos pero están mal entonces son

**[0:58:59]** los positivos son los positivos que yo la tiene partido de los positivos los positivos reales

**[0:59:06]** técnicamente entonces estoy diciendo a cuántos de los positivos le achumte realmente porque

**[0:59:15]** estos son mis positivos todos mis positivos a cuanto a todos los positivos para esa clase

**[0:59:19]** yo le mi modelo le achumto correctamente y el precision aquí tengo los verdaderos positivos

**[0:59:28]** partido los verdaderos positivos más los falsos positivos los verdaderos positivos ya dijimos a

**[0:59:35]** los positivos que mi modelo encontró bien y los falsos positivos son los que mi modelo dijo

**[0:59:42]** que eran positivos pero están mal entonces tengo los verdaderos positivos partido de todo

**[0:59:50]** lo que mi modelo dijo que era positivo entonces el precision es de todo lo que mi

**[0:59:56]** modelo dijo que era positivo cuánto realmente a cuánto realmente le asunté

**[1:00:00]** ok esto es de los verdaderos positivos a cuánto le asunté y esto es de todo lo que

**[1:00:06]** mi modelo dijo que era positivo cuánto es realmente positivo

**[1:00:10]** ese es el precision y ese es el recall

**[1:00:13]** ahi está acá ya entonces el precision determina cuántas de nuestras

**[1:00:17]** predicciones son correctas mientras que el recall indica el número de

**[1:00:19]** etiquetas verdaderas que fueron correctamente identificadas por el

**[1:00:23]** increíble y el f1 es como una media tres o dos y además otra cosa que tenemos que es

**[1:00:34]** muy visual es la matriz de confusión entonces aquí en saikiller punto

**[1:00:40]** matrix tengo la matriz de confusión entonces dado que yo tengo por ejemplo algo

**[1:00:46]** binario y tengo las etiquetas verdaderas y tengo una predicción puedo llamar esta

**[1:00:51]** función y le digo oye te voy a pasar las predicciones aquí están las predicciones

**[1:00:56]** de verdad y aquí están las predicciones de mi modelo me va a dibujar una esta es

**[1:01:01]** la matriz de confusión que deberon haberla visto entonces aquí me indica

**[1:01:06]** dónde están las etiquetas verdaderas y aquí están las etiquetas predichas

**[1:01:09]** entonces la diagonal es donde está lo que mi modelo predijo correctamente y

**[1:01:15]** las otras son en donde se fue equivocando en donde cometió errores

**[1:01:19]** entonces en este ejemplo que me cree dice tengo siete imágenes con etiqueta

**[1:01:25]** estoy diciendo imágenes

**[1:01:29]** tengo siete imágenes con etiqueta guitarra de las cuatro de las cuales dije que cuatro

**[1:01:34]** eran guitarra y el resto no y después tengo cinco imágenes que no tienen la

**[1:01:38]** etiqueta o sea que son no guitarra de las cuales dije eso que solo una era

**[1:01:41]** guitarra entonces eso está puesto aquí entonces estoy diciendo que en el

**[1:01:48]** caso que si eran guitarra

**[1:01:50]** no tengo el reggae guitarra, guitarra, guitarra, 1, 2, 3, 4, 5, 6, 7, 7, guitarra

**[1:01:56]** guitarra es uno

**[1:01:59]** de las siete guitarras cuatro dije que eran guitarras o sea de los siete unos

**[1:02:04]** que eran guitarras los verdaderos unos yo predije uno para cuatro casos y en

**[1:02:10]** los otros tres casos predije cero y para los casos en que era no guitarra

**[1:02:16]** o sea la verdad la etiqueta verdadera era cero yo a cuatro de esos predije cero y

**[1:02:23]** a uno de esos predije uno, entonces ahí está mi matriz eso significa como que haga

**[1:02:29]** cuadrante cuando estoy en binario, ve una mano levantada o no, lo peseando

**[1:02:36]** si era la es la mía no era es la mía pero la pregunta era como una una

**[1:02:43]** diapo mucho más tranto se nos quiero como interrofiere la base así que

**[1:02:47]** prefiero dejarlo al final ya ok me acuerdas al final

**[1:02:55]** bueno esa es la matriz de confusión y si no estamos cuenta es muy visual y

**[1:03:00]** podemos ver por ejemplo los cuadrantes los verdaderos positivos los falsos

**[1:03:03]** positivos etcétera cuando es binaria es muy visual cuando es cuando son más

**[1:03:09]** clases es como para entender en dónde cuáles son las clases en las que me

**[1:03:14]** estoy confundiendo más que también lo estoy haciendo porque la

**[1:03:17]** diagonal es bastante visible y tiene por ejemplo siempre tiene esta escala de

**[1:03:21]** color entonces entre más cercano al color de arriba yo veo que lo estoy haciendo en

**[1:03:25]** su mayoría si las clases están desbalanceadas ahí voy a perder un poco

**[1:03:29]** la la como esta notación del color pero si que las clases están balanceados puedo

**[1:03:35]** darme cuenta fácilmente en qué clase lo estoy haciendo más mal por ejemplo ya

**[1:03:40]** y todas las métricas que vimos acá arriba todos esas y más y más no

**[1:03:45]** son las únicas están en ese color punto métricas aquí yo podría haber puesto copa

**[1:03:49]** y haber importado todas en una sola línea pero aquí yo puedo importar todas las

**[1:03:53]** que están y más si es que quiero entonces yo no tengo que hacer la fórmula

**[1:03:57]** que dice ahí yo simplemente puedo llegar y ocuparlas entonces podemos sacar el

**[1:04:00]** aquí ahora si por ejemplo de los datos que muestra esta matriz de confusión

**[1:04:04]** por poder a la que hubo así me da eso

**[1:04:09]** entonces sabiendo que la que ahora si es esta fórmulita no es esto de más de

**[1:04:16]** no lo que lo hice más de p más de n ahora la idea es que llenen esto a manito

**[1:04:24]** cuáles son los verdaderos positivos los verdaderos negativos los falsos positivos

**[1:04:28]** los falsos negativos dado la matriz o dado los numeritos si es que son más de

**[1:04:32]** numeritos pero dado la matriz que llenen esto para que saquemos el

**[1:04:38]** acurasi a mano entonces vamos a hacerlo en conjunto para no dejarles un

**[1:04:45]** cronómetro triste sin habla entonces dado esta matriz y dado que mi uno o mi

**[1:04:54]** positivo es guitarra si es que lo quieren ver así cuántos serían los

**[1:04:59]** trupos y que valor debería ir en trupos y

**[1:05:14]** el es el cuatro cuatro cuatro porque porque uno uno cuatro y entro negativo que son los

**[1:05:32]** que yo dije que eran negativos o yo predije mi modelo predijo que eran negativos y lo hice bien

**[1:05:38]** diríamos que ver el plot nuevamente

**[1:05:47]** cuatro igual es cuatro igual porque porque sería esta parte si 0 0 ya los falsos positivos

**[1:06:02]** el uno era que era verdadero y

**[1:06:12]** estrés

**[1:06:33]** los falsos positivos son los que yo predije que eran positivos pero está mal

**[1:06:45]** entonces los que yo predije que eran positivos pero eso está mal entonces uno en ese caso

**[1:06:56]** porque qué significa que yo predije que eran positivos que sería el uno pero su etiqueta

**[1:07:01]** real no era uno entonces este cuadrante ya y me quedan los falsos negativos los falsos

**[1:07:16]** negativos son los que mi modelo dijo que eran negativos pero eso está malo

**[1:07:21]** son positivos entonces el tres y si yo hago esto me da exactamente el mismo valor que me dio el aquí

**[1:07:39]** porque porque esta fórmula que estamos haciendo de la misma fórmula que tiene por dentro esta

**[1:07:43]** cuestión y bravo bravo para todos entonces más o menos así entiendo cómo están ubicados en

**[1:07:52]** los cuadrantes cuando la variable binaria donde va cada uno de si tuviéramos tres clases y aquí

**[1:08:00]** ni siquiera le puse número y todo le puse tal cual las palabras se vería como algo así que le puse

**[1:08:06]** las palabras porque aquí sale con palabras pero estoy segura de que aquí hay un parámetro que

**[1:08:12]** no me acuerdo cuál es que es el labels donde le puedo poner los labels de la de la de las

**[1:08:23]** clases para que aquí me de en vez de los numeritos las etiquetas de las clases entonces le paso en orden

**[1:08:30]** cual la clase 0 1 y ya entonces sí se vería por ejemplo un caso en donde tengo una matriz de

**[1:08:39]** confusión de más de dos que no es binaria entonces de más de dos clases entonces la diagonal sigue

**[1:08:45]** representando lo mismo cada elemento de la diagonal es la cantidad de esa clase que yo

**[1:08:50]** predije bien y todo lo demás que no está dentro de la diagonal son las veces que me equivoqué lo

**[1:08:57]** importante es ver en dónde me equivoqué para entender cómo estoy equivocando ok entonces qué

**[1:09:02]** clases estoy confundiendo más entonces por ejemplo en todas me estoy confundiendo siempre

**[1:09:12]** hay siempre siempre hay una que mentir en una no me estoy confundiendo para la clase y

**[1:09:20]** cuando la etiqueta real es guitarra yo no me confundo yo no predigo otra cosa pero lo que si estoy

**[1:09:26]** haciendo es predecir otras cosas como guitarras y se dan cuenta en bajo estoy prediciendo la una

**[1:09:34]** como batería o sea esa imagen de estar malísima para confundir un bajo con una batería es poco

**[1:09:39]** probable pero es bastante probable que la confunda con una guitarra porque se parece un poco en el

**[1:09:45]** tipo de instrumento entonces esto yo lo esperaría esta confusión yo la esperaría esta no entonces

**[1:09:51]** ahí quizás entre tendría que entrar a ver los datos a ver si la imagen está no sé está mal

**[1:09:57]** clasificada o se ve extraña o está mala le hice mal el preprocesamiento etcétera

**[1:10:03]** etcétera entonces la matriz de confusión me ayuda a entender como el patrón de lo que está

**[1:10:08]** pasando con los datos y lo que está haciendo mi modelo y de manera mucho más visual que ver

**[1:10:12]** los numeritos y aquí les pediría que sacáramos el rico la mano pero quizás está muy largo porque

**[1:10:19]** tendría que sacarlo para cada clase igual tan largo entonces podríamos dejarlo pueden dejarlo como

**[1:10:29]** tarea interna para no quedarme sin tiempo ya algo que si tengo que mostrar que fue muerto de nuevo

**[1:10:37]** es el clasificación report y aquí tendría que explicar en macro y el wait que no sé si me dan

**[1:10:48]** tanta gana voy a pausar estos cinco segundos para poner la documentación de saikirla entonces

**[1:10:57]** donde está y vamos a buscar por ejemplo el recall ustedes no lo ven pero yo estoy buscando la

**[1:11:07]** documentación de la becha entonces me voy a guardar esta pestaña para mostrar ya aquí importé

**[1:11:17]** algo que se llama clasificación report o report de clasificación y le estoy pasando las etiquetas

**[1:11:23]** reales y etiquetas preditas que nada predijo no he entrenado ningún modelo me las creé yo nomás

**[1:11:28]** que son de juguetes y lo que me da el clasificación report es el precision el recall el f1 y el

**[1:11:35]** support entonces el precision es el precision por clase precision para la clase bajo precision para la

**[1:11:41]** clase de batería precision para la clase y tal el recall también está por clase y el f1 técnicamente

**[1:11:46]** también está por clase pero yo lo podría sacar lo podría sacar en general podría sacar un promedio

**[1:11:55]** ahora lo que me importa es cómo voy a calcular ese ese número general ok y eso es lo que varía

**[1:12:01]** con esto de macro average y weighted average lo voy a explicar en un segundo y también está el accuracy

**[1:12:07]** y el accuracy se saca global no es cierto entonces ahí está la que ya el support es el número de

**[1:12:17]** elementos por clase o sea yo tengo seis elementos de la clase bajo cuatro elementos de la clase

**[1:12:22]** batería y cinco elementos de la clase guitarra que eso es el súper es el número de elementos

**[1:12:28]** que yo tengo y aquí tengo un macro average y un weighted average y está para para mi precisión

**[1:12:37]** para mi recall para mi f1 y el support tiene todo lo mismo y lo que es el support aquí es

**[1:12:43]** simplemente el total de la el total de elementos porque acá sobre eso me sale 15 15 porque el

**[1:12:48]** total de elementos está tomando todos los elementos en consideración para calcular

**[1:12:52]** y aquí me metí a la documentación de scikit-learn y aquí me podría meter al del f1 o al del precision a

**[1:13:01]** cualquiera me metí al recall porque sí y aquí tiene una forma de calcular el average tiene un

**[1:13:08]** parámetro para el av o el parámetro para el average y aquí me dice que puede tomar los

**[1:13:12]** valores los valores micro macro samples weighted binary o non y que tiene de defecto el binary

**[1:13:21]** y aquí me dice cómo voy a calcular este promedio

**[1:13:30]** entonces por ejemplo tengo el micro y me dice que va a calcular las las métricas de manera

**[1:13:38]** global tomando el total de verdaderos positivos de falsos negativos y de falsos positivos el macro

**[1:13:45]** las va a calcular para cada etiqueta y va a básicamente sacarle el promedio y dice que no toma el desbalanceo

**[1:13:55]** en cuenta aquí voy a sacarle el promedio no tomó no tomó desbalanceó el weighted me calcula el promedio

**[1:14:05]** o sea me calcula las métricas para cada etiqueta y luego va a tomar el promedio pero este cuando

**[1:14:14]** la está calculando esto va a estar pesado por el supo o sea por el número de elementos en cada

**[1:14:20]** clase entonces esto sí toma en consideración la la el imbalance para las clases imbalance

**[1:14:29]** para el desbalanceo de clases el desbalanceo de entonces estas distintas formas es para calcular

**[1:14:36]** esta este promedio y como la forma que voy a hacer para calcular este este esta métrica de forma

**[1:14:46]** global para todas las cosas entonces está la forma que el número que me da si es que yo ocupo la

**[1:14:52]** forma macro y el número que me da si es que yo ocupo la forma weight ok entonces eso significa

**[1:14:57]** cada una en el classification report y básicamente eso ya entonces ahora vamos porque no entrenado

**[1:15:12]** ningún modelo vamos a ver cómo entrenamos modelos de clasificación y un spoiler es que me muy pareció

**[1:15:18]** los de regresión primero vamos a ocupar un modelo o sea vamos a necesitar datos que tengan

**[1:15:23]** clases y para eso nos vamos a vamos a ocupar un data set que se llama iris iris iris se confundía

**[1:15:32]** con un dato fenómeno ya que se llama iris y en este data set tenemos longitud y ancho de

**[1:15:41]** el sepalo y del pétalo que son descripciones de una planta o una flor y cada fila pertenece

**[1:15:49]** una planta que son estas tres puede ser cada una de estas tres categorías o clases entonces yo de

**[1:15:56]** scikit-learn voy a cargar los datos y el scikit-learn también tiene data sets internos y me da una

**[1:16:02]** minidescripción del data set también me da estadísticas del data set y por ejemplo que hay una

**[1:16:08]** alta correlación aquí o sea alta correlación como que son importantes

**[1:16:17]** hay no lo muestro que me creo bueno es que aquí lo estoy cargando aquí está cargando solamente la

**[1:16:24]** descripción y aquí me voy a cargar los datos y aquí sí los muestro entonces por ejemplo aquí una

**[1:16:31]** fila me da la clase sepalo el largo el largo el largo y el ancho del sepalo y el largo y el

**[1:16:44]** ancho del pétalo y que está en centímetros y la columna especie ya es la categoría que ya está

**[1:16:51]** puesta en el formato que nosotros necesitamos y se dan cuenta porque eso lo necesitamos en formato

**[1:16:59]** numérico y si es que yo quisiera puedo obtener los target names que es como el diccionario

**[1:17:07]** interior que tiene el data set para indicarme que significa cada cada columna y entonces

**[1:17:13]** cero es cetosa uno es esa y dos es entonces yo debería aquí empezar a buscar si es que el data

**[1:17:21]** se tiene nulos etcétera etcétera pero como es un dato hacer de juguete que ya está limpio no va a

**[1:17:26]** tener como nada así le puedo hacer algún describe pero que tiene todos los valores no hay nada como

**[1:17:33]** extraño fuera de rango etcétera etcétera ya y aquí lo muestro que me creo ya aquí lo

**[1:17:45]** único que estoy haciendo es crearme una columna que se llame tipo y lo que estoy haciendo es poner

**[1:17:50]** la clase y reemplazarla por la clase en palabras luego voy a hacer un histograma pero en de la columna

**[1:18:01]** de la columna de la clase y con esta función que ya habíamos visto en la clase de gráficos

**[1:18:06]** entonces simple como eso voy a ver visualmente si es que hay un desbalanceo notable de

**[1:18:11]** clases y me doy cuenta también lo hubiera visto en el disc que está balanceado el data set porque si

**[1:18:19]** no estuviera balanceado yo vería una barrita mucho más arriba o abajo que las demás también

**[1:18:26]** cuando yo quiero ver como variables útiles en cierto atributos útiles que me puedan servir

**[1:18:36]** para predecir la clase lo que normalmente hacemos son scatterplots aquí voy a hacer un voy a ocupar

**[1:18:45]** seborn que es otra librería y voy a ocupar un counter plot para hacer básicamente esto mismo que

**[1:18:51]** pero de forma más bonita porque estoy haciendo el mismo histograma pero estoy pintando por clase y

**[1:18:58]** eso yo no se lo tuve que decir explícitamente al gráfico en cambio aquí en matplotlib hubiera

**[1:19:05]** tenido que decirle explícitamente a cada tendría que haber creado tres histogramas y haberle dicho que

**[1:19:10]** quería que fueran de colores distintos cada uno en cambio aquí si yo pongo en el parámetro

**[1:19:17]** y le digo que se pinte por tipo entonces me las pinta por colores así entonces ya viendo eso

**[1:19:25]** hago por ejemplo un lindo histograma de las por las características entonces aquí estoy usando

**[1:19:33]** bueno estoy usando cada característica y estoy diciendo que quiero un histograma para todas las

**[1:19:39]** características entonces aquí tengo el sépalo en largo y el ancho el pétalo en largo y el ancho y

**[1:19:45]** las espé entonces con esto me creo todo de una y lo que yo quisiera hacer es como dije hacemos

**[1:19:53]** scatter los scatterplots de los gráficos de dispersión entonces ahora le voy a decir que

**[1:20:01]** creé un perplot que sería como el equivalente no es el equivalente exacto pero es para que me

**[1:20:06]** cree hartos scatterplots pero en el idioma en sentido de la sintaxis para esta librería que

**[1:20:13]** no es patplotlib que se llama SNS pero que está construida encima de matplotlib así que si le

**[1:20:19]** pongo después comandos de matplotlib por ejemplo este para ponerle un subtítulo también

**[1:20:26]** y le voy a pasar mi dataset y le voy a decir que los colores se pintan por la columna tipo que es la

**[1:20:35]** columna donde yo tengo el nombre de la clase en palabras y aquí le estoy dando como la paleta de

**[1:20:42]** colores un código muy fácil que voy a llegar ya entonces qué está pasando que me está generando

**[1:20:53]** si se dan cuenta es una grilla entonces me está generando muchos scatterplots muchos gráficos

**[1:20:59]** de dispersión de esta variable por ejemplo versus ella misma y ver su ella misma lo tiene sentido

**[1:21:06]** ser un scatterplot así que técnicamente lo que me hace es darme la distribución entonces después

**[1:21:12]** tenemos el largo del sépalo versus el ancho del sépalo y se me forma un scatterplot después

**[1:21:21]** tengo el largo del sépalo versus el largo del pétalo ok entonces tengo muchas scatterplots entonces

**[1:21:31]** como veo cuando unas variables potencialmente útil cuando en el gráfico de dispersión yo puedo separar

**[1:21:37]** las clases linealmente por ejemplo aquí este me está diciendo que esta combinación de variables no

**[1:21:44]** es muy buena para hacer la separación o está aquí yo no estoy viendo bien la separación aquí

**[1:21:50]** los histogramas están todos juntos pero las distribuciones están todas juntas entonces

**[1:21:59]** esto no me sirve para separar en cambio aquí por ejemplo veo que esta clase que es la verde que

**[1:22:03]** es la setosa está muy lejos de todas las demás entonces esta variable el petal length sobre

**[1:22:11]** sí misma aquí por mirar la diagonal por mirar los scatterplots lo que quiera gráficamente es

**[1:22:17]** muy útil para clasificación con esta variable puedo separar como fácilmente esta clase y ahora

**[1:22:23]** necesito información adicional para separar estas porque puedo separar una parte de esta y otra parte

**[1:22:28]** de esta pero la parte donde están juntas con estas o la variable yo no las puedo separar no me dan

**[1:22:33]** información para cuando es de una y cuando es de la otra entonces aquí tengo información

**[1:22:37]** complementaria para separarlas un poquito más y quizás yo uso toda la información de las

**[1:22:42]** variables puedo encontrar esa separación pero si se dan cuenta estas dos clases que son la

**[1:22:48]** naranja y la azul son las más difíciles de separar porque con dos variables la verde es

**[1:22:53]** linealmente separable yo hago una línea y ya separo esa clase de las demás entonces aquí es donde

**[1:22:58]** voy a tener conflictos yo se lo puedo ver con esto maravilloso ya entonces tengo tres modelos

**[1:23:07]** el primero aquí simplemente estoy dividiendo los datos aquí está diciendo un caplos que son gráficos

**[1:23:14]** de cajita pueden llegar y pegarlo por si necesitan hacer algún análisis les te lo dejo ahí de bonito

**[1:23:21]** primero tenemos el svm el support vector magic que lo que hacía era generar un hiper plano

**[1:23:30]** no cierto que me separara las clases y lo que hacen normalmente cuando trabajamos con este

**[1:23:35]** tipo de modelos que trabajan hiper planos es que es coge una clase y si hay multiclases pues todas

**[1:23:40]** las demás se vuelven como negativas entonces trata de crear un hiper plano que se pare esa

**[1:23:45]** clase versus todas las demás después para separar la otra un hiper plano para esa clase

**[1:23:49]** versus todas las demás y después hace una combinación de estos hiper planos que se paran

**[1:23:52]** cada vez y entonces un hiper plano que maximice la distancia de los puntos más cercanos de

**[1:23:58]** cada y como lo ocupó teco digo no vale la pena explicarlo funcionan igual que los modelos que ya

**[1:24:09]** entrenamos de regresión para esto yo tengo que importar no me acuerdo a lo importe a importe

**[1:24:15]** se ve su port vector machín aquí lo importe y lo que vamos a ocupar es para clasificación entonces

**[1:24:23]** tenemos que ponerle sbc para clasificación entonces que terminen c entonces vamos a crear

**[1:24:30]** nuestra instancia de modelo de svm para clasificación y le podemos dejar todos los parámetros por defecto

**[1:24:36]** y creo que por defecto tiene el kernel linea y creamos nuestra instancia y como todos los

**[1:24:44]** modelos para poder entrenarlo tenemos que hacerle punto fit y le vamos a pasar nuestros

**[1:24:49]** datos de entrenamiento nuestros datos que ya vimos la tabla no es cierto de iris yo dividí entre

**[1:24:56]** entrenamiento y test esto se le vamos a pasar los datos de entrenamiento y con eso igual con la misma

**[1:25:03]** sintaxis para los modelos ya se entrenó y con eso yo ya puedo predecir con el punto predict de

**[1:25:09]** siempre pasando en mi conjunto de test yo ya predijo entonces aquí con una función que yo no hice

**[1:25:17]** está definida en esta librería podemos pintar o graficar los límites de decisión entonces el

**[1:25:25]** svm creó este hiper plano y después este hiper plano y después este hiper plano para tratar de

**[1:25:32]** separar las clases recuerden que esto es el conjunto aquí estoy mostrando el conjunto de test ok

**[1:25:37]** estas no son todos los datos son los datos de test entonces podemos ver por ejemplo que

**[1:25:43]** en el test clasifica parece que todas las clases bien pero aquí si es que algún círculo se pasará

**[1:25:51]** para acá lo más probable es que el modelo tendría problema esto creo que está de más que son

**[1:25:59]** un escátero para las etiquetas verdaderas y la predicción pero creo que eso se ve mejor aquí

**[1:26:07]** pero el modelo lo hace bastante bien nuestro svm lo hace bastante bien te podemos sacar las

**[1:26:13]** las distintas métricas con el reporte de clasificación o si es que quisiera alguna específica

**[1:26:19]** simplemente yo sacarla amar ya y le puedo sacar la matriz de confusión ahí sí es que la quiero

**[1:26:28]** con numeritos y pos pasarle a la función que ya habíamos visto si es que quiero hacer

**[1:26:33]** entonces pensé que era mejor aquí en donde se está equivocando a en estos datos

**[1:26:49]** ya entonces aquí puedo ver más o menos cómo se comporta pero podemos compararlo al final cuando

**[1:26:55]** estemos comparando modelos lo importante es que cómo funciona esto crea hiper planos ya vimos

**[1:27:02]** qué pasa cuando es multiclase que hace un mi clase actual versus todas las demás y cómo se ocupa

**[1:27:08]** las sintaxis es muy muy similar a todos los modelos de regreso y vamos a ver que todos los demás

**[1:27:14]** modelos funcionan igual este catito me lo voy a saltar y si me queda tiempo vuelvo a qué pasa con

**[1:27:22]** un árbol de decisión este un modelo bastante usado porque es fácil de entender y además porque

**[1:27:29]** lo puedo dibujar básicamente lo que estoy haciendo es crearme un árbol y cada en cada paso cada

**[1:27:38]** bifurcación lo que estoy haciendo es hacer una regla y los que no cumplen esa regla se van para

**[1:27:42]** un lado y los que si cumplen esa regla se van para el otro lado hasta que llegó a las hojas

**[1:27:46]** ok que cada una tiene su clase entonces llegue por ejemplo a una hoja en esta hoja va a ser

**[1:27:52]** clasificada con la clase 1 otra hoja con la clase 2 esta otra hoja con la clase 3 y

**[1:27:57]** esta otra hoja con la clase 1 y así entonces es muy visible como lo ocupo como es un modelo

**[1:28:06]** de árboles voy a entrar a ese calderón punto 3 y me voy a voy a ocupar el de clasificación

**[1:28:14]** que todos tienen su versión también de regresión voy a ocupar mi decisión 3 clasificado entonces

**[1:28:23]** esto es muy repetitivo como lo ocupo me creo mi instancia del modelo aquí lo estoy creando

**[1:28:29]** en esta variable que se llama dt con parámetros por defecto luego tengo que hacer el punto fit

**[1:28:35]** y le paso los datos de entrenamiento algo interesante es que en la accediendo literalmente a la librería

**[1:28:43]** árboles existe una función que se llama plot 3 que significa dibujar árbol y yo le puedo

**[1:28:49]** pasar mi modelo y me puede mostrar como es el modelo por dentro y cada es bastante

**[1:28:58]** profundo no tiene bastante niveles entonces cada nodo de cerquita y ahí está como el mejor

**[1:29:23]** resolución un poquito de mejor resolución entonces por ejemplo aquí me está diciendo que el atributo

**[1:29:30]** 0 si es menor o igual a 5.55 si eso es verdad se va para acá y aquí hace otra pregunta en el atributo

**[1:29:37]** 1 hace una pregunta y para acá se va a otra cosa así voy viendo como el proceso del modelo

**[1:29:45]** entonces por eso es muy querido este algoritmo porque lo puedo ver maravilloso y para predecir es

**[1:29:52]** exactamente igual que como habíamos visto antes la instancia punto predic y le paso el conjunto

**[1:29:57]** y aquí yo puedo dibujar mi scatter plot de las etiquetas verdaderas versus las etiquetas

**[1:30:03]** y puedo hacer lo mismo para evaluar mi reporte de clasificación o mi matriz de confusión que

**[1:30:12]** veo que aquí tengo un problema porque me estoy equivocando lo veo visualmente solo por colores

**[1:30:15]** solo por los colores veo que me estoy equivocando más que lo que estaba haciendo en el sbm y creo

**[1:30:23]** que el último es el random forest y el random forest es un bosque y se basa en ocupar el árbol

**[1:30:33]** de decisión porque porque el árbol de decisión como vimos aquí son muchas decisiones anidadas y

**[1:30:38]** entonces un modelo muy muy simple entonces una manera de de ocupar este modelo muy muy simple

**[1:30:47]** y complejizar lo voy a hacer que tenga mejor performance es utilizar muchos de esto pero

**[1:30:53]** que cada cada uno de estos árboles sea distinto que si tuviera todo el rato el mismo árbol no

**[1:30:59]** tiene sentido necesito que sean distintos unos de otros entonces yo voy a utilizar n árboles de

**[1:31:05]** decisión y por cada árbol voy a seleccionar m atributos de manera aleatoria con reemplazo

**[1:31:11]** y entrenamos usando los m atributos para dividir cada nodo y eso me permite hacer que los

**[1:31:16]** árboles sean distintos bueno para sacar la etiqueta voy a ver cuál se repite más en la

**[1:31:26]** mayoría de los arbolitos entonces para entrenar esto como es un está combinando muchos de otro modelo

**[1:31:41]** lo que se llama este tipo de modelo se llama ensembla es un ensamble de modelo tipo ensamble

**[1:31:47]** entonces está en psychic learn punto ensamble aquí van a encontrar otros modelos que también son

**[1:31:52]** así como el xx de boost creo también un ensamble etcétera etcétera como lo ocupamos creamos nuestra

**[1:32:02]** instancia random forest que lo queremos para clasificación así que random forest classified un

**[1:32:08]** hiperparámetro muy como fácil de entender que tiene este modelo es el número de árboles por

**[1:32:14]** defecto es 100 ilumina por favor ahí dice el número de árboles este parámetro que se llama

**[1:32:21]** en estimator y por defecto tiene el valor 100 o sea que por defecto cuando nosotros entrenamos esto va a

**[1:32:27]** tener 100 árboles internamente y va a entrenar esos 100 entonces cuando yo corra esto con el punto

**[1:32:33]** fit se va a entrenar y no se demora nada entonces con esto el árbol ya se entrenó

**[1:32:40]** bueno los árboles ya se entrenaron y puedo predecir normalmente y no me hace ningún problema el

**[1:32:47]** random forest funciona muy muy bien y altamente utiliza y el random forest algo interesante que

**[1:32:58]** tiene es algo que yo puedo le puedo sacar a la instancia que se llama feature importan y

**[1:33:05]** va a tener presión de la corriña voy a darle a darle mi culpa a lo que me pasó antes que

**[1:33:14]** algo corrí mal en el orden y voy a asumir que todo me pasó lo mismo porque yo corrí esto

**[1:33:19]** entero en el respuestas y me funciona todo así que lo voy a ingrar pero que es el feature importan

**[1:33:26]** es básicamente porque me ha mostrado valor si debería mostrarme 4 y algo de ahorita algo de ahorita

**[1:33:36]** en el código algo no corrí totalmente vincula el feature importan es lo que hace es mostrarme

**[1:33:41]** una lista básicamente de la importancia de cada atributo en el modelo entonces normalmente

**[1:33:50]** puedo probar cuando estoy analizando los modelos probar a ver cuál feature tiene la importancia

**[1:33:57]** más baja y tratar de entrenar por ejemplo el modelo sin esos atributos a ver si esos atributos son

**[1:34:02]** inútiles y en realidad solo me están confundiendo a los árboles en una decisión inútil entonces

**[1:34:07]** puedo probar por ejemplo otra instancia del modelo sin utilizar esas dos esos dos atributos

**[1:34:14]** y aquí lo puedo evaluar con mi classification report y aquí tengo un resumen que es básicamente

**[1:34:25]** me muestra todas las matrices las tres matrices de confusión porque porque me sirve más verlo

**[1:34:32]** visual y visualmente veo en la diagonal cuál es el modelo que lo hace mejor así ustedes

**[1:34:38]** me pueden decir solamente viendo las matrices de confusión en el conjunto de test cuál es el

**[1:34:42]** modelo que lo hace mejor el primero el primero el sbm porque porque solamente tengo que observar la

**[1:34:54]** diagonal para darme cuenta que es el que mejor entrega mejor predice cada clase solamente viendo

**[1:35:04]** los valores de la diagonal porque todo se confunde pero este es el que se confunde menos le ganó

**[1:35:12]** si le ganó el ramo pero como dije y el sbm de repente se puede demorar

**[1:35:20]** mucho en el cálculo entonces por ejemplo un hiperparámetro es la máxima cantidad como

**[1:35:28]** iteraciones que hace por dentro y eso se lo puedo bajar que de repente se demora ya para no pasarme

**[1:35:37]** tanto creo que me voy a pasar tres minutitos más dudas hasta aquí porque esto lo pasa igual

**[1:35:42]** rapidísimo con mi cálculo de impacto de la grabación por ahí masticarnos para algunos conservencias

**[1:35:55]** sí pero yo asumo que el profe igual pasó como esto me ha pasado como asumo que pasó

**[1:36:07]** como se formaban los modelos ya pero quizá no quizá no entender tan tan tan a fondo todos los

**[1:36:29]** modelos quizás el que más le llame la atención el que más quieran ocupar pero lo importante es como

**[1:36:33]** entender las métricas qué significa cada métrica al menos qué significa el f1 qué significa el

**[1:36:41]** recall qué significa el precision y cómo se sacan los verdaderos positivos los verdaderos

**[1:36:46]** negativos cómo interpretar una matriz de confusión eso es como súper importante porque en sus

**[1:36:50]** proyectos lo más probable que lo más que el profe pregunte es los resultados y qué

**[1:36:55]** significan los resultados que significa cuando usted hace un plot qué significa eso qué

**[1:37:00]** significa aquello etcétera entonces eso se entiende bien encuentro que estamos bien

**[1:37:08]** veo que pricila tiene la mano levantada

**[1:37:13]** cuéntame y quería volver al tema del análisis de las categorías es que lo que sucede que

**[1:37:21]** tengo una duda

**[1:37:27]** más a la espera en eso

**[1:37:36]** algo es como es como tratar de entender es como que el profesor me comentó de que esa me dijo

**[1:37:45]** cambia tus variables categorica variables numéricas

**[1:37:49]** y lo mismo es un tema para poder entender la intención metodológica

**[1:37:59]** por qué motivo por en porque es la matriz de correlación o sea es más para el modelo que

**[1:38:08]** para la matriz de correlación hacer ese cambio y cuando tú calculas correlación y tienes

**[1:38:18]** variables en estrés la correlación no te la va a calcular te va a calcular la correlación por

**[1:38:23]** defecto si tú haces por ejemplo el tabla punto cor de correlación va a utilizar la correlación

**[1:38:32]** de pierson sino mal recuerdo y por defecto y no va a tomarte en consideración las variables

**[1:38:40]** que estén con letras o te va a dar error o las va a ignorar porque ahora me toca justo

**[1:38:47]** hacer el análisis de variables categorica ya porque ya mi conjunto de gatos ya lo limpié lo

**[1:38:55]** modifique y me arrojó el ssb con el cual estoy trabajando ya para hacer el edad entonces ahí

**[1:39:06]** ya tengo lo cargué en el nuevo notebook porque no sé para el notebook para que no para así

**[1:39:11]** como tan grande y se la descripción de la muestra y se el análisis de la variable objetivo

**[1:39:21]** analice la variable estado porque me tocó sacar una nueva variable ya una una nueva variable

**[1:39:30]** desde la variable objetivo porque era como como es una nota era como aprobado o reprobado

**[1:39:37]** entonces a lo pasada estado de aprobado aprobado y hice la relación entre las variables y por

**[1:39:47]** eso ahora me toca hice la matriz de correlación me toca hacer la matriz de correlación perdón me

**[1:39:52]** toca hacer lo tengo ahí apuntado como me toca las variables categorica porque ya hice las

**[1:39:58]** variables numéricas entonces ahí voy a tener que cambiar hacer esta modificación cierto o

**[1:40:03]** sea en esta parte donde yo tengo que incorporar lo que el profe me dijo era que la matriz de

**[1:40:10]** correlación me ante bien normalmente tendría que hacer un get dummies porque así vas a ver qué

**[1:40:18]** pasa cuando tu variable es un valor y qué pasa cuando no es ese valor y así va a medir la correlación

**[1:40:25]** la correlación va a ser cuando el valor si cuando el valor importa eso para la clase o no

**[1:40:29]** importa ya si y ahí tenía mi duda porque por lo que había leído y todo por el tema de poder

**[1:40:37]** entender cuál era la intención metodológica del profesor que era lo que él quería para porque en mí

**[1:40:44]** pensaba desde lo poquito y nada que se desinicia la tarea recién aprendiendo yo pensé que

**[1:40:51]** sigo utilizar más en el modelo pero no la matriz de correlación por eso pero tu etiqueta es

**[1:40:57]** un string tu etiqueta es categóricas

**[1:41:04]** entonces lo que más te aconsejo es que hagas el tipo de gráficos que vimos para el iris

**[1:41:11]** este tipo de gráficos y que pintes por clase que analizan las variables y que pintas por clase

**[1:41:17]** para ver qué variables potencialmente te separan las clases pero es importante que pasa así que

**[1:41:25]** sacarás correlación y pasarás por ejemplo las variables a números conocederos 1 2 3 4 ahí

**[1:41:32]** podrías ver una correlación falsa porque te darías cuenta no sé pues te daría que la correlación

**[1:41:35]** entre más aumenta este valor se relaciona más con no sé algo nada que ver que lo tenga que ver

**[1:41:43]** con el peso porque te creo que mandarina tengo un peso va pero algún algún valor que no tenga

**[1:41:48]** nada que ver con eso podría crearte una correlación falsa como te digo que esto que el valor de esto

**[1:41:55]** aumente cuando yo paso manzana roja a uno y manzana verde a dos esto es ficticio yo lo creé manzana verde

**[1:42:02]** podría estar en uno y manzana roja podría estar en dos y iré igual de correr por eso no quiero

**[1:42:09]** sacar correlaciones cuando tengo así por eso las quiero sacar con el get damis solamente para

**[1:42:15]** decir si es manzana roja no es manzana roja si es manzana verde no es manzana así perfecto pero

**[1:42:23]** recuerda que si es en la clase puede en la etiqueta final me refiero a decir en la etiqueta que tú

**[1:42:29]** quieres decir puedes hacer esto y para este análisis ya ocupan los gráficos lo gráfico

**[1:42:36]** es la mejor manera de verlo para la variable numérica ocupe gráfico saque

**[1:42:47]** perfecto si el histograma saque la simetría saque el boxplot

**[1:42:57]** está súper bien igual quizá como tiene variable numérica quizá también sacarle

**[1:43:02]** la correlación con respecto a no mentía tendría que hacer a ver de que gupe se espirman

**[1:43:10]** pero realmente con la no me acuerdo cómo funciona cuando la clase numérica hacer esto

**[1:43:16]** gráfico hacer esto gráfico tendría que hacer para analizarla con respecto también ponen el análisis

**[1:43:21]** de la clase no solamente cómo se comporta sino si es útil para separar la clase linealmente

**[1:43:27]** porque relacionan los lineales no puedo ver si porque lo que estaba pensando yo el análisis que

**[1:43:35]** quiero hacer de la variable categorica va en relación con la variable objetivo o sea dentro de entonces

**[1:43:42]** ahí yo decía no hay que pasar la numérica pero si no no se van a no van a conversar en ningún

**[1:43:48]** momento y la relación como que muchas gracias me quedó mucho más claro de nada gracias a

**[1:44:00]** ti ya no sé si hay más duditas tenía una duda con alguien alguien me quedó nada por alguien

**[1:44:08]** no me acuerdo pero sé que tengo una duda pendiente era yo yo sí era yo no sé por qué pensé que me

**[1:44:25]** había quedado otra duda pendiente bueno ya entonces si no hay nada más dejaríamos la clase

**[1:44:32]** hasta aquí para no pasarme más tiempo que estén muy muy bien que tengan buen fin de semana

**[1:44:37]** recuerden que queda todo grabado por si quedaron dudas me pueden escribir no hay problemas

**[1:44:57]** tengo dos personas hay alguna duda y está viendo como como salir igual muchas gracias por la clase

**[1:45:08]** porque de verdad lo vimos en lo vimos hoy en la clase con el profesor pero la clase práctica

**[1:45:14]** no va a servir muchísimo para proyectar como decía tú así que muy gracias me quedó que estén muy

**[1:45:21]** bien igual o en fin de igual me queda una una persona tienes alguna duda voy a dar las

**[1:45:41]** dos manitos y si no si pasan las dos manitos y no pasa nada voy a finalizar la clase ya

**[1:45:59]** asumo que no hay más dudas entonces voy a finalizar la clase adiós
