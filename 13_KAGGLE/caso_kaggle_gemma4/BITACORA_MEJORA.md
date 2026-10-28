# Bitácora del ciclo de mejora — agente Gemma 4 en Kaggle

Una entrada por vuelta. Cada una dice qué se leyó, qué se predijo antes de correr, qué salió y qué se
decide. Solo agregados: sin enunciados, parches, pruebas ni identificadores de tareas.

## Reglas del ciclo

1. Un cambio por corrida.
2. La predicción se escribe antes de conocer el resultado.
3. Un cambio se conserva solo si mejora más que el ruido medido entre dos corridas iguales.
4. Todo lo que no necesita el modelo se valida sin GPU antes de subir: chequeo previo, guardia con el
   árbol real, captura de errores y ensayo con el modelo falso.
5. El conjunto de desarrollo son 15 tareas de rich que discriminan en el sandbox de Kaggle. fastapi queda
   fuera de la mejora.

## Límites reales del ciclo

| Límite | Valor | Fuente |
|---|---|---|
| Espera en cola de GPU | 8 h 20 min y 3 h 12 min en las dos corridas con ese dato | Versiones 1 y 3 de `prueba-a-ajustada` |
| Sesiones de GPU por lotes a la vez | 2 | Cuenta, leído con la sesión web |
| Envíos al concurso | 1 por día | Reglas |
| Cuota de GPU | 30 h semanales; L4×4 cuenta al doble | Kaggle |

Una vuelta completa con el modelo tarda del orden de medio día. El ciclo no puede ir más rápido que eso.

## Punto de partida (2026-10-04)

| Medida | Valor |
|---|---|
| Nota pública del envío actual | 0,06 = 4 de 58 tareas |
| Media de un primer envío en la tabla | 3,83 tareas (413 equipos) |
| Mediana de la tabla | 5 tareas |
| Primer puesto | 14 tareas |
| Tareas públicas que sirven para medir en Kaggle | 71 de 129 (rich 42 de 48, fastapi 29 de 67) |
| Configuración enviada | Razonamiento apagado, 4 min, 40 llamadas, 60 s por comando |

## Vuelta 1 — 2026-10-04, 19:07 a 19:35 UTC

**Estado leído.**

- Envío 56830336 (repetición del mismo zip): pendiente de nota.
- `prueba-a-ajustada` versión 3 (GPU): en cola desde las 16:53 UTC.
- `sesion-unica-a` (GPU): en cola desde las 18:37 UTC; la subió la otra sesión.
- Cuota de GPU: 1,89 h usadas de 30.

**Qué se preparó.** El notebook `iteracion-01`: tres corridas en una sola sesión de GPU sobre las 15
tareas de desarrollo, en este orden: configuración enviada, variante con razonamiento, configuración
enviada otra vez. El modelo se carga una vez.

**Validado sin GPU.**

| Comprobación | Resultado |
|---|---|
| Chequeo previo | Pasa |
| Guardia con el árbol real, dos disposiciones | Pasa |
| Captura del error del servidor, dos tipos de fallo | La causa queda guardada |
| Ensayo local de las celdas nuevas con el modelo falso | Flujo, archivo de resultados y limpieza correctos |
| Parámetros que recibe el modelo por corrida | Apagado, encendido con presupuesto 4 096, apagado |

**Qué no se pudo hacer.** Subirlo: Kaggle respondió «máximo de 2 sesiones de GPU por lotes». Las dos
plazas están ocupadas.

**Hallazgo sobre `sesion-unica-a`.** Corre 20 tareas de rich elegidas antes de conocer la validez: 16
discriminan y 4 no. Esas 4 no pueden salir resueltas. No conviene cancelarla: se pierde el lugar en la
cola, y basta con excluir esas 4 al leer el resultado.

**Predicciones para la primera sesión con el modelo** (escritas antes de cualquier resultado):

| Predicción | La refuta |
|---|---|
| P1. Entre dos corridas iguales cambiarán de resultado entre 1 y 3 de 15 tareas | 0 tareas, o más de 3 |
| P2. La mayoría de las no resueltas terminará por tiempo agotado, con o sin parche | Que la clase más frecuente sea otra |
| P3. Con razonamiento, la diferencia frente a la configuración enviada no superará el ruido de P1 | Una diferencia mayor que las tareas que cambian entre corridas iguales |

**Hipótesis para la vuelta siguiente, sin probar.** El arnés rescata los cambios que quedan en disco
aunque la sesión termine sin entregar. Si la clase dominante es «tiempo agotado sin parche», el cambio a
probar es de instrucciones: editar primero y verificar después. Si es «parche que no pasa», ese cambio no
sirve y hay que mirar la calidad de la edición.

**Decisión.** Esperar. `iteracion-01` se sube en cuanto se libere una plaza de GPU, salvo que
`sesion-unica-a` ya responda lo mismo; en ese caso se reemplaza su plan por el cambio que indique la
tabla de fallos.

## Vuelta 3 — 2026-10-04, 20:16 a 20:45 UTC

**Primer resultado con el modelo.** `prueba-a-ajustada` versión 3 corrió tras 3 h 12 min de cola y terminó
sin error en 18 minutos de sesión.

| Medida | Valor |
|---|---|
| El servidor del modelo arranca con la orden del arnés | Sí |
| Carga del modelo | 764,5 s |
| Dos tareas, tiempo total | 193,9 s; 1,62 min por tarea, de 4 disponibles |
| Peticiones al modelo | 60, ninguna cortada por longitud ni con error |
| Tokens generados | 3 425 en total: 57 por petición |
| Tokens de entrada | 594 018 en total: unos 9 900 por petición |
| Latencia por petición | 2,2 s de media |
| Tarea 1 | No resuelta: 39 llamadas a herramientas de 40, sin parche, 100 s |
| Tarea 2 | No resuelta: 15 llamadas, parche de 2 101 caracteres que no pasa las pruebas, 93 s |

**Contraste con las predicciones de la vuelta 1** (con solo 2 tareas, es un indicio):

- P2 decía que la mayoría de las no resueltas terminaría por tiempo agotado. **No se cumple en estas dos:**
  ninguna agotó el tiempo. Una agotó las llamadas a herramientas y la otra entregó un parche incorrecto.
- P1 y P3 necesitan corridas repetidas; siguen abiertas.

**Lectura.** Con el razonamiento apagado el modelo responde con 57 tokens por turno: llamadas a herramientas
casi sin texto. Gasta sus 40 llamadas en 100 segundos y le sobra más de la mitad del tiempo. El límite que
aprieta es el de llamadas, no el de minutos.

**Cambio elegido para la siguiente corrida: 100 llamadas a herramientas en vez de 40.** Un solo valor de
`eval_config.yaml`. Lo respalda el dato de arriba: a 2,5 s por llamada, en 4 minutos caben unas 95.

**Validado sin GPU.** El candidato compila y el simulacro da el desenlace esperado en sus cuatro modos.

**Predicción, escrita antes de correr** (15 tareas de rich, dos pasadas de cada configuración):

| Predicción | La refuta |
|---|---|
| P4. Con 100 llamadas hay menos tareas que terminan sin parche que con 40 | Igual o más tareas sin parche |
| P5. Con 100 llamadas se resuelven más tareas que con 40, sumando las dos pasadas, y la diferencia supera las tareas que cambian entre las dos pasadas iguales | Una diferencia menor o igual que ese ruido |
| P6. El tiempo por tarea con 100 llamadas sigue por debajo de 4 minutos de media | Una media de 4 minutos o más |

**Decisión.** Subir `iteracion-01` a la plaza de GPU que quedó libre, con el plan: enviada, 100 llamadas,
enviada, 100 llamadas. La comparación con razonamiento la cubre `sesion-unica-a`, que sigue en cola.

## Vuelta 4 — 2026-10-04, 20:55 a 21:20 UTC

**Rescate.** Segunda bajada completa (envíos, tabla, 7 notebooks propios con log y salidas) y, nuevo, los 112
notebooks públicos del concurso con su fuente. El documento `__results__.html` y el notebook ejecutado no los
entrega la API: solo salen con sesión web. El log trae todo lo que imprimen las celdas.

**Dónde estamos.** 1 709 equipos; mediana 5 tareas de 58; máximo 14; nuestro envío 4. Los notebooks públicos
declaran entre 3 y 8 tareas. Con un error estándar de unas 2,3 tareas, nuestro 4 no se distingue del kit.

**Tres hallazgos.**

1. El envío público con más nota (8 tareas) usa dos agentes en secuencia: uno de solo lectura que localiza y
   deja un plan corto, y otro que edita y verifica. Quita la búsqueda por similitud porque inunda el contexto.
   Nuestra corrida midió unos 9 900 tokens de entrada por petición.
2. Un notebook público ya hizo nuestra medición de validez y obtiene 114 tareas válidas de 129 reparando
   dependencias. La nuestra da 71. Coinciden en rich; difieren en fastapi y requests.
3. Causa probable de la diferencia, leída en el código del arnés: el sandbox de subproceso que usa el notebook
   oficial no instala dependencias por tarea. Falta confirmarlo con el error real de pytest.

**Cambio en la corrida en cola.** `iteracion-01` se reemplazó: enviada, referencia pública, enviada, 100
llamadas, sobre las 15 tareas de rich. Guarda además la anatomía de cada sesión en conteos.

**Predicciones nuevas, escritas antes de correr:**

| Predicción | La refuta |
|---|---|
| P7. La referencia pública resuelve más tareas que la enviada, por encima de las que cambian entre las dos pasadas iguales | Diferencia menor o igual que ese ruido |
| P8. La referencia pública usa menos tokens de entrada por tarea que la enviada | Igual o más |
| P9. En la enviada, más de la mitad de las tareas sin parche nunca llegan a editar un archivo | La mitad o menos |

**Decisión.** Si P7 se cumple, la base de trabajo pasa a ser el diseño en dos etapas y las mejoras se miden
sobre él. Si no, se conserva la enviada y se prueba el cambio que indique la anatomía.

## Vuelta 5 — 2026-10-04, 21:20 a 21:45 UTC

**Estado leído.** `sesion-unica-a` pasó a ejecutarse con GPU. `validez-causa-cpu`, de la otra sesión, corre en
CPU. `iteracion-01` sigue en cola. El segundo envío sigue sin nota.

**Decisiones del dueño.**

- Licencia Apache 2.0 del conjunto de datos: aprobada.
- Agents Learning Loops va primero en toda publicación. El título del manuscrito ya lo refleja, en el PR #141.
- Leer la salida de `validez-causa-cpu` cuando termine.

**Corrección propia.** Afirmé que la evaluación oculta usa contenedores. No tenía evidencia: la nota se calcula
en un notebook de Kaggle, donde lo probable es el mismo entorno de subproceso.

**Sin cambio de configuración en esta vuelta.** No hay resultado nuevo que lo respalde.

**Documentación.** Se añadieron la página visual del desafío y el recorrido paso a paso, y se actualizó el
estado del caso.

## Vuelta 6 — 2026-10-04, 21:55 a 22:05 UTC

**Resultado leído.** `validez-causa-cpu` terminó en 25 minutos. En 34 de las 55 tareas donde la solución oficial
no pasa, los tests no se ejecutan porque falta un paquete que solo usan los tests (27 y 7 tareas, dos
paquetes). No vienen en los datos de la competencia. Las otras 21 son tests que fallan.

**Contraste.** La causa del entorno queda confirmada para 34. La pista de la versión de starlette queda
descartada.

**Sin cambio de configuración del agente.** Este resultado mejora el instrumento, no al agente.

**Cambio propuesto al instrumento.** Instalar esos dos paquetes en el notebook de medición: de 71 tareas a un
máximo de 105. Queda en el issue #103 para quien lleva el chequeo de validez.

## Vuelta 7 — 2026-10-04, 22:05 a 22:15 UTC

**Hipótesis nueva, del dueño.** Zorzal, el agente de ALL que consolida un fallo dentro del mismo episodio
para no repetirlo, puede ser la pieza de ALL que este concurso sí permite expresar: no necesita memoria entre
tareas, solo dentro de una.

**Qué se cambió.** Ninguna configuración del agente. Se añadió una medida a `iteracion-01`: por tarea, cuántas
llamadas a herramientas repiten una llamada idéntica anterior, y cuántas repiten una que ya había fallado.
Solo conteos. Validado con una traza sintética y con el ensayo local. Se resubió y empezó a ejecutarse a las
22:11 UTC.

**Predicción, escrita antes de ver resultados:**

| Predicción | La refuta |
|---|---|
| P10. En la configuración enviada, las tareas que terminan sin parche tienen más llamadas repetidas tras un fallo que las que entregan parche | Igual o menos |
| P11. Al menos 1 de cada 10 llamadas de la configuración enviada repite una llamada idéntica anterior | Menos de 1 de cada 10 |

**Decisión que depende de esto.** Si P10 y P11 se cumplen, el siguiente cambio es una instrucción de tipo
zorzal: tras un fallo, anotar qué falló y no repetir la misma llamada. Se compara contra un texto de relleno
del mismo largo. Si no se cumplen, repetir no es el problema y zorzal no es el cambio siguiente.

## Vuelta 8 — 2026-10-04, 22:20 a 22:45 UTC

**Sin subidas a Kaggle.** El dueño aprobó la hipótesis Zorzal, sus umbrales y H-O.

**Qué quedó hecho.** Umbrales congelados a las 22:30 UTC, sin haber leído `sesion-unica-a` ni `iteracion-01`.
Las hipótesis se escribieron como historias de usuario y de uso de datos; cada criterio de aceptación es una
prueba (39). PR #145 del repositorio de ALL, en borrador.

**Corrección.** `iteracion-01` se resubió una cuarta vez a las 22:11 UTC, antes de la instrucción de no subir.
Queda anotada en el punto de partida de H-O.

**Lo que falta por oír.** Las dos corridas con GPU y `validez-con-paquetes`. Se leen con las reglas congeladas.

## Vuelta 9 — 2026-10-04, 23:07 a 23:20 UTC

**Resultado leído.** `validez-con-paquetes` terminó en 73 minutos de CPU. Con tres paquetes de pruebas
instalados, las tareas válidas pasan de 71 a 103: fastapi de 29 a 60, rich de 42 a 43, requests y httpx
siguen en 0.

**Contraste.** La causa del entorno queda confirmada por intervención: 31 de las 34 tareas de fastapi se
recuperan. Ninguna de las 71 que servían dejó de servir, que era el riesgo. Con 60 segundos por comando no
cambia ningún veredicto (0 de 103).

**Sin explicar.** Una tarea de rich cambió sola de «el parche no pasa» a válida. Quedan 23 tareas sin causa.

**Cambio respaldado por este dato.** Es del instrumento, no del agente: el notebook de medición puede
instalar esos paquetes y usar fastapi como segundo repositorio. No se preparó ni se subió ninguna corrida.

**Decisión.** Conservar. Se aplica cuando el dueño apruebe la siguiente corrida con GPU.

## Vuelta 10 — 2026-10-04, 23:10 a 23:40 UTC

**Sin subidas a Kaggle.** Concilio de tres revisores terminado; nombre aprobado por el dueño: ZorzALL.

**Límite oficial, leído en las páginas de la competencia.** No hay límite por tarea. El único oficial es de 12
horas para todas las tareas. El tope de 40 llamadas que usamos es nuestro.

**Idea puesta a prueba: el oído.** El envío lleva una skill que deja disponibles los paquetes de pruebas que
faltan en el entorno del agente, sin tocar el árbol de trabajo.

**Reglas.** Las herramientas y datos externos se permiten si son públicos y sin costo. No encontré una
prohibición de llevar paquetes de código abierto en una skill. Las licencias de los cinco paquetes son MIT,
Apache 2.0 y PSF.

**Corrección a mi propio planteamiento.** Dije que el agente estaba sordo en las 34 tareas medidas. El dato
dice otra cosa: en esas 34 lo que fallaba era la verificación, que añade pruebas nuevas. Lo que afecta al
agente es distinto y se midió aparte: qué parte de las pruebas que ya existen en el repositorio puede cargar.

**Resultado, en local, con el arnés real y un modelo de guion fijo.** Tres tareas de fastapi de muestra:

| Tarea | Pruebas que cargan antes | Después | Errores de carga antes | Después |
|---|---|---|---|---|
| 1 | 1 032 | 3 083 | 301 | 4 |
| 2 | 690 | 2 486 | 132 | 3 |
| 3 | 2 927 | 3 711 | 65 | 4 |

En las tres el árbol de trabajo quedó limpio y la activación fue automática. En cinco instantáneas de
fastapi, entre el 13 % y el 61 % de los archivos de prueba existentes importan esos paquetes.

**Límites.** Es el sandbox Docker local, no el entorno de Kaggle. Son tres tareas. Mide que el agente puede
oír, no que resuelva más. No se sabe qué paquetes faltan en los repositorios ocultos.

**Decisión.** Conservar como candidato. El siguiente paso, que requiere aprobación, es medirlo en el entorno
de Kaggle en CPU.

## Vuelta 11 — 2026-10-05, 00:05 a 00:25 UTC

**Resultado leído: `sesion-unica-a`,** la primera corrida completa con el modelo. 20 tareas de rich, 16 válidas
en las dos mediciones. Sesión de 2 h 39 min; unas 5,3 h de cuota.

| Pasada | Resueltas (de 16) | Minutos por tarea | No resueltas que agotan llamadas | Que agotan tiempo |
|---|---|---|---|---|
| Enviada, 1.ª | 4 | 1,86 | 8 de 12 | 2 de 12 |
| Con razonamiento | 3 | 3,76 | 3 de 13 | 11 de 13 |
| Enviada, 2.ª | 4 | 1,70 | 7 de 12 | 0 de 12 |

**Ruido:** 2 tareas de 16 cambian entre las dos pasadas iguales.

**Contraste con las predicciones.**

- P1 (de 1 a 3 tareas cambian): se cumple.
- P2 (la mayoría falla por tiempo): refutada. En la configuración enviada fallan por llamadas agotadas.
- P3 (el razonamiento no supera el ruido): se cumple. Resuelve una menos.

**Decisiones.**

- Razonamiento con tope de 4 minutos: **descartar.** Gasta el doble y no resuelve más.
- Tope de 40 llamadas: es el freno principal y lo pusimos nosotros. El cambio que respalda este dato es
  subirlo; ya lo mide la pasada de 100 llamadas de `iteracion-01`, que sigue corriendo. No se lanza nada nuevo.

**Dato para ZorzALL.** Más de la mitad de los fallos entregan un parche que no pasa. Coincide con lo que
encontró la revisión de literatura: el cuello de botella es comprobar.

## Vuelta 12 — 2026-10-05, 00:32 a 01:00 UTC

**Segundo envío, mismo zip:** 0,05, es decir 3 de 58. El primero dio 4.

**`iteracion-01`,** 15 tareas de rich válidas, cuatro pasadas, 2 h 8 min.

| Pasada | Resueltas (de 15) | Minutos por tarea | Llamadas repetidas | Sesiones sin edición |
|---|---|---|---|---|
| Enviada, 1.ª | 3 | 1,52 | 50 % | 7 |
| Pública de dos etapas | 3 | 2,07 | 47 % | 3 |
| Enviada, 2.ª | 3 | 1,46 | 54 % | 6 |
| Enviada con 100 llamadas | 2 | 2,93 | 68 % | 5 |

**Ruido:** 2 tareas entre las dos pasadas iguales.

**Predicciones.** Refutadas: P5 (100 llamadas resuelven más) y P7 (la pública resuelve más). No apoyada: P4.
Se cumplen: P6, P8, P9 y P11. P10 no se puede leer con lo guardado.

**Lo que dicen los datos.** El freno no es el presupuesto: es el bucle. La mitad de las llamadas repite una
idéntica. Con más llamadas el agente repite más y edita más tarde. Las tareas resueltas usan de 5 a 8
llamadas, sin repeticiones y con una edición. El agente casi nunca ejecuta las pruebas.

**Decisiones.**

- 100 llamadas: **descartar.**
- Configuración pública de dos etapas como base: **no adoptar.** Edita antes, pero no resuelve más.
- Siguiente cambio respaldado: romper el bucle. Falta decidir cómo y aprobar la corrida.

**Corrección al instrumento.** Guardar qué herramienta se repite y si hubo una edición entre una llamada y su
repetición.

## Vuelta 13 — 2026-10-05, entre las 00:45 y las 02:20 UTC

**Sin subidas a Kaggle.** Análisis de los datos de `iteracion-01` y preparación en local.

**Hallazgo.** El agente hace su primera edición cuando el arnés le avisa que le quedan 10 llamadas. Con tope
de 40, las tareas no resueltas editan en las llamadas 31, 31, 32, 37 y 40 en una pasada, y 31, 32, 32 y 40
en la otra. Con tope de 100, en la 91, 91 y 92. Las resueltas editan en la 3, 5 y 12. El ensayo local
confirmó que el aviso llega tras la llamada 30 con tope de 40.

**Tres candidatos, un cambio cada uno, ensayados en local con el arnés real:**

| Candidato | Cambio | Qué confirmó el ensayo |
|---|---|---|
| Aviso temprano | Tope de 40 a 20 llamadas | El aviso llega tras la llamada 10; la 21 se rechaza |
| Regla escrita | Tres líneas en la instrucción | La instrucción crece 291 caracteres; compila |
| Penalizar la repetición | `frequency_penalty` 0,3 | El parámetro llega al modelo |

Los tres pasan las cuatro comprobaciones del simulacro. Ninguno se ha medido con el modelo.

**Predicción para el aviso temprano, escrita antes de medir:**

| Predicción | La refuta |
|---|---|
| P12. La mediana de la primera edición baja de 31 a entre 10 y 13 | Una mediana de 20 o más |
| P13. Las sesiones sin ninguna edición bajan de 6 o 7 a 3 o menos, de 15 | 5 o más |
| P14. Las tareas resueltas no bajan más que el ruido | 0 resueltas de 15 |

No predigo que resuelva más: adelantar la edición no garantiza que sea correcta.

**Decisión.** Pendiente del dueño: cuál medir y con qué diseño.

## Vuelta 14 — 2026-10-05, entre las 00:45 y las 02:20 UTC

**Sin subidas a Kaggle.** Plan de `iteracion-02` revisado por la otra sesión y corregido.

**Qué cambió del plan y por qué.**

- El tope 20 pasa a ser un diagnóstico y no un candidato: deja al agente 10 llamadas para resolver.
- Las predicciones de la vuelta 13 se reemplazan: P12 no podía fallar con ese tope y P14 era demasiado laxa.
- El costo de la fase 3 estaba mal: son unas 17 horas de cuota, no 9. Queda para después del 10 de octubre.
- No se añade una pasada con el arreglo del defecto heredado: el agente llamó a su ayudante 1 o 2 veces en
  15 tareas, y la pasada con más bucle no lo llamó nunca. Ese defecto no puede ser la causa del bucle.
- La segunda pasada del tope 20 se cambia por una con la regla escrita, que no recorta presupuesto.

**Plan final, aprobado por el dueño.** Tope 20 → enviada → regla escrita, sobre las mismas 15 tareas.

**Predicciones, escritas antes de correr.** Una tarea que nunca edita cuenta como «no editó a tiempo».

| Predicción | Se cumple | No concluyente | La refuta |
|---|---|---|---|
| P12. Con tope 20, tareas que editan antes de la llamada 14 | 9 o más de 15 | 6 a 8 | 5 o menos |
| P13. Con tope 20, sesiones sin ninguna edición | 3 o menos | 4 | 5 o más |
| P14. Con tope 20, tareas resueltas | 2 o más | 1 | 0, si la enviada resuelve 2 o más |
| P15. Con la regla escrita, tareas que editan antes de la llamada 14 | 5 o menos | 6 a 8 | 9 o más |

Referencia: la configuración enviada dejó 3 y 4 de 15 editando antes de la llamada 14. La corrida no puede
detectar un daño menor que 3 tareas.

**Validado sin GPU.** Chequeo previo, guardia en las dos disposiciones, y ensayo local de las tres pasadas con
un modelo que repite llamadas: el aviso aparece tras la llamada 10 con tope 20 y no aparece con tope 40; los
contadores de repetición por herramienta y de empujones (los tres textos del arnés) funcionan.

**Estado.** Listo y sin subir. Espera el «sube» explícito del dueño.

## Vuelta 15 — 2026-10-05, entre las 00:45 y las 02:20 UTC

**Sin subidas a Kaggle.** Auditoría de `iteracion-01` desde los datos crudos, a pedido del dueño.

**Se sostiene.** Integridad del archivo, la tabla informada, y que la traza guarda los argumentos completos.

**Correcciones.**

- «Sesiones sin ninguna edición» contaba solo llamadas a las herramientas de editar. En dos sesiones hay parche
  sin ninguna: el agente también edita por consola.
- El mecanismo del aviso no es general: 3 de 5, 4 de 5 y 3 de 8 ediciones tardías caen justo tras el aviso en
  la configuración enviada; 0 de 5 en la de dos etapas.

**Datos nuevos.** 11 de 15 tareas no se resolvieron en ninguna de las cuatro pasadas. Quedarse sin editar es en
parte cosa de la tarea: 5 se repiten en las dos pasadas iguales.

**Instrumento.** `iteracion-02` guarda ahora los comandos que pueden escribir. Mi primer intento de esa regla
tenía un error de sintaxis; lo atraparon el chequeo previo y el ensayo local. La regla final pasa 16 casos.
El notebook se volvió a ensayar completo.

**Estado.** `iteracion-02` listo y sin subir. Página publicada corregida.

## Vuelta 16 — 2026-10-05, entre las 00:45 y las 02:20 UTC

**Sin subidas a Kaggle.** Análisis de los datos ya bajados, cruzados con los enunciados de las tareas.

**Hallazgo.** Lo que separa las tareas resueltas de las que no es el largo del enunciado.

| Enunciado | Tareas | Resueltas alguna vez | Pasadas resueltas |
|---|---|---|---|
| 250 caracteres o más | 6 | 5 | 22 de 42 |
| Menos de 250 | 10 | 0 | 0 de 66 |

Fisher exacto: p = 0,0014. Los enunciados cortos son un título y una referencia que el agente no puede abrir.
Son 47 de las 129 tareas públicas.

**Lo que corrige.**

- El bucle es un síntoma: ocurre donde el enunciado no dice qué corregir.
- El mecanismo del aviso es de 3 tareas de enunciado largo, las mismas en tres pasadas. La pasada de 100
  llamadas ya fue una intervención sobre ellas.
- Las comparaciones de hoy se decidieron en 6 tareas.

**Predicciones de `iteracion-02` por estrato, escritas antes de correr.** Las de la vuelta 14 se conservan; la
lectura principal pasa a ser esta.

| Estrato | Predicción | Se cumple | No concluyente | La refuta |
|---|---|---|---|---|
| Largo (6) | P16. Con tope 20, las 3 tareas que editaban en la llamada 31 o 32 editan antes de la 14 | 2 o 3 | 1 | 0 |
| Largo (6) | P17. Con tope 20, tareas resueltas | 2 o más | 1 | 0, si la enviada resuelve 2 o más |
| Largo (6) | P18. Con la regla escrita, esas 3 tareas editan antes de la llamada 14 | 0 o 1: decirlo no basta | — | 2 o 3 |
| Corto (9) | P19. Con tope 20, sesiones que entregan parche | 5 o más | 3 o 4 | 2 o menos |
| Corto (9) | P20. Con cualquiera de las dos, tareas resueltas | 0 | — | 1 o más |

P20 es la que más me gustaría ver refutada.

**Umbral.** El corte de 250 caracteres se eligió mirando estos datos. Hay que confirmarlo en tareas no vistas.

**Estado.** `iteracion-02` sigue lista y sin subir. El notebook no cambia: el estrato se calcula después.

## Vuelta 17 — 2026-10-05, entre las 00:45 y las 02:20 UTC

**Sin subidas a Kaggle.** Análisis local de las tareas de enunciado corto, sobre las copias de los repositorios.

**Resultado.**

| | Enunciado corto (9) | Enunciado largo (6) |
|---|---|---|
| Archivo corregido en el puesto 1 al buscar las palabras del enunciado | 6 | 0 |
| Entre los 5 primeros | 7 | 3 |
| Las pruebas exigen algún nombre nuevo | 2 | 2 |
| Resueltas alguna vez | 0 | 5 |

**Lectura.** En las tareas cortas, ubicar el archivo no es el obstáculo. Falta saber qué cambiar: 8 de 9 citan
un issue que no está en el repositorio. Y el agente no busca texto: hace 43 a 49 búsquedas por similitud.

**Mi suposición de la vuelta anterior, corregida.** Supuse que en las tareas cortas el agente no podía ubicar
el fallo. El dato dice que el archivo es fácil de encontrar.

**Instrumento.** `iteracion-02` guarda ahora si el agente ve, lee y edita el archivo corregido, y en qué
llamada, separado por largo del enunciado. Probado y vuelto a ensayar completo.

**Predicción nueva, escrita antes de correr:**

| Predicción | Se cumple | La refuta |
|---|---|---|
| P21. En la configuración enviada, el agente lee el archivo corregido en menos de la mitad de las tareas cortas | 4 o menos de 9 | 5 o más |

Si P21 se refuta, el agente llega al archivo y no sabe qué hacer con él; el problema sería de comprensión, no
de búsqueda.

**Estado.** `iteracion-02` lista y sin subir.

## Vuelta 18 — 2026-10-05, 02:21 UTC

**Corrección de registro.** Las vueltas 13 a 17 llevaban horas que yo estimé y eran incorrectas. Ocurrieron en
ese orden, entre las 00:45 y las 02:20 UTC. La hora de esta vuelta sí está leída del reloj.

**Subida.** `cs4all/iteracion-02`, versión 1, a las 02:21 UTC, con el «súbela» explícito del dueño. Una sola
subida. Quedó en cola. El contenido remoto coincide celda por celda con el validado.

**Plan.** Tope 20 → enviada → regla escrita, sobre las mismas 15 tareas de rich.

**Predicciones vigentes.** P12 a P21, escritas en las vueltas 14, 16 y 17.

**Registro.** La ficha completa de la prueba está en [`REGISTRO_DE_PRUEBAS.md`](REGISTRO_DE_PRUEBAS.md).

**Operación.** Primera subida dentro de la ventana del indicador de operación (2026-10-05 a 2026-10-11).

**Seguimiento, 11:05 UTC.** La corrida sigue en cola tras 8 h 42 min. Comprobado: sin error informado, sin
otro notebook corriendo, contenido remoto igual al validado. Cuota de GPU leída por API: 13,41 h usadas de 30,
nada reservado. La espera es de la cola de Kaggle, no de la cuenta. No se cancela ni se resube.

## Vuelta 19 — 2026-10-05, 19:02 UTC

**Sin subidas a Kaggle.** Lectura de `iteracion-02` (terminada: 5 433 s de sesión, unas 3 h de cuota) desde su
archivo de resultados, cruzada con `iteracion-01`. Las cifras salen del json, no del log.

**Resultado.**

| Pasada | Resueltas (de 15) | Largo (de 6) | Corto (de 9) | Llamadas repetidas sin cambio | Tokens de entrada |
|---|---|---|---|---|---|
| Tope 20 | 2 | 2 | 0 | 18 % | 1,85 M |
| Enviada (tope 40) | 2 | 2 | 0 | 42 % | 3,90 M |
| Regla escrita (tope 40) | 4 | 4 | 0 | 40 % | 3,94 M |

**Contraste con las predicciones.**

| Id | Dato | Lectura |
|---|---|---|
| P12 | 3 de 15 editan antes de la llamada 14 | Refutada |
| P13 | 5 sesiones sin ninguna edición | Refutada |
| P14 | 2 resueltas | Se cumple |
| P15 | 3 de 15 editan antes de la llamada 14 | Se cumple: la regla no adelanta la edición |
| P16 | 0 de 3 antes de la 14; editan en la 14, 14 y 18 (antes: 31, 31 y 32) | Refutada por el umbral; la edición sí sigue al aviso, 4 a 8 llamadas después |
| P17 | 2 resueltas | Se cumple |
| P18 | 0 de 3; editan en la 31, 31 y 32 | Se cumple: decirlo no basta |
| P19 | 2 de 9 entregan parche | Refutada |
| P20 | 0 resueltas de enunciado corto, en las dos | Se cumple |
| P21 | Lee el archivo corregido en 6 de 9 | Refutada: llega al archivo y no sabe qué cambiar |

**Decisiones que ya estaban fijadas.** Tope 20: diagnóstico, no pasa a candidato. Regla escrita: **descartar**;
era candidata solo si adelantaba la edición y no la adelanta. Sus 2 tareas de más son las que cambian solas
entre pasadas iguales, y las resolvió editando en la llamada 31, tras el aviso.

**Lo que dicen las 7 pasadas juntas sobre estas 15 tareas** (105 sesiones):

| Tareas | Resultado en 7 pasadas |
|---|---|
| 2 | Resueltas siempre (14 de 14) |
| 2 | A veces (5 de 14) |
| 11 | Nunca (0 de 77): las 9 de enunciado corto y 2 de enunciado largo |

Toda diferencia entre configuraciones de estos dos días (2, 3 o 4 de 15) sale de 2 tareas. El conjunto ya no
puede distinguir un cambio de otro. Elegir lo mejor de varias pasadas daría como máximo 4 de 15.

**Otros datos.**

- Las sesiones resueltas gastan una mediana de 50 000 a 82 000 tokens de entrada; las no resueltas, 285 000.
  Con tope 20 se resuelve lo mismo que con tope 40 con la mitad de tokens.
- El agente ejecuta pytest en 2 o 3 sesiones de 15. La clase de fallo más frecuente con tope 40 es «el parche
  no pasa» (7 de 13 y 6 de 11).
- Tiempo usado: 75 a 106 s por tarea.

**Dudas del instrumento.** «Comandos con salida distinta de cero» vale 0 en las 45 sesiones, con decenas de
errores de comando: revisar el contador. Una tarea falló por el parche de pruebas, no por el agente.

**Decisión.** Pendiente del dueño: plan propuesto en la sesión (mapa de una pasada sobre las tareas válidas
no vistas, rich y fastapi, antes de probar otro cambio).

**Corrección, entre las 19:02 y las 19:22 UTC.** Dos afirmaciones mías de esta vuelta eran falsas y se quitaron de arriba.

- Escribí que el límite reparte 12 minutos por tarea. La evaluación corre unas 120 tareas en 12 horas: con
  reserva y montaje son 5,4 minutos. Usamos entre un cuarto y un tercio, no un octavo.
- Escribí una cuenta que explicaba la nota por las tareas de rich. Suponía que el conjunto oculto tiene la
  mezcla pública. La página de datos dice que se curó de repositorios privados: las 129 tareas públicas son de
  entrenamiento y ninguna es de los repositorios con que se puntúa. La cuenta no vale.

**Dato nuevo, leído en el log crudo.** La búsqueda por similitud falla casi siempre: 386 avisos de «no se pudo
obtener el embedding» en el log, que los imprime por duplicado, frente a 196 llamadas a esa herramienta en las
tres pasadas. El arnés lo documenta: sin servidor de embeddings, la herramienta solo acepta el nombre exacto
de un símbolo, y el modelo le pasa frases. Pasa lo mismo en `iteracion-01` (228 avisos) y `sesion-unica-a`
(148). Es parte del bucle de las tareas cortas, donde esa herramienta llega a ser 38 de 40 llamadas. Ojo: la
pasada pública de dos etapas, que la quita, tampoco resolvió más en estas 15.

**Lo que esto cambia.** El plan del «mapa» se retira tal como estaba: medir más tareas de rich y fastapi
afina una regla sobre repositorios que no se puntúan.

## Vuelta 20 — 2026-10-05, 19:22 UTC

**Sin subidas a Kaggle.** Revisión del proceso a pedido del dueño: se leyó entero el documento del arnés, el
paquete enviado y lo que quedó guardado de las sesiones con el modelo.

**Hechos comprobados.**

| Tema | Hecho | Fuente |
|---|---|---|
| Paquete enviado | Es el del kit sin adaptadores y con cuatro topes y dos parámetros de muestreo cambiados. La instrucción es la del kit, sin tocar. No lleva ninguna skill | Registro de envíos y carpeta de la condición A |
| Instrucción del kit | Manda usar la búsqueda por similitud con palabras clave cuando el enunciado no trae rutas, y desaconseja `find` y `grep` | `prompts/system.md` |
| Arnés | Esa búsqueda solo resuelve nombres exactos de símbolos | Documento del arnés, sección 6.3 |
| Consecuencia medida | Casi todas las llamadas a esa herramienta fallan (vuelta 19). El agente obedece una instrucción que lo manda a una herramienta que no puede responderle | Log crudo |
| Verificar | El arnés ya le pide verificar antes de entregar y la instrucción del kit también. Ejecuta pytest en 2 o 3 sesiones de 15 | Documento del arnés, sección 5.2; json |
| Contexto | El arnés resume la conversación cada 5 eventos o al pasar de 14 336 tokens | Sección 7.2 |
| Trazas | El arnés escribe por tarea la traza completa, la transcripción y la salida de pytest de la verificación. De más de 100 sesiones con el modelo no se guardó ninguna: el notebook las reduce a conteos y las borra | Sección 9.2; celda 9 del notebook; carpetas locales |
| Adaptadores | Los dos del kit son de muestra: rango 4, una capa, 217 kB | `adapter_config.json` |

**Corrección propia.** Dije que el texto no mueve a este modelo. Es demasiado: el modelo sí obedece la
instrucción del kit sobre qué herramienta usar. Lo medido es más estrecho: tres líneas añadidas al final no
adelantaron la edición.

**Hipótesis sin probar.** Que las llamadas idénticas repetidas empiecen cuando el arnés resume la conversación
y el agente pierde el registro de lo que ya hizo. Solo se puede comprobar con trazas.

**Decisión.** Pendiente del dueño: una sesión cuyo producto sean las trazas completas, antes de cualquier
cambio.

## Vuelta 21 — 2026-10-05, 20:35 UTC

**Sin subidas a Kaggle.** Dos trabajos: el notebook de trazas y el experimento de tareas propias.

**Notebook `iteracion-03`.** Hay dos versiones, de dos sesiones.

| Versión | Pasadas | Estado |
|---|---|---|
| De la otra sesión | rich (15) y requests (13) | Ensayada con el arnés real en Linux, también con sesiones largas y tope de tiempo |
| Corregida | rich (15), fastapi (15) y requests (13); tope de tareas 7 200 s | Se genera a partir de la anterior con un guion; lleva también su captura de los resúmenes del arnés |

Por qué la corrección: ninguna tarea de requests discrimina en Kaggle, así que ahí «el parche no pasa» no
distingue al agente del entorno. En el ensayo, con el parche de referencia, las 15 de fastapi resuelven y
coinciden con la validez medida en Kaggle; de requests coinciden 9 de 13.

**Hallazgo de la otra sesión, en el ensayo largo.** Después de que el arnés resume la conversación, el modelo
ya no recibe el enunciado: recibe el resumen y las últimas llamadas. La traza no guarda ese resumen; por eso
se añadió su captura. Con un modelo falso el resumen es una frase fija: qué conserva Gemma ahí es lo que hay
que ver. Es la pieza que faltaba para probar si las llamadas repetidas empiezan tras un resumen.

**Experimento nuevo, por decisión del dueño: tareas de repositorios propios.** Proceso y datos en
[`EXPERIMENTO_TAREAS_PROPIAS.md`](EXPERIMENTO_TAREAS_PROPIAS.md).

| Medida | Valor |
|---|---|
| Candidatos en Agents Learning Loops | 32 de 60 commits |
| Discriminan | 19 |
| Mediana de líneas del parche de referencia | 255; en el concurso, 12 |
| De 60 líneas o menos | 2 de 19; en el concurso, 103 de 129 |

**Lectura.** Las tareas existen y se validan, pero son funcionalidades enteras, no correcciones. Con ellas tal
como están lo esperable es cero resueltas. Falta sacar tareas pequeñas, llevar tres dependencias que el
sandbox no tiene y probar el arnés con un repositorio que no conoce.

**Hecho de operación.** A pedido del dueño se apagó Smart App Control en su equipo (valor del registro de 1 a
0) para destrabar una DLL de pandas del entorno del arnés. No se aisló si era la única política implicada.

## Vuelta 22 — 2026-10-05, 21:45 UTC

**Sin subidas a Kaggle.** Cierre de sesión con trabajo en curso; nada de lo que sigue está leído ni validado.

- La otra sesión cambió su captura de resúmenes y la versión corregida de `iteracion-03` se volvió a generar
  sobre ella. El ensayo largo de la versión anterior se detuvo: ya no valía.
- En ejecución al cerrar, en Docker: ensayo largo y ensayo completo de la versión corregida vigente, y la
  validez de las tareas propias sacadas de los PR.
- Tareas propias: mirando los commits individuales de los 81 PR hay 93 candidatos, 15 con parche de 60 líneas o
  menos. Falta saber cuántos discriminan.
- El equipo se suspendió durante los ensayos y los frenó cerca de una hora.

**Pendiente.** Leer los tres resultados, chequeo previo del notebook, y la decisión de subir.

## Vuelta 23 — 2026-10-06, 02:05 UTC

**Sin subidas a Kaggle.** Lectura de los tres resultados que la vuelta 22 dejó corriendo en Docker (terminaron a
las 22:03 UTC del día 5), chequeo previo del notebook y una sola consulta a Kaggle. Solo agregados.

**1. Ensayo completo de `iteracion-03` corregida** (arnés real, Linux, modelo falso que aplica el parche de
referencia y entrega). Pasa: 43 tareas validadas de 43, 0 problemas, 1 936 s.

| Grupo | Tareas | Resueltas con el parche de referencia | Coinciden con la validez medida en Kaggle |
|---|---|---|---|
| rich conocidas | 15 | 14 | 14 |
| fastapi no vistas | 15 | 15 | 15 |
| requests no vistas | 13 | 3 | 9 |

La de rich que no pasa en el contenedor discrimina en Kaggle en las dos mediciones: es el entorno de pruebas
del contenedor, no el notebook. El ensayo lo advierte: «resuelta» no es criterio ahí. Parámetros que recibió el
modelo: razonamiento apagado, 8 192 tokens, temperatura 0,2, top_p 0,95, iguales a la configuración enviada.

**2. Ensayo largo** (modelo falso que sigue llamando tras aplicar el parche; mitad de las tareas entrega en la
llamada 31, la otra mitad nunca). Pasa: 43 filas, 0 problemas, 1 937 s. La traza del zip trae las mismas llamadas,
en el mismo orden y con los mismos argumentos que emitió el modelo, en las 43. Resúmenes del arnés capturados:
45, 43 y 41 por grupo, uno por cada petición de resumen que recibió el modelo. El historial baja alguna vez en
las 43 tareas (129 bajadas); tras el primer resumen, el enunciado ya no está en la petición.

**Hallazgo del instrumento, leído en las trazas y en el código del arnés.** El tope de 40 llamadas no termina la
sesión. En las 22 sesiones que no entregan, las llamadas 41 a 100 (60 por sesión) vuelven con «presupuesto de
llamadas agotado» y la sesión sigue hasta el tope de 100 vueltas. El contador del arnés deja de subir en 40. Dos
consecuencias: el «40, el tope» de las tareas cortas en Kaggle es el contador saturado, no el número de intentos;
y una parte de las llamadas repetidas puede ocurrir después de la primera negativa. `iteracion-03` lo mide.

**3. Tareas propias, segunda pasada: commits individuales de los PR.** Detalle en
[`EXPERIMENTO_TAREAS_PROPIAS.md`](EXPERIMENTO_TAREAS_PROPIAS.md).

| Medida | Commits aplastados | Commits de los PR |
|---|---|---|
| Candidatos | 32 | 93 |
| Discriminan | 19 | 65 |
| No pasan con el parche | 12 | 24 |
| Pasan sin el parche | 1 | 4 |
| Líneas del parche, mediana (de las que discriminan) | 255 | 230 |
| De 60 líneas o menos, que discriminan | 2 | 9 |

Nueve tareas pequeñas que discriminan. Es un conjunto, no una medición: quedan los pasos 3 a 6 de la ficha.

**4. Chequeo previo del notebook corregido** (`scripts/kaggle_preflight.py`, tope 150 min): 19 comprobaciones,
todas pasan, «se puede subir». La orden quedó impresa; no se ejecutó.

**5. Kaggle, una consulta a las 01:55 UTC.** `iteracion-03` no está subida (ninguna sesión la subió). Cuota: 16,43 h
usadas de 30; quedan 13,57 h; reinicio 2026-10-10 00:00 UTC. Con la reserva de 5 h de la regla 2.6, hay 8,57 h
disponibles.

**Costo de `iteracion-03` si se sube.** 43 tareas en una pasada con la configuración enviada. A 100 s por tarea
(medido en `iteracion-02`) más 13 min de carga: unos 85 a 100 min de sesión, 3 a 3,4 h de cuota. Máximo: 150 min
de sesión, 5 h de cuota (el notebook corta las tareas a los 120 min). Supera el umbral de 4 h de la regla 3 en el
peor caso: necesita aprobación explícita de todos modos.

**Predicciones propuestas, para escribir antes de correr (pendientes de aprobación del dueño):**

| Id | Estrato | Predicción | Se cumple | La refuta |
|---|---|---|---|---|
| P22 | fastapi no vistas | El umbral de 250 caracteres se sostiene en tareas no vistas | largas ≥ 2 de 9 y cortas 0 de 6 | cortas ≥ 2 de 6, o largas 0 de 9 |
| P23 | Todas | En las sesiones que llegan a 40 llamadas, el modelo sigue llamando tras la primera negativa | ≥ 10 llamadas rechazadas en la mitad o más de esas sesiones | en menos de un cuarto |
| P24 | Todas | En las sesiones con ≥ 5 llamadas idénticas repetidas, la primera repetición ocurre después del primer resumen del arnés o de la primera negativa | en 2 de cada 3 o más | en 1 de cada 3 o menos |
| P25 | Todas | Tras el primer resumen, el enunciado completo no está en la petición (como en el ensayo local) | en ninguna sesión | en alguna |
| P26 | rich conocidas | Resueltas, como en las 7 pasadas anteriores | 2 a 4 de 15 | 0 a 1, o 6 o más |

**Decisión pendiente del dueño.** Subir `cs4all/iteracion-03` (orden impresa por el chequeo previo) o no. Nada se
sube sin su «súbela».

## Vuelta 24 — 2026-10-06, 02:08 a 02:55 UTC

**Sin subidas a Kaggle hasta el cierre de esta vuelta.** Sesión nueva que retoma la 23. Orden del dueño, textual:
«aplicar todas las correcciones posibles antes de subir, para mejorar el modelo ZorzALL, considera la importancia
del arnés. Adelante, luego avanzar en la carga, realiza todo esto en 1 /loop». Se leyó como: corregir el instrumento
sin tocar la configuración del agente, validar sin GPU, subir y seguir la corrida.

**1. Estado leído al empezar (02:08 UTC, una consulta).** `iteracion-03` sin subir; cuota 16,43 h usadas y 13,57 h
libres; los dos envíos ya con nota (0,06 y 0,05). Docker sin ensayos corriendo. El chequeo previo repetido pasa.

**2. Revisión independiente del notebook** (revisor de código aparte; sin GPU, sin Kaggle, sin Docker). Veredicto:
«se puede subir», sin objeción bloqueante. Confirmó con sus propios conteos los agregados de la vuelta 23. Objeciones:

| Gravedad | Objeción |
|---|---|
| Importante | P25 no se podía medir en la corrida real: la captura descartaba las peticiones con herramientas |
| Importante | Margen de unos 3 min frente al `-t` de 150 en el peor caso medido: el tope se contaba desde el inicio de las tareas, no de la sesión, y la carga del modelo en `iteracion-02` fue de 19 min, no 13 |
| Importante | Si vLLM caía a mitad de la pasada no quedaba registro y el notebook no lo detectaba |
| Menor | CAPTURA imprimía acumulados; los resúmenes no llevaban hora ni número de petición; `int(test_exit_code)` falla con None; la celda 3 escribe una configuración que la 4 borra |

Dato nuevo del revisor: la carga del modelo en las corridas guardadas fue 364, 635, 765 y 1 142 s.

**3. Correcciones aplicadas, solo al instrumento.** Los seis archivos de la condición A siguen idénticos al envío.

1. `peticiones.jsonl` por grupo: una línea por petición con número dentro de la tarea, hora, mensajes, caracteres,
   si lleva herramientas y si los 300 primeros caracteres del enunciado están en lo que recibió el modelo. Sin
   contenido. Con esto P25 se mide en la corrida real.
2. Tope de sesión: además del tope de tareas (120 min desde que empiezan), se corta cuando a la sesión le quedan
   menos de 10 min frente a los 150, contado desde el arranque del proceso. Cubre una carga lenta del modelo.
3. Antes de cada tarea se consulta `/health` del servidor; si no responde, se guarda la causa y la cola de su log en
   `/kaggle/working` y se corta. El manejo de fallo también guarda el log y deja el json diciendo por qué se cortó.
4. CAPTURA por grupo; resúmenes con número de petición y hora; `codigo_pruebas` tolera None.

La celda 3 queda como corrió (no tiene efecto). Las celdas 0 a 3, 5 a 8 y 10 siguen intactas respecto de
`iteracion-02`.

**4. Validado sin GPU, cuatro ensayos en Docker con el arnés real.** Los cuatro pasan con 0 problemas.

| Ensayo | Qué prueba | Resultado |
|---|---|---|
| Servidor caído tras 60 peticiones | Detección y registro | El arnés no lanza: la tarea en curso termina como «llamadas agotadas sin parche» a los 179 s, con 66 peticiones rechazadas. Antes de la siguiente, el notebook ve el 503, escribe `servidor_caido_*.txt` y corta con `cortado_por = servidor`. Json y zip intactos |
| Tope de sesión de 200 s | Corte por sesión | Corta tras 14 tareas con `cortado_por = sesion`; las 14 validadas |
| Completo (parche de referencia) | Flujo y validez | 43 de 43, 754 s; rich 14 de 15, fastapi 15 de 15, requests 3 de 13; el modelo recibió los parámetros del envío |
| Largo (sesiones de hasta 100 llamadas) | Trazas, resúmenes, P25 | 43 de 43, 751 s; resúmenes capturados 45, 43 y 59, iguales a los recibidos; 3 019 peticiones registradas; la presencia del enunciado coincide petición por petición con lo que vio el modelo falso en las 43 tareas |

Hallazgo del ensayo largo para P25: tras el primer resumen, el enunciado no está en 42 de 43 tareas; en una sigue
en 20 peticiones. «En ninguna sesión» ya es falso con el modelo falso: es conducta del arnés, no de Gemma. La
predicción se deja como estaba, con este dato a la vista.

**5. Chequeo previo tras las correcciones:** 19 comprobaciones pasan. Huella del notebook: `a463dc724073e9fa…`,
55 120 bytes.

**Predicciones, escritas antes de correr:** P22 a P26 de la vuelta 23, sin cambios. El dueño ordenó subir; no
corrigió las predicciones.

**Costo:** esperado 75 a 100 min de sesión, 2,5 a 3,3 h de cuota; peor caso 150 min, 5 h. Disponible con la
reserva de 5 h: 8,57 h.

**Subida.** 02:47 UTC, con la orden impresa por el chequeo previo: `cs4all/iteracion-03`, versión 1, en cola. El
contenido remoto se bajó y coincide con el validado en las 11 celdas. Seguimiento en la ficha 11 del registro de
pruebas. Lo que sigue: una consulta de estado por hora; al terminar, rescate de la salida y lectura en la vuelta 25.

### En paralelo, por orden del dueño: qué le sirve a ZorzALL del laboratorio C4A

Lo leído en `AC_C20_2026` (plataforma de auditoría estática con ledger, identificadores deterministas,
`reproduce` por hash de contenido y ciclo de vida por hallazgo) y lo que de ahí se midió aquí, sin tocar el
agente ni los umbrales congelados. Instrumentos en `instrumentos/`, fuera de git: `zorzal_oye_v2.py` y
`zorzal_reproducir.py`.

**1. «Oye» hoy, en las 7 pasadas con datos (105 sesiones).** La medida de la versión 1 es «algún comando que
nombra pytest».

| Pasada | Sesiones que nombran pytest | Resueltas | Resueltas que nombran pytest |
|---|---|---|---|
| iteracion-01, enviada 1.ª y 2.ª | 2 y 3 de 15 | 3 y 3 | 0 y 0 |
| iteracion-01, pública y 100 llamadas | 0 y 4 | 3 y 2 | 0 y 0 |
| iteracion-02, tope 20, enviada, regla | 3, 3 y 2 | 2, 2 y 4 | 0, 0 y 0 |

Ninguna de las 19 sesiones resueltas nombró pytest. Con esa medida, H-Z1 saldría en contra de «oye» por
construcción: las resueltas usan de 5 a 8 llamadas y no las gastan en pruebas. La medida mide otra cosa.

**2. «Oye», versión 2, a la manera de C4A (un detector observa, otro rol concluye).** Una comprobación es un
comando que ejecuta pruebas, o un `python -c` o `python x.py` que afirma algo o que falla; imprimir un valor no
es escuchar. La sesión «oye» si hizo al menos una, no ignoró ninguna que fallara (la siguiente acción fue
editar o comprobar distinto, no repetirla igual ni entregar) y, si editó, comprobó después de la última
edición. Solo conteos y posiciones, como exige HD-1. El instrumento pasa 6 casos de autoprueba y da 0 en las
43 trazas del modelo falso (que no comprueba nada). No se puede aplicar a `iteracion-01` ni `02`: no guardaron
trazas. `iteracion-03` es la primera corrida con trazas; se mide en cuanto llegue. Es una propuesta de versión 2
de `umbrales.json`, que exige enmienda y aprobación del dueño; no se ha cambiado nada.

**3. `reproducir`: dos pasadas, identificadores deterministas, qué cambió, huella.** Sobre los json ya
guardados:

| Comparación | Cambian de resultado | Cambian de clase de desenlace |
|---|---|---|
| iteracion-01, enviada 1.ª frente a 2.ª (el ruido) | 2 de 15 | 6 de 15 |
| iteracion-01, enviada frente a pública | 2 y 0 | 10 y 8 |
| iteracion-02, enviada frente a tope 20 | 0 | 8 |
| iteracion-02, enviada frente a regla escrita | 2 | 9 |

La clase de desenlace cambia entre tres y cinco veces más que el resultado. Cualquier lectura de ZorzALL
que se apoye en la tabla de fallos necesita su propio ruido, medido con dos pasadas iguales, no el de
resueltas. Hoy ese ruido es 6 de 15.

**4. Ledger de subidas (H-O).** `bitacora_operacion.json` del PR #145 ya es un ledger de solo añadir. Fila
que le corresponde a esta subida, sin escribirla allí (el PR es de otra sesión): fecha 2026-10-06T02:47Z,
notebook iteracion-03, sesión de retoma, aprobada por el dueño, ensayo local previo, una sola subida, sin
fallo visible en local; resultado útil pendiente. Lo que C4A añade y aquí falta: huella del notebook,
parámetros y resumen del resultado en la misma fila.

**5. Lo que no se toma de C4A.** El sensor léxico con salida precisa (323 hallazgos en VT en menos de un
segundo, cinco de seis «reproducidos» porque el mismo grep vuelve a coincidir). Es el defecto que ya medimos
en H8 y en las tareas cortas.

**Decisión que queda al dueño.** Enmendar `umbrales.json` a versión 2 con «oye v2» cuando `iteracion-03`
entregue trazas, y si las vueltas 1 a 23 de esta bitácora pasan a episodios de ALL para que `recall` las vea.

### Subida de `iteracion-04`, 13:45 UTC

`iteracion-03` pasó a ejecución entre las 13:14 y las 13:45, tras unas 11 h de cola. El dueño ordenó «Súbela,
iteracion-04 también»: el mismo notebook byte a byte (huella `a463dc724073e9fa…`), para medir el ruido entre dos
pasadas iguales en fastapi no vistas, que hoy no existe. Subida a las 13:45 con la orden del chequeo previo;
contenido remoto igual al validado en las 11 celdas; en cola con la 03 corriendo. Predicciones P27 a P30 en la
ficha 12 del registro, escritas antes de que corra. Aviso dado al dueño: la regla 2 pedía una sola sesión en
cola, y el peor caso conjunto (10 h) deja 3,6 h de cuota, bajo la reserva de 5 h.

### Tareas propias, paso 5: el arnés con un repositorio que no conoce

Primer ciclo, nueve tareas pequeñas con el parche de referencia y el modelo falso, en Docker: 5 de 9 resueltas;
4 fallan al importar el paquete. Causa aislada: el arnés escribe su propio `pytest.ini` en el espacio de trabajo
y ese archivo anula el `pythonpath` del `pyproject.toml` del repositorio; con `PYTHONSAFEPATH=1`, el paquete de
`src/` deja de importarse. La misma orden de pytest, a mano sobre el mismo snapshot, pasa en las 4. Segundo ciclo:
un `conftest.py` en la raíz del snapshot (fuera de git; el arnés conserva el existente) repone `src/` en
`sys.path`, como el sandbox de la competencia instala el paquete de cada repositorio. Resultado: **9 de 9
resueltas**, 117 s, sin módulos faltantes. El arnés monta un repositorio que no conoce, aplica el parche, corre
sus pruebas y declara la tarea; la única pieza que faltaba es que el paquete sea importable, que en la
competencia la pone el sandbox. Detalle y lo que sigue en `EXPERIMENTO_TAREAS_PROPIAS.md`.

## Vuelta 25 — 2026-10-06, 14:48 a 15:05 UTC

**Resultado de `iteracion-03`.** Terminada y completa: 43 tareas, sin cortes, unos 89 min de sesión, 2,96 h de
cuota. Una sola subida, ningún fallo visible en local. Datos crudos en `data/rescate_kaggle/iteracion-03/` (json y
tres zips con trazas, peticiones, resúmenes, parches y salidas de pytest). Lectura con `instrumentos/leer_iteracion_03.py`.

| Grupo | Resueltas | Enunciado largo | Enunciado corto | Llamadas repetidas | Segundos por tarea |
|---|---|---|---|---|---|
| rich conocidas | 3 de 15 | 3 de 6 | 0 de 9 | 49 % | 106 |
| fastapi no vistas | 3 de 15 | 3 de 9 | 0 de 6 | 55 % | 97 |
| requests no vistas (no discriminan) | 0 de 13 | — | — | 47 % | 138 |

**Predicciones.**

| Id | Predicción | Salió | Veredicto |
|---|---|---|---|
| P22 | En fastapi no vistas, largas ≥ 2 de 9 y cortas 0 de 6 | 3 de 9 y 0 de 6 | Se cumple |
| P23 | En las sesiones que llegan a 40 llamadas, ≥ 10 rechazadas en la mitad o más | 0 de 19; un solo rechazo por presupuesto en las 43 sesiones | Refutada |
| P24 | Con ≥ 5 repetidas, la primera repetición ocurre tras el primer resumen o la primera negativa en 2 de cada 3 | 2 de 29 | Refutada |
| P25 | Tras el primer resumen, el enunciado no está en la petición | 0 de 22 sesiones con resumen lo conservan | Se cumple |
| P26 | rich conocidas: 2 a 4 de 15 | 3 | Se cumple |

**Lo que dicen los datos.**

- El umbral de 250 caracteres se sostiene en tareas que el agente no había visto: 0 de 15 cortas entre rich y
  fastapi, 6 de 15 largas. Con las 66 pasadas anteriores, van 0 resueltas de enunciado corto.
- fastapi no vistas rinde igual que rich conocidas (3 y 3). No hay señal de que rich esté sobreajustado.
- El bucle no lo causa el resumen del arnés ni la negativa: en 27 de 29 sesiones la primera repetición llega
  antes que ambos. Y con el modelo real la sesión no sigue tras el tope: lo que el ensayo mostró con el modelo
  falso (60 rechazos por sesión) no ocurre con Gemma. Dos hipótesis sobre el arnés descartadas con una corrida.
- El enunciado sí desaparece tras el primer resumen, en las 22 sesiones que tuvieron uno; pero las repeticiones
  empiezan antes, así que no es la causa del bucle.
- Tabla de fallos de las 37 no resueltas: parche que no pasa 15, llamadas agotadas 15, tiempo agotado 5, sin
  parche 2. Errores de herramienta: 122 de comando, 4 de edición, 4 de tiempo.

**ZorzALL, primera medida con trazas reales («oye v2»).** Sesiones con alguna comprobación: 20 de 43. Que
comprueban, reaccionan al fallo y comprueban después de la última edición: 4 de 43. De las 6 resueltas, ninguna
cumple «oye v2» y solo 2 hicieron alguna comprobación; usaron 5, 8, 15, 20, 35 y 40 llamadas. Cuando una
comprobación falla, el agente reacciona (edita o comprueba distinto) en 15 sesiones y la ignora en 5. Lectura:
el agente casi nunca comprueba lo que entrega, y las que resuelve las resuelve sin comprobar. «Oye» no acompaña
hoy al acierto; es lo que H-Z2 tendría que cambiar, no lo que ya ocurre.

**Decisión de palanca (regla 2.3), a la espera del ruido de `iteracion-04`.** Las dos clases más numerosas empatan
en 15. «Parche que no pasa» es la que ZorzALL ataca: el agente entrega sin comprobar. «Llamadas agotadas» es el
bucle, cuya causa sigue sin medir. Ningún cambio se lee antes de tener el ruido en fastapi.

## Vuelta 26 — 2026-10-06, 18:45 a 19:05 UTC

**Sin subidas a Kaggle, sin GPU.** Rumbo nuevo, de [`INSTRUCCION_DATITO_DATOS.md`](INSTRUCCION_DATITO_DATOS.md):
dejar de mover el agente y contar los registros de las tareas. Tres conteos, escritos antes de cambiar nada.
Instrumento: `instrumentos/conteos_datos_tareas.py`; salida en `instrumentos/conteos_datos_tareas.json`.

**Dónde la instrucción no coincide con esta bitácora (gana la bitácora).**

- Dice «0 de 10 cortas»: desde la vuelta 25 son 0 de 16 tareas (10 de rich y 6 de fastapi no vistas).
- Dice que el dato que falta «está en el repositorio de la tarea»: la vuelta 17 ya midió que 8 de 9 citan un
  issue que no está en el repositorio. El conteo B de hoy lo confirma.
- La cuenta que pide C supone que la tabla tiene la mezcla pública; la vuelta 19 la retiró porque el conjunto
  oculto es de repositorios privados. Se hace igual, marcada como cálculo.

**A. Tareas medidas con el modelo, por resultado, largo del enunciado y repositorio.** 31 tareas que
discriminan: 16 de rich (15 con 11 pasadas, 1 con 3) y 15 de fastapi (1 pasada). Fuentes: `iteracion_01.json`,
`iteracion_02.json`, `iteracion_03.json`, `sesion_unica.json`; largos de `tasks.jsonl`.

| Repositorio | Enunciado | Tareas | Nunca resueltas | Resueltas alguna vez | Sesiones resueltas |
|---|---|---|---|---|---|
| rich | Corto (< 250) | 10 | 10 | 0 | 0 de 102 |
| rich | Largo | 6 | 1 | 5 | 33 de 66 |
| fastapi | Corto | 6 | 6 | 0 | 0 de 6 |
| fastapi | Largo | 9 | 6 | 3 | 3 de 9 |
| **Total** | | **31** | **23** | **8** | |

De las 23 nunca resueltas, 16 son cortas y 7 largas. Las 16 cortas medidas están todas ahí. En las públicas hay
47 cortas de 129 (rich 27 de 48, fastapi 16 de 67, requests 3 de 13, httpx 1 de 1); entre las 103 válidas, 40.
fastapi entra solo en este conteo, con lo ya medido en `iteracion-03`; no entra en la mejora.

**B. Qué nombra el texto de las cortas nunca resueltas, y qué hay de eso en el repositorio.** Fuentes:
`tasks.jsonl` y las instantáneas de `snapshots/` (hay 20 en disco: 9 de las 10 cortas de rich, ninguna de las 6
de fastapi).

| Medida | Cortas nunca resueltas | Largas nunca resueltas | Resueltas alguna vez |
|---|---|---|---|
| Tareas | 16 | 7 | 8 |
| Nombran un archivo, un test o un error | 0 | 4 | 4 |
| Solo un título (ni archivo, ni test, ni error) | 16 | 3 | 4 |
| Citan una referencia numerada (issue o PR) | 12 | 5 | 6 |
| Líneas no vacías del enunciado, mediana | 2 | 8 | 13 |
| Campo `hints_text` vacío | 16 | 7 | 8 |
| Con instantánea en disco | 9 | 2 | 5 |
| El número citado aparece en algún archivo de la instantánea | 0 de 9 | 0 de 2 | 0 de 5 |
| La instantánea trae historial de git | 0 de 9 | 0 de 2 | 0 de 5 |
| Nombran un módulo o un símbolo que existe en el código | 3 de 9 | 2 de 2 | 5 de 5 |

En las 47 cortas públicas: 44 solo título; 31 citan una referencia numerada; `hints_text` vacío en las 47.

**Lectura de A y B.** La masa no resuelta es la de enunciado corto: 16 de 23, y 16 de 16. Pero la mitad de la
premisa del cambio no se sostiene: la referencia que el título señala **no está dentro del repositorio** en
ninguna de las 9 instantáneas (ni el número en un archivo, ni historial de git), y el notebook corre sin
Internet. No hay nada que el agente pueda abrir. Lo que sí hay, ya medido en la vuelta 17
(`instrumentos/cortos_dev15.json`): las palabras del título aparecen en pruebas existentes en las 9 (de 1 a 7
palabras por tarea), y el agente ya lee el archivo corregido en 6 de 9 (vuelta 19) sin resolver ninguna.

**C. Cálculo, no medición.** Supone que la tabla se comporta como lo público: cortas a 0 y largas a la tasa
medida. Tasa de largas en una pasada: 6 de 15 (`iteracion_03.json`); en todas las pasadas: 36 de 75.

| Supuesto | Resueltas esperadas de 58 |
|---|---|
| Las 58 rinden como largas | 23 (una pasada) a 28 |
| Mezcla pública: 21 cortas a cero y 37 largas | 15 a 18 |
| Nota real | 3 y 4 |

Para un 4 de 58 bastan 8 a 10 tareas que rindan como largas, y las otras 48 a 50 tendrían que rendir cero; para
un 3, de 6 a 8 y de 50 a 52. La mezcla pública aporta 21 tareas a cero: explica bajar de 23 a 15, no a 3 o 4.
Faltan otras 27 a 31 tareas a cero, el 47 a 53 % de la tabla, que la mezcla pública no explica. O la tabla
tiene de 83 a 89 % de tareas que rinden como cortas, o las largas de la tabla rinden mucho menos que las
públicas (para 3 o 4 con 37 largas: 8 a 11 %, frente a 40 %). Los datos de hoy no separan las dos.

**El cambio pedido y su predicción, escrita antes de correr.** Cambio: antes de editar, el agente abre dentro
del repositorio la referencia que el título señala y escribe qué comportamiento hay que corregir. Subconjunto:
las 9 cortas de rich del conjunto de desarrollo, una pasada. Punto de partida: 0 resueltas en 99 sesiones.

| Id | Predicción | Se conserva | Se descarta |
|---|---|---|---|
| P31 | Cortas de rich que pasan de no resuelta a resuelta: 0 de 9 (a lo más 1) | 3 o más | 2 o menos |

Razón de la predicción: la referencia no está en 0 de 9; el texto añadido a la instrucción ya se probó una vez
y no cambió la conducta (regla escrita, vuelta 19); y leer el archivo correcto no bastó en 6 de 9.

**Estado.** No se corrió. El equipo no tiene GPU: correrlo es subir un notebook a Kaggle (9 tareas, unos 35 min
de sesión, cerca de 1,2 h de cuota; quedan unas 2,6 h sobre la reserva si `iteracion-04` gasta como la 03), y
eso espera el «súbela» del dueño. No se armó notebook ni se tocó el agente.

**Qué sigue sin verse.** El largo y la forma de los enunciados del conjunto oculto: es el único dato que decide
entre las dos lecturas de C, y la tabla no lo entrega. Y el ruido en fastapi, que depende de `iteracion-04`.

## Vuelta 27 — 2026-10-06, 19:05 a 19:35 UTC

**Sin subidas a Kaggle, sin GPU.** Dos trabajos: cerrar lo que marcó la revisión de la otra sesión y buscar, en
las trazas de `iteracion-03`, por qué fallan las tareas que sí traen información.

**1. Plataforma (repositorio de ALL, rama `fix/kaggle-rescate-ruta-larga-y-registro`, sin commit).**

- El rescate ya no muere con un nombre de salida largo: lo acorta, anota lo que falte en `faltantes.json` y sale
  con 4. Bajada nueva completa a las 19:10 UTC: 12 notebooks, 0 faltantes (`rescate_kaggle/2026-10-06T1910Z/`).
- `registry.json` lleva el reenvío 56830336 como `sub-003`. Es **el mismo zip** que dio 0,06: el 0,05 es ruido
  de la tabla (una tarea), no un segundo intento peor.
- Los dos zips compilan con `adk-submission` (entorno del arnés). El código 3 de la otra sesión era por correr
  la verificación en el `.venv` del repositorio, que no trae el compilador.
- Tabla a las 19:10 UTC: 1 935 equipos, mediana 6 tareas (era 5), envío propio en el puesto 1 503.
- `iteracion-04` sigue en ejecución a las 19:28 UTC. Sin leer.

**2. Fallos de `iteracion-03` con la lista cerrada de `scripts/kaggle_replicas.py`** (`classify_harness` sobre
`task_results.jsonl` de los tres zips crudos).

| Grupo | Tareas | Resueltas | `tests_failed` | `empty_patch` | `agent_timeout` | Otras |
|---|---|---|---|---|---|---|
| rich conocidas | 15 | 3 | 5 | 5 | 2 | 0 |
| fastapi no vistas | 15 | 3 | 8 | 3 | 1 | 0 |
| requests (no discrimina) | 13 | 0 | 9 | 2 | 2 | 0 |

Por largo del enunciado, en rich y fastapi: las 15 cortas dan 8 `empty_patch`, 6 `tests_failed` y 1 tiempo; las
9 largas no resueltas dan 7 `tests_failed` y 2 tiempo, todas con parche.

**3. Hallazgo: una parte del bucle es `edit_file` sin `old_string`.** Fuente: las 43 trazas de los zips crudos
de `iteracion-03`; instrumentos en `%TEMP%\claude\anat03*.py`.

| Medida | Valor |
|---|---|
| Llamadas a `edit_file` | 202 |
| Sin `old_string` (el arnés responde «faltan parámetros obligatorios») | 160 |
| Llamadas distintas a `edit_file` | 53; sin `old_string`, 11 |
| `write_file` mal formadas | 0 de 16 distintas |
| `run_command` mal formadas | 0 de 318 distintas |
| Sesiones atrapadas (12 o más fallos seguidos de la misma llamada) | 4 de 43: 12, 20, 53 y 74 repeticiones |
| De ellas, por grupo | rich 1, fastapi 2, requests 1 |
| De ellas, de enunciado largo no resuelto | 2 de 9 |
| `edit_file` en las 6 sesiones resueltas | 9 llamadas, 0 fallos |

En las 11 llamadas mal formadas solo llegan `filepath` y `new_string`; el resto del texto queda partido en
claves sin sentido. La primera edición mal formada es la primera o la segunda edición de la sesión en las 5
sesiones que tienen alguna. La traza no guarda el texto crudo del modelo: no se sabe si el modelo omite
`old_string` o si el intérprete de llamadas del servidor lo pierde. El efecto es el mismo: el agente sabe qué
escribir, la llamada no entra, y la repite idéntica hasta agotar el presupuesto.

Otro dato de las largas no resueltas: el parche toca algún archivo de la corrección de referencia en 4 de 9
(en las resueltas, 6 de 6), y 6 de 9 dejan en el parche un archivo nuevo.

**4. Candidato `h_edicion`, sin subir.** Un cambio: tres líneas en la sección de implementación de la
instrucción, que fijan el orden de argumentos de `edit_file`, dicen que repetir la llamada fallida falla igual
y dan la salida (una llamada corregida más corta; si falla, aplicar el cambio con un guion de `python3` por
`run_command`). La instrucción pasa de 3 888 a 4 531 caracteres. Carpeta `data/envios/h_edicion/`; zip
`submission_h_edicion.zip`, 3 756 bytes, huella `c58c572b44f0a3ec…`; compila y es válido. No registrado.
Sin simulacro: Docker no estaba en marcha.

**Predicción, escrita antes de correr.** Mismo notebook de `iteracion-03` con esta condición, 43 tareas.

| Id | Predicción | Se conserva | Se descarta |
|---|---|---|---|
| P32 | Sesiones atrapadas en `edit_file` sin `old_string` (hoy 4 de 43) | 1 o menos | 3 o más |
| P33 | Resueltas en rich y fastapi (hoy 6 de 30) | 5 a 8; no se declara mejora salvo 9 o más | 3 o menos |

Lo que la predicción no promete: el techo del cambio son las 2 sesiones largas atrapadas, es decir 2 tareas de
30, igual al ruido. Se lee por P32, que es el mecanismo, no por resueltas. En contra: la regla escrita de
`iteracion-02` ya decía «no repitas una llamada idéntica» y las repetidas quedaron en 40 % frente a 42 %.

**Costo y decisión.** Unas 3 h de cuota por las 43 tareas (2,2 h si solo rich y fastapi); sobre la reserva
quedan unas 2,6 h si `iteracion-04` gasta como la 03. Antes hay que leer `iteracion-04`: da la segunda medida
de las sesiones atrapadas con la configuración enviada. Subir espera el «súbela» del dueño.

## Vuelta 28 — 2026-10-06, 19:40 a 20:05 UTC

**Sin subidas a Kaggle, sin GPU.** Por indicación del dueño el concilio sumó tres roles técnicos, en paralelo y
en solo lectura: depurador, revisor SAST y DevOps. Aquí queda lo que cada uno verificó y lo que se cambió.

**1. Depurador: quién pierde `old_string`.** Veredicto: lo provoca el modelo y el intérprete del servidor no
lo tolera. Scripts en `%TEMP%\claude\dbg\`.

| Hecho | Estado |
|---|---|
| Las 160 llamadas malas tienen la misma firma: `new_string` se cierra con un acento grave (159) o una comilla (1) en vez del delimitador de cadena de Gemma, y el intérprete se traga la etiqueta de `old_string` dentro del valor | Verificado en las trazas |
| El intérprete público de vLLM (dos versiones) produce las mismas claves sin sentido con una llamada sintética que tiene ese defecto | Verificado por reproducción |
| La conversión intermedia (LiteLLM, ADK, arnés) no puede causarlo | Verificado leyendo el código |
| Son 5 eventos de origen independientes, en 5 sesiones, ninguna resuelta | Verificado |
| Las 5 sesiones tienen resumen del arnés; ninguna de las 21 sin resumen falla; 4 de 5 ocurren tras una caída de contexto | Verificado; con 5 eventos es correlación |
| 38 de 39 resúmenes del arnés contienen acentos graves de markdown; 1 de 42 llamadas buenas contiene alguno | Verificado |
| El bucle se alimenta solo: la plantilla vuelve a mostrar la llamada rota y el modelo la copia | Inferido |
| La llamada rota falla antes de ejecutarse y no descuenta del tope de llamadas: solo quema el tiempo | Inferido (74 fallos en una sesión con tope 40) |

Sin comprobar: el texto crudo del modelo (no se guardó) y la versión de vLLM de la corrida.

**Corrige lo que escribí en la vuelta 27.** El candidato `h_edicion` atacaba el síntoma y tenía dos defectos:
fijaba un orden de argumentos contrario al que el modelo ve (alfabético), y añadía acentos graves al texto de
la instrucción, que es justo el rasgo asociado al fallo.

**2. Candidato `h_edicion`, versión 2, sin subir.** Una sola línea, sin acentos graves: si `edit_file`
responde que faltan parámetros obligatorios, no volver a llamarla en esa tarea y aplicar el cambio con un
guion de `python3` por `run_command`, o con `write_file` si el archivo es chico. Instrucción de 3 888 a 4 222
caracteres. Zip `submission_h_edicion.zip`, 3 644 bytes, huella `598236b202051175…`; compila y es válido. La
huella de la vuelta 27 (`c58c572b…`) queda sin efecto.

Segundo candidato posible, no armado: quitar `edit_file` de las herramientas. Elimina el fallo por
construcción (`write_file` 0 de 16 y `run_command` 0 de 318 mal formadas), pero las 6 sesiones resueltas
usaron `edit_file` sin fallos (9 de 9): puede costar lo que hoy se resuelve. Va después del primero.

Las predicciones P32 y P33 no cambian. P32 sigue siendo la lectura principal.

**3. Revisor SAST.** Sin hallazgos críticos; 31 pruebas del rescate pasan.

| Hallazgo | Gravedad | Estado |
|---|---|---|
| El token viajaba en las redirecciones a cualquier host | Alta | Corregido en `scripts/kaggle_rescate.py`, con prueba |
| Una respuesta ilegible tumbaba la bajada y `faltantes.json` no llegaba a existir: la carpeta parecía completa | Alta | Corregido: se anota como faltante y `faltantes.json` se escribe tras cada notebook, con prueba |
| El scraper aceptaba cualquier host terminado en «kaggle.com» y direcciones sin https | Alta | Corregido en el instrumento |
| La caché del scraper da por buena una lista truncada si una página falla | Alta | Pendiente; los conteos del scraper valen solo si `errores_de_red` sale vacío |
| Dos archivos de salida con el mismo nombre en subcarpetas distintas se pisan | Media | Pendiente |
| El manifiesto puede llevar un identificador de tarea como clave si un csv ajeno no trae la columna de repositorio | Media | Pendiente; el manifiesto no entra a git hasta filtrarlo |
| Tamaños sin límite, nombres con dos puntos, sufijos falsos | Media y baja | Pendiente |

**4. DevOps.** Fuentes: fichas 10 a 12 del registro y esta bitácora.

- En `iteracion-03` la cola fue el 88 % del ciclo (unas 11 h) y la sesión el 12 % (89 min). Esta semana el
  tope es la cuota: unas 2,6 h útiles hasta el reinicio del 2026-10-10.
- Las 13 tareas de requests gastan el 37 % del tiempo de tareas (1 794 de 4 839 s) y no cuentan para
  resueltas. Sacarlas ahorra cerca de 1 h de cuota por corrida.
- Base y candidato caben en una sesión: 30 tareas, dos condiciones y la peor carga medida suman unos 121 min,
  bajo el tope de 150. `iteracion-04` fue una sesión aparte idéntica a la 03: otra cola y otras 3 h de cuota.
- La próxima sesión debe guardar el texto crudo del modelo. No cuesta cuota y cierra lo que el depurador no
  pudo comprobar.
- Riesgos de hoy: dos sesiones en el mismo árbol con 5 archivos sin commit; dos entornos Python que no
  coinciden; el código 3 de la verificación vale igual para «falta el compilador» que para «zip inválido»;
  nada impide subir dos veces el mismo notebook.
- Docker está en marcha: el simulacro de `h_edicion` se puede correr.

**Diseño de la próxima medición, propuesto, sin armar.** Una sesión: rich (15) y fastapi (15), condición
enviada y `h_edicion` versión 2, con captura del texto crudo del modelo. Unos 121 min en el peor caso, cerca
de 4 h de cuota: no cabe en las 2,6 h de esta semana. Opciones: esperar al reinicio del 2026-10-10, o medir
solo el candidato (unas 2,2 h) contra `iteracion-03` y `04` como base. Decide el dueño.

### Scraper de lo público, 19:51 UTC (misma vuelta)

Por la API oficial de Kaggle, con el token y en solo lectura; sin navegador. Instrumento
`instrumentos/scraper_publicos.py`; crudo en `rescate_kaggle/publicos_2026-10-06/` (ignorado por git). El
manifiesto quedó en `%TEMP%\claude\manifiesto_publicos.json` y no entra a git hasta filtrar sus claves
(hallazgo del revisor SAST). Hubo 3 respuestas 404: los conteos son mínimos, no exactos.

| Fuente | Conteo |
|---|---|
| Notebooks públicos del concurso | 121; con salida 97; con log 115 |
| Comentarios en notebooks | 12, en 10 notebooks |
| Foro del concurso | 134 temas, 304 comentarios |
| Product Feedback | 20 temas recientes leídos; 10 de cola, GPU o límites, con 29 comentarios |
| `eval_summary.csv` | 1 (10 filas) |
| En ese csv | 1 resuelta de 10 (fastapi 1 de 7, rich 0 de 2, requests 0 de 1); 2 con «exceeded turns»; mediana de llamadas 17 en la resuelta y 63 en las no resueltas; no resueltas sin ninguna corrida de pytest: 6 de 9 |
| `tasks.jsonl` | `hints_text` vacío en 129 de 129; enunciado de menos de 250 caracteres: rich 27 de 48, fastapi 16 de 67, requests 3 de 13, httpx 1 de 1 |

**Lo que el foro dice sobre lo ya medido aquí** (temas por palabra clave, de 134): colas y GPU 43; ruedas y
Python 3.13, 42; adaptadores 33; pytest y verificación 31; tiempo límite 29; tamaño del conjunto oculto 19;
compactación de contexto 17; ruido de la nota 14; búsqueda por similitud 13; bucles 12; `edit_file` 7.

- **Confirma el hallazgo del depurador, de forma independiente.** Otro equipo reporta que, tras el arreglo del
  2026-09-30, lo que sigue fallando es «una llamada que pierde un argumento porque una cadena se cerró con un
  acento grave»: 7 de 40 llamadas de edición en su réplica. Aquí: 11 de 53 llamadas distintas.
- **Confirma que el texto no rompe el bucle.** Dos equipos informan que «no repitas un comando idéntico» ya
  está en su instrucción y el modelo lo ignora una vez en bucle; lo único que les contuvo el daño fue bajar el
  tope de llamadas. Coincide con la regla escrita de `iteracion-02` (40 % frente a 42 %) y con el tope 20
  (mismas resueltas con la mitad de tokens, vuelta 19). Baja mi confianza en `h_edicion`.
- **Descarta el segundo candidato.** Si el modelo llama a una herramienta que el envío no declara, la tarea
  termina y el parche se pierde; el mensaje de la tarea anuncia las herramientas igual. El organizador dijo el
  2026-10-01 que lo arreglaría; el 2026-10-03 nadie había confirmado el arreglo. Quitar `edit_file` de las
  herramientas puede convertir sesiones resueltas en ceros.
- **Ruido.** Un equipo obtuvo 3 de 10 y 1 de 10 con la misma configuración. Coincide con las 2 tareas de aquí.
- **Tamaño de la tabla.** La página de datos dice «unas 120 tareas, mitad públicas y mitad privadas», y las 12
  horas cubren las 120. El rescate calcula 58 como menor tamaño compatible con las notas; 60 no es compatible
  con las notas observadas. Las dos cifras: 60 según el texto, 58 según las notas.
- **Versión del servidor.** El foro nombra vLLM 0.19.1 parcheado en el wheelhouse: es el dato que al depurador
  le faltaba, y coincide con una de las dos versiones con que reprodujo el fallo (0.19.0).

**Simulacro de `h_edicion` versión 2** (arnés real en Docker, modelo falso, 2 tareas, 4 modos): los 8
desenlaces coinciden con lo esperado. El envío no pierde tareas por una causa mecánica.

## Vuelta 29 — 2026-10-06, 20:00 a 20:12 UTC

**Subida de `iteracion-05`, 20:09 UTC.** Orden del dueño: «Lee iteracion-04 y mide solo el candidato». Es una
corrida de medición, no un envío al concurso. Ficha 13 del registro, con el candado y las predicciones P32 a
P34 escritas antes de subir.

- Notebook de la 03 y la 04 con tres cambios: condición `h_edicion` versión 2, sin requests, nombres nuevos.
  Huella `eb9fdbe6ea4fc110…`. Nueve celdas quedan byte a byte.
- Validado sin GPU: chequeo previo (19 comprobaciones), ensayo completo en Docker (30 de 30, 0 problemas),
  simulacro del zip (8 de 8) y compilación.
- Una sola subida, versión 1, en cola. El contenido remoto coincide con el validado en las 11 celdas.
- Sin captura del texto crudo del modelo: la API del servidor entrega la llamada ya interpretada, no el texto;
  haría falta el log del servidor con otro nivel de detalle. Queda fuera de esta corrida.
- `iteracion-04` seguía en ejecución a las 20:10 UTC. Un rescate a las 20:00 recibió 429 por el volumen del
  scraper; las consultas de estado ya responden.
- Cuota: no leída (exige la sesión web). Estimado: la 05 gasta 1,9 a 2,3 h; si la 04 gasta como la 03, quedan
  unas 0,3 a 0,7 h sobre la reserva de 5 h. El peor caso de la 05 (150 min) dejaría la cuenta bajo la reserva.

## Vuelta 30 — 2026-10-06, 20:15 a 20:25 UTC

**Resultado de `iteracion-04`** (el mismo notebook de la 03, byte a byte). Terminada y completa, sin cortes;
carga del modelo 652 s. Datos en `rescate_kaggle/iteracion-04/` (bajada de las 20:15 UTC, 0 faltantes).

| Grupo | Resueltas en la 03 | En la 04 | Cambian de resultado | Cambian de clase | Largas y cortas resueltas en la 04 |
|---|---|---|---|---|---|
| rich conocidas (15) | 3 | 3 | 0 | 7 | 3 y 0 |
| fastapi no vistas (15) | 3 | 4 | 1 | 6 | 4 y 0 |
| requests (13) | 0 | 1 | 1 | 3 | 1 y 0 |

| Id | Predicción | Salió | Veredicto |
|---|---|---|---|
| P27 | rich: cambian 2 o menos de 15 | 0 | Se cumple |
| P28 | fastapi: cambian 3 o menos de 15 | 1 | Se cumple |
| P29 | La clase cambia al menos el doble que el resultado | 13 frente a 1 en rich y fastapi | Se cumple |
| P30 | requests: 0 resueltas en ambas | 1 en la 04 | Refutada |

**Lo que fija.**

- **El ruido en las 30 tareas es 1.** Dos pasadas iguales dan 6 y 7 de 30, con las mismas 6 resueltas en ambas.
  La regla sigue siendo no declarar mejora por debajo de 2 tareas.
- **Las cortas siguen en cero:** 0 de 15 en la 04. Van 0 resueltas en 30 sesiones de enunciado corto entre la
  03 y la 04, y 13 de 30 en las largas.
- **P30 refutada:** una tarea de requests se resolvió en Kaggle. «Ninguna de requests discrimina» era
  demasiado fuerte; la validez medida decía que el parche de referencia no pasaba ahí. Hay que revisar esa
  tarea en la validez antes de volver a usar el grupo.
- **La clase de desenlace no es estable:** 13 de 30 tareas cambian de clase entre dos pasadas iguales. La tabla
  de fallos de una sola pasada no sirve para elegir palanca.

**Segunda base para `iteracion-05`: sesiones atrapadas en `edit_file` sin `old_string`.**

| Medida, en rich y fastapi (30 tareas) | 03 | 04 |
|---|---|---|
| Sesiones atrapadas (3 fallos seguidos o más) | 3 | 3 |
| Llamadas a `edit_file` sin `old_string` | 107 de 134 | 49 de 75 |
| Tareas atrapadas en las dos pasadas | 1 | 1 |
| Tareas atrapadas en alguna | 5 | 5 |
| De las atrapadas, resueltas en esa pasada | 0 de 3 | 0 de 3 |
| De las atrapadas en una pasada, resueltas en la otra (donde 2 de 3 no quedaron atrapadas) | 0 de 3 | 0 de 3 |

La base de P32 queda en 3 de 30, medida dos veces. El fallo no es de la tarea: solo 1 de 5 tareas se repite.

**Dato que baja lo que se puede esperar del candidato.** Las tareas que quedaron atrapadas en una pasada no se
resolvieron en la otra, tampoco cuando no quedaron atrapadas (0 de 4 sesiones libres). Evitar la trampa
recupera tiempo de sesión, pero estos datos no muestran que recupere tareas. Mi estimación para P33 baja: lo
esperable es 6 o 7 de 30, igual que la base, aunque P32 se cumpla.

**`iteracion-05`** salió de la cola en menos de 6 minutos y está en ejecución desde antes de las 20:15 UTC.

## Vuelta 31 — 2026-10-06, 21:12 a 21:25 UTC

**Resultado de `iteracion-05`** (candidato `h_edicion` versión 2 sobre las 30 tareas de rich y fastapi).
Terminada y completa, sin cortes; unos 58 min de sesión. Una sola subida, ningún fallo visible en local. Datos
en `rescate_kaggle/iteracion-05/`; lectura con `%TEMP%\claude\leer05.py` sobre el json y las 30 trazas.

| Medida, en las mismas 30 tareas | 03 (enviada) | 04 (enviada) | 05 (`h_edicion`) |
|---|---|---|---|
| Resueltas | 6 | 7 | 7 |
| rich y fastapi | 3 y 3 | 3 y 4 | 3 y 4 |
| Enunciado largo y corto | 6 y 0 | 7 y 0 | 7 y 0 |
| Sesiones atrapadas en `edit_file` sin `old_string` | 3 | 3 | 0 |
| Sesiones con alguna llamada así | 4 | 5 | 0 |
| Llamadas a `edit_file`, y de ellas sin `old_string` | 134 y 107 | 75 y 49 | 26 y 0 |
| Llamadas a herramientas, y repetidas idénticas | 1 036 y 545 | 1 021 y 489 | 925 y 405 |
| `run_command` | 494 | 487 | 568 |
| `search_similar_code` | 90 | 106 | 25 |
| Segundos por tarea | 101 | 99 | 99 |

| Id | Predicción | Salió | Veredicto |
|---|---|---|---|
| P32 | Sesiones atrapadas: 1 o menos (base 3 de 30) | 0 | Se cumple |
| P33 | Resueltas: 5 a 8; mejora solo con 9 o más | 7 | Dentro del ruido: no hay mejora |
| P34 | Tras el fallo de `edit_file`, pasa a otra herramienta | No hubo ningún fallo: sin casos | No se puede leer |

**Lectura.**

- **El mecanismo desapareció y las tareas resueltas no cambiaron.** Las 7 resueltas de la 05 son exactamente
  las 7 de la 04; las 6 que resolvieron la 03 y la 04 siguen resueltas; ninguna tarea nueva. Es lo que anticipó
  la vuelta 30: las tareas que quedaban atrapadas tampoco se resolvían cuando no lo estaban.
- **No ocurrió como lo predije.** Esperaba que el agente fallara una vez y cambiara de herramienta (P34). Lo
  que pasó es que no hubo ninguna llamada mal formada en 26. Con una base de 4 y 5 sesiones afectadas de 30,
  cero en 30 por azar es poco probable (cerca de 1 en 100 si la tasa fuera 15 %), pero es una sola pasada.
- **Cambió la conducta más de lo que la línea dice.** El agente llamó a `edit_file` mucho menos (26 frente a
  134 y 75) y a la búsqueda por similitud también (25 frente a 90 y 106), y más a `run_command`. No sé por
  qué baja la búsqueda: la línea no la nombra. Es un efecto que no predije.
- **Las repetidas bajan poco:** 44 % de las llamadas frente a 53 % y 48 %. El bucle de lectura sigue.
- **Las cortas siguen en cero:** 0 de 15, por tercera pasada.

**Decisión, con las reglas fijadas antes de correr.** P32 se cumple: `h_edicion` se **conserva como
candidato**. No es una mejora de resueltas: 7 de 30 es la base. Si se enviara, lo esperable es la misma nota
dentro del ruido de la tabla (3 o 4 tareas). No se pide un envío.

**Lo que sigue sin verse.** Si el cero en llamadas mal formadas se repite en una segunda pasada; por qué baja
la búsqueda por similitud; y el dato de fondo: qué separa las 23 tareas que nunca se resuelven de las 7 que
sí, más allá del largo del enunciado. Las 15 cortas no las mueve ningún cambio de instrucción probado hasta
hoy (regla escrita, tope 20, dos etapas, 100 llamadas, `h_edicion`).

## Vuelta 32 — 2026-10-06, 21:30 a 22:20 UTC

**Sin subidas a Kaggle, sin GPU.** Concilio sobre las 23 tareas que no se resolvieron en ninguna de las tres
pasadas (`iteracion-03`, `04` y `05`; 0 de 69 sesiones): 15 de enunciado corto y 8 de largo. Cuatro roles en
paralelo y en solo lectura. Tablas por tarea en `instrumentos/concilio_23/` (ignorada por git); aquí solo conteos.

**1. Techo (ingeniero de software).** Leyó enunciado, corrección, pruebas ocultas, código base y los parches
del agente de las 30 tareas. El veredicto es su juicio; solo ejecutó dos comprobaciones.

| Veredicto | Cortas | Largas | Total |
|---|---|---|---|
| Resoluble con el enunciado y el repositorio | 7 | 5 | 12 |
| Solo acertando una elección entre pocas alternativas | 4 | 0 | 4 |
| Solo adivinando un nombre o un texto exacto | 2 | 3 | 5 |
| No resoluble sin el issue | 2 | 0 | 2 |

- 12 de 23 pruebas ocultas exigen algo que el enunciado no dice (nombre nuevo, texto exacto, valor arbitrario,
  o un comportamiento contrario a una prueba visible). En las 7 resueltas: 0 de 7.
- Ningún registro de cambios ni documento del commit base anticipa la corrección: 0 de 23.

**2. Dónde se pierde cada tarea (depurador de trazas).** Escalón más alto alcanzado en al menos 2 de 3 pasadas.

| Último escalón estable | Las 23 | De las 12 resolubles | Las 7 resueltas |
|---|---|---|---|
| No ve o no lee el archivo que había que corregir | 10 | 6 | 0 |
| Lo lee y no lo edita | 6 | 4 | 0 |
| Edita el archivo en otra región | 2 | 0 | 0 |
| Llega a la región correcta | 5 | 2 | 7 |

Cruce propio de las dos tablas por tarea: **10 de las 12 resolubles se pierden antes de hacer una edición
pertinente.** El problema de esas no es el contenido del parche: es llegar al sitio y decidirse a editar.

- La mediana del primer intento de edición ocurre con el 80 % de las llamadas gastadas; en las resueltas, 28 %.
- El límite que ata es el de llamadas: 36 de 69 sesiones llegan a 40; 4 terminan por tiempo.
- Llamadas idénticas repetidas: 50 % (1 267 de 2 532); en las resueltas, 38 %.
- La compactación no explica que no encuentre el archivo: quien lo ve, lo ve antes de cualquier compactación.

**3. Por qué fallan las pruebas (QA).** Ningún fallo es del entorno ni del arnés: 0 de 41 sesiones con parche.

| Desenlace de las 69 sesiones | Sesiones | Tareas |
|---|---|---|
| Sin parche | 28 | 14 |
| Parche inerte (solo guiones de depuración, pruebas propias o documentación) | 16 | 9 |
| Cambio real y las pruebas fallan | 19 | 13, contando las de sintaxis rota |
| Sintaxis rota por la edición del agente | 6 | 3 |

- «Parche que no pasa» mezclaba dos cosas: de 41 sesiones con parche, solo 25 tocan el código bajo prueba.
- En 23 de esas 25 el agente pasa 0 pruebas objetivo. Una sola tarea está casi resuelta de verdad.
- La sintaxis rota sale de escapes literales al editar (5 de 6); nada comprueba la sintaxis antes de entregar.
- Los archivos de más no intervienen en ningún fallo.

**4. Defecto nuevo, medido aquí: `read_file` pierde el rango de líneas.** En 344 de las llamadas a
`read_file` de las tres pasadas el nombre del parámetro llega con una comilla pegada; el arnés lo ignora y
devuelve las primeras 150 líneas del archivo. En la 04 y la 05 son 229 de 571 llamadas (40 %).

| Grupo de sesiones | Con alguna lectura así | Con 5 o más | Llamadas así, y repetidas idénticas |
|---|---|---|---|
| Resueltas (20) | 7 | 2 | 56 y 40 |
| No resueltas, resolubles (36) | 12 | 7 | 129 y 92 |
| No resueltas, otras (34) | 8 | 7 | 159 y 131 |

Afecta a 27 de 90 sesiones y explica parte del bucle de lectura, pero **no separa** resueltas de no resueltas
(7 de 20 frente a 20 de 70). Es gasto de llamadas, no la causa de fondo. El foro da este fallo por arreglado
el 2026-10-01; en nuestras corridas del 2026-10-06 sigue ocurriendo.

**5. Inteligencia pública (analista del foro).** Fuentes en `concilio_23/foro_evidencia.json`.

- **El organizador** dice que las tareas ocultas se revisaron y editaron mucho más que las públicas, buscando
  las «imposibles». Nada oficial sobre el largo de los enunciados ocultos.
- **El razonamiento no está medido aquí.** `include_thoughts: false` lo apaga del todo y nuestro envío lo
  lleva; estuvo roto hasta el 2026-10-01; y la única prueba propia lo midió con 4 minutos, donde 11 de 13
  sesiones agotaron el tiempo (vuelta 11). Un participante publicó el 2026-10-06 un barrido local de las 129
  tareas, una corrida por celda: 23 resueltas con razonamiento apagado y 48 encendido.
- **El presupuesto importa en ese barrido:** 36 con 25 llamadas y 50 con 50; 37, 46 y 54 con 6, 10 y 15 min.
- **Ruido ajeno:** la misma configuración dio 55 y 48 de 129; un mismo zip, 0,12 y 0,15.
- **Fallos abiertos del arnés que nos alcanzan:** cualquier excepción descarta el parche ya editado; una
  herramienta no declarada termina la tarea; editar una prueba existente hace fallar la verificación; la
  compactación pierde resultados de herramientas.

**Correcciones a esta bitácora.**

- Vuelta 11, «razonamiento: descartar»: queda **sin efecto**. Lo descartado fue el razonamiento con 4 minutos.
- Vueltas 16 y 26, «las cortas son irresolubles»: demasiado fuerte. 7 de 15 son resolubles según el ingeniero.
  Lo medido es que el agente no las resuelve, no que no se pueda.
- Vuelta 26, cuenta C: suponía que el conjunto oculto tiene la mezcla pública de enunciados cortos. El
  organizador dice que el oculto se depuró aparte. La cuenta no sostiene nada.
- Vueltas 12 y 25, clase «parche que no pasa»: 16 de 41 son parches inertes. No sirve como medida de intento.

**Lo que el conjunto dice.** El agente no falla por el contenido de sus parches sino antes: en 10 de 12 tareas
resolubles no llega a una edición pertinente con 40 llamadas, la mitad repetidas, sin razonar. Las palancas con
dato a favor son dos, y ninguna está medida aquí en condiciones válidas: razonamiento encendido con tiempo
suficiente, y más llamadas. Las de instrucción (cinco probadas) no movieron resueltas.

**Medición propuesta, sin armar.** Una condición: razonamiento encendido (`include_thoughts: true`), 5,5 min
y 60 llamadas por tarea, sobre las 19 tareas que pueden moverse (las 12 resolubles y las 7 resueltas, estas
para ver daño). Base: las tres pasadas existentes, 7 de 19 en cada una.

| Id | Predicción | Se conserva | Se descarta |
|---|---|---|---|
| P35 | Resueltas de 19 (base 7, ruido 1) | 10 o más | 8 o menos |
| P36 | De las 7 ya resueltas, se mantienen | 6 o 7 | 5 o menos |
| P37 | Segundos por tarea, media | 330 o menos | más de 330 |

Costo: peor caso 19 × 330 s más la carga, unos 125 min de sesión y 4,2 h de cuota. Cuota estimada hoy: unas
5,7 h hasta el reinicio del 2026-10-10, es decir casi nada sobre la reserva de 5 h. O se rompe la reserva, o
se espera al 10. Decide el dueño. Riesgo del propio envío con esta configuración: 120 tareas a 5,5 min son
11 h de las 12 permitidas; pasarse anula el envío.

## Vuelta 33 — 2026-10-07, 00:15 a 00:35 UTC

**Orden del dueño:** «adelante, sí, arma la condición y envíala hoy», y rescatar la fecha de cierre por la API.

**Fecha de cierre, leída por la API a las 00:19 UTC.** Code Track: 2026-12-02 23:59 UTC. Fusión de equipos y
nuevos participantes: hasta el 2026-11-25. Un envío por día. Paper Track: 2026-11-12. Quedan 57 días de envíos.

**Condición `i_razona`.** La enviada con tres valores cambiados y ningún archivo más:

| Parámetro | Enviada | `i_razona` |
|---|---|---|
| `include_thoughts` | false (razonamiento apagado) | true |
| `max_tool_calls` | 40 | 60 |
| `max_time_minutes` | 4 | 4,5 |

Lo demás igual: presupuesto de razonamiento 4 096, 8 192 tokens de salida, temperatura 0,2, 100 turnos, 60 s
por comando, sin adaptadores, instrucción del kit sin tocar. No lleva `h_edicion`.

**Por qué 4,5 minutos y no los 5 que propuse.** Mi cuenta de «10 h de 12» no sumaba la verificación ni el
montaje de cada tarea. Un participante midió unas 10 h de corrida con tope de 4,5 min (foro, 2026-10-06); con
razonamiento casi todas las sesiones llegan al tope (11 de 13 en la vuelta 11). Con 5 min la corrida quedaría
cerca de 11 h, a una hora de anular el envío. Con 4,5 quedan unas 2 h de margen.

**Son tres cambios juntos, no uno.** El razonamiento sin más tiempo ya se midió y no sirve (vuelta 11); el
tiempo y las llamadas van con él. Si la nota sube, no se sabrá cuál de los tres la subió.

**Validado sin GPU.** Compila con `adk-submission`: válido. Zip `submission_i_razona.zip`, 3 494 bytes, huella
`65a0216007e19bf6…`. Simulacro en Docker con el arnés real (2 tareas, 4 modos): 8 de 8 desenlaces esperados;
el modelo recibe razonamiento encendido con presupuesto 4 096, en el agente y en el subagente.

**No medido con el modelo.** Esta condición no ha corrido con Gemma en ningún notebook. El envío es la medición.

**Predicción, escrita antes de enviar.** Base: 4 y 3 tareas de 58 con el mismo zip.

| Id | Predicción | Se conserva | No decide | Se descarta |
|---|---|---|---|---|
| P38 | Tareas de 58 en la tabla pública | 6 o más (nota 0,10 o más) | 5 (0,08): se reenvía el mismo zip | 4 o menos |
| P39 | El envío termina dentro de las 12 h | termina con nota | — | error o tiempo excedido |

Mi probabilidad de 6 o más: cerca de 1 en 3. A favor, el barrido ajeno (23 frente a 48 de 129, una corrida).
En contra: aquí el razonamiento con 4 min resolvió una menos, y 4,5 min es poco más.

**Envío, 00:26 UTC del 2026-10-07.** Referencia 56895202, estado `pending`, confirmado por la API. Un solo
envío; era el cupo del día. El resultado puede tardar hasta unas 14 h (12 de corrida y 2 de validación).
`registry.json` del repositorio se actualiza cuando llegue la nota, en un PR aparte: el árbol local sigue
compartido con otra sesión.

## Vuelta 34 — 2026-10-07, 00:28 a 00:40 UTC

**Subida de `iteracion-06`, 00:37 UTC.** Orden del dueño: «mídela»: las 19 tareas, la condición del envío
56895202, la misma regla. Corrida de medición, no envío. Ficha 14 del registro, con el candado y las
predicciones P35, P36, P37 y P40 escritas antes de subir.

- La pregunta ya no es si conviene enviar (el envío salió): es explicar la nota que llegue. Si el agente llega
  a editar en las tareas resolubles, si se queda sin tiempo o si sigue gastando las llamadas antes.
- Validado sin GPU: chequeo previo (19), ensayo completo en Docker (19 de 19, 0 problemas; el modelo recibe el
  razonamiento encendido). Una sola subida, versión 1; el remoto coincide en las 11 celdas. Arrancó sin cola.
- Cuota: no leída. Con el peor caso (3,4 a 3,8 h) la cuenta queda con unas 2 h hasta el reinicio del
  2026-10-10, bajo la reserva de 5 h. El dueño lo aceptó: esas horas no pasan a la semana siguiente.

## Vuelta 35 — 2026-10-07, 00:45 a 01:20 UTC

**Sin subidas nuevas, sin GPU.** Reglas del Paper Track leídas por la API, concilio sobre el manuscrito y
puesta al día de los documentos del caso. A las 01:16 UTC `iteracion-06` sigue en ejecución y el envío
56895202 sigue pendiente: no hay resultado nuevo de Kaggle en esta vuelta.

**Falta mía, señalada por el dueño.** Desde la vuelta 26 fui anotando los datos en esta bitácora y en el
registro, y no actualicé los documentos que se leen primero: el README del caso seguía en el estado del
2026-10-05, el recorrido paso a paso terminaba en la prueba 17 «en cola», y la página visual decía
«razonamiento: no» y «0 de 66 pasadas, 10 tareas». Quedaron corregidos en esta vuelta. Regla desde ahora: cada
vuelta que cambie una cifra vigente actualiza en el mismo paso la sección de estado del README y el recorrido.

**1. Reglas del Paper Track** (`ListCompetitionPages`, 01:12 UTC).

| Regla | Valor |
|---|---|
| Cierre | 2026-11-12 23:59 UTC; un Writeup en borrador sin enviar no se considera |
| Extensión | 3 000 palabras como máximo. No dice si cuentan las referencias |
| Contenido obligatorio | Título y subtítulo, resumen, introducción, métodos y experimentos, trabajos relacionados y citas |
| Formato | Writeup de Kaggle, o PDF listo para arXiv enlazado. Notebook público opcional |
| Idioma | No lo fija ninguna página |
| Criterios | Cinco, de 0 a 5 y a partes iguales: novedad, calidad (generalidad), relevancia, verificabilidad, claridad |
| Temas sugeridos | Incluyen «tareas y benchmarks». No exige participar en el Code Track |
| Envíos | 5 por día; el equipo no ha enviado ninguno |

El manuscrito del PR #141 tiene 3 044 palabras con referencias y 2 816 sin ellas; el de `main`, 2 790.

**2. Concilio sobre el manuscrito** (`docs/paper/manuscript.md`, versión del PR #141). Cinco revisores en
paralelo y en solo lectura; tres siguen las skills de revisión de texto público del repositorio.

| Revisor | Veredicto | Motivo principal |
|---|---|---|
| Validador estadístico | No publicar | Las tablas coinciden con sus fuentes; el veto es por afirmaciones falsas o viejas |
| Revisor redactor | Veto | «No hemos ejecutado Gemma 4», desmentido por el propio texto |
| Revisor de figuras | Veto condicionado | Las 7 figuras versionadas son de un manuscrito anterior y ninguna está citada |
| Auditor de vigencia | Premisa central vieja | 14 corridas y 3 envíos desde que se escribió |
| Investigador de papers | Apto con cambios | Las 14 referencias existen; un párrafo que corregir |

Lo que el validador dio por bueno: las dos tablas, recontadas desde el crudo; las figuras y tablas se
regeneran idénticas; la aritmética de McNemar (6 discordantes; 14,3, 9,0 y 12,5 puntos).

Lo que impide publicar:

1. «No hemos ejecutado Gemma 4» y «ninguna repetición»: falso, y dudoso ya el día que se escribió.
2. «No sabemos qué interrumpe los tests»: en 34 tareas falta un paquete que solo usan las pruebas (vuelta 6).
3. «La Tabla 1 no se repitió»: se repitió y da 103 válidas, con las 71 conservadas (vuelta 9).
4. Con 60 tareas válidas, fastapi sí es apto como repositorio de prueba y el umbral sería 10 puntos, no 14.
5. «No hemos medido la variación»: está medida en tres pares de pasadas, fuera del diseño preregistrado.
6. El desglose 35, 19 y 1 no tiene fuente en `main`: su archivo está en una rama sin fusionar.

Otros hallazgos que cambian el plan del manuscrito:

- **La validez no es novedad.** Dos notebooks públicos la midieron antes (informan 119 y 114 tareas válidas).
  Lo propio es la causa confirmada por intervención.
- **El preregistro se abandonó sin declararlo.** El repositorio de prueba se usó como desarrollo y el test de
  McNemar nunca se aplicó. Hay que decirlo y presentar lo medido como exploratorio.
- **Las predicciones de esta bitácora no tienen sello verificable:** `13_KAGGLE/` está sin seguimiento en git.
- **Balance de las 40 predicciones** (conteo del auditor): 19 cumplidas, 11 refutadas, 3 que no se pudieron
  leer, 1 sin correr y 6 pendientes.
- **Dos «P2» distintas.** La del preregistro dice «agotó tiempo o presupuesto» y se cumple (10 de 12 en la
  vuelta 11). La de esta bitácora dice «por tiempo agotado» y está refutada. No es un error de transcripción:
  son dos predicciones con la misma etiqueta. Al citarlas hay que decir cuál.
- **Citas que faltan** (existencia verificada): arXiv 2507.02825, 2411.00640, 2407.01502 y 2506.12286.

**3. Decisión del dueño.** Reescribir el manuscrito en inglés sobre el esquema nuevo: la tesis del título de
`main` («cuánto se puede creer una diferencia») con lo medido como cuerpo, y el solver determinista reducido a
una frase. En curso.

**4. Documentos puestos al día en esta vuelta.** `README.md` del caso (sección 1.8), `RECORRIDO_PASO_A_PASO.md`
(pruebas 17 a 24 y secciones 5 y 6) y `desafio_kaggle_gemma4.html` (diez celdas y un aviso de vigencia).
Siguen viejos, en el repositorio de ALL: `drafts/flujo_desafio.html`, `drafts/estado_2026-10-03.html` y la
sección 13 del `README.md`, que dicen que el modelo nunca se ejecutó.

**5. Borrador en inglés, 01:20 UTC.** `docs/paper/manuscript_en.md`, en un árbol de trabajo aparte
(`F:/Code/.aal-paper-en`, rama `paper/manuscrito-en`), sin commit ni subida: 2 761 palabras con referencias y
tablas. Cuatro tablas (validez, ruido, intervenciones, embudo), 15 referencias, desviaciones del preregistro
declaradas, solo agregados. Falta: la fila del envío con razonamiento y de `iteracion-06`; la firma del
validador estadístico sobre este texto; abrir el notebook citado como [13], que nadie leyó; y las figuras.

## Vuelta 36 — 2026-10-07, 01:20 a 01:55 UTC

**Sin subidas a Kaggle, sin GPU.** Manuscrito en inglés, tres rondas más de revisión, PDF en APA 7 y la suite
de revisión convertida en herramientas y skills del repositorio.

**1. Manuscrito en inglés.** `docs/paper/manuscript_en.md`, versionado en la rama `paper/manuscrito-en`
(PR #150, en borrador). Huella `2f96d1ae3fdd…`; 2 995 palabras con tablas y referencias, de 3 000.

Tres rondas de revisión cambiaron lo que el texto afirma:

| Lo que escribí | Por qué estaba mal | Cómo quedó |
|---|---|---|
| «Ningún cambio resuelve más tareas» | Una fila de la tabla sube de 2 a 4 | «No se estableció una mejora; el mayor aumento no se replicó; no es evidencia de que no haya efecto» |
| El umbral de tres tareas como conclusión | Tres pares de corridas no fijan una diferencia mínima detectable | Regla operativa, sin test ni potencia, dicho en el texto |
| «Las corridas idénticas difieren en 1 a 2 tareas» | Mezclaba tareas que cambian de resultado (2, 2 y 1) con cambio neto del total (0, 0 y 1) | Dos columnas distintas; y entre siete pasadas base el total va de 2 a 4 de 15 |
| «Se recuperan 32 tareas instalando paquetes» | Solo 31 son del grupo sin dependencias; una cambió sin causa conocida | 31, y la otra aparte |
| «Mediana de 80 % del presupuesto antes de editar» | Incluía 25 sesiones que nunca intentan editar | 65 % entre las 44 que intentan; 26 % en las 20 resueltas |
| «229 de 571 lecturas pierden el rango» | El crudo da 234 en dos pasadas y 344 de 851 en las tres | 344 de 851 |
| «La búsqueda no devuelve nada en 209 de 209» | 209 son solo las de sesiones fallidas | Las 221 llamadas |
| «36 sesiones agotan las llamadas y 4 el tiempo» | Salían de dos fuentes distintas | 36 con 40 llamadas o más y 5 con error de tiempo del arnés, 3 de ellas entre las 36 |
| «34 predicciones con veredicto» | Contaba como veredicto las que no se pudieron leer | 30 evaluadas: 19 cumplidas y 11 refutadas; 4 sin evaluar; 6 pendientes |
| «Reprodujimos la causa del fallo de edición» | El texto crudo del modelo no se guardó | Una llamada sintética reproduce los mismos argumentos rotos |
| «Todo se midió con Gemma 4» | Hay controles sin modelo y un juicio de revisor | Tres fuentes de evidencia, nombradas |

**2. Citas.** Pasaron de numéricas a APA 7 autor–año: 12 referencias en orden alfabético, cada una contrastada
con su registro oficial (API de arXiv o Crossref) y con su enlace pedido. Tres obras tenían versión publicada
y se citaban como preprint. Se quitaron tres citas: una porque el resumen de su versión vigente ya no decía lo
que le atribuíamos, y dos prescindibles. La frase sobre los dos notebooks públicos era inexacta: uno
reimplementa el evaluador y el otro solo repara dependencias con el evaluador oficial.

**3. PDF.** `docs/paper/manuscript_en.pdf`, 12 páginas en formato APA 7; su texto coincide palabra por palabra
con la fuente. Desviaciones declaradas: conserva los números de sección y la portada no lleva afiliación.

**4. Reglas del Paper Track sobre formato.** No mencionan Markdown, APA ni plantilla. Dos vías: el Writeup de
Kaggle, o un PDF «listo para arXiv» enlazado. La API no permite crear ni enviar un Writeup: se hace a mano.

**5. Suite de revisión, en el repositorio de ALL** (PR #149, issue #148).

| Pieza | Qué hace |
|---|---|
| `auditor-datos` (rol nuevo) | De qué medición sale cada dato, sobre qué universo y si sigue vigente |
| `revisor-figuras-tablas` (rol nuevo) | Figuras y tablas contra el texto y su fuente; formato de tabla APA |
| `validador-estadistico`, `revisor-redactor`, `investigador-papers` | Confirmados, con las reglas que salieron de esta revisión |
| `scripts/paper_check.py comprobar` | Sin red: extensión, resumen, citas y lista, tablas, cifras del resumen sin respaldo |
| `scripts/paper_check.py referencias` | Registro oficial y código de respuesta de cada referencia |
| `scripts/paper_pdf.py` | PDF en APA 7 con comparación del texto contra la fuente |
| `revisar-manuscrito`, `maquetar-apa` (skills de proceso) | El orden: lo mecánico primero, la firma al final y una sola vez |

**Estado de la firma.** El validador leyó entera la huella `2254ebc0f386…`, recontó casi todo desde el crudo y
vetó cuatro frases; están corregidas. La versión resultante, `2f96d1ae3fdd…`, no tiene firma.

**Falta mía de proceso.** Pedí la firma tres veces antes de terminar las correcciones de los otros roles: cada
ronda dejó sin firma a la anterior. Queda como regla en `revisar-manuscrito`.

## Vuelta 37 — 2026-10-07, 02:13 a 02:35 UTC

**Resultado de `iteracion-06`** (condición `i_razona` del envío 56895202: razonamiento encendido, 60 llamadas y
4,5 min; 19 tareas). Terminada y completa, sin cortes. Carga del modelo 828 s; 4 708 s de tareas: unos 92 min
de sesión, cerca de 3,1 h de cuota (estimado). Una sola subida, ningún fallo visible en local. Datos en
`rescate_kaggle/iteracion-06/`; lectura con `%TEMP%\claude\leer06.py` y `hist06.py` sobre el json y las 19 trazas.

| Medida, en las mismas 19 tareas | 03 (enviada) | 04 (enviada) | 05 (`h_edicion`) | 06 (`i_razona`) |
|---|---|---|---|---|
| Resueltas | 6 | 7 | 7 | **9** |
| De las 7 ya resueltas | 6 | 7 | 7 | 6 |
| De las 12 juzgadas resolubles | 0 | 0 | 0 | **3** |
| rich (8) y fastapi (11) | 3 y 3 | 3 y 4 | 3 y 4 | 2 y 7 |
| Sesiones que terminan por tiempo | 1 | 0 | 0 | 9 |
| Sesiones con 40 llamadas o más | 7 | 8 | 5 | 3; ninguna llega a 60 |
| Resolubles que editan el archivo de la corrección | 5 de 12 | 4 de 12 | 4 de 12 | 4 de 12 |
| Llamadas a `edit_file` sin `old_string` | 12 | 13 | 0 | 1 |
| Segundos por tarea | 93 | 96 | 88 | 248 |
| Llamadas por tarea | 30 | 31 | 28 | 26 |

| Id | Predicción | Salió | Veredicto |
|---|---|---|---|
| P35 | Resueltas de 19: se conserva con 10 o más, 9 no decide, 8 o menos se descarta | 9 | No decide |
| P36 | De las 7 ya resueltas se mantienen 6 o 7 | 6 | Se cumple |
| P37 | Sesiones por tiempo agotado: 6 o menos; 7 a 9 no decide; 10 o más, ata el tiempo | 9 | No decide, en el borde |
| P40 | Resolubles que editan el archivo de la corrección: 6 o más; 3 a 5 no decide | 4 | No decide |

**Lo que dicen los datos.**

- **Primera vez que se resuelven tareas que nunca se habían resuelto.** Tres de las 12 juzgadas resolubles,
  las tres de fastapi, cada una con 0 de 3 sesiones antes. Dos son de enunciado corto: hasta hoy iban 0
  resueltas en 138 sesiones de enunciado corto.
- **Ganancia neta de dos sobre la mejor base (9 frente a 7), con cuatro tareas que cambian:** tres ganadas y
  una perdida. Entre corridas idénticas el neto fue 0, 0 y 1, y cambiaron 1 o 2 tareas. Está por encima de lo
  visto entre idénticas y por debajo del umbral de 10 que fijé: una corrida, no decide.
- **El freno cambió de llamadas a tiempo.** De las 10 no resueltas, 9 agotaron los 4,5 minutos (6 de ellas con
  parche) y la otra fue un rechazo por contexto. Ninguna llegó a 60 llamadas. Con razonamiento, el agente usa
  menos llamadas (26 por tarea) y casi tres veces más tiempo.
- **La edición llega antes.** En las resolubles, la primera edición ocurre en las llamadas 1, 6, 8, 10, 12, 13,
  14 y 36; cuatro sesiones no editan nunca. En la base la mediana era el 65 % del presupuesto de 40.
- **Una pérdida es del arnés, no del agente.** Una tarea resuelta en 9 de 13 sesiones anteriores terminó con
  «rechazo por contexto» y sin parche: es el fallo abierto del arnés que descarta lo ya editado cuando una
  petición excede el contexto (foro, vuelta 32). El razonamiento alarga el contexto y lo hace más probable.
- **rich empeora y fastapi mejora:** 2 de 8 frente a 3, y 7 de 11 frente a 3 y 4. Con 8 y 11 tareas no se
  puede leer como efecto del repositorio.

**Lo que esto adelanta sobre el envío pendiente (56895202, misma condición).**

- A 248 s por tarea, 120 tareas son unas 8,3 h de agente; con verificación y carga queda dentro de las 12 h.
  P39 (termina dentro del plazo) es probable.
- La predicción P38 no cambia: se conserva con 6 tareas o más de 58. Este resultado público no predice la
  tabla; solo dice que la condición no rompe nada y que resuelve cosas que la enviada no resolvía.

**Decisión, con las reglas fijadas antes de correr.** P35 no decide: `i_razona` ni se conserva ni se descarta
por esta corrida. Decide la nota del envío. Si la nota no decide tampoco (5 tareas), se reenvía el mismo zip.

**Siguiente medición que estos datos piden, sin armar.** El tiempo ata: 9 de 10 fallos. Las candidatas son
subir el tope de tiempo con el razonamiento encendido, o bajar el presupuesto de razonamiento para gastar
menos tiempo por turno. El límite de 12 h del envío acota la primera: 5,5 min por tarea son unas 11 h.

**Qué sigue sin verse.** La nota del envío. Y si las tres tareas nuevas se repiten en una segunda pasada.

## Vuelta 38 — 2026-10-07, 15:15 a 16:00 UTC

**Sin subidas a Kaggle, sin GPU.** Orden del dueño: revisar el proceso, actualizar los README del repositorio,
evaluar si el concurso valida el principio de ALL y seguir iterando «con el equipo multidisciplinario, incluso
Datito». Concilio de seis roles en paralelo y en solo lectura sobre `iteracion-06` y sus tres bases. Tablas por
tarea, guiones y fuentes en `instrumentos/concilio_38/` (ignorada por git); aquí solo conteos.

**Antes de empezar: `devlog recall`** (primera vuelta que lo ejecuta). Tres consultas de operador devolvieron
1 de 5 lecciones que este ciclo ya había pagado (la imagen con Python 3.13). No aparecen la ruta fija de
`/kaggle/input`, las cuatro resubidas, el razonamiento con 4 minutos ni la línea de `edit_file`: ninguna
corrida de esta bitácora tiene episodio en el repositorio.

**Estado leído por la API a las 15:15 UTC.** Envío 56895202: `PENDING`, sin nota. Cuota de GPU: 27,64 h
usadas, 2,36 h libres, reinicio el 2026-10-10 00:00 UTC. Tabla pública (15:17): 1 981 equipos; mediana 0,10
(6 tareas), percentil 75 0,12 (7), percentil 90 0,13 (8), máximo 0,24 (14); nosotros 0,06, puesto 1 559.
El último envío puntuado de toda la tabla se hizo el 2026-10-06 a las 16:01 UTC: la cola de puntuación lleva
cerca de un día, así que el nuestro no está atrasado (inferencia; el organizador no lo ha dicho).

**1. Datito: adónde se va el tiempo** (mismas 19 tareas; recuento independiente: coincide con la vuelta 37).

| Media por sesión | 03 | 04 | 05 | 06 (`i_razona`) |
|---|---|---|---|---|
| Espera del modelo, s | 72 | 77 | 74 | 218 |
| Herramientas, s | 5 | 3 | 8 | 3 |
| Turnos del modelo | 31 | 32 | 29 | 27 |
| Segundos por turno, media | 2,4 | 2,4 | 2,6 | 8,1 |
| Tokens de salida por turno | 62 | 58 | 64 | 247 |

- El tiempo extra es más segundos por turno, no más turnos; la velocidad no cambió (unos 35 tokens por segundo).
- Las 9 sesiones cortadas por tiempo esperaban al modelo; ninguna ejecutaba una herramienta ni pruebas.
- Las 9 resueltas terminan en 60 a 267 s: 3 antes de 180 s, 7 antes de 240 s, 2 a 3 s del tope.
- Bajar el presupuesto de razonamiento a 2 048 ahorra como máximo 11 s por sesión: solo 7 de 509 turnos pasan
  de 2 048 tokens de salida (cálculo, cota superior).
- Cuenta de las 12 h con 120 tareas (cálculo): con 4,5 min, 8,5 h con la mezcla medida y 10,3 h si todas llegan
  al tope; con 5,0 min, 9,0 y 11,3 h; con 5,5 min, 9,5 y 12,3 h. La carga del modelo midió 390, 652 y 828 s.

**2. QA: qué tan cerca quedaron las 10 no resueltas.**

| Clase de la sesión no resuelta | Sesiones |
|---|---|
| Sin parche | 4 (3 por tiempo, 1 por rechazo de contexto) |
| Parche inerte: solo guiones propios | 5 |
| Cambio real en otro archivo fuente | 1 |
| Región correcta que no pasa, o sintaxis rota | 0 |

- De las 6 cortadas por tiempo con parche, ninguna había acertado (juicio): 0 de 6. Cota de «más tiempo»:
  0 por el parche tal como quedó, 2 como máximo por trayectoria.
- Las 10 leyeron el archivo de la corrección; 8 nunca intentaron editarlo.
- La tarea perdida tenía el parche de referencia ya escrito (llamada 7); después delegó en el subagente, que
  hizo 25 llamadas, y la petición 37 excedió el contexto. El arnés descartó el parche.
- El subagente: lo usaron 6 sesiones en las cuatro pasadas y se resolvieron 0; en la 06, 2 de 2 perdidas.

| Fallo mecánico, mismas 19 tareas | 03 | 04 | 05 | 06 |
|---|---|---|---|---|
| `read_file` con el parámetro roto | 58 de 161 | 76 de 195 | 81 de 167 | 6 de 174 |
| Llamadas idénticas repetidas | 50 % | 47 % | 40 % | 7 % |
| Ediciones rechazadas | 14 de 35 | 14 de 44 | 1 de 27 | 4 de 55 |
| Búsquedas por similitud vacías | 78 de 78 | 56 de 56 | 14 de 14 | 54 de 54 |
| Escrituras de guiones propios | 6 | 16 | 8 | 29 |
| Resolubles (12) que leen el archivo de la corrección | 6 | 6 | 7 | 12 |
| Resolubles con edición aceptada en ese archivo | 3 | 3 | 3 | 3 |

**3. Ingeniero del arnés: qué palancas existen en el código** (swegemma 0.2.7, leído; sin ejecutar).

- Al agotar el tiempo, el arnés toma el diff del repositorio, con los guiones sueltos incluidos; no depende
  de `submit_patch`. Cualquier otra excepción (el rechazo por contexto) entrega parche vacío.
- El subagente comparte reloj y contador de llamadas con el principal, razona con el mismo presupuesto y
  corre sin compactación. Se puede quitar o darle su propio `sampling.yaml` desde el envío.
- `read_file`: el arnés descarta en silencio todo argumento que no esté en la firma; por eso no falla. No
  hay nada configurable; solo queda la instrucción.
- La búsqueda «por similitud» es una coincidencia exacta de nombre de nodo: por eso devuelve vacío. Se puede
  no declarar, pero el mensaje de tarea la anuncia igual y llamar a una herramienta no declarada termina la
  tarea con parche vacío. No se recomienda quitarla.
- Skills: se cargan bajo demanda con cuatro herramientas más; el modelo gasta al menos dos turnos en listar
  y cargar. No están siempre en contexto.
- En esta versión la verificación usa nuestro `timeout_seconds` (60 s). No se sabe si el guion de puntuación
  hace lo mismo; en las públicas el máximo medido con parche fue 7,6 s.

**4. Inteligencia pública.** Ningún notebook declara una nota con razonamiento encendido. Los diez diseños
con nota declarada llevan instrucción propia y corta; dos de los que superan 0,12 no dan herramientas de
grafo al que edita; cinco usan 120 a 300 s por comando. Un único barrido ajeno de presupuestos de
razonamiento (129 tareas locales, una corrida por celda): 23 apagado, 50, 48 y 48 con 2 048, 4 096 y 6 144;
su repetición de una misma celda dio 55 y 48. Varios envíos ajenos con razonamiento y tope de 60 min
agotaron las 12 h. Nada nuevo del organizador desde el 2026-10-05.

**5. Auditor del método: ¿el ciclo pasa por el bucle de ALL?** No, en ninguno de los dos niveles.

| Etapa | Operación | Envío |
|---|---|---|
| Estimar | Sí, fuera del repositorio: 40 predicciones, sin sello | Sí, fuera: regla de conservar o descartar |
| Recuperar | No: ninguna vuelta anterior ejecutó `recall` | No: 9 de 9 paquetes propios sin carpeta `skills/` |
| Actuar | 14 corridas y 3 envíos | 3 envíos de 2 zips: el kit con parámetros cambiados |
| Observar | Sí, fuera: bitácora y registro; 0 episodios por corrida | Sí, fuera: trazas en datos que git ignora |
| Consolidar | Lateral: 2 episodios (un guion y el manuscrito); 0 skills para operar Kaggle | 2 candidatos de instrucción; 0 skills; la palanca 5 no empezó |
| Confirmar | El ciclo no tiene tarjeta propia | P38 pendiente |

- Errores repetidos después de anotados: 4. Uno, enviar una condición que no había corrido con el modelo
  (vuelta 33, por orden del dueño). Tres, afirmar más de lo medido (vueltas 28, 32 y 36).
- No repetidos: más de una subida por resultado (5 subidas, 5 resultados desde `iteracion-02`).
- ZorzALL hoy es un medidor de trazas en un PR en borrador (#145). No existe como configuración de envío ni
  como arnés de operación. `z_oido` arregla el entorno; no enseña una lección y no corrió con Gemma.

**6. Gestor.** `devlog board --since 100`: 6 hallazgos. Resueltos en esta vuelta los 4 de #146 y #148
(campos del tablero y comentario de evidencia). Queda uno real: #101 sin episodio en `main` (está en el PR
#130, sin fusionar). #103 exige una decisión del dueño: reformularlo como medición exploratoria o cerrarlo
como no ejecutado.

**Correcciones a esta bitácora (vuelta 37).**

- «El tiempo ata» es el desenlace, no la palanca: 9 de 10 fallos agotan el tiempo, pero ninguno de los 6
  parches cortados era correcto y 5 eran solo guiones.
- «La edición llega antes (llamadas 1, 6, 8, 10, 12, 13, 14 y 36)» contaba la escritura de guiones propios.
  Ediciones aceptadas en el archivo de la corrección entre las resolubles: 3 (llamadas 8, 12 y 14).
- «Resolubles que editan el archivo de la corrección: 4 de 12»: 4 lo intentan; 3 con edición aceptada, igual
  que en las tres bases.
- «Siguiente medición: subir el tiempo o bajar el presupuesto de razonamiento»: ninguna tiene respaldo.
  Bajar el presupuesto devuelve como máximo 11 s por sesión; subir a 5,0 min recupera como máximo 2 tareas
  (juicio) y 5,5 min no cabe en el peor caso de las 12 h.

**Desacuerdos del concilio, y cómo quedan.**

- Datito propuso subir el tope a 5,0 min; QA mostró que el tiempo extra no habría recuperado ningún parche.
  Queda la lectura de QA: responde justo lo que Datito dejó como «sin verse».
- QA propone quitar el subagente; el ingeniero, darle un `sampling.yaml` sin razonamiento. Las dos atacan
  lo mismo (reloj compartido y contexto sin compactar). Quitarlo es el cambio más simple de leer: 0 de 6.

**Lo que el conjunto dice.** El razonamiento arregló lo que las instrucciones no pudieron: localizar (12 de
12 resolubles leen el archivo, antes 6 o 7) y dejar de repetir (7 % de llamadas idénticas, antes 40 a 50 %).
No cambió la decisión de editar: 3 de 12 en las cuatro pasadas. Lo que queda es un agente que encuentra el
archivo, escribe guiones de reproducción en vez de editarlo y agota el reloj esperando al modelo.

**Orden de medición propuesto. Primero el ruido; después un cambio por corrida.**

1. `iteracion-07`: segunda pasada de `i_razona`, recortada a la cuota que queda. **Armada y ensayada; no
   subida.** Espera el «súbela» del dueño.
2. Tras el reinicio del 2026-10-10: `i_razona` sin subagente, sobre las 19.
3. Después: la primera condición con una lección consolidada (editar el archivo antes de escribir guiones),
   contra un texto de relleno del mismo largo. Es la palanca 5 de la instrucción y la primera prueba real del
   bucle de ALL en el envío.

**`iteracion-07`, lista para subir.**

| Campo | Valor |
|---|---|
| Qué cambia respecto de la 06 | Nada en el agente: la misma condición (huella `0f52de0b84cb`) |
| Tareas | 10 de las 19: las 7 ya resueltas antes de la 06 y las 3 que la 06 resolvió por primera vez (7 de fastapi, 3 de rich) |
| Orden | fastapi primero: ahí están las 3 nuevas, y un corte por sesión no debe dejarlas fuera |
| Tope de sesión | 60 min desde el arranque, 5 de margen; tope del notebook 64 min |
| Costo | Hasta 64 min de sesión: 2,13 h de las 2,36 h libres, que se pierden el 2026-10-10 |
| Huella del notebook | `28bfe9f2b18163cc…`, 54 503 bytes; nueve celdas byte a byte con la 03 |
| Chequeo previo | Se puede subir, 19 comprobaciones |
| Ensayo completo en Docker, arnés real y parche de referencia | 10 de 10 validadas, 0 problemas, 190 s; el modelo recibió razonamiento encendido, 4 096 y 8 192 |
| El notebook no existe en Kaggle | Comprobado por API |

Mi primer ensayo salió «no pasa»: el error estaba en mi guion de ensayo, que esperaba los archivos de salida
en otro orden, no en el notebook. Corregido el guion, pasa.

Si la carga del modelo tarda lo peor visto (947 s antes de la primera tarea), alcanzan a empezar 8 o 9 tareas.

| Id | Predicción, escrita antes de subir | Se sostiene | No decide | Fue ruido |
|---|---|---|---|---|
| P41 | De las 3 tareas resueltas por primera vez en la 06, se resuelven otra vez | 2 o 3 | 1 | 0 |
| P42 | De las 7 ya resueltas se mantienen (en cuatro pasadas: 6, 7, 7 y 6) | 6 o 7 | — | 5 o menos |
| P43 | Sesiones que terminan con rechazo por contexto (en la 06: 1 de 19) | 0 o 1 | — | 2 o más: el fallo es sistemático con razonamiento |

Mi probabilidad de que P41 se sostenga: cerca de 3 en 5. A favor: en las tres el razonamiento cambió la
localización (antes no leían el archivo; ahora lo leen en las llamadas 4, 5 y 9). En contra: una sola pasada.

**El cupo de envío del 2026-10-08.** Sin nota del 56895202 no decide nada. Regla ya fijada (P38): con 6
tareas o más se conserva; con 5 se reenvía el mismo zip; con 4 o menos se descarta. En dos de los tres casos
lo que toca es reenviar el mismo zip, que además da la segunda nota de esta condición (el ruido de la tabla
con razonamiento). Requiere la aprobación del dueño con la orden a la vista. `i_razona` ya corrió con el
modelo en `iteracion-06`.

**Qué sigue sin verse.** La nota del envío. Los tokens de razonamiento reales por turno. Si el rechazo por
contexto ocurrió en el agente principal o en el subagente. El método de los equipos con 0,17 o más.

### Resultado del envío 56895202, leído a las 15:55 UTC: `ERROR`, sin nota

A las 15:15 UTC seguía `PENDING`; a las 15:55 la API lo da como `ERROR`, sin nota pública. La API no entrega
el texto del error: solo se ve en la página de envíos, con la sesión web del dueño.

| Id | Predicción | Salió | Veredicto |
|---|---|---|---|
| P39 | El envío termina dentro de las 12 h, con nota | Error, 15 h y media después de enviar | **Refutada** |
| P38 | 6 tareas o más de 58 | Sin nota | No se puede leer |

**Lo que no sé.** La causa. Dos lecturas caben y no las puedo separar sin el texto del error: que la corrida
pasó de las 12 h, o un fallo de otro tipo. A favor de la primera: envíos ajenos con razonamiento agotaron el
plazo (foro, 2026-10-06) y mi cuenta daba 10,3 h en el peor caso, con poco margen si las tareas ocultas
montan más lento o si todas llegan al tope. En contra: nada medido.

**Fallo mío de cálculo, si la causa es el plazo.** La vuelta 37 dijo «P39 es probable» con 8,3 h de agente
calculadas sobre 19 tareas públicas elegidas, de las que 9 terminaron antes del tope. En el conjunto oculto
nada garantiza esa fracción.

**Lo que esto cambia, ya.**

- El reenvío del mismo zip el 2026-10-08 queda **retirado**. No se reenvía una configuración que dio error.
- `i_razona` no se conserva como condición de envío, por la regla fijada (P39: error o tiempo excedido).
  La señal medida en notebook (9 de 19) sigue en pie como dato; lo que falla es que quepa en el envío.
- `iteracion-07` sigue armada, pero su valor depende de la causa: si fue el plazo, lo que hay que medir con
  las 2,36 h es el razonamiento con un tope que quepa con holgura, no la misma condición otra vez. No la
  rearmo sin el texto del error.

**El único dato que falta y quién lo tiene.** El mensaje de error del envío 56895202 en la página
«Submissions» del concurso. Lo ve el dueño con su sesión.

### El texto del error, leído por la API a las 16:25 UTC

Corrección: la API sí lo entrega. El listado en tabla no lo muestra, pero el objeto del envío trae el campo
`errorDescription`: «A system error. Please try resubmitting to resolve the error and contact Kaggle Support
if it persists.» Y `totalBytes = 0`; los dos envíos anteriores guardaron 86 883 y 72 047 bytes.

**Lo que cambia.**

- Es un error genérico de sistema, no un mensaje de plazo excedido. No dice nada de la condición.
- Con 0 bytes guardados, cabe que el archivo ni siquiera llegara a puntuarse. Es inferencia, no dato.
- Me precipité arriba: «P39 refutada», «la condición no se conserva» y «el reenvío queda retirado» daban por
  hecho que el fallo era de la configuración. P39 y P38 quedan **sin poder leerse**; la condición ni se
  conserva ni se descarta; y reenviar el mismo zip vuelve a ser lo indicado, que además es lo que pide Kaggle.
- No sé si un envío con error consume el cupo del día.

**Decisión que espera al dueño.** Reenviar `submission_i_razona.zip` (huella `65a0216007e19bf6…`), con la
orden a la vista. Sigue en pie el riesgo del plazo: 10,3 h en el peor caso calculado.

### Reenvío y subida de `iteracion-07`, 16:25 y 16:26 UTC

**Orden del dueño:** «Sí, reenvía el mismo zip y sube iteracion-07».

- **Envío 56916129**, 16:25:34 UTC: el mismo zip, huella `65a0216007e19bf6…` comprobada antes de enviar, 3 494
  bytes. Estado `PENDING`. Kaggle informa 0 envíos restantes hoy: el envío con error sí consumió cupo, o el
  cupo es de dos al día; no lo sé. Predicciones: las mismas P38 y P39 de la vuelta 33.
- **`cs4all/iteracion-07`**, versión 1, 16:26 UTC: una sola subida, encadenada al chequeo previo (19
  comprobaciones). Cuota leída justo antes: 2,36 h libres. El contenido remoto se bajó y coincide con el
  validado en las 11 celdas; privado, GPU, sin Internet, imagen fijada, `NvidiaL4`. Estado: en cola.
  Tope del notebook 64 min. Predicciones P41 a P43, fechadas en el issue #103 antes de subir.

## Vuelta 39 — 2026-10-08, 17:45 a 21:45 UTC

**Nada se subió, se envió ni se contrató en esta vuelta.** Dos rescates de solo lectura y siete roles en solo
lectura. Informes completos y guiones en `data\rescate_kaggle\instrumentos\concilio_39\` y
`data\rastreo_2608_05643\` (ignorados por git).

### Qué se leyó

| Qué | 21:13 UTC (`2026-10-08T2113Z`) | 21:37 UTC (`2026-10-08T2137Z`) |
|---|---|---|
| Envío 56895202 (`i_razona`, 65a02160…) | `error`, 0 bytes, sin mensaje | **`complete`, nota 0,08 (5 de 58), 79 355 bytes** |
| Envío 56916129 (el mismo zip) | `error`, 0 bytes, «A system error…» | igual |
| Envíos contados en la tabla pública | 8 472 | 8 660, sin moverse la fecha del último puntuado |
| `iteracion-07` | completa | completa |

Kaggle volvió a puntuar el 56895202 sin que hiciéramos nada. Un `error` genérico no es un estado final.

**`iteracion-07`** (10 tareas, condición `i_razona`): 9 de 10.

| Id | Predicción | Salió | Veredicto |
|---|---|---|---|
| P41 | Las 3 tareas nuevas de la 06 se repiten (2 o 3) | 3 de 3 | Se sostiene |
| P42 | De las 7 ya resueltas se mantienen 6 o 7 | 6 de 7 | Se sostiene |
| P43 | Rechazos por contexto, 0 o 1 | 0 | Se sostiene |
| P39 | El envío termina dentro de las 12 h, con nota | Nota 0,08 tras una repuntuación; el plazo no se puede leer | Sin poder leerse |
| P38 | 6 tareas o más de 58 | 5 | No decide (regla escrita en la vuelta 33) |

El 9 de 10 no se compara con los 9 de 19: las diez se eligieron por haberse resuelto. Solo informa la réplica
de las 3 nuevas (0 de 9 sesiones antes, 3 de 3 ahora), y es efecto de tres cambios juntos.

Notas del equipo a la fecha: 0,06 y 0,05 (sin razonamiento), 0,08 (con razonamiento, 60 llamadas, 4,5 min).
Son 4, 3 y 5 tareas de 58. No hay diferencia medible.

### Fallos de esta vuelta, del orquestador

1. Afirmé «el zip con razonamiento dio error dos veces» con una sola lectura del estado. A los 24 minutos era
   falso.
2. Afirmé «las iteraciones 03 a 07 traen dos logs por tarea» mirando que los archivos existían. Los
   `logs/<tarea>.log` pesan 0 bytes: 155 de los 290 `.log` de los zips «crudo» están vacíos. Tres roles
   repitieron el mismo error.
3. Fijé como «presupuesto del envío» el del zip `a_ajustado` sin leer la bitácora: el último enviado era
   `i_razona`.
4. Di una estimación de costo de GPU de memoria y repetí un piso de US$0,33 que no tenía URL abierta.

### Lo que el concilio midió

- **Potencia** (Datito, recalculada por el auditor): con 19 tareas y una pasada, una mejora real de +2 se
  detecta 1 a 2 veces de cada 100. El suelo de `analisis_replicas.md` (6 discordantes a favor) no se alcanza.
  Ninguna decisión de conservar o descartar tomada hasta hoy pasa ese suelo.
- **Cortes** (forense, sobre 145 sesiones de 03 a 07): 22 por tiempo, todas esperando al modelo; 2 por tope de
  llamadas con corte del arnés; 1 por contexto. El parche se conserva tras el corte por tiempo y se pierde
  tras el rechazo por contexto. QA cuenta 61 «cortadas» porque incluye las que entregaron al borde del tope de
  llamadas sin corte del arnés: falta una sola definición.
- **Causa del corte en disco** (QA): escrita en `task_results.jsonl` en 21 de 61; solo en el log del notebook
  en 4; en ningún archivo, solo deducible, en 36. En las 22 de tiempo no queda la petición en vuelo.
- **Huecos de registro** (forense): el motivo del corte se borra cuando la tarea se resuelve; la petición solo
  se registra si termina bien; no hay log de vLLM ni memoria de GPU; 01, 02 y `sesion-unica-a` no tienen nada
  por tarea; los envíos no dejan log.
- **Parches que no pasan** (QA, 14 en 03 a 05): en 13 lo único que falla es una prueba que el agente no ve o
  que el evaluador reescribe. 8 de 38 resueltas vieron rojo sobre un parche ya correcto.
- **Paper de Bilal et al., arXiv:2608.05643v1**: el método (N=8, D=4, 104 generaciones por tarea) no cabe; sin
  voto, la corrección sola da beneficio neto negativo en tres de sus cuatro modelos (su Fig. 4b). Su derivado
  «ejecuta una prueba y edita solo si falla» queda sin señal de dónde recuperar, por lo anterior.
- **Público** (hasta el 2026-10-06; después, no medido): el mismo «system error» lo reportan otros tres
  participantes sin respuesta; 767 equipos con 7 tareas o más; el zip público de dos etapas (0,13 declarado)
  es reproducible byte a byte, huella `6b3ebb33…`; no hay forma de sacar logs de un envío.
- **Cómputo** (DevOps, con URL abierta): el checkpoint pesa 23,27 GB, no 16 a 18; no cabe en 24 GB. GPU de
  48 GB entre US$0,49 y 1,09 por hora. La factura total no está medida: depende de una velocidad que nadie
  midió.

### Lo que cada rol retiró tras la nota 0,08 y los logs vacíos

- **Forense:** «dio error las dos veces»; sus ramas de plazo, caída propia y rechazo al cargar para ese envío;
  y reenviar `a_ajustado` como control.
- **Datito:** «31 nunca resueltas en 250 sesiones» (son 166); los contrastes con p ≈ 0,05 (no sobreviven a 6
  comparaciones); «3 veces menos en lo oculto»; «6 resueltas cortadas» (son 4); la vara «12 de 14 estables».
- **Inteligencia pública:** «dejar de enviar la condición con razonamiento» y gastar el próximo cupo en el zip
  público.
- **Auditor:** «con rastro suficiente: 03 a 07»; con el criterio corregido ninguna de las 7 iteraciones es una
  corrida válida.
- **zorzALL:** su borrador de H-Z2 v2.
- **DevOps:** la factura en dólares y los precios sin URL propia.
- **QA:** «leí logs»: trabajó con trazas; su guion mostró los 145 vacíos y no lo informó.

### Pareceres, copiados tal cual (escritos antes de conocerse la nota 0,08)

**Forense.**
1. Afirmo que (a) y (b) difieren en las tres cosas declaradas y en la fecha interna del zip, que juzgo inocua.
2. Afirmo que los dos zips pasan igual el validador publicado del arnés; `4.5` es un tipo admitido.
3. Afirmo que `totalBytes` 0 significa que la etapa 1 no entregó su parquet de parches; la salida con
   pensamientos no puede ser la causa.
4. Afirmo que (b) 1 tardó entre 14,8 y 15,5 h en dar error: no fue un rechazo al cargar.
5. Afirmo, con la tabla pública, que los dos errores cayeron en ventanas de puntuación degradada: 23 h sin
   ninguna nota nueva el 10-07, y 13 notas donde suele haber unas 400 el 10-08.
6. Mi causa más probable es la plataforma (≈60 %); plazo ≈15 %, caída propia de la condición ≈20 %, rechazo al
   cargar ≈5 %.
7. No sé el motivo exacto: los envíos no dejan log y `inference.py` no está publicado.
8. Sobre los cortes: 22 de 145 sesiones por tiempo, todas esperando al modelo; el diff se salva salvo en el
   rechazo por contexto.
9. Hallé que los 145 logs por tarea están vacíos y que el motivo del corte se borra cuando la tarea se
   resuelve.
10. Propongo no probar más condiciones: vigilar la tabla pública, reenviar (a) como control cuando el flujo
    esté sano, y antes arreglar el registro.

**QA de parches.**
1. Afirmo que la ganancia del razonamiento es de pensar y no de presupuesto: las 6 sesiones nuevas usan 34
   llamadas o menos y dejan su última edición antes de los 240 s; 17 de 18 resueltas caben en los topes
   viejos.
2. Afirmo que la tarea perdida se pierde por tomar en serio una prueba visible que afirma el defecto: en la 06
   editó bien y la vio fallar; en la 07 la vio pasar y no editó.
3. Afirmo que «ejecuta una prueba y edita solo si falla» no tiene de dónde recuperar: en 13 de 14 parches
   malos lo único que falla es una prueba que el agente no ve, o una que el evaluador reescribe.
4. Las dos sesiones que corrieron pytest probaron su propio archivo: una prueba pasaba sin arreglo y la otra
   se corrigió a sí misma hasta dar verde.
5. El riesgo es simétrico o peor: 8 de 38 resueltas vieron rojo sobre un parche ya correcto, y el parche
   oculto reescribe una prueba existente en 28 de 129 tareas públicas.
6. De 61 sesiones cortadas, 48 son de tareas que nunca se resolvieron en 250 sesiones, 8 se evitaban con otra
   conducta, 1 con otra regla del arnés y 4 se resolvieron igual. Subir topes no recupera ninguna.
7. No sé qué dice el resto de la suite visible con cada parche, ni si algún estado intermedio correcto fue
   sobrescrito.
8. Propongo, antes de otra condición con GPU, medir en `aal-ensayo:local` los 14 parches malos y los 38 buenos
   contra las pruebas visibles: es gratis y decide si la señal existe.
9. Lo único con respaldo hoy es una comprobación de sintaxis antes de entregar: no puede dar falsa alarma
   sobre un parche correcto, y recupera a lo sumo 1 de 14 aquí.
10. Mi veredicto se cae si esa tabla da rojo en 5 o más de los 14 malos y en 1 o menos de los 38 buenos.

**Inteligencia pública.**
1. Afirmo que nuestro «system error» con 0 bytes es una clase que otros tres participantes reportaron sin
   respuesta del organizador.
2. Afirmo que no es el mensaje que el foro asocia al plazo de 12 h, que se describe como «notebook timed out».
3. Afirmo que el primer error no nos costó cupo: dos envíos aceptados el mismo día UTC con tope de uno.
4. Afirmo que nadie en público declara nota con `include_thoughts: true`; los paquetes de 0,10 o más llevan el
   razonamiento apagado.
5. Afirmo que el zip público de 0,13 es reproducible byte a byte desde lo guardado: 4 667 bytes, SHA-256
   `6b3ebb33…a92f6`.
6. Afirmo que el techo sigue en 0,24 con un solo equipo y que el grueso subió: 767 equipos con 7 tareas o más,
   contra nuestras 3 a 4.
7. Afirmo que no existe vía pública para sacar logs de un envío puntuado; el log por tarea solo existe en
   corridas propias.
8. No sé la causa del error, cuánto tardó el segundo, qué pasó en el foro desde el 10-06 ni el método de los
   equipos de 0,17 o más.
9. Propongo reabrir el descarte de las dos etapas midiéndolo donde importa: enviar ese zip tal cual, con
   predicción escrita antes.
10. Propongo que toda condición con razonamiento pase primero por una corrida propia con `task_results.jsonl`
    completo antes de gastar otro cupo.

**Auditor del método.**
1. Afirmo que con 19 tareas y una pasada no puedo decidir nada sobre resueltas: el suelo es de 6 discordantes
   y una mejora de +2 se detecta 1 vez de cada 100.
2. Afirmo que el caso usa el vocabulario de ALL y no su bucle: 0 episodios por corrida, `recall` en 1 de 38
   vueltas, 5 fallos repetidos después de anotados.
3. Afirmo que 105 de 250 sesiones (01 y 02) y los 4 envíos no dejaron rastro por tarea, y que sobre ellos se
   tomaron cinco descartes y un envío.
4. Corrijo a Datito: «3 veces menos en lo oculto» y los dos contrastes con p cercano a 0,05 no se sostienen;
   «31 nunca resueltas» son 166 sesiones, no 250.
5. Confirmo su tabla de potencia y la réplica de las 3 tareas nuevas (0 de 9 contra 3 de 3, p = 0,0045), que
   es efecto de tres cambios juntos.
6. Sobre los cortes: se anotaron como clase; la causa del corte por tiempo se midió en la vuelta 38, después
   de mover el tope en la 33.
7. No sé por qué el zip con razonamiento da error con 0 bytes, ni cuánto rinde Gemma en código no visto, ni si
   `recall` cambiaría una decisión.
8. Propongo, en vez de otra condición: adoptar «corrida válida» y «decisión válida», escribir un episodio por
   vuelta con sus fallos, y no enviar nada que no tenga una corrida válida.
9. Propongo una regla de parada: 60 tareas no vistas por brazo, McNemar exacto, un contraste por semana, y
   fecha límite el 2026-10-22 para tener el instrumento externo calibrado.

**zorzALL.**
1. Afirmo que H-Z1, leída como manda el guion congelado (tareas válidas, por condición, perfil primario), sale
   «apoyada» en A, H e I: 6 de 15 contra 7 de 45, 5 de 12 contra 2 de 18, y 5 de 7 contra 13 de 22.
2. Afirmo que eso vale poco: la regla no usa p, el perfil completo es no evaluable en las tres condiciones, y
   la revisión ya dijo que saldría «apoyada» casi siempre.
3. Controlando por tarea queda una señal débil del perfil primario (6 contra 3,9 esperadas, p = 0,06) y
   ninguna de «oye» (4 contra 4,2).
4. Afirmo que «acierta una vez» describe al agente sin razonamiento (19 de 21 resueltas) y no al que razona (7
   de 18; 8 entregan más de una vez).
5. Sobre «probar antes de entregar»: 15 de 145 sesiones prueban tras la última edición, y 3 de ellas
   entregaron igual un parche que no pasa. Los datos no deciden; son observación.
6. No sé si obligar a probar ayuda o rompe: nunca se intervino, y TDAD advierte que la instrucción sola puede
   empeorar.
7. Propongo registrar una v2 en archivo nuevo, con las 145 sesiones declaradas exploratorias y los umbrales
   congelados antes de leer tareas no vistas.
8. Propongo una sola prueba de H-Z2 v2: prueba tras la última edición contra relleno del mismo largo, 60
   tareas no vistas o más, conteo pareado de rotos y recuperados.
9. Es mejor que seguir probando condiciones porque ataca una conducta medible y tiene una refutación escrita
   antes de gastar.

**Datito** (no dejó bloque de parecer; su voto en la convocatoria): cerrar las puertas 1 y 2 con un solo agente
limpio sobre el rescate `2137Z`, arreglar y ensayar en local el registro de causa por tarea, y no subir, enviar
ni contratar nada hasta que ese ensayo pase.

**DevOps** (ídem): no contratar nada; primero contrato de registro, manifiesto con bytes y ensayo local de los
tres cortes, y las puertas 1 y 2 las hace un agente nuevo que no herede este relato.

### Decisión del concilio (seis votos de seis, tras la nota 0,08)

**Se deja de probar condiciones. Primero se arregla el instrumento.** En este orden:

1. **Puertas 1 y 2 del encargo del dueño** (`prompt-reflexion-recursiva-rescate.md`), por un solo agente nuevo
   que no hereda este relato: recibe el encargo, el rescate, la lista de la puerta 0 y las afirmaciones como
   frases sin cifras (`concilio_39\afirmaciones_a_verificar.md`). Los informes de los roles se contrastan al
   final. Si su recuento difiere, vale el suyo y se anota la diferencia.
2. **Contrato de registro.** Por tarea y con bytes mayores que 0: traza, parche, salida de pruebas, motivo de
   fin en campo propio aunque se resuelva, reloj del agente sin montaje, y la petición registrada al iniciar,
   no solo al terminar. Por corrida: log de vLLM, memoria de GPU, y un manifiesto con bytes y huella de cada
   archivo, escrito también si la corrida muere. La celda final falla si hay un archivo vacío.
3. **Rescate.** Un archivo exigido de 0 bytes va a `faltantes.json` y el código es 4, nunca 0, con una prueba
   que falle sin el cambio. Cada lectura de `envios.json` se guarda con su hora; un `error` genérico se anota
   «sin lectura» y se relee.
4. **Ensayo local** en `aal-ensayo:local` con el modelo falso: un corte por tiempo, uno por llamadas y un
   rechazo por contexto, forzados. Pasa cuando los tres dejan causa y petición en vuelo en disco, y cuando
   vaciar un log a propósito hace salir el rescate con 4. Docker estaba apagado a las 21:40 UTC.
5. **Medición gratis de QA**: los 14 parches que no pasan y los 38 que pasan contra las pruebas visibles, en
   local. Decide si «probar antes de entregar» tiene señal. Antes de eso no se registra H-Z2 v2.
6. **Episodio de esta vuelta** en `learning/episodes/`, con tres lecciones: no afirmar el estado de un envío
   con una sola lectura; no decir «hay logs» sin mirar bytes; no decidir con 19 tareas.

**Criterio adoptado, pendiente de la aprobación del dueño.**

> **Corrida válida.** Cuenta solo si cada tarea deja en disco, con bytes mayores que 0 y con huella: traza,
> parche, salida de pruebas y una fila con el motivo de fin aunque se resuelva, más la última petición en
> vuelo; y si quedan el notebook o zip exacto, el log completo de la sesión y las predicciones fechadas antes
> de subir. Un envío a la tabla no es una corrida válida: es una nota.
>
> **Decisión válida.** Conservar o descartar exige predicción previa con umbral, el mismo conjunto de tareas
> en los dos brazos, 60 tareas o más por brazo o 6 discordantes a favor, McNemar exacto con p ≤ 0,05 y una
> repetición de la base en la misma semana. Con menos, el resultado es «exploratorio» y no cambia lo enviado.

**Qué no se hace todavía, y qué lo desbloquea.**

| No se hace | Lo desbloquea |
|---|---|
| Subir un notebook o enviar un zip | El ensayo local del paso 4 en verde |
| Contratar una GPU | El paso 4 en verde, la puerta 2 cerrada y la orden del dueño |
| Conservar o descartar `i_razona` | Una segunda nota del mismo zip (el 56916129 puede repuntuarse solo) o 60 tareas por brazo |
| Probar «ejecuta una prueba antes de entregar» | La tabla del paso 5 |
| Subir topes de tiempo o de llamadas | Nada medido lo justifica |

**Desacuerdos que quedan abiertos, con el dato que los cierra.**

- Qué es un «corte»: 25 (forense) o 61 (QA). Lo cierra una definición única y el recuento de la puerta 2.
- Si la ganancia del razonamiento cabe en el presupuesto viejo: en llamadas sí (QA); en reloj no se sabe
  (Datito). Lo cierra el reloj del agente sin montaje, que hoy no se guarda.
- GPU externa: Datito la propone como salida; auditor, QA y DevOps la ponen después del registro («un
  instrumento más rápido con logs vacíos pierde más rápido»); inteligencia pública pide antes correr una vez
  las 9 tareas propias en Kaggle, porque si Gemma resuelve 0 el instrumento externo no tiene señal.

**Lo que no sé.** La causa del error del 56916129. Cuánto rinde Gemma en código que no vio. Qué pasó en el foro
desde el 2026-10-06. Si el modelo carga con el contexto completo en una GPU de 48 GB.

### Después del concilio, 21:47 UTC

- **Criterio aprobado por el dueño:** «Apruebo el criterio». «Corrida válida» y «decisión válida» quedan vigentes desde hoy.
- **Episodio de la vuelta:** `learning/episodes/065-issue-103-vuelta-39-concilio-y-registro.json`, en el PR #153 del repositorio (sin fusionar; en revisión independiente). `devlog recall "leer el estado de un envío a Kaggle"` devuelve la lección nueva en una copia local.
- **Docker encendido por el dueño.** Con eso arrancó el paso 5 del plan: QA mide en local los 14 parches que no pasan y los 38 que pasan contra las pruebas visibles. Sin resultado todavía.
- **Paso 1 en curso:** un agente nuevo, sin el relato, ejecuta las puertas 0 a 2 del encargo. Sin resultado todavía.
- Nada se subió, se envió ni se contrató.

### Puertas 0 a 2, por un verificador que no heredó el relato (rescate `2026-10-08T2141Z`, código 0)

Informe completo: `instrumentos\puertas_2026-10-08\informe_puertas.md`. Recibió las afirmaciones como frases
sin cifras y abrió esta vuelta solo después de dejar sus medidas en disco. Donde difiere, vale su recuento.

| Afirmación del relato | Marca | Su medida |
|---|---|---|
| Estado de los envíos; cambió entre rescates | Se sostiene | 56895202 pasó de `error` a `complete`, 0,08; 56916129 sigue en `error`, 0 bytes, sin causa |
| Qué zip se envió | No medido desde la bajada | Kaggle no deja bajar el zip; el vínculo es la descripción del envío. Los zips locales coinciden |
| `iteracion-07`, 9 de 10 | Se sostiene | Las 10 ya se habían resuelto alguna vez; ninguna es nueva |
| «76 corridas y 47 fallos» en 03 a 06 | **Se cae** | Son **135 sesiones** (43, 43, 30 y 19): 30 resueltas y 105 no. El 76 contaba solo las 19 tareas elegidas, sin decirlo |
| Sesiones que prueban antes de entregar | **Se cae** la cifra | 22 de 135 antes de la primera entrega; 9 de 58 entre los parches que no pasan |
| El razonamiento alarga la sesión | Se sostiene, confundido | Mediana 81 s sin él y 224 s con él; la condición cambia a la vez el tope de tiempo y el de llamadas |
| Los logs por tarea tienen contenido | **Se cae** | 145 de 145 `logs\<tarea>.log` con 0 bytes; 155 de 290 `.log` vacíos |
| Cortes por clase | Se sostiene | 25 en 03 a 07: 22 por tiempo, 2 por llamadas, 1 por contexto. «Esperando al modelo» es inferencia: la petición en vuelo no está en ningún archivo |
| El parche se conserva tras el tiempo y se pierde tras el contexto | Se sostiene (contexto: n = 1) | `agent_runner.py:758-776` y `:799` |
| Las resueltas con razonamiento caben en los topes viejos | Se sostiene en llamadas, **se cae en reloj** | 17 de 18 con 40 llamadas o menos; 12 de 18 con 240 s o menos |
| «13 de 14» parches fallan por una prueba que el agente no ve | **Se cae** la cifra | 69 parches que no pasan; archivo de prueba identificable en 55: nunca aparece en la traza en 41, aparece sin correrse en 12, el agente lo corrió en 2 |
| Siempre, nunca, a veces (03 a 06) | Se sostiene con otro alcance | 43 tareas: 5 siempre, 32 nunca, 6 a veces |
| Tanda de repuntuación el 10-08 | Se sostiene | 8 472, 8 660 y 8 703 envíos contados sin moverse el último puntuado. «Puntuación degradada» queda no medido |
| Precios de GPU y peso del checkpoint | No medido | No abrió ninguna URL; salen de la conclusión hasta que alguien las abra |

**Los dos desacuerdos del concilio, cerrados.**

- «25 cortes o 61»: son 25. La etiqueta `llamadas_agotadas` del notebook no es un corte: es una inferencia
  por conteo. De 39 sesiones así etiquetadas, 37 terminaron con un `submit_patch` del propio agente.
- «Cabe en el presupuesto viejo»: en llamadas sí; en reloj, 6 de 18 resueltas con razonamiento pasan de 240 s.
  La ganancia del razonamiento sí depende del tiempo extra, contra lo que afirmó QA.

**Puerta 2. ¿El log contiene la causa del corte?** Se trunca antes de la causa en **22 de 25** cortes, los 22
de tiempo: están el límite y la última acción terminada, y no está lo que el modelo generaba al corte. El
tramo sin registro es de 10 s o menos en 15, de 10 a 60 s en 5 y de más de 160 s en 2. En esos dos el agente
entregó un parche vacío hacia el segundo 70 y el arnés esperó hasta el tope sin dejar un solo evento. En 4
cortes (los de tareas que resolvieron) el motivo solo está en el log del notebook. Las 27 sesiones «sin
parche» entregaron un parche vacío por decisión del agente: no son cortes.

**Fallo del orquestador que esto destapa.** El «76 corridas y 47 fallos» con que abrí la vuelta venía de un
resumen por tarea de las 19 elegidas, presentado como la clasificación de las iteraciones. El universo real
es de 135 sesiones. Es el mismo fallo que la vuelta le corrigió a otros: no declarar el universo del conteo.

**Qué cambiar, en una frase del verificador.** Que el notebook escriba por tarea, al enviar cada petición y no
solo al terminarla, la petición en vuelo y el motivo de fin en un campo que no se borre cuando la tarea
resuelve, y que `scripts/kaggle_rescate.py` abra los zips «crudo» y mande a `faltantes.json`, con código 4,
todo log por tarea de 0 bytes en vez de salir con 0.

## Vuelta 40 — 2026-10-08, desde las 22:05 UTC

**Pregunta de la vuelta** (fijada por el dueño): ¿qué corrida debe ser la iteración 08 para que sea la primera
corrida válida, y qué puede decidir con una semana de cuota?

**Nada se subió, se envió ni se contrató.** Roles con definición escrita desde hoy (`.claude/agents/`, PR #155
fusionado a las 22:13 UTC). En esta sesión corrieron como agentes genéricos leyendo su definición: una sesión
no carga las definiciones creadas durante ella.

### Puerta 0

- **Recall** desde `main` al día: 5 lecciones; aplican «una subida a Kaggle por resultado», «no mover el tope
  de tiempo ni el presupuesto de razonamiento sin mirar los parches cortados» y «leer el zip que de verdad se
  envió antes de fijar el presupuesto».
- **Rescate:** valió el de las 21:41 UTC (código 0), hecho por el verificador y no por el orquestador.
- **Envíos, tres lecturas iguales** (21:37, 21:41 y 22:17 UTC): 0,06 y 0,05 sin razonamiento; 0,08 con
  razonamiento; el reenvío 56916129 sigue en `error`, 0 bytes, mensaje genérico: «sin lectura».

### Lo que el concilio midió

- **Por qué los logs por tarea pesan 0 bytes** (forense, reproducido en local): `event_display.py:281` del
  arnés no escribe cuando el proceso es un núcleo Jupyter. 0 bytes frente a 152 en proceso normal; con una
  línea en el notebook vuelven los 152.
- **El ensayo local no podía verlo:** corre como programa normal y deja logs de 715 bytes. Su «pasa» en las
  iteraciones 06 y 07 no validaba el registro. El modelo falso actual no fuerza ningún corte.
- **Dónde se va el tiempo** (arquitecto): 94 a 99 % del reloj del agente es espera al modelo, que genera a 37
  a 40 tokens por segundo con y sin razonamiento. El razonamiento cuadruplica los tokens de salida por turno
  (65 frente a 266) y lleva la tarea de unos 110 a unos 246 s.
- **`include_thoughts` enciende o apaga el razonamiento;** no lo «muestra». Los dos zips difieren en tres
  líneas.
- **El rechazo por contexto ocurrió en el subagente,** que no tiene compactación (851 a 23 527 tokens de
  entrada en 25 turnos); al fallar se pierde el parche del agente principal.
- **Las dos entregas vacías colgadas:** el arnés pide un turno más tras `submit_patch` y el servidor siguió
  generando. Unos 6 min en un envío de 120 tareas.
- **Potencia** (auditor, con la mezcla correcta): 60 tareas detectan +20 puntos 76 a 94 % de las veces y +10
  puntos solo 26 a 35 %. El efecto visto del razonamiento es de unos 8 puntos.
- **«6 pares a favor» solo no basta** (analista): con 103 tareas y sin efecto real sale por azar 13 de cada
  100 veces.
- **Solo 30 de las 43 tareas ya corridas son válidas** (auditor).

### Auditoría de la propuesta externa (otro asistente, traída por el dueño)

Los cuatro roles que entregaron coinciden: **acierta en la disciplina y su experimento no decide.**

- Acierta: parar las condiciones nuevas, un cambio por corrida, no repetir tareas ya resueltas, partir del zip
  barato y «sin registro no hay iteración», dicho con más filo que el concilio.
- Se cae: «el zip con razonamiento volvió con error y 0 bytes» (puntuó 0,08; lo que está en error es su
  reenvío); «el zip que sí puntuó» como si fuera solo el de sin razonamiento; «hasta que el mensaje esté
  copiado» (ya está en `envios.json`; es genérico); `completo: true` leído como «ninguna sesión cortada» (la
  07 tuvo 3 cortes).
- La regla «ejecutar las pruebas antes de `submit_patch`» ya está en el `system.md` del zip y el agente la
  cumple en 22 de 135 sesiones. Las pruebas con que se puntúa no existen para el agente.
- Correr solo sobre las «nunca resueltas» no tiene control: 0, 1 o 2 resueltas serían indistinguibles de «la
  regla no hace nada», y no mide lo que la regla rompe.
- Su puerta de registro (`log.txt` más el JSON de salida) es la de las iteraciones 01 y 02.
- Falta la medición de QA en Docker, que es el dato que decide la regla.

### Pareceres, copiados tal cual

**Auditor del método.**
1. Confirmo el universo del verificador: 135 sesiones, 43 tareas (5 siempre, 32 nunca, 6 a veces); solo 30 son
   válidas.
2. Retiro tres cifras mías: «15 de 145» (son 17), «3 con parche que no pasa» (son 9) y «43 parches que no
   pasan» (son 58). Mi recuento de pruebas copió la definición de Datito.
3. Afirmo que la potencia con la mezcla correcta no cambia la conclusión: 60 tareas detectan +20 puntos 76 a
   94 % de las veces y +10 puntos solo 26 a 35 %.
4. Entrego la derivación de las 60 tareas para versionar; el criterio se aprobó antes de tenerla, y esa falta
   es mía.
5. Propongo la 08: base, base repetida y base con solo el razonamiento encendido, sobre las 71 válidas sin
   elegir, McNemar exacto, unas 21 h de cuota (inferido).
6. Digo sin rodeos: es confirmatoria solo para efectos de 15 puntos o más; con los 8 vistos saldrá «no
   concluyente» 2 de cada 3 veces, y eso se escribe antes.
7. Sobre la propuesta externa: acierta en la disciplina; su experimento no tiene control, su regla ya está en
   el zip y su criterio de registro es el de 01 y 02.
8. No sé si el contrato de registro y el ensayo local ya están hechos, ni las horas reales de cuota con
   razonamiento.
9. Señalo que el criterio «vigente» vive en una rama sin fusionar y que siete afirmaciones de la vuelta 39
   siguen sin segundo recuento.
10. Como zorzALL propongo una sola hipótesis nueva, en archivo aparte: edición aceptada en archivo fuente
    antes de la mitad de las llamadas, leída por tarea.

**Analista de datos.**
1. Mis cifras de «presupuesto agotado» (57) y «6 resueltas cortadas» se caen; valen 25 cortes y 4. «31 nunca
   en 250 sesiones» era otro universo: son 32 nunca en 03 a 06, con 93 sesiones.
2. Reloj todo incluido: 109 s por tarea sin razonamiento y 246 s con él. En 30 h de cuota caben unas 470 a 490
   tareas-corrida, o unas 210 a 217.
3. Una decisión válida sobre el razonamiento no cabe con confianza en una semana: 12 % con 60 tareas y 24 %
   con 103, si el efecto es el medido.
4. «6 pares a favor» solo no basta: con 103 tareas sale por azar 13 de cada 100 veces.
5. La 08 que más informa: 60 tareas (30 corridas y 30 válidas nuevas, fastapi primero), dos brazos, más las 9
   propias. 14,5 h de cuota; 17,8 h con base repetida. Se anota exploratoria.
6. Las esperas finales cuestan 22 a 29 min en 120 tareas: no son la palanca, pero no dejan evento.
7. La propuesta externa acierta en parar y registrar. Su corrida no informa: las pruebas de la tarea no
   existen para el agente, la regla ya está en el zip y 0 de 34 no distinguiría nada.
8. Sigue sin medirse: Gemma sobre código no visto y el límite de sesión de Kaggle.

**Forense del arnés.**
1. Afirmo que los logs por tarea salen vacíos por `event_display.py:281`, que no escribe bajo Jupyter; lo
   reproduje: 0 bytes frente a 152.
2. Afirmo que el ensayo local de la 07 corre (código 0, 10 tareas) y deja logs de 715 bytes: no reproduce el
   fallo de Kaggle porque no es un notebook.
3. Afirmo que `completo: true` y `cortado_por: null` hablan del notebook, no de las sesiones: la 07 tuvo 3
   cortes por tiempo.
4. Afirmo que el modelo falso actual no fuerza ningún corte; llamadas, tope del notebook y servidor caído
   existen solo para la 03.
5. Propongo seis enganches en el notebook: inicio y fin de petición, motivo de fin, latido con GPU, log entero
   del servidor, diff al cierre y parche de rich.
6. Propongo que el rescate abra los zips y mande a faltantes, con código 4, todo log exigido de 0 bytes.
7. No sé si los enganches de litellm se disparan en la ruta del arnés ni ante una cancelación; lo decide el
   ensayo.
8. No sé la causa del 56916129, y un estado de envío no es un desenlace.
9. Sobre la propuesta externa: acierta en parar y exigir registro; su regla ya está en el zip y su criterio de
   registro no explica un corte.
10. Mejor que otra condición: ensayo con cuatro cortes forzados bajo un núcleo real, y no subir la 08 hasta
    que cada uno deje su causa en disco.

**Arquitecto de IA.**
1. `include_thoughts` enciende o apaga el razonamiento; el zip A lleva un `thinking_budget` muerto. Los zips
   difieren en tres líneas.
2. El modelo decodifica a 37–40 tokens por segundo en 4 × L4; del 94 al 99 % del reloj del agente es espera al
   modelo. El razonamiento cuadruplica la salida (65 → 266 tokens por turno) y lleva la tarea de 110 a 246 s.
3. El rechazo por contexto ocurrió en el subagente, que no tiene compactación (851 → 23 527 tokens en 25
   turnos). «24 577» es un piso, no una medida.
4. Las dos entregas vacías colgadas: el arnés pide un turno más tras `submit_patch` y el servidor generó sin
   terminar. Costo: unos 6 min en 120 tareas.
5. Registro: envolver `LiteLLMClient.acompletion` (`lite_llm.py:497`) y `_run_agent_sandbox`
   (`evaluate.py:194`), copiar el log del servidor y sondear `/metrics`. El texto parcial no se obtiene sin
   streaming.
6. Concurrencia: el arnés la soporta y el notebook no; cambia una condición atada al reloj. No va en la 08.
7. Iteración 08: A y A′, 60 tareas sorteadas de 129, en serie, 3,9 h, tope de sesión 5 h.
8. Después, en la misma semana: B (solo razonamiento), T (+30 s) e I (+20 llamadas); 17 a 19 h en total.
9. Propuesta externa: no adoptarla tal cual. La regla ya está en `system.md`, las pruebas de la tarea no
   existen para el agente y el conjunto «nunca resueltas» no puede medir daño.
10. Sin medir: cuota por sesión, compactación del evaluador (5 o 15) y la fecha `lastRunTime` de la 07.

### Desacuerdos abiertos, con el dato que los cierra

1. **Cómo se descuenta la cuota.** Una lectura dice al doble del reloj de sesión; el arquitecto supuso que al
   reloj. Lo cierra leer la cuota antes y después de la próxima sesión.
2. **Qué tareas.** Las 71 válidas (auditor); 30 corridas, 30 válidas nuevas y las 9 propias (analista); 60
   sorteadas de las 129 (arquitecto, aunque 58 de las 129 no discriminan en el sandbox).
3. **Qué brazos.** Base y repetición primero (arquitecto); base, repetición y solo razonamiento (auditor); el
   zip con los tres cambios (analista).
4. **Enganche del registro.** Callbacks (forense) o envoltorio de la llamada (arquitecto, porque los callbacks
   no ven una cancelación). Lo cierra el ensayo local con un corte forzado.
5. **Criterio «60 tareas o 6 pares».** Los 6 pares solos no bastan. Decisión del dueño.

### Fallos del orquestador en esta vuelta

- La convocatoria dio a los roles una cifra equivocada: «10 a 24 mil tokens por turno». Medido: 8,7 a 17,7 mil.
- Llamó «razonamiento visible» a un cambio que enciende o apaga el razonamiento.
- Dio por vigente un criterio que aún no estaba en `main`.
- Puso a diseñar la 08 sobre un plan cuyos pasos de registro y ensayo no estaban hechos.
- La convocatoria llevó cifras del verificador, no «solo archivos».

*Pendiente al escribir esto: la medición de QA en Docker y el verificador limpio del concilio 40. La decisión
va en la parte siguiente.*

### Cierre del concilio 40 (QA y verificador limpio)

**El dueño detuvo la medición de QA en Docker** («ha demorado mucho»): iba en la tarea 19 de 29 de su segunda
pasada. QA entregó con lo que había en disco; la pasada del parche de referencia no corrió.

**QA de trayectorias, medido en local** (parches contra las pruebas visibles, comparando con la base):

| Universo | Parches malos en rojo | Parches buenos en rojo (falsa alarma) |
|---|---|---|
| Las 19 tareas elegidas (14 malos, 38 buenos) | 5 de 14 | 3 de 38 (2 sin medir por tope de tiempo) |
| Resto, parcial (fastapi) | 6 de 20 | — |
| Suma fiable | 11 de 34 | — |

- Quedan sin medir 35 de los 69 parches que no pasan: 21 por la detención y 14 de un repositorio cuyo control
  no es fiable (falla en 5 de 15).
- El control local coincide con Kaggle en 72 de 72 sesiones de los otros dos repositorios.
- La señal sale casi solo de la **suite completa comparada con la base**, que la instrucción del zip prohíbe.
  El archivo de prueba «de la tarea» no existe para el agente en 24 de 48 parches malos medidos.
- La suite ya viene roja en la base en 33 de 33 tareas: sin comparar, alarma siempre.
- Punto ciego: 9 a 18 % de las pruebas visibles dan error de entorno en la base; causa no medida.

**Parecer de QA, copiado tal cual.**
1. Medí en Docker 52 sesiones de las 19 tareas elegidas y 35 más del resto; el control coincide con Kaggle en
   72 de 72 de rich y fastapi, y falla en 5 de 15 de requests, que dejo fuera.
2. Retiro mi frase de la vuelta 39: las pruebas visibles sí delatan parches malos, 5 de 14 en las 19 tareas y
   11 de 34 en lo medido.
3. Falsa alarma sobre parches buenos: 3 de 38; sin razonamiento, 1 de 20.
4. La señal sale casi solo de la suite completa comparada contra la base; el archivo «de la tarea» no existe
   para el agente en 24 de 48 parches malos.
5. La suite ya viene roja en la base en 33 de 33 tareas: la regla externa, leída literal, alarma siempre o no
   ve nada.
6. Punto ciego: 9 a 18 % de las pruebas dan error de entorno en la base (0 % rich, 13 % fastapi, 32 %
   requests); causa no medida.
7. Quedan sin medir 35 de los 69 parches malos y la pasada del parche de referencia.
8. Una señal roja no es un arreglo: no sé si Gemma corrige al verla.
9. Mi veredicto: no decide; no probar la regla como está escrita.
10. Propongo terminar en local las 21 sesiones pendientes y la pasada de referencia antes de gastar cuota, y
    solo entonces ensayar «suite antes y después» como exploratoria.

**Verificador limpio** (rescate propio `2026-10-08T2231Z`, código 0; 16 afirmaciones sin cifras; informe en
`concilio_40\verificador-limpio\informe_verificador.md`). Donde difiere, vale su recuento.

| Afirmación | Marca | Su medida |
|---|---|---|
| La cuota se descuenta al doble del reloj | Se sostiene el factor | 2,00 con el par de lecturas alrededor de una sesión; 1,73 a 1,79 con otra lectura. Ninguna lectura cubre una sesión con razonamiento. El «al reloj» del arquitecto se cae |
| Segundos por tarea-corrida | Se sostiene | 109,4 sin razonamiento (99,8 en tareas válidas) y 246,0 con él. Antes de la primera tarea: 479 a 1 337 s |
| Velocidad del modelo | Se sostiene | 36,6 a 39,8 tokens por segundo; 64 y 256 tokens de salida por turno |
| «94 a 99 % del reloj es espera al modelo» | Se cae la cifra | 90 a 92 % sin razonamiento y 98 % con él, sobre el bucle del agente |
| El rechazo por contexto ocurrió en el subagente | Se sostiene | 851 a 23 527 tokens en 25 turnos. No es el único: hay otro en la iteración 02 |
| El arnés pide otro turno tras `submit_patch` | Se sostiene | 121 de 123 entregas tienen un turno posterior. «El servidor siguió generando» queda no medido |
| Causa de los logs por tarea de 0 bytes | Se sostiene, reproducida | 145 de 145; 169 bytes en proceso normal y 0 bajo la detección de Jupyter. Ya son dos mediciones |
| El ensayo local no corre como notebook | Se sostiene | Ejecuta las celdas con `exec` en un proceso normal |
| El zip ya ordena verificar con una prueba | Se sostiene | `prompts/system.md`, líneas 4 y 26 |
| Las pruebas que puntúan no existen para el agente | Se sostiene con matiz | Faltan los casos con que se puntúa; en 85 de las 129 tareas el archivo de prueba sí está, sin esos casos |
| «41 de 55» | Se sostiene con su definición | Con el archivo del parche de pruebas: 69 parches, aparece en 18 y el agente lo ejecutó en 7 |
| Tareas válidas | Se sostiene | 129 públicas; válidas 103 según un archivo de validez y 71 según el otro; corridas 43, de ellas 30 válidas |
| Un registro por callbacks no ve una cancelación | Se cae como frase general | El callback de antes de la llamada sí se dispara; los de éxito y de fallo, no |
| Los dos zips difieren en tres líneas | Se sostiene | — |

**Su cuenta.** En 30 h de cuota caben 465 a 535 tareas-corrida sin razonamiento y 213 a 215 con él (factor 2).
Una corrida de 60 tareas en dos brazos sin razonamiento cuesta **6,9 a 9,0 h de cuota**, caso central 7,5 h, y
necesita dos sesiones: 120 tareas no caben en el tope de 9 000 s que usan los notebooks.

### Desacuerdos, cerrados o no

1. **Cuota:** cerrado a favor del doble (o 1,76). Las 3,9 h del arquitecto eran reloj, no cuota.
2. **Enganche del registro:** cerrado a medias. El diseño del forense (emparejar inicio y fin; un inicio sin
   fin es la petición cortada) funciona con el callback de antes de la llamada. El texto parcial sigue sin
   poder guardarse.
3. **Qué tareas:** abierto en un punto nuevo: hay dos archivos de validez (103 y 71 tareas). Se sortea dentro
   del más estricto, las 71, con semilla fechada.
4. **Qué brazos:** se adopta el orden del arquitecto con el brazo del auditor: primero base y repetición;
   después solo el razonamiento.
5. **«60 tareas o 6 pares»:** sigue abierto; es del dueño.

### Decisión (aprobada por el dueño: «De acuerdo, empieza por el cambio al rescate»)

**Iteración 08: la base y su repetición, sin ningún cambio en el agente, con el registro nuevo.**

| Campo | Valor |
|---|---|
| Condición | Zip sin razonamiento (`d8a3e1d3…`), dos pasadas sobre las mismas tareas |
| Tareas | 60, sorteadas con semilla fechada dentro de las 71 válidas |
| Qué es | Exploratoria en resueltas; válida en su registro. Mide el ruido entre dos pasadas idénticas |
| Costo | 6,9 a 9,0 h de cuota (central 7,5 h), en dos sesiones. Se lee la cuota antes y después de cada una |
| A fechar antes de subir | Resueltas por brazo, discordantes entre pasadas, cortes por tiempo, y que todo corte deje su petición en vuelo |
| La refuta | 6 o más discordantes entre las dos pasadas, o un corte sin causa en disco |
| Brazo siguiente, misma semana | Solo el razonamiento encendido, con 4 minutos y 40 llamadas |

**Antes de subir nada:** (1) el rescate abre los zips y un log exigido de 0 bytes es un faltante con código 4
(issue #156, en curso); (2) el notebook con los seis enganches de registro y la línea que devuelve los logs
por tarea; (3) el ensayo local bajo un núcleo Jupyter real con cuatro cortes forzados.

**No se hace:** la propuesta externa tal cual; contratar GPU; concurrencia; reenviar o enviar.

**Queda para después, en local y gratis:** las 21 sesiones que QA no midió y la pasada del parche de
referencia. Con eso se sabrá si «suite antes y después» merece un brazo exploratorio.

### Fallos del orquestador, añadidos

- Dejé correr casi una hora una medición que no bloqueaba la decisión, y avisé al dueño una y otra vez que
  «todavía no llega» en vez de entregar la recomendación con lo que había.
- Repetí el costo del arquitecto (3,9 h) sin decir que era reloj y no cuota.

### Estado al cierre y cómo retomar (2026-10-08, hacia las 22:50 UTC)

El dueño cerró la sesión: «Cierra por ahora, documenta todo. Próxima sesión sigo».

**Hecho y verificado.**
- PR #153 (episodio 065, vuelta 39) fusionado a las 22:01 UTC; PR #155 (staff de experimento) fusionado a las
  22:13 UTC. En `main`: siete definiciones nuevas en `.claude/agents/`, el procedimiento de una vuelta y el
  criterio de corrida válida y decisión válida en `CONTRIBUTING.md`, y las skills `corrida-valida` y
  `concilio-de-experimento`.
- Decisión sobre la iteración 08 tomada y registrada arriba.

**A medias.**
- **Issue #156** (el rescate abre los zips; un log exigido de 0 bytes es un faltante con código 4): lo
  implementaba un agente con Sonnet en `F:\Code\ALL-wt-rescate-bytes`, rama `issue-156-rescate-bytes`. Al
  cerrar tenía cambios sin commit en el guion, su prueba, el documento del rescate y el registro de cambios.
  Comprobar si llegó a abrir PR; si no, retomar en ese árbol. Episodio reservado: 067.
  *Actualización, misma noche:* terminó y abrió el **PR #158** (sin fusionar). Las pruebas nuevas fallan sin el
  cambio; sobre el rescate `2026-10-08T2217Z` el guion sale ahora con 4 y lista 145 miembros exigidos de 0
  bytes. Pasó a revisión de código independiente; falta su dictamen, la CI y la palabra del dueño para fusionar.
- **PR #157** (episodio 068, esta vuelta): abierto, sin revisión independiente y sin fusionar.
- **Issue #154:** cerrado por la fusión pero sin confirmar. Falta ver las siete definiciones cargadas en una
  sesión nueva.
- **Medición de QA en Docker:** detenida. Faltan 21 sesiones y la pasada del parche de referencia. Datos en
  `instrumentos\concilio_39\qa\`.

**Sin empezar.**
- Los seis enganches de registro del notebook y la línea que devuelve los logs por tarea.
- El ensayo local bajo un núcleo Jupyter real con cuatro cortes forzados (a la imagen le faltan dos paquetes).
- El sorteo fechado de las 60 tareas y las predicciones de la iteración 08.

**Pendiente del dueño.** Si el criterio exige siempre la prueba exacta además de los «6 pares».

**Para retomar.** Sesión nueva en el repositorio; `devlog recall`; leer esta vuelta; mirar el estado de #156
y #157; seguir con el registro del notebook. La instrucción para orquestar una vuelta está en
`prompt-concilio-de-experimento.md`, en la raíz del repositorio y sin versionar.

Nada se subió, se envió ni se contrató en las vueltas 39 y 40. No quedó ningún contenedor corriendo.

### Sesiones de continuación (2026-10-08, 23:43 UTC, y 2026-10-09, desde las 00:05 UTC)

**Sesión de las 23:43 UTC: se cortó a las 23:49 UTC sin registrar nada.** Reconstruida desde su transcripción
y desde GitHub:

- Pasó el PR #157 por `revisor-docs`: aprobado con ocho observaciones de redacción, ninguna cifra retirada.
  Siete se aplicaron en el commit `b354488`; la octava (la regla de leer la cuota «sin otra sesión entre
  medias») el revisor la dio por aceptable como práctica.
- Abrió el issue #160 (notebook de la iteración 08 con registro y ensayo bajo núcleo real), talla L, con su
  tarjeta, y fijó en un comentario la semilla del sorteo: `ALL-kaggle-iteracion-08-2026-10-08`. El comentario
  dice «23:55 UTC» pero GitHub lo fecha a las 23:48:54 UTC: vale la hora de GitHub.
- El #159 es el mismo issue creado por error con la cuenta `vinculaterritorio`; quedó cerrado como «no
  planeado» y sin tarjeta.
- Lanzó el revisor de código del PR #158 y el implementador del #160. Los dos murieron con la sesión: el
  revisor sin dictamen, el implementador a los 20 segundos, sin rama ni archivos.

**Sesión de las 00:05 UTC.**

- PR #157 fusionado: `mergedAt` 2026-10-09T00:10:57Z, commit `49294a5`, 12 de 12 comprobaciones en verde. El
  episodio 068 está en `main`.
- Issue #154 confirmado: las siete definiciones del staff de experimento aparecen en la lista de agentes de
  una sesión nueva; comentario de evidencia en el issue y tarjeta en *Verificada*. Ninguno de los siete roles
  se convocó aún con la definición cargada.
- Relanzados, con el mismo encargo: `revisor-codigo` sobre el PR #158 e `implementador-opus` sobre el #160
  (árbol `F:\Code\ALL-wt-registro-08`, rama `issue-160-registro-notebook-08`, instrumentos en
  `instrumentos\iteracion_08\`).

**PR #158 (rescate que mira bytes): tres revisiones y dos recuentos antes de fusionar.**

- Primera revisión (`d0f5051`): aprobado con observaciones. Los ocho criterios cumplen; 7 de 26 defectos
  inyectados no los detectaba ninguna prueba.
- **Fallo del orquestador.** Al corregir añadí pruebas y, sin que nadie lo pidiera, cambié la regla (decidía
  la carpeta conocida más externa). Lo subí (`578de13`) y avisé al dueño de que «ese trozo no pasó por el
  revisor» mientras esperaba la CI para fusionar. El dueño: «si no pasó por el revisor debes pasarlo siempre
  por ese ciclo, claude y datito, esto no es un juego».
- Segunda revisión (`578de13`) y primer recuento de Datito. El revisor midió que el cambio aflojaba la
  detección: un log vacío bajo `test_outputs/<tarea>/logs/` dejaba de dar código 4. Datito, contando desde los
  zips crudos con código propio: 93 zips de salida en 11 rescates, 5 043 miembros, 1 574 de 0 bytes (1 191 en
  `logs/`, 311 en `patches/`, 72 en `test_outputs/`); 0 cambian de clasificación entre versiones; ninguna ruta
  real trae dos carpetas conocidas; el tamaño declarado coincide con el real en todos.
- Retiré el cambio (`bde8104`): la revisión de zips vuelve a ser la de `d0f5051`. Única línea de código
  distinta: `--sin-red` busca los zips sin distinguir mayúsculas en la extensión, como la bajada (hallazgo de
  la segunda revisión).
- Tercera revisión (`bde8104`): apto para fusionar, observaciones menores. 38 defectos inyectados, 32
  detectados; de los 6 que sobreviven, dos solo sobreviven en Windows y ninguno cambia el código de salida
  hacia el silencio. Segundo recuento de Datito: salida idéntica byte a byte entre `d0f5051` y `bde8104` en
  las 14 carpetas con fecha; su cuenta coincide con el guion (43, 43, 86, 116, 135 y 145 cinco veces).
- Fusionado: `mergedAt` 2026-10-09T01:10:20Z, commit `d8b95f7`. Desde `main`, `--sin-red` sobre una copia de
  `2026-10-08T2217Z` sale con 4 y lista 145 (43, 43, 30, 19, 10).
- Lo que Datito encontró y nadie había mirado: el rescate `2026-10-06T185453Z` está anidado un nivel de más;
  apuntando a la carpeta externa el guion sale con 2 (entrada inválida) sin mirar sus zips, y apuntando a la
  subcarpeta da 4 y 43. Ni el arreglo de las mayúsculas ni el filtro de carpetas los ejerce ningún dato real.
- Observaciones que quedan sin atender (no bloquean): faltan casos negativos para `x_task_results.jsonl` y
  `mypatches/`; ni el prefijo `salida__` ni el orden de revisión están fijados por una prueba; un zip sin
  ningún log sale con 0 (fuera del alcance del #156); el episodio 067 narra la segunda revisión dentro de un
  `error` y no como paso propio.

**PR #161 (issue #160: notebook de la iteración 08 con registro, y ensayo bajo núcleo real).** Abierto por el
implementador hacia las 01:45 UTC, CI en verde. Declara 8 de 10 criterios cumplidos; el 3 en parte (el tope
de llamadas y el tope de sesión del notebook cortan sin petición en vuelo; una sesión muerta desde fuera no
deja diff al cierre, solo el del último latido). Tres decisiones suyas fuera del issue: parche de `rich`
estrecho en vez de la línea global (que multiplicaba por 96 la salida de la celda), un séptimo enganche
`agente_fin`, y tope de sesión a 150 min sin medir si caben 60 tareas. En revisión de código.

**Recuento de Datito sobre el ensayo (parecer, resumido; su informe completo está en la sesión).**
- Reproduce todas las cifras del implementador: 6 de 6 logs en 0 bytes sin parche y 26 de 26 con 721 a 722
  bytes con él; 78 inicios y 78 fines sin huérfanos; `registro/` de 273 337 bytes; 246 latidos sin huecos; los
  cinco cortes; el sorteo exacto (71 con `clase == "discrimina"`, 60 sorteadas: 33 de rich y 27 de fastapi);
  las 194 huellas.
- Matiz: en la sesión muerta desde fuera, el zip se empaqueta antes de la muerte y no muestra el corte; la
  evidencia está en los archivos sueltos de `working/`.
- **Hallazgo nuevo, medido en las corridas reales** (12 zips distintos, iteraciones 03 a 07, 145 sesiones): 4
  sesiones figuran como resueltas y fueron cortadas por tiempo en mitad de una acción, sin `error_message`
  (2 en la 06 y 2 en la 07): 4 de 39 resueltas; en 06 y 07, 4 de 18. Otras 4 pasaron el tope y sí cerraron la
  traza (2 resueltas). Ninguna cortada por llamadas figura como resuelta. Las 145 filas dicen `SUCCESS`; solo
  21 llevan `error_message`. Señal usada: duración mayor o igual al tope y traza sin mensaje final.
- Lo que el ensayo no cubre: usa las 26 tareas ya corridas (las únicas con snapshot local); las 34 nuevas del
  sorteo no las ha visto. El modelo falso repite una forma de 3 peticiones, sin peticiones de resumen.
- Costo del registro: unos 38 ms por petición; 0,7 % del tope de 4 min en una tarea de 40 llamadas
  (extrapolado). La comparación con y sin enganches es de 3 corridas contra 3: p mínimo posible 0,10.
- Inferido, sin medir: a ~245 s por tarea (iteraciones 06 y 07), dos pasadas de 7 200 s dan unas 58 tareas,
  menos que 60.
- Otra lectura del universo: «el dorado resuelve» da 74 y no 71; el sorteo usa 71.

**Preguntas que esto abre para el concilio y el dueño, antes de leer la iteración 08:** si una sesión cortada
cuyo parche pasa cuenta como resuelta; y si los topes dejan caber 30 tareas por pasada.

**Dictamen del revisor de código sobre el PR #161 (`1c0b7dc`): aprobado con observaciones.** Ningún enganche
cambia lo que el arnés devuelve; el notebook difiere del de la 07 solo en lo declarado (comparado celda a
celda sin `armar.py`); el sorteo se reproduce. Defectos devueltos al implementador antes de fusionar:
`diagnosticar` da por «completa» una sesión con los enganches fallados y 0 peticiones; marca como «en vuelo»
una petición que falló y se recuperó; pisa los datos de una tarea repetida; confunde un archivo ilegible con
«difiere»; el notebook no se detiene si un enganche falla; 13 de 56 defectos inyectados sobreviven; el
episodio dice 2381 pruebas y son 2409. Sin verificar para subir: que el arnés de las ruedas de Kaggle tenga
`agent_runner.Console` como el de la imagen local, de lo que depende el parche de `rich`.

**Decisiones del dueño (2026-10-09, hacia las 02:20 UTC):** «Acepto tu recomendación, y en la 2 fijarlos».
1. El criterio 3 del #160 se acepta como cumplido con su límite: el tope de llamadas y el tope de sesión del
   notebook cortan entre peticiones y no tienen petición en vuelo; la sesión muerta desde fuera no deja diff
   al cierre. Comentario en el issue #160.
2. Se fija antes de leer la iteración 08 cómo cuenta una sesión cortada cuyo parche pasa. La redacción es del
   orquestador (comentario en el issue #103): la cifra principal es `resolved` del arnés, como en 03 a 07;
   cada sesión lleva su marca de corte; todo informe da las dos cifras juntas; los criterios fechados se leen
   con la principal y se dice cuántas discordancias tienen una sesión cortada; hacia atrás no se reescribe.
   El dueño puede corregir la redacción antes de subir.

**PR #161, segunda ronda (commits `41ec1c5` y `34a0b7c`; hacia las 03:40 UTC).** El implementador corrigió el
diagnóstico (códigos 0 completa, 2 ilegible, 3 cortada por el notebook, 4 registro no fiable, 5 muerta desde
fuera), añadió dos guardias al notebook y la orden `comprobar` (rescate más diagnóstico), y repitió la batería
entera (16 escenarios; la anterior se sobrescribió).

- Segundo recuento de Datito: el notebook en disco lleva el código de enganches de `34a0b7c` byte a byte; los
  16 escenarios dan el código que predijo antes de ejecutar; cortes, logs, latidos, sorteo y 236 huellas se
  reproducen. Hallazgos: `diagnosticar` solo da 0 sobre una corrida con los 6 logs vacíos (solo `comprobar` la
  ve); en la guardia del log el zip se empaqueta antes de la guardia y, leído solo, da 5 en vez de 4; un
  veredicto dice «registro no fiable» y «sesión completa» a la vez; el ensayo late cada 2 s y el notebook real
  cada 30 s; el notebook de la segunda pasada nunca se ejecutó; `armar.py` y los notebooks no están
  versionados; nueve escenarios corrieron en paralelo; el «1,35 veces» del parche de `rich` solo sale con una
  medida no declarada; la sincronización a disco subió de 16–36 a 47–86 ms entre baterías, sin causa medida.
- Segunda revisión de código: **cambios requeridos antes de fusionar**, uno: `comprobar` salta en silencio un
  notebook sin registro y sale con 0. No bloquean: la guardia tras la primera tarea no mira `diff_cierre` ni
  `agente_fin`; `comprobar` pierde el resultado del rescate si ningún notebook trae registro; tipos
  equivocados dan código 1; textos inexactos. De 78 defectos inyectados sobreviven 5; uno toca el arnés (la
  parada del sandbox fuera del `finally`, sin prueba con cancelación).
- Devuelto al implementador con una lista de diez puntos; después, tercera revisión y tercer recuento.

**PR #161, tercera ronda (commits `20b6136` y `f89a375`; hacia las 04:10 UTC).** El implementador arregló
`comprobar` (lista los notebooks omitidos), añadió a la guardia la exigencia de `agente_fin` y `diff_cierre`,
ejecutó la pasada 2, reempaquetó el zip tras la guardia y repitió la batería (18 corridas válidas).

- Tercer recuento de Datito: todas las cifras se reproducen; los 19 escenarios dan el código predicho; el
  registro del zip y el suelto son idénticos en las guardias; 49 de 49 defectos detectados, repetido por él.
  Señala: una sesión colgada sale con 5 («muerta desde fuera») aunque su latido siga; un tope de tarea no
  cambia el código de salida; los instrumentos no están versionados; no se ensayó la cadencia real (latido de
  2 s y tope de 45 s contra 30 s y 150 min). Cero cuelgues en 60 tareas en modo `archivo`: acota la tasa por
  debajo del 5 % por tarea, nada más.
- Tercera revisión de código: **cambios requeridos, uno**: `comprobar` sale con 0 si una pasada muere antes de
  instalar el registro (el servidor no arranca en la celda 7 y el registro nace en la 8) y la otra sale bien.
  Los otros nueve puntos, resueltos. De 50 defectos inyectados sobreviven 6. Sin interbloqueo visible en los
  enganches.
- Devuelta una cuarta ronda mínima (05:00 UTC): la orden recibe la lista de pasadas esperadas y exige registro
  en cada una. Sin tocar el notebook ni los enganches.

**Una corrida del ensayo se colgó: parecer del forense del arnés (05:10 UTC), resumido.**
- Hecho medido: el escenario `parche_global` se paró a las 03:41:16 UTC entre `tarea_inicio` de su tercera
  tarea y la primera petición. Arranque del sandbox terminado, log por tarea en 0 bytes, ninguna petición al
  servidor, latido vivo 16 minutos. Lo mató el implementador.
- Causa más probable (cerca del 75 %, inferida; el cuelgue no se reprodujo en 9 corridas): bucle infinito en
  `ipykernel 6.29.5`, `iostream.py:516`. El núcleo guarda un mapa de hilo a padre por identificador de hilo,
  los identificadores se reutilizan, y `run_sync` crea un hilo nuevo por tarea: bajo carga el mapa puede
  cerrar un ciclo y la primera escritura a stdout desde ese hilo no vuelve.
- Medido en la imagen: el ciclo construido a mano bloquea la escritura con la CPU girando; la carrera natural
  da 4 a 7 ciclos en 1 000 a 1 500 fronteras con la máquina cargada y 0 de 3 000 sin carga.
- Descartado: interbloqueo en el registro (el latido tomó el candado unas 450 veces tras el paro) y el
  servidor falso.
- **Puede ocurrir en el modo `archivo`, el que iría a Kaggle** (certeza del forense, cerca del 90 % en esta
  imagen): el arnés escribe a stdout desde el hilo de la tarea cuando salta un tope, y los logs reales traen
  cientos de avisos. En contra de una tasa alta: 310 tareas en 8 sesiones reales sin un cuelgue así.
- **Ningún tope lo corta:** el tope de 4 min no interrumpe un bucle síncrono, el de sesión solo se mira entre
  tareas y `run_sync` espera sin tope. Giraría hasta que Kaggle mate la sesión.
- Arreglo que propone, sin aplicar: vaciar ese mapa antes de cada tarea o usar un único grupo de hilos para
  toda la sesión; y esperar cada tarea con tope, volcando la pila y cerrando el registro si vence.
- Sin medir: la versión de ipykernel de Kaggle y la pila del proceso colgado.

**Condición nueva antes de subir** (no bloquea fusionar el #161, porque el arreglo es del notebook): tope por
tarea y vaciado del mapa de hilos en la celda 10, ensayados bajo el núcleo. Es un issue aparte.

**Experimento nuevo, pedido por el dueño (04:50 a 05:10 UTC): caja `experiments/azar/`.** Issue #162, PR #163.
Pregunta general: si un sistema físico hecho para dar azar tiene estructura predecible. Pregunta con que
arranca, fijada por el dueño: «¿podemos predecir el error antes que ocurra?», aplicada al propio proceso.
Contiene el documento de entrada, un estado del arte verificado por `investigador-papers` (corrigió cinco
datos que el orquestador había dicho de memoria) y un pre-registro con seis predicciones fechadas, cuatro de
ellas sobre los PR #161 y #163. Al añadir su episodio falló una prueba de la bitácora que en `main` pasaba
con un margen de 0,01; se arregló en el mismo PR. En revisión: `revisor-docs`, `revisor-codigo` y Datito.

**PR #161 fusionado (05:27 UTC), tras cuatro revisiones de código y cuatro recuentos.**
- Cuarta ronda (`f5c1e62`, cabeza `90e6b31`): `comprobar` recibe las pasadas esperadas con `--notebook`
  repetible y exige registro en cada una; sin pasadas nombradas nunca sale con 0. Sin tocar el notebook ni
  los enganches.
- Cuarto recuento de Datito: todas las cifras se reproducen; los 8 casos nuevos y los 18 escenarios dan el
  código que predijo. Encontró que `comprobar` da 0 sobre corridas incompletas fabricadas a mano (un registro
  con 1 de 3 tareas o con ninguna, la pasada 2 copiada de la 1, tareas fuera del sorteo): la orden no lee el
  sorteo ni cuenta tareas.
- Cuarta revisión: **apto con observaciones no bloqueantes**. Ocho entradas sintéticas salen con 0 sin
  merecerlo y ninguna la produce el notebook armado (inferido leyendo las celdas 8, 10 y 11, no ejecutado):
  todo corte del notebook deja un evento `corte`. De 48 defectos inyectados sobreviven 9, dos equivalentes.
- Observaciones que quedan sin atender (no se editó nada entre el dictamen y la fusión): el nombre de una
  pasada lo decide el sistema de archivos y dos alias de la misma carpeta dan 0 con dos pasadas en el JSON;
  con dos registros en una carpeta se lee el primero en silencio; no se comprueba que el registro sea de la
  pasada nombrada, cuántas tareas corrió ni que exista su zip; la salida redirigida en Windows no es UTF-8.
  Conviene cerrarlas antes de dar por bueno el 0 de una corrida real.
- Sin verificar: qué devuelve Kaggle como salida de un notebook con una versión anterior completa y la última
  fallida; `comprobar` no ata el registro a una versión ni a una fecha.
- `mergedAt` 2026-10-09T05:27:08Z, commit `e6b8f66`. Con esto, dos de las tres condiciones para subir están
  en `main` (rescate que mira bytes; notebook con registro y ensayo bajo núcleo real). Se suma una cuarta
  condición, la del forense: issue #164.

**Predicciones del experimento azar con desenlace** (pre-registro en el PR #163): la 1 (la cuarta revisión
exige un cambio, 0,45) no ocurrió; la 2 (encuentra otro «da por bueno» alcanzable, 0,35; la historia decía 3
de 3) no ocurrió; la 3 (el recuento contradice una cifra, 0,10) no ocurrió, marcada por Datito; la 4 (la
revisión de documentos halla una frase que dice más que la fuente, 0,65) ocurrió; la 5 (CI del primer commit
en verde, 0,80) ocurrió. Cinco casos: no se lee nada con menos de 100.

**PR #163 (caja azar), revisiones.** Documentos: aprobado con observaciones (hora del pre-registro
equivocada, predicciones no comprobables por un tercero). Datito: tres de seis líneas base mal o sin contar;
con 30 predicciones el diseño no decide; faltaba una clase de fallo. Código: apto con observaciones, y dos
afirmaciones del orquestador eran falsas (la causa del fallo de la prueba era el decaimiento de las aristas,
no `update_docs`; `main` no habría fallado al fusionar los dos PR). Corregido en `f7af948` y `d929b25`; en
segunda revisión.

**Issues abiertos con estimación:** #164 (tope por tarea y mapa de hilos), #165 (roles del lazo de
predicción), #166 (skill «predecir-e-investigar»), #167 (`devlog base-rates`).

**Cierre del avance (06:05 UTC).**
- Issue #160 confirmado: CI de `main` en `e6b8f66` con 12 de 12 en verde, sorteo reproducido desde `main`,
  comentario de evidencia con lo que el cierre no cubre, tarjeta en *Verificada*.
- PR #163 fusionado tras cuatro revisiones de documentos, una de código y un recuento (`mergedAt`
  2026-10-09T05:48:58Z, commit `3a55b08`). Issue #162 confirmado: CI de `main` con 12 de 12 en verde.
- Predicción 6 del experimento azar (que `main` quede en verde tras fusionar los dos PR sin commit de arreglo,
  0,75; la historia da 0,97): ocurrió. Seis predicciones cerradas: tres «no ocurrió» con probabilidades de
  0,45, 0,35 y 0,10, y tres «ocurrió» con 0,65, 0,80 y 0,75. No se calcula nada con seis.
- Lo que las revisiones corrigieron al orquestador en el PR #163: cinco de unas veinte obras citadas de
  memoria, tres de seis líneas base, la causa de un fallo de prueba, una CI dada por «en curso» que ya había
  terminado y una regla de lectura que afirmaba y refutaba a la vez.

### Estado al cierre y cómo retomar (2026-10-09, 06:10 UTC, sin agentes en curso)

**Hecho y verificado.** PR #153, #155, #157, #158, #161 y #163 fusionados. Issues #154, #156, #160 y #162
confirmados, con evidencia y tarjeta en *Verificada*. `experiments/azar/` está en `main`.

**Condiciones para subir la iteración 08.** En `main`: rescate que mira bytes; notebook con registro y ensayo
bajo núcleo real. Faltan: el tope por tarea y el arreglo del cuelgue (#164); las predicciones fechadas de la
corrida, que escribe el concilio; medir si caben 60 tareas en 7 200 s por pasada. Subir necesita la orden del
dueño.

**Abierto, con estimación, sin empezar** (cada uno lleva predicción previa en el pre-registro del
experimento azar):
- #164 (M, Opus): tope por tarea y vaciado del mapa de hilos en el notebook de la 08.
- #165 (M, Opus): roles del lazo de predicción (pronosticador, marcador de desenlaces, probador adversarial,
  custodio del pre-registro).
- #166 (S, Sonnet): skill «predecir-e-investigar».
- #167 (S, Sonnet): `devlog base-rates`, líneas base contadas desde los episodios.

**Sin issue todavía.**
- Fijar los episodios dentro de las pruebas de recall (tres pruebas dependen de los episodios reales).
- Endurecer `comprobar`: que ate el registro a su pasada, cuente tareas y exija el zip.
- Anotar en el pre-registro el desenlace de la predicción 6 y la remisión de la sección 4 a la 8.4.

**Pendiente del dueño.**
- Si el criterio exige siempre la prueba exacta además de los «6 pares».
- Leer y, si no es la que quiere, corregir la regla de las sesiones cortadas (comentario en el issue #103).
- Qué hacer con el #159 (duplicado «no planeado»): el guardián salta por las reglas 2 y 3.
- Qué probabilidad de cuelgue por sesión acepta para lanzar.

**En local y gratis, sin hacer.** Las 21 sesiones que QA no midió y la pasada del parche de referencia.

**Para retomar.** Sesión nueva en el repositorio; `git worktree list`; `gh pr list`; leer esta sección y
`experiments/azar/preregistro/prediccion_de_fallos.md`. Antes de empezar un issue: escribir su predicción.
Antes de relanzar un agente: mirar qué dejó el anterior en disco.

Nada se subió, se envió ni se contrató. No queda ningún agente ni contenedor corriendo.

## Vuelta 41 — 2026-10-09, desde las 12:15 UTC

**Preguntas de la vuelta** (del dueño, que las pasó al concilio): qué se hace con el issue #159, y qué
probabilidad de que una sesión se cuelgue se acepta para lanzar una corrida.

**Nada se subió, se envió ni se contrató.** Esta vuelta no baja datos nuevos: las dos preguntas se responden
con los rescates ya bajados y con el repositorio. Recall hecho desde `main` al día (lección aplicable: el
ensayo del tope de llamadas ya mostró que el arnés no corta donde se espera).

**Decisiones del dueño antes del concilio** (comentario en el issue #103):
1. La prueba exacta se exige siempre, además de los «6 pares»: «Sí, por favor. Realizar esto; la intención
   es poder, antes de enviar, lograr determinar una solución».
2. La regla de las sesiones cortadas queda aprobada como estaba redactada: «Adelante, aplicar esto».
3. El #159 y la probabilidad de cuelgue aceptable: «Llama al concilio… pide ayuda y consejo a los expertos».
4. Empezar por el issue #164.

**Issue #164 en curso:** seis predicciones fechadas en el commit `44e9e3f` de la rama
`issue-164-tope-por-tarea` (12:16 UTC), antes de lanzar al implementador (`implementador-opus`, árbol
`F:\Code\ALL-wt-tope-tarea`).

### Parecer del gestor del proyecto sobre el #159, copiado tal cual

1. El #159 es un duplicado sin trabajo, cerrado `NOT_PLANNED`. Es el segundo de este tipo, después del #104,
   y solo el #159 salta, porque el #104 está fuera del `--since` y completo.
2. El fallo es de la regla, no del issue. Las reglas 2, 3 y 9 de `scripts/board_check.py` no miran
   `stateReason`, y la regla 4 y `pilot_metrics.py` sí.
3. No hay política escrita para cerrados sin trabajo. Solo `docs/piloto-estimacion.md:17` los excluye del
   piloto.
4. Se descarta rellenar el #159 como *Verificada*. Sería un cierre confirmado falso y duplicaría la talla L y
   los 5 puntos del #160 en el tablero.
5. Se descarta quitar la tarjeta y aceptar la regla 9. Un guardián que salta siempre se deja de leer.
6. Se recomienda un issue XS o S: un cerrado distinto de `COMPLETED` queda fuera de las reglas 2, 3 y 9. Las
   reglas 1, 5, 7 y 8 no cambian y las pruebas incluyen controles `COMPLETED` y `OPEN` que siguen saltando.
7. Mientras tanto, la tarjeta del #159 se queda como está y R2 y R3 del #159 son un falso positivo conocido.
   No se rellena ningún campo.
8. Problema de fondo: ningún control avisa de issues creados con una cuenta distinta de `cherrera0001`.

Riesgo que el propio gestor anota: que alguien cierre trabajo real como «no planeado» para eludir la
verificación.

### Parecer del analista de datos sobre el cuelgue, copiado tal cual

1. Analista de datos, concilio 41. Los 310 inicios de tarea y las 8 sesiones reales de GPU del rescate
   `2026-10-08T2231Z` no tienen ningún cuelgue; cota al 95 %: menos de 0,96 % por frontera y menos de 44 % por
   sesión de 60 tareas.
2. Ninguna tarea real pasó de 304 s; un cuelgue de 16 min habría quedado dentro de alguna tarea y hay 0 de
   310. Para pausas cortas, solo se puede ver la distancia inicio a primera petición en 145 tareas: máximo
   42 s.
3. El forense midió 0 de 4 500 fronteras sin carga y 16 de 4 000 con carga artificial (0,4 %, cerca de 21 %
   por sesión de 60). Los datos reales no lo descartan: P(0 de 310) = 0,29.
4. Sin tope, un cuelgue quema unas 24 h de cuota (supuesto de kill a 12 h, factor 2), 20 h sobre lo planeado;
   con 7,9 h de plan, dos cuelgues superan las 30 h semanales.
5. El #164 tal como está termina la sesión al vencer el tope. Arregla la cuota, no el resultado: se pierden
   las tareas de k en adelante. Hay que quitar la causa (vaciar el mapa) o seguir tras el corte para perder
   solo una.
6. Curva (2 pasadas): extra de cuota esperado sin tope = 40 h × p. Con p = 1 %, 0,4 h; con 5 %, 2 h y 8 % de
   corridas inservibles; con 25 %, 10 h y 37 %.
7. Para acotar p < 5 % por sesión hacen falta 3 540 fronteras sin cuelgue (24 h a 150/h en local; 6 min con el
   bucle sintético); 17 940 para < 1 %. En Kaggle son unas 216 h de cuota: imposible.
8. El diseño de ruido (6 o más discordantes de 60) detecta con 80 % de potencia un ruido de 13 %, no uno de 5
   a 8 %; perder tareas lo debilita más.
9. No se fija una probabilidad: se fija la pérdida máxima por cuelgue (una tarea y 0,5 h de cuota) y se exige
   que el notebook la garantice.
10. Regla propuesta: lanzar la 08 con #164 fusionado, sus dos escenarios verdes y 3 540 fronteras con carga
    con 0 ciclos. Sin medir: ipykernel de Kaggle, límite de sesión, cuota restante, carga real y si se puede
    parar una sesión.

Lo que el analista deja como supuesto y no como dato: que Kaggle corta una sesión a las 12 h (las «12 horas»
que aparecen en los documentos del caso son el límite del envío al concurso, no el de un notebook). Pregunta
suya al forense, sin responder: si «ciclo en el mapa» (1 554 de 4 000 sin carga) y «escritura que no
terminaría» (0 de 4 500) miden lo mismo.

**Efecto inmediato sobre el #164:** el orquestador pasó al implementador las líneas 5 y 10 (perder una sola
tarea si se puede demostrar, y registrar carga del sistema, hilos vivos y versiones en el latido).

### Parecer del arquitecto de IA sobre el cuelgue, copiado tal cual

1. La versión de `ipykernel` de Kaggle no está medida; el 6.29.5 del ensayo lo eligió el `Dockerfile` local.
   Kaggle corre Python 3.12.13 con papermill.
2. El bucle `iostream.py:516` existe de la 6.29.0 a la 7.0.1; no existe hasta la 6.28.0 ni desde la 7.1.0. La
   imagen base pública de Colab trae hoy 6.17.1 (inferencia para la imagen fijada).
3. Kaggle L4×4 tiene 48 CPU (medido); la carga se estima en 0,35 ejecutables por CPU o menos, contra 2,3 a
   3,3 en el ensayo que vio la carrera. Se parece al brazo sin carga: 0 ciclos en 4 500 fronteras.
4. Si el mecanismo existe allí, la probabilidad por corrida (118 fronteras) es de 7,6 % o menos sin carga y de
   27 a 56 % con carga. Las 310 tareas reales sin cuelgue no acotan nada por sí solas.
5. Un cuelgue sin vigilancia gira hasta el tope de Kaggle: 12 h (fuente no oficial) × 2 = 24 h de cuota, 80 %
   de la semana, y la repetición no cabe.
6. Con tope por tarea de 15 min (3 veces el máximo medido de 303,6 s) un cuelgue cuesta 0,76 a 1,03 h;
   vigilado a mano, 5,3 h como máximo.
7. Regla: se lanza si la pérdida esperada por cuelgue es de 1 h de cuota o menos y un cuelgue deja repetir la
   pasada dentro de las 30 h. Sin vigilancia ni tope no se lanza.
8. El #164 debe llevar vaciado del mapa con `getattr` (en 6.17.1 el atributo no existe) y tope por tarea sin
   `with`, que termine la sesión con excepción. No conviene el grupo único de hilos ni partir las pasadas.
9. Si el #164 tarda: lanzar vigilado, con 14,3 h o más de cuota libre, las dos pasadas en paralelo y corte a
   los 10 min sin línea `TAREA`.
10. Antes de lanzar, y con aprobación del dueño: una sesión de CPU sobre la misma imagen que imprima
    `ipykernel.__version__` y la carga. No gasta cuota de GPU.

Fuentes que el arquitecto abrió: el código de `iostream.py` de ipykernel por etiquetas y su registro de
cambios (PR #1186 y #1451), el `Dockerfile.tmpl` y los requisitos de la imagen pública de Kaggle, y la lista
de paquetes de Colab. El tope de 12 h sale de dos fuentes no oficiales; la página oficial de Kaggle no le
abrió.

**Desacuerdos abiertos, con el dato que los cierra.**
1. Al vencer el tope por tarea: seguir con la siguiente (analista) o terminar la sesión (arquitecto: el hilo
   que gira altera el reloj de las demás). Lo cierra el ensayo del #164: si tras vaciar el mapa el hilo viejo
   termina o sigue vivo. Regla pasada al implementador: seguir solo si se comprueba que terminó; si no,
   terminar; nunca dos tareas a la vez.
2. Umbral: «una tarea y 0,5 h por cuelgue» (analista) o «pérdida esperada de 1 h o menos y que quepa repetir
   la pasada» (arquitecto).
3. Si el #164 tarda: lanzar vigilado a mano (arquitecto) o esperar (analista).
4. Si el mecanismo existe en Kaggle. Lo cierra leer la versión de ipykernel allí.

**Efecto inmediato sobre el #164:** se pidió al implementador ensayar también bajo un núcleo con
`ipykernel 6.17.1`, donde el atributo no existe, y registrar la versión al instalar.

### Parecer del auditor del método, copiado tal cual

1. Auditor del método, concilio 41. #159: enmiendo al gestor. Exento de las reglas 2, 3 y 9 solo si está
   `CLOSED`, su `stateReason` es `NOT_PLANNED` o `DUPLICATE` y ningún episodio lo cita; el vacío no exime;
   cada exento sale como aviso.
2. El #104 no es «del mismo tipo»: es `NOT_PLANNED` con 6 PR fusionados que lo referencian y dos episodios
   (048 y 053). La condición del gestor lo habría eximido; el hueco vale 1 de 2 casos.
3. Se reproducen: 310 tareas en 8 sesiones sin cuelgue, máximo de 303,6 s, 16 de 4 000 con carga, 2 de 43
   discordantes entre 03 y 04, y el `Dockerfile` que fija `ipykernel==6.29.5`.
4. 44 % por sesión y 69 % por corrida son la misma cuenta (0 de 302 fronteras). No acota nada útil.
5. Corregido: «0 de 4 500 sin carga» omite una corrida sin carga con un ciclo formado en la iteración 2 446 de
   4 000. «Ciclos 1 554» cuenta iteraciones con el ciclo presente, no eventos. La tasa del laboratorio va de
   0,03 % a 29 % según la configuración.
6. La versión de `ipykernel` de Kaggle no está en ningún log; 6.17.1 es inferencia. El bucle existe en 6.29.5
   a 7.0.1 y no en 6.28.0 ni en 7.1.0 (medido en el código).
7. Veto toda condición de lanzamiento expresada como probabilidad de cuelgue en Kaggle, y leer las 3 540
   fronteras como cota de Kaggle: cae dentro de lo no medido.
8. Regla: se lanza cuando el ensayo demuestra que un cuelgue de cualquier causa cuesta 1,1 h de cuota como
   máximo (tope de 900 s y cierre con excepción) y la cuota leída ese día es de 14,6 h o más. Hoy no se
   cumple: faltan el #164, la versión de Kaggle y la lectura de cuota.
9. No se lanza vigilado a mano. Una tarea cortada por `tarea_colgada` es un par faltante, fechado antes de
   subir. La primera subida va en serie, pasada 1 y luego pasada 2.
10. La sesión de CPU vale para la versión (mismo digest) y no para la carga (4 CPU frente a 48). Decide qué
    versión fija el ensayo local, no cuándo se lanza, y necesita la orden del dueño.

**Lo que cada rol retira o queda corregido tras el cruce.**
- Gestor: «segundo de este tipo, después del #104» (el #104 tuvo trabajo).
- Forense: «0 de 4 500 sin carga» como cuadro completo; su reparto 75 % y 25 % es un juicio.
- Analista: las 3 540 fronteras miden el laboratorio, no Kaggle; «una tarea y 0,5 h» solo vale si se sigue.
- Arquitecto: «3 a 1 a favor de 6.17.1» y «0,35 por CPU» son juicio; lanzar vigilado a mano contradice su
  propio umbral; «la repetición no cabe» depende del factor de cuota.

### Decisiones del concilio 41

**A. Issue #159.** Se cambia la regla, no el issue: exento de las reglas 2, 3 y 9 si está cerrado como «no
planeado» o «duplicado» y ningún episodio lo cita. La tarjeta del #159 se queda como está y no se rellena.
Issue #169 abierto con la regla exacta del auditor (S, Sonnet).

**B. Cuelgue.** No se fija una probabilidad (vetado). Regla de lanzamiento con ocho condiciones, en un
comentario del issue #103: pérdida máxima de 1,1 h de cuota por cuelgue, demostrada en el ensayo; tope por
tarea de 900 s; ensayo con la misma versión de `ipykernel` que Kaggle; el notebook imprime versión y carga;
cuota leída de 14,6 h o más; primera subida en serie; orden del dueño. No se lanza vigilado a mano. Cláusula
fechada: una tarea cortada por `tarea_colgada` es un par faltante.

**Lo que el auditor señala sin vetar:** el criterio «6 o más discordantes de 60» de la iteración 08 casi no
puede refutar con el ruido observado (lo alcanzaría unas 6 veces de 100). La corrida entregará una cota del
ruido. Conviene fechar, antes de subir, qué ruido haría indecidible el brazo de razonamiento.

### Fallos del orquestador en esta vuelta

- Pasó al implementador del #164 «ensayar bajo `ipykernel 6.17.1`» antes del dictamen: esa versión era una
  inferencia del arquitecto. Corregido en un mensaje posterior (ensayar donde el atributo no existe; no
  afirmar qué trae Kaggle).
- La convocatoria del analista y del arquitecto llevaba el resumen del forense con «0 de 3 000 sin carga»
  como dato; el auditor mostró que el cuadro omitía una corrida. Otra vez una cifra en el encargo.
- Escribió «recall hecho desde `main`» sin anotar cuántas veces ni con qué consulta.

- Tras el concilio volvió a preguntar al dueño tres cosas que ya estaban delegadas o que podía resolver solo
  (el 1,1 h, la cuota y la sesión de CPU). El dueño: «te pedí resolver junto al concilio, ¿por qué vuelves a
  preguntar?».

**Resuelto sin preguntar (12:45 UTC).**
- El 1,1 h queda fijado: es la cifra del concilio.
- Cuota leída por API (`uvx kaggle quota`, 12:43 UTC): GPU 29,53 h usadas, **0,47 h libres** de 30,00; se
  repone el 2026-10-10 a las 00:00 UTC. La condición 6 de la regla (14,6 h libres) no se cumple hoy y sí
  podrá cumplirse desde mañana.
- Sonda del núcleo armada y ensayada en local: `instrumentos\sonda_nucleo\` (`armar_sonda.py`,
  `kernel_sonda\sonda.ipynb` con SHA-256 `7d10c9b3…`, `kernel-metadata.json` con el mismo `docker_image` de las
  corridas, sin GPU, sin internet y sin fuentes de datos). Una celda: versión de `ipykernel` y de otros once
  paquetes, si stdout tiene el mapa de hilos, CPU, afinidad, carga, y la lista entera de paquetes a
  `sonda_nucleo.json`. Ensayada bajo núcleo real con `ipykernel` 6.29.5, 6.17.1 y 7.1.0: las tres terminan y
  la sonda distingue las versiones (mapa de hilos presente solo en la 6.29.5).
- **La sonda no se subió.** Es una ejecución en Kaggle, y la regla del dueño del 2026-10-04 dice que ninguna
  subida, tampoco en CPU ni en privado, se hace sin su palabra. El propio concilio lo dijo: «necesita la orden
  del dueño». Queda lista: `uvx kaggle kernels push -p <carpeta kernel_sonda>`.

**Único pendiente del dueño tras el concilio:** la palabra para subir la sonda de CPU.

**La regla del concilio para el #159 falló en su propio control (13:10 UTC).** El implementador del #169 (PR
#170) midió que, con la regla tal como la escribió el auditor, el #104 sale exento: ningún episodio lo cita
como `#104` en su `ref` (los episodios de ese trabajo citan `#100` y `#103`). El auditor había afirmado que lo
citaban dos episodios; lo citan en su texto, no en la referencia que la regla mira. Se aplicó la salida que el
propio auditor dejó prevista: añadir «y que ningún PR fusionado lo referencie». Devuelto al implementador con
esa enmienda, sin preguntar al dueño. Además el implementador encontró que el guardián de inicio de sesión
(`scripts/session_guard.py`) llamaba a la regla 9 por su cuenta y habría seguido avisando; lo arregló.

## Vuelta 42 — 2026-10-09, desde las 13:20 UTC

**Pregunta de la vuelta** (del dueño): Anthropic publicó `anthropics/oss-scanner`, la inscripción a un
servicio que busca y corrige vulnerabilidades en proyectos de código abierto con agentes. «Datito, y el
concilio: ¿qué podemos aprender de él para nuestro desafío?»

**Nada se subió, se envió ni se contrató.** Esta vuelta no baja datos nuevos: usa el rescate
`2026-10-08T2231Z` y una copia local del repositorio del servicio (un día de vida, un commit, sin el código
del escáner: solo la inscripción, tres plantillas y tres guiones que construyen la imagen de prueba).

**Lo que el orquestador leyó antes de convocar** (repositorio, página y términos; estas dos últimas a través
de un resumen automático): servicio alojado y gratuito para proyectos con «impacto crítico en infraestructura
y seguridad»; el proyecto se construye con red y se audita sin ella; el dueño aporta un `threat_model.md`;
cada hallazgo lleva reproductor y parche propuesto; otros agentes vuelven a comprobar y analizan la causa; los
informes no los revisa una persona y pueden traer falsos positivos. Nuestro repositorio no califica y el
servicio busca vulnerabilidades, no fallos de lógica.

**Convocados en paralelo, con la pregunta y las rutas, sin conclusión:** analista de datos (qué dicen las
trayectorias sobre reproducir, localizar, volver a comprobar y gastar presupuesto), QA de trayectorias (qué
hace de verdad el agente frente a ese método), arquitecto de IA (qué cabe en Gemma con 4 minutos y 40
llamadas, y qué permiten las reglas precomputar) e inteligencia pública (qué hay publicado sobre el método y
sobre arneses comparables, y el estado de la competencia). Después cruza el auditor del método.

Lo que esta vuelta no cambia: la iteración 08 sigue siendo la base y su repetición, sin tocar el agente.

### Parecer de inteligencia pública, copiado tal cual

1. Lo publicado por Anthropic describe el método (contenedor sin red, ranking de archivos, oráculo de fallos,
   segundo agente), pero ningún post mide qué pieza aporta más; no hay ablación de ese escáner.
2. Lo transferible del escáner a nosotros es una disciplina de entrega, "no entregues sin demostrar", no una
   técnica de modelo pequeño.
3. La evidencia más fuerte de que un reproductor ayuda viene de Agentless, que lo usa como filtro sobre 40
   muestras con modelos fuertes; con un modelo pequeño y 40 llamadas no hay evidencia publicada.
4. Las pruebas generadas discriminan poco (<20 % de señal en R2E-Gym), así que un reproductor que el propio
   modelo escribe puede validar parches malos.
5. Las ablaciones de SWE-agent (visor de ~100 líneas, edición con lint, historial recortado) son las de mayor
   efecto medido, y están cerca de lo que ya vemos: lecturas que pierden rango y ~50 % de llamadas repetidas.
6. Los modelos abiertos pequeños fallan sobre todo por bucles, parches vacíos y topes de pasos, no por el
   contenido del parche, igual que lo medido en nuestras trazas.
7. Ninguna regla de la competencia prohíbe un reproductor, un verificador como subagente o varios candidatos
   dentro del presupuesto; la pregunta sobre metadatos precomputados (tema 743751) sigue sin respuesta oficial
   en lo que leímos.
8. Notas o índices por repositorio probablemente no transfieren, porque la respuesta del staff (744951) dice
   que el conjunto oculto sale de repositorios privados; eso es inferencia, no regla.
9. El estado de la tabla y el foro después del 2026-10-07 no está medido; este informe no cubre cambios
   recientes de la competencia.
10. Nada de esto justifica subir o enviar; cualquier cambio sigue necesitando ensayo local y más de 19 tareas
    por brazo para distinguirse del ruido.

Cifras que trae, con su fuente (leídas a través de un resumidor automático; releer la página si una cifra
decide algo): anuncio de Anthropic del 2026-10-08: 97 vulnerabilidades críticas o altas en 48 proyectos
validadas por personas, 85 válidas (88 %), 11 duplicadas y 1 inválida. Agentless (arXiv 2407.01489, tabla 4,
300 tareas): 77 arreglos con voto solo, 81 con pruebas de regresión, 96 con pruebas de reproducción generadas.
SWE-agent (arXiv 2405.15793): 18,0 % de base; 10,3 % sin editor; 15,0 % sin lint; visor de 100 líneas 18,0 %
contra 12,7 % con el archivo entero; conservar las últimas 5 observaciones 18,0 % contra 15,0 % con todo el
historial. R2E-Gym (arXiv 2504.07164): menos del 20 % de las pruebas generadas discriminan. SWE-smith (arXiv
2504.21798): más del 25 % de las trayectorias de un modelo de 32B tienen una secuencia repetida de 10 o más
acciones, y las intervenciones simples contra la repetición no mejoran la resolución.

Reglas de la competencia que cita: el envío solo puede pedir herramientas del arnés o subagentes propios; el
mismo modelo para todo agente y subagente; no se pueden mandar las tareas a una API ajena (2.4.b). Sin
respuesta oficial: si una skill puede llevar metadatos precomputados por repositorio.

No pudo refrescar el estado de la competencia sin iniciar sesión: tabla, foro y notebooks quedan al
2026-10-06/07. No leyó el final del post que describe el arnés ni el código de los finalistas de AIxCC.

### Parecer del arquitecto de IA, copiado tal cual

1. Del escáner solo es código la inscripción: construcción de 45 min en 16 CPU y 64 GB, agente en 2 CPU y 8 GB
   sin red, capa con Claude Code y depuradores, y un documento del dueño que el escáner lee antes de empezar.
   Lo de «agentes que recomprueban, causa raíz y parches» es declaración.
2. Su recomprobación funciona porque tiene oráculo ejecutable (reproductor, AddressSanitizer) y modelos de
   frontera con cientos de corridas por proyecto; nada de eso existe aquí.
3. Corrijo dos premisas: los repositorios que puntúan son privados, así que no hay notas por repositorio que
   valgan; y los 4 minutos y 40 llamadas son nuestros, lo oficial son 12 h.
4. Medido en 116 sesiones sin razonamiento: mediana de 35 de 40 llamadas y 96 de 240 s; 21 tocan el tope de
   llamadas. Sin razonamiento muerde el tope de llamadas; con razonamiento, el reloj (21 de 29 en 235 s o
   más).
5. Un reproductor cuesta 5 a 7 llamadas y 25 a 45 s: cabe en reloj y no en llamadas, salvo que se recorte
   exploración. Con razonamiento no cabe.
6. Leído en el arnés: `submit_patch` hace `git add -N .`, así que el reproductor va en `/tmp`; y `run_command`
   devuelve la cabeza de la salida, así que las pruebas se leen con `tail`.
7. Lo trasladable del documento del dueño es «cómo ejercitarlo», generado en el reloj por un guion de skill: 1
   llamada, 3 a 5 s, hasta 1 250 tokens. En el sistema, no más de 300 a 500 tokens.
8. Brazos limpios: guion-mapa (con relleno de control), salida con `tail`, línea de causa. El reproductor es
   limpio solo con topes fijos. Segundo agente, causa raíz por subagente y varias pasadas arrastran tres
   cambios.
9. Orden, después del brazo de razonamiento: primero el guion-mapa (útil si la mediana de llamadas baja a 30 o
   menos y las sesiones con prueba pasan de 15 % a 40 %); después el reproductor (útil si «falla antes, pasa
   después» predice pasar las ocultas).
10. Descarto el segundo agente que aprueba: mismo modelo, sin oráculo, sin compactación y con un fallo que ya
    hizo perder el parche. No abrí las reglas de Kaggle de primera mano; `z_oido` no corrió con Gemma.

**Fallo del orquestador en la convocatoria:** el encargo decía «el concurso da pocos repositorios, conocidos
de antemano» y trataba los 4 minutos y 40 llamadas como regla. El arquitecto corrigió las dos: las tareas que
puntúan salen de repositorios privados, y esos topes son de nuestro `eval_config.yaml`; lo oficial son 12
horas para todo el envío (techo de unos 349 s por tarea con 120 tareas).

**Dos hallazgos de código del arquitecto que valen con independencia de lo demás** (leídos en
`swegemma/tools/execution.py`, sin ejecutar): `run_command` devuelve los primeros 5 000 caracteres de la
salida, de modo que en una salida larga de pruebas el resumen del fallo, que va al final, queda fuera; y
`submit_patch` añade al parche todo archivo nuevo del espacio de trabajo, así que un guion de reproducción
creado ahí entraría en la entrega.

Coincidencias entre los dos roles que ya entregaron: el segundo agente del escáner funciona porque tiene un
oráculo ejecutable y aquí no lo hay; las notas por repositorio no transfieren; el reproductor no tiene
evidencia publicada con un modelo pequeño.

### Parecer de QA de trayectorias, copiado tal cual

1. Leí 14 trayectorias sorteadas con semilla 4242 y medí 145 con reglas automáticas; el recorrido típico es
   explorar con grep, editar hacia la llamada 12 y entregar, sin comprobar en 22 de 110 sesiones que editan.
2. El entorno funciona desde la primera llamada: unas 29 llamadas de 4246 se pierden por entorno.
3. `search_similar_code` devolvió vacío en 300 de 300 llamadas y el subagente gastó 198 llamadas del tope
   compartido sin resolver ninguna de sus 7 sesiones.
4. En 507 lecturas de archivo (11,9 % de las llamadas) la clave rota del argumento hace que el arnés devuelva
   las líneas 1 a 150 en silencio, y 359 se repiten sin que el agente lo note.
5. De 43 parches que no pasan, 30 están en el archivo y la zona correctos con lógica incompleta; 6 tienen
   sintaxis rota por comillas escapadas, y en esos 6 no se ejecutó nada tras la última edición.
6. Un reproductor existe en muchas sesiones, pero en 16 de 23 malos con ejecución previa nunca falló antes de
   editar: el enunciado no siempre da la entrada que falla.
7. La comprobación propia posterior sale verde en 20 de 23 malos y en 27 de 32 buenos, así que "ejecuta y
   corrige si falla" casi no discrimina.
8. Cambio con más apoyo: tras la última edición, una sola comprobación de sintaxis o importación; delata 6 de
   6 rotos y 0 de 39 buenos; techo de recuperación 1 a 3 sesiones, inferido.
9. Del método del escáner no se traslada el tiempo sin tope, el modelo más capaz ni los depuradores; sí se
   traslada, barato, el reproductor del parche, con el límite de que el enunciado no siempre lo permite.
10. No medido: si Gemma corrige tras una alarma, y cuántos malos delataría un reproductor de dos líneas.

Otras cifras de su informe (145 sesiones, 4 246 llamadas del agente principal, iteraciones 03 a 07; las reglas
son automáticas y las declara): 53 sesiones nunca editan código fuente; entre las 110 que editan, resuelven 5
de 22 las que no ejecutan nada y 34 de 70 las que ejecutan algo (no es causal: las tareas fáciles explican las
dos cosas); reproductor «roja antes, verde después con el mismo comando»: 8 resueltas contra 2 que no pasan;
1 336 de 4 246 llamadas son repeticiones idénticas (31 %); 131 `edit_file` fallan por esquema con la clave
rota; 61 de 139 ediciones aceptadas pasaron por el desescapado de comillas del arnés; la salida de pruebas
quedó truncada sin su resumen en 6 de 69 corridas de pytest; 22 de las 23 sesiones cortadas por llamadas sin
parche nunca editaron nada, y en 14 de ellas el gasto es un bucle de la misma orden; en 14 de 26 cortadas con
parche, lo entregado son los archivos de reproducción del propio agente.

**Discrepancia que QA no pudo reconciliar:** cuenta 56 cortes con la clase del instrumento (39 por llamadas,
17 por tiempo, más 1 por contexto); en la vuelta 40 se contaron 25 (22 por tiempo, 2 por llamadas, 1 por
contexto). Es otro criterio de corte. Queda para el auditor.

**Desacuerdo abierto entre roles:** el arquitecto propone el reproductor como segundo brazo; QA lo desmiente
con las trayectorias (el reproductor que el agente escribe sale verde antes de editar en 16 de 23 parches
malos, y su comprobación posterior sale verde en 20 de 23). Dato que lo cerraría: cuántos de los parches
malos delataría un reproductor construido con la entrada que de verdad falla, que el enunciado no siempre da.

### Parecer del analista de datos, copiado tal cual

1. Universo: 145 sesiones de 43 tareas (A dos pasadas, H, I), 39 resueltas; el diseño distingue unos 30 a 50
   puntos de diferencia entre prácticas, así que todo lo que sigue es asociación exploratoria (unas 45 a 50
   comparaciones), no efecto.
2. Re-comprobar tras la última edición es la señal más fuerte: entre las editadas que entregan 30/55 con
   ejecución posterior contra 6/33 sin ella, 20 contra 2 pares dentro de la misma tarea (6 tareas «a veces»),
   y se mantiene sin las sesiones cortadas.
3. El 60 % de las editadas ya ejecuta algo tras la última edición aunque el `system.md` de A y H lo pide; el
   brazo no sería pedirlo sino exigirlo (no aceptar `submit_patch` sin ejecución posterior).
4. Reproducir antes de arreglar no se sostiene dentro de la tarea (3 pares a favor, 4 en contra) y solo 14 de
   20 «reproducciones en rojo» revisadas eran fallos del defecto; se prueba, a lo sumo, junto con la anterior.
5. El análogo del `threat_model.md` no tiene señal: descubrir cómo correr las pruebas cuesta 0,7 llamadas por
   sesión (2,2 % de las llamadas) y solo 17 % de las sesiones corre alguna vez un ejecutor de pruebas.
6. Localizar es necesario (38 de 39 resueltas tocan un archivo de referencia; 0 de 31 sin abrirlo resuelven)
   pero no suficiente: 79 % lo abre en una mediana de 3,5 llamadas.
7. El mayor lastre es no llegar a editar: 53 de 106 no resueltas no tienen parche de fuente, 27 de ellas con
   39 o 40 llamadas y entrega vacía, y el 69 % de las no resueltas gasta 20 o más llamadas antes de editar
   contra 23 % de las resueltas.
8. Con una pasada sobre 43 tareas un efecto de OR 3 (+8 puntos sobre 20 %) cumple «6 pares + McNemar exacto»
   solo 13 veces de 100; con 150 tareas 63 de 100, con 300 94 de 100.
9. El segundo agente que re-comprueba del escáner no se puede juzgar con estos datos (no hay segundo lector) y
   4 minutos no lo permiten sin recortar al primero.
10. Orden de brazos con señal: 1) exigir ejecución tras la última edición, 2) editar antes o ahorrar lectura y
    búsqueda, 3) reproducir primero como complemento; sin señal: contexto de cómo correr las pruebas.

Lo que el analista no pudo reproducir: las «4 resueltas cortadas» del concilio 41 (con el campo de error de
las trazas cuenta 0; con duración de 270 s o más cuenta 6, todas de la condición I). Pide la definición.

**Desacuerdos entre roles, con el dato que los cierra.**
1. **Volver a ejecutar tras la última edición.** El analista: es la señal más fuerte (30 de 55 contra 6 de 33).
   QA: la comprobación propia sale verde en 20 de 23 parches malos, casi no discrimina. No se contradicen si
   lo que se asocia con resolver es ejecutar algo (y ver un error de sintaxis o de importación), no acertar
   con la prueba. Lo cierra separar, en las mismas sesiones, qué delató la ejecución posterior.
2. **Reproductor.** El arquitecto lo propone como segundo brazo; QA y el analista no le ven señal dentro de la
   misma tarea.
3. **Guion-mapa de cómo correr las pruebas.** El arquitecto lo propone como primer brazo; el analista mide que
   ese descubrimiento cuesta 0,7 llamadas por sesión.
4. **Conteos que no cuadran entre roles:** sesiones que nunca editan fuente (53 según QA, 47 según el
   analista); cortes (56 según QA con la clase del instrumento; 21 con marca según el analista; 25 en la vuelta
   40); resueltas cortadas (4 en el concilio 41; 0 o 6 según el analista).

Coincidencia de tres roles: el lastre principal es no llegar a editar y gastar llamadas en repeticiones y
herramientas que no devuelven nada, no la falta de un reproductor. Pendiente: el auditor del método.

### El dueño corrige el procedimiento (14:30 UTC)

Dijo: «¿Realmente se debe iterar en 31 llamadas? … si tenemos un total de 40 llamados no podemos iterar 31
solo intentando resolver una tarea. ¿Te parece coherente? ¿Qué dice el concilio ante esto? … no están haciendo
bien su ciclo de consulta o discusión. Creo que hoy no están funcionando realmente como un concilio», y pidió
revisar `karpathy/llm-council`.

**Tiene razón en las dos cosas, y el fallo es del orquestador.**
- Sobre el tope: los informes midieron el problema (31 % de llamadas repetidas; el subagente con 31, 27, 39,
  27, 9, 25 y 40 llamadas del tope compartido; 27 sesiones con 39 o 40 llamadas y entrega vacía) y ninguno
  propuso limitarlo. Cada rol contestó su parte y la pregunta obvia quedó sin dueño.
- Sobre el concilio: los roles se convocaron en paralelo con sub-preguntas distintas, ninguno leyó a otro y
  solo el auditor veía todo al final. El paso 5 de la skill `concilio-de-experimento` ya mandaba volver a
  preguntar a cada rol qué afirmación suya se cae, y no se hizo en las vueltas 41 ni 42.

**Lo leído en `karpathy/llm-council`** (un commit, unas 1 600 líneas; el autor lo describe como un experimento
de un sábado, sin evaluación de que dé mejores respuestas): tres etapas. (1) La misma pregunta va a todos los
modelos por separado. (2) Cada modelo recibe las respuestas de los demás anonimizadas («Response A, B, C»),
dice qué hace bien y mal cada una y entrega un orden con formato fijo («FINAL RANKING:»); se calcula la
posición media. (3) Un presidente sintetiza con las respuestas y las evaluaciones. La diversidad viene de usar
modelos de proveedores distintos.

**Qué se adopta:** la etapa 2, que es la que faltaba, con el orden por respaldo en datos y no por opinión; la
misma pregunta para todos; el formato fijo del orden. **Qué no se traslada:** la diversidad de modelos (todos
los roles son el mismo modelo; el anonimato evita deferencia al rol, nada más), y el voto como sustituto de una
medición.

**Hechos del arnés leídos por el orquestador para la pregunta del tope** (`swegemma/budget.py`, `config.py`,
`agent.yaml` del envío): no hay guardia contra llamadas repetidas ni tope por herramienta; los presupuestos son
totales (tiempo, llamadas, turnos); la lista de herramientas del agente sí es nuestra, y hoy incluye la
búsqueda que devolvió vacío 300 de 300 veces y el subagente. Quitar una herramienta es una garantía; una regla
en la instrucción es una petición.

### Ronda 2: revisión cruzada (15:00 a 15:20 UTC)

Los cuatro roles leyeron los cuatro informes anonimizados y respondieron con formato fijo.

**Orden de las once acciones candidatas** (posición en el orden de cada rol; A arquitecto, B QA, C inteligencia
pública, D analista de datos):

| Candidata | A | B | C | D | Media |
|---|---|---|---|---|---|
| P2 quitar la búsqueda y las herramientas de grafo que no devuelven nada | 2 | 1 | 1 | 1 | 1,25 |
| P1 quitar el subagente | 1 | 2 | 2 | 2 | 1,75 |
| P4 comprobar sintaxis o importación tras la última edición | 3 | 3 | 4 | 6 | 4,00 |
| P5 exigir una ejecución tras la última edición | 5 | 5 | 5 | 3 | 4,50 |
| P9 corregir la llamada mal formada de lectura y edición | 4 | 6 | 3 | 5 | 4,50 |
| P3 regla contra repetir la misma llamada | 7 | 4 | 7 | 7 | 6,25 |
| P11 tope de exploración antes de la primera edición | 6 | 11 | 6 | 4 | 6,75 |
| P8 leer la salida de pruebas por la cola | 8 | 7 | 9 | 8 | 8,00 |
| P6 reproductor antes de editar | 9 | 8 | 8 | 9 | 8,50 |
| P7 guion-mapa al inicio | 10 | 9 | 10 | 10 | 9,75 |
| P10 subir los topes | 11 | 10 | 11 | 11 | 10,75 |

Los cuatro son el mismo modelo leyendo los mismos datos: el acuerdo no es una medición.

**Respuesta de los cuatro a la pregunta del dueño:** no es coherente gastar 31 de 40 llamadas así, y hace
falta un tope. Lo único que el envío puede imponer es la lista de herramientas y los totales; «no repitas»,
«edita antes de la llamada N» y «ejecuta antes de entregar» solo se pueden pedir en la instrucción.

**Lo que cada rol retiró.**
- Arquitecto: el guion-mapa como primera pieza y el reproductor como segundo brazo; y que «el tope que muerde
  son las llamadas» (lo llama síntoma: 45 de 116 sesiones llegan a 39 o más llamadas, no 21).
- QA: «el agente localiza bien» como frase general; matiza «ejecutar y corregir no discrimina».
- Inteligencia pública: «unos 50 % de llamadas repetidas» (lo medido es 31 %) y «varios candidatos es
  impensable».
- Analista: el reproductor como tercer brazo; rebaja «exigir ejecución» a asociación con 6 tareas
  informativas.

**Hechos nuevos de la ronda 2** (pendientes de que el auditor los verifique):
- El subagente no admite un tope propio: el esquema del envío rechaza campos de presupuesto en su archivo. La
  herramienta de entrega no admite precondiciones.
- La línea 11 de `prompts/system.md` del envío ordena usar la búsqueda que devuelve vacío; 60 sesiones
  empiezan por ella.
- El arnés avisa «termina y entrega» cuando quedan 10 llamadas, en la llamada 30. Entre quienes editan y
  entregan, los que no ejecutan después tienen su última edición en la llamada 30 a 32 de mediana; con margen,
  solo 8 sesiones no verifican. La señal de «volver a ejecutar» sería en buena parte presupuesto agotado.
- Regla de no repetir con un máximo de 2: liberaría 989 llamadas en 59 sesiones no resueltas. Sin evidencia de
  que cambie el resultado: esas sesiones no habían editado, y un estudio con un modelo de 32B no vio mejora al
  suprimir la repetición.
- Obligar a editar antes de la llamada 20 rompería 9 de 39 resueltas.
- Resuelven 12 de 30 sesiones con 20 llamadas o menos, 5 de 26 con 21 a 34 y 4 de 60 con 35 o más (116
  sesiones sin razonamiento; asociación).

**Qué dio la ronda 2 que la ronda 1 no había dado:** dos propuestas retiradas por su propio autor, un hecho
que explica el desacuerdo sobre «volver a ejecutar», la respuesta a la pregunta del tope con lo que se puede
imponer, y un orden común. Enviado al auditor como presidente, con las cuatro mediciones locales que los roles
proponen.

### Parecer del auditor del método (presidente, con la ronda 2 integrada), copiado tal cual

1. Recalculé desde los 12 zips: 145 sesiones, 4 246 llamadas del principal y 198 del subagente; se reproducen
   300 de 300 búsquedas vacías, 507 lecturas con clave rota (359 repetidas), 61 de 139 ediciones
   desescapadas, 6 parches con sintaxis rota y 14 de 26 «cortadas con parche» que solo llevan archivos
   auxiliares.
2. La búsqueda vacía no es un índice ausente: la herramienta busca por nombre exacto de nodo y no embebe texto
   libre; 0 de 300 consultas tenían esa forma y la línea 11 de la instrucción ordena usarla con palabras del
   error.
3. Corregidos: las ediciones rechazadas por parámetro son 211 (no 131 ni 234) y no cuentan contra el tope; los
   «56 cortes» son la clase «39 o más llamadas» (37 de 39 entregaron solas); los cortes reales son 21 con
   marca más 6 resueltas sobre el límite, cuya marca borra el arnés.
4. Volver a ejecutar tras editar es asociación sin mecanismo: 0 sesiones vieron sintaxis o importación como
   última salida y solo 8 de 27 corrigieron tras un rojo; con margen de presupuesto 32 de 54 contra 1 de 10, y
   dentro de la tarea quedan 2 tareas informativas. No se puede imponer desde el envío.
5. Reproductor y guion-mapa quedan retirados por sus autores y por los datos (verde antes de editar en 18 de 27
   malos; 0,3 a 0,7 llamadas por sesión de descubrimiento).
6. Tope: el envío solo impone la lista de herramientas y los totales; quitar subagente y grafo libera 324
   llamadas (2,2 por sesión); «no repitas más de 2» liberaría 1 145 pero solo se puede pedir.
7. Liberar llamadas cambia sobre todo el gasto: de 41 sesiones no resueltas con 39 o más llamadas, 28 no
   dejaron fuente en el parche y solo 5 tenían la referencia abierta, fuente editada y 10 o más llamadas
   liberables.
8. Potencia confirmada: con 43 tareas y una pasada, OR 3 se detecta 8 a 13 veces de 100; con 71 tareas y 2
   pasadas por brazo, 52; ningún arreglo de interfaz llega a OR 3, así que se decide por criterio mecánico y no
   por resolución.
9. Plan: kit «interfaz limpia» (sin subagente, sin grafo, sin línea 11) ensayado en local; base 08 y
   razonamiento como estaba; después «interfaz limpia» a 71 tareas por 2 pasadas con criterios mecánicos y de
   no daño fechados; una petición de lectura con `sed -n` solo exploratoria; verificador limpio antes de pedir
   la subida.
10. Veto: exigir ejecución, reproductor, guion-mapa, tope de exploración (rompería 9 de 39 resueltas), subir
    topes en este paquete y cualquier afirmación de eficacia de un arreglo de interfaz con una pasada.
11. Del escáner solo es código la inscripción; el segundo agente y sus cifras están en la página, leídas por
    resumidor; ninguna recomendación avalada depende de ellas.
12. Procedimiento: faltaron el forense, el recall anotado y el cruce del paso 5 en las vueltas 41 y 42; la
    ronda 2 sí cambió el resultado (dos brazos retirados, el aviso de la llamada 30), pero su orden es acuerdo
    de un mismo modelo, no una medición.

**Respuesta del auditor a la pregunta del dueño sobre el tope:** «No es coherente, pero lo que el envío puede
imponer libera 2,2 llamadas por sesión, y lo que liberaría más solo se puede pedir; las trazas dicen que
liberarlas cambiaría el resultado en 5 a 7 de 145 sesiones como mucho.»

**Su respuesta a la pregunta de la vuelta:** del escáner no se aprende una técnica sino una disciplina: no dar
al agente nada que no pueda devolver algo y no afirmar nada sin un oráculo. Aquí significa limpiar la interfaz
del envío antes de añadirle pasos.

**Decisiones del concilio 42** (el dueño delegó en el concilio; subir sigue necesitando su orden):
1. Se arma y se ensaya en local, con el modelo falso y sin cuota, el kit «interfaz limpia»: sin subagente, sin
   las tres herramientas de grafo y sin la línea 11 de la instrucción. Es una sola supresión de configuración,
   definida por una regla: quitar del envío lo que no puede devolver nada.
2. La iteración 08 (base y repetición) y el brazo de razonamiento siguen como estaban. Se añade como criterio
   secundario, gratis, la fracción de lecturas con clave rota.
3. «Interfaz limpia» contra la base se decide por criterio mecánico y de no daño, no por resolución: no se
   afirmará que mejora la tasa de resueltas.
4. Vetado como brazo: exigir ejecución antes de entregar, reproductor, guion-mapa, tope de exploración, subir
   topes en este paquete, y la regla de no repetir como brazo de resolución.
5. Definiciones del proyecto desde hoy: «sin edición de fuente» se cuenta por el parche final; «corte» es
   marca del arnés, o duración mayor que el límite, o 40 llamadas sin entrega (hoy son 27).

**Fallos del orquestador que el auditor señala en la vuelta 42:** las dos premisas falsas de la convocatoria;
la hipótesis «ejecutar ayuda porque delata la sintaxis», refutada (ninguna sesión vio un error de sintaxis como
última salida); no convocó al forense en la vuelta cuyos hallazgos eran del arnés; redactó una candidata como
«corregir» cuando solo se puede pedir; calculó una media de posiciones, que es un promedio de opiniones; y no
anotó el recall. Cambios que propone a la skill: la revisión cruzada como entrega obligatoria de cada rol; el
orquestador no escribe decisiones si falta; el auditor entra después de la ronda 2; la misma pregunta para
todos y sin cifras; prohibido promediar órdenes; y un rol responsable de «la pregunta obvia del dueño».

**Lo que el auditor no tenía al dictaminar:** el rescate de las 13:42 UTC (abajo), con el reenvío puntuado.

### Rescate del 2026-10-09 a las 13:42 UTC: el reenvío puntuó y cambió el puesto

Rescate por la API (`scripts/kaggle_rescate.py`, carpeta `2026-10-09T1342Z`; sale con 4 por los logs por tarea
de 0 bytes de las iteraciones viejas, que ahora sí cuenta como faltantes).

- **El reenvío 56916129, que estaba en `error`, figura ahora `complete` con nota 0,13: 8 tareas de 58.** Es el
  mismo zip con razonamiento que el 56895202, que dio 0,08 (5 tareas). El mismo zip, dos envíos: 5 y 8
  tareas. Los dos envíos del zip sin razonamiento dieron 4 y 3.
- **Tabla pública:** 2 177 equipos; nosotros, 8 tareas con 4 envíos; 269 equipos tienen más tareas y 290
  tienen 8. Mediana 6 tareas, máximo 14 (2 equipos); 12 o más, 10 equipos; 10 o más, 115.
- **La tabla premia el número de envíos:** la media de tareas sube de 4,19 con un envío a 7 u 8 con diez o
  más. El mejor de m envíos iguales esperado, según el propio guion: 4,19 con uno, 6,27 con cuatro, 6,99 con
  siete.
- El 2026-10-07 la lectura era 4 tareas y puesto 1 559 de 1 981.

### El dueño pregunta por qué Datito no lo vio (15:30 UTC)

«Datito, este es un error grave. ¿Por qué en tu análisis no habías logrado identificar este problema?
necesito que sea investigado en otra línea, de forma independiente. ¿Cómo se puede medir esto usando zorzALL?
¿Quién controla cada llamada que hace un agente? ¿Dónde se mide o se registra?»

**Respuesta de Datito, resumida de su informe.** No lo identificó porque en las vueltas 39, 40 y 41 respondía
preguntas de potencia y de qué tareas elegir, y nunca abrió qué devolvió cada llamada: clasificó las llamadas
por su nombre, no por su salida. Cuando la cifra pasó delante («llamadas agotadas») la trató como contexto o
como tautología. Lo asume como suyo: su propia regla pedía mirar adónde se va el presupuesto.

**El dato estaba en disco desde antes de su primera vuelta**, con ruta en esta misma bitácora:
- Repeticiones: rasgo «observa» de ZorzALL, 2026-10-04 (vuelta 7); medido el 2026-10-05 (vuelta 12) y el
  2026-10-06 (vuelta 32): «50 % (1 267 de 2 532)».
- Tope agotado sin editar: vueltas 11, 12, 25 y 32.
- Lectura con argumento mal formado: vuelta 32, 344 llamadas; se concluyó que «no separa resueltas de no
  resueltas» y se dejó.
- Búsqueda vacía y subagente: vuelta 38 (2026-10-07): «búsquedas por similitud vacías 78 de 78, 56 de 56, 14
  de 14, 54 de 54» y «subagente: 6 sesiones, 0 resueltas».
Es decir: el problema se midió cuatro veces en cinco días y nunca se convirtió en una acción. El fallo es del
ciclo y del orquestador tanto como del analista.

**Lo que Datito dice que sigue sin mirar:** qué devuelve cada llamada en todo el universo (su primer recuento:
de 4 444 llamadas, 2 503 con contenido, 805 lecturas truncadas, 439 errores, 309 búsquedas vacías, 211
rechazadas por esquema y 177 órdenes sin salida); las ediciones rechazadas en cadena (8 sesiones con 5 o más
seguidas, 0 resueltas); y qué se pierde en la compactación del contexto.

**Frase que propone añadir a su definición:** «Antes de agrupar las llamadas por herramienta, cuenta qué
devolvió cada una (vacío, error, repetida, truncada) y qué parte del presupuesto se fue en llamadas sin
información nueva. Cualquier tope agotado se explica con trayectoria, no con una etiqueta.»

**Línea independiente abierta, dos roles que no heredan el relato:** el verificador limpio mide el gasto sin
avance con el instrumento ZorzALL (`scripts/zorzal_perfil.py`, rama `zorzal/hipotesis-y-criterios`, PR #145 en
borrador) y dice qué ve y qué no ve ese instrumento; el forense del arnés reconstruye, con el código, por
dónde pasa una llamada, quién la cuenta, quién la registra y dónde se puede medir o frenar. En curso además:
bajada por la API de los notebooks públicos y del foro al 2026-10-09.

### Línea independiente, forense del arnés: quién controla cada llamada (16:20 UTC)

Leyó el código del arnés y del marco y contó sobre las trazas; no ejecutó nada.

**Sus dos respuestas, copiadas tal cual.**
- «¿Quién controla cada llamada? Nadie la juzga: el servidor del modelo la convierte en llamada, el marco ADK
  la ejecuta descartando en silencio los argumentos que no reconoce, y el arnés solo comprueba un contador
  compartido, el reloj y los turnos. No existe, ni en el arnés ni en el marco, detector de repetición, de
  bucle, de resultado vacío, ni límite por herramienta o por subagente.»
- «¿Dónde se mide o se registra? Cada llamada queda solo en la traza por tarea, que vive en memoria y se
  escribe al terminar la tarea. El contador queda como un único número por tarea, y hoy nada escribe en vivo
  si la llamada contó, si era repetida o si un argumento fue ignorado.»

**Medido** (145 sesiones, 4 444 llamadas en traza, 4 086 contadas por el arnés; su modelo de conteo, sacado
del código, coincide con el contador en 145 de 145 sesiones): 1 822 llamadas contadas (45 %) caen en alguna de
cuatro clases de gasto sin avance: repetidas sin edición de por medio (1 438), lecturas con el argumento mal
formado (506, las 506 devueltas desde la línea 1), búsquedas vacías (300 de 300) y llamadas del subagente
(198). En 51 sesiones son más de la mitad de lo contado. 211 ediciones las rechaza el marco y no cuentan.
`BudgetExceeded` apareció 5 veces en 4 sesiones: seguir tras el tope fue raro.

**El camino de una llamada**, con archivo y línea en su informe: el servidor vLLM convierte el texto en
llamada (código no disponible: no se sabe si la comilla de más la pone el modelo o ese analizador); ADK no
valida los argumentos contra el esquema y `function_tool.py:172` descarta sin aviso toda clave que no
reconoce; el contador vive en `swegemma/context.py:467-550` y suma antes de ejecutar; no cuentan la entrega,
el estado, la llamada al subagente ni los rechazos; sí cuentan las llamadas del subagente, las fallidas y las
vacías; el aviso de presupuesto se pega a la respuesta cuando quedan 10 o menos; la traza se guarda al
terminar la tarea.

**Por qué la búsqueda devuelve vacío** (coincide con el auditor, por otra vía): no codifica texto; consulta
una tabla por nombre exacto de nodo. El índice sí está montado. `log.txt` tiene 600 avisos «Could not obtain
embedding» para las 300 llamadas: el aviso llegó a la consola y nunca al agente. La instrucción del envío
(`system.md:11`) y el propio arnés mandan usarla con palabras clave.

**Lo que no queda registrado en ningún sitio:** el texto crudo del modelo; los argumentos descartados; si una
llamada contó o era repetida, en vivo; ninguna llamada de la tarea en curso si la sesión muere; el motivo de
fin cuando hay parche. El registro nuevo del equipo engancha las peticiones al modelo, no las herramientas.

**Tres niveles.**
- Medir después: ya se puede, desde la traza (issue #171).
- Medir en vivo sin tocar al agente: posible y sin ejecutar. Un plugin del marco con retrollamadas de
  herramienta que siempre devuelvan `None`, añadido desde el notebook; ve los argumentos crudos antes del
  descarte, el autor y los rechazos. Debe tragarse sus errores y no tocar los argumentos. Prueba: el ensayo
  local con y sin el plugin, y que contador, turnos y traza sean idénticos.
- Frenar desde el zip: casi nada. Quitar herramientas de la lista es el único freno real. Las retrollamadas
  declaradas en el YAML no se rechazan: se ignoran en silencio. No hay campo de presupuesto.

**Advertencia suya que queda como regla:** los enganches del notebook propio deben medir, nunca frenar; un
freno ahí haría que las corridas propias dejaran de predecir la corrida que puntúa el organizador.

**Sin determinar:** quién pone la comilla en el nombre del argumento, y si la corrida de puntuación del
organizador usa la misma versión del arnés.

### Línea independiente, verificador limpio: medir con ZorzALL (16:40 UTC)

Trabajó con rescate propio (13:42 UTC, código 4 por los 145 logs por sesión de 0 bytes; los zips tienen el
mismo SHA-256 que los del rescate del día 8) y sin abrir la bitácora ni los informes de otros roles.

| Afirmación, dada sin cifras | Marca | Su medida |
|---|---|---|
| Una parte grande de las llamadas repite una anterior | Se sostiene con tope 40; se cae con tope 60 | 1 783 de 4 444 (40,1 %); 46,1 % con tope 40 y 9,4 % con tope 60 |
| Una búsqueda casi nunca devuelve resultado | Se sostiene, más fuerte | 300 de 300 vacías: nunca |
| Un subagente consume gran parte del tope sin resolver | Se sostiene, con 7 sesiones | 0 de 7 resueltas; mediana del 65 % del tope |
| Lecturas con argumento mal formado devuelven otra cosa | Se sostiene con tope 40; se cae con tope 60 | 507 de 1 371 lecturas; 505 devueltas desde la línea 1; 10 de 243 en las iteraciones 06 y 07 |
| Muchas no resueltas agotan el tope sin editar | Se sostiene por poco | 29 de 106 no resueltas sin ninguna edición ejecutada y al tope; 25 con parche de 0 bytes |
| Las resueltas usan muchas menos llamadas y casi no repiten | Se cae como está escrita | Mediana 21 contra 37; las resueltas sí repiten (mediana 3; solo 8 de 39 sin ninguna) |
| El arnés no cuenta algunas llamadas que la traza registra | Se sostiene, con cuadre exacto | 4 444 en traza, 4 086 contadas; la diferencia de 358 cuadra en 145 de 145 sesiones |

**Lo que el relato no había separado:** el tope fue de 40 llamadas y 4 minutos en las iteraciones 03 a 05 y de
60 llamadas y 4,5 minutos en la 06 y la 07, que además llevan el razonamiento encendido. El gasto sin avance es
de 51,9 % con tope 40 y de 14,5 % con tope 60. Es una comparación confundida (otras tareas, otro tope y el
razonamiento a la vez), pero dice que la condición con razonamiento casi no repite ni rompe el argumento de
lectura.

**¿ZorzALL mide el gasto sin avance? No, tal como está.** Sin avance, por su definición: 2 037 de 4 444
llamadas (45,8 %). El rasgo «observa» ve 172 de esas (8,4 %): solo cuenta una repetición si la llamada anterior
falló, y una búsqueda vacía, una lectura mal formada o una edición rechazada no son «fallo» para el instrumento.
La anatomía no guarda el autor, así que el subagente no aparece. «Espera» sí separa (50 sesiones lo incumplen,
2 resueltas), pero es una señal del final y no dice en qué se fue el gasto.

**La regla H-Z1 da «apoyada» y no es fiable:** 16 de 34 con perfil contra 22 de 85 sin perfil; pero 37
sesiones sin ninguna edición caen en «sin perfil» por construcción, y entre las 82 que editaron la diferencia
desaparece (16 de 32 contra 22 de 50; Fisher p = 0,65). El perfil cambia en 13 de 43 tareas entre dos pasadas
idénticas, mientras el resultado cambia en 2. «Observa» va al revés de lo esperado: lo cumplen 23 de 39
resueltas y 76 de 106 no resueltas, porque volver a correr un comando fallido después de editar es el ciclo
normal de probar.

**Tres defectos de medida del instrumento, sin tocar umbrales:** «espera» suma las llamadas de la traza y no
las que cuenta el arnés (cambia 9 sesiones); «acierta» cuenta como edición las 211 rechazadas (cambia 8);
«busca» toma como primera edición una que no se ejecutó (13 sesiones).

**Contadores que propone añadir**, sin tocar `umbrales.json`: contadas por el arnés, rechazadas sin ejecutar,
vacías, repetidas sin cambio, mal formadas, del subagente, ediciones ejecutadas y posición de la primera, y
llamadas tras el aviso de presupuesto (718 en 79 sesiones; de esas sesiones se resolvieron 8). Pasados al
implementador del issue #171. Corregir qué es «fallo» o qué cuenta como edición sería una versión 2 de ZorzALL,
que necesita la aprobación del dueño.

**Potencia, por su cuenta:** dos pasadas idénticas difieren en 2 de 43 tareas; con una pasada por brazo sobre
esas 43 tareas solo se distinguiría, ocho de cada diez veces, una mejora de unas 8 tareas.

**Coincidencia de las dos líneas independientes con el concilio**, sin haberse leído: las 300 búsquedas vacías,
el cuadre de 4 444 frente a 4 086, las 211 ediciones rechazadas, y cerca del 45 % de gasto sin avance (2 037
de 4 444 en traza; 1 822 de 4 086 contadas).

### Inteligencia pública: qué hacen los demás equipos (lectura del 2026-10-09, 17:30 UTC)

Leído en los archivos bajados hoy por la API (142 notebooks, 161 hilos del foro, tabla de 2 177 equipos).
Límite del material: de los 34 notebooks nuevos desde el día 4 solo hay log de ejecución, no código.

**Su respuesta en una línea, copiada:** «ningún notebook público declara una nota medida mayor que 0,18, y el
0,18 es una sola autodeclaración dentro del log de otro notebook. La parte alta de la tabla (0,20 a 0,24, 10
equipos) no tiene método público.»

**Tabla pública, en tareas de 58:** 14: 2 equipos; 13: 1; 12: 7; 11: 23; 10: 82; 9: 154; 8: 290 (nosotros,
puestos 270 a 559); 7: 393; 6: 359; 5: 283; 4: 181; 3: 140; 2: 77; 1: 50; 0: 135. Con un envío, el 10 % de los
equipos llega a 0,13 o más; con 5, el 32 %; con 10, el 53 %; con 14, el 77 %. El último salto de la tabla (de
150 a 269 equipos con 0,15 o más entre el día 8 y el 9) es una tanda de repuntuación: 214 equipos subieron y
ninguno bajó; coincide con el aviso fijado del organizador de que repuntúa los envíos que marcó «Kaggle Error»
tras más de 15 h de cola. Nuestro paso de «error» a 0,13 encaja en esa tanda (inferencia).

**Lo que hacen los que declaran más nota, con una lectura cada uno y ninguna medida por nosotros:**
- Familia «Budget-Fit» (el mismo paquete impreso en 8 logs; 0,18 por autodeclaración ajena): un solo agente,
  sin subagente ni herramientas de grafo, 28 llamadas, 8 minutos por tarea, 80 turnos, 240 s por orden;
  razonamiento encendido (inferido por el tamaño del archivo de muestreo). Su instrucción no está en disco.
- «v19» (0,17, dicho por su autor en el foro): analizador y programador, 100 llamadas, 7,5 minutos,
  razonamiento apagado. Sus otras versiones dieron 0,13, 0,08, 0,13, 0,13, 0,10 y 0,17.
- «0.13 Submission»: explorador de solo lectura y después programador, 60 llamadas, 5 minutos, sin la
  búsqueda por similitud; la instrucción manda una sola búsqueda acotada, primera edición mínima y «no
  vuelvas a buscar».
- Paquete más votado (0,12 y 0,15 con el mismo zip): reproduce antes de editar, comprueba la compilación tras
  cada edición, sin topes declarados.

**Lo que dice el organizador en el foro** (citas con número de hilo en el informe): el puntuador lee del
`eval_config.yaml` cuatro campos y solo esos (segundos por orden, llamadas, minutos, turnos); el valor por
defecto es sin límite; las tareas corren en serie con un tope global de 12 h para unas 120 tareas (públicas y
privadas en la misma corrida, con el arranque del servidor dentro); si se pasa de 12 h, el envío entero da
error. Sobre la lectura con el argumento mal formado: «Fix incoming» el 2026-09-30, sin versión confirmada. No
hay respuesta sobre qué versión del arnés usa hoy el puntuador.

**Lo que dicen participantes, sin notebook que lo respalde:** el razonamiento encendido resolvió de 48 a 51
de 129 tareas en local frente a 23 con él apagado (una corrida); bajar el tope de 50 a 25 llamadas costó 14
tareas en local; las herramientas de grafo no ayudan (21 búsquedas, 21 vacías; otro hilo, 140 de 142); el
mismo comando repetido hasta 69 veces; un mismo zip dio 0,12 y 0,15.

**Coincidencias con lo nuestro, halladas por otros sin conocernos:** la búsqueda vacía por nombre exacto, las
repeticiones, el ruido entre envíos idénticos, y que el analizador no aporta.

**Lo que no hemos probado y otros sí:** más minutos por tarea. Nuestro tope de 4 minutos y 40 llamadas es
nuestro, no del concurso: 12 h para unas 120 tareas dan unos 6 minutos de media por tarea, y los que declaran
más nota usan de 5 a 8. Nuestra condición con razonamiento, 60 llamadas y 4,5 minutos dio 0,08 y 0,13; la de
40 llamadas y 4 minutos, 0,06 y 0,05. Dos lecturas por variante: no refuta ni prueba.

**Lo que no se puede saber con lo público:** el método de los diez equipos con 0,20 o más; si algún envío
puntuado usa adaptadores; qué versión del arnés puntúa.

**Reglas que miró antes de proponer nada:** una sola cuenta por participante; datos externos solo si son
públicos y accesibles para todos sin costo; prohibido entregar los datos de la competencia a terceros. Nada de
lo adoptable usa red ni cómputo externo.

**Ronda 2, cómo se hizo:** expediente con los cuatro informes anonimizados (A a D) en
`C:\Users\herre\AppData\Local\Temp\concilio_42_ronda2\`; cada rol, reanudado con su contexto, responde qué
refuta de los otros con sus datos, qué retira, la pregunta del tope, y ordena once acciones candidatas (P1 a
P11). El auditor recibió la pregunta del dueño y el encargo de auditar el propio procedimiento.

### (Sección anterior, superada) Estado a las 05:35 UTC

**Hecho y verificado.** PR #153, #155, #157 y #158 fusionados. Issues #154 y #156 confirmados. Decisión de la
iteración 08 tomada (arriba). De las tres condiciones para subir, la primera (rescate que mira bytes) está en
`main`.

**En curso al escribir esto** (si la sesión se corta, muere y no deja informe):
- Segunda revisión de documentos del PR #163 (árbol `F:\Code\ALL-wt-azar`, commit `d929b25`).
- CI de `main` en `e6b8f66` (fusión del PR #161).

**Falta.**
- #160: confirmar el cierre cuando la CI de `main` termine en verde (comentario de evidencia, tarjeta en
  *Verificada*, Modelo usado Opus 5.5, Escaló No).
- #162: tras la segunda revisión, traer `main` a la rama (el `CHANGELOG` chocará), fusionar y confirmar; que
  un rol distinto del orquestador registre los desenlaces de las predicciones en el pre-registro.
- #164 a #167: sin empezar. Cada uno lleva predicción previa.
- Issue por abrir: fijar los episodios dentro de las pruebas de recall (tres pruebas dependen de los episodios
  reales y de un umbral al límite).
- (Hecho a las 01:20 UTC) #156 confirmado: CI de `main` en `d8b95f7` con 12 de 12 en verde, comentario de
  evidencia en el issue y tarjeta en *Verificada*.
- Guardián: el #159 tiene tarjeta desde las 00:25 UTC por orden del dueño y ahora salta por las reglas 2 y 3
  (tarjeta en *Done* sin estimación ni verificación). Falta decidir: ajustar las reglas para los «no
  planeados» o rellenar los campos.
- #160: los diez criterios, PR, revisión de código **y recuento de Datito**, fusión y confirmación. Toda
  corrección posterior a un dictamen vuelve al revisor antes de fusionar.
- Las predicciones fechadas de la iteración 08 (las escribe el concilio, antes de subir).
- En local y gratis: las 21 sesiones que QA no midió y la pasada del parche de referencia.
- Guardián del tablero: el #159 (duplicado erróneo, cerrado como «no planeado») salta por la regla 9 al no
  tener tarjeta. La regla no exceptúa los «no planeados»; decidir si se le pone tarjeta o se ajusta la regla.

**Pendiente del dueño.** Si el criterio exige siempre la prueba exacta además de los «6 pares». Y la orden de
subir: nada se sube a Kaggle sin ella.

**Para retomar.** `git worktree list`; `gh pr list`; leer esta sección; no relanzar un agente sin mirar antes
qué dejó el anterior en disco.

Nada se subió, se envió ni se contrató. Todo lo de esta sesión es local o de GitHub.


### Estado al cierre y cómo retomar (2026-10-09 16:10 UTC)

**Nada se subió ni se envió a Kaggle.** Todos los agentes de la sesión quedaron detenidos. Cierre pedido por el
dueño al terminar su jornada.

**Fusionado hoy en `main`:** PR #172 (episodio 073, lecciones de las vueltas 41 y 42) y PR #170 (regla del
guardián). Issue #169 confirmado (Verificada).

**Abierto, con lo que falta a cada uno:**
- **PR #175 / issue #173 (kit K «interfaz limpia»): cambios requeridos.** El kit está armado, compila y
  quedó registrado como `prepared`, no enviado. El revisor pide: (1) resolver el conflicto con `main` en
  `prediccion_de_fallos.md` para que corra la CI (hoy no tiene); (2) la comprobación lee el YAML con expresiones
  regulares y deja pasar diez formas que el compilador real acepta: cargar con PyYAML y un constructor
  `!include`, o fallar cerrado; (3) once falsos positivos; (4) seis huecos de prueba. Datito: la cifra «12
  carpetas, 0 errores» no se reproduce (la réplica pública da 1 error por una mención en negativo); K retira
  324 llamadas contadas (7,9 %); una pasada por brazo no distingue K de A. Predicciones 21 y 22 cumplidas, 23 y
  24 no.
- **PR #174 / issue #171 (vigía, cuenta por llamada, registro de hallazgos): entregado, sin revisar.** Falta
  `revisor-codigo` y Datito. Añade un gancho de inicio de sesión en `.claude/settings.json`: enseñárselo al
  dueño antes de fusionar. El implementador pide confirmar las razones con que sembró `hallazgos.json`.
- **Issue #164 (tope por tarea): a medias.** Rama `issue-164-tope-por-tarea`, árbol `F:\Code\ALL-wt-tope-tarea`,
  commit de código `2e57468`; sin confirmar quedaron `CHANGELOG.md`, `docs/ensayo_nucleo_jupyter.md` y el
  episodio 071. No hay PR ni informe final del implementador (se detuvo al cierre): leer el diff antes de seguir.
- Sin empezar: #165, #166, #167; issue de seguimiento de las observaciones no bloqueantes del PR #170; marcar
  en el pre-registro los desenlaces de las predicciones 13 a 16 y 21 a 24; actualizar la skill
  `concilio-de-experimento` con los seis cambios del auditor.

**Decisiones vigentes:** iteración 08 sin cambios (base A más el brazo que enciende solo el razonamiento);
kit K se juzga por criterio mecánico; el tiempo por tarea vuelve al concilio con revisión cruzada (los que
declaran más nota usan de 5 a 8 minutos; el presupuesto real es de unos 6); la sonda de CPU
`cs4all/sonda-nucleo-08` espera solo la palabra del dueño.

**Hechos de hoy:** 8 tareas de 58 (0,13), puestos 270 a 559 de 2 177; cuota de GPU repuesta el 2026-10-10
00:00 UTC.

**Regla nueva de operación:** no correr suites completas ni varios agentes pesados en paralelo en el equipo del
dueño: hoy saturaron la memoria y contaminaron un diagnóstico. La suite completa se lee en la CI.

**Fuera de Kaggle, el mismo día:** caso forense `D:\SandboxConfigs\SandboxTransfer\DFIR_IA_STREAM_20261009_124500`
(respuestas de IA que no cargan en el navegador), skill de usuario `forense-endpoint` y limpieza del equipo
autorizada por el dueño. Pendiente de él: reiniciar y repetir la consulta.

**Cómo retomar:** `python -m scripts.devlog board --since 150`; corregir el PR #175; revisar el #174 con los dos
roles, de a uno; leer el diff del #164 y terminarlo.


### Estado al cierre y cómo retomar (2026-10-09 17:10 UTC)

Sustituye al cierre de las 16:10 UTC: el dueño pidió seguir con lo pendiente. **Nada se subió ni se envió a
Kaggle.**

**En `main` hoy:** PR #172 (episodio 073), #170 (guardián; issue #169 confirmado) y #175 (kit K y comprobación
de la instrucción; issue #173 confirmado, `mergedAt` 16:28:30Z, commit `8ed4763`).

**Kit K «interfaz limpia»:** registrado como `sub-004`, `prepared`, no enviado. SHA-256 `3346af0e…c8b1`. Es el
kit A sin subagente, sin las tres herramientas de grafo y sin la línea que ordenaba la búsqueda. Retira 324
llamadas contadas de 4 086 (7,9 %; mediana 1 por sesión). Una pasada por brazo no distingue K de A (diferencia
mínima detectable de 30 a 56 puntos). Seguimiento: issue #177 (la opción `--permitir-mencion` puede tapar una
orden real).

**PR #174 / issue #171 (vigía, cuenta por llamada, registro de hallazgos):** segunda revisión de código,
«aprobado con observaciones no bloqueantes»; CI de `605e3ba` 12 de 12. Corrigió: el vigía podía imprimir el
token con un salto de línea interior; un rescate incompleto apagaba el aviso; 13 contadores sin prueba. Falta
el recuento de Datito (en curso) y **que el dueño vea el gancho de `SessionStart`** que añade a
`.claude/settings.json` (una orden: `python "$CLAUDE_PROJECT_DIR/scripts/kaggle_vigia.py"`, tope 30 s; solo
lee). Tras fusionar #175 la rama vuelve a chocar con `main` en el pre-registro y el `CHANGELOG`: fusionar
`main` conservando su sección 12.

**PR #176 / issue #164 (tope por tarea):** primera revisión, «cambios requeridos» y «no listo para lanzar»;
corregido en `43c93ca` sin tocar el texto del notebook (p1 `30aa9b31…`, p2 `0351fd80…`, sin repetir ensayo);
segunda revisión en curso; falta Datito. Medido: el tope corta a 90,0 y 900,0 s; vaciar el mapa de hilos
quita la carrera en la sonda (60 de 1 500 frente a 0 de 1 500); 20 de 26 corridas pasan su validación; tarea
legítima más larga con tope 900: 269,1 s.

**Condiciones de lanzamiento de la iteración 08, escritas en `ensayo_nucleo_jupyter.md`:** PR #176 fusionado
con CI en verde; ensayo repetido con la versión de `ipykernel` de Kaggle (sin medir); el análisis de p1 contra
p2 debe excluir los pares con `par_faltante` (no existe guion versionado que compare las dos pasadas); primera
subida en serie; orden del dueño con la orden a la vista; cuota de al menos 14,6 h.

**Para el concilio de la próxima vuelta, con revisión cruzada:** tiempo por tarea (los que declaran más nota
usan de 5 a 8 minutos; presupuesto real de unos 6); no hay tope al total de tareas colgadas, solo a dos
seguidas; el margen de 30 s tras el corte queda justo.

**PR #178:** desenlaces de las predicciones 13 a 16 y 21 a 24 (seis de ocho ocurrieron); en revisión de
documentos.

**Sin empezar:** #165, #166, #167, #177; seguimiento de las observaciones no bloqueantes de los PR #170 y
#174; cambios de la skill del concilio.

**Operación:** suites completas y mutaciones solo en la CI; agentes de a pocos, con esa restricción en el
encargo.

**Cómo retomar:** leer los informes pendientes (segunda revisión del #176, Datito del #174, revisor del #178);
fusionar `main` en las ramas de #174 y #176 antes de fusionarlas; pasar #176 por Datito; enseñar el gancho al
dueño.


### Estado al cierre y cómo retomar (2026-10-09 17:40 UTC)

Sustituye a los cierres anteriores del día. **Nada se subió ni se envió a Kaggle.** Ningún agente ni proceso
queda corriendo. No queda ningún PR abierto de esta jornada.

**En `main` (cabeza `acc9a0a`):**
- #172: episodio 073, lecciones de las vueltas 41 y 42.
- #170: el guardián exime al issue cerrado sin trabajo (#169 confirmado).
- #175: kit K «interfaz limpia», `sub-004`, `prepared`, no enviado, y la comprobación de que la instrucción no
  ordena herramientas ausentes (#173 confirmado).
- #178: desenlaces de las predicciones 13 a 16 y 21 a 24 (seis de ocho ocurrieron).
- #176: tope de 900 s por tarea, vaciado del mapa de hilos, códigos 6 y 7 del diagnóstico (#164 confirmado).
- #174: vigía de envíos al iniciar sesión, cuenta por llamada, registro de hallazgos con 19 filas
  (#171 confirmado). El gancho de `SessionStart` lo aprobó el dueño. Ejecutado a mano tras fusionar: «envíos
  sin cambios desde esa lectura» y siete hallazgos que siguen en `medido`.

**Abiertos, con estimación:** #177 (la opción `--permitir-mencion`), #179 (seguimiento del vigía y del tope:
doce puntos, entre ellos el guion que compare las dos pasadas excluyendo pares faltantes, y probar el gancho
en un arranque real), #165, #166, #167.

**La iteración 08 no está lista para lanzar.** Condiciones, en `ensayo_nucleo_jupyter.md`: ensayo repetido
con la versión de `ipykernel` de Kaggle (sin medir); análisis de p1 contra p2 que excluya los pares con
`par_faltante` (#179, punto 11); primera subida en serie; orden del dueño con la orden a la vista; cuota de
al menos 14,6 h. Notebooks armados: p1 `30aa9b31…14fa`, p2 `0351fd80…14c5`.

**Para el concilio de la próxima vuelta, con revisión cruzada** (el dueño: «cada duda debes resolverla en loop
junto al concilio»): tiempo por tarea (los que declaran más nota usan de 5 a 8 minutos; presupuesto real de
unos 6; el tope propio es de 4); tope al total de tareas colgadas (hoy solo dos seguidas; con colgadas
alternas se irían unas 2 de las 2,5 h, por aritmética); margen de 30 s tras el corte; si `hallazgos.json`
cuenta como «cuenta por llamada» para la predicción 19; y los siete hallazgos que el vigía lista en `medido`:
cada uno pasa a decidido o descartado, o se dice por qué sigue abierto.

**Predicciones sin marcar en el pre-registro:** 7 a 12 (#164) y 17 a 20 (#171). Datos: 17, 18 y 20
ocurrieron; 19 pendiente del concilio; 7 a 12 sin recontar (el analista no llegó a ese punto).

**Repositorio:** los archivos sueltos de la raíz pasaron a `.scratch/` (ignorada), con un `LEEME.md`. Quedan
sin versionar `.codex/` y un borrador del manuscrito.

**Operación:** suite completa y mutaciones solo en la CI; pocos agentes a la vez. Tras cada fusión, las ramas
abiertas chocan en `CHANGELOG.md` y en el pre-registro: fusionar `main` y conservar los dos lados.

**Cómo retomar:** al abrir sesión el vigía dirá si algún envío cambió. Después, `python -m scripts.devlog
board --since 150`; convocar el concilio con las cinco dudas de arriba; #179.


**Lectura final por la API, 2026-10-09 17:41 UTC** (rescate `2026-10-09T1741Z`, salida 4 por los logs por
sesión de 0 bytes ya conocidos). Envíos: los mismos cuatro, sin cambios de estado ni de nota desde las 13:42
(0,13, 0,08, 0,05 y 0,06; el último es del 2026-10-07 16:25). Ningún envío nuevo. Notebooks propios: 15; la
última ejecución es la de `iteracion-07`, del 2026-10-07 16:48: hoy no corrió ninguno. Tabla pública: 2 188
equipos (eran 2 177); CS4ALL en el puesto oficial 544 con 0,13 (8 tareas de 58) y 4 envíos; 277 equipos con
más nota (eran 269) y 293 empatados (puestos 278 a 570). Máximo 0,24 y mediana 0,10, sin cambio. En cuatro
horas, sin enviar nada, ocho equipos más nos pasaron y el puesto oficial bajó de 540 a 544.


**Cierre definitivo del 2026-10-09 (18:20 UTC).** PR #181 fusionado (issue #180 confirmado): el manuscrito, en
castellano y en inglés, añade como nota posterior a su fecha de corte el segundo par de envíos del mismo
archivo, 0,08 y 0,13; los PDF no se regeneraron. Texto para LinkedIn revisado por el redactor y por el
validador estadístico, guardado en `.scratch\linkedin_2026-10-09_final.md`: **no se publicó**; lo publica el
dueño. Dos correcciones del validador a lo dicho durante el día: (1) los 293 equipos con 0,13 no están
«empatados»: tienen puestos del 278 al 570 y la nota está truncada; (2) el reenvío no llevaba «dos días
puntuado»: el 2026-10-08 22:31 UTC seguía en error y recibió la nota en las 15 horas siguientes; corregido con
un comentario en el #171 y anotado en el #179 para el episodio 073. Enlaces: tabla
`https://www.kaggle.com/competitions/gemma-4-developer-agent/leaderboard`, envíos `…/submissions`.


## Vuelta 43 — 2026-10-09, desde las 21:45 UTC

**Pregunta de la vuelta** (del dueño): «retomar dónde quedaste la última vez, revisa el detalle de toda la
información documental, y foco junto al concilio de seguir mejorando».

**Nada se subió, se envió ni se contrató.** La vuelta no baja datos nuevos: usa el rescate `2026-10-09T1741Z`.
Lecturas del orquestador por la API a las 21:55 UTC: los mismos cuatro envíos, sin cambio de estado ni de
nota (0,13, 0,08, 0,05 y 0,06); cuota de GPU, 29,53 h usadas de 30,00, con reposición el 2026-10-10 a las
00:00 UTC. Recall anotado: sin lecciones propias de la pregunta; los issues parecidos que devolvió son #171,
#164 y el episodio de las vueltas 41 y 42.

**Leído antes de convocar:** la memoria de reanudación, la vuelta 42 entera y sus tres cierres, los issues
#177 y #179, la skill del concilio, `hallazgos.json`, el pre-registro de predicciones y
`ensayo_nucleo_jupyter.md` (topes, ramas del corte, condiciones de lanzamiento y límites).

**Convocatoria.** La misma pregunta para los cinco roles, sin conclusiones ni cifras del orquestador
(`…\instrumentos\concilio_43\encargo.md`): P0, cuál es el siguiente paso con más respaldo para subir la
nota y qué hacer con la cuota semanal y con el envío diario; y siete dudas (D1 los cuatro campos de
`eval_config.yaml`; D2 tope al total de colgadas; D3 margen tras el corte y ventana final; D4 predicción 19;
D5 los siete hallazgos en `medido`; D6 si la iteración 08 sigue siendo el mejor primer uso de la cuota; D7 la
pregunta obvia que nadie contesta). El auditor del método entra después de la ronda 2.

**Incidente de la ronda 1.** A las 22:12 UTC tres roles (analista, forense y QA) se cortaron a la vez por un
fallo de conexión del equipo, no por su trabajo. El forense ya había dejado su informe completo en disco; los
otros dos se reanudaron con su contexto y entregaron a las 23:00 y 23:05 UTC. Los cinco informes pasan del
tope de 900 palabras del encargo. Informes completos y guiones: `…\instrumentos\concilio_43\<rol>\`.

**Reparto con otra sesión.** La sesión `maci-6a`, con el mismo encargo del dueño, pone al día el README del
caso, el registro de pruebas y el recorrido; esta sesión lleva el concilio, el repositorio y esta bitácora.
Su medición de la tabla pública entró a la ronda 2 como informe F, sin firma y marcada «sin recontar».

### Primer paso que propone cada rol en la ronda 1, copiado tal cual

**Forense del arnés:**

1. Siguiente paso: enviar el kit K con su `eval_config.yaml` intacto (un envío, 0 h de cuota), y antes leer la versión de `ipykernel` de Kaggle con la sonda de CPU ya armada (0 h de GPU).
2. Por qué: en las 131 filas propias de la condición A el tope que corta es el de llamadas (46 filas, 31 sin parche), no el de tiempo (7); el peor caso de reloj lo fija `max_time_minutes`, y con 4 min quedan unas 2 h de holgura bajo las 12 h.
3. Lo refutaría: que el organizador corra más lento que nuestras sesiones (no medido: ningún rescate guarda la duración de un envío) o que K sin grafos pase a agotar el tiempo.

**Analista de datos:**

1. Siguiente paso: gastar la cuota nueva en medir la condicion I (la de mejor nota en la tabla: 5 y 8 de 58, frente a 3 y 4 de A) sobre tareas sorteadas sin elegir, antes que repetir A. La duracion media de I (246 s) sale de tareas elegidas y de ella dependen el tope de D1 y el riesgo del limite global. Orden: I sobre el sorteo de 60 (unas 4,6 h de reloj, 2 sesiones, unas 10 h de cuota), luego A sobre las mismas 60 (2,0 h de reloj, unas 4,5 h de cuota). El envio diario va a repetir el zip mejor, no a probar cambios pequenos.
2. Por que: es el unico cambio con senal en el mismo sentido en tabla y en local (3 tareas de fastapi pasan de 0/3 a 2/2; en rich no gana y pierde una). Ningun diseno detecta menos de 6 a 8 tareas.
3. Lo refutaria: media de I sobre tareas sin elegir mayor de 300 s (mas de 10 h en 120 tareas), I no mejor que A sobre las mismas tareas, o un nuevo «system error» sin relacion con el tiempo.

**Inteligencia pública:**

1. Paso: usar el envío diario en el kit I (razonamiento encendido) cambiando timeout_seconds de 60 a 240 y subiendo max_time_minutes solo hasta donde el tiempo medio por tarea, leído de logs ya bajados, lo permita; la cuota nueva, a la iteración 08 solo si D6 se cumple.
2. Por qué: una lectura tiene ruido de 2 a 3 tareas, así que un envío aislado no separa nada. Lo público respalda (a) razonamiento encendido y (b) más de 4 minutos, ambos declarados por otros en corridas únicas. Nuestro timeout_seconds de 60 es además el valor que el código 0.2.7 aplica a la verificación del parche.
3. Lo refutaría: que el tiempo medio por tarea con razonamiento y tope de 6 a 8 minutos pase de unos 5 minutos (se pasa de 12 h), o que dos envíos del kit cambiado no se separen de los dos del kit I (0,08 y 0,13).

**QA de trayectorias:**

Siguiente paso con más respaldo en trayectorias: razonamiento encendido con 60/4,5 y limpiar la interfaz (argumentos, sintaxis) antes de tocar topes. Por qué: en las 19 tareas comunes resuelven 18 de 29 sesiones encendidas contra 20 de 57 apagadas, y los argumentos mal formados bajan de 44 % a 4 % de las lecturas (comparación confundida por tres cambios). Lo refutaría: un brazo sin razonamiento con interfaz limpia (kit K) que llegue a 0,5 o más de resueltas en esas 19 tareas, o un brazo con razonamiento y 40/4 que no pase de 0,35.

**Arquitecto de IA:**

1. Siguiente paso: la pasada 1 de la iteración 08, sola y en serie (hasta 5,0 h de cuota); después la pasada 2 y, tercero, el brazo «solo razonamiento encendido» con los mismos topes.
2. Por qué: es la única comparación que separa «razona mejor» de «tuvo más presupuesto»; hoy tareas, llamadas, minutos y razonamiento cambian juntos.
3. Lo refutaría: que la pasada 1 no complete 60 tareas en sus 7 200 s (media por tarea sobre 120 s), o que el montaje por tarea del puntuador pase de unos 30 s.

### Parecer de forense del arnés, copiado tal cual

1. El archivo de topes del envío no lo lee el código que tenemos; lo lee un guion del organizador que no está en disco.
2. El organizador escribió que lee cuatro campos y solo esos, y que corre las tareas una tras otra.
3. Con el kit A, lo que corta las tareas es el tope de 40 llamadas, no los 4 minutos.
4. Cuando se acaba el tiempo o las llamadas, lo editado en disco se entrega igual como parche.
5. Con 4 minutos por tarea, el peor caso medido da unas 10 horas para 120 tareas; el límite es 12.
6. No sabemos cuánto tardó ninguno de nuestros envíos.
7. Dos envíos marcados con error terminaron con nota sin que hiciéramos nada: un estado no es un desenlace.
8. El mismo archivo sacó 0,08 y 0,13: un solo envío por kit no distingue kits.
9. La iteración 08 está armada con el kit A, no con el K.
10. La versión de `ipykernel` de Kaggle sigue sin leerse; hay una sonda sin GPU lista para leerla.

### Parecer de analista de datos, copiado tal cual

1. Las cifras de duracion y llamadas se reproducen desde los archivos crudos (4 086, 4 444, 145 sesiones).
2. Con 4 min y 40 llamadas, un tercio de las sesiones se acaba por llamadas y ninguna de esas se resuelve.
3. Con razonamiento cada llamada tarda tres veces mas y manda el tiempo: un tercio termina por tiempo.
4. Evaluar 120 tareas con razonamiento ocuparia de 8 a 10 horas; 6 minutos o mas puede pasar las 12.
5. Los dos envios con razonamiento dieron error de sistema al principio y los otros dos no; no sabemos si fue el tiempo.
6. Un envio solo distingue diferencias de 6 a 9 tareas; mejoras de 1 o 2 tareas no se ven.
7. La tabla premia reintentar: mas envios, mejor nota, sin que el agente mejore.
8. La iteracion 08 tal como esta mide ruido de A, no un cambio; conviene medir antes la condicion con razonamiento.
9. Las ediciones que el marco rechaza (57 % de las ediciones) estan en 11 sesiones: arreglarlas vale a lo sumo una tarea de 58.
10. Falta la duracion real en la maquina del organizador y la media de la condicion con razonamiento sin tareas elegidas.

### Parecer de inteligencia pública, copiado tal cual

1. Una nota sola no vale: el mismo zip dio 0,08 y 0,13.
2. La tabla muestra la mejor nota de cada equipo y nunca baja.
3. Quien envía más puntúa más, y el ruido casi basta para explicarlo.
4. El organizador confirmó cuatro campos y que no hay tope por defecto.
5. Nuestros 60 s por orden son lo más bajo de lo público y pueden cortar la verificación.
6. Hay un límite nuevo de envíos pendientes.
7. La versión que puntúa sigue sin respuesta.
8. Elegir finales por la nota pública máxima es mala idea.

### Parecer de QA de trayectorias, copiado tal cual

1. En 145 sesiones, 21 se cortaron por tope.
2. Sin razonamiento, 9 de 10 cortes giraban en bucles; más tiempo no los habría salvado.
3. Con razonamiento el tiempo sí aprieta, y 4 de 11 cortes avanzaban.
4. Las llamadas nunca son el límite con tope 60.
5. Los argumentos mal formados son 44 % sin razonamiento y 4 % con él.
6. Cuatro entregas rotas de sintaxis, todas sin razonamiento y sin ejecutar nada tras editar.
7. Tras compactar, el enunciado literal desaparece siempre.
8. No se puede decir si la mejora viene del razonamiento o de los topes.
9. Falta medir el límite global y la iteración 08; no los vi.

### Parecer de arquitecto de IA, copiado tal cual

1. El kit A usa unas 4 de las 12 horas; el kit con razonamiento, unas 8,5.
2. Con razonamiento, 16 de 29 tareas se cortan por tiempo y ninguna por llamadas.
3. El modelo escribe 34 tokens por segundo: un minuto son unos 2 000 tokens.
4. Defiendo hasta 4,5 minutos por tarea; con 5, el peor caso da 12,0 horas, sin margen.
5. Pasar las 12 horas da error del envío entero, según el organizador; el arreglo no está confirmado.
6. El montaje por tarea del puntuador no está medido.
7. El notebook propio difiere del puntuador en compactación, memoria y sandbox.
8. Las dos pasadas de la 08 cuestan hasta 10 horas de cuota; con el brazo de razonamiento, unas 20.
9. Una tarea colgada puede dejar una pasada sin sus 60 tareas.
10. No cambiaría el notebook armado.

### Ronda 2: revisión cruzada (2026-10-09, 23:08 a 23:40 UTC)

Expediente con seis informes sin firma (A forense, B analista, C inteligencia pública, D QA, E arquitecto;
F, la medición de la tabla pública que llegó de la sesión `maci-6a`) en `…\instrumentos\concilio_43\ronda2\`.
Cada rol, reanudado con su contexto, respondió con formato fijo: qué mide bien cada otro informe, qué refuta
con su número, qué se le pasó, qué retira, ocho puntos donde los informes no cuadraban, vetos y orden final de
dieciséis candidatas (C1 a C16, listadas en `encargo_ronda2.md`). Los órdenes no se promedian. Las cinco
respuestas pasan del tope de 600 palabras. Lo que sigue está copiado tal cual de cada `ronda2.md`.

**Forense del arnés (informe A). Qué retira:**

Mi primer paso (enviar K): K no razona y parte de la base más baja; un envío no lo separa de A. Retiro también «46 de 131» como cifra de decisión: mezcla iteraciones 01 y 02.

**Vetos:**

- C8: a 5 min el peor caso es 10,8 a 12,0 h (B, E) y pasar las 12 h anula el envío entero.
- C13: ningún dato pide otros márgenes e invalida el ensayo.

**Orden final:**

1. C11
2. C15
3. C9 (orden del dueño; el mismo día que 4)
4. C4, que sigue como C7 cuando haya segundo zip
5. C10
6. C1, solo la pasada 1: base de A en las 60 tareas y estreno de los enganches con el brazo barato (hasta 5 h)
7. C2 (es C14 con el kit de razonamiento; unas 10 h)
8. C3 (unas 10 h; total de cuota, 25 de 30)
9. C16, como segundo zip de C7

Fuera: la pasada 2 de C1, C5, C6, C12.

**Analista de datos (informe B). Qué retira:**

- «El unico cambio con senal en tabla y en local» (P0 de B): I contra A tiene Fisher 0,24; las tareas de I fueron elegidas; los dos zips I fueron repuntuados tras error de sistema. Queda como hipotesis.
- Que repetir el zip I sea el uso del envio diario: sube el maximo publico, no la privada (F).

**Vetos:**

- C8 (subir minutos): peor caso 11,8 h a 5,5 min y 12,8 h a 6 (E: 12,0 h a 5 con carga de 1 142 s). Sin media de I sin elegir, no.
- C12 y C16 (kits nuevos): techo 1 tarea de 58, indetectable.
- C14 (rearmar 08 con K): K contra A no se detecta; obliga a repetir el ensayo.
- C13: solo si se rearma por otra causa.
- C5 (K al envio diario): sin potencia.

**Orden final:**

1. C10 (local, mismo dia que la subida)
2. C11 (local)
3. C15 (regla, local)
4. C1 (cuota, pasada 1) junto con C4 el mismo dia (envio: el zip I, control)
5. C2 (tras construir y ensayar el notebook)
6. C3
7. C7 con C6 (alternar I e I con timeout_seconds 240, una variable)

Fuera: C5, C8, C9 (la pasada 1 ya lee la version, segun E), C12, C13, C14, C16.

**Inteligencia pública (informe C). Qué retira:**

- «Casi basta el ruido» (D7 y parecer 3). F tiene razón: la varianza con 1 envío es 6,9 frente a 3,8 binomial (mi recuento, redondeando; F da 6,84), hay 135 ceros y 122 con 10 o más. Hay heterogeneidad de equipos.
- «`timeout_seconds` es lo que aplica la verificación del puntuador» pasa a hipótesis. Nota: el organizador dijo el 10-07 que la validación «generally shouldn't timeout», sin ligarlo a esa pregunta.
- La prioridad de C6 como primer paso.

**Vetos:**

- C8 por encima de 5 min: el peor caso de E llega a 12,0 h sin margen.
- C15 no es veto, pero C4 como único plan: 54 envíos de un mismo zip suben la nota pública y no la privada (F, supuestos sin verificar).
- C9 sin orden del dueño.

**Orden final:**

1. C11 (registro, hora de estado, límite de pendientes; local)
2. C15 (regla de finales por varias lecturas)
3. C4 (envío diario, mismo día que lo que haga la cuota)
4. C14 o C2 (el notebook del kit que se quiere enviar, tras ensayo local)
5. C7 (alternar dos zips con calendario)
6. C5
Fuera: C1 tal como está, C6, C8, C13, C16, C12 y C3 hasta tener C14. C9 y C10 si el dueño decide.

**QA de trayectorias (informe D). Qué retira:**

- Mi «decidido» para `argumento_mal_formado`: pasa a abierto. No separé interfaz de razonamiento, y el techo en tareas es pequeño (B).
- Mi P0 como paso único: era «razonamiento más interfaz limpia», dos cambios juntos. No se sostiene sin C3.
- Mi «4 sintaxis rotas» es cota inferior: 66 archivos no se pudieron verificar.

**Vetos:**

- C1 como primer uso: A ya tiene 116 sesiones y 9 de 10 cortes son bucles; añade ruido, no causa.
- C8: sin dato mío a favor. El peor caso con 5 min es 10,8 h (B) o 12,0 h (E).
- C12 como kit aislado: con razonamiento 0 de 20 parches rotos; el techo es 4 de 116 sin razonamiento.
- C6 sin aislar: mezclaría un campo no medido con el kit de razonamiento.

**Orden final:**

1. C3 (cuota, notebook; separa razonamiento de topes sobre las 19 tareas comunes).
2. C5 (envío del mismo día que C3, 0 cuota).
3. C16 (interfaz limpia más razonamiento).
4. C4.
5. C10.
6. C11.
7. C15.
Fuera: C1, C2, C6, C7, C8, C9, C12, C13, C14.

**Arquitecto de IA (informe E). Qué retira:**

- «12 al tope de llamadas»: conté 40 o más y el tope ata en 39. Vale 39 de 116.
- «16 se cortan por tiempo»: son 16 sobre 270 s de reloj con montaje; cortadas por mensaje, 10 (B, D).
- El factor 2 para planificar: uso el 2,25 de B, que no reconté. Una pasada, hasta 5,6 h; las dos, 11,3 h.
- La pasada 2 como segundo paso.

**Vetos:**

- C8: a 5 min el peor caso es 12,0 h y pasarse da error del envío entero.
- C13 y C14 antes de la pasada 1: invalidan el ensayo y hoy no hay Docker.
- C16: dos cambios a la vez, sin corrida propia.
- C6: un campo no medido en el puntuador, con ruido de 2 tareas por envío.

**Orden final:**

1. C11
2. C15
3. C9
4. C1 (solo la pasada 1), el mismo día que C4
5. C4
6. C10
7. C3 (unas 11 h; con la pasada 1, unas 17 de 24)
8. C7, cuando C3 dé un candidato

Fuera: C2 (difiere de C3 en 30 s y cambia tres cosas), la pasada 2 de C1, C5, C12 y las vetadas.

### Parecer del auditor del método (presidente, con la ronda 2 a la vista), copiado tal cual

Entregado el 2026-10-10 a las 00:10 UTC. Recontó con código propio desde los 12 zips, la tabla pública y los
envíos. No escribió su archivo de informe; el orquestador lo guardó desde su respuesta, sin cambios de
contenido, en `concilio_43/auditor/informe.md` (carpeta de instrumentos, ignorada por git), junto a sus guiones.

1. Las cifras de duración y de la tabla se reproducen.
2. Con tope 40, 41 de 116 sesiones acaban empujadas por el tope; solo 2 por corte duro.
3. Con razonamiento, 10 de 29 se cortan por tiempo.
4. Cinco minutos por tarea deja el peor caso entre 11 y 12,4 horas: vetado.
5. El factor de cuota medido es 2,0; 2,25 es un techo.
6. Las 14,6 horas no tienen derivación.
7. Una colgada deja la pasada sin sus 60 tareas.
8. Nuestra verificación local corta a 60 s en 16 sesiones de un repositorio.
9. Reenviar sube la nota pública, no la privada.
10. La cuota elige al candidato; los envíos lo confirman.
11. Faltan las predicciones fechadas antes de subir.
12. Siete hallazgos: cuatro decididos, dos descartados, uno abierto.

**Lo que recontó y corrigió, copiado tal cual:**

Universo: 12 zips de `iteracion-03` a `-07`, 145 filas (116 sin razonamiento, 29 con él).

| Cifra | Marca | Número del auditor |
|---|---|---|
| Sin razonamiento, fin por tope de llamadas | Cuatro definiciones | 2 por mensaje del arnés; 12 con contador 40; 41 con 39 o más (2 resueltas); 39 con 39 o más y no resueltas |
| «15, cuenta de trazas» (inteligencia) | Refutada | 15 = 12 sin razonamiento + 3 con tope 60; el contador es del arnés |
| «46 de 131» (forense) | No recontada | mezcla iteraciones 01 y 02 |
| Con razonamiento, fin por tiempo | Confirmada | 10 por mensaje, 1 por contexto; 16 duran 270 s o más, 6 de ellas resueltas |
| Duración por tarea | Confirmada | 109,4 s (mediana 95,2; máx. 303,6) y 245,9 s (mediana 276,2; máx. 294,8) |
| 120 tareas, media | Confirmada | 3,65 h y 8,20 h |
| 120 tareas, peor caso con carga de 1 142 s | Corregida a rango | 4 min: 9,1 a 10,4 h; 4,5: 10,1 a 11,4; 5: 11,1 a 12,4 |
| Código 124 en la verificación local | Corregida (analista: 5) | 16 de 116, todas en un grupo de repositorio (16 de 26); 3 sin parche; 0 de 29 con razonamiento |
| Parche vacío | Confirmada | 37 (32 y 5), 0 resueltas |
| Factor 2,25 | Cota superior | 29,53/13,14 se reproduce, pero el reloj solo suma la última versión de cada notebook; el analista escribió «mínimo», y es al revés |
| Factor 2,00 | Vale para estimar | bitácora 2419, lectura a ambos lados de una sesión |
| 14,6 h | No reproducible | bitácora 2913, sin derivación; el propio documento dice «no se comprobó» |
| Informe F | Confirmado | 2 188 equipos, 9 526 envíos, 511 con un envío (media 4,19; varianza 6,84 contra 3,89), 122 con 10 o más, 135 con cero; Fisher 0,242 |
| F, diferencia detectable | Corregida, F es prudente | 5 envíos por zip, 4,3 tareas; 10, 3,0; 27, 1,8 (normal, dos colas) |
| Holgura de una pasada | Arquitecto confirmado | manda `TOPE_SEGUNDOS = 7200` desde el inicio de tareas (celda 10); el tope de sesión solo ata si la carga pasa de 1 200 s; holgura 360 a 1 260 s; una colgada cuesta 930 s |

- **Cuál vale para D1:** 41 de 116. El código deja pasar 40 llamadas y rechaza la 41; el histograma tiene 29
  filas en 39 frente a 2 a 8 en cada valor de 31 a 38. Mide cuántas sesiones acaban empujadas por el tope, no
  que más llamadas resuelvan.
- **No recontó:** sintaxis rota, las 58 sin fuente, los 46 de las trazas (su conteo de trazas falló).

**Los siete hallazgos, copiado tal cual:**

1. `argumento_mal_formado`: **decidido**. «Sin kit ni envío propio; se recuenta en C3.»
2. `aviso_de_presupuesto_en_la_llamada_30`: **decidido**. «No actuar: 41 de 116 acaban en 39 a 40 llamadas y 2
   resuelven; con razonamiento, máximo 53 de 60.»
3. `ruido_entre_dos_envios_del_mismo_zip`: **decidido**. «Ninguna nota única decide; comparar zips pide 5
   envíos por zip; finales por media.»
4. `sesiones_sin_edicion_de_fuente`: **descartado**. Es consecuencia, no palanca; 0 resueltas en las tres
   definiciones.
5. `compactacion_del_contexto`: **abierto**. Falta el intervalo del puntuador (5 o 15); lectura local.
6. `minutos_por_tarea_frente_al_presupuesto`: **decidido**. «4 y 4,5 no se suben; 5 o más, vetado; se revisa
   con C3.»
7. `sintaxis_rota_por_comillas_escapadas`: **descartado** como palanca (techo 4 de 116, 0 de 20 con
   razonamiento); cifra de QA.

Nuevos al registro: verificación local cortada a 60 s; el tope de 7 200 s fija la holgura; límite de envíos
pendientes; la tabla guarda el máximo.

**Vetos, copiado tal cual:**

- **C8:** peor caso de 11,1 a 12,4 h.
- **C13 y C14:** sin dato, e invalidan el ensayo.
- **C5:** un envío no separa K de A.
- **C12:** techo de una tarea.
- **C2:** tres variables; lo desplaza C3.
- **C6 y C16:** aplazadas, no vetadas. Hoy serían exploratorias.

**Plan, copiado tal cual:**

**Local, sin preguntar:** C11, antes de cualquier envío; C10; C15; predicciones fechadas de la 08; armar y
ensayar el notebook de C3; reverificación a 240 s.

**Lo decide el dueño:**
1. **C9** (0 h de GPU). Después, ensayo local con esa versión.
2. **C4:** reenviar el zip con razonamiento hasta 5 lecturas (3 envíos, hacia el 13-10). Abandono: dos errores
   sin repuntuar.
3. **Pasada 1** (5,0 a 5,6 h). Abandono: una colgada, menos de 55 tareas o registros de 0 bytes.
4. **Pasada 2** (igual). Abandono de C3: más de 6 discordantes de 60.
5. **C3** (10 a 11,3 h; total 22,5 de 30). Decide: 6 pares netos a favor y McNemar de 0,05 o menos; si no,
   exploratorio y nada cambia.
6. **C7** con el zip que salga: 5 por zip, calendario escrito antes.

**Su auditoría del procedimiento, copiada tal cual:**

- La ronda 2 sí cambió algo: los cinco retiraron su primer paso o una cifra. No cerró el punto 2, y el
  arquitecto adoptó 2,25 sin recontarlo.
- El expediente no era anónimo: cada informe cita su carpeta.
- Todos pasaron el tope de palabras.
- Faltó un verificador limpio y alguien que escribiera las predicciones.
- El corte no dañó informes; el analista quedó armado por trozos.
- Aceptar F fue correcto: marcado sin recontar, y se reproduce.
- Orquestador: dejó 14,6 h como condición sin derivación, «17, 18 y 20 ocurrieron» sin enlace y «5 a 8
  minutos» sin verificar.
- Del propio auditor: su primer recuento de la tabla redondeaba mal (4,08); corregido. Un guion suyo imprimió
  nombres de registro en su consola, no en disco.

**Su frase para el dueño:** «Poner el registro al día y, con tu orden, leer la versión de `ipykernel`, reenviar a diario el zip con razonamiento y gastar la cuota en base, base repetida y solo razonamiento, sin tocar los topes.»

### Decisiones del concilio 43

El dueño delegó en el concilio y ordenó aplicar lo que decida; subir y enviar siguen necesitando su orden.

1. **Topes.** Los cuatro campos de `eval_config.yaml` se mantienen en cada kit. Subir los minutos a 5 o más
   queda vetado: el peor caso de 120 tareas da de 11,1 a 12,4 h frente al límite de 12.
2. **Notebook.** Sin tope al total de tareas colgadas y sin cambiar el margen de 30 s ni la ventana final.
   Regla de lectura: una pasada con una tarea colgada no cuenta como completa.
3. **Cuota semanal** (30 h desde las 00:00 UTC): base (pasada 1), base repetida (pasada 2) y un brazo que
   solo enciende el razonamiento, con los mismos topes y las mismas 60 tareas. Costo previsto: 5,0 a 5,6 h
   por pasada y 10 a 11,3 h el brazo; en total unas 22,5 h. Decide el brazo: 6 pares netos a favor y McNemar
   exacto de 0,05 o menos; si no, es exploratorio y nada cambia.
4. **Envío diario:** reenviar el zip con razonamiento, sin cambios, hasta tener cinco lecturas; después,
   alternar dos zips con calendario escrito antes. Los dos envíos finales se eligen por la media de varias
   lecturas, no por la nota pública máxima.
5. **Vetado:** subir minutos; rearmar el notebook con otros márgenes u otro kit; enviar el kit K solo; un kit
   que pida comprobar la sintaxis; medir el kit de 4,5 minutos y 60 llamadas en notebook (cambia tres cosas).
   Aplazado: cambiar los segundos por orden y el kit de interfaz limpia con razonamiento.
6. **Hallazgos:** cuatro decididos, dos descartados y uno abierto, como los dejó el auditor; entran cuatro
   nuevos al registro.
7. **Predicciones:** la 19 no ocurrió; la 7 y la 12 ocurrieron; la 11 no ocurrió; 8, 9 y 10 no se pueden
   marcar porque los informes de revisión no se publicaron; 17, 18 y 20 quedan sin marcar hasta que conste
   el enlace.

**Aplicación, en curso al escribir esto (00:30 UTC del 2026-10-10).** Issue #182: notebook del brazo «solo
razonamiento», armado y ensayado en Docker por un implementador, sin tocar los notebooks de las pasadas 1 y
2. Issue #179, ampliado con los puntos 15 a 19: guion que compara pasadas excluyendo pares faltantes, los dos
envíos que faltan en el registro, el vigía con la hora de cada cambio de estado y el aviso de envío
pendiente, la regla de los envíos finales y la corrección de la condición de las 14,6 h. Pendiente de
lanzar, de a uno: reverificación local a 240 s de los parches cortados a 60 s; predicciones fechadas de la
iteración 08, escritas por un rol y no por el orquestador; actualización de `hallazgos.json` y del
pre-registro; verificador limpio antes de pedir la primera subida.

**Fallos del orquestador en esta vuelta.** El expediente de la ronda 2 no era anónimo: cada informe cita su
carpeta. No convocó a un verificador limpio ni a nadie que escribiera las predicciones. Dejó pasar tres
afirmaciones heredadas sin fuente: la condición de 14,6 h, «17, 18 y 20 ocurrieron» y «los que declaran más
nota usan de 5 a 8 minutos». No hizo cumplir el tope de palabras: los diez textos lo pasaron. Su guion de
copia a la bitácora metió un retorno de carro en una ruta, corregido en el acto. Ningún rol propuso por sí
solo mirar el envío diario como instrumento de medida: llegó de otra sesión.

**Corrección a la decisión 7 (2026-10-10, 01:20 UTC), tras la revisión de documentos del PR #183.** El revisor
señaló que la sección de desenlaces marcaba las predicciones 7, 11 y 19 con un criterio distinto del que
aplicaba a otras seis: dos con una fuente sin publicar y una sobre un hecho que no llegó a existir (el primer
commit con código no tuvo CI). Queda un solo criterio: no se marca una predicción sobre un informe que no está
publicado. Resultado: una marcada (la 12, ocurrió) y nueve sin marcar. Desde el PR #183 los informes del
revisor y del analista se publican como comentario del PR.

**Recuento de Datito sobre las cifras del PR #183 (00:55 UTC):** se reproducen desde los zips las llamadas,
las duraciones, las verificaciones cortadas, la compactación y la tabla pública. Tres textos pasan de «medido»
a «calculado» (peor caso frente a las 12 h, holgura de una pasada, diferencia detectable por envío). Matiz: el
enunciado también falta en 204 de 3 042 peticiones sin compactación previa. Retira dos cifras suyas de la
ronda 1: 5 verificaciones cortadas (vale 16; había filtrado solo una parte de las filas) y la holgura de 1 300
a 1 800 s (manda el tope de 7 200 s).

### Predicciones fechadas 25 a 37 (auditor del método; selladas en el issue #182 el 2026-10-10)

**Predicciones 25 a 37: iteración 08, sonda de CPU y reenvíos.** Autor: auditor del método, concilio 43 (un rol, no el orquestador). Escritas sin que exista ningún resultado: nada se ha subido ni enviado. Copiadas tal cual por el orquestador; la hora la sella este comentario.

Plazo común: cada una se marca al leer la salida de su corrida. Si la corrida no existe el 2026-10-17 a las 00:00 UTC (fin de la semana de cuota), queda sin desenlace. Las de envíos vencen el 2026-10-16.

| # | Hecho | Prob. | Línea base | Qué la marca |
|---|---|---|---|---|
| 25 | La sonda de CPU informa una versión de `ipykernel` de la serie 6 | 0,80 | Sin historia contada (0,5). Ningún log propio trae la versión | La línea de versión en el log de la sonda |
| 26 | En esa versión existe el mapa de hilos `_thread_to_parent` | 0,65 | Sin historia contada (0,5). `ensayo_nucleo_jupyter.md` lo sitúa en 6.29.5 a 7.0.1 y no en 6.28.0 ni 7.1.0; no recontado | La sonda, o el primer evento del registro de la pasada 1 |
| 27 | La pasada 1 termina las 60 tareas sin ningún `CORTE` (tareas, sesión o servidor) | 0,60 | Recuento del auditor: 60 × 109,4 s = 6 564 s contra un tope de 7 200 s; holgura de 360 a 1 260 s según la iteración | El log no contiene `CORTE por` y la salida trae 60 filas |
| 28 | Al menos una tarea de la pasada 1 se corta por `tarea_colgada` | 0,10 | 0 de 145 filas pasan de 303,6 s; el tope es 900 s | `tareas_colgadas` ≥ 1 en el registro |
| 29 | Los registros por tarea de la pasada 1 salen con contenido: ninguno de 0 bytes | 0,55 | 145 de 145 fueron de 0 bytes en las iteraciones 03 a 07 (cifra del forense, no recontada). Los enganches nuevos no han corrido en Kaggle | Tamaño de cada archivo de registro en la salida bajada |
| 30 | La pasada 1 resuelve entre 7 y 15 de 60 | 0,70 | 21 de 116 (18 %) sin razonamiento; el sorteo no es el mismo conjunto | `resolved` en `task_results.jsonl` |
| 31 | Su duración media por tarea cae entre 95 y 125 s | 0,70 | 109,4 s; de 99 a 114 por iteración (cifra del arquitecto) | Media de `duration_seconds` |
| 32 | `diagnosticar` sale con código 0 sobre la pasada 1 | 0,50 | Sin historia contada (0,5): nunca corrió sobre una sesión de Kaggle | Código de salida de la orden, copiado en la bitácora |
| 33 | Entre las pasadas 1 y 2 hay 5 o menos pares discordantes, sobre los pares válidos | 0,65 | 2 de 43 entre las iteraciones 03 y 04 (bitácora; no recontado en esta vuelta) | Salida del guion de comparación (#179, punto 11) |
| 34 | El kit B resuelve más tareas que la media de las dos pasadas de A | 0,70 | 18 de 29 contra 21 de 116, confundido: tareas elegidas, 4,5 min y 60 llamadas | Recuento de `resolved` de los tres brazos |
| 35 | B contra la pasada 1: 6 pares netos o más a favor y McNemar exacto de 0,05 o menos | 0,30 | Sin historia contada (0,5). El diseño detecta 6 netas con potencia de 38 % (analista) | Salida del guion de comparación |
| 36 | En B se cortan por tiempo (mensaje del arnés) entre 30 % y 60 % de las tareas, y la media por tarea cae entre 185 y 235 s | 0,55 | 10 de 29 (34 %) y 245,9 s con tope de 4,5 min; aquí el tope es 4 | `error_message` y `duration_seconds` |
| 37 | En las lecturas tercera a quinta del zip `65a02160…`: (a) alguna pasa por estado de error; (b) las tres notas caen entre 4 y 10 tareas de 58; (c) la media de las cinco supera 6,5 | (a) 0,60; (b) 0,75; (c) 0,40 | (a) 2 de 2 envíos de ese zip pasaron por error y 0 de 2 del kit A; (b) y (c) lecturas previas de 5 y 8 | Historial del vigía con la hora de cada estado; `envios.json` |

- La 36 solo ocurre si se cumplen sus dos partes.
- La 35 se lee contra la pasada 1, fijada aquí, para no elegir la pasada después.
- La 37 se marca por letra, como tres desenlaces.
- La 26 tiene efecto de predecir: quien arma la sonda decide qué imprime.

**Qué haría abandonar el plan.** Cualquiera de estos resultados:
1. La 29 no ocurre (registros vacíos): no se lanza la pasada 2 hasta arreglarlo.
2. La 28 ocurre, o la pasada 1 deja menos de 55 tareas válidas.
3. La 33 no ocurre con más de 6 discordantes: el diseño de 60 pares no separa nada, no se gasta cuota en B y la medida pasa a los envíos alternados.
4. La media de B pasa de 240 s: el razonamiento no cabe en 4 minutos y no se envía con ese tope.
5. Dos reenvíos terminan en error sin repuntuarse: se detienen los envíos hasta tener la duración de una evaluación.

### Verificador limpio de la vuelta 43 (2026-10-10, hacia las 00:40 UTC)

No abrió la bitácora ni los informes. Midió sobre la copia `2026-10-09T1741Z` (12 zips distintos, 145 sesiones;
sin rescate nuevo porque el encargo le prohibía la red). Diez afirmaciones dadas sin cifras:

| Afirmación | Marca | Su medida |
|---|---|---|
| Sin razonamiento, una sesión dura menos de la mitad | Se sostiene | 109,4 s frente a 245,9 s |
| Muchas sin razonamiento acaban al tope de llamadas o a una, y casi ninguna resuelve | Se sostiene | 41 de 116 con 39 o 40 llamadas (12 y 29); 2 resueltas; el resto resuelve 19 de 75 |
| Con razonamiento, ninguna al tope y un tercio cortada por tiempo | Se sostiene, con caso contrario | Máximo 53 de 60; 10 de 29 por mensaje; 16 de 29 duran 270 s o más y 6 de esas resuelven |
| 120 tareas caben en 12 h; márgenes con todas al tope | La media se sostiene; los márgenes, tal como se le dieron, se caen | 8,20 h con la media. Al tope de 4,5 min: margen de 3,00, 2,17 o 0,88 h según el sobrepaso, **sin sumar la carga del modelo** |
| En el notebook de la 08 manda el tope del conjunto de tareas | Se sostiene | 7 200 s; holgura de 636 s con la media global y 1 204 s con la mezcla del sorteo |
| El kit B difiere del A en una línea; el I, además, en dos topes | Se sostiene | Una línea (`include_thoughts`); I añade 40→60 llamadas y 4→4,5 min |
| El mismo archivo, notas distintas | Se sostiene | 0,06 y 0,05; 0,08 y 0,13. La identidad del archivo consta solo en la descripción del envío |
| Más envíos, mejor nota; más dispersión que una binomial | Se sostiene, condicionada | Media 0,068 con un envío y 0,124 con 11 a 20; vale si las tareas públicas son más de 32 |
| Verificaciones cortadas por tiempo, de un solo repositorio | Se sostiene, con una mitad vacía | 16 sin razonamiento, del mismo repositorio (16 de 26). Con razonamiento hay 0, **pero ese repositorio nunca se corrió con razonamiento** |
| Parche vacío, ninguna resuelta | Se sostiene | 37 de 145; 0 resueltas |

**Sobre la fila que se cae:** el margen de «media hora a hora y media» que el concilio escribió incluye la carga
del modelo (1 142 s, el máximo medido) además del sobrepaso; el verificador no la sumó. Con ella, sus cifras dan
0,56 a 1,85 h de margen, que es el rango del auditor (peor caso de 10,1 a 11,4 h). La frase del orquestador
estaba mal dada, no la cuenta.

**Lo que el relato no separa y el verificador sí vio:**
- El kit con razonamiento que se envió cambia tres cosas a la vez, y ningún zip corre el kit B: el brazo «solo
  razonamiento» que se va a medir nunca ha corrido. Tres sesiones del kit con razonamiento pasan de 39 llamadas y
  habrían topado con el tope de 40.
- Las sesiones con razonamiento son de un subconjunto de tareas y nunca del tercer repositorio, que es el más
  lento sin razonamiento (142,6 s frente a unos 100 s): la media de 245,9 s no representa la mezcla oculta.
- «Sin razonamiento» mezcla dos kits (86 y 30 sesiones) con instrucción de sistema distinta.
- «Enciende el razonamiento» es interpretación: el presupuesto de razonamiento es el mismo en todos los kits; la
  línea solo cambia si los pensamientos se incluyen.
- El campo de estado no distingue nada (vale lo mismo en las 145); el corte solo se ve en el mensaje de error.

**Consecuencia para el plan, sin cambiarlo:** la predicción 36 (duración y cortes del brazo B) parte de tareas
elegidas y de otro tope; el verificador da una razón más para leer la pasada del brazo con cuidado y para no
subir minutos antes de tenerla.

### Estado al cierre y cómo retomar (2026-10-10, 00:55 UTC)

Cierre pedido por el dueño. **Nada se subió ni se envió a Kaggle.** Todos los agentes de la sesión quedaron
detenidos y no queda ningún contenedor de ensayo corriendo. Sustituye a los cierres del 2026-10-09.

**En `main` (cabeza `72ca143`):** PR #183 fusionado (`mergedAt` 2026-10-10T00:12:01Z, CI 12 de 12): registro de
hallazgos tras el concilio 43 (cuatro decididos, dos descartados, uno abierto, cuatro nuevos), desenlaces de
predicciones con un solo criterio (una marcada y nueve sin marcar), la revisión cruzada en `CONTRIBUTING.md` y
en la skill, y los episodios 076 (#180) y 079 (vuelta 43). El guardián del tablero termina sin hallazgos.

**Decisiones vigentes del concilio 43:** topes del envío sin tocar (subir a 5 minutos, vetado); notebook sin
cambios; cuota semanal en base, base repetida y brazo «solo razonamiento» (kit B: el A con una línea distinta),
unas 22,5 h; envío diario reenviando el zip con razonamiento hasta cinco lecturas; finales por media, no por
máximo. Predicciones 25 a 37 escritas por el auditor y selladas en el issue #182. Verificador limpio: nueve de
diez afirmaciones se sostienen.

**A medias, tal como quedó cada cosa (leer el diff antes de seguir):**
- **PR #184 / issue #179: «cambios requeridos».** El guion `kaggle_comparar_pasadas.py` salía con 0 sobre
  pasadas que no merecen compararse (seis bloqueantes, en el comentario del PR). Datito confirmó que las cuentas
  son correctas. Árbol `F:\Code\ALL-wt-179`: un commit local sin subir, `bb83975`, con las correcciones del
  guion; al implementador le faltaban las frases de los documentos y fusionar `main`. Árbol
  `F:\Code\ALL-wt-179b`, rama `issue-179-b`: cambios **sin confirmar** en `scripts/kaggle_vigia.py`,
  `CONTRIBUTING.md`, el episodio 078 y un archivo de pruebas nuevo. Ninguno de los dos pasó por pruebas
  completas ni por el revisor. El guion de comparación es condición de lanzamiento.
- **PR #185 / issue #177:** entregado; Datito recontó y se reproduce; CI en 11 de 12 al cerrar; la revisión de
  código se detuvo sin informe. No fusionar sin ella.
- **Issue #182 (notebook del brazo «solo razonamiento»):** en `…\instrumentos\iteracion_08_razona\` hay cinco
  notebooks armados (`kernel_iteracion_08_r1` a `r5`: cinco porciones, no tres) y salidas de ensayo de las
  cinco sesiones completas, de un corte por tiempo y de una tarea colgada con el tope real, con `HUELLAS.txt` y
  `RESUMEN.json`. El implementador se detuvo sin informe final, sin PR y con `ensayo_nucleo_jupyter.md` a medio
  editar y sin confirmar en `F:\Code\ALL-wt-brazo-razona`. **No está validado por nadie:** leer `RESUMEN.json`
  y el diff antes de darlo por armado.
- **Reverificación local a 240 s:** preparada en `…\concilio_43\reverificacion_240\` (guiones y lista de
  sesiones); detenida al empezar la primera corrida. Sin resultado.
- **Concilio ZorzALL (¿secuencia como memoria?):** rondas 1 y 2 completas, los cuatro roles en «metáfora»; el
  auditor se detuvo mientras recontaba, sin dictamen. Todo está en la carpeta ignorada
  `.scratch\concilio_zorzall_secuencia\` del repositorio (encargo, fuentes, informes, respuestas cruzadas y
  tres guiones del auditor). La entrega al dueño se dio con el dictamen marcado como pendiente.

**Lo que espera la orden del dueño (nada está subido):** la sonda de CPU que lee la versión de `ipykernel`
(0 h de GPU); el reenvío diario del zip con razonamiento; la pasada 1 de la iteración 08 (5,0 a 5,6 h de cuota).
Antes de la pasada 1 faltan: el guion de comparación corregido y revisado (PR #184) y el ensayo con la versión
de `ipykernel` que dé la sonda. La cuota se repuso a las 00:00 UTC (30 h); el plan suma unas 22,5 h y la
instrucción del dueño fija 24 h por semana.

**Sin empezar:** #165, #166, #167; las dos discrepancias del manuscrito entre castellano e inglés (en ambas
vale la versión inglesa; cambiarlas exige otra firma del validador y regenerar el PDF).

**Fallos del orquestador en esta sesión:** esperó pasivamente una CI en cola en vez de adelantar lo demás, y el
dueño tuvo que pedir tres veces el cierre; afirmó que un paso «no llegó a ejecutarse» sin comprobarlo (el
commit y el comentario ya estaban hechos); corrió solo parte de las pruebas en local y la CI del PR #183 falló
en las ocho tandas; marcó tres predicciones con un criterio distinto del que aplicaba a otras seis.

**Cómo retomar:** `gh pr list`; leer los comentarios de los PR #184 y #185; `git status` en `F:\Code\ALL-wt-179`,
`ALL-wt-179b` y `ALL-wt-brazo-razona`; no relanzar un agente sin mirar antes qué dejó el anterior.


## Vuelta 44 — 2026-10-11 y 2026-10-12 (UTC)

**Pregunta de la vuelta** (del dueño, en dos encargos): primero, un concilio de investigación de al menos diez
ciclos sobre memoria bioinspirada para agentes, con Claude y Codex como investigadores; después, «diez
iteraciones más», reparando desde lo aprendido hasta decidir en concilio sin preguntarle: **¿cómo mejorar
ALL?, y continuar en el concurso**.

**Nada se subió, se envió ni se ejecutó en Kaggle. No se gastó GPU.** El vigía, al iniciar la sesión: envíos
sin cambios desde el rescate `2026-10-09T1741Z` (0,13, 0,08, 0,05 y 0,06). No se hizo rescate nuevo ni lectura
de cuota.

**Dónde está todo.** Cuaderno de los 22 ciclos, con lo que cada uno retiró:
`F:\Code\Agents Learning Loops\.scratch\concilio_memoria\CUADERNO.md` (carpeta ignorada por git). Salida
auditada del concilio de memoria: `…\concilio_memoria\SALIDA_FINAL.md`. Segunda tanda: `…\concilio_memoria\fase2\`
(encargo, seis informes, revisión cruzada, guiones del analista y del auditor). Lo versionado está en los PR
citados abajo; la medición, resumida en el issue #103.

### Lo que el concilio de memoria dejó (primera tanda, 12 ciclos)

- Cinco candidatas que difieren en **qué modifican**: qué se observa primero (diagnóstico), qué se da por
  terminado (aceptación), la política por defecto, los recursos y el peso de la evidencia. Finalistas por voto
  de Claude y de Codex: diagnóstico y aceptación. Los votos no son independientes (Codex leyó la síntesis de
  Claude antes de votar) y la confianza discrepa: 0,25 y 0,35 frente a 0,60 y 0,55.
- Diseño de experimento en tres etapas (techo con oráculo, piloto de 60 tareas, confirmación de 240), auditado:
  el auditor encontró tres bloqueantes en los veredictos y se corrigieron. El costo que manda es escribir
  tareas: hoy hay 9.
- **Ninguna candidata está medida.** El banco propio tiene tres tareas independientes por estrato y no detecta
  nada al 5 %.
- Citas del documento base que no se sostienen: «MemGuard (Zhong et al. 2024)» no existe; «PER ~20 %» no
  tiene fuente.

### Lo medido en esta vuelta (resumen; detalle en el issue #103)

Con los 73 episodios del repositorio, memoria reconstruida solo con los anteriores a cada uno (63 evaluables):
el ranking de acciones de `devlog recall` no se separa del azar (AUC 0,550; p = 0,055) y **la tasa base de
fallo por acción lo supera** (0,646; gana en 34 episodios, pierde en 20). 21 de 75 lecciones automáticas eran
«si X falla, usar X», y ocupaban 120 de las 295 posiciones que `recall` mostró. El heredoc largo falló en 10
episodios; la lección ya estaba guardada en las 9 repeticiones y 5 son posteriores a la regla escrita.
Exploratorio: un corpus, episodios dependientes, código de hoy; no hay contrafactual.

### Decisiones del concilio de la segunda tanda (dictamen del auditor del método, 2026-10-12)

Registradas en el issue #182. Seis roles con la misma pregunta, revisión cruzada sin firmas, auditor después.

- **Se hace:** cerrar condiciones de lanzamiento; gancho que rechaza heredocs y guarda de la cuenta de GitHub
  (#186); filtrar de `recall` las lecciones de «misma acción» (#187); tasa base por acción (#167).
- **No se hace:** una compuerta de aceptación en el agente enviado (sigue el veto del concilio 43; quien la
  propuso la retiró al separar sus datos por kit: 9 recuperables en 73 sesiones antiguas y 0 en 29 con
  razonamiento); «diagnóstico primero» (100 de 102 sesiones ya miran antes de editar); orden única antes del
  push; apagar `recall` en issues alternos (sin potencia).
- **Vetado por el auditor por estar dentro del ruido:** que `recall` deje de ser condición para empezar un
  issue, y quitar «issues parecidos».
- **Aplazado:** corregir la consolidación en la biblioteca (antes hay que medir su efecto en la referencia del
  Experimento 1); recontar sintaxis y hueco en el brazo (no existe ninguna corrida real).
- **Regla nueva del brazo «solo razonamiento»:** tras su primera porción se lee la media; si pasa de 240 s por
  tarea, o la proyección pasa de 24 h, no se lanzan las otras cuatro. Una primera porción sin datos cuenta
  como «no lanzar».

### Cuenta de horas, corregida

El brazo, armado en cinco porciones de doce tareas, no cuesta «10 a 11,3 h». Con el máximo por tarea observado
(304 s) y carga de 364 a 1 142 s: 11,1 a 13,3 h con factor de cuota 2,0. **Plan completo (dos pasadas de base y
el brazo): 21,1 a 23,3 h con factor 2,0 y 23,8 a 26,2 h con factor 2,25, que es el que el documento adopta
para decidir; el tope del dueño es 24 h.** El factor 2,0 no tiene fuente versionada. Detalle y guion:
`experiments/gemma_developer_agent/docs/ensayo_nucleo_jupyter.md`, sección del #182, y
`scripts/kaggle_costo_brazo.py`.

### Hallazgo nuevo, no medido en Kaggle

En 4 de 6 sesiones completas del ensayo local del brazo, un latido guardó un diff de 4,6 a 23,8 MB (el árbol a
medio montar, no un parche). Cabe en disco (un archivo que se sobrescribe); su duración no está medida.
Registrado en `hallazgos.json` por el PR #190.

### Lo que otros publicaron (copias guardadas hasta el 2026-10-09; las páginas vivas no se dejaron leer)

Cierre de envíos el 2026-12-02; Paper Track el 2026-11-12; un envío por día. Nadie publica memoria entre
tareas. El razonamiento encendido de otro equipo da 47 de 129 frente a 44 y 49 sin él, dentro del ruido, con
más cortes y más parches vacíos. Las reglas permiten conocimiento dentro del zip, pero una tabla derivada de
las tareas públicas choca con la regla 2.4.b y ninguna respuesta lo aclara.

### Lo aplicado: ocho PR fusionados, cada uno con revisor independiente

| PR | Issue | Qué trae | `mergedAt` (UTC, 2026-10-12) | Commit |
|---|---|---|---|---|
| #185 | #177 | `--permitir-mencion` avisa por línea y no da `[OK]` | 02:26:29 | `33f07be` |
| #189 | #167 | `python -m scripts.devlog base-rates` | 03:20:07 | `a32357e` |
| #190 | #182 (`Refs`) | Brazo «solo razonamiento»: armado, ensayo, cuenta de horas y regla de parada | 03:50:06 | `a8e809f` |
| #191 | #186 | Gancho que rechaza heredocs y guarda de la cuenta de GitHub | 04:18:07 | `ddc9e88` |
| #192 | #187 | `recall` omite las lecciones de «misma acción» | 04:35:21 | `19b734e` |
| #193 | #188 | Prueba de reloj estable; fronteras del validador de envíos | 04:35:53 | `4c94115` |
| #194 | #103, #167 | Predicciones 38 a 47 con desenlaces; episodio 086 | 05:22:15 | `d5be5cc` |
| #184 | #179 | Comparación de pasadas, cambios de estado del vigía y registro de envíos | 05:47:03 | `281e822` |

De ocho PR, cuatro recibieron «cambios requeridos» en su primera revisión (#184, #190, #191 y #193; el #184,
además, en la segunda).
Lo que encontró el revisor y no había visto el implementador con la suite en verde: una regla de parada que
autorizaba lanzar cuatro porciones con una primera porción sin datos; un gancho que rechazaba todos los
`git push` y que, si faltaba su guion, bloqueaba todas las órdenes; una prueba que ya no podía fallar; un
guion de comparación que daba por buenas dos salidas que no cuadraban.

**Cierres confirmados** (criterios comprobados sobre `main`, tarjeta en *Done* con *Verificación* =
*Verificada*): #167, #177, #186, #187, #188. El guardián del tablero termina sin hallazgos.

**Condiciones de lanzamiento de la iteración 08, una por una:**
1. #164 fusionado: cumplida desde antes (`c6e9193`).
2. Guion de comparación corregido y revisado: **cumplida** (PR #184, tres revisiones; las salidas reales
   guardadas se releyeron: un par real sale con 0 y las 37 salidas guardadas cuadran con su registro).
3. Notebook del brazo «solo razonamiento»: armado y validado en bytes (5 de 5 hashes, 125 de 125 huellas);
   **parcial**: el corte por tiempo y la tarea colgada solo se forzaron sobre `r1` (el resto pide Docker).
4. Ensayo local con la versión de `ipykernel` de Kaggle: **pendiente**; depende de la sonda de CPU, que
   espera la orden del dueño.

### Estado al cierre y cómo retomar (2026-10-12, 05:55 UTC)

Sustituye al cierre del 2026-10-10. **Nada se subió ni se envió a Kaggle; no se gastó GPU.** No queda ningún
agente corriendo.

**`main` en `281e822`**, con el árbol principal al día y la CI en verde hasta `d5be5cc` (la de `281e822`
estaba corriendo al cerrar: comprobarla).

**Lo único que espera la palabra del dueño** (una sola cosa, lista): **lanzar la iteración 08.**
- Sonda de CPU que lee la versión de `ipykernel` (0 h de GPU).
- Reenvío diario del zip con razonamiento `65a02160`, sin cambios, hasta cinco lecturas (0 h; un envío por día).
- Pasada 1 (5,0 a 5,6 h), solo tras el ensayo local con el `ipykernel` que dé la sonda.
- Plan completo: 21,1 a 23,3 h con factor 2,0 y 23,8 a 26,2 h con factor 2,25, frente al tope de 24 h. El
  brazo se corta tras su primera porción si la media pasa de 240 s.
- **La cuota de la semana se pierde el 2026-10-17 a las 00:00 UTC**, y ahí vencen las predicciones 25 a 37.
  Para medir los tres brazos, la orden tendría que llegar hacia el 14 (cálculo del auditor, no medido).

**Abierto, sin depender del dueño:**
- **#179:** fusionado y cerrado; **sin confirmar**. Su punto 8 pide la salida del gancho de inicio en una
  sesión nueva: la pegada es del vigía anterior a los cambios. **La primera sesión que se abra debe pegar en
  el #179 la salida del vigía** y, si cuadra, marcar *Verificada*.
- **#182:** abierto. Falta el ensayo de corte y colgada en `r2` a `r5` (Docker) y tres observaciones menores
  del revisor en `scripts/kaggle_costo_brazo.py` y en el documento.
- **Gancho del #186, a vigilar:** `python -m scripts.guarda_previa --contar`. Condición de reversión: 2 o más
  pasos fallidos por heredoc en 15 episodios, o más de 1 orden legítima frenada → pasa a solo contar. Primer
  uso real: rechazó un heredoc a `python`, sin falsos rechazos. Fricción vista: un agente sin herramienta de
  escritura no puede seguir el consejo del mensaje («escribe el archivo») y cae en `python -c`. Observación
  abierta del revisor: un usuario dado por variable se toma por cuenta ajena. La guarda de cuenta no se ha
  visto rechazar en una sesión real. No cubre PowerShell ni a Codex.
- **Predicción 41** (un fallo por heredoc en 15 episodios): abierta, vence el 2026-11-11.
- **Aplazado por el concilio:** corregir `memory/consolidation.py` (medir antes su efecto en la referencia del
  Experimento 1); #165 y #166 (predicciones contra tasa base, ahora que existe `base-rates`).
- **Candidatos a issue, sin abrir:** tres de cuatro PR en paralelo chocaron en `CHANGELOG.md`; la tabla por
  clase de `base-rates` necesita un segundo lector antes de servir de línea base; el concilio de memoria
  (`SALIDA_FINAL.md`) no está versionado: publicarlo exige pasar por el staff de texto público.
- Siguen como estaban: #165, #166, las discrepancias del manuscrito, la reverificación a 240 s y el concilio
  ZorzALL sin dictamen del auditor.

**Otra sesión trabajó en paralelo** en la misma carpeta del concilio de memoria durante el ciclo 5 (con otros
modelos): dejó `fuentes/ciclo2_mecanismos.md`, `codex/prompt_c3b.md`, tres informes de rol con guion en el
nombre y una entrada «convocatoria» en el cuaderno. No se tocó nada suyo.

**Fallos del orquestador en esta vuelta** (están en el episodio 086): usó un heredoc largo que falló, con la
lección ya guardada y sin consultar; leyó mal dos resultados propios al resumir la evidencia (los corrigieron
Codex y el auditor); presentó tres veces como coincidencia independiente algo que él mismo había escrito en lo
que el otro leyó; no fijó la cuenta de GitHub al delegar y un comentario salió con la cuenta equivocada;
afirmó sin comprobar que los ganchos no alcanzan a los subagentes; dio por confirmable un cierre antes de mirar
la CI de `main`; y selló predicciones en comentarios en vez de en el archivo versionado.

**Cómo retomar:** leer esta sección y el cuaderno; `gh pr list`; `python -m scripts.devlog board --since 160`
con `GH_TOKEN` de `cherrera0001`; pegar en el #179 la salida del vigía de la sesión nueva; `python -m
scripts.guarda_previa --contar`.

**Añadido al cierre (05:58 UTC): lectura del contador del gancho tras su primera hora.** Rechazos 3, pasa-dudoso 8, push visto 2, fallas 0. Uno de los rechazos fue la prueba deliberada; los otros dos, un `cat` con heredoc hacia un archivo fuente hecho por agentes de solo lectura (revisor y analista), que no tienen herramienta de edición y por tanto no pueden seguir el remedio del mensaje. Si se cuentan como órdenes legítimas frenadas, la condición de reversión («más de 1») ya se cumpliría. No se aplicó: el registro no guarda la orden y la lectura es dudosa. Queda para el próximo concilio, con tres opciones escritas en el issue #186.


### Lanzamiento de la iteración 08 (2026-10-12, 06:45 a 06:49 UTC)

**Orden del dueño, textual: «lanza la iteración 08».** Llegó después de presentarle una sola cosa lista:
sonda de CPU y reenvío diario (0 h de GPU) y pasada 1 (5,0 a 5,6 h). Estas son las primeras subidas desde el
2026-10-07.

| Hora (UTC) | Qué | Orden | Resultado |
|---|---|---|---|
| 06:45 | Lectura de cuota | `uvx kaggle quota` | GPU 0,00 h usadas de 30,00; reposición 2026-10-17T00:00 |
| 06:45 | Lectura de envíos y notebooks propios | `uvx kaggle competitions submissions …`, `kernels list --mine` | Ningún envío pendiente; el último, del 2026-10-07 |
| 06:46:20 | **Sonda de CPU** (`cs4all/sonda-nucleo-08`, privada, sin GPU, sin internet, sin datos) | `uvx kaggle kernels push -p …/sonda_nucleo/kernel_sonda` | Versión 1; terminó en menos de un minuto |
| 06:46:48 | **Envío del día**: zip `65a02160…` sin cambios (sha256 comprobado antes de enviar), lectura 3 de 5 | `uvx kaggle competitions submit gemma-4-developer-agent -f submission.zip -m "I razona, lectura 3 de 5 (mismo zip 65a02160, sin cambios)"` | Aceptado; «0 submissions remaining today» |
| 06:48:31 | **Pasada 1** (`cs4all/iteracion-08-p1`, privada, NvidiaL4, tope de 9 000 s) | `uvx kaggle kernels push -p …/iteracion_08/kernel_iteracion_08_p1 -t 9000 --accelerator NvidiaL4` | Versión 1; estado `QUEUED` a las 06:48:51 |

**Lo que midió la sonda** (`…/instrumentos/sonda_nucleo/salida_kaggle_2026-10-12/sonda_nucleo.json`): Python
3.12.13; **`ipykernel` 6.17.1**; `sys.stdout` es `ipykernel.iostream.OutStream` **sin** el mapa
`_thread_to_parent`; `ipython` 7.34.0, `jupyter_client` 7.4.9, `nbclient` 0.5.13, `papermill` 2.7.0, `rich`
13.9.4, `litellm` 1.82.4; 4 CPU; 952 paquetes. La imagen es la misma que fija el notebook de la pasada
(`sha256:37c64f7d…`).

**Condición «ensayo con el `ipykernel` de Kaggle»: cumplida con un ensayo ya hecho, no con uno nuevo.** La
versión medida, 6.17.1, es una de las dos que el #164 ensayó el 2026-10-09 con este mismo notebook (sha256
`30aa9b31…`, comprobado hoy antes de subir): `completa_ipykernel_6.17.1` (4 tareas, todas las celdas
terminan, diagnóstico 0) y `colgada_ipk_6.17.1` (el tope por tarea corta, diagnóstico 3), las dos con
`pasa: true` en el `RESUMEN.json` del ensayo. Con 6.17.1 el bucle que causó el cuelgue del #160 no existe y el
vaciado del mapa no actúa; el tope por tarea no depende de la versión.

**Lo que ese ensayo no cubre** (no se repitió: Docker no estaba en marcha, y la condición escrita pide solo
`ipykernel`): la imagen local del ensayo difiere de Kaggle en `ipython` (9.17.1 frente a 7.34.0),
`jupyter_client` (8.10.0 frente a 7.4.9), `nbclient` (0.10.2 frente a 0.5.13), `papermill` (ausente frente a
2.7.0), `rich` (15.0.0 frente a 13.9.4) y `litellm` (1.104.0 frente a 1.82.4). Es el riesgo que queda en la
pasada 1. Si la sesión falla por una de esas diferencias, la primera tarea lo dirá (la guardia corre tras la
primera tarea) y el costo queda acotado por el tope.

**Chequeos antes de subir la pasada 1:** las 12 celdas compilan; `python -m scripts.kaggle_preflight comprobar
--tope-min 150` da 18 de 18 en verde (privado, sin internet, imagen fijada, acelerador `NvidiaL4`, sin rutas
fijas, la guardia pasa con las dos disposiciones reales de `/kaggle/input` y se detiene sin las ruedas).

**Costo comprometido:** hasta 150 min de sesión, 5,0 h de cuota con factor 2,0 y 5,6 h con 2,25. Una sola
sesión de GPU en cola.

**Qué sigue, en este orden, y qué no se hace todavía:**
1. Cuando `cs4all/iteracion-08-p1` termine: `uvx kaggle kernels output cs4all/iteracion-08-p1 -p <carpeta>`,
   rescate, leer solo agregados (ningún identificador de tarea) y `python -m scripts.kaggle_registro
   comprobar` sobre su salida. Leer la cuota gastada: da el factor real entre reloj y cuota.
2. **La pasada 2 no se sube hasta leer la 1** (condición 4: en serie).
3. Brazo «solo razonamiento»: solo su primera porción (`r1`); las otras cuatro, si la media no pasa de 240 s y
   la proyección no pasa de 24 h (`python -m scripts.kaggle_costo_brazo`).
4. Envío diario: lecturas 4 y 5 del mismo zip, una por día, si el envío anterior ya terminó de puntuar.
5. Marcar las predicciones 25 a 37 (selladas en el issue #182) con lo que salga.

**Pendiente de registrar en el repositorio** (va por PR, no a mano): el envío de hoy en
`experiments/gemma_developer_agent/submissions/registry.json`; y en `docs/ensayo_nucleo_jupyter.md`, que la
versión de `ipykernel` de Kaggle ya está medida (hoy dice «no está medida») y que la condición 2 se dio por
cumplida con el ensayo del 2026-10-09. La ficha de estas tres corridas en `REGISTRO_DE_PRUEBAS.md` la lleva la
otra sesión; aquí queda el dato para copiarla.


### La pasada 1 falló a los 106 s: el arnés cambió de versión (2026-10-12, 06:50 a 06:56 UTC)

**Qué pasó.** `cs4all/iteracion-08-p1` pasó de `QUEUED` a `RUNNING` en menos de seis minutos y terminó en
`ERROR`. Gastó **0,07 h de cuota** (lectura de las 06:56: 29,93 h restantes). No llegó a cargar el modelo ni a
correr ninguna tarea. No dejó archivos de salida; solo el log.

**Log extraído:** `…\instrumentos\iteracion_08\salida_kaggle_p1\iteracion-08-p1.log` (18 449 bytes, 149
trozos). El cliente de Kaggle no pudo escribirlo en el primer intento por la codificación de la consola de
Windows (`'charmap' codec can't encode character '✔'`); se bajó con `PYTHONUTF8=1`.

**Causa, leída en el log:**
- La instalación de ruedas dice `INSTALADA ✔ swegemma 0.2.11` (las corridas anteriores eran con 0.2.7).
- Línea propia del notebook: `SERVIDOR FALLO ModuleNotFoundError No module named 'swegemma.models.discovery'`.
- Traza: la celda que arranca el servidor del modelo hace
  `from swegemma.models.discovery import validate_single_declared_model`.

**Causa, comprobada fuera del log:**
- El conjunto público de ruedas `metric/gemma-4-developer-agent-wheelhouse` se actualizó el **2026-10-09 a las
  14:43 UTC**: `swegemma-0.2.11`, `adk_submission-0.2.13` (antes 0.2.12), `adk_eval_core-0.1.0`,
  `google_adk-1.36.1`. Nuestro último rescate del foro llegaba a las 13:43 de ese día: una hora antes.
- Diff de las ruedas (bajadas hoy a `…\instrumentos\arnes_2026-10-12\`, solo leídas, no ejecutadas) contra la
  copia anterior: en `swegemma` desaparecen `models/discovery.py` y `models/registry.py`; cambian `cli.py`
  (+101), `harness/agent_runner.py` (+324/−16), `harness/verification.py` (+145/−9), tres módulos de `graph/`
  y dos de `tools/`; en `adk_submission` cambia `resolvers/generation.py` (+131/−20).
- Comprobación estática de los 13 imports del notebook contra las fuentes nuevas: ese import está roto; contra
  las antiguas, no.
- **El notebook oficial vigente, bajado hoy, también importa `swegemma.models.discovery`:** no sirve de modelo
  para el arreglo.

**Por qué no lo vio el ensayo local.** El ensayo corre un arnés simulado (`scripts/kaggle_simulacro.py`), no
las ruedas reales, y nadie comparó las versiones del conjunto de ruedas con las ensayadas antes de subir. El
chequeo previo (18 de 18 en verde) no mira eso. **Fallo del orquestador:** di por cumplida la condición del
ensayo mirando solo `ipykernel`, y subí sin releer el foro ni el conjunto de ruedas, con un rescate de casi
tres días. La vigía de inicio de sesión lo había avisado («corre el rescate»).

**Consecuencias que van más allá del notebook** (lectura de código pendiente; forense en curso):
- El envío de hoy (ref 57098570) se está puntuando con un arnés distinto del que puntuó las cuatro lecturas
  anteriores. **Las «cinco lecturas del mismo zip» ya no miden solo ruido**: mezclan dos versiones del arnés.
- Las 145 sesiones propias de las iteraciones 03 a 07 corrieron con 0.2.7.
- Cambió el módulo que resuelve la generación (`sampling.yaml`): hay que leer si el kit con razonamiento y el
  de base se comportan distinto con la versión nueva.

**En curso:** rescate nuevo (`2026-10-12T0700Z`), forense del cambio de arnés (lista completa de roturas, no
solo la primera), y después corrección del notebook, ensayo local con la imagen de `ipykernel` 6.17.1 y
comprobación de imports contra las ruedas reales, revisión independiente y, solo entonces, nueva subida.


### Concilio 45 (2026-10-12): el kit de base ahora razona; primer paso, un sondeo de 12 tareas

**Confirmado con una medición local, no solo leyendo el código.** Prueba sin GPU con las ruedas reales del
arnés y un servidor falso que guarda cada petición (2 tareas y 6 peticiones por corrida, `ipykernel` 6.17.1;
issue #195, `…\lanzamiento\prueba_ruedas\RESULTADO.json`):

| Kit | Arnés anterior (0.2.7 / 0.2.12) | Arnés nuevo (0.2.11 / 0.2.13) |
|---|---|---|
| Base, `d8a3e1d3…` | `enable_thinking: false`, sin presupuesto (6 de 6) | **`enable_thinking: true`, presupuesto 4 096 (6 de 6)**; el pensamiento no vuelve al historial |
| Razonamiento, `65a02160…` | `enable_thinking: true`, 4 096 (6 de 6); el pensamiento vuelve en 4 de 6 | Igual |

Tras sustituir el import eliminado no apareció otra rotura dura (predicción 48: no ocurrió; predicción 49:
ocurrió). No medido: la conducta real del modelo, las peticiones del subagente y qué arnés usa el puntuador.

**Ronda 1** (encargo en `…\fase2\concilio_45\encargo.md`; informes en `…\concilio_45\<rol>\`). La misma
pregunta a arquitecto, analista de datos, QA e inteligencia pública: qué se corre con las 29,93 h que quedan y
qué se envía cada día. Límite: la lista de candidatas la escribí yo y el sondeo era una de ellas.

- **Los cuatro, por separado, ponen primero lo mismo:** un **sondeo de 12 tareas con el kit de base** bajo el
  arnés nuevo, para medir segundos por tarea, cortes y razonamiento. Costo estimado: 1,9 a 2,7 h de cuota.
- **Arquitecto (cuenta, inferida con tiempos del arnés anterior):** razonando, 60 tareas piden de 12 600 a
  18 240 s contra el tope de 7 200 s; correrían entre 23 y 34. Relanzar tal cual no dejaría ninguna pasada de
  base completa. Las tres condiciones a la vez (22,9 a 30,2 h) no caben con margen. El prompt nuevo añade unos
  640 a 1 230 tokens por turno (el árbol del espacio de trabajo).
- **Analista (recontado desde los rescates):** 246,0 s por tarea con razonamiento (29 sesiones; censurado: 16
  se cortan por tiempo) y 109,4 s sin él (116 sesiones). Razonar frente a no razonar con 60 tareas solo
  detecta 16,5 puntos o más: no vale como prueba. Oculto frente a devuelto costaría 22 a 27 h con un efecto
  esperado menor: no correrlo. **Siguen comparables las 29 sesiones con razonamiento; las 116 del kit de base y
  las lecturas 0,05 y 0,06 ya no.** La tabla pública no muestra cambio de nivel tras el 2026-10-09 (de 1 149
  equipos sin envío nuevo, ninguno cambió de nota), pero como guarda la mejor nota, no prueba nada.
- **QA:** de 31 sesiones resueltas, 0 dependían de tocar pruebas o configuración; el filtro nuevo del arnés
  vaciaría 2 entregas no resueltas de 82. En las 19 tareas comunes, razonar tarda 276 s frente a 82 s.
- **Inteligencia pública:** las páginas vivas y el foro no se dejan leer sin sesión; lo último leído es de una
  hora antes de la actualización. El 2026-09-29 el organizador dijo que no repuntúa envíos existentes y que
  los arreglos llegan en silencio con el conjunto de ruedas. El 2026-10-02 un participante pidió que
  `include_thoughts` no apagara el razonamiento: coincide con el cambio, sin anuncio conocido.

**Decisión, limitada al primer paso (unánime en la ronda 1):**
1. **Sondeo de 12 tareas con el kit de base** (`cs4all/iteracion-08-s1`), cuando el notebook corregido tenga
   ensayo local con `ipykernel` 6.17.1, prueba con las ruedas reales, chequeo previo nuevo y revisión
   independiente. Regla de lectura: rediseñar en porciones si la media pasa de 120 s por tarea; parar y volver
   al concilio si pasa de 270 s o si más de la mitad se corta por tiempo.
2. **El envío diario sigue con el zip `65a02160…`** (su petición es idéntica en las dos versiones), rotulando
   cada lectura con su fecha; las dos anteriores no se promedian con las nuevas.
3. **Releer el foro y los notebooks públicos desde el 2026-10-09** antes de gastar la cuota (en curso, solo
   lectura).

**Lo que queda sin decidir, a propósito:** qué se corre después del sondeo. Ahí los roles discrepan
(arquitecto: kit sin razonar de 60 tareas y las otras cuatro porciones de la base; analista: no correr razonar
frente a no razonar como prueba). **La revisión cruzada y el dictamen del auditor se hacen con el dato del
sondeo**, que es lo que cambia la respuesta.

**Foro releído (lectura del 2026-10-12 por la API, 202 temas; informe en `…ase2\concilio_45\inteligenciaoro_2026-10-12.md`).** Lo que cambia o confirma:

- **El cambio del razonamiento fue intencional.** Organizador, 2026-10-10 12:31: «This was intended. […] This change was meant to have include_thoughts manage what is carried in the chat template from call to call, more consistent with the Gemini API.» Prometió una actualización y un README para hoy; no está en la lectura.
- **Otro participante midió lo mismo que nuestra prueba local** (con 0.2.13 la petición lleva el razonamiento encendido aunque `include_thoughts` sea falso; con `thinking_budget: 0` se apaga) y, en una tarea, pasó de unos 90 s a 316 s: unas 3,5 veces más. Es un caso ajeno, una tarea.
- **El `ModuleNotFoundError` de `swegemma.models.discovery` se reportó en el foro el 2026-10-09 a las 16:20**, hora y media después de la actualización. Estaba a la vista tres días antes de nuestra subida.
- **Puntuador:** no está dicho desde cuándo usa las ruedas nuevas; el organizador dijo de otro cambio (2026-10-11) «The scorer has this update already», de donde se infiere que sigue al conjunto de ruedas. Sin repuntuación anunciada.
- **Cola de envíos:** varios participantes reportan de 22 a 46 h entre el envío y la nota, y el límite de pendientes sigue en vigor: **el «envío diario» en la práctica será uno cada día y medio o dos.** La cola no cuenta para las 12 h.
- **Modelos:** desde el 2026-10-11 se permiten tres variantes más pequeñas (12b, e4b y e2b), sin mezclar en un envío; hardware, 12 h y topes, iguales.
- Las respuestas de los roles a D4 se mantienen: seguir con el mismo zip, no alternar todavía, no parar.

### Arreglo fusionado y sondeo subido (2026-10-12, 08:38 a 08:48 UTC)

- **PR #196 (issue #195) fusionado**, `mergedAt` 08:38:47, `2c1f05f`, CI 12 de 12. Revisión independiente: PR «apto con observaciones»; sondeo «listo con salvedades». El chequeo previo compara ahora las versiones del conjunto de ruedas con las ensayadas y comprueba los imports del notebook contra las ruedas reales; sin las ruedas no dice «se puede subir». El ensayo rearmado pasó 7 de 7 corridas con las ruedas reales. Predicciones: 48 no ocurrió, 49 ocurrió, 50 no ocurrió.
- **Antes de subir:** listado del conjunto de ruedas releído a las 08:40, sin cambios desde las 07:07 (las del arnés, del 2026-10-09 14:43); cuota 29,93 h; hash del notebook igual al revisado (`9ea5149a…`); `kaggle_preflight comprobar --tope-min 160 --ruedas … --listado …`: 24 de 24 en verde, código 0.
- **08:39:19 — sondeo subido:** `uvx kaggle kernels push -p …/issue_195_2026-10-12/iteracion_08_razona/kernel_iteracion_08_s1 -t 9600 --accelerator NvidiaL4`. `cs4all/iteracion-08-s1`, versión 1. Doce tareas (la primera porción del sorteo) con el kit de base `d8a3e1d3…`, que con este arnés razona con el pensamiento oculto. Costo esperado 2,2 a 2,7 h; techo, 160 min de sesión.
- **08:41 a 08:48:** `RUNNING` en cinco lecturas seguidas; ya pasó el punto donde murió la pasada 1 (106 s). El log no se puede leer mientras corre.
- **Riesgo residual que el revisor dejó escrito** (lo que solo se ejecuta por primera vez en Kaggle): el servidor real del modelo; la guarda de versiones tras instalar las 41 ruedas; los enganches con `litellm` 1.82.4; si vLLM informa los tokens de razonamiento; el modelo real razonando; el subagente; 6 de las 12 tareas sin copia local; las novedades del arnés.
- **Regla de lectura del sondeo:** rediseñar en porciones si la media pasa de 120 s por tarea; parar y volver al concilio si pasa de 270 s o si más de la mitad se corta por tiempo.

### El sondeo terminó completo: 4 de 12 resueltas, 212 s por tarea (2026-10-12, 09:33 UTC)

`cs4all/iteracion-08-s1`: sesión completa (3 064 s de reloj; el registro termina en «cierre»; `kaggle_registro comprobar --notebook iteracion-08-s1 --tareas-esperadas 12` da código 0). Rescate nuevo en `…escate_kaggle�6-10-12T0940Z\`; salida en `…\instrumentos\issue_195_2026-10-12\salida_kaggle_s1\`. Solo agregados:

| Medida | Valor |
|---|---|
| Arnés instalado (lo escribe el notebook) | `swegemma` 0.2.11, `adk_submission` 0.2.13: las esperadas |
| Cuota gastada | 1,71 h (de 0,07 a 1,78); **factor 2,01** entre reloj y cuota; quedan 28,22 h |
| Carga del modelo | registro instalado a los 519 s de sesión |
| Resueltas | **4 de 12** |
| Clase de fin | resuelta 4; tiempo agotado sin parche 5; tiempo agotado con parche 1; llamadas agotadas sin parche 2 |
| Segundos por tarea | media **212,0** (censurada por el tope de 240 s); mediana 242,6; de 85,9 a 248,2 |
| Llamadas a herramientas por tarea | media 19,2; máximo 40 |
| Peticiones | 260; 7 canceladas por el tope; media 9,5 s por petición |
| Tokens de entrada por petición | media 8 530; máximo 18 252 |
| Razonamiento | 173 de 253 respuestas traen razonamiento (media 1 167 caracteres); vLLM no informó sus tokens aparte |
| Colgadas / errores del registro | 0 / 0 |

**Frente a la regla escrita antes de subir:** se cumple «rediseñar en porciones» (media sobre 120 s); no se cumple por la letra «parar» (la media no pasa de 270 s; los cortes por tiempo son 6 de 12, justo la mitad).

**Predicción 51** (el notebook rearmado falla en Kaggle por una causa que el ensayo local no vio; 0,30): **no ocurrió**.

**Cuenta que sale de aquí (inferida):** una porción de 12 tareas cuesta 1,71 h; las 60 del sorteo en cinco porciones, unas 8,5 h por condición. En 28,22 h caben unas tres condiciones completas.

Resumen para el concilio en `…ase2\concilio_45\sondeo_resultado.md`. Ronda 2 en curso (analista, arquitecto y QA con las trazas del sondeo); después, auditor.


### Concilio 45, ronda 2 y dictamen del auditor (2026-10-12)

**Ronda 2, con el dato del sondeo** (`…\fase2\concilio_45\<rol>\ronda2.md`). Los tres roles propusieron un
primer paso distinto:

- **Arquitecto:** completar las otras cuatro porciones de la misma condición (6,8 h) y después una condición
  sin razonar de 60 tareas (4,2 a 5,0 h) y su repetición. Cuenta del envío con unas 120 tareas ocultas: 7,2 a
  8,6 h con el kit de base a 4 min; 8,1 a 9,6 h con el de razonamiento a 4,5 min; 4,5 min sigue siendo el
  máximo defendible.
- **Analista:** repetir la porción con el tope en 5 min (1,9 a 2,4 h); él mismo lo llamó conjetura. Recontó el
  sondeo (se reproduce) y lo comparó con sesiones previas de las mismas tareas: solo 6 de 12 tienen
  antecedente sin razonar; en ellas el acierto no cambió (1 y 1) y el tiempo se multiplicó por 2,7 (de 82 a
  218 s). El 96 a 98 % del reloj son peticiones al modelo.
- **QA (leyó las trazas):** de las 8 no resueltas por tope, ninguna tenía una edición plausible en disco; de
  las 6 por tiempo, 4 avanzaban despacio y 2 giraban; dos gastaron unos 120 s en una sola respuesta de 4 000 a
  4 300 tokens; las 2 de llamadas agotadas son bucles de la misma lectura mal formada, que empiezan tras la
  primera compactación. Propuso bajar el presupuesto de razonamiento.

**El auditor reprodujo las cifras desde el registro crudo** (guiones en `…\concilio_45\auditor\`):

| Afirmación | Su número |
|---|---|
| 4 de 12 resueltas | Igual; intervalo del 95 %: 10 a 65 % |
| El modelo genera el 97 % del reloj | 2 471 de 2 544 s |
| «173 de 253 respuestas traen razonamiento» | **151** con más de 0 caracteres |
| «79 % de los tokens de salida es razonamiento» | **Entre 84 y 93 %** |
| «Bajar a 1 024 ahorra 28 s por tarea» | 27,4 s, el 90 % en 2 de 12 tareas; con 2 048, 14,3 s |
| Respuestas que agotan el presupuesto | 2 con 4 096 tokens o más; 3 con 4 000 o más |

Las dos cuentas del razonamiento miden cosas distintas y ambas valen: casi todo lo que el modelo escribe es
razonamiento, pero son 151 pensamientos cortos (mediana 255 tokens), así que **bajar el tope apenas ahorra; lo
único que mueve el reloj es apagarlo** (unos 150 a 170 s por tarea, en cuenta estática).

**Plan decidido** (tope propio de 20 h; el dueño fijó 24):

| Paso | Qué | Cuota (h) | Qué decide | Lo detiene |
|---|---|---|---|---|
| 0 | Kit sin razonar (una línea: `thinking_budget: 0`), ensayo local con ruedas reales, revisor | 0 | Que la petición salga con el razonamiento apagado 6 de 6 | Cualquier otra diferencia con el kit de base |
| 1 | Las mismas 12 tareas del sondeo con ese kit | 1,0 a 1,5 | Segundos y clases de fin sin razonar; el tamaño del paso 2. **No decide acierto** | Alguna petición que pida razonar (corrida inválida); una colgada; más de 1,7 h |
| 2 | Las otras 48, en una sesión si la media del paso 1 es 135 s o menos; si no, en dos de 24 | 3,2 a 4,1 | El nivel sin razonar con 60 tareas (±12 puntos) | Menos de 55 válidas |
| 3 | Repetir las 60 sin razonar | 4,2 a 5,6 | La discordancia entre pasadas iguales: el ruido del arnés nuevo | No empieza con más de 12 h acumuladas |
| 4 | Las otras cuatro porciones de la base que razona | 6,8 a 8,2 | 60 pares razonar frente a no razonar | Solo si la discordancia del paso 3 es 20 % o menos |

Total: 15,2 a 19,4 h. **Regla escrita antes de leer:** en el paso 4 solo una diferencia de 16,5 puntos o más
cambia el kit; por debajo se anota «exploratoria». Si las ruedas cambian, se para y vuelve al concilio.

**Vetos del auditor (no se corre esta semana):** repetir las 12 con 5 min (el concilio 43 vetó los 5 min en el
envío y la cuenta de las 12 h lo confirma; y son 6 tareas sin medida de ruido); presupuesto a 2 048 o 1 024
(toca 3 respuestas en 2 tareas; con 12 pares no hay mínimo detectable); el razonamiento devuelto en local (8,5
a 10 h, tres ajustes distintos, sin dato previo); subir a 4,5 min y repetir la base que razona (no caben).

**Envío:** seguir con `65a02160…`; no cambiar al kit de base (4 de 12 con 6 cortadas no es evidencia de mejora
y es el kit cuya conducta cambió); un envío en cuanto vuelve la nota, rotulado con su fecha; 0,08 y 0,13 no se
promedian con las nuevas. Un kit retador entra tras cinco lecturas posteriores al cambio y solo si ganó un
contraste local por 16,5 puntos o más. Antes de fijar los finales (propone el 2026-11-25): saber qué arnés usa
el puntuador, que la lectura 3 vuelva, la dispersión de cinco lecturas y que las ruedas no cambien después.

**Fallos de método que señala:**
- **Del orquestador:** la regla «parar si la media pasa de 270 s» era **inalcanzable** con un tope de 240 s; el
  otro criterio quedó en el borde exacto. Y el sondeo estaba en la lista de candidatas que yo escribí, con una
  duda que preguntaba «qué porción conviene correr primero»: la unanimidad de la ronda 1 vale como un voto
  anclado, no como cuatro. No invalida (el gasto fue bajo y el dato útil).
- **De los roles:** se sigue usando como «base» lo que dejó de serlo (las 116 sesiones, las lecturas 0,05 y
  0,06, los 109 s por tarea y el «tres veces más lento»); el 79 % era un supuesto; la comparación de bucles
  cruza arneses.
- **Del propio auditor:** no reprodujo lo que depende de las trazas; los ahorros por tope suponen la misma
  trayectoria.

**Lo que espera la palabra del dueño** (una sola cosa; redacción del auditor): la siguiente subida es el
notebook del sondeo con las mismas 12 tareas, cambiando solo el kit: el de base con `thinking_budget: 0`.
Cuesta 1,0 a 1,5 h de cuota (se corta a 1,7). Dice cuánto tarda y cómo termina una tarea sin razonar con el
arnés nuevo; no dice cuál kit acierta más. Pierde valor si las ruedas dejan de ser 0.2.11 / 0.2.13, y después
del 2026-10-15 ya no caben detrás los pasos siguientes antes del 2026-10-17 a las 00:00 UTC.

**En curso (paso 0, sin subir nada):** el implementador arma el kit sin razonar y su notebook, lo prueba con las
ruedas reales y lo ensaya; después, revisor.

### Paso 0 del concilio 45 cerrado; el paso 1 espera la orden del dueño (2026-10-12, 10:26 UTC)

- **PR #197 fusionado** (`mergedAt` 10:24:23, `756e2c2`, CI 12 de 12). Revisión independiente: PR «apto con observaciones»; notebook `s2` con el kit `A0`, «listo para subirse».
- **Kit `A0`** (`submission_a0_sin_razonar.zip`, sha256 `01a6d82f…`): idéntico al de base salvo la línea 5 de `configs/sampling.yaml` (`thinking_budget: 4096` → `0`). Prueba con las ruedas reales, recontada por el revisor: con el arnés nuevo, 6 de 6 peticiones con `enable_thinking: false` y sin presupuesto; temperatura, `top_p` y tokens máximos, iguales. Leído en el arnés: un 0 no se sustituye por el valor por defecto.
- **Notebook `s2`** (`…\issue_195_2026-10-12\paso0\kernel_iteracion_08_s2\`, sha256 `e8a5604c…`): 7 líneas distintas de `s1`, todas de condición o nombres; las mismas 12 tareas.
- **Regla de validez nueva:** `kaggle_registro comprobar --sin-razonar` sale con 8 si alguna petición pide razonar.
- **Comprobado a las 10:25, listo para subir:** ruedas sin cambios; chequeo previo con código 0; cuota 28,22 h; el envío del día sigue `PENDING`.
- **Orden que se ejecutará cuando el dueño lo diga:** `uvx kaggle kernels push -p …/issue_195_2026-10-12/paso0/kernel_iteracion_08_s2 -t 9600 --accelerator NvidiaL4` (costo esperado 1,0 a 1,5 h; se corta a 1,7 h). **No se subió.**
- Lo que nadie ha medido: qué hace el modelo real con el razonamiento apagado bajo el arnés nuevo. Es lo que viene a medir el paso 1.


### Paso 1 del concilio 45 subido por orden del dueño (2026-10-12, 13:53 UTC)

El dueño dijo «adelante» a la subida presentada (12 tareas, kit `A0` sin razonar, 1,0 a 1,5 h; corte a 1,7 h).

- **Antes de subir, releído:**
  - Ruedas del arnés (12:27 UTC, `listado_ruedas_1227.txt`): `swegemma` 0.2.11, `adk_submission` 0.2.13, `adk_eval_core` 0.1.0 y `google_adk` 1.36.1, con el mismo tamaño y fecha (2026-10-09 14:43). El conjunto sigue con `lastUpdated` 2026-10-09 14:43:19 (releído a las 13:55).
  - **Diferencia del listado, explicada:** el de las 12:27 trae una fila más, `tokenizers-0.22.2`, con la misma fecha de creación que el resto. No es un cambio del conjunto: sin `--page-size` el cliente devuelve 19 ruedas; con 100 o más, 41. El sondeo `s1` ya la había anotado en su `versiones_arnes_…json`. Los listados de las 07:07, 08:40 y 10:25 estaban incompletos por una fila. Pendiente: que el listado del chequeo previo se pida siempre con página grande y se cuente.
  - Chequeo previo con ese listado: código 0, «Se puede subir» (16 imports presentes en las ruedas). Notebook `e8a5604c…`, sin cambios.
  - Foro (12:34 UTC, `publicos_2026-10-12_1230\`): 185 temas (dos nuevos, tres con comentarios nuevos). Ningún anuncio de cambio del arnés. El organizador respondió a las 11:05: el `eval_config.yaml` del participante no afecta a la puntuación (el puntuador solo recibe los parches); las pruebas del puntuador corren con tope de 300 s; el puntuador usa **«el mismo sandbox pero ruedas distintas»**; las tareas ocultas se filtraron con un modelo comercial fuerte (las que resolvió o falló por una aserción). Queda sin respuesta si los topes de `evaluation:` rigen en la fase del agente.
  - Cuota: 1,78 h usadas, 28,22 h restantes. Envío 57098570: sigue `PENDING`.
- **Subida:** `uvx kaggle kernels push -p …/issue_195_2026-10-12/paso0/kernel_iteracion_08_s2 -t 9600 --accelerator NvidiaL4`.
  - 12:38:28 y 12:39:38 UTC: Kaggle respondió `500 Internal Server Error` en `SaveKernel`. No se creó el notebook (`GetKernelSessionStatus` 404) ni se gastó cuota (1,78 h). La carpeta difiere de la de `s1`, que subió bien, solo en el nombre y los finales de línea del `kernel-metadata.json`. Causa: del lado de Kaggle, no reconstruida; en la lista de notebooks aparece una fila sin nombre («[Private Notebook]», sin fecha de ejecución) que no sé si es anterior.
  - 13:53:18 UTC: tercer intento, sin cambiar nada: «Kernel version 1 successfully pushed». Estado a los 30 s: `QUEUED`.
- **Regla de lectura (del dictamen, escrita antes):** inválida si alguna petición pide razonar (`kaggle_registro comprobar --sin-razonar`, código 8), si hay una colgada o si pasa de 1,7 h. Decide segundos y clases de fin sin razonar y el tamaño del paso 2 (una sesión de 48 si la media es 135 s o menos; si no, dos de 24). **No decide acierto.**


### Cierre de sesión por orden del dueño (2026-10-12, 13:58 UTC)

El dueño pidió cerrar y actualizar la documentación, incluido el paper. No se lanzó trabajo nuevo; el vigía de estado se detuvo.

**Estado en Kaggle al cierre (leído, no supuesto):**
- `cs4all/iteracion-08-s2` (paso 1: 12 tareas, kit `A0` sin razonar): `KernelWorkerStatus.RUNNING`. Subido a las 13:53:18 UTC. **Corre solo; nadie lo está mirando.** Tope de sesión 9 600 s.
- Cuota de GPU: 1.82h usadas, 28.18h restantes.
- Envío 57098570 (zip `65a02160…`, lectura 3 de 5): `SubmissionStatus.PENDING `.

**Al retomar, en este orden:**
1. `uvx kaggle kernels status cs4all/iteracion-08-s2` (con `PYTHONUTF8=1`).
2. Si terminó: bajar la salida a `…\issue_195_2026-10-12\salida_kaggle_s2\`, rescate, `python -m scripts.kaggle_registro comprobar --sin-razonar --notebook iteracion-08-s2 --tareas-esperadas 12` (código 8 = alguna petición pidió razonar: corrida inválida), leer solo agregados (el lector `leer_sondeo.py` busca `iteracion_08_s1.json`: hay que pasarle el nombre nuevo), `uvx kaggle quota` y anotar el factor.
3. Si dio error: log extraído y causa reconstruida antes de cualquier otra cosa (forense).
4. Paso 2 (las otras 48): una sesión si la media del paso 1 es 135 s o menos; si no, dos de 24. Necesita ensayo local, releer ruedas y foro, y la palabra del dueño. Después del 2026-10-15 ya no caben detrás los pasos 3 y 4 antes del 2026-10-17 a las 00:00 UTC.
5. Envío: cuando 57098570 tenga nota, anotarla con su fecha y hacer la lectura siguiente del mismo zip (con la palabra del dueño); actualizar `sub-008` en `submissions/registry.json` por PR.

**Documentación actualizada en este cierre:**
- Esta bitácora (subida del paso 1 y cierre).
- Paper: versión nueva `experiments\gemma_developer_agent\drafts\paper\manuscript_defendible_2026-10-12.md` (sin versionar, **borrador no publicado**; la del 2026-10-04 queda intacta). Cambios: ya no dice que Gemma 4 no se ejecutó; § 4.1 nuevo con las notas públicas, el cambio del arnés del 2026-10-09 (la línea de base preregistrada ya no describe lo que el arnés hace: necesita enmienda), el sondeo de 12 tareas y el paso en curso; tres amenazas nuevas; y **se corrigió la lectura del placebo del § 3**, que decía lo contrario de `docs/results/failure-transfer.md` (H7c: el contenido importa en cuatro de seis casos). Guion de los cambios: `…\fase2\lanzamiento\actualizar_paper.py`.
- Cuaderno del concilio (`.scratch\concilio_memoria\CUADERNO.md`), memoria del proyecto e issue #182.

**No hecho, queda escrito como pendiente (requiere PR con revisión, no cabe en un cierre):**
- Documentos versionados: `docs/ensayo_nucleo_jupyter.md` y `docs/rescate_kaggle.md` no recogen aún que el listado de ruedas hay que pedirlo con página grande (sin `--page-size` salen 19 de 41 ruedas; los listados de las 07:07, 08:40 y 10:25 perdían una fila) ni la subida del paso 1. `kaggle_rescate` y el chequeo previo deberían contar las filas del listado.
- El paper nuevo no ha pasado por validador estadístico, auditor de datos, investigador de citas ni redactor; antes de publicarlo o versionarlo, pasa por ellos. La Tabla 3 y las cifras del § 4.1 salen de la API y del sondeo recontado por el auditor del concilio 45; la frase sobre las predicciones P2 y P3 es descripción, no contraste.
- La enmienda al preregistro por el cambio del arnés (línea de base con `thinking_budget: 0` o declarada «razona») no está escrita.
- Causa de los dos `500` de `SaveKernel`: no reconstruida.
- Siguen abiertos: #179 sin confirmar, #182, confirmación de cierre de #195, predicciones 25 a 37 y 41, seguimiento del gancho del #186, y los candidatos a issue de la vuelta 44.


## Vuelta 45 — 2026-10-12 (UTC), tarde: el paso 1 terminó y las ruedas cambiaron

### Retomar: salida del paso 1 rescatada (2026-10-12, 20:45 a 20:55 UTC)

Orden del dueño: «sigue con la primera: las 60 tareas de Kaggle» (la primera de tres salidas que dejó el
concilio cuantitativo de memoria, ver más abajo) y «evalúa junto al concilio los resultados».

- `cs4all/iteracion-08-s2`: `COMPLETE`. Salida bajada a `…\issue_195_2026-10-12\salida_kaggle_s2\` y rescate
  completo por la API en `…\rescate_kaggle\2026-10-12T2051Z\2026-10-12T2051Z\` (código 4: 145 faltantes, ninguno
  de `s1` ni de `s2` según el forense).
- `uvx kaggle quota` (leída por el orquestador a las 20:47 UTC): 2,77 h usadas, 27,23 h restantes; renovación
  2026-10-17 00:00 UTC. Con 1,78 h antes de subir, `s2` costó 0,99 h: factor 2,013 sobre los 1 770,5 s del log.
- Envío 57098570: sigue `PENDING` (más de 14 h).
- `kaggle_registro comprobar --sin-razonar --notebook iteracion-08-s2 --tareas-esperadas 12`: «completa», 408
  peticiones piden no razonar, 0 piden razonar, 0 sin el dato. Regla «sin razonar» cumplida.
- No se subió ni se envió nada.

### Concilio 46 (2026-10-12): cinco roles, revisión cruzada sin firmas y auditor

Expediente: `F:\Code\Agents Learning Loops\.scratch\concilio_memoria\fase2\concilio_46\` (encargo con las frases
del dueño literales, prompts de las dos rondas y del auditor en `prompts\`, un informe y una `ronda2.md` por
rol con sus guiones, y `auditor\dictamen.md`). El orquestador no ocupó ningún rol ni votó.

**Parecer del auditor, tal cual (su resumen):**

> El paso 1 es válido según la regla escrita antes: 408 de 408 peticiones sin pedir razonar, 0 colgadas, media
> de 101,0 s por tarea. La regla manda una sesión para el paso 2, pero la misma regla manda parar si cambian
> las ruedas, y cambiaron a las 19:51 UTC: `swegemma` creció 150 bytes y `vllm` 198, con la misma versión. `s2`
> corrió antes, con las anteriores.
>
> El veto unánime a subir se sostiene. Lo levanta el diff de contenido; de `vllm` vieja no hay copia local, así
> que recomiendo que el paso 2 sean 60 tareas con las ruedas nuevas (3,7 h de cuota) y después su repetición
> (3,7 h). El paso 4 no se presenta esta semana.
>
> Tres roles dieron horas de reloj como cuota; el factor es 2,0, medido una sola vez. Quedan unas 27,2 h,
> inferidas: nadie leyó la cuota. Ninguna predicción fechada cubría el paso 1.
>
> Con 12 pares no se detecta nada; con 60, 16 puntos solo si la discordancia es 0,2.
>
> Para el dueño: ninguna cosa lista todavía. Faltan la lectura de cuota, el diff, el paso 0 con las ruedas
> nuevas, y las definiciones y predicciones escritas por analista y forense.

(La cuota sí estaba leída; el orquestador no la puso en el encargo. El auditor lo añadió como nota.)

**Lo que cada rol midió (ronda 1) y lo que retiró (ronda 2):**

- **Analista:** con 12 pares no se detecta ninguna diferencia de acierto; `s2` fue más rápida en 12 de 12
  tareas; una petición rechazada por ventana de contexto que la herramienta no marca. Retiró sus cifras de
  cuota (eran reloj) y «31 veces» sobre la lectura repetida.
- **Forense:** las ruedas se republicaron a las 19:51 UTC; la guarda del notebook compara versiones y no
  bytes; cuatro finales anómalos sin corte. Retiró que la compactación hiciera perder el enunciado en dos
  tareas (esos enunciados no traían el problema) y su «1,5 h» del paso 2 (era reloj).
- **QA:** sin razonar el límite activo son las 40 llamadas; las lecturas mal formadas empiezan en la llamada 2
  en cuatro tareas, antes de cualquier compactación (contradice al concilio 45). Corrigió sus horas a cuota.
- **Arquitecto:** los pasos 2 a 4 caben en la cuota. Retiró «el plan cabe» como permiso para seguir, al ver el
  cambio de ruedas que se le había pasado.
- **Inteligencia pública:** mismo cambio de bytes, por otro guion; el mismo zip ya dio 0,08 y 0,13. Retiró «7
  cortes por tiempo en `s1`» (son 6). No pudo leer el foro posterior a las 12:05 UTC sin sesión.

**Correcciones del auditor a cifras de los roles:** 7 tareas con 35 o más llamadas (no 8); las lecturas
repetidas antes del rechazo son 11 seguidas (no 7 ni 31); «`s1` y `s2` idénticas byte a byte» queda en
«tamaños iguales» (no se registró sha256). El auditor no rehízo lo que sale de las trazas.

**Plan del auditor** (pasos 1 a 4 sin cuota y sin la palabra del dueño; 5 y 6 la necesitan):
1. Leer la cuota (hecho). 2. Bajar las ruedas nuevas, sha256 y diff. 3. Guarda por sha256 en el notebook y
paso 0 repetido con las ruedas nuevas, con revisor. 4. Definiciones («válida», «corte», «discordante», unidad
de costo) y predicciones fechadas, escritas por analista y forense. 5. Las 60 tareas en una sesión, kit `A0`,
ruedas nuevas: 3,7 h (2,7 a 4,7). 6. Repetir las 60: 3,7 h. El paso de comparar con el kit que razona no se
presenta esta semana (es el más caro y está confundido: un brazo lo corta el reloj y el otro las llamadas).

**Fallos del orquestador en esta vuelta (lista del auditor):** retuvo la lectura de cuota y cinco informes la
infirieron; dijo que el encargo no traía conclusiones y traía la suya sobre el paso 3 más el plan como marco
(el orden 2 → 3 → 4 vale como un voto anclado, no cinco); convocó con un rescate que ya traía el listado nuevo
de ruedas sin que nada avisara; no hubo predicción fechada antes del paso 1 (las 48 a 51 no están en el
archivo versionado); no hizo cumplir el tope de palabras; la ronda 2 duró de 60 a 103 s por rol, poco para
rehacer cuentas. De la herramienta: dice «completa» con un 400 dentro y rotula como «con caracteres de
razonamiento: 225» respuestas que traen el campo vacío.

### Paso 2 del dictamen: las ruedas nuevas, bajadas y comparadas (2026-10-12, hacia las 21:20 UTC)

Orden del dueño: «sigue con los pasos 2 a 4 del auditor». Carpeta: `…\instrumentos\arnes_2026-10-12_1951\`.

- Bajadas del conjunto `metric/gemma-4-developer-agent-wheelhouse` las cuatro ruedas del arnés. sha256 frente a
  la copia local que corrió en `s1` y `s2`: `google_adk` igual; `swegemma`, `adk_submission` y `adk_eval_core`
  distintos.
- Contenido, archivo por archivo: `adk_submission` y `adk_eval_core` son **idénticos** (solo cambió el
  empaquetado; mismo tamaño). **`swegemma` cambió de código** en cinco archivos (`budget.py`, `cli.py`,
  `config.py`, `context.py`, `harness/verification.py`): añade `verification_timeout_seconds`, por defecto 300,
  y la verificación con pytest deja de usar el tope de cada orden y usa ese. Diff completo en
  `diff_swegemma_0951_vs_1951.diff` (98 líneas).
- Lectura del orquestador, **sin comprobar por otro todavía**: no toca al agente, a la compactación ni al
  servidor; toca cuánto tiempo tiene la verificación. Si en `s1` o `s2` alguna verificación se cortó por el
  tope anterior, su «resuelta» pudo salir distinta. Encargado al forense.
- `vllm` nueva no se bajó (433 MB) y de la anterior no hay copia: su cambio de 198 bytes sigue sin medir.
- Con la regla del dictamen («48 solo con empaquetado puro probado en las dos»), el paso siguiente son **60
  tareas con las ruedas nuevas**, y `s1` y `s2` quedan rotuladas «ruedas del 2026-10-09».
- **En curso, sin subir nada:** forense (comprobar el diff y su efecto en `s1` y `s2`, y sus predicciones),
  analista (definiciones y predicciones fechadas) e implementador (guarda por sha256, notebook de 60 y paso 0
  repetido, por PR con `Refs #182`). Encargos literales en `…\concilio_46\prompts\pasos_2_a_4.md`.

### Pasos 2 a 4 del dictamen y cierre de sesión por orden del dueño (2026-10-12, 21:40 UTC)

El dueño pidió cerrar y documentar, sin crear más tareas. Se detuvieron el implementador y la espera de CI.
**No se subió ni se envió nada a Kaggle en toda la tarde.** No queda ningún agente corriendo.

**Paso 2, cerrado.** El forense rehízo la comparación de ruedas por su cuenta y coincide con la del
orquestador (`…\concilio_46\forense\paso2_ruedas.md`): `google_adk` igual; `adk_submission` y `adk_eval_core`,
solo empaquetado; `swegemma` cambia el código, y solo la verificación: el tope de pytest pasa de 60 s (lo que
configuró el notebook en `s1` y `s2`) a 300 s por defecto. Ninguna verificación de `s1` ni de `s2` terminó por
ese tope (la más larga, 4,0 s): para las 12 tareas medidas el cambio es inerte; para las otras 48 no está
medido. `vllm`: sin medir. La regla manda **60 tareas con las ruedas nuevas**.

**Paso 4, escrito y revisado; falta fusionarlo.** PR #200 (rama `issue-182-predicciones-concilio-46`, cabeza
`d824e8a`): sección 20 de `experiments/azar/preregistro/prediccion_de_fallos.md` con las definiciones
(«válida», «corte», «discordante», unidad de costo), la puerta escrita sobre el conteo y las predicciones 52 a
65 (analista) y 66 a 73 (forense), copiadas tal cual, más dos notas de precisiones de los propios autores
tras la revisión, sin cambiar probabilidades. Fechadas 21:19 a 21:31 UTC, antes de cualquier dato. El revisor
independiente aprobó en la tercera pasada. **Al cerrar, la CI iba 3 de 12 con 9 corriendo: no se fusionó.**

**Paso 3, a medias: NO está hecho.** El implementador (rama `issue-182-guarda-sha256-ruedas`, worktree
`.claude\worktrees\agent-a0a0d5a3887c12502`, sin commits ni PR) fue detenido cuando empezaba a escribir
código. No existe todavía la guarda por sha256, ni el notebook de 60 tareas, ni el paso 0 repetido con las
ruedas nuevas. Su encargo literal está en `…\concilio_46\prompts\pasos_2_a_4.md`.

**Lo que espera la palabra del dueño: nada todavía.** Cuando el paso 3 esté hecho, ensayado y revisado, la
subida se presentará con la redacción del auditor: 60 tareas del sorteo, kit `A0` sin razonar, ruedas del
2026-10-12 19:51 UTC con sha256 comprobado; unas 3,7 h de cuota, corte a 5,4 h; dice el nivel sin razonar con
±11 puntos; no compara kits.

**Estado en Kaggle, leído a las 20:47 UTC y no releído al cierre:** cuota 2,77 h usadas, 27,23 h restantes,
renovación 2026-10-17 00:00 UTC; envío 57098570 `PENDING`.

**Al retomar, en este orden:**
1. PR #200: comprobar la CI de `d824e8a`; si está 12 de 12, fusionar y verificar `mergedAt`.
2. Releer el listado de ruedas (`--page-size 200`) y comparar sha256 con
   `…\instrumentos\arnes_2026-10-12_1951\sha256_ruedas_1951.txt`. Si cambió otra vez, vuelve al concilio.
3. Relanzar el paso 3 con el mismo encargo (mirar antes qué dejó el worktree del implementador).
4. Para que las predicciones 65 y 71 sean evaluables, **copiar en esta bitácora la salida literal de cada
   orden `kernels push`**; y leer `uvx kaggle quota` justo antes del push y tras `complete` (predicción 60).
5. Episodio de la vuelta en `learning/episodes/` (no escrito).

**Otra línea cerrada hoy (memoria selectiva):** concilio cuantitativo de ocho roles con auditor; PR #199
fusionado (`0db6c49`) con el pre-registro de un predicado de alcance y su informe, veredicto INSUFICIENTE: los
operadores del solver acotado solo actúan en seis sitios de la aplicación y el banco nuevo no se escribió.
Issue #198 abierto. Expediente en `.scratch\concilio_cuantitativo\`. De ahí salió la orden del dueño de usar
las 60 tareas de Kaggle como población.

---

## Vuelta 46 — 2026-10-12 y 13 (UTC): la nota no bajó, el puesto sí; staff de construcción y bloque R1 listo sin subir

**Nada se subió ni se envió a Kaggle en esta vuelta.** El envío 57098570 seguía PENDING en la última lectura
(no es anómalo antes del 2026-10-14 05:00 UTC).

### Lo hecho, con su prueba

| Qué | Dónde | Estado |
|---|---|---|
| Predicciones 52 a 73 (concilio 46) | PR #200, `0d3725f` | Fusionado |
| Guarda por sha256 de las ruedas y notebook de 60 tareas ensayado en Docker | PR #201, `52eb0f0` | Fusionado |
| Sección 21: definición del «cerrojo» del auditor y predicciones 74 a 83 | PR #204, `ea3ab21` | Fusionado |
| Staff de construcción: estratega, diseñador del agente, calibrador, constructor del kit; los revisores publican su revisión en GitHub | PR #203, `acca047`, issue #202 | Fusionado y **verificado** (los cuatro tipos cargaron; un revisor publicó solo en el PR #208) |
| Sección 22: predicciones 84 a 98 del bloque R1 | PR #207, `a5302f6` | Fusionado |
| Cuatro candidatos de kit y seis notebooks de R1, ensayados en Docker | PR #209, `8dae1bb`, issue #205 | Fusionado; issue abierto hasta correr y leer |
| Secciones 22.5 (precisiones del diseñador) y 22.6 (orden de tandas y regla de parada) | PR #211 | Aprobado dos veces; esperando CI |
| La guarda de cuentas falla abierta | PR #208, issue #206 | Cambios requeridos; en arreglo |
| Caminos de la guarda fuera del #206 | Issue #210 | Abierto, sin empezar |

### Concilio 47: qué se midió y qué se decidió

- **Medido:** la nota sigue en 0,13 (8 de 58) y el puesto pasó de 544 a 864. Desde el 2026-10-07 no hay un
  envío puntuado. Los kits públicos llegan a 0,18; el mejor es nuestro kit que razona con tres cambios, y su
  0,18 es el máximo de seis o más lecturas (ventaja probable: 1,5 a 2,5 tareas). El ruido entre dos envíos
  idénticos es de unas 1,6 tareas.
- **Regla que cambia el plan:** el puesto final lo decide la tabla privada con hasta dos envíos elegidos.
  Reenviar el mismo zip solo sube el máximo público.
- **Dictamen y adenda del auditor:** 12 tareas locales filtran seguridad, no calidad; la calidad se lee en la
  tabla, un candidato por envío. Hallazgo retirado: el «cerrojo de lectura» (p = 0,13, confundido, 0 de 29 en
  el kit que razona).
- **Regla de envío, literal:** «el primer candidato, en este orden, revisado, ensayado en Docker, con media de
  262 s o menos en R1, ninguna colgada y neto de −1 o mejor frente a la base. Si ninguno está listo, no se
  reenvía la base.»
- **Candidatos, en orden:** C1 tres cambios a 6 min (28 llamadas, 240 s por orden, sin subagente, grafo
  prohibido, edición temprana); C2 edición temprana sola; C3 `thinking_budget` 1 536; C4 triaje de enunciado
  corto. **No construir:** quitar `read_file`, reglas de lectura sobre el kit sin razonar, 8 minutos,
  adaptadores, copia literal del kit público.

### El bloque R1, tal como quedó

- Artefactos, con 330 huellas comprobadas: `experiments\gemma_developer_agent\data\rescate_kaggle\instrumentos\issue_205_bloque_r1\`.
  Zips: C1 `a038a389…`, C2 `aa0750f0…`, C3 `e655e942…`, C4 `8e7009dd…`; base `65a02160…`.
  Notebooks `iteracion-08-br1-{i1,i2,c1,c2,c3,c4}`.
- **Revisión de código (5497999068):** aprobar. Bases y C2, listos; C1, C3 y C4, listos con reservas (C1: aviso
  de presupuesto desde la llamada 18; C3: subagente con 1 536 sin ensayar; C4: resuelto en 22.5).
- **Cuota (estratega, rehecha):** 11,1 a 12,1 h esperadas, techo 13,4 h. La cuenta anterior (10,40 a 11,39 h)
  partía de `s1`, que corrió otro kit a 4 min y 40 llamadas. **No hay ninguna pasada de la base con el arnés
  nuevo: toda la cuenta es proyección.** La semana cabe sin recortes (27,23 h en la lectura de las 00:44 UTC).
- **Tandas:** i1 + c1; c2 + c3; i2 + c4. **Parada entre tandas:** una colgada, guarda de ruedas, sesión sobre
  3 830 s (c1: 4 910 s), tanda sobre 4,9 h (4,3 h las otras), o i1 con 0 o 1 resueltas. Si i1 baja de
  29 tokens/s, las restantes van de una en una. Texto literal en la sección 22.6 del pre-registro.
- **El contador:** `llamadas_herramientas` cuenta solo las llamadas que gastan presupuesto; la traza las cuenta
  todas (28 contra 33 en el ensayo del corte de C1).
- **Sin ensayar:** si el modelo real obedece las instrucciones, si el servidor aplica el 1 536, las duraciones
  por tarea, 6 de las 12 tareas (sin copia local) y la instalación real de las ruedas.

### Obligaciones al subir (si el dueño da la orden)

1. Chequeo previo con el listado de ruedas del día, antes de **cada** tanda.
2. `uvx kaggle quota` justo antes del primer `kernels push` y tras cada `complete`; ninguna otra sesión de GPU
   en medio (predicción 91).
3. Copiar aquí la salida literal de cada `kernels push`.
4. Rescatar el zip crudo de cada sesión: las predicciones marcadas (T) se leen en las trazas.
5. Aplicar la regla de parada de 22.6 tras cada tanda, antes de lanzar la siguiente.

### Fallos del orquestador en esta vuelta

- Fusioné los PR #199 y #200 sin ninguna revisión publicada en GitHub. El dueño lo corrigió: una aprobación
  dicha en el chat no cuenta.
- Destaqué el «cerrojo de lectura» como mejor candidato antes de que el auditor lo midiera; se retiró.
- Sembré el encuadre en varios encargos del concilio (nombrar un hallazgo en el encargo, elegir yo los 18
  notebooks). Lo señaló el auditor.
- Di por cierta la cuenta de cuota del constructor sin mirar de qué corrida salía; lo encontró el revisor.
- Escribí en una nota del pre-registro que una revisión «no encontró ambigua» ninguna predicción del analista,
  cuando no las había examinado; lo encontró el revisor.
- La guarda de cuentas no me protegía: mis órdenes empiezan con `cd`, y esa forma pasa siempre (47 de 47
  «pasa-dudoso» en el registro). Lo que evitó errores fue fijar y comprobar la cuenta a mano.

### Al retomar

1. PR #211: fusionar con CI 12 de 12 y verificar `mergedAt`.
2. PR #208: revisión sobre la cabeza nueva, publicada por el revisor; fusionar con CI en verde.
3. Presentar al dueño **una cosa**: la subida del bloque R1 (techo de 13,4 h de cuota).
4. Episodio de la vuelta en `learning/episodes/` (no escrito).
5. Sin decidir por el dueño: la propuesta de cambio a `AGENTS.md` y `CLAUDE.md`; cómputo local o de pago.

### Subida de la tanda 1 de R1, por orden del dueño (2026-10-13, 12:19 UTC)

El dueño escribió «Adelante, sube el bloque R1». Lectura completa en experiments/gemma_developer_agent/data/rescate_kaggle/lecturas_envios\subida_r1_tanda1_2026-10-13T1218Z.txt (dentro del repositorio). Salida literal:

```
== 2026-10-13T1218Z tanda 1: i1 + c1
huellas_ok
listado_igual
preflight i1 0
preflight c1 0
== quota antes
resource  used   remaining  total   refreshAt            
--------  -----  ---------  ------  -------------------  
GPU       2.77h  27.23h     30.00h  2026-10-17T00:00:00  
TPU       0.00h  20.00h     20.00h  2026-10-17T00:00:00  
== kernels en curso
ref                              title                     author  lastRunTime                 totalVotes  
-------------------------------  ------------------------  ------  --------------------------  ----------  
cs4all/iteracion-08-s2           iteracion-08-s2           CS4ALL  2026-10-12 13:57:31.263000           0  
cs4all/iteracion-08-s1           iteracion-08-s1           CS4ALL  2026-10-12 08:41:06.287000           0  
cs4all/sonda-nucleo-08           sonda-nucleo-08           CS4ALL  2026-10-12 06:46:21.787000           0  
cs4all/sesion-unica-a            sesion-unica-a            CS4ALL  2026-10-04 21:23:28.010000           0  
cs4all/iteracion-06              iteracion-06              CS4ALL  2026-10-07 00:37:40.847000           0  
cs4all/validez-causa-cpu         validez-causa-cpu         CS4ALL  2026-10-04 21:17:41.937000           0  
== 2026-10-13T12:19:12Z kernels push i1
Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/cs4all/iteracion-08-br1-i1
codigo 0
== 2026-10-13T12:19:18Z kernels push c1
Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/cs4all/iteracion-08-br1-c1
codigo 0
== 2026-10-13T12:19:24Z estado
cs4all/iteracion-08-br1-i1 has status "KernelWorkerStatus.QUEUED"
cs4all/iteracion-08-br1-c1 has status "KernelWorkerStatus.QUEUED"
```

### Tanda 1 de R1 leída, y subida de la tanda 2 (2026-10-13, 13:41 a 13:52 UTC)

- **i1 (base 1):** completa, 12 de 12, **5 resueltas**, media 238,4 s, sesión 3 362 s, 0 colgadas, 0 errores del registro, mediana 33,9 tokens/s.
- **c1:** completa, 12 de 12, **5 resueltas**, media 297,2 s, sesión 4 478 s, 0 colgadas, 0 errores, 34,0 tokens/s. **Descartado por la regla de envío** (media sobre 262 s).
- **Cuota:** 27,23 h antes, 22,85 h después: 4,38 h. Reloj 7 840 s por 2,01 = 4,38 h.
- **Regla de parada (22.6):** todas las condiciones pasan salvo una en duda: la orden de comprobación dio código 4. El forense (informe en .scratch/concilio_memoria/fase2/concilio_47/forense/tanda1_codigo_4.md) lo reconstruyó: el 4 son 145 logs de 0 bytes de iteracion-03 a -07; ninguno es de i1 ni c1; el rescate de toda la cuenta da 4 desde el 2026-10-09. A/B sin red: comprobar sobre una copia con solo las dos sesiones da 0, y 4 al añadir iteracion-07. Por pasada, las dos dan 0. La condición manda «primero el forense»; hecho, y las sesiones están sanas: se sigue. **Para las tandas siguientes la comprobación se lee por pasada, y se dice.**
- Del forense: las canceladas (9 y 6) son la última petición de cada tarea cortada por tiempo; el error de i1 es un desborde de contexto recuperado en la petición siguiente; la bajada directa falla porque la CLI escribe el log en cp1252; el notebook rescatado es idéntico al subido como JSON, no byte a byte.
- Rescate: experiments/gemma_developer_agent/data/rescate_kaggle/2026-10-13T1342Z/.

Salida literal de la subida de la tanda 2 (c2 + c3), en experiments/gemma_developer_agent/data/rescate_kaggle/lecturas_envios\subida_r1_tanda2_2026-10-13T1351Z.txt:

```
== 2026-10-13T1351Z tanda 2: c2 + c3
huellas_ok
listado_igual
preflight c2 0
preflight c3 0
== quota antes
GPU       7.15h  22.85h     30.00h  2026-10-17T00:00:00  
== 2026-10-13T13:51:53Z kernels push c2
Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/cs4all/iteracion-08-br1-c2
codigo 0
== 2026-10-13T13:51:57Z kernels push c3
Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/cs4all/iteracion-08-br1-c3
codigo 0
cs4all/iteracion-08-br1-c2 has status "KernelWorkerStatus.QUEUED"
cs4all/iteracion-08-br1-c3 has status "KernelWorkerStatus.QUEUED"
```

### Bloque R1, tanda 2 leída y tanda 3 subida — 2026-10-13, 15:28 a 15:32 UTC

**No es un envío a la competencia.** Son sesiones privadas del bloque R1, con la orden del dueño «Adelante, sube el bloque R1».

Tanda 2 (C2 con C3), subida a las 13:51 UTC, las dos `COMPLETE` en la lectura de las 15:28 UTC.

| Sesión | Resueltas | Media por tarea | Sesión | Colgadas | Errores del registro | Frente a la base 1 |
|---|---|---|---|---|---|---|
| base 1 (`i1`) | 5 de 12 | 238,4 s | 3 362 s | 0 | 0 | — |
| C1 | 5 de 12 | 297,2 s | 4 478 s | 0 | 0 | neto 0; descartado por media > 262 s |
| C2 | 6 de 12 | 234,6 s | 3 371 s | 0 | 0 | gana `rich_3470`, no pierde ninguna: neto +1 |
| C3 | 3 de 12 | 235,6 s | 3 301 s | 0 | 0 | pierde `rich_2725` y `rich_3278`: neto −2 |

Regla de parada de 22.6, aplicada a la tanda 2: las dos completas, 12 `tarea_fin` cada una, ninguna colgada, ningún error del registro, `comprobar` por pasada en 0 (el código global sigue en 4 por los 145 registros vacíos de notebooks viejos, igual que en la tanda 1), guarda de ruedas con `distintas` vacío, sesiones bajo 3 830 s, cuota de la tanda 3,74 h (22,85 h a 19,11 h; tope 4,3 h). **Pasa.**

Una sola pasada por brazo: las diferencias de una o dos tareas están dentro del ruido medido entre dos corridas iguales; la base 2 (`i2`) es la que dice cuánto.

Chequeo previo de la tanda 3: 330 huellas sin cambio, listado de ruedas igual al de las 13:51, `preflight` 0 en `i2` y `c4`. Salida literal de la subida:

```
== quota antes
GPU       10.89h  19.11h     30.00h  2026-10-17T00:00:00
== 2026-10-13T15:31:35Z kernels push i2
Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/cs4all/iteracion-08-br1-i2
codigo 0
== 2026-10-13T15:31:40Z kernels push c4
Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/cs4all/iteracion-08-br1-c4
codigo 0
cs4all/iteracion-08-br1-i2 has status "KernelWorkerStatus.QUEUED"
cs4all/iteracion-08-br1-c4 has status "KernelWorkerStatus.QUEUED"
```

Archivos: `lecturas_envios/{rescate_2026-10-13T1530Z,comprobar_tanda2_2026-10-13T1530Z,quota_2026-10-13T1528Z_tras_tanda2,subida_r1_tanda3_2026-10-13T1535Z}.txt`; rescate fechado en `rescate_kaggle/2026-10-13T1530Z/2026-10-13T1528Z/`.

### Bloque R1, tanda 3 terminada y rescatada; concilio 48 convocado — 2026-10-13, 23:35 a 23:50 UTC

**Nada se subió ni se envió.** Solo lecturas y un rescate (descarga).

- **Estado (lectura de las 23:35 UTC):** las seis sesiones `iteracion-08-br1-{i1,c1,c2,c3,i2,c4}` en `COMPLETE`.
- **Cuota:** 14,64 h usadas, 15,36 h restantes; se renueva el 2026-10-17 00:00 UTC. La tanda 3 gastó 3,75 h
  (de 19,11 h a 15,36 h; techo 4,3 h).
- **Envío 57098570:** pasó de `PENDING` a `COMPLETE` con 0,13. El zip `65a02160…` lleva tres lecturas: 0,08,
  0,13 y 0,13. Entre la lectura de las 15:28 UTC y esta no hay otra: no se sabe a qué hora puntuó.
- **Rescate:** `rescate_kaggle/2026-10-13T2337Z/2026-10-13T2335Z/`, código 4 (los mismos 145 registros vacíos
  de notebooks viejos). `comprobar` por pasada: `i2` 0 y `c4` 0, «completa» las dos. Prueba del rescate, con
  los bytes de cada archivo y de cada miembro de los zips:
  `lecturas_envios/prueba_rescate_tanda3_2026-10-13T2337Z.txt` (164 líneas). 13 archivos por sesión y ninguno
  de 0 bytes en `i2` ni en `c4`; dentro de los zips hay parches, diffs y salidas de prueba de 0 bytes, que
  quedan para el forense.
- **El orquestador no leyó los resultados de la tanda 3.** Los leen los roles desde los archivos.
- **Concilio 48:** pregunta del dueño, literal: «realizar un llamado al concilio para definir ¿Cómo avanzar en
  el desafío kaggle? analiza todos los datos, datos, datos y planifica ¿qué haras para mejorar esto?». Encargo
  y prompts en `.scratch/concilio_memoria/fase2/concilio_48/`. Primera ronda en paralelo: analista de datos,
  QA de trayectorias, forense del arnés, inteligencia pública y arquitecto de IA.

Archivos: `lecturas_envios/{lectura_tanda3_2026-10-13T2335Z,rescate_2026-10-13T2337Z,comprobar_tanda3_2026-10-13T2337Z,prueba_rescate_tanda3_2026-10-13T2337Z}.txt`.

### Concilio 48: dictamen, corrección de una lectura y envío del día — 2026-10-14, 00:07 UTC

**Corrección de la entrada anterior.** Escribí que el envío 57098570 «pasó de `PENDING` a `COMPLETE`» en la
lectura de las 23:35 UTC y que no se sabía cuándo puntuó. Es falso: ya figuraba `complete` con 0,13 en el
`envios.json` de los rescates de las 13:42 y de las 15:28 UTC, y estaba `PENDING` a las 00:44 UTC del día 13.
Tardó entre 17,95 y 30,92 h (forense, inteligencia pública y auditor, cada uno por su cuenta). No leí mis
propios archivos antes de afirmar un estado remoto: es el mismo fallo que el auditor anotó en el concilio 47.

**Dictamen del auditor** (`.scratch/concilio_memoria/fase2/concilio_48/auditor/dictamen.md`), en corto:
- Las cifras de R1 se reproducen: resueltas 5, 5, 5, 6, 3, 5; base contra base, 0 discordantes; solo el tiempo
  de C1 (+55 s) sale del ruido. Ninguna decisión alcanza el criterio de decisión válida: todas exploratorias.
- C2 es otra lectura de un kit equivalente a la base: su instrucción no adelantó la primera edición.
- El modelo de tiempo se reproduce (0,248 s + 28,49 ms por token de salida + 0,033 ms por token de entrada,
  R² 0,996, 1 953 peticiones). «97 % de espera al modelo» era 93,9 %.
- Los 145 logs por tarea de las iteraciones 03 a 07 están vacíos en el origen y no son recuperables; desde
  `08-s1` hay 96 de 96.
- Vetos: llamar mejora a C2; concluir por repositorio o por «tarea imposible» desde las 241 tarea-sesiones (27
  de las 33 tareas nunca resueltas solo se vieron con kits viejos).
- Fallos del orquestador: afirmó un estado remoto contra sus archivos; sembró la ronda 2 con su primer hecho
  nuevo (traía juicio y nombraba mecanismos); los hechos 2 y 3 y un mensaje del dueño no fueron a ningún rol;
  nadie leyó los criterios de descarte de la adenda del concilio 47; no anotó el recall en la bitácora (lo
  ejecutó a las 23:4x UTC sobre la rama `issue-investigacion-fuentes`, sin registrarlo); ocho hallazgos
  siguen en «medido».

**Envío del día, por decisión del dueño.** El dueño escribió: «tienes total libertad de decidir. /loop puedes
incluso corregir todo, sin detención». Se envió el candidato que da la regla de envío escrita antes de los
datos (C2), rotulado como lectura y no como mejora, que es la acción 5 del dictamen. Salida literal, en
`lecturas_envios/envio_c2_2026-10-14T0007Z.txt`:

```
== 2026-10-14T0007Z envio del dia: candidato C2 (edicion temprana), rotulado lectura, no mejora
sha256 aa0750f0f47f63276cfcd3756fd0771d0b6633b3e21393e60ce8f9351dea0f39
huella_ok
== 00:07:17Z submit
0 submissions remaining today.
Successfully submitted to Google - The Gemma 4 Developer Agent Competition
codigo 0
57160374  submission.zip  2026-10-14 00:07:20  C2 edicion temprana (zip aa0750f0): lectura, no mejora; regla de envio del concilio 47  SubmissionStatus.PENDING
```

No decide nada por sí solo: con una lectura, la diferencia mínima detectable es de 9 a 15 tareas (auditor).
`registry.json` todavía dice `prepared` para ese zip: lo corrige el PR del issue #215.

**En construcción, sin gastar cuota ni envíos:** issue #215 (el registro escribe el muestreo, la causa del
fin y las peticiones canceladas) e issue #216 (sonda de caudal con peticiones concurrentes, ensayada en
Docker), cada uno con un constructor del kit. PR #214 (matriz RACI y definiciones de agentes), en revisión.

### Plan único del caso, fijado el 2026-10-14 (01:10 UTC) tras la orden del dueño de ordenar el trabajo

El dueño: «deja de generar basura […] Aún veo iteraciones sin sentido, y desordenadas. Falta enfocarnos de
acuerdo a 1 planificación.» Se detuvieron dos constructores que no servían a este plan (la sonda de caudal,
#216, y los tres candidatos anteriores, #217) y el loop de vueltas automáticas.

**Hipótesis única.** El agente pierde porque no localiza el sitio de la edición cuando el enunciado no lo
nombra. Localizarlo por el grafo de código (semillas en los símbolos del enunciado y propagación, el mecanismo
de ALL) sube las tareas resueltas.

| Paso | Qué | Costo | Puerta para pasar al siguiente |
|---|---|---|---|
| 1 | Medir en local, sin modelo, si la propagación sobre el grafo pone el sitio entre los 5 primeros (#221) | 0 h | Supera a las palabras clave en las tareas públicas. Si no supera a los vecinos a 2 saltos, se usa lo más simple |
| 2 | Un solo candidato de kit que localiza por el grafo, con la ficha del diseñador, ensayado en Docker | 0 h | El cambio se ve en la petición y la sesión de ensayo termina |
| 3 | Medición pareada en Kaggle: el candidato en las tareas 1 a 12 (la base ya está) y base y candidato en las tareas 13 a 48 | 13,9 h de las 15,36 h que caducan el 17 | Sesiones completas, sin colgadas |
| 4 | Decidir con la regla escrita antes de correr y enviar el candidato si pasa; si no, se descarta y se anota | 1 envío por día | Neto de 3 tareas o más a favor en las 48 pareadas y media por tarea dentro del tope |

**Congelado hasta cerrar el paso 4:** concilios nuevos, roles, documentos de proceso, esperas de CI, issues
que no sean de estos cuatro pasos, la sonda de caudal, los candidatos de texto y los tres estructurales
anteriores, y el adaptador LoRA. El writeup del Paper Track (cierre el 12 de noviembre) queda aparte: espera
los pendientes que el dueño ve en la página.

**Lo que no está decidido y se dice:** la regla del paso 4 (neto de 3 en 48) la fija el orquestador hoy; no la
revisó ningún rol. Las predicciones del paso 3 las escribe un rol antes de subir.

### Plan único, enmienda del 2026-10-14 (01:45 UTC): la cuenta del estratega cambia los pasos 3 y 4

El dueño preguntó qué dice el concilio y «el matemático experto». La cuenta la hizo el estratega de
experimentos (`.scratch/concilio_memoria/fase2/concilio_48/estratega/cuenta.md`, con sus guiones `e1` a `e4`);
el orquestador la había adelantado por su cuenta (`orquestador/g12_potencia_tabla.py`) y coinciden.

Parecer del estratega, tal cual lo resumió:

> - **Ruido:** un mismo zip varía 1,43 tareas (IC 95 % 0,97 a 2,75), de 13 lecturas: 5 propias y 8 públicas declaradas. La base vigente tiene media 7,0 ± 0,83.
> - **Qué se mide en la tabla:** ver 1 tarea pide 26 lecturas por brazo; 2 piden 7; 3 piden 3; 4 piden 2. Con 25 a 38 envíos efectivos caben 0, 3 a 4, 8 a 12 y 13 a 19 brazos.
> - **Qué se mide en local:** con 3 de 48 tareas cambiando, hacen falta 1 415, 352, 159 y 97 tareas pareadas (466 a 32 h de cuota).
> - **Máximo frente a media:** el máximo de 12 lecturas sube 2,33 sobre la media. La parte alta es compatible con una media de 9 a 10, así que la distancia real es de 2 a 3 tareas, no 6.
> - **Plan del orquestador:** su regla (neto de 3 en 48) pasa con probabilidad 0,07 a 0,23 con efecto nulo y 0,11 a 0,27 con el efecto que los datos dan al grafo (0,55 a 0,72). Los pasos 3 y 4 no deciden nada.
> - **Propuesta:** ensayar la receta pública (+3,67 declarado) con hasta 3,52 h y 3 envíos. Merece envío quien prometa 3 tareas o más.
> - **Nota final:** cuenta la tabla privada, no el máximo público.

**Lo que cambia.** Los pasos 3 y 4 del plan de las 01:10 UTC (medición pareada del candidato de grafo en 48
tareas, 13,9 h, y regla de neto 3) quedan **retirados**: no pueden decidir. Se detuvo el constructor del
notebook de la base en las tareas restantes (#218).

| Paso | Qué | Costo | Qué lo detiene |
|---|---|---|---|
| 1 | Terminar la medición local de localización por grafo (#221) como conocimiento; no gasta cuota | 0 h | — |
| 2 | Dejar ensayados en Docker el candidato de una línea y nuestro C1 a 8 minutos (#224) | 0 h | — |
| 3 | Una sesión de 12 tareas del C1 a 8 minutos, para comprobar tiempos y validez antes de enviarlo | hasta 3,52 h (cota, sin medir) | Una colgada, guarda de ruedas, o la proyección de 120 tareas fuera de plazo |
| 4 | Tres lecturas del C1 a 8 minutos en la tabla, una por día | 3 envíos | Media de las tres por debajo de la media de la base (7,0 tareas): se descarta |
| 5 | Regla desde hoy: solo recibe un envío un candidato que prometa 3 tareas o más sobre la base, con su fuente | — | — |

**Lo que no está medido y se dice:** las tres notas de la configuración pública son declaradas por quienes
la publican; el costo de una sesión con tope de 8 minutos es una cota; y el efecto que los datos dan a la
localización por grafo (0,55 a 0,72 tareas) sale de una prueba pública ajena, no nuestra.

### Protocolo de envíos fijado por el dueño — 2026-10-14, 02:12 UTC

Sustituye al plan enmendado de las 01:45 UTC en lo que toca a envíos. Texto del dueño, tal cual:

> Próxima acción: esperar el resultado definitivo del envío C2 (`aa0750f0…`) y registrarlo con su versión de arnés y tamaño efectivo de tabla. No modificar C2 ni inferir conclusiones mientras esté pendiente.
>
> Decisión posterior:
>
> - Si C2 logra al menos 9 tareas o supera claramente la referencia histórica, conservarlo como candidato y repetir exactamente el mismo ZIP una vez para comprobar que el resultado no fue una lectura excepcional.
> - Si C2 queda en 7 tareas o menos, enviar C1 (`a038a389…`) sin modificar ningún byte. C1 se evalúa como paquete de alto impacto, no como ablación.
> - Si C2 queda entre 8 y 8,9 tareas, registrar el resultado como ambiguo y enviar C1 como candidato alternativo; no gastar un día repitiendo la base.
>
> Después de la primera lectura de C1, realizar solo una relectura de la base actual como control de versión del arnés. No alternar diariamente base y candidato: conservar las demás oportunidades para repetir únicamente el candidato que alcance el mejor resultado consistente.
>
> El objetivo no es demostrar causalidad académica de cada cambio. El objetivo es identificar un ZIP robusto que aumente la cantidad de tareas resueltas y tenga opciones reales de transferir al leaderboard privado.

**Estado al fijarlo.** Envío 57160374 (C2, zip `aa0750f0…`): `PENDING` en la lectura de las 02:12 UTC
(`lecturas_envios/lectura_2026-10-14T0212Z.txt`); se envió a las 00:07 UTC. El envío anterior tardó entre
17,95 y 30,92 h en puntuar. El cupo del día 14 (UTC) está usado; el siguiente se abre el 15 a las 00:00 UTC.

**Cómo se lee la nota en tareas** (tabla de 58, nota truncada a dos decimales): 0,12 son 7 tareas; 0,13 son
8; 0,15 son 9; 0,17 son 10. Con 58 y con 60 tareas las notas vistas hasta hoy son compatibles: al registrar
el resultado se vuelve a deducir el tamaño de la tabla desde la tabla pública del rescate.

**Al llegar la nota:** rescate (que trae `envios.json`, la tabla pública y el listado de ruedas del día),
registro en `registry.json` con la fecha de la lectura que lo vio completo y el conjunto de ruedas público de
ese día, y la rama del protocolo que corresponda. Ningún rol ni el orquestador cambia un byte de C2 ni de C1.

## Vuelta 48 � 2026-10-14 (UTC): concilio 49, auditor�a decisiva local mientras C2 espera nota

### Retomar, #179 verificado y convocatoria del concilio 49 (2026-10-14, 09:30 a 10:15 UTC)

**Nada se subi� ni se envi�.** Solo lecturas.

- **Env�o 57160374 (C2):** `PENDING` en la lectura de las 09:30 UTC (`uvx kaggle competitions submissions`). Lleva 9,4 h; el anterior tard� entre 17,95 y 30,92 h. El loop lo consulta cada hora.
- **#179:** la salida del vig�a de esta sesi�n (arranque real con `main` en `11b65eb`, que contiene `281e822`) se peg� en el issue y coincide con la lectura independiente de Kaggle. Tarjeta pasada a *Verificada*.
- **Orden del due�o:** �llamar al concilio a trabajar en la planificaci�n lograda antes�, y despu�s �insisto, recuerda el foco�: los dos encargos de auditor�a (Lead Data Scientist y auditor�a decisiva local con `KAGGLE_AUDIT.md`), guardados tal cual en `.scratch/concilio_memoria/fase2/concilio_49/prompts/`.
- **Concilio 49, ronda 1** (en paralelo, la misma pregunta): analista de datos, estratega, QA de trayectorias y forense del arn�s. Encargo en `.scratch/concilio_memoria/fase2/concilio_49/encargo.md`. Despu�s, la revisi�n cruzada sin firmas y el auditor del m�todo. Con su dictamen se escribe `KAGGLE_AUDIT.md`.
- **Anexo del encargo:** cada rol deja hoy, antes de la nota, su predicci�n fechada para la nota de C2. El protocolo del due�o de las 02:12 UTC no cambia.
- Los cuatro archivos sin versionar de la ra�z (`STATE_OF_COMPETITION.md`, `HARNESS_AUDIT.md`, `FAILURE_TAXONOMY.md`, `EXPERIMENT_LEDGER.csv`, del 13 a las 21:17) son de autor no verificado: los roles los tratan como hip�tesis.

### Correcci�n (2026-10-14, ~11:00 UTC): el concilio 49 repet�a trabajo ya hecho

El due�o: �este an�lisis ya lo hicimos ayer. Luego fuimos a comentarios claves en Kaggle y definimos un plan�. Es cierto. La auditor�a decisiva est� en `.scratch/concilio_memoria/fase2/concilio_48/orquestador/auditoria_decisiva_sintesis.md` (14, 00:50 UTC) y el foro en `.../concilio_48/inteligencia2/informe.md`; de ah� sali� el plan enmendado de las 01:45 y el protocolo del due�o de las 02:12, que es el plan vigente. **Fallo del orquestador:** convoc� un concilio nuevo y escribi� un `KAGGLE_AUDIT.md` sin leer antes la carpeta del concilio 48. Se detuvieron analista, estratega y QA; se borr� el `KAGGLE_AUDIT.md` duplicado.

**Lo �nico nuevo que dej�, del forense** (`.../concilio_49/forense/informe.md`): repetir C2 se proyecta en 8,0 a 10,1 h; C1 en 11,3 a 11,5 h, en 12,3 a 12,5 h si el puntuador suma 30 s por tarea, y en 13,9 h si todas llegan al tope: probabilidad de pasar de las 12 h 0,25 (juicio del forense). Predicci�n del forense para C2, fechada a las 09:48 UTC: 7 tareas, intervalo 80 % de 5 a 9; P(9 o m�s) 0,19, P(8) 0,20, P(7 o menos) 0,61. El protocolo no cambia; se informa al due�o.

**Comprobaci�n p�blica del plazo de C1 (2026-10-14, ~11:20 UTC, 0 h, sin env�o).** En lo bajado el 13 (`concilio_48/inteligencia2/nb18.txt`, l�neas 35, 79 y 86): la receta p�blica de 8 min, 28 llamadas y 240 s por orden puntu� 0,18 dos veces (su autor y la reproducci�n 56932359) sin pasar de las 12 h, porque la mayor�a de las tareas paran en el tope de llamadas o entregan antes. C1 tiene el mismo tope de 28 llamadas y menos minutos (6), as� que cabe si cabe la receta. Salvedad: esas lecturas son de antes del cambio de ruedas del 9 y del 12. Conclusi�n: nada impide la rama C1 del protocolo; el riesgo de 0,25 del forense no se sostiene frente a lo p�blico.

**Zip nuevo, por orden del due�o (2026-10-14, ~11:40 UTC).** El due�o record� que la tabla privada decide la posici�n final y que copiar el zip p�blico no sirve: el env�o tiene que ser un zip nuevo, nuestro. Se construye en local, sin cuota ni env�o: la receta p�blica de 0,18 (control, armada byte a byte) m�s un solo cambio, quitar `write_file` (plan �nico de la auditor�a decisiva del 14 a las 00:50 UTC; 17 de 43 fallos de R1 terminan solo con archivos nuevos). Carpeta `instrumentos/receta_publica_018/`; antes, el conteo de cu�ntos parches de referencia crean un archivo fuente nuevo. Su env�o espera la palabra del due�o: el protocolo de las 02:12 autoriza C1, no este zip.

**Regla del env�o del 15 (escrita el 14 a las ~11:55 UTC, antes de cualquier dato nuevo).** Orden del due�o: avanzar sin preguntar. (1) Si C2 punt�a 9 tareas o m�s: repetir C2 (protocolo). (2) Si no, y la sesi�n de 12 tareas de la receta sin `write_file` termin� completa, sin colgadas, y resuelve al menos lo mismo que la receta exacta menos 1: se env�a la receta sin `write_file`. (3) Si esa sesi�n no termin� a tiempo o falla la condici�n: C1 sin tocar (protocolo). Antes del env�o, el analista de datos y el auditor leen la nota de C2 y la sesi�n (a�adido del due�o). Sesiones de GPU de hasta 4,5 h de las 15,36 que caducan el 17, subidas por el constructor sin esperar al due�o.

**Cambio de base y concilio 50 (2026-10-14, ~12:15 UTC).** Se ley� el bundle p�blico �contract-first� (t�tulo �LB 0.24�): mismos topes que la receta 0,18, sin grafo, y una instrucci�n que dice que los archivos que quedan en el repositorio entran en el diff y hacen fallar la tarea (17 de 43 fallos nuestros en R1 dejan solo archivos nuevos). El zip nuevo pasa a ser el 0,24 sin `write_file`, frente al 0,24 exacto, con dos sesiones de 12 tareas. En la regla del env�o del 15, �receta� se lee ahora �0,24�. Concilio 50 convocado con la pregunta del due�o ��C�mo logramos llegar al primer lugar?�: inteligencia p�blica, arquitecto y estratega en paralelo; despu�s, el auditor. Encargo en `.scratch/concilio_memoria/fase2/concilio_50/encargo.md`.

**Regla del env�o del 15, ajuste (2026-10-14 ~13:00 UTC, antes de cualquier dato nuevo).** En la rama (3), si la sesi�n de nuestro zip no termin� a tiempo, se env�a el bundle 0,24 exacto en lugar de C1 (C1 no tiene ninguna lectura en la tabla; el 0,24 es la mejor base p�blica). Las ramas (1) y (2) no cambian.

**Sesiones del 0,24 subidas (2026-10-14, 10:28 UTC, reloj de la m�quina).** Las subi� el orquestador por la orden del due�o de avanzar (el constructor no lo hizo, por la prohibici�n de su encargo). `cs4all/iteracion-08-p24-sinwf` (zip `b1f904c8�`, el 0,24 sin `write_file`) y `cs4all/iteracion-08-p24-exacta` (zip `1fd1c073�`), 12 tareas de R1 cada una, las dos `RUNNING` a los 20 s. Cuota antes: 15,36 h de GPU y 20 h de TPU, las dos caducan el 17. Costo estimado por el constructor: de 5,2 a 6,0 h las dos. Salida literal en `lecturas_envios/subida_p24_*.txt`. Correcci�n: las horas �~11:00 a ~13:00 UTC� de las entradas anteriores de hoy est�n adelantadas unas 2 h; el reloj de la m�quina daba de 09:30 a 10:30 UTC. Ensayo, huellas y conteo: `instrumentos/receta_publica_018/INFORME.md` (11 de 129 parches de referencia crean un archivo fuente nuevo; sin `write_file` se crean por `run_command`).

**Adaptador LoRA nulo: aceptado por el arn�s sin GPU; sonda armada (2026-10-14, ~10:45 UTC).** Constructor: `validate_directory` OK, orden de vLLM con `--enable-lora --max-lora-rank 16 --lora-modules main_lora=�`, y las peticiones salen con `model=main_lora`. Zip `submission_024_lora_nulo.zip` (sha `409f58fe�`), adaptador r16 en `q_proj` y `o_proj`, `lora_B` en ceros (sha `9aadc3af�`). Que vLLM lo aplique solo lo dice una sesi�n de GPU: kernel `cs4all/sonda-lora-nulo` armado (`instrumentos/lora_nulo/kernel_sonda_lora/`, 4 celdas compiladas), costo estimado de 0,7 a 1,3 h. Criterio escrito antes de los datos: nulo id�ntico a la base en 8 de 8 y ruido distinto en al menos 1 de 8 : el arn�s sirve el adaptador; si no, la v�a LoRA queda fuera. Se sube en cuanto termine una de las dos sesiones del 0,24 (tope de 2 sesiones de GPU por cuenta).

**Dictamen del auditor, concilio 50 (2026-10-14, ~10:55 UTC), aplicado.** Estrategia �nica: un suelo propio de la familia contract-first en la tabla y una sola apuesta de techo, el adaptador LoRA, detr�s de tres puertas (G2 efecto en logits, E2 aceptaci�n en el puntuador, G3 tok/s de entrenamiento). Parada el 11-14 si ning�n brazo promedia 13 tareas o m�s en 3 lecturas. P(primero) entre 0,01 y 0,035 con cualquier plan (juicio con priores, no medido). **Veto 1 aplicado:** la rama (3) del env�o del 15 vuelve a C1 sin tocar (el 0,24 exacto contradice la orden del due�o de no copiar el zip p�blico). En obra: la sonda G2 rehecha seg�n el dictamen (gemelos N(0,1e-3) y N(0,1), gpu 0,80, 5 indicaciones a T=0, top-20 del primer token, deriva de la base dos veces) y el cuaderno G3 m�s la conversi�n de trayectorias en CPU. Las 20 h de TPU caducan sin uso. Fallos del orquestador se�alados por el auditor: sembr� el encargo con cifras y conclusiones del concilio 48 y con el LoRA (el acuerdo entre roles no es una medici�n); omiti� analista, forense y revisi�n cruzada; horas adelantadas unas 2 h. Dictamen: `.scratch/concilio_memoria/fase2/concilio_50/auditor/dictamen.md`.

**Sesiones del 0,24 terminadas (2026-10-14, 12:04 UTC).** Las dos `COMPLETE`, rescatadas en `rescate_kaggle/p24_2026-10-14T1204Z/`. Recuento del orquestador, para que lo vuelva a hacer el analista: 0,24 exacto 4 de 12 (270 s de media de reloj), 0,24 sin `write_file` 4 de 12 (269 s), discordantes 1 y 1. La base hab�a hecho 5 y 5 en las mismas tareas, y C2 6. Todo dentro del ruido de 12 tareas. Por la regla del env�o del 15, rama (2), el 0,24 sin `write_file` cumple (4 frente a 4 menos 1). Sonda G2 subida a las 12:04 UTC, `RUNNING`; cuota antes de subirla, 11,05 h de GPU.

**Sonda G2: PASA (2026-10-14, 12:36 UTC).** `cs4all/sonda-lora-nulo` completa; salida en `rescate_kaggle/sonda_g2_2026-10-14T1236Z/sonda_g2.json`. vLLM arranca con LoRA a `gpu_memory_utilization` 0,80 (427 s). Primer token, 5 indicaciones a T=0: deriva de la base 0 en 4 y 0,19 nat en 1; adaptador de ceros 0 en 5 de 5; ruido N(0,1e-3) de 0,13 a 0,25 nat; ruido N(0,1) de 12,2 a 16,5 nat en 5 de 5. Criterio escrito antes (ceros dentro de la deriva en 5 de 5; N(0,1) de 1 nat o m�s y 10 veces la deriva o m�s en 4 de 5 o m�s): **cumplido**. Decodificaci�n: base 37,85 tok/s, con adaptador 35,38 (6,5 por ciento m�s lenta). Cach� KV 6,13 GiB por GPU. Siguen G3 (tok/s de entrenamiento) y E2 (aceptaci�n en el puntuador con un env�o del adaptador nulo).

**G3 subida (2026-10-14, 12:47 UTC).** Dataset privado `cs4all/ruedas-g3` creado con peft 0.21.2, accelerate 1.15.0, psutil, PyYAML y tqdm (faltaban en el wheelhouse; transformers 5.13.1 exige accelerate). Kernel `cs4all/sonda-g3-entreno` (sha `3c676fc6�`) `QUEUED`; tope 1,9 h de reloj (~3,8 h de cuota). Criterio escrito en la celda: 150 tok/s o m�s, 31B viable; de 50 a 150, solo una miniatura de 4 M de tokens o menos; menos de 50, se cierra el entrenamiento en GPU. Hallazgo del constructor: con `run_compressed=True` la capa ct no se ejecuta y peft no la envuelve; el cuaderno descomprime a bf16 (60,9 GiB) o recuantiza a nf4 (21,7 GiB). Cuota antes: 10,72 h de GPU. Tope de `episodios-01` bajado a 3,0 h de reloj para que quepa. Trayectorias abiertas: Nebius SWE-rebench-openhands (CC-BY-4.0) convertidas a nuestro formato; 3 336 caben en 24k tokens, pero solo 142 caben adem�s en 28 llamadas. Detalle en `instrumentos/lora_g3/INFORME.md`.

**Kit propio ALL-1 y nueva regla del env�o del 15 (2026-10-14, 13:10 UTC, antes de cualquier dato del kit).** El due�o: �no puedes usar el mismo de 0.24, debes crear el nuestro a partir de este aprendizaje�. Se retira el 0,24 sin `write_file` como candidato. Especificaci�n propia en `instrumentos/kit_all_1/ESPECIFICACION.md`: texto escrito desde cero y dos mecanismos que el agente ejecuta, la skill `localizar` (grep m�s BM25 sobre los t�rminos del enunciado, top 5 de archivos) y la skill `entregar` (limpia rutas de pruebas y archivos sueltos, `py_compile`, proh�be el diff vac�o). Cada pieza nombra el fallo medido que ataca. `episodios-01` se borr� de la cola sin haber empezado: los episodios se generan con el kit que se env�a, porque el adaptador aprende su formato; se relanzan con ALL-1. G3 fall� en 85 s por falta de `loguru` (dependencia de `compressed-tensors`); dataset `ruedas-g3` versionado con `loguru` 0.7.3 y G3 relanzada, `QUEUED`. **Regla del env�o del 15, reemplaza a la anterior:** (1) si C2 saca 9 tareas o m�s, repetir C2; (2) si no, ALL-1, si su sesi�n de 12 tareas termin� completa, sin colgadas y con 4 resueltas o m�s (la base hizo 5 y 5; se admite menos 1); (3) si no, C1 sin tocar.

**Correcci�n del due�o (2026-10-14 ~13:15 UTC):** ALL-1 se construye a partir del zip 0,24 (`1fd1c073�`), no desde cero. Base: sus cuatro archivos tal cual. Encima, solo nuestras mejoras: la skill `localizar`, la skill `entregar` y las reglas de higiene de llamadas que le falten al prompt. Mismos topes, muestreo y herramientas. El diff frente al 0,24 debe mostrar solo esas adiciones. La regla del env�o del 15 no cambia.

**ALL-1 subido (2026-10-14, 13:32 UTC).** `cs4all/iteracion-08-all1`, `RUNNING`. Zip `240e5df8�` = 0,24 exacto + skills `localizar` y `entregar` (scripts Python; el arn�s no admite `.sh`) + sus dos l�neas de prompt + tres reglas de higiene; 0 l�neas quitadas frente al 0,24. Puertas: (1) `validate_directory` pasa, las ruedas admiten skills con script; (2) Docker: sesi�n completa y tarea colgada pasan, 5 de 6 resueltas; (3) `localizar` sin modelo: archivo del parche entre los 5 primeros en 72 de 129 tareas (55,8 por ciento), igual que `git grep` del identificador m�s raro, y peor en el primer puesto (33 frente a 55). Cumple el umbral del 50 por ciento escrito, pero no mejora la localizaci�n. Sin comprobar: si Gemma gasta llamadas en `load_skill`. Cuota antes: 10,49 h. Informe: `instrumentos/kit_all_1/INFORME.md`.

**G3 v2 sin lectura (2026-10-14, 13:12 a 13:17 UTC).** Con `loguru` ya instalado, fall� por falta de memoria al descomprimir el modelo, en los dos modos. Memoria m�xima reservada por GPU: 0 = 9,6 GiB; 1 = 21,8 de 22,0 GiB (sin memoria al pedir 442 MiB); 2 = 4,9; 3 = 4,6. `device_map` reparti� mal, y el modo nf4 tambi�n pasa por la descompresi�n a bf16. Costo: unos 5 min de reloj. Encargo: `max_memory` equilibrado, `expandable_segments` y recuantizar capa a capa para nf4. Salida en `rescate_kaggle/sonda_g3v2_2026-10-14T1340Z/`.

**Fallo del orquestador y regla nueva (2026-10-14, 13:45 UTC).** Las dos fallas de G3 (falta de `loguru` y memoria de la GPU 1) eran detectables antes de subir: dependencias declaradas en la rueda y `device_map` sin `max_memory`. El constructor hab�a escrito �sin comprobar CUDA ni memoria� y el orquestador subi� sin revisi�n. Regla desde ahora: ning�n cuaderno de GPU se sube sin (1) cierre de dependencias, (2) plan de memoria por GPU escrito en el cuaderno y (3) premortem del forense del arn�s.

**Datos de entrenamiento: decisi�n (2026-10-14, 14:40 UTC).** `entrenamiento-01` armado en `instrumentos/lora_entreno/`, con 179 ejemplos de 84 tareas (R1 29, p24 8, Nebius 142). Todas las trazas propias resueltas son de las 12 tareas de R1, que son la guarda de evaluaci�n: **se excluyen** (`--filtro sin_r1`). Quedan las 142 de Nebius m�s los episodios de `episodios-02` (kit ALL-1, que s� usan las skills). G3 v3 armada (mapa de memoria sobre el modelo denso, 16 GiB por GPU; nf4 descomprime en RAM de CPU y pide 70 GiB o m�s); premortem del forense en curso antes de subirla.

**ALL-1, sesi�n de 12 tareas le�da (2026-10-14, 14:35 UTC).** `COMPLETE`, completa, sin colgadas; 6 de 12 resueltas (base 5 y 5; C2 6; 0,24 exacto 4; 0,24 sin `write_file` 4), 272,5 s de media de reloj, 2 sin parche (el 0,24 tuvo 4). Frente al 0,24 exacto: 3 tareas que solo resuelve ALL-1 y 1 que solo resuelve el exacto (neto +2, dentro del ruido). Skills usadas por Gemma real: 83 `run_skill_script`, 12 `load_skill`, 25 `list_skills`, sin errores de skill encontrados. Cumple la rama (2) de la regla del env�o del 15. Rescate en `rescate_kaggle/all1_2026-10-14T1435Z/`. `episodios-02` subida a las 14:36 UTC (sha `88ba79dd�`, 94 tareas v�lidas, tope 7 020 s), `QUEUED`; cuota antes: 8,39 h de GPU.

**G3 v3 subida (2026-10-14, 14:43 UTC).** Sha `2a89a14d�`, `-t 7800`, `RUNNING`. Pas� los tres controles: dependencias completas (dictamen del forense), plan de memoria por GPU en la celda y premortem del forense con 4 arreglos aplicados (RAM le�da del cgroup, mapa guardado antes de cargar, etiqueta de OOM a 16k, se�al de muerte por RAM). `episodios-02` en `RUNNING`. Cuota antes: 8,29 h.

**G3 v3 sin lectura, con avance (2026-10-14, 15:18 UTC).** Carg� el modelo: bf16 en 184 s y nf4 en 861 s, sin falta de memoria; RAM de la sesi�n 173 GiB (l�mite cgroup v2); atenci�n SDPA con flash. Fall� al envolver con peft en los dos modos: `peft` 0.19.1 de la imagen rechaza `torchao` 0.10.0 (�only versions above 0.16.0�). El cierre de dependencias no lo vio: comprueba faltantes, no conflictos de versi�n con paquetes opcionales que trae la imagen. Arreglo: desinstalar `torchao`, forzar `peft` 0.21.2 del dataset y ensayar con el inventario exacto de la imagen. Duraci�n: 1 114 s.

**Causa de la falla de `loguru` (2026-10-14).** Ya estaba resuelta: `loguru` 0.7.3 viene en el wheelhouse y los cuadernos de iteraci�n lo instalan desde el 4 de octubre. La celda de G3 instal� a mano solo 5 ruedas en vez de reutilizar la celda de instalaci�n probada. Regla: todo cuaderno nuevo parte de uno que ya corri� en Kaggle y solo cambia lo necesario. La memoria de la GPU 1 y el choque de `torchao` no ten�an antecedente.

**G3 v4 subida, intento �nico (2026-10-14, 15:39 UTC).** Sha `56187d24�`, `-t 7800`, `QUEUED`. Cumpli� los tres compromisos: parte de las celdas del p24 sin cambios (wheelhouse completo); ensayo en una r�plica local de la imagen (`aal-g3-replica:cpu`), que reproduce el error de la v3 y en la que la v4 pasa; premortem del forense SUBIR (65 por ciento de obtener tok/s a 16k; riesgo principal, el paso a 16k en bf16; preflight 19 de 19 `[OK]`). `ruedas-g3` contiene `peft-0.21.2`. Si falla, no se reintenta esta semana. Cuota antes: 5,80 h.

**Regla de oro del due�o (2026-10-14, 15:45 UTC): �siempre resolver�.** Se retira la promesa de no reintentar G3 esta semana. Ante una falla: causa con evidencia, arreglo, ensayo en la r�plica, controles y nuevo intento. Una v�a se cierra solo por un resultado medido con el criterio escrito antes.

**Orden del due�o de las 16:00 UTC, aplicada.** Loop detenido, junto con la regla vencida �si C2 no llega a 9, va C1�. ALL-1 se define como el zip 0,24 m�s tres piezas: `localizar`, `entregar` y la instrucci�n �editar un archivo de fuente existente antes de la llamada 10; no repetir `submit_patch` si sali� vac�o�. El zip `240e5df8�` no tra�a la pieza 3, as� que se rearma. `episodios-02` se borr� a las 16:06 UTC porque corr�a con ese zip incompleto (cuota tras borrarla: 4,04 h). G3 v4 sigue corriendo. El QA de ALL-2 se detuvo.

**ALL-1 (`450e1a1a�`), pasos 1 a 3 (2026-10-14).** Ensayo en Docker: `completa`, `submit_vacio` y `tarea_colgada` pasan; el arn�s acepta un `submit_patch` vac�o repetido, y solo lo frenan la l�nea del prompt y el aviso de `entregar`. `localizar` sin modelo: 72 de 129 tareas con el archivo del parche entre los 5 primeros. Sesi�n de 12 tareas `cs4all/iteracion-08-all1b` subida a las 16:17 UTC (notebook `768ee46e�`, `-t 9600`), `RUNNING`; cuota antes: 3,68 h, con G3 todav�a corriendo.

**G3 v4 detenida (2026-10-14, 16:52 UTC).** Cuota a las 16:50 UTC: 1,48 h, con G3 y ALL-1b corriendo a la vez (~4 h de cuota por hora: ~22 min). Ninguna de las dos habr�a terminado. Se prioriz� el paso 3 (sesi�n ALL-1b) seg�n el orden del due�o, y G3 se borr� tras 65 min sin salida parcial disponible. Cuota tras borrarla: 2,42 h. G3 v4 pas� todos los controles y se vuelve a subir tal cual con la cuota del 17.
