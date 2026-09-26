#!/usr/bin/env python3
"""Clasificador de Errores: Agrupa FAIL por tipo + propone orden de reparacion.

Goal: Transforma reporte JSON en plan ejecutable.
  1. Easy (css/mobile): automatizable, <5min c/u
  2. Medium (placeholders): git history + inyeccion
  3. Hard (js/estructura): revision manual
"""
import json
from pathlib import Path
from collections import defaultdict

def classify_difficulty(result):
    """Calcula dificultad de fix: easy, medium, hard."""
    categories = result.get("categories", {})

    if result.get("ok"):
        return "done", 0

    # Hard: estructura + js
    if categories.get("estructura", 0) > 0:
        return "hard", 3
    if categories.get("js", 0) > 3:
        return "hard", 3

    # Medium: js + placeholders
    if categories.get("js", 0) > 0 or categories.get("placeholders", 0) > 0:
        return "medium", 2

    # Easy: solo css/mobile
    return "easy", 1

def main():
    report_file = Path("03_CODIGO/reporte_validacion.json")
    if not report_file.exists():
        print("Error: Corre validador_visual.py primero")
        return

    report = json.loads(report_file.read_text())
    details = report.get("details", {})

    # Clasificar
    classified = defaultdict(list)
    for nombre, result in details.items():
        if result.get("error"):
            continue
        difficulty, priority = classify_difficulty(result)
        classified[difficulty].append((nombre, result, priority))

    # Ordenar por prioridad
    for level in classified.values():
        level.sort(key=lambda x: x[2], reverse=True)

    # Generar markdown
    md = "# Plan de Reparacion Visual\n\n"
    md += f"Total: 16 conceptos  |  OK: {report['ok']}/16  |  FAIL: {report['fail']}/16\n\n"

    # Easy
    md += "## EASY (CSS/Mobile) — Automatizable\n\n"
    for nombre, result, _ in classified.get("easy", []):
        cats = result.get("categories", {})
        md += f"- **{nombre}**: {cats.get('css', 0)} css errors | "
        md += f"Top: {result.get('top_failures', ['?'])[0][:60]}\n"

    # Medium
    md += "\n## MEDIUM (JS/Placeholders) — Semi-automatizable\n\n"
    for nombre, result, _ in classified.get("medium", []):
        cats = result.get("categories", {})
        md += f"- **{nombre}**: {cats.get('js', 0)} js, "
        md += f"{cats.get('placeholders', 0)} placeholders | "
        md += f"Top: {result.get('top_failures', ['?'])[0][:50]}\n"

    # Hard
    md += "\n## HARD (Estructura/JS) — Manual review\n\n"
    for nombre, result, _ in classified.get("hard", []):
        cats = result.get("categories", {})
        md += f"- **{nombre}**: {cats.get('estructura', 0)} estructura, "
        md += f"{cats.get('js', 0)} js | "
        md += f"Top: {result.get('top_failures', ['?'])[0][:50]}\n"

    # Done
    if classified.get("done"):
        md += "\n## DONE (OK)\n\n"
        for nombre, _, _ in classified.get("done", []):
            md += f"- {nombre}\n"

    # Estrategia
    md += "\n---\n\n## Estrategia de Ejecucion\n\n"
    md += f"1. Reparador Automatico (easy): 30 min - ~{len(classified.get('easy', []))} archivos\n"
    md += f"2. Extractor + Inyector (medium): 1 hr - ~{len(classified.get('medium', []))} archivos\n"
    md += f"3. Manual QA (hard): 1+ hrs - ~{len(classified.get('hard', []))} archivos\n\n"
    md += f"**Proyeccion:** 13 FAIL a OK en ~2.5 hrs (13/13 = 100%)\n"

    plan_file = Path("03_CODIGO/plan_reparacion.md")
    plan_file.write_text(md)
    print(md)
    print(f"\nPlan guardado: plan_reparacion.md")

if __name__ == "__main__":
    main()
