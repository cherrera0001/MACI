"""
Construye la navegacion de visual/ sin editar HTML a mano.

QUE HACE
  1. En cada visual inyecta (o reemplaza) un bloque entre
         <!-- datito:nav:inicio -->  ...  <!-- datito:nav:fin -->
     justo despues de <main> (o de <body> si no hay main), con:
       - enlace al indice
       - de donde viene y que habilita cada concepto (grafo.yaml)
       - sus dos prioridades, y la tension si existe (G12)
       - las preguntas de certamen que entrena
       - DONDE SE ENSENO en clase: clase, rango, hablante y ruta completa de la
         transcripcion (05_CLASES/mapa_ensenanza.yaml)
  2. Renderiza las dudas resueltas de dudas.yaml en cada visual que
     listan, en orden cronologico y con la respuesta oculta, entre
         <!-- datito:dudas:inicio -->  ...  <!-- datito:dudas:fin -->
     (antes del <footer>). Asi nada de lo que Datito responde queda solo en la
     terminal (spec.md G9, REGLA UNO-B).
  3. Genera visual/index.html: ruta de repaso del certamen, dudas
     resueltas, distinciones (desde patron_evaluacion.md), cadenas y clases.

Es idempotente: correrlo dos veces deja el mismo resultado. Lo que esta fuera
de los marcadores no se toca.

POR QUE ASI
Cuando llega una transcripcion nueva basta con agregar sus tramos a
mapa_ensenanza.yaml y volver a correr esto: la trazabilidad y la navegacion de
los 20 visuales se actualizan solas. El contenido pedagogico de cada HTML se
sigue escribiendo a mano (o con /datito-visual), porque eso no es mecanizable.

USO
  python 03_SCRIPTS/construir_navegacion.py            # inyecta y genera
  python 03_SCRIPTS/construir_navegacion.py --revisar  # solo dice que cambiaria

MULTI-CURSO (ADR-001)
  Lee datito.config.yaml para resolver las rutas de course_id y learner_id.
  Sin config → backward compatibility: curso=fcd-2026-2, alumno=cristobal_herrera
"""
import argparse
import html
import os
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote

import yaml

RAIZ = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRANS = "05_CLASES/transcripciones"

INI, FIN = "<!-- datito:nav:inicio -->", "<!-- datito:nav:fin -->"
DINI, DFIN = "<!-- datito:dudas:inicio -->", "<!-- datito:dudas:fin -->"


def cargar_config():
    """Carga datito.config.yaml, con fallback para backward compatibility."""
    config_path = RAIZ / "07_DATITO" / "datito.config.yaml"
    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {"course_id": "fcd-2026-2", "learner_id": "cristobal_herrera"}


def resolver_rutas(config):
    """Resuelve las rutas del curso y alumno."""
    course_id = config.get("course_id", "fcd-2026-2")
    learner_id = config.get("learner_id", "cristobal_herrera")

    course_root = RAIZ / "courses" / course_id
    learner_root = RAIZ / "learners" / learner_id

    # Fallback para backward compatibility
    if not course_root.exists():
        course_root = RAIZ / "07_DATITO"
    if not learner_root.exists():
        learner_root = RAIZ / "07_DATITO"

    return {
        "course_root": course_root,
        "learner_root": learner_root,
        "visual": course_root / "visual",
        "dudas": learner_root / "dudas.yaml",
        "grafo": course_root / "grafo.yaml",
        "clases": course_root / "clases.yaml",
        "mapa_ensenanza": Path("05_CLASES") / "mapa_ensenanza.yaml",
    }


RUTAS = resolver_rutas(cargar_config())
# Fallback para visuales migrados en 01_CONCEPTOS/visual
VISUAL = str(RAIZ / "07_DATITO" / "01_CONCEPTOS" / "visual") if (RAIZ / "07_DATITO" / "01_CONCEPTOS" / "visual").exists() else str(RUTAS["visual"])
DUDAS = str(RUTAS["dudas"])
CLASES_YAML = str(RUTAS["clases"])
ESTADO_DUDA = {
    "resuelta": "resuelta en la sesión",
    "abierta": "quedó abierta en la sesión: aquí está la respuesta",
    "practica": "práctica: intenta antes de abrir la respuesta",
}

# --------------------------------------------------------------------------
# Catalogo: que visual cubre que concepto. Los conceptos que comparten un
# artefacto apuntan a su ancla.
VISUAL_DE = {
    "fundamentos_ciencia_datos": "01_fundamentos.html",
    "datos_features_target": "02_datos_features_target.html",
    "eda": "03_eda.html",
    "limpieza_preparacion": "04_limpieza_preparacion.html",
    "train_validation_test": "05_train_validation_test.html",
    "validacion_cruzada": "06_validacion_cruzada.html",
    "generalizacion": "07_generalizacion.html",
    "overfitting_underfitting": "08_overfitting_underfitting.html",
    "regresion": "09_regresion.html",
    "clasificacion": "10_clasificacion.html",
    "matriz_confusion": "11_matriz_confusion.html",
    "metricas_clasificacion": "12_metricas_clasificacion.html",
    "roc_auc": "13_roc_auc.html",
    "arboles_decision": "14_arboles_decision.html",
    "redes_neuronales": "18_redes_neuronales.html",
    "deep_learning": "19_deep_learning.html",
}

# Preguntas de certamen que entrena cada concepto. Fuente: patron_evaluacion.md
# (fichas del Certamen 2 y tabla del Certamen 1) y la nota de prioridad de
# grafo.yaml. (C, ancla)
CERTAMEN = {
    "fundamentos_ciencia_datos": [("C1", "p1"), ("C1", "p2"), ("C1", "p3"), ("C1", "p4"),
                                  ("C1", "p7"), ("C1", "p8"), ("C2", "p10"), ("C2", "p11")],
    "datos_features_target": [("C1", "p6"), ("C1", "p9a"), ("C2", "p3")],
    "eda": [("C1", "p9a"), ("C2", "p4"), ("C2", "p11")],
    "limpieza_preparacion": [("C1", "p9a"), ("C1", "p9b")],
    "train_validation_test": [("C2", "p2"), ("C2", "p7")],
    "validacion_cruzada": [("C2", "p3")],
    "generalizacion": [("C2", "p2"), ("C2", "p3"), ("C2", "p7")],
    "overfitting_underfitting": [("C2", "p2"), ("C2", "p3"), ("C2", "p7")],
    "regresion": [("C2", "p7")],
    "clasificacion": [("C1", "p6"), ("C2", "p4")],
    "matriz_confusion": [("C2", "p8")],
    "metricas_clasificacion": [("C2", "p4"), ("C2", "p8")],
    "roc_auc": [("C2", "p9")],
    "arboles_decision": [],
    "random_forest": [],
    "gradient_boosting": [],
    "ensembles": [("C2", "p1")],
    "redes_neuronales": [("C2", "p6")],
    "deep_learning": [("C2", "p6")],
    "llm": [("C2", "p5")],
    "agentes_ia": [("C2", "p5")],
}
CERT_ARCHIVO = {"C1": "certamen_1.html", "C2": "certamen_2.html"}

