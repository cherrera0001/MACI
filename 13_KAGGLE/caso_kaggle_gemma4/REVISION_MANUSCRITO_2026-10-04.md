# Revisión del manuscrito para la pista de artículo

> **Vigencia (2026-10-04, 21:33 UTC).** Documento fechado. Desde que se escribió hubo una corrida con el
> modelo, se midió la validez de las tareas y cambió el título del manuscrito. El estado vigente está en
> [`README.md`](README.md), sección 1.6, y en [`RECORRIDO_PASO_A_PASO.md`](RECORRIDO_PASO_A_PASO.md).

- **Archivo revisado:** `experiments/gemma_developer_agent/drafts/paper/manuscript_defendible_2026-10-04.md`
  (sin versionar, 2 353 palabras con tablas y referencias; el límite es 3 000).
- **Fecha:** 2026-10-04.
- **Contra qué se contrastó:** las tablas de `docs/paper/tables/`, los informes de
  `docs/results/`, el pre-registro de la línea base y los comentarios de #103 y #106.

## Veredicto

**Es defendible y no es competitivo.** Todo lo que afirma se sostiene en el repositorio, y el
texto no promete nada que no tenga. Pero la pista de artículo premia a tres trabajos por novedad,
generalidad y relevancia, y el manuscrito no contiene ningún resultado con Gemma 4: su único
dato medido es de un solver de tres operadores sobre nueve tareas de un proyecto.

## Nota estimada por criterio

Es mi estimación, sobre la escala de 0 a 5 de la página *Evaluation*. El jurado no publica la suya.

| Criterio | Estimación | Por qué |
|---|---|---|
| Novedad | 1 a 2 | El resultado del señuelo es casi una consecuencia del diseño; el diseño «ruido primero» combina prácticas conocidas y no se ejecutó |
| Calidad (generalidad) | 1 | El propio texto dice que no se puede generalizar |
| Relevancia | 1 a 2 | Sin resultado sobre el modelo ni sobre las tareas de la competencia |
| Verificabilidad | 4 a 5 | Tablas regenerables, pre-registro, enmiendas, desviaciones declaradas |
| Claridad | 4 | Bien escrito, honesto, estructura completa |
| **Promedio** | **2,2 a 2,8** | Insuficiente para estar entre los tres premiados |

## Lo que comprobé y está bien

- Las tablas 1 y 2 coinciden con las tablas regeneradas del repositorio.
- Los promedios de intentos (1,0 / 2,0 / 2,5) coinciden.
- El párrafo de lecciones de fallos coincide con el informe: cuatro umbrales, sin exposición en
  el más estricto, daño de 3 de 18 con el placebo en tres de ellos.
- La aritmética del pre-registro es correcta: 6 discordantes en un mismo sentido es el mínimo
  para p < 0,05 con McNemar exacto; 6/67 son 9 puntos y 6/48 son 12,5.
- Las diez referencias tienen el identificador de arXiv correcto.
- Cumple los requisitos formales: título, subtítulo, resumen, introducción, métodos y
  experimentos, trabajo relacionado con citas.

## Problemas de fondo

1. **El resultado principal es casi tautológico.** Una memoria que recupera por las palabras del
   enunciado, puesta frente a enunciados reescritos para nombrar el subsistema equivocado,
   recupera la lección equivocada. La tabla de atribución del repositorio lo muestra: cita la
   lección errónea en 12 de 12 casos. Un revisor leerá «0 de 18» como una propiedad del montaje,
   no como un hallazgo.
2. **Los conteos no son una muestra.** Son 18 corridas deterministas. El «6 de 18» de la
   condición sin memoria parece ser un tercio por construcción (tres operadores, seis
   permutaciones). El texto no lo explica y el lector lo tomará por una tasa empírica.
3. **«Grafo igual a historial» se presenta como resultado.** En un montaje tan pequeño puede
   significar que la prueba no distingue entre ambos, no que sean equivalentes.
4. **Dos tercios del artículo describen algo no ejecutado.** Las secciones 4 y 5 son un plan.
   Un plan pre-registrado es valioso con sus resultados; solo, es una propuesta.
5. **El título promete Gemma 4** y el texto no lo ejecuta. El subtítulo lo aclara, pero el
   desajuste resta.

## Problemas concretos, corregibles hoy

1. **Posible error de hecho en la sección 3.** Dice «6 órdenes deterministas de las tareas
   anteriores». El informe H4 dice «6 permutaciones del prior». Si lo que se permuta es la
   prioridad de los operadores y no el orden de las tareas, la frase es incorrecta. Verificar.
2. **Faltan las tres referencias que más importan**, y están en el README del experimento:
   - Bjarnason et al. (2026), sobre la variación entre corridas: es la justificación directa del
     diseño «ruido primero».
   - SkillsBench v1 (Li et al., 2026) y el estudio de AGENTS.md (Gloaguen et al., 2026): son la
     evidencia más cercana a la pregunta de la sección 5, y es mixta.
   - Dietterich (1998) para McNemar y Nosek et al. (2018) para el pre-registro.
   Sin ellas, la afirmación «ninguna obra citada incluye un control» es cierta solo porque se
   citaron las obras que no lo tienen.
3. **El umbral 6/24 aparece sin explicación** en las reglas de decisión.
4. **El párrafo de lecciones de fallos es ilegible sin tabla.** O se pone la tabla o se reduce a
   una frase.
5. **«Byte for byte»** en la sección 7: no lo volví a ejecutar; conviene comprobarlo antes de
   enviarlo.
6. **Riesgo de «no publicado».** Los resultados de la sección 3 ya están en un repositorio
   público. La pregunta sigue sin respuesta de los organizadores.

## Qué lo haría competitivo

No es redacción: son datos. En orden de valor por hora de cuota:

1. **La variación medida del kit.** Réplicas de A sobre un repositorio reservado, con tareas que
   cambian entre corridas. Convierte la sección 4 de plan en resultado y es útil para los 1 587
   equipos. Entra en el tema «Tasks & Benchmarks».
2. **Tres notas del mismo zip en la tabla.** Cuesta tres envíos y cero cuota. Mide el ruido sobre
   repositorios privados.
3. **La tabla de fallos del kit.** De qué mueren las tareas no resueltas: sin parche, tiempo,
   llamadas, contexto. Responde la predicción P2 y nadie la ha publicado.
4. **La validez de las 129 tareas**, medida con el guion propio.

Con los puntos 1 a 3, el artículo cambia de tesis: de «un resultado negativo de otro sistema y
un plan» a «cuánto ruido tiene el kit oficial de Gemma 4 y qué diferencia de la tabla se puede
creer». La sección 3 pasaría a ser un párrafo de motivación.

## Recomendación

Guardar este texto como plan B: es lo que se envía el 12 de noviembre si no hay nada más. No
invertir más horas en pulirlo. Las horas van a desbloquear el modelo y obtener los puntos 1 a 3;
el 26 de octubre se decide con los datos en la mano qué versión se escribe.
