"""Visuales v2 (REQ-TUT-012…018): contrato del validador y modelo de juguete del lab de LLM."""
import json
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "03_SCRIPTS"))

import generar_llm_lab  # noqa: E402
import sincronizar_nucleo  # noqa: E402
from verificar_visuales import revisar_v2  # noqa: E402

LLM = RAIZ / "07_DATITO" / "01_CONCEPTOS" / "visual" / "20_llm.html"
NODE = shutil.which("node")


def pagina():
    return LLM.read_text(encoding="utf-8")


class ContratoV2Tests(unittest.TestCase):
    def setUp(self):
        self.t = pagina()
        self.nucleo = sincronizar_nucleo.bloque()

    def fallos(self, t):
        return revisar_v2("20_llm.html", t, self.nucleo)

    def test_lab_llm_cumple(self):
        self.assertEqual([], self.fallos(self.t))

    def test_todos_los_visuales_v2_cumplen(self):
        paginas = sincronizar_nucleo.paginas_v2()
        self.assertGreaterEqual(len(paginas), 2)  # 20_llm, 21_agentes
        for ruta in paginas:
            t = Path(ruta).read_text(encoding="utf-8")
            self.assertEqual([], revisar_v2(Path(ruta).name, t, self.nucleo), ruta)

    def test_v1_no_se_revisa(self):
        self.assertEqual([], revisar_v2("x.html", "<!-- datito:template:v1 --><details class=\"resp\">", self.nucleo))

    def test_respuesta_sin_intento(self):
        t = self.t.replace('<details class="resp" data-intento="q2">', '<details class="resp">', 1)
        self.assertTrue(any("sin data-intento" in f for f in self.fallos(t)))

    def test_respuesta_sin_caja_de_intento(self):
        t = self.t.replace('<div class="intento" data-intento="q2">', '<div class="intento" data-intento="otra">', 1)
        self.assertTrue(any("sin su caja de intento" in f for f in self.fallos(t)))

    def test_nivel_2_abierto(self):
        t = self.t.replace('data-nivel="2" id="n2-temp">', 'data-nivel="2" id="n2-temp" open>', 1)
        self.assertTrue(any("nivel 2 arranca abierto" in f for f in self.fallos(t)))

    def test_control_antes_de_predecir(self):
        t = self.t.replace('<h2 id="lab-siguiente">', '<input type="range" id="x"><h2 id="lab-siguiente">', 1)
        self.assertTrue(any("antes de la primera prediccion" in f for f in self.fallos(t)))

    def test_requiere_sin_prediccion(self):
        t = self.t.replace('data-requiere="p2"', 'data-requiere="p9"', 1)
        self.assertTrue(any('data-requiere="p9"' in f for f in self.fallos(t)))

    def test_sin_decision_ni_codigo(self):
        t = self.t.replace('id="decision"', 'id="d"').replace('id="codigo"', 'id="c"')
        f = self.fallos(t)
        self.assertTrue(any("#decision" in x for x in f) and any("#codigo" in x for x in f))

    def test_nucleo_editado_a_mano(self):
        t = self.t.replace("var MIN = 3;", "var MIN = 0;", 1)
        self.assertTrue(any("nucleo v2" in f for f in self.fallos(t)))

    def test_nucleo_sincronizado(self):
        self.assertEqual([], sincronizar_nucleo.desincronizadas())

    def test_corpus_regenerable(self):
        # misma transcripcion -> mismos datos embebidos
        self.assertEqual(self.t, generar_llm_lab.renderizar(self.t))


@unittest.skipUnless(NODE, "node no instalado")
class ModeloJugueteTests(unittest.TestCase):
    """Corre las funciones puras de <script id="llm-modelo"> en node."""

    @classmethod
    def setUpClass(cls):
        js = re.search(r'<script id="llm-modelo">(.*?)</script>', pagina(), re.S).group(1)
        prueba = js + r"""
var d = function (T, k) { return distribucion(CORPUS.bigramas["la"], T, k); };
var sig = CORPUS.bigramas["la"], tot = 0; for (var w in sig) tot += sig[w];
var PROF = [30, 30, 30, 10].concat([0.15, 0.15, 0.15, 0.15, 0.15]).map(Math.log);
console.log(JSON.stringify({
  ent: [0.3, 0.7, 1, 1.5, 2, 3].map(function (T) { return entropia(d(T, 0)); }),
  top: [0.3, 1, 2].map(function (T) { return d(T, 0)[0][1]; }),
  t1: d(1, 0).map(function (p) { return [p[0], p[1], sig[p[0]] / tot]; }),
  k3: d(1, 3).length, entk3: entropia(d(1, 3)), entTodas: entropia(d(1, 0)),
  gen1: generar("la", 12, 1, 0, 7).join(" "), gen2: generar("la", 12, 1, 0, 7).join(" "),
  frio: generar("la", 6, 0.05, 0, 3).join(" "), frio2: generar("la", 6, 0.05, 0, 99).join(" "),
  at: softmax(PROF, 1)
}));
"""
        r = subprocess.run([NODE, "-e", prueba], capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            raise AssertionError(r.stderr)
        cls.r = json.loads(r.stdout)

    def test_entropia_crece_con_la_temperatura(self):
        e = self.r["ent"]
        self.assertTrue(all(a < b for a, b in zip(e, e[1:])), e)

    def test_temperatura_baja_concentra(self):
        top = self.r["top"]
        self.assertGreater(top[0], top[1])
        self.assertGreater(top[1], top[2])

    def test_t1_reproduce_las_frecuencias(self):
        for w, p, f in self.r["t1"]:
            self.assertAlmostEqual(p, f, places=9, msg=w)

    def test_topk_recorta_y_baja_la_entropia(self):
        self.assertEqual(3, self.r["k3"])
        self.assertLess(self.r["entk3"], self.r["entTodas"])

    def test_generar_es_determinista_por_semilla(self):
        self.assertEqual(self.r["gen1"], self.r["gen2"])
        self.assertEqual(13, len(self.r["gen1"].split()))

    def test_casi_cero_elige_siempre_la_mas_contada(self):
        self.assertEqual(self.r["frio"], self.r["frio2"])

    def test_atencion_reproduce_al_profesor(self):
        at = self.r["at"]
        self.assertAlmostEqual(1.0, sum(at), places=9)
        for i, esperado in enumerate([0.30, 0.30, 0.30, 0.10]):
            self.assertAlmostEqual(esperado, at[i], delta=0.005)


if __name__ == "__main__":
    unittest.main()
