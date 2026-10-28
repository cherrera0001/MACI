"""Generadores de transcripts para el harness (REQ-TUT-006).

Un generador recibe un escenario y devuelve un transcript con la misma forma
que los de referencia: {"turnos": [...], "meta": {...}}. El harness evalua las
mismas reglas sin importar quien produjo el transcript.

  referencia  transcripts escritos a mano (verifica al verificador)
  claude      la skill /datito real via `claude -p` en un worktree aislado
  socratico   la politica de 15_TERMINITO (oraculo determinista, REQ-TUT-011)
"""
import importlib
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
TIPOS = {"budget", "timeout", "parse", "skill-no-cargada", "aislamiento", "cli", "esquema"}
NOMBRES = {"referencia": "referencia", "claude": "claude_cli", "socratico": "socratico"}


class ErrorGeneracion(Exception):
    def __init__(self, tipo, detalle=""):
        if tipo not in TIPOS:
            raise ValueError(f"tipo de error desconocido: {tipo}")
        super().__init__(f"{tipo}: {detalle}" if detalle else tipo)
        self.tipo = tipo


def obtener(nombre):
    if nombre not in NOMBRES:
        raise ValueError(f"generador desconocido: {nombre} (validos: {sorted(NOMBRES)})")
    return importlib.import_module(f"{__name__}.{NOMBRES[nombre]}")


def transcript_referencia(esc):
    return yaml.safe_load((BASE / esc["transcript"]).read_text(encoding="utf-8"))


def guion_alumno(esc):
    """Turnos del alumno que un generador vivo debe enviar, en orden.

    Si el escenario declara `turnos_alumno` se usa tal cual; si no, se toman los
    turnos del alumno del transcript de referencia, con sus marcas (resultado,
    pide_respuesta). Devuelve (abre_alumno, turnos): abre_alumno indica si el
    alumno habla antes que el tutor.
    """
    ref = transcript_referencia(esc)["turnos"]
    explicitos = esc.get("turnos_alumno")
    if explicitos is not None:
        if not isinstance(explicitos, list) or not all(isinstance(t, dict) and t.get("texto")
                                                       for t in explicitos):
            raise ErrorGeneracion("esquema", f"{esc['id']}: turnos_alumno mal formado")
        return ref[0]["rol"] == "alumno", explicitos
    marcas = ("texto", "resultado", "pide_respuesta")
    turnos = [{k: t[k] for k in marcas if k in t} for t in ref if t["rol"] == "alumno"]
    return ref[0]["rol"] == "alumno", turnos
