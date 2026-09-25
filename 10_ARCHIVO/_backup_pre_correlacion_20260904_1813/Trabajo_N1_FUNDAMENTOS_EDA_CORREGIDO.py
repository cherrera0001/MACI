# -*- coding: utf-8 -*-
"""Trabajo N°1 — Fundamentos de Ciencia de Datos
Proyecto 3 — Predicción del valor de propiedades
Hito 1 — Análisis exploratorio de datos

Versión Python sincronizada con Trabajo_N1_FUNDAMENTOS_EDA_CORREGIDO.ipynb.
No contiene modelamiento de Hito 2.
"""

# %% [markdown]
# # Trabajo N°1 — Fundamentos de Ciencia de Datos
# ## Proyecto 3 — Predicción del valor de propiedades
# ### Hito 1 — Análisis exploratorio de datos
#
# **Integrantes**
# - C. Abrigo
# - C. Herrera
# - K. Urbina
#
# > El objetivo de este notebook es comprender y caracterizar los datos antes del modelamiento, identificando patrones y problemas que permitan formular una hipótesis de investigación coherente con la predicción de 2017 a partir de 2016.
#
# **Estado de reproducibilidad de esta copia:** el archivo `housing_data.csv` no fue adjuntado durante la reconstrucción. Por esa razón, se eliminaron outputs históricos y no se fijan cifras como si hubieran sido revalidadas. El notebook queda preparado para recalcular todo desde el CSV y, si el archivo no está disponible, finaliza sus celdas sin inventar resultados.

# %% [markdown]
# ## 1. Problema del proyecto
#
# El proyecto solicita utilizar las ventas de propiedades observadas durante **2016** como información de entrenamiento para un modelo posterior y evaluar ese modelo con propiedades de **2017**. En este Hito 1 no se entrenará ningún modelo: primero se debe comprender el conjunto de datos, revisar su calidad y explorar relaciones descriptivas.
#
# **Pregunta inicial de trabajo**
#
# > ¿Qué características presentan los datos de propiedades de Melbourne y qué patrones observados permiten plantear una hipótesis razonable para predecir los precios de 2017 utilizando información de 2016?

# %% [markdown]
# ## 2. Importación de librerías

# %%
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 140)

# %% [markdown]
# ## 3. Carga del dataset
#
# Se realiza una sola carga controlada del archivo. Se buscan ubicaciones habituales de Jupyter/Colab y la misma carpeta de trabajo. Si el CSV no está presente, se informa de forma explícita y las celdas posteriores no fabrican resultados.

# %%
DATA_CANDIDATES = [
    Path("housing_data.csv"),
    Path("/content/housing_data.csv"),
    Path("/housing_data.csv"),
    Path("/mnt/data/housing_data.csv"),
]

DATA_PATH = next((p for p in DATA_CANDIDATES if p.exists()), None)
DATA_AVAILABLE = DATA_PATH is not None

if DATA_AVAILABLE:
    df = pd.read_csv(DATA_PATH)
    print(f"Dataset cargado desde: {DATA_PATH}")
    print(f"Filas: {df.shape[0]:,} | Columnas: {df.shape[1]}")
    print("\nPrimeras filas:")
    print(df.head().to_string())
    print("\nNombres de columnas:")
    print(df.columns.tolist())
    print("\nTipos de datos:")
    print(df.dtypes.to_string())
    print("\nInformación general:")
    df.info()
else:
    df = pd.DataFrame()
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES: no se encontró housing_data.csv.")

# %% [markdown]
# ## 4. Descripción del conjunto de datos
#
# Una fila representa una observación de una propiedad registrada en el conjunto de datos. La variable objetivo del proyecto es **`Price`**.
#
# Variables estructurales a revisar: `Rooms`, `Bedroom2`, `Bathroom`, `Car`, `Landsize`, `BuildingArea`, `YearBuilt`, `Type`.
#
# Variables espaciales: `Suburb`, `Distance`, `CouncilArea`, `Regionname`, `Lattitude`, `Longtitude`, `Propertycount`.
#
# Variables comerciales/contextuales: `Method`, `SellerG`, `Date`.
#
# Las cantidades exactas, los tipos y el rango temporal se obtienen desde el CSV; no se fijan aquí cifras históricas no revalidadas.

