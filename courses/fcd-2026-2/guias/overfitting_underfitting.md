# Guía · Sobreajuste y subajuste

Material de estudio para prueba escrita sin Internet.
Fundamentos de Ciencia de Datos, UdeC T2-2026.

**Por qué esta guía existe:** sobreajuste y validación concentran el **36 %** del
Certamen 2 (preguntas 1, 2, 3 y 7). Es el bloque de mayor peso del curso.

**Versión interactiva:** `07_DATITO/visual/overfitting_underfitting.html`.

---

## 1 · Las dos preguntas que hay que responder, en orden

Ante una tabla de resultados, **no diagnostiques mirando valores sueltos.**
Hay dos criterios y actúan en secuencia:

```
1. LA BRECHA    ¿cuánto empeora al pasar de entrenamiento a prueba?
                → aísla el SOBREAJUSTE

2. EL NIVEL     ¿son aceptables los valores, en ambos conjuntos?
                → separa SUBAJUSTE de AJUSTE CORRECTO
```

La brecha sola no basta. Subajuste y ajuste correcto tienen **los dos** una
brecha pequeña: lo que los distingue es si el modelo sirve para algo.

| Brecha | Nivel | Diagnóstico |
|---|---|---|
| Grande | Bueno dentro, malo fuera | **Sobreajuste** |
| Pequeña | Malo en ambos | **Subajuste** |
| Pequeña | Aceptable en ambos | **Ajuste correcto** |

---

## 2 · Cuidado con la métrica: no todas apuntan al mismo lado

Éste es el error que más barato sale de evitar y más caro de cometer.

| Métrica | Rango | Mejor es |
|---|---|---|
| **R²** | ≤ 1 | **más alto** |
| **MAE** | ≥ 0 | **más bajo** |
| **RMSE** | ≥ 0 | **más bajo** |
| **Accuracy, Precision, Recall, F1, AUC** | 0 a 1 | **más alto** |

Si aplicas de memoria *"brecha = entrenamiento − prueba"* con MAE, te sale
negativa y el diagnóstico invertido.

**Regla:** antes de restar, pregúntate qué significa el número. La brecha es
siempre *"cuánto empeora al salir del entrenamiento"*, no una resta fija.

### Ejemplo del giro

```
Con R²    0,98 → 0,54     empeora (cae 0,44)     sobreajuste
Con MAE   0,15 → 0,92     empeora (sube 0,77)    sobreajuste
```

Mismo fenómeno, la resta va en sentido contrario.

---

## 3 · Los remedios, y por qué mecanismo actúa cada uno

El profesor **no pregunta el nombre del remedio. Pregunta el mecanismo.** La
distinción entre bajar el grado de un polinomio —que *elimina* términos— y
regularizar —que los *amortigua*— **no viene del profesor**: ni sus clases ni el
enunciado de la P7 la mencionan. Proviene de la reconstrucción del certamen hecha
por el alumno (`01_DOCUMENTACION/01_CERTAMEN2/01_ANALISIS_RECONSTRUCCION_CERTAMEN.md`,
l.456 y l.497). **[INFERENCIA]** útil para un oral, no materia de clase.

### Para el sobreajuste

| Remedio | Mecanismo | ¿Depende del algoritmo? |
|---|---|---|
| **Más datos de entrenamiento** | Más evidencia por parámetro: el ruido deja de ser ajustable | **No** |
| **Reducir features** | Menos oportunidades de encontrar patrones espurios | **No** |
| **Validación cruzada** | No reduce el sobreajuste: lo **detecta** antes de decidir | **No** |
| **Regularizar (L1/L2)** | Penaliza coeficientes grandes y los encoge hacia cero, sin eliminarlos → **amortigua** | **Sí** — necesita coeficientes |
| **Podar el árbol / limitar profundidad** | Corta ramas: quita capacidad del modelo → **elimina** | **Sí** — necesita ser un árbol |
| **Simplificar el modelo** | Menos parámetros, menos capacidad de memorizar | **Sí** |

### Para el subajuste

| Remedio | Mecanismo | ¿Depende del algoritmo? |
|---|---|---|
| **Modelo más flexible** | El modelo actual no tiene capacidad para la relación real | **Sí** |
| **Feature engineering** | Las variables actuales no contienen la señal necesaria | **No** |
| **Permitir relaciones no lineales** | Si la relación real es curva, un modelo lineal nunca la alcanza | **Sí** |
| **Reducir la regularización** | Si se penalizó demasiado, el modelo quedó rígido de más | **Sí** |

**Más datos NO cura el subajuste.** Si el modelo no tiene capacidad, darle más
filas solo confirma lo que ya no podía aprender.

---

## 4 · La distinción que más se cae en el papel: filas frente a columnas

Es la P3 del Certamen 2.

```
MÁS FILAS     (más observaciones)   →  REDUCE el sobreajuste
MÁS COLUMNAS  (más variables)       →  lo AUMENTA, si no traen señal
```

Ambas cosas son "más datos" en lenguaje coloquial y tienen efectos opuestos.
Más filas dan más evidencia por parámetro. Más columnas dan más parámetros que
ajustar con la misma evidencia.

---

## 5 · Cuando no te dicen qué algoritmo es

Situación frecuente en el certamen, y hay que responderla en dos partes.

### ¿Afecta al diagnóstico? **No**

