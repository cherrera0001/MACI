# Hipótesis Zorzal

**Aprobada por el dueño el 2026-10-04.** Umbrales congelados a las 22:30 UTC, antes de leer ninguna corrida.
La versión que manda está en el repositorio de ALL, PR #145 (borrador):
`experiments/gemma_developer_agent/zorzal/`. Allí cada criterio de aceptación es una prueba.
Todo lo que sigue es hipótesis: ningún resultado propio la respalda todavía.

## La idea

Un zorzal no gana por fuerza. Camina, se detiene, ladea la cabeza y escucha lo que hay bajo la tierra. Pasa
casi todo el tiempo quieto. Cuando ataca, lo hace una vez.

Gemma 4 es un modelo pequeño con un presupuesto fijo. No puede ganar por fuerza. La hipótesis es que gana
igual que el zorzal.

> **Un modelo pequeño resuelve más tareas cuando escucha antes de actuar y actúa una sola vez, que cuando
> usa el mismo presupuesto en actuar muchas veces.**

## Los cinco rasgos, convertidos en algo que se cuenta

Cada rasgo se mide en la traza de una tarea, con conteos que el notebook ya guarda. No hace falta leer el
texto de la tarea.

| Rasgo | En el agente | Cómo se cuenta | Se cumple si |
|---|---|---|---|
| **Busca** | Recorre el código antes de tocarlo | Llamadas anteriores a la primera edición | Hay al menos una lectura o búsqueda antes de editar |
| **Oye** | Toma la señal de la ejecución, no solo las palabras del problema | Comandos que ejecutan pruebas o una comprobación | Ejecutó al menos una antes de entregar |
| **Observa** | Nota lo que ya falló | Llamadas idénticas a una que ya había fallado | Cero |
| **Espera** | No gasta el presupuesto en moverse | Llamadas totales frente al límite | Terminó sin agotar el límite |
| **Acierta** | Un golpe pequeño y comprobado | Ediciones y entregas | A lo más 3 ediciones y una entrega |

Una sesión tiene **perfil zorzal** si cumple los cinco.

«Oye» tiene una razón propia de ALL. En los resultados previos sin modelo de lenguaje, la memoria que se
guiaba por las palabras del problema acertó 0 de 18 veces cuando el problema nombraba la parte equivocada. La
superficie engaña; la ejecución no.

## Las tres hipótesis, con lo que las refuta

**H-Z1 · El perfil acompaña al acierto.** Entre las tareas válidas, las sesiones con perfil zorzal se resuelven
con más frecuencia que las que no lo tienen.

- La refuta: una frecuencia igual o menor.
- Límite: es una observación, no una causa. Una tarea fácil produce una sesión limpia. Sirve para descartar la
  idea barato, no para probarla.

**H-Z2 · Inducir el perfil sube el resultado.** Una configuración que enseña a escuchar antes de actuar resuelve
más tareas que la enviada, y más que un texto de relleno del mismo largo, sobre las mismas tareas.

- La refuta: una ventaja menor o igual que el ruido medido entre dos pasadas iguales, o un relleno que rinde lo
  mismo.
- Comprobación previa: la configuración tiene que cambiar el perfil. Si las sesiones con perfil zorzal no
  aumentan, la corrida no puso a prueba la hipótesis y no cuenta ni a favor ni en contra.

**H-Z3 · La paciencia tiene un costo y hay que pagarlo.** Escuchar gasta tiempo. Con la configuración zorzal,
las tareas que terminan por tiempo agotado no aumentan.

- La refuta: más tareas cortadas por tiempo que con la enviada.

H-Z2 es la hipótesis del artículo. H-Z1 y H-Z3 la acotan.

## Lo que hoy se sabe, sin adornos

| Dato | Qué sugiere | Cuánto vale |
|---|---|---|
| En la única corrida propia, una tarea usó 39 de 40 llamadas en 100 segundos y no produjo parche | El agente se mueve mucho y no acierta | 1 tarea |
| El modelo generó 57 tokens por turno con el razonamiento apagado | Actúa sin detenerse | 2 tareas |
| El envío público con más nota separa una etapa que solo lee de una que edita una vez | Un diseño parecido al zorzal existe y puntúa | Una nota de otro equipo |
| H8, sin modelo de lenguaje: la señal de la ejecución calló en 7 de 9 tareas y eligió mal en la que habló | Escuchar no garantiza elegir bien | Resultado negativo, propio |

