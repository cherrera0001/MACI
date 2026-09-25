"""
Verifica las garantias de spec.md que se pueden comprobar sin criterio humano.

POR QUE EXISTE
Analisis de nueve errores propios cometidos en el desarrollo de Datito: el
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
    for f in glob.glob(os.path.join(RAIZ, "07_DATITO", "bitacora", "*.md")):
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
    cfg = leer("07_DATITO/datito.config.yaml")
    if cfg is None:
        return AVISO, "no existe datito.config.yaml"
    # Palabras que delatan una REGLA, no un dato
    reglas = len(re.findall(r"\b(nunca|prohibido|obligatori|no abrir|debe )", cfg, re.I))
    skill = leer(".claude/skills/datito/SKILL.md")
    if skill is None:
        return FALLO, "no existe la skill datito"
    if "datito.config" not in skill:
        return FALLO, "SKILL.md no referencia la config: nada de lo escrito alli se lee"
    if reglas > 12:
        return AVISO, f"la config tiene {reglas} marcas de regla; deberia guardar datos"
    return OK, f"SKILL.md referencia la config; {reglas} marcas de regla en ella"


def g9_exposicion_consultable():
    """Cada concepto trabajado deja material consultable. El medio es libre."""
    import yaml
    pro = yaml.safe_load(leer("07_DATITO/progreso.yaml"))
    tocados = [c["id"] for c in pro["conceptos"] if c["estado"] != "NO_ESTUDIADO"]
    if not tocados:
        return OK, "ningun concepto iniciado todavia"

    # Cualquier medio vale: HTML, guia, cuadernillo o bitacora con desarrollo.
    material = " ".join(
        os.path.basename(p) for p in
        glob.glob(os.path.join(RAIZ, "07_DATITO", "visual", "*")) +
        glob.glob(os.path.join(RAIZ, "07_DATITO", "guias", "*")) +
        glob.glob(os.path.join(RAIZ, "07_DATITO", "cuadernillos", "*")) +
        glob.glob(os.path.join(RAIZ, "07_DATITO", "bitacora", "*"))
    ).lower()

    sin = [c for c in tocados
           if not any(t in material for t in c.split("_") if len(t) > 4)]
    if sin:
        return FALLO, "conceptos trabajados sin material consultable: " + ", ".join(sin)
    return OK, f"los {len(tocados)} conceptos trabajados tienen material"


def g12_dos_prioridades():
    """El grafo debe traer ambas dimensiones, y estar al dia."""
    import yaml
    g = leer("07_DATITO/grafo.yaml")
    if g is None:
        return FALLO, "no existe grafo.yaml; ejecutar grafo_conceptual.py"
    doc = yaml.safe_load(g)
    cs = doc.get("conceptos", {})
    faltan = [cid for cid, d in cs.items()
              if "importancia_curricular" not in d or "prioridad_evaluacion" not in d]
    if faltan:
        return FALLO, f"{len(faltan)} conceptos sin las dos prioridades"

    gp = os.path.join(RAIZ, "07_DATITO", "grafo.yaml")
    cp = os.path.join(RAIZ, "07_DATITO", "curriculum.yaml")
    if os.path.getmtime(cp) > os.path.getmtime(gp) + 5:
        return FALLO, "curriculum.yaml es mas nuevo que grafo.yaml: regenerar"

    tens = sum(1 for d in cs.values() if d.get("tension"))
    return OK, f"{len(cs)} conceptos con ambas prioridades; {tens} con tension declarada"


def g13_sin_deficiencia_inferida():
    """Nada debe marcarse como bajo o fallido sin evidencia registrada."""
    import yaml
    err = yaml.safe_load(leer("07_DATITO/errores_conceptuales.yaml"))
    malos = []
    for o in (err.get("observados") or []):
        if not (o.get("dijo") or "").strip():
            malos.append(f"{o.get('id')} sin cita de lo que dijo")
    if malos:
        return FALLO, "errores sin evidencia textual: " + "; ".join(malos[:3])
    n = len(err.get("observados") or [])
    return OK, f"{n} errores observados, todos con evidencia textual"


def memoria_dominado_con_evidencia():
    """DOMINADO exige las CUATRO evidencias de spec.md, no la etiqueta sola.

    La cadena del contrato es:
        EXPLICAR -> APLICAR EN MELBOURNE -> INTERPRETAR RESULTADOS -> TRANSFERIR
    Hasta 2026-09-20 esta comprobacion miraba solo tres y se saltaba
    'interpretar': un concepto podia pasar el test incumpliendo spec.md §3.
    """
    import yaml
    pro = yaml.safe_load(leer("07_DATITO/progreso.yaml"))
    malos = []
    for c in pro["conceptos"]:
        if c["estado"] != "DOMINADO":
            continue
        ev = c.get("evidencias") or {}
        faltan = [k for k in ("explicar", "aplicar", "interpretar", "transferir")
                  if not ev.get(k)]
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
    e = os.path.join(RAIZ, "07_DATITO", "estado.md")
    p = os.path.join(RAIZ, "07_DATITO", "progreso.yaml")
    if not os.path.exists(e):
        return FALLO, "no existe estado.md; ejecutar datito_estado.py"
    if os.path.getmtime(p) > os.path.getmtime(e) + 5:
        return FALLO, "progreso.yaml es mas nuevo que estado.md: ejecutar datito_estado.py"
    return OK, "estado.md al dia respecto de progreso.yaml"


def rutas_declaradas_existen():
    """El curriculum no debe citar material inexistente."""
    import yaml
    cur = yaml.safe_load(leer("07_DATITO/curriculum.yaml"))
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


def g9_visuales_sin_red_y_citables():
    """Los visuales abren sin red, sus enlaces existen y sus citas de clase se
    pueden comprobar (ruta .md completa + marca que existe). Detalle en
    03_CODIGO/verificar_visuales.py; la prueba en navegador real es
    03_CODIGO/probar_visuales_offline.py."""
    sys.path.insert(0, os.path.join(RAIZ, "03_CODIGO"))
    import verificar_visuales
    fallos, avisos, resumen = verificar_visuales.revisar()
    if fallos:
        return FALLO, f"{len(fallos)} fallos en visuales; el primero: {fallos[0]}"
    if avisos:
        return AVISO, f"{resumen}; {len(avisos)} avisos (verificar_visuales.py --detalle)"
    return OK, resumen


def g9_lo_respondido_queda_escrito():
    """Lo que Datito responde en una sesion queda en dudas.yaml y en los
    visuales, no solo en el chat (spec.md G9, REGLA UNO-B).

    No se puede leer el chat, pero si exigir el rastro: desde el 2026-09-21 cada
    bitacora declara «Dudas registradas:» con ids que existen, y cada duda esta
    renderizada en los visuales que lista."""
    import yaml
    texto = leer("07_DATITO/dudas.yaml")
    if texto is None:
        return FALLO, "no existe 07_DATITO/dudas.yaml"
    dudas = (yaml.safe_load(texto) or {}).get("dudas") or []
    ids = {d.get("id") for d in dudas}
    problemas = []
    for d in dudas:
        for campo in ("respuesta", "resolucion", "fuentes"):
            if not d.get(campo):
                problemas.append(f"{d.get('id')} sin {campo}")
        for v in d.get("visuales") or []:
            html_v = leer(f"07_DATITO/01_CONCEPTOS/visual/{v}") or ""
            if f'id="duda-{d.get("id")}"' not in html_v:
                problemas.append(f"{d.get('id')} no esta en {v} (correr construir_navegacion.py)")
    for f in sorted(glob.glob(os.path.join(RAIZ, "07_DATITO", "bitacora", "*.md"))):
        nombre = os.path.basename(f)
        if nombre[:10] < "2026-09-21":
            continue  # la regla rige desde esa fecha
        t = open(f, encoding="utf-8", errors="replace").read()
        m = re.search(r"\*\*Dudas registradas:\*\*\s*([^\n]+)", t)
        if not m:
            problemas.append(f"{nombre} sin la linea «Dudas registradas:»")
            continue
        declarados = re.findall(r"\d{4}-\d{2}-\d{2}-[\w-]+", m.group(1))
        if not declarados and "ninguna" not in m.group(1).lower():
            problemas.append(f"{nombre}: «Dudas registradas:» vacia")
        for i in declarados:
            if i not in ids:
                problemas.append(f"{nombre}: la duda {i} no existe en dudas.yaml")
    if problemas:
        return FALLO, "; ".join(problemas[:3])
    return OK, f"{len(dudas)} dudas registradas, todas renderizadas en sus visuales"


def g14_el_material_es_un_curso():
    """Cada clase de clases.yaml con visual tiene barra, ficha Bloom, cierre y
    (si es de concepto) al menos tres preguntas con respuesta oculta; la
    portada existe (spec.md G14)."""
    import yaml
    texto = leer("07_DATITO/clases.yaml")
    if texto is None:
        return FALLO, "no existe 07_DATITO/clases.yaml"
    clases = (yaml.safe_load(texto) or {}).get("clases") or []
    portada = leer("07_DATITO/01_CONCEPTOS/visual/index.html") or ""
    if 'id="curso"' not in portada:
        return FALLO, "visual/index.html no es la portada del curso (correr construir_navegacion.py)"
    problemas, pendientes = [], 0
    for c in clases:
        for campo in ("titulo", "objetivo", "activacion", "bloom"):
            if not c.get(campo):
                problemas.append(f"clase {c.get('n')} sin {campo}")
        if not c.get("visual"):
            pendientes += 1
            continue
        base, _, ancla = c["visual"].partition("#")
        html_c = leer(f"07_DATITO/01_CONCEPTOS/visual/{base}")
        if html_c is None:
            problemas.append(f"clase {c['n']}: no existe {base}")
            continue
        if ancla and f'id="{ancla}"' not in html_c:
            problemas.append(f"clase {c['n']}: falta el ancla #{ancla}")
        if f'data-clase="{c["n"]}"' not in html_c:
            problemas.append(f"clase {c['n']}: sin barra de clase en {base}")
        if (c.get("cierre") or {}).get("aprendiste") and f'id="cierre-clase-{c["n"]}"' not in html_c:
            problemas.append(f"clase {c['n']}: sin cierre en {base}")
        if c.get("tipo") == "concepto" and html_c.count('class="resp"') < 3:
            problemas.append(f"clase {c['n']}: menos de 3 preguntas con respuesta oculta")
    if problemas:
        return FALLO, "; ".join(problemas[:3])
    return OK, f"{len(clases)} clases en orden; {pendientes} pendiente(s) declarada(s) en la portada"


COMPROBACIONES = [
    ("G1  no simula respuestas",      g1_no_simula_respuestas),
    ("G8  reglas donde se leen",      g8_reglas_donde_se_leen),
    ("G9  exposicion consultable",    g9_exposicion_consultable),
    ("G9  visuales sin red y citables", g9_visuales_sin_red_y_citables),
    ("G9  lo respondido queda escrito", g9_lo_respondido_queda_escrito),
    ("G12 dos prioridades",           g12_dos_prioridades),
    ("G14 el material es un curso",   g14_el_material_es_un_curso),
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

    print("Verificacion del contrato de Datito (spec.md)")
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
