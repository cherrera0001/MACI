"""La memoria del Agents Learning Loop se puede leer como dice program_loop.md.

program_loop.md manda leer `failure_patterns` primero. Si una lección de fallo
queda archivada bajo `keep_patterns`, el agente que sigue el protocolo no la ve.
"""
import csv
import os
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LOOP = ROOT / "07_DATITO" / "07_BITACORA" / "learning_loop"
LECCIONES = LOOP / "agent_lessons.yaml"
RESULTADOS = LOOP / "results.tsv"
SKILLS = ROOT / ".claude" / "skills"
MARCA = {"failure_patterns": "-FAIL-", "keep_patterns": "-KEEP-"}
CORTE_LECCIONES = date(2026, 10, 1)  # T-4.2.2: lecciones 011–015 (2026-09-27) quedan exentas
LOOP_ONCE = ROOT / "04_CODIGO" / "datito_loop_once.py"
TEMPLATE = ROOT / "07_DATITO" / "01_CONCEPTOS" / "visual" / "_TEMPLATE_CANONICO.html"


def lecciones():
    return yaml.safe_load(LECCIONES.read_text(encoding="utf-8"))


class TestLearningLoop(unittest.TestCase):
    def test_cada_leccion_esta_en_su_lista(self):
        datos = lecciones()
        fuera = [f"{l['id']} en {lista}" for lista, marca in MARCA.items()
                 for l in datos[lista] if marca not in l["id"]]
        self.assertEqual(fuera, [], "lecciones archivadas en la lista equivocada")

    def test_ids_unicos(self):
        datos = lecciones()
        ids = [l["id"] for lista in MARCA for l in datos[lista]]
        repetidos = sorted({i for i in ids if ids.count(i) > 1})
        self.assertEqual(repetidos, [])

    def test_cada_fila_de_resultados_cita_una_leccion_que_existe(self):
        datos = lecciones()
        ids = {l["id"] for lista in MARCA for l in datos[lista]}
        with RESULTADOS.open(encoding="utf-8", newline="") as f:
            filas = [r for r in csv.DictReader(f, delimiter="\t") if not r["ts"].startswith("#")]
        huerfanas = sorted({r["lesson_id"] for r in filas if r["lesson_id"] not in ids})
        self.assertEqual(huerfanas, [])

    # D-4.4: el espejo .agents/skills dejo de versionarse (queda en disco,
    # ignorado por git). Este test se elimino con esa decision: vigilar un
    # espejo que git ya no conoce es trabajo de configuracion local, no del
    # contrato del repo.


