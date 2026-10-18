"""Grafo de prerrequisitos con estado de dominio y gating (US5, patron Mathigon).

grafo/grafo.yaml   — estructura (nodos, viene_de/habilita) migrada de v0.0.1
grafo/dominio.yaml — estado por nodo (no_estudiado..dominado)
Panel textual con colores ANSI; gating: solo se muestran nodos cuyos
prerrequisitos estan dominados/en_estudio; escape "revelar mapa completo".
"""
from __future__ import annotations

from pathlib import Path

import yaml

from .config import ESTADOS_DOMINIO

COLOR = {"no_estudiado": "\033[90m", "en_estudio": "\033[33m",
         "comprendido": "\033[36m", "dominado": "\033[32m", "fin": "\033[0m"}
SIMBOLO = {"no_estudiado": "○", "en_estudio": "◐",
           "comprendido": "◑", "dominado": "●"}


def cargar_grafo(curso) -> dict:
    p = curso.ruta("grafo", "grafo.yaml")
    if not p.exists():
        return {"meta": {}, "cadenas": {}, "nodos": {}}
    datos = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    # formatos soportados: nodos bajo 'nodos' o 'conceptos', o como claves
    # de primer nivel con campo 'nombre' (grafo v0.0.1 usa 'conceptos')
    nodos = datos.get("nodos") or datos.get("conceptos")
    if nodos is None:
        nodos = {k: v for k, v in datos.items()
                 if isinstance(v, dict) and "nombre" in v}
    return {"meta": datos.get("meta", {}), "cadenas": datos.get("cadenas", {}),
            "nodos": nodos or {}}


def ruta_dominio(curso) -> Path:
    return curso.ruta("grafo", "dominio.yaml")


def cargar_dominio(curso) -> dict:
    p = ruta_dominio(curso)
    if p.exists():
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    return {}


def guardar_dominio(curso, dominio: dict):
    ruta_dominio(curso).write_text(
        yaml.safe_dump(dominio, allow_unicode=True, sort_keys=False), encoding="utf-8")


def estado_nodo(curso, concepto: str) -> str:
    dom = cargar_dominio(curso)
    return dom.get(concepto, {}).get("estado", "no_estudiado")


def actualizar_dominio(curso, conceptos: list[str], resultado: str):
    """logrado->dominado; parcial/no_logrado->en_estudio. Reevalua 'comprendido'."""
    dom = cargar_dominio(curso)
    grafo = cargar_grafo(curso)
    for concepto in conceptos:
        entrada = dom.setdefault(concepto, {})
        previo = entrada.get("estado", "no_estudiado")
        if resultado == "logrado":
            entrada["estado"] = "dominado"
        elif previo == "no_estudiado":
            entrada["estado"] = "en_estudio"
        entrada["ultimo_resultado"] = resultado
    # comprendido = dominado pero con al menos un habilitado aun no dominado
    for concepto, nodo in grafo.get("nodos", {}).items():
        entrada = dom.get(concepto)
        if not entrada or entrada.get("estado") != "dominado":
            continue
        habilitados = nodo.get("habilita", []) + nodo.get("habilita_indirectamente", [])
        if any(dom.get(h, {}).get("estado") != "dominado" for h in habilitados):
            entrada["estado"] = "comprendido"
    guardar_dominio(curso, dom)


def _visible(nodo: dict, dominio: dict) -> bool:
    """Visible si el nodo fue tocado o algun prerrequisito esta empezado
    (gating progresivo: se revela lo que se estudia, no todo el mapa)."""
    nombre = nodo.get("id", "")
    if dominio.get(nombre, {}).get("estado", "no_estudiado") != "no_estudiado":
        return True
    reqs = nodo.get("requiere_antes", []) or nodo.get("viene_de", [])
    return any(dominio.get(r, {}).get("estado", "no_estudiado") != "no_estudiado"
               for r in reqs) or not reqs


def panel(curso, mapa_completo: bool = False, color: bool = True) -> str:
    """Panel de dominio. Gating: solo visibles con prerrequisitos empezados."""
    grafo = cargar_grafo(curso)
    dominio = cargar_dominio(curso)
    lineas = [f"— Dominio: {curso.datos.get('nombre')} —"]
    for cadena, miembros in (grafo.get("cadenas") or {}).items():
        lineas.append(f"\n[{cadena.replace('_', ' ')}]")
        for m in miembros:
            nodo = grafo.get("nodos", {}).get(m)
            if not nodo:
                continue
            if not mapa_completo and not _visible({**nodo, "id": m}, dominio):
                continue
            est = dominio.get(m, {}).get("estado", "no_estudiado")
            if est not in ESTADOS_DOMINIO:
                est = "no_estudiado"
            nombre = nodo.get("nombre", m)
            prefijo = COLOR.get(est, "") + SIMBOLO.get(est, "?") if color else SIMBOLO.get(est, "?")
            reset = COLOR["fin"] if color else ""
            lineas.append(f"  {prefijo} {nombre} ({est}){reset}")
    if not mapa_completo:
        lineas.append("\n(mostando solo lo desbloqueado; 'datito status --mapa' revela todo)")
    return "\n".join(lineas)