# Visuales que no son de un concepto, y los que cubren varios.
ESPECIALES = {
    "certamen_1.html": {"titulo": "Certamen 1 auditado", "conceptos": [
        "fundamentos_ciencia_datos", "datos_features_target", "limpieza_preparacion", "eda"],
        "rol": "certamen", "sesion": "05Certamen_Fundamentos_en_Ciencia_de_Datos_24_Julio",
        "rango": ("0:05:42", "0:22:34")},
    "certamen_2.html": {"titulo": "Certamen 2 auditado", "conceptos": [
        "overfitting_underfitting", "metricas_clasificacion", "matriz_confusion", "roc_auc",
        "ensembles", "llm", "agentes_ia", "redes_neuronales"],
        "rol": "certamen", "sesion": "2026-08-28T22_09_14Z_Fundamentos_en_Ciencia_de_Datos",
        "rango": ("0:11:54", "2:01:28")},
    "triaje_de_problemas.html": {"titulo": "Triaje de problemas", "conceptos": [], "rol": "herramienta"},
    "regresion_y_costo.html": {"titulo": "Función de costo, error y R²",
                               "conceptos": ["regresion"], "rol": "clase"},
}

# Orden de repaso para el certamen presencial (pedido del alumno, 2026-09-21).
RUTA_REPASO = [
    ("metricas_clasificacion", "Precisión, sensibilidad (recall), exactitud y F1: el denominador decide"),
    ("matriz_confusion", "Construir y leer la matriz; el ejercicio de 100 pacientes del profesor"),
    ("roc_auc", "Umbral, punto de operación, curva ROC y AUC: comparar modelos, no puntos"),
    ("train_validation_test", "Tres conjuntos: elegir con validación, medir con test"),
    ("validacion_cruzada", "Re-particionar para no depender de una partición con suerte"),
    ("generalizacion", "Funcionar en datos no vistos; interpolar y extrapolar"),
    ("overfitting_underfitting", "La brecha, no un número: sobreajuste, subajuste, error alto"),
    ("regresion", "Modelo lineal, costo, R²; el árbol y el radio del tronco"),
    ("limpieza_preparacion", "Calidad de datos: la 9B, centinelas, atípico ≠ error"),
    ("eda", "Distribución, resumen, faltantes y atípicos antes de modelar"),
]
TAMBIEN = ["fundamentos_ciencia_datos", "datos_features_target", "clasificacion",
           "arboles_decision", "redes_neuronales", "deep_learning"]

# --------------------------------------------------------------------------
# El curso (spec.md G14). El orden, la ficha Bloom y el cierre de cada clase
# viven en clases.yaml; aqui solo se derivan prerrequisitos,
# habilitaciones, tiempo de lectura y navegacion. LECCIONES se conserva por
# compatibilidad: (n, titulo, visual, objetivo, bloom, prerrequisitos).
BLOOM = ["Recordar", "Comprender", "Aplicar", "Analizar", "Evaluar", "Crear"]
CURSO = {"clases": [], "unidades": {}, "por_archivo": {}, "de_concepto": {}, "con_visual": []}
LECCIONES = []
CINI, CFIN = "<!-- datito:cierre:inicio -->", "<!-- datito:cierre:fin -->"


def minutos_de_lectura(archivo, partes):
    """~170 palabras por minuto sobre el texto visible, sin la navegacion."""
    ruta = os.path.join(VISUAL, archivo)
    if not os.path.exists(ruta):
        return None
    t = open(ruta, encoding="utf-8").read()
    t = re.sub(r"<!-- datito:(nav|cierre|dudas):inicio -->.*?<!-- datito:\1:fin -->", " ", t, flags=re.S)
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", t, flags=re.S)
    palabras = len(t.split()) / max(1, partes)
    return max(5, int(round(palabras / 170 / 5.0)) * 5)


def cargar_curso(grafo):
    data = cargar(CLASES_YAML)
    clases = sorted(data["clases"], key=lambda c: c["n"])
    CURSO["clases"] = clases
    CURSO["unidades"] = {int(k): v for k, v in data["unidades"].items()}
    por_archivo = {}
    for c in clases:
        if c.get("visual"):
            por_archivo.setdefault(c["visual"].split("#")[0], []).append(c)
    CURSO["por_archivo"] = por_archivo
    CURSO["con_visual"] = [c for c in clases if c.get("visual")]
    de = {}
    for c in clases:
        if c.get("tipo") == "concepto":
            for cid in c.get("conceptos", []):
                de.setdefault(cid, c["n"])
    CURSO["de_concepto"] = de
    g = grafo["conceptos"]
    for c in clases:
        pre, hab = set(), set()
        for cid in c.get("conceptos", []):
            if de.get(cid) and de[cid] < c["n"]:
                pre.add(de[cid])        # el mismo concepto se enseño antes
            for x in g.get(cid, {}).get("viene_de", []):
                if de.get(x) and de[x] < c["n"]:
                    pre.add(de[x])
            for x in g.get(cid, {}).get("habilita", []):
                if de.get(x) and de[x] > c["n"]:
                    hab.add(de[x])
        for otra in clases:  # una clase que repite un concepto de esta la necesita
            if otra["n"] > c["n"] and otra.get("tipo") == "concepto" and \
                    set(otra.get("conceptos", [])) & set(c.get("conceptos", [])):
                hab.add(otra["n"])
        c["_pre"], c["_hab"] = sorted(pre), sorted(hab)
        base = c["visual"].split("#")[0] if c.get("visual") else None
        c["_min"] = minutos_de_lectura(base, len(por_archivo.get(base, [1]))) if base else None
    for c in clases:
        if c.get("bloom", {}).get("nivel") not in BLOOM:
            sys.exit(f"clases.yaml: la clase {c['n']} tiene un nivel Bloom invalido")
    LECCIONES[:] = [(c["n"], c["titulo"], c.get("visual") or "", c["objetivo"], c["bloom"]["nivel"],
                     ", ".join(f"Clase {x}" for x in c["_pre"]) or "-") for c in clases]


def clase_n(n):
    return next((c for c in CURSO["clases"] if c["n"] == n), None)


def vecina(c, paso):
    """La clase anterior o siguiente CON visual (las pendientes se saltan)."""
    lista = CURSO["con_visual"]
    i = next((i for i, x in enumerate(lista) if x["n"] == c["n"]), None)
    if i is None:
        return None
    j = i + paso
    return lista[j] if 0 <= j < len(lista) else None


def enlace_clase(c, desde=None, forma="{t}"):
    if not c:
        return ""
    texto = f'Clase {c["n"]} · {esc(c["titulo"])}'
    if not c.get("visual"):
        return f'{texto} <span class="apagado">(pendiente)</span>'
    href = c["visual"]
    if desde and href.split("#")[0] == desde and "#" in href:
        href = "#" + href.split("#")[1]
    return f'<a href="{href}">{forma.replace("{t}", texto)}</a>'


def leccion_para(archivo):
    base = archivo.split("#", 1)[0]
    return next((l for l in LECCIONES if l[2].split("#", 1)[0] == base), None)


def lista_clases(nums, desde):
    return ", ".join(enlace_clase(clase_n(x), desde) for x in nums) or "ninguna"


