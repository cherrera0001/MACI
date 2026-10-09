# Recorrido paso a paso: el desafío y cada prueba que hicimos

Este documento cuenta, en orden, qué pide el concurso y qué hicimos para resolverlo: cada prueba, qué
esperábamos, qué salió y qué decidimos después. Sirve para dos cosas: retomar el trabajo sin releer todo, y
aprender cómo se itera en un desafío de Kaggle.

- **Estado al:** 2026-10-09, 18:20 UTC.
- **Registro de cada corrida:** [`REGISTRO_DE_PRUEBAS.md`](REGISTRO_DE_PRUEBAS.md).
- **Versión visual, pensada para publicarse en la web:** [`desafio_kaggle_gemma4.html`](desafio_kaggle_gemma4.html). Es una sola página y no depende de este documento.
- **Solo agregados:** no hay enunciados, parches, pruebas ni identificadores de tareas.
- **Documentos hermanos:** la evaluación crítica está en [`README.md`](README.md); el registro vuelta por
  vuelta, con predicciones, en [`BITACORA_MEJORA.md`](BITACORA_MEJORA.md).

---

## 0. El caso en seis preguntas

| Pregunta | Respuesta corta |
|---|---|
| ¿Qué plantea Google? | Convertir un modelo abierto y pequeño, Gemma 4, en un agente fiable que corrija problemas reales de código sin depender de la nube. Dos pistas: código (nota por tareas resueltas) y artículo (cinco criterios) |
| ¿Qué pregunta buscamos resolver? | La de ALL: si un agente convierte su experiencia en instrucciones, ¿resuelve más tareas? Y antes, la que la hace medible: ¿qué diferencia entre dos configuraciones se distingue de repetir una sola? |
| ¿Qué datos usamos? | Las 129 tareas públicas con su copia del repositorio y sus grafos; la tabla pública; 112 notebooks públicos; nuestros logs. La solución oficial solo se usa para comprobar que una tarea sirve |
| ¿Qué ofrecemos? | Una medición del instrumento (71 de 129 tareas sirven en el notebook oficial, y por qué), un método para no confundir ruido con mejora, y herramientas abiertas para validar sin GPU |
| ¿Qué hemos enviado? | El kit oficial con cuatro ajustes y nada entrenado, dos veces: 0,06 y 0,05 (4 y 3 de 58). Después, el mismo kit con razonamiento encendido, 60 llamadas y 4,5 min, también dos veces: 0,08 y 0,13 (5 y 8 de 58). Ningún artículo todavía |
| ¿Cuál es el artículo? | «Cuánto se puede creer una diferencia»: validez de las tareas, ruido entre ejecuciones y predicciones escritas antes de correr. El borrador del 2026-10-04 no se puede publicar como está (cinco revisores, 2026-10-07); se reescribe en inglés. Cierre: 2026-11-12, 3 000 palabras |

El detalle de cada respuesta está en la [versión visual](desafio_kaggle_gemma4.html).

---

## 1. El desafío en una página

**Qué se entrega.** Un archivo `submission.zip` que describe un agente: sus instrucciones, sus herramientas,
sus subagentes y, si se quiere, adaptadores entrenados. No se entrega código que corra libre ni predicciones.

**Qué hace Kaggle con eso.** Carga el modelo Gemma 4 (fijo, igual para todos) y pone al agente a corregir
errores reales de repositorios de Python. Por cada tarea, el agente lee el problema, explora el código, edita
y entrega un parche. Unas pruebas ocultas dicen si el parche resuelve la tarea.

**Cómo se pone la nota.** La nota es la fracción de tareas resueltas.

| Dato | Valor |
|---|---|
| Tareas públicas, para practicar | 129, de 4 repositorios de código abierto |
| Tareas ocultas, con las que se pone la nota | Unas 120, de repositorios privados |
| Tareas de la tabla pública | 58 |
| Cuánto vale una tarea en la tabla | 0,017 |
| Tiempo máximo para todo el envío | 12 horas |
| Envíos | 1 por día |
| Cierre de la pista de código | 2026-12-02 |
| Cierre de la pista de artículo | 2026-11-12 |

