#!/usr/bin/env python3
"""Repara piel canónica en archivos HTML del Sprint 01"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import re

def repair_file(filepath, template_path):
    """Repara un archivo aplicando head del template y preservando main"""
    # Lee template y original
    tmpl = template_path.read_text(encoding='utf-8')
    orig = filepath.read_text(encoding='utf-8')

    # Extrae head del template (incluyendo <head>...</head>)
    head_start = tmpl.find('<head>')
    head_end = tmpl.find('</head>') + len('</head>')
    tmpl_head = tmpl[head_start:head_end]

    # Extrae main del original
    main_start = orig.find('<main')
    if main_start < 0:
        return False, "No <main> found"

    main_start = orig.find('>', main_start) + 1  # Después de <main ...>
    main_end = orig.rfind('</main>')  # El ÚLTIMO </main>

    if main_end < main_start:
        return False, "Invalid <main> structure"

    main_content = orig[main_start:main_end].strip()

    # Busca h1 real (primer h1 en el contenido)
    h1_match = re.search(r'<h1>([^<]+)</h1>', main_content)
    h1_real = h1_match.group(1) if h1_match else "Sin título"

    # Quita placeholder del main_content si está
    placeholder_h1 = main_content.find('<h1>TÍTULO DEL CONCEPTO')
    if placeholder_h1 > 0:
        # Encuentra dónde termina el placeholder (antes de </main> del template)
        main_content_clean = main_content[:placeholder_h1].strip()
        # Si el contenido limpio termina con </section> o similar, mantenerlo
        if main_content_clean.endswith(('</section>', '</div>', '</article>')):
            main_content = main_content_clean

    # Construye: template_head + <body><main>content</main></body></html>
    new_html = tmpl_head + '\n<body>\n<main>\n' + main_content + '\n</main>\n</body>\n</html>'

    # Actualiza title
    new_html = new_html.replace('<title>TÍTULO · Datito</title>', f'<title>{h1_real} · Datito</title>')

    # Guarda
    filepath.write_text(new_html, encoding='utf-8')
    return True, h1_real

# Procesa archivos
template = Path("07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html")
files = [
    (7, "08_overfitting_underfitting.html"),
    (8, "09_regresion.html"),
    (9, "10_clasificacion.html"),
    (10, "12_metricas_clasificacion.html"),
]

for issue, filename in files:
    filepath = Path(f"07_DATITO/01_CONCEPTOS/visual/{filename}")
    ok, msg = repair_file(filepath, template)
    status = "✓" if ok else "✗"
    print(f"{status} #{issue} {filename}: {msg}")

print("Archivos reparados. Ejecutar verificación.")
