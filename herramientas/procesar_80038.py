#!/usr/bin/env python3
"""
Procesador de JSONs del backup UdeC 80038 (Procesos de Innovación)
Agrupa por módulo, crea estructura y genera INDEX.md
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

# Rutas
BACKUP_DIR = Path(r"F:\MACI_RESPALDOS\udec\2026-09-22-001\80038")
OUTPUT_DIR = Path(r"F:\MACI\courses\80038_Procesos_Innovacion")

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
        "01_Sesion_01_Proceso_General": [],
        "02_Sesion_02_Entendimiento": [],
        "03_Sesion_03_Ideacion": [],
        "04_Sesion_04_Prototipaje": [],
        "05_Sesion_05_Testeo": [],
        "06_Lecturas_Fundacionales": [],
        "07_Lecturas_Metodos": [],
        "08_Practicos_Entregas": [],
        "99_Archivos_Generales": []
    }

    for resource in resources:
        title = resource.get('title', '')

        # Clasificar por patrón de título
        if 'Syllabus' in title or 'Nomina' in title or 'Notas finales' in title or 'Criterios' in title:
            modules["00_Inicio"].append(resource)
        elif 'Sesion 01' in title or 'Proceso General' in title:
            modules["01_Sesion_01_Proceso_General"].append(resource)
        elif 'Sesion 02' in title or 'Entendimiento' in title:
            modules["02_Sesion_02_Entendimiento"].append(resource)
        elif 'Sesion 03' in title or 'Ideacion' in title:
            modules["03_Sesion_03_Ideacion"].append(resource)
        elif 'Sesion 04' in title or 'Prototipaje' in title:
            modules["04_Sesion_04_Prototipaje"].append(resource)
        elif 'Sesion 05' in title or 'Testeo' in title or 'Testing' in title or 'Validacion' in title:
            modules["05_Sesion_05_Testeo"].append(resource)
        elif 'Book_' in title:
            # Separar libros por tema
            if 'Designing' in title or 'Digital Age' in title:
                modules["06_Lecturas_Fundacionales"].append(resource)
            elif 'Startup' in title or 'Blank' in title or 'Innovation' in title or 'Testing business' in title:
                modules["07_Lecturas_Metodos"].append(resource)
            else:
                modules["06_Lecturas_Fundacionales"].append(resource)
        elif 'Entrega' in title or 'Practica' in title or 'Ejercicio' in title or 'Actividad' in title:
            modules["08_Practicos_Entregas"].append(resource)
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

    index = """# Procesos de Innovación (80038) — Índice Procesado

**Fecha de extracción:** 2026-09-22
**Curso:** PROCESOS DE INNOVACIÓN (T2-2026)
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
- **Estructura generada en:** `courses/80038_Procesos_Innovacion/`

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
    print(f"[OK] Cargados {len(resources)} recursos")

    # 2. Categorizar
    modules = categorize_resources(resources)
    print(f"[OK] Agrupados en {len(modules)} módulos")
    for mod_name, mods in sorted(modules.items()):
        print(f"  - {mod_name}: {len(mods)} recursos")

    # 3. Crear estructura
    create_directory_structure(modules)
    print(f"[OK] Estructura de directorios creada")

    # 4. Generar INDEX.md
    index_content = generate_index(modules)
    index_file = OUTPUT_DIR / "INDEX.md"

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"[OK] INDEX.md generado: {index_file}")
    print()
    print(f"Listo. Se procesaron {len(resources)} archivos en {len(modules)} módulos.")

if __name__ == "__main__":
    main()
