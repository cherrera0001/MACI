"""
Auditoria y optimizacion de la regla de decision.

    python src/05_decision_rule.py <npz> <nombre_modelo> <variante>

Puntos clave:
  - Los pesos se ajustan SOLO con probabilidades OOF del train.
  - Se reporta ademas una estimacion ANIDADA (pesos ajustados en folds de
    entrenamiento, aplicados al fold de validacion). Es la unica cifra
    honesta: el "mejor F1-macro OOF" tras tunear pesos sobre todo el OOF
    esta optimisticamente sesgado, porque se optimiza y se reporta sobre
    los mismos datos.
  - Se construye el frente de Pareto entre F1-macro, F1 clase 0 y recall 0.
"""
import os
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

NPZ = sys.argv[1] if len(sys.argv) > 1 else os.path.join(G.ANALYSIS_DIR, "oof_models_D.npz")
MODEL = sys.argv[2] if len(sys.argv) > 2 else "CatBoost(bal)"
VARIANT = sys.argv[3] if len(sys.argv) > 3 else "D"


def main():
    X, y, Xt, test_ids, const = G.get_xy(VARIANT, clean=True)
    y = np.asarray(y)
    proba = np.load(NPZ)[MODEL]
    fl = G.folds(X, y)

    print("=" * 72)
    print(f"REGLA DE DECISION -- {MODEL} / features {VARIANT}")
    print("=" * 72)

    res = G.search_weights(proba, y, step=0.05, lo=0.5, hi=2.6)
    G.save_csv(res, os.path.join(G.ANALYSIS_DIR, "weight_search_full.csv"))

    best_macro = res.sort_values("f1_macro", ascending=False).iloc[0]
    thr = best_macro.f1_macro - 0.005
    elig = res[res.f1_macro >= thr]
    best_c0 = elig.sort_values(["f1_0", "rec_0"], ascending=False).iloc[0]
    best_rec0 = elig.sort_values(["rec_0", "f1_0"], ascending=False).iloc[0]

    rows = []

    def add(nombre, w):
        pred = G.apply_weights(proba, w)
        m = G.metrics_row(y, pred, nombre)
        m["w0"], m["w1"], m["w2"] = float(w[0]), float(w[1]), float(w[2])
        rows.append(m)
        print(f"{nombre:44s} w={np.round(w,2)} F1m={m['f1_macro']:.4f} "
              f"f1_0={m['f1_0']:.4f} rec_0={m['rec_0']:.4f} prec_0={m['prec_0']:.4f}")
        return m

    print("\nA. argmax normal")
    add("A argmax [1,1,1]", [1, 1, 1])
    print("\nB/C. pesos declarados por el usuario")
    add("B declarado macro [1.7,0.9,0.9]", [1.7, 0.9, 0.9])
    add("C declarado clase0 [1.9,0.8,1.0]", [1.9, 0.8, 1.0])
    print("\nD. busqueda sistematica nueva (paso 0.05)")
    add("D1 MEJOR F1-MACRO", [best_macro.w0, best_macro.w1, best_macro.w2])
    add("D2 MAX F1-CLASE0 con F1m >= best-0.005", [best_c0.w0, best_c0.w1, best_c0.w2])
    add("D3 MAX RECALL-0 con F1m >= best-0.005", [best_rec0.w0, best_rec0.w1, best_rec0.w2])

    # compromiso: maximiza f1_macro + f1_0 normalizados
    comp = res.copy()
    comp["score_comp"] = comp.f1_macro / comp.f1_macro.max() + comp.f1_0 / comp.f1_0.max()
    bc = comp.sort_values("score_comp", ascending=False).iloc[0]
    add("D4 MEJOR COMPROMISO macro/clase0", [bc.w0, bc.w1, bc.w2])

    df = pd.DataFrame(rows)[["nombre", "w0", "w1", "w2", "f1_macro",
                             "prec_0", "rec_0", "f1_0", "f1_1", "f1_2", "n_pred_0"]]
    G.save_csv(df, os.path.join(G.ANALYSIS_DIR, "decision_rule.csv"))
    print("\n" + df.to_string(index=False))

    # ---- Pareto ----------------------------------------------------------
    pf = G.pareto_front(res).sort_values("f1_macro", ascending=False)
    G.save_csv(pf, os.path.join(G.ANALYSIS_DIR, "pareto_front.csv"))
    print(f"\nFrente de Pareto (F1-macro, F1_0, rec_0): {len(pf)} puntos")
    print(pf.head(25).round(4).to_string(index=False))

    # ---- estimacion honesta ---------------------------------------------
    print("\n" + "=" * 72)
    print("ESTIMACION ANIDADA (honesta) DEL BENEFICIO DE TUNEAR PESOS")
    pred_nested, chosen = G.nested_weight_score(proba, y, fl, step=0.05, lo=0.5, hi=2.6)
    m_nested = G.metrics_row(y, pred_nested, "pesos anidados")
    m_argmax = G.metrics_row(y, proba.argmax(axis=1), "argmax")
    print("pesos elegidos por fold:", [tuple(np.round(w, 2)) for w in chosen])
    print(f"argmax            F1m={m_argmax['f1_macro']:.4f} f1_0={m_argmax['f1_0']:.4f}")
    print(f"pesos ANIDADOS    F1m={m_nested['f1_macro']:.4f} f1_0={m_nested['f1_0']:.4f}")
    print(f"pesos tuneados en TODO el OOF (sesgado) F1m={best_macro.f1_macro:.4f}")
    print(f"=> sesgo optimista estimado = "
          f"{best_macro.f1_macro - m_nested['f1_macro']:+.4f}")

    G.save_csv(pd.DataFrame([m_argmax, m_nested]),
               os.path.join(G.ANALYSIS_DIR, "decision_rule_nested.csv"))


if __name__ == "__main__":
    main()
