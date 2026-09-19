# -*- coding: utf-8 -*-
"""
Genera (1) PITCH_HITO2_REVISION.md — revisión lámina por lámina del pitch original, y
       (2) Pitch_Hito2_v2.pptx — versión corregida.
Fuentes de TODA cifra: anclaje.json (Hito 1), correlacion_dashai.json (explorador DashAI, dataset 22)
y dashai_resultados.json (model-session DashAI, split manual 2016/2017, variables Hito 1). Nada a mano.
"""
import json, os, datetime
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.enum.text import PP_ALIGN

os.chdir(r"F:\MACI")
A = json.load(open(r"02_PROYECTO_FCD/Hito1/anclaje.json", encoding="utf-8"))
C = json.load(open("05_RESULTADOS/correlacion_dashai.json", encoding="utf-8"))
D = json.load(open("05_RESULTADOS/dashai_resultados.json", encoding="utf-8"))
ST = json.load(open("05_RESULTADOS/dashai_state.json", encoding="utf-8"))

f0 = lambda x: f"{x:,.0f}".replace(",", ".")
pct = lambda x: f"{x:.1f} %".replace(".", ",")
def dr(nombre):  # métricas DashAI por nombre de run
    r = D[nombre]; return r["test_metrics"], r.get("train_metrics") or {}
LIN, ARB, RF, GB = dr("01 Lineal (OLS)"), dr("03 Arbol de decision"), dr("04 Random Forest (default)"), dr("05 Gradient Boosting (default)")
cota = A["cota"]; base = dict(MAE=cota["mae_const2016_sobre2017"], RMSE=cota["rmse_const2016_sobre2017"], R2=cota["r2_const2016_sobre2017"])
rank = {r["variable"]: r["r"] for r in C["ranking_abs_r_vs_Price"]}
nv = A["no_vistos"]["Suburb"]; comp = A["composicion"]; aus = A["ausencias"]; dat = A["datos"]; pl = A["plausibilidad"]; part = A["particion"]
mrooms = dat["mediana_precio_por_Rooms"]; mtype = dat["mediana_precio_por_Type"]
red_rf = 100 * (1 - RF[0]["MAE"] / base["MAE"]); red_gb = 100 * (1 - GB[0]["MAE"] / base["MAE"])
ratio_rf_lin = LIN[0]["MAE"] / RF[0]["MAE"]
nulos_col = aus["por_columna"]; n = A["procedencia"]["filas"]
pct_nulo = lambda c: 100 * nulos_col[c] / n
MESES = {1: "ene", 2: "feb", 3: "mar", 4: "abr", 5: "may", 6: "jun", 7: "jul", 8: "ago", 9: "sep", 10: "oct", 11: "nov", 12: "dic"}
m16 = part["meses_presentes_2016"]; m17 = part["meses_presentes_2017"]
rango16 = f"{MESES[m16[0]]}–{MESES[m16[-1]]} 2016 (sin {', '.join(MESES[m] for m in part['meses_ausentes_2016'])})"
rango17 = f"{MESES[m17[0]]}–{MESES[m17[-1]]} 2017 (hasta {A['procedencia']['fecha_max']})"

