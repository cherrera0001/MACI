"""Los documentos canónicos no mienten: comandos y enlaces existen (REQ-EST-003).

Leccion del proyecto (EVALUACION.md C2/C3): la documentacion de entrada describia
arboles y scripts que ya no existen, y un agente que la lee recibe un mapa falso.

Este test recorre los documentos canónicos y exige:
- que todo comando `python <ruta>.py` o `uv run ... <ruta>.py` cite un script
  que existe en el repo;
- que todo enlace Markdown local apunte a un archivo o directorio existente
  (se resuelve primero relativo a la raiz del repo y despues al directorio
  del documento);
- que ningun documento canonico cite rutas Windows legado `F:\\MACI`
  (el repo vive en Linux/WSL; las rutas deben ser relativas).

Los placeholders de plantilla (<ruta>, $ARGUMENTS), URLs, anclas, rutas de
home (~) y absolutas se ignoran: no son afirmaciones sobre este repo.
"""
import re
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

# documentos de ENTRADA vivos. EVALUACION.md y REPORTE-*.md son auditorias de
# fecha fija: citan rutas muertas como hallazgo, y eso es su contenido, no un
# enlace roto.
CANONICOS = [
    RAIZ / "README.md",
    *sorted((RAIZ / "00_INICIO").glob("*.md")),
]

COMANDO_SCRIPT = re.compile(
    r"(?:python3?|uv run[^`\"\n]*?|node|bash)\s+(?:-m\s+\S+\s+)?((?:03_SCRIPTS|04_CODIGO|07_DATITO|10_ARCHIVO|13_KAGGLE|14_INVESTIGACION|15_TERMINITO|docs|dist-src)/[^\s`'\"]+\.(?:py|sh|mjs|js))"
)
ENLACE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BACKTICK_RUTA = re.compile(r"`((?:[0-9A-Za-z_]{2,}/)+[^`\n]+\.(?:py|md|yaml|json|html|ipynb|csv|toml|txt))`")
WINDOWS_LEGADO = re.compile(r"F:\\\\MACI|F:/MACI|G:\\\\MACI|G:/MACI")

IGNORABLE = re.compile(r"^(?:https?://|mailto:|#|data:|javascript:|<|\{|\$|~|/|\.env)")


def _resolver(ruta_cruda, doc):
    destino = ruta_cruda.split("#")[0].strip().rstrip("/")
    if not destino or IGNORABLE.match(destino) or WINDOWS_LEGADO.search(destino):
        return None  # no es una afirmacion comprobable sobre este repo
    base = RAIZ if not destino.startswith(".") else doc.parent
    if "*" in destino:
        return None if list(base.glob(destino)) else destino  # glob sin coincidencias
    candidatos = [RAIZ / destino, doc.parent / destino]
    return None if any(c.exists() for c in candidatos) else destino


class DocumentosCanonicosTests(unittest.TestCase):
    def test_documentos_canonicos_existen(self):
        faltan = [str(d.relative_to(RAIZ)) for d in CANONICOS if not d.is_file()]
        self.assertEqual(faltan, [], "documento canonico ausente")

    def test_comandos_citan_scripts_existentes(self):
        rotos = []
        for doc in CANONICOS:
            texto = doc.read_text(encoding="utf-8", errors="replace")
            for m in COMANDO_SCRIPT.finditer(texto):
                script = RAIZ / m.group(1)
                if not script.is_file():
                    rotos.append(f"{doc.relative_to(RAIZ)}: {m.group(1)}")
        self.assertEqual(rotos, [], "comandos que citan scripts inexistentes")

    def test_enlaces_locales_existen(self):
        rotos = []
        for doc in CANONICOS:
            texto = doc.read_text(encoding="utf-8", errors="replace")
            for m in ENLACE.finditer(texto):
                destino = _resolver(m.group(1), doc)
                if destino:
                    rotos.append(f"{doc.relative_to(RAIZ)}: {destino}")
        self.assertEqual(rotos, [], "enlaces rotos en documentos canonicos")

    def test_rutas_en_backticks_existen(self):
        rotos = []
        for doc in CANONICOS:
            texto = doc.read_text(encoding="utf-8", errors="replace")
            for m in BACKTICK_RUTA.finditer(texto):
                destino = _resolver(m.group(1), doc)
                if destino:
                    rotos.append(f"{doc.relative_to(RAIZ)}: {destino}")
        self.assertEqual(rotos, [], "rutas entre backticks que no existen")

    def test_sin_rutas_windows_legado(self):
        citan = []
        for doc in CANONICOS:
            texto = doc.read_text(encoding="utf-8", errors="replace")
            for i, linea in enumerate(texto.splitlines(), 1):
                if WINDOWS_LEGADO.search(linea):
                    citan.append(f"{doc.relative_to(RAIZ)}:{i}")
        self.assertEqual(citan, [], "rutas Windows legado F:\\MACI en documentos canonicos")


if __name__ == "__main__":
    unittest.main()
