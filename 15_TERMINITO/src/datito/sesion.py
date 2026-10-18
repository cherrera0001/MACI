"""Sesion de conversacion con lucha productiva (FR-008, SC-003, contrato API).

Clasifica cada mensaje del estudiante y gobierna la maquina de estados
(lucha.py): en ejercicios de practica, cero soluciones antes del intento;
los pasos se revelan de a uno (patron "Show a step" de Khan, validacion REA);
toda revelacion queda registrada en sesion.yaml (auditable, principio III).

Estados (contracts/api.md): pista -> esperando_intento -> paso_mostrado -> revision.
En modo exploracion (sin LLM) los pasos son fragmentos del material, uno por
llamada; en modo tutor el paso se redacta con el LLM solo desde el fragmento.

Mapeo documentado de estado_interaccion para interacciones sin ejercicio:
- conceptual respondida -> "revision" (el intercambio quedo resuelto);
- sin fuente -> "pista" (la unica accion posible es orientar o esperar).
"""
from __future__ import annotations

import datetime

import yaml

from . import llm, tutor
from .indice import Indice
from .lucha import LuchaProductiva
from .modelo import ErrorCurso

K_PASOS = 4  # pasos/fragmentos que la sesion ofrece por ejercicio

MARCAS_PASO = ("pista", "paso", "hint", "por donde empiezo", "por dónde empiezo",
               "no se por donde empezar", "no sé por dónde empezar")
MARCAS_SOLUCION = ("dame la respuesta", "dame la solucion", "dime la respuesta",
                   "dime la solucion", "cual es la respuesta",
                   "cual es la solucion", "muestrame la solucion",
                   "muestrame la respuesta", "me rindo", "ya me rindo")
MARCAS_EJERCICIO = ("ejercicio", "problema", "resuelve", "resuelvo", "calcula",
                    "no me sale", "no se hacer", "no sé hacer", "como hago",
                    "cómo hago", "como resuelvo", "cómo resuelvo", "me trabe",
                    "me trabé")
MARCAS_CONFUSION = ("no entiendo", "no me queda claro", "no me queda", "confundido",
                    "confundida", "no comprendo", "no lo entiendo", "me confunde")
MARCAS_FUERA = ("fuera del curso", "aunque no sea del curso",
                "no importa que no sea del curso", "off topic", "off-topic",
                "fuera del temario")
# una afirmación en primera persona del estudiante (intento/comprobación)
# NO es un ejercicio nuevo; se exige marcador posesivo para no confundir con
# preguntas como "¿cuál está bien?" (que llevan "ejercicio" en el enunciado)
MARCAS_INTENTO = ("mi respuesta", "mi intento", "mi solucion", "mi solución",
                  "yo creo", "creo que", "asi quedo", "así quedó",
                  "mi resultado", "mi analisis", "mi análisis")


def _norm(s: str) -> str:
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")


def clasificar(texto: str) -> str:
    n = _norm(texto).strip()
    if "pista" in n or any(n == m or n.startswith(m + " ") for m in MARCAS_PASO):
        return "pedir_paso"
    if any(m in n for m in MARCAS_SOLUCION):
        return "pedir_solucion"
    if any(m in n for m in MARCAS_FUERA):
        return "fuera_del_curso"
    if any(m in n for m in MARCAS_INTENTO):
        return "conceptual"
    if any(m in n for m in MARCAS_EJERCICIO):
        return "ejercicio"
    if any(m in n for m in MARCAS_CONFUSION):
        return "confusion"
    return "conceptual"


def _ruta(curso):
    return curso.ruta("sesion.yaml")


def cargar(curso) -> dict | None:
    p = _ruta(curso)
    if not p.exists():
        return None
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def guardar(curso, ses: dict):
    _ruta(curso).write_text(
        yaml.safe_dump(ses, allow_unicode=True, sort_keys=False), encoding="utf-8")


def _hoy() -> str:
    return datetime.date.today().isoformat()


def _salida(texto, citas=None, modo="exploracion", aviso="",
            estado="revision", duda=None, paso=None,
            fuera=False) -> dict:
    return {"texto": texto, "citas": citas or [], "modo": modo, "aviso": aviso,
            "estado_interaccion": estado, "duda": duda, "paso": paso,
            "fuera_del_curso": fuera}


def _top(curso, ses, indice: Indice) -> list[tuple[str, float]]:
    """Pasos de la sesion: fija desde la creacion (estable entre llamadas)."""
    fids = ses.get("contexto") or []
    top = [(f, 1.0) for f in fids if f in indice.textos]
    if not top:
        top = indice.buscar(ses.get("ejercicio", ""), k=K_PASOS)
    return top