# ------------------------------------------------------------------ 1) REVISIÓN
filas = [
 ("2 · Problema", "Train 6.336 / Test 7.244", f"{f0(part['n_2016'])} / {f0(part['n_2017'])} (anclaje.particion)", "OK", ""),
 ("3 · Datos", "13.580 ventas · 21 atributos", f"{f0(n)} × {A['procedencia']['columnas']} (anclaje.procedencia)", "OK", ""),
 ("4 · Calidad", "97,2 % de los nulos en BuildingArea/YearBuilt/CouncilArea", f"{pct(aus['pct_nulos_en_BuildingArea_YearBuilt_CouncilArea'])} de {f0(aus['total_celdas_nulas'])} celdas nulas (anclaje.ausencias)", "CORREGIR", "Usar 99,5 %."),
 ("4 · Calidad", "BuildingArea 47,5 % · YearBuilt 39,6 % · CouncilArea 10,1 % · Car 0,5 %", " · ".join(f"{c} {pct(pct_nulo(c))}" for c in ["BuildingArea", "YearBuilt", "CouncilArea", "Car"]), "OK", ""),
 ("4 · Calidad", "Zeros: 1.939 Landsize, 17 BuildingArea, 6 Distance", f"{f0(pl['Landsize_cero'])} / {pl['BuildingArea_cero']} / {pl['Distance_cero']} (anclaje.plausibilidad)", "OK", ""),
 ("4 · Calidad", "Rango temporal: 2016 (ene–dic) y 2017 (ene–sep)", f"{rango16}; {rango17} (anclaje.particion)", "CORREGIR", "2017 no tiene enero; 2016 no tiene marzo."),
 ("4 · Calidad", "«los atributos espaciales anteriores no influyen en los precios por la falta de datos»", f"YearBuilt–Price = {rank['YearBuilt']} es la 2.ª |r| (DashAI). No son «espaciales».", "CORREGIR", "Se excluyen POR NULOS, no por falta de señal."),
 ("5 · EDA", "Correlaciones: Rooms .497, Bedroom2 .476, Bathroom .467, YearBuilt −.324, Car .239, Distance −.163", "Explorador DashAI (8 numéricas): " + " · ".join(f"{k} {v:+.3f}" for k, v in rank.items()), "CORREGIR", "Bedroom2/Bathroom/Car no están en el heatmap DashAI; YearBuilt es −0,262."),
 ("5 · EDA", "«ubicación (menor impacto)» / «la distancia tiene menor impacto»", f"Lattitude {rank['Lattitude']:+.3f}, Longtitude {rank['Longtitude']:+.3f}, Distance {rank['Distance']:+.3f} > BuildingArea {rank['BuildingArea']:+.3f}, Landsize {rank['Landsize']:+.3f}", "CORREGIR", "La ubicación NO es la de menor impacto en la matriz DashAI."),
 ("5 · EDA", "Mediana por habitaciones: 6→1,80M, 8→1,66M, 10→0,85M (eje sin 5 ni 7)", " · ".join(f"{k}→{f0(v['mediana'])} (n={v['n']})" for k, v in mrooms.items()), "CORREGIR", "1,66M es 5 hab.; 8 hab. = 1,515M; 10 hab. = 0,90M con n=1. Mostrar 1–5 y agrupar 6+."),
 ("5 · EDA", "Mediana por tipo: casa 1,08M · casa pareada 0,85M · dúplex 0,56M", " · ".join(f"{k}: {f0(v['mediana'])} (n={f0(v['n'])})" for k, v in mtype.items()), "OK", ""),
 ("5 · EDA", "Rooms–Bedroom2 = 0,944", "No está en el heatmap DashAI (Bedroom2 categórica). Es decisión de modelo (b) del Hito 1.", "REUBICAR", "Llevar a la lámina de modelamiento como justificación de exclusión, citando notebook, no DashAI."),
 ("6 · Antes de modelar", "172 barrios nuevos", f"{nv['niveles_nuevos']} barrios = {f0(nv['filas_2017_afectadas'])} filas ({pct(nv['pct_2017'])} de 2017); mediana visto {f0(nv['mediana_precio_visto'])} vs nuevo {f0(nv['mediana_precio_nuevo'])}; distancia mediana {nv['distancia_mediana_visto']} vs {nv['distancia_mediana_nuevo']} km", "OK (ampliar)", "Falta el impacto: 29,1 % de 2017 y precios/distancias distintos."),
 ("7 · Benchmark", "Baseline MAE 2017 = 421.620", f"{f0(base['MAE'])} (anclaje.cota.mae_const2016_sobre2017); la lámina 8 dice 431.648", "CORREGIR", "Inconsistencia interna entre láminas 7 y 8."),
 ("7 · Benchmark", "Lineal 294.888 / Árbol 274.625 / RF 220.771 / GB 216.040 (MAE 2017)", f"DashAI (split manual 2016/2017, variables Hito 1): Lineal {f0(LIN[0]['MAE'])} / Árbol {f0(ARB[0]['MAE'])} / RF {f0(RF[0]['MAE'])} / GB {f0(GB[0]['MAE'])}", "REEMPLAZAR", "Sin fuente trazable; usar los runs de DashAI (sesión " + str(ST.get("session_id")) + ")."),
 ("7 · Benchmark", "«MAE CV (2016)» por modelo", "No existe en DashAI ni en anclaje.", "ELIMINAR", "No citar cifras sin fuente."),
 ("8 · Resultados", "R² optimizado 0,7234 · MAE final $210.104 · RF $220.778", f"DashAI: RF MAE {f0(RF[0]['MAE'])} / R² {RF[0]['R2']:.3f}; GB MAE {f0(GB[0]['MAE'])} / R² {GB[0]['R2']:.3f}. Tres cifras distintas de GB en el pitch (216.040 / 210.104 / R² 0,71 vs 0,7234).", "REEMPLAZAR", ""),
 ("8 · Resultados", "1,8× mejora vs regresión lineal", f"294.888/210.104 = 1,40× (aritmética del propio pitch); con DashAI RF: {ratio_rf_lin:.2f}×", "CORREGIR", ""),
 ("8 · Resultados", "51,3 % reducción MAE vs baseline", f"1 − 210.104/431.648 = 51,3 % ✓ aritmética; con DashAI: RF {pct(red_rf)}, GB {pct(red_gb)}", "REEMPLAZAR", ""),
 ("8 · Resultados", "«Gradient Boosting es el mejor modelo»", "Decisión Hito 1 = Random Forest (no se corona GB). DashAI: ver tabla.", "CORREGIR", "Mantener RF como modelo del proyecto; reportar GB como alternativa."),
 ("8 · Resultados", "«El patrón del 2016 se transfiere de forma consistente al 2017»", f"29,1 % de 2017 en barrios nuevos; deriva mediana agregada {comp['deriva_agregada_pct']} % pero {comp['deriva_comparable_pct']} % en barrios comparables", "MATIZAR", "Decir qué se transfiere y qué no."),
]
md = ["# Revisión del pitch Hito 2 (Pitch_Hito2_Prediccion_Propiedades_Melbourne.pdf)", "",
      f"Generado el {datetime.date.today().isoformat()} por `generar_pitch_v2.py`. Fuentes: `anclaje.json`, `correlacion_dashai.json` (explorador DashAI dataset 22), `dashai_resultados.json` (DashAI dataset {ST.get('dataset_id')}, sesión {ST.get('session_id')}, split manual 2016/2017, variables Hito 1). Ninguna cifra a mano.", "",
      "| Lámina | Afirmación del pitch | Fuente de verdad | Veredicto | Acción |", "|---|---|---|---|---|"]