# %%
EXPECTED_COLUMNS = {
    "Suburb", "Rooms", "Address", "Price", "Type", "Method", "SellerG", "Date",
    "Distance", "Bedroom2", "Bathroom", "Car", "Landsize", "BuildingArea",
    "YearBuilt", "CouncilArea", "Lattitude", "Longtitude", "Regionname",
    "Propertycount"
}

if DATA_AVAILABLE:
    missing_columns = sorted(EXPECTED_COLUMNS.difference(df.columns))
    if missing_columns:
        raise ValueError(f"Faltan columnas esperadas en el dataset: {missing_columns}")

    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_columns = df.select_dtypes(exclude=[np.number]).columns.tolist()

    print(f"Filas: {df.shape[0]:,}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Variables numéricas ({len(numeric_columns)}): {numeric_columns}")
    print(f"Variables no numéricas ({len(categorical_columns)}): {categorical_columns}")
else:
    print("NO REVALIDADA DESDE EL CSV.")

# %% [markdown]
# ## 5. Tratamiento correcto de `Date`
#
# `Date` se interpreta como fecha con día primero. A partir de ella se crea `Year`, que permite separar 2016 y 2017 sin usar todavía `train_test_split`.

# %%
if DATA_AVAILABLE:
    date_original_non_null = df["Date"].notna().sum()
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    date_parsed_non_null = df["Date"].notna().sum()
    df["Year"] = df["Date"].dt.year

    print("Registros por año:")
    print(df["Year"].value_counts(dropna=False).sort_index().to_string())
    print(f"Fechas no nulas antes de convertir: {date_original_non_null}")
    print(f"Fechas válidas después de convertir: {date_parsed_non_null}")
    print(f"Rango temporal: {df['Date'].min()} a {df['Date'].max()}")
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** `NO REVALIDADA DESDE EL CSV` en esta entrega.
#
# **Interpretación exploratoria:** la variable `Year` será la base para comparar 2016 y 2017 una vez ejecutado el notebook con los datos reales.
#
# **Límite:** sin el CSV no corresponde afirmar cuántos registros existen en cada año ni cuál es el rango temporal efectivo.

# %% [markdown]
# ## 6. Calidad de datos

# %% [markdown]
# ### 6.1 Valores faltantes

# %%
if DATA_AVAILABLE:
    missing_table = pd.DataFrame({
        "Cantidad": df.isna().sum(),
        "Porcentaje (%)": (df.isna().sum() / len(df) * 100).round(2)
    }).sort_values(["Porcentaje (%)", "Cantidad"], ascending=False)

    print(missing_table.to_string())
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** la celda anterior cuantifica faltantes antes de cualquier imputación.
#
# **Interpretación exploratoria:** una fracción alta de datos ausentes puede reducir la información utilizable de una variable y debe considerarse antes de modelar.
#
# **Límite:** en este Hito 1 no se imputan automáticamente `BuildingArea` ni `YearBuilt`; hacerlo antes del EDA podría alterar su distribución y sus correlaciones.

# %% [markdown]
# ### 6.2 Duplicados

# %%
if DATA_AVAILABLE:
    duplicate_count = int(df.duplicated().sum())
    print(f"Filas completamente duplicadas: {duplicate_count}")
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se cuantifican duplicados completos, pero no se eliminan de manera automática.
#
# **Interpretación exploratoria:** su existencia debe revisarse antes de decidir si representan registros repetidos o eventos legítimos.
#
# **Límite:** `duplicated()` detecta igualdad completa de filas; no demuestra por sí solo que dos observaciones correspondan al mismo evento inmobiliario.

# %% [markdown]
# ### 6.3 Rangos y valores potencialmente problemáticos

# %%
RANGE_COLUMNS = ["Price", "Rooms", "Landsize", "BuildingArea", "YearBuilt", "Distance"]

