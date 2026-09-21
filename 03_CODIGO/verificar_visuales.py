"""
Verifica que los visuales de 07_DATITO/visual/ sirvan para estudiar sin
conexion y que sus citas de clase se puedan comprobar.

QUE COMPRUEBA
  sin red        ningun src/href a http(s):// o //, ni @import/url() remoto, ni fetch()
  enlaces        todo href local existe; si lleva #ancla, el id existe en el destino
  scripts        cada <script> pasa `node --check` (si node esta instalado)
  citas          toda ruta a 09_CLASES/transcripciones/ es un .md completo que
                 existe (nunca _plano.txt ni truncada con "…") y lleva cerca una
                 marca H:MM:SS que existe en esa transcripcion (+-20 s)
  fidelidad      en los bloques <div class="cita">, que las palabras citadas
                 esten en la transcripcion alrededor de la marca (aviso si no)
  navegacion     cada visual tiene el bloque generado y al menos un enlace
                 entrante desde otro visual
  etiquetas      los visuales de concepto usan etiquetas G4
  mapa           cada marca de 09_CLASES/mapa_ensenanza.yaml existe

Distingue FALLO (impide estudiar o citar) de AVISO (revisar a mano).

USO
  python 03_CODIGO/verificar_visuales.py
  python 03_CODIGO/verificar_visuales.py --detalle     # lista cada aviso
  python 03_CODIGO/verificar_visuales.py --estricto    # codigo 1 si hay fallos
"""
import argparse
import glob
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VISUAL = os.path.join(RAIZ, "07_DATITO", "visual")
TRANS_DIR = os.path.join(RAIZ, "09_CLASES", "transcripciones")

MARCA_MD = re.compile(r"\*\*\[(\d+:\d{2}:\d{2})\]\*\*\s*(.*)")
MARCA = re.compile(r"\b(\d:\d{2}:\d{2})\b")
RUTA_T = re.compile(r"09_CLASES/transcripciones/([^\s<>\"'\]\)·,;]+)")
TOL = 20  # segundos de tolerancia para una marca

_cache = {}


def seg(t):
    h, m, s = (int(x) for x in t.split(":"))
    return h * 3600 + m * 60 + s


def transcripcion(nombre):
    """[(segundo, texto)] de una transcripcion .md, con cache."""
    if nombre not in _cache:
        ruta = os.path.join(TRANS_DIR, nombre)
        if not os.path.exists(ruta):
            _cache[nombre] = None
        else:
            with open(ruta, encoding="utf-8", errors="replace") as f:
                _cache[nombre] = [(seg(m.group(1)), m.group(2)) for m in
                                  (MARCA_MD.match(l) for l in f) if m]
    return _cache[nombre]


def marca_existe(segs, t):
    s = seg(t)
    return any(abs(x - s) <= TOL for x, _ in segs)


