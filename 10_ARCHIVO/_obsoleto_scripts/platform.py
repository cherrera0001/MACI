#!/usr/bin/env python
"""MACI Platform CLI — wrapper FASE-0 (ARCHIVADO, no activo).

ARCHIVADO el 2026-10-18 en 10_ARCHIVO/_obsoleto_scripts/ porque su
presencia en 03_SCRIPTS/ envenenaba la cadena de verificacion: cualquier
`import platform` (stdlib, usado por playwright entre otros) ejecutado
con 03_SCRIPTS/ en sys.path resolvia ESTE archivo en vez del modulo
estandar y reventaba con ModuleNotFoundError: No module named
'maci_platform'. Nada en el repo lo invoca.

El paquete maci_platform (borrado del arbol en la reorganizacion del
2026-09-25) se recupero junto a este wrapper, intacto de bff8bd8.
Depende de `click` (externo) y lee courses.yaml; es un experimento
historico, no herramienta vigente.

Uso historico:
    python platform.py status      # Show capability matrix
    python platform.py report      # Generate capability report
    python platform.py process --course 80014  # Process a course
"""

import sys
import os

# Add 03_SCRIPTS to path so we can import maci_platform
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '03_SCRIPTS'))

from maci_platform.cli import main

if __name__ == '__main__':
    sys.exit(main())