def bloque_leccion(archivo, conceptos=()):
    """Encabezado de clase: numero, unidad, objetivo, prerrequisitos, habilita,
    tiempo, ficha Bloom, activacion, marca de avance y Anterior/Indice/Siguiente."""
    clases = CURSO["por_archivo"].get(archivo, [])
    if not clases:
        return ""
    total = len(CURSO["clases"])
    partes = []
    for c in clases:
        b = c["bloom"]
        minutos = f"~{c['_min']} min" if c.get("_min") else "—"
        compartida = ""
        if len(clases) > 1:
            compartida = (' <span class="apagado">(este archivo contiene las clases '
                          + " y ".join(str(x["n"]) for x in clases) + ")</span>")
        if c["_pre"]:
            pre = lista_clases(c["_pre"], archivo)
        elif c.get("tipo") == "repaso":
            pre = "las clases anteriores"
        else:
            pre = "ninguna: es el punto de partida"
        partes.append(
            f'<section class="leccion" data-clase="{c["n"]}" id="clase-{c["n"]}">\n'
            f'<div class="leccion-top"><span class="uni">Unidad {c["unidad"]} · '
            f'{esc(CURSO["unidades"][c["unidad"]])}</span><b>Clase {c["n"]} de {total}</b></div>\n'
            f'<div class="barra"><span style="width:{c["n"] / total * 100:.1f}%"></span></div>\n'
            f'<div class="lt">Clase {c["n"]} · {esc(c["titulo"])}{compartida}</div>\n'
            f'<p><b>Objetivo.</b> {esc(c["objetivo"])}</p>\n'
            f'<div class="fichas"><div><span class="et">prerrequisitos</span>{pre}</div>\n'
            f'<div><span class="et">habilita</span>{lista_clases(c["_hab"], archivo)}</div>\n'
            f'<div><span class="et">tiempo estimado</span>{minutos}</div></div>\n'
            f'<div class="ficha"><b>Ficha Bloom · {esc(b["nivel"])}</b><ul>\n'
            f'<li><b>Evidencia de aprendizaje:</b> {esc(b["evidencia"])}</li>\n'
            f'<li><b>Actividad final:</b> {esc(b["actividad_final"])}</li>\n'
            f'<li><b>Criterio de dominio:</b> {esc(b["criterio_dominio"])}</li></ul></div>\n'
            f'<div class="activ"><b>Activación.</b> {esc(c["activacion"])} '
            f'<span class="apagado">Escribe tu respuesta antes de seguir: la retomas en el cierre.</span></div>\n'
            f'<label class="hecha"><input type="checkbox" data-clase-hecha="{c["n"]}"> Terminé esta clase '
            f'<span class="apagado">(marca personal en este navegador; no es evidencia para Datito)</span></label>\n'
            f'</section>')
    ant, sig = vecina(clases[0], -1), vecina(clases[-1], +1)
    izq = enlace_clase(ant, archivo, "← {t}") if ant else '<span class="apagado">Inicio del curso</span>'
    der = enlace_clase(sig, archivo, "{t} →") if sig else '<span class="apagado">Fin del curso</span>'
    nav = (f'<nav class="pasos"><span>{izq}</span><a href="index.html">Índice del curso</a>'
           f'<span>{der}</span></nav>')
    js = ("<script>(function(){try{document.querySelectorAll('[data-clase-hecha]').forEach(function(c){"
          "var k='datito-clase-'+c.getAttribute('data-clase-hecha');c.checked=localStorage.getItem(k)==='1';"
          "c.addEventListener('change',function(){localStorage.setItem(k,c.checked?'1':'0');});});}"
          "catch(e){}})();</script>")
    return "\n".join(partes) + "\n" + nav + "\n" + js


CSS_CIERRE = (
    "<style>.dcierre{margin:2.4rem 0 1.2rem;padding:1.1rem 1.2rem;background:#f8fafc;border:2px solid #2563eb;"
    "border-radius:12px}.dcierre h2{margin-top:0;border:0;padding-top:0}.dcierre h3{font-size:1rem;margin:1rem 0 .3rem}"
    ".dcierre .c2{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}"
    ".dcierre .pf{background:#fff;border:1px dashed #d97706;border-radius:8px;padding:.7rem 1rem;margin:1rem 0}"
    ".dcierre details.resp{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:.6rem 1rem;margin:.6rem 0}"
    ".dcierre details.resp summary{cursor:pointer;font-weight:700;color:#065f46}"
    ".dcierre .continuar{display:inline-block;margin-top:.6rem;background:#2563eb;color:#fff;padding:.55rem 1.1rem;"
    "border-radius:8px;font-weight:700;text-decoration:none}.dcierre .apagado{color:#94a3b8}</style>"
)


def bloque_cierre(archivo):
    clases = [c for c in CURSO["por_archivo"].get(archivo, []) if (c.get("cierre") or {}).get("aprendiste")]
    if not clases:
        return None
    secs = []
    for c in clases:
        ci = c["cierre"]
        ant, sig = vecina(c, -1), vecina(c, +1)

        def lis(xs):
            return "".join(f"<li>{esc(x)}</li>" for x in xs)

        if sig:
            cont = (f'<a class="continuar" href="{sig["visual"]}">Continuar → Clase {sig["n"]} · '
                    f'{esc(sig["titulo"])}</a>')
        else:
            cont = '<a class="continuar" href="index.html">Volver al índice del curso</a>'
        secs.append(
            f'<section class="dcierre" id="cierre-clase-{c["n"]}">\n'
            f'<h2>Cierre de la Clase {c["n"]} · {esc(c["titulo"])}</h2>\n'
            f'<div class="c2"><div><h3>Qué aprendiste</h3><ul>{lis(ci["aprendiste"])}</ul></div>\n'
            f'<div><h3>Qué no debes confundir</h3><ul>{lis(ci["no_confundir"])}</ul></div></div>\n'
            f'<h3>Procedimiento para el papel</h3><ol>{lis(ci["procedimiento"])}</ol>\n'
            f'<p><b>Viene de:</b> {enlace_clase(ant) if ant else "el inicio del curso"} · '
            f'<b>Sigue:</b> {enlace_clase(sig) if sig else "el índice del curso"}</p>\n'
            f'<p><b>Vuelve a tu activación:</b> {esc(c["activacion"])} ¿Cambiarías tu respuesta?</p>\n'
            f'<div class="pf"><b>Pregunta final.</b> {esc(ci["pregunta_final"])}\n'
            f'<details class="resp"><summary>Respuesta correcta y cómo se resuelve</summary>'
            f'<p>{esc(ci["respuesta_final"])}</p>\n'
            f'<p class="apagado">El cierre es una síntesis de la clase [DATITO]: cada afirmación tiene su fuente '
            f'en el cuerpo de este visual. Fuente del cierre: <code>07_DATITO/clases.yaml</code>.</p></details></div>\n'
            f'{cont}\n</section>')
    return f"{CINI}\n{CSS_CIERRE}\n" + "\n".join(secs) + f"\n{CFIN}"


def inyectar_cierre(ruta, bloque, revisar):
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    patron_c = re.escape(CINI) + r".*?" + re.escape(CFIN)
    if CINI in t:
        nuevo = re.sub(patron_c, lambda _: bloque or "", t, count=1, flags=re.S)
    elif bloque:
        m = (re.search(re.escape(DINI), t) or re.search(r"<footer", t)
             or re.search(r"</main>", t) or re.search(r"</body>", t))
        if not m:
            return "sin lugar para el cierre"
        nuevo = t[:m.start()] + bloque + "\n" + t[m.start():]
    else:
        return "sin cierre"
    if nuevo == t:
        return "cierre sin cambios"
    if not revisar:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            f.write(nuevo)
    return "cierre actualizado"

MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
HABLA = {"titular": "profesor", "segundo_docente": "segundo docente",
         "ayudantia": "ayudantía", "alumnos": "alumnos", "invitado": "invitado"}

CSS_NAV = (
    "<style>.dnav{max-width:900px;margin:0 auto 1.4rem;font:14px/1.55 \"Segoe UI\",system-ui,sans-serif;"
    "background:#fff;border:1px solid #d8d8d8;border-radius:10px;padding:.7rem 1rem;color:#1a1a1a}"
    ".dnav a{color:#2563eb;text-decoration:none}.dnav a:hover{text-decoration:underline}"
    ".dnav .fila{margin:.18rem 0}.dnav .et{font-size:.7rem;font-weight:700;text-transform:uppercase;"
    "letter-spacing:.05em;color:#666;margin-right:.4rem}.dnav .ten{color:#7c3aed;font-weight:600}"
    ".dnav details{margin-top:.35rem}.dnav summary{cursor:pointer;font-weight:600}"
    ".dnav ul{margin:.4rem 0 .2rem 1.1rem;padding:0}.dnav li{margin:.25rem 0}"
    ".dnav .f{color:#666;font-size:.76rem;word-break:break-all}.dnav .ay{color:#92400e}"
    ".dnav .cpt{font-weight:700}.leccion{max-width:900px;margin:0 auto 1.2rem;padding:1rem;"
    "background:#eef6ff;border:1px solid #bfdbfe;border-radius:10px;font:14px/1.5 \"Segoe UI\",system-ui,sans-serif}"
    ".leccion-top,.pasos{display:flex;justify-content:space-between;gap:1rem;align-items:center}.leccion-top span{color:#475569}"
    ".barra{height:6px;background:#dbeafe;border-radius:8px;margin:.7rem 0}.barra span{display:block;height:100%;background:#2563eb;border-radius:8px}"
    ".ficha{padding:.6rem .8rem;background:#fff;border-left:3px solid #2563eb}.activacion{margin:.7rem 0;padding:.6rem .8rem;background:#fff7ed;border-left:3px solid #ea580c}"
    ".actividad{margin:.7rem 0;color:#334155}"
    ".lt{font-size:1.25rem;font-weight:700;margin:.2rem 0 .4rem}.uni{color:#475569}"
    ".fichas{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.4rem;margin:.5rem 0}"
    ".fichas .et{display:block;font-size:.68rem;font-weight:700;text-transform:uppercase;color:#64748b}"
    ".ficha ul{margin:.3rem 0 0 1.1rem;padding:0}.activ{margin:.7rem 0;padding:.6rem .8rem;background:#fffbeb;border-left:3px solid #d97706}"
    ".hecha{display:block;margin:.5rem 0;font-size:.85rem}"
    ".pasos{border-top:1px solid #bfdbfe;padding-top:.7rem}.pasos a{color:#1d4ed8}.apagado{color:#94a3b8}</style>"
)


# --------------------------------------------------------------------------
def cargar(ruta):
    with open(os.path.join(RAIZ, ruta), encoding="utf-8") as f:
        return yaml.safe_load(f)


def esc(t):
    return html.escape(str(t), quote=True)


def fecha_corta(iso):
    a, m, d = iso.split("-")
    return f"{int(d)}-{MESES[int(m) - 1]}"


def etiqueta_clase(meta, hablante):
    f = fecha_corta(meta["fecha"])
    tipo = meta["tipo"]
    if hablante == "ayudantia":
        return f"Ayudantía del {f}"
    if tipo == "certamen":
        return f"Sesión de certamen del {f}"
    if tipo == "presentaciones":
        return f"Presentaciones del {f}"
    return f"Clase del {f}"


def enlace_concepto(cid, desde, nombres):
    destino = VISUAL_DE.get(cid)
    nombre = esc(nombres.get(cid, cid))
    if not destino:
        return nombre
    archivo = destino.split("#")[0]
    if archivo == desde:
        ancla = destino.split("#")[1] if "#" in destino else ""
        return f'<a href="#{ancla}">{nombre}</a>' if ancla else f"<b>{nombre}</b>"
    return f'<a href="{destino}">{nombre}</a>'


def enlaces_certamen(pares):
    out = []
    for c, p in pares:
        out.append(f'<a href="{CERT_ARCHIVO[c]}#{p}">{c} {p.upper()}</a>')
    return " · ".join(out)


def li_tramo(t, clases):
    meta = clases[t["clase"]]
    ruta = f"{TRANS}/{t['clase']}.md"
    extra = ""
    if t["hablante"] == "ayudantia":
        extra += ' <span class="ay">· ayudantía: no entra al certamen</span>'
    if t.get("spoiler"):
        extra += (f' <span class="ay">· ⚠ resuelve el {esc(t["spoiler"])}: '
                  f'intenta antes su versión (vacío)</span>')
    return (f"<li><b>{esc(etiqueta_clase(meta, t['hablante']))}</b> · "
            f"{esc(t['inicio'])}–{esc(t['fin'])} · {esc(HABLA[t['hablante']])} — {esc(t['que'])}{extra}"
            f'<br><span class="f">[FUENTE · Repo: {esc(ruta)} · {esc(t["inicio"])}]</span></li>')


def bloque_nav(archivo, conceptos, grafo, nombres, mapa, especial=None):
    g = grafo["conceptos"]
    filas = ['<div class="fila"><a href="index.html">← Índice de repaso</a>'
             ' · <span class="et">Datito</span>sin conexión · citas con ruta y marca de tiempo</div>']
    if especial and especial["rol"] == "laboratorio":
        filas.append('<div class="fila"><span class="et">Laboratorio</span>'
                     'la clase completa está en <a href="clase6_regresion.html">clase6_regresion.html</a></div>')
    tramos_html = []
    for cid in conceptos:
        d = g[cid]
        nombre = esc(nombres.get(cid, cid))
        viene = ", ".join(enlace_concepto(c, archivo, nombres) for c in d.get("viene_de", [])) or "—"
        habil = ", ".join(enlace_concepto(c, archivo, nombres) for c in d.get("habilita", [])) or "—"
        pe = d.get("prioridad_evaluacion") or {}
        prio = (f'importancia curricular {d.get("importancia_curricular")} · '
                f'peso en certamen {esc(pe.get("peso", "?"))} ({esc(pe.get("nota", ""))})')
        if d.get("tension"):
            prio += ' · <span class="ten">tensión declarada (G12): las dos prioridades difieren</span>'
        cert = enlaces_certamen(CERTAMEN.get(cid, []))
        cabeza = enlace_concepto(cid, archivo, nombres) if len(conceptos) > 1 else f"<b>{nombre}</b>"
        filas.append(f'<div class="fila"><span class="cpt">{cabeza}</span> · '
                     f'<span class="et">viene de</span>{viene} · <span class="et">habilita</span>{habil}</div>')
        filas.append(f'<div class="fila"><span class="et">prioridad</span>{prio}'
                     + (f' · <span class="et">certamen</span>{cert}' if cert else "") + "</div>")
        for t in mapa["conceptos"].get(cid, []):
            li = li_tramo(t, mapa["clases"])
            if li not in tramos_html:
                tramos_html.append(li)
    if especial and especial.get("sesion"):
        s = especial["sesion"]
        meta = mapa["clases"][s]
        ini, fin = especial["rango"]
        filas.append(f'<div class="fila"><span class="et">sesión del certamen</span>'
                     f'{esc(etiqueta_clase(meta, "titular"))} · aclaraciones del profesor {ini}–{fin} · '
                     f'<span class="f">[FUENTE · Repo: {esc(TRANS)}/{esc(s)}.md · {ini}]</span></div>')
    if tramos_html:
        filas.append(f"<details><summary>Dónde se enseñó en clase ({len(tramos_html)} tramos)</summary>"
                     f"<ul>{''.join(tramos_html)}</ul></details>")
    leccion = bloque_leccion(archivo, conceptos)
    return (f"{INI}\n{CSS_NAV}\n{leccion}\n<nav class=\"dnav\" aria-label=\"Navegación de Datito\">\n"
            + "\n".join(filas) + f"\n</nav>\n{FIN}")


