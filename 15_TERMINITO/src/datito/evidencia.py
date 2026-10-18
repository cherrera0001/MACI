"""Evidencia citada o silencio (principio II / research R5).

El LLM debe citar [fid] por afirmacion. El motor valida post-generacion:
  1. toda cita resuelve a un fid existente (SC-002);
  2. hay al menos una cita cuando la respuesta afirma sobre el curso;
  3. chequeo de soporte: la respuesta comparte contenido con el fragmento citado
     (heuristica v1: overlap de tokens de contenido).
Si no pasa, la respuesta se rechaza y el motor recurre al extracto con cita.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .indice import Indice, tokenizar

CITA_RE = re.compile(r"\[([a-z0-9-]+#\d+)\]")
MIN_OVERLAP = 2  # tokens de contenido compartidos (fuera de stopwords)


@dataclass
class ResultadoEvidencia:
    ok: bool
    texto: str
    citas: list[str] = field(default_factory=list)
    invalidas: list[str] = field(default_factory=list)
    sin_soporte: list[str] = field(default_factory=list)
    sin_fuente: bool = False


def extraer_citas(texto: str) -> list[str]:
    return CITA_RE.findall(texto)


def validar(texto: str, indice: Indice) -> ResultadoEvidencia:
    citas = extraer_citas(texto)
    invalidas = [c for c in citas if c not in indice.textos]
    if not citas:
        return ResultadoEvidencia(False, texto, sin_fuente=True)
    if invalidas:
        return ResultadoEvidencia(False, texto, citas, invalidas)
    tokens_resp = set(tokenizar(texto))
    sin_soporte = []
    for cita in set(citas):
        tokens_frag = set(tokenizar(indice.textos[cita]))
        if len(tokens_resp & tokens_frag) < MIN_OVERLAP:
            sin_soporte.append(cita)
    ok = not sin_soporte
    return ResultadoEvidencia(ok, texto, citas, [], sin_soporte)


def bloque_evidencia(citas: list[str], indice: Indice) -> str:
    lineas = []
    for cita in dict.fromkeys(citas):  # orden, sin duplicados
        fuente, ref = indice.referencias.get(cita, ("?", "?"))
        lineas.append(f"  [{cita}] {fuente} · {ref}")
    return "\n".join(lineas)


def limpiar_citas(texto: str) -> str:
    """Quita las marcas [fid] del texto visible."""
    return CITA_RE.sub("", texto).strip()
