"""Esquema del estado pedagogico: seis estados y cadena de 4 evidencias (spec §3).

Modulo compartido (T032): lo usan el test de esquema de 04_CODIGO, que valida
07_DATITO/progreso.yaml, y la politica socratica del motor. Antes vivia dentro
de un archivo de test y el motor repetia las constantes.
"""
import datetime
import re

ESTADOS = {"NO_ESTUDIADO", "EN_ESTUDIO", "COMPRENSION_PARCIAL", "COMPRENDIDO",
           "DOMINADO", "REQUIERE_REPASO"}
EVIDENCIAS = ("explicar", "aplicar", "interpretar", "transferir")
ESTADOS_DUDA = {"resuelta", "practica", "abierta"}
ESTADOS_ERROR = {"abierto", "resuelto", "reincidente", "anulado"}
FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ErrorEsquema(AssertionError):
    """Un campo viola el esquema; el mensaje nombra el campo."""


def exige(cond, campo, mensaje):
    if not cond:
        raise ErrorEsquema(f"{campo}: {mensaje}")


def fecha_iso(valor, campo):
    # YAML convierte las fechas sin comillas en datetime.date; ambas formas valen
    if isinstance(valor, datetime.date):
        return
    exige(isinstance(valor, str) and FECHA.match(valor), campo,
           f"fecha '{valor}' no es ISO (AAAA-MM-DD)")


def evidencia(valor, campo):
    if valor is None:
        return
    exige(isinstance(valor, dict), campo, "la evidencia debe ser un mapa o null")
    exige(set(valor) >= {"fecha", "detalle"}, campo, "faltan claves fecha/detalle")
    fecha_iso(valor["fecha"], f"{campo}.fecha")
    exige(isinstance(valor["detalle"], str) and valor["detalle"].strip(),
           f"{campo}.detalle", "el detalle no puede estar vacio")


def validar_progreso(doc):
    meta = doc.get("meta") or {}
    for clave in ("alumno", "tutor", "asignatura"):
        exige(isinstance(meta.get(clave), str) and meta[clave].strip(),
               f"meta.{clave}", "obligatorio y no vacio")
    exige(isinstance(meta.get("sesiones_totales"), int) and meta["sesiones_totales"] >= 0,
           "meta.sesiones_totales", "entero >= 0")
    exige(isinstance(meta.get("diagnostico_inicial_hecho"), bool),
           "meta.diagnostico_inicial_hecho", "booleano")

    conceptos = doc.get("conceptos") or []
    exige(isinstance(conceptos, list) and conceptos, "conceptos", "lista no vacia")
    ids = [c.get("id") for c in conceptos]
    exige(len(ids) == len(set(ids)), "conceptos", f"ids repetidos: {ids}")

    for c in conceptos:
        cid = f"concepto {c.get('id')}"
        exige(c.get("estado") in ESTADOS, f"{cid}.estado",
               f"'{c.get('estado')}' no es un estado valido {sorted(ESTADOS)}")
        evs = c.get("evidencias") or {}
        exige(set(evs) == set(EVIDENCIAS), f"{cid}.evidencias",
               f"deben ser exactamente {list(EVIDENCIAS)}")
        for nombre in EVIDENCIAS:
            evidencia(evs.get(nombre), f"{cid}.evidencias.{nombre}")
        exige(isinstance(c.get("sesiones"), int) and c["sesiones"] >= 0,
               f"{cid}.sesiones", "entero >= 0")
        if c.get("ultima_verificacion") is not None:
            fecha_iso(c["ultima_verificacion"], f"{cid}.ultima_verificacion")

        exigir_estado(c["estado"], [n for n in EVIDENCIAS if evs.get(n)],
                      c["sesiones"], c.get("ultima_verificacion"), cid)

    resumen = doc.get("resumen") or {}
    for estado in ESTADOS:
        real = sum(1 for c in conceptos if c["estado"] == estado)
        exige(resumen.get(estado) == real, f"resumen.{estado}",
               f"declara {resumen.get(estado)}, hay {real}")
    exige(resumen.get("siguiente_recomendado") in ids,
           "resumen.siguiente_recomendado", "debe ser el id de un concepto existente")




def exigir_estado(estado, presentes, sesiones, ultima_verificacion, cid):
    """El estado declarado debe estar sostenido por las evidencias presentes."""
    if estado == "NO_ESTUDIADO":
        exige(not presentes and sesiones == 0, cid,
              "NO_ESTUDIADO exige evidencias vacias y sesiones 0")
    elif estado == "EN_ESTUDIO":
        exige(sesiones >= 1, cid, "EN_ESTUDIO exige al menos 1 sesion")
    elif estado == "COMPRENSION_PARCIAL":
        exige("explicar" in presentes, cid,
              "COMPRENSION_PARCIAL exige evidencia de explicar")
    elif estado == "COMPRENDIDO":
        exige({"explicar", "aplicar"} <= set(presentes), cid,
              "COMPRENDIDO exige explicar y aplicar")
    elif estado == "DOMINADO":
        exige(set(presentes) == set(EVIDENCIAS), cid,
              "DOMINADO exige las cuatro evidencias")
    elif estado == "REQUIERE_REPASO":
        exige(presentes and ultima_verificacion, cid,
              "REQUIERE_REPASO exige al menos una evidencia y ultima_verificacion")


# --- eventos de los laboratorios v2 (REQ-TUT-013) ---------------------------
# El nucleo de 07_DATITO/01_CONCEPTOS/visual/ (03_SCRIPTS/plantillas/nucleo_v2.js)
# exporta lo que el alumno hizo como un bloque que se pega en el chat:
#   DATITO-EVENTOS v1 · 20_llm
#   {"tipo":"prediccion","id":"p1","texto":"...","ts":"..."}
TIPOS_EVENTO = {"prediccion", "intento", "pidio_respuesta", "observacion", "nivel"}
CABECERA_EVENTOS = re.compile(r"DATITO-EVENTOS v1 · (\S+)")


def leer_eventos(texto):
    """(pagina, [evento]) del bloque DATITO-EVENTOS de un mensaje; None si no hay bloque.

    Las lineas que no son un evento valido se descartan: el bloque viene del
    portapapeles del alumno y puede llegar cortado."""
    import json
    m = CABECERA_EVENTOS.search(texto or "")
    if not m:
        return None
    eventos = []
    for linea in texto[m.end():].splitlines():
        linea = linea.strip()
        if not linea.startswith("{"):
            continue
        try:
            ev = json.loads(linea)
        except ValueError:
            continue
        if isinstance(ev, dict) and ev.get("tipo") in TIPOS_EVENTO and isinstance(ev.get("id"), str):
            if ev["tipo"] != "pidio_respuesta" and ev["tipo"] != "nivel" and not isinstance(ev.get("texto"), str):
                continue
            eventos.append(ev)
    return m.group(1), eventos


def contraste(eventos):
    """(prediccion, observacion) a contrastar: la ultima prediccion y la primera
    observacion posterior a ella. None si falta alguna."""
    pred = None
    for i, ev in enumerate(eventos):
        if ev["tipo"] == "prediccion":
            pred = (i, ev)
    if pred is None:
        return None
    obs = next((ev for ev in eventos[pred[0] + 1:] if ev["tipo"] == "observacion"), None)
    return (pred[1], obs) if obs else None
