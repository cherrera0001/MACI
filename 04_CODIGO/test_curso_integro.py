"""El curso completo sigue integro: cada regresion del 2026-09-27 tiene aqui su prueba.

python -m unittest discover -s 04_CODIGO -p "test_*.py"
"""
import os
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATITO = ROOT / "07_DATITO"
VISUAL = DATITO / "01_CONCEPTOS" / "visual"
BLOQUE = re.compile(r"<!-- datito:(nav|cierre|dudas):inicio -->.*?<!-- datito:\1:fin -->", re.S)
COMENTARIO = re.compile(r"<!--.*?-->", re.S)
RELLENO = re.compile(
    r"&#x27;titulo|\{'titulo'|importancia curricular None|peso en certamen \?|"
    r"Pregunta de inicio|Aplicación correcta del concepto")


def paginas_del_curso():
    base = [p for p in VISUAL.glob("*.html") if not p.name.startswith("_")]
    extra = list((DATITO / "04_EJERCICIOS").glob("*.html"))
    extra.append(DATITO / "02_REFERENCIA" / "clase6_regresion.html")
    return sorted(base) + sorted(extra)


def rotos(pagina, raiz=None):
    texto = pagina.read_text(encoding="utf-8")
    fallos = []
    for href in re.findall(r'(?:href|src)="([^"]*)"', texto):
        if not href or re.match(r"(https?:|mailto:|javascript:|data:)", href) or "${" in href:
            continue
        ruta, _, ancla = href.partition("#")
        destino = (pagina.parent / unquote(ruta)).resolve() if ruta else pagina
        if raiz and not str(destino).startswith(str(raiz)) or not destino.is_file():
            fallos.append(f"{pagina.name}: {href}")
        elif ancla and destino.suffix == ".html" and f'id="{ancla}"' not in destino.read_text(encoding="utf-8"):
            fallos.append(f"{pagina.name}: {href} (ancla)")
    return fallos


class CursoIntegro(unittest.TestCase):
    def test_enlaces_y_anclas_de_todas_las_paginas(self):
        self.assertEqual([], [f for p in paginas_del_curso() for f in rotos(p)])

    def test_sin_relleno_ni_bloques_atrapados(self):
        fallos = []
        for p in paginas_del_curso():
            t = p.read_text(encoding="utf-8")
            if RELLENO.search(t):
                fallos.append(f"{p.name}: relleno")
            for tipo in ("nav", "cierre", "dudas"):
                if t.count(f"datito:{tipo}:inicio") != t.count(f"datito:{tipo}:fin"):
                    fallos.append(f"{p.name}: marcadores {tipo} desbalanceados")
            sin_bloques = BLOQUE.sub("", t)
            if 'class="leccion-top"' in sin_bloques:
                fallos.append(f"{p.name}: encabezado de clase fuera de su bloque")
            vivo = COMENTARIO.sub("", t)
            if "TEMPLATE CANÓNICO DATITO" in vivo or "PROHIBIDO: CDN" in vivo:
                fallos.append(f"{p.name}: texto interno de la plantilla visible")
        self.assertEqual([], fallos)

    def test_plantilla_sin_bloques_generados(self):
        t = (VISUAL / "_TEMPLATE_CANONICO.html").read_text(encoding="utf-8")
        self.assertNotIn('class="dnav"', t)
        self.assertNotIn('class="leccion"', t)

    def test_viewport_en_todas_las_paginas(self):
        sin = [p.name for p in paginas_del_curso()
               if p.name != "index.html" and 'name="viewport"' not in p.read_text(encoding="utf-8")]
        self.assertEqual([], sin)

    def test_cada_clase_tiene_su_bloque_y_su_cierre(self):
        clases = yaml.safe_load((DATITO / "clases.yaml").read_text(encoding="utf-8"))["clases"]
        fallos = []
        for c in clases:
            if not c.get("visual"):
                continue
            t = (VISUAL / c["visual"].split("#")[0]).resolve().read_text(encoding="utf-8")
            if f'data-clase="{c["n"]}"' not in t:
                fallos.append(f"clase {c['n']} sin bloque")
            if (c.get("cierre") or {}).get("aprendiste") and f'id="cierre-clase-{c["n"]}"' not in t:
                fallos.append(f"clase {c['n']} sin cierre")
        self.assertEqual([], fallos)

    def test_cada_duda_esta_en_sus_visuales(self):
        dudas = yaml.safe_load((DATITO / "dudas.yaml").read_text(encoding="utf-8"))["dudas"]
        faltan = [f"{d['id']} en {v}" for d in dudas for v in d["visuales"]
                  if f'id="duda-{d["id"]}"' not in (VISUAL / v).resolve().read_text(encoding="utf-8")]
        self.assertEqual([], faltan)

    def test_una_sola_copia_de_cada_dato(self):
        dobles = [n for n in ("clases", "curriculum", "grafo", "dudas", "progreso", "errores_conceptuales")
                  if (DATITO / "00_INICIO" / f"{n}.yaml").exists()]
        self.assertEqual([], dobles)

    def test_el_generador_no_tiene_nada_pendiente(self):
        r = subprocess.run([sys.executable, str(ROOT / "03_SCRIPTS" / "construir_navegacion.py"), "--revisar"],
                           capture_output=True, text=True, encoding="utf-8",
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        self.assertEqual(0, r.returncode, r.stderr)
        pendientes = [l for l in r.stdout.splitlines()
                      if re.search(r"\b(actualizado|inyectado|cambiaria|actualizadas)\b", l)]
        self.assertEqual([], pendientes, "correr 03_SCRIPTS/construir_navegacion.py")

    @unittest.skipUnless(shutil.which("node"), "node no instalado")
    def test_el_sitio_publicado_no_tiene_enlaces_rotos(self):
        subprocess.run(["node", str(ROOT / "03_SCRIPTS" / "publicar_sitio.mjs")], check=True, capture_output=True)
        public = (ROOT / "public").resolve()
        paginas = [p for p in public.rglob("*.html")]
        self.assertGreater(len(paginas), 20)
        self.assertEqual([], [f for p in paginas for f in rotos(p, raiz=public)])
        privados = [p for p in ("datito.config.yaml", "progreso.yaml", "README.md", "_TEMPLATE_CANONICO.html")
                    if list(public.rglob(p))]
        self.assertEqual([], privados)


if __name__ == "__main__":
    unittest.main()
