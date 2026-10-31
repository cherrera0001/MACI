"""Micro-talleres prácticos de autonomía y reconversión (D-14.1).

Misiones cotidianas de 3 pasos sobre LuchaProductiva: se revela un paso a
la vez, «ayuda» acerca la pista del paso actual sin penalización y
completar celebra y conecta con una memoria del usuario. Cada taller se
ancla a una guía del curso citada [fid] y validada con evidencia.validar;
si la guía no existe en el índice, el taller no se ofrece (la regla
anti-alucinación manda también aquí). Sin estados punitivos de fallo:
la persona nunca reprueba, solo avanza a su ritmo.
"""
from __future__ import annotations

import yaml

from . import evidencia, progreso
from .lucha import LuchaProductiva

RUTA_DEFINICIONES = "talleres.yaml"
RUTA_ESTADO = "taller_estado.yaml"


def _leer(curso, nombre: str) -> dict:
    p = curso.ruta(nombre)
    if not p.exists():
        return {}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def _escribir(curso, nombre: str, datos: dict):
    curso.ruta(nombre).write_text(
        yaml.safe_dump(datos, allow_unicode=True, sort_keys=False),
        encoding="utf-8")


def _definiciones(curso) -> list[dict]:
    return (_leer(curso, RUTA_DEFINICIONES).get("talleres") or [])


def _paso_texto(taller: dict, n: int, total: int, fid: str, indice) -> str:
    """Texto del paso con su cita; la cita se retira si no valida."""
    base = f"Paso {n + 1}/{total}: {taller['pasos'][n]['objetivo']}"
    val = evidencia.validar(f"{base} [{fid}]", indice)
    return f"{base} [{fid}]" if val.ok else base


def _anclaje(taller: dict, fid: str, indice) -> str | None:
    """Presentación del taller citando su guía (texto de la guía, valida)."""
    guia = indice.textos[fid]
    texto = f"Esto se apoya en lo que guardamos juntos: «{guia}» [{fid}]"
    val = evidencia.validar(texto, indice)
    return texto if val.ok else None


def _ofrecibles(curso, indice) -> list[dict]:
    """Talleres cuya guía existe y cuyo primer paso con cita valida."""
    salida = []
    for t in _definiciones(curso):
        fid = str(t.get("guia_fid", ""))
        pasos = t.get("pasos") or []
        if fid not in indice.textos or not pasos:
            continue
        val = evidencia.validar(f"{pasos[0]['objetivo']} [{fid}]", indice)
        if val.ok:
            salida.append(t)
    return salida


def _estado(curso) -> dict:
    est = _leer(curso, RUTA_ESTADO)
    est.setdefault("completados", [])
    return est


def _memoria_asociada(taller: dict, indice) -> dict | None:
    """Un recuerdo del usuario cercano al tema (citable y validado)."""
    try:
        top = indice.buscar_asociativo(taller.get("tema", ""), k=8)
    except Exception:  # noqa: BLE001 - la celebración nunca rompe el taller
        top = []
    for fid, _score, _puentes in top:
        if not fid.startswith("memoria#"):
            continue
        if indice.referencias.get(fid, ("", ""))[1].startswith("guia:"):
            continue
        val = evidencia.validar(
            f"Recuerde que {indice.textos[fid]} [{fid}]", indice)
        if val.ok:
            return {"fid": fid, "texto": indice.textos[fid]}
    return None


def _completar(curso, indice, taller: dict) -> dict:
    est = _estado(curso)
    est["activo"] = None
    if taller["id"] not in est["completados"]:
        est["completados"].append(taller["id"])
    _escribir(curso, RUTA_ESTADO, est)
    datos = progreso.cargar(curso)
    datos["metricas"]["talleres_completados"] = \
        datos["metricas"].get("talleres_completados", 0) + 1
    progreso.guardar(curso, datos)
    memoria = _memoria_asociada(taller, indice)
    cierre = (f"¡Taller terminado! Aprendió «{taller['titulo']}» paso a paso, "
              "a su ritmo y sin miedo. Esto queda suyo para siempre.")
    evidencia_cierre = []
    if memoria:
        candidato = (f"{cierre} Y viendo lo que practicó, recuerdo esto "
                     f"suyo: «{memoria['texto']}» [{memoria['fid']}]")
        if evidencia.validar(candidato, indice).ok:
            cierre = candidato
            evidencia_cierre = [{"fid": memoria["fid"],
                                 "fuente": indice.referencias[memoria["fid"]][0],
                                 "referencia":
                                 indice.referencias[memoria["fid"]][1]}]
        else:
            memoria = None
    return {"completado": True, "celebracion": cierre, "memoria": memoria,
            "paso": None, "evidencia": evidencia_cierre,
            "modo": "compania"}


