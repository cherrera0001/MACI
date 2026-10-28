"""Generador de referencia: el transcript escrito a mano del escenario."""
from . import transcript_referencia


def generar(esc, corrida=1, **_):
    tr = transcript_referencia(esc)
    tr.setdefault("meta", {}).update({"generador": "referencia", "corrida": corrida, "costo_usd": 0.0})
    return tr
