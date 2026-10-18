"""Evaluacion por distinciones (principio V): separar conceptos vecinos, no recitar.

Items en evaluaciones/*.yaml: {id, conceptos, pregunta, criterios, pasos, solucion}.
Calificacion: LLM local con rubrica si esta disponible; heuristica de criterios
(palabras clave) en modo exploracion. Resultado actualiza dominio del grafo y
el micro-progreso de la sesion (patron Khan, T066).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from . import llm
from .indice import tokenizar

RESULTADOS = ("no_logrado", "parcial", "logrado")


@dataclass
class Item:
    id: str
    conceptos: list[str]
    pregunta: str
    criterios: list[str]
    pasos: list[str] = field(default_factory=list)
    solucion: str = ""


@dataclass
class ResultadoItem:
    item: Item
    respuesta_estudiante: str
    resultado: str
    retroalimentacion: str
    criterios_logrados: list[str] = field(default_factory=list)


def cargar_items(curso) -> list[Item]:
    items = []
    for p in sorted(curso.ruta("evaluaciones").glob("*.yaml")):
        datos = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for raw in datos.get("items", []):
            if len(raw.get("conceptos", [])) < 2:
                continue  # sin >=2 conceptos vecinos no es distincion
            items.append(Item(
                id=raw["id"], conceptos=raw["conceptos"], pregunta=raw["pregunta"],
                criterios=raw.get("criterios", []), pasos=raw.get("pasos", []),
                solucion=raw.get("solucion", "")))
    return items


def calificar(item: Item, respuesta: str, contexto: str = "") -> ResultadoItem:
    """Rubrica: logrado = todos los criterios; parcial = la mitad o mas."""
    if llm.disponible():
        return _calificar_llm(item, respuesta, contexto)
    return _calificar_heuristica(item, respuesta)


def _calificar_llm(item: Item, respuesta: str, contexto: str) -> ResultadoItem:
    rubrica = "\n".join(f"- {c}" for c in item.criterios)
    prompt = f"""Eres evaluador. Evalua si la respuesta del estudiante logra DISTINGUIR
los conceptos: {', '.join(item.conceptos)}.
Criterios (todos deben cumplirse para 'logrado'):
{rubrica}
Material de referencia: {contexto[:1500]}
Respuesta del estudiante: {respuesta}
Responde SOLO una linea: RESULTADO: no_logrado|parcial|logrado | RETRO: <una frase>"""
    try:
        out = llm.generar(prompt, temperatura=0.0)
        linea = [l for l in out.splitlines() if l.upper().startswith("RESULTADO")][0]
        res = linea.split("|")[0].split(":")[1].strip()
        retro = linea.split("|")[1].split(":", 1)[1].strip() if "|" in linea else out.strip()
        if res not in RESULTADOS:
            raise ValueError(res)
        return ResultadoItem(item, respuesta, res, retro)
    except Exception:
        # ante cualquier fallo del LLM, cae a la heuristica determinista
        return _calificar_heuristica(item, respuesta)


def _criterio_logrado(criterio: str, respuesta: str) -> bool:
    """Heuristica: el criterio se considera logrado si su token principal (raiz
    de 5 chars) aparece en la respuesta. Morfologia espanol simple."""
    claves = [t for t in tokenizar(criterio) if len(t) > 4]
    baja = respuesta.lower()
    return any(t[:5] in baja for t in claves)


def _calificar_heuristica(item: Item, respuesta: str) -> ResultadoItem:
    logrados = [c for c in item.criterios if _criterio_logrado(c, respuesta)]
    n, total = len(logrados), max(1, len(item.criterios))
    resultado = "logrado" if n >= total else ("parcial" if n >= (total + 1) // 2 else "no_logrado")
    return ResultadoItem(item, respuesta, resultado,
                         f"Criterios logrados: {n}/{total}", logrados)


def guardar_resultado(curso, res: ResultadoItem):
    p = curso.ruta("evaluaciones", "resultados.yaml")
    datos = yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {"resultados": []}
    datos["resultados"].append({
        "item_id": res.item.id, "conceptos": res.item.conceptos,
        "resultado": res.resultado, "retroalimentacion": res.retroalimentacion,
        "fecha": __import__("datetime").date.today().isoformat(),
    })
    p.write_text(yaml.safe_dump(datos, allow_unicode=True, sort_keys=False), encoding="utf-8")


def cargar_resultados_guardados(curso) -> list[dict]:
    p = curso.ruta("evaluaciones", "resultados.yaml")
    if not p.exists():
        return []
    return (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("resultados", [])
