#!/usr/bin/env python3
"""
Limpia nombres de archivos: reemplaza + por espacios
"""

from pathlib import Path

BASE_DIR = Path(r"F:\MACI\courses\80014_Emprendimiento")

def clean_filenames(directory: Path) -> int:
    """Renombra archivos reemplazando + por espacios."""

    count = 0
    for old_path in directory.rglob('*'):
        if old_path.is_file() and '+' in old_path.name:
            new_filename = old_path.name.replace('+', ' ')
            new_path = old_path.parent / new_filename

            old_path.rename(new_path)
            print(f"  {old_path.name} → {new_filename}")
            count += 1

    return count

def main():
    print("Limpiando nombres de archivos en 80014_Emprendimiento...")
    count = clean_filenames(BASE_DIR)
    print(f"\nListo. {count} archivos renombrados.")

if __name__ == "__main__":
    main()