if DATA_AVAILABLE:
    rows = []
    current_year = pd.Timestamp.today().year

    for col in RANGE_COLUMNS:
        s = pd.to_numeric(df[col], errors="coerce")
        row = {
            "Variable": col,
            "Mínimo": s.min(),
            "Máximo": s.max(),
            "Nulos": int(s.isna().sum()),
            "Valores < 0": int((s < 0).sum()),
            "Valores = 0": int((s == 0).sum()),
        }
        if col == "YearBuilt":
            row["Años > año actual"] = int((s > current_year).sum())
        rows.append(row)

    range_review = pd.DataFrame(rows)
    print(range_review.to_string(index=False))
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se muestran mínimos, máximos, nulos y señales básicas que merecen revisión.
#
# **Interpretación exploratoria:** valores cero, negativos o años futuros deben investigarse según el significado de cada variable; no se borran en silencio.
#
# **Límite:** un valor extremo no es automáticamente un error. Por ejemplo, un valor poco frecuente puede ser una observación válida.

# %% [markdown]
# ### 6.4 `Method` y el concepto de "venta"

# %%
if DATA_AVAILABLE:
    method_counts = df["Method"].value_counts(dropna=False)
    method_props = df["Method"].value_counts(dropna=False, normalize=True).mul(100).round(2)

    method_table = pd.DataFrame({
        "Cantidad": method_counts,
        "Porcentaje (%)": method_props
    })
    print(method_table.to_string())
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se presentan las categorías reales de `Method` y su frecuencia.
#
# **Interpretación exploratoria:** `Method` debe revisarse antes de definir operativamente qué observaciones constituyen una "venta" para el proyecto.
#
# **Límite:** no se adjuntó en esta revisión un diccionario oficial de categorías de `Method`. Por lo tanto, este notebook **no filtra** categorías ni reemplaza sus códigos por interpretaciones no verificadas.

# %% [markdown]
# ## 7. Análisis exploratorio

# %% [markdown]
# ### 7.1 Distribución de `Price`

# %%
if DATA_AVAILABLE:
    price = pd.to_numeric(df["Price"], errors="coerce").dropna()

    q1 = price.quantile(0.25)
    q3 = price.quantile(0.75)
    price_stats = pd.Series({
        "count": price.count(),
        "mínimo": price.min(),
        "máximo": price.max(),
        "media": price.mean(),
        "mediana": price.median(),
        "desviación estándar": price.std(),
        "varianza": price.var(),
        "Q1": q1,
        "Q3": q3,
        "IQR": q3 - q1,
    })

    print(price_stats.to_string())

    plt.figure(figsize=(9, 5))
    plt.hist(price, bins=50)
    plt.axvline(price.mean(), linestyle="--", label="Media")
    plt.axvline(price.median(), linestyle=":", label="Mediana")
    plt.title("Distribución de Price")
    plt.xlabel("Precio")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** `NO REVALIDADA DESDE EL CSV` en esta entrega; el histograma y las estadísticas se recalculan al ejecutar.
#
# **Interpretación exploratoria:** deben compararse media y mediana, forma del histograma e IQR para describir asimetría y valores extremos. Si media y mediana difieren de forma visible, la mediana puede ser una referencia más robusta del precio típico.
#
# **Límite:** un histograma no demuestra normalidad y la presencia de outliers no autoriza a eliminarlos.

# %% [markdown]
# ### 7.2 Distribución de `Type`

# %%
if DATA_AVAILABLE:
    type_counts = df["Type"].value_counts(dropna=False)
    type_props = df["Type"].value_counts(dropna=False, normalize=True).mul(100).round(2)
    type_table = pd.DataFrame({"Cantidad": type_counts, "Porcentaje (%)": type_props})
    print(type_table.to_string())

    type_counts.plot(kind="bar")
    plt.title("Distribución de tipos de propiedad")
    plt.xlabel("Type")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** la tabla y el gráfico muestran qué tipos de propiedad predominan.
#
# **Interpretación exploratoria:** una composición muy desigual entre categorías debe considerarse al comparar precios y, posteriormente, al evaluar el modelo.
#
# **Límite:** predominio de una categoría no implica que esa categoría explique por sí sola el precio.

# %% [markdown]
# ### 7.3 Distribución de `Method`

# %%
if DATA_AVAILABLE:
    method_counts = df["Method"].value_counts(dropna=False)
    method_props = df["Method"].value_counts(dropna=False, normalize=True).mul(100).round(2)
    print(pd.DataFrame({"Cantidad": method_counts, "Porcentaje (%)": method_props}).to_string())

    method_counts.plot(kind="bar")
    plt.title("Distribución de Method")
    plt.xlabel("Method")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se cuantifica la composición de `Method`.
