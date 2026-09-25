# 04 · DATOS

Datasets de los dos proyectos del semestre.

| Archivo | Proyecto | Filas × columnas |
|---|---|---|
| `housing_dashai_2016_2017.csv` | Melbourne — regresión | preprocesado para DashAI |
| `GZ_mini_challenge_train.csv` | Galaxy Zoo — clasificación | 1.000 × 90 |
| `GZ_mini_challenge_test.csv` | Galaxy Zoo — clasificación | 10.000 × 86 |

> **Nota sobre duplicados.** Los dos archivos `GZ_*` son **byte a byte
> idénticos** a los de `02_PROYECTO_FCD/Desafio/`. Se conservan ambas copias:
> aquí como dato canónico del repositorio, allá junto al código que los usa.
> Verificado con SHA-256.

---

## Galaxy Zoo · el dataset de clasificación

Clasificación multiclase de galaxias del sondeo SDSS. **Métrica oficial del
desafío: F1-macro.**

### El target: `label`

| Clase | Qué es | Filas | % |
|---|---|---|---|
| **0** | No decidible · votación ambigua | 96 | **9,6 %** |
| **1** | Espiral | 227 | 22,7 % |
| **2** | Elíptica | 677 | **67,7 %** |

**Desbalance de 7,1×** entre la clase mayoritaria y la minoritaria.

Ese número explica por sí solo la elección de métrica: un modelo que responda
siempre «elíptica» acierta el **67,7 %** de las veces sin haber aprendido nada.
La exactitud lo premiaría; el F1-macro no, porque promedia las tres clases y una
clase rara pesa igual que una frecuente.

### Cuatro columnas que están en train y NO en test

```
label · objID · p_el · p_cs
```

`label` es el target, y `objID` un identificador. Pero **`p_el` y `p_cs` son un
caso de estudio**: son las fracciones de voto de los clasificadores humanos de
Galaxy Zoo, y están claramente asociadas a la clase.

| Clase | `p_el` medio | `p_cs` medio |
|---|---|---|
| 0 · ambigua | 0,356 | 0,271 |
| 1 · espiral | 0,212 | **0,739** |
| 2 · elíptica | **0,735** | 0,139 |

Son informativas — y **no se pueden usar**. No por fuga de información en el
sentido clásico, sino por algo más simple y más frecuente en la práctica:

> **No existen en el momento de predecir.** Un modelo entrenado con ellas no
> podría ejecutarse sobre el test, porque esas columnas no están ahí.

Es exactamente el mismo problema que `costo_combustible_clp` en el dataset
sintético de transferencia — pero aquí es **real y está en tus propios datos**.

### Por qué la clase 0 es la difícil

Mira sus dos medias: `p_el` 0,356 y `p_cs` 0,271. **Ninguna domina.**

La clase 0 no es «otro tipo de galaxia»: es *«los humanos no se pusieron de
acuerdo»*. Un modelo que intente separarla tiene que aprender a reconocer
**ausencia de consenso**, que es una señal mucho más débil que la forma de una
galaxia.

Eso, más el 9,6 % de representación, la convierte en la clase que hunde el
F1-macro. El análisis de la clase 0 tiene su propia sección en
`02_PROYECTO_FCD/Desafio/REPORT.md`.

### Lo demás

- **86 features numéricas** utilizables, descontando target y auxiliares
- **Cero nulos** en ambos conjuntos
- El test tiene **diez veces más filas** que el train: 10.000 frente a 1.000.
  Poco habitual, y obliga a que el modelo generalice con poca evidencia

---

## Melbourne · el dataset de regresión

`housing_dashai_2016_2017.csv` — versión preprocesada y subida a DashAI.

El original con todas las columnas está en
`02_PROYECTO_FCD/Hito1/Corrección/Trabajo N°1 _ FINAL/…/housing_data.csv`.

Cifras verificadas en `05_RESULTADOS/resultados_temporal.json`: 6.336
propiedades de 2016 para entrenar, 7.244 de 2017 para evaluar, y **29,1 % del
test en suburbios que no existen en el train**.
