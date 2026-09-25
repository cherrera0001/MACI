import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. CARGAR DATOS
# ============================================================================
csv_path = r"F:\MACI\08_PROYECTO_FCD\Hito1\Corrección\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
df = pd.read_csv(csv_path)

# Limpiar datos básicos
df = df.dropna(subset=['Price'])
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df = df.dropna(subset=['Price'])

print("Creando visualizaciones...")

# ============================================================================
# 2. VISUALIZACIÓN 1: DISTRIBUCIÓN DE PRECIOS
# ============================================================================
fig1 = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Histograma de Precios", "Box Plot de Precios")
)

fig1.add_trace(
    go.Histogram(x=df['Price'], name='Distribución', nbinsx=50,
                 marker_color='#2E86AB'),
    row=1, col=1
)

fig1.add_trace(
    go.Box(y=df['Price'], name='Box Plot', marker_color='#A23B72'),
    row=1, col=2
)

fig1.update_xaxes(title_text="Precio (AUD)", row=1, col=1)
fig1.update_xaxes(title_text="", row=1, col=2)
fig1.update_yaxes(title_text="Frecuencia", row=1, col=1)
fig1.update_yaxes(title_text="Precio (AUD)", row=1, col=2)
fig1.update_layout(
    title="DISTRIBUCIÓN DE PRECIOS DE PROPIEDADES EN MELBOURNE",
    height=500,
    showlegend=False,
    hovermode='x unified'
)
fig1.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_1_price_distribution.html")
print("✓ viz_1_price_distribution.html")

# ============================================================================
# 3. VISUALIZACIÓN 2: PRECIOS POR TIPO DE PROPIEDAD
# ============================================================================
type_price = df.groupby('Type')['Price'].agg(['mean', 'median', 'count']).reset_index()
type_price = type_price.sort_values('mean', ascending=False)

fig2 = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "bar"}, {"type": "box"}]],
    subplot_titles=("Precio Promedio por Tipo", "Distribución de Precios")
)

fig2.add_trace(
    go.Bar(x=type_price['Type'], y=type_price['mean'], name='Precio Promedio',
           marker_color=['#F18F01', '#2E86AB', '#A23B72']),
    row=1, col=1
)

for ptype in df['Type'].unique():
    fig2.add_trace(
        go.Box(y=df[df['Type']==ptype]['Price'], name=ptype,
               marker_color={'h': '#F18F01', 'u': '#2E86AB', 't': '#A23B72'}.get(ptype, '#666')),
        row=1, col=2
    )

fig2.update_xaxes(title_text="Tipo de Propiedad (h=house, u=unit, t=townhouse)", row=1, col=1)
fig2.update_xaxes(title_text="Tipo", row=1, col=2)
fig2.update_yaxes(title_text="Precio (AUD)", row=1, col=1)
fig2.update_yaxes(title_text="Precio (AUD)", row=1, col=2)
fig2.update_layout(
    title="PRECIOS POR TIPO DE PROPIEDAD",
    height=500,
    hovermode='x unified'
)
fig2.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_2_price_by_type.html")
print("✓ viz_2_price_by_type.html")

# ============================================================================
# 4. VISUALIZACIÓN 3: PRECIOS POR REGIÓN
# ============================================================================
region_price = df.groupby('Regionname')['Price'].agg(['mean', 'median', 'count']).reset_index()
region_price = region_price.dropna().sort_values('mean', ascending=False)

fig3 = go.Figure()
fig3.add_trace(
    go.Bar(
        x=region_price['Regionname'],
        y=region_price['mean'],
        marker_color=['#F18F01', '#2E86AB', '#A23B72', '#F18F01'],
        text=[f"${v:,.0f}" for v in region_price['mean']],
        textposition='outside',
        name='Precio Promedio'
    )
)

fig3.update_layout(
    title="PRECIO PROMEDIO POR REGIÓN",
    xaxis_title="Región",
    yaxis_title="Precio Promedio (AUD)",
    height=500,
    hovermode='x unified',
    showlegend=False
)
fig3.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_3_price_by_region.html")
print("✓ viz_3_price_by_region.html")

# ============================================================================
# 5. VISUALIZACIÓN 4: CORRELACIÓN DISTANCIA vs PRECIO
# ============================================================================
df_clean = df.dropna(subset=['Distance'])

fig4 = px.scatter(
    df_clean, x='Distance', y='Price',
    color='Rooms',
    size='Rooms',
    hover_data=['Rooms', 'Type', 'Regionname'],
    title="DISTANCIA AL CBD vs PRECIO",
    labels={'Distance': 'Distancia al CBD (km)', 'Price': 'Precio (AUD)', 'Rooms': 'Cuartos'},
    color_continuous_scale='Viridis'
)

