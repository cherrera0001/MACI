#!/usr/bin/env python3
"""Tablero del proyecto generado desde GitHub Projects (sustituto de las vistas).

GitHub no expone la creacion de vistas de Projects V2 por API (verificado,
#70). Este script produce lo que las vistas mostrarian: un markdown agrupado
por epica con estado, tipo, prioridad y proceso de cada item. Se commitea
como docs/gestion/tablero.md y se refresca con:

  python 03_SCRIPTS/actualizar_tablero.py

Requiere: gh autenticado. Sin red, deja el archivo anterior intacto.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "docs" / "gestion" / "tablero.md"
PROYECTO = "PVT_kwHOASvtSs4Bkwxr"

Q = """query {
  node(id: "%s") {
    ... on ProjectV2 {
      items(first: 100) {
        nodes {
          content { ... on Issue { number title state } }
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                name field { ... on ProjectV2SingleSelectField { name } }
              }
            }
          }
        }
      }
    }
  }
}""" % PROYECTO


def _gql() -> dict:
    r = subprocess.run(["gh", "api", "graphql", "-f", f"query={Q}"],
                       capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[:200])
    return json.loads(r.stdout)


def main() -> int:
    datos = _gql()["data"]["node"]["items"]["nodes"]
    items = {}
    for n in datos:
        c = n.get("content") or {}
        if not c.get("number"):
            continue
        campos = {}
        for fv in (n.get("fieldValues") or {}).get("nodes") or []:
            if fv and fv.get("field") and fv.get("name"):
                campos[fv["field"]["name"]] = fv["name"]
        items[c["number"]] = {
            "titulo": c["title"], "cerrado": c["state"] == "CLOSED",
            "tipo": campos.get("Tipo", ""), "prioridad": campos.get("Prioridad", ""),
            "proceso": campos.get("Proceso", ""), "status": campos.get("Status", ""),
        }

    # jerarquia: epica = issues tipo Épica; el resto se ordena por prioridad
    epica = {n: i for n, i in items.items() if i["tipo"] == "Épica"}
    prioridad = {"P0": 0, "P1": 1, "P2": 2, "": 3}

    def fila(n: int, i: dict) -> str:
        marca = "✅" if i["cerrado"] else "⬜"
        partes = [p for p in (i["tipo"], i["prioridad"], i["proceso"]) if p]
        return (f"| {marca} #{n} | {i['titulo'].replace('|', '·')} | "
                f"{i['status'] or '—'} | {' · '.join(partes) or '—'} |")

    lineas = ["# Tablero del proyecto (generado)",
              "",
              "> Generado por `03_SCRIPTS/actualizar_tablero.py` desde GitHub Projects. "
              "**No editar a mano.**",
              "",
              "| Estado | Ítem | Status | Tipo · Prioridad · Proceso |",
              "|---|---|---|---|"]
    for n in sorted(epica, key=lambda n: prioridad.get(epica[n]["prioridad"], 3)):
        i = epica[n]
        lineas.append(fila(n, i))
    lineas += ["", "## Ítems sueltos (no épicas)", "",
               "| Estado | Ítem | Status | Tipo · Prioridad · Proceso |",
               "|---|---|---|---|"]
    sueltos = [n for n, i in items.items() if i["tipo"] != "Épica"]
    for n in sorted(sueltos, key=lambda n: (prioridad.get(items[n]["prioridad"], 3), n)):
        lineas.append(fila(n, items[n]))
    abiertos = sum(1 for i in items.values() if not i["cerrado"])
    lineas += ["", f"**{len(items)} ítems · {abiertos} abiertos.**", ""]
    SALIDA.write_text("\n".join(lineas), encoding="utf-8")
    print(f"tablero.md: {len(items)} items ({abiertos} abiertos)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as e:
        print(f"sin acceso a la API ({e}); se conserva el tablero anterior", file=sys.stderr)
        sys.exit(1)
