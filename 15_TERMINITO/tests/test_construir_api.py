"""Regresión: POST /construir funciona end-to-end (bug d sin definir, ola 5)."""
import json
import threading
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer

import pytest

from datito import servidor

BASE = "http://127.0.0.1"
COMPONENTES = {"rol_dominio": "r", "mision": "m", "funciones": "f",
               "estilo_ensenanza": "e", "contexto_curso": "c",
               "estilo_aprendizaje": "a", "restricciones": "x",
               "relacion_temporal": "t"}


def _post(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())


@pytest.fixture
def httpd(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"{BASE}:{server.server_address[1]}"
    server.shutdown()


def test_construir_end_to_end_por_api(httpd, tmp_path_curso):
    req = urllib.request.Request(
        f"{httpd}/api/cursos/testcurso/materiales?nombre=clase.md",
        data="# Sobreajuste\n\nEl sobreajuste memoriza el entrenamiento.\n".encode(),
        method="PUT")
    urllib.request.urlopen(req, timeout=30).read()
    status, r = _post(f"{httpd}/api/cursos/testcurso/componentes", COMPONENTES)
    assert status == 200 and r["completo"]
    status, r = _post(f"{httpd}/api/cursos/testcurso/construir")
    assert status == 200, r
    assert r["fuentes"] == 1 and r["fragmentos"] >= 1
    assert "prompt" in r and len(r["prompt"]) > 100
    # el curso quedó listo y con grafo generado
    with urllib.request.urlopen(f"{httpd}/api/cursos/testcurso/grafo", timeout=10) as resp:
        grafo = json.loads(resp.read().decode())
    assert grafo["cadenas"], "el grafo no se generó en /construir"