**La nota se trunca a dos decimales.** Un 0,06 son 4 tareas de 58; un 0,13 son 8.

**Por qué es difícil.** Lo que vemos (129 tareas de 4 repositorios conocidos) no es lo que se evalúa
(repositorios privados). Y con 58 tareas, una o dos de diferencia entre dos envíos pueden ser azar.

**Qué buscamos nosotros.** El concurso es el marco. Lo que se quiere mostrar es *Agents Learning Loops*
(ALL): si la experiencia acumulada de un agente, convertida en instrucciones, mejora su resultado. Para
afirmarlo hay que poder medir una mejora y distinguirla del ruido. Casi todo este recorrido trata de eso.

---

## 2. Las piezas que hay que entender

| Pieza | Qué es | Por qué importa |
|---|---|---|
| El modelo | Gemma 4, servido en cuatro GPU L4 | No se puede cambiar. Tarda 12 min 45 s en cargar |
| El arnés | El programa del organizador que corre al agente y verifica el parche con pytest | Es el instrumento de medida. Si mide mal, todo lo demás mide mal |
| El sandbox | El entorno aislado donde corre cada tarea | En el notebook oficial es de tipo subproceso, no un contenedor |
| El presupuesto | Minutos, llamadas a herramientas, turnos y segundos por comando, por tarea | Decide cuándo se corta al agente |
| La cola de GPU | La espera antes de que Kaggle ejecute un notebook con GPU | De 3 a 8 horas. Marca el ritmo de todo |
| La cuota | 30 horas semanales de GPU; la máquina de cuatro L4 gasta el doble | Se reinicia el 2026-10-10 |

---

## 3. Cómo iteramos

Cinco reglas, que salieron de errores propios:

1. **Un cambio por corrida.** Si cambian dos cosas, no se sabe cuál causó el resultado.
2. **La predicción se escribe antes.** Así el resultado puede contradecirnos.
3. **Un cambio se conserva solo si mejora más que el ruido.** El ruido se mide repitiendo la misma
   configuración dos veces en la misma sesión.
4. **Todo lo que no necesita el modelo se valida sin GPU.** Una corrida con GPU cuesta horas de cola; un error
   de ruta de archivos no puede descubrirse ahí.
5. **Se rescata todo lo que Kaggle entrega.** Logs, salidas, tabla, envíos y notebooks públicos.

---

## 4. Las pruebas, en orden

### Prueba 1 — Primer envío (2026-10-03)

- **Qué se probó.** El kit oficial ajustado: sin adaptadores, 4 minutos y 40 llamadas por tarea.
- **Por qué ajustado.** El foro mostró que el kit sin cambios falla o corre con un presupuesto mínimo.
- **Resultado.** 0,06: 4 tareas de 58.
- **Lección.** Leer el foro antes de enviar. Mi primer consejo fue «enviar el kit tal cual» y habría
  desperdiciado el envío del día.

### Prueba 2 — El servidor del modelo cae en el notebook (2026-10-04, madrugada)

- **Qué se probó.** Arrancar el modelo en un notebook propio para medir sin gastar envíos.
- **Resultado.** El servidor cayó dos veces antes de quedar listo y el error no quedó guardado.
- **Causa del error perdido.** El arnés borra su log cuando el servidor no arranca.
- **Qué se hizo.** El notebook ahora guarda la salida que trae la propia excepción. Se validó provocando dos
  fallos distintos en local.
- **Lección.** Un fallo sin su mensaje de error obliga a repetir la prueba. Capturar el error es parte de la
  prueba.

### Prueba 3 — Simulacro sin GPU

- **Qué se probó.** Si el zip enviado es mecánicamente correcto: que el arnés lo cargue, que el agente pueda
  llamar herramientas, y que un parche correcto se reconozca como resuelto.
