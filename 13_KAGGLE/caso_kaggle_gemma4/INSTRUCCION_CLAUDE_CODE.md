# Prompt único para Claude Code en `Agents Learning Loops`

> **Vigencia (2026-10-04, 21:33 UTC).** Documento fechado. Desde que se escribió hubo una corrida con el
> modelo, se midió la validez de las tareas y cambió el título del manuscrito. El estado vigente está en
> [`README.md`](README.md), sección 1.6, y en [`RECORRIDO_PASO_A_PASO.md`](RECORRIDO_PASO_A_PASO.md).

Versión 3, del 2026-10-04 01:40 UTC. Reemplaza a todas las anteriores.
Se pega completo en una sesión abierta en `F:\Code\Agents Learning Loops`.
El análisis que lo justifica está en [`README.md`](README.md) de esta carpeta.

## Qué se validó antes de escribirlo

Cada instrucción anterior, contrastada con el repositorio y con Kaggle a las 01:40 UTC:

| Instrucción anterior | Estado | Evidencia |
|---|---|---|
| Enviar la condición A | Cumplida | Envío 56808559, 2026-10-03 23:46 UTC; sigue «pendiente» |
| Leer foro y notebooks | Cumplida | Comentario en #103 con fuentes |
| Registro igual a lo enviado | Cumplida | `33c0ddd`: `sub-002` con SHA-256 `d8a3e1d3…` |
| El empaquetador falla sin compilador | Cumplida | `33c0ddd`, con test |
| Enmienda 2 antes de conocer la nota | Cumplida | `fce9f5f`, 00:47 UTC, con los tres cambios pedidos |
| Commits en rama, sin fusionar | Cumplida | Rama `issue-106-envio-code-track`; `main` sigue en `4af63cc` |
| Reportar la cuota real | Cumplida | 0,87 h usadas de 30; quedan 29,13 h |
| No reenviar sin resultado | Cumplida | Ningún reenvío |
| Ensayo de notebook | **Bloqueada** | El servidor del modelo cae a los 474 s y a los 753 s; el error no se leyó |
| No crear documentos nuevos | **Incumplida** | `6b79d12` versionó dos páginas HTML en `drafts/` |
| Explicar los tres procesos en marcha | **Sin respuesta** | — |

Instrucciones retiradas por ser falsas o estar resueltas: «cuota 0,00 h», «ensayo con 2
tareas» y «averiguar si la cuenta ve L4×4».

---

## El prompt

