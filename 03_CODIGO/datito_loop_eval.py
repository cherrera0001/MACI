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
    }
    # Si hay gráfico, exigir canvas o svg local
    mentions_chart = bool(re.search(r"<canvas|roc|FPR|TPR", live, re.I))
    if mentions_chart:
        g["offline_draw"] = bool(
            re.search(r"<canvas|</svg>|getContext\(\s*['\"]2d['\"]", live, re.I)
        )
    return g


def profundidad_certamen(html: str) -> dict[str, bool]:
    """Gates extra si parece visual de certamen."""
    if "certamen" not in html.lower() and "subpregunta" not in html.lower():
        return {}
    return {
        "bloque_que_paso": bool(re.search(r"Qu[eé]\s+[Pp]as[oó]|Datos de Entrada|figura", html, re.I)),
        "bloque_pasos": bool(re.search(r"[Cc][oó]mo [Ss]e [Rr]esuelve|paso-numero|ol class=\"pasos\"", html)),
        "details_resp": bool(re.search(r'<details[^>]*class="[^"]*resp', html)),
        "errores": bool(re.search(r"[Ee]rror(es)?\s+(t[ií]pico|com[uú]n)|examen castiga", html)),
    }


def score_of(g: dict[str, bool]) -> float:
    if not g:
        return 0.0
    return sum(1 for v in g.values() if v) / len(g)


def evaluate(path: Path) -> dict:
    html = path.read_text(encoding="utf-8", errors="replace")
    g = gates(html)
    g.update(profundidad_certamen(html))
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