- **Cómo.** Un modelo falso que responde lo que se le programa, en lugar de Gemma. Corre en un computador
  normal en minutos.
- **Resultado.** 8 de 8 comprobaciones pasan. El zip no está roto.
- **Lección.** Separar «el envío está mal armado» de «el modelo no resuelve». La primera pregunta no necesita
  GPU.

### Prueba 4 — ¿Las tareas públicas sirven para medir? (CPU, 65 minutos)

- **Qué se probó.** Cada una de las 129 tareas, dos veces: sin parche y con el parche oficial. Una tarea sirve
  si falla sin parche y pasa con él.
- **Resultado.**

| Repositorio | Tareas | Sirven para medir |
|---|---|---|
| rich | 48 | 42 |
| fastapi | 67 | 29 |
| requests | 13 | 0 |
| httpx | 1 | 0 |
| Total | 129 | 71 |

- **Otros dos resultados de la misma corrida.** Con 60 segundos por comando no cambia ningún veredicto (0 de
  71). La verificación tarda 4,4 segundos de mediana.
- **Decisión.** Medir solo sobre tareas que sirven; el conjunto de desarrollo son 15 tareas de rich.
- **Lección.** Antes de medir al agente, medir el instrumento.

### Prueba 5 — Primera corrida con el modelo: tres intentos

| Intento | Espera en cola | Qué pasó |
|---|---|---|
| Versión 1 | 8 h 20 min | Se detuvo: encontró 0 archivos de instalación. Kaggle monta los datos en dos disposiciones distintas y el notebook solo conocía una |
| Versión 2 | — | Cancelada antes de correr: tenía la misma ruta fija y habría fallado igual |
| Versión 3 | 3 h 12 min | Corrió completa |

- **Qué se hizo entre la 1 y la 3.** Una guardia al inicio del notebook que busca los datos en cualquiera de
  las dos disposiciones y se detiene con un mensaje claro si no los encuentra. Se probó en local contra el
  árbol real de archivos de Kaggle.
- **Resultado de la versión 3.**

| Medida | Valor |
|---|---|
| Carga del modelo | 764,5 s |
| Tiempo por tarea | 1,62 min, de 4 disponibles |
| Tokens generados por turno | 57 |
| Tokens de entrada por petición | Unos 9 900 |
| Tareas resueltas | 0 de 2 |
| Tarea 1 | Usó 39 de 40 llamadas, sin parche |
| Tarea 2 | Entregó un parche que no pasa las pruebas |

- **Predicción refutada.** Yo había predicho que las tareas no resueltas terminarían por tiempo agotado.
  Ninguna lo agotó: el límite que aprieta es el de llamadas.
- **Lección.** Ocho horas de cola perdidas por una ruta de archivos. Desde entonces la guardia se prueba sin
  GPU antes de subir.

### Prueba 6 — Cancelar corridas en cola

- **Problema.** Kaggle permite 2 sesiones de GPU a la vez y la API pública no cancela.
- **Qué se encontró.** Una llamada interna de la API que cancela una sesión si se conoce su identificador.
- **Resultado.** La versión 2 se canceló así y liberó la plaza.

### Prueba 7 — Leer a los demás (2026-10-04, tarde)

- **Qué se hizo.** Bajar los 112 notebooks públicos del concurso y tabular su configuración.
- **Resultado.**

| Dato | Valor |
|---|---|
| Equipos en la tabla | 1 709 |
| Mediana | 5 tareas de 58 |
| Máximo | 14 tareas |
| Nuestro envío | 4 tareas |
| Notas que declaran los notebooks públicos | De 3 a 8 tareas |
| Error estándar con 58 tareas y tasa cercana al 10 % | Unas 2,3 tareas |

- **Tres hallazgos.**
  1. Nuestro 4 no se distingue del 6 del kit más copiado: estamos en la base, no por debajo.
  2. El envío público con más nota usa dos agentes en secuencia: uno que solo lee y deja un plan corto, y otro
     que edita y verifica. Quita la búsqueda por similitud porque llena el contexto.
  3. Otro participante ya hizo nuestra prueba 4 en su propio entorno y, reparando dependencias, obtiene 114
     tareas que sirven, no 71.