class TestLessonIdObligatorio(unittest.TestCase):
    """T-4.2.1: sin ids por defecto; registrar exige --lesson-id."""

    def test_funcion_exige_id(self):
        sys.path.insert(0, str(ROOT / "04_CODIGO"))
        try:
            from datito_loop_once import lesson_id_o_error
        finally:
            sys.path.remove(str(ROOT / "04_CODIGO"))
        with self.assertRaises(SystemExit):
            lesson_id_o_error("")
        self.assertEqual(lesson_id_o_error("VIZ-KEEP-001"), "VIZ-KEEP-001")

    def test_sin_lesson_id_no_registra(self):
        antes = RESULTADOS.read_bytes()
        r = subprocess.run(
            [sys.executable, str(LOOP_ONCE), "--path", str(TEMPLATE),
             "--hypothesis", "test T-4.2.1 sin id"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn("--lesson-id es obligatorio", r.stderr)
        self.assertEqual(RESULTADOS.read_bytes(), antes, "no se tocó results.tsv")

    def test_con_lesson_id_registra(self):
        """T-4.2.1 + T-8.4.1: registra fila y traza en un loop aislado (tmp)."""
        import shutil
        import tempfile
        antes = RESULTADOS.read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_loop = Path(tmp)
            shutil.copy2(LECCIONES, tmp_loop / "agent_lessons.yaml")
            env = {**os.environ, "DATITO_LOOP_DIR": str(tmp_loop)}
            r = subprocess.run(
                [sys.executable, str(LOOP_ONCE), "--path", str(TEMPLATE),
                 "--hypothesis", "test T-4.2.1 con id", "--lesson-id", "VIZ-KEEP-001"],
                capture_output=True, text=True, encoding="utf-8", env=env,
            )
            self.assertIn(r.returncode, (0, 1), r.stderr + r.stdout)
            ultima = (tmp_loop / "results.tsv").read_text(encoding="utf-8").splitlines()[-1]
            self.assertIn("VIZ-KEEP-001", ultima)
            # T-8.4.1: la traza quedó adjunta a la lección (en el loop aislado)
            self.assertTrue((tmp_loop / "trazas" / "VIZ-KEEP-001.json").exists())
            self.assertIn('traza: "trazas/VIZ-KEEP-001.json"',
                          (tmp_loop / "agent_lessons.yaml").read_text(encoding="utf-8"))
        self.assertEqual(RESULTADOS.read_bytes(), antes,
                         "no se tocó results.tsv real")


class TestGateContrato(unittest.TestCase):
    """T-4.3.1: el gate parsea contrato_conocimiento.yaml y solo aplica a los targets con contrato."""

    def _importar(self):
        sys.path.insert(0, str(ROOT / "04_CODIGO"))
        try:
            import datito_loop_once as m
        finally:
            sys.path.remove(str(ROOT / "04_CODIGO"))
        return m

    def test_sin_contrato_gate_no_aplica(self):
        m = self._importar()
        self.assertIsNone(m.contrato_de(TEMPLATE))
        self.assertIsNone(m.gate_contrato(TEMPLATE))

    def test_contrato_de_clase_08(self):
        m = self._importar()
        contrato = m.contrato_de(ROOT / "07_DATITO/01_CONCEPTOS/visual/08_overfitting_underfitting.html")
        self.assertIsNotNone(contrato)
        self.assertEqual(contrato["control"], "grado")
        self.assertEqual(contrato["selector"], "#m-lec")
        self.assertTrue(any("Sobreajuste" in e for e in contrato["esperados"]))
        self.assertTrue(any("Subajuste" in e for e in contrato["esperados"]))


class TestLeccionesRecientesConFila(unittest.TestCase):
    """T-4.2.2: toda lección fechada después del 2026-10-01 tiene ≥1 fila en results.tsv."""

    def test_cada_leccion_post_corte_tiene_fila(self):
        datos = lecciones()
        with RESULTADOS.open(encoding="utf-8", newline="") as f:
            filas = [r for r in csv.DictReader(f, delimiter="\t") if not r["ts"].startswith("#")]
        con_fila = {r["lesson_id"] for r in filas}
        faltan = sorted(l["id"] for lista in MARCA for l in datos[lista]
                        if date.fromisoformat(str(l["date"])) > CORTE_LECCIONES
                        and l["id"] not in con_fila)
        self.assertEqual(faltan, [], "lecciones post 2026-10-01 sin fila en results.tsv")


class TestTrazaAdjuntaALaLeccion(unittest.TestCase):
    """T-8.4.1: la evidencia ligera de la corrida queda adjunta a la lección."""

    def _importar(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("datito_loop_once", LOOP_ONCE)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return m

    def _fixture(self, tmp):
        lecciones = tmp / "agent_lessons.yaml"
        lecciones.write_text(
            "# comentario de cabecera (debe sobrevivir)\n"
            "version: 1\n"
            "failure_patterns:\n"
            "  - id: VIZ-FAIL-999\n"
            "    date: '2026-10-29'\n"
            "    summary: 'lección de prueba'\n"
            "keep_patterns: []\n", encoding="utf-8")
        return lecciones

    def test_adjunta_traza_y_preserva_comentarios(self):
        import tempfile
        m = self._importar()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            lecciones = self._fixture(tmp)
            ruta = m.adjuntar_traza("VIZ-FAIL-999",
                                    {"decision": "discard", "score": 0.4},
                                    lecciones=lecciones, dir_trazas=tmp / "trazas")
            self.assertTrue(ruta.exists())
            self.assertIn('"decision": "discard"', ruta.read_text(encoding="utf-8"))
            texto = lecciones.read_text(encoding="utf-8")
            self.assertIn("# comentario de cabecera", texto, "se perdieron comentarios")
            self.assertIn('traza: "trazas/VIZ-FAIL-999.json"', texto)
            self.assertIn("- id: VIZ-FAIL-999", texto)

    def test_idempotente_y_leccion_inexistente(self):
        import tempfile
        m = self._importar()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            lecciones = self._fixture(tmp)
            m.adjuntar_traza("VIZ-FAIL-999", {"a": 1},
                             lecciones=lecciones, dir_trazas=tmp / "trazas")
            m.adjuntar_traza("VIZ-FAIL-999", {"a": 2},
                             lecciones=lecciones, dir_trazas=tmp / "trazas")
            self.assertEqual(lecciones.read_text(encoding="utf-8").count("traza:"), 1)
            # lección aún no archivada: la traza se guarda sin tocar el yaml
            ruta = m.adjuntar_traza("VIZ-FAIL-000", {"b": 1},
                                    lecciones=lecciones, dir_trazas=tmp / "trazas")
            self.assertTrue(ruta.exists())
            self.assertNotIn("VIZ-FAIL-000", lecciones.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
