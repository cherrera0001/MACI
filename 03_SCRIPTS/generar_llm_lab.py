"""
Rellena el corpus del laboratorio de LLM (20_llm.html, REQ-TUT-018) con un
bigrama contado sobre la clase del 21-ago, tramo de redes, atención y LLM.

  transcripción 2:11:41–2:46:54 -> palabras -> c(siguiente | anterior)
  se guardan las 10 siguientes más contadas de cada palabra con >= 3 apariciones

Determinista: misma transcripción, mismos datos.

USO
  python 03_SCRIPTS/generar_llm_lab.py            # escribe
  python 03_SCRIPTS/generar_llm_lab.py --revisar  # codigo 1 si el HTML no coincide
"""
import collections
import json
from pathlib import Path
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS = os.path.join(RAIZ, "05_CLASES", "transcripciones", "2026-08-21T22_13_35Z_Fundamentos_en_Ciencia_de_Datos.md")
PAGINA = os.path.join(RAIZ, "07_DATITO", "01_CONCEPTOS", "visual", "20_llm.html")
DESDE, HASTA = "2:11:41", "2:46:54"
MIN_APARICIONES, TOPE = 3, 10
MARCA = re.compile(r"\*\*\[(\d+:\d{2}:\d{2})\]\*\*\s*(.*)")
DATOS = re.compile(r"(/\* datito:llm:datos:inicio \*/).*?(/\* datito:llm:datos:fin \*/)", re.S)


def seg(t):
    h, m, s = (int(x) for x in t.split(":"))
    return h * 3600 + m * 60 + s


def corpus():
    lineas = [m.group(2) for m in (MARCA.match(l) for l in Path(TRANS).read_text(encoding="utf-8").splitlines()) if m
              and seg(DESDE) <= seg(m.group(1)) <= seg(HASTA)]
    palabras = re.findall(r"[a-záéíóúñü]+", " ".join(lineas).lower())
    pares = collections.Counter(zip(palabras, palabras[1:]))
    siguientes = collections.defaultdict(dict)
    for (a, b), n in pares.items():
        siguientes[a][b] = n
    bigramas = {a: dict(sorted(d.items(), key=lambda x: (-x[1], x[0]))[:TOPE])
                for a, d in sorted(siguientes.items()) if sum(d.values()) >= MIN_APARICIONES}
    frec = collections.Counter(palabras)
    return {"fuente": f"{os.path.basename(TRANS)} {DESDE}-{HASTA}", "palabras": len(palabras),
            "frecuencia": {w: frec[w] for w in bigramas}, "bigramas": bigramas}


def renderizar(t):
    datos = json.dumps(corpus(), ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return DATOS.sub(lambda m: m.group(1) + datos + m.group(2), t, count=1)


def main():
    t = Path(PAGINA).read_text(encoding="utf-8")
    if not DATOS.search(t):
        sys.exit("20_llm.html no tiene los marcadores datito:llm:datos")
    nuevo = renderizar(t)
    if "--revisar" in sys.argv:
        sys.exit(0 if nuevo == t else 1)
    if nuevo != t:
        Path(PAGINA).write_text(nuevo, encoding="utf-8")
    c = corpus()
    print(f"20_llm.html: {c['palabras']} palabras, {len(c['bigramas'])} con continuaciones")


if __name__ == "__main__":
    main()
