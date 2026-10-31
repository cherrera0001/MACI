"""Síntesis de voz neuronal local (D-12.1). Zero-lock-in, misma filosofía que llm.py.

Detecta un motor neuronal offline (hoy: piper) y sintetiza WAV; si no hay
motor, degrada limpio y /api/salud explica cómo activarlo con un comando.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile

_MOTOR: tuple[str, str] | None | bool = None  # cache: (nombre, binario)

GUIA_INSTALACION = ("pipx install piper-tts   # y un modelo en español: "
                    "https://github.com/rhasspy/piper/blob/master/VOICES.md")


def _detectar() -> tuple[str, str] | None:
    global _MOTOR
    if _MOTOR is None:
        piper = shutil.which("piper")
        _MOTOR = ("piper", piper) if piper else False
    return _MOTOR or None


def disponible() -> bool:
    return _detectar() is not None


def motor() -> str | None:
    d = _detectar()
    return d[0] if d else None


def info() -> dict:
    return {"neuronal": disponible(), "motor": motor(),
            "instalar": None if disponible() else GUIA_INSTALACION}


def sintetizar(texto: str) -> bytes | None:
    """WAV neuronal del texto, o None si el motor no está o falla.

    Nunca lanza excepciones al llamador: la voz es un adorno del vínculo,
    no un punto de falla del sistema.
    """
    d = _detectar()
    if not d or not texto.strip():
        return None
    nombre, binario = d
    try:
        if nombre == "piper":
            modelo = os.environ.get("TERMITO_VOZ_MODELO",
                                    "es_ES-davefx-medium")
            with tempfile.TemporaryDirectory() as tmp:
                salida = os.path.join(tmp, "voz.wav")
                r = subprocess.run(
                    [binario, "--model", modelo, "--output_file", salida],
                    input=texto.encode("utf-8"),
                    capture_output=True, timeout=60)
                if r.returncode != 0 or not os.path.exists(salida):
                    return None
                with open(salida, "rb") as f:
                    return f.read()
    except Exception:
        return None
    return None
