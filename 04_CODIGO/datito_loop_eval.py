#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Evalúa un HTML Datito contra el template canónico y lecciones VIZ-FAIL-001/002."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_MARK = "<!-- datito:template:v1 -->"
CDN_RE = re.compile(
    r"https?://(cdn\.|cdnjs\.|unpkg\.|jsdelivr\.|fonts\.google|googleapis\.com)",
    re.I,
)
# Solo falla si hay carga real, no si el comentario del template nombra lo prohibido
CHART_CDN_RE = re.compile(
    r'<script[^>]+src=["\'][^"\']*chart\.js|cdn\.jsdelivr[^"\']*chart',
    re.I,
)
AI_GRADIENT_RE = re.compile(
    r"(?:linear-gradient\s*\([^)]*)?#667eea|(?:linear-gradient\s*\([^)]*)?#764ba2",
    re.I,
)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


def _live_html(html: str) -> str:
    """HTML sin comentarios: las lecciones del template no deben disparar FAIL."""
    return COMMENT_RE.sub("", html)


def gates(html: str) -> dict[str, bool]:
    live = _live_html(html)
    g = {
        "template_marker": TEMPLATE_MARK in html,
        "anti_cdn": not bool(CDN_RE.search(live)),
        "anti_chart_cdn": not bool(CHART_CDN_RE.search(live)),
        "anti_ai_gradient": not bool(AI_GRADIENT_RE.search(live)),
        "has_style_embed": bool(re.search(r"<style>.*?</style>", html, re.S)),
        "no_http_script_src": not bool(
            re.search(r'<script[^>]+src=["\']https?://', live, re.I)
        ),
        # La navegación puede sobrevivir a un head truncado: el marcador solo
        # no demuestra que el alumno vea el template (Sprint 01, visual 04).
        "document_structure": bool(re.search(
            r"<head>.*?<title>[^<]+</title>.*?</head>\s*<body[^>]*>", live, re.S | re.I
        )) and len(re.findall(r"<main\b", live, re.I)) == 1
        and len(re.findall(r"<h1\b", live, re.I)) == 1,
        "canonical_root": len(re.findall(r":root\s*\{", live)) == 1
        and bool(re.search(r"--tinta\s*:\s*#1a1a1a\b", live, re.I))
        and bool(re.search(r"--morado\s*:\s*#7c3aed\b", live, re.I)),
        "no_template_placeholders": not any(token in live for token in (
            "TÍTULO DEL CONCEPTO", "fórmula = aquí", "Paso 1…", "Paso 2…"
        )),
    }
    # offline_draw: si hay intención de dibujo (canvas/svg o lib charts), exigir canvas/svg local
    # NO dispara por "roc" en prosa ni "procedimiento"
    has_canvas_or_svg = bool(re.search(r"<canvas|<svg", live, re.I))
    mentions_chart_lib = bool(re.search(r"Chart|Plotly|D3\.js|Vega|matplotlib|ggplot", live, re.I))
    if has_canvas_or_svg or mentions_chart_lib:
        g["offline_draw"] = has_canvas_or_svg or bool(re.search(r"</svg>|getContext\(\s*['\"]2d['\"]", live, re.I))
    return g


def profundidad_certamen(html: str, path: Path | None = None) -> dict[str, bool]:
    """Gates extra si parece visual de certamen."""
    live = _live_html(html)
    headings = " ".join(re.findall(r"<(?:title|h1)\b[^>]*>(.*?)</(?:title|h1)>", live, re.S | re.I))
    identity = headings + " " + (path.stem if path else "")
    # Una cita o enlace al certamen no convierte una lección en examen.
    if not re.search(r"\b(?:certamen|examen|subpregunta)(?=\b|\d|_)", identity, re.I):
        return {}
    return {
        "bloque_que_paso": bool(re.search(r"Qu[eé]\s+[Pp]as[oó]|Datos de Entrada|figura", live, re.I)),
        "bloque_pasos": bool(re.search(r"[Cc][oó]mo [Ss]e [Rr]esuelve|paso-numero|ol class=\"pasos\"", live)),
        "details_resp": bool(re.search(r'<details[^>]*class="[^"]*resp', live)),
        "errores": bool(re.search(r"[Ee]rror(es)?\s+(t[ií]pico|com[uú]n)|examen castiga", live)),
    }


def score_of(g: dict[str, bool]) -> float:
    if not g:
        return 0.0
    return sum(1 for v in g.values() if v) / len(g)


def evaluate(path: Path) -> dict:
    html = path.read_text(encoding="utf-8", errors="replace")
    g = gates(html)
    g.update(profundidad_certamen(html, path))
    s = score_of(g)
    return {
        "path": str(path),
        "score": round(s, 4),
        "keep_eligible": s >= 1.0 and g.get("template_marker", False) and g.get("anti_cdn", False),
        "gates": g,
        "lessons_to_respect": ["VIZ-FAIL-001", "VIZ-FAIL-002"],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True, help="HTML a evaluar")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    path = Path(args.path)
    if not path.is_file():
        print(f"FALTA: {path}", file=sys.stderr)
        return 2
    result = evaluate(path)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"path={result['path']}")
        print(f"score={result['score']} keep_eligible={result['keep_eligible']}")
        for k, v in result["gates"].items():
            print(f"  {'OK' if v else 'FAIL'}  {k}")
    return 0 if result["keep_eligible"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
