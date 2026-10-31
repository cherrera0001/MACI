"""Orquestador del tutor: generacion anclada a fragmentos + evidencia + lucha.

Flujo (research R5): 1) recuperar fragmentos, 2) generar SOLO desde ellos con
citas [fid], 3) validar citas post-generacion (SC-002), 4) si falla: extracto
citable con aviso. Sin LLM: modo exploracion transparente.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from . import dudas, evidencia, identidad, llm
from .indice import Indice

MODO_COMPANIA = "compania"
_TEXTO_NO_RECUERDA = (
    "Prefiero no afirmar algo que no recuerdo con certeza. Cuéntemelo de "
    "nuevo y lo guardo con cuidado para la próxima vez.")
_TEXTO_COMPANIA_EXPLORACION = (
    "Gracias por contármelo. Estoy aquí para acompañarla y escucharla "
    "cuando quiera. ¿Qué más le gustaría contarme hoy?")


@dataclass
class Respuesta:
    texto: str
    citas: list[str] = field(default_factory=list)
    modo: str = "tutor"            # tutor | exploracion | sin_fuente
    aviso: str = ""


def prompt_sistema(curso) -> str:
    """System prompt del Datito + retroalimentacion derivada de notas reales."""
    try:
        system = curso.ruta("prompt", "actual.md").read_text(encoding="utf-8")
    except FileNotFoundError:
        system = "Eres un tutor. Cita siempre tus fuentes."
    retro = curso.datos.get("retroalimentacion")
    if retro:
        system += ("\n\nRETROALIMENTACION DEL ESTUDIANTE (notas reales): "
                   + " | ".join(str(r) for r in retro[-3:]))
    return system


def _prompt(system_prompt: str, pregunta: str, contexto: list[tuple[str, str, str]]) -> str:
    bloques = []
    for fid, fuente, texto in contexto:
        bloques.append(f"[{fid}] ({fuente})\n{texto}")
    return f"""{system_prompt}

MATERIAL DEL CURSO (unica fuente permitida):
{chr(10).join(bloques)}