```text
Eres el único responsable del experimento Kaggle en este repositorio. Trabajas en la rama
issue-106-envio-code-track, sin fusionar a main. Este prompt reemplaza a todos los anteriores.

OBJETIVO
Que el agente del envío mejore de forma medida. Eso exige dos cosas, en este orden:
primero poder correr el modelo y contar tareas resueltas; después cambiar una cosa a la vez
y conservar solo lo que mejora. Sin la primera, la segunda es adivinar.

ESTADO VERIFICADO (2026-10-04 01:40 UTC)
- Envío 56808559 (kit ajustado, SHA-256 d8a3e1d3…): pendiente, sin nota ni error.
- Enmienda 2 versionada en fce9f5f: A es el kit ajustado. Registro de envíos correcto.
- Cuota de GPU: 0,87 h usadas de 30; se reinicia el 2026-10-10 00:00 UTC y no se acumula.
- Bloqueo: con scripts/kaggle_ensayo.py el servidor del modelo cae a los 474 s y a los 753 s.
  El error de vLLM nunca se leyó.
- En cola: el notebook privado cs4all/prueba-a-ajustada (notebook oficial + zip enviado,
  2 tareas, tope 75 min).
- Corridas propias con el modelo: cero.

REGLAS PERMANENTES
1. Un cambio por corrida. Nunca dos a la vez.
2. Antes de cada corrida con GPU me dices su costo en horas de cuota y su tope en minutos.
   Una sola sesión de GPU en cola a la vez. Ninguna sin tope.
3. Me pides aprobación antes de: cada envío a Kaggle, cada enmienda del pre-registro y
   cualquier corrida que gaste más de 4 h de cuota.
4. Nada de contenido de la competencia en commits, PR, issues ni en tus informes: ni
   enunciados, ni parches, ni pruebas, ni salidas de tareas. Solo conteos y medidas.
5. Las tareas de fastapi no se usan para mejorar nada. Son la prueba reservada.
6. Ningún guion, documento ni pre-registro nuevo, salvo la bitácora de la Fase 2.
7. Cada afirmación lleva su evidencia: comando, salida o enlace. Separa lo verificado de lo
   supuesto. Si algo falla, primero el error textual y la causa; después la propuesta.

FASE 0 — CERRAR LO PENDIENTE (hoy)
0.1 Dime qué eran los tres procesos que quedaron corriendo y en qué estado están.
0.2 Las dos páginas HTML de drafts/ ya están versionadas: quedan así. No hagas más.
0.3 La Enmienda 2 bajó timeout_seconds a 60 y scripts/kaggle_validez.py lo hereda. No lo
    cambies todavía. Averigua en HARNESS qué límite de tiempo rige la verificación de un
    parche (la segunda fase) y dime si es el mismo campo. Con ese dato decido.
0.4 Envío 56808559: cuando tenga nota o error, anótalo en #106 y en registry.json, en un
    commit aparte. Si es error, dime si el total superó las 12 horas y no reenvíes.

FASE 1 — DESBLOQUEAR EL MODELO (antes del 2026-10-10)
1.1 Lee el resultado de cs4all/prueba-a-ajustada. Es el experimento que separa las causas:
    - Si el servidor arranca ahí, el fallo está en cómo kaggle_ensayo.py lanza vLLM.
      Arréglalo usando VllmServer del arnés, igual que el notebook oficial. Solo eso.
    - Si tampoco arranca, el problema es del entorno y no del guion. Detente y me informas.
1.2 En toda corrida, escribe la salida de error del servidor en /kaggle/working, para que
    no se pierda al cerrar la sesión. De ese archivo solo me reportas las líneas del error.
1.3 Entrega de esta fase, cuatro números: segundos de carga del modelo, tokens por segundo,
    minutos de montaje por tarea y minutos totales de dos tareas.
1.4 Con el montaje medido, comprueba la cuenta de las 12 horas: tareas × (4 min + montaje)
    + carga. Si no cabe, me propones el nuevo valor de minutos por tarea.
Tope de esta fase: dos corridas con GPU. Si a la segunda el servidor no arranca, te detienes.

FASE 2 — CICLO DE MEJORA (empieza cuando la Fase 1 entregue sus cuatro números)
Es exploratoria. No reemplaza a la línea base pre-registrada ni a la campaña.

2.1 Conjunto de desarrollo. Veinte tareas de los repositorios de entrenamiento (rich,
    requests, httpx), elegidas por orden de sha256(instance_id). Antes de usarlas, mide su
    validez con scripts/kaggle_validez.py en modo --task-ids, en un notebook sin GPU. Se
    reemplaza la que no discrimine por la siguiente del orden. Me reportas solo el conteo.
2.2 Punto de partida. Corre A dos veces sobre las veinte. Entregas:
    - resueltas en cada corrida y cuántas tareas cambiaron de resultado entre las dos;
    - la tabla de fallos de las no resueltas, en conteos por clase: sin parche, tiempo
      agotado, llamadas agotadas, rechazo por contexto, herramienta no declarada, parche
      que no pasa las pruebas.
    El número de tareas que cambian entre dos corridas iguales es el ruido. Una mejora que
    no lo supere se lee como «sin diferencia».
2.3 Cada iteración, en este orden:
    a) Eliges la clase de fallo más numerosa de la tabla.
    b) Escribes en la bitácora, ANTES de correr: qué cambias, qué clase de fallo atacas y
       qué resultado te haría descartar el cambio.
    c) Corres las veinte tareas con ese único cambio.
    d) Conservas el cambio solo si las resueltas no bajan y la clase atacada baja más que
       el ruido. Si no, lo descartas y lo anotas igual. Un descarte también es un resultado.
2.4 Orden de las palancas, de la más barata a la más cara. No saltes a una posterior
    mientras la anterior tenga fallos por resolver:
    1. Fiabilidad: que ninguna tarea termine sin parche por una causa mecánica.
    2. Presupuesto: minutos, llamadas, turnos y tokens de razonamiento.
    3. Instrucciones del agente: reproducir, localizar, cambio mínimo, probar, entregar.
    4. Arquitectura: con o sin subagente; qué herramientas se declaran.
    5. Skills escritas a partir de las lecciones de la bitácora. Este es el bucle de ALL:
       corridas, lecciones, consolidación. Quedan como candidatas; probarlas contra el
       placebo es la campaña, que sigue sin empezar.
    6. Adaptadores LoRA: fuera de alcance hasta después del 2026-11-12.
2.5 Bitácora. Un solo archivo: experiments/gemma_developer_agent/mejora/bitacora.md.
    Una fila por corrida: fecha, SHA-256 del zip, el cambio, lo que se predijo, resueltas,
    tabla de fallos, horas de cuota, decisión (conservar o descartar) y la lección en una
    frase. Solo agregados.
2.6 Presupuesto de cuota. Como máximo 24 h por semana, y nunca dejes menos de 5 h sin usar
    al llegar el reinicio: la cuota que no se usa se pierde.

FASE 3 — LA TABLA DE KAGGLE (un envío al día)
3.1 Primero el ruido. Cuando el envío 56808559 tenga nota, reenvía el mismo zip dos días
    más, byte a byte y con el mismo nombre de archivo. Tres notas del mismo envío. Me
    muestras el comando y esperas mi aprobación cada vez.
3.2 Después, candidatos. Solo se envía un zip que se conservó en la Fase 2. La nota se lee
    en tareas, no en decimales: la tabla pública tiene 58 tareas y una vale 0,017.
3.3 No se elige ni se descarta un cambio por una sola nota de la tabla. La tabla confirma o
    contradice lo visto en desarrollo; si lo contradice, me lo dices antes de decidir.

LO QUE SIGUE DETENIDO
Figuras y tablas del artículo, recall y tablero, el agente zorzal, H8, el pre-registro de
la campaña, Docker en Windows y cualquier fusión a main. Los PR #129, #130, #132 y #133
quedan como están.

FECHAS
- 2026-10-10: reinicio de cuota. Para ese día, la Fase 1 terminada y la 2.2 corrida.
- 2026-10-26: con lo que haya en la bitácora, decido qué cuenta el artículo.
- 2026-11-12: cierre de la pista de artículo.
- 2026-12-02: envío final.

CÓMO ME INFORMAS
Al terminar cada punto numerado, tres líneas: qué hiciste, qué número salió, qué te
bloquea. Al cerrar cada sesión, una tabla con: cuota usada y restante, corridas hechas,
filas nuevas de la bitácora y decisiones que esperan mi respuesta. No declares nada
«listo» sin su evidencia.

EMPIEZA POR la Fase 0 y por el punto 1.1. No avances a la Fase 2 sin los cuatro números.
```

## Por qué está armado así

- **Dos fases de medición antes de mejorar.** Hoy no se puede correr el modelo; cualquier
  «mejora» anterior a eso es una conjetura.
- **Conjunto de desarrollo distinto del de prueba.** Las tareas de fastapi quedan intactas, así
  la mejora no contamina la prueba reservada. Es la separación entre validación y test.
- **Tabla de fallos antes que tasa de resueltas.** Con veinte tareas, la tasa de resueltas se
  mueve de a 5 puntos. Las clases de fallo mecánico cambian mucho más y permiten ver un efecto
  con pocas tareas.
- **Predicción antes de correr.** Es un pre-registro de una línea: impide justificar después
  cualquier resultado.
- **Ruido medido al inicio.** Dos corridas iguales dicen cuánto cambia el resultado solo por
  repetir; ese número es el umbral de todas las decisiones siguientes.
- **Las skills llegan en la quinta palanca.** Es donde el ciclo de ALL entra de verdad: las
  lecciones de la bitácora se consolidan en guías. Antes de eso hay fallos más baratos de quitar.
