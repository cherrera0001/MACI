# Recorrido paso a paso: el desafío y cada prueba que hicimos

Este documento cuenta, en orden, qué pide el concurso y qué hicimos para resolverlo: cada prueba, qué
esperábamos, qué salió y qué decidimos después. Sirve para dos cosas: retomar el trabajo sin releer todo, y
aprender cómo se itera en un desafío de Kaggle.

- **Estado al:** 2026-10-05, 02:25 UTC.
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
| ¿Qué hemos enviado? | El kit oficial con cuatro ajustes y nada entrenado, dos veces. Primera nota: 0,06 (4 de 58). Ningún artículo todavía |
| ¿Cuál es el artículo? | «Agents Learning Loops con Gemma 4: cuánto se puede creer una diferencia antes de convertir una lección en instrucción del agente». Borrador, sin enviar |

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

## 5. Qué sabemos y qué no

| Afirmación | Estado |
|---|---|
| El zip enviado está bien armado | Medido |
| El modelo arranca y el agente opera en Kaggle | Medido |
| Con el razonamiento apagado el modelo escribe muy poco por turno | Medido, en 2 tareas |
| En el notebook, 71 de 129 tareas públicas sirven para medir | Medido, una vez |
| Nuestro resultado está dentro del ruido del kit público | Calculado con la tabla |
| El límite que aprieta es el de llamadas | Indicio, 2 tareas |
| El entorno del notebook explica 34 de las 55 tareas que no sirven | Medido |
| Por qué fallan las otras 21 | Sin medir |
| El diseño de dos agentes resuelve más tareas que el nuestro | Sin medir; es la prueba 11 |
| El razonamiento encendido ayuda | Sin medir; es la prueba 9 |
| Cuánto cambia el resultado entre dos corridas iguales | Sin medir; pruebas 9 y 11 |

---

## 6. Qué sigue

1. Decidir si se instalan los dos paquetes que faltan para medir sobre más tareas.
2. Leer las pruebas 9 y 11. Si el diseño de dos agentes gana por más que el ruido, pasa a ser la base.
3. Sobre esa base, probar un cambio de ALL: una instrucción derivada de experiencia, frente a un texto de
   relleno del mismo largo.
4. Enviar a Kaggle solo lo que ganó en la medición propia.

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
