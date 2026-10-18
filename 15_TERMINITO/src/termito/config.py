"""Rutas y configuracion. Toda ruta se deriva de __file__ (nada hardcodeado)."""
from __future__ import annotations

import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DIR_CURSOS = RAIZ / "cursos"
DIR_WEB = RAIZ / "src" / "web"
ENV_PATH = RAIZ / ".env"


def _env(clave: str, defecto: str) -> str:
    if ENV_PATH.exists():
        for linea in ENV_PATH.read_text(encoding="utf-8").splitlines():
            if linea.startswith(clave + "="):
                return linea.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get(clave, defecto)


OLLAMA_HOST = _env("OLLAMA_HOST", "http://localhost:11434")
MODELO = _env("TERMITO_MODELO", "qwen2.5:3b")
PUERTO = int(_env("TERMITO_PUERTO", "8377"))

# Estados del curso (data-model.md)
ESTADOS_CURSO = ("configurando", "listo", "activo", "cerrado")
# Estados de dominio de un nodo (grafo)
ESTADOS_DOMINIO = ("no_estudiado", "en_estudio", "comprendido", "dominado")
# Estados de interaccion de lucha productiva (contracts/api.md)
ESTADOS_INTERACCION = ("pista", "esperando_intento", "paso_mostrado", "revision")
