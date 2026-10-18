# Registro de pruebas en Kaggle

Una fila por cada corrida subida a Kaggle y por cada envío a la competencia. Sirve para saber, sin releer la
bitácora, qué se subió, para responder qué, con qué resultado y dónde están sus datos.

- **Solo agregados:** sin enunciados, parches, pruebas ni identificadores de tareas.
- **Detalle de cada vuelta y sus predicciones:** [`BITACORA_MEJORA.md`](BITACORA_MEJORA.md).
- **Datos crudos:** en el repositorio del experimento, carpeta `data/rescate_kaggle/`, que git ignora.
- Las horas son UTC.

## Envíos a la competencia

| Fecha | Referencia | Qué se envió | Nota | En tareas |
|---|---|---|---|---|
| 2026-10-03 23:46 | 56808559 | Kit ajustado: 4 minutos, 40 llamadas, sin adaptadores, razonamiento apagado | 0,06 | 4 de 58 |
| 2026-10-04 17:41 | 56830336 | El mismo archivo, para ver el ruido de la tabla | 0,05 | 3 de 58 |
| 2026-10-07 00:26 | 56895202 | `i_razona`: el mismo kit con razonamiento encendido, 60 llamadas y 4,5 min por tarea (zip `65a0216007e19bf6…`). Ordenado por el dueño. Predicciones P38 y P39 en la vuelta 33 de la bitácora | **0,08.** Estuvo en error de sistema (leído el 2026-10-07 a las 15:55 UTC) y Kaggle lo volvió a puntuar solo: `complete` el 2026-10-08 a las 21:37 UTC. P38: no decide (regla de la vuelta 33). P39: sin poder leerse | 5 de 58 |
| 2026-10-07 16:25 | 56916129 | El mismo zip `65a0216007e19bf6…` del 56895202, byte a byte, reenviado tras su error de sistema. Aprobado por el dueño («Sí, reenvía el mismo zip»). Mismas predicciones P38 y P39 | **0,13.** En error de sistema hasta el 2026-10-08 a las 22:31 UTC; `complete` leído el 2026-10-09 a las 13:42 UTC, dentro de una tanda de repuntuación del organizador (inferencia) | 8 de 58 |

Los cuatro envíos son dos archivos enviados dos veces: sin razonamiento, 4 y 3 tareas; con razonamiento, 5 y 8.
Con dos notas por archivo no se distingue uno de otro. Última lectura por la API: 2026-10-09 a las 21:55 UTC,
sin cambios. Tabla pública a las 17:41 UTC: 2 188 equipos, puesto oficial 544, 277 equipos con más nota.

**Preparado y no enviado:** kit K «interfaz limpia» (`sub-004` en el registro del repositorio, huella
`3346af0e…c8b1`): la base sin subagente, sin las tres herramientas de grafo y sin la línea de la instrucción
que ordenaba la búsqueda. Vuelta 42 de la bitácora.

## Corridas en notebooks

