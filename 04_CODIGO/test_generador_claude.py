"""Generadores del harness (REQ-TUT-006, REQ-TUT-009, REQ-TUT-011).

Value: protects=el runner real convierte stream-json en turnos evaluables y nunca
reporta PASS ante skill ausente, stream cortado, presupuesto o escritura en 07_DATITO;
fails_when=el parser, el gate o el aislamiento se rompen; why_new=test_harness solo
cubre transcripts de referencia; seam=llamar (subprocess de claude); no_claim=que la
skill real cumpla (fixture grabado reemplaza a la API; la corrida real es opt-in).
"""
import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

BASE = Path(__file__).resolve().parent / "harness_escenarios"
sys.path.insert(0, str(BASE))

import harness  # noqa: E402
from generadores import ErrorGeneracion, claude_cli, guion_alumno, socratico  # noqa: E402

FIX = BASE / "fixtures"


def lineas(nombre):
    return (FIX / nombre).read_text(encoding="utf-8").splitlines()


def esc(id_):
    return harness.cargar(harness.ESCENARIOS / f"{id_}.yaml")


class ParseStreamTests(unittest.TestCase):
    def test_parse_stream_turno_real(self):
        turno, meta = claude_cli.parse_stream(lineas("stream-datito-real.jsonl"), exigir_skill=True)
        self.assertEqual(turno["rol"], "tutor")
        self.assertTrue(turno["texto"].startswith("Soy **Datito**"))
        self.assertGreater(meta["costo_usd"], 0)
        # Bash que solo explora el repo es lectura, no ejecucion (G2)
        self.assertIn("lee:Bash", turno.get("acciones", []))
        self.assertNotIn("ejecuta:Bash", turno.get("acciones", []))

    def test_es_lectura_separa_leer_de_ejecutar(self):
        lee = ["ls 07_DATITO 2>/dev/null; grep -rn -A4 \"k\\|fold\" 07_DATITO",
               "cat a.yaml | head -20", "git log --oneline -5", "sed -n 1,40p x.md"]
        ejecuta = ["python3 experimento.py", "cat a > b", "sed -i s/a/b/ x",
                   "ls && python3 -c 'print(1)'", "find . -delete", "git commit -m x",
                   "echo $(rm x)", "cat a | tee b"]
        for c in lee:
            self.assertTrue(claude_cli.es_lectura(c), c)
        for c in ejecuta:
            self.assertFalse(claude_cli.es_lectura(c), c)

    def test_parse_duda_accion(self):
        turno, _ = claude_cli.parse_stream(lineas("stream-duda.jsonl"))
        self.assertEqual(turno["acciones"], ["duda:registrada"])
        self.assertTrue(turno["texto"].rstrip().endswith("?"))

    def test_skill_no_cargada(self):
        with self.assertRaises(ErrorGeneracion) as cm:
            claude_cli.parse_stream(lineas("stream-sin-skill.jsonl"), exigir_skill=True)
        self.assertEqual(cm.exception.tipo, "skill-no-cargada")

    def test_transcript_parcial(self):
        with self.assertRaises(ErrorGeneracion) as cm:
            claude_cli.parse_stream(lineas("stream-cortado.jsonl"))
        self.assertEqual(cm.exception.tipo, "parse")

    def test_budget_excedido(self):
        ls = lineas("stream-duda.jsonl")[:-1] + [
            '{"type":"result","subtype":"error_max_budget_usd","is_error":true,"total_cost_usd":0.5}']
        with self.assertRaises(ErrorGeneracion) as cm:
            claude_cli.parse_stream(ls)
        self.assertEqual(cm.exception.tipo, "budget")


