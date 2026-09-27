#!/usr/bin/env python3
"""CSS Mobile Fixer: Inyecta media queries para viewport 390px.

Goal: EASY category (4 archivos): 05, 07, 11, 19
  - Agregar @media(max-width:600px) si falta
  - Verificar post-fix
  - Reportar resultados
"""
import json
import re
import subprocess
from pathlib import Path

EASY_FILES = [
    "05_train_validation_test",
    "07_generalizacion",
    "11_matriz_confusion",
    "19_deep_learning",
]

VISUAL_DIR = Path("07_DATITO/01_CONCEPTOS/visual")
VERIFY_SCRIPT = Path("03_CODIGO/verificar_piel_lectura.py")

MEDIA_QUERY = "@media(max-width:600px){body{padding:0.6rem 0.4rem;font-size:14px}main{margin:0;padding:0}table{font-size:0.85rem;display:block;overflow-x:auto}canvas{max-width:100%}div{max-width:100%}}"

def inject_media_query(html_path):
    """Inyecta media query si falta."""
    content = html_path.read_text(encoding="utf-8")

    if "@media(max-width:" in content:
        return "ya_existe", content

    # Busca el ultimo </style> y agrega antes
    new_content = re.sub(
        r"(</style>)",
        f"  {MEDIA_QUERY}\n\\1",
        content,
        count=1
    )

    if new_content == content:
        return "error", content

    return "inyectado", new_content

def verify_file(html_path):
    """Verifica si pasa ok=true."""
    try:
        result = subprocess.run(
            ["python", str(VERIFY_SCRIPT), "--path", str(html_path)],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(result.stdout)
        return data.get("ok", False)
    except:
        return False

def main():
    print("=== CSS Mobile Fixer (EASY Category) ===\n")

    fixed_count = 0

    for nombre in EASY_FILES:
        html_file = VISUAL_DIR / f"{nombre}.html"

        # Inyectar
        status, content = inject_media_query(html_file)

        if status == "error":
            print(f"{nombre:30} [ERROR] No se pudo inyectar")
            continue
        elif status == "ya_existe":
            print(f"{nombre:30} [SKIP] Media query ya existe")
            continue

        # Escribir
        html_file.write_text(content, encoding="utf-8")

        # Verificar
        ok = verify_file(html_file)
        if ok:
            print(f"{nombre:30} [FIXED] ok=true")
            fixed_count += 1
        else:
            print(f"{nombre:30} [PARTIAL] media query added, pero falla en otro")

    print(f"\n--- Resultado ---")
    print(f"Reparados: {fixed_count}/{len(EASY_FILES)}")

    return fixed_count == len(EASY_FILES)

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
