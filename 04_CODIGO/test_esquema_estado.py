"""Esquema e invariantes de los YAML de estado de Datito (REQ-EST-005).

Los archivos de estado son la fuente unica de verdad del progreso
(`07_DATITO/progreso.yaml`, `dudas.yaml`, `errores_conceptuales.yaml`).
Se escriben a mano (el tutor los edita en cada sesion), y hasta ahora nada
validaba su forma: un estado mal escrito o una evidencia faltante pasaba
desapercibido hasta que un script consumia el dato.

Las reglas codifican el contrato de `00_INICIO/spec.md` §3:
- los seis estados y su orden;
- la cadena de evidencia de 4 pasos (explicar, aplicar, interpretar,
  transferir), cada una `{fecha: ISO, detalle: str}` o null;
- que un estado avanzado exija las evidencias que lo definen
  (COMPRENDIDO exige explicar+aplicar, DOMINADO las cuatro);
- coherencia de contadores (resumen == conceptos, total_observados).

Uso: `python -m unittest 04_CODIGO/test_esquema_estado.py`
"""
import datetime
import re
import unittest
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]
DATITO = RAIZ / "07_DATITO"
VISUAL = DATITO / "01_CONCEPTOS" / "visual"

ESTADOS = {"NO_ESTUDIADO", "EN_ESTUDIO", "COMPRENSION_PARCIAL", "COMPRENDIDO",
           "DOMINADO", "REQUIERE_REPASO"}
EVIDENCIAS = ("explicar", "aplicar", "interpretar", "transferir")
ESTADOS_DUDA = {"resuelta", "practica", "abierta"}
ESTADOS_ERROR = {"abierto", "resuelto", "reincidente", "anulado"}
FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ErrorEsquema(AssertionError):
    """Un campo viola el esquema; el mensaje nombra el campo."""


def _exige(cond, campo, mensaje):
    if not cond:
        raise ErrorEsquema(f"{campo}: {mensaje}")


def _fecha_iso(valor, campo):
    # YAML convierte las fechas sin comillas en datetime.date; ambas formas valen
    if isinstance(valor, datetime.date):
        return
    _exige(isinstance(valor, str) and FECHA.match(valor), campo,
           f"fecha '{valor}' no es ISO (AAAA-MM-DD)")


def _evidencia(valor, campo):
    if valor is None:
        return
    _exige(isinstance(valor, dict), campo, "la evidencia debe ser un mapa o null")
    _exige(set(valor) >= {"fecha", "detalle"}, campo, "faltan claves fecha/detalle")
    _fecha_iso(valor["fecha"], f"{campo}.fecha")
    _exige(isinstance(valor["detalle"], str) and valor["detalle"].strip(),
           f"{campo}.detalle", "el detalle no puede estar vacio")


def validar_progreso(doc):
    meta = doc.get("meta") or {}
    for clave in ("alumno", "tutor", "asignatura"):
        _exige(isinstance(meta.get(clave), str) and meta[clave].strip(),
               f"meta.{clave}", "obligatorio y no vacio")
    _exige(isinstance(meta.get("sesiones_totales"), int) and meta["sesiones_totales"] >= 0,
           "meta.sesiones_totales", "entero >= 0")
    _exige(isinstance(meta.get("diagnostico_inicial_hecho"), bool),
           "meta.diagnostico_inicial_hecho", "booleano")

    conceptos = doc.get("conceptos") or []
    _exige(isinstance(conceptos, list) and conceptos, "conceptos", "lista no vacia")
    ids = [c.get("id") for c in conceptos]
    _exige(len(ids) == len(set(ids)), "conceptos", f"ids repetidos: {ids}")

    for c in conceptos:
        cid = f"concepto {c.get('id')}"
        _exige(c.get("estado") in ESTADOS, f"{cid}.estado",
               f"'{c.get('estado')}' no es un estado valido {sorted(ESTADOS)}")
        evs = c.get("evidencias") or {}
        _exige(set(evs) == set(EVIDENCIAS), f"{cid}.evidencias",
               f"deben ser exactamente {list(EVIDENCIAS)}")
        for nombre in EVIDENCIAS:
            _evidencia(evs.get(nombre), f"{cid}.evidencias.{nombre}")
        _exige(isinstance(c.get("sesiones"), int) and c["sesiones"] >= 0,
               f"{cid}.sesiones", "entero >= 0")
        if c.get("ultima_verificacion") is not None:
            _fecha_iso(c["ultima_verificacion"], f"{cid}.ultima_verificacion")

        estado, presentes = c["estado"], [n for n in EVIDENCIAS if evs.get(n)]
        if estado == "NO_ESTUDIADO":
            _exige(not presentes and c["sesiones"] == 0, cid,
                   "NO_ESTUDIADO exige evidencias vacias y sesiones 0")
        elif estado == "EN_ESTUDIO":
            _exige(c["sesiones"] >= 1, cid, "EN_ESTUDIO exige al menos 1 sesion")
        elif estado == "COMPRENSION_PARCIAL":
            _exige("explicar" in presentes, cid,
                   "COMPRENSION_PARCIAL exige evidencia de explicar")
        elif estado == "COMPRENDIDO":
            _exige({"explicar", "aplicar"} <= set(presentes), cid,
                   "COMPRENDIDO exige explicar y aplicar")
        elif estado == "DOMINADO":
            _exige(set(presentes) == set(EVIDENCIAS), cid,
                   "DOMINADO exige las cuatro evidencias")
        elif estado == "REQUIERE_REPASO":
            _exige(presentes and c.get("ultima_verificacion"), cid,
                   "REQUIERE_REPASO exige al menos una evidencia y ultima_verificacion")

    resumen = doc.get("resumen") or {}
    for estado in ESTADOS:
        real = sum(1 for c in conceptos if c["estado"] == estado)
        _exige(resumen.get(estado) == real, f"resumen.{estado}",
               f"declara {resumen.get(estado)}, hay {real}")
    _exige(resumen.get("siguiente_recomendado") in ids,
           "resumen.siguiente_recomendado", "debe ser el id de un concepto existente")