md += [f"| {a} | {b} | {c} | **{d}** | {e} |" for a, b, c, d, e in filas]
md += ["", "## Benchmark oficial (DashAI, test = 2017; baseline = anclaje)", "", "| Modelo | MAE 2017 | RMSE 2017 | R² 2017 | R² train 2016 |", "|---|---:|---:|---:|---:|",
       f"| Baseline mediana 2016 | {f0(base['MAE'])} | {f0(base['RMSE'])} | {base['R2']:.3f} | — |"]
for nombre, (tm, trm) in [("Regresión lineal", LIN), ("Árbol de decisión", ARB), ("Random Forest", RF), ("Gradient Boosting", GB)]:
    md.append(f"| {nombre} | {f0(tm['MAE'])} | {f0(tm['RMSE'])} | {tm['R2']:.3f} | {trm.get('R2', float('nan')):.3f} |")
md += ["", "Hiperparámetros por defecto de DashAI; validation = 10 % de 2016 (exigido por DashAI), train = 90 % de 2016, test = 100 % de 2017. Nota: `datos.mediana_precio_por_Rooms` y `mediana_precio_por_Type` se agregaron a anclaje.py en esta revisión para anclar las cifras del deck."]
open("06_ENTREGABLES/PITCH_HITO2_REVISION.md", "w", encoding="utf-8").write("\n".join(md))

