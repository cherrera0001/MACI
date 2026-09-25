#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Migración iterativa: copia template v1, preserva contenido pedagógico.
USO: python datito_migracion_inicio.py --archivo 01_fundamentos.html
"""

import sys
import argparse
import shutil
import re
import io
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DATITO_DIR = ROOT / "07_DATITO"
TEMPLATE_PATH = DATITO_DIR / "01_CONCEPTOS" / "visual" / "_TEMPLATE_CANONICO.html"

def migrate_html(target_html):
    """Migra un HTML al template v1"""
    target_path = None

    # Buscar el archivo
    for html_file in DATITO_DIR.rglob(target_html):
        if html_file.name == target_html:
            target_path = html_file
            break

    if not target_path:
        print(f"ERROR: No encontrado {target_html}")
        return False

    print(f"=" * 70)
    print(f"MIGRACION: {target_html}")
    print(f"=" * 70)
    print(f"\n1. Leyendo template canónico...")
    template_content = TEMPLATE_PATH.read_text(encoding='utf-8')

    print(f"2. Leyendo HTML viejo: {target_path.relative_to(DATITO_DIR)}")
    old_content = target_path.read_text(encoding='utf-8')

    # Extraer info básica del HTML viejo (si existe)
    # title, h1, descripción, contenido

    title_match = re.search(r'<title>([^<]+)</title>', old_content)
    title = title_match.group(1) if title_match else target_html.replace('.html', '')

    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', old_content, re.DOTALL)
    h1 = h1_match.group(1).strip() if h1_match else title

    # Extraer contenido main (entre <main> y </main>)
    main_match = re.search(r'<main[^>]*>(.*?)</main>', old_content, re.DOTALL)
    body_content = main_match.group(1) if main_match else ""

    # Usar template como base
    new_content = template_content
    new_content = new_content.replace("<title>TÍTULO · Datito</title>", f"<title>{title} · Datito</title>")
    new_content = new_content.replace("<h1>TÍTULO DEL CONCEPTO O PREGUNTA</h1>", f"<h1>{h1}</h1>")

    # Reemplazar contenido placeholder
    new_content = re.sub(
        r'(<p class="sub">).*?(</p>)',
        r'\1Aprende qué es, cómo funciona, cuándo usar\2',
        new_content,
        count=1
    )

    # Crear archivo _NEW
    new_path = target_path.parent / f"{target_path.stem}_NEW.html"
    new_path.write_text(new_content, encoding='utf-8')

    print(f"\n3. Creado: {new_path.name}")
    print(f"\n4. PRÓXIMOS PASOS MANUALES:")
    print(f"   a) Abre en editor: {new_path}")
    print(f"   b) Reemplaza el contenido entre <main> y <!-- datito:nav:fin -->")
    print(f"      Con el contenido pedagógico del HTML viejo")
    print(f"   c) Asegúrate de usar:")
    print(f"      - <h2> para secciones")
    print(f"      - <details> para expandibles")
    print(f"      - <details class=\"resp\"> para respuestas")
    print(f"      - <table> para datos")
    print(f"      - .clave / .nota / .peligro para énfasis")
    print(f"   d) NO uses: CDN, Chart.js remoto, #667eea, #764ba2")
    print(f"\n5. Cuando esté listo, evalúa:")
    print(f"   python 03_CODIGO/datito_loop_eval.py --path {new_path}")
    print(f"\n6. Si score=1.0:")
    print(f"   python 03_CODIGO/datito_loop_once.py --path {new_path} --hypothesis \"migrate to template v1\"")
    print(f"\n7. Finalmente:")
    print(f"   mv {new_path.name} {target_path.name}")
    print(f"\n" + "=" * 70)

    return True

def main():
    ap = argparse.ArgumentParser(description="Migración iterativa a template v1")
    ap.add_argument("--archivo", required=True, help="Archivo a migrar (ej: 01_fundamentos.html)")
    args = ap.parse_args()

    if migrate_html(args.archivo):
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
