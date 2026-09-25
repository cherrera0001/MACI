"""
Driver DashAI (http://localhost:8000) - Proyecto 3 FCD: train 2016 -> test 2017.
Etapas (reanudables via dashai_state.json):
  A) Subir dataset preparado (numerico, sin fuga) como DatasetJob.
  B) Crear model-session RegressionTask con split MANUAL: train=idx 2016, test=idx 2017.
  C) Crear runs (jerarquia de modelos), encolar ModelJob, esperar, leer metricas.
Uso: python dashai_driver.py [A|B|C|all]
"""
import sys, json, time, os, requests

BASE = "http://localhost:8000/api/v1"
CSV = r"F:\MACI\04_DATOS\housing_dashai_2016_2017.csv"
IDX = r"F:\MACI\05_RESULTADOS\dashai_split_indices.json"
STATE = r"F:\MACI\05_RESULTADOS\dashai_state.json"
DS_NAME = "housing_hito1_feats_2016train_2017test"   # variables Hito 1: sin BuildingArea/YearBuilt/CouncilArea/Suburb
SESSION_NAME = "FCD-P3 Hito1-feats 2016->2017 (split temporal manual)"
TARGET = "Price"
H = {"Accept-Language": "en"}

state = json.load(open(STATE)) if os.path.exists(STATE) else {}
def save(): json.dump(state, open(STATE, "w"), indent=2)
def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)

def wait_job(job_id, every=3, timeout=3600):
    t0 = time.time()
    while time.time() - t0 < timeout:
        jobs = requests.get(f"{BASE}/job/", timeout=30).json()
        j = next((x for x in jobs if x["id"] == job_id), None)
        if j is None:
            j = requests.get(f"{BASE}/job/{job_id}", timeout=30).json()
        st = j.get("status")
        if st in ("finished", "error", "failed", "cancelled"):
            return j
        time.sleep(every)
    raise TimeoutError(job_id)

# ---------------------------------------------------------------- A) dataset
def stage_A():
    if state.get("dataset_id") and state.get("dataset_status") == "finished":
        log("A) dataset ya subido id=", state["dataset_id"]); return
    if state.get("dataset_id"):   # intento previo fallido: limpiar registro
        d = requests.delete(f"{BASE}/dataset/{state['dataset_id']}", timeout=30)
        log("A) borro dataset fallido", state["dataset_id"], "->", d.status_code)
        state.pop("dataset_id", None); state.pop("dataset_status", None); save()
    # defaults del CSVDataLoader desde el schema del componente
    sch = requests.get(f"{BASE}/component/CSVDataLoader/", headers=H, timeout=30).json()["schema"]
    params = {}
    for k, v in sch["properties"].items():
        ph = v.get("placeholder")
        params[k] = ph.get("fixed_value") if isinstance(ph, dict) else ph
    params.update(separator=",", header="infer", encoding="utf-8", name=DS_NAME, dataloader="CSVDataLoader", compute_metadata=True)
    # tipos inferidos (imitando al frontend)
    with open(CSV, "rb") as f:
        pv = requests.post(f"{BASE}/dataset/preview_with_types",
                           files={"file": (os.path.basename(CSV), f, "text/csv")},
                           data={"params": json.dumps({**{k: params[k] for k in sch["properties"]}, "dataloader_name": "CSVDataLoader"})}, timeout=120)
    if pv.ok and pv.json().get("inferred_types"):
        params["inferred_types"] = pv.json()["inferred_types"]
        log("A) tipos inferidos:", {k: (v.get("type") if isinstance(v, dict) else v) for k, v in list(params["inferred_types"].items())[:6]}, "...")
    else:
        log("A) preview_with_types fallo:", pv.status_code, pv.text[:200])
    # crear registro
    r = requests.post(f"{BASE}/dataset/", json={"name": DS_NAME}, timeout=30)
    if r.status_code == 409:
        existing = [d for d in requests.get(f"{BASE}/dataset/", timeout=30).json() if d["name"] == DS_NAME]
        ds_id = existing[0]["id"]; log("A) nombre existente, reutilizo id=", ds_id)
    else:
        r.raise_for_status(); ds_id = r.json()["id"]
    state["dataset_id"] = ds_id; save()
    # encolar DatasetJob
    with open(CSV, "rb") as f:
        kw = {"dataset_id": ds_id, "notebook_id": None, "url": "", "params": params}
        r = requests.post(f"{BASE}/job/", data={"job_type": "DatasetJob", "kwargs": json.dumps(kw)},
                          files={"file": (os.path.basename(CSV), f, "text/csv")},
                          headers={"filename": os.path.basename(CSV)}, timeout=120)
    log("A) enqueue DatasetJob ->", r.status_code, r.text[:300]); r.raise_for_status()
    job = wait_job(r.json()["id"])
    log("A) job:", job["status"], job.get("error_msg"))
    state["dataset_status"] = job["status"]; save()
    if job["status"] != "finished": sys.exit("DatasetJob fallo")
    info = requests.get(f"{BASE}/dataset/{ds_id}/info", timeout=30).json()
    types = requests.get(f"{BASE}/dataset/{ds_id}/types", timeout=30).json()
    log("A) dataset", ds_id, "filas", info["total_rows"], "cols", info["total_columns"])
    log("A) tipos:", {k: v["type"] for k, v in types.items()})

