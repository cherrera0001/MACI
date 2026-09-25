import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. CARGAR DATOS
# ============================================================================
csv_path = r"F:\MACI\Fundamentos de ciencia de datos\Hito1\Corrección\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
df = pd.read_csv(csv_path)

print("="*80)
print("ANÁLISIS EXPLORATORIO DE DATOS - HOUSING MELBOURNE")
print("="*80)

# ============================================================================
# 2. INFORMACIÓN GENERAL DEL DATASET
# ============================================================================
print("\n1. INFORMACIÓN GENERAL")
print(f"   - Filas: {df.shape[0]}")
print(f"   - Columnas: {df.shape[1]}")
print(f"   - Rango de fechas: {df['Date'].min()} a {df['Date'].max()}")
print(f"\nColumnas del dataset:")
print(df.columns.tolist())

# ============================================================================
# 3. ANÁLISIS DE VALORES FALTANTES
# ============================================================================
print("\n2. VALORES FALTANTES")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({'Faltantes': missing, 'Porcentaje': missing_pct})
missing_df = missing_df[missing_df['Faltantes'] > 0].sort_values('Porcentaje', ascending=False)
print(missing_df)

# ============================================================================
# 4. ESTADÍSTICAS DESCRIPTIVAS - VARIABLE TARGET (PRECIO)
# ============================================================================
print("\n3. ESTADÍSTICAS DEL PRECIO (VARIABLE TARGET)")
print(df['Price'].describe())
print(f"\n   - Precio mínimo: ${df['Price'].min():,.0f}")
print(f"   - Precio máximo: ${df['Price'].max():,.0f}")
print(f"   - Precio promedio: ${df['Price'].mean():,.0f}")
print(f"   - Precio mediano: ${df['Price'].median():,.0f}")
print(f"   - Desv. estándar: ${df['Price'].std():,.0f}")

# ============================================================================
# 5. ANÁLISIS DE CARACTERÍSTICAS
# ============================================================================
print("\n4. CARACTERÍSTICAS PRINCIPALES")
print("\n   a) Tipos de propiedades:")
print(df['Type'].value_counts())
print("\n   b) Métodos de venta:")
print(df['Method'].value_counts())
print("\n   c) Regiones:")
print(df['Regionname'].value_counts())
print("\n   d) Cuartos por propiedad:")
print(df['Rooms'].value_counts().sort_index())

# ============================================================================
# 6. ANÁLISIS DE CORRELACIÓN
# ============================================================================
print("\n5. CORRELACIÓN CON PRECIO")
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
correlations = df[numeric_cols].corr()['Price'].sort_values(ascending=False)
print(correlations)

# ============================================================================
# 7. PREPARACIÓN DE DATOS PARA MODELAMIENTO
# ============================================================================
print("\n" + "="*80)
print("PREPARACIÓN DE DATOS PARA MODELAMIENTO")
print("="*80)

# Hacer una copia del dataframe
df_model = df.copy()

# Eliminar filas con precio nulo
df_model = df_model.dropna(subset=['Price'])
print(f"\nDataset después de eliminar Precio nulo: {df_model.shape[0]} filas")

# Llenar valores faltantes en características numéricas con la mediana
numeric_features = ['Rooms', 'Bedroom2', 'Bathroom', 'Car', 'Landsize',
                   'BuildingArea', 'YearBuilt', 'Distance', 'Propertycount']
for col in numeric_features:
    if col in df_model.columns:
        df_model[col] = df_model[col].fillna(df_model[col].median())

# Codificar variables categóricas
le_dict = {}
categorical_features = ['Type', 'Method', 'Regionname', 'CouncilArea']
for col in categorical_features:
    if col in df_model.columns:
        le = LabelEncoder()
        df_model[col + '_encoded'] = le.fit_transform(df_model[col].fillna('Unknown'))
        le_dict[col] = le

# Características para el modelo
feature_cols = [col for col in numeric_features if col in df_model.columns]
feature_cols += [col + '_encoded' for col in categorical_features if col in df_model.columns]

X = df_model[feature_cols].fillna(0)
y = df_model['Price']

print(f"\nCaracterísticas usadas: {len(feature_cols)}")
print(feature_cols)
print(f"Variable target: Price")
print(f"Muestras de entrenamiento: {len(X)}")

# ============================================================================
# 8. DIVISIÓN EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA
# ============================================================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nConjunto de entrenamiento: {len(X_train)} muestras")
print(f"Conjunto de prueba: {len(X_test)} muestras")

# Normalizar características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================================================
# 9. MODELAMIENTO - ENTRENAMIENTO DE MODELOS
# ============================================================================
print("\n" + "="*80)
print("ENTRENAMIENTO DE MODELOS")
print("="*80)

models = {}

