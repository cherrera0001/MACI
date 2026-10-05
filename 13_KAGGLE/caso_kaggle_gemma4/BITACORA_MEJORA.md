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