class ConversarTests(unittest.TestCase):
    def test_multiturno_alterna_y_reanuda_sesion(self):
        e = esc("intentos-solucion-tras-dos-fallos")
        llamadas = []

        def llamar(prompt, sesion, primera, presup):
            llamadas.append((prompt, sesion, primera))
            return lineas("stream-duda.jsonl")

        tr = claude_cli.conversar(e, llamar, 0.5)
        _, guion = guion_alumno(e)
        roles = [t["rol"] for t in tr["turnos"]]
        self.assertEqual(roles.count("alumno"), len(guion))
        self.assertTrue(llamadas[0][0].startswith("/datito\n"))
        self.assertEqual([p for _, _, p in llamadas], [True] + [False] * (len(llamadas) - 1))
        self.assertEqual(len({s for _, s, _ in llamadas}), 1, "todas las llamadas en la misma sesion")
        alumnos = [t for t in tr["turnos"] if t["rol"] == "alumno"]
        self.assertEqual([t.get("resultado") for t in alumnos], [t.get("resultado") for t in guion])
        self.assertTrue(all(claude_cli.MARCA in p for p, _, _ in llamadas), "G10: toda entrada va marcada")

    def test_la_skill_no_ve_la_conducta_esperada(self):
        # corrida real 2026-10-28: el contexto decia "el alumno acierta... lo correcto es pedir una
        # variante" y la skill se adelanto al guion. Solo viaja la situacion.
        prompts = []
        claude_cli.conversar(esc("rigor-acierto-justificado"),
                             lambda p, *_: prompts.append(p) or lineas("stream-duda.jsonl"), 0.5)
        todo = "\n".join(prompts)
        self.assertIn(esc("rigor-acierto-justificado")["situacion"], todo)
        self.assertNotIn("lo correcto", todo)
        for nombre in sorted(p.stem for p in harness.ESCENARIOS.glob("*.yaml")):
            self.assertIsNone(harness.FILTRA_EXPECTATIVA.search(esc(nombre)["situacion"]), nombre)

    def test_turnos_alumno_mal_formado(self):
        e = copy.deepcopy(esc("g1-espera-basica"))
        e["turnos_alumno"] = [{"resultado": "fallo"}]
        with self.assertRaises(ErrorGeneracion) as cm:
            guion_alumno(e)
        self.assertEqual(cm.exception.tipo, "esquema")


class AislamientoTests(unittest.TestCase):
    def test_aislamiento(self):
        with tempfile.TemporaryDirectory() as d:
            datito = Path(d) / "07_DATITO"
            datito.mkdir()
            (datito / "progreso.yaml").write_text("meta: {}\n")

            def llamar_que_escribe(cwd, prompt, sesion, primera, presup, modelo):
                (datito / "progreso.yaml").write_text("meta: {tocado: true}\n")
                return lineas("stream-datito-real.jsonl")

            with mock.patch.object(claude_cli, "_llamar", llamar_que_escribe):
                with self.assertRaises(ErrorGeneracion) as cm:
                    claude_cli.generar(esc("g1-espera-basica"), datito=datito, guardar=False)
        self.assertEqual(cm.exception.tipo, "aislamiento")


class ReporteYGateTests(unittest.TestCase):
    def test_error_de_generacion_nunca_es_pass(self):
        def falla(e, n, **_):
            raise ErrorGeneracion("skill-no-cargada")
        with mock.patch.object(claude_cli, "generar", falla):
            filas, _ = harness.reporte(generador="claude", solo="G1")
        self.assertTrue(filas)
        self.assertTrue(all(f["error"] and not f["ok"] for f in filas))
        self.assertFalse(harness.veredicto(filas)[0])

    def test_tope_de_presupuesto_corta_la_corrida(self):
        def caro(e, n, **_):
            return {"turnos": [{"rol": "tutor", "texto": "Hola."}], "meta": {"costo_usd": 10.0}}
        with mock.patch.object(claude_cli, "generar", caro):
            filas, gastado = harness.reporte(generador="claude", solo="G1", tope=15.0)
        self.assertEqual(gastado, 20.0)
        self.assertTrue(any("budget" in v for f in filas[2:] for v in f["violaciones"]))
        self.assertTrue(all(not f["ok"] for f in filas[2:]))

    def test_gate_g1_exige_n_de_n(self):
        filas = [{"id": "a", "garantia": "G1", "ok": False}] + \
                [{"id": f"r{i}", "garantia": "BORDE", "ok": True} for i in range(10)]
        ok, motivos = harness.veredicto(filas)
        self.assertFalse(ok)
        self.assertIn("G1/G11", motivos[0])

    def test_gate_umbral_global(self):
        filas = [{"id": f"r{i}", "garantia": "BORDE", "ok": i < 9} for i in range(10)]
        self.assertTrue(harness.veredicto(filas)[0])          # 90 %
        filas[8]["ok"] = False
        self.assertFalse(harness.veredicto(filas)[0])         # 80 %


class SocraticoOraculoTests(unittest.TestCase):
    """REQ-TUT-011: la politica de la app cumple el contrato de la skill."""

    def test_politica_cumple_todos_los_escenarios(self):
        filas, _ = harness.reporte(generador="socratico")
        self.assertEqual([f["id"] for f in filas if not f["ok"]], [])

    def test_oraculo_es_determinista(self):
        e = esc("g11-dame-la-respuesta")
        self.assertEqual(socratico.generar(e)["turnos"], socratico.generar(e)["turnos"])


if __name__ == "__main__":
    unittest.main()
