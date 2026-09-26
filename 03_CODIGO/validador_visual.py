#!/usr/bin/env python3
"""Validador Visual Batch: Clasifica 16 conceptos por tipo de error.

Goal: Categoriza cada HTML en 5 tipos:
  - estructura (no main, h1, duplicados)
  - js (sliders no funcionan)
  - css (mobile overflow, colores, CDN)
  - placeholders (contenido sin reemplazar)
  - ok (pasa verificacion)
"""
import json
import subprocess
from pathlib import Path
from collections import defaultdict

CONCEPTOS = [
    "01_fundamentos", "02_datos_features_target", "03_eda",
    "04_limpieza_preparacion", "05_train_validation_test",
    "06_validacion_cruzada", "07_generalizacion",
    "08_overfitting_underfitting", "09_regresion",
    "10_clasificacion", "11_matriz_confusion",
    "12_metricas_clasificacion", "13_roc_auc",
    "14_arboles_decision", "18_redes_neuronales", "19_deep_learning"
]

VISUAL_DIR = Path("07_DATITO/01_CONCEPTOS/visual")
VERIFY_SCRIPT = Path("03_CODIGO/verificar_piel_lectura.py")

def categorize_errors(failures):
    """Clasifica failures en categorias."""
    categories = {
        "estructura": [],
        "js": [],
        "css": [],
        "placeholders": [],
    }

    for failure in failures:
        if any(x in failure.lower() for x in ["main", "h1", "head", "body"]):
            categories["estructura"].append(failure)
        elif "slider" in failure.lower() or "no cambia" in failure.lower():
            categories["js"].append(failure)
        elif any(x in failure.lower() for x in ["desbordamiento", "overflow", "color", "cdn", "googleapis"]):
            categories["css"].append(failure)
        elif any(x in failure for x in ["TITULO", "formula", "Paso 1", "Paso 2"]):
            categories["placeholders"].append(failure)
        else:
            categories["css"].append(failure)

    return categories

def validate_one(nombre):
    """Valida un concepto, retorna {ok, failures, categories}."""
    html_file = VISUAL_DIR / f"{nombre}.html"
    if not html_file.exists():
        return None

    try:
        result = subprocess.run(
            ["python", str(VERIFY_SCRIPT), "--path", str(html_file)],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(result.stdout)
        failures = data.get("failures", [])
        ok = data.get("ok", False)
        categories = categorize_errors(failures)

        return {
            "name": nombre,
            "ok": ok,
            "failures_count": len(failures),
            "categories": {k: len(v) for k, v in categories.items()},
            "top_failures": failures[:2],
        }
    except Exception as e:
        return {"name": nombre, "error": str(e)}

def main():
    print("=== Validador Visual Batch ===\n")
    print(f"Verificando {len(CONCEPTOS)} conceptos...\n")

    results = {}
    summary = defaultdict(int)

    for nombre in CONCEPTOS:
        result = validate_one(nombre)
        if result:
            results[nombre] = result
            if result.get("ok"):
                status = "[OK]"
                summary["ok"] += 1
            else:
                status = f"[FAIL] {result.get('failures_count')} errors"
                summary["fail"] += 1

            print(f"{nombre:30} {status}")

    print(f"\n--- Resumen ---")
    print(f"  OK:   {summary['ok']}/16")
    print(f"  FAIL: {summary['fail']}/16")

    print(f"\n--- Errores por categoria ---")
    category_totals = defaultdict(int)
    for result in results.values():
        if not result.get("ok"):
            for cat, count in result.get("categories", {}).items():
                if count > 0:
                    category_totals[cat] += 1

    for cat, count in sorted(category_totals.items(), key=lambda x: -x[1]):
        print(f"  {cat:15} {count:2} archivos")

    report = {
        "timestamp": str(Path.cwd()),
        "total": len(CONCEPTOS),
        "ok": summary["ok"],
        "fail": summary["fail"],
        "by_category": dict(category_totals),
        "details": results,
    }

    report_file = Path("03_CODIGO/reporte_validacion.json")
    report_file.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nReporte guardado: reporte_validacion.json")

    return summary["ok"], summary["fail"]

if __name__ == "__main__":
    ok_count, fail_count = main()
