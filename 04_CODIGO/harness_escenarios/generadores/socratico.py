"""Generador socratico: la politica de 15_TERMINITO como oraculo (REQ-TUT-011).

Corre sin red ni LLM. Si un escenario pasa aqui y falla con `claude`, el
defecto esta en el prompt de la skill; si falla en los dos, en el escenario o
en la regla. La politica no conoce G6 (degradacion): esos escenarios fallan a
proposito y quedan en el reporte de divergencia.
"""
import sys

from . import BASE, guion_alumno

sys.path.insert(0, str(BASE.parent.parent / "15_TERMINITO" / "src"))
from datito import socratico as pol_mod  # noqa: E402


def generar(esc, corrida=1, **_):
    abre_alumno, guion = guion_alumno(esc)
    senal = esc.get("senal_solucion") or "La respuesta completa"
    pol = pol_mod.Politica(pol_mod.Concepto(esc["id"]),
                           solucion=f"{senal} (solucion del escenario {esc['id']}).",
                           pistas=["Mira que mide cada numero antes de comparar."])
    if not abre_alumno:
        pol.responder(esc["entrada"])  # el tutor abre: la politica responde al tema
    for t in guion:
        if t.get("resultado") in ("fallo", "acerto"):
            pol.responder(t["texto"], es_intento=True, acierto=t["resultado"] == "acerto")
            pol.turnos[-2 if pol.turnos[-1]["rol"] == "tutor" else -1]["texto"] = t["texto"]
        else:
            pol.responder(t["texto"])
            if t.get("pide_respuesta"):
                pol.turnos[-2]["pide_respuesta"] = True
        # R5 por cada entrega (Politica.transferida no se reinicia entre entregas)
        if any(str(a).startswith("entrega:") for a in pol.turnos[-1].get("acciones", [])):
            pol.exigir_transferencia()
    return {"turnos": pol.turnos, "meta": {"generador": "socratico", "corrida": corrida,
                                           "costo_usd": 0.0, "metricas": pol.metricas()}}