| # | Notebook | Máquina | Pregunta | Resultado | Estado |
|---|---|---|---|---|---|
| 1 | `ensayo-a0-anfitrion` | CPU | ¿Qué trae el entorno del notebook? | Sondas del entorno guardadas | Terminada |
| 2 | `validez-ensayo-cpu` | CPU | ¿Qué tareas públicas sirven para medir? | 71 de 129; con 60 s por comando no cambia ninguna | Terminada |
| 3 | `prueba-a-ajustada`, versión 1 | GPU | ¿Arranca el modelo y resuelve? | Se detuvo: no encontró los archivos de instalación | Fallida, causa visible en local |
| 4 | `prueba-a-ajustada`, versión 2 | GPU | La misma | Cancelada antes de correr: tenía la misma ruta fija | Cancelada |
| 5 | `prueba-a-ajustada`, versión 3 | GPU | La misma | Arranca; carga en 764,5 s; 0 de 2 tareas | Terminada |
| 6 | `sesion-unica-a` (otra sesión) | GPU | ¿Ayuda el razonamiento? ¿Cuánto ruido hay? | 4, 3 y 4 de 16; ruido de 2 tareas | Terminada |
| 7 | `validez-causa-cpu` (otra sesión) | CPU | ¿Cuál es el error real de las tareas que no sirven? | En 34 falta un paquete que solo usan las pruebas | Terminada |
| 8 | `iteracion-01` | GPU | ¿Gana el diseño público de dos etapas? ¿Y 100 llamadas? | 3, 3, 3 y 2 de 15; ninguna gana | Terminada |
| 9 | `validez-con-paquetes` | CPU | ¿Se recuperan las tareas instalando esos paquetes? | De 71 a 103 válidas; ninguna de las 71 se pierde | Terminada |
| 10 | `iteracion-02` | GPU | ¿Qué hace el agente al adelantar el aviso o al pedírselo por escrito? ¿Llega al archivo correcto? | 2, 2 y 4 de 15; la regla escrita no adelanta la edición; lee el archivo correcto en 6 de 9 tareas cortas | Terminada |
| 11 | `iteracion-03` | GPU | ¿Se sostiene el umbral de 250 caracteres en tareas no vistas? ¿Sigue llamando tras la primera negativa? ¿Repite después del resumen del arnés? | 3 de 15 en rich, 3 de 15 en fastapi no vistas, 0 de 13 en requests; 0 de 15 de enunciado corto; el bucle empieza antes del resumen y de la negativa | Terminada |
| 12 | `iteracion-04` | GPU | El mismo notebook byte a byte: ¿cuántas tareas cambian de resultado entre dos pasadas iguales en fastapi no vistas (el ruido) y en rich? | 3 de 15 en rich, 4 de 15 en fastapi, 1 de 13 en requests; cambian de resultado 0, 1 y 1 tareas; se cumplen P27, P28 y P29, se refuta P30 | Terminada |
| 13 | `iteracion-05` | GPU | Con una línea más en la instrucción (candidato `h_edicion`), ¿dejan de quedar sesiones atrapadas repitiendo `edit_file` sin `old_string`? | 7 de 30 (rich 3, fastapi 4), igual que la base; 0 sesiones atrapadas (base 3 y 3) y 0 llamadas a `edit_file` sin `old_string` (base 107 y 49); se cumple P32, P33 dentro del ruido, P34 sin casos | Terminada |
| 14 | `iteracion-06` | GPU | Con la condición del envío 56895202 (razonamiento encendido, 60 llamadas, 4,5 min), ¿el agente llega a editar en las tareas resolubles, o se queda sin tiempo? | 9 de 19 (base 6, 7 y 7): tres tareas nunca resueltas antes, dos de enunciado corto; 9 de 10 fallos por tiempo agotado; P36 se cumple, P35, P37 y P40 no deciden | Terminada |
| 15 | `iteracion-07` | GPU | Segunda pasada de la condición del envío (`i_razona`) sobre 10 tareas: las 7 ya resueltas y las 3 que la 06 resolvió por primera vez. ¿Se repiten? | 9 de 10. Las 3 nuevas de la 06 se repiten (3 de 3) y de las 7 ya resueltas se mantienen 6; 0 rechazos por contexto. P41, P42 y P43 se sostienen. No se compara con los 9 de 19: las diez se eligieron por haberse resuelto | Terminada |

**Armada y no subida:** iteración 08 (la base dos veces sobre 60 tareas sorteadas entre las 71 válidas, con el
registro nuevo; 6,9 a 9,0 h de cuota). No está lista para lanzar: falta repetir el ensayo local con la versión
de `ipykernel` de Kaggle, el análisis que excluye los pares faltantes, cuota de 14,6 h o más y la orden del
dueño. Vueltas 40 a 42 de la bitácora.

**Aviso sobre las filas 11 a 15:** el 2026-10-08 un verificador halló que los 145 logs por tarea de las
iteraciones 03 a 07 tienen 0 bytes. Las cifras de resueltas valen (salen de los resultados y las trazas), pero
ninguna de esas corridas cumple el criterio de «corrida válida» aprobado ese día.

`iteracion-01` se subió cuatro veces antes de ejecutarse: tres resubidas para cambiar el plan o añadir medidas.

## Ficha de la prueba 10 · `iteracion-02`