def estado(curso, indice) -> dict:
    """GET /taller: talleres ofrecibles + activo + paso visible."""
    ofrecibles = _ofrecibles(curso, indice)
    est = _estado(curso)
    activo = paso = anclaje = None
    if est.get("activo"):
        tid = est["activo"].get("taller_id")
        t = next((x for x in ofrecibles if x["id"] == tid), None)
        if t:
            fid = str(t.get("guia_fid", ""))
            total = len(t["pasos"])
            n = min(max(1, int(est["activo"].get("revelados", 1))), total)
            paso = {"n": n, "total": total,
                    "texto": _paso_texto(t, n - 1, total, fid, indice)}
            anclaje = _anclaje(t, fid, indice) if n == 1 else None
            activo = {"taller_id": tid, "titulo": t["titulo"], "revelados": n}
    return {"talleres": [{"id": t["id"], "titulo": t["titulo"],
                          "n_pasos": len(t["pasos"])} for t in ofrecibles],
            "completados": est["completados"], "activo": activo,
            "paso": paso, "anclaje": anclaje, "completado": False,
            "modo": "compania"}


def elegir(curso, indice, taller_id: str | None = None) -> dict:
    """Inicia un taller (el pedido, o el primero sin completar)."""
    ofrecibles = _ofrecibles(curso, indice)
    if not ofrecibles:
        return {"talleres": [], "activo": None, "paso": None,
                "anclaje": None, "completado": False,
                "motivo": "sin_talleres"}
    t = next((x for x in ofrecibles if x["id"] == taller_id), None) \
        if taller_id else None
    est = _estado(curso)
    if t is None:
        t = next((x for x in ofrecibles
                  if x["id"] not in est["completados"]), ofrecibles[0])
    fid = str(t.get("guia_fid", ""))
    total = len(t["pasos"])
    est["activo"] = {"taller_id": t["id"], "revelados": 1}
    _escribir(curso, RUTA_ESTADO, est)
    paso = {"n": 1, "total": total,
            "texto": _paso_texto(t, 0, total, fid, indice)}
    return {"talleres": [{"id": x["id"], "titulo": x["titulo"],
                          "n_pasos": len(x["pasos"])} for x in ofrecibles],
            "completados": est["completados"],
            "activo": {"taller_id": t["id"], "titulo": t["titulo"],
                       "revelados": 1},
            "paso": paso, "anclaje": _anclaje(t, fid, indice),
            "completado": False, "modo": "compania"}


def avanzar(curso, indice) -> dict:
    """«Lo hice»: revela el siguiente paso o completa el taller."""
    est = _estado(curso)
    if not est.get("activo"):
        return elegir(curso, indice)
    tid = est["activo"]["taller_id"]
    t = next((x for x in _ofrecibles(curso, indice) if x["id"] == tid), None)
    if not t:
        est["activo"] = None
        _escribir(curso, RUTA_ESTADO, est)
        return elegir(curso, indice)
    fid = str(t.get("guia_fid", ""))
    total = len(t["pasos"])
    lucha = LuchaProductiva(
        pasos=[_paso_texto(t, i, total, fid, indice) for i in range(total)],
        estado="pista",
        pasos_revelados=int(est["activo"].get("revelados", 1)))
    siguiente = lucha.mostrar_paso()
    if siguiente is None:
        return _completar(curso, indice, t)
    est["activo"]["revelados"] = lucha.pasos_revelados
    _escribir(curso, RUTA_ESTADO, est)
    return {"activo": {"taller_id": tid, "titulo": t["titulo"],
                       "revelados": lucha.pasos_revelados},
            "paso": {"n": lucha.pasos_revelados, "total": total,
                     "texto": siguiente},
            "celebracion": "¡Muy bien! Vamos con el siguiente paso.",
            "completado": False, "modo": "compania"}


def ayuda(curso, indice) -> dict:
    """Pista del paso actual: acerca ayuda sin cambiar de paso ni penalizar."""
    est = _estado(curso)
    if not est.get("activo"):
        r = elegir(curso, indice)
        r["pista"] = None
        return r
    tid = est["activo"]["taller_id"]
    t = next((x for x in _ofrecibles(curso, indice) if x["id"] == tid), None)
    if not t:
        return {"pista": None, "motivo": "sin_taller_activo"}
    n = max(1, int(est["activo"].get("revelados", 1)))
    pista = t["pasos"][min(n, len(t["pasos"])) - 1].get("ayuda", "")
    return {"activo": {"taller_id": tid, "titulo": t["titulo"],
                       "revelados": n},
            "paso": {"n": n, "total": len(t["pasos"])},
            "pista": pista, "completado": False, "modo": "compania"}
