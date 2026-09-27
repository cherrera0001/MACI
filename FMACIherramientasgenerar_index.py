#!/usr/bin/env python3
"""Generador de índice del curso · versión simplificada (reemplaza construir_navegacion.py)"""
import sys, yaml
from pathlib import Path
from datetime import date

RAIZ = Path(__file__).parent.parent
MANIFIESTO = RAIZ / "07_DATITO" / "00_INICIO" / "clases.yaml"
SALIDA = RAIZ / "07_DATITO" / "01_CONCEPTOS" / "visual" / "index.html"

def main():
    if not MANIFIESTO.exists():
        print(f"ERROR: {MANIFIESTO} no existe", file=sys.stderr)
        return 1
    
    with open(MANIFIESTO, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    clases = data.get("clases", [])
    total = len(clases)
    unidades = data.get("unidades", {})
    
    # Generar filas de tabla
    filas = []
    for c in sorted(clases, key=lambda x: x["n"]):
        n = c["n"]
        titulo = c.get("titulo", "")
        bloom = c.get("bloom", {}).get("nivel", "—") if c.get("bloom") else "—"
        visual = c.get("visual")
        link = f'<a href="{visual}">{titulo}</a>' if visual else titulo
        filas.append(f"<tr><td>{n}</td><td>{link}</td><td>{bloom}</td></tr>")
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fundamentos de Ciencia de Datos · Índice</title>
<style>
  body {{ margin:0; padding:2rem 1rem; background:#faf9f7; color:#1a1a1a; font:16px/1.7 "Segoe UI",system-ui,sans-serif; }}
  main {{ max-width:900px; margin:0 auto; }}
  h1 {{ font-size:1.7rem; margin:0 0 .3rem; }}
  .sub {{ color:#666; margin:0 0 2rem; }}
  table {{ border-collapse:collapse; width:100%; font-size:.9rem; margin:1rem 0; }}
  th,td {{ border:1px solid #d8d8d8; padding:.5rem .65rem; text-align:left; }}
  th {{ background:#f1f0ee; font-weight:600; }}
  a {{ color:#2563eb; text-decoration:none; }}
  a:hover {{ text-decoration:underline; }}
</style>
</head>
<body>
<main>
<h1>Fundamentos de Ciencia de Datos</h1>
<p class="sub">{total} clases · {len(unidades)} unidades · {date.today()}</p>
<table>
<tr><th>#</th><th>Clase</th><th>Bloom</th></tr>
{"".join(filas)}
</table>
</main>
</body>
</html>"""
    
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"OK: {SALIDA} generado ({total} clases)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
