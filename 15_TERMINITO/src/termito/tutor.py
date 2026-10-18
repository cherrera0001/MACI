"""Orquestador del tutor: generacion anclada a fragmentos + evidencia + lucha.

Flujo (research R5): 1) recuperar fragmentos, 2) generar SOLO desde ellos con
citas [fid], 3) validar citas post-generacion (SC-002), 4) si falla: extracto
citable con aviso. Sin LLM: modo exploracion transparente.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from . import dudas, evidencia, llm
from .indice import Indice


@dataclass
class Respuesta:
    texto: str
    citas: list[str] = field(default_factory=list)
    modo: str = "tutor"            # tutor | exploracion | sin_fuente
    aviso: str = ""


def prompt_sistema(curso) -> str:
    """System prompt del Termito + retroalimentacion derivada de notas reales."""
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
        lineas.append(f"\nInstala Ollama para que el Termito genere explicaciones: {e}")
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


def registrar_duda_si_confusion(curso, pregunta: str, resp: Respuesta) -> dict | None:
    if resp.modo in ("sin_fuente",) or not resp.citas:
        return None
    texto = resp.texto.split("\n\nInstala Ollama")[0].strip()  # sin avisos de instalacion
    resolucion = "El tutor explico con la fuente citada y el estudiante confirmo."
    return dudas.registrar(curso, pregunta, texto[:400], resolucion, resp.citas)
