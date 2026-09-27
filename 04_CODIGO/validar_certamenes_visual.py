#!/usr/bin/env python3
"""Validación visual de certámenes en Playwright - verifica que Ficha Bloom y Cierre estén presentes"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def validate_certamen(file_path, width=1280, height=800):
    """Valida visualmente un archivo de certamen"""

    file_path = Path(file_path).resolve()
    if not file_path.exists():
        return {"status": "ERROR", "message": f"Archivo no existe: {file_path}"}

    url = f"file:///{file_path}".replace("\\", "/")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": width, "height": height})
        page = context.new_page()
        page.goto(url)

        # Buscar elementos clave
        has_ficha_bloom = page.locator("b:has-text('Ficha Bloom')").count() > 0
        has_cierre = page.locator("h2:has-text('Cierre')").count() > 0 or page.locator("text='Cierre de la Clase'").count() > 0
        has_peligro = page.locator("div.peligro").count() > 0

        # Validar que la ficha Bloom tiene elementos anidados
        ficha_complete = False
        if has_ficha_bloom:
            ficha_element = page.locator("div.ficha")
            if ficha_element.count() > 0:
                content = ficha_element.first.inner_html()
                ficha_complete = "Evidencia de aprendizaje" in content and "Criterio de dominio" in content and "Actividad final" in content

        browser.close()

    return {
        "status": "PASS" if (has_ficha_bloom and has_cierre and has_peligro and ficha_complete) else "FAIL",
        "viewport": f"{width}x{height}",
        "ficha_bloom": has_ficha_bloom,
        "ficha_complete": ficha_complete,
        "cierre": has_cierre,
        "peligro": has_peligro
    }

def main():
    """Valida los tres certámenes"""
    certamenes = [
        "F:\\MACI\\07_DATITO\\04_EJERCICIOS\\certamen_1.html",
        "F:\\MACI\\07_DATITO\\04_EJERCICIOS\\certamen_2.html",
        "F:\\MACI\\07_DATITO\\04_EJERCICIOS\\certamen_3.html"
    ]

    print("=== VALIDACIÓN VISUAL DE CERTÁMENES ===\n")

    all_pass = True
    for certamen in certamenes:
        print(f"Validando: {Path(certamen).name}")

        for viewport in [1280, 390]:
            result = validate_certamen(certamen, width=viewport)
            print(f"  {viewport}px: {result['status']}")
            if result['status'] == 'FAIL':
                print(f"    - Ficha Bloom: {result['ficha_bloom']} (completa: {result['ficha_complete']})")
                print(f"    - Cierre: {result['cierre']}")
                print(f"    - Peligro: {result['peligro']}")
                all_pass = False
        print()

    if all_pass:
        print("✅ TODOS LOS CERTÁMENES VALIDADOS VISUALMENTE")
        return 0
    else:
        print("❌ ERRORES EN VALIDACIÓN VISUAL")
        return 1

if __name__ == "__main__":
    sys.exit(main())