# ---------------------------------------------------------------- B) session
def stage_B():
    if state.get("session_id"):
        log("B) sesion ya creada id=", state["session_id"]); return
    ds_id = state["dataset_id"]
    cols = requests.get(f"{BASE}/dataset/{ds_id}/info", timeout=30).json()["column_names"]
    inputs = [c for c in cols if c != TARGET]
    idx = json.load(open(IDX))
    assert len(idx["train"]) + len(idx["validation"]) == 6336 and len(idx["test"]) == 7244 and len(idx["validation"]) > 0
    log("B) split manual: train", len(idx["train"]), "val", len(idx["validation"]), "(ambos 2016) | test", len(idx["test"]), "(2017)")
    v = requests.post(f"{BASE}/model-session/validation", json={"task_name": "RegressionTask", "dataset_id": ds_id,
                      "inputs_columns": inputs, "outputs_columns": [TARGET]}, timeout=60)
    log("B) validacion columnas:", v.status_code, v.text[:200])
    splits = {"train": idx["train"], "validation": idx["validation"], "test": idx["test"], "splitType": "manual"}
    metrics = ["MAE", "RMSE", "R2", "MedianAbsoluteError"]
    body = {"dataset_id": ds_id, "task_name": "RegressionTask", "name": SESSION_NAME,
            "input_columns": inputs, "output_columns": [TARGET],
            "train_metrics": metrics, "validation_metrics": metrics, "test_metrics": metrics,
            "splits": json.dumps(splits)}
    r = requests.post(f"{BASE}/model-session/", json=body, timeout=120)
    log("B) create session ->", r.status_code, r.text[:400]); r.raise_for_status()
    state["session_id"] = r.json()["id"]; state["inputs"] = inputs; save()

