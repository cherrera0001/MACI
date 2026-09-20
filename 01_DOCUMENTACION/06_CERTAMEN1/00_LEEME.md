# 06 · CERTAMEN 1 — Material de un compañero

> ## Advertencia de procedencia
>
> **Este documento no es de Cristóbal y sus respuestas no están verificadas.**
>
> Procede de un compañero de curso. Se titula *"Pauta Oficial de Corrección y
> Guía de Estudio"*, pero **cierra con dos campos de plantilla sin rellenar**:
>
> ```
> Documento revisado y validado por: Person
> Fecha de publicación de pauta: Date
> ```
>
> `Person` y `Date` son marcadores literales. Ninguna pauta publicada por un
> profesor saldría con los campos en blanco. Eso, sumado a la prosa uniforme y
> al formato de "Fundamento Teórico" repetido, indica una **reconstrucción con
> apariencia de pauta**, probablemente asistida por IA.

---

## Qué se puede usar y qué no

| Elemento | Fiabilidad | Uso permitido |
|---|---|---|
| **Enunciados de las preguntas** | **Alta** | Evidencia directa del formato y los temas que evalúa el profesor |
| **Tablas de datos** (calificaciones, consumo de camiones) | **Alta** | Son los datos reales del certamen; sirven como ejercicios |
| **Clasificación V/F** | Media | Plausible, pero sin verificar |
| **Justificaciones y "Fundamento Teórico"** | **Baja** | **No citar como pauta.** Contrastar contra el material del curso antes de darlo por válido |

**Regla para Guillito:** los enunciados entran como material de entrenamiento;
las respuestas **no** son criterio de corrección. Si una respuesta de este
documento contradice el material de la asignatura, manda el material de la
asignatura (`spec.md` §G5).

---

## Estructura del Certamen 1

11 preguntas. Formato y puntaje:

| # | Formato | Pts | Tema |
|---|---|---|---|
| 1 | V/F con justificación | 0,5 | Ciencia de datos como campo interdisciplinario |
| 2 | V/F con justificación | 0,5 | Organización *data-driven* frente a *data-informed* |
| 3 | V/F con justificación | 0,5 | Rol del líder de un proyecto de datos |
| 4 | V/F con justificación | 0,5 | Ciclo de vida iterativo y puesta en producción |
| 5 | Selección múltiple | 0,5 | Webscraping: alcance y límites frente a una API |
| 6 | Selección múltiple | 0,5 | Tipo de problema: clasificación multiclase supervisada |
| 7 | Selección múltiple | 0,5 | Reclutamiento de un data scientist |
| 8 | Selección múltiple | 0,5 | Big Data: las "V" |
| 9A | Desarrollo con tabla | — | Calidad y estructura de datos tabulares |
| 9B | Desarrollo con tabla | 2,0 | Caso minero: consumo de combustible |
| 10 | Retroalimentación | 0 | — |

---

## Qué aporta respecto al Certamen 2

Cubren **bloques distintos del curso**, y juntos lo mapean casi entero:

| | Certamen 1 | Certamen 2 |
|---|---|---|
| **Enfoque** | Fundamentos, adquisición y calidad de datos | Modelamiento y evaluación |
| **Temas** | Qué es la ciencia de datos, roles, ciclo de vida, webscraping, Big Data, tipos de problema, *tidy data* | Sobreajuste, validación, métricas, ROC, ensambles, LLM y agentes |
| **Peso del desarrollo** | Alto: la P9B vale 2,0 pts, más que las ocho primeras juntas | Medio |

**La pregunta de mayor puntaje de todo el Certamen 1 es la 9B**, un caso de
calidad de datos con una tabla real. Vale 2,0 puntos frente a 0,5 de cada
pregunta cerrada. Eso reordena la prioridad: `limpieza_preparacion` pesa mucho
más de lo que sugería el Certamen 2 por sí solo.

---

## Los dos casos de desarrollo

Son ejercicios reales y utilizables tal cual.

### 9A · Calificaciones

Tabla de 4 alumnos × 3 fechas, con las fechas **como encabezados de columna**.
Contiene `N/A` en texto mezclado con números y celdas vacías, y un identificador
(`Matrícula`) que pierde integridad al valer `N/A`.

Problemas a detectar: formato ancho frente a *tidy data*, inconsistencia de
tipos, clave primaria rota.

### 9B · Consumo de combustible en minería

Tabla de 16 filas donde la columna `CONSUMO` mezcla **días, IDs de camiones y
estados operativos** en el mismo campo. Incluye el centinela `-999` para
mantenimiento y un valor de `2900` frente a `200` del resto.

Problemas a detectar: sobrecarga semántica de una columna, códigos centinela que
sesgan cualquier estadístico, valor atípico, y filas usadas como separadores
jerárquicos.

**Ambos casos son entrenamiento de primera calidad** porque tienen los datos a
la vista y se resuelven en papel.

### La 9B no es una pregunta nueva

**[EVIDENCIA]** La 9B es una **variante del ejercicio de la lámina 27** de la
clase 4 (`11_PRESENTACIÓN/FCD-2026-2_04_CalidadDeDatos.pdf`), que plantea la
misma tabla de consumo de camiones con días como filas separadoras. La
**lámina 28 contiene la respuesta del propio profesor**:

| Su pregunta | Su respuesta |
|---|---|
| ¿Cuáles son las variables en este conjunto de datos? | Día, Camión, Consumo |
| ¿Qué objeto o evento estamos midiendo? | Consumo |

Y su tabla destino es `ID · Día · Camión · Consumo`. Cuatro columnas, sin tabla
de hechos ni de dimensiones.

Dos consecuencias para corregir la respuesta del compañero:

1. **El profesor conserva los ceros.** En su ejercicio hay consumos de 0 y no los
   borra ni los imputa. Un cero es una medición que resultó cero. El compañero
   **no menciona el `0` del conductor enfermo en ningún momento**, y esa es la
   distinción central de la pregunta frente al centinela `-999`.
2. **En su ejercicio conviven 3500 y 3600 con valores de 350, y no los llama
   errores.** El compañero afirma que el `2900` «sugiere un error de ingreso de
   datos o una falla de sensor»: eso es **[INFERENCIA]** presentada como
   hallazgo.

El método del profesor, repetido en las láminas 23 a 28, son dos preguntas:
*¿qué objeto o evento estamos midiendo?* y *¿cuáles son las variables?*. No usa
el vocabulario de *tidy data* ni de pandas.

---

## Lo que no sabemos

- Si el compañero obtuvo buena nota con esas respuestas.
- Si el profesor considera correcta cada justificación del documento.
- Si la próxima evaluación escrita seguirá el patrón del Certamen 1, el del 2,
  o una mezcla.

Nada de eso se puede inferir del archivo. Queda declarado como vacío, no
completado con algo plausible.
