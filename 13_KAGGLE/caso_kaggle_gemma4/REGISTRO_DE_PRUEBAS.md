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
| 10 | `iteracion-02` | GPU | ¿Qué hace el agente al adelantar el aviso o al pedírselo por escrito? ¿Llega al archivo correcto? | — | **En cola desde el 2026-10-05 02:21** |

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

**Resultado.** Pendiente.
