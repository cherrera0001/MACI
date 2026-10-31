"""Síntesis de voz neuronal local (D-12.1 + D-13.3). Zero-lock-in.

Detecta el binario piper y un modelo .onnx (autodescubrimiento en
15_TERMINITO/.piper/ y ~/.local/share/piper/, sin configuración manual).
Si no hay motor, degrada limpio y /api/salud explica cómo activarlo:

  pipx install piper-tts
  python3 -m datito.voz --instalar-modelo
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

from . import config

_MOTOR: tuple[str, str] | None | bool = None  # cache: (nombre, binario)

MODELO_POR_DEFECTO = "es_ES-davefx-medium"
# v1.0.0 de rhasspy/piper-voices: voz es neutra/culta, lista para usar.
URL_MODELO = ("https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/"
              "es/es_ES/davefx/medium/es_ES-davefx-medium")


def _dirs_modelos() -> list[Path]:
    return [config.RAIZ / ".piper",
            Path.home() / ".local" / "share" / "piper"]


def modelos_locales() -> list[Path]:
    """Todos los .onnx encontrados en los directorios de modelos."""
    hallados = []
    for d in _dirs_modelos():
        if d.is_dir():
            hallados.extend(sorted(d.glob("*.onnx")))
    return hallados


def modelo_a_usar() -> Path | None:
    """El modelo preferido (nombre por defecto) o el primero disponible."""
    modelos = modelos_locales()
    if not modelos:
        return None
    for m in modelos:
        if m.stem == MODELO_POR_DEFECTO:
            return m
    return modelos[0]


def instalar_modelo(url: str = URL_MODELO, destino: Path | None = None) -> Path:
    """Descarga modelo .onnx + .onnx.json listos para usar. Devuelve el .onnx."""
    destino = destino or (config.RAIZ / ".piper")
    destino.mkdir(parents=True, exist_ok=True)
    onnx = destino / (MODELO_POR_DEFECTO + ".onnx")
    for ruta, sufijo in ((onnx, ".onnx"), (onnx.with_suffix(onnx.suffix + ".json"), ".onnx.json")):
        if not ruta.exists():
            with urllib.request.urlopen(url + sufijo, timeout=300) as r:
                ruta.write_bytes(r.read())
    global _MOTOR
    _MOTOR = None  # re-detectar con el nuevo modelo
    return onnx


def _detectar() -> tuple[str, str] | None:
    global _MOTOR
    if _MOTOR is None:
        piper = shutil.which("piper")
        _MOTOR = ("piper", piper) if piper and modelo_a_usar() else False
    return _MOTOR or None


def disponible() -> bool:
    return _detectar() is not None


def motor() -> str | None:
    d = _detectar()
    return d[0] if d else None


def info() -> dict:
    modelo = modelo_a_usar()
    return {"neuronal": disponible(), "motor": motor(),
            "modelo": modelo.name if modelo else None,
            "instalar": None if disponible() else
            "pipx install piper-tts && python3 -m datito.voz --instalar-modelo"}


def sintetizar(texto: str) -> bytes | None:
    """WAV neuronal del texto, o None si el motor no está o falla.

    Nunca lanza excepciones al llamador: la voz es un adorno del vínculo,
    no un punto de falla del sistema.
    """
    d = _detectar()
    modelo = modelo_a_usar()
    if not d or not modelo or not texto.strip():
        return None
    nombre, binario = d
    try:
        if nombre == "piper":
            with tempfile.TemporaryDirectory() as tmp:
                salida = os.path.join(tmp, "voz.wav")
                r = subprocess.run(
                    [binario, "--model", str(modelo), "--output_file", salida],
                    input=texto.encode("utf-8"),
                    capture_output=True, timeout=60)
                if r.returncode != 0 or not os.path.exists(salida):
                    return None
                with open(salida, "rb") as f:
                    return f.read()
    except Exception:
        return None
    return None


if __name__ == "__main__":
    if "--instalar-modelo" in sys.argv:
        ruta = instalar_modelo()
        print(f"modelo listo: {ruta}")
        print("reinicia el servidor y tendrás voz neuronal en /api/tts")
    else:
        print(info())
