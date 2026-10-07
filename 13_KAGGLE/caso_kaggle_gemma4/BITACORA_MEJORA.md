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
