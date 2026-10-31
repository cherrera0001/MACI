"""Detección determinista de recuerdos episódicos (modo compañía, T-10.3.1).

v1 sin LLM: una oración es un recuerdo candidato si tiene al menos
MIN_PALABRAS palabras y contiene un nombre propio (mayúscula no inicial)
o un marcador de primera persona. Las preguntas no son recuerdos. Tope
MAX_POR_MENSAJE por mensaje para no inundar la memoria.
"""
from __future__ import annotations

import re

MAX_POR_MENSAJE = 3
MIN_PALABRAS = 4
MARCAS_PRIMERA_PERSONA = (" mi ", " mis ", " me ", " yo ", " mí ", " conmigo ")
_SPLIT = re.compile(r"[.!?\n]+")


def _nombre_propio(oracion: str) -> bool:
    for p in oracion.split()[1:]:          # la palabra inicial no cuenta
        limpio = p.strip('",;:()¿¡"').strip()
        if len(limpio) >= 2 and limpio[0].isupper() \
                and not limpio.isupper():  # excluye siglas y gritos
            return True
    return False


def _primera_persona(oracion: str) -> bool:
    n = " " + oracion.lower() + " "
    return any(m in n for m in MARCAS_PRIMERA_PERSONA)


def detectar(texto: str, max_recuerdos: int = MAX_POR_MENSAJE) -> list[str]:
    """Oraciones del texto que merecen quedar en la memoria episódica."""
    candidatos = []
    for oracion in _SPLIT.split(texto or ""):
        o = " ".join(oracion.split())
        if not o or o.endswith("?"):
            continue
        if len(o.split()) < MIN_PALABRAS:
            continue
        if _nombre_propio(o) or _primera_persona(o):
            candidatos.append(o)
        if len(candidatos) >= max_recuerdos:
            break
    return candidatos
