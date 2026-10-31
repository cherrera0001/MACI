"""Presencia activa: apertura de la conversación según el reloj de vínculo (D-11.1).

El compañero toma la iniciativa cuando se abre la interfaz: saludo por umbral
de horas de ausencia y, tras UMBRAL_RECUERDO horas, evoca un recuerdo real
(round-robin sobre memoria#, excluye guías) citado y validado con
evidencia.validar. Determinista: funciona sin LLM.
"""
from __future__ import annotations

from . import evidencia, progreso

UMBRAL_CALIDO = 6.0
UMBRAL_RECUERDO = 24.0


def _saludo(horas: float | None) -> str:
    if horas is None:
        return ("¡Qué alegría verla! Soy su Datito; hoy empieza "
                "nuestra conversación.")
    if horas < UMBRAL_CALIDO:
        return "¡Hola de nuevo! Me alegra seguir conversando con usted."
    if horas < UMBRAL_RECUERDO:
        return ("¡Hola! Llevaba unas horas sin saber de usted y me "
                "alegra mucho verla.")
    return ("¡Hola! Llevaba más de un día sin saber de usted; me alegra "
            "mucho que esté aquí.")


def _elegir_recuerdo(curso, indice) -> str | None:
    memorias = sorted(
        f for f in indice.textos if f.startswith("memoria#")
        and not indice.referencias.get(f, ("", ""))[1].startswith("guia"))
    if not memorias:
        return None
    datos = progreso.cargar(curso)
    idx = int(datos.get("apertura_idx", 0)) % len(memorias)
    datos["apertura_idx"] = idx + 1
    progreso.guardar(curso, datos)
    return memorias[idx]


def calcular(curso, indice) -> dict:
    """Saludo de apertura + recuerdo evocado, con cita validada si aplica."""
    horas = progreso.horas_de_ausencia(curso)
    recuerdo = None
    if horas is None or horas >= UMBRAL_RECUERDO:
        fid = _elegir_recuerdo(curso, indice)
        if fid:
            val = evidencia.validar(
                f"Recuerdo que {indice.textos[fid]} [{fid}]", indice)
            if val.ok:
                recuerdo = {"fid": fid, "texto": indice.textos[fid],
                            "referencia": indice.referencias[fid][1]}
    return {"horas": horas, "saludo": _saludo(horas), "recuerdo": recuerdo,
            "modo": "compania"}