def inyectar(ruta, bloque, revisar):
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    if INI in t and FIN in t:
        nuevo = re.sub(re.escape(INI) + r".*?" + re.escape(FIN), lambda _: bloque, t, count=1, flags=re.S)
    else:
        m = re.search(r"<main[^>]*>", t) or re.search(r"<body[^>]*>", t)
        if not m:
            return "sin <main> ni <body>"
        nuevo = t[:m.end()] + "\n" + bloque + "\n" + t[m.end():]
    if nuevo == t:
        return "sin cambios"
    if not revisar:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            f.write(nuevo)
    return "actualizado" if INI in t else "inyectado"


# --------------------------------------------------------------------------
# Dudas resueltas: lo que Datito explico en una sesion queda en el visual.
CSS_DUDAS = (
    "<style>.ddudas{margin:2.4rem 0 1rem;padding-top:1.2rem;border-top:2px solid #059669}"
    ".ddudas h2{border:0;margin-top:0}.ddudas .duda{background:#fff;border:1px solid #d8d8d8;"
    "border-radius:10px;padding:.8rem 1.1rem;margin:1rem 0}.ddudas .dm{font-size:.78rem;color:#666}"
    ".ddudas .dr{background:#fffbeb;border-left:3px solid #d97706;padding:.5rem .8rem;font-size:.92rem}"
    ".ddudas details.resp{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;"
    "padding:.6rem 1rem;margin:.6rem 0 .2rem}.ddudas details.resp summary{cursor:pointer;"
    "font-weight:700;color:#065f46}.ddudas .df{font-size:.78rem;color:#666;word-break:break-word}"
    "</style>"
)


def cargar_dudas():
    ruta = os.path.join(RAIZ, DUDAS)
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as f:
        lista = (yaml.safe_load(f) or {}).get("dudas") or []
    # orden cronologico estable: por fecha, respetando el orden del archivo
    return [d for _, d in sorted(enumerate(lista), key=lambda x: (str(x[1]["fecha"]), x[0]))]


def articulo_duda(d, archivo, nombres):
    otros = [v for v in d["visuales"] if v != archivo]
    tambien = (" · también en " + ", ".join(f'<a href="{v}#duda-{esc(d["id"])}">{esc(v)}</a>' for v in otros)
               if otros else "")
    conceptos = ", ".join(enlace_concepto(c, archivo, nombres) for c in d.get("conceptos", []))
    respondio = (f'<p class="dr"><b>Lo que respondiste en la sesión:</b> {esc(d["respondio"])}</p>'
                 if d.get("respondio") else "")
    pasos = "".join(f"<li>{esc(p)}</li>" for p in d.get("resolucion", []))
    fuentes = "<br>".join(esc(x) for x in d.get("fuentes", []))
    return (f'<article class="duda" id="duda-{esc(d["id"])}">'
            f'<div class="dm">{esc(fecha_corta(str(d["fecha"])))} · {esc(ESTADO_DUDA.get(d["estado"], d["estado"]))}'
            f' · {conceptos}{tambien}</div>'
            f'<p><b>Pregunta.</b> {esc(d["pregunta"])}</p>{respondio}'
            f'<details class="resp"><summary>Respuesta correcta y cómo se resuelve</summary>'
            f'<p><b>Respuesta.</b> {esc(d["respuesta"])}</p><ol>{pasos}</ol>'
            f'<p><b>Error típico.</b> {esc(d.get("error_tipico", ""))}</p>'
            f'<p class="df">{fuentes}<br>Contexto de la sesión: <code>{esc(d.get("sesion", ""))}</code></p>'
            f"</details></article>")


def bloque_dudas(archivo, dudas, nombres):
    mias = [d for d in dudas if archivo in d.get("visuales", [])]
    if not mias:
        return None
    arts = "\n".join(articulo_duda(d, archivo, nombres) for d in mias)
    return (f"{DINI}\n{CSS_DUDAS}\n<section class=\"ddudas\" id=\"dudas-resueltas\">\n"
            f"<h2>Dudas resueltas con Datito, en orden</h2>\n"
            f"<p>Lo que se trabajó en las sesiones sobre este tema, para volver a leerlo y "
            f"re-intentarlo. Primero responde tú; después abre la respuesta. Fuente: "
            f"<code>07_DATITO/dudas.yaml</code>.</p>\n{arts}\n</section>\n{DFIN}")


def inyectar_dudas(ruta, bloque, revisar):
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    patron_bloque = re.escape(DINI) + r".*?" + re.escape(DFIN)
    if DINI in t:
        nuevo = re.sub(patron_bloque, lambda _: bloque or "", t, count=1, flags=re.S)
        if not bloque:
            nuevo = re.sub(r"\n{3,}", "\n\n", nuevo)
    elif bloque:
        m = (re.search(r"<footer", t) or re.search(r"</main>", t) or re.search(r"</body>", t))
        if not m:
            return "sin lugar para las dudas"
        nuevo = t[:m.start()] + bloque + "\n" + t[m.start():]
    else:
        return "sin dudas"
    if nuevo == t:
        return "dudas sin cambios"
    if not revisar:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            f.write(nuevo)
    return "dudas actualizadas"


# --------------------------------------------------------------------------
def distinciones():
    """Lee la tabla de §1 de patron_evaluacion.md: la fuente unica."""
    with open(os.path.join(RAIZ, "07_DATITO", "patron_evaluacion.md"), encoding="utf-8") as f:
        texto = f.read()
    return re.findall(r"^\| (P\d+) \| (.+?) \|\s*$", texto, flags=re.M)


DIST_VISUAL = {
    "P1": ["ensembles"], "P2": ["overfitting_underfitting", "generalizacion"],
    "P3": ["overfitting_underfitting", "datos_features_target", "validacion_cruzada"],
    "P4": ["clasificacion", "eda"], "P5": ["agentes_ia", "llm"],
    "P6": ["deep_learning", "redes_neuronales"], "P7": ["overfitting_underfitting", "regresion"],
    "P8": ["metricas_clasificacion", "matriz_confusion"], "P9": ["roc_auc"],
    "P10": ["fundamentos_ciencia_datos"], "P11": ["eda", "fundamentos_ciencia_datos"],
}
C1_ITEMS = [
    ("p1", "Campo interdisciplinario (V/F)", ["fundamentos_ciencia_datos"]),
    ("p2", "Organización data-driven (V/F)", ["fundamentos_ciencia_datos"]),
    ("p3", "Rol del líder y reclutamiento (V/F)", ["fundamentos_ciencia_datos"]),
    ("p4", "Ciclo de vida iterativo (V/F)", ["fundamentos_ciencia_datos"]),
    ("p5", "Webscraping (selección múltiple)", []),
    ("p6", "Tipo de problema / tipo de variable", ["datos_features_target", "clasificacion"]),
    ("p7", "Reclutamiento del equipo", ["fundamentos_ciencia_datos"]),
    ("p8", "Big Data: las V", ["fundamentos_ciencia_datos"]),
    ("p9a", "Desarrollo con tabla: estructura y calidad", ["datos_features_target", "limpieza_preparacion"]),
    ("p9b", "Desarrollo con tabla: consumo minero (2,0 pts)", ["limpieza_preparacion", "eda"]),
]


