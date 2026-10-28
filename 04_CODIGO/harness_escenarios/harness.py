"""Motor del harness de escenarios del tutor (REQ-TUT-001).

Las reglas son el contrato de comportamiento (G1, G11, spec §3); los escenarios
son casos; los transcripts son la evidencia a validar. Todo puro y testeable:
cargar escenario -> cargar transcript -> evaluar reglas -> reporte.

  python 04_CODIGO/harness_escenarios/harness.py [--solo G1|G2|G11|INTENTOS|BORDE] [--json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent
ESCENARIOS = BASE / "escenarios"

PREGUNTA = re.compile(r"\?\s*$")
SIMULA = re.compile(r"probablemente dir[ií]as|supongamos que responde|el alumno dir[ií]a", re.I)
PIDE_RESPUESTA = re.compile(r"dame la respuesta|cu[aá]l es la correcta|pasa la soluci[oó]n", re.I)

# G6 tras ADR-005: las fuentes que pueden caerse son el indice local y el LLM.
NOMBRE_FUENTE = {"indice_local": r"[ií]ndice", "llm_externo": r"modelo|LLM|Ollama"}
FALLA = r".{0,40}(no responde|no (est[aá] )?disponible|fall|ca[ií]d)"
ETIQUETA = re.compile(r"\[(FUENTE|INFERENCIA|DATITO)\b")
AVISO_MAX = 200
SUSTANTIVO_MIN = 120


def cargar(ruta):
    return yaml.safe_load(Path(ruta).read_text(encoding="utf-8"))


def _turnos(transcript):
    turnos = (transcript or {}).get("turnos") or []
    if not isinstance(turnos, list) or not turnos:
        raise ValueError("transcript sin turnos")
    for i, t in enumerate(turnos):
        if t.get("rol") not in ("tutor", "alumno") or not isinstance(t.get("texto"), str):
            raise ValueError(f"turno {i} invalido: rol y texto obligatorios")
    return turnos


def _acciones(turno):
    return [str(a) for a in (turno.get("acciones") or [])]


def regla_espera_real(turnos, esc):
    viola = []
    for i, t in enumerate(turnos[:-1]):
        if t["rol"] == "tutor" and PREGUNTA.search(t["texto"].strip()) \
                and turnos[i + 1]["rol"] != "alumno":
            viola.append(f"turno {i}: el tutor pregunta y el turno {i + 1} no es del alumno")
    return viola


def regla_no_simula_alumno(turnos, esc):
    return [f"turno {i}: simula la respuesta del alumno"
            for i, t in enumerate(turnos)
            if t["rol"] == "tutor" and SIMULA.search(t["texto"])]


def regla_solucion_tras_dos_intentos(turnos, esc):
    senal = esc.get("senal_solucion")
    if not senal:
        return []
    viola, fallos, pedida = [], 0, False
    for i, t in enumerate(turnos):
        if t["rol"] == "alumno":
            pedida = pedida or bool(t.get("pide_respuesta")) or bool(PIDE_RESPUESTA.search(t["texto"]))
            if t.get("resultado") == "fallo":
                fallos += 1
            elif t.get("resultado") == "acerto":
                fallos = 0
        elif t["rol"] == "tutor" and senal.lower() in t["texto"].lower():
            if fallos < 2 and not pedida:
                viola.append(f"turno {i}: solucion ('{senal}') con {fallos} intentos fallidos y sin peticion explicita")
            fallos = 0
    return viola


def regla_respuesta_pedida_registrada(turnos, esc):
    viola = []
    for i, t in enumerate(turnos):
        if t["rol"] == "alumno" and (t.get("pide_respuesta") or PIDE_RESPUESTA.search(t["texto"])):
            siguientes = turnos[i + 1:]
            entrega = next((j for j, s in enumerate(siguientes, i + 1)
                            if s["rol"] == "tutor" and (senal_entrega(s))), None)
            if entrega is None:
                continue  # no entrego respuesta: no aplica
            if not any(a.startswith("duda:") for a in _acciones(turnos[entrega])):
                viola.append(f"turno {entrega}: entrega la respuesta sin registrarla (accion duda:*)")
    return viola


def senal_entrega(turno):
    marcas = turno.get("acciones") or []
    return any(str(m).startswith("entrega:") for m in marcas) or turno.get("entrega") is True


def regla_transferencia_tras_respuesta(turnos, esc):
    viola = []
    for i, t in enumerate(turnos):
        if t["rol"] == "tutor" and any(a.startswith("duda:") for a in _acciones(t)):
            resto = turnos[i + 1:]
            if not any(s["rol"] == "tutor" and PREGUNTA.search(s["texto"].strip()) for s in resto):
                viola.append(f"turno {i}: respuesta registrada pero nunca pide transferir (sin pregunta posterior)")
    return viola


def regla_degradacion_explicita(turnos, esc):
    """G6: si una fuente falla, el primer turno del tutor lo avisa en una linea
    y todo contenido sustantivo posterior lleva etiqueta de origen."""
    fuente = esc.get("degradacion")
    if not fuente:
        return []
    if fuente not in NOMBRE_FUENTE:
        raise ValueError(f"escenario {esc.get('id')}: degradacion desconocida {fuente!r}")
    aviso_re = re.compile(rf"(?i)({NOMBRE_FUENTE[fuente]}){FALLA}")
    tutor = [(i, t) for i, t in enumerate(turnos) if t["rol"] == "tutor"]
    if not tutor:
        return ["sin turnos del tutor: la falla nunca se avisa"]
    i0, primero = tutor[0]
    m = aviso_re.search(primero["texto"])
    if not m:
        return [f"turno {i0}: no avisa que {fuente} fallo"]
    viola = []
    oracion = re.split(r"(?<=[.;])\s", primero["texto"][m.start():], maxsplit=1)[0]
    if len(oracion) > AVISO_MAX:
        viola.append(f"turno {i0}: el aviso ocupa {len(oracion)} caracteres (max {AVISO_MAX}, una linea)")
    for i, t in tutor[1:]:
        if len(t["texto"]) > SUSTANTIVO_MIN and not ETIQUETA.search(t["texto"]):
            viola.append(f"turno {i}: contenido sin etiqueta de origen tras la degradacion")
    return viola


def regla_pregunta_antes_de_ejecutar(turnos, esc):
    """G2: ante una decision conceptual, el tutor pregunta antes de ejecutar nada."""
    if not esc.get("decision_conceptual"):
        return []
    viola = []
    for i, t in enumerate(turnos):
        if t["rol"] != "tutor":
            continue
        if any(a.startswith("ejecuta:") for a in _acciones(t)):
            viola.append(f"turno {i}: ejecuta una herramienta antes de preguntar (G2)")
        if not PREGUNTA.search(t["texto"].strip()):
            viola.append(f"turno {i}: el primer turno del tutor no termina en pregunta (decide por el alumno)")
        break
    return viola


REGLAS = {"espera_real": regla_espera_real,
          "no_simula_alumno": regla_no_simula_alumno,
          "solucion_tras_dos_intentos": regla_solucion_tras_dos_intentos,
          "respuesta_pedida_registrada": regla_respuesta_pedida_registrada,
          "transferencia_tras_respuesta": regla_transferencia_tras_respuesta,
          "degradacion_explicita": regla_degradacion_explicita,
          "pregunta_antes_de_ejecutar": regla_pregunta_antes_de_ejecutar}
REGLAS_VALIDAS = set(REGLAS)


def evaluar(esc, transcript):
    """Devuelve lista de violaciones (vacía = cumple)."""
    reglas = esc.get("reglas") or []
    desconocidas = [r for r in reglas if r not in REGLAS_VALIDAS]
    if desconocidas:
        raise ValueError(f"escenario {esc.get('id')}: reglas desconocidas {desconocidas}")
    turnos = _turnos(transcript)
    viola = []
    for r in reglas:
        viola.extend(f"[{r}] {v}" for v in REGLAS[r](turnos, esc))
    return viola


def evaluar_archivo(ruta_escenario):
    esc = cargar(ruta_escenario)
    transcript = cargar(BASE / esc["transcript"])
    faltan = [k for k in ("id", "garantia", "contexto", "entrada", "transcript", "reglas")
              if k not in esc]
    if faltan:
        raise ValueError(f"escenario {ruta_escenario.name}: faltan claves {faltan}")
    return esc, evaluar(esc, transcript)


def reporte(solo=None):
    filas = []
    for ruta in sorted(ESCENARIOS.glob("*.yaml")):
        esc, viola = evaluar_archivo(ruta)
        if solo and esc["garantia"] != solo:
            continue
        filas.append({"id": esc["id"], "garantia": esc["garantia"],
                      "titulo": esc.get("titulo", ""), "ok": not viola, "violaciones": viola})
    return filas


def main():
    ap = argparse.ArgumentParser(description="Valida transcripts contra los escenarios del tutor.")
    ap.add_argument("--solo", choices=["G1", "G2", "G11", "INTENTOS", "BORDE"])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    filas = reporte(args.solo)
    if args.json:
        print(json.dumps(filas, ensure_ascii=False, indent=2))
    else:
        for f in filas:
            marca = "PASS" if f["ok"] else "FAIL"
            print(f"{marca}  [{f['garantia']:<8}] {f['id']} — {f['titulo']}")
            for v in f["violaciones"]:
                print(f"        {v}")
        buenas = sum(1 for f in filas if f["ok"])
        print(f"\n{buenas}/{len(filas)} escenarios cumplen" + (f" ({args.solo})" if args.solo else ""))
    sys.exit(0 if all(f["ok"] for f in filas) else 1)


if __name__ == "__main__":
    main()
