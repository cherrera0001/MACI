#!/usr/bin/env python3
"""Test: validar estructura y rutas del manifiesto clases.yaml"""

import yaml
from pathlib import Path

def test_manifiesto_estructura():
    """Verifica que clases.yaml tenga estructura válida"""
    manifest_path = Path("07_DATITO/clases.yaml")

    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifiesto no encontrado: {manifest_path}")

    with open(manifest_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    assert data is not None, "YAML parsing falló"
    assert "clases" in data, "Key 'clases' no encontrado"
    assert isinstance(data["clases"], list), "clases debe ser lista"
    assert len(data["clases"]) > 0, "clases lista vacía"

    for i, clase in enumerate(data["clases"]):
        assert isinstance(clase, dict), f"Clase {i} no es dict"
        assert "n" in clase, f"Clase {i} sin field 'n'"
        assert "titulo" in clase, f"Clase {i} sin field 'titulo'"
        assert "conceptos" in clase, f"Clase {i} sin field 'conceptos'"

def test_manifiesto_rutas_visuales():
    """Verifica que todas las rutas visual apunten a archivos existentes"""
    manifest_path = Path("07_DATITO/clases.yaml")

    with open(manifest_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    visual_dir = Path("07_DATITO/01_CONCEPTOS/visual")
    fallidas = []

    for clase in data.get("clases", []):
        visual = clase.get("visual")
        n = clase.get("n")

        if visual:
            base = visual.split("#")[0]
            ruta = visual_dir / base

            if not ruta.exists():
                fallidas.append(f"Clase {n}: {visual}")

    assert len(fallidas) == 0, f"Rutas rotas ({len(fallidas)}):\n" + "\n".join(fallidas)

if __name__ == "__main__":
    test_manifiesto_estructura()
    print("[OK] Estructura valida")
    test_manifiesto_rutas_visuales()
    print("[OK] Todas las rutas validas")
