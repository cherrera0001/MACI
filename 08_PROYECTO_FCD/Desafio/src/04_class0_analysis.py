"""
Analisis profundo de la clase 0 sobre predicciones OOF.

    python src/04_class0_analysis.py <npz> <nombre_modelo> <variante>

Responde:
  1. Como se reparten los errores de la clase 0 (0->0, 0->1, 0->2).
  2. Que features distinguen a los aciertos de los falsos negativos.
  3. La clase 0 vive en la zona de incertidumbre entre 1 y 2?
     Test: entropia y margen top-2 por clase real, y tasa de clase 0 en
     funcion de |P1 - P2| (balance entre espiral y eliptica).
"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

NPZ = sys.argv[1] if len(sys.argv) > 1 else os.path.join(G.ANALYSIS_DIR, "oof_models_D.npz")
MODEL = sys.argv[2] if len(sys.argv) > 2 else "CatBoost(bal)"
VARIANT = sys.argv[3] if len(sys.argv) > 3 else "D"


def main():
    X, y, Xt, test_ids, const = G.get_xy(VARIANT, clean=True)
    y = np.asarray(y)
    proba = np.load(NPZ)[MODEL]
    pred = proba.argmax(axis=1)

    print("=" * 72)
    print(f"CLASE 0 -- modelo {MODEL}, features {VARIANT}")
    print("=" * 72)

    is0 = y == 0
    print(f"\nn clase 0 real = {is0.sum()}")
    for c in (0, 1, 2):
        n = int((pred[is0] == c).sum())
        print(f"  real 0 -> pred {c}: {n:3d}  ({n / is0.sum() * 100:5.1f}%)")

    # ---- 1. incertidumbre por clase real ---------------------------------
    eps = 1e-12
    ent = -(proba * np.log(proba + eps)).sum(axis=1)
    srt = np.sort(proba, axis=1)
    margin = srt[:, -1] - srt[:, -2]
    bal12 = np.abs(proba[:, 1] - proba[:, 2])

    print("\n" + "-" * 72)
    print("INCERTIDUMBRE POR CLASE REAL (entropia alta / margen bajo = zona ambigua)")
    unc = pd.DataFrame({"label": y, "entropia": ent, "margen_top2": margin,
                        "abs_P1_menos_P2": bal12, "P0": proba[:, 0]})
    print(unc.groupby("label").agg(["mean", "median"]).round(4).to_string())

    # ---- 2. tasa de clase 0 segun el balance 1 vs 2 ----------------------
    print("\n" + "-" * 72)
    print("HIPOTESIS FRONTERA: tasa de clase 0 real segun |P1-P2| (deciles)")
    unc["q"] = pd.qcut(unc.abs_P1_menos_P2, 10, labels=False, duplicates="drop")
    t = unc.groupby("q").apply(
        lambda d: pd.Series({"n": len(d),
                             "tasa_clase0_real": (d.label == 0).mean(),
                             "abs_P1_P2_medio": d.abs_P1_menos_P2.mean()}),
        include_groups=False)
    print(t.round(4).to_string())
    print("  -> si la tasa de clase 0 baja monotonamente al crecer |P1-P2|,")
    print("     la clase 0 se concentra en la frontera espiral/eliptica.")

    print("\nIdem con entropia (deciles):")
    unc["qe"] = pd.qcut(unc.entropia, 10, labels=False, duplicates="drop")
    te = unc.groupby("qe").apply(
        lambda d: pd.Series({"n": len(d), "tasa_clase0_real": (d.label == 0).mean(),
                             "entropia_media": d.entropia.mean()}),
        include_groups=False)
    print(te.round(4).to_string())

    # ---- 3. features por grupo de error ----------------------------------
    print("\n" + "-" * 72)
    print("FEATURES: aciertos clase 0 vs falsos negativos 0->1 y 0->2")
    Z = (X - X.mean()) / X.std(ddof=0)
    grp = pd.Series(np.where(~is0, "otro",
                             np.where(pred == 0, "TP_0",
                                      np.where(pred == 1, "FN_0a1", "FN_0a2"))),
                    index=X.index)
    sub = Z[is0].copy()
    sub["grupo"] = grp[is0].values
    gm = sub.groupby("grupo").mean().T
    for col in ("TP_0", "FN_0a1", "FN_0a2"):
        if col not in gm.columns:
            gm[col] = np.nan
    gm["dif_TP_menos_FN1"] = gm["TP_0"] - gm["FN_0a1"]
    gm["dif_TP_menos_FN2"] = gm["TP_0"] - gm["FN_0a2"]
    gm["max_abs_dif"] = gm[["dif_TP_menos_FN1", "dif_TP_menos_FN2"]].abs().max(axis=1)
    top = gm.sort_values("max_abs_dif", ascending=False)
    print("\nTop 20 features por diferencia (medias estandarizadas):")
    print(top.head(20).round(3).to_string())

    out = top.reset_index().rename(columns={"index": "feature"})
    out.insert(0, "modelo", MODEL)
    G.save_csv(out, os.path.join(G.ANALYSIS_DIR, "class0_analysis.csv"))

    G.save_csv(t.reset_index(), os.path.join(G.ANALYSIS_DIR, "class0_frontera_P1P2.csv"))
    G.save_csv(unc.groupby("label").mean().reset_index(),
               os.path.join(G.ANALYSIS_DIR, "class0_incertidumbre.csv"))


if __name__ == "__main__":
    main()