def _paso(curso, ses, indice: Indice) -> tuple[str, str] | None:
    """Paso siguiente: (texto, fid). None si se agotaron."""
    top = _top(curso, ses, indice)
    n = ses.get("pasos_revelados", 0)
    if n >= len(top):
        return None
    fid = top[n][0]
    fragmento = indice.textos[fid]
    fuente, ref = indice.referencias[fid]
    if llm.disponible():
        try:
            system = tutor.prompt_sistema(curso)
            prompt = f"""{system}

MATERIAL (unica fuente permitida):
[{fid}] ({fuente})
{fragmento}

REGLAS: Redacta el paso {n + 1} del procedimiento para resolver el ejercicio,
usando solo el material. NO des la solucion final ni el resultado numerico.
Cita el fragmento como [{fid}]."""
            crudo = llm.generar(prompt)
            if crudo.strip():
                return f"Pasó {n + 1}: {crudo.strip()}", fid
        except llm.ModoExploracion:
            pass
    return (f"Paso {n + 1} (material de apoyo, no es la solucion):\n"
            f"«{fragmento[:600]}…»\n  → [{fid}] {fuente} · {ref}", fid)


def _orientar(curso, ses, indice: Indice) -> str:
    """Orientacion socratica inicial, sin tocar la solucion."""
    if llm.disponible():
        try:
            top = _top(curso, ses, indice)[:2]
            system = tutor.prompt_sistema(curso)
            bloques = "\n\n".join(
                f"[{fid}] ({indice.referencias[fid][0]})\n{indice.textos[fid]}"
                for fid, _ in top)
            prompt = f"""{system}

MATERIAL DE REFERENCIA (unica fuente permitida):
{bloques}

El estudiante trae este ejercicio: {ses['ejercicio']}

REGLAS: Orientalo sin resolver: que datos tiene, que se pide, que concepto del
material aplica, y como empezar. PROHIBIDO dar el resultado o la solucion
completa. No necesitas citar; esto es orientacion, no respuesta."""
            crudo = llm.generar(prompt)
            if crudo.strip():
                return crudo.strip()
        except llm.ModoExploracion:
            pass
    return ("Este es un ejercicio de practica: primero tu intento, aunque salga mal. "
            "Cuando lo tengas, escribelo y lo revisamos juntos con el material. "
            "Si te trabas escribe «pista» y te muestro un paso del procedimiento "
            "(nunca la solucion completa).")


def _resolver(curso, ses, indice: Indice) -> tuple[str, list[str]]:
    """Material de resolucion revelado con consentimiento (queda registrado)."""
    top = _top(curso, ses, indice)
    citas = [fid for fid, _ in top]
    if llm.disponible():
        try:
            system = tutor.prompt_sistema(curso)
            bloques = "\n\n".join(
                f"[{fid}] ({indice.referencias[fid][0]})\n{indice.textos[fid]}"
                for fid, _ in top)
            prompt = f"""{system}

MATERIAL (unica fuente permitida):
{bloques}

Resuelve paso a paso el ejercicio: {ses['ejercicio']}
Cita cada afirmacion con su [fid]."""
            from . import evidencia
            crudo = llm.generar(prompt)
            val = evidencia.validar(crudo, indice)
            if val.ok:
                return evidencia.limpiar_citas(crudo), val.citas
        except llm.ModoExploracion:
            pass
    lineas = ["Material de resolucion (revelado con tu consentimiento):"]
    for fid in citas:
        fuente, ref = indice.referencias[fid]
        lineas.append(f"\n«{indice.textos[fid][:500]}…»\n  → [{fid}] {fuente} · {ref}")
    return "\n".join(lineas), citas