fig4.add_trace(
    go.Scatter(
        x=df_clean.groupby('Distance')['Price'].mean().index,
        y=df_clean.groupby('Distance')['Price'].mean().values,
        mode='lines',
        name='Tendencia (promedio)',
        line=dict(color='red', width=3),
        hoverinfo='skip'
    )
)

fig4.update_layout(height=600, hovermode='closest')
fig4.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_4_distance_vs_price.html")
print("✓ viz_4_distance_vs_price.html")

# ============================================================================
# 6. VISUALIZACIÓN 5: CUARTOS vs PRECIO
# ============================================================================
rooms_price = df.groupby('Rooms')['Price'].agg(['mean', 'count']).reset_index()
rooms_price = rooms_price[rooms_price['count'] > 20].sort_values('Rooms')

fig5 = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "scatter"}, {"type": "bar"}]],
    subplot_titles=("Tendencia de Precio", "Cantidad de Propiedades")
)

fig5.add_trace(
    go.Scatter(
        x=rooms_price['Rooms'],
        y=rooms_price['mean'],
        mode='lines+markers',
        name='Precio Promedio',
        marker=dict(size=10, color='#F18F01'),
        line=dict(width=3)
    ),
    row=1, col=1
)

fig5.add_trace(
    go.Bar(
        x=rooms_price['Rooms'],
        y=rooms_price['count'],
        name='Cantidad',
        marker_color='#2E86AB'
    ),
    row=1, col=2
)

fig5.update_xaxes(title_text="Número de Cuartos", row=1, col=1)
fig5.update_xaxes(title_text="Número de Cuartos", row=1, col=2)
fig5.update_yaxes(title_text="Precio Promedio (AUD)", row=1, col=1)
fig5.update_yaxes(title_text="Cantidad de Propiedades", row=1, col=2)
fig5.update_layout(
    title="RELACIÓN ENTRE CUARTOS Y PRECIO",
    height=500,
    hovermode='x unified'
)
fig5.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_5_rooms_vs_price.html")
print("✓ viz_5_rooms_vs_price.html")

# ============================================================================
# 7. VISUALIZACIÓN 6: MAPA GEOGRÁFICO DE PRECIOS
# ============================================================================
df_geo = df.dropna(subset=['Lattitude', 'Longtitude', 'Price'])
df_geo['Price_log'] = np.log10(df_geo['Price'])

fig6 = px.scatter_map(
    df_geo,
    lat='Lattitude',
    lon='Longtitude',
    color='Price',
    size='Rooms',
    hover_data=['Suburb', 'Price', 'Rooms', 'Type'],
    title="MAPA DE PRECIOS DE PROPIEDADES EN MELBOURNE",
    color_continuous_scale='Viridis',
    zoom=10,
    center=dict(lat=-37.8, lon=145.0)
)

fig6.update_layout(
    map_style='open-street-map',
    height=700,
    hovermode='closest'
)
fig6.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_6_price_map.html")
print("✓ viz_6_price_map.html")

# ============================================================================
# 8. VISUALIZACIÓN 7: AÑO CONSTRUIDO vs PRECIO
# ============================================================================
df_year = df.dropna(subset=['YearBuilt', 'Price'])
df_year = df_year[(df_year['YearBuilt'] >= 1800) & (df_year['YearBuilt'] <= 2020)]

year_price = df_year.groupby('YearBuilt')['Price'].agg(['mean', 'count']).reset_index()
year_price = year_price[year_price['count'] >= 5]

fig7 = go.Figure()

fig7.add_trace(
    go.Scatter(
        x=year_price['YearBuilt'],
        y=year_price['mean'],
        mode='lines+markers',
        name='Precio Promedio',
        line=dict(color='#F18F01', width=3),
        marker=dict(size=5)
    )
)

fig7.update_layout(
    title="PRECIO POR AÑO DE CONSTRUCCIÓN",
    xaxis_title="Año de Construcción",
    yaxis_title="Precio Promedio (AUD)",
    height=500,
    hovermode='x unified'
)
fig7.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_7_year_vs_price.html")
print("✓ viz_7_year_vs_price.html")

# ============================================================================
# 9. VISUALIZACIÓN 8: MÉTODO DE VENTA
# ============================================================================
method_price = df.groupby('Method')['Price'].agg(['mean', 'median', 'count']).reset_index()
method_price = method_price.dropna().sort_values('mean', ascending=False)

fig8 = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "bar"}, {"type": "bar"}]],
    subplot_titles=("Precio Promedio", "Cantidad de Ventas")
)

