# Auditoría de artefactos con el modelo nuevo

**2026-09-20** · Ocho artefactos evaluados contra las siete preguntas de
razonamiento, las ocho dimensiones de comprensión y el patrón de interacción.

Ningún HTML fue modificado. Esto es el diagnóstico.

---

## Medición

```
artefacto                  KB  slid  pred  ecua  inv  grafo
---------------------------------------------------------
certamen_1                 22     0     0     0    0      0
certamen_2                 24     0     4     3    0      1
clase6_regresion           14     2     1    14    0      0
generalizacion             15     1     0     3    0      0
matriz_confusion           13     4     0     4    0      1
regresion_y_costo          11     2     0    10    0      0
train_validation_test      13     0     1     0    0      1
triaje_de_problemas        17     0     4     0    0      1
```

`slid` controles · `pred` invitaciones a predecir · `ecua` símbolos formales ·
`inv` camino inverso · `grafo` conexión con prerrequisitos y dependientes

---

## Hallazgo sistemático: el camino inverso no existe

**Cero de ocho.** Ningún artefacto parte de una ecuación para reconstruir el
fenómeno. Todos recorren realidad → intuición → visual → números → notación, y
ninguno el sentido contrario.

Eso importa porque **en una prueba escrita la ecuación llega primero**. Le van a
poner `R² = 1 − SSres/SStot` en el papel y tendrá que saber qué compara.

No es un defecto de un artefacto: es un defecto del molde con que los construí.

## Segundo hallazgo: nueve controles, ninguna predicción

Los cuatro sliders de `matriz_confusion` mueven pacientes, prevalencia,
sensibilidad y especificidad —cuatro relaciones causales nítidas, exactamente
el caso donde predecir rinde— y **no hay una sola pregunta previa**.

Es el artefacto que más lo necesita y el que menos lo tiene.

## Tercer hallazgo: duplicación no declarada

`clase6_regresion` y `regresion_y_costo` cubren el mismo terreno —recta, coste,
R²— con sliders equivalentes. No es necesariamente malo, pero **ninguno declara
la relación con el otro**, y el alumno no sabe cuál abrir.

---

## Artefacto por artefacto

### `matriz_confusion.html` — **prioridad 1**

| Pregunta de razonamiento | Estado |
|---|---|
| Objetivo | Claro: distinguir métricas por su denominador |
| Representación faltante | **La ecuación desarmada.** Las fórmulas están como etiquetas de texto, nunca como objeto de estudio |
| Relación a hacer visible | Lograda: el efecto del desbalance sobre la exactitud |
| Interacción útil | Cuatro sliders bien elegidos, **sin predicción** |
| Matemática asociada | **Subservida.** Un artefacto sobre cinco cocientes con 4 símbolos formales |
| Conexión con el grafo | Ausente |
| Evidencia de comprensión | **Ninguna.** No pide producir nada |

Es el de mayor `prioridad_evaluacion` —27 % del Certamen 2— y el de peor
cobertura de dimensiones.

**Cambios propuestos**
1. Predicción antes de cada slider. *«Si la enfermedad se vuelve más rara y el
   modelo no cambia, ¿qué le pasa a la precisión?»* — la respuesta es
   contraintuitiva y por eso enseña
2. Desarmar las cinco fórmulas: qué es dato, qué se cuenta, qué se decide
3. Camino inverso: dar `FPR = FP/(FP+TN)` y pedir reconstruir qué universo es el
   denominador y por qué **no** es `1 − precisión`
4. Situar en el grafo: viene de `clasificacion`, habilita `roc_auc`

### `generalizacion.html` — prioridad 2

| Pregunta | Estado |
|---|---|
| Objetivo | Claro y bien acotado |
| Representación faltante | La ecuación de la brecha; el camino inverso |
| Relación a hacer visible | **Muy lograda**: la zona sin datos y la recta punteada |
| Interacción útil | Un slider, sin predicción |
| Matemática | Escasa: 3 símbolos |
| Grafo | Ausente |
| Evidencia | Hay pregunta abierta al final — **bien** |

**Cambios**: predicción antes del slider de radio; declarar que viene de
`train_validation_test` y habilita todo el bloque de validación.

### `regresion_y_costo.html` + `clase6_regresion.html` — prioridad 3

Buena cobertura matemática —10 y 14 símbolos— y la mejor interacción del
conjunto. Les falta predicción, camino inverso y, sobre todo, **declarar su
relación mutua**.

**Cambio propuesto**: diferenciarlos explícitamente.
- `clase6_regresion` = la clase completa, punto de entrada
- `regresion_y_costo` = el laboratorio de la función de coste

Y una nota cruzada en cada uno.

### `train_validation_test.html` — prioridad 4

Sin sliders, y **está bien**: su valor está en la visualización de los cuatro
métodos de validación, que se entiende mirándola. No todo concepto necesita una
perilla, y forzar una aquí sería interacción por interacción.

**Cambio**: es el artefacto de un concepto con `importancia_curricular` 11. Debe
decirlo. Y la validación cruzada, que está dentro, tiene tensión declarada —
poco preguntada, fundacional — y el artefacto no la menciona.

### `triaje_de_problemas.html` — sin cambios de fondo

Cumple su función y no necesita ecuaciones: es un árbol de decisión sobre tipos
de problema. Forzarle matemática sería cumplir una lista.

**Único cambio**: enlazar cada desenlace con el artefacto del concepto
correspondiente.

### `certamen_1.html` y `certamen_2.html` — sin cambios de fondo