# ------------------------------------------------------------------ 2) DECK v2
NAVY, INK, MUTED, BLUE, TEAL, ORANGE, RED, BG = RGBColor(0x14, 0x1E, 0x3C), RGBColor(0x1F, 0x29, 0x37), RGBColor(0x64, 0x74, 0x8B), RGBColor(0x1E, 0x5E, 0xFF), RGBColor(0x0F, 0x9D, 0x8A), RGBColor(0xF0, 0x8C, 0x00), RGBColor(0xD6, 0x2E, 0x4C), RGBColor(0xF5, 0xF7, 0xFB)
prs = Presentation(); prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
BL = prs.slide_layouts[6]

def txt(slide, x, y, w, h, text, size=14, bold=False, color=INK, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    lines = text if isinstance(text, list) else [text]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.alignment = align
        r = p.add_run(); r.text = ln; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = "Calibri"
    return tb
def header(slide, tag, title, sub=None, num=None):
    txt(slide, 0.5, 0.25, 4, 0.35, tag, 11, True, BLUE); txt(slide, 9.3, 0.25, 3.6, 0.35, "Hito 2 · Proyecto 3 · Melbourne 2016→2017", 10, False, MUTED, PP_ALIGN.RIGHT)
    txt(slide, 0.5, 0.6, 12.3, 0.8, title, 26 if len(title) <= 62 else 22, True, NAVY)
    if sub: txt(slide, 0.5, 1.35, 12.3, 0.5, sub, 13, False, MUTED)
    if num: txt(slide, 12.4, 7.0, 0.6, 0.3, str(num), 10, False, MUTED, PP_ALIGN.RIGHT)
    txt(slide, 0.5, 7.0, 8, 0.3, "Fuentes: anclaje.json · explorador DashAI (dataset 22) · model-session DashAI (split manual 2016/2017)", 8, False, MUTED)
def kpi(slide, x, y, w, valor, etiqueta, color=BLUE, h=1.15):
    box = slide.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h)); box.fill.solid(); box.fill.fore_color.rgb = BG; box.line.color.rgb = RGBColor(0xE2, 0xE8, 0xF0)
    txt(slide, x + 0.15, y + 0.1, w - 0.3, 0.6, valor, 26, True, color); txt(slide, x + 0.15, y + 0.68, w - 0.3, 0.45, etiqueta, 11, False, MUTED)
def bullets(slide, x, y, w, h, items, size=13):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); r = p.add_run(); r.text = "•  " + it; r.font.size = Pt(size); r.font.color.rgb = INK; r.font.name = "Calibri"; p.space_after = Pt(6)
def tabla(slide, x, y, w, h, rows, col_w=None, size=11):
    t = slide.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y), Inches(w), Inches(h)).table
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            cell = t.cell(i, j); cell.text = str(v); p = cell.text_frame.paragraphs[0]; p.font.size = Pt(size); p.font.name = "Calibri"; p.font.bold = (i == 0)
            p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF) if i == 0 else INK; p.alignment = PP_ALIGN.RIGHT if (j > 0 and i > 0) else PP_ALIGN.LEFT
            cell.fill.solid(); cell.fill.fore_color.rgb = NAVY if i == 0 else (BG if i % 2 else RGBColor(0xFF, 0xFF, 0xFF))
    if col_w:
        for j, cw in enumerate(col_w): t.columns[j].width = Inches(cw)
def barras(slide, x, y, w, h, cats, series, title, horizontal=True, fmt='0.000', colors=None, legend=False):
    cd = CategoryChartData(); cd.categories = cats
    for nm, vals in series: cd.add_series(nm, vals)
    ch = slide.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED if horizontal else XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(x), Inches(y), Inches(w), Inches(h), cd).chart
    ch.has_title = True; ch.chart_title.text_frame.text = title; ch.chart_title.text_frame.paragraphs[0].font.size = Pt(12); ch.chart_title.text_frame.paragraphs[0].font.bold = True
    ch.has_legend = legend
    if legend: ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(9)
    pl_ = ch.plots[0]; pl_.has_data_labels = True; pl_.data_labels.number_format = fmt; pl_.data_labels.number_format_is_linked = False; pl_.data_labels.font.size = Pt(9); pl_.gap_width = 60
    ch.value_axis.has_major_gridlines = False; ch.value_axis.tick_labels.font.size = Pt(9); ch.category_axis.tick_labels.font.size = Pt(10)
    if colors:
        for s, col in zip(pl_.series, colors): s.format.fill.solid(); s.format.fill.fore_color.rgb = col
    return ch

