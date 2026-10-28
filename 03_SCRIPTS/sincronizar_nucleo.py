"""
Embebe el núcleo v2 (plantillas/nucleo_v2.css + nucleo_v2.js) en cada visual v2,
entre los marcadores datito:nucleo. Los visuales siguen autocontenidos: la copia
embebida es idéntica a la fuente (REQ-TUT-017).

USO
  python 03_SCRIPTS/sincronizar_nucleo.py            # reescribe los que difieren
  python 03_SCRIPTS/sincronizar_nucleo.py --revisar  # codigo 1 si alguno difiere
"""
import glob
from pathlib import Path
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLAS = os.path.join(RAIZ, "03_SCRIPTS", "plantillas")
VISUAL = os.path.join(RAIZ, "07_DATITO", "01_CONCEPTOS", "visual")
INI, FIN = "<!-- datito:nucleo:inicio -->", "<!-- datito:nucleo:fin -->"
MARCA_V2 = "<!-- datito:template:v2 -->"
BLOQUE = re.compile(re.escape(INI) + r".*?" + re.escape(FIN), re.S)


def bloque():
    css = Path(os.path.join(PLANTILLAS, "nucleo_v2.css")).read_text(encoding="utf-8").strip()
    js = Path(os.path.join(PLANTILLAS, "nucleo_v2.js")).read_text(encoding="utf-8").strip()
    return f'{INI}\n<style id="nucleo-datito-css">\n{css}\n</style>\n<script id="nucleo-datito">\n{js}\n</script>\n{FIN}'


def paginas_v2():
    return sorted(p for p in glob.glob(os.path.join(VISUAL, "*.html")) if MARCA_V2 in Path(p).read_text(encoding="utf-8"))


def desincronizadas():
    """[(ruta, motivo)] de las paginas v2 cuya copia no es la fuente."""
    esperado, malas = bloque(), []
    for p in paginas_v2():
        t = Path(p).read_text(encoding="utf-8")
        m = BLOQUE.findall(t)
        if len(m) != 1:
            malas.append((p, f"{len(m)} bloques datito:nucleo (debe haber 1)"))
        elif m[0] != esperado:
            malas.append((p, "nucleo distinto de 03_SCRIPTS/plantillas"))
    return malas


def main():
    revisar = "--revisar" in sys.argv
    malas = desincronizadas()
    if revisar:
        for p, motivo in malas:
            print(f"{os.path.basename(p)}: {motivo}")
        sys.exit(1 if malas else 0)
    esperado = bloque()
    for p, _ in malas:
        t = Path(p).read_text(encoding="utf-8")
        if INI in t:
            t = BLOQUE.sub(lambda _m: esperado, t, count=1)
        else:
            t = t.replace("</body>", esperado + "\n</body>", 1)
        Path(p).write_text(t, encoding="utf-8")
        print(f"  sincronizado {os.path.basename(p)}")
    print(f"{len(paginas_v2())} visuales v2 · {len(malas)} actualizados")


if __name__ == "__main__":
    main()
