#!/usr/bin/env python3
"""
Procesador de JSONs del backup UdeC 83706 (Prototipos y Creatividad)
Agrupa por módulo, crea estructura y genera INDEX.md
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

# Rutas
BACKUP_DIR = Path(r"F:\MACI_RESPALDOS\udec\2026-09-22-001\83706")
OUTPUT_DIR = Path(r"F:\MACI\PROCESADO\83706_Prototipos")

def load_json_files() -> Dict:
    """Carga todos los JSONs del backup."""
    manifest_file = BACKUP_DIR / "manifest.json"

    with open(manifest_file, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    return manifest.get('resources', [])

def categorize_resources(resources: List) -> Dict[str, List]:
    """Agrupa recursos por módulo/categoría."""

    # Categorías de módulos basadas en patrones en los títulos
    modules = {
        "00_Inicio": [],
        "01_Sesion_01_Intro": [],
        "02_Sesion_02_Creatividad": [],
        "03_Sesion_03_Metricas": [],
        "04_Lecturas_Creatividad": [],
        "05_Lecturas_Complementarias": [],
        "06_Sesion_04_Prototipaje": [],
        "07_Sesion_05_Roadmapping": [],
        "99_Archivos_Generales": []
    }

    for resource in resources:
        title = resource.get('title', '')

        # Clasificar por patrón de título
        if 'Syllabus' in title or 'Nomina' in title or 'Notas finales' in title:
            modules["00_Inicio"].append(resource)
        elif '601' in title or 'Intro.pdf' in title:
            modules["01_Sesion_01_Intro"].append(resource)
        elif '602' in title:
            modules["02_Sesion_02_Creatividad"].append(resource)
        elif '603' in title:
            modules["03_Sesion_03_Metricas"].append(resource)
        elif 'Kleon' in title or 'Gray' in title or 'Sherwin' in title or 'HBR' in title or 'Book_' in title or 'Tarot' in title:
            if 'Mapping' in title or 'Lean' in title or 'Testing' in title or 'Designing' in title:
                modules["05_Lecturas_Complementarias"].append(resource)
            else:
                modules["04_Lecturas_Creatividad"].append(resource)
        elif '604' in title or 'T2' in title and 'Instrucciones' in title:
            modules["06_Sesion_04_Prototipaje"].append(resource)
        elif '605' in title or 'TF' in title:
            modules["07_Sesion_05_Roadmapping"].append(resource)
        else:
            modules["99_Archivos_Generales"].append(resource)

    # Eliminar módulos vacíos
    return {k: v for k, v in modules.items() if v}

def create_directory_structure(modules: Dict[str, List]) -> None:
    """Crea la estructura de directorios."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for module_name, resources in modules.items():
        module_dir = OUTPUT_DIR / module_name
        module_dir.mkdir(parents=True, exist_ok=True)

        # Crear un archivo JSON con la metadata del módulo
        metadata_file = module_dir / "METADATA.json"
        metadata = {
            "module": module_name,
            "resource_count": len(resources),
            "resources": resources
        }

        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

def generate_index(modules: Dict[str, List]) -> str:
    """Genera el INDEX.md con la estructura del curso."""

    index = """# Prototipos y Creatividad (83706) — Índice Procesado

**Fecha de extracción:** 2026-09-22
**Curso:** 4321005-0 PROTOTIPOS Y CREATIVIDAD (T2-2026)
**Estudiante:** Cristóbal Herrera
**Fuente:** UdeC Canvas Backup

---

## Estructura del Curso

"""

    for module_name, resources in sorted(modules.items()):
        # Formatear nombre del módulo
        display_name = module_name.replace('_', ' ').title()
        index += f"### {display_name}\n\n"
        index += f"**Recursos:** {len(resources)}\n\n"

        for resource in resources:
            title = resource.get('title', 'Sin título')
            resource_id = resource.get('id', 'N/A')
            index += f"- `[{resource_id}]` {title}\n"

        index += "\n"

    # Estadísticas finales
    total_resources = sum(len(r) for r in modules.values())
    total_modules = len(modules)

    index += f"""---

## Estadísticas

- **Total de módulos:** {total_modules}
- **Total de recursos:** {total_resources}
- **Estructura generada en:** `PROCESADO/83706_Prototipos/`

---

## Archivos Generados

Cada módulo contiene:
- `METADATA.json` — Metadata de los recursos del módulo

Para ver el contenido de cada recurso, consultar el archivo original en:
`{BACKUP_DIR}`

---

**Nota:** Este índice fue generado automáticamente el 2026-09-22.
Los archivos PDF y DOCX originales se encuentran en `{BACKUP_DIR}`.

"""

    return index

def main():
    print(f"Procesando JSONs desde: {BACKUP_DIR}")
    print(f"Escribiendo a: {OUTPUT_DIR}")
    print()

    # 1. Cargar recursos
    resources = load_json_files()
    print(f"✓ Cargados {len(resources)} recursos")

    # 2. Categorizar
    modules = categorize_resources(resources)
    print(f"✓ Agrupados en {len(modules)} módulos")
    for mod_name, mods in modules.items():
        print(f"  - {mod_name}: {len(mods)} recursos")

    # 3. Crear estructura
    create_directory_structure(modules)
    print(f"✓ Estructura de directorios creada")

    # 4. Generar INDEX.md
    index_content = generate_index(modules)
    index_file = OUTPUT_DIR / "INDEX.md"

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"✓ INDEX.md generado: {index_file}")
    print()
    print(f"Listo. Se procesaron {len(resources)} archivos en {len(modules)} módulos.")

if __name__ == "__main__":
    main()
