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


def entidades(indice, min_df: int = 2, min_len: int = 4) -> dict:
    """Mapa de entidades recurrentes: token -> fids de memorias (no guías).

    Una entidad es un término de contenido presente en al menos min_df
    memorias: los nietos, Rufo, Temuco. Es la materia prima de la Bitácora
    de Vida y de la reminiscencia.
    """
    memorias = {f for f in indice.textos if f.startswith("memoria#")
                and not indice.referencias.get(f, ("", ""))[1].startswith("guia:")}
    salida = {}
    for t in indice.idf:
        if len(t) < min_len:
            continue
        fids = sorted(f for f in memorias
                      if t in (indice.vectores.get(f) or {}))
        if len(fids) >= min_df:
            salida[t] = fids
    return salida


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
