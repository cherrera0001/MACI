"""
MODELAMIENTO CON VALIDACION TEMPORAL ESTRICTA (Proyecto 3, FCD 2026-2)
Instruccion del PDF: entrenar con ventas 2016, predecir y evaluar sobre 2017.

Protocolo:
  1. Train = 2016 (n=6336), Test = 2017 (n=7244). Test se toca UNA sola vez al final.
  2. Seleccion de modelo por 5-fold CV DENTRO de 2016 (no sobre test).
  3. Jerarquia: Baseline -> Lineal -> Arbol -> Ensambles.
  4. Pipeline sklearn: imputacion/escala/encoding aprendidos solo en train.
  5. Features robustas a covariate shift (sin Suburb/Postcode/Address/SellerG).
  6. Estabilidad: 5 semillas para modelos estocasticos.
  7. Error desagregado: suburbios conocidos vs nuevos en 2017.
"""
import json, time, warnings
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
warnings.filterwarnings("ignore")

CSV = r"F:\MACI\08_PROYECTO_FCD\Hito1\Corrección\Trabajo N°1 _ FINAL\1° Trabajo _FUNDAMENTOS\housing_data.csv"
RS = 42
SEEDS = [0, 1, 2, 3, 4]

df = pd.read_csv(CSV)
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["Year"] = df["Date"].dt.year
train = df[df.Year == 2016].copy()
test = df[df.Year == 2017].copy()

NUM = ["Rooms", "Distance", "Bedroom2", "Bathroom", "Car", "Landsize",
       "Lattitude", "Longtitude", "Propertycount"]
CAT = ["Type", "Method", "Regionname"]
EXCLUIDAS = ["Suburb", "Postcode", "Address", "SellerG", "CouncilArea", "Date",
             "BuildingArea", "YearBuilt"]

def preproc(scale: bool):
    num_steps = [("imp", SimpleImputer(strategy="median", add_indicator=True))]
    if scale:
        num_steps.append(("sc", StandardScaler()))
    return ColumnTransformer([
        ("num", Pipeline(num_steps), NUM),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="constant", fill_value="missing")),
                          ("oh", OneHotEncoder(handle_unknown="ignore"))]), CAT),
    ])

def modelos(seed):
    return {
        "Baseline (mediana)":      (False, DummyRegressor(strategy="median")),
        "Ridge (lineal)":          (True,  Ridge(alpha=1.0)),
        "Arbol de decision":       (False, DecisionTreeRegressor(max_depth=8, min_samples_leaf=20, random_state=seed)),
        "Random Forest":           (False, RandomForestRegressor(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=seed)),
        "Gradient Boosting":       (False, GradientBoostingRegressor(n_estimators=400, max_depth=4, learning_rate=0.05, subsample=0.8, random_state=seed)),
        "HistGradientBoosting":    (False, HistGradientBoostingRegressor(max_iter=500, learning_rate=0.05, max_leaf_nodes=31, l2_regularization=1.0, random_state=seed)),
    }

X_tr, X_te = train[NUM + CAT], test[NUM + CAT]
y_tr, y_te = train["Price"].values, test["Price"].values
suburbios_2016 = set(train["Suburb"])
mask_nuevo = ~test["Suburb"].isin(suburbios_2016).values

def metricas(y, p):
    return dict(MAE=float(mean_absolute_error(y, p)),
                RMSE=float(np.sqrt(mean_squared_error(y, p))),
                R2=float(r2_score(y, p)),
                MAPE=float(np.mean(np.abs(y - p) / y) * 100))

resultados = {}
kf = KFold(n_splits=5, shuffle=True, random_state=RS)