| Campo | Valor |
|---|---|
| Subida | 2026-10-05, 02:21 UTC. Una sola subida. Aprobada por el dueño con un «súbela» explícito |
| Notebook | `cs4all/iteracion-02`, versión 1, privado, sin Internet, cuatro GPU L4 |
| Huella del notebook subido | `e3d693ca350b83ef…`; el contenido remoto se comparó celda por celda con el validado y coincide |
| Tareas | Las mismas 15 de rich de `iteracion-01`: 9 de enunciado corto y 6 de enunciado largo |
| Pasadas, en orden | Tope 20 → enviada (tope 40) → regla escrita (tope 40) |
| Qué cambia en cada una | Tope 20: solo `max_tool_calls`, de 40 a 20. Regla escrita: tres líneas añadidas a la instrucción, 291 caracteres |
| Huellas de las configuraciones | Enviada `3b0e87556166`, tope 20 `59dc90d2ecc3`, regla escrita `2aa3c76ad0ce` |
| Tope del notebook | 150 minutos |
| Costo estimado | 75 minutos de sesión, unas 2,5 horas de cuota |

**Qué responde.**

1. Si adelantar el aviso del arnés adelanta la edición en las 3 tareas de enunciado largo que editaban justo
   después de él.
2. Si pedirlo por escrito consigue lo mismo sin recortar el presupuesto.
3. Si, en las tareas de enunciado corto, el agente llega a leer el archivo que había que corregir.

**Qué no responde.** Si alguna de las dos resuelve más tareas: con 15 tareas, y 9 de ellas nunca resueltas por
ninguna configuración, no se puede ver un daño ni una mejora menor que 3 tareas.

**Predicciones escritas antes de correr** (vueltas 14, 16 y 17 de la bitácora):

| Id | Estrato | Predicción | Se cumple | La refuta |
|---|---|---|---|---|
| P12 | Todas | Con tope 20, tareas que editan antes de la llamada 14 | 9 o más de 15 | 5 o menos |
| P13 | Todas | Con tope 20, sesiones sin ninguna edición | 3 o menos | 5 o más |
| P14 | Todas | Con tope 20, tareas resueltas | 2 o más | 0, si la enviada resuelve 2 o más |
| P15 | Todas | Con la regla escrita, tareas que editan antes de la llamada 14 | 5 o menos | 9 o más |
| P16 | Largo | Con tope 20, las 3 tareas que editaban tras el aviso editan antes de la llamada 14 | 2 o 3 | 0 |
| P17 | Largo | Con tope 20, tareas resueltas | 2 o más | 0, si la enviada resuelve 2 o más |
| P18 | Largo | Con la regla escrita, esas 3 tareas editan antes de la llamada 14 | 0 o 1 | 2 o 3 |
| P19 | Corto | Con tope 20, sesiones que entregan parche | 5 o más | 2 o menos |
| P20 | Corto | Con cualquiera de las dos, tareas resueltas | 0 | 1 o más |
| P21 | Corto | En la enviada, el agente lee el archivo corregido | 4 o menos de 9 | 5 o más |

**Decisiones fijadas antes de correr.**

- El tope 20 es un diagnóstico. No pasa a ser candidato, salga lo que salga.
- La regla escrita es candidata solo si adelanta la edición.
- Si P21 se refuta, el problema de las tareas cortas es de comprensión y no de búsqueda.

**Validado sin GPU antes de subir.**

| Comprobación | Resultado |
|---|---|
| Chequeo previo del repositorio, con tope de 150 minutos | Se puede subir |
| Guardia de entradas en las dos disposiciones de Kaggle | Pasa en ambas |
| Todas las celdas compilan | Sí, 11 celdas |
| Ensayo local de las tres pasadas con el arnés real y un modelo que repite llamadas | Flujo, archivo de resultados y limpieza correctos; el aviso llega tras la llamada 10 con tope 20 |
| Contador de repeticiones por herramienta | Prueba con traza sintética |
| Contador de empujones, tres textos del arnés | Prueba con traza sintética |
| Regla «comando que puede escribir» | 16 casos, ninguno mal clasificado |
| Contador de ubicación del archivo corregido | Prueba con traza sintética |
| Las tres configuraciones compilan y pasan las cuatro comprobaciones del simulacro | Sí |

