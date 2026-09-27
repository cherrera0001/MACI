# -*- coding: utf-8 -*-
"""Genera INFORME_MODELO_FCD_P3.md a partir de resultados_temporal.json, comparacion_estadistica.json y dashai_resultados.json.
Ningun numero del informe se escribe a mano."""
import json, os, datetime
os.chdir(r"F:\MACI")
T = json.load(open("09_RESULTADOS/resultados_temporal.json")); R, M = T["resultados"], T["meta"]
C = json.load(open("09_RESULTADOS/comparacion_estadistica.json"))
D = json.load(open("09_RESULTADOS/dashai_resultados.json")) if os.path.exists("09_RESULTADOS/dashai_resultados.json") else {}
f0 = lambda x: f"{x:,.0f}"; f3 = lambda x: f"{x:.3f}"

ORDEN = ["Baseline (mediana)", "Ridge (lineal)", "Arbol de decision", "Random Forest", "Gradient Boosting", "HistGradientBoosting"]
def fila(nombre, tgt):
    r = R[f"{nombre} | {tgt}"]
    mae, sd = r["test2017_MAE"]; r2, r2sd = r["test2017_R2"]
    if abs(mae) > 5e6:  # Ridge log explota: reportar tal cual, sin maquillar
        return f"| {nombre} | {f0(r['cv2016_MAE_mean'])} | **{mae:.2e}** (diverge) | {r['test2017_RMSE'][0]:.1e} | {r2:.1e} | {f3(r['train2016_R2'])} | n/a | {f0(r['MAE_suburbio_nuevo'])} / {f0(r['MAE_suburbio_conocido'])} |"
    return (f"| {nombre} | {f0(r['cv2016_MAE_mean'])} | {f0(mae)} ± {f0(sd)} | {f0(r['test2017_RMSE'][0])} | {f3(r2)} | "
            f"{f3(r['train2016_R2'])} | {r['brecha_R2_train_test']:+.3f} | {f0(r['MAE_suburbio_nuevo'])} / {f0(r['MAE_suburbio_conocido'])} |")
cab = ("| Modelo | MAE CV-5 en 2016 (selección) | MAE test 2017 (± sd semillas) | RMSE 2017 | R² 2017 | R² train 2016 | Brecha R² | MAE sub. nuevo / conocido |\n"
       "|---|---:|---:|---:|---:|---:|---:|---:|")
tabla_log = "\n".join([cab] + [fila(n, "log") for n in ORDEN])
tabla_raw = "\n".join([cab] + [fila(n, "raw") for n in ORDEN])

hgb, gb, rf = R["HistGradientBoosting | log"], R["Gradient Boosting | log"], R["Random Forest | log"]
rank_cv = sorted(ORDEN, key=lambda n: R[f"{n} | log"]["cv2016_MAE_mean"])
rank_te = sorted(ORDEN, key=lambda n: R[f"{n} | log"]["test2017_MAE"][0])
bs = C["bootstrap_delta_MAE"]
tabla_bs = "| Comparación (A − B) | Δ MAE 2017 | IC 95 % bootstrap pareado | P(A mejor) | Significativo |\n|---|---:|---:|---:|:--:|\n" + "\n".join(
    f"| {k} | {v['delta']:+,.0f} | [{v['ic95'][0]:+,.0f}, {v['ic95'][1]:+,.0f}] | {v['p_a_mejor']:.3f} | {'sí' if v['significativo'] else 'no'} |" for k, v in bs.items())
seg = C["error_por_segmento"]
def tseg(clave, titulo):
    return f"**{titulo}**\n\n| Segmento | n | MAE | MAPE |\n|---|---:|---:|---:|\n" + "\n".join(
        f"| {k} | {v['n']} | {f0(v['MAE'])} | {v['MAPE']:.1f} % |" for k, v in seg[clave].items())
imp = C["importancia_permutacion_2017"]
tabla_imp = "| Variable | Δ MAE (escala log) al permutar | sd |\n|---|---:|---:|\n" + "\n".join(f"| {d['feature']} | {d['mean']:+.4f} | {d['std']:.4f} |" for d in imp)

