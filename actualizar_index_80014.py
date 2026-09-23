#!/usr/bin/env python3
"""
Regenera INDEX.md con nombres limpios
"""

from pathlib import Path
import json

BASE_DIR = Path(r"F:\MACI\courses\80014_Emprendimiento")

def get_module_structure():
    """Lee la estructura de módulos desde _metadata.json files."""

    modules = {}

    for module_dir in sorted(BASE_DIR.glob("*/")):
        if module_dir.is_dir():
            module_name = module_dir.name
            metadata_file = module_dir / "_metadata.json"

            if metadata_file.exists():
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                modules[module_name] = data['resources']

    return modules

def generate_index(modules):
    """Genera INDEX.md con nombres actualizados."""

    index = """# Emprendimiento Tecnológico (80014) — Índice de Materiales

**Fecha de extracción:** 2026-09-22
**Curso:** 80014 EMPRENDIMIENTO TECNOLÓGICO (T2-2026)
**Estudiante:** Cristóbal Herrera
**Fuente:** UdeC Canvas Backup

---

## Estructura de Contenidos

"""

    for module_name in sorted(modules.keys()):
        # Nombre legible del módulo
        display_name = module_name.replace('_', ' ').replace('0 ', '').replace('1 ', '').replace('2 ', '').replace('3 ', '').replace('4 ', '').replace('5 ', '').replace('6 ', '').replace('7 ', '').replace('8 ', '').replace('9 ', '')
        # Mejor: usar regex
        import re
        display_name = re.sub(r'^\d+_', '', module_name).replace('_', ' ').title()

        resources = modules[module_name]
        index += f"### {display_name}\n\n"
        index += f"**Recursos:** {len(resources)}\n\n"

        # Listar archivos reales en el directorio
        module_dir = BASE_DIR / module_name
        pdf_files = sorted([f.name for f in module_dir.glob("*.pdf")])

        for pdf in pdf_files:
            index += f"- {pdf}\n"

        index += "\n"

    # Estadísticas
    total_files = sum(len(list((BASE_DIR / mod).glob("*.pdf"))) for mod in modules.keys())

    index += f"""---

## Estadísticas

- **Total de módulos temáticos:** {len(modules)}
- **Total de archivos:** {total_files}
- **Estructura de salida:** `courses/80014_Emprendimiento/`

---

## Notas

- Cada módulo contiene un archivo `_metadata.json` con información de los recursos
- Los archivos PDF están limpios y listos para leer
- La estructura refleja la agrupación temática del curso

**Regenerado automáticamente el 2026-09-22**

"""

    return index

def main():
    print("Regenerando INDEX.md con nombres limpios...")
    modules = get_module_structure()
    index_content = generate_index(modules)

    index_file = BASE_DIR / "INDEX.md"
    index_file.write_text(index_content, encoding='utf-8')

    print(f"✓ Índice actualizado: {index_file}")
    print(f"  - {len(modules)} módulos")
    print(f"  - {sum(len(list((BASE_DIR / mod).glob('*.pdf'))) for mod in modules.keys())} archivos")

if __name__ == "__main__":
    main()
