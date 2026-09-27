#!/usr/bin/env python3
"""
Procesador de curso 80714 - Fundamentos de Bases de Datos
Extrae, agrupa y organiza contenido de JSONs del respaldo.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import re

# Rutas
SOURCE_DIR = Path("F:/MACI_RESPALDOS/udec/2026-09-22-001/80714/")
DEST_DIR = Path("F:/MACI/courses/80714_Fundamentos_BD/")

# Crear directorio destino
DEST_DIR.mkdir(parents=True, exist_ok=True)

# Mapeo de módulos basado en palabras clave en títulos
MODULE_KEYWORDS = {
    "Introducción": ("00_Introduccion", "Introducción al curso"),
    "Python": ("01_Python_Basico", "Python: Fundamentos"),
    "Bases de Datos": ("02_Bases_Datos_Conceptos", "Bases de Datos: Conceptos"),
    "SQL": ("03_SQL_Basico", "SQL: Fundamentos"),
    "Consultas": ("03_SQL_Basico", "SQL: Fundamentos"),
    "Tablas": ("03_SQL_Basico", "SQL: Fundamentos"),
    "Modelos": ("04_Modelado_Datos", "Modelado de Datos"),
    "Entidades": ("04_Modelado_Datos", "Modelado de Datos"),
    "Relaciones": ("04_Modelado_Datos", "Modelado de Datos"),
    "Normalización": ("05_Normalizacion", "Normalización de Bases de Datos"),
    "Formas": ("05_Normalizacion", "Normalización de Bases de Datos"),
    "Transacciones": ("06_Transacciones", "Transacciones y Concurrencia"),
    "Índices": ("07_Optimizacion", "Optimización y Desempeño"),
    "Desempeño": ("07_Optimizacion", "Optimización y Desempeño"),
    "Seguridad": ("08_Seguridad", "Seguridad en Bases de Datos"),
    "Backup": ("08_Seguridad", "Seguridad en Bases de Datos"),
    "Respaldo": ("08_Seguridad", "Seguridad en Bases de Datos"),
}

# Procesar JSONs
items_by_module = defaultdict(list)
all_items = []

for json_file in sorted(SOURCE_DIR.glob("*.json")):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extraer información
        title = data.get('title', '').strip()
        text = data.get('text', '')[:200]  # primeros 200 caracteres
        url = data.get('url', '')

        # Extraer tipo de documento (por defecto "Page")
        item_type = "Page"

        # Determinar módulo basado en título
        module_id = None
        module_name = None

        # Extraer solo la parte descriptiva del título
        if " : " in title:
            title_short = title.split(" : ")[0].strip()
        else:
            title_short = title

        for keyword, (mod_folder, mod_label) in MODULE_KEYWORDS.items():
            if keyword.lower() in title_short.lower():
                module_id = mod_folder
                module_name = mod_label
                break

        # Si no encuentra módulo, ponerlo en Introducción
        if module_id is None:
            module_id = "00_Introduccion"
            module_name = "Introducción al curso"

        item = {
            'id': json_file.stem,
            'filename': json_file.name,
            'title': title_short,
            'title_full': title,
            'type': item_type,
            'module': module_id,
            'module_label': module_name,
            'excerpt': text,
        }

        items_by_module[module_id].append(item)
        all_items.append(item)

        print(f"✓ {json_file.stem}: {title_short} → {module_id}")

    except Exception as e:
        print(f"✗ Error procesando {json_file.name}: {e}")

# Crear carpetas y copiar archivos
print("\n" + "="*60)
print("CREANDO ESTRUCTURA DE CARPETAS")
print("="*60)

for module_folder in sorted(items_by_module.keys()):
    module_dir = DEST_DIR / module_folder
    module_dir.mkdir(exist_ok=True)

    items = items_by_module[module_folder]
    module_label = items[0]['module_label']

    # Copiar JSONs
    for item in items:
        src_file = SOURCE_DIR / item['filename']
        dest_file = module_dir / item['filename']

        if src_file.exists():
            import shutil
            shutil.copy2(src_file, dest_file)
            print(f"  ✓ Copiado: {module_folder}/{item['filename']}")

    # Crear METADATA.json del módulo
    metadata = {
        'module_id': module_folder,
        'module_label': module_label,
        'item_count': len(items),
        'items': [
            {
                'id': item['id'],
                'title': item['title'],
                'type': item['type']
            }
            for item in items
        ]
    }

    metadata_file = module_dir / "METADATA.json"
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"  → {len(items)} items en {module_folder}/")

# Crear INDEX.md
print("\n" + "="*60)
print("GENERANDO INDEX.md")
print("="*60)

index_content = """# Índice General - Curso 80714: Fundamentos de Bases de Datos

**Estructura de contenido organizada por módulo temático**

## Resumen de Módulos

"""

# Tabla de resumen
index_content += "| Módulo | Descripción | Items | Ruta |\n"
index_content += "|--------|-------------|-------|------|\n"

for module_folder in sorted(items_by_module.keys()):
    items = items_by_module[module_folder]
    module_label = items[0]['module_label']
    index_content += f"| {module_folder} | {module_label} | {len(items)} | `{module_folder}/` |\n"

index_content += "\n---\n\n"

# Detalle por módulo
for module_folder in sorted(items_by_module.keys()):
    items = items_by_module[module_folder]
    module_label = items[0]['module_label']

    index_content += f"## {module_folder}\n"
    index_content += f"**{module_label}**\n\n"

    index_content += f"| # | Título | ID | Tipo |\n"
    index_content += f"|---|--------|----|----- |\n"

    for i, item in enumerate(items, 1):
        index_content += f"| {i} | {item['title']} | `{item['id']}` | {item['type']} |\n"

    index_content += f"\n**Archivo de metadatos:** `{module_folder}/METADATA.json`\n\n"
    index_content += "---\n\n"

# Estadísticas finales
total_items = len(all_items)
total_modules = len(items_by_module)

index_content += f"""
## Estadísticas

- **Total de módulos:** {total_modules}
- **Total de items:** {total_items}
- **Fecha de procesamiento:** 2026-09-22
- **Fuente:** Respaldo `F:/MACI_RESPALDOS/udec/2026-09-22-001/80714/`

## Estructura de directorios

```
80714_Fundamentos_BD/
"""

for module_folder in sorted(items_by_module.keys()):
    items = items_by_module[module_folder]
    index_content += f"├── {module_folder}/\n"
    index_content += f"│   ├── METADATA.json\n"
    for item in items:
        index_content += f"│   ├── {item['filename']}\n"

index_content += "└── INDEX.md\n"
index_content += "```\n"

# Escribir INDEX.md
index_file = DEST_DIR / "INDEX.md"
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"✓ Archivo INDEX.md creado: {index_file}")

# Resumen final
print("\n" + "="*60)
print("PROCESAMIENTO COMPLETADO")
print("="*60)
print(f"Ubicación: {DEST_DIR}")
print(f"Módulos creados: {total_modules}")
print(f"Items procesados: {total_items}")
print(f"Índice: {index_file}")
