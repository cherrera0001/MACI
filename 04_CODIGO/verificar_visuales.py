#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificación de visuales Datito: template v1 + anti-CDN + profundidad certamen.

Preferir el gate canónico:
  python 03_CODIGO/datito_loop_eval.py --path <html>

Este script mantiene checks de estructura Certamen 3 y delega anti-CDN
con comentarios HTML ignorados (para no fallar el propio template).
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_MARK = "<!-- datito:template:v1 -->"
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
CDN_PATTERNS = [
    r"https?://cdn\.",
    r"googleapis\.com",
    r"fonts\.google",
    r"cdnjs\.com",
    r"unpkg\.com",
    r"jsdelivr\.net",
    r"stackpath\.bootstrapcdn",
]
AI_PURPLE = re.compile(r"#667eea|#764ba2", re.I)


def _live(html: str) -> str:
    return COMMENT_RE.sub("", html)


def check_template(html: str) -> list[str]:
    errs = []
    if TEMPLATE_MARK not in html:
        errs.append("Falta marcador <!-- datito:template:v1 --> (partir del template canónico)")
    return errs


def check_html_no_cdn(html: str) -> list[str]:
    live = _live(html)
    errors = []
    for pattern in CDN_PATTERNS:
        if re.search(pattern, live, re.I):
            errors.append(f"CDN detectado: {pattern}")
    if AI_PURPLE.search(live):
        errors.append("Gradiente AI prohibido (#667eea/#764ba2) — VIZ-FAIL-001")
    if re.search(r'<script[^>]+src=["\']https?://', live, re.I):
        errors.append("script src remoto")
    return errors


def check_structure(html: str) -> dict[str, str]:
    checks = {
        "Indice": r'<div class="nav-indice">',
        "P1a Enunciado": r'id="p1a".*?bloque-titulo">.*?Enunciado',
        "P1a QuePaso": r'id="p1a".*?bloque-titulo">.*?Qu',
        "P1a Pasos": r'id="p1a".*?bloque-titulo">.*?Resuelve',
        "P1a Details": r'id="p1a".*?<details>',
        "P1a Respuesta": r'id="p1a".*?<details class="resp">',
        "P1a Errores": r'id="p1a".*?<div class="checklist">',
        "P2a presente": r'id="p2a"',
        "P2b presente": r'id="p2b"',
        "P2c presente": r'id="p2c"',
        "P3a presente": r'id="p3a"',
        "P3b presente": r'id="p3b"',
        "P3c presente": r'id="p3c"',
        "P3d presente": r'id="p3d"',
    }
    results = {}
    for name, pattern in checks.items():
        results[name] = "OK" if re.search(pattern, html, re.DOTALL) else "FALTA"
    return results


def check_canvas_local(html: str) -> dict[str, bool]:
    live = _live(html)
    has_canvas = bool(re.search(r"<canvas", live, re.I))
    has_chart_cdn = bool(
        re.search(r'<script[^>]+src=["\'][^"\']*chart\.js|cdn\.jsdelivr[^"\']*chart', live, re.I)
    )
    return {"Canvas/SVG local posible": has_canvas, "Sin Chart.js CDN": not has_chart_cdn}


def check_offline(html: str) -> dict[str, bool]:
    live = _live(html)
    return {
        "CSS embebido": bool(re.search(r"<style>.*?</style>", html, re.DOTALL)),
        "Sin CSS externo http": "href=\"http" not in live.lower(),
        "Sin JS externo http": "src=\"http" not in live.lower(),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--path",
        default=str(ROOT / "07_DATITO" / "visual" / "certamen3_examen_fcd2026.html"),
    )
    args = ap.parse_args()
    html_path = Path(args.path)
    if not html_path.is_file():
        print(f"FALTA: {html_path}")
        return 1

    html = html_path.read_text(encoding="utf-8", errors="replace")
    print("=" * 60)
    print(f"VERIFICACION: {html_path}")
    print("=" * 60)

    print("\n0. TEMPLATE CANONICO")
    terr = check_template(html)
    for e in terr or ["OK: marcador template v1"]:
        print(f"  {'X' if terr else 'OK'} {e if terr else e}")

    print("\n1. SIN CDN / ANTI LOOK AI")
    errors = check_html_no_cdn(html)
    if errors:
        for e in errors:
            print(f"  X {e}")
    else:
        print("  OK: Sin CDN ni #667eea/#764ba2 en HTML vivo")

    print("\n2. ESTRUCTURA (Certamen 3 si aplica)")
    struct = check_structure(html)
    for name, result in struct.items():
        print(f"  {'OK' if result == 'OK' else 'X'} {name}")

    print("\n3. GRAFICOS")
    for name, ok in check_canvas_local(html).items():
        print(f"  {'OK' if ok else 'X'} {name}")

    print("\n4. OFFLINE-READY")
    for name, ok in check_offline(html).items():
        print(f"  {'OK' if ok else 'X'} {name}")

    print("\n" + "=" * 60)
    print("Gate KEEP: python 03_CODIGO/datito_loop_eval.py --path <html>")
    print("Workflow: 07_DATITO/07_BITACORA/learning_loop/WORKFLOW_VISUAL.md")
    print("=" * 60)

    bad = bool(terr) or bool(errors)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
