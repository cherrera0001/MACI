"""Bitácora de historias de vida (D-12.3): legado con citas, sin alertas.

Agrupa las memorias consolidadas por entidades recurrentes con sus [fid]
verificables, lista para compartir con la familia. Las alertas de guardian
viven en alertas.yaml y jamás entran al legado.
"""
from __future__ import annotations

import datetime

from . import cerebro, memoria


def construir(curso, indice) -> dict:
    memorias = [f for f in sorted(indice.textos)
                if f.startswith("memoria#")
                and not indice.referencias.get(f, ("", ""))[1].startswith("guia:")]
    entidades = memoria.entidades(indice)
    # E-15: con cerebro activo, el orden de capítulos sigue la activación
    # acumulada del grafo (temas más vivos primero); sin cerebro, recuento.
    rango = cerebro.orden_entidades(curso)

    def peso(kv):
        ent, fids = kv
        if rango:
            return (rango.get(ent, len(rango)), ent)  # temas desconocidos al final
        return (-len(fids), ent)

    grupos: dict[str, list] = {}
    asignadas: set[str] = set()
    ordenadas = sorted(entidades.items(), key=peso)
    for ent, fids in ordenadas:
        vivos = [f for f in fids if f in memorias]
        if len(vivos) < 2:
            continue
        grupos[ent] = [{"fid": f, "texto": indice.textos[f]} for f in vivos]
        asignadas.update(vivos)
    return {"entidades": grupos,
            "otras": [{"fid": f, "texto": indice.textos[f]}
                      for f in memorias if f not in asignadas],
            "total": len(memorias),
            "alertas": 0,
            "generado": datetime.date.today().isoformat()}
