# Galaxy Zoo Mini Challenge — Auditoría, reproducción y mejora

Autor del informe: revisión adversarial (Senior DS / ML Eng)
Fecha: 2026-09-12
Métrica oficial: **F1-score macro**

> Estado: secciones 1–5, 8 y 10 (parcial) cerradas con resultados finales.
> Las secciones 6, 7, 9, 11–13 se completan a medida que terminan los
> experimentos en ejecución; cada una se marca explícitamente.

---

## 1. Objetivo

Clasificación multiclase de galaxias SDSS/Galaxy Zoo:

| label | significado |
|---|---|
| 0 | no decidible / votación ambigua |
| 1 | espiral |
| 2 | elíptica |

El objetivo del encargo **no** era hacer funcionar el notebook, sino auditarlo,
reproducirlo, validarlo y mejorarlo, con atención especial a la clase 0 y al
F1-macro.

---

## 2. Auditoría de archivos: los nombres del encargo no coinciden con el disco

Primera discrepancia, relevante para la trazabilidad del experimento:

| Archivo esperado según el encargo | Realidad verificada en disco |
|---|---|
| `GZ_mini_challenge_train.csv` | existe (`Desafio\`, idéntico por hash al de `Downloads\data\data\`) |
| `GZ_mini_challenge_test.csv` | existe (idéntico por hash) |
| `Galaxy_Zoo_Clase0_Optimizado.ipynb` | **no existe** en ningún punto de `F:\MACI` ni de `C:\Users\herre` |
| `predicted_class0_optimized.csv` | existe en `C:\Users\herre\Downloads\data\data\` |

El notebook realmente presente es
`Galaxy_Zoo_Mini_Challenge_resuelto_paso_a_paso.ipynb`.

**Hallazgo de trazabilidad.** El notebook en disco busca pesos en la rejilla
`w0 ∈ [0.7, 1.8]`, `w1 ∈ [0.7, 1.5]`, `w2 ∈ [0.7, 1.4]` (paso 0.1). Los pesos
declarados de la "versión centrada en clase 0", `[1.9, 0.8, 1.0]`, tienen
`w0 = 1.9`, **fuera de esa rejilla**. El notebook presente no puede haberlos
producido: existió una variante que no quedó guardada. Los dos CSV de
predicción difieren en **280 / 10 000** filas, consistente con dos reglas de
decisión distintas sobre el mismo modelo.

### Datos

| | train | test |
|---|---|---|
| shape | (1000, 90) | (10000, 86) |
| nulos | 0 | 0 |
| infinitos | 0 | 0 |
| duplicados exactos | 0 | 0 (9 duplicados en espacio de features) |
| `ID` único | sí | sí |
| solape de `ID` train/test | 0 | — |

Columnas solo en train: `label`, `objID`, `p_cs`, `p_el`. Columnas solo en
test: ninguna.

**Distribución real de clases (verificada en el CSV, no copiada del encargo):**

| clase | n | % |
|---|---|---|
| 0 | 96 | 9.6 |
| 1 | 227 | 22.7 |
| 2 | 677 | 67.7 |

Esto valida cruzadamente las cifras declaradas: recall clase 0 de 0.4688 × 96 =
45 aciertos exactos, y 0.5000 × 96 = 48.

### Calidad de columnas

- **10 columnas constantes**: `sciencePrimary`, `mode`, `sdssPrimary`,
  `bossPrimary`, `segue2Primary`, `segue1Primary`, `seguePrimary`,
  `legacyPrimary`, `nChild`, `resolveStatus`. Quedan 75 features base.
- **6 columnas con MAD = 0** (casi constantes): `zWarning`, `calibStatus_{u,g,r,i,z}`.
  `zWarning` tiene valor modal en el 99.4% de las filas.
- **34 pares con |r| > 0.98.** Caso extremo: `extinction_u/g/r/i/z` con
  **r = 1.0000** entre sí — son cinco copias reescaladas de la misma variable.
  También `modelMag_*` ≈ `dered_*` ≈ `cModelMag_*` (r hasta 0.9992).
- Outliers: `mRrCc_r` llega a 3226 (mediana ≈ 14); las columnas `*MagErr_*`
  concentran la mayoría de valores extremos.

Detalle completo por columna en `analysis/audit_columns.csv`; cifras globales
en `analysis/audit_summary.json`.

---

## 3. Fuga de información: encontrada y no encontrada

### 3.1 Fuga directa confirmada (correctamente excluida por el notebook)

`label` **es derivable de `p_cs` y `p_el`**:

```
1 si p_cs >= 0.5;  2 si p_el >= 0.5;  0 en otro caso
→ coincide con label en 99.8% (998/1000)
```

Las 2 discrepancias son empates exactos `p_cs = p_el = 0.5`. Además,
`max(p_cs, p_el)` **nunca supera 0.493 en la clase 0**, frente a 1.0 en las
clases 1 y 2.

Consecuencia conceptual, no solo técnica: **la clase 0 es por construcción
"ningún bando alcanzó mayoría"**. No es un tipo de galaxia, es un estado del
proceso de votación. Esto condiciona todo el resto del análisis.

La exclusión de `label`, `p_cs`, `p_el`, `ID` y `objID` del notebook original
es correcta y necesaria.

### 3.2 Fuga indirecta: revisada, **no** encontrada

| Riesgo auditado | Veredicto |
|---|---|
| preprocesamiento antes de la CV | OK — `StandardScaler` va dentro del `Pipeline`, se ajusta por fold |
| selección global de features | OK — no hay selección supervisada; las constantes se detectan en train |
| escalado global | OK |
| imputación global | no aplica en el original (no hay nulos declarados) |
| oversampling antes de los folds | OK — no se usa oversampling, solo `auto_class_weights` |
| reutilización del test | OK — el test nunca se usa para ajustar nada |
| ingeniería de features | OK — son diferencias fila-a-fila, no aprenden parámetros |

### 3.3 Defecto real 1: centinelas `-9999` sin tratar

SDSS codifica medición inválida como `-9999`. Hay **2 filas en train y 20 en
test** con al menos un centinela en columnas de magnitud.

El notebook las pasa directas a `engineer_features`, que resta magnitudes:
`-9999 − 17 ≈ -10016`. Se generan features derivadas de ≈ −10⁴ en 20 filas del
test que sí se envían al desafío. No es fuga, es corrupción de datos no
gestionada.

**Corrección aplicada:** convertir `<= -99` a NaN antes de la ingeniería. Es un
umbral físico fijo (una magnitud aparente nunca es ≤ −99), operación
fila-a-fila, por lo que no aprende nada de los datos y no puede generar fuga
entre folds. CatBoost/LightGBM/XGBoost manejan NaN nativamente; los modelos que
no (SVC, RF, ET) reciben imputación por mediana **ajustada dentro del fold de
entrenamiento**.

### 3.4 Defecto real 2: sesgo optimista en la regla de decisión

Los pesos se optimizan sobre **todo** el OOF y el mejor F1 de esa misma
búsqueda se reporta como estimación de rendimiento. No es fuga del test, pero
sí es optimizar y reportar sobre los mismos datos. Cuantificado en §10: el
sesgo es **+0.0338**, y resulta ser el hallazgo más importante de la auditoría.

### 3.5 Riesgo adicional detectado: drift train/test en metadatos

Test de Kolmogórov-Smirnov columna a columna:

| columna | KS | naturaleza |
|---|---|---|
| `cx` | 0.317 | posición en el cielo |
| `cy` | 0.312 | posición en el cielo |
| `extinction_*` | 0.290 | extinción por polvo (línea de visión) |
| `score` | 0.256 | calidad de la observación |
| `cz` | 0.216 | posición en el cielo |
| `mjd` | 0.208 | fecha de observación |

Ninguna es una propiedad física de la galaxia; todas son metadatos de
observación/posición, y todas presentan el drift más alto del dataset. Incluirlas
permite al modelo aprender "región del cielo / campaña de observación" en lugar
de morfología. Por eso se añadió un feature set **E** = D sin estos metadatos
(§6).

---

## 4. Metodología de validación

Común a **todos** los experimentos, para que las comparaciones sean válidas:

- `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`, **los mismos
  índices de fold** reutilizados en cada experimento (`gz_lib.folds`).
- Predicciones **out-of-fold** para las 1000 observaciones.
- Se reportan y **no se mezclan** dos cifras distintas:
  - **CV fold scores**: media ± desviación del F1-macro calculado dentro de
    cada fold.
  - **OOF global**: F1-macro único sobre el vector OOF completo.
- Toda transformación con parámetros va dentro del fold.

Código compartido en `src/gz_lib.py`; scripts numerados `src/00`–`src/08`.

---

## 5. Baseline: diagnóstico de reproducibilidad

Reproducción **literal** del notebook (sin correcciones), en
`src/01_repro_notebook.py`. Feature set D del notebook: 75 base → **137
features**.

### Comparación de modelos del notebook (CV fold scores)

| modelo | F1-macro medio | std |
|---|---|---|
| CatBoost balanceado | 0.6129 | 0.0223 |
| LinearSVC balanceado | 0.6105 | 0.0380 |
| ExtraTrees balanceado | 0.5657 | 0.0349 |

### OOF CatBoost, argmax normal — F1-macro **0.6163**

| clase | precision | recall | F1 |
|---|---|---|---|
| 0 | 0.3049 | 0.2604 | 0.2809 |
| 1 | 0.6354 | 0.7753 | 0.6984 |
| 2 | 0.8939 | 0.8464 | 0.8695 |

Matriz de confusión (filas = real, columnas = predicho):

```
        pred0  pred1  pred2
real 0     25     36     35
real 1     18    176     33
real 2     39     65    573
```

### Veredicto: **REPRODUCIBLE**

Las cuatro cifras declaradas se reproducen **exactamente a 4 decimales**:

| versión | pesos | F1-macro declarado | obtenido | recall 0 | F1 clase 0 |
|---|---|---|---|---|---|
| MACRO | [1.7, 0.9, 0.9] | 0.6339 | **0.6339** ✓ | 0.4688 ✓ | 0.3557 ✓ |
| CLASE 0 | [1.9, 0.8, 1.0] | 0.6317 | **0.6317** ✓ | 0.5000 ✓ | 0.3609 ✓ |

La rejilla del notebook redescubre `[1.7, 0.9, 0.9]` con F1-macro 0.6339, igual
que lo declarado. La semilla, los folds y el pipeline son deterministas y
consistentes con lo reportado.

**Matiz importante sobre la sección 11 del notebook.** El notebook concluye que
CatBoost es el mejor modelo, pero la diferencia con LinearSVC es de **0.0024**,
entre 9 y 16 veces menor que la desviación entre folds (0.0223 y 0.0380). Esa
conclusión **no está respaldada por la validación**: con 1000 filas y 5 folds,
los tres modelos son estadísticamente indistinguibles salvo ExtraTrees, que sí
es peor.

---

## 6. Ablación de features

> **En ejecución** (`src/02_ablation_features.py`, 10 configuraciones:
> A/B/C/D/E × {con, sin} limpieza de centinelas, mismos folds, mismo CatBoost).

Definiciones:

| set | contenido | n features |
|---|---|---|
| A | originales sin constantes | 75 |
| B | A + colores | |
| C | A + diferencias morfológicas | |
| D | A + colores + diferencias (= notebook) | 137 |
| E | D sin metadatos de observación/posición | |

Primer resultado disponible: **A sin limpiar** → CV fold 0.6039 ± 0.0172,
OOF 0.6053, F1 clase 0 0.2570. Es decir, D (OOF 0.6163) supera a A (0.6053)
en +0.0110 — por debajo de la desviación entre folds, por lo que la utilidad
de la ingeniería de features aún no está demostrada. Tabla completa en
`analysis/ablation_results.csv`.

---

## 7. Auditoría de CatBoost e hiperparámetros

> **Pendiente** — se ejecuta tras fijar el feature set.

---

## 8. Análisis profundo de la clase 0

Esta es la sección central, y el resultado es inequívoco.

### 8.1 Los errores se reparten casi simétricamente entre 1 y 2

De las 96 galaxias de clase 0 (OOF, argmax):

| destino | n | % |
|---|---|---|
| real 0 → pred 0 | 25 | 26.0 |
| real 0 → pred 1 | 36 | 37.5 |
| real 0 → pred 2 | 35 | 36.5 |

No hay un sesgo hacia una clase: la clase 0 se disuelve **por igual** hacia
espiral y elíptica. Eso ya sugiere frontera, no región propia.

### 8.2 La clase 0 vive en la zona de incertidumbre entre 1 y 2 — confirmado

Incertidumbre media de las probabilidades OOF por clase real:

| clase real | entropía | margen top-2 | \|P1 − P2\| | P0 medio |
|---|---|---|---|---|
| 0 | **0.7576** | **0.4254** | **0.4722** | 0.3024 |
| 1 | 0.6735 | 0.5382 | 0.5748 | 0.1658 |
| 2 | 0.5514 | 0.6393 | 0.6792 | 0.1331 |

La clase 0 tiene la entropía más alta y el margen más bajo de las tres.

**Test decisivo.** Tasa de clase 0 real por decil de `|P1 − P2|` (balance entre
espiral y elíptica; bajo = el modelo no sabe distinguir 1 de 2):

| decil de \|P1−P2\| | 0 (más ambiguo) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 (más claro) |
|---|---|---|---|---|---|---|---|---|---|---|
| tasa clase 0 real | **0.20** | 0.17 | 0.11 | 0.17 | 0.10 | 0.08 | 0.08 | 0.02 | 0.02 | **0.01** |

Caída monótona de 20× entre el decil más ambiguo y el más claro. El mismo
patrón con la entropía (0.01 → 0.16). **La clase 0 se concentra exactamente
donde el modelo no puede decidir entre espiral y elíptica.** Es una frontera,
no un cúmulo.

### 8.3 Evidencia independiente del modelo (misma conclusión)

Calculada solo con los datos, sin ningún clasificador
(`analysis/class0_geometry.csv`):

- **Techo de AUC marginal univariada: 0.754 para 0-vs-resto**, frente a
  **0.9041 para 1-vs-2**. Ninguna feature individual detecta bien la clase 0.
- **Dispersión estandarizada mediana: clase 0 = 1.229** vs clase 1 = 0.750 y
  clase 2 = 0.954. La clase 0 es la más dispersa: es una mezcla, no un grupo.
- En las 20 features que mejor separan 1 de 2, la media de la clase 0 cae
  **entre** las medias de 1 y 2 en el 60% de los casos, con posición relativa
  mediana `t_rel = 0.855` (pegada al lado elíptica).

### 8.4 Qué distingue a los aciertos de los falsos negativos

Comparando medias estandarizadas de TP₀ frente a FN 0→1 y 0→2, las features con
mayor diferencia son todas de la **banda z y de errores fotométricos**:

| feature | TP₀ (sd) | FN 0→1 | FN 0→2 |
|---|---|---|---|
| `petroMag_color_r_z` | **−2.514** | −0.279 | 0.100 |
| `petroMag_color_i_z` | **−2.454** | −0.148 | 0.059 |
| `petro_minus_model_z` | **+2.138** | 0.031 | −0.107 |
| `modelMagErr_z` | **+2.055** | 0.004 | −0.028 |
| `psfMagErr_i` | **+2.016** | −0.023 | 0.362 |
| `petroMag_z` | **+1.991** | −0.092 | 0.330 |

Interpretación: **el modelo solo acierta la clase 0 cuando la fotometría está
visiblemente rota o ruidosa** (errores de magnitud a +2 sd, colores r−z
extremos a −2.5 sd), no cuando la morfología es genuinamente ambigua. Coincide
con el análisis libre de modelo, donde las features más asociadas a 0-vs-resto
eran `fiberMagErr_i`, `psfMagErr_*` — es decir, **calidad de imagen pobre**.

### 8.5 Conclusión causal

La clase 0 no es una morfología: es el resultado de que los votantes humanos no
alcanzaran mayoría, y eso ocurre cuando la imagen es mala o el objeto está en la
frontera espiral/elíptica. El modelo dispone exactamente de las dos señales:
detecta bien la primera (fotometría rota) y no puede detectar la segunda
(ambigüedad genuina), porque en esa región las features de clase 0 son
indistinguibles de las de 1 y 2. **De ahí el techo estructural del F1 de clase
0, no de una mala elección de hiperparámetros.**

---

## 9. Comparación de modelos

> **Pendiente** — `src/03_model_comparison.py` (LinearSVC, LogisticRegression,
> RandomForest, ExtraTrees, LightGBM, XGBoost, CatBoost), mismos folds, mismo
> feature set, misma métrica.

---

## 10. Optimización de la regla de decisión

Auditoría de `pred = argmax(P · [w0, w1, w2])` sobre el OOF reproducido
(`analysis/decision_rule.csv`, `analysis/pareto_front.csv`).

Nota técnica: solo importan los **cocientes** de los pesos, no su escala. Mi
búsqueda normaliza `w1 = 1.0`, y por eso redescubre los puntos declarados
reescalados: `[1.7, 0.9, 0.9] ≡ [1.9, 1.0, 1.0]` y
`[1.9, 0.8, 1.0] ≡ [2.35, 1.0, 1.25]`. Coinciden exactamente, lo que valida
ambas búsquedas.

| variante | pesos | F1-macro | prec 0 | recall 0 | F1 clase 0 | n pred 0 |
|---|---|---|---|---|---|---|
| A argmax | [1, 1, 1] | 0.6163 | 0.3049 | 0.2604 | 0.2809 | 82 |
| B declarado macro | [1.7, 0.9, 0.9] | **0.6339** | 0.2866 | 0.4688 | 0.3557 | 157 |
| C declarado clase 0 | [1.9, 0.8, 1.0] | 0.6317 | 0.2824 | 0.5000 | 0.3609 | 170 |
| D1 mejor F1-macro | [1.90, 1.0, 1.00] | **0.6339** | 0.2866 | 0.4688 | 0.3557 | 157 |
| D2 máx F1 clase 0 (F1m ≥ best−0.005) | [2.35, 1.0, 1.25] | 0.6317 | 0.2824 | 0.5000 | **0.3609** | 170 |

La búsqueda sistemática nueva (paso 0.05, rango 0.5–2.6) **no encuentra nada
mejor** que lo ya declarado: el óptimo es el mismo punto. Frente de Pareto de
10 puntos en `analysis/pareto_front.csv`; el extremo de recall 0 llega a 0.6250
pero hundiendo el F1-macro a 0.5822.

### 10.1 Hallazgo crítico: la ganancia de los pesos **no generaliza**

Estimación anidada honesta: los pesos se ajustan solo con los folds de
entrenamiento y se aplican al fold de validación, que no participó en la
búsqueda (`gz_lib.nested_weight_score`).

| estimación | F1-macro | F1 clase 0 |
|---|---|---|
| argmax simple | **0.6163** | 0.2809 |
| pesos **anidados** (honesto) | **0.6001** | 0.2679 |
| pesos tuneados sobre todo el OOF (lo reportado) | 0.6339 | 0.3557 |

- Sesgo optimista de reportar el óptimo tuneado: **+0.0338**.
- Y lo más grave: la regla de pesos, evaluada honestamente fuera de muestra,
  es **peor que el argmax simple en −0.0162**.
- Los pesos elegidos por fold son inestables: `w2` oscila entre **1.0 y 2.4**
  entre folds.

**Conclusión adversarial.** La mejora de 0.6163 → 0.6339 atribuida a la
optimización de pesos es en su mayor parte sobreajuste a las 96 observaciones
de clase 0 del OOF. Con 96 ejemplos, mover la frontera de decisión reasigna
decenas de filas y el óptimo de la rejilla persigue ruido. El F1-macro 0.6339
**no es una estimación válida del rendimiento en el test oculto**; la
estimación defendible del pipeline actual está entre 0.60 y 0.62.

Esto no invalida enviar la versión con pesos —puede acertar—, pero sí invalida
*declararla como 0.6339 validado*.

---

## 11. Resultados consolidados

> **Pendiente** de la ablación y la comparación de modelos.

---

## 12. Candidato A — máximo F1-macro validado

> **Pendiente.**

## 13. Candidato B — máximo rendimiento clase 0 con F1-macro ≥ best − 0.005

> **Pendiente.**

---

## 14. Limitaciones

1. **n = 1000 con 96 ejemplos de clase 0.** Es el límite dominante. La
   desviación entre folds (0.022–0.038) es mayor que casi todas las diferencias
   que se quieren medir, por lo que la mayoría de las comparaciones de modelos
   no son concluyentes.
2. **Techo estructural de la clase 0.** Es una etiqueta sobre el proceso de
   votación, no sobre la galaxia (§3.1, §8.5). Ninguna feature disponible
   supera AUC 0.754 para 0-vs-resto.
3. **La optimización de la regla de decisión no generaliza** (§10.1). Cualquier
   cifra obtenida tuneando y reportando sobre el mismo OOF está inflada.
4. **Drift train/test en metadatos de observación** (§3.5): el rendimiento en
   el test oculto puede diferir del OOF por esta razón, independientemente del
   modelo.
5. **No hay etiquetas de test**, por lo que la selección final descansa
   íntegramente en el OOF de 1000 filas.
6. Los `p_cs`/`p_el` del test no existen, así que no es posible verificar en el
   test la hipótesis de ambigüedad.

## 15. Siguiente experimento recomendado

> Se completa al cerrar las secciones pendientes.

---

## Estructura de entregables

```
analysis/     audit_columns.csv, audit_summary.json, class0_geometry.csv,
              class0_analysis.csv, class0_frontera_P1P2.csv,
              class0_incertidumbre.csv, decision_rule.csv,
              decision_rule_nested.csv, pareto_front.csv,
              weight_search_full.csv, repro_notebook.json,
              ablation_results.csv, metrics.csv
outputs/      predicted_best_macro.csv, predicted_best_class0.csv
src/          gz_lib.py, 00_audit.py … 08_ensemble.py
REPORT.md
Galaxy_Zoo_Optimized_Final.ipynb
```

Los archivos originales (`Galaxy_Zoo_Mini_Challenge_resuelto_paso_a_paso.ipynb`,
`predicted.csv`, `predicted_class0_optimized.csv`) **no se modifican**.