#
# **Interpretación exploratoria:** esta distribución ayuda a verificar si el universo observado mezcla distintos mecanismos de transacción.
#
# **Límite:** sin la definición oficial de cada código no corresponde convertir esta distribución en un filtro de "ventas efectivas".

# %% [markdown]
# ### 7.4 `Price` vs `Rooms`

# %%
if DATA_AVAILABLE:
    rooms_price = df[["Rooms", "Price"]].apply(pd.to_numeric, errors="coerce").dropna()
    corr_rooms = rooms_price["Rooms"].corr(rooms_price["Price"])
    median_by_rooms = rooms_price.groupby("Rooms")["Price"].median().sort_index()

    print(f"Correlación Rooms-Price: {corr_rooms:.4f}")
    print("\nMediana de Price por Rooms:")
    print(median_by_rooms.to_string())

    plt.figure(figsize=(8, 5))
    plt.scatter(rooms_price["Rooms"], rooms_price["Price"], alpha=0.35)
    plt.title("Price vs Rooms")
    plt.xlabel("Número de habitaciones")
    plt.ylabel("Precio")
    plt.tight_layout()
    plt.show()
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se calcula una correlación lineal y medianas de precio por cantidad de habitaciones.
#
# **Interpretación exploratoria:** una relación consistente sugeriría asociación entre tamaño estructural aproximado y precio.
#
# **Límite:** correlación y diferencias de mediana describen asociación; no prueban que aumentar habitaciones cause un aumento de precio.

# %% [markdown]
# ### 7.5 `Price` vs `Type`

# %%
if DATA_AVAILABLE:
    type_price = df[["Type", "Price"]].copy()
    type_price["Price"] = pd.to_numeric(type_price["Price"], errors="coerce")
    type_price = type_price.dropna()

    summary_type_price = type_price.groupby("Type")["Price"].agg(["count", "median"]).sort_values("median", ascending=False)
    print(summary_type_price.to_string())

    plt.figure(figsize=(9, 5))
    type_price.boxplot(column="Price", by="Type", grid=False)
    plt.title("Distribución de Price por Type")
    plt.suptitle("")
    plt.xlabel("Type")
    plt.ylabel("Precio")
    plt.tight_layout()
    plt.show()
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se comparan cantidad de observaciones, mediana y distribución de precios entre tipos.
#
# **Interpretación exploratoria:** diferencias persistentes entre cajas y medianas pueden indicar que `Type` contiene información útil asociada a `Price`.
#
# **Límite:** los outliers no resumen el comportamiento de una categoría y las diferencias observadas pueden coexistir con otros factores locacionales o estructurales.

# %% [markdown]
# ### 7.6 `Price` vs `Distance`