for target in ["raw", "log"]:
    ytr = np.log1p(y_tr) if target == "log" else y_tr
    inv = (lambda z: np.expm1(z)) if target == "log" else (lambda z: z)
    for nombre, (scale, _) in modelos(0).items():
        t0 = time.time()
        # --- CV dentro de 2016 (seleccion) ---
        pipe = Pipeline([("prep", preproc(scale)), ("m", modelos(RS)[nombre][1])])
        cv_pred_mae = []
        for tr_idx, va_idx in kf.split(X_tr):
            pipe.fit(X_tr.iloc[tr_idx], ytr[tr_idx])
            p = inv(pipe.predict(X_tr.iloc[va_idx]))
            cv_pred_mae.append(mean_absolute_error(y_tr[va_idx], p))
        # --- Test 2017 con multiples semillas (estabilidad) ---
        seeds = SEEDS if nombre in ("Random Forest", "Gradient Boosting", "HistGradientBoosting", "Arbol de decision") else [RS]
        te_list, tr_list, nuevo_list, conocido_list = [], [], [], []
        for s in seeds:
            pipe = Pipeline([("prep", preproc(scale)), ("m", modelos(s)[nombre][1])])
            pipe.fit(X_tr, ytr)
            p_te = inv(pipe.predict(X_te)); p_tr = inv(pipe.predict(X_tr))
            te_list.append(metricas(y_te, p_te)); tr_list.append(metricas(y_tr, p_tr))
            nuevo_list.append(mean_absolute_error(y_te[mask_nuevo], p_te[mask_nuevo]))
            conocido_list.append(mean_absolute_error(y_te[~mask_nuevo], p_te[~mask_nuevo]))
        agg = lambda L, k: (float(np.mean([d[k] for d in L])), float(np.std([d[k] for d in L])))
        r = dict(
            target=target, n_seeds=len(seeds), segundos=round(time.time() - t0, 1),
            cv2016_MAE_mean=float(np.mean(cv_pred_mae)), cv2016_MAE_std=float(np.std(cv_pred_mae)),
            test2017_MAE=agg(te_list, "MAE"), test2017_RMSE=agg(te_list, "RMSE"),
            test2017_R2=agg(te_list, "R2"), test2017_MAPE=agg(te_list, "MAPE"),
            train2016_R2=agg(tr_list, "R2")[0], train2016_MAE=agg(tr_list, "MAE")[0],
            brecha_R2_train_test=agg(tr_list, "R2")[0] - agg(te_list, "R2")[0],
            MAE_suburbio_nuevo=float(np.mean(nuevo_list)), MAE_suburbio_conocido=float(np.mean(conocido_list)),
        )
        resultados[f"{nombre} | {target}"] = r
        print(f"[{target:3s}] {nombre:22s} CV16 MAE={r['cv2016_MAE_mean']:>9,.0f}  "
              f"TEST17 MAE={r['test2017_MAE'][0]:>9,.0f}±{r['test2017_MAE'][1]:<6,.0f} "
              f"RMSE={r['test2017_RMSE'][0]:>9,.0f}  R2={r['test2017_R2'][0]:.3f}±{r['test2017_R2'][1]:.3f}  "
              f"R2train={r['train2016_R2']:.3f}  brecha={r['brecha_R2_train_test']:+.3f}  "
              f"MAE nuevo/conocido={r['MAE_suburbio_nuevo']:,.0f}/{r['MAE_suburbio_conocido']:,.0f}  ({r['segundos']}s)")

meta = dict(n_train_2016=int(len(train)), n_test_2017=int(len(test)),
            pct_test_suburbio_nuevo=float(mask_nuevo.mean() * 100),
            features_num=NUM, features_cat=CAT, excluidas=EXCLUIDAS, seeds=SEEDS,
            precio_mediana_2016=float(np.median(y_tr)), precio_mediana_2017=float(np.median(y_te)))
json.dump(dict(meta=meta, resultados=resultados), open(r"F:\MACI\09_RESULTADOS\resultados_temporal.json", "w"), indent=2)
print("\nGuardado: F:\\MACI\\09_RESULTADOS\\resultados_temporal.json")