def validar_dudas(doc, ids_conceptos):
    dudas = doc.get("dudas") or []
    _exige(isinstance(dudas, list), "dudas", "lista")
    vistos = set()
    for d in dudas:
        _exige(d.get("id") and d["id"] not in vistos, "duda.id", f"ausente o repetido: {d.get('id')}")
        vistos.add(d["id"])
        _fecha_iso(d.get("fecha"), f"duda {d['id']}.fecha")
        _exige(isinstance(d.get("estado"), str) and d["estado"] in ESTADOS_DUDA,
               f"duda {d['id']}.estado", f"'{d.get('estado')}' no es valido")
        for campo in ("pregunta", "respuesta", "sesion"):
            _exige(isinstance(d.get(campo), str) and d[campo].strip(),
                   f"duda {d['id']}.{campo}", "obligatorio y no vacio")
        _exige((RAIZ / d["sesion"]).resolve().is_file(),
               f"duda {d['id']}.sesion", f"no existe {d['sesion']}")
        conceptos = d.get("conceptos") or []
        _exige(conceptos and all(c in ids_conceptos for c in conceptos),
               f"duda {d['id']}.conceptos", "vacios o con id de concepto inexistente")
        visuales = d.get("visuales") or []
        _exige(visuales, f"duda {d['id']}.visuales", "al menos un visual")
        for v in visuales:
            _exige((VISUAL / v).resolve().is_file(),
                   f"duda {d['id']}.visuales", f"no existe {v}")
        fuentes = d.get("fuentes") or []
        _exige(isinstance(fuentes, list) and len(fuentes) >= 1,
               f"duda {d['id']}.fuentes", "al menos una fuente (etiqueta G4)")


def validar_errores(doc, ids_conceptos):
    meta = doc.get("meta") or {}
    observados = doc.get("observados") or []
    patrones = doc.get("patrones_vigilados") or []
    _exige(isinstance(observados, list), "observados", "lista")
    _exige(isinstance(patrones, list), "patrones_vigilados", "lista")

    vistos = set()
    activos = 0
    for o in observados:
        oid = o.get("id")
        _exige(oid and oid not in vistos, "error.id", f"ausente o repetido: {oid}")
        vistos.add(oid)
        _exige(o.get("concepto") in ids_conceptos, f"error {oid}.concepto",
               f"'{o.get('concepto')}' no es un concepto del curriculum")
        _exige(isinstance(o.get("veces"), int) and o["veces"] >= 0,
               f"error {oid}.veces", "entero >= 0")
        _exige(o.get("estado") in ESTADOS_ERROR, f"error {oid}.estado",
               f"'{o.get('estado')}' no es valido")
        fechas = o.get("fechas") or []
        _exige(isinstance(fechas, list) and fechas, f"error {oid}.fechas", "lista no vacia")
        for i, f in enumerate(fechas):
            _fecha_iso(f, f"error {oid}.fechas[{i}]")
        if o["estado"] != "anulado":
            activos += 1
            _exige(isinstance(o.get("dijo"), str) and o["dijo"].strip(),
                   f"error {oid}.dijo", "todo error activo exige la cita textual (G13)")
    _exige(meta.get("total_observados") == activos, "meta.total_observados",
           f"declara {meta.get('total_observados')}, hay {activos} no anulados")

    for p in patrones:
        pid = p.get("id")
        _exige(pid and pid not in {q.get("id") for q in patrones if q is not p},
               "patron.id", f"ausente o repetido: {pid}")
        _exige(p.get("concepto") in ids_conceptos, f"patron {pid}.concepto",
               f"'{p.get('concepto')}' no es un concepto del curriculum")
        _exige(isinstance(p.get("confusion"), str) and p["confusion"].strip(),
               f"patron {pid}.confusion", "obligatorio y no vacio")


