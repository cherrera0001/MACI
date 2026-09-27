#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluación en batch de todos los HTML Datito.
Genera tabla CSV con status de cada archivo.
"""

import subprocess
import sys
import io
from pathlib import Path
import re

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DATITO_DIR = ROOT / "07_DATITO"

# Archivos a procesar (excluir templates e índice)
EXCLUDE = {"_TEMPLATE_CANONICO.html", "00_index.html"}

def find_html_files():
    """Encuentra todos los HTML bajo 07_DATITO"""
    html_files = []
    for html in DATITO_DIR.rglob("*.html"):
        if html.name not in EXCLUDE:
            html_files.append(html)
    return sorted(html_files)

def evaluate_file(html_path):
    """Ejecuta datito_loop_eval.py en un archivo"""
    try:
        result = subprocess.run(
            [sys.executable, "03_CODIGO/datito_loop_eval.py", "--path", str(html_path)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10
        )
        # Analizar output para extraer score
        if "LISTO" in result.stdout or "Gate KEEP" in result.stdout:
            return "KEEP", result.returncode == 0
        elif "X" in result.stdout or result.returncode != 0:
            return "DISCARD", False
        else:
            return "UNKNOWN", None
    except Exception as e:
        return f"ERROR: {e}", False

def main():
    html_files = find_html_files()

    print("=" * 80)
    print("EVALUACION EN BATCH: Datito Visual Migration to Template v1")
    print("=" * 80)
    print(f"\nTotal archivos a evaluar: {len(html_files)}\n")

    results = []
    keep_count = 0
    discard_count = 0

    for i, html_path in enumerate(html_files, 1):
        relative_path = html_path.relative_to(DATITO_DIR)
        status, success = evaluate_file(html_path)

        # Contar
        if status == "KEEP":
            keep_count += 1
        elif status == "DISCARD":
            discard_count += 1

        results.append({
            "num": i,
            "archivo": str(relative_path),
            "status": status,
            "success": "✓" if success else "✗"
        })

        # Mostrar progreso
        print(f"[{i:2d}/{len(html_files)}] {status:8s} {relative_path}")

    # Resumen
    print("\n" + "=" * 80)
    print("RESUMEN")
    print("=" * 80)
    print(f"KEEP (ya cumplen template v1):     {keep_count:3d}")
    print(f"DISCARD (necesitan migración):     {discard_count:3d}")
    print(f"TOTAL:                             {len(html_files):3d}")
    print("=" * 80)

    # Archivos a migrar (ordenados)
    print("\nARCHIVOS A MIGRAR (DISCARD):")
    print("-" * 80)
    for r in results:
        if r["status"] == "DISCARD":
            print(f"  • {r['archivo']}")

    print("\n" + "=" * 80)
    print("PRÓXIMOS PASOS:")
    print("-" * 80)
    print("1. Para cada archivo DISCARD:")
    print("   python 03_CODIGO/datito_loop_once.py --path <archivo> --hypothesis 'migrate to template v1'")
    print("\n2. O ejecutar la migración automática:")
    print("   python 03_CODIGO/datito_migracion_masiva.py")
    print("=" * 80)

if __name__ == "__main__":
    main()
