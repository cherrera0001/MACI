# Caso: un desafío tipo Kaggle desde cero — Gemma 4 Developer Agent

Evaluación crítica del experimento `Agents Learning Loops/experiments/gemma_developer_agent`
y, sobre ese caso, el flujo paso a paso para enfrentar un desafío de este tipo.

- **Empieza aquí:** [`desafio_kaggle_gemma4.html`](desafio_kaggle_gemma4.html), la página visual del
  desafío, con una calculadora de ruido. Después, el
  [recorrido paso a paso](RECORRIDO_PASO_A_PASO.md) de cada prueba.
- **Fechas:** primera evaluación el 2026-10-03 (día 11 de la competencia); segunda el
  2026-10-04 a las 00:10 UTC; estado actualizado el 2026-10-04 a las 21:33 UTC (sección 1.6) y el
  2026-10-05 a las 02:25 UTC (sección 1.7); la última actualización es del 2026-10-09 a las 18:20 UTC
  (sección 1.10).
- **Qué se leyó:** el `README.md` del experimento, los dos pre-registros, los registros de
  corridas (`data/test_results_*`, `artifacts/control-vacio-*`, `calibracion/`), la configuración
  del kit, las páginas oficiales guardadas en `data/pages/`, el `HARNESS_README`, y por API de
  Kaggle: mis envíos, las primeras 20 filas de la tabla y tres notebooks públicos.
- **Qué no contiene este documento:** enunciados, parches, pruebas ni identificadores de tareas;
  solo agregados y cifras públicas de la tabla. El 2026-10-04 el dueño aprobó tratar el conjunto
  de datos según su licencia Apache 2.0; este documento se mantiene en agregados igualmente.

**Documentos del caso**

| Documento | Para qué sirve |
|---|---|
| [`desafio_kaggle_gemma4.html`](desafio_kaggle_gemma4.html) | El desafío explicado de forma visual e interactiva |
| [`RECORRIDO_PASO_A_PASO.md`](RECORRIDO_PASO_A_PASO.md) | Cada prueba en orden: qué se probó, qué salió, qué se decidió |
| [`BITACORA_MEJORA.md`](BITACORA_MEJORA.md) | Registro por vuelta, con las predicciones escritas antes de correr |
| [`REGISTRO_DE_PRUEBAS.md`](REGISTRO_DE_PRUEBAS.md) | Una fila por corrida subida a Kaggle y por envío, con la ficha de la que está en curso |
| [`HIPOTESIS_ZORZAL.md`](HIPOTESIS_ZORZAL.md) | La hipótesis ZorzALL y lo que cambió tras la revisión independiente |
| Este `README.md` | Evaluación crítica del experimento y flujo general de un desafío |
| [`INSTRUCCION_CLAUDE_CODE.md`](INSTRUCCION_CLAUDE_CODE.md) | Instrucción para la otra sesión; fechada, ver su nota de vigencia |
| [`REVISION_MANUSCRITO_2026-10-04.md`](REVISION_MANUSCRITO_2026-10-04.md) y [`REVISION_PROYECTO_2026-10-04.md`](REVISION_PROYECTO_2026-10-04.md) | Revisiones fechadas; ver su nota de vigencia |

---

## 0. Qué ejercicio se evalúa, exactamente

Hay tres cosas distintas con nombres parecidos. Este documento evalúa la tercera.

