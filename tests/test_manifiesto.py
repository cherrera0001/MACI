#!/usr/bin/env python3
"""Test: todas las rutas visuales del manifiesto existen en el repo"""

import yaml
from pathlib import Path

def test_manifiesto_rutas_validas():
    """Verifica que todas las rutas visual del manifiesto apunten a archivos existentes"""

    # Cargar manifiesto canónico
    manifest_path = Path("07_DATITO/clases.yaml")
    with open(manifest_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    visual_dir = Path("07_DATITO/01_CONCEPTOS/visual")
    fallidas = []

    # Verificar cada clase
    for clase in data.get("clases", []):
        visual = clase.get("visual")
        n = clase.get("n")

        if visual:
            # Extraer base sin ancla
            base = visual.split("#")[0]
            ruta = visual_dir / base

            if not ruta.exists():
                fallidas.append(f"Clase {n}: {visual} NO EXISTE en {ruta}")

    assert len(fallidas) == 0, f"Rutas rotas ({len(fallidas)}):\n" + "\n".join(fallidas)
    print(f"✓ Todas las rutas están válidas ({len(data.get('clases', []))} clases)")

if __name__ == "__main__":
    test_manifiesto_rutas_validas()
