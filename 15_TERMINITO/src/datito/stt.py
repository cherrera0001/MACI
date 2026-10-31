"""STT local (D-16.1): adaptador faster-whisper estilo llm.py/voz.py.

El audio del usuario se transcribe **en esta máquina** y se descarta:
nada persiste, nada sale de la LAN. Si faster-whisper no está instalado,
``disponible()`` es False y /api/salud explica cómo activarlo con un comando.
El paquete datito no declara esta dependencia (zero-lock-in, como piper).
"""
from __future__ import annotations

import importlib.util
import io
import wave

_FW = importlib.util.find_spec("faster_whisper")
DISPONIBLE = _FW is not None

_MODELO = "base"          # ~150 MB descarga en primer uso; "small" = más exacto
_IDIOMA = "es"
_MOTOR = None             # caché del modelo cargado

# Benchmarks públicos aproximados (CPU moderna) para el reporte cuando el
# motor no está instalado en la máquina de medición. Los números reales
# siempre reemplazan a estos en eval_conversacion.py.
REFERENCIA_CPU_BASE_MS = 900.0


def disponible() -> bool:
    return DISPONIBLE


def motor() -> str | None:
    return "faster-whisper" if DISPONIBLE else None


def info() -> dict:
    return {
        "activo": DISPONIBLE,
        "motor": motor(),
        "modelo": _MODELO if DISPONIBLE else None,
        "guia": (f"uv pip install --python .venv/bin/python faster-whisper  "
                 f"(modelo '{_MODELO}' ~150 MB en el primer uso)") if not DISPONIBLE else None,
    }


def _cargar():
    global _MOTOR
    if _MOTOR is None:
        from faster_whisper import WhisperModel

        _MOTOR = WhisperModel(_MODELO, device="cpu", compute_type="int8")
    return _MOTOR


def _a_pcm(datos: bytes):
    """Audio como numpy float32 a 16 kHz, listo para faster-whisper.

    WAV estándar: decodificación stdlib (wave + audioop-like), sin PyAV.
    Otros contenedores (webm/opus del navegador): PyAV vía decode_audio.
    """
    import numpy as np

    if datos[:4] == b"RIFF":
        with wave.open(io.BytesIO(datos), "rb") as w:
            n = w.getnframes()
            sr = w.getframerate()
            pcm = np.frombuffer(w.readframes(n), dtype="int16").astype("float32") / 32768.0
        if sr != 16000:  # kokoro habla a 24 kHz
            paso = max(1, round(sr / 16000))
            pcm = pcm[::paso]
        return pcm
    from faster_whisper.audio import decode_audio

    return decode_audio(io.BytesIO(datos))


def transcribir(datos: bytes) -> str | None:
    """Texto del audio, o None si no hay motor o falla. Nunca lanza."""
    if not DISPONIBLE or not datos:
        return None
    try:
        segmentos, _ = _cargar().transcribe(_a_pcm(datos), language=_IDIOMA,
                                            beam_size=5, vad_filter=True)
        return " ".join(s.text.strip() for s in segmentos).strip() or None
    except Exception:
        return None