- **Lección.** Los notebooks públicos son datos. Leerlos el primer día habría ahorrado una semana.

### Prueba 8 — Leer el código del arnés

- **Pregunta.** ¿Por qué en 55 tareas el parche oficial no pasa?
- **Qué dice el código.** En el sandbox de subproceso, el arnés se salta la instalación de dependencias por
  tarea, y el entorno se crea sin pip. Todas las tareas de un repositorio se prueban contra los paquetes que
  traiga el notebook.
- **Estado.** Confirmada para 34 de las 55 por la prueba 10. Antes de eso: dos lecturas independientes del código coinciden. Dos cruces de
  datos (por fecha y por versión declarada de una dependencia) no separan las tareas que fallan de las que
  pasan.
- **Qué falta.** El mensaje de error real de pytest. Lo recoge la prueba 10.
- **Una corrección mía.** Afirmé que la evaluación oculta usa contenedores. No tenía evidencia: la nota se
  calcula en un notebook de Kaggle, donde lo probable es el mismo sandbox.

### Pruebas 9, 10 y 11 — En curso

| Prueba | Qué compara | Estado a las 21:33 UTC |
|---|---|---|
| 9. `sesion-unica-a` | Enviada dos veces y enviada con razonamiento, 20 tareas de rich | Corriendo con GPU |
| 10. `validez-causa-cpu` | El error real de pytest en cada tarea | **Terminó.** Ver abajo |
| 11. `iteracion-01` | Enviada, diseño público de dos agentes, enviada, 100 llamadas; 15 tareas de rich | En cola de GPU |
| Segundo envío | El mismo zip otra vez, para ver el ruido de la tabla | Sin nota todavía |

Las predicciones de cada una, escritas antes de correr, están en la bitácora (P1 a P9).

### Prueba 10 — El error real (CPU, 25 minutos)

- **Resultado.** En 34 de las 55 tareas, todas de fastapi, los tests no llegan a ejecutarse porque falta un
  paquete que solo usan los tests: uno falta en 27 tareas y otro en 7.
- **Por qué faltan.** No vienen entre los archivos de instalación de la competencia, y el entorno del notebook
  no instala dependencias por tarea.
- **Qué descarta.** La pista de la versión de starlette. La conjetura correcta fue la de la otra sesión: decide
  qué importa cada archivo de tests.
- **Qué queda abierto.** Las otras 21 (requests 12, rich 6, fastapi 2, httpx 1): son tests que fallan, no
  paquetes que faltan.
- **Uso práctico.** Instalando esos dos paquetes en el notebook de medición se podrían recuperar hasta 34
  tareas: de 71 a un máximo de 105.
- **Lección.** Dos cruces de datos indirectos no separaron nada. Leer el mensaje de error lo resolvió en 25
  minutos.

---

### Pruebas 9 y 11 — La primera medición completa con el modelo

- **Resultado.** La configuración enviada resuelve 3 de 15 y 4 de 16 tareas de rich, igual al repetirla. El
  razonamiento con 4 minutos resuelve una menos y gasta el doble. El diseño público de dos etapas resuelve las
  mismas. Con 100 llamadas resuelve una menos.
- **Ruido.** Entre dos pasadas iguales cambian 2 tareas.
- **Predicciones propias refutadas.** Que 100 llamadas ayudarían, y que el diseño público ganaría.
- **Lección.** Escribir la predicción antes fue lo que permitió ver que estaba equivocada.

### Prueba 12 — Instalar lo que falta (CPU, 73 minutos)

- **Resultado.** Con tres paquetes de pruebas instalados, las tareas válidas pasan de 71 a 103. Ninguna de las
  71 se pierde.
- **Lección.** Una causa se confirma interviniendo, no solo leyendo.

