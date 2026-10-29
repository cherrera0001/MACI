"""API de distinciones desde la web (H-7.2 / T-7.2.1)."""
import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest
import yaml

from datito import evaluador, servidor
from datito.indice import Indice
from datito import fragmentos as frag

BASE = "http://127.0.0.1"


def _get(url):
    with urllib.request.urlopen(url, timeout=10) as r:
        return r.status, json.loads(r.read().decode())


def _post(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode())


@pytest.fixture
def httpd(tmp_path_curso, tmp_path, monkeypatch):
    mat = tmp_path / "mat"
    mat.mkdir()
    (mat / "clase.md").write_text(
        "# Sobreajuste\n\nEl sobreajuste memoriza el entrenamiento.\n\n"
        "# Generalización\n\nLa generalización mide el rendimiento en datos nuevos.\n",
        encoding="utf-8")
    destino = tmp_path_curso.ruta("materiales", "clase.md")
    destino.symlink_to(mat / "clase.md")
    fuentes, frags = frag.parsear_materiales([destino])
    Indice().construir(frags).guardar(tmp_path_curso.ruta(".indice"))
    g = {"cadenas": {"cadena uno": ["sobreajuste", "generalizacion"]},
         "conceptos": {
             "sobreajuste": {"nombre": "Sobreajuste", "viene_de": [], "habilita": []},
             "generalizacion": {"nombre": "Generalización", "viene_de": [], "habilita": []}}}
    (tmp_path_curso.ruta("grafo") / "grafo.yaml").write_text(
        yaml.safe_dump(g, allow_unicode=True), encoding="utf-8")

    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}"
    server.shutdown()


DISTINCTION_OK = {
    "conceptos": ["sobreajuste", "generalizacion"],
    "pregunta": "¿Cuál de los dos memoriza y cuál mide datos nuevos?",
    "criterios": ["identifica al memorizador", "nombra la generalizacion"],
    "pasos": ["Paso 1: ¿qué conjunto de datos evalúa cada uno?"],
    "solucion": "el que memoriza es sobreajuste",
}


def test_conceptos_del_grafo(httpd):
    status, r = _get(f"{httpd}/api/cursos/testcurso/conceptos")
    assert status == 200
    ids = {c["id"] for c in r["conceptos"]}
    assert {"sobreajuste", "generalizacion"} <= ids


def test_crear_distincion_valida(httpd, tmp_path_curso):
    status, r = _post(f"{httpd}/api/cursos/testcurso/evaluaciones", DISTINCTION_OK)
    assert status == 201 and r["guardado"].startswith("d1-web-")
    items = evaluador.cargar_items(tmp_path_curso)
    assert any(i.id == r["guardado"] and i.pasos for i in items)
    # aparece en el endpoint público de evaluación
    status, pub = _get(f"{httpd}/api/cursos/testcurso/evaluacion")
    assert any(i["id"] == r["guardado"] for i in pub["items"])


@pytest.mark.parametrize("caso,fragmento", [
    ({"conceptos": ["sobreajuste"], "pregunta": "p", "criterios": ["c"]}, ">=2 conceptos"),
    ({"conceptos": ["sobreajuste", "fantasma"], "pregunta": "p", "criterios": ["c"]},
     "fuera del grafo"),
    ({"conceptos": ["sobreajuste", "generalizacion"], "pregunta": "", "criterios": ["c"]},
     "pregunta"),
    ({"conceptos": ["sobreajuste", "generalizacion"], "pregunta": "p", "criterios": []},
     "criterio"),
])
def test_rechaza_distinciones_invalidas(httpd, caso, fragmento):
    status, r = _post(f"{httpd}/api/cursos/testcurso/evaluaciones", caso)
    assert status == 422, f"esperaba 422 para {fragmento}"
    assert fragmento.split()[0] in r["detalle"] or fragmento in r["detalle"]


def test_ids_automaticos_unicos(tmp_path_curso):
    g = {"conceptos": {"a": {}, "b": {}}, "cadenas": {}}
    (tmp_path_curso.ruta("grafo") / "grafo.yaml").write_text(
        yaml.safe_dump(g), encoding="utf-8")
    item = {**DISTINCTION_OK, "conceptos": ["a", "b"]}
    i1 = evaluador.agregar_item(tmp_path_curso, item, {"a", "b"})
    i2 = evaluador.agregar_item(tmp_path_curso, item, {"a", "b"})
    assert i1.id != i2.id
