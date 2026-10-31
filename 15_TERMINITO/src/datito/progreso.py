"""Progreso: metricas de adopcion (T067) + micro-progreso de sesion (T066).

progreso.yaml: {metricas: {sesiones, mensajes, evaluaciones_completadas,
tiempo_minutos, racha_dias}, ultima_sesion, distinciones_sesion}
"""
from __future__ import annotations

import datetime
from pathlib import Path

import yaml

METRICAS_DEFECTO = {
    "sesiones": 0, "mensajes": 0, "evaluaciones_completadas": 0,
    "tiempo_minutos": 0, "racha_dias": 0,
}


def ruta(curso) -> Path:
    return curso.ruta("progreso.yaml")


def cargar(curso) -> dict:
    p = ruta(curso)
    if p.exists():
        datos = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    else:
        datos = {}
    datos.setdefault("metricas", dict(METRICAS_DEFECTO))
    for k, v in METRICAS_DEFECTO.items():
        datos["metricas"].setdefault(k, v)
    return datos


def guardar(curso, datos: dict):
    ruta(curso).write_text(
        yaml.safe_dump(datos, allow_unicode=True, sort_keys=False), encoding="utf-8")


def iniciar_sesion(curso) -> dict:
    datos = cargar(curso)
    hoy = datetime.date.today().isoformat()
    if datos.get("ultima_sesion") != hoy:
        datos["metricas"]["sesiones"] += 1
        ayer = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
        datos["metricas"]["racha_dias"] = (
            datos["metricas"]["racha_dias"] + 1
            if datos.get("ultima_sesion") == ayer else 1)
        datos["ultima_sesion"] = hoy
        datos["distinciones_sesion"] = 0
        guardar(curso, datos)
    return datos


def contar_mensaje(curso, n: int = 1):
    datos = cargar(curso)
    datos["metricas"]["mensajes"] += n
    guardar(curso, datos)


def marcar_interaccion(curso):
    """Reloj de vínculo (D-11.1): stamp ISO de la última interacción real."""
    datos = cargar(curso)
    datos["ultima_interaccion"] = datetime.datetime.now().isoformat(
        timespec="seconds")
    guardar(curso, datos)


def horas_de_ausencia(curso) -> float | None:
    """Horas desde la última interacción; None si aún no hay ninguna."""
    u = cargar(curso).get("ultima_interaccion")
    if not u:
        return None
    try:
        ultima = datetime.datetime.fromisoformat(u)
    except ValueError:
        return None
    return max(0.0, (datetime.datetime.now() - ultima).total_seconds() / 3600)


def contar_distincion(curso, lograda: bool):
    """Micro-progreso visible: 'N distinciones de esta sesion'."""
    datos = cargar(curso)
    datos["distinciones_sesion"] = datos.get("distinciones_sesion", 0) + 1
    datos.setdefault("distinciones_logradas_sesion", 0)
    if lograda:
        datos["distinciones_logradas_sesion"] += 1
    guardar(curso, datos)
    return datos["distinciones_sesion"], datos["distinciones_logradas_sesion"]


def resumen(curso) -> str:
    datos = cargar(curso)
    m = datos["metricas"]
    return (f"sesiones: {m['sesiones']} · mensajes: {m['mensajes']} · "
            f"evaluaciones: {m['evaluaciones_completadas']} · "
            f"racha: {m['racha_dias']} dia(s) · "
            f"distinciones de esta sesion: "
            f"{datos.get('distinciones_logradas_sesion', 0)}/"
            f"{datos.get('distinciones_sesion', 0)}")