fig8.add_trace(
    go.Bar(
        x=method_price['Method'],
        y=method_price['mean'],
        marker_color='#2E86AB',
        name='Precio Promedio',
        text=[f"${v:,.0f}" for v in method_price['mean']],
        textposition='outside'
    ),
    row=1, col=1
)

fig8.add_trace(
    go.Bar(
        x=method_price['Method'],
        y=method_price['count'],
        marker_color='#A23B72',
        name='Cantidad'
    ),
    row=1, col=2
)

fig8.update_xaxes(title_text="Método de Venta", row=1, col=1)
fig8.update_xaxes(title_text="Método de Venta", row=1, col=2)
fig8.update_yaxes(title_text="Precio Promedio (AUD)", row=1, col=1)
fig8.update_yaxes(title_text="Cantidad", row=1, col=2)
fig8.update_layout(
    title="ANÁLISIS POR MÉTODO DE VENTA (S=Sale, PI=Private Sale, VB=Vendor Bid, SP=Sold Prior)",
    height=500,
    showlegend=False
)
fig8.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_8_method.html")
print("✓ viz_8_method.html")

# ============================================================================
# 10. VISUALIZACIÓN 9: MATRIZ DE CORRELACIÓN
# ============================================================================
# Método del explorador de DashAI (dataset 22): solo las 8 columnas que DashAI tipó numéricas (Bedroom2/Bathroom/Car
# NO entran: DashAI las tipó categóricas), todas las filas, sin dropna() global; nulos de BuildingArea/YearBuilt ->
# media sin outliers (cercas de Tukey). Bloque canónico y autoverificación: F:\MACI\correlacion_dashai.py
from correlacion_dashai import matriz_dashai, verificar, COLS_DASHAI
corr_data, _ = matriz_dashai(df, COLS_DASHAI)
verificar(corr_data)

fig9 = go.Figure(data=go.Heatmap(
    z=corr_data.values,
    x=corr_data.columns,
    y=corr_data.columns,
    colorscale='RdBu',
    zmid=0,
    text=np.round(corr_data.values, 2),
    texttemplate='%{text}',
    textfont={"size": 10},
    colorbar=dict(title="Correlación")
))

fig9.update_layout(
    title="MATRIZ DE CORRELACIÓN PEARSON — 8 numéricas, método explorador DashAI (dataset 22)",
    height=600,
    width=700
)
fig9.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_9_correlation.html")
print("✓ viz_9_correlation.html")

# ============================================================================
# 11. VISUALIZACIÓN 10: RESUMEN ESTADÍSTICO
# ============================================================================
summary_stats = {
    'Total de Propiedades': len(df),
    'Precio Promedio': f"${df['Price'].mean():,.0f}",
    'Precio Mediano': f"${df['Price'].median():,.0f}",
    'Precio Mín': f"${df['Price'].min():,.0f}",
    'Precio Máx': f"${df['Price'].max():,.0f}",
    'Cuartos Promedio': f"{df['Rooms'].mean():.1f}",
    'Distancia Promedio': f"{df['Distance'].dropna().mean():.1f} km",
    'Regiones Únicas': df['Regionname'].nunique(),
    'Suburbios Únicos': df['Suburb'].nunique()
}

fig10 = go.Figure(data=[go.Table(
    header=dict(values=['Métrica', 'Valor'],
                fill_color='#2E86AB',
                align='left',
                font=dict(color='white', size=12)),
    cells=dict(values=[list(summary_stats.keys()), list(summary_stats.values())],
               fill_color='#F0F0F0',
               align='left',
               font=dict(size=11))
)])

fig10.update_layout(
    title="RESUMEN ESTADÍSTICO DEL DATASET",
    height=500,
    width=600
)
fig10.write_html("F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_10_summary.html")
print("✓ viz_10_summary.html")

print("\n" + "="*80)
print("✓ TODAS LAS VISUALIZACIONES CREADAS EXITOSAMENTE")
print("="*80)
print("\nArchivos generados:")
print("  1. viz_1_price_distribution.html - Distribución de precios")
print("  2. viz_2_price_by_type.html - Precios por tipo de propiedad")
print("  3. viz_3_price_by_region.html - Precios por región")
print("  4. viz_4_distance_vs_price.html - Distancia vs Precio")
print("  5. viz_5_rooms_vs_price.html - Cuartos vs Precio")
print("  6. viz_6_price_map.html - Mapa geográfico de precios")
print("  7. viz_7_year_vs_price.html - Año construcción vs Precio")
print("  8. viz_8_method.html - Análisis por método de venta")
print("  9. viz_9_correlation.html - Matriz de correlación")
print("  10. viz_10_summary.html - Resumen estadístico")