def indice(grafo, nombres, mapa, dudas=()):
    g = grafo["conceptos"]
    import yaml as _y
    try:
        prog = {c["id"]: c["estado"] for c in _y.safe_load(
            open(os.path.join(RAIZ, "07_DATITO", "progreso.yaml"), encoding="utf-8"))["conceptos"]}
    except (OSError, KeyError, TypeError):
        prog = {}
    orden_estado = ["NO_ESTUDIADO", "EN_ESTUDIO", "COMPRENSION_PARCIAL", "REQUIERE_REPASO",
                    "COMPRENDIDO", "DOMINADO"]
    unidades_html = []
    for u, nombre_u in sorted(CURSO["unidades"].items()):
        filas = []
        for c in [x for x in CURSO["clases"] if x["unidad"] == u]:
            estados = [prog.get(cid, "NO_ESTUDIADO") for cid in c.get("conceptos", [])]
            ev = min(estados, key=orden_estado.index) if estados else "—"
            pre = ", ".join(f"C{x}" for x in c["_pre"]) or ("anteriores" if c.get("tipo") == "repaso" else "—")
            titulo = enlace_clase(c)
            minutos = f"~{c['_min']} min" if c.get("_min") else "—"
            marca = (f'<span class="marca" data-marca="{c["n"]}"></span>' if c.get("visual")
                     else '<span class="apagado">pendiente</span>')
            filas.append(f'<tr><td class="num">{c["n"]}</td><td>{titulo}</td><td>{esc(c["bloom"]["nivel"])}</td>'
                         f'<td>{pre}</td><td>{minutos}</td><td><code>{esc(ev)}</code></td><td>{marca}</td></tr>')
        unidades_html.append(f'<h3>Unidad {u} · {esc(nombre_u)}</h3><table><tr><th>#</th><th>Clase</th>'
                             f'<th>Bloom</th><th>Requiere</th><th>Tiempo</th><th>Evidencia en Datito</th>'
                             f'<th>Tu marca</th></tr>{"".join(filas)}</table>')
    primera = CURSO["con_visual"][0] if CURSO["con_visual"] else None
    cubiertos = sorted(CURSO["de_concepto"].items(), key=lambda kv: kv[1])
    lista_cubiertos = ", ".join(f'{esc(nombres.get(cid, cid))} (C{n})' for cid, n in cubiertos)
    sin_clase = [cid for cid in nombres if cid not in CURSO["de_concepto"]]
    pendientes = [c for c in CURSO["clases"] if not c.get("visual")]
    txt_pend = ("; ".join(f'Clase {c["n"]} · {esc(c["titulo"])}' for c in pendientes)
                or "ninguna")
    usa = {}
    for cid, tramos in mapa["conceptos"].items():
        for tr in tramos:
            if cid in CURSO["de_concepto"]:
                usa.setdefault(tr["clase"], set()).add(CURSO["de_concepto"][cid])
    filas_dudas = []
    for d in dudas:
        principal = d["visuales"][0]
        preg = d["pregunta"] if len(d["pregunta"]) <= 170 else d["pregunta"][:167].rsplit(" ", 1)[0] + "…"
        filas_dudas.append(
            f"<tr><td>{esc(fecha_corta(str(d['fecha'])))}</td><td>{esc(preg)}</td>"
            f"<td>{esc(ESTADO_DUDA.get(d['estado'], d['estado']))}</td>"
            f'<td><a href="{principal}#duda-{esc(d["id"])}">{esc(principal)}</a></td></tr>')
    tabla_dudas = ("<table><tr><th>Fecha</th><th>Pregunta</th><th>Estado</th><th>Dónde está</th></tr>"
                   + "".join(filas_dudas) + "</table>") if filas_dudas else "<p>Todavía no hay dudas registradas.</p>"

    def fila_concepto(cid, nota=""):
        d = g[cid]
        pe = d.get("prioridad_evaluacion") or {}
        ten = ' <span class="ten">⚑ tensión</span>' if d.get("tension") else ""
        cert = enlaces_certamen(CERTAMEN.get(cid, [])) or "—"
        n = len(mapa["conceptos"].get(cid, []))
        return (f"<tr><td>{enlace_concepto(cid, 'index.html', nombres)}{ten}</td>"
                f"<td>{esc(nota)}</td><td class=\"num\">{d.get('importancia_curricular')}</td>"
                f"<td>{esc(pe.get('peso', '?'))}</td><td>{cert}</td><td class=\"num\">{n}</td></tr>")

    cab = ("<tr><th>Concepto</th><th>Qué te llevas</th><th>Importancia curricular</th>"
           "<th>Peso en certamen</th><th>Preguntas</th><th>Tramos de clase</th></tr>")
    ruta = "".join(fila_concepto(c, n) for c, n in RUTA_REPASO)
    tambien = "".join(fila_concepto(c) for c in TAMBIEN)

    filas_d = []
    for p, texto in distinciones():
        vis = ", ".join(enlace_concepto(c, "index.html", nombres) for c in DIST_VISUAL.get(p, [])) or "—"
        filas_d.append(f'<tr><td><a href="certamen_2.html#{p.lower()}">C2 {p}</a></td>'
                       f"<td>{esc(re.sub(r'[*]', '', texto))}</td><td>{vis}</td></tr>")
    for p, texto, cs in C1_ITEMS:
        vis = ", ".join(enlace_concepto(c, "index.html", nombres) for c in cs) or "solo en el certamen auditado"
        filas_d.append(f'<tr><td><a href="certamen_1.html#{p}">C1 {p.upper()}</a></td>'
                       f"<td>{esc(texto)}</td><td>{vis}</td></tr>")

    cadenas = []
    for nombre_cad, ids in grafo["cadenas"].items():
        pasos = " → ".join(enlace_concepto(c, "index.html", nombres) for c in ids)
        cadenas.append(f"<li><b>{esc(nombre_cad)}</b>: {pasos}</li>")

    filas_c = []
    for clave, meta in mapa["clases"].items():
        href = "../../" + quote(f"{TRANS}/{clave}.md")
        evaluable = "no (práctica)" if meta["tipo"] == "ayudantia" else (
            "sesión de certamen" if meta["tipo"] == "certamen" else "sí")
        en = ", ".join(enlace_clase(clase_n(x)) for x in sorted(usa.get(clave, []))) or "—"
        filas_c.append(f"<tr><td>{esc(fecha_corta(meta['fecha']))}</td><td>{esc(meta['tipo'])}</td>"
                       f"<td>{esc(meta['hablantes'])}</td><td>{evaluable}</td>"
                       f'<td><a href="{href}">{esc(clave)}.md</a></td><td>{en}</td></tr>')

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Fundamentos de Ciencia de Datos · el curso de Datito</title>
<style>
  :root{{--tinta:#1a1a1a;--suave:#666;--linea:#d8d8d8;--fondo:#faf9f7;--azul:#2563eb;--morado:#7c3aed;--ambar:#d97706}}
  *{{box-sizing:border-box}}
  body{{margin:0;padding:2rem 1rem;background:var(--fondo);color:var(--tinta);font:16px/1.65 "Segoe UI",system-ui,sans-serif}}
  main{{max-width:980px;margin:0 auto}}
  h1{{font-size:1.7rem;margin:0 0 .3rem}}
  h2{{font-size:1.2rem;margin:2.4rem 0 .7rem;padding-top:1.2rem;border-top:1px solid var(--linea)}}
  .sub{{color:var(--suave);margin:0 0 1.5rem}}
  a{{color:var(--azul);text-decoration:none}} a:hover{{text-decoration:underline}}
  table{{border-collapse:collapse;width:100%;font-size:.9rem;margin:.8rem 0}}
  th,td{{border:1px solid var(--linea);padding:.45rem .6rem;text-align:left;vertical-align:top}}
  th{{background:#f1f0ee;font-weight:600}} td.num{{text-align:right;font-variant-numeric:tabular-nums}}
  .ten{{color:var(--morado);font-weight:600;font-size:.82rem}}
  .nota{{background:#fffbeb;border-left:3px solid var(--ambar);padding:.8rem 1.1rem;margin:1rem 0;font-size:.94rem}}
  .clave{{background:#eff6ff;border-left:3px solid var(--azul);padding:.8rem 1.1rem;margin:1rem 0}}
  code{{background:#f1f0ee;padding:.1rem .35rem;border-radius:4px;font-size:.9em}}
  footer{{margin-top:3rem;color:var(--suave);font-size:.82rem;border-top:1px solid var(--linea);padding-top:1rem}}
  h3{{font-size:1rem;margin:1.4rem 0 .3rem}} .apagado{{color:#94a3b8}}
  .boton{{display:inline-block;background:var(--azul);color:#fff;padding:.7rem 1.3rem;border-radius:9px;font-weight:700;margin:.3rem .5rem .3rem 0}}
  .boton.alt{{background:#fff;color:var(--azul);border:2px solid var(--azul)}}
  .barra{{height:10px;background:#dbeafe;border-radius:8px;margin:.4rem 0}} .barra span{{display:block;height:100%;background:var(--azul);border-radius:8px;width:0}}
  @media (max-width:640px){{body{{padding:1rem .6rem}} table{{font-size:.8rem}} th,td{{padding:.3rem .35rem}}}}
</style>
</head>
<body>
<main>
<h1 id="curso">Fundamentos de Ciencia de Datos</h1>
<p class="sub">El curso de Datito · UdeC, T2-2026 · {len(CURSO["clases"])} clases en {len(CURSO["unidades"])} unidades · todo funciona sin conexión</p>

<p><b>Bienvenido.</b> Este es tu curso para el certamen presencial: las clases del profesor, ordenadas de
lo que necesitas primero a lo que se apoya en eso, con preguntas que intentas antes de ver la respuesta.</p>
<p><b>Propósito.</b> Que puedas resolver en papel, sin Internet, las preguntas que el profesor realmente hace:
distinguir conceptos vecinos, calcular a mano e interpretar el resultado
[FUENTE · Repo: 07_DATITO/patron_evaluacion.md].</p>

<p>{('<a class="boton" href="' + primera["visual"] + '">Comenzar la Clase 1 →</a>') if primera else ""}
<a class="boton alt" id="seguir" href="#curso-clases">Seguir donde quedé</a>
<a class="boton alt" href="#repaso">Repaso del certamen</a>
<a class="boton alt" href="#dudas">Dudas resueltas</a></p>
<p>Tu avance (marcas de «Terminé esta clase» en este navegador): <b id="avance">0</b> de
{len(CURSO["con_visual"])} clases disponibles.</p>
<div class="barra"><span id="barra"></span></div>

<div class="clave"><b>Cómo usarlo.</b> Abre este archivo con doble clic: no necesita Internet.
En cada visual, <b>predice antes de mover</b> un control, resuelve los ejercicios <b>antes</b> de abrir
las soluciones (<code>&lt;details&gt;</code>) y termina con la tarea de producción: explícaselo a Datito.
Leer sin responder no es estudiar.</div>

<h2 id="curso-clases">0 · El curso, clase por clase</h2>
<p>El orden sigue los prerrequisitos del currículum y la secuencia real de las clases del profesor, y sube de
comprender a aplicar, analizar, evaluar y crear [FUENTE · Repo: 07_DATITO/clases.yaml]. Cada clase abre con
su objetivo, su ficha Bloom y una pregunta de activación, y cierra con qué aprendiste, qué no confundir, un
procedimiento y una pregunta final. «Requiere» son las clases que conviene tener antes; «Evidencia en Datito»
es el estado registrado en <code>progreso.yaml</code> al generar esta página.</p>
{"".join(unidades_html)}
<p><b>Conceptos cubiertos ({len(cubiertos)} de {len(nombres)}):</b> {lista_cubiertos}.</p>
<p><b>Conceptos sin clase:</b> {(", ".join(esc(nombres[c]) for c in sin_clase)) or "ninguno"}.
<b>Clases pendientes de construir:</b> {txt_pend}.</p>

<h2 id="repaso">1 · Repaso recomendado antes del certamen</h2>
<p>El orden sigue tu pedido de repaso. El peso en el certamen viene de
<a href="../patron_evaluacion.md">patron_evaluacion.md</a>: sobreajuste, generalización y validación suman el
36 % del Certamen 2 y las métricas de clasificación otro 27 % [FUENTE · Repo: 07_DATITO/patron_evaluacion.md].
Cuando la importancia curricular y el peso en el certamen difieren, se marca ⚑ (G12): lo que menos se pregunta
puede ser lo que más sostiene al resto.</p>
<table>{cab}{ruta}</table>
<p>También conviene repasar:</p>
<table>{cab}{tambien}</table>

<h2 id="dudas">2 · Dudas resueltas por Datito, en orden</h2>
<p>Todo lo que se resolvió en una sesión queda aquí y en el visual del tema, con la respuesta
correcta y cómo se resuelve (oculta hasta que la abras). Nada queda solo en la terminal.
Fuente única: <a href="../dudas.yaml">07_DATITO/dudas.yaml</a>.</p>
{tabla_dudas}

<h2>2b · Distinciones que deciden el certamen</h2>
<p>Cada pregunta real se resuelve separando dos conceptos vecinos. No evalúa definiciones: evalúa
discriminación [FUENTE · Repo: 07_DATITO/patron_evaluacion.md §1].</p>
<table><tr><th>Pregunta</th><th>La distinción</th><th>Dónde se entrena</th></tr>{''.join(filas_d)}</table>
<div class="nota">Los enunciados del Certamen 1 vienen de un compañero: son fiables; sus respuestas no están
verificadas. El profesor dijo que cada certamen se arma desde un «pool de preguntas», así que tu versión puede
diferir [FUENTE · Repo: {TRANS}/05Certamen_Fundamentos_en_Ciencia_de_Datos_24_Julio.md · 0:05:48].</div>

<h2>3 · Mapa por cadenas del currículum</h2>
<p>De <a href="../grafo.yaml">grafo.yaml</a>: cada cadena es un camino de prerrequisitos.</p>
<ul>{''.join(cadenas)}</ul>
<p>Herramientas: <a href="triaje_de_problemas.html">triaje de problemas</a> (¿qué tipo de problema tengo?) ·
<a href="regresion_y_costo.html">laboratorio de la función de costo</a> ·
<a href="certamen_1.html">Certamen 1 auditado</a> · <a href="certamen_2.html">Certamen 2 auditado</a> ·
guía escrita <a href="../guias/overfitting_underfitting.md">overfitting_underfitting.md</a> ·
cuadernillo <a href="../cuadernillos/01_sobreajuste_y_calidad_de_datos.md">01_sobreajuste_y_calidad_de_datos.md</a>.</p>

<h2>4 · Clases transcritas</h2>
<p>La fuente citable de cada visual. Las transcripciones son automáticas y pueden errar en números y términos:
el material oficial del curso manda. El profesor fue explícito sobre qué entra al certamen:
«Entran solo mis clases. No entran las clases de Alejandra.»
[FUENTE · Repo: {TRANS}/03Clase_Recuperación_Fundamentos_en_Ciencia_de_Datos_15_julio.md · 1:18:16].</p>
<table><tr><th>Fecha</th><th>Tipo</th><th>Quién habla</th><th>¿Entra al certamen?</th><th>Transcripción</th><th>Se usa en</th></tr>{''.join(filas_c)}</table>

<h2>5 · Cómo leer las etiquetas</h2>
<table>
<tr><td><code>[FUENTE · Repo: ruta · marca]</code></td><td>Sale de un archivo del repositorio: lámina, práctico, transcripción (con marca de tiempo) o resultados.</td></tr>
<tr><td><code>[INFERENCIA]</code></td><td>Se deriva de las fuentes, pero no está escrito en ninguna.</td></tr>
<tr><td><code>[DATITO]</code></td><td>Explicación, analogía o cifra ilustrativa del tutor. Útil, pero no es del profesor.</td></tr>
<tr><td><code>⟨ ⟩</code></td><td>Corrección de un error de la transcripción automática dentro de una cita.</td></tr>
<tr><td><code>⚠</code></td><td>Cifra o término que la transcripción pudo alterar: contrastar con la lámina.</td></tr>
</table>

<script>(function(){{try{{var n=0,total=0,seguir=null;
document.querySelectorAll('[data-marca]').forEach(function(s){{total++;var k=s.getAttribute('data-marca');
var h=localStorage.getItem('datito-clase-'+k)==='1';s.textContent=h?'✓ terminada':'';if(h)n++;
else if(!seguir){{var a=s.closest('tr').querySelector('a');if(a)seguir=a.getAttribute('href');}}}});
document.getElementById('avance').textContent=n;
document.getElementById('barra').style.width=(total?Math.round(100*n/total):0)+'%';
if(seguir)document.getElementById('seguir').setAttribute('href',seguir);}}catch(e){{}}}})();</script>

<footer>Generado por <code>03_SCRIPTS/construir_navegacion.py</code> el {date.today().isoformat()} desde
<code>07_DATITO/clases.yaml</code>, <code>07_DATITO/grafo.yaml</code>, <code>07_DATITO/curriculum.yaml</code>, <code>07_DATITO/patron_evaluacion.md</code>
y <code>05_CLASES/mapa_ensenanza.yaml</code>. No editar a mano. Funciona sin conexión.</footer>
</main>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true", help="no escribe; dice que cambiaria")
    a = ap.parse_args()

    grafo = cargar(str(RUTAS["grafo"].relative_to(RAIZ)))
    cur = cargar(str((RUTAS["course_root"] / "curriculum.yaml").relative_to(RAIZ)))
    mapa = cargar("05_CLASES/mapa_ensenanza.yaml")
    nombres = {c["id"]: c["nombre"] for c in cur["conceptos"]}

    dudas = cargar_dudas()
    cargar_curso(grafo)
    for c in CURSO["clases"]:
        if c.get("visual"):
            base, _, ancla = c["visual"].partition("#")
            if not os.path.exists(os.path.join(VISUAL, base)):
                sys.exit(f"clases.yaml: la clase {c['n']} apunta a un visual inexistente: {base}")
    faltan = [c for c in VISUAL_DE if c not in grafo["conceptos"]]
    if faltan:
        sys.exit(f"conceptos del catalogo ausentes de grafo.yaml: {faltan}")
    for d in dudas:
        for campo in ("id", "fecha", "visuales", "estado", "pregunta", "respuesta", "resolucion", "fuentes"):
            if not d.get(campo):
                sys.exit(f"dudas.yaml: la duda {d.get('id', '?')} no tiene '{campo}'")
        for v in d["visuales"]:
            if not os.path.exists(os.path.join(VISUAL, v)):
                sys.exit(f"dudas.yaml: {d['id']} apunta a un visual inexistente: {v}")
    for cid, tramos in mapa["conceptos"].items():
        for t in tramos:
            if t["clase"] not in mapa["clases"]:
                sys.exit(f"{cid}: clase desconocida {t['clase']}")

    # visual -> conceptos que cubre
    cubre = {}
    for cid, destino in VISUAL_DE.items():
        cubre.setdefault(destino.split("#")[0], []).append(cid)

    archivos = sorted(f for f in os.listdir(VISUAL) if f.endswith(".html") and f != "index.html")
    for f in archivos:
        esp = ESPECIALES.get(f)
        conceptos = esp["conceptos"] if esp else cubre.get(f, [])
        if not esp and not conceptos:
            print(f"  {f:34} sin concepto en el catalogo: solo enlace al indice")
        bloque = bloque_nav(f, conceptos if not (esp and esp["rol"] == "certamen") else [],
                            grafo, nombres, mapa, esp)
        if esp and esp["rol"] == "certamen":
            # los certamenes enlazan los conceptos que evaluan, sin repetir tramos
            links = " · ".join(enlace_concepto(c, f, nombres) for c in esp["conceptos"])
            bloque = bloque.replace("</nav>", f'<div class="fila"><span class="et">conceptos</span>{links}</div>\n</nav>')
        estado = inyectar(os.path.join(VISUAL, f), bloque, a.revisar)
        estado_c = inyectar_cierre(os.path.join(VISUAL, f), bloque_cierre(f), a.revisar)
        estado_d = inyectar_dudas(os.path.join(VISUAL, f), bloque_dudas(f, dudas, nombres), a.revisar)
        print(f"  {f:34} {estado} · {estado_c} · {estado_d}")

    ruta_idx = os.path.join(VISUAL, "index.html")
    contenido = indice(grafo, nombres, mapa, dudas)
    previo = open(ruta_idx, encoding="utf-8").read() if os.path.exists(ruta_idx) else ""
    # la fecha del pie no cuenta como cambio
    iguales = re.sub(r"el \d{4}-\d{2}-\d{2}", "", previo) == re.sub(r"el \d{4}-\d{2}-\d{2}", "", contenido)
    if not iguales and not a.revisar:
        with open(ruta_idx, "w", encoding="utf-8", newline="\n") as f:
            f.write(contenido)
    print(f"  {'index.html':34} {'sin cambios' if iguales else ('cambiaria' if a.revisar else 'generado')}")


if __name__ == "__main__":
    main()
