"""El harness detecta cada violacion que dice detectar (REQ-TUT-001).

Un harness que solo pasa es inutil: estas pruebas inyectan violaciones en
transcripts de referencia y exigen que la regla correspondiente las nombre.
"""
import copy
import sys
import unittest
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent / "harness_escenarios"
sys.path.insert(0, str(BASE))

from harness import cargar, evaluar, reporte, ESCENARIOS  # noqa: E402


def transcript(id_esc):
    esc = cargar(ESCENARIOS / f"{id_esc}.yaml")
    return esc, cargar(BASE / esc["transcript"])


class ReglasDetectanViolacionesTests(unittest.TestCase):
    def _viola(self, id_esc, muta, regla):
        esc, tr = transcript(id_esc)
        muta(tr["turnos"])
        viola = evaluar(esc, tr)
        self.assertTrue(any(v.startswith(f"[{regla}]") for v in viola),
                        f"{regla} no detecto la violacion en {id_esc}: {viola}")

    def test_espera_real_detecta_respuesta_propia(self):
        def muta(turnos):
            turnos.insert(1, {"rol": "tutor", "texto": "Probablemente pensaste en la brecha."})
        self._viola("g1-espera-basica", muta, "espera_real")

    def test_no_simula_detecta_dialogo_fabricado(self):
        def muta(turnos):
            turnos[0]["texto"] += " Supongamos que responde que es la brecha: correcto, pero..."
        self._viola("g1-no-simula-dialogo", muta, "no_simula_alumno")

    def test_solucion_antes_de_dos_intentos(self):
        def muta(turnos):
            turnos.insert(1, {"rol": "tutor", "texto": "La respuesta completa: B sobreajusta."})
        self._viola("intentos-solucion-tras-dos-fallos", muta, "solucion_tras_dos_intentos")

    def test_respuesta_pedida_sin_registrar(self):
        def muta(turnos):
            for t in turnos:
                if any(str(a).startswith("duda:") for a in (t.get("acciones") or [])):
                    t["acciones"] = [a for a in t["acciones"] if not str(a).startswith("duda:")]
        self._viola("g11-dame-la-respuesta", muta, "respuesta_pedida_registrada")

    def test_respuesta_sin_transferencia(self):
        def muta(turnos):
            turnos[:] = [t for t in turnos
                         if not (t["rol"] == "tutor" and t["texto"].rstrip().endswith("?"))]
        self._viola("g11-dame-la-respuesta", muta, "transferencia_tras_respuesta")


class EscenariosSanosTests(unittest.TestCase):
    """Los transcripts de referencia cumplen sus propias reglas y el reporte esta en 100%."""

    def test_todos_los_escenarios_cumplen(self):
        filas = reporte()
        self.assertGreaterEqual(len(filas), 15)
        malos = [f["id"] for f in filas if not f["ok"]]
        self.assertEqual(malos, [], f"escenarios de referencia con violaciones: {malos}")

    def test_cobertura_minima_por_garantia(self):
        filas = reporte()
        por_garantia = {}
        for f in filas:
            por_garantia.setdefault(f["garantia"], []).append(f["id"])
        self.assertGreaterEqual(len(por_garantia.get("G1", [])), 4)
        self.assertGreaterEqual(len(por_garantia.get("G11", [])), 4)
        self.assertGreaterEqual(len(por_garantia.get("INTENTOS", [])), 2)
        self.assertGreaterEqual(len(por_garantia.get("BORDE", [])), 4)

    def test_schema_rechaza_regla_desconocida(self):
        esc, tr = transcript("g1-espera-basica")
        esc = copy.deepcopy(esc)
        esc["reglas"] = ["espera_real", "regla_inventada"]
        with self.assertRaisesRegex(ValueError, "regla_inventada"):
            evaluar(esc, tr)

    def test_schema_rechaza_transcript_sin_turnos(self):
        esc, _ = transcript("g1-espera-basica")
        with self.assertRaisesRegex(ValueError, "turnos"):
            evaluar(esc, {"turnos": []})

    def test_cada_escenario_tiene_transcript(self):
        for ruta in sorted(ESCENARIOS.glob("*.yaml")):
            esc = yaml.safe_load(ruta.read_text(encoding="utf-8"))
            self.assertTrue((BASE / esc["transcript"]).is_file(),
                            f"{esc['id']}: falta {esc['transcript']}")


if __name__ == "__main__":
    unittest.main()
