"""Pares pre/post del protocolo a ciegas (REQ-TUT-004).

Value: protects=cada medicion de mediciones.csv es auditable (pre completo, post a
>= 14 dias con delta coherente, concepto existente); fails_when=un post sin pre, una
fecha invalida, un post prematuro o un delta mal calculado; why_new=test_esquema_estado
no lee mediciones.csv; seam=none; no_claim=que la prueba haya sido realmente a ciegas.
"""
import csv
import datetime
import io
import unittest
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
CSV = RAIZ / "07_DATITO/06_AUDITORIAS/evaluacion_a_ciegas/mediciones.csv"
CURRICULUM = RAIZ / "07_DATITO/curriculum.yaml"
PRE = ("concepto", "instrumento", "fecha_pre", "puntaje_pre", "detalle_pre")
POST = ("fecha_post", "puntaje_post", "detalle_post", "delta")
DIAS_MIN = 14


class ErrorMedicion(ValueError):
    pass


def _fecha(valor, campo):
    try:
        return datetime.date.fromisoformat(valor)
    except ValueError as e:
        raise ErrorMedicion(f"{campo}: fecha no ISO {valor!r}") from e


def _puntaje(valor, campo):
    try:
        obtenido, total = valor.split("/")
        return float(obtenido) / float(total)
    except (ValueError, ZeroDivisionError) as e:
        raise ErrorMedicion(f"{campo}: puntaje {valor!r} no es x/z") from e


def filas(texto):
    limpias = "\n".join(l for l in texto.splitlines() if l.strip() and not l.startswith("#"))
    return list(csv.DictReader(io.StringIO(limpias)))


def validar(fila, conceptos):
    cid = fila.get("concepto", "")
    faltan = [c for c in PRE if not (fila.get(c) or "").strip()]
    if faltan:
        raise ErrorMedicion(f"{cid}: pre incompleto {faltan}")
    if cid not in conceptos:
        raise ErrorMedicion(f"{cid}: concepto no existe en curriculum.yaml")
    pre = _fecha(fila["fecha_pre"], f"{cid}.fecha_pre")
    p_pre = _puntaje(fila["puntaje_pre"], f"{cid}.puntaje_pre")
    if not (fila.get("fecha_post") or "").strip():
        if any((fila.get(c) or "").strip() for c in POST):
            raise ErrorMedicion(f"{cid}: datos de post sin fecha_post")
        return
    faltan = [c for c in POST if not (fila.get(c) or "").strip()]
    if faltan:
        raise ErrorMedicion(f"{cid}: post incompleto {faltan}")
    post = _fecha(fila["fecha_post"], f"{cid}.fecha_post")
    if (post - pre).days < DIAS_MIN:
        raise ErrorMedicion(f"{cid}: post a {(post - pre).days} dias (min {DIAS_MIN})")
    esperado = _puntaje(fila["puntaje_post"], f"{cid}.puntaje_post") - p_pre
    if abs(float(fila["delta"]) - esperado) > 1e-6:
        raise ErrorMedicion(f"{cid}: delta {fila['delta']} != {esperado:.3f}")


def conceptos_curriculum():
    return {c["id"] for c in yaml.safe_load(CURRICULUM.read_text(encoding="utf-8"))["conceptos"]}


class MedicionesRealesTests(unittest.TestCase):
    def test_mediciones_csv_es_valido(self):
        conceptos = conceptos_curriculum()
        for fila in filas(CSV.read_text(encoding="utf-8")):
            validar(fila, conceptos)


class MedicionesInvalidasTests(unittest.TestCase):
    CONCEPTOS = {"regresion"}
    BASE = {"concepto": "regresion", "instrumento": "c1", "fecha_pre": "2026-10-28",
            "puntaje_pre": "1/4", "detalle_pre": "x", "fecha_post": "2026-11-15",
            "puntaje_post": "3/4", "detalle_post": "y", "delta": "0.5", "notas": ""}

    def _falla(self, patron, **cambios):
        with self.assertRaisesRegex(ErrorMedicion, patron):
            validar({**self.BASE, **cambios}, self.CONCEPTOS)

    def test_par_valido(self):
        validar(dict(self.BASE), self.CONCEPTOS)

    def test_post_sin_pre(self):
        self._falla("pre incompleto", fecha_pre="", puntaje_pre="")

    def test_post_prematuro(self):
        self._falla("min 14", fecha_post="2026-11-05")

    def test_fecha_no_iso(self):
        self._falla("no ISO", fecha_post="15/11/2026")

    def test_delta_incoherente(self):
        self._falla("delta", delta="0.9")

    def test_post_incompleto(self):
        self._falla("post incompleto", detalle_post="")

    def test_concepto_inexistente(self):
        self._falla("no existe", concepto="astrologia")


if __name__ == "__main__":
    unittest.main()
