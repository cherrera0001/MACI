#!/usr/bin/env python3
"""Audita rutas canónicas del orden documental MACI. Solo lectura. Exit 1 si falta algo."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "01_DOCUMENTACION/00_INDICE_GENERAL.md",
    "01_DOCUMENTACION/00_ORDEN_DOCUMENTAL.md",
    "01_DOCUMENTACION/DIAGNOSTICO_DRIFT.md",
    "01_DOCUMENTACION/01_CERTAMEN2/00_LEEME.md",
    "01_DOCUMENTACION/01_CERTAMEN2/AUDITORIA_FORENSE_FECHAS_DOCUMENTOS.md",
    "01_DOCUMENTACION/02_CURSO/00_LEEME.md",
    "01_DOCUMENTACION/03_PROYECTO_MELBOURNE/00_LEEME.md",
    "01_DOCUMENTACION/04_DESAFIO_GALAXYZOO/00_LEEME.md",
    "01_DOCUMENTACION/05_HISTORICO/00_LEEME.md",
    "01_DOCUMENTACION/06_CERTAMEN1/00_LEEME.md",
    "06_ENTREGABLES/INFORME_MODELO_FCD_P3.md",
    "06_ENTREGABLES/PITCH_HITO2_REVISION.md",
    "05_RESULTADOS/resultados_temporal.json",
    "07_GUILLITO/00_LEEME.md",
    "08_PRACTICA/00_LEEME.md",
    "09_CLASES/00_LEEME.md",
    "02_PROYECTO_FCD/Hito1",
    "spec.md",
    ".mcp.json",
]

# Rutas que NO deben usarse como canónicas (aviso si existen como única copia — solo informativo)
LEGACY_WARN = [
    "DOCUMENTACION",
    "INFORME_MODELO_FCD_P3.md",  # raíz
    "PITCH_HITO2_REVISION.md",   # raíz
]


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    print(f"ROOT={ROOT}")
    if missing:
        print("FALTAN rutas canónicas:")
        for p in missing:
            print(f"  - {p}")
        code = 1
    else:
        print(f"OK: {len(REQUIRED)} rutas canónicas presentes.")
        code = 0

    for p in LEGACY_WARN:
        path = ROOT / p
        if path.exists():
            if p in ("INFORME_MODELO_FCD_P3.md", "PITCH_HITO2_REVISION.md"):
                print(f"AVISO: existe copia en raíz `{p}` — canónico está en 06_ENTREGABLES/")
            elif p == "DOCUMENTACION":
                print("AVISO: carpeta legacy `DOCUMENTACION/` (usar `01_DOCUMENTACION/`).")
    return code


if __name__ == "__main__":
    sys.exit(main())
