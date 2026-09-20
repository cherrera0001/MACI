"""
Verifica las garantias de spec.md que se pueden comprobar sin criterio humano.

POR QUE EXISTE
Analisis de nueve errores propios cometidos en el desarrollo de Guillito: el
patron comun no fue descuido, fue verificar la ENTRADA y no verificar que la
ACCION surtiera efecto. Escribir una regla no la pone en vigor; correr git add
no dice que quedo en el indice; disenar un instrumento no garantiza que mida.

Y el segundo hallazgo: los errores que quedaron corregidos de forma permanente
son exactamente aquellos donde se escribio una comprobacion externa. Los que se
resolvieron con "lo hare mejor" reaparecieron al turno siguiente.

Esto es esa comprobacion externa. No depende de que el agente recuerde.

USO
  python 03_CODIGO/verificar_contrato.py
  python 03_CODIGO/verificar_contrato.py --estricto   # codigo 1 si algo falla
"""
import argparse
import glob
import os
import re
import subprocess
import sys

RAIZ = r"F:\MACI"
OK, FALLO, AVISO = "OK", "FALLO", "AVISO"


def leer(ruta):
    p = os.path.join(RAIZ, ruta)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def git(*args):
    r = subprocess.run(["git", "-C", RAIZ, *args],
                       capture_output=True, text=True, errors="replace")
    return r.stdout


# --------------------------------------------------------------------------
def g1_no_simula_respuestas():
    """Ninguna bitacora debe contener una respuesta inventada del alumno."""
    sospechosos = []
    for f in glob.glob(os.path.join(RAIZ, "07_GUILLITO", "bitacora", "*.md")):
        t = open(f, encoding="utf-8", errors="replace").read()
        for patron in (r"probablemente dirias", r"supongamos que responde",
                       r"el alumno diria"):
            if re.search(patron, t, re.I):
                sospechosos.append(f"{os.path.basename(f)}: '{patron}'")
    if sospechosos:
        return FALLO, "respuestas simuladas en bitacora: " + "; ".join(sospechosos)
    return OK, "ninguna respuesta simulada en las bitacoras"


def g8_reglas_donde_se_leen():
    """Las reglas de conducta van en SKILL.md, no en la config."""
    cfg = leer("07_GUILLITO/guillito.config.yaml")
    if cfg is None:
        return AVISO, "no existe guillito.config.yaml"
    # Palabras que delatan una REGLA, no un dato
    reglas = len(re.findall(r"\b(nunca|prohibido|obligatori|no abrir|debe )", cfg, re.I))
    skill = leer(".claude/skills/guillito/SKILL.md")
    if skill is None:
        return FALLO, "no existe la skill guillito"
    if "guillito.config" not in skill:
        return FALLO, "SKILL.md no referencia la config: nada de lo escrito alli se lee"
    if reglas > 12:
        return AVISO, f"la config tiene {reglas} marcas de regla; deberia guardar datos"
    return OK, f"SKILL.md referencia la config; {reglas} marcas de regla en ella"


def g9_exposicion_consultable():
    """Cada concepto trabajado deja material consultable. El medio es libre."""
    import yaml
    pro = yaml.safe_load(leer("07_GUILLITO/progreso.yaml"))
    tocados = [c["id"] for c in pro["conceptos"] if c["estado"] != "NO_ESTUDIADO"]
    if not tocados:
        return OK, "ningun concepto iniciado todavia"

    # Cualquier medio vale: HTML, guia, cuadernillo o bitacora con desarrollo.
    material = " ".join(
        os.path.basename(p) for p in
        glob.glob(os.path.join(RAIZ, "07_GUILLITO", "visual", "*")) +
        glob.glob(os.path.join(RAIZ, "07_GUILLITO", "guias", "*")) +
        glob.glob(os.path.join(RAIZ, "07_GUILLITO", "cuadernillos", "*")) +
        glob.glob(os.path.join(RAIZ, "07_GUILLITO", "bitacora", "*"))
    ).lower()

    sin = [c for c in tocados
           if not any(t in material for t in c.split("_") if len(t) > 4)]
    if sin:
        return FALLO, "conceptos trabajados sin material consultable: " + ", ".join(sin)
    return OK, f"los {len(tocados)} conceptos trabajados tienen material"


def g12_dos_prioridades():
    """El grafo debe traer ambas dimensiones, y estar al dia."""
    import yaml
    g = leer("07_GUILLITO/grafo.yaml")
    if g is None:
        return FALLO, "no existe grafo.yaml; ejecutar grafo_conceptual.py"
    doc = yaml.safe_load(g)
    cs = doc.get("conceptos", {})
    faltan = [cid for cid, d in cs.items()
              if "importancia_curricular" not in d or "prioridad_evaluacion" not in d]
    if faltan:
        return FALLO, f"{len(faltan)} conceptos sin las dos prioridades"

    gp = os.path.join(RAIZ, "07_GUILLITO", "grafo.yaml")
    cp = os.path.join(RAIZ, "07_GUILLITO", "curriculum.yaml")
    if os.path.getmtime(cp) > os.path.getmtime(gp) + 5:
        return FALLO, "curriculum.yaml es mas nuevo que grafo.yaml: regenerar"

    tens = sum(1 for d in cs.values() if d.get("tension"))
    return OK, f"{len(cs)} conceptos con ambas prioridades; {tens} con tension declarada"


