"""Motor del harness de escenarios del tutor (REQ-TUT-001).

Las reglas son el contrato de comportamiento (G1, G11, spec §3); los escenarios
son casos; los transcripts son la evidencia a validar. Todo puro y testeable:
cargar escenario -> cargar transcript -> evaluar reglas -> reporte.

  python 04_CODIGO/harness_escenarios/harness.py [--solo G1|G2|G11|INTENTOS|BORDE|RIGOR|LAB] [--json]
      [--generador referencia|claude|socratico] [--corridas N] [--presupuesto USD] [--tope USD]
      [--comparar socratico,claude]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
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

# TutorMoments (REQ-TUT-015): exigir rigor tras un acierto, no andamiar antes de intentar.
RIGOR = re.compile(r"por ?qu[eé]|expl[ií]ca|qu[eé] le (pasa|ocurre)|te falta|justific|mecanismo|\by si\b|qu[eé] pasar[ií]a|"
                   r"otro (caso|dominio|ejemplo|contexto)|variante|si cambi|generaliz|transfi[eé]r|sin (ayuda|mirar)",
                   re.I)
PISTA = re.compile(r"\bpista\s*:|te doy una pista|una pista\b(?![^.?!]*\?)", re.I)
# ofrecer la pista para despues del intento no es darla: "si quieres una pista, la pides tu"
OFRECE_PISTA = re.compile(r"si (quieres|necesitas)|p[ií]de(me|la|s)|la pides|no te doy", re.I)
# una consigna en imperativo tambien exige: "Clasifica R y S y muestra la brecha."
CONSIGNA = re.compile(r"\b(clasifica|calcula|explica|justifica|responde|muestra|escribe|demuestra|compara)\b", re.I)


def _da_pista(texto):
    for frase in re.split(r"(?<=[.?!\n])", texto):
        m = PISTA.search(frase)
        if m and not OFRECE_PISTA.search(frase):
            return m.group(0)
    return None


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
            # la pregunta de transferencia puede cerrar el mismo turno de la entrega
            resto = turnos[i:]
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
        # basta que pregunte: puede cerrar con una instruccion ("responde con tu eleccion")
        if "?" not in t["texto"]:
            viola.append(f"turno {i}: el primer turno del tutor no pregunta nada (decide por el alumno)")
        break
    return viola


def _siguiente_tutor(turnos, i):
    return next(((j, s) for j, s in enumerate(turnos[i + 1:], i + 1) if s["rol"] == "tutor"), (None, None))


def regla_empuja_rigor(turnos, esc):
    """Tras un acierto, el tutor sube la exigencia (explicar, variar, transferir) y pregunta:
    no re-explica ni cierra el tema (TutorMoments: los LM sobre-andamian y no empujan rigor)."""
    viola = []
    for i, t in enumerate(turnos):
        if t["rol"] != "alumno" or t.get("resultado") != "acerto":
            continue
        j, sig = _siguiente_tutor(turnos, i)
        if sig is None:
            continue
        if "?" not in sig["texto"] and not CONSIGNA.search(sig["texto"]):
            viola.append(f"turno {j}: tras el acierto del turno {i} no pregunta nada (cierra sin exigir mas)")
        elif not RIGOR.search(sig["texto"]):
            viola.append(f"turno {j}: tras el acierto no pide explicar, variar ni transferir")
    return viola


def regla_sin_sobreandamiaje(turnos, esc):
    """Antes del primer intento del alumno, el tutor no entrega pistas."""
    senales = [x.lower() for x in esc.get("senal_pista") or []]
    viola = []
    for i, t in enumerate(turnos):
        if t["rol"] == "alumno" and t.get("resultado"):
            break
        if t["rol"] == "tutor":
            txt = t["texto"].lower()
            m = _da_pista(t["texto"]) or next((x for x in senales if x in txt), None)
            if m:
                viola.append(f"turno {i}: da una pista antes del primer intento ({m!r})")
    return viola


def regla_parte_del_evento(turnos, esc):
    """REQ-TUT-013: si el alumno pega DATITO-EVENTOS, el tutor abre contrastando lo que predijo
    con lo que observo, y pregunta."""
    ev = esc.get("evento_lab")
    if not ev:
        return []
    for i, t in enumerate(turnos):
        if t["rol"] == "alumno" and "DATITO-EVENTOS" in t["texto"]:
            j, sig = _siguiente_tutor(turnos, i)
            if sig is None:
                return [f"turno {i}: el bloque del lab queda sin respuesta"]
            txt, viola = sig["texto"].lower(), []
            if not any(w.lower() in txt for w in ev["citar_prediccion"]):
                viola.append(f"turno {j}: no retoma lo que el alumno predijo")
            if not any(w.lower() in txt for w in ev["citar_observacion"]):
                viola.append(f"turno {j}: no retoma lo que el alumno observo")
            if "?" not in sig["texto"]:
                viola.append(f"turno {j}: no pregunta por que")
            return viola
    return ["el alumno nunca pega el bloque DATITO-EVENTOS"]


REGLAS = {"espera_real": regla_espera_real,
          "no_simula_alumno": regla_no_simula_alumno,
          "solucion_tras_dos_intentos": regla_solucion_tras_dos_intentos,
          "respuesta_pedida_registrada": regla_respuesta_pedida_registrada,
          "transferencia_tras_respuesta": regla_transferencia_tras_respuesta,
          "degradacion_explicita": regla_degradacion_explicita,
          "pregunta_antes_de_ejecutar": regla_pregunta_antes_de_ejecutar,
          "empuja_rigor": regla_empuja_rigor,
          "sin_sobreandamiaje": regla_sin_sobreandamiaje,
          "parte_del_evento": regla_parte_del_evento}
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
    faltan = [k for k in ("id", "garantia", "situacion", "contexto", "entrada", "transcript", "reglas")
              if k not in esc]
    if faltan:
        raise ValueError(f"escenario {ruta_escenario.name}: faltan claves {faltan}")
    return esc, evaluar(esc, transcript)


def cargar_escenarios(solo=None):
    escenarios = []
    for ruta in sorted(ESCENARIOS.glob("*.yaml")):
        esc = cargar(ruta)
        faltan = [k for k in ("id", "garantia", "situacion", "contexto", "entrada", "transcript", "reglas")
                  if k not in esc]
        if faltan:
            raise ValueError(f"escenario {ruta.name}: faltan claves {faltan}")
        if not solo or esc["garantia"] == solo:
            escenarios.append(esc)
    return escenarios


# Lo que ve la skill real: hechos de la situacion, nunca la conducta esperada.
FILTRA_EXPECTATIVA = re.compile(r"\b(el tutor|datito|tutormoments|req-tut|lo correcto|acierta|falla|debe|g\d+|regla)\b", re.I)


# REQ-TUT-009 (aprobado 2026-10-28): G1 y G11 sin excepcion; el resto >= 90 % en N/N.
GATE_ESTRICTO = {"G1", "G11"}
UMBRAL_GLOBAL = 0.90
PRESUPUESTO_LLAMADA = 0.50
TOPE_CORRIDA = 15.0


def reporte(solo=None, generador="referencia", corridas=1,
            presupuesto=PRESUPUESTO_LLAMADA, tope=TOPE_CORRIDA, modelo=None):
    from generadores import ErrorGeneracion, obtener
    gen = obtener(generador)
    filas, gastado = [], 0.0
    for esc in cargar_escenarios(solo):
        pasa, viola, errores = 0, [], []
        for n in range(1, corridas + 1):
            if gastado >= tope:
                errores.append(f"corrida {n}: budget (tope {tope:.2f} USD alcanzado)")
                continue
            try:
                tr = gen.generar(esc, n, presupuesto=presupuesto, modelo=modelo)
            except ErrorGeneracion as e:
                errores.append(f"corrida {n}: {e}")
                if e.tipo == "aislamiento":
                    raise
                continue
            gastado += float((tr.get("meta") or {}).get("costo_usd") or 0.0)
            v = evaluar(esc, tr)
            pasa += not v
            viola.extend(v if corridas == 1 else [f"(corrida {n}) {x}" for x in v])
        filas.append({"id": esc["id"], "garantia": esc["garantia"], "titulo": esc.get("titulo", ""),
                      "ok": pasa == corridas, "pasa": pasa, "corridas": corridas,
                      "error": bool(errores), "violaciones": errores + viola})
    return filas, gastado


def veredicto(filas):
    """Gate de REQ-TUT-009: (ok, motivos)."""
    motivos = []
    estrictas = [f for f in filas if f["garantia"] in GATE_ESTRICTO and not f["ok"]]
    if estrictas:
        motivos.append("G1/G11 deben pasar N/N: " + ", ".join(f["id"] for f in estrictas))
    resto = [f for f in filas if f["garantia"] not in GATE_ESTRICTO]
    if resto:
        tasa = sum(f["ok"] for f in resto) / len(resto)
        if tasa < UMBRAL_GLOBAL:
            motivos.append(f"resto {tasa:.0%} < {UMBRAL_GLOBAL:.0%}")
    return not motivos, motivos


def comparar(a, b, **kw):
    fa, _ = reporte(generador=a, **kw)
    fb, _ = reporte(generador=b, **kw)
    ok_b = {f["id"]: f["ok"] for f in fb}
    return [(f["id"], f["ok"], ok_b.get(f["id"])) for f in fa if f["ok"] != ok_b.get(f["id"])]


def main():
    ap = argparse.ArgumentParser(description="Valida transcripts contra los escenarios del tutor.")
    ap.add_argument("--solo", choices=["G1", "G2", "G11", "INTENTOS", "BORDE", "RIGOR", "LAB"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--generador", default="referencia", choices=["referencia", "claude", "socratico"])
    ap.add_argument("--corridas", type=int, default=1)
    ap.add_argument("--presupuesto", type=float, default=PRESUPUESTO_LLAMADA, help="USD por llamada")
    ap.add_argument("--tope", type=float, default=TOPE_CORRIDA, help="USD por corrida completa")
    ap.add_argument("--modelo")
    ap.add_argument("--comparar", metavar="A,B", help="lista escenarios donde dos generadores difieren")
    args = ap.parse_args()
    kw = dict(solo=args.solo, corridas=args.corridas, presupuesto=args.presupuesto,
              tope=args.tope, modelo=args.modelo)

    if args.comparar:
        a, b = args.comparar.split(",")
        dif = comparar(a, b, **kw)
        for id_, oa, ob in dif:
            print(f"DIFIERE  {id_}: {a}={'PASS' if oa else 'FAIL'} {b}={'PASS' if ob else 'FAIL'}")
        print(f"\n{len(dif)} escenarios difieren entre {a} y {b}")
        sys.exit(0)

    filas, gastado = reporte(generador=args.generador, **kw)
    if args.json:
        print(json.dumps(filas, ensure_ascii=False, indent=2))
    else:
        for f in filas:
            marca = "ERROR" if f["error"] and not f["ok"] else ("PASS" if f["ok"] else "FAIL")
            if args.corridas > 1:
                marca += f" {f['pasa']}/{f['corridas']}"
            print(f"{marca}  [{f['garantia']:<8}] {f['id']} — {f['titulo']}")
            for v in f["violaciones"]:
                print(f"        {v}")
        buenas = sum(1 for f in filas if f["ok"])
        print(f"\n{buenas}/{len(filas)} escenarios cumplen" + (f" ({args.solo})" if args.solo else ""))
        if args.generador != "referencia":
            ok, motivos = veredicto(filas)
            print(f"gate REQ-TUT-009: {'PASS' if ok else 'FAIL'}" + (f" — {'; '.join(motivos)}" if motivos else "")
                  + f" · gastado {gastado:.2f} USD")
    if args.generador == "referencia":
        sys.exit(0 if all(f["ok"] for f in filas) else 1)
    sys.exit(0 if veredicto(filas)[0] else 1)


if __name__ == "__main__":
    main()