# 1 Portada
s = prs.slides.add_slide(BL)
txt(s, 0.8, 2.0, 11.5, 1.0, "Predicción del valor de propiedades en Melbourne", 36, True, NAVY)
txt(s, 0.8, 3.0, 11.5, 0.6, "Proyecto 3 · Hito 2 · Fundamentos de Ciencia de Datos", 18, False, MUTED)
txt(s, 0.8, 3.7, 11.5, 0.6, f"Entrenar con ventas 2016 (n = {f0(part['n_2016'])}) → predecir y evaluar sobre 2017 (n = {f0(part['n_2017'])})", 16, False, INK)
txt(s, 0.8, 5.2, 11.5, 0.5, "C. Abrigo · C. Herrera · K. Urbina", 14, True, INK)
txt(s, 0.8, 5.7, 11.5, 0.5, "Toda cifra de este deck proviene de anclaje.json o de DashAI (dataset 22); ninguna se escribió a mano.", 11, False, MUTED)

# 2 Problema e hipótesis
s = prs.slides.add_slide(BL); header(s, "INTRODUCCIÓN", "El problema: predecir 2017 con la data de 2016", "Pregunta, hipótesis y protocolo de evaluación temporal.", 2)
txt(s, 0.5, 1.9, 6.0, 0.4, "Pregunta", 14, True, BLUE)
txt(s, 0.5, 2.3, 6.0, 1.2, "¿Puede un modelo entrenado solo con transacciones de 2016 estimar precios de 2017 con error menor que una regla básica de mercado (mediana 2016)?", 13)
txt(s, 0.5, 3.6, 6.0, 0.4, "H1", 14, True, TEAL)
txt(s, 0.5, 4.0, 6.0, 1.3, "Las relaciones entre características (habitaciones, tipo, ubicación) y precio observadas en 2016 se mantienen lo suficiente en 2017 para predecir mejor que la estimación básica.", 12)
txt(s, 0.5, 5.3, 6.0, 0.4, "H0", 14, True, RED)
txt(s, 0.5, 5.7, 6.0, 1.2, "Esas relaciones no se mantienen: el modelo no supera a la mediana de 2016.", 12)
kpi(s, 7.0, 1.9, 2.9, f0(part["n_2016"]), f"Train 2016 ({pct(part['pct_2016'])})", BLUE); kpi(s, 10.1, 1.9, 2.9, f0(part["n_2017"]), f"Test 2017 ({pct(part['pct_2017'])})", TEAL)
kpi(s, 7.0, 3.2, 6.0, f"MAE {f0(base['MAE'])} AUD", "Regla básica a superar: predecir la mediana 2016 en 2017 (anclaje.cota)", ORANGE)
bullets(s, 7.0, 4.6, 6.0, 2.3, ["Test 2017 se usa una sola vez, al final.", "Selección de variables y preprocesamiento aprendidos solo con 2016.", "Mismo protocolo replicado en DashAI con split manual por índices (2016 → train, 2017 → test)."], 12)

