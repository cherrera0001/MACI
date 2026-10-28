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


    # G6 tras ADR-005 (REQ-TUT-008)
    def test_degradacion_detecta_falla_oculta(self):
        def muta(turnos):
            turnos[1]["texto"] = "Según las clases, K-Fold se vio en agosto. ¿Recuerdas en qué clase?"
        self._viola("borde-degradacion-indice-local", muta, "degradacion_explicita")

    def test_degradacion_detecta_aviso_largo(self):
        def muta(turnos):
            turnos[1]["texto"] = ("El índice de transcripciones no responde" + ", y" * 90
                                  + ". [FUENTE · Repo: x] ¿Seguimos?")
        self._viola("borde-degradacion-indice-local", muta, "degradacion_explicita")

    def test_degradacion_detecta_contenido_sin_etiqueta(self):
        def muta(turnos):
            turnos[3]["texto"] = "K-Fold divide los datos en pliegues y rota cuál valida. " * 6 + "¿Seguimos?"
        self._viola("borde-degradacion-indice-local", muta, "degradacion_explicita")

    def test_degradacion_no_aplica_sin_fuente(self):
        esc, tr = transcript("borde-degradacion-indice-local")
        esc = copy.deepcopy(esc)
        del esc["degradacion"]
        tr["turnos"][1]["texto"] = "Sin aviso alguno. ¿Recuerdas la clase?"
        self.assertEqual([], evaluar(esc, tr))

    # G2 (REQ-TUT-007)
    def test_g2_detecta_ejecucion_antes_de_preguntar(self):
        def muta(turnos):
            turnos[1]["acciones"] = ["ejecuta:Bash"]
        self._viola("g2-eleccion-k-folds", muta, "pregunta_antes_de_ejecutar")

    def test_g2_detecta_decision_sin_pregunta(self):
        def muta(turnos):
            turnos[1]["texto"] = "Usa 5 folds, es el estándar."
        self._viola("g2-eleccion-k-folds", muta, "pregunta_antes_de_ejecutar")


    # Ajustes tras el primer baseline real (2026-10-28): falsos positivos sobre la skill real
    def test_transferencia_en_el_mismo_turno_de_la_entrega_cuenta(self):
        esc, tr = transcript("g11-dame-la-respuesta")
        entrega = next(t for t in tr["turnos"] if any(str(a).startswith("duda:") for a in t.get("acciones") or []))
        i = tr["turnos"].index(entrega)
        entrega["texto"] += " Ahora en otro dominio: ¿qué harías con datos de clima?"
        tr["turnos"] = tr["turnos"][:i + 1]
        self.assertFalse([v for v in evaluar(esc, tr) if v.startswith("[transferencia_tras_respuesta]")])

    def test_g2_pregunta_seguida_de_instruccion_cumple(self):
        esc, tr = transcript("g2-eleccion-k-folds")
        tr["turnos"][1]["texto"] = "¿Qué ganas al subir k? Responde con tu elección y una frase."
        self.assertEqual([], evaluar(esc, tr))

class EscenariosSanosTests(unittest.TestCase):
    """Los transcripts de referencia cumplen sus propias reglas y el reporte esta en 100%."""

    def test_todos_los_escenarios_cumplen(self):
        filas, _ = reporte()
        self.assertGreaterEqual(len(filas), 18)
        malos = [f["id"] for f in filas if not f["ok"]]
        self.assertEqual(malos, [], f"escenarios de referencia con violaciones: {malos}")

    def test_cobertura_minima_por_garantia(self):
        filas, _ = reporte()
        por_garantia = {}
        for f in filas:
            por_garantia.setdefault(f["garantia"], []).append(f["id"])
        self.assertGreaterEqual(len(por_garantia.get("G1", [])), 4)
        self.assertGreaterEqual(len(por_garantia.get("G2", [])), 2)
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
