"""Reminiscencia guiada por pistas progresivas (D-12.3).

Vanishing cues sobre LuchaProductiva: tres pistas graduales por memoria
(entidades -> comienzo del relato -> relato completo citado y validado).
Sin estados punitivos: la persona nunca falla; solo se le acercan las pistas.
"""
from __future__ import annotations

import datetime

import yaml

from . import evidencia, progreso
from .lucha import LuchaProductiva


def _ruta(curso):
    return curso.ruta("reminiscencia.yaml")


def _cargar(curso) -> dict | None:
    p = _ruta(curso)
    if not p.exists():
        return None
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def _guardar(curso, datos: dict):
    _ruta(curso).write_text(
        yaml.safe_dump(datos, allow_unicode=True, sort_keys=False),
        encoding="utf-8")


def _memorias(indice) -> list[str]:
    return sorted(
        f for f in indice.textos if f.startswith("memoria#")
        and not indice.referencias.get(f, ("", ""))[1].startswith("guia:"))


def _elegir_memoria(curso, indice) -> str | None:
    memorias = _memorias(indice)
    if not memorias:
        return None
    datos = progreso.cargar(curso)
    idx = int(datos.get("reminiscencia_idx", 0)) % len(memorias)
    datos["reminiscencia_idx"] = idx + 1
    progreso.guardar(curso, datos)
    return memorias[idx]


def _entidades_de(fid: str, indice, top: int = 3) -> list[str]:
    vec = indice.vectores.get(fid) or {}
    orden = sorted(vec, key=lambda t: -indice.idf.get(t, 1.0))
    largos = [t for t in orden if len(t) >= 4]
    return (largos or orden)[:top]


def _pistas(fid: str, indice) -> list[str]:
    texto = indice.textos[fid]
    palabras = texto.split()
    ents = _entidades_de(fid, indice)
    guia = ", ".join(ents) if ents else "su vida"
    corte = " ".join(palabras[:max(4, int(len(palabras) * 0.6))]).rstrip(",;.")
    pistas = [
        f"Vamos a recordar juntos algo de su vida. Esto tiene que ver con "
        f"{guia}. ¿Se le ocurre de qué hablamos?",
        f"Le acerco otra pista: «{corte}…». ¿Le suena?",
        f"Se lo cuento completo: «{texto}» [{fid}] — me encanta esta historia "
        f"suya. ¿Qué más recuerda de eso?",
    ]
    # la pista final evoca el pasado: su cita debe validar o se retira
    val = evidencia.validar(pistas[2], indice)
    if not val.ok:
        pistas[2] = pistas[2].replace(f" [{fid}]", "")
    return pistas


def siguiente(curso, indice, nueva: bool = False) -> dict:
    """Devuelve la pista siguiente (o la primera) de la reminiscencia."""
    est = _cargar(curso)
    if nueva or not est or est.get("fid") not in indice.textos:
        fid = _elegir_memoria(curso, indice)
        if fid is None:
            return {"pista": None, "motivo": "sin_memorias"}
        est = {"fid": fid, "revelados": 0}
    pistas = _pistas(est["fid"], indice)
    lucha = LuchaProductiva(pasos=pistas, estado="pista",
                            pasos_revelados=int(est.get("revelados", 0)))
    if lucha.pasos_revelados >= len(pistas):
        pista = pistas[-1]
    else:
        pista = lucha.mostrar_paso()
        est["revelados"] = lucha.pasos_revelados
    est["fecha"] = datetime.date.today().isoformat()
    _guardar(curso, est)
    return {"fid": est["fid"], "pista_n": lucha.pasos_revelados,
            "total": len(pistas), "pista": pista,
            "completa": lucha.pasos_revelados >= len(pistas),
            "estado_interaccion": lucha.estado}