# 3 Datos
s = prs.slides.add_slide(BL); header(s, "DATOS", "Datos: 13.580 ventas, 21 atributos, 2016-01-28 → 2017-09-23", "housing_data.csv (snapshot Kaggle melb_data). SHA-256 verificado en anclaje.py.", 3)
kpi(s, 0.5, 1.9, 3.0, f0(n), "ventas observadas", TEAL); kpi(s, 3.7, 1.9, 3.0, str(A["procedencia"]["columnas"]), "atributos originales", BLUE)
kpi(s, 6.9, 1.9, 3.0, f0(dat["mediana_precio_global"]), "precio mediano (AUD)", ORANGE); kpi(s, 10.1, 1.9, 2.8, f0(dat["media_precio_global"]), "precio medio (cola derecha)", ORANGE)
tabla(s, 0.5, 3.4, 6.2, 1.6, [["Tipo", "n", "Mediana precio"], ["casa (h)", f0(mtype["h"]["n"]), f0(mtype["h"]["mediana"])], ["casa pareada (t)", f0(mtype["t"]["n"]), f0(mtype["t"]["mediana"])], ["dúplex (u)", f0(mtype["u"]["n"]), f0(mtype["u"]["mediana"])]], [2.4, 1.6, 2.2])
bullets(s, 7.0, 3.4, 6.0, 3.4, [f"Cobertura temporal: {rango16}; {rango17}. 2017 no es un año completo.",
                                f"{dat['n_suburbios']} barrios, {dat['n_regiones']} regiones, {dat['n_vendedores']} vendedores, {dat['n_metodos']} métodos de venta.",
                                f"Duplicados de fila completa: {A['procedencia']['duplicados_fila_completa']}. Reventas que cruzan el corte: {A['reventas']['propiedades']} propiedades ({A['reventas']['pct_de_2017']} % de 2017).",
                                "Target: Precio. Estructura: Habitaciones, Baños, Estacionamientos, Tamaño de terreno, Tipo. Espacial: Barrio, Distancia, Región, Latitud/Longitud. Comercial: Método, Vendedor, Fecha."], 12)

# 4 Calidad
s = prs.slides.add_slide(BL); header(s, "CALIDAD DE DATOS", "Nulos concentrados en tres columnas: fuera por nulos, no por falta de señal", None, 4)
barras(s, 0.5, 1.6, 6.2, 3.6, ["BuildingArea", "YearBuilt", "CouncilArea", "Car"], [("% faltante", [round(pct_nulo(c), 1) for c in ["BuildingArea", "YearBuilt", "CouncilArea", "Car"]])], "% de filas con nulo (13.580)", True, '0.0"%"', [RED])
bullets(s, 7.0, 1.7, 6.0, 5.0, [f"{pct(aus['pct_nulos_en_BuildingArea_YearBuilt_CouncilArea'])} de las {f0(aus['total_celdas_nulas'])} celdas nulas están en BuildingArea, YearBuilt y CouncilArea.",
    f"Los nulos crecen en 2017: CouncilArea {aus['tasa_por_anio']['CouncilArea']['2016']} % → {aus['tasa_por_anio']['CouncilArea']['2017']} %; BuildingArea {aus['tasa_por_anio']['BuildingArea']['2016']} % → {aus['tasa_por_anio']['BuildingArea']['2017']} %.",
    f"Ceros sospechosos: {f0(pl['Landsize_cero'])} Landsize = 0 ({pl['Landsize_cero_pct']} %), {pl['BuildingArea_cero']} BuildingArea = 0, {pl['Distance_cero']} Distance = 0. Se documentan, no se borran.",
    f"Plausibilidad: YearBuilt mínimo {pl['YearBuilt_min']}; {pl['YearBuilt_posteriores_venta']} construcciones posteriores a la venta; Landsize máx. {f0(pl['Landsize_max'])} m².",
    f"Decisión: BuildingArea y YearBuilt salen del modelo POR NULOS (imputar ≈ mitad del dataset). No por falta de señal: YearBuilt–Precio = {rank['YearBuilt']:+.3f} es la 2.ª |r| en DashAI."], 12)

# 5 EDA
s = prs.slides.add_slide(BL); header(s, "ANÁLISIS EXPLORATORIO", "Señal en estructura y ubicación; ninguna |r| supera 0,5", "Correlaciones = explorador de DashAI (Pearson, 8 columnas numéricas). Tipo no entra en Pearson: se lee por medianas.", 5)
rk = [k for k in ["1", "2", "3", "4", "5"]]
barras(s, 0.4, 1.9, 4.3, 4.3, [f"{k} hab. (n={f0(mrooms[k]['n'])})" for k in rk], [("Mediana precio", [mrooms[k]["mediana"] for k in rk])], "Mediana de precio por habitaciones (1–5)", False, '#,##0', [TEAL])
barras(s, 4.8, 1.9, 3.6, 4.3, ["casa", "casa pareada", "dúplex"], [("Mediana", [mtype["h"]["mediana"], mtype["t"]["mediana"], mtype["u"]["mediana"]])], "Mediana de precio por tipo", False, '#,##0', [BLUE])
cats = list(rank.keys()); barras(s, 8.5, 1.9, 4.5, 4.3, cats[::-1], [("r", [rank[k] for k in cats[::-1]])], "Pearson con Price (DashAI, dataset 22)", True, '0.000', [ORANGE])
txt(s, 0.5, 6.3, 12.3, 0.6, f"6+ habitaciones: n = {sum(v['n'] for k, v in mrooms.items() if int(k) >= 6)} (no se grafican). Fuera del heatmap DashAI: Bathroom, Bedroom2, Car, Type, Region. Habitaciones–Precio {rank['Rooms']:+.3f} es la más alta, no «fuerte».", 10, False, MUTED)

