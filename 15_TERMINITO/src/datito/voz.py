"""Síntesis de voz neuronal local (D-12.1 + D-13.3 + D-16.2). Zero-lock-in.

Motores soportados (detección en runtime, ninguno es dependencia dura):
- **piper**: binario + modelo .onnx (autodescubrimiento en 15_TERMINITO/.piper/
  y ~/.local/share/piper/), activación:
    pipx install piper-tts && python3 -m datito.voz --instalar-modelo
- **kokoro**: paquete kokoro-onnx (o kokoro) + pesos en 15_TERMINITO/.kokoro/,
  activación:
    uv pip install --python .venv/bin/python kokoro-onnx

Selección: argumento ``motor`` > clave ``voz:`` del curso.yaml
(piper|kokoro|auto) > primer motor disponible. Si no hay nada, degrada
limpio y /api/salud explica cómo activarlo.
"""
from __future__ import annotations

import importlib.util
import io
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import wave
from pathlib import Path

from . import config

_DETECTADO: dict[str, bool] | None = None  # cache: {piper: bool, kokoro: bool}
# Compat E-12/E-13: cache piper de la API original (None = sin cache,
# False = piper ausente, (nombre, binario) = piper presente). Los tests lo
# usan como palanca; kokoro se apaga en tests mockeando _kokoro_listo.
_MOTOR: tuple[str, str] | None | bool = None

MODELO_POR_DEFECTO = "es_ES-davefx-medium"
# v1.0.0 de rhasspy/piper-voices: voz es neutra/culta, lista para usar.
URL_MODELO = ("https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/"
              "es/es_ES/davefx/medium/es_ES-davefx-medium")
VOZ_KOKORO_DEFECTO = "ef_dora"   # voz femenina latina de Kokoro
URL_KOKORO = ("https://github.com/thewh1teagle/kokoro-onnx/releases/download/"
              "model-files-v1.0/kokoro-v1.0.onnx")
URL_KOKORO_VOCES = ("https://github.com/thewh1teagle/kokoro-onnx/releases/"
                    "download/model-files-v1.0/voices-v1.0.bin")
PASOS_KOKORO = 1.0               # naturalidad; el A/B (D-16.2) lo calibra


# ------------------------------------------------------------------ piper
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
    global _DETECTADO, _MOTOR
    _DETECTADO = None  # re-detectar con el nuevo modelo
    return onnx


# ----------------------------------------------------------------- kokoro
def _dir_kokoro() -> Path:
    return config.RAIZ / ".kokoro"


def _kokoro_listo() -> bool:
    d = _dir_kokoro()
    return (d / "kokoro-v1.0.onnx").exists() and (d / "voices-v1.0.bin").exists()


def instalar_kokoro() -> Path:
    """Descarga pesos de Kokoro listos para usar. Devuelve el .onnx."""
    d = _dir_kokoro()
    d.mkdir(parents=True, exist_ok=True)
    onnx = d / "kokoro-v1.0.onnx"
    for ruta, url in ((onnx, URL_KOKORO),
                      (d / "voices-v1.0.bin", URL_KOKORO_VOCES)):
        if not ruta.exists():
            with urllib.request.urlopen(url, timeout=600) as r:
                ruta.write_bytes(r.read())
    global _DETECTADO, _PIPE_KOKORO
    _DETECTADO = None
    _PIPE_KOKORO = None
    return onnx


_PIPE_KOKORO = None


def _pipeline_kokoro():
    global _PIPE_KOKORO
    if _PIPE_KOKORO is None:
        try:
            from kokoro_onnx import Kokoro

            _PIPE_KOKORO = Kokoro(str(_dir_kokoro() / "kokoro-v1.0.onnx"),
                                  str(_dir_kokoro() / "voices-v1.0.bin"))
        except Exception:
            try:  # variante con dependencia pesada (torch)
                from kokoro import KPipeline

                _PIPE_KOKORO = KPipeline(lang_code="e")
            except Exception:
                return None
    return _PIPE_KOKORO


def _wav_desde_muestras(muestras, sr: int) -> bytes:
    import numpy as np

    pcm = (np.asarray(muestras, dtype="float32").clip(-1, 1) * 32767) \
        .astype("int16")
    with io.BytesIO() as buf:
        with wave.open(buf, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sr)
            w.writeframes(pcm.tobytes())
        return buf.getvalue()


