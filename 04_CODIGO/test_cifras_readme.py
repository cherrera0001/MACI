"""Las cifras del README se comprueban contra la fuente (H-3.2).

Sin generar el README: solo comprobarlo. Si una cifra cambia en
clases.yaml, curriculum.yaml, dudas.yaml o indice_clases.yaml, este test
obliga a actualizar el README en el mismo commit.
"""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
CLASES = yaml.safe_load((ROOT / "07_DATITO" / "clases.yaml").read_text(encoding="utf-8"))["clases"]
CURRICULUM = yaml.safe_load((ROOT / "07_DATITO" / "curriculum.yaml").read_text(encoding="utf-8"))["conceptos"]
DUDAS = yaml.safe_load((ROOT / "07_DATITO" / "dudas.yaml").read_text(encoding="utf-8"))["dudas"]
HISTORIAS = yaml.safe_load((ROOT / "07_DATITO" / "historias_usuario.yaml").read_text(encoding="utf-8"))["historias"]
INDICE = yaml.safe_load((ROOT / "05_CLASES" / "indice_clases.yaml").read_text(encoding="utf-8"))


class TestCifrasReadme(unittest.TestCase):
    def test_clases_totales(self):
        n = len(CLASES)
        self.assertIn(f"{n} clases", README, f"README no dice «{n} clases»")

    def test_unidades(self):
        n = len({c["unidad"] for c in CLASES})
        self.assertIn(f"{n} unidades", README, f"README no dice «{n} unidades»")

    def test_clases_construidas(self):
        construidas = sum(1 for c in CLASES if c.get("visual"))
        m = re.search(r"(\d+) están construidas", README)
        self.assertIsNotNone(m, "README no declara cuántas clases están construidas")
        self.assertEqual(int(m.group(1)), construidas,
                         f"README dice {m.group(1)} construidas; clases.yaml tiene {construidas} con visual")

    def test_certamenes(self):
        n = len(list((ROOT / "07_DATITO" / "04_EJERCICIOS").glob("certamen_*.html")))
        self.assertIn(f"{n} certámenes", README, f"README no dice «{n} certámenes»")

    def test_conceptos(self):
        self.assertIn(f"{len(CURRICULUM)} conceptos", README,
                      f"README no dice «{len(CURRICULUM)} conceptos»")

    def test_dudas(self):
        self.assertIn(f"{len(DUDAS)} dudas", README, f"README no dice «{len(DUDAS)} dudas»")

    def test_historias(self):
        self.assertIn(f"{len(HISTORIAS)} historias", README,
                      f"README no dice «{len(HISTORIAS)} historias»")

    def test_clases_transcritas(self):
        n_indice = INDICE["meta"]["total_clases"]
        n_md = len(list((ROOT / "05_CLASES" / "transcripciones").glob("*.md")))
        self.assertEqual(n_indice, n_md, "indice_clases.yaml desactualizado contra transcripciones/")
        self.assertIn(f"{n_indice} clases transcritas", README,
                      f"README no dice «{n_indice} clases transcritas»")


if __name__ == "__main__":
    unittest.main()