**Errores propios que atrapó la validación.** La primera versión de la regla de escritura tenía un error de
sintaxis; lo detuvieron el chequeo previo y el ensayo local.

**Qué guarda por tarea.** Resultado y clase de final; llamadas y minutos; en qué llamada ocurre la primera
edición y el primer aviso; repeticiones sin cambio, por herramienta; empujones del arnés; comandos que pueden
escribir; en qué llamada el agente ve, lee y edita el archivo corregido; largo del enunciado.

**Seguimiento de la cola.**

| Hora UTC del 2026-10-05 | Estado | Dato |
|---|---|---|
| 02:21 | En cola | Subida |
| 11:03 | En cola | 8 h 42 min de espera, más que la mayor vista antes (8 h 20 min). Kaggle no informa error. Ningún otro notebook de la cuenta está corriendo. El contenido remoto sigue igual al validado, en versión 1 |
| 11:05 | En cola | Cuota semanal de GPU: 13,41 h usadas de 30; 0 h reservadas; reinicio el 2026-10-10 a las 00:00. La cuota no es la causa de la espera |

**Resultado.** Terminada: 5 433 s de sesión. Tope 20: 2 de 15. Enviada: 2 de 15. Regla escrita: 4 de 15; la
diferencia es igual a las tareas que cambian entre pasadas iguales. Se cumplen P14, P15, P17, P18 y P20; se
refutan P12, P13, P16, P19 y P21. Contraste completo en la vuelta 19 de la bitácora. Datos crudos en
`data/rescate_kaggle/iteracion-02/`. El `__results__.html` no se recuperó: la API no lo entrega.

## Ficha de la prueba 11 · `iteracion-03`

| Campo | Valor |
|---|---|
| Subida | 2026-10-06, hora en el seguimiento de la cola. Una sola subida. Ordenada por el dueño («Adelante, luego avanzar en la carga») tras aplicar las correcciones de la revisión independiente |
| Notebook | `cs4all/iteracion-03`, versión 1, privado, sin Internet, cuatro GPU L4 |
| Huella del notebook subido | `a463dc724073e9fa…`, 55 120 bytes |
| Tareas | 43 en una pasada: 15 de rich conocidas (las de `iteracion-01` y `02`), 15 de fastapi no vistas (9 de enunciado largo, 6 corto), 13 de requests no vistas (ninguna discrimina en el sandbox: sirven para la traza, no para contar resueltas) |
| Pasadas, en orden | rich → fastapi → requests, todas con la configuración enviada |
| Qué cambia | Nada en el agente. El instrumento guarda además cada petición al modelo (forma y presencia del enunciado), los resúmenes del arnés, el parche y la salida de pytest por tarea; corta por tope de tareas (120 min), por tope de sesión (140 min desde el arranque) o si el servidor deja de responder |
| Tope del notebook | 150 minutos |
| Costo estimado | 75 a 100 minutos de sesión, 2,5 a 3,3 horas de cuota; peor caso 150 minutos, 5 horas |

**Qué responde.** P22 a P26 (vuelta 23 de la bitácora): si el umbral de 250 caracteres se sostiene en tareas no
vistas; si el modelo sigue llamando tras la primera negativa del arnés; si las repeticiones empiezan después del
primer resumen o de la primera negativa; si tras el primer resumen el enunciado desaparece de la petición; y si
rich conocidas sigue en 2 a 4 de 15.

**Validado sin GPU antes de subir.**

| Comprobación | Resultado |
|---|---|
| Revisión independiente del notebook (revisor aparte) | «Se puede subir», sin bloqueantes; 3 objeciones importantes y 4 menores, todas aplicadas salvo una sin efecto |
| Chequeo previo del repositorio, con tope de 150 minutos | Se puede subir, 19 comprobaciones |
| Ensayo completo con el arnés real y el parche de referencia | 43 de 43; rich 14 de 15, fastapi 15 de 15, requests 3 de 13 |
| Ensayo largo (hasta 100 llamadas por tarea) | 43 de 43; resúmenes capturados iguales a los recibidos; presencia del enunciado igual a la vista por el modelo falso en las 43 |
| Ensayo con tope de sesión de 200 s | Corta por sesión tras 14 tareas |
| Ensayo con el servidor caído tras 60 peticiones | Lo detecta antes de la tarea siguiente, guarda el archivo y corta; el arnés no lanza excepción |

