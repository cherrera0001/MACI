"""Guardián de autonomía y bienestar (D-11.3): detección determinista y auditable.

Sin ML: las señales viven en listas legibles en el código, revisables por un
humano. Niveles: ok | fraude | alerta. El guardián nunca diagnostica; protege
y deja traza. La privacidad manda: la alerta guarda fecha y señales, no el
mensaje completo.
"""
from __future__ import annotations

import datetime
import unicodedata

import yaml

from . import evidencia

SENALES_FRAUDE = (
    "clave", "claves", "contrasena", "contraseña", "password", "pin",
    "transferencia", "transferir", "deposito", "depósito", "premio",
    "ganaste", "ganó", "loteria", "lotería", "cuenta bloqueada",
    "verificacion", "verificación", "codigo de seguridad", "codigo",
    "banco", "urgente", "sobrino", "sobrina", "nieto", "nieta",
)
SENALES_FRAUDE_FUERTES = (
    "clave", "claves", "contrasena", "contraseña", "pin", "transferencia",
    "transferir", "premio", "ganaste", "cuenta bloqueada",
)
SENALES_ALERTA = (
    "no puedo mas", "no puedo más", "quiero morir", "morirme",
    "dolor en el pecho", "me cai", "me caí", "no puedo levantarme",
    "no se donde estoy", "no sé donde estoy", "emergencia",
    "llamen a la ambulancia", "ambulancia", "me siento muy mal", "desmayo",
    "sangre", "accidente",
)


def _norm(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")


def evaluar(texto: str) -> dict:
    """Nivel de riesgo del mensaje y señales que lo sostienen (auditables)."""
    n = " " + _norm(texto or "") + " "
    debiles = [s for s in SENALES_FRAUDE if _norm(s) in n]
    fuertes = [s for s in SENALES_FRAUDE_FUERTES if _norm(s) in n]
    alerta = [s for s in SENALES_ALERTA if _norm(s) in n]
    if alerta:
        return {"nivel": "alerta", "senales": alerta}
    if len(debiles) >= 3 or (fuertes and len(debiles) >= 2) or len(fuertes) >= 2:
        return {"nivel": "fraude", "senales": sorted(set(debiles))}
    return {"nivel": "ok", "senales": []}


def proteccion(curso, indice, senal: dict) -> tuple[str, list[str]]:
    """Respuesta protectora anclada a una guía citada y validada.

    Devuelve (texto, citas). Si la guía no valida, cae a una protección
    genérica sin cita: la regla anti-alucinación manda también aquí.
    """
    base = ("Lo que me cuenta suena a un intento de estafa, y su seguridad "
            "va primero. ")
    top = indice.buscar("estafa clave banco premio urgente transferencia", k=6)
    guia = next((f for f, _ in top
                 if indice.referencias.get(f, ("", ""))[1].startswith("guia:")),
                None)
    if guia:
        texto = (f"{base}Recuerde lo que guardamos juntos: "
                 f"{indice.textos[guia]} [{guia}]")
        val = evidencia.validar(texto, indice)
        if val.ok:
            return texto, [guia]
    return (base + "No comparta claves ni dinero, corte la comunicación y "
            "consulte con alguien de confianza."), []


def registrar_alerta(curso, senal: dict) -> dict:
    """Traza ética: fecha y señales, nunca el mensaje completo."""
    entrada = {"fecha": datetime.date.today().isoformat(),
               "tipo": "bienestar", "senales": senal.get("senales", [])}
    p = curso.ruta("alertas.yaml")
    datos = yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() \
        else {"alertas": []}
    datos = datos or {"alertas": []}
    datos["alertas"].append(entrada)
    p.write_text(yaml.safe_dump(datos, allow_unicode=True, sort_keys=False),
                 encoding="utf-8")
    return entrada


def contar_alertas(curso) -> tuple[int, dict | None]:
    p = curso.ruta("alertas.yaml")
    if not p.exists():
        return 0, None
    datos = yaml.safe_load(p.read_text(encoding="utf-8")) or {"alertas": []}
    alertas = datos.get("alertas") or []
    return len(alertas), (alertas[-1] if alertas else None)