Sobreajuste y subajuste son propiedades del **comportamiento empírico** del
modelo, no de la familia del algoritmo. Una brecha grande es una brecha grande
sea una regresión lineal, un árbol, un ensamble o una red neuronal. Se
diagnostican comparando métricas entre entrenamiento y prueba, y nada más.

### ¿Afecta a los remedios? **Sí, a algunos**

- **Los remedios a nivel de datos siguen disponibles:** más filas, selección de
  features, validación cruzada. No necesitas saber qué algoritmo es.
- **Los remedios a nivel de modelo, no:** no puedes proponer regularización L1/L2
  sin saber si hay coeficientes que penalizar; ni poda sin saber si hay un árbol;
  ni más capas sin saber si hay una red.

### Qué escribir en el papel

Dos salidas válidas, y ambas puntúan:

1. **Declarar el supuesto:** *"Si se trata de un modelo de árbol, podarlo…"*
2. **Limitarse a remedios agnósticos:** más datos, selección de features

Lo que **no** puntúa es proponer poda sin que nadie haya dicho que es un árbol.
Eso es la P11 del Certamen 2: separar lo medido de lo supuesto.

---

## 6 · Qué modelo llevar a producción

La pregunta parece obvia y tiene una trampa: **el criterio es el error en datos
no vistos, no el de entrenamiento.**

Orden de razonamiento:

1. **Comparar el desempeño en prueba.** Es lo único que estima el mundo real.
2. **Mirar la brecha como control de estabilidad.** Un modelo con brecha enorme
   es frágil: su buen número de entrenamiento no significa nada.
3. **Traducir el error a la unidad del problema.** Un MAE de 0,78 horas son
   ~47 minutos de error promedio. Eso es lo que entiende quien decide.

Un modelo puede tener mejor entrenamiento y peor producción. Es el caso normal
del sobreajuste, y es justo lo que pregunta el certamen.

---

## 7 · Ejemplos resueltos

### Caso 1 · Métrica R² (más alto es mejor)

| Modelo | R² entren. | R² prueba | Brecha | Diagnóstico |
|---|---|---|---|---|
| A | 0,62 | 0,59 | **0,03** | Ajuste correcto |
| B | 0,98 | 0,54 | **0,44** | **Sobreajuste** |
| C | 0,41 | 0,39 | **0,02** | **Subajuste** |

A y C tienen casi la misma brecha. Lo que los separa es el **nivel**: C es malo
en ambos conjuntos.

> *"B aprende mucho mejor los datos, descartemos A."*
> **Falso.** B memoriza pero generaliza peor: sobre datos no vistos, A obtiene
> 0,59 y B solo 0,54. Aprender los datos ≠ ser mejor modelo.

### Caso 2 · Métrica MAE (más bajo es mejor)

| Modelo | MAE entren. | MAE prueba | Cambio | Diagnóstico |
|---|---|---|---|---|
| P | 0,15 | 0,92 | **+0,77** | **Sobreajuste** |
| Q | 0,71 | 0,78 | **+0,07** | Ajuste correcto |
| R | 1,84 | 1,90 | **+0,06** | **Subajuste** |

**A producción: Q.** Menor error sobre datos nuevos (0,78 h ≈ 47 min, frente a
0,92 h ≈ 55 min de P y 1,90 h de R) y brecha pequeña, o sea estable.

P parece excelente con 0,15 en entrenamiento. Esa cifra no sirve para decidir.

---

## 8 · Tu propio proyecto como caso real

`05_RESULTADOS/resultados_temporal.json`, modelos sobre `log1p(Price)`:

| Modelo | R² train 2016 | R² test 2017 | Brecha |
|---|---|---|---|
| Árbol de decisión | 0,7523 | 0,6123 | 0,1400 |
| **Random Forest** | **0,9423** | 0,7109 | **0,2314** |
| Gradient Boosting | 0,8858 | 0,7466 | 0,1392 |
| HistGradientBoosting | 0,9274 | 0,7571 | 0,1703 |

Random Forest tiene la mayor brecha: 0,94 dentro y 0,71 fuera. Sobreajusta más
que Gradient Boosting, que con **menos** R² de entrenamiento consigue **más** en
prueba.

Es exactamente el patrón del Caso 1, medido en tu propio trabajo.

---

## 9 · Errores que el formato castiga

- Diagnosticar mirando **un solo número** en vez de la brecha
- Confundir **más filas** con **más columnas**
- Aplicar la resta de memoria sin mirar **si la métrica sube o baja**
- Proponer un remedio específico **sin declarar el supuesto** del algoritmo
- Elegir el modelo de producción por su **error de entrenamiento**
- Creer que **más datos** cura el subajuste
- Decir "sobreajuste" **sin nombrar el mecanismo**

---

## 10 · Procedimiento para el papel

```
1. Identificar la métrica y si más alto es mejor o peor
2. Calcular la brecha de cada modelo
3. ¿Brecha grande?        → sobreajuste
4. ¿Brecha pequeña?       → mirar el nivel
      malo en ambos       → subajuste
      aceptable en ambos  → ajuste correcto
5. Nombrar el MECANISMO, no solo la etiqueta
6. Remedios: decir POR QUÉ actúa cada uno
      ¿sé qué algoritmo es?  → puedo proponer específicos
      ¿no lo sé?             → declaro el supuesto o uso agnósticos
7. ¿Producción? → decidir por el error en datos no vistos
```

Cabe en una tarjeta. Apréndete la secuencia, no las definiciones.