| Qué | Qué es | De quién |
|---|---|---|
| **El concurso** | *Google – The Gemma 4 Developer Agent Competition* en Kaggle. Pista de código (id 149921, cierra 2026-12-02) y pista de artículo (id 163111, cierra 2026-11-12) | Google DeepMind |
| **El proyecto** | *Agents Learning Loops* (ALL): estudia si un agente puede reutilizar su experiencia. Sus resultados previos (H4, #58, H6, H7) son de un solver sin modelo de lenguaje | Cristobal |
| **El experimento** | `experiments/gemma_developer_agent`: usa el concurso como marco para una pregunta propia, medida en local con las tareas públicas | Cristobal |

**La versión evaluada** es la de `main` en el commit `4af63cc` (2026-10-03), que es la que
describe el `README.md` del experimento.

**Las dos preguntas del experimento**, con su estado en esa versión:

| Pregunta | Estado |
|---|---|
| **Línea base A.** Con el kit oficial sin cambios, ¿cuánto varía el resultado al repetir la misma corrida sobre las mismas tareas, y qué diferencia entre dos condiciones no se distingue de esa variación? | **Pre-registrada** y fijada. Sin ejecutar |
| **Campaña A/B/C/D.** ¿Unas skills consolidadas a partir de episodios con Gemma mejoran la resolución en otro repositorio, frente al kit (A) y frente a un texto de relleno de igual longitud (B)? D añade la instrucción de usar el grafo de código | **Propuesta** del issue #104, **sin pre-registro**. Estimador y predicción «por fijar». Sin ejecutar |

**Lo que el ejercicio no es**, según su propio README:

- No es una prueba de la memoria asociativa de ALL: esa pregunta se retiró porque en este arnés
  cada tarea corre aislada y quien «recuerda» es el modelo leyendo un archivo fijo.
- No busca una nota alta en la tabla, ni afirma nada sobre el conjunto oculto.
- No entrena adaptadores LoRA.
- No prueba que un agente aprenda: prueba si unos documentos estáticos derivados de experiencia
  ayudan.

**Nota de versión.** Mi primera lectura fue sobre un árbol de trabajo local que incluía un
borrador sin fusionar de la rama `docs/kaggle-campana-104`: un pre-registro de la campaña con
estimador «mayoría estricta» y la predicción de que H(C, A) no quedaría apoyada. Eso **no está en
`main`**. Donde este documento citaba ese borrador, quedó corregido y señalado.

---

## 1. Estado y veredicto al 2026-10-04 00:10 UTC

> **Lo vigente está en la sección 1.10 (2026-10-09).** Las secciones 1.1 a 1.9 son historia fechada.

### 1.1 Qué cambió desde la primera evaluación

| Qué | Antes | Ahora |
|---|---|---|
| Envíos a Kaggle | 0 | **1**, enviado el 2026-10-03 23:46 UTC (ref. 56808559), estado «pendiente» |
| Foro y notebooks | Sin leer | Leídos: unos 17 hilos y 4 notebooks, resumidos con fuentes en #103 |
| Concurrencia de la puntuación | Sin medir | Secuencial, según el staff en el foro |
| Tamaño de la tabla pública | «Unas 60» | 58 tareas: una tarea vale 0,017 |
| Decisión de cómputo (#101) | Abierta | Cerrada: notebooks de Kaggle, L4×4, 0 USD, 30 h semanales |
| Corridas propias con el modelo | 0 | **0**. Cuota de GPU usada: 0,00 de 30 h |
| Código nuevo | — | Unas 2 460 líneas más: figuras del artículo y empaquetado de envíos, con sus pruebas |

### 1.2 Lo que se hizo bien en este tramo

1. **Se envió.** Es el primer contacto del experimento con la medición real.
2. **Se leyó el foro antes de enviar, y cambió la decisión.** El kit sin cambios da error o corre
   con 1 minuto y 10 llamadas por tarea; sus adaptadores tienen pesos en cero y reducen el
   contexto; con `max_output_tokens` 16 384 el servidor rechaza prompts largos. Se envió un kit
   ajustado: sin adaptadores, 8 192 tokens de salida, 4 minutos y 40 llamadas por tarea.
3. **Se rotuló con honestidad.** El envío se anotó en #106 como exploratorio, no como réplica de
   la línea base pre-registrada, y con la advertencia de que sus valores no salen de una regla.

**Corrección a mi primera evaluación.** Recomendé «enviar el kit tal cual». Era un mal consejo:
ese zip habría gastado el envío del día en un error o en una nota sin valor. La lectura del foro
lo evitó. La lección es de orden: foro primero, envío después.

### 1.3 Lo que sigue mal

1. **Cero corridas propias y la cuota de la semana sin tocar.** Las 30 h de GPU se reinician el
   2026-10-10 y no se acumulan. El ensayo de notebook (compuerta C0.5), del que depende todo el
   pre-registro, sigue sin ejecutarse.
2. **El registro no coincide con lo enviado.** `submissions/registry.json` contiene un solo
   envío, `sub-001`: el kit con adaptadores, estado «preparado». El zip que de verdad se envió
   (3 495 bytes, `d8a3e1d3…`) está en una carpeta que git ignora y consta solo en un comentario
   de #106. El instrumento creado para registrar envíos no registró el único envío.
3. **El empaquetador aprueba sin comprobar.** La supervisión detectó que `compile_with_adk()`
   devuelve éxito cuando no encuentra el compilador. Un control que aprueba en vacío es peor que
   no tener control.
4. **La condición A pre-registrada ya no es ejecutable como está.** El pre-registro define A como
   el kit con un solo archivo cambiado. El foro muestra que ese kit falla o desperdicia contexto.
   Hace falta una enmienda corta que redefina A antes de la primera réplica; si no, la línea base
   medirá una configuración que nadie usaría.
5. **El trabajo sigue yendo a lo que no es el cuello de botella.** Desde la primera evaluación:
   1 742 líneas para figuras de un artículo sin resultados de Gemma, correcciones de procedencia
   del `recall`, un agente nuevo (`zorzal`) y el pre-registro de H8. Hay 34 árboles de trabajo
   y cuatro PR abiertos.
6. **El congelamiento no se respeta.** La supervisión ordenó no fusionar durante el experimento y
   después se fusionaron tres PR (#125, #127 y #128). Una regla que su propio dueño salta deja de
   ser regla; o se levanta, o se cumple.
7. **Datos con procedencia discutida.** El PR #130 atribuye la cuota a una «lectura del panel por
   el dueño» cuando se leyó por API; el episodio 051 da 59,85 h donde el comando da 54,27 h.
   Son detalles, pero son justo el tipo de detalle que el proyecto dice cuidar.
8. **La potencia de la campaña sigue igual** (paso 6). Y ahora hay un dato más: un mismo zip dio
   0,12 y 0,15 en la tabla, es decir, 7 y 9 tareas de 58.

### 1.3 bis Actualización de las 01:40 UTC

De la lista anterior ya están resueltos los puntos 2, 3 y 4: el registro contiene el zip
enviado, el empaquetador falla sin compilador y la Enmienda 2 redefine A como el kit ajustado.
Se versionó a las 00:47 UTC, con el envío aún pendiente.

Lo nuevo es un bloqueo: en el notebook de Kaggle el servidor del modelo cae antes de quedar
listo (a los 474 s y a los 753 s) y el error no se leyó. La cuenta sí obtiene cuatro GPU L4. Cuota
usada: 0,87 h de 30. El plan vigente, con el ciclo de mejora, está en
[`INSTRUCCION_CLAUDE_CODE.md`](INSTRUCCION_CLAUDE_CODE.md).

### 1.4 Riesgo del envío en curso

La puntuación es secuencial y, si excede las 12 horas, el envío entero da error. Con 4 minutos de
agente por tarea, el total depende del montaje por tarea, que no está medido en Kaggle:

| Tareas | Montaje por tarea | Total, sin la carga del modelo |
|---|---|---|
| 116 | 1,0 min | 9,7 h |
| 116 | 2,0 min | 11,6 h |
| 120 | 1,5 min | 11,0 h |
| 120 | 2,0 min | 12,0 h |

Si el montaje ronda 1 minuto hay holgura; si se acerca a 2, el envío puede fallar. No todas las
tareas agotan los 4 minutos, lo que ayuda. Si llega un error en vez de una nota, esta es la
primera causa a descartar.

### 1.5 Veredicto

El proyecto dio el paso correcto y lo dio bien. Sigue sin un solo resultado propio, y la
proporción entre aparato y datos empeoró en vez de mejorar. La prioridad no cambió: un número
real, y después otro.

### 1.6 Estado al 2026-10-04 21:33 UTC

Las secciones 1.1 a 1.5 describen la madrugada del 4 de octubre y quedan como historia. Esto es lo vigente.

| Qué | A las 00:10 UTC | A las 21:33 UTC |
|---|---|---|
| Nota del primer envío | Pendiente | **0,06: 4 tareas de 58** |
| Segundo envío (mismo zip) | — | Enviado a las 17:41 UTC, sin nota todavía |
| Corridas propias con el modelo | 0 | **1**: carga en 764,5 s; 0 de 2 tareas; 1,62 min por tarea |
| Servidor del modelo en el notebook | Caía sin dejar el error | Arranca; el notebook guarda el error si cae |
| Tareas públicas que sirven para medir | Sin medir | **71 de 129** en el entorno del notebook |
| Tabla pública | Primeras 20 filas | Completa: 1 709 equipos, mediana 5, máximo 14 |
| Notebooks públicos | 4 leídos | 112 bajados; 62 arman un envío |
| Cuota de GPU usada | 0,87 h | Unas 2,5 h de 30, más una sesión corriendo |

**Lo que cambió en el diagnóstico.**

1. **Ya hay resultados propios.** La debilidad principal de las secciones 1.3 y 5 (cero corridas) dejó de
   ser cierta. Siguen siendo pocos: una corrida de 2 tareas no mide una tasa.
2. **Nuestro 4 está dentro del ruido del kit público.** Los notebooks públicos declaran entre 3 y 8
   tareas, y el error estándar es de unas 2,3.
3. **El límite que aprieta es el de llamadas, no el de tiempo.** Indicio de 2 tareas: el agente usó 39 de
   40 llamadas en 100 segundos, con el razonamiento apagado y 57 tokens por turno.
4. **El instrumento tiene un defecto probable.** En el entorno del notebook, el arnés no instala
   dependencias por tarea. Explicaría las 55 tareas donde la solución oficial no pasa. Sin confirmar.
5. **El envío público con más nota usa otro diseño:** dos agentes en secuencia. Está en cola la corrida que
   lo compara con el nuestro.

**En curso.** `sesion-unica-a` (razonamiento, GPU, corriendo), `validez-causa-cpu` (el error real de las
tareas que no sirven, CPU, corriendo) e `iteracion-01` (diseño de dos agentes y 100 llamadas, en cola).

**Veredicto actualizado.** El proyecto pasó de construir aparato a medir. Lo que falta es lo que nombra el
paso 5: cuánto cambia el resultado entre dos corridas iguales. Hasta tener ese número, ninguna mejora puede
afirmarse.

### 1.7 Estado al 2026-10-05 02:25 UTC

Lo vigente. La sección 1.6 queda como historia del día anterior.

| Qué | A las 21:33 UTC del día 4 | A las 02:25 UTC del día 5 |
|---|---|---|
| Envíos con nota | 1: 4 de 58 | 2 del mismo archivo: 4 y 3 de 58 |
| Corridas completas con el modelo | 0 | 2: `sesion-unica-a` e `iteracion-01` |
| Tasa en tareas públicas de rich | Sin medir | 3 de 15 y 4 de 16, igual en las pasadas repetidas |
| Ruido entre dos pasadas iguales | Sin medir | 2 tareas |
| Tareas válidas para medir | 71 | 103, instalando tres paquetes de pruebas |
| Límite oficial por tarea | Se suponía que había | No hay: solo 12 horas para todo el envío |
| Nombre de la propuesta | — | ZorzALL |
| En cola | — | `iteracion-02` |

**Lo que se aprendió, en orden de importancia.**

1. **Lo que separa las tareas resueltas de las que no es el largo del enunciado.** Con 250 caracteres o más: 5
   de 6 tareas resueltas alguna vez (22 de 42 pasadas). Con menos: 0 de 10 (0 de 66 pasadas). Los enunciados
   cortos son un título y una referencia que el agente no puede abrir; son el 36 % de las tareas públicas.
2. **En las tareas cortas, ubicar el archivo no es el obstáculo.** Buscar las palabras del título lo deja
   primero en 6 de 9. Falta saber qué cambiar.
3. **Ningún ajuste probado resuelve más:** ni el razonamiento con 4 minutos, ni 100 llamadas, ni el diseño
   público de dos etapas. Todas las comparaciones se decidieron en 6 tareas.
4. **El bucle es un síntoma.** La mitad de las llamadas repite una idéntica, sobre todo en las tareas cortas.
5. **El agente rinde tres o cuatro veces mejor en tareas públicas que en la tabla** (20 a 25 % frente a 6 %).

**Lo que se corrigió de afirmaciones propias.** El tope de 100 llamadas no ayudó; «sesiones sin edición»
contaba mal; el mecanismo del aviso no es general; la regla de decisión «ruido más una tarea» estaba mal
planteada; el costo de la fase 3 son 17 horas de cuota y no 9. El detalle está en la bitácora.

**Veredicto actualizado.** El proyecto ya mide, y medir mostró dónde está el problema: no en el presupuesto ni
en el diseño del agente, sino en un tercio de las tareas donde el enunciado no dice qué corregir. Ahí está la
palanca, y todavía no hay un candidato probado para moverla.

---

### 1.8 Estado al 2026-10-07 01:20 UTC

Lo vigente. La sección 1.7 queda como historia; cuatro de sus afirmaciones se corrigen abajo.

| Qué | A las 02:25 UTC del día 5 | A las 01:20 UTC del día 7 |
|---|---|---|
| Envíos | 2 del mismo archivo: 4 y 3 de 58 | 3: el tercero (56895202, razonamiento encendido, 60 llamadas, 4,5 min) está pendiente de nota |
| Corridas con el modelo terminadas | 2 | 7 |
| Conjunto de medición | 15 tareas de rich | 30: las 15 de rich y 15 de fastapi no vistas |
| Resueltas en ese conjunto | 3 de 15 y 4 de 16 | 6, 7 y 7 de 30 en tres pasadas |
| Ruido entre dos pasadas iguales | 2 tareas de 15 | 1 tarea de 30; la clase de fallo cambia en 13 de 30 |
| Enunciado corto | 0 de 10 tareas | 0 de 16 tareas, replicado en fastapi no vistas (0 de 6) |
| Cambios de configuración probados | 3 | 6 con resultado; ninguno resuelve más |
| Predicciones escritas antes de correr | 11 | 40: 19 cumplidas, 11 refutadas, 3 sin poder leerse, 1 sin correr, 6 pendientes |
| Cierre | Sin leer | Code Track 2026-12-02; Paper Track 2026-11-12, 3 000 palabras |
| Tabla pública | 1 709 equipos, mediana 5 | 1 935 equipos, mediana 6; envío propio en el puesto 1 503 |
| Cuota de GPU | 13,4 h usadas de 30 | Estimado: unas 2 h libres hasta el reinicio del 2026-10-10 |

**Lo que se aprendió desde la 1.7, en orden de importancia.**

1. **El agente no falla por el contenido del parche sino antes.** De 23 tareas nunca resueltas en tres pasadas,
   un revisor juzgó 12 resolubles con el enunciado y el repositorio. En 10 de esas 12 el agente no llega a una
   edición pertinente: 6 no leen el archivo correcto y 4 lo leen sin editarlo.
2. **El límite que ata es el de llamadas.** 36 de 69 sesiones fallidas llegan a 40 llamadas; 4 terminan por
   tiempo. La mitad de las llamadas repite una idéntica.
3. **Quitar un fallo real no recupera tareas.** Una línea en la instrucción dejó en cero las llamadas a
   `edit_file` sin `old_string` (107 y 49 en la base) y se resolvieron las mismas 7 de 30.
4. **La herramienta de lectura pierde el rango de líneas en 4 de cada 10 llamadas**, y la búsqueda por
   similitud no devuelve nada en 209 de 209. Gastan llamadas; no separan resueltas de no resueltas.
5. **Lo público no representa lo oculto.** El organizador dice que las tareas ocultas se depuraron aparte.
6. **Ningún fallo de verificación es del entorno.** De 41 sesiones con parche, 16 son parches inertes y en 23
   de las 25 restantes el agente pasa cero pruebas objetivo.

**Lo que se corrigió de la 1.7.**

- «En las tareas cortas, ubicar el archivo no es el obstáculo»: demasiado fuerte. Buscando palabras del título
  el archivo sale primero en 6 de 9, pero el agente no llega a leerlo en 10 de las 23 nunca resueltas.
- «Un tercio de las tareas donde el enunciado no dice qué corregir» como palanca: retirado. 7 de las 15 cortas
  eran resolubles, y el conjunto oculto no tiene por qué traer esa mezcla.
- «Ningún ajuste resuelve más, tampoco el razonamiento»: el razonamiento solo se midió con 4 minutos, donde 11
  de 13 sesiones se quedaron sin tiempo, y el envío lo llevaba apagado. No está medido en condiciones válidas.
- «El agente rinde tres o cuatro veces mejor en lo público»: el dato sigue, la lectura cambia. No es que la
  tabla sea más difícil por tener tareas cortas; es otro conjunto.

**El manuscrito.** Cinco revisores lo leyeron el 2026-10-07: no se puede publicar como está. Sus tablas
coinciden con sus fuentes, pero dice «no hemos ejecutado Gemma 4», da por desconocida la causa de las tareas
que no sirven y por no repetida la medición de validez; las tres cosas son falsas hoy. Se reescribe en inglés,
sobre lo medido. Detalle en la vuelta 35 de la bitácora.

**Manuscrito nuevo, 01:55 UTC.** En inglés, 2 995 palabras, citas en APA 7 y PDF de 12 páginas: PR #150 del
repositorio de ALL, en borrador. Pasó tres rondas de revisión y está sin firma del validador sobre su versión
exacta. La suite de revisión quedó en el repositorio (PR #149): dos roles nuevos, un comprobador automático
del manuscrito y el generador del PDF. Detalle en la vuelta 36.

**Primer resultado a favor, 02:13 UTC del día 7 (`iteracion-06`).** Con razonamiento encendido, 60 llamadas y
4,5 minutos, 9 de 19 tareas (base 6, 7 y 7). Tres de ellas nunca se habían resuelto, dos de enunciado corto:
las primeras en 138 sesiones. Se pierde una de las 7 que ya se resolvían. Es una sola corrida y queda bajo
el umbral de 10 que se fijó antes: no decide. El freno pasó de las llamadas al tiempo: 9 de 10 fallos agotan
los 4,5 minutos. Detalle en la vuelta 37.

**Veredicto actualizado.** El proyecto mide bien, sabe dónde se pierde el agente y tiene su primera señal de
mejora, todavía sin confirmar. La confirma o la desmiente la nota del envío pendiente, que lleva esa misma
condición.

### 1.9 Estado al 2026-10-07 16:00 UTC

Superado por la 1.10. Ningún resultado nuevo de Kaggle: un concilio de seis roles releyó `iteracion-06` y corrige tres
lecturas de la 1.8. Detalle en la vuelta 38 de la bitácora.

| Qué | A las 02:35 UTC | A las 16:00 UTC |
|---|---|---|
| Envío 56895202 | Pendiente | **Terminó en error, sin nota** (leído a las 15:55 UTC). La API no da la causa; el texto del error está en la página de envíos |
| Cuota de GPU | Unas 2 h libres (estimado) | 2,36 h libres (leído por la API); reinicio el 2026-10-10 |
| Tabla pública | 1 935 equipos, mediana 6 tareas | 1 981 equipos; mediana 6, percentil 75 en 7, percentil 90 en 8; nosotros 4, puesto 1 559 |
| Siguiente corrida | Sin armar | `iteracion-07` armada y ensayada sin GPU; no subida |
| README del repositorio de ALL | Decían que el modelo nunca corrió | Corregidos en un PR, con cada cifra referida al manuscrito |

**Lo que se corrigió de la 1.8.**

- «El freno pasó de las llamadas al tiempo»: es el desenlace, no la palanca. De las 6 sesiones cortadas por
  tiempo con parche, ninguna había acertado y 5 solo tenían guiones propios. Más tiempo recuperaría 2 tareas
  como máximo.
- «La edición llega antes»: contaba guiones. El razonamiento no cambió cuántas tareas resolubles editan el
  archivo correcto (3 de 12 en las cuatro pasadas).
- Lo que el razonamiento sí cambió: las 12 resolubles leen el archivo de la corrección (antes 6 o 7) y las
  llamadas repetidas bajan del 40 a 50 % al 7 %.

**Lo que se aprendió.** El agente con razonamiento encuentra el archivo, escribe guiones en vez de editarlo
y agota el reloj esperando al modelo. El subagente no resolvió nada en 6 sesiones y le costó una tarea ya
resuelta. Bajar el presupuesto de razonamiento casi no ahorra tiempo.

**Sobre el principio de ALL.** El ciclo de mejora no pasó por el bucle: ninguna vuelta consultó la memoria
antes de actuar, ninguna corrida tiene episodio y ningún envío lleva una lección consolidada. La primera
condición que lo pondría a prueba (una skill con una lección medida, contra un texto de relleno) queda tercera
en el orden de medición.

**El envío con razonamiento dio error.** P39 (termina dentro de las 12 h) queda refutada y P38 no se puede
leer. La condición no se conserva para enviar; la señal de 9 de 19 en notebook sigue como dato. El reenvío
del mismo zip queda retirado.

**Decisiones que esperan al dueño.** Leer en la página de envíos el texto del error del 56895202: sin él no
se sabe si fue el plazo de 12 h. Con ese dato, qué medir con las 2,36 h que se pierden el día 10
(`iteracion-07` tal como está, o el razonamiento con un tope menor). Qué hacer con el issue #103 del repositorio: reformularlo o cerrarlo.

### 1.10 Estado al 2026-10-09 18:20 UTC

Lo vigente; sustituye a la 1.9. Detalle en las vueltas 38 a 42 de la bitácora. Desde el 2026-10-07 16:26 UTC
no se subió ni se envió nada a Kaggle: lo nuevo son notas que Kaggle puso por su cuenta y trabajo local.

| Qué | El 2026-10-07 a las 16:00 UTC | El 2026-10-09 a las 18:20 UTC |
|---|---|---|
| Envío 56895202 (`i_razona`) | Error, sin nota | **0,08: 5 de 58.** Kaggle lo volvió a puntuar solo (leído el 2026-10-08 a las 21:37 UTC) |
| Envío 56916129 (el mismo zip) | Sin enviar | Enviado el 2026-10-07 a las 16:25 por orden del dueño; en error hasta el 2026-10-08 a las 22:31; **0,13: 8 de 58** (leído el 2026-10-09 a las 13:42) |
| Notas del equipo | 0,06 y 0,05 | Sin razonamiento, 40 llamadas y 4 min: 4 y 3 de 58. Con razonamiento, 60 llamadas y 4,5 min: 5 y 8 de 58 |
| Tabla pública | 1 981 equipos; nosotros 4 tareas, puesto 1 559 | 2 188 equipos; 8 tareas, puesto oficial 544; 277 equipos con más nota. Mediana 0,10 y máximo 0,24 (14 tareas, 2 equipos) |
| `iteracion-07` | Armada, sin subir | Corrió: 9 de 10. Las diez se eligieron por haberse resuelto antes, así que no se compara con los 9 de 19; las 3 nuevas de la 06 se repiten (3 de 3) |
| Kit K «interfaz limpia» | No existía | Armado y registrado como `sub-004`, **no enviado**: la base sin subagente, sin las tres herramientas de grafo y sin la línea que ordenaba la búsqueda |
| Iteración 08 | No existía | Diseñada (la base dos veces sobre 60 tareas, con registro nuevo) y armada; **no lista para lanzar** |
| Cuota de GPU | 2,36 h libres | 29,53 h usadas de 30 (leído a las 21:55 UTC); se repone el 2026-10-10 a las 00:00 UTC |

**Lo que se aprendió en estas vueltas.**

- **Un `error` de Kaggle no es un estado final.** Los dos envíos con razonamiento estuvieron en error de
  sistema y después recibieron nota sin que hiciéramos nada. El organizador repuntúa los envíos que marcó con
  error tras más de 15 h de cola. Desde ahora cada lectura de envíos se guarda con su hora.
- **El mismo zip dio 5 y 8 tareas; el otro, 4 y 3.** Con dos notas por variante no se puede decir que el
  razonamiento mejora: no lo refuta ni lo prueba.
- **La tabla premia el número de envíos.** Con un envío el 10 % de los equipos llega a 0,13 o más; con 10, el
  53 %. La nota que se ve es la mejor de varias tiradas ruidosas. Nosotros llevamos 4 envíos en 6 días.
- **Cerca del 45 % de las llamadas no trae información nueva** (1 822 de 4 086 contadas, en 145 sesiones):
  repeticiones idénticas, lecturas con el argumento mal formado que devuelven el principio del archivo,
  búsquedas por similitud vacías (300 de 300) y llamadas del subagente (0 de 7 sesiones resueltas). Dos
  líneas independientes llegaron a la misma cifra sin leerse. Con tope de 60 llamadas y razonamiento el gasto
  sin avance baja a 14,5 %, en una comparación confundida.
- **Nadie juzga una llamada.** Ni el arnés ni el marco detectan repeticiones, bucles o resultados vacíos; solo
  hay un contador total, el reloj y los turnos. Lo único que el envío puede imponer es la lista de
  herramientas y los cuatro totales de `eval_config.yaml`. De ahí sale el kit K, que retira 324 llamadas
  contadas (7,9 %): se juzgará por criterio mecánico, no por tareas resueltas.
- **Los 4 minutos y 40 llamadas son nuestros, no del concurso.** Lo oficial son 12 h para unas 120 tareas,
  unos 6 minutos de media. Los participantes que declaran más nota (0,17 y 0,18, sin medir por nosotros) usan
  de 5 a 8 minutos. Ningún notebook público declara más de 0,18; los diez equipos con 0,20 o más no tienen
  método público.
- **Ninguna de las siete iteraciones era una corrida válida:** los 145 logs por tarea tenían 0 bytes y el
  rescate no lo decía. Ahora un archivo exigido vacío cuenta como faltante.
- **Con 19 tareas y una pasada no se decide nada:** una mejora real de 2 tareas se detectaría 1 o 2 veces de
  cada 100.

**Criterio vigente, aprobado por el dueño el 2026-10-08.** *Corrida válida:* cada tarea deja en disco, con
bytes, traza, parche, salida de pruebas y motivo de fin. *Decisión válida:* predicción previa con umbral, las
mismas tareas en los dos brazos, 60 tareas o más por brazo o 6 discordantes a favor, prueba exacta y una
repetición de la base en la misma semana. Con menos, el resultado es exploratorio y no cambia lo enviado.

**Fallos nuestros de estas vueltas.** El gasto sin avance se midió cuatro veces en cinco días (vueltas 12,
32, 38 y 42) y no se convirtió en acción hasta que el dueño preguntó por él. Se afirmó «refutada» sobre un
error que no era final. El concilio trabajó dos vueltas sin que un rol leyera a otro; desde la 42 hay segunda
ronda cruzada. Los documentos de entrada (este, el registro y el recorrido) estuvieron dos días sin las notas
0,08 y 0,13.

**Vetado por el concilio 42 como brazo de medición:** exigir una ejecución antes de entregar, el reproductor
antes de editar, el guion-mapa, un tope de exploración (rompería 9 de 39 resueltas) y la regla de no repetir.

**Qué falta para lanzar la iteración 08.** Repetir el ensayo local con la versión de `ipykernel` de Kaggle,
que no está medida; un análisis de la pasada 1 contra la 2 que excluya los pares faltantes; primera subida en
serie; cuota de 14,6 h o más; y la orden del dueño.

**Medición de Datito del 2026-10-09 a las 22:50 UTC, pendiente de cruce por el concilio 43.** Sobre la tabla
pública de las 17:41 UTC (2 188 equipos, 9 526 envíos), con [`instrumentos/tabla_ruido.py`](instrumentos/tabla_ruido.py):

| Pregunta | Respuesta | Tipo |
|---|---|---|
| ¿La tabla es solo suerte? | No. Entre los equipos de un envío la varianza es 6,84 y el puro azar daría 3,89; un modelo de tasa única espera 51 equipos con 10 tareas o más y hay 122 | Medido |
| ¿Se distinguen nuestros dos archivos? | No: 7 de 116 frente a 13 de 116, prueba exacta p = 0,24 | Medido |
| ¿Cuánto sube la nota pública por enviar más veces el mismo archivo? | Un archivo de 6,5 tareas reales da, como mejor nota esperada, 9,0 con 4 envíos, 10,4 con 10 y 12,5 con 54 | Calculado, con ruido binomial |
| ¿Eso mejora el resultado final? | No. Decide la tabla privada con 2 envíos finales: su nota esperada es de unas 8,1 tareas de 60 con 4, 10 o 54 envíos. Solo la sube una tasa real mayor | Simulado; supone que cuenta el mejor de los dos finales |
| ¿Sirve el envío diario para medir? | Sí, y no gasta cuota: 58 tareas del conjunto oculto por día. Alternando dos archivos se detecta, 8 de cada 10 veces, una diferencia de 5,0 tareas con 10 días, de 3,5 con 20 y de 2,0 con los 54 que quedan | Calculado |

Qué significa: parte de la ventaja de los primeros puestos es paciencia y parte es real. Para nosotros, cada día
sin envío es una medición perdida sobre el conjunto que puntúa; un calendario de envíos alternados, fechado
antes de empezar, mediría lo que 19 tareas en un notebook no pueden. Qué archivos alternar y si se hace es
decisión del dueño, después del concilio.

**En curso al escribir esto:** el concilio de la vuelta 43, con la pregunta de cuál es el siguiente paso con
más respaldo, y entre sus dudas los minutos por tarea y qué hacer con el envío diario. Sus resultados irán en
la bitácora y aquí.

**Decisiones que esperan al dueño.** La orden de subir la iteración 08 o de enviar un zip (el kit K u otro):
nada se sube sin ella. El texto para LinkedIn está revisado y sin publicar.

---

## 2. El desafío, leído como problema de ciencia de datos

| Elemento | En esta competencia |
|---|---|
| Qué se entrega | Un `submission.zip` con la configuración de un agente: YAML, prompts, subagentes, skills y, opcionalmente, adaptadores LoRA. No se entrega código propio |
| Modelo | Uno solo, fijo: `gemma-4-31b-it-qat-w4a16-ct` |
| Métrica | Proporción de tareas cuyo parche hace pasar pruebas ocultas (PASS/FAIL por tarea) |
| Datos públicos | 129 tareas de 4 repositorios abiertos: 67, 48, 13 y 1 |
| Datos de la nota | Unas 120 tareas de **repositorios privados**, mitad tabla pública y mitad privada |
| Presupuesto | 12 horas para todas las tareas; 1 envío al día; 2 envíos finales |
| Fechas | Artículo: 2026-11-12. Envío final: 2026-12-02 |

La equivalencia con lo que se ve en Fundamentos de Ciencia de Datos:

| Concepto del curso | Aquí |
|---|---|
| Entrenamiento | Las tareas públicas de los repositorios no reservados |
| Validación | Las tareas públicas del repositorio reservado (`leave_one_repo_out`) |
| Test | La tabla privada: tareas que nadie ve, de repositorios que nadie ve |
| Generalización | Que lo aprendido en tres repositorios sirva en un cuarto que no se vio |
| Sobreajuste | Elegir el envío que mejor puntúa en la tabla pública después de muchos intentos |
| Fuga de datos | Que el parche de referencia o un resultado de prueba llegue al prompt o a las skills |
| Varianza | El mismo envío, repetido, resuelve tareas distintas |

---

## 3. El flujo desde cero, y cómo quedó este caso en cada paso

### Paso 1 — Leer las reglas y la métrica antes de escribir código

**Qué se hace.** Página por página: qué se entrega, cómo se puntúa, qué datos se pueden usar,
cuántos envíos hay, qué fechas mandan.

**En este caso: bien hecho.** La ficha de reglas cita cada afirmación por página y sección, y
detectó dos cosas que muchos participantes pasan por alto: los datos no se pueden publicar, y
cada tarea corre aislada, sin memoria entre tareas.

**Lo que faltó, y ya se corrigió.** El README declaraba: «no se consultaron las páginas vivas ni
el foro». En Kaggle el foro y los notebooks públicos son parte de la documentación. La lectura
se hizo el 2026-10-03 y respondió cómo se envía, la concurrencia y qué pasa al exceder las 12
horas. Siguen sin fuente las preguntas sobre publicar agregados y sobre la cuota.

### Paso 2 — Explorar los datos (EDA)

**Qué se hace.** Tamaño, distribución, desbalances, valores vacíos, qué no sirve.

**En este caso: bien hecho, con cuidado poco común.** Los agregados se calculan sin imprimir
contenido de tareas. Hallazgos que importan:

- El desbalance es extremo: un repositorio tiene 67 tareas y otro tiene 1.
- `hints_text` está vacío en las 129.
- La mitad de los parches de referencia cambia 12 líneas o menos; el percentil 90 es 127.
- 86 de 129 tareas son posteriores al corte de entrenamiento declarado del modelo.

**Lo que no se ha hecho.** Medir qué tareas son válidas (fallan sin arreglo y pasan con el parche
de referencia). El guion existe y tiene más de 2 000 líneas de pruebas, pero nunca corrió con el
verificador real. Otro participante ya publicó una auditoría que deja 119 de 129.

### Paso 3 — Diseñar la validación antes de optimizar

**Qué se hace.** Decidir cómo se va a estimar el rendimiento en datos no vistos. Es la decisión
más importante del flujo: una validación mala hace que todo lo demás optimice ruido.

**En este caso: la mejor decisión del experimento.** Como la nota se calcula en repositorios
privados, una partición al azar mezclaría tareas del mismo repositorio en entrenamiento y
prueba, y mediría algo más fácil que lo que el concurso mide. Reservar un repositorio entero
imita la situación real. Es el mismo principio que la validación temporal estricta del proyecto
de Melbourne: la partición debe reproducir cómo llegarán los datos nuevos.

**Su límite.** Con cuatro repositorios, y solo dos de tamaño útil, hay como mucho dos pliegues.
Un solo repositorio de prueba no separa «repositorio no visto» de «este repositorio en
particular es difícil». El README lo reconoce.

### Paso 4 — Línea base de punta a punta, el primer día

**Qué se hace.** Enviar lo más simple que funcione. Sirve para comprobar que el circuito
completo anda, y entrega el primer número real de la competencia.

**En este caso: dado el día 11.** Un envío exploratorio, pendiente de nota (sección 1).

Lo que la tabla y el foro decían el 2026-10-03 a las 23:00 UTC, según la lectura anotada en #103:

| Dato | Valor |
|---|---|
| Equipos | 1 587 |
| Tabla pública | 58 tareas; una tarea vale 0,017 |
| Arriba | 1 equipo en 0,24 · 5 en 0,17 · 26 en 0,15 |
| Donde está la mayoría | 0,10 (321 equipos), 0,08 (298), 0,12 (241); 129 equipos en 0,00 |
| Ruido observado | Un mismo zip dio 0,12 y 0,15 |
| Mejor configuración pública | 0,12 a 0,15; la de 0,17 y la de 0,24 no son públicas |

Cuatro consecuencias:

1. **La tabla se mueve de a una tarea.** De 0,15 a 0,17 hay una tarea; de 0,12 a 0,15, dos.
2. **La línea base real está entre 0,08 y 0,12**, no en 0,15. Llegar a 0,15 ya es estar entre los
   primeros 32 de 1 587.
3. **El trabajo local sobre Docker en Windows está fuera del camino.** El notebook oficial usa el
   sandbox `subprocess` en Linux.
4. **El presupuesto derivado en el pre-registro (3 a 5 minutos por tarea) era correcto**, y la
   puntuación es secuencial, como se había supuesto.

**Cada envío es una réplica gratis sobre la distribución real.** Reenviar el mismo zip varios
días mide la variación de la nota en 58 tareas de repositorios privados, sin gastar cuota (un
participante reporta que la puntuación no la consume; el staff no lo ha confirmado). Solo entrega
la nota agregada, no el resultado por tarea, así que no reemplaza las réplicas locales: las
complementa.

### Paso 5 — Medir el ruido antes de comparar

**Qué se hace.** Repetir la misma configuración y ver cuánto cambia el resultado. Una mejora
menor que esa variación no es una mejora.

**En este caso: la idea es correcta y está bien fundamentada, pero sin ejecutar.** La pregunta de
la línea base («¿cuánto varía A contra sí misma?») es justo la que casi nadie en la tabla se
hace.

Lo que se puede anticipar con aritmética, sin ninguna corrida. Para una proporción `p` medida
sobre `n` tareas, el error estándar es `sqrt(p·(1−p)/n)`:

| n tareas | p | Error estándar | Intervalo del 95 % |
|---|---|---|---|
| 62 (validación local) | 0,15 | 4,5 puntos | ± 8,9 puntos |
| 62 (validación local) | 0,24 | 5,4 puntos | ± 10,6 puntos |
| 58 (tabla pública) | 0,10 | 3,9 puntos | ± 7,7 puntos |
| 58 (tabla pública) | 0,15 | 4,7 puntos | ± 9,2 puntos |

Solo por el tamaño de la muestra, un envío de 0,15 y uno de 0,24 tienen intervalos que se tocan.

### Paso 6 — Preguntarse si el diseño puede detectar el efecto que busca (potencia)

**Qué se hace.** Antes de gastar cómputo: ¿qué tamaño de efecto espero?, ¿con mis datos lo
distinguiría del ruido?

**En este caso: es el punto débil del diseño.**

- El umbral de lectura del pre-registro tiene un suelo de `6/n`. Con 62 tareas son 9,7 puntos.
- La referencia más cercana que cita el propio README (SkillsBench v1, skills curadas en
  ingeniería de software) es una mejora de 4,5 puntos.
- La campaña no tiene pre-registro en `main`: su estimador y su predicción están «por fijar».
  Un borrador sin fusionar (rama `docs/kaggle-campana-104`) predice que la hipótesis principal
  «no queda apoyada»; es un borrador, no una regla del experimento.

Simulación de una prueba pareada de McNemar con 62 tareas (una corrida por condición; el
estimador de varias corridas aún no está fijado, y agregar réplicas mejoraría algo estas cifras):

| Mejora real | Sin ruido entre corridas | Con 5 % de tareas que cambian en cada sentido |
|---|---|---|
| 4,5 puntos | potencia 0,06 | 0,08 |
| 10 puntos | 0,60 | 0,32 |
| 15 puntos | 0,92 | 0,60 |

Para detectar 4,5 puntos con potencia 0,80 harían falta entre 400 y 800 tareas. Hay 62.

**Lectura.** Esto afecta a la campaña, no a la línea base: la pregunta de la línea base
(cuánto varía A) sí es contestable con estos datos. La campaña, tal como está propuesta, casi
con certeza terminará en «sin diferencia», y
ese resultado no distinguirá entre «las skills no ayudan» y «no había tareas suficientes para
verlo». Un nulo sin potencia no informa. Como la campaña aún no está pre-registrada, este es el
momento de decidirlo.

### Paso 7 — Presupuestar el cómputo

**Qué se hace.** Traducir el diseño a horas de GPU y compararlo con lo disponible.

**En este caso.** La cuota es de 30 horas semanales y la máquina L4×4 la consume al doble.

- Una réplica: 62 tareas × (4,5 min + 1 min de montaje) ≈ 5,7 h de máquina ≈ 11,4 h de cuota.
- Caben unas 2,6 réplicas por semana.
- Tres réplicas de A más dos de B y dos de C son 7 réplicas: unas 80 h de cuota, casi tres
  semanas completas, sin contar el pase de entrenamiento ni los errores.
- El corte de la campaña es el 2026-11-05. La cuota se reinicia el 2026-10-10.

Cabe, sin margen. Cualquier semana perdida elimina una condición.

### Paso 8 — Iterar: una hipótesis, un cambio, un número

**Qué se hace.** Cambiar una cosa, medir, anotar, decidir. Un registro simple de experimentos.

**En este caso: empezó con un envío.** Y el instrumento para hacerlo ya es más grande que el
experimento: cuatro condiciones, nueve parámetros abiertos, una cadena de ocho compuertas,
enmiendas, diario encadenado por hashes y tres agentes supervisándose entre sí.

**Actualización del 2026-10-04.** El ciclo ya funciona con cinco reglas: un cambio por corrida,
predicción escrita antes, conservar solo lo que supera el ruido, validar sin GPU todo lo posible y
rescatar todo lo que Kaggle entrega. Lleva once pruebas; están en el
[recorrido](RECORRIDO_PASO_A_PASO.md) y en la [bitácora](BITACORA_MEJORA.md).

### Paso 9 — Elegir los envíos finales

**Qué se hace.** Se eligen dos. La regla práctica: uno por la validación local y otro por la
tabla pública, y desconfiar de la tabla cuando contradice una validación bien diseñada.

**En este caso: no aplica todavía**, pero el diseño de validación del paso 3 es lo que permitirá
hacerlo con criterio.

### Paso 10 — Escribir lo aprendido

**En este caso.** La pista de artículo se califica en cinco criterios: novedad, calidad,
relevancia, verificabilidad y claridad. El experimento está muy bien parado en verificabilidad y
claridad. Sin ninguna corrida con el modelo, novedad y relevancia quedan vacías: un artículo de
«diseño y resultado previo negativo de otro sistema» difícilmente compite.

**Actualización del 2026-10-04.** Tres cambios. El título del manuscrito pone primero a Agents
Learning Loops, por decisión del dueño. Un notebook público ya publicó la misma medición de validez
con otro resultado (114 de 129 en su entorno); el manuscrito ahora lo cita y delimita lo propio: el
entorno del notebook oficial. Y si se confirma que ese entorno no instala dependencias por tarea, el
hallazgo deja de ser «71 tareas sirven» y pasa a ser «por qué en el notebook oficial solo sirven 71».

---

## 4. Fortalezas

1. **Honestidad del registro.** El README abre con «hoy no hay ninguna corrida con el modelo ni
   ningún resultado» y separa en una tabla lo medido de lo no medido.
2. **Validación por grupos.** Reservar un repositorio completo es la partición correcta para
   este problema.
3. **Ruido primero.** Medir la variación de la línea base antes de comparar condiciones.
4. **Control con placebo.** Un texto de longitud comparable separa «las skills ayudan» de «más
   texto en el prompt cambia algo».
5. **Frontera de fuga explícita.** Quien valida tareas no redacta skills; el parche de
   referencia no entra en prompts ni recibos.
6. **Cumplimiento de reglas.** No se versiona contenido de la competencia y hay un guion que lo
   comprueba.
7. **Revisión del área con evidencia adversa incluida**, no solo la favorable.

## 5. Debilidades, de mayor a menor

1. **Cero ejecuciones propias del modelo en once días**, y un solo envío. *Al 2026-10-04 21:33 UTC:
   una corrida propia de 2 tareas y dos envíos. Sigue sin medirse la variación entre corridas.*
2. **Sin potencia estadística para la pregunta de la campaña** (paso 6). La pregunta de la
   línea base no tiene este problema.
3. **Desalineación con el concurso.** Se excluye LoRA, que es la vía que el concurso nombra, y se
   declara que no se busca nota, en una competencia que ordena por nota.
4. **Proceso antes que datos.** Un pre-registro de 61 KB con reglas para casos que quizá nunca
   ocurran. Pre-registrar protege contra elegir el análisis después de ver los datos; no exige
   prever cada contingencia antes de saber si el modelo carga.
5. **Entorno equivocado.** Esfuerzo en Docker sobre Windows cuando la medición válida, según el
   propio pre-registro, es en el notebook de Kaggle.
6. **Fuentes gratuitas usadas tarde.** Foro, notebooks y tabla se leyeron el día 11.
7. **Transferencia dudosa por construcción.** Skills consolidadas de tres repositorios públicos
   de Python muy conocidos, aplicadas a repositorios privados. Lo que transfiera será lo
   genérico (cómo localizar, cómo verificar), no lo específico de cada proyecto.
8. **El vínculo con ALL es débil en este arnés.** No hay memoria entre tareas, así que lo que se
   prueba es si un archivo fijo ayuda, no si un agente aprende. El README lo dice con claridad.

---

## 6. Qué hacer ahora, en orden

Actualizado el 2026-10-04 a las 21:33 UTC. La tabla anterior se cumplió en lo esencial: la nota llegó, se
reenvió el mismo zip, se hizo el ensayo en el notebook, se enmendó A y se midió la validez.

| Cuándo | Acción | Qué entrega |
|---|---|---|
| Al terminar `validez-causa-cpu` | Leer el error real de pytest por tarea | Confirmar o descartar la causa del entorno |
| Al terminar `sesion-unica-a` | Leer las dos pasadas iguales y la de razonamiento, sin sus 4 tareas no válidas | Primera medida del ruido; efecto del razonamiento |
| Al terminar `iteracion-01` | Comparar el diseño de dos agentes y las 100 llamadas contra el ruido | La base sobre la que se sigue |
| Al llegar la nota del segundo envío | Leerla en tareas junto a la primera | Ruido de la tabla con el mismo zip |
| Después | Un cambio de ALL sobre la base ganadora, frente a un relleno del mismo largo | La pregunta propia del proyecto |
| Regla de envío | Enviar solo lo que ganó en la medición propia | Envíos que aportan información |
| Regla de trabajo | Un responsable por pieza; los hallazgos van al issue | Sin trabajo duplicado entre sesiones |

**Sobre la pregunta del artículo.** Con lo que el diseño sí puede medir bien, hay una pregunta
más pequeña y contestable: *¿cuánto ruido tiene el kit oficial y qué diferencia de la tabla es
distinguible de ese ruido?* Entra en el tema «Tasks & Benchmarks» de la pista de artículo, usa
todo lo ya construido (validez, réplicas, intervalos) y es útil para los 1 435 equipos. La
campaña de skills quedaría como segunda parte, solo si el ruido medido la permite.

**Sobre la nota.** Si además se quiere subir en la tabla, el orden habitual es: presupuesto y
prompt primero (es donde están hoy las diferencias de una o dos tareas), y después trayectorias
exitosas como datos para un adaptador LoRA. Eso hoy está fuera de alcance por decisión propia;
conviene que sea una decisión revisada y no heredada.

---

## 7. Cómo reproducir los números de este documento

```python
from math import sqrt

# Error estándar de una proporción
def ee(p, n): return sqrt(p * (1 - p) / n)
print(ee(0.15, 62), ee(0.24, 62))          # 0.045 y 0.054

# Suelo del umbral de lectura del pre-registro
print(6 / 62)                               # 0.097

# Tareas necesarias para detectar `delta` con una prueba pareada (McNemar),
# alfa 0.05 bilateral, potencia 0.80; `disc` = proporción de tareas discordantes
def n_mcnemar(delta, disc):
    return (1.96 * sqrt(disc) + 0.8416 * sqrt(disc - delta**2))**2 / delta**2
print(n_mcnemar(0.045, 0.10), n_mcnemar(0.045, 0.20))   # 385 y 773

# Cómputo por réplica
horas = 62 * (4.5 + 1.0) / 60
print(horas, 2 * horas, 30 / (2 * horas))   # 5.7 h de máquina, 11.4 h de cuota, 2.6 por semana
```

La tabla y los envíos se leen con la API de Kaggle
(`/api/v1/competitions/gemma-4-developer-agent/leaderboard/view` y
`/api/v1/competitions/submissions/list/gemma-4-developer-agent`), con el token en la variable
`KAGGLE_API_TOKEN`. La vista devuelve 20 filas; la tabla completa se baja como zip y se resume con
`scripts/kaggle_rescate.py` del repositorio del experimento, que también guarda envíos, logs y salidas.

---

## 8. Preguntas para trabajar

Sin respuesta aquí: son para resolver en papel.

1. Un equipo tiene 0,17 y otro 0,15 sobre unas 60 tareas. Calcula el error estándar de cada
   tasa. ¿Puedes afirmar que el primero es mejor?
2. ¿Por qué una partición al azar de las 129 tareas daría una estimación optimista de la nota,
   y en qué se parece ese error a mezclar años en el proyecto de Melbourne?
3. El pre-registro predice que la hipótesis principal no quedará apoyada. Si el resultado es
   «sin diferencia», ¿qué dos explicaciones distintas son compatibles con ese resultado, y qué
   dato haría falta para separarlas?
4. Te quedan 60 envíos, uno por día. Si eliges como final el mejor de los 60 según la tabla
   pública, ¿qué le pasa a la estimación de tu nota privada, y cómo se llama ese fenómeno?
5. La condición B es un texto de relleno del mismo largo que las skills. ¿Qué conclusión
   equivocada permitiría sacar el experimento si B no existiera?
