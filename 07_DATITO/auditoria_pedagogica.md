# Auditoría de diseño instruccional — 2026-09-20

Primera auditoría de Datito con marco de **taxonomía de Bloom revisada**
(Anderson y Krathwohl) y **alineamiento constructivo** (Biggs).

No evalúa si el contenido técnico es correcto. Evalúa si el material **hace
aprender lo que la evaluación va a exigir**.

---

## Hallazgo principal: la distribución cognitiva está invertida

### Lo que exige el profesor

Clasificación de las 22 preguntas reales de los dos certámenes, por el **verbo**
y por lo que el estudiante tiene que hacer con la cabeza:

| Nivel | C1 | C2 | Formato que lo delata |
|---|---|---|---|
| **Evaluar** | 4 | ~4 | *"V/F con justificación"*, *"¿tiene razón?"*, declarar supuestos |
| **Analizar** | 4 | ~6 | *"¿cuál afirmación es incorrecta?"*, comparar curvas ROC |
| **Crear** | 2 | — | *"identifica los problemas y propón una solución"* (9A, 9B) |
| Aplicar | — | 1 | cálculo desde matriz de confusión |
| Comprender | 0 | 0 | — |
| Recordar | 0 | 0 | — |

**Nada por debajo de Aplicar.** El grueso está en Analizar y Evaluar.

Eso es coherente con la firma detectada en `patron_evaluacion.md`: las 11 fichas
del Certamen 2 comparten el campo *distinción conceptual clave*. Distinguir **es**
Analizar. Justificar la distinción **es** Evaluar.

### Lo que entrena el banco de preguntas diagnósticas

`curriculum.yaml`, campo `pregunta_diagnostico`, 21 conceptos:

```
Comprender    6      "explícame", "qué significa", "qué te dice"
Analizar      3
Evaluar       1
Aplicar       0
Crear         0
sin clasificar 11    redacción ambigua, no fuerza un nivel
```

**Está al revés que la evaluación.**

---

## Por qué importa

El principio de alineamiento constructivo: **el nivel cognitivo de la práctica
debe igualar al de la evaluación.**

Practicar por debajo del nivel exigido produce **falsa confianza**. El estudiante
responde bien en la práctica, se siente preparado, y falla en la prueba porque
pedía otra operación mental.

**Ya ocurrió, y está documentado.** Sesión 3, 2026-09-19: Cristóbal explicó el
mecanismo del sobreajuste correctamente —*"buenos resultados en entrenamiento,
pero con datos nuevos mucho error"*, que es **Comprender**— y acto seguido
asignó los tres diagnósticos a las filas equivocadas, que era **Aplicar**.

Explicar bien no predijo resolver bien. Es exactamente lo que el desalineamiento
anticipa.

---

## Lo que sí está alineado

| Material | Nivel dominante | Veredicto |
|---|---|---|
| `cuadernillos/01_…` | Evaluar y Analizar | **Bien alineado.** Tiene V/F con justificación, *"¿tiene razón tu compañero?"*, y los dos casos de calidad de datos que llegan a Crear |
| `visual/matriz_confusion.html` | Analizar | Los tres botones montan comparaciones, no definiciones |
| `visual/clase6_regresion.html` | Comprender y Aplicar | **Aceptable**: introduce un concepto nuevo, y ahí Comprender es el punto de partida correcto |
| Cadena de evidencia de `spec.md` | — | **Bien**: EXPLICAR→APLICAR→INTERPRETAR→TRANSFERIR cubre de Comprender a Analizar. Ver observación abajo |

No todo está mal. El problema está localizado en un archivo.

---

## Los tres cambios de mayor impacto

### 1 · Reescribir el banco de preguntas diagnósticas

Es el de mayor impacto porque `pregunta_diagnostico` es lo que decide **qué se
estudia y en qué orden**. Un diagnóstico que mide un nivel más bajo que el
certamen clasifica mal desde el primer día.

Patrón de conversión, sin cambiar el tema:

| Antes — Comprender | Después — Evaluar |
|---|---|
| *"¿Qué diferencia hay entre train, validation y test?"* | *"Un compañero dice: «usé validación cruzada sobre todo el conjunto y después reporté el error del mejor fold». ¿Es correcto? Justifica."* |
| *"¿Qué significa R² = 0,30?"* | *"Un informe concluye: «el modelo explica el 30 % de los casos». ¿Es correcta esa lectura? Corrígela si no."* |

La forma general: **poner una afirmación falsa o discutible en boca de alguien y
pedir juicio con justificación.** Es literalmente el formato del profesor.

### 2 · Añadir un nivel 4 a la escala de problemas

Los tres niveles actuales —Reconocimiento, Aplicación, Transferencia— mapean a
Aplicar y Analizar. **Falta Evaluar**, que es donde vive el grueso del certamen.

Propuesta: **nivel 2,5 · Juicio.** Entre aplicar y transferir. Una afirmación
plausible pero incorrecta sobre el concepto recién practicado, y hay que
detectarla y sostener por qué.

### 3 · Exigir justificación anclada en cifra

Observación de la sesión 3: ante *"¿tiene razón tu compañero?"*, Cristóbal
respondió *"B memoriza pero generaliza peor"* — correcto, pero **sin el número**.

En Evaluar, un juicio sin criterio explícito no puntúa completo. El criterio
aquí era `A 0,59 · B 0,54`.

Debe quedar como regla: **toda respuesta de nivel Evaluar cita el dato que la
sostiene**, o no se acredita.

---

## Observación sobre la cadena de evidencia

`EXPLICAR → APLICAR → INTERPRETAR → TRANSFERIR` es sólida, pero conviene ser
explícito en que **INTERPRETAR es donde vive Evaluar**.

Hoy la definición dice *"lee resultados reales y dice qué significan y qué no"*.
Eso es Analizar. Para cubrir Evaluar debería exigir además **emitir un juicio con
criterio explícito**: decidir, recomendar, o refutar una afirmación.

---

## Lo que esta auditoría no revisó

- Si las afirmaciones técnicas del material son correctas. No es su campo: eso
  lo verifica Datito.
- Los artefactos de `visual/` con criterio de carga cognitiva y recuperación
  activa en detalle. Queda para una segunda pasada.
- El material de `08_PRACTICA/`, que es del profesor y no de Datito.