### Prueba 13 — El concilio: tres revisores independientes

- **Qué se hizo.** Antes de gastar cuota, tres revisores intentaron refutar la hipótesis ZorzALL: uno con la
  literatura, uno con estadística y simulaciones, y uno leyendo y ejecutando el arnés.
- **Resultado.** «Solo con cambios». La regla de decisión estaba mal planteada, una de las hipótesis era en
  parte una tautología, y dos afirmaciones sobre el arnés eran falsas.
- **De paso.** No hay límite oficial por tarea: solo 12 horas para todo el envío.
- **Lección.** Pedir que te refuten antes de gastar la cuota.

### Prueba 14 — El oído, en local

- **Qué se probó.** Si un envío puede llevar dentro los paquetes de pruebas que faltan.
- **Resultado.** Sí. En tres tareas de muestra, las pruebas que el agente puede cargar pasan de 1 032, 690 y
  2 927 a 3 083, 2 486 y 3 711.
- **Límite.** Sandbox local, tres tareas. Mide que el agente puede oír, no que resuelva más.

### Prueba 15 — Auditoría de los propios resultados

- **Qué se hizo.** Recalcular todo desde los datos crudos antes de subir otra corrida.
- **Resultado.** La tabla se sostiene. Dos afirmaciones no: «sesiones sin edición» contaba solo una
  herramienta, y el mecanismo del aviso se había presentado como general.
- **Lección.** Auditar lo propio antes de construir encima.

### Prueba 16 — Qué separa lo resuelto de lo no resuelto (sin GPU)

- **Qué se hizo.** Cruzar los resultados con los enunciados y con las copias de los repositorios.
- **Resultado.**

| Enunciado | Tareas | Resueltas alguna vez | Pasadas resueltas |
|---|---|---|---|
| 250 caracteres o más | 6 | 5 | 22 de 42 |
| Menos de 250 | 10 | 0 | 0 de 66 |

- **Y además.** En las tareas cortas, buscar las palabras del título deja el archivo correcto primero en 6 de
  9. Ubicar no es el obstáculo; falta saber qué cambiar.
- **Lección.** La respuesta estaba en datos que ya teníamos. Tres hipótesis sobre el agente salieron de mirar
  al agente; la que explicaba el resultado salió de mirar las tareas.

### Prueba 17 — `iteracion-02`, en cola

- **Qué pregunta.** Qué hace el agente al adelantar el aviso o al pedírselo por escrito, y si en las tareas
  cortas llega a leer el archivo correcto.
- **Estado.** Subida el 2026-10-05 a las 02:21 UTC. Su ficha está en el registro de pruebas.

---

### Prueba 17 — resultado (2026-10-05)

- **Qué salió.** 2, 2 y 4 de 15. El tope de 20 llamadas resuelve lo mismo con la mitad de tokens. La regla
  escrita no adelanta la edición; sus 2 tareas de más son las que cambian solas entre pasadas iguales.
- **Qué dejó.** En las tareas cortas el agente lee el archivo correcto en 6 de 9 y no sabe qué cambiar.

### Pruebas 18 y 19 — La misma configuración dos veces, con trazas (`iteracion-03` y `04`, 2026-10-06)

- **Qué preguntan.** Si el corte por largo del enunciado se sostiene en tareas no vistas, y cuánto ruido hay.
- **Qué salió.** 6 y 7 de 30 (rich 3 y 3; fastapi 3 y 4). Enunciado corto: 0 de 15 en las dos. Cambia de
  resultado 1 tarea de 30; cambia de clase de fallo en 13 de 30.
- **Qué dejó.** Por primera vez se guardaron las trazas. Con ellas se vio que el agente llama a `edit_file` sin
  `old_string` en 160 de 202 llamadas y queda atrapado repitiéndola en 3 de 30 sesiones.

### Prueba 20 — Leer lo público por la API (sin GPU, 2026-10-06)