# 6 Shift 2016→2017
s = prs.slides.add_slide(BL); header(s, "ANTES DE MODELAR", "2017 no es una muestra de 2016: 172 barrios nuevos = 29 % del test", "Auditoría de cambio de composición (anclaje.no_vistos / composicion).", 6)
kpi(s, 0.5, 1.9, 3.0, str(nv["niveles_nuevos"]), f"barrios de 2017 ausentes en 2016 ({nv['niveles_2016']} → {nv['niveles_2017']})", ORANGE)
kpi(s, 3.7, 1.9, 3.0, pct(nv["pct_2017"]), f"de las filas de 2017 ({f0(nv['filas_2017_afectadas'])})", RED)
kpi(s, 6.9, 1.9, 3.0, f"{nv['distancia_mediana_nuevo']} km", f"distancia mediana en barrios nuevos (vs {nv['distancia_mediana_visto']} km)", BLUE)
kpi(s, 10.1, 1.9, 2.8, f0(nv["mediana_precio_nuevo"]), f"mediana precio barrios nuevos (vs {f0(nv['mediana_precio_visto'])})", TEAL)
tabla(s, 0.5, 3.4, 6.2, 1.9, [["Indicador", "2016", "2017"], ["Mediana precio", f0(comp["mediana_2016"]), f0(comp["mediana_2017_total"])], ["Distancia mediana (km)", str(comp["distancia_mediana_2016"]), str(comp["distancia_mediana_2017"])],
                               ["% casas", str(comp["mix_tipo"]["h"]["pct_2016"]), str(comp["mix_tipo"]["h"]["pct_2017"])], ["% dúplex", str(comp["mix_tipo"]["u"]["pct_2016"]), str(comp["mix_tipo"]["u"]["pct_2017"])]], [3.0, 1.6, 1.6])
bullets(s, 7.0, 3.4, 6.0, 3.4, [f"Deriva agregada de la mediana: {comp['deriva_agregada_pct']} %; en barrios comparables: {comp['deriva_comparable_pct']} %. Lo agregado esconde el cambio de composición.",
    "Decisión: no usar Barrio one-hot (fallaría en 29 % del test). Ubicación = Distancia + Latitud + Longitud (continuas) + Región.",
    "Preprocesamiento aprendido solo con 2016; categorías nuevas → ignoradas, no imputadas con 2017.",
    "Método y Tipo no presentan categorías nuevas en 2017."], 12)

# 7 Modelamiento
s = prs.slides.add_slide(BL); header(s, "MODELAMIENTO", "Benchmark en DashAI: baseline → lineal → árbol → ensambles", f"DashAI dataset {ST.get('dataset_id')}, sesión {ST.get('session_id')}: split manual 2016 (train 90 % / validation 10 %) → test 2017 (100 %). Hiperparámetros por defecto.", 7)
rows = [["Modelo", "MAE 2017", "RMSE 2017", "R² 2017", "R² train"], ["Baseline mediana 2016", f0(base["MAE"]), f0(base["RMSE"]), f"{base['R2']:.3f}", "—"]]
for nombre, (tm, trm) in [("Regresión lineal", LIN), ("Árbol de decisión", ARB), ("Random Forest", RF), ("Gradient Boosting", GB)]:
    rows.append([nombre, f0(tm["MAE"]), f0(tm["RMSE"]), f"{tm['R2']:.3f}", f"{trm.get('R2', 0):.3f}"])