# 1. Regresión Lineal
print("\n1. REGRESIÓN LINEAL")
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)
mse_lr = mean_squared_error(y_test, y_pred_lr)
rmse_lr = np.sqrt(mse_lr)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)
models['Regresión Lineal'] = {'model': lr, 'rmse': rmse_lr, 'mae': mae_lr, 'r2': r2_lr}
print(f"   RMSE: ${rmse_lr:,.0f}")
print(f"   MAE:  ${mae_lr:,.0f}")
print(f"   R²:   {r2_lr:.4f}")

# 2. Random Forest
print("\n2. RANDOM FOREST")
rf = RandomForestRegressor(n_estimators=100, max_depth=20, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = np.sqrt(mse_rf)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
models['Random Forest'] = {'model': rf, 'rmse': rmse_rf, 'mae': mae_rf, 'r2': r2_rf}
print(f"   RMSE: ${rmse_rf:,.0f}")
print(f"   MAE:  ${mae_rf:,.0f}")
print(f"   R²:   {r2_rf:.4f}")

# 3. Gradient Boosting
print("\n3. GRADIENT BOOSTING")
gb = GradientBoostingRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
mse_gb = mean_squared_error(y_test, y_pred_gb)
rmse_gb = np.sqrt(mse_gb)
mae_gb = mean_absolute_error(y_test, y_pred_gb)
r2_gb = r2_score(y_test, y_pred_gb)
models['Gradient Boosting'] = {'model': gb, 'rmse': rmse_gb, 'mae': mae_gb, 'r2': r2_gb}
print(f"   RMSE: ${rmse_gb:,.0f}")
print(f"   MAE:  ${mae_gb:,.0f}")
print(f"   R²:   {r2_gb:.4f}")

# ============================================================================
# 10. COMPARACIÓN DE MODELOS
# ============================================================================
print("\n" + "="*80)
print("RESUMEN COMPARATIVO DE MODELOS")
print("="*80)
results_df = pd.DataFrame(models).T
results_df = results_df[['rmse', 'mae', 'r2']].astype(float)
print("\n", results_df)

best_model_name = results_df['r2'].idxmax()
best_model = models[best_model_name]['model']
print(f"\n✓ MEJOR MODELO: {best_model_name}")
print(f"  R² Score: {models[best_model_name]['r2']:.4f}")

# ============================================================================
# 11. IMPORTANCIA DE CARACTERÍSTICAS (Random Forest)
# ============================================================================
print("\n" + "="*80)
print("IMPORTANCIA DE CARACTERÍSTICAS (Random Forest)")
print("="*80)
feature_importance = pd.DataFrame({
    'Característica': feature_cols,
    'Importancia': rf.feature_importances_
}).sort_values('Importancia', ascending=False)

print("\nTop 10 características más importantes:")
print(feature_importance.head(10).to_string(index=False))

# ============================================================================
# 12. EJEMPLOS DE PREDICCIONES
# ============================================================================
print("\n" + "="*80)
print("EJEMPLOS DE PREDICCIONES (GRADIENT BOOSTING)")
print("="*80)
y_pred_gb_train = gb.predict(X_train)
residuals = y_train - y_pred_gb_train

# Mostrar algunas predicciones
sample_indices = np.random.choice(len(X_test), 5, replace=False)
print("\nMuestras de predicción en conjunto de prueba:")
for i, idx in enumerate(sample_indices, 1):
    actual = y_test.iloc[idx]
    predicted = y_pred_gb[idx]
    error_pct = abs(actual - predicted) / actual * 100
    print(f"\n   Predicción {i}:")
    print(f"   Precio Real:      ${actual:,.0f}")
    print(f"   Precio Predicho:  ${predicted:,.0f}")
    print(f"   Error:            ${abs(actual - predicted):,.0f} ({error_pct:.1f}%)")

# ============================================================================
# 13. ANÁLISIS DE ERRORES
# ============================================================================
print("\n" + "="*80)
print("ANÁLISIS DE ERRORES")
print("="*80)
errors = np.abs(y_test - y_pred_gb)
print(f"\nError Promedio:           ${errors.mean():,.0f}")
print(f"Error Máximo:             ${errors.max():,.0f}")
print(f"Error Mínimo:             ${errors.min():,.0f}")
print(f"Percentil 25 de Error:    ${errors.quantile(0.25):,.0f}")
print(f"Percentil 50 de Error:    ${errors.quantile(0.50):,.0f}")
print(f"Percentil 75 de Error:    ${errors.quantile(0.75):,.0f}")
print(f"Percentil 95 de Error:    ${errors.quantile(0.95):,.0f}")

# Porcentaje de predicciones dentro de cierto rango
for margin in [50000, 100000, 150000]:
    pct = (errors <= margin).sum() / len(errors) * 100
    print(f"Predicciones dentro de ±${margin:,}: {pct:.1f}%")

print("\n" + "="*80)
print("✓ ANÁLISIS COMPLETADO")
print("="*80)