Nada de esto prueba la hipótesis. El último dato va en contra de una parte de ella y se queda en la tabla.

## Lo que falta por oír

Las dos corridas que ya están ejecutándose guardan los conteos de los cinco rasgos. De ellas sale, sin lanzar
nada nuevo:

1. Cuántas sesiones de la configuración enviada tienen perfil zorzal.
2. Si el diseño público de dos etapas tiene más sesiones con ese perfil. Es una primera lectura de H-Z1.
3. El ruido: cuántas tareas cambian entre dos pasadas iguales.

**Un límite de la medida actual.** «Oye» se cuenta hoy solo por los comandos que nombran pytest. Una
comprobación escrita en línea, como la que usa el diseño público, no se cuenta, y tampoco se guarda si ocurrió
antes de entregar. Ese rasgo saldrá subestimado en estas dos corridas. Hay que corregir el conteo antes de la
prueba de H-Z2.

Con 15 tareas solo se ven efectos grandes. Una prueba de H-Z2 que se pueda creer necesita tareas que no
participaron en la elección, y el texto de relleno.

## La misma hipótesis, aplicada a nosotros

El principio vale para quien opera, y hoy se puede contar.

| Rasgo | Cómo operamos hoy | La regla |
|---|---|---|
| Busca | Se subió un notebook para averiguar algo que estaba en el disco | Antes de pedir un dato nuevo, recorrer lo que ya existe |
| Oye | Se leyó el resumen y no el log | Leer la salida completa |
| Observa | Tres cambios sobre el mismo párrafo; dos corridas que se solapan | Cruzar lo que hicieron las otras sesiones |
| Espera | Un mismo notebook subido cuatro veces antes de dar un resultado | Mientras la señal no sea clara, no actuar |
| Acierta | Ocho horas de cola perdidas por una ruta de archivos | Una acción, la de más evidencia, y volver a escuchar |

**H-O · Operar como zorzal cuesta menos.** Con un informe previo a cada acción (qué oí, qué vi, qué falta, la
única acción), el número de subidas por resultado útil baja a una, y ninguna corrida falla por una causa que
se podía ver sin GPU.

- Punto de partida, hoy: cuatro subidas de `iteracion-01` y tres versiones de `prueba-a-ajustada` para un
  resultado.
- La refuta: más de una subida por resultado, o una corrida perdida por una causa visible en local, en la
  semana siguiente.

## Decisiones tomadas

1. H-Z2 es la hipótesis del artículo, con la medición de validez como su primer caso.
2. Los umbrales quedan como en la tabla. El de 3 ediciones tiene ahora respaldo: es el percentil 75 de los
   bloques de cambio de las soluciones de referencia en las 71 tareas válidas (mediana 2).
3. H-O se mide del 2026-10-05 al 2026-10-11, con una bitácora de subidas.

Mientras «oye» siga mal medido, el perfil que decide lo deja fuera. La ventaja exigida es el ruido más una
tarea, y nunca menos de 2.

## Lo que cambió después (2026-10-05)

**El nombre.** La propuesta se llama ZorzALL.

**La revisión independiente.** Tres revisores la pusieron a prueba. Veredicto: solo con cambios.

- La regla de decisión «ruido más una tarea» estaba mal planteada.
- H-Z1 es en parte una tautología y pasa a ser exploratoria.
- H-O no es una hipótesis: es un indicador de operación.
- Lo que queda como contraste es uno solo: el arnés base con texto de relleno, contra el arnés ZorzALL, con los
  mismos topes. Aún sin registrar como versión 2.

**La definición corregida, propuesta por la otra sesión.** Escucha, resuelve, comprueba. Sustituye «acierta
una vez» por «resuelve», las veces que haga falta. Espera aprobación como versión 2.

**Lo que dijeron los datos.** El perfil de las tareas resueltas se parece al de ZorzALL: pocas llamadas, sin
repeticiones, una edición. Pero la causa principal de no resolver no está en la conducta del agente: está en
las tareas cuyo enunciado es solo un título. Ahí ninguna configuración resolvió nada, en 66 pasadas.

**Lo que eso le pide a ZorzALL.** «Oír» no puede significar solo ejecutar las pruebas. En un tercio de las
tareas no hay descripción del defecto, y el agente tiene que deducirlo del código que rodea las palabras del
título. Ese es el caso que la hipótesis todavía no cubre.