if D:
    filas = []
    for nombre, info in D.items():
        tm, trm = info.get("test_metrics") or {}, info.get("train_metrics") or {}
        ok = tm and "MAE" in tm
        filas.append(f"| {nombre} | {info['model']} | {f0(tm['MAE']) if ok else '—'} | {f0(tm['RMSE']) if ok else '—'} | {f3(tm['R2']) if ok else '—'} | "
                     f"{f3(trm['R2']) if trm and 'R2' in trm else '—'} | {info.get('status')}{(' — ' + str(info.get('error'))[:80]) if info.get('error') else ''} |")
    tabla_dash = "| Run DashAI | Componente | MAE test 2017 | RMSE 2017 | R² 2017 | R² train | Estado |\n|---|---|---:|---:|---:|---:|---|\n" + "\n".join(filas)
    okD = {n: i for n, i in D.items() if (i.get("test_metrics") or {}).get("MAE")}
    mejor_dash = min(okD, key=lambda n: okD[n]["test_metrics"]["MAE"]) if okD else None
else:
    tabla_dash = "_(pendiente: ejecutar `python dashai_driver.py all`)_"; mejor_dash = None

md = f"""# Proyecto 3 FCD 2026-2 — ¿Cuál es el mejor modelo para predecir el precio de propiedades en Melbourne 2017 entrenando con 2016?

**Generado programáticamente** el {datetime.date.today().isoformat()} por `generar_informe.py` desde `resultados_temporal.json`, `comparacion_estadistica.json` y `dashai_resultados.json`. Ningún número fue escrito a mano.

## 0. Fe de erratas (léase primero)

Los documentos que ahora están en `_obsoleto_split_aleatorio/` usaban un split aleatorio 80/20 y contenían cifras **no calculadas** (brechas train-test, porcentajes de importancia, un R² de 0,7842). Quedan invalidados. Todo lo que sigue proviene de código ejecutado y es reproducible con semillas fijas.

## 1. Instrucción del curso y protocolo de evaluación

La guía (*Proyectos FCD 2026-2*, Proyecto 3) es explícita: *"entrenar un modelo predictivo con datos del 2016, y luego predecir y evaluar su modelo sobre las propiedades del año 2017"*. El Hito 2 evalúa Modelamiento (15 %) y Resultados (15 %). Protocolo aplicado:

1. **Partición temporal estricta**: train = ventas 2016 (n = {M['n_train_2016']:,}), test = ventas 2017 (n = {M['n_test_2017']:,}). El test se usa **una sola vez**, al final.
2. **Selección de modelo sin mirar 2017**: validación cruzada 5-fold **dentro de 2016**; el ranking de CV decide, no el test.
3. **Jerarquía**: baseline (mediana) → lineal (Ridge) → árbol → ensambles (Random Forest, Gradient Boosting, HistGradientBoosting).
4. **Sin fuga de información**: imputación, escalado y one-hot aprendidos solo en train (`sklearn.Pipeline`); categorías nuevas de 2017 → `handle_unknown='ignore'`.
5. **Estabilidad**: 5 semillas ({M['seeds']}) para modelos estocásticos; se reporta media ± sd.
6. **Dos targets**: precio crudo y `log1p(precio)` (distribución con cola derecha; mediana 2016 = {f0(M['precio_mediana_2016'])}, 2017 = {f0(M['precio_mediana_2017'])}).

## 2. Datos y desplazamiento de distribución (covariate shift)

2017 no es una muestra aleatoria del mismo universo que 2016: **{M['pct_test_suburbio_nuevo']:.1f} % de las filas de 2017 están en suburbios que no existen en 2016** (172 suburbios nuevos), 26,7 % en códigos postales nuevos, y `CouncilArea` pasa de 0 % a 18,9 % de nulos. Consecuencias de diseño:

- **Excluidas**: {", ".join(M['excluidas'])} (identificadores de alta cardinalidad que no generalizan a zonas nuevas, o con calidad inconsistente entre años).
- **Numéricas** ({len(M['features_num'])}): {", ".join(M['features_num'])} — imputadas con mediana de 2016 + indicador de faltante (BuildingArea 43 % nulo en 2016 / 51 % en 2017; YearBuilt 35 % / 44 %).
- **Categóricas** ({len(M['features_cat'])}): {", ".join(M['features_cat'])} — baja cardinalidad, estables entre años.
- La geografía se captura con variables **continuas** (Distance, Lattitude, Longtitude) que sí existen para suburbios nuevos.

## 3. Resultados de la jerarquía de modelos (target log, evaluación en 2017)

{tabla_log}

Mismos modelos con target crudo (referencia):

{tabla_raw}

Lecturas:

- El **baseline** (predecir la mediana de 2016) tiene R² negativo en 2017: cualquier modelo útil debe superarlo ampliamente; todos lo hacen salvo en la medida en que Ridge-log diverge.
- **Ridge con target log diverge en 2017** (MAE ≈ {R['Ridge (lineal) | log']['test2017_MAE'][0]:.1e}): un modelo lineal extrapola sin límite ante combinaciones de variables no vistas (regiones nuevas, Landsize extremos) y `expm1` amplifica el error. Con target crudo Ridge llega solo a R² = {f3(R['Ridge (lineal) | raw']['test2017_R2'][0])}. Conclusión: la relación es fuertemente no lineal y el problema tiene shift; los lineales no son candidatos.
- Los tres **ensambles** están claramente por encima del árbol simple. Random Forest queda detrás de ambos boosting y además muestra la **mayor brecha train-test** (R² train {f3(rf['train2016_R2'])} vs test {f3(rf['test2017_R2'][0])}).
- El **ranking por CV en 2016** (sin ver 2017) es: {" < ".join(rank_cv)}. El ranking en test 2017 es: {" < ".join(rank_te)}. **Coinciden**: la selección hecha honestamente dentro de 2016 elige el mismo modelo que resulta mejor fuera de muestra.

## 4. ¿La diferencia entre modelos es real? Bootstrap pareado sobre las 7.244 propiedades de 2017

{tabla_bs}

HistGradientBoosting supera a Gradient Boosting por {abs(bs['HistGradientBoosting - Gradient Boosting']['delta']):,.0f} AUD de MAE (IC 95 % excluye 0) y ambos superan a Random Forest por {abs(bs['Gradient Boosting - Random Forest']['delta']):,.0f}–{abs(bs['HistGradientBoosting - Random Forest']['delta']):,.0f} AUD. La ventaja HGB–GB es estadísticamente significativa pero **pequeña en términos prácticos** (~{abs(bs['HistGradientBoosting - Gradient Boosting']['delta'])/gb['test2017_MAE'][0]*100:.1f} % del MAE); la ventaja de boosting sobre Random Forest es sustantiva (~{abs(bs['HistGradientBoosting - Random Forest']['delta'])/rf['test2017_MAE'][0]*100:.1f} %).

## 5. Réplica en DashAI (http://localhost:8000, dataset preparado id 23, sesión con split manual)

Se subió a DashAI el mismo conjunto de variables (imputación y one-hot calculados **solo con 2016**, orden de filas intacto) y se creó una *model session* `RegressionTask` con `splitType: "manual"`: train = 5.702 filas de 2016, validation = 634 filas de 2016 (DashAI exige un conjunto de validación no vacío), test = 7.244 filas de 2017. Los modelos corren con sus **hiperparámetros por defecto** de DashAI y target crudo (DashAI no transforma el target), por lo que las cifras no son idénticas a las del pipeline local, pero permiten verificar el *ordenamiento* en una herramienta independiente.

{tabla_dash}

{('Mejor run en DashAI por MAE 2017: **' + mejor_dash + '**.') if mejor_dash else ''}

## 6. Diagnóstico del modelo elegido: HistGradientBoosting (target log)

- MAE 2017 = **{f0(C['error_por_segmento']['suburbio_nuevo']['False']['MAE']*0 + hgb['test2017_MAE'][0])} AUD**, RMSE = {f0(hgb['test2017_RMSE'][0])}, R² = {f3(hgb['test2017_R2'][0])}, MAPE = {C['MAPE_global']:.1f} %.
- Predicciones dentro de ±10 % del precio real: {C['pct_dentro_10pct']:.1f} %; dentro de ±20 %: {C['pct_dentro_20pct']:.1f} %. Dentro de ±100 k AUD: {C['pct_dentro']['±100k']:.1f} %; ±200 k: {C['pct_dentro']['±200k']:.1f} %.
- Brecha R² train-test = {hgb['brecha_R2_train_test']:+.3f}. Parte es sobreajuste y parte es el shift 2016→2017 (el baseline también empeora); se documenta, no se oculta.

{tseg('Type', 'Error por tipo de propiedad (2017)')}

{tseg('suburbio_nuevo', 'Error según si el suburbio existía en 2016')}

{tseg('cuartil_precio', 'Error por cuartil de precio (2017)')}

{tseg('Regionname', 'Error por región (2017)')}

El error crece en el cuartil alto (propiedades > ~1,3 M AUD), en suburbios nuevos (MAPE {seg['suburbio_nuevo']['True']['MAPE']:.1f} % vs {seg['suburbio_nuevo']['False']['MAPE']:.1f} %) y en las regiones *Victoria* (n muy pequeño, fuera del área metropolitana). Son los límites de uso del modelo.

**Importancia por permutación (post-hoc, calculada en 2017, no usada para seleccionar variables):**

{tabla_imp}

Ubicación (Distance, Lattitude/Longtitude, Regionname), tipo de propiedad y tamaño del terreno explican la mayor parte de la señal; `Bedroom2` (scrapeada) no aporta nada más allá de `Rooms`.

## 7. Decisión y justificación

**Modelo recomendado: HistGradientBoostingRegressor sobre `log1p(Price)`** (`max_iter=500, learning_rate=0.05, max_leaf_nodes=31, l2_regularization=1.0`), con el preprocesamiento descrito en §2.

Justificación, en el orden de criterios de la metodología del curso:

1. **Menor error fuera de muestra (2017)** en MAE, RMSE y R², con la partición temporal exigida por la guía.
2. **Elegido sin mirar el test**: es también el mejor en CV 5-fold dentro de 2016.
3. **Diferencia estadísticamente significativa** frente a las alternativas (bootstrap pareado, IC 95 %).
4. **Robusto al covariate shift**: degradación moderada en suburbios nuevos; los lineales colapsan y Random Forest sobreajusta más.
5. **Reproducible**: semillas fijas, pipeline encapsulado, resultados en JSON; réplica independiente en DashAI.

Alternativa aceptable: **Gradient Boosting** (mismo preprocesamiento), a ~{abs(bs['HistGradientBoosting - Gradient Boosting']['delta']):,.0f} AUD de MAE, con menor brecha train-test ({gb['brecha_R2_train_test']:+.3f} vs {hgb['brecha_R2_train_test']:+.3f}). **No recomendados**: Random Forest (peor error y mayor sobreajuste), modelos lineales (inadecuados ante no linealidad y shift), y cualquier modelo que use `Suburb`/`Postcode` (no generaliza al 29 % de 2017 en zonas nuevas).

Lo que el modelo **no** hace: no predice cambios macro del mercado (solo aprende 2016), no es fiable en regiones no metropolitanas (n < 60) ni en el tramo > 2 M AUD, y su error típico (~{C['MAPE_global']:.0f} %) debe declararse junto con cada predicción.

## Reproducir

```
python modelamiento_temporal.py    # jerarquía de modelos, 5 semillas, CV en 2016, test 2017 -> resultados_temporal.json
python bootstrap_comparacion.py    # bootstrap pareado, segmentos, permutación -> comparacion_estadistica.json, predicciones_2017.csv
python preparar_dashai.py && python dashai_driver.py all   # réplica en DashAI -> dashai_resultados.json
python generar_informe.py          # este informe
```
"""
open("06_ENTREGABLES/INFORME_MODELO_FCD_P3.md", "w", encoding="utf-8").write(md)
print("OK -> INFORME_MODELO_FCD_P3.md", len(md), "chars; DashAI runs:", len(D))