- **Qué se bajó.** 121 notebooks públicos, 12 comentarios en ellos, 134 temas del foro con 304 comentarios y
  10 temas de cola y GPU de Product Feedback. Todo por la API oficial, sin navegador.
- **Qué dejó.** Otro equipo ya reportaba el mismo fallo de edición. Dos equipos informan que las reglas
  escritas no rompen los bucles. Una herramienta no declarada termina la tarea: no conviene quitar herramientas.

### Prueba 21 — Una línea para la herramienta de edición (`iteracion-05`, 2026-10-06)

- **Qué pregunta.** Si con una línea en la instrucción dejan de quedar sesiones atrapadas.
- **Qué salió.** 0 sesiones atrapadas (base 3 y 3) y 0 llamadas mal formadas de 26. Resueltas: 7 de 30, las
  mismas de la base.
- **Qué dejó.** Un mecanismo puede desaparecer sin que cambie el resultado.

### Prueba 22 — El concilio sobre las 23 tareas nunca resueltas (sin GPU, 2026-10-06)

- **Quiénes.** Cuatro revisores en paralelo: trazas, código, pruebas y foro.
- **Qué salió.** 12 de las 23 eran resolubles; 10 de esas 12 se pierden antes de una edición pertinente. De 41
  sesiones con parche, 16 son parches inertes. Ningún fallo es del entorno.
- **Qué dejó.** Tres correcciones a lo que creíamos: el razonamiento no está medido, las cortas no son
  irresolubles, y la mezcla pública no dice nada de la tabla.

### Prueba 23 — Tercer envío: razonamiento encendido (2026-10-07, 00:26 UTC)

- **Qué se envió.** El mismo kit con razonamiento encendido, 60 llamadas y 4,5 minutos por tarea.
- **Predicción.** Se conserva con 6 tareas o más de 58; con 5 se reenvía; con 4 o menos se descarta.
- **Estado.** Quedó en error de sistema y Kaggle lo volvió a puntuar solo: 0,08, 5 de 58 (leído el
  2026-10-08). Con 5 la regla escrita dice «no decide». Sigue en la prueba 25.

### Prueba 24 — La misma condición en 19 tareas (`iteracion-06`, 2026-10-07, 00:37 UTC)

- **Qué pregunta.** Si con esa condición el agente llega a editar en las tareas resolubles o se queda sin tiempo.
- **Qué salió.** 9 de 19 (base 6, 7 y 7). Tres tareas nunca resueltas antes, dos de enunciado corto; se
  pierde una de las 7 que ya se resolvían. De 10 fallos, 9 agotan el tiempo y ninguno llega a 60 llamadas.
- **Qué dejó.** Primera señal a favor, en una sola corrida y bajo el umbral de 10 fijado antes: no decide.
  El freno pasó de las llamadas al tiempo.

### Prueba 25 — Reenviar el mismo archivo y repetir en notebook (2026-10-07, 16:25 UTC)

- **Qué pregunta.** Si el error era de la configuración o del sistema, y si las tareas nuevas de la prueba 24
  se repiten.
- **Qué salió.** El reenvío estuvo en error hasta el 2026-10-08 y el 2026-10-09 apareció con 0,13: 8 de 58.
  El mismo archivo dio 5 y 8. En el notebook (`iteracion-07`, 10 tareas elegidas por haberse resuelto antes):
  9 de 10, y las 3 nuevas se repiten.
- **Qué dejó.** Un error de Kaggle no es un estado final: el organizador repuntúa. Dos notas por archivo
  (4 y 3; 5 y 8) no bastan para decir que el razonamiento mejora.

### Prueba 26 — Auditar el propio instrumento (sin GPU, 2026-10-08)

- **Qué pregunta.** Si lo afirmado en la bitácora se sostiene cuando lo vuelve a medir alguien que no leyó el
  relato.
- **Qué salió.** Los 145 logs por tarea tenían 0 bytes y el rescate no lo avisaba. Varias cifras se cayeron
  (eran 135 sesiones y no 76). Con 19 tareas y una pasada, una mejora real de 2 tareas se detecta 1 o 2 veces
  de cada 100.
