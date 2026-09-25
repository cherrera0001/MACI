"""
Auditoria de datos y de fuga -- persiste los resultados en analysis/.

    python src/00_audit.py

Genera:
  analysis/audit_columns.csv   una fila por columna con todos los diagnosticos
  analysis/audit_summary.json  cifras globales citadas en REPORT.md
  analysis/class0_geometry.csv evidencia (independiente del modelo) de donde
                               vive la clase 0 en el espacio de features
"""
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
from sklearn.metrics import roc_auc_score

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

os.makedirs(G.ANALYSIS_DIR, exist_ok=True)


def main():
    train, test = G.load_raw()
    summary = {}

    summary["train_shape"] = list(train.shape)
    summary["test_shape"] = list(test.shape)
    summary["cols_solo_train"] = sorted(set(train.columns) - set(test.columns))
    summary["cols_solo_test"] = sorted(set(test.columns) - set(train.columns))
    summary["nulos_train"] = int(train.isna().sum().sum())
    summary["nulos_test"] = int(test.isna().sum().sum())
    summary["duplicados_train"] = int(train.duplicated().sum())
    summary["ID_unico_train"] = bool(train.ID.is_unique)
    summary["ID_unico_test"] = bool(test.ID.is_unique)
    summary["overlap_ID_train_test"] = len(set(train.ID) & set(test.ID))

    vc = train.label.value_counts().sort_index()
    summary["distribucion_clases"] = {int(k): int(v) for k, v in vc.items()}
    summary["distribucion_clases_pct"] = {
        int(k): round(v * 100, 2) for k, v in
        train.label.value_counts(normalize=True).sort_index().items()}

    base, const = G.base_feature_list(train)
    summary["columnas_constantes"] = const
    summary["n_features_base"] = len(base)

    # ---- regla de generacion del label (fuga directa) -------------------
    rule = np.where(train.p_cs >= 0.5, 1, np.where(train.p_el >= 0.5, 2, 0))
    summary["label_derivable_de_p_cs_p_el"] = {
        "regla": "1 si p_cs>=0.5; 2 si p_el>=0.5; 0 en otro caso",
        "coincidencia": round(float((rule == train.label).mean()), 4),
        "discrepancias": int((rule != train.label).sum()),
        "nota": "las discrepancias son empates exactos p_cs=p_el=0.5",
    }
    pmax = train[["p_cs", "p_el"]].max(axis=1)
    summary["max_voto_por_clase"] = {
        int(k): round(float(v), 4) for k, v in pmax.groupby(train.label).max().items()}

    # ---- centinelas -----------------------------------------------------
    magcols = [c for c in base if ("Mag" in c) or c.startswith("dered") or c.startswith("mRrCc")]
    summary["filas_con_centinela_-9999"] = {
        "train": int((train[magcols] <= -99).any(axis=1).sum()),
        "test": int((test[magcols] <= -99).any(axis=1).sum()),
    }

    # ---- por columna ----------------------------------------------------
    trc = G.clean_sentinels(train, magcols)
    rows = []
    sp = trc[base + ["label"]].corr(method="spearman")["label"].abs()
    m12 = train.label != 0
    for c in base:
        s = train[c]
        sc = trc[c]
        vcx = s.value_counts(normalize=True)
        med = sc.median()
        mad = (sc - med).abs().median()
        ok = sc.notna()
        try:
            auc0 = roc_auc_score((train.label == 0)[ok], sc[ok])
            ok2 = ok & m12
            auc12 = roc_auc_score((train.label[ok2] == 2).astype(int), sc[ok2])
        except ValueError:
            auc0 = auc12 = np.nan
        ks, pv = ks_2samp(train[c], test[c])
        rows.append({
            "columna": c,
            "dtype": str(s.dtype),
            "n_unicos": int(s.nunique(dropna=False)),
            "constante": s.nunique(dropna=False) <= 1,
            "nzv_modal_pct": round(float(vcx.iloc[0]), 4) if len(vcx) else np.nan,
            "n_centinelas": int((s <= -99).sum()),
            "min": float(sc.min()), "max": float(sc.max()),
            "n_outliers_z10": int(((sc - med).abs() / (1.4826 * mad) > 10).sum()) if mad > 0 else 0,
            "spearman_abs_label": round(float(sp.get(c, np.nan)), 4),
            "auc_0_vs_resto": round(abs(auc0 - 0.5) + 0.5, 4) if auc0 == auc0 else np.nan,
            "auc_1_vs_2": round(abs(auc12 - 0.5) + 0.5, 4) if auc12 == auc12 else np.nan,
            "ks_train_test": round(float(ks), 4),
            "ks_pvalue": float(pv),
            "meta_drift_excluida_en_E": c in G.META_DRIFT_COLS,
        })
    cols = pd.DataFrame(rows).sort_values("ks_train_test", ascending=False)
    G.save_csv(cols, os.path.join(G.ANALYSIS_DIR, "audit_columns.csv"))

    summary["techo_auc_marginal"] = {
        "0_vs_resto": float(cols.auc_0_vs_resto.max()),
        "1_vs_2": float(cols.auc_1_vs_2.max()),
    }
    summary["top5_drift_train_test"] = (
        cols[["columna", "ks_train_test"]].head(5).to_dict("records"))

    # ---- pares redundantes ---------------------------------------------
    cm = trc[base].corr().abs().to_numpy(copy=True)
    np.fill_diagonal(cm, 0)
    cmd = pd.DataFrame(cm, index=base, columns=base)
    pairs = [(a, b, round(float(cmd.loc[a, b]), 4))
             for i, a in enumerate(base) for b in base[i + 1:]
             if cmd.loc[a, b] > 0.98]
    summary["n_pares_correlacion_mayor_098"] = len(pairs)
    summary["pares_correlacion_mayor_098"] = [list(p) for p in pairs]

    # ---- geometria de la clase 0 ---------------------------------------
    Z = (trc[base] - trc[base].mean()) / trc[base].std()
    mu = Z.groupby(train.label).mean().T
    mu.columns = ["mu0", "mu1", "mu2"]
    mu["sep_12"] = (mu.mu1 - mu.mu2).abs()
    mu["mu0_entre_mu1_mu2"] = ((mu.mu0 > mu[["mu1", "mu2"]].min(axis=1)) &
                               (mu.mu0 < mu[["mu1", "mu2"]].max(axis=1)))
    mu["t_rel"] = (mu.mu0 - mu.mu1) / (mu.mu2 - mu.mu1)
    sd = Z.groupby(train.label).std().T
    sd.columns = ["sd0", "sd1", "sd2"]
    geo = mu.join(sd).sort_values("sep_12", ascending=False)
    G.save_csv(geo.reset_index().rename(columns={"index": "feature"}),
               os.path.join(G.ANALYSIS_DIR, "class0_geometry.csv"))

    top20 = geo.head(20)
    summary["geometria_clase0"] = {
        "frac_entre_top20_discriminantes": round(float(top20.mu0_entre_mu1_mu2.mean()), 3),
        "frac_entre_todas": round(float(geo.mu0_entre_mu1_mu2.mean()), 3),
        "t_rel_mediano_top20": round(float(top20.t_rel.median()), 3),
        "dispersion_mediana": {"clase0": round(float(sd.sd0.median()), 3),
                               "clase1": round(float(sd.sd1.median()), 3),
                               "clase2": round(float(sd.sd2.median()), 3)},
    }

    with open(os.path.join(G.ANALYSIS_DIR, "audit_summary.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, ensure_ascii=False)
    print("escrito analysis/audit_summary.json")
    print(json.dumps({k: v for k, v in summary.items()
                      if k not in ("pares_correlacion_mayor_098",)},
                     indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
