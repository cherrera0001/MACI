"""Smoke test del paquete distribuible (T-7.3.3).

Corre contra ``dist/datito.zip`` (lo construye con build_paquete.py si no
existe), verifica que no haya contradicciones de marca/versión en sus textos
y que el demo socrático funcione dentro del zip descomprimido.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[2]
ZIP = RAIZ / "dist" / "datito.zip"
BUILDER = RAIZ / "15_TERMINITO" / "scripts" / "build_paquete.py"


@pytest.fixture(scope="module")
def zip_paquete() -> Path:
    if not ZIP.exists():
        subprocess.run([sys.executable, str(BUILDER)], check=True, cwd=RAIZ,
                       capture_output=True, text=True)
    return ZIP


def _texto(z: zipfile.ZipFile, nombre: str) -> str:
    return z.read(nombre).decode("utf-8")


def test_contiene_lo_esencial(zip_paquete: Path):
    with zipfile.ZipFile(zip_paquete) as z:
        nombres = set(z.namelist())
    for esperado in ("start.py", "LEEME.txt", "LICENSE",
                     "15_TERMINITO/pyproject.toml", "15_TERMINITO/README.md"):
        assert esperado in nombres, f"falta {esperado} en el zip"
    assert any(n.startswith("wheels/") for n in nombres), "sin wheels/ no hay offline"


def test_sin_contradicciones_de_marca_y_version(zip_paquete: Path):
    with zipfile.ZipFile(zip_paquete) as z:
        leeme = _texto(z, "LEEME.txt")
        uso = _texto(z, "15_TERMINITO/docs/USO.md")
        readme = _texto(z, "15_TERMINITO/README.md")
        pyproject = _texto(z, "15_TERMINITO/pyproject.toml")
    assert "TERMITO" not in leeme, "LEEME sigue vendiendo la marca vieja"
    assert "placeholder" not in uso, "USO.md sigue diciendo que la UI es placeholder"
    version = [l for l in pyproject.splitlines() if l.startswith("version")][0]
    numero = version.split('"')[1].split(".")[0] + "." + version.split('"')[1].split(".")[1]
    assert numero in readme.splitlines()[0], "README y pyproject no coinciden en la version"


def test_demo_funciona_dentro_del_zip(zip_paquete: Path, tmp_path_factory):
    dest = tmp_path_factory.mktemp("datito-zip")
    with zipfile.ZipFile(zip_paquete) as z:
        z.extractall(dest)
    motor = dest / "15_TERMINITO"
    env = {**os.environ, "PYTHONPATH": str(motor / "src")}
    r = subprocess.run([sys.executable, "-m", "datito.cli", "demo", "--json"],
                       capture_output=True, text=True, cwd=motor, env=env, timeout=120)
    assert r.returncode == 0, f"demo fallo en el zip: {r.stderr[-500:]}"
    salida = json.loads(r.stdout[r.stdout.index("{"):])
    assert salida["estado_final"] == "DOMINADO"
    assert salida["violaciones_protocolo"] == []
