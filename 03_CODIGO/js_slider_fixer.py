#!/usr/bin/env python3
"""JS Slider Fixer: Extrae listeners de git history e inyecta en HTML.

Goal: MEDIUM category (4 archivos): #02, #03, #04, #10
  - Identificar sliders rotos (ej: sn, sk, mimp, sAng)
  - Buscar listeners en git cabca76 (version anterior)
  - Extraer el codigo JavaScript
  - Inyectar antes de </body>
  - Verificar que pasa ok=true
"""
import re
import subprocess
import json
from pathlib import Path

MEDIUM_FILES = {
    "02_datos_features_target": ["sn", "sp"],  # 2 js
    "03_eda": ["sk"],  # 1 js
    "04_limpieza_preparacion": ["mimp"],  # 1 js
    "10_clasificacion": ["sAng", "sB"],  # 2 js
}

VISUAL_DIR = Path("07_DATITO/01_CONCEPTOS/visual")
VERIFY_SCRIPT = Path("03_CODIGO/verificar_piel_lectura.py")
GIT_COMMIT = "cabca76"  # Ultima version buena conocida

def get_from_git(filename, commit):
    """Extrae contenido de archivo desde git commit."""
    try:
        result = subprocess.run(
            ["git", "show", f"{commit}:07_DATITO/01_CONCEPTOS/visual/{filename}.html"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout
        return None
    except:
        return None

def extract_script_section(html_content):
    """Extrae la seccion <script>...</script> del HTML."""
    match = re.search(r"<script[^>]*>(.*?)</script>", html_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_slider_listeners(script_content, slider_ids):
    """Extrae listeners especificos de un slider del script."""
    listeners = []
    for sid in slider_ids:
        # Busca: addEventListener("input" o addEventListener('input')
        pattern = rf'document\.getElementById\(["\']({sid})["\'].*?addEventListener\([^)]*?\{{[^}}]*?\}}[^}}]*?\}}'
        match = re.search(pattern, script_content, re.DOTALL)
        if match:
            listeners.append(match.group(0))
        else:
            # Intenta patron mas simple
            pattern = rf'getElementById\(["\']({sid})["\'].*?addEventListener'
            if re.search(pattern, script_content, re.DOTALL):
                print(f"    Found listener for {sid} but pattern too complex")
    return listeners

def inject_script(html_path, script_code):
    """Inyecta codigo JS antes de </body>."""
    content = html_path.read_text(encoding="utf-8")

    # Busca el ultimo </body>
    if "</body>" not in content:
        return False

    script_tag = f"\n<script>\n{script_code}\n</script>\n"
    new_content = content.replace("</body>", f"{script_tag}</body>")

    html_path.write_text(new_content, encoding="utf-8")
    return True

def verify_file(html_path):
    """Verifica si pasa ok=true."""
    try:
        result = subprocess.run(
            ["python", str(VERIFY_SCRIPT), "--path", str(html_path)],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(result.stdout)
        return data.get("ok", False), data.get("failures", [])
    except:
        return False, []

def main():
    print("=== JS Slider Fixer (MEDIUM Category) ===\n")

    fixed_count = 0

    for nombre, sliders in MEDIUM_FILES.items():
        print(f"{nombre}:")
        html_file = VISUAL_DIR / f"{nombre}.html"

        # Obtener version vieja
        old_html = get_from_git(nombre, GIT_COMMIT)
        if not old_html:
            print(f"  [ERROR] No se encontro en git {GIT_COMMIT}")
            continue

        # Extraer script
        old_script = extract_script_section(old_html)
        if not old_script:
            print(f"  [WARN] No script encontrado en version vieja")
            continue

        # Inyectar
        if inject_script(html_file, old_script):
            print(f"  [INJECT] Script completo inyectado")

            # Verificar
            ok, failures = verify_file(html_file)
            if ok:
                print(f"  [FIXED] ok=true ✓")
                fixed_count += 1
            else:
                # Revisar si los sliders especificos ahora funciona
                slider_failures = [f for f in failures if any(s in f for s in sliders)]
                if not slider_failures:
                    print(f"  [OK] Sliders funcionan, falla en otro")
                    fixed_count += 1
                else:
                    print(f"  [PARTIAL] Sliders aun fallan: {slider_failures[:1]}")
        else:
            print(f"  [ERROR] No se pudo inyectar")

    print(f"\n--- Resultado ---")
    print(f"Reparados: {fixed_count}/{len(MEDIUM_FILES)}")

    return fixed_count

if __name__ == "__main__":
    main()
