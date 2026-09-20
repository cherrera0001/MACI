# 08 · PRÁCTICA — Laboratorios de la asignatura

Los cinco prácticos de Fundamentos de Ciencia de Datos (UdeC, T2-2026), cada uno
en dos versiones:

| Versión | Qué es | Para qué sirve |
|---|---|---|
| `(res)` | Resuelta, con salidas ejecutadas | Material de consulta y referencia |
| `(vacio)` | Enunciados sin resolver | **Ejercicios reales** para practicar |

La distinción importa: los `(vacio)` son la fuente de ejercicios con solución
conocida pero no visible. Guillito los usa como evidencia de **APLICAR**, porque
resolver uno sin mirar el `(res)` es una prueba genuina de comprensión.

---

## Contenido por práctico

### P1 · Laboratorio Pandas — 133 celdas

Series y DataFrames, crear y recorrer tablas, acceso y modificación de
filas/columnas, cargar y guardar, **combinar tablas** (tipos de `merge`),
describir, filtrar, operaciones, ordenar y `groupby`.

**10 ejercicios** en dos bloques (1.1–1.4 y 2.1–2.6).

→ Conceptos: `datos_features_target`, `eda`

### P2 · Calidad de Datos — 119 celdas

Duplicados (de filas y de índices), valores fuera de rango, valores faltantes
—reemplazar frente a eliminar—, datos no útiles, inconsistencias, y columnas con
tipo de dato incorrecto.

→ Concepto: `limpieza_preparacion`

### P3 · Numpy + Análisis Descriptivo — 125 celdas

Arreglos de Numpy: definición, operaciones, acceso, conversión desde
DataFrame/Serie. Análisis descriptivo: **centralidad**, **extensión**,
`describe`. Visualización con Matplotlib.

→ Concepto: `eda`

### P4 · Regresión — 113 celdas

Regresión lineal y construcción manual de la función a partir de los
coeficientes. Métricas de evaluación. Dataset **California Housing** de sklearn.
Regresión polinomial. **Validación cruzada** y **sesgo frente a varianza**.

→ Conceptos: `regresion`, `train_validation_test`, `validacion_cruzada`,
`overfitting_underfitting`

Es el práctico más denso en conceptos del programa. El apartado de sesgo y
varianza es la base teórica del problema que ya trabajamos con Melbourne.

### P5 · Clasificación — 117 celdas

Codificación de variables categóricas: a mano, `get_dummies` y `LabelEncoder`.
Concepto de clasificación y métricas — **qué significan TP, TN, FP y FN**.
Modelos: **SVM** (con distintos kernels), **árbol de decisión** (incluida su
visualización) y **Random Forest**, cada uno con entrenamiento, predicción y
evaluación.

→ Conceptos: `clasificacion`, `matriz_confusion`, `metricas_clasificacion`,
`arboles_decision`, `random_forest`

---

## Qué aporta esto al curriculum

Antes de incorporar este material, cuatro conceptos se apoyaban solo en el
proyecto Melbourne y en Galaxy Zoo. Ahora tienen **el tratamiento oficial de la
asignatura**, que es la fuente de máxima prioridad según `spec.md` §G5.

Dos ganancias concretas:

- **`validacion_cruzada` y `overfitting_underfitting`** pasan a tener el
  desarrollo formal de sesgo y varianza (P4), no solo la evidencia empírica de
  los seis modelos de Melbourne.
- **`matriz_confusion`** gana la definición explícita de TP/TN/FP/FN (P5),
  que hasta ahora solo existía aplicada en el informe de Galaxy Zoo.

**Tema fuera del curriculum:** P5 incluye **SVM**, que no está entre los 21
conceptos del programa. Queda registrado como material disponible, no como
concepto a dominar.

---

## `_markdown/`

Conversión de los notebooks resueltos a Markdown, generada por
`03_CODIGO/practica_a_markdown.py`. Existe por una razón concreta: **NotebookLM
no acepta `.ipynb` como fuente, pero sí Markdown.**

Se conservan texto y código, y se descartan las salidas binarias —imágenes en
base64— que inflarían el archivo sin aportar al índice de búsqueda. Las salidas
de texto se truncan a 2.000 caracteres.

No se convierten los `(vacio)`: son los ejercicios del alumno, no material de
consulta, y subirlos a NotebookLM permitiría consultarles la respuesta.

Regenerar:

```bash
python 03_CODIGO/practica_a_markdown.py
```