# %%
if DATA_AVAILABLE:
    distance_price = df[["Distance", "Price"]].apply(pd.to_numeric, errors="coerce").dropna()
    corr_distance = distance_price["Distance"].corr(distance_price["Price"])
    print(f"Correlación Distance-Price: {corr_distance:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(distance_price["Distance"], distance_price["Price"], alpha=0.35)
    plt.title("Price vs Distance")
    plt.xlabel("Distance")
    plt.ylabel("Precio")
    plt.tight_layout()
    plt.show()
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se calcula la asociación lineal entre `Distance` y `Price` y se inspecciona su dispersión.
#
# **Interpretación exploratoria:** el signo y magnitud de la correlación ayudan a evaluar si la variable locacional merece atención en el modelamiento posterior.
#
# **Límite:** no se puede afirmar que la distancia produzca por sí misma un cambio en el precio.

# %% [markdown]
# ### 7.7 `Price` vs `BuildingArea`

# %%
if DATA_AVAILABLE:
    building_missing = int(df["BuildingArea"].isna().sum())
    building_missing_pct = building_missing / len(df) * 100
    print(f"Nulos en BuildingArea: {building_missing} ({building_missing_pct:.2f}%)")

    building_price = df[["BuildingArea", "Price"]].apply(pd.to_numeric, errors="coerce").dropna()
    corr_building = building_price["BuildingArea"].corr(building_price["Price"])
    print(f"Pares válidos para el análisis: {len(building_price)}")
    print(f"Correlación BuildingArea-Price sobre pares válidos: {corr_building:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(building_price["BuildingArea"], building_price["Price"], alpha=0.35)
    plt.title("Price vs BuildingArea")
    plt.xlabel("Área de construcción")
    plt.ylabel("Precio")
    plt.tight_layout()
    plt.show()
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** primero se cuantifican los faltantes y luego se analiza únicamente la información válida.
#
# **Interpretación exploratoria:** si aparece una asociación, esta debe interpretarse considerando cuánto dato efectivo existe en `BuildingArea`.
#
# **Límite:** no se imputa la mediana antes del gráfico ni de la correlación, porque eso introduciría valores artificiales y podría modificar la relación observada.

# %% [markdown]
# ### 7.8 `YearBuilt`

# %%
if DATA_AVAILABLE:
    year_built = pd.to_numeric(df["YearBuilt"], errors="coerce")
    yearbuilt_summary = pd.Series({
        "mínimo": year_built.min(),
        "máximo": year_built.max(),
        "nulos": year_built.isna().sum(),
        "porcentaje nulo": year_built.isna().mean() * 100,
        "años <= 0": (year_built <= 0).sum(),
        "años futuros": (year_built > pd.Timestamp.today().year).sum(),
    })
    print(yearbuilt_summary.to_string())
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se revisan rango, nulos y valores potencialmente imposibles antes de derivar una variable de antigüedad.
#
# **Interpretación exploratoria:** `YearBuilt` puede ser útil, pero su calidad debe comprobarse antes de transformarlo o imputarlo.
#
# **Límite:** en este Hito no se crea automáticamente "antigüedad" ni se corrigen años sin evidencia.

# %% [markdown]
# ## 8. Comparación 2016 vs 2017

# %%
if DATA_AVAILABLE:
    df_2016 = df[df["Year"] == 2016].copy()
    df_2017 = df[df["Year"] == 2017].copy()

    comparison = pd.DataFrame({
        "2016": {
            "Registros": len(df_2016),
            "Mediana Price": pd.to_numeric(df_2016["Price"], errors="coerce").median(),
            "Mediana Distance": pd.to_numeric(df_2016["Distance"], errors="coerce").median(),
            "Suburb distintos": df_2016["Suburb"].nunique(dropna=True),
        },
        "2017": {
            "Registros": len(df_2017),
            "Mediana Price": pd.to_numeric(df_2017["Price"], errors="coerce").median(),
            "Mediana Distance": pd.to_numeric(df_2017["Distance"], errors="coerce").median(),
            "Suburb distintos": df_2017["Suburb"].nunique(dropna=True),
        }
    })
    print("Resumen comparativo:")
    print(comparison.to_string())

    print("\nComposición de Type por año (%):")
    type_year = pd.crosstab(df["Type"], df["Year"], normalize="columns").mul(100).round(2)
    print(type_year.to_string())

    suburbs_2016 = set(df_2016["Suburb"].dropna().unique())
    suburbs_2017 = set(df_2017["Suburb"].dropna().unique())
    new_suburbs_2017 = sorted(suburbs_2017 - suburbs_2016)

    print(f"\nSuburb presentes en 2017 y ausentes en 2016: {len(new_suburbs_2017)}")
    if len(new_suburbs_2017) <= 30:
        print(new_suburbs_2017)
    else:
        print(new_suburbs_2017[:30], "...")

    for col in ["Type", "Method"]:
        values_2016 = set(df_2016[col].dropna().unique())
        values_2017 = set(df_2017[col].dropna().unique())
        new_values = sorted(values_2017 - values_2016)
        print(f"Categorías nuevas de {col} en 2017 respecto de 2016: {new_values}")

    price_2016 = pd.to_numeric(df_2016["Price"], errors="coerce").dropna()
    price_2017 = pd.to_numeric(df_2017["Price"], errors="coerce").dropna()

    if len(price_2016) and len(price_2017):
        plt.figure(figsize=(9, 5))
        plt.hist(price_2016, bins=40, alpha=0.5, label="2016")
        plt.hist(price_2017, bins=40, alpha=0.5, label="2017")
        plt.title("Distribución de Price: 2016 vs 2017")
        plt.xlabel("Precio")
        plt.ylabel("Frecuencia")
        plt.legend()
        plt.tight_layout()
        plt.show()
else:
    df_2016 = pd.DataFrame()
    df_2017 = pd.DataFrame()
    new_suburbs_2017 = []
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Pregunta de esta sección:** ¿2017 presenta exactamente la misma composición que los datos disponibles en 2016?
#
# **Resultado observado:** `NO REVALIDADA DESDE EL CSV` en esta entrega. La celda calcula registros, mediana de precio, distancia, composición de `Type`, cobertura de `Suburb` y categorías nuevas.
#
# **Interpretación exploratoria:** cualquier diferencia descriptiva entre años es relevante para comprender el desafío de evaluar en 2017 un modelo construido con 2016.
#
# **Límite:** una diferencia de composición no constituye por sí sola una explicación causal ni implica necesariamente que el modelo vaya a fallar.

# %% [markdown]
# ## 9. Matriz de correlación

# %%
def describe_correlation(r):
    if pd.isna(r):
        return "No calculable"
    magnitude = abs(r)
    if magnitude < 0.20:
        level = "muy débil"
    elif magnitude < 0.40:
        level = "débil"
    elif magnitude < 0.60:
        level = "moderada"
    elif magnitude < 0.80:
        level = "fuerte"
    else:
        level = "muy fuerte"
    direction = "positiva" if r > 0 else "negativa" if r < 0 else "nula"
    return f"{direction}, {level}"

if DATA_AVAILABLE:
    numeric_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_df.corr()

    print("Matriz de correlación numérica:")
    print(correlation_matrix.round(3).to_string())

    if "Price" in correlation_matrix.columns:
        price_correlations = (
            correlation_matrix["Price"]
            .drop(labels=["Price"], errors="ignore")
            .dropna()
            .sort_values(key=lambda s: s.abs(), ascending=False)
        )
        correlation_table = pd.DataFrame({
            "Variable": price_correlations.index,
            "Correlación con Price": price_correlations.values,
            "Interpretación exploratoria": [describe_correlation(r) for r in price_correlations.values],
        })
        print("\nCorrelaciones específicas con Price:")
        print(correlation_table.to_string(index=False))

        if {"Rooms", "Bedroom2"}.issubset(correlation_matrix.columns):
            print(f"\nCorrelación Rooms-Bedroom2: {correlation_matrix.loc['Rooms', 'Bedroom2']:.4f}")
else:
    print("NO VERIFICABLE CON LOS DATOS DISPONIBLES.")

# %% [markdown]
# **Resultado observado:** se priorizan las correlaciones de variables numéricas con `Price` en lugar de interpretar una matriz completa sin foco.
#
# **Interpretación exploratoria:** magnitudes altas pueden señalar variables descriptivamente relacionadas con el precio; una correlación alta entre dos explicativas, como `Rooms` y `Bedroom2`, puede sugerir redundancia.
#
# **Límite:** correlación lineal no equivale a causalidad y una correlación cercana a cero no descarta relaciones no lineales.

# %% [markdown]
# ## 10. De los datos a la hipótesis
#
# Esta sección debe leerse únicamente junto con los outputs reproducidos desde `housing_data.csv`.
#
# ### Evidencia A — `Price`
# Revisar forma de la distribución, diferencia entre media y mediana, dispersión, IQR y valores extremos.
#
# ### Evidencia B — variables asociadas con `Price`
# Revisar las relaciones de `Rooms`, `BuildingArea`, `Distance` y las demás variables numéricas calculadas en la tabla de correlaciones.
#
# ### Evidencia C — diferencias por tipo de propiedad
# Revisar medianas, cantidades y boxplots de `Price` según `Type`.
#
# ### Evidencia D — componente locacional
# Revisar `Distance`, cobertura de `Suburb` y otras variables espaciales disponibles, sin atribuir causalidad.
#
# ### Evidencia E — composición 2016 vs 2017
# Revisar diferencias de registros, precio, `Type`, distancia, cobertura de suburbios y categorías nuevas.
#
# **Estado de esta reconstrucción:** los apartados anteriores quedan calculables, pero sus cifras son `NO REVALIDADAS DESDE EL CSV` hasta ejecutar este notebook con el archivo real.

# %% [markdown]
# ## 11. Pregunta de investigación
#
# Si los resultados reproducidos respaldan las asociaciones exploradas, la pregunta principal queda formulada así:
#
# > **¿En qué medida las características estructurales y locacionales observadas en las ventas de propiedades de Melbourne durante 2016 permiten sustentar la construcción de un modelo capaz de predecir el precio de las propiedades de 2017?**
#
# La formulación es predictiva y descriptiva, no causal.

# %% [markdown]
# ## 12. Hipótesis exploratoria
#
# **Hipótesis principal propuesta, condicionada a que el EDA reproducido confirme asociaciones relevantes:**
#
# > **Las características estructurales y locacionales disponibles contienen información asociada al precio de las propiedades, por lo que un modelo entrenado con las ventas de 2016 debería ser capaz de mejorar una predicción basal al ser evaluado sobre las propiedades de 2017.**
#
# ### H0
# > Las relaciones observadas en los datos de 2016 no permitirán mejorar de manera relevante una predicción basal aplicada a 2017.
#
# ### H1
# > Las relaciones observadas entre los atributos y `Price` en 2016 permitirán construir un modelo que supere una predicción basal sobre 2017.
#
# En este Hito 1 **no se evalúan H0/H1 mediante machine learning**.

# %% [markdown]
# ## 13. Hipótesis secundaria, solo si el EDA la respalda
#
# Si la comparación reproducida demuestra que una parte relevante de 2017 corresponde a suburbios ausentes en 2016, puede plantearse:
#
# > **El desempeño predictivo podría ser menos estable en propiedades ubicadas en suburbios no representados durante 2016.**
#
# Esta afirmación se mantiene como hipótesis derivada del EDA y no como conclusión mientras no se evalúe en el Hito 2.

# %% [markdown]
# ## 14. Decisión sobre imputación
#
# No se imputan automáticamente `BuildingArea` ni `YearBuilt` en el DataFrame principal.
#
# Una imputación masiva con la mediana puede:
# - reducir artificialmente la variabilidad;
# - introducir numerosos valores idénticos;
# - modificar correlaciones;
# - ocultar el patrón real de ausencia.
#
# En Hito 1 se prioriza **describir y cuantificar** el problema. Cualquier imputación del Hito 2 deberá justificarse y evaluarse dentro del proceso de modelamiento, sin contaminar el análisis exploratorio original.

# %% [markdown]
# ## 15. Limitaciones
#
# - Existen valores faltantes que deben cuantificarse por variable.
# - `BuildingArea` y `YearBuilt` requieren atención particular antes de imputar o transformar.
# - Los outliers deben revisarse, no eliminarse por conveniencia gráfica.
# - La interpretación de `Method` depende del diccionario oficial del proyecto; en esta reconstrucción no fue adjuntado.
# - La composición de 2016 y 2017 puede diferir y debe comprobarse descriptivamente.
# - La cobertura geográfica puede variar entre años.
# - El dataset no contiene necesariamente todos los factores que influyen en el mercado inmobiliario.
# - Asociación y correlación no implican causalidad.
# - Si el rango de 2017 no cubre doce meses completos, ese año no debe describirse como un año calendario completo sin verificarlo.
# - En esta entrega de reconstrucción no se adjuntó `housing_data.csv`; por tanto, las cifras deben ser recalculadas antes de presentarlas como evidencia.

# %% [markdown]
# ## 16. Conclusiones exploratorias
#
# El valor de este Hito 1 está en establecer un flujo reproducible: primero se identifica el problema, luego se comprueba la estructura y calidad del dataset, se estudian las variables relevantes, se compara 2016 con 2017 y finalmente se formula una hipótesis que pueda ponerse a prueba más adelante.
#
# **No se incorporan conclusiones numéricas no revalidadas.** Al ejecutar con el CSV real, los resultados visibles de las celdas anteriores constituyen la evidencia que debe utilizarse en la presentación oral.

# %% [markdown]
# ## 17. Conexión con Hito 2
#
# > El Hito 1 permite comprender los datos y formular la hipótesis. En el Hito 2 se deberá construir un modelo usando 2016 y evaluar objetivamente su desempeño sobre 2017.
#
# El paso siguiente será comparar el desempeño del modelo contra una **referencia basal simple**, manteniendo 2017 como período de evaluación. Ese modelamiento no se implementa en este notebook.
