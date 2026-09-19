# Sesión 1 — train / validation / test

**Fecha:** 2026-09-18
**Concepto:** `train_validation_test`
**Estado al cerrar:** `EN_ESTUDIO`

---

## Diagnóstico de entrada

No se hizo pregunta diagnóstica: el repositorio ya daba la evidencia. Cristóbal
había construido un split de tres vías temporal y lo tenía documentado en
`05_RESULTADOS/dashai_split_indices.json`. La clase partió desde ahí, no desde
la definición.

## Qué se enseñó

- Explicación intuitiva con la analogía del ensayo de práctica `[GUILLITO]`.
- Los tres conjuntos y qué se ajusta en cada uno, con el material de la
  asignatura `[FUENTE · NotebookLM: FCD-2026-2, Resumen_Clase6_Regresion.pdf]`.
- Por qué tres y no dos: contaminación por selección, sesgo estadístico y
  métrica optimista.
- Aplicación con sus propios números: 5.702 train + 634 validation (ambos 2016)
  y 7.244 test (todo 2017). La aritmética 5.702 + 634 = 6.336 muestra que el
  corte es temporal, no solo de tres vías.

## Pregunta de comprobación

Se le mostró su tabla real de MAE (CV en 2016 frente a test 2017):

| Modelo | CV 2016 | Test 2017 | Cambio |
|---|---|---|---|
| Baseline (mediana) | 449.160 | 431.649 | mejora 17.511 |
| Árbol de decisión | 219.821 | 246.568 | empeora 26.747 |
| HistGradientBoosting | 159.777 | 188.218 | empeora 28.441 |

**Pregunta:** ¿por qué el baseline mejora al pasar a 2017 mientras los modelos
empeoran, y por qué el mejor modelo es el que más empeora?

Datos entregados como apoyo: mediana 900.000 (2016) y 910.000 (2017); 29,1 % de
las propiedades de 2017 están en suburbios ausentes en 2016.

## Respuestas

**Intento 1:** *"entonces, podemos hablar de un sobreajuste"*

Etiqueta sin mecanismo. Además imprecisa en este contexto: el sobreajuste se
diagnostica comparando train contra validación, y ambas columnas de la tabla son
datos que el modelo nunca usó para entrenar.

**Intento 2:** *"el modelo fue entrenado con datos del 2016, pero un modelo que
deberías validar, o que debería probar es gradient boosting, o random forest"*

Dos cosas distintas en una frase:

- **Hilo correcto:** "el modelo fue entrenado con datos del 2016". Es
  exactamente el punto de partida de la respuesta.
- **Desvío:** propone probar Gradient Boosting o Random Forest. Ambos ya están
  en `resultados_temporal.json`, y HistGradientBoosting es una variante de
  gradient boosting. Está leyendo la tabla como ejercicio hipotético en vez de
  como los resultados de su propio proyecto.

## Errores registrados

1. `sobreajuste_como_etiqueta_de_toda_degradacion`
2. `no_reconoce_sus_propios_resultados`

Ambos en estado `abierto`, sin desmontaje confirmado todavía.

## Estado de la cadena de evidencia

```
EXPLICAR    ✗ pendiente
APLICAR     ✗ pendiente
TRANSFERIR  ✗ pendiente
```

Ninguna evidencia registrada. La pregunta sigue abierta: se le acotó el problema
al caso más simple (el baseline) en vez de entregarle la respuesta.

## Siguiente paso

Cerrar el razonamiento sobre el baseline. Si lo resuelve, la degradación de los
modelos flexibles se deduce sola. Después, verificar transferencia con un caso
de Galaxy Zoo o externo.

---

## Continuación de la sesión

**Intento 3:** *"pero hay sobre 170 barrios nuevos, y códigos postales"*

Cifra exacta: son **172** suburbios nuevos (142 en 2016, 313 en 2017), 2.109
filas, 29,1 %. Identificó el fenómeno correcto sin ayuda.

Mecanismo equivocado: supuso categorías desconocidas. Pero `Suburb` y
`Postcode` están excluidas del modelo. El mecanismo real es **extrapolación
geográfica** — 831/2.109 filas fuera del rango de latitud de 2016, 1.092/2.109
fuera del de longitud. Verificado en vivo sobre `housing_data.csv`.

## Corrección de Guillito sobre sí mismo

Se le mostró una tabla recortada a 3 filas de 12, ocultando Random Forest y
Gradient Boosting, y se le corrigió con un "ya los probaste" que no podía
verificar. Su desconfianza fue metodológicamente correcta. El registro
`no_reconoce_sus_propios_resultados` queda **anulado**: fue error del tutor.

## Preocupación sobre la evaluación del profesor

Planteó si el profesor había validado los datos, dado que el notebook está
guardado sin outputs. **Resuelto con evidencia:** la presentación entregada
(`Trabajo_N2_FUNDAMENTOS_(...).pptx`, lámina 6) contiene los resultados —
*"Mejor R² en test: Gradient Boosting = 0,719. Mejor MAE: 205.546 AUD"* — y la
lámina 3 documenta el diseño de validación temporal. Los resultados sí estaban
en el entregable.

## Estado al cerrar

```
EXPLICAR    ✓ parcial — fenómeno correcto, mecanismo incompleto
APLICAR     ✗ pendiente
TRANSFERIR  ✗ pendiente
```

Estado: `COMPRENSION_PARCIAL`.

## Siguiente paso

Ejercicio de APLICAR surgido de su propia pregunta: si añade `CouncilArea`
(18,9 % de nulos en 2017), dónde debe medir la mejora para no quemar el test.
Después, TRANSFERIR con un caso de otro dominio, no de Melbourne.
