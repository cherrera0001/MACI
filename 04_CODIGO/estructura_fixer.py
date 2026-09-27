#!/usr/bin/env python3
"""Estructura Fixer: Repara HTML malformados (#14, #18).

Goal: HARD category
  #14 arboles_decision: Falta <h1>, <p class="sub">, <main>
  #18 redes_neuronales: Head/body incompletos

Estrategia:
  1. Lee archivo roto
  2. Extrae <title> para deducir h1
  3. Busca primer <main> o lo agrega
  4. Inserta h1 + .sub despues de nav
"""
import re
from pathlib import Path
from collections import defaultdict

HARD_FILES = {
    "14_arboles_decision": {
        "h1": "Arboles de Decision y Ensambles",
        "sub": "Complejos, interpretables, sesgo-varianza"
    },
    "18_redes_neuronales": {
        "h1": "Redes Neuronales y Deep Learning",
        "sub": "Capas, activaciones, backpropagation"
    },
}

VISUAL_DIR = Path("07_DATITO/01_CONCEPTOS/visual")

def fix_estructura(nombre, h1_text, sub_text):
    """Repara estructura HTML de un archivo."""
    html_file = VISUAL_DIR / f"{nombre}.html"
    content = html_file.read_text(encoding="utf-8")

    # Verificar si ya tiene h1 y main adecuados
    has_h1 = f"<h1>{h1_text}</h1>" in content
    if has_h1:
        return "ya_existe", None

    # Buscar <!-- datito:nav:fin -->
    nav_fin = "<!-- datito:nav:fin -->"
    if nav_fin not in content:
        return "error_nav", None

    # Buscar <main>
    has_main = "<main>" in content

    if not has_main:
        # Agregar <main> despues de <body>
        content = re.sub(
            r"(<body>)",
            r"\1\n<main>",
            content
        )
        # Y cerrar antes de </body>
        content = re.sub(
            r"(</body>)",
            r"</main>\n\1",
            content
        )

    # Inserta h1 + .sub despues de nav:fin
    header = f'\n<h1>{h1_text}</h1>\n<p class="sub">{sub_text}</p>\n'
    content = content.replace(nav_fin, nav_fin + header, 1)

    html_file.write_text(content, encoding="utf-8")
    return "fixed", None

def main():
    print("=== Estructura Fixer (HARD Category) ===\n")

    fixed_count = 0

    for nombre, meta in HARD_FILES.items():
        h1 = meta["h1"]
        sub = meta["sub"]

        status, error = fix_estructura(nombre, h1, sub)

        if status == "ya_existe":
            print(f"{nombre:30} [SKIP] Estructura correcta")
        elif status == "error_nav":
            print(f"{nombre:30} [ERROR] No encontro <!-- datito:nav:fin -->")
        elif status == "fixed":
            print(f"{nombre:30} [FIXED] Agregado <main>, h1, .sub")
            fixed_count += 1
        else:
            print(f"{nombre:30} [ERROR] {error}")

    print(f"\n--- Resultado ---")
    print(f"Reparados: {fixed_count}/{len(HARD_FILES)}")

    return fixed_count == len(HARD_FILES)

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