**Seguimiento de la cola.**

| Hora UTC del 2026-10-06 | Estado | Dato |
|---|---|---|
| 02:47 | En cola | Subida, versión 1. Ningún otro notebook de la cuenta en cola. El contenido remoto se bajó y coincide con el validado en las 11 celdas; metadatos remotos: privado, GPU, sin Internet, imagen fijada, `NvidiaL4` |
| 13:14 | En cola | 10 h 27 min de espera, más que la mayor vista antes (8 h 42 min). Kaggle no informa error por API. Ningún otro notebook de la cuenta corre. Cuota: 16,43 h usadas de 30, sin movimiento; la cuota no es la causa. Una consulta por hora desde las 02:47 |
| 13:45 | En ejecución | Pasó a correr entre las 13:14 y las 13:45 (unas 11 h de cola). A las 13:50 la cuota marca 17,38 h usadas: lleva unos 28 min de sesión |
| 14:48 | Terminada | Completa, sin cortes; 2,96 h de cuota. Se cumplen P22, P25 y P26; se refutan P23 y P24. Contraste en la vuelta 25 de la bitácora. Datos crudos en `data/rescate_kaggle/iteracion-03/` |

## Ficha de la prueba 12 · `iteracion-04`

| Campo | Valor |
|---|---|
| Subida | 2026-10-06, 13:45 UTC. Una sola subida. Ordenada por el dueño con un «Súbela, iteracion-04 también», con `iteracion-03` todavía en cola (dos sesiones en cola, el máximo de la cuenta; la regla 2 de la instrucción pedía una) |
| Notebook | `cs4all/iteracion-04`, versión 1, privado, sin Internet, cuatro GPU L4, imagen fijada |
| Huella del notebook subido | `a463dc724073e9fa…`, la misma de `iteracion-03`: el archivo es idéntico byte a byte; solo cambian el id y el título en los metadatos. El contenido remoto se bajó y coincide en las 11 celdas |
| Tareas y pasadas | Las mismas 43 en el mismo orden: rich conocidas (15), fastapi no vistas (15), requests no vistas (13), con la configuración enviada |
| Qué cambia | Nada. Es la segunda pasada igual que exige la regla 2.2 de la instrucción: sin ella no hay ruido medido en fastapi y ninguna mejora se podría leer ahí |
| Tope del notebook | 150 minutos |
| Costo estimado | 75 a 100 minutos de sesión, 2,5 a 3,3 horas de cuota; peor caso 150 minutos, 5 horas. Con `iteracion-03` corriendo, el peor caso conjunto deja 3,6 h de cuota, por debajo de la reserva de 5 h; el caso típico deja unas 7 h |

**Qué responde.** El ruido entre dos pasadas iguales en cada grupo, que es la vara con la que se leerá cualquier
cambio posterior (regla 3 de la bitácora).

**Predicciones escritas antes de correr** (se leen contra `iteracion-03`):

| Id | Estrato | Predicción | Se cumple | La refuta |
|---|---|---|---|---|
| P27 | rich conocidas | Tareas que cambian de resultado entre las dos pasadas, como en `iteracion-01` | 2 o menos de 15 | 4 o más |
| P28 | fastapi no vistas | Tareas que cambian de resultado entre las dos pasadas | 3 o menos de 15 | 5 o más |
| P29 | Todas | La clase de desenlace cambia en más tareas que el resultado, como en los json de `iteracion-01` y `02` (6 a 10 frente a 0 a 2) | al menos el doble | en menos tareas que el resultado |
| P30 | requests no vistas | Resueltas en ambas pasadas, porque ninguna discrimina en el sandbox | 0 | 1 o más en alguna |

**Validado sin GPU antes de subir.** El mismo notebook y las mismas comprobaciones de la ficha 11; el chequeo
previo se repitió sobre el kit de la 04 y se encadenó a la orden de subida.

**Seguimiento de la cola.**

| Hora UTC del 2026-10-06 | Estado | Dato |
|---|---|---|
| 13:45 | En cola | Subida, versión 1. `iteracion-03` corriendo al mismo tiempo. Contenido remoto igual al validado en las 11 celdas |

