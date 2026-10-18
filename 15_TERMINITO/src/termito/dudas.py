"""Registro de dudas resueltas (patron maci.c4a.cl, esquema de 07_DATITO/dudas.yaml).

Cada duda queda con pregunta, respuesta del tutor, procedimiento y fuentes.
Fuente unica: nada de lo que se explica queda solo en la terminal (G9).
"""
from __future__ import annotations

import datetime
from pathlib import Path

import yaml


def ruta_dudas(curso) -> Path:
    return curso.ruta("dudas.yaml")


def cargar(curso) -> list[dict]:
    p = ruta_dudas(curso)
    if not p.exists():
        return []
    datos = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    return datos.get("dudas", [])


def registrar(curso, pregunta: str, respuesta: str, resolucion: str,
              fuentes: list[str], conceptos: list[str] | None = None) -> dict:
    dudas = cargar(curso)
    hoy = datetime.date.today().isoformat()
    duda = {
        "id": f"{hoy}-{len(dudas) + 1:02d}",
        "fecha": hoy,
        "conceptos": conceptos or [],
        "estado": "resuelta",
        "pregunta": pregunta.strip(),
        "respuesta": respuesta.strip()[:500],
        "resolucion": resolucion.strip(),
        "fuentes": fuentes,
    }
    dudas.append(duda)
    ruta_dudas(curso).write_text(
        yaml.safe_dump({"dudas": dudas}, allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    return duda