def normal(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.findall(r"[a-z0-9ñ]+", t)


def texto_plano(fragmento):
    sin = re.sub(r"<script.*?</script>|<style.*?</style>", " ", fragmento, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", sin))


# --------------------------------------------------------------------------
def revisar(detalle=False):
    fallos, avisos = [], []
    archivos = sorted(glob.glob(os.path.join(VISUAL, "*.html")))
    nombres = {os.path.basename(a) for a in archivos}
    contenido = {os.path.basename(a): open(a, encoding="utf-8", errors="replace").read() for a in archivos}
    ids = {n: set(re.findall(r'\bid\s*=\s*["\']([^"\']+)["\']', t)) for n, t in contenido.items()}
    entrantes = {n: set() for n in nombres}
    node = shutil.which("node")
    n_citas = n_bloques = 0

    for n, t in contenido.items():
        sin_script = re.sub(r"<script.*?</script>", " ", t, flags=re.S)

        # --- sin red
        if re.search(r"""(?:src|href)\s*=\s*["']\s*(?:https?:)?//""", t, re.I) \
                or re.search(r"""url\(\s*["']?\s*(?:https?:)?//|@import""", t, re.I):
            fallos.append(f"{n}: referencia a un recurso remoto")
        if re.search(r"\bfetch\s*\(|XMLHttpRequest", t):
            fallos.append(f"{n}: usa fetch/XMLHttpRequest (no funciona desde file://)")

        # --- enlaces
        hrefs = re.findall(r'\bhref\s*=\s*"([^"]*)"', sin_script)
        hrefs += re.findall(r"""['"`]([a-z0-9_]+\.html(?:#[\w-]+)?)['"`]""", "".join(
            re.findall(r"<script.*?</script>", t, flags=re.S)))
        for h in hrefs:
            if not h or h.startswith(("#", "mailto:", "javascript:")) or "${" in h:
                if h.startswith("#") and len(h) > 1 and h[1:] not in ids[n]:
                    fallos.append(f"{n}: ancla interna rota {h}")
                continue
            ruta, _, ancla = h.partition("#")
            destino = os.path.normpath(os.path.join(VISUAL, unquote(ruta)))
            if not os.path.exists(destino):
                fallos.append(f"{n}: enlace roto {h}")
                continue
            base = os.path.basename(destino)
            if os.path.dirname(destino) == VISUAL and base in nombres:
                if base != n:
                    entrantes[base].add(n)
                if ancla and ancla not in ids.get(base, set()):
                    fallos.append(f"{n}: ancla rota {h}")

        # --- scripts
        if node:
            for i, js in enumerate(re.findall(r"<script[^>]*>(.*?)</script>", t, flags=re.S)):
                if not js.strip():
                    continue
                with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tmp:
                    tmp.write(js)
                r = subprocess.run([node, "--check", tmp.name], capture_output=True, text=True,
                                   encoding="utf-8", errors="replace")
                os.unlink(tmp.name)
                if r.returncode != 0:
                    linea = (r.stderr.strip().splitlines() or ["?"])
                    fallos.append(f"{n}: <script> #{i + 1} con error de sintaxis: {linea[-1][:120]}")

        # --- citas a transcripciones
        # El <footer> lista las fuentes consultadas (bibliografia): ahi se exige
        # la ruta completa pero no la marca. En el cuerpo, ruta y marca.
        for pie in re.findall(r"<footer.*?</footer>", t, flags=re.S):
            for m in RUTA_T.finditer(texto_plano(pie)):
                arch = m.group(1).rstrip(".")
                if "_plano.txt" in arch or "…" in arch or "..." in arch or not arch.endswith(".md"):
                    fallos.append(f"{n}: ruta de transcripcion incompleta en el pie: {arch}")
                elif transcripcion(arch) is None:
                    fallos.append(f"{n}: transcripcion inexistente en el pie: {arch}")
        plano = texto_plano(re.sub(r"<footer.*?</footer>", " ", t, flags=re.S))
        for m in RUTA_T.finditer(plano):
            n_citas += 1
            arch = m.group(1).rstrip(".")
            if "_plano.txt" in arch:
                fallos.append(f"{n}: cita un _plano.txt (sin marcas): {arch}")
                continue
            if "…" in arch or "..." in arch or not arch.endswith(".md"):
                fallos.append(f"{n}: ruta de transcripcion incompleta: {arch}")
                continue
            segs = transcripcion(arch)
            if segs is None:
                fallos.append(f"{n}: transcripcion inexistente: {arch}")
                continue
            ventana = plano[max(0, m.start() - 260): m.end() + 60]
            marcas = MARCA.findall(ventana)
            if not marcas:
                fallos.append(f"{n}: cita sin marca de tiempo: {arch}")
                continue
            malas = [x for x in marcas if not marca_existe(segs, x)]
            if len(malas) == len(marcas):
                fallos.append(f"{n}: marca(s) {', '.join(malas)} no existen en {arch}")

        # --- fidelidad de las citas en bloque
        for bloque in re.findall(r'<div class="cita"[^>]*>(.*?)</div>', t, flags=re.S):
            mr = RUTA_T.search(texto_plano(bloque))
            if not mr or not mr.group(1).endswith(".md"):
                continue
            segs = transcripcion(mr.group(1))
            partes = re.split(r'<span class="f"', bloque, maxsplit=1)
            cita = texto_plano(partes[0])
            cita = re.sub(r"⟨[^⟩]*⟩|\[[^\]]*\]", " ", cita)  # correcciones y etiquetas no cuentan
            marcas = MARCA.findall(texto_plano(partes[1]) if len(partes) > 1 else "")
            palabras = [w for w in normal(cita) if len(w) >= 4]
            if not segs or not marcas or len(palabras) < 3:
                continue
            n_bloques += 1
            ini, fin = seg(marcas[0]), seg(marcas[-1])
            ventana = " ".join(x for s, x in segs if ini - 30 <= s <= max(fin, ini + 45) + 30)
            vocab = set(normal(ventana))
            tasa = sum(w in vocab for w in palabras) / len(palabras)
            if tasa < 0.6:
                avisos.append(f"{n}: cita en {marcas[0]} coincide {tasa:.0%} con la transcripcion "
                              f"({mr.group(1)[:38]}…): «{' '.join(cita.split())[:70]}»")

        # --- navegacion y etiquetas
        if n != "index.html" and "<!-- datito:nav:inicio -->" not in t:
            fallos.append(f"{n}: falta el bloque de navegacion (correr construir_navegacion.py)")
        if n not in ("index.html",) and not re.search(r"\[(FUENTE|INFERENCIA|DATITO)", texto_plano(t)):
            avisos.append(f"{n}: sin ninguna etiqueta G4")

    for n in nombres:
        if n != "index.html" and not (entrantes[n] - {"index.html"}):
            avisos.append(f"{n}: ningun otro visual enlaza aqui (solo el indice)")

    # --- mapa de ensenanza
    try:
        import yaml
        mapa = yaml.safe_load(open(os.path.join(RAIZ, "09_CLASES", "mapa_ensenanza.yaml"), encoding="utf-8"))
        for cid, tramos in (mapa.get("conceptos") or {}).items():
            for tr in tramos:
                segs = transcripcion(tr["clase"] + ".md")
                if segs is None:
                    fallos.append(f"mapa_ensenanza: {cid}: no existe {tr['clase']}.md")
                    continue
                for k in ("inicio", "fin"):
                    if not marca_existe(segs, tr[k]):
                        fallos.append(f"mapa_ensenanza: {cid}: {tr[k]} no existe en {tr['clase'][:30]}…")
    except FileNotFoundError:
        avisos.append("no existe 09_CLASES/mapa_ensenanza.yaml")

    resumen = (f"{len(contenido)} visuales · {n_citas} citas a transcripciones · "
               f"{n_bloques} citas textuales comparadas · node {'si' if node else 'no'}")
    return fallos, avisos, resumen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detalle", action="store_true")
    ap.add_argument("--estricto", action="store_true")
    a = ap.parse_args()
    fallos, avisos, resumen = revisar()
    print("Verificacion de visuales (07_DATITO/visual/)")
    print("=" * 74)
    print(resumen)
    for f in fallos:
        print(f"[FALLO] {f}")
    if a.detalle:
        for x in avisos:
            print(f"[aviso] {x}")
    print("=" * 74)
    print(f"{len(fallos)} fallos · {len(avisos)} avisos"
          + ("" if a.detalle or not avisos else "  (--detalle para verlos)"))
    if fallos and a.estricto:
        sys.exit(1)


if __name__ == "__main__":
    main()