## Ficha de la prueba 13 · `iteracion-05`

| Campo | Valor |
|---|---|
| Orden del dueño | «Lee iteracion-04 y mide solo el candidato», 2026-10-06. Es una corrida de medición, no un envío al concurso |
| Operador | Una sola sesión sube: la de Datito. Ninguna otra sube este notebook |
| Notebook | `cs4all/iteracion-05`, privado, sin Internet, cuatro GPU L4, imagen fijada (la misma de la 03 y la 04) |
| Huella del notebook | `eb9fdbe6ea4fc110…`, 55 251 bytes |
| De dónde sale | El notebook de `iteracion-03` y `04` con tres cambios: la condición, los grupos y los nombres de salida. Las celdas 0 a 3, 5 a 8 y 10 quedan byte a byte (`instrumentos/iteracion_05/armar.py`) |
| Condición | `h_edicion` versión 2: los seis archivos de la enviada, y solo cambia `prompts/system.md` con una línea más (de 3 888 a 4 222 caracteres). Huella de la condición `7e2082197834`; zip `598236b202051175…`. El armador comprueba que la condición de la 04 es byte a byte la enviada |
| Tareas | 30 en una pasada: las 15 de rich conocidas y las 15 de fastapi no vistas de la 03 y la 04, en el mismo orden. Sin requests |
| Base de comparación | `iteracion-03` y `iteracion-04`, que corrieron la condición enviada sobre esas mismas 30 tareas |
| Tope del notebook | 150 minutos |
| Costo estimado | 30 tareas a unos 102 s más la carga del modelo (6 a 19 min): 57 a 70 min de sesión, 1,9 a 2,3 h de cuota. Peor caso 150 min, 5 h |

**Predicciones escritas antes de correr.**

| Id | Predicción | Se conserva | Se descarta |
|---|---|---|---|
| P32 | Sesiones atrapadas en `edit_file` sin `old_string` (3 fallos seguidos o más). Base en `iteracion-03`: 3 de 30 | 1 o menos | 3 o más |
| P33 | Resueltas en las 30. Base en `iteracion-03`: 6 | 5 a 8; solo se declara mejora con 9 o más | 3 o menos |
| P34 | En las sesiones donde `edit_file` falla por parámetros, el agente pasa a `run_command` o `write_file` en la llamada siguiente | en la mitad o más | en ninguna |

Lectura: P32 decide. Si la 04 da una base distinta de 3 de 30, se usa el promedio de las dos. Con 2 sale «no
concluyente». El foro del concurso informa que las reglas escritas no rompen los bucles: mi probabilidad de que
P32 se cumpla es baja, cerca de 1 en 3.

**Validado sin GPU antes de subir.**

| Comprobación | Resultado |
|---|---|
| Chequeo previo del repositorio, con tope de 150 minutos | Se puede subir, 19 comprobaciones; repetido justo antes de la subida |
| Ensayo completo en Docker con el arnés real y el parche de referencia | 30 de 30 validadas, 0 problemas, 430 s; rich 14 de 15 y fastapi 15 de 15, igual que en la 03; el modelo recibió los parámetros del envío |
| Simulacro del zip del candidato (arnés real, modelo falso, 2 tareas, 4 modos) | Los 8 desenlaces coinciden con lo esperado |
| Compilación del zip del candidato con `adk-submission` | Válido |
| El notebook no existía en Kaggle antes de subir | Comprobado por API |

Sin ensayo largo ni de servidor caído: esas rutas del notebook no cambiaron respecto de la 03.

**Seguimiento de la cola.**

| Hora UTC del 2026-10-06 | Estado | Dato |
|---|---|---|
| 20:09 | En cola | Subida, versión 1, una sola subida. El contenido remoto se bajó y coincide con el validado en las 11 celdas; metadatos remotos: privado, GPU, sin Internet, imagen fijada, `NvidiaL4`. `iteracion-04` en ejecución al mismo tiempo. Cuota no leída: exige la sesión web |
| 20:15 | En ejecución | Salió de la cola en menos de 6 minutos |
| 21:12 | Terminada | Completa, sin cortes. Carga del modelo 390 s; las tareas empezaron a los 483 s de sesión; 99 s por tarea: unos 58 min de sesión, cerca de 1,9 h de cuota (estimado; la cuota no se leyó). Datos crudos en `data/rescate_kaggle/iteracion-05/` |

