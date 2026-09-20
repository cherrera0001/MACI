# Sesión 3 — overfitting / underfitting

**Fecha:** 2026-09-19
**Modo:** entrenamiento de resolución de problemas (nuevo)
**Estado al cerrar:** `COMPRENSION_PARCIAL`

---

## Cambio de misión

Se detuvo la expansión hacia Ñuble, OSINT y CouncilArea. La prioridad pasa a
preparar una **evaluación escrita sin Internet**, y el criterio de avance deja
de ser cuánto contenido se explicó para pasar a **cuántos problemas resuelve
solo**.

Se reconstruyó el patrón real del profesor en
[`../patron_evaluacion.md`](../patron_evaluacion.md).

---

## Problema 1 — Nivel 1

Tres modelos con R² de entrenamiento y prueba: A 0,62/0,59 · B 0,98/0,54 ·
C 0,41/0,39.

### a) Diagnóstico

**Primer intento — incorrecto.** *"A sobreajusta, B subajusta, C está bien"*.
Los tres asignados a la fila equivocada.

Pero la explicación del mecanismo fue **correcta**: *"buenos resultados en
entrenamiento, pero con datos nuevos mucho error a diferencia con lo conocido"*.
Avance real frente a la sesión 1, donde solo usó la etiqueta "sobreajuste" sin
mecanismo.

**Diagnóstico del fallo:** no es incomprensión del concepto, es haberse saltado
el paso 2 del procedimiento — calcular la brecha. Se corrigió exigiendo el paso,
no reexplicando el concepto.

**Segundo intento — correcto.** Calculó las tres brechas (0,03 · 0,44 · 0,02) y
reasignó: B sobreajusta, C subajusta *"porque ambos valores son bajos"*, A está
bien. Aplicó los dos criterios en el orden correcto: brecha para aislar el
sobreajuste, nivel para separar subajuste de ajuste correcto.

### b) Correcta

*"Mi compañero no tiene razón, B memoriza pero generaliza peor que el modelo A."*

Captura la distinción evaluada: *aprender los datos* ≠ *ser mejor modelo*.
Observación de técnica: no ancló la afirmación con la cifra (A 0,59 · B 0,54).
En una prueba escrita el número es lo que convierte una opinión en justificación.

### c) Correcta

Regularizar (amortigua los coeficientes) y podar el árbol (elimina capacidad).
Dos mecanismos genuinamente distintos — es la distinción de la P7 del Certamen 2.

**Observación importante:** dijo "podar el árbol", pero el enunciado nunca
declaró que B fuera un árbol. Supuesto no declarado. Es exactamente el patrón
que evalúa la P11 del Certamen 2: separar lo medido de lo supuesto.

---

## Problema 2 — Nivel 2 (incompleto)

Tres modelos de tiempo de entrega, métrica **MAE**: P 0,15/0,92 · Q 0,71/0,78 ·
R 1,84/1,90.

La trampa: con MAE **menos es mejor**, al revés que R². Aplicar la regla de
memoria daría el diagnóstico invertido.

### a) Correcta, sin ayuda

P sobreajusta, Q está bien, R subajusta. Leyó qué significaba el número antes de
restar, que era justo lo que el problema ponía a prueba.

**b) y c) quedaron sin responder.** Sesión cerrada por hora.

---

## Errores registrados

`diagnostica_sin_calcular_la_brecha` — marcado explícitamente como fallo de
**procedimiento**, no de concepto. La nota advierte a Guillito que no lo trate
como incomprensión: se corrige exigiendo el paso, no reexplicando.

---

## Estado de la cadena

```
EXPLICAR    ✓  mecanismo descrito con sus palabras, sin ayuda
APLICAR     ✗  falta completar un nivel 2 entero sin andamiaje
TRANSFERIR  ✗  pendiente
```

---

## Siguiente sesión

Cristóbal propuso un formato distinto: **un certamen completo generado por
Guillito**, que pueda leer y digerir entero en vez de ir pregunta a pregunta.

Es compatible con el plan: la simulación de certamen ya estaba prevista, pero
condicionada a tener suficientes conceptos en "puedo resolver solo". Conviene
acordar si se quiere:

- una **simulación completa** con corrección al final, o
- un **cuadernillo de estudio** con problemas resueltos para leer antes de
  practicar

No es lo mismo: la primera mide, el segundo enseña.

Pendiente inmediato: cerrar b) y c) del Problema 2 para acreditar `APLICAR`.
