#!/usr/bin/env python3
"""
Prueba visual de los tres certamenes en viewport 390px (móvil).
Verifica: layout responsivo, overflow, visibilidad de elementos clave.
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).parent.parent
CERTAMENES = [
    "07_DATITO/04_EJERCICIOS/certamen_1.html",
    "07_DATITO/04_EJERCICIOS/certamen_2.html",
    "07_DATITO/04_EJERCICIOS/certamen_3.html",
]

def prueba_responsive(archivo, viewport_width=390, viewport_height=800):
    """Prueba un certamen en viewport móvil específico."""
    ruta = (RAIZ / archivo).resolve()
    if not ruta.exists():
        return {"status": "ERROR", "mensaje": f"Archivo no existe: {ruta}"}

    url = f"file:///{ruta}".replace("\\", "/")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": viewport_width, "height": viewport_height})
        page = context.new_page()

        try:
            page.goto(url)

            # Esperar a que cargue completamente
            page.wait_for_load_state("networkidle")

            # Verificaciones clave
            checks = {
                "titulo_visible": page.locator("h1").count() > 0,
                "ficha_bloom_visible": page.locator("text=Ficha Bloom").count() > 0,
                "cierre_visible": page.locator("text=Cierre").count() > 0,
                "preguntas_visibles": page.locator("h2:has-text('Pregunta')").count() > 0,
                "sin_overflow_x": page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 1"),
                "body_width": page.evaluate("document.body.offsetWidth"),
                "viewport_width": viewport_width,
            }

            # Detectar problemas de layout
            problemas = []
            if not checks["sin_overflow_x"]:
                problemas.append("OVERFLOW HORIZONTAL detectado")
            if checks["body_width"] > viewport_width + 5:
                problemas.append(f"Body ancho {checks['body_width']}px > viewport {viewport_width}px")

            # Tomar screenshot
            screenshot_path = f"{RAIZ}/04_CODIGO/screenshot_{Path(archivo).stem}_{viewport_width}px.png"
            page.screenshot(path=screenshot_path)

            browser.close()

            return {
                "archivo": Path(archivo).name,
                "viewport": f"{viewport_width}x{viewport_height}",
                "status": "OK" if not problemas and all(checks.values()) else "REVISAR",
                "checks": checks,
                "problemas": problemas,
                "screenshot": screenshot_path,
            }

        except Exception as e:
            browser.close()
            return {
                "archivo": Path(archivo).name,
                "status": "ERROR",
                "error": str(e),
            }

def main():
    print("\n" + "="*70)
    print("PRUEBA VISUAL: CERTAMENES EN VIEWPORT 390px (MÓVIL)")
    print("="*70 + "\n")

    resultados = []
    for archivo in CERTAMENES:
        print(f"Probando {Path(archivo).name}...", end=" ")
        resultado = prueba_responsive(archivo, viewport_width=390)
        resultados.append(resultado)

        if resultado["status"] == "OK":
            print("[OK]")
        elif resultado["status"] == "REVISAR":
            print("[REVISAR]")
            for p in resultado.get("problemas", []):
                print(f"   - {p}")
        else:
            print("[ERROR]")
            print(f"   {resultado.get('error', resultado.get('mensaje'))}")

    print("\n" + "="*70)
    print("RESULTADOS")
    print("="*70 + "\n")

    for r in resultados:
        print(f"\n{r.get('archivo', 'DESCONOCIDO')}")
        print(f"  Status: {r['status']}")
        if r['status'] == 'OK':
            print(f"  [OK] Ficha Bloom: {r['checks'].get('ficha_bloom_visible')}")
            print(f"  [OK] Cierre: {r['checks'].get('cierre_visible')}")
            print(f"  [OK] Sin overflow: {r['checks'].get('sin_overflow_x')}")
            print(f"  [OK] Body width: {r['checks'].get('body_width')}px (viewport {r['checks'].get('viewport_width')}px)")
        if r.get('screenshot'):
            print(f"  Screenshot: {r['screenshot']}")

    # Resumen
    print("\n" + "="*70)
    ok_count = sum(1 for r in resultados if r['status'] == 'OK')
    print(f"RESUMEN: {ok_count}/{len(resultados)} certamenes OK en 390px")
    print("="*70 + "\n")

    return 0 if all(r['status'] == 'OK' for r in resultados) else 1

if __name__ == "__main__":
    sys.exit(main())
