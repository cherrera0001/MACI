"""Maquina de estados de lucha productiva (R4 + validacion REA: Khan 'Show a step').

Estados (contracts/api.md): pista -> esperando_intento -> paso_mostrado -> revision.
- 'mostrar un paso' revela UN paso del procedimiento, nunca la solucion completa.
- 0 soluciones completas antes del intento (SC-003).
- Cada revelacion queda registrada (auditable, antipatron A1 de la validacion REA).
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .config import ESTADOS_INTERACCION


@dataclass
class LuchaProductiva:
    pasos: list[str] = field(default_factory=list)   # procedimiento, ordenado
    estado: str = "pista"
    pasos_revelados: int = 0
    intentos: int = 0
    revelaciones: list[dict] = field(default_factory=list)
    solucion: str = ""

    def __post_init__(self):
        if self.estado not in ESTADOS_INTERACCION:
            raise ValueError(f"estado invalido: {self.estado}")

    def registrar_intento(self):
        self.intentos += 1
        self.estado = "revision"

    def mostrar_paso(self) -> str | None:
        """Revela el siguiente paso; None si se agotaron."""
        if self.pasos_revelados >= len(self.pasos):
            return None
        paso = self.pasos[self.pasos_revelados]
        self.pasos_revelados += 1
        self.estado = "paso_mostrado"
        self.revelaciones.append({"tipo": "paso", "n": self.pasos_revelados})
        return paso

    def puede_ver_solucion(self) -> bool:
        """La solucion completa solo tras intento o agotar todos los pasos + consentimiento."""
        return self.intentos > 0 or self.pasos_revelados >= len(self.pasos)

    def ver_solucion(self, consentimiento: bool = False) -> str:
        if not self.puede_ver_solucion() and not consentimiento:
            raise PermissionError(
                "La solucion completa solo se revela despues de un intento "
                "o con consentimiento informado (principio III).")
        self.revelaciones.append({"tipo": "solucion",
                                  "consentido": consentimiento})
        return self.solucion

    def proxima_accion(self) -> str:
        return {
            "pista": "ofrecer pista o esperar intento",
            "esperando_intento": "esperar el intento del estudiante",
            "paso_mostrado": "ofrecer otro paso o esperar intento",
            "revision": "revisar el intento y retroalimentar",
        }[self.estado]