- **Qué dejó.** Se dejó de probar condiciones para arreglar primero el registro. Criterio nuevo, aprobado por
  el dueño: una corrida vale si cada tarea deja sus archivos con contenido; una decisión vale con 60 tareas
  por brazo o 6 discordantes a favor, predicción previa y una repetición de la base.

### Prueba 27 — Diseñar la iteración 08 y ensayarla en local (sin GPU, 2026-10-08 y 09)

- **Qué pregunta.** Cuánto cambia el resultado entre dos pasadas idénticas de la base sobre 60 tareas, con un
  registro que no pierda nada.
- **Qué salió.** Notebooks armados; ensayo local con cortes forzados; tope de 900 s por tarea para que una
  tarea colgada no se lleve la sesión. No se subió.
- **Qué dejó.** Condiciones de lanzamiento sin cumplir, entre ellas repetir el ensayo con la versión de
  `ipykernel` de Kaggle y la orden del dueño.

### Prueba 28 — En qué se van las llamadas (sin GPU, 2026-10-09)

- **Qué pregunta.** La del dueño: ¿es coherente gastar 31 de 40 llamadas sin resolver? ¿Quién controla cada
  llamada?
- **Qué salió.** Cerca del 45 % de las llamadas contadas no trae información nueva (1 822 de 4 086):
  repeticiones, lecturas con el argumento mal formado, búsquedas vacías (300 de 300) y un subagente que no
  resolvió ninguna de sus 7 sesiones. Nadie juzga una llamada: el arnés solo lleva un contador total, el
  reloj y los turnos.
- **Qué dejó.** El kit K «interfaz limpia» (sin subagente, sin grafo, sin la línea que ordenaba la búsqueda),
  armado y sin enviar; retira 7,9 % de las llamadas y se juzgará por criterio mecánico. El concilio pasó a
  tener una segunda ronda en que cada rol lee a los demás. El dato se había medido cuatro veces sin
  convertirse en acción.

### Prueba 29 — Leer la tabla y a los demás otra vez (sin GPU, 2026-10-09)

- **Qué salió.** 2 188 equipos; nosotros 8 tareas, puesto oficial 544. La tabla premia el número de envíos:
  con uno, el 10 % de los equipos llega a 0,13 o más; con diez, el 53 %. Los que declaran más nota usan de 5
  a 8 minutos por tarea; nuestro tope de 4 minutos es nuestro, no del concurso (12 h para unas 120 tareas).
  Ningún notebook público declara más de 0,18.
- **Qué dejó.** Los minutos por tarea y el uso del envío diario pasan al concilio de la vuelta 43.

---

## 5. Qué sabemos y qué no

Al 2026-10-09, 18:20 UTC.

| Afirmación | Estado |
|---|---|
| El zip enviado está bien armado | Medido |
| El modelo arranca y el agente opera en Kaggle | Medido |
| En el notebook, 71 de 129 tareas públicas sirven para medir; 103 instalando tres paquetes de pruebas | Medido, dos veces |
| El entorno del notebook explica 34 de las 55 tareas que no sirven | Medido, y confirmado al instalar los paquetes |
| Por qué fallan las otras 23 | Sin medir |
| Cuánto cambia el resultado entre dos corridas iguales | Medido: 2 de 16, 2 de 15 y 1 de 30 tareas |
| El mismo envío da notas distintas | Medido dos veces: 4 y 3 de 58; 5 y 8 de 58 |
| Un envío en error no tiene nota | No: los dos en error recibieron nota después, sin reenviar |
| En qué se van las llamadas | Medido por dos líneas independientes: cerca del 45 % no trae información nueva |
| Los registros de las corridas estaban completos | No: 145 de 145 logs por tarea con 0 bytes; corregido en el rescate |
| La clase de fallo de una sola pasada es fiable | No: cambia en 13 de 30 tareas entre pasadas iguales |
| El límite que aprieta es el de llamadas | Sin razonamiento, sí, y es síntoma del gasto sin avance; con razonamiento aprieta el reloj |
| El diseño de dos agentes resuelve más | Medido una vez: 3 frente a 3 de 15 |
| El razonamiento encendido ayuda | Sin decidir: 9 de 19 en notebook y notas de 5 y 8 frente a 4 y 3. Cambia tres cosas a la vez y dos notas por archivo no bastan |
| Más minutos por tarea ayudan | Sin medir por nosotros; otros declaran más nota con 5 a 8 minutos |
| Con enunciado corto el agente no resuelve nada | Cierto con el razonamiento apagado (0 de 16 tareas). Con razonamiento se resolvieron 2, en una corrida |
| Las tareas cortas son irresolubles | No: 7 de 15 lo eran, según un revisor |
| Quitar el fallo de la herramienta de edición resuelve más | Medido una vez: no, 7 de 30 igual que la base |
| El conjunto oculto se parece al público | El organizador dice que se depuró aparte; sin medir |

