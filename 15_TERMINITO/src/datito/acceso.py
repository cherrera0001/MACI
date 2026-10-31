"""Acceso por dispositivo con token de un solo uso (D-16.3).

Modelo de amenaza (ver docs/gestion/THREAT_MODEL.md): la red LAN no es
confiable (Wi-Fi compartido, visitas, dispositivos desconocidos). Para los
endpoints sensibles del modo compañía (/mensajes, /familiar) el curso puede
activar `seguridad.yaml`: un token de un solo uso vincula un dispositivo
(canje 1:1 → device_id persistente), revocable desde el servidor.

Retrocompatible: sin seguridad.yaml, todo sigue abierto como hasta E-15
(los 186 tests previos no rotan; los tests nuevos crean el archivo).
"""
from __future__ import annotations

import hashlib
import secrets
import uuid
from pathlib import Path

import yaml

RUTA = "seguridad.yaml"


def _ruta(curso) -> Path:
    return curso.ruta(RUTA)


def activada(curso) -> bool:
    return _ruta(curso).exists()


def _cargar(curso) -> dict:
    p = _ruta(curso)
    if not p.exists():
        return {"tokens": {}, "dispositivos": {}}
    return yaml.safe_load(p.read_text("utf-8")) or {"tokens": {}, "dispositivos": {}}


def _guardar(curso, datos: dict) -> None:
    _ruta(curso).write_text(
        yaml.safe_dump(datos, allow_unicode=True, sort_keys=False),
        encoding="utf-8")


def _h(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def emitir(curso, etiqueta: str = "") -> str:
    """Crea un token de un solo uso. Mostrar UNA vez al cuidador/familiar."""
    datos = _cargar(curso)
    token = secrets.token_urlsafe(24)
    datos["tokens"][_h(token)] = {"usado": False, "etiqueta": etiqueta}
    _guardar(curso, datos)
    return token


def canjear(curso, token: str) -> str | None:
    """Canjea el token: devuelve device_id nuevo, o None si inválido/usado."""
    datos = _cargar(curso)
    reg = datos["tokens"].get(_h(token or ""))
    if not reg or reg.get("usado"):
        return None
    reg["usado"] = True
    dispositivo = uuid.uuid4().hex[:16]
    datos["dispositivos"][dispositivo] = {"creado": _hoy(), "etiqueta": reg.get("etiqueta", "")}
    _guardar(curso, datos)
    return dispositivo


def _hoy() -> str:
    import datetime

    return datetime.date.today().isoformat()


def autorizado(curso, device_id: str | None) -> bool:
    """False solo si la seguridad está activada y el dispositivo no está
    registrado (o fue revocado)."""
    if not activada(curso):
        return True
    if not device_id:
        return False
    return device_id in _cargar(curso).get("dispositivos", {})


def revocar(curso, device_id: str) -> bool:
    datos = _cargar(curso)
    if device_id in datos.get("dispositivos", {}):
        del datos["dispositivos"][device_id]
        _guardar(curso, datos)
        return True
    return False


def dispositivos(curso) -> list[dict]:
    return [{"id": k, **v} for k, v in _cargar(curso).get("dispositivos", {}).items()]


def verificar_o_error(curso, headers) -> str | None:
    """None si pasa; device_id faltante/inválido si la seguridad lo exige.

    El header es ``X-Device-Id`` (lo pone chat.html tras el canje).
    """
    if not activada(curso):
        return None
    device = headers.get("X-Device-Id") or headers.get("x-device-id")
    if autorizado(curso, device):
        return None
    return device or "faltante"


if __name__ == "__main__":  # pragma: no cover - CLI
    import sys

    from .modelo import cargar

    if "--emitir" in sys.argv:
        slug = sys.argv[sys.argv.index("--emitir") + 1]
        curso = cargar(slug)
        print("TOKEN (mostrar una sola vez):", emitir(curso))
        print("dispositivos vinculados:", len(dispositivos(curso)))
    elif "--revocar" in sys.argv:
        slug = sys.argv[sys.argv.index("--revocar") + 1]
        dispositivo = sys.argv[sys.argv.index("--revocar") + 2]
        print("revocado:", revocar(cargar(slug), dispositivo))
    elif "--listar" in sys.argv:
        slug = sys.argv[sys.argv.index("--listar") + 1]
        for d in dispositivos(cargar(slug)):
            print(f"  {d['id']}  ({d.get('etiqueta', '')})  {d.get('creado', '')}")
    else:
        print("uso: python -m datito.acceso --emitir|--listar <slug> | --revocar <slug> <id>")