def conversar(curso, texto: str, indice: Indice) -> dict:
    """Punto de entrada del chat: clasifica, gobierna la maquina, responde."""
    tipo = clasificar(texto)
    ses = cargar(curso)

    if tipo == "fuera_del_curso":
        if llm.disponible():
            crudo = llm.generar(
                "Respondes FUERA del temario del curso, como conocimiento general. "
                "Sin citas (no hay material). Se breve.\n\nPregunta: " + texto)
            return _salida(crudo.strip() or "(sin respuesta)", modo="tutor",
                           aviso="Respuesta fuera del curso: sin evidencia posible "
                                 "(principio II no aplica a lo que el estudiante "
                                 "explicitamente pidio fuera del temario).",
                           fuera=True)
        return _salida("El modo exploracion solo recupera material del curso; no "
                       "puedo responder fuera del temario sin modelo local.",
                       aviso="Sin LLM local no hay respuesta fuera del curso.",
                       fuera=True)

    if tipo == "pedir_paso":
        if not ses:
            return _salida("No hay un ejercicio activo. Mandame primero el "
                           "enunciado del ejercicio.")
        paso = _paso(curso, ses, indice)
        if paso is None:
            ses["estado"] = "esperando_intento"
            guardar(curso, ses)
            return _salida("Ya te mostre todos los pasos que tengo para este "
                           "ejercicio. Ahora es tu turno: escribe tu intento "
                           "(aunque este incompleto) y lo revisamos juntos.",
                           estado="esperando_intento")
        texto_paso, fid = paso
        ses["pasos_revelados"] = ses.get("pasos_revelados", 0) + 1
        ses["estado"] = "paso_mostrado"
        ses.setdefault("revelaciones", []).append(
            {"tipo": "paso", "n": ses["pasos_revelados"], "fecha": _hoy()})
        guardar(curso, ses)
        return _salida(texto_paso, citas=[fid], estado="paso_mostrado",
                       paso={"numero": ses["pasos_revelados"],
                             "total": len(_top(curso, ses, indice))})

    if tipo == "pedir_solucion":
        if not ses:
            return _salida("No hay un ejercicio activo. Mandame primero el "
                           "enunciado; la solucion completa solo se revela con "
                           "tu consentimiento informado y queda registrada.")
        if ses.get("intentos", 0) == 0:
            ses["estado"] = "esperando_intento"
            guardar(curso, ses)
            return _salida("Todavia no has intentado resolverlo, y la solucion "
                           "completa antes del intento no es opcion (principio "
                           "III). Dos caminos: escribe tu intento y lo revisamos, "
                           "o pide «pista» y vamos paso a paso. Si despues de los "
                           "pasos sigues sin poder, la revelacion consentida "
                           "queda registrada para tu registro de estudio.",
                           estado="esperando_intento")
        solucion, citas = _resolver(curso, ses, indice)
        ses.setdefault("revelaciones", []).append(
            {"tipo": "solucion", "consentido": True, "via": "chat",
             "fecha": _hoy(), "intentos": ses.get("intentos", 0)})
        guardar(curso, ses)
        return _salida(solucion, citas=citas, estado="revision")

    if tipo == "ejercicio":
        if ses and _norm(ses.get("ejercicio", "")) == _norm(texto):
            return _salida("Seguimos con el mismo ejercicio. Tu turno: escribe "
                           "tu intento (aunque incompleto) o pide «pista».",
                           estado=ses["estado"])
        top = indice.buscar(texto, k=K_PASOS)
        ses = {"ejercicio": texto.strip(), "estado": "pista",
               "pasos_revelados": 0, "intentos": 0,
               "revelaciones": [], "desde": _hoy(),
               "contexto": [fid for fid, _ in top]}
        guardar(curso, ses)
        if not top:
            return _salida("Guardé el ejercicio, pero no encontré material del "
                           "curso que se le parezca. Revisa que sea de este "
                           "curso: solo trabajo con tus materiales (principio "
                           "VI). Si es del temario, trae el enunciado con más "
                           "contexto.", estado="pista")
        return _salida(_orientar(curso, ses, indice), estado="pista",
                       aviso="" if llm.disponible() else
                       "En modo exploracion no genero orientacion; con Ollama "
                       "activo el Datito guia socraticamente.")

    # conceptual / confusion: con sesion abierta cuenta como intento
    if ses and ses.get("estado") in ("pista", "esperando_intento", "paso_mostrado"):
        m = LuchaProductiva(estado=ses["estado"])
        m.pasos_revelados = ses.get("pasos_revelados", 0)
        m.intentos = ses.get("intentos", 0)
        m.registrar_intento()
        ses["intentos"] = m.intentos
        ses["estado"] = m.estado
        guardar(curso, ses)
        resp = tutor.responder(curso, texto, indice)
        duda = None
        if tipo == "confusion":
            duda = tutor.registrar_duda_si_confusion(curso, texto, resp)
        return _salida(resp.texto, citas=resp.citas, modo=resp.modo,
                       aviso=resp.aviso, estado="revision", duda=duda)

    resp = tutor.responder(curso, texto, indice)
    duda = None
    if tipo == "confusion":
        duda = tutor.registrar_duda_si_confusion(curso, texto, resp)
    return _salida(resp.texto, citas=resp.citas, modo=resp.modo, aviso=resp.aviso,
                   estado="pista" if resp.modo == "sin_fuente" else "revision",
                   duda=duda)


def revelar(curso, consentimiento: bool, indice: Indice) -> dict:
    """Revelacion consentida y registrada de la solucion (contrato API)."""
    ses = cargar(curso)
    if not ses:
        raise ErrorCurso("sin_sesion: no hay ejercicio activo")
    if not consentimiento:
        raise ValueError("consentimiento_requerido")
    puede = ses.get("intentos", 0) > 0 or \
        ses.get("pasos_revelados", 0) >= len(_top(curso, ses, indice))
    if not puede:
        raise PermissionError(
            "La solucion completa se revela tras un intento o tras agotar los "
            "pasos; queda registrada. Estado actual: "
            f"{ses.get('estado', 'pista')}.")
    solucion, citas = _resolver(curso, ses, indice)
    ses.setdefault("revelaciones", []).append(
        {"tipo": "solucion", "consentido": True, "via": "api",
         "fecha": _hoy(), "intentos": ses.get("intentos", 0)})
    guardar(curso, ses)
    return {"solucion": solucion, "citas": citas,
            "registro": ses["revelaciones"][-1],
            "estado_interaccion": ses.get("estado", "pista")}