---

## 6. Qué sigue

1. Cerrar el concilio de la vuelta 43: minutos por tarea, uso del envío diario y los siete hallazgos medidos
   que siguen sin decisión.
2. Cumplir las condiciones de lanzamiento de la iteración 08 y pedir la orden del dueño. La cuota se repone el
   2026-10-10.
3. Decidir con el dueño qué se envía y cuándo: nada se sube sin su orden.
4. Firmar el manuscrito en inglés (PR #150 de ALL, 2 995 palabras, APA 7, PDF de 12 páginas) cuando lleguen
   los dos resultados pendientes, y enviarlo como Writeup antes del 2026-11-12.

---

## 7. Errores nuestros que cambiaron el método

| Error | Qué se cambió |
|---|---|
| Recomendar un envío sin leer el foro | Foro y notebooks públicos primero |
| Entregar informes en lugar de arreglar | Leer el código, medir y entregar el cambio probado |
| Subir un notebook con una ruta fija | Guardia probada en local contra el árbol real |
| Perder el error del servidor | El notebook guarda la salida de la excepción |
| Dos sesiones haciendo el mismo trabajo sin coordinarse | Un responsable por pieza; los hallazgos se dejan en el issue |
| Afirmar algo del entorno oculto sin evidencia | Separar en cada afirmación lo medido de lo supuesto |
| Dar por final un error de Kaggle con una sola lectura | Cada lectura de envíos se guarda con su hora; un vigía avisa al abrir sesión si algo cambió |
| Decir «hay logs» sin mirar su tamaño | El rescate cuenta un archivo vacío como faltante |
| Medir cuatro veces el mismo problema sin actuar | Registro de hallazgos: ninguno pasa dos vueltas sin decisión escrita |
| Un concilio en que nadie lee a nadie | Segunda ronda cruzada, con los informes anonimizados |
| Documentos de entrada dos días atrasados | Se actualizan en el mismo paso que la bitácora |

---

## 8. Preguntas para trabajar

Sin respuesta aquí: son para resolver en papel.

1. Un envío resuelve 4 de 58 tareas y otro 6 de 58. Calcula el error estándar de cada tasa. ¿Puedes afirmar
   que el segundo es mejor?
2. La prueba 4 dio 71 tareas que sirven y otro participante obtuvo 114. Nombra dos razones por las que ambas
   cifras pueden ser correctas a la vez.
3. En la prueba 11 la configuración enviada se corre dos veces. ¿Qué mide la diferencia entre esas dos
   pasadas, y por qué no basta con correrla una vez?
4. El modelo usó 39 de 40 llamadas y le sobró más de la mitad del tiempo. ¿Qué dos explicaciones distintas son
   compatibles con ese dato, y qué conteo las separaría?
5. Medimos sobre rich y la nota se pone sobre repositorios privados. ¿Qué tipo de error de validación es ese,
   y en qué se parece a entrenar y evaluar con años mezclados?
