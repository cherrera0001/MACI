"""
Hipotesis alternativa: clasificador JERARQUICO.

    python src/06_hierarchical.py <variante>

Etapa A: 0 vs {1,2}   -- "es ambigua / no decidible?"
Etapa B: 1 vs 2       -- "espiral o eliptica?", entrenada SOLO con filas
                         decidibles DEL FOLD DE ENTRENAMIENTO.

Control de fuga: en cada fold, la etapa B se entrena unicamente con las filas
de entrenamiento cuyo label es 1 o 2. Las filas de validacion nunca se usan
para entrenar ninguna de las dos etapas, y el filtro label in {1,2} se aplica
solo del lado del entrenamiento (usar el label real de validacion para decidir
a que filas aplicar la etapa B seria fuga).

Reconstruccion: P = [pA0, (1-pA0)*pB1, (1-pA0)*pB2], luego argmax ponderado
o umbral sobre pA0. Ambos se comparan contra CatBoost multiclase plano.
"""
import os
import sys
import warnings

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import f1_score

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

warnings.filterwarnings("ignore")
VARIANT = sys.argv[1] if len(sys.argv) > 1 else "D"


def cb(fold, **kw):
    p = dict(iterations=700, depth=5, learning_rate=0.03, l2_leaf_reg=5,
             random_seed=G.SEED + fold, verbose=False, thread_count=8)
    p.update(kw)
    return CatBoostClassifier(**p)


def main():
    X, y, Xt, test_ids, const = G.get_xy(VARIANT, clean=True)
    y = np.asarray(y)
    fl = G.folds(X, y)

    pA0 = np.zeros(len(X))          # P(clase 0) etapa A
    pB = np.zeros((len(X), 2))      # P(1), P(2) etapa B

    for k, (itr, iva) in enumerate(fl):
        Xtr, Xva = X.iloc[itr], X.iloc[iva]
        ytr = y[itr]

        # Etapa A: binario 0 vs resto
        mA = cb(k, loss_function="Logloss", auto_class_weights="Balanced")
        mA.fit(Xtr, (ytr == 0).astype(int))
        pA0[iva] = mA.predict_proba(Xva)[:, 1]

        # Etapa B: solo filas decidibles del fold de ENTRENAMIENTO
        dec = ytr != 0
        mB = cb(k, loss_function="Logloss", auto_class_weights="Balanced")
        mB.fit(Xtr[dec], (ytr[dec] == 2).astype(int))
        p2 = mB.predict_proba(Xva)[:, 1]
        pB[iva, 0] = 1 - p2
        pB[iva, 1] = p2

    np.savez(os.path.join(G.ANALYSIS_DIR, f"oof_hier_{VARIANT}.npz"),
             pA0=pA0, pB=pB)

    print("=" * 72)
    print(f"JERARQUICO -- features {VARIANT}")
    print("=" * 72)
    from sklearn.metrics import roc_auc_score
    print(f"AUC etapa A (0 vs resto): {roc_auc_score((y==0).astype(int), pA0):.4f}")
    m12 = y != 0
    print(f"AUC etapa B (1 vs 2, solo decidibles): "
          f"{roc_auc_score((y[m12]==2).astype(int), pB[m12,1]):.4f}")

    rows = []

    # --- variante 1: umbral sobre pA0 ---
    print("\nBarrido de umbral t sobre P(clase 0):")
    best = None
    for t in np.arange(0.10, 0.91, 0.01):
        pred = np.where(pA0 >= t, 0, np.where(pB[:, 1] >= 0.5, 2, 1))
        m = G.metrics_row(y, pred, f"jerarquico_t={t:.2f}")
        m["t"] = float(t)
        rows.append(m)
        if best is None or m["f1_macro"] > best["f1_macro"]:
            best = m
    print(f"  mejor t={best['t']:.2f} F1m={best['f1_macro']:.4f} "
          f"f1_0={best['f1_0']:.4f} rec_0={best['rec_0']:.4f}")

    # --- variante 2: probabilidad reconstruida + pesos ---
    P = np.column_stack([pA0, (1 - pA0) * pB[:, 0], (1 - pA0) * pB[:, 1]])
    res = G.search_weights(P, y, step=0.05, lo=0.5, hi=2.6)
    bm = res.sort_values("f1_macro", ascending=False).iloc[0]
    pred_w = G.apply_weights(P, [bm.w0, bm.w1, bm.w2])
    mw = G.metrics_row(y, pred_w, "jerarquico_reconstruido_pesos")
    mw.update({"w0": float(bm.w0), "w1": float(bm.w1), "w2": float(bm.w2)})
    print(f"\nReconstruido + pesos w={np.round([bm.w0,bm.w1,bm.w2],2)}: "
          f"F1m={mw['f1_macro']:.4f} f1_0={mw['f1_0']:.4f} rec_0={mw['rec_0']:.4f}")

    m_plain = G.metrics_row(y, P.argmax(axis=1), "jerarquico_reconstruido_argmax")
    print(f"Reconstruido argmax: F1m={m_plain['f1_macro']:.4f} "
          f"f1_0={m_plain['f1_0']:.4f}")

    df = pd.DataFrame(rows + [mw, m_plain])
    G.save_csv(df, os.path.join(G.ANALYSIS_DIR, "hierarchical_results.csv"))

    # honestidad: umbral anidado
    pred_nested = np.zeros(len(y), dtype=int)
    for itr, iva in fl:
        bt, bs = 0.5, -1
        for t in np.arange(0.10, 0.91, 0.01):
            pr = np.where(pA0[itr] >= t, 0, np.where(pB[itr, 1] >= 0.5, 2, 1))
            s = f1_score(y[itr], pr, average="macro")
            if s > bs:
                bs, bt = s, t
        pred_nested[iva] = np.where(pA0[iva] >= bt, 0,
                                    np.where(pB[iva, 1] >= 0.5, 2, 1))
    mn = G.metrics_row(y, pred_nested, "jerarquico_umbral_ANIDADO")
    print(f"\nUmbral ANIDADO (honesto): F1m={mn['f1_macro']:.4f} "
          f"f1_0={mn['f1_0']:.4f} rec_0={mn['rec_0']:.4f}")
    print(f"sesgo optimista del umbral tuneado en todo el OOF: "
          f"{best['f1_macro'] - mn['f1_macro']:+.4f}")


if __name__ == "__main__":
    main()
