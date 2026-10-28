"""historias_usuario.yaml describe las clases vigentes y solo conceptos reales (H-2.2).

Una historia por clase (18 de concepto + 5 de repaso). Toda historia cita
conceptos que existen en curriculum.yaml y un criterio de aceptación con
fuente (la ficha Bloom de su clase). Sin este test el archivo podía volver
a referenciar clases o conceptos que ya no existen.
"""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CLASES = yaml.safe_load((ROOT / "07_DATITO" / "clases.yaml").read_text(encoding="utf-8"))["clases"]
CURRICULUM = {c["id"] for c in yaml.safe_load((ROOT / "07_DATITO" / "curriculum.yaml").read_text(encoding="utf-8"))["conceptos"]}
HISTORIAS = yaml.safe_load((ROOT / "07_DATITO" / "historias_usuario.yaml").read_text(encoding="utf-8"))["historias"]


class TestHistoriasClasesCurriculo(unittest.TestCase):
    def test_una_historia_por_clase(self):
        clases = sorted(c["n"] for c in CLASES)
        de_historias = sorted(h["clase"] for h in HISTORIAS)
        self.assertEqual(de_historias, clases,
                         f"faltan historias para {sorted(set(clases) - set(de_historias))} "
                         f"o sobran para {sorted(set(de_historias) - set(clases))}")

    def test_ids_unicos_y_secuenciales(self):
        ids = [h["id"] for h in HISTORIAS]
        self.assertEqual(len(ids), len(set(ids)), "ids de historia repetidos")
        mal = [h["id"] for h in HISTORIAS if not re.fullmatch(r"US-\d{2}", h["id"])]
        self.assertEqual(mal, [])

    def test_conceptos_existen_en_curriculo(self):
        colgantes = sorted({c for h in HISTORIAS for c in h.get("conceptos", [])} - CURRICULUM)
        self.assertEqual(colgantes, [], "conceptos que no existen en curriculum.yaml")

    def test_conceptos_coinciden_con_los_de_su_clase(self):
        por_clase = {c["n"]: set(c.get("conceptos") or []) for c in CLASES}
        mal = [f"{h['id']} (clase {h['clase']})" for h in HISTORIAS
               if set(h.get("conceptos") or []) != por_clase[h["clase"]]]
        self.assertEqual(mal, [], "historias cuyos conceptos no son los de su clase en clases.yaml")

    def test_criterio_de_aceptacion_presente(self):
        vacios = [h["id"] for h in HISTORIAS if not (h.get("criterio_aceptacion") or "").strip()]
        self.assertEqual(vacios, [], "historias sin criterio de aceptación")

    def test_criterio_igual_al_de_la_clase(self):
        """El criterio viene de la ficha Bloom de clases.yaml: nada inventado."""
        de_clase = {c["n"]: (c.get("bloom") or {}).get("criterio_dominio", "") for c in CLASES}
        mal = [h["id"] for h in HISTORIAS
               if h.get("criterio_aceptacion") and de_clase[h["clase"]]
               and h["criterio_aceptacion"] != de_clase[h["clase"]]]
        self.assertEqual(mal, [], "criterios que no son el criterio_dominio de su clase")


if __name__ == "__main__":
    unittest.main()