def cargar(ruta):
    return yaml.safe_load(Path(ruta).read_text(encoding="utf-8"))


class EsquemaEstadoActualTests(unittest.TestCase):
    """Los YAML vigentes cumplen el esquema (suite en verde = contrato intacto)."""

    @classmethod
    def setUpClass(cls):
        cls.progreso = cargar(DATITO / "progreso.yaml")
        cls.ids = [c["id"] for c in cls.progreso["conceptos"]]

    def test_progreso_actual(self):
        validar_progreso(self.progreso)

    def test_dudas_actuales(self):
        validar_dudas(cargar(DATITO / "dudas.yaml"), self.ids)

    def test_errores_actuales(self):
        validar_errores(cargar(DATITO / "errores_conceptuales.yaml"), self.ids)


class FixturesInvalidosTests(unittest.TestCase):
    """Cada regla rechaza el fixture que la viola, nombrando el campo."""

    @classmethod
    def setUpClass(cls):
        cls.ids = [c["id"] for c in cargar(DATITO / "progreso.yaml")["conceptos"]]

    def base(self):
        doc = cargar(DATITO / "progreso.yaml")
        return doc

    def test_estado_invalido(self):
        doc = self.base()
        doc["conceptos"][0]["estado"] = "CASI_DOMINADO"
        with self.assertRaisesRegex(ErrorEsquema, r"concepto \S+\.estado"):
            validar_progreso(doc)

    def test_evidencia_sin_detalle(self):
        doc = self.base()
        doc["conceptos"][4]["evidencias"]["explicar"] = {"fecha": "2026-09-18"}
        with self.assertRaisesRegex(ErrorEsquema, r"explicar"):
            validar_progreso(doc)

    def test_fecha_no_iso(self):
        doc = self.base()
        doc["conceptos"][4]["evidencias"]["explicar"]["fecha"] = "18/09/2026"
        with self.assertRaisesRegex(ErrorEsquema, r"fecha"):
            validar_progreso(doc)

    def test_comprendido_sin_aplicar(self):
        doc = self.base()
        doc["conceptos"][4]["evidencias"]["aplicar"] = None  # COMPRENDIDO sin aplicar
        with self.assertRaisesRegex(ErrorEsquema, r"COMPRENDIDO"):
            validar_progreso(doc)

    def test_dominado_sin_transferir(self):
        doc = self.base()
        doc["conceptos"][0]["estado"] = "DOMINADO"  # sin ninguna evidencia
        with self.assertRaisesRegex(ErrorEsquema, r"DOMINADO"):
            validar_progreso(doc)

    def test_resumen_mentiroso(self):
        doc = self.base()
        doc["resumen"]["NO_ESTUDIADO"] = 99
        with self.assertRaisesRegex(ErrorEsquema, r"resumen\.NO_ESTUDIADO"):
            validar_progreso(doc)

    def test_siguiente_recomendado_inexistente(self):
        doc = self.base()
        doc["resumen"]["siguiente_recomendado"] = "no_existe"
        with self.assertRaisesRegex(ErrorEsquema, r"siguiente_recomendado"):
            validar_progreso(doc)

    def test_error_activo_sin_cita(self):
        doc = cargar(DATITO / "errores_conceptuales.yaml")
        doc["observados"][0]["dijo"] = ""
        with self.assertRaisesRegex(ErrorEsquema, r"\.dijo"):
            validar_errores(doc, self.ids)

    def test_total_observados_desactualizado(self):
        doc = cargar(DATITO / "errores_conceptuales.yaml")
        doc["meta"]["total_observados"] += 1
        with self.assertRaisesRegex(ErrorEsquema, r"total_observados"):
            validar_errores(doc, self.ids)

    def test_duda_con_visual_roto(self):
        doc = cargar(DATITO / "dudas.yaml")
        doc["dudas"][0]["visuales"] = ["99_no_existe.html"]
        with self.assertRaisesRegex(ErrorEsquema, r"visuales"):
            validar_dudas(doc, self.ids)


if __name__ == "__main__":
    unittest.main()