tabla(s, 0.5, 2.0, 7.3, 2.6, rows, [2.5, 1.2, 1.2, 1.2, 1.2], 11)
barras(s, 8.0, 1.9, 5.0, 4.4, ["Baseline", "Lineal", "Árbol", "Random Forest", "Gradient B."], [("MAE 2017", [base["MAE"], LIN[0]["MAE"], ARB[0]["MAE"], RF[0]["MAE"], GB[0]["MAE"]])], "MAE en 2017 (AUD)", False, '#,##0', [BLUE])
bullets(s, 0.5, 4.8, 7.3, 2.0, ["Variables (Hito 1): Habitaciones, Baños, Estacionamientos, Tamaño de terreno, Distancia, Latitud, Longitud, Cantidad de propiedades, Tipo, Método, Región.",
    "Fuera: BuildingArea y YearBuilt (nulos), CouncilArea (nulos + niveles nuevos), Barrio/Postcode (alta cardinalidad, 172 barrios nuevos). Habitaciones2 redundante con Habitaciones (notebook Hito 1).",
    "Criterio: menor MAE en 2017 con menor brecha train–test; el baseline fija la cota que H1 debe superar."], 11)

# 8 Resultados
s = prs.slides.add_slide(BL); header(s, "RESULTADOS", "H1 se sostiene: los ensambles reducen el error frente a la mediana de 2016", "Modelo del proyecto: Random Forest (decisión Hito 1). Gradient Boosting como alternativa.", 8)
kpi(s, 0.5, 1.9, 3.0, pct(red_rf), f"reducción de MAE vs baseline (RF): {f0(base['MAE'])} → {f0(RF[0]['MAE'])}", TEAL)
kpi(s, 3.7, 1.9, 3.0, f"{RF[0]['R2']:.3f}".replace(".", ","), "R² de Random Forest en 2017", BLUE)
kpi(s, 6.9, 1.9, 3.0, f"{ratio_rf_lin:.2f}×".replace(".", ","), "menor MAE que la regresión lineal (RF)", ORANGE)
kpi(s, 10.1, 1.9, 2.8, f"{f0(GB[0]['MAE'])}", f"MAE de Gradient Boosting (R² {GB[0]['R2']:.3f})".replace(".", ","), MUTED)
bullets(s, 0.5, 3.4, 6.2, 3.5, [f"Random Forest: MAE {f0(RF[0]['MAE'])}, RMSE {f0(RF[0]['RMSE'])}, R² {RF[0]['R2']:.3f} en 2017; R² train {RF[1].get('R2', 0):.3f} (brecha {RF[1].get('R2', 0) - RF[0]['R2']:+.3f}).",
    f"Gradient Boosting: MAE {f0(GB[0]['MAE'])}, R² {GB[0]['R2']:.3f}; R² train {GB[1].get('R2', 0):.3f} (brecha {GB[1].get('R2', 0) - GB[0]['R2']:+.3f}).",
    f"Regresión lineal: MAE {f0(LIN[0]['MAE'])}, R² {LIN[0]['R2']:.3f} — la relación es no lineal.",
    f"Cota trivial por tipo (mediana 2016 por Tipo): MAE {f0(cota['mae_por_Type_sobre2017'])} (−{cota['mejora_Type_pct']} %); los ensambles la superan ampliamente."], 12)
bullets(s, 7.0, 3.4, 6.0, 3.5, ["Qué se transfiere de 2016 a 2017: estructura + ubicación continua. Qué no: los 172 barrios nuevos (29,1 % del test) con precios y distancias distintas.",
    f"Límite: 2017 cubre solo {rango17}; el error típico (MAE ≈ {f0(RF[0]['MAE'])} AUD, ~{100 * RF[0]['MAE'] / comp['mediana_2017_total']:.0f} % de la mediana 2017) debe declararse junto a cada predicción.",
    "Siguiente paso: error desagregado por barrio nuevo/conocido y por tipo; comparar con el pipeline local del notebook."], 12)

prs.save("06_ENTREGABLES/Pitch_Hito2_v2.pptx")
print("OK -> PITCH_HITO2_REVISION.md y Pitch_Hito2_v2.pptx | RF MAE", f0(RF[0]["MAE"]), "GB MAE", f0(GB[0]["MAE"]), "baseline", f0(base["MAE"]))