REGLAS DE RESPUESTA:
- Responde en el mismo idioma en que escribe el estudiante (FR-022).
- Cita la fuente de CADA afirmacion sobre el curso con su id entre corchetes,
  ej: [transcripcion-08#3]. Solo puedes citar ids del material de arriba.
- Si el material no cubre la pregunta, di "No tengo fuente en los materiales
  para responder eso" y nada mas.
- Si pide la solucion de un ejercicio sin haber intentado, ofrece una pista
  (un paso del procedimiento), no la solucion.

PREGUNTA DEL ESTUDIANTE:
{pregunta}

RESPUESTA (con citas [fid]):"""


def responder(curso, pregunta: str, indice: Indice, k: int = 4) -> Respuesta:
    if identidad.es_compania(curso):
        return _responder_compania(curso, pregunta, indice, k)
    top = indice.buscar(pregunta, k=k)
    if not top:
        return Respuesta("No tengo fuente en los materiales para responder eso.",
                         modo="sin_fuente",
                         aviso="La busqueda no recupero fragmentos relevantes.")
    contexto = [(fid, indice.referencias[fid][0], indice.textos[fid]) for fid, _ in top]

    system = prompt_sistema(curso)
    prompt = _prompt(system, pregunta, contexto)

    try:
        crudo = llm.generar(prompt)
    except llm.ModoExploracion as e:
        lineas = ["[modo exploracion — sin LLM local] Fragmentos mas relevantes:"]
        citas = []
        for fid, _ in top[:3]:
            citas.append(fid)
            fuente, ref = indice.referencias[fid]
            lineas.append(f"\n«{indice.textos[fid][:500]}…»\n  → [{fid}] {fuente} · {ref}")
        lineas.append(f"\nInstala Ollama para que el Datito genere explicaciones: {e}")
        return Respuesta("\n".join(lineas), citas=citas, modo="exploracion",
                         aviso="Esto es recuperacion, no una explicacion generada (R5).")

    val = evidencia.validar(crudo, indice)
    if val.ok:
        limpio = evidencia.limpiar_citas(crudo)
        return Respuesta(limpio, citas=val.citas, modo="tutor")
    if val.sin_fuente:
        return Respuesta(
            "No tengo fuente en los materiales para responder eso.", modo="sin_fuente",
            aviso="El modelo no produjo citas; se aplica la regla de silencio.")
    # citas invalidas o sin soporte: un reintento con contexto mas chico
    crudo2 = llm.generar(_prompt(system, pregunta, contexto[:2]))
    val2 = evidencia.validar(crudo2, indice)
    if val2.ok:
        return Respuesta(evidencia.limpiar_citas(crudo2), citas=val2.citas, modo="tutor")
    fid = top[0][0]
    return Respuesta(
        f"No logre sostener la respuesta con evidencia valida. Extracto mas cercano:\n"
        f"«{indice.textos[fid][:500]}…»",
        citas=[fid], modo="sin_fuente",
        aviso=f"Citas rechazadas: invalidas={val.invalidas} sin_soporte={val.sin_soporte}")


# ---------------------------------------------------------------------------
# Modo compania (E-10): asimetria de actos de habla (D-10.2).
# Escuchar y acompanar no exige citas; afirmar sobre la vida del usuario sí,
# y la afirmación valida con el mismo gate de evidencia. La asociatividad
# cambia la recuperación, nunca la verdad.
# ---------------------------------------------------------------------------

def _prompt_compania(system_prompt: str, mensaje: str,
                     contexto: list[tuple[str, str, str]]) -> str:
    bloques = []
    for fid, fuente, texto in contexto:
        bloques.append(f"[{fid}] ({fuente})\n{texto}")
    return f"""{system_prompt}

MEMORIA DE NUESTRA CONVERSACION (unica fuente permitida sobre su vida):
{chr(10).join(bloques)}

La persona escribe: {mensaje!r}

REGLAS:
- Escucha con empatia; responde en el mismo idioma, con frases cortas y
  calidas, a lo mas tres lineas.
- Si afirmas algo sobre su vida o su pasado, DEBES citarlo como [fid] desde
  la memoria de arriba. PROHIBIDO inventar recuerdos.
- Si nada de la memoria aplica, responde sin citas: solo presencia, validacion
  y una pregunta abierta que invite a seguir conversando."""

def _generar_seguro(prompt: str) -> str:
    try:
        return llm.generar(prompt)
    except llm.ModoExploracion:
        return ""


def _responder_compania(curso, mensaje: str, indice: Indice, k: int = 4) -> Respuesta:
    top = indice.buscar(mensaje, k=k)
    system = prompt_sistema(curso)

    if not top:
        # escucha activa sin evocación: no afirma nada verificable
        crudo = _generar_seguro(
            f"{system}\n\nLa persona escribe: {mensaje!r}\n\n"
            "REGLAS: escucha activa y empatia, sin afirmar hechos sobre su vida "
            "(no hay memoria recuperada). No inventes recuerdos. Frases cortas y "
            "calidas; termina con una pregunta abierta y afectuosa.")
        if crudo.strip():
            return Respuesta(crudo.strip(), modo=MODO_COMPANIA,
                             aviso="Escucha activa: sin afirmaciones verificables (D-10.2).")
        return Respuesta(_TEXTO_COMPANIA_EXPLORACION, modo=MODO_COMPANIA,
                         aviso="Modo exploracion: respuesta de compania determinista (sin LLM).")

    contexto = [(fid, indice.referencias[fid][0], indice.textos[fid])
                for fid, _ in top]
    crudo = _generar_seguro(_prompt_compania(system, mensaje, contexto))
    if crudo.strip():
        val = evidencia.validar(crudo, indice)
        if val.ok:
            return Respuesta(evidencia.limpiar_citas(crudo), citas=val.citas,
                             modo=MODO_COMPANIA)
        if val.sin_fuente:
            return Respuesta(crudo.strip(), modo=MODO_COMPANIA,
                             aviso="Escucha activa: sin evocacion de recuerdos (sin citas).")
        # cita invalida o sin soporte: un reintento con contexto menor;
        # una cita invalida jamas llega a la persona
        crudo2 = _generar_seguro(_prompt_compania(system, mensaje, contexto[:2]))
        val2 = evidencia.validar(crudo2, indice) if crudo2.strip() \
            else evidencia.ResultadoEvidencia(False, "", sin_fuente=True)
        if crudo2.strip() and val2.ok:
            return Respuesta(evidencia.limpiar_citas(crudo2), citas=val2.citas,
                             modo=MODO_COMPANIA)
        return Respuesta(_TEXTO_NO_RECUERDA, modo=MODO_COMPANIA,
                         aviso="Cita sin soporte: se rehúsa a afirmar (anti-alucinacion).")

    # sin LLM pero hay memoria relevante: ofrecerla citada (modo exploracion)
    fid = top[0][0]
    _, ref = indice.referencias[fid]
    return Respuesta(
        f"Recuerdo que en nuestra conversación quedó: "
        f"«{indice.textos[fid][:300]}…» [{fid}] {ref} "
        f"— cuénteme más, ¿cómo sigue eso hoy?",
        citas=[fid], modo=MODO_COMPANIA,
        aviso="Modo exploracion: memoria citada sin generacion.")


def registrar_duda_si_confusion(curso, pregunta: str, resp: Respuesta) -> dict | None:
    if resp.modo in ("sin_fuente",) or not resp.citas:
        return None
    texto = resp.texto.split("\n\nInstala Ollama")[0].strip()  # sin avisos de instalacion
    resolucion = "El tutor explico con la fuente citada y el estudiante confirmo."
    return dudas.registrar(curso, pregunta, texto[:400], resolucion, resp.citas)