Función distinta: entrenar formato y distinción, no explicar conceptos. La
ausencia de sliders y ecuaciones es coherente con eso.

**Cambio menor**: enlazar cada pregunta con el artefacto del concepto que
evalúa, para poder saltar del problema a la explicación.

---

## Cobertura de dimensiones, en conjunto

| Dimensión | Cobertura |
|---|---|
| `intuicion` | **Buena** — analogías y casos reales en todos |
| `visual` | **Buena** — es el punto fuerte del conjunto |
| `matematica` | **Débil** — presente en dos, subservida en el que más la necesita |
| `calculo` | Parcial — hay ejemplos numéricos, falta pedirle que calcule |
| `interpretacion` | Buena — casi todos traducen el resultado al problema |
| `aplicacion` | Buena — las cifras de Melbourne y Galaxy Zoo |
| `transferencia` | **Débil** — solo el dataset de logística la ejercita |
| `explicacion` | **Ausente** — ningún artefacto le pide explicar algo |

Las dos ausencias reales son **matemática** y **explicación**. La primera venía
de la hipótesis equivocada. La segunda no la había considerado.

---

## Plan, por impacto

| # | Acción | Artefactos | Coste |
|---|---|---|---|
| 1 | Predicción en los controles que representan una relación causal | matriz_confusion, generalizacion, regresion_y_costo | Medio |
| 2 | Camino inverso: partir de la ecuación | matriz_confusion, clase6_regresion | Medio |
| 3 | Desarmar las fórmulas de clasificación | matriz_confusion | Medio |
| 4 | Situar cada concepto en el grafo | los 6 conceptuales | Bajo |
| 5 | Enlaces cruzados entre artefactos | los 8 | Bajo |
| 6 | Pedirle producir algo, no solo leer | los 6 conceptuales | Bajo |

El 1 y el 3 caen sobre el mismo archivo, que además es el de mayor peso en la
evaluación. **Empezar por `matriz_confusion.html`** cubre tres de las seis
acciones sobre el artefacto que más lo necesita.

---

## Lo que esta auditoría no hace

No propone rehacer nada desde cero. Los ocho artefactos tienen la parte difícil
resuelta —el caso concreto, la visualización, las cifras verificables— y lo que
falta se añade encima.

Tampoco propone forzar interacción ni matemática donde no aportan. El triaje y
los certámenes están bien como están.

---

# Cierre del plan

**2026-09-20, misma fecha · añadido después de ejecutar las seis acciones**

Lo de arriba es el diagnóstico y se deja intacto. Esto es qué se hizo con él.

## Medición después

```
artefacto                  KB  slid  pred  inv  grafo  href
-----------------------------------------------------------
certamen_1                 24     0     0    0      0     5
certamen_2                 26     0     0    0      0     8
clase6_regresion           23     3     1    1      1     1
generalizacion             25     2     1    1      1     3
matriz_confusion           32     5     4    1      2     3
regresion_y_costo          19     3     1    1      1     1
train_validation_test      17     0     0    0      1     2
triaje_de_problemas        18     0     0    0      0     1
```

`href` es la columna nueva: enlaces a otros artefactos, que antes no existían.
En `triaje_de_problemas` el 1 es literal —los enlaces de sus ocho desenlaces se
generan en JavaScript desde una sola plantilla.

**[EVIDENCIA]** El hallazgo sistemático quedó corregido donde correspondía: el
camino inverso pasó de **0 de 8** a estar en los cuatro artefactos con contenido
matemático. Los otros cuatro no lo llevan, y es deliberado —dos son certámenes y
uno es un árbol de decisión.

## Las seis acciones

| # | Acción | Estado |
|---|---|---|
| 1 | Predicción en controles causales | **Hecha** — matriz_confusion (4), generalizacion, clase6_regresion, regresion_y_costo |
| 2 | Camino inverso desde la ecuación | **Hecha** — los 4 con matemática |
| 3 | Desarmar las fórmulas de clasificación | **Hecha** — matriz_confusion, con etiquetas de rol |
| 4 | Situar cada concepto en el grafo | **Hecha** — los 6 conceptuales |
| 5 | Enlaces cruzados entre artefactos | **Hecha** — los 8, sin enlaces rotos |
| 6 | Pedirle producir algo | **Hecha** — los 6 conceptuales |

## Lo que se decidió no hacer, y por qué

**[INFERENCIA]** Tres omisiones son deliberadas, no deuda pendiente:

- **Sin sliders en `train_validation_test`.** Su valor está en la visualización
  de los cuatro métodos de validación, que se entiende mirándola. Una perilla
  aquí sería interacción por interacción.
- **Sin ecuaciones en `triaje_de_problemas`.** Es un árbol de decisión sobre
  tipos de problema. Forzarle matemática sería cumplir una lista.
- **Sin bloque de grafo en los dos certámenes.** Su función es entrenar formato
  y distinción, no explicar conceptos. Sí llevan enlaces, que era lo que les
  faltaba de verdad.

## Lo que sigue abierto

**[NO EVIDENCIADO]** Tres conceptos que aparecen como desenlace del triaje no
tienen artefacto propio: **segmentación (no supervisado)**, **EDA** y **calidad
y limpieza de datos**. Los dos últimos pesan en el Certamen 1 —la 9B, de 2,0
puntos, es de limpieza— y hoy solo se cubren enlazando al certamen resuelto.
Es la brecha más clara del conjunto.

**[NO EVIDENCIADO]** La dimensión `transferencia` seguía marcada como débil en
el diagnóstico y ninguna de las seis acciones la atacaba de frente. Sigue
sostenida por un solo dataset, el de logística.
