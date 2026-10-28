"""El glosario del curso tiene forma y cubre clases reales (H-1.2)."""
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
GLOSARIO = ROOT / "07_DATITO" / "glosario.yaml"
TERMINOS = yaml.safe_load(GLOSARIO.read_text(encoding="utf-8"))["terminos"]
CLASES = {c["n"] for c in yaml.safe_load((ROOT / "07_DATITO" / "clases.yaml").read_text(encoding="utf-8"))["clases"]}


class TestGlosario(unittest.TestCase):
    def test_campos_presentes(self):
        mal = [t["termino"] for t in TERMINOS
               if not (t.get("termino") or "").strip()
               or not (t.get("definicion") or "").strip()
               or t.get("clase") is None
               or "en" not in t]
        self.assertEqual(mal, [])

    def test_clases_existen(self):
        mal = sorted({t["clase"] for t in TERMINOS} - CLASES)
        self.assertEqual(mal, [], "términos que citan clases inexistentes")

    def test_terminos_unicos(self):
        nombres = [t["termino"] for t in TERMINOS]
        repetidos = sorted({n for n in nombres if nombres.count(n) > 1})
        self.assertEqual(repetidos, [])

    def test_cada_clase_de_concepto_tiene_al_menos_un_termino(self):
        # las clases de repaso tipo certamen (20, 21, 23) integran vocabulario;
        # el glosario cubre el vocabulario nuevo, que vive en las de concepto
        clases_concepto = {c["n"] for c in yaml.safe_load(
            (ROOT / "07_DATITO" / "clases.yaml").read_text(encoding="utf-8"))["clases"]
            if c.get("tipo", "concepto") == "concepto"}
        cubiertas = {t["clase"] for t in TERMINOS}
        sin = sorted(clases_concepto - cubiertas)
        self.assertEqual(sin, [], "clases de concepto sin ningún término en el glosario")


if __name__ == "__main__":
    unittest.main()
