"""
Ensemble -- solo se adopta si mejora sobre OOF.

    python src/08_ensemble.py <npz> <variante>

Primero mide DIVERSIDAD de errores entre modelos (si dos modelos fuertes
fallan en las mismas filas, promediarlos no puede aportar). Luego busca alpha
en P = alpha*PA + (1-alpha)*PB usando unicamente probabilidades OOF, con y sin
pesos de decision.
"""
import itertools
import os
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gz_lib as G

NPZ = sys.argv[1] if len(sys.argv) > 1 else os.path.join(G.ANALYSIS_DIR, "oof_models_D.npz")
VARIANT = sys.argv[2] if len(sys.argv) > 2 else "D"


def main():
    X, y, Xt, test_ids, const = G.get_xy(VARIANT, clean=True)
    y = np.asarray(y)
    z = np.load(NPZ)
    names = list(z.keys())
    P = {n: z[n] for n in names}

    base = pd.DataFrame([
        {"modelo": n, "f1_macro": f1_score(y, P[n].argmax(1), average="macro")}
        for n in names]).sort_values("f1_macro", ascending=False)
    print("F1-macro OOF (argmax) por modelo:")
    print(base.round(4).to_string(index=False))

    print("\n" + "=" * 72)
    print("DIVERSIDAD DE ERRORES (fraccion de filas donde ambos fallan / alguno falla)")
    rows = []
    for a, b in itertools.combinations(names, 2):
        ea = P[a].argmax(1) != y
        eb = P[b].argmax(1) != y
        both = (ea & eb).mean()
        either = (ea | eb).mean()
        rows.append({"A": a, "B": b, "err_A": ea.mean(), "err_B": eb.mean(),
                     "ambos_fallan": both, "alguno_falla": either,
                     "jaccard_error": both / either if either else np.nan,
                     "desacuerdo_pred": (P[a].argmax(1) != P[b].argmax(1)).mean()})
    div = pd.DataFrame(rows).sort_values("jaccard_error")
    print(div.round(4).to_string(index=False))
    G.save_csv(div, os.path.join(G.ANALYSIS_DIR, "ensemble_diversity.csv"))

    top2 = base.modelo.tolist()[:2]
    print(f"\nCandidatos por fuerza: {top2}")
    cand_pairs = [tuple(top2)]
    # tambien el par mas diverso entre los 4 mejores
    strong = set(base.modelo.tolist()[:4])
    dv = div[div.A.isin(strong) & div.B.isin(strong)].sort_values("jaccard_error")
    if len(dv):
        cand_pairs.append((dv.iloc[0].A, dv.iloc[0].B))

    out = []
    for a, b in dict.fromkeys(cand_pairs):
        print("\n" + "=" * 72)
        print(f"ENSEMBLE {a} + {b}")
        best = None
        for alpha in np.arange(0.0, 1.001, 0.05):
            Pe = alpha * P[a] + (1 - alpha) * P[b]
            s = f1_score(y, Pe.argmax(1), average="macro")
            out.append({"A": a, "B": b, "alpha": float(alpha),
                        "f1_macro_argmax": float(s)})
            if best is None or s > best[1]:
                best = (alpha, s)
        sa = f1_score(y, P[a].argmax(1), average="macro")
        sb = f1_score(y, P[b].argmax(1), average="macro")
        print(f"  mejor alpha={best[0]:.2f} F1m={best[1]:.4f} "
              f"(solo A={sa:.4f}, solo B={sb:.4f})")
        gain = best[1] - max(sa, sb)
        print(f"  ganancia sobre el mejor individual: {gain:+.4f}"
              f"  -> {'ADOPTAR' if gain > 0.005 else 'NO ADOPTAR (no supera el ruido)'}")

        Pe = best[0] * P[a] + (1 - best[0]) * P[b]
        res = G.search_weights(Pe, y, step=0.05, lo=0.5, hi=2.6)
        bm = res.sort_values("f1_macro", ascending=False).iloc[0]
        print(f"  con pesos w={np.round([bm.w0,bm.w1,bm.w2],2)}: "
              f"F1m={bm.f1_macro:.4f} f1_0={bm.f1_0:.4f} rec_0={bm.rec_0:.4f}")

    G.save_csv(pd.DataFrame(out), os.path.join(G.ANALYSIS_DIR, "ensemble_alpha.csv"))


if __name__ == "__main__":
    main()
