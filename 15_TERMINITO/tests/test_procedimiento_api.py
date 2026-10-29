"""API de evaluación procedural (H-8.2): POST /evaluacion con código."""
import json
import threading
import urllib.request
from http.server import ThreadingHTTPServer

import pytest
import yaml

from datito import servidor
from datito import grafo as grafo_mod

BASE = "http://127.0.0.1"


def _post(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())


@pytest.fixture
def httpd_con_protocolo(tmp_path_curso, monkeypatch):
    g = {"cadenas": {}, "conceptos": {
        "a": {"nombre": "A", "viene_de": [], "habilita": []},
        "b": {"nombre": "B", "viene_de": [], "habilita": []}}}
    (tmp_path_curso.ruta("grafo") / "grafo.yaml").write_text(
        yaml.safe_dump(g, allow_unicode=True), encoding="utf-8")
    item = {"id": "d1", "conceptos": ["a", "b"], "pregunta": "brecha antes que etiqueta",
            "criterios": ["orden"], "solucion": "n/a",
            "protocolo": [{"evento": "brecha", "antes_de": ["etiquetar"]},
                          {"evento": "etiquetar", "requiere": True}]}
    (tmp_path_curso.ruta("evaluaciones") / "p.yaml").write_text(
        yaml.safe_dump({"items": [item]}, allow_unicode=True), encoding="utf-8")

    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}", tmp_path_curso
    server.shutdown()


BIEN = 'print("#@brecha")\nprint("#@etiquetar")\n'
MAL = 'print("#@etiquetar")\nprint("#@brecha")\n'


def test_procedural_bien_logrado_y_dominio(httpd_con_protocolo):
    url, curso = httpd_con_protocolo
    status, r = _post(f"{url}/api/cursos/testcurso/evaluacion",
                      {"item_id": "d1", "codigo": BIEN})
    assert status == 200
    assert r["resultado"] == "logrado"
    assert r["confianza"] == "baja"          # traza, no razonamiento
    assert r["traza"]["eventos"] == ["brecha", "etiquetar"]
    dominio = yaml.safe_load(curso.ruta("grafo", "dominio.yaml").read_text())
    assert dominio["a"]["estado"] == "dominado"


def test_procedural_mal_no_logrado(httpd_con_protocolo):
    url, curso = httpd_con_protocolo
    status, r = _post(f"{url}/api/cursos/testcurso/evaluacion",
                      {"item_id": "d1", "codigo": MAL})
    assert status == 200
    assert r["resultado"] in ("parcial", "no_logrado")
    assert r["traza"]["eventos"] == ["etiquetar", "brecha"]
    dominio = yaml.safe_load(curso.ruta("grafo", "dominio.yaml").read_text())
    assert dominio["a"]["estado"] != "dominado"


def test_items_publicos_marcan_protocolo(httpd_con_protocolo):
    url, _ = httpd_con_protocolo
    with urllib.request.urlopen(f"{url}/api/cursos/testcurso/evaluacion",
                                timeout=10) as r:
        items = json.loads(r.read().decode())["items"]
    assert items[0]["protocolo"] is True