# ---------------------------------------------------------------- C) runs
MODELOS = [  # (model_name DashAI, nombre run, parametros)  jerarquia: lineal -> arbol -> ensambles
    ("LinearRegression",             "01 Lineal (OLS)",              {}),
    ("RidgeRegression",              "02 Ridge",                     {}),
    ("DecisionTreeRegression",       "03 Arbol de decision",         {}),
    ("RandomForestRegression",       "04 Random Forest (default)",   {}),
    ("GradientBoostingR",            "05 Gradient Boosting (default)", {}),
    ("HistGradientBoostingRegression", "06 HistGradientBoosting (default)", {}),
]
def stage_C():
    sid = state["session_id"]; runs = state.setdefault("runs", {})
    for model_name, run_name, params in MODELOS:
        if run_name in runs: continue
        body = {"model_session_id": sid, "model_name": model_name, "name": run_name, "parameters": params,
                "optimizer_name": "", "optimizer_parameters": {}, "plot_history_path": "", "plot_slice_path": "",
                "plot_contour_path": "", "plot_importance_path": "", "goal_metric": "MAE",
                "description": "FCD P3: train 2016 / test 2017, features robustas (sin Suburb/Postcode)"}
        r = requests.post(f"{BASE}/run/", json=body, timeout=60)
        log("C) create run", run_name, "->", r.status_code, r.text[:200]); r.raise_for_status()
        run_id = r.json()["id"]
        j = requests.post(f"{BASE}/job/", data={"job_type": "ModelJob", "kwargs": json.dumps({"run_id": run_id})}, timeout=60)
        log("C) enqueue ModelJob run", run_id, "->", j.status_code, j.text[:200]); j.raise_for_status()
        runs[run_name] = {"run_id": run_id, "job_id": j.json()["id"], "model": model_name}; save()
    # esperar todos
    for run_name, info in runs.items():
        if info.get("status") in ("finished",): continue
        job = wait_job(info["job_id"]); info["status"] = job["status"]; info["error"] = job.get("error_msg"); save()
        log("C)", run_name, "->", job["status"], (job.get("error_msg") or "")[:300])
    # leer metricas
    out = []
    for run_name, info in runs.items():
        run = requests.get(f"{BASE}/run/{info['run_id']}", timeout=30).json()
        info["train_metrics"] = run.get("train_metrics"); info["test_metrics"] = run.get("test_metrics")
        info["run_status"] = run.get("status"); out.append((run_name, run))
    save()
    print("\n=== RESULTADOS DASHAI (test = 2017, train = 2016) ===")
    print(f"{'run':38s} {'MAE_test':>12s} {'RMSE_test':>12s} {'R2_test':>8s} {'R2_train':>9s} {'MAE_train':>12s}")
    for run_name, run in out:
        tm, trm = run.get("test_metrics") or {}, run.get("train_metrics") or {}
        g = lambda d, k: (f"{d[k]:,.0f}" if isinstance(d.get(k), (int, float)) and k != "R2" else (f"{d[k]:.3f}" if k in d else "-"))
        print(f"{run_name:38s} {g(tm,'MAE'):>12s} {g(tm,'RMSE'):>12s} {g(tm,'R2'):>8s} {g(trm,'R2'):>9s} {g(trm,'MAE'):>12s}  status={run.get('status')}")
    json.dump({k: v for k, v in runs.items()}, open(r"F:\MACI\05_RESULTADOS\dashai_resultados.json", "w"), indent=2)

def stage_R():
    """Re-encolar runs existentes (tras reinicio de DashAI): reset del run + nuevo ModelJob."""
    runs = state.get("runs", {})
    for run_name, info in runs.items():
        cur = requests.get(f"{BASE}/run/{info['run_id']}", timeout=30).json()
        if cur.get("test_metrics"):
            info["status"] = "finished"; log("R)", run_name, "ya tiene metricas, no re-encolo"); continue
        rs = requests.patch(f"{BASE}/run/{info['run_id']}/reset", timeout=60)
        j = requests.post(f"{BASE}/job/", data={"job_type": "ModelJob", "kwargs": json.dumps({"run_id": info["run_id"]})}, timeout=60)
        log("R)", run_name, "reset ->", rs.status_code, "| enqueue ->", j.status_code, j.text[:120]); j.raise_for_status()
        info["job_id"] = j.json()["id"]; info.pop("status", None); info.pop("error", None)
    save()

if __name__ == "__main__":
    st = sys.argv[1] if len(sys.argv) > 1 else "all"
    if st in ("A", "all"): stage_A()
    if st in ("B", "all"): stage_B()
    if st == "R": stage_R()
    if st in ("C", "R", "all"): stage_C()
