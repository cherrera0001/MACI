#!/usr/bin/env python3
"""
Procesador de JSONs del backup UdeC 83703 (Liderazgo y Equipos)
Agrupa por módulo, crea estructura y genera INDEX.md
"""

import json
import os
from pathlib import Path
from typing import Dict, List

# Rutas
BACKUP_DIR = Path(r"F:\MACI_RESPALDOS\udec\2026-09-22-001\83703")
OUTPUT_DIR = Path(r"F:\MACI\courses\83703_Liderazgo")


def load_json_files() -> Dict:
    """Carga manifest.json del backup."""
    manifest_file = BACKUP_DIR / "manifest.json"

    with open(manifest_file, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    return manifest.get('resources', [])


def categorize_resources(resources: List) -> Dict[str, List]:
    """Agrupa recursos por módulo/jornada."""

    modules = {
        "00_Inicio": [],
        "01_Modulo_Liderazgo_Jornada_1": [],
        "01_Modulo_Liderazgo_Lecturas": [],
        "02_Modulo_Liderazgo_Jornada_2": [],
        "02_Modulo_Liderazgo_Tareas": [],
        "03_Modulo_Equipos_Jornadas": [],
        "03_Modulo_Equipos_Lecturas": [],
        "04_Modulo_Innovacion": [],
        "05_Modulo_Conflicto_Diversidad": [],
        "99_Archivos_Generales": []
    }

    for resource in resources:
        title = resource.get('title', '')
        resource_type = resource.get('type', '')

        # Inicio: Bienvenida, normativa, foro social
        if 'Bienvenida' in title or 'Normativa' in title or 'Conoce a tus' in title:
            modules["00_Inicio"].append(resource)

        # Jornadas (sesiones del profesor)
        elif 'Jornada 1' in title:
            modules["01_Modulo_Liderazgo_Jornada_1"].append(resource)
        elif 'Jornada 2' in title:
            modules["02_Modulo_Liderazgo_Jornada_2"].append(resource)
        elif 'Jornada 3' in title or 'Jornada 4' in title or 'Jornada 5' in title or 'Jornada 6' in title:
            modules["03_Modulo_Equipos_Jornadas"].append(resource)

        # Tareas (Ta1, Ta2, etc)
        elif title.startswith('Ta') or 'Plan de desarrollo' in title or 'Conexiones de Alta Calidad' in title:
            modules["02_Modulo_Liderazgo_Tareas"].append(resource)

        # Lecturas módulo liderazgo (Jornada 1)
        elif any(x in title for x in ['Banks', 'HBR-Liderazgo', 'autentico', 'Prieto', 'Elogio del lider']):
            modules["01_Modulo_Liderazgo_Lecturas"].append(resource)

        # Lecturas módulo liderazgo 2 (Jornada 2)
        elif any(x in title for x in ['Innovation Leadership', 'High_Quality_Connections', 'Tushman', 'Puertas', 'Joly', 'Rosing']):
            modules["03_Modulo_Equipos_Lecturas"].append(resource)

        # Innovación
        elif 'Innovación' in title or 'innovaci' in title.lower():
            modules["04_Modulo_Innovacion"].append(resource)

        # Conflicto y diversidad
        elif 'Conflicto' in title or 'Diversidad' in title or 'Diagnóstico' in title or 'Anticiparse' in title or 'Casos a desarrollar' in title:
            modules["05_Modulo_Conflicto_Diversidad"].append(resource)

        # Introducciones y foros
        elif 'Introducción' in title or 'Foro' in title or 'Video instructivo' in title:
            modules["00_Inicio"].append(resource)

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

    index = """# Liderazgo y Equipos para la Innovación (83703) — Índice Procesado

**Fecha de extracción:** 2026-09-22
**Curso:** 4321006-9 LIDERAZGO Y EQUIPOS PARA LA INNOVACION (T2-2026)
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
            resource_type = resource.get('type', 'desconocido')
            index += f"- `[{resource_id}]` ({resource_type}) {title}\n"

        index += "\n"

    # Estadísticas finales
    total_resources = sum(len(r) for r in modules.values())
    total_modules = len(modules)

    index += f"""---

## Estadísticas

- **Total de módulos:** {total_modules}
- **Total de recursos:** {total_resources}
- **Estructura generada en:** `courses/83703_Liderazgo/`

---

## Composición de Recursos

"""

    # Contar por tipo
    type_counts = {}
    for resources in modules.values():
        for resource in resources:
            rtype = resource.get('type', 'desconocido')
            type_counts[rtype] = type_counts.get(rtype, 0) + 1

    for rtype, count in sorted(type_counts.items()):
        index += f"- **{rtype.capitalize()}:** {count}\n"

    index += f"""

---

## Archivos Generados

Cada módulo contiene:
- `METADATA.json` — Metadata de los recursos del módulo

**Recursos descargados en:**
- `{BACKUP_DIR}/files/` — Archivos PDF
- `{BACKUP_DIR}/pages/` — Páginas del curso
- `{BACKUP_DIR}/assignments/` — Tareas y asignaciones

---

**Nota:** Este índice fue generado automáticamente el 2026-09-22.
Los archivos originales se encuentran en `{BACKUP_DIR}`.

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
    for mod_name, mods in sorted(modules.items()):
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
