"""Lección de evidencia viva (H-8.1 / T-8.1.1–T-8.1.2)."""
import json
import threading
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

from datito import demo_brecha, servidor

BASE = "http://127.0.0.1"
WEB = Path(__file__).parent.parent / "src" / "web"


def test_escenario_determinista_misma_semilla():
    r1, r2 = demo_brecha.correr(42), demo_brecha.correr(42)
    assert r1["salida"] == r2["salida"]
    assert r1["eventos"] == ["paso-1-rendimiento", "paso-2-brechas",
                             "paso-3-etiquetado"]


def test_semilla_distinta_numeros_distintos():
    r1, r2 = demo_brecha.correr(42), demo_brecha.correr(7)
    assert r1["salida"] != r2["salida"]  # mismo procedimiento, otros datos


def test_etiquetado_despues_de_la_brecha():
    r = demo_brecha.correr(42)
    assert r["eventos"].index("paso-2-brechas") < r["eventos"].index("paso-3-etiquetado")
    assert "A brecha=+1.00" in r["salida"] and "A sobreajusta" in r["salida"]


@pytest.fixture
def httpd(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}"
    server.shutdown()


def test_endpoint_demo_brecha(httpd):
    with urllib.request.urlopen(f"{httpd}/api/demo/brecha?semilla=42", timeout=30) as r:
        datos = json.loads(r.read().decode())
    assert datos["semilla"] == 42 and datos["codigo_salida"] == 0
    assert datos["eventos"][0] == "paso-1-rendimiento"


def test_endpoint_demo_brecha_semilla_invalida_cae_a_42(httpd):
    with urllib.request.urlopen(f"{httpd}/api/demo/brecha?semilla=abc", timeout=30) as r:
        datos = json.loads(r.read().decode())
    assert datos["semilla"] == 42


def test_pagina_evidencia_servida_y_embebe_la_referencia_real(httpd):
    with urllib.request.urlopen(f"{httpd}/evidencia-brecha.html", timeout=10) as r:
        html = r.read().decode()
    assert "84b485dd" in html            # la captura REA de referencia citada
    assert "A: R2 train=1.00 test=-0.00" in html  # números reales embebidos
    assert "brecha=+1.00" in html
    assert "/api/demo/brecha" in html    # el botón re-ejecutar apunta al endpoint