## Ficha de la prueba 14 · `iteracion-06`

| Campo | Valor |
|---|---|
| Orden del dueño | «mídela», 2026-10-07: las 19 tareas, la condición enviada, la misma regla de conservar o descartar. Acepta quedar bajo la reserva de 5 h hasta el reinicio del 2026-10-10 |
| Operador | Una sola sesión sube: la de Datito |
| Notebook | `cs4all/iteracion-06`, privado, sin Internet, cuatro GPU L4, imagen fijada |
| Huella del notebook | `f172380f781d567d…`, 54 636 bytes |
| De dónde sale | El notebook de la 03 y la 04 con tres cambios: condición, tareas y nombres de salida (`instrumentos/iteracion_06/armar.py`). Nueve celdas quedan byte a byte |
| Condición | `i_razona`, la del envío 56895202: los seis archivos de la enviada con `include_thoughts: true`, 60 llamadas y 4,5 min. Huella de la condición `0f52de0b84cb`; zip `65a0216007e19bf6…` |
| Tareas | 19 de las 30 de rich y fastapi, en su orden de siempre: las 12 que el concilio juzgó resolubles y las 7 ya resueltas (8 de rich, 11 de fastapi) |
| Base de comparación | Las mismas 19 tareas en `iteracion-03`, `04` y `05`: 6, 7 y 7 resueltas |
| Tope del notebook | 150 minutos; las tareas se cortan a los 120 |
| Costo estimado | Peor caso 19 × 4,5 min más verificación y carga: unos 100 a 115 min de sesión, 3,4 a 3,8 h de cuota |

**Predicciones escritas antes de correr** (P35 a P37 de la vuelta 32, con el tope de 4,5 min que se envió).

| Id | Predicción | Se conserva | No decide | Se descarta |
|---|---|---|---|---|
| P35 | Resueltas de 19 (base 7, ruido 1) | 10 o más | 9 | 8 o menos |
| P36 | De las 7 ya resueltas, se mantienen | 6 o 7 | — | 5 o menos |
| P37 | Sesiones que terminan por tiempo agotado | 6 o menos de 19 | 7 a 9 | 10 o más: lo que ata es el tiempo |
| P40 | De las 12 resolubles, llegan a editar el archivo de la corrección | 6 o más (base: 2 llegan a la región correcta) | 3 a 5 | 2 o menos |

Lectura: P35 y P36 deciden si la condición se conserva. P37 y P40 dicen por qué: si el agente llega a editar y
no resuelve, el freno es el contenido; si no llega y agota el tiempo, es el tope; si no llega y agota las
llamadas, el razonamiento no arregla el recorrido.

**Validado sin GPU antes de subir.**

| Comprobación | Resultado |
|---|---|
| Chequeo previo del repositorio, con tope de 150 minutos | Se puede subir, 19 comprobaciones |
| Ensayo completo en Docker con el arnés real y el parche de referencia | 19 de 19 validadas, 0 problemas, 257 s; rich 7 de 8 y fastapi 11 de 11, como en los ensayos anteriores; el modelo recibió razonamiento encendido con presupuesto 4 096 y 8 192 tokens |
| Simulacro y compilación del zip de la condición | 8 de 8 desenlaces; válido (vuelta 33) |
| El notebook no existía en Kaggle antes de subir | Comprobado por API |

**Seguimiento de la cola.**

| Hora UTC del 2026-10-07 | Estado | Dato |
|---|---|---|
| 00:37 | Subida | Versión 1, una sola subida. El contenido remoto coincide con el validado en las 11 celdas; privado, GPU, sin Internet, imagen fijada, `NvidiaL4` |
| 00:38 | En ejecución | Arrancó sin cola |
| 02:13 | Terminada | Completa, sin cortes. Carga del modelo 828 s; 248 s por tarea: unos 92 min de sesión, cerca de 3,1 h de cuota (estimado). Contraste en la vuelta 37 de la bitácora. Datos crudos en `data/rescate_kaggle/iteracion-06/` |