def g13_sin_deficiencia_inferida():
    """Nada debe marcarse como bajo o fallido sin evidencia registrada."""
    import yaml
    err = yaml.safe_load(leer("07_GUILLITO/errores_conceptuales.yaml"))
    malos = []
    for o in (err.get("observados") or []):
        if not (o.get("dijo") or "").strip():
            malos.append(f"{o.get('id')} sin cita de lo que dijo")
    if malos:
        return FALLO, "errores sin evidencia textual: " + "; ".join(malos[:3])
    n = len(err.get("observados") or [])
    return OK, f"{n} errores observados, todos con evidencia textual"


def memoria_dominado_con_evidencia():
    """DOMINADO exige las evidencias registradas, no la etiqueta sola."""
    import yaml
    pro = yaml.safe_load(leer("07_GUILLITO/progreso.yaml"))
    malos = []
    for c in pro["conceptos"]:
        if c["estado"] != "DOMINADO":
            continue
        ev = c.get("evidencias") or {}
        faltan = [k for k in ("explicar", "aplicar", "transferir") if not ev.get(k)]
        if faltan:
            malos.append(f"{c['id']} sin {'/'.join(faltan)}")
    if malos:
        return FALLO, "DOMINADO sin evidencia completa: " + "; ".join(malos)
    n = sum(1 for c in pro["conceptos"] if c["estado"] == "DOMINADO")
    return OK, f"{n} conceptos en DOMINADO, todos con evidencia completa"


def seguridad_sin_secretos():
    """Ningun secreto ni binario pesado versionado."""
    archivos = git("ls-files").splitlines()
    patron = re.compile(r"storage_state|master_token|auth\.json|cookie|\.env$"
                        r"|\.mp4$|\.zip$|\.mkv$", re.I)
    malos = [a for a in archivos if patron.search(a)]
    if malos:
        return FALLO, "versionado lo que no debe: " + ", ".join(malos[:5])

    cfg = leer(".git/config") or ""
    if re.search(r"ghp_|github_pat_", cfg):
        return FALLO, "hay un token escrito en .git/config"
    return OK, f"{len(archivos)} archivos versionados, ningun secreto ni binario pesado"


def estado_al_dia():
    """estado.md es lo que se inyecta: si esta viejo, la sesion abre mal."""
    e = os.path.join(RAIZ, "07_GUILLITO", "estado.md")
    p = os.path.join(RAIZ, "07_GUILLITO", "progreso.yaml")
    if not os.path.exists(e):
        return FALLO, "no existe estado.md; ejecutar guillito_estado.py"
    if os.path.getmtime(p) > os.path.getmtime(e) + 5:
        return FALLO, "progreso.yaml es mas nuevo que estado.md: ejecutar guillito_estado.py"
    return OK, "estado.md al dia respecto de progreso.yaml"


def rutas_declaradas_existen():
    """El curriculum no debe citar material inexistente."""
    import yaml
    cur = yaml.safe_load(leer("07_GUILLITO/curriculum.yaml"))
    faltan = []
    for c in cur["conceptos"]:
        for r in (c.get("material_local") or []):
            if not os.path.exists(os.path.join(RAIZ, r)):
                faltan.append(f"{c['id']}: {r}")
    for k, v in (cur.get("practicos") or {}).items():
        for campo in ("res", "vacio"):
            if v.get(campo) and not os.path.exists(os.path.join(RAIZ, v[campo])):
                faltan.append(f"{k}.{campo}: {v[campo]}")
    if faltan:
        return FALLO, "material citado que no existe: " + "; ".join(faltan[:4])
    return OK, "todas las rutas del curriculum existen"


COMPROBACIONES = [
    ("G1  no simula respuestas",      g1_no_simula_respuestas),
    ("G8  reglas donde se leen",      g8_reglas_donde_se_leen),
    ("G9  exposicion consultable",    g9_exposicion_consultable),
    ("G12 dos prioridades",           g12_dos_prioridades),
    ("G13 sin deficiencia inferida",  g13_sin_deficiencia_inferida),
    ("Memoria  DOMINADO con evidencia", memoria_dominado_con_evidencia),
    ("Seguridad  sin secretos",       seguridad_sin_secretos),
    ("Estado  resumen al dia",        estado_al_dia),
    ("Curriculum  rutas existen",     rutas_declaradas_existen),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--estricto", action="store_true",
                    help="codigo de salida 1 si alguna comprobacion falla")
    args = ap.parse_args()

    print("Verificacion del contrato de Guillito (spec.md)")
    print("=" * 74)
    fallos = avisos = 0
    for nombre, fn in COMPROBACIONES:
        try:
            estado, detalle = fn()
        except Exception as e:
            estado, detalle = FALLO, f"la comprobacion reviento: {e}"
        marca = {OK: "  ok  ", FALLO: " FALLO", AVISO: " aviso"}[estado]
        print(f"[{marca}] {nombre:<34} {detalle}")
        fallos += estado == FALLO
        avisos += estado == AVISO

    print("=" * 74)
    print(f"{len(COMPROBACIONES) - fallos - avisos} ok · {avisos} avisos · {fallos} fallos")
    if fallos and args.estricto:
        sys.exit(1)


if __name__ == "__main__":
    main()
