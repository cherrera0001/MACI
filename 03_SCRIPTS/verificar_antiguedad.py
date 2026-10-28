#!/usr/bin/env python3
"""Candidatos a re-verificacion: conceptos dominados/comprendidos que envejecen.

El contrato (spec.md §3, Re-verificacion) exige re-preguntar lo ya dado por
sabido: sin esto el registro solo sube y deja de medir. Este script lista los
conceptos cuya `ultima_verificacion` supera el umbral (por defecto 21 dias).
Falla el fallo los mueve a REQUIERE_REPASO en la sesion; aqui solo se lista.

USO
  python 03_SCRIPTS/verificar_antiguedad.py                 # texto, umbral 21
  python 03_SCRIPTS/verificar_antiguedad.py --dias 14
  python 03_SCRIPTS/verificar_antiguedad.py --json
  python 03_SCRIPTS/verificar_antiguedad.py --course fcd-2026-2 --learner cristobal_herrera
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from context_manager import add_context_args, get_context  # noqa: E402

ESTADOS_RIESGO = {"COMPRENDIDO", "DOMINADO"}
UMBRAL_POR_DEFECTO = 21


def _fecha(valor):
    if isinstance(valor, datetime.datetime):
        return valor.date()
    if isinstance(valor, datetime.date):
        return valor
    if isinstance(valor, str):
        return datetime.date.fromisoformat(valor[:10])
    return None


def candidatos(progreso_doc, hoy=None, dias=UMBRAL_POR_DEFECTO):
    """Conceptos con ultima_verificacion mas antigua que `dias`. Puro."""
    hoy = hoy or datetime.date.today()
    out = []
    for c in progreso_doc.get("conceptos") or []:
        if c.get("estado") not in ESTADOS_RIESGO:
            continue
        f = _fecha(c.get("ultima_verificacion"))
        if f is None:
            out.append({"id": c["id"], "estado": c["estado"],
                        "ultima_verificacion": None, "dias": None})
        elif (hoy - f).days > dias:
            out.append({"id": c["id"], "estado": c["estado"],
                        "ultima_verificacion": f.isoformat(), "dias": (hoy - f).days})
    return out


def main():
    parser = argparse.ArgumentParser(description="Lista candidatos a re-verificacion.")
    add_context_args(parser)
    parser.add_argument("--dias", type=int, default=UMBRAL_POR_DEFECTO)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    ctx = get_context(course_id=args.course, learner_id=args.learner)
    pro = yaml.safe_load(open(ctx.paths.progreso, encoding="utf-8"))
    nombres = {}
    try:
        cur = yaml.safe_load(open(ctx.paths.curriculum, encoding="utf-8"))
        nombres = {c["id"]: c.get("nombre", c["id"]) for c in cur.get("conceptos") or []}
    except OSError:
        pass

    filas = candidatos(pro, dias=args.dias)
    if args.json:
        print(json.dumps(filas, ensure_ascii=False))
        sys.exit(0)
    if not filas:
        print(f"Ningun candidato: todo {sorted(ESTADOS_RIESGO)} verificado hace <= {args.dias} dias.")
        return
    print(f"{len(filas)} candidato(s) con ultima_verificacion > {args.dias} dias:")
    for f in sorted(filas, key=lambda x: -(x["dias"] or 10**6)):
        fecha = f["ultima_verificacion"] or "nunca"
        print(f"- {f['id']} ({nombres.get(f['id'], '')}) — {f['estado']} · {fecha}"
              + (f" · hace {f['dias']} dias" if f["dias"] is not None else ""))


if __name__ == "__main__":
    main()
