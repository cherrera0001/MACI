"""La memoria del Agents Learning Loop se puede leer como dice program_loop.md.

program_loop.md manda leer `failure_patterns` primero. Si una lección de fallo
queda archivada bajo `keep_patterns`, el agente que sigue el protocolo no la ve.
"""
import csv
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LOOP = ROOT / "07_DATITO" / "07_BITACORA" / "learning_loop"
LECCIONES = LOOP / "agent_lessons.yaml"
RESULTADOS = LOOP / "results.tsv"
SKILLS = ROOT / ".claude" / "skills"
ESPEJO = ROOT / ".agents" / "skills"
MARCA = {"failure_patterns": "-FAIL-", "keep_patterns": "-KEEP-"}


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

    @unittest.skipUnless(ESPEJO.is_dir(), "sin espejo .agents/skills en esta máquina")
    def test_espejo_de_skills_no_diverge(self):
        def texto(p):
            return p.read_text(encoding="utf-8").replace("\r\n", "\n")

        nombres = {p.parent.name for p in SKILLS.glob("*/SKILL.md")} | {p.parent.name for p in ESPEJO.glob("*/SKILL.md")}
        distintos = sorted(n for n in nombres
                           if not (SKILLS / n / "SKILL.md").is_file() or not (ESPEJO / n / "SKILL.md").is_file()
                           or texto(SKILLS / n / "SKILL.md") != texto(ESPEJO / n / "SKILL.md"))
        self.assertEqual(distintos, [], ".agents/skills difiere de .claude/skills")


if __name__ == "__main__":
    unittest.main()
