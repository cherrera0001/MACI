# Revisión del pitch Hito 2 (Pitch_Hito2_Prediccion_Propiedades_Melbourne.pdf)

Generado el 2026-09-04 por `generar_pitch_v2.py`. Fuentes: `anclaje.json`, `correlacion_dashai.json` (explorador DashAI dataset 22), `dashai_resultados.json` (DashAI dataset 24, sesión 8, split manual 2016/2017, variables Hito 1). Ninguna cifra a mano.

| Lámina | Afirmación del pitch | Fuente de verdad | Veredicto | Acción |
|---|---|---|---|---|
| 2 · Problema | Train 6.336 / Test 7.244 | 6.336 / 7.244 (anclaje.particion) | **OK** |  |
| 3 · Datos | 13.580 ventas · 21 atributos | 13.580 × 21 (anclaje.procedencia) | **OK** |  |
| 4 · Calidad | 97,2 % de los nulos en BuildingArea/YearBuilt/CouncilArea | 99,5 % de 13.256 celdas nulas (anclaje.ausencias) | **CORREGIR** | Usar 99,5 %. |
| 4 · Calidad | BuildingArea 47,5 % · YearBuilt 39,6 % · CouncilArea 10,1 % · Car 0,5 % | BuildingArea 47,5 % · YearBuilt 39,6 % · CouncilArea 10,1 % · Car 0,5 % | **OK** |  |
| 4 · Calidad | Zeros: 1.939 Landsize, 17 BuildingArea, 6 Distance | 1.939 / 17 / 6 (anclaje.plausibilidad) | **OK** |  |
| 4 · Calidad | Rango temporal: 2016 (ene–dic) y 2017 (ene–sep) | ene–dic 2016 (sin mar); feb–sep 2017 (hasta 2017-09-23) (anclaje.particion) | **CORREGIR** | 2017 no tiene enero; 2016 no tiene marzo. |
| 4 · Calidad | «los atributos espaciales anteriores no influyen en los precios por la falta de datos» | YearBuilt–Price = -0.262 es la 2.ª |r| (DashAI). No son «espaciales». | **CORREGIR** | Se excluyen POR NULOS, no por falta de señal. |
| 5 · EDA | Correlaciones: Rooms .497, Bedroom2 .476, Bathroom .467, YearBuilt −.324, Car .239, Distance −.163 | Explorador DashAI (8 numéricas): Rooms +0.497 · YearBuilt -0.262 · Lattitude -0.213 · Longtitude +0.204 · Distance -0.163 · BuildingArea +0.070 · Landsize +0.038 | **CORREGIR** | Bedroom2/Bathroom/Car no están en el heatmap DashAI; YearBuilt es −0,262. |
| 5 · EDA | «ubicación (menor impacto)» / «la distancia tiene menor impacto» | Lattitude -0.213, Longtitude +0.204, Distance -0.163 > BuildingArea +0.070, Landsize +0.038 | **CORREGIR** | La ubicación NO es la de menor impacto en la matriz DashAI. |
| 5 · EDA | Mediana por habitaciones: 6→1,80M, 8→1,66M, 10→0,85M (eje sin 5 ni 7) | 1→385.000 (n=681) · 2→690.000 (n=3648) · 3→950.000 (n=5881) · 4→1.285.000 (n=2688) · 5→1.660.000 (n=596) · 6→1.800.000 (n=67) · 7→1.496.000 (n=10) · 8→1.515.000 (n=8) · 10→900.000 (n=1) | **CORREGIR** | 1,66M es 5 hab.; 8 hab. = 1,515M; 10 hab. = 0,90M con n=1. Mostrar 1–5 y agrupar 6+. |
| 5 · EDA | Mediana por tipo: casa 1,08M · casa pareada 0,85M · dúplex 0,56M | h: 1.080.000 (n=9.449) · t: 846.750 (n=1.114) · u: 560.000 (n=3.017) | **OK** |  |
| 5 · EDA | Rooms–Bedroom2 = 0,944 | No está en el heatmap DashAI (Bedroom2 categórica). Es decisión de modelo (b) del Hito 1. | **REUBICAR** | Llevar a la lámina de modelamiento como justificación de exclusión, citando notebook, no DashAI. |
| 6 · Antes de modelar | 172 barrios nuevos | 172 barrios = 2.109 filas (29,1 % de 2017); mediana visto 999.000 vs nuevo 755.000; distancia mediana 8.0 vs 17.9 km | **OK (ampliar)** | Falta el impacto: 29,1 % de 2017 y precios/distancias distintos. |
| 7 · Benchmark | Baseline MAE 2017 = 421.620 | 431.649 (anclaje.cota.mae_const2016_sobre2017); la lámina 8 dice 431.648 | **CORREGIR** | Inconsistencia interna entre láminas 7 y 8. |
| 7 · Benchmark | Lineal 294.888 / Árbol 274.625 / RF 220.771 / GB 216.040 (MAE 2017) | DashAI (split manual 2016/2017, variables Hito 1): Lineal 297.317 / Árbol 286.088 / RF 218.986 / GB 212.760 | **REEMPLAZAR** | Sin fuente trazable; usar los runs de DashAI (sesión 8). |
| 7 · Benchmark | «MAE CV (2016)» por modelo | No existe en DashAI ni en anclaje. | **ELIMINAR** | No citar cifras sin fuente. |
| 8 · Resultados | R² optimizado 0,7234 · MAE final $210.104 · RF $220.778 | DashAI: RF MAE 218.986 / R² 0.683; GB MAE 212.760 / R² 0.710. Tres cifras distintas de GB en el pitch (216.040 / 210.104 / R² 0,71 vs 0,7234). | **REEMPLAZAR** |  |
| 8 · Resultados | 1,8× mejora vs regresión lineal | 294.888/210.104 = 1,40× (aritmética del propio pitch); con DashAI RF: 1.36× | **CORREGIR** |  |
| 8 · Resultados | 51,3 % reducción MAE vs baseline | 1 − 210.104/431.648 = 51,3 % ✓ aritmética; con DashAI: RF 49,3 %, GB 50,7 % | **REEMPLAZAR** |  |
| 8 · Resultados | «Gradient Boosting es el mejor modelo» | Decisión Hito 1 = Random Forest (no se corona GB). DashAI: ver tabla. | **CORREGIR** | Mantener RF como modelo del proyecto; reportar GB como alternativa. |
| 8 · Resultados | «El patrón del 2016 se transfiere de forma consistente al 2017» | 29,1 % de 2017 en barrios nuevos; deriva mediana agregada 1.11 % pero 11.0 % en barrios comparables | **MATIZAR** | Decir qué se transfiere y qué no. |

## Benchmark oficial (DashAI, test = 2017; baseline = anclaje)

| Modelo | MAE 2017 | RMSE 2017 | R² 2017 | R² train 2016 |
|---|---:|---:|---:|---:|
| Baseline mediana 2016 | 431.649 | 654.393 | -0.080 | — |
| Regresión lineal | 297.317 | 457.460 | 0.472 | 0.626 |
| Árbol de decisión | 286.088 | 466.126 | 0.452 | 1.000 |
| Random Forest | 218.986 | 354.664 | 0.683 | 0.973 |
| Gradient Boosting | 212.760 | 338.848 | 0.710 | 0.821 |

Hiperparámetros por defecto de DashAI; validation = 10 % de 2016 (exigido por DashAI), train = 90 % de 2016, test = 100 % de 2017. Nota: `datos.mediana_precio_por_Rooms` y `mediana_precio_por_Type` se agregaron a anclaje.py en esta revisión para anclar las cifras del deck.