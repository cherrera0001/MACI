"""Cliente LLM local (Ollama) via urllib de stdlib. Modo exploracion sin Ollama.

El motor funciona sin modelo: 'modo exploracion' muestra estructura y
evidencia recuperada, pero no genera respuestas (spec: edge case LLM ausente).
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

from . import config


class ModoExploracion(Exception):
    """No hay LLM local disponible."""


def _get(path: str, timeout: float = 3.0) -> dict:
    with urllib.request.urlopen(config.OLLAMA_HOST + path, timeout=timeout) as r:
        return json.loads(r.read().decode())


def _post(path: str, payload: dict, timeout: float = 180.0) -> dict:
    req = urllib.request.Request(
        config.OLLAMA_HOST + path,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def disponible() -> bool:
    try:
        _get("/api/version", timeout=2.0)
        return True
    except Exception:
        return False


def modelo_instalado(modelo: str = config.MODELO) -> bool:
    try:
        tags = _get("/api/tags")
        return any(m.get("name", "").startswith(modelo.split(":")[0])
                   for m in tags.get("models", []))
    except Exception:
        return False


def generar(prompt: str, modelo: str = config.MODELO, temperatura: float = 0.3) -> str:
    """Genera texto con el modelo local. Lanza ModoExploracion si no hay Ollama."""
    if not disponible():
        raise ModoExploracion(
            f"Ollama no responde en {config.OLLAMA_HOST}. "
            "Instala Ollama (https://ollama.com) y ejecuta: "
            f"ollama pull {modelo}")
    try:
        resp = _post("/api/generate", {
            "model": modelo, "prompt": prompt, "stream": False,
            "options": {"temperature": temperatura},
        })
        return (resp.get("response") or "").strip()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ModoExploracion(
                f"modelo '{modelo}' no instalado. Ejecuta: ollama pull {modelo}")
        raise