def _sintetizar_kokoro(texto: str) -> bytes | None:
    try:
        pipe = _pipeline_kokoro()
        if pipe is None:
            return None
        if hasattr(pipe, "create"):            # kokoro-onnx
            muestras, sr = pipe.create(texto, voice=VOZ_KOKORO_DEFECTO,
                                       speed=PASOS_KOKORO, lang="es")
            return _wav_desde_muestras(muestras, sr)
        for _, _, audio in pipe(texto, voice=VOZ_KOKORO_DEFECTO,  # kokoro
                                speed=PASOS_KOKORO, lang="es"):
            return _wav_desde_muestras(audio.cpu().numpy(), 24000)
    except Exception:
        return None
    return None


# --------------------------------------------------------------- detección
def motores_disponibles() -> dict[str, bool]:
    """{piper: bool, kokoro: bool}. Cacheado por proceso.

    El cache piper retrocompatible (_MOTOR: False ausente, tuple presente)
    sigue siendo la palanca que usan los tests E-12/E-13; kokoro se detecta
    por paquete + pesos presentes.
    """
    global _DETECTADO
    if _DETECTADO is None:
        m = globals()["_MOTOR"]
        if m is False:
            piper_ok = False
        elif isinstance(m, tuple):
            piper_ok = True
        else:
            piper_ok = bool(shutil.which("piper") and modelo_a_usar())
        _DETECTADO = {
            "piper": piper_ok,
            "kokoro": (importlib.util.find_spec("kokoro_onnx") is not None
                       or importlib.util.find_spec("kokoro") is not None)
                      and _kokoro_listo(),
        }
    return dict(_DETECTADO)


def disponible(motor: str | None = None) -> bool:
    m = motores_disponibles()
    return m.get(motor, False) if motor else any(m.values())


def info() -> dict:
    m = motores_disponibles()
    modelo = modelo_a_usar()
    activo = next((k for k, v in m.items() if v), None)
    return {"neuronal": any(m.values()), "motor": activo, "motores": m,
            "modelo": modelo.name if modelo and m.get("piper")
            else ("kokoro-v1.0" if m.get("kokoro") else None),
            "instalar": None if any(m.values()) else
            ("pipx install piper-tts && python3 -m datito.voz --instalar-modelo "
             "|| uv pip install --python .venv/bin/python kokoro-onnx && "
             "python3 -m datito.voz --instalar-kokoro")}


def resolver_motor(curso=None, motor: str | None = None) -> str | None:
    """motor explícito > voz del curso.yaml > primer motor disponible."""
    m = motores_disponibles()
    if motor and motor != "auto":
        return motor if m.get(motor) else None
    preferencia = "auto"
    if curso is not None:
        preferencia = str((getattr(curso, "datos", None) or {})
                          .get("voz", "auto")).lower()
    if preferencia in m:
        # preferencia explícita: solo ese motor (None si no está: silencio
        # con aviso en /api/salud, nunca sustituto sorpresa)
        return preferencia if m[preferencia] else None
    return next((k for k, v in m.items() if v), None)


def sintetizar(texto: str, curso=None, motor: str | None = None) -> bytes | None:
    """WAV neuronal del texto, o None si el motor no está o falla.

    Nunca lanza excepciones al llamador: la voz es un adorno del vínculo,
    no un punto de falla del sistema.
    """
    if not texto.strip():
        return None
    elegido = resolver_motor(curso, motor)
    if elegido is None:
        return None
    if elegido == "kokoro":
        return _sintetizar_kokoro(texto)
    modelo = modelo_a_usar()
    if not modelo:
        return None
    try:
        with tempfile.TemporaryDirectory() as tmp:
            salida = os.path.join(tmp, "voz.wav")
            r = subprocess.run(
                ["piper", "--model", str(modelo), "--output_file", salida],
                input=texto.encode("utf-8"),
                capture_output=True, timeout=60)
            if r.returncode != 0 or not os.path.exists(salida):
                return None
            with open(salida, "rb") as f:
                return f.read()
    except Exception:
        return None


if __name__ == "__main__":
    if "--instalar-modelo" in sys.argv:
        ruta = instalar_modelo()
        print(f"modelo listo: {ruta}")
        print("reinicia el servidor y tendrás voz neuronal en /api/tts")
    elif "--instalar-kokoro" in sys.argv:
        ruta = instalar_kokoro()
        print(f"kokoro listo: {ruta}")
    else:
        print(info())
