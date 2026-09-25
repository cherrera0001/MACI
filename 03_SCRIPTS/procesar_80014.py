#!/usr/bin/env python3
"""
Procesador de JSONs del backup UdeC 80014 (Emprendimiento Tecnológico)
Copia archivos con nombres decodificados, agrupa por tema y genera INDEX.md
"""

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List
from urllib.parse import unquote

# Rutas
BACKUP_DIR = Path(r"F:\MACI_RESPALDOS\udec\2026-09-22-001\80014")
BACKUP_FILES = BACKUP_DIR / "files"
OUTPUT_DIR = Path(r"F:\MACI\courses\80014_Emprendimiento")

def load_manifest() -> List:
    """Carga los recursos desde manifest.json."""
    manifest_file = BACKUP_DIR / "manifest.json"

    with open(manifest_file, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    return manifest.get('resources', [])

def categorize_resources(resources: List) -> Dict[str, List]:
    """Agrupa recursos por tema/módulo."""

    modules = {
        "00_Syllabus": [],
        "01_Lean_Startup": [],
        "02_Modelo_Negocios": [],
        "03_Estrategia": [],
        "04_OKR": [],
        "05_Financiamiento": [],
        "06_Casos_Startups": [],
        "07_Manuales_Referencias": [],
        "08_Talleres": []
    }

    for resource in resources:
        title = resource.get('title', '')

        # Clasificación por patrón
        if 'Syllabus' in title:
            modules["00_Syllabus"].append(resource)
        elif 'Lean Startup' in title or ('Clase' in title and '1' in title):
            modules["01_Lean_Startup"].append(resource)
        elif 'Modelo de negocios' in title or ('Clase' in title and '2' in title) or 'Osterwalder' in title:
            modules["02_Modelo_Negocios"].append(resource)
        elif 'Estrategia' in title or ('Clase' in title and '3' in title) or 'Blue Ocean' in title or 'Value Innovation' in title or 'Baldwin' in title or 'Shapiro' in title or 'Strategy for' in title:
            modules["03_Estrategia"].append(resource)
        elif 'OKR' in title or 'Objetivos y resultados' in title or ('Clase' in title and '4' in title) or 'Mide lo que importa' in title:
            modules["04_OKR"].append(resource)
        elif 'Rondas de inversión' in title or 'Financiamiento' in title or ('Clase' in title and '5' in title) or 'VC Deal' in title:
            modules["05_Financiamiento"].append(resource)
        elif 'Casos en crecimiento' in title or ('Clase' in title and '6' in title):
            modules["06_Casos_Startups"].append(resource)
        elif 'Manual' in title or 'Design-a-Better' in title:
            modules["07_Manuales_Referencias"].append(resource)
        elif 'Taller' in title:
            modules["08_Talleres"].append(resource)
        else:
            modules["07_Manuales_Referencias"].append(resource)

    return {k: v for k, v in modules.items() if v}

def decode_filename(encoded_name: str) -> str:
    """Decodifica nombres URL-encoded."""
    return unquote(encoded_name)

def copy_files(resources: List, output_dir: Path) -> None:
    """Copia archivos desde backup decodificando nombres."""

    for resource in resources:
        encoded_path = resource.get('details', {}).get('path', '')
        if not encoded_path:
            continue

        # Construir ruta origen (Windows)
        source_file = BACKUP_FILES / encoded_path.split('\\')[-1]

        if not source_file.exists():
            print(f"  ⚠ Archivo no encontrado: {source_file}")
            continue

        # Decodificar nombre destino
        original_filename = source_file.name
        decoded_filename = decode_filename(original_filename)

        # Crear directorio de destino si no existe
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copiar archivo
        dest_file = output_dir / decoded_filename
        try:
            shutil.copy2(source_file, dest_file)
            print(f"  ✓ {decoded_filename}")
        except Exception as e:
            print(f"  ✗ Error copiando {decoded_filename}: {e}")

def create_directory_structure(modules: Dict[str, List]) -> None:
    """Crea estructura de directorios y copia archivos."""

    for module_name, resources in modules.items():
        module_dir = OUTPUT_DIR / module_name

        print(f"\n{module_name}:")
        copy_files(resources, module_dir)

        # Guardar metadata
        metadata_file = module_dir / "_metadata.json"
        metadata = {
            "module": module_name,
            "resource_count": len(resources),
            "resources": [
                {
                    "id": r.get('id'),
                    "title": r.get('title'),
                    "timestamp": r.get('details', {}).get('timestamp')
                }
                for r in resources
            ]
        }

        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

def generate_index(modules: Dict[str, List]) -> str:
    """Genera INDEX.md con estructura navegable."""

    index = """# Emprendimiento Tecnológico (80014) — Índice de Materiales

**Fecha de extracción:** 2026-09-22
**Curso:** 80014 EMPRENDIMIENTO TECNOLÓGICO (T2-2026)
**Estudiante:** Cristóbal Herrera
**Fuente:** UdeC Canvas Backup

---

## Estructura de Contenidos

"""

    for module_name, resources in sorted(modules.items()):
        # Nombre legible del módulo
        display_name = module_name.replace('_', ' ').title()
        index += f"### {display_name}\n\n"
        index += f"**Recursos:** {len(resources)}\n\n"

        for resource in resources:
            title = resource.get('title', 'Sin título')
            # Decodificar título para mejor lectura
            title_decoded = unquote(title)
            index += f"- {title_decoded}\n"

        index += "\n"

    # Estadísticas
    total_resources = sum(len(r) for r in modules.values())

    index += f"""---

## Estadísticas

- **Total de módulos temáticos:** {len(modules)}
- **Total de recursos:** {total_resources}
- **Estructura de salida:** `courses/80014_Emprendimiento/`

---

## Notas

- Cada módulo contiene un archivo `_metadata.json` con información de los recursos
- Los archivos PDF están decodificados y listos para leer
- La estructura refleja la agrupación temática del curso

**Generado automáticamente el 2026-09-22**

"""

    return index

def main():
    print("=" * 70)
    print("PROCESADOR: 80014 EMPRENDIMIENTO TECNOLÓGICO")
    print("=" * 70)
    print(f"\nOrigen: {BACKUP_DIR}")
    print(f"Destino: {OUTPUT_DIR}")

    # 1. Cargar manifest
    resources = load_manifest()
    print(f"\n✓ Cargados {len(resources)} recursos del manifest")

    # 2. Categorizar
    modules = categorize_resources(resources)
    print(f"✓ Agrupados en {len(modules)} módulos temáticos")
    for mod_name, mods in sorted(modules.items()):
        print(f"  - {mod_name}: {len(mods)} recursos")

    # 3. Crear estructura y copiar archivos
    print("\n→ Copiando archivos y creando estructura...")
    create_directory_structure(modules)

    # 4. Generar índice
    index_content = generate_index(modules)
    index_file = OUTPUT_DIR / "INDEX.md"
    index_file.write_text(index_content, encoding='utf-8')
    print(f"\n✓ Índice generado: {index_file}")

    print("\n" + "=" * 70)
    print(f"LISTO. Procesados {len(resources)} archivos en {len(modules)} módulos.")
    print("=" * 70)

if __name__ == "__main__":
    main()
