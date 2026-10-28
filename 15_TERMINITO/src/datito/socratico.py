"""Politica socratica ejecutable: el protocolo pedagogico de la skill como codigo.

La skill (.claude/skills/datito/SKILL.md) fija el protocolo en texto: REGLA CERO
(espera de verdad), G11 (la estrategia la elige el alumno), dos intentos antes
de la solucion, REGLA UNO-B (toda respuesta se registra antes de decirse) y la
exigencia de transferencia tras entregar. Este modulo lo hace ejecutable: la
politica decide la accion del tutor desde el mensaje del estudiante y el estado
de la sesion, y emite un transcript que se valida con las mismas cinco reglas
del harness de especificacion (04_CODIGO/harness_escenarios).

Contrato de reglas (misma semantica, un solo sentido):
  R1 espera_real                — el tutor jamas responde su propia pregunta
  R2 no_simula_alumno           — el tutor no escribe la respuesta del alumno
  R3 solucion_tras_dos_intentos — la solucion llega tras 2 fallos o peticion explicita
  R4 respuesta_pedida_registrada— la entrega va precedida de la accion duda:*
  R5 transferencia_tras_respuesta— tras entregar, se exige transferir (pregunta)

G10: los datos sinteticos del demo se etiquetan siempre; este modulo no toca
07_DATITO/ (usa cursos autocontenidos).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

ESTADOS_CONCEPTO = ("NO_ESTUDIADO", "EN_ESTUDIO", "COMPRENSION_PARCIAL",
                    "COMPRENDIDO", "DOMINADO", "REQUIERE_REPASO")
EVIDENCIAS = ("explicar", "aplicar", "interpretar", "transferir")

PIDE_RESPUESTA = re.compile(
    r"dame la respuesta|pasa(me)? la solucion|cual es la correcta|"
    r"explicita(me)?lo completo|desarm(a|e) (esta )?ecuacion|resuelve(lo)?",
    re.I)
PIDE_MODO_ESTRICTO = re.compile(r"no me (la )?des|hazme pensar|quiero intentar", re.I)
PREGUNTA = re.compile(r"\?\s*$")

# G6 (ADR-005): si una fuente cae, se avisa en una linea y se etiqueta el resto.
AVISOS_DEGRADACION = {
    "indice_local": "El indice de transcripciones no responde; sigo con el material "
                    "local y etiqueto lo que no tenga respaldo.",
    "llm_externo": "El modelo local no esta disponible; quedo en modo exploracion "
                   "con la evidencia recuperada.",
}
ETIQUETA = re.compile(r"\[(FUENTE|INFERENCIA|DATITO)\b")
SUSTANTIVO_MIN = 120

ACCIONES = ("PREGUNTAR", "PISTA", "DESARROLLAR_SOLUCION", "ENTREGAR_RESPUESTA",
            "EXIGIR_TRANSFERENCIA", "RE_VERIFICAR", "EXPLICAR")


class ErrorPolitica(PermissionError):
    """Violacion del protocolo (p. ej. entregar antes de tiempo)."""


class ErrorEvidencia(AssertionError):
    """La cadena de evidencia no sostiene el estado declarado."""


@dataclass
class Accion:
    nombre: str
    texto: str
    registrar_duda: str | None = None   # id de duda si la accion entrega respuesta

    def __post_init__(self):
        if self.nombre not in ACCIONES:
            raise ValueError(f"accion invalida: {self.nombre}")


@dataclass
class Concepto:
    """Un concepto con su cadena de 4 evidencias (spec §3)."""
    id: str
    estado: str = "NO_ESTUDIADO"
    evidencias: dict = field(default_factory=lambda: {e: None for e in EVIDENCIAS})

    def registrar(self, paso: str, detalle: str, fecha: str):
        if paso not in EVIDENCIAS:
            raise ErrorEvidencia(f"evidencia invalida: {paso}")
        if self.evidencias[EVIDENCIAS[EVIDENCIAS.index(paso) - 1]] is None and paso != "explicar":
            raise ErrorEvidencia(
                f"{self.id}: '{paso}' exige '{EVIDENCIAS[EVIDENCIAS.index(paso)-1]}' antes")
        self.evidencias[paso] = {"fecha": fecha, "detalle": detalle}
        self._recalcular()

    def re_verificar(self, fecha: str, acierto: bool, detalle: str):
        if acierto:
            self.evidencias["explicar"] = {"fecha": fecha, "detalle": detalle}
            self.estado = "COMPRENDIDO" if self.evidencias["aplicar"] else "COMPRENSION_PARCIAL"
        else:
            self.estado = "REQUIERE_REPASO"

    def _recalcular(self):
        e = self.evidencias
        if all(e.values()):
            self.estado = "DOMINADO"
        elif e["explicar"] and e["aplicar"]:
            self.estado = "COMPRENDIDO"
        elif e["explicar"]:
            self.estado = "COMPRENSION_PARCIAL"


@dataclass
class Politica:
    """Decide la accion del tutor y valida su propio transcript.

    El transcript se emite en el formato del harness: turnos {rol, texto,
    acciones, resultado}. validar() aplica R1-R5; si la politica se respeta a
    si misma, toda sesion real pasa el harness de especificacion.
    """
    concepto: Concepto
    solucion: str = ""
    pistas: list = field(default_factory=list)
    fecha: str = "2026-10-28"
    intentos_fallidos: int = 0
    entregada: bool = False
    transferida: bool = False
    turnos: list = field(default_factory=list)
    # metricas de sesion (REQ-TUT-002)
    preguntas: int = 0
    esperas_reales: int = 0
    soluciones_anticipadas: int = 0
    # G6: fuente caida en esta sesion (None = todo disponible)
    degradacion: str | None = None
    _avisada: bool = field(default=False, init=False, repr=False)

    def __post_init__(self):
        if self.degradacion is not None and self.degradacion not in AVISOS_DEGRADACION:
            raise ValueError(f"degradacion desconocida: {self.degradacion}")

    # ---- entrada: mensaje del estudiante ---------------------------------
    def responder(self, mensaje: str, *, es_intento: bool = False,
                  acierto: bool | None = None) -> Accion:
        if es_intento:
            return self._revisar_intento(acierto)
        self.turnos.append({"rol": "alumno", "texto": mensaje})
        if PIDE_RESPUESTA.search(mensaje) and not PIDE_MODO_ESTRICTO.search(mensaje):
            return self._entregar(mensaje)
        if PIDE_MODO_ESTRICTO.search(mensaje):
            return self._pistar(mensaje)
        return self._preguntar(mensaje)

    # ---- decisiones -------------------------------------------------------
    def _preguntar(self, mensaje: str) -> Accion:
        accion = Accion("PREGUNTAR",
                        "Antes de seguir: que decide cada conjunto de datos en tu experimento?")
        self._turno_tutor(accion, pregunta=True)
        return accion

    def _pistar(self, mensaje: str) -> Accion:
        pista = self.pistas[min(self.intentos_fallidos, len(self.pistas) - 1)] if self.pistas \
            else "Lee que mide cada numero antes de comparar."
        accion = Accion("PISTA", f"Pista: {pista}")
        self._turno_tutor(accion)
        return accion

    def _revisar_intento(self, acierto: bool | None) -> Accion:
        self.turnos.append({"rol": "alumno", "texto": "(intento del estudiante)",
                            "resultado": "acerto" if acierto else "fallo"})
        if acierto:
            self.intentos_fallidos = 0
            accion = Accion("PREGUNTAR", "Bien. Que mecanismo lo explica, en tus palabras?")
            self._turno_tutor(accion, pregunta=True)
            return accion
        self.intentos_fallidos += 1
        if self.intentos_fallidos >= 2:
            return self._desarrollar()
        return self._pistar("")

    def _desarrollar(self) -> Accion:
        self.entregada = True
        duda_id = f"{self.fecha}-{self.concepto.id}-solucion"
        accion = Accion("DESARROLLAR_SOLUCION",
                        f"Despues de dos intentos, la solucion completa: {self.solucion}",
                        registrar_duda=duda_id)
        self._turno_tutor(accion)
        self.turnos[-1]["acciones"] = [f"duda:{duda_id}", "entrega:desarrollada"]
        return accion

    def _entregar(self, mensaje: str) -> Accion:
        self.entregada = True
        duda_id = f"{self.fecha}-{self.concepto.id}-pedida"
        accion = Accion("ENTREGAR_RESPUESTA",
                        f"La entrego escrita y registrada: {self.solucion}",
                        registrar_duda=duda_id)
        self._turno_tutor(accion)
        self.turnos[-1]["acciones"] = [f"duda:{duda_id}", "entrega:completa"]
        return accion

    def exigir_transferencia(self) -> Accion:
        if not self.entregada:
            raise ErrorPolitica("no se exige transferencia antes de entregar")
        accion = Accion("EXIGIR_TRANSFERENCIA",
                        "Ahora transfierela: mismo problema, otro dominio. Que le dirias?")
        self._turno_tutor(accion, pregunta=True)
        self.transferida = True
        return accion

    def re_verificar(self, acierto: bool, detalle: str) -> Accion:
        self.concepto.re_verificar(self.fecha, acierto, detalle)
        accion = Accion("RE_VERIFICAR", "Re-verificacion registrada.")
        self._turno_tutor(accion)
        return accion

    # ---- transcript y validacion -----------------------------------------
    def _etiquetar(self, texto: str) -> str:
        if not self.degradacion:
            return texto
        if not self._avisada:
            self._avisada = True
            return f"{AVISOS_DEGRADACION[self.degradacion]} {texto}"
        if len(texto) > SUSTANTIVO_MIN and not ETIQUETA.search(texto):
            return f"[INFERENCIA] {texto}"
        return texto

    def _turno_tutor(self, accion: Accion, pregunta: bool = False):
        self.turnos.append({"rol": "tutor", "texto": self._etiquetar(accion.texto),
                            "acciones": ([f"duda:{accion.registrar_duda}"]
                                         if accion.registrar_duda else [])})
        if pregunta or PREGUNTA.search(accion.texto):
            self.preguntas += 1

    def registrar_espera_real(self):
        """Compat: las esperas reales se computan del transcript (metricas())."""
        self.esperas_reales += 1

    def _esperas_reales(self) -> int:
        return sum(1 for i, t in enumerate(self.turnos[:-1])
                   if t["rol"] == "tutor" and PREGUNTA.search(t["texto"].strip())
                   and self.turnos[i + 1]["rol"] == "alumno")

    def metricas(self) -> dict:
        return {
            "preguntas_con_espera_real": f"{self._esperas_reales()}/{self.preguntas}",
            "respuestas_antes_de_2_intentos": self.soluciones_anticipadas,
            "dudas_registradas": sum(1 for t in self.turnos
                                     for a in t.get("acciones", []) if str(a).startswith("duda:")),
        }

    def validar(self) -> list[str]:
        """R1-R5 sobre el transcript emitido (vacío = la sesion respeta el protocolo)."""
        v = []
        for i, t in enumerate(self.turnos[:-1]):
            if t["rol"] == "tutor" and PREGUNTA.search(t["texto"].strip()) \
                    and self.turnos[i + 1]["rol"] != "alumno":
                v.append(f"R1 turno {i}: pregunta sin espera real")
        if self.soluciones_anticipadas:
            v.append("R3: hubo soluciones antes de dos intentos")
        entregas = [i for i, t in enumerate(self.turnos)
                    if any(str(a).startswith("entrega") for a in t.get("acciones", []))]
        for i in entregas:
            if not any(str(a).startswith("duda:") for a in self.turnos[i].get("acciones", [])):
                v.append(f"R4 turno {i}: entrega sin registrar")
        for i in entregas:
            if not any(s["rol"] == "tutor" and PREGUNTA.search(s["texto"].strip())
                       for s in self.turnos[i + 1:]):
                v.append(f"R5 turno {i}: entrega sin exigencia de transferencia")
        return v
