"""Guía de instalación de Ollama (H-9.1 / T-9.1.1, decisión D-7.1)."""
import json
import sys
import threading
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from datito import servidor

BASE = "http://127.0.0.1"


@pytest.fixture
def httpd(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"{BASE}:{server.server_address[1]}"
    server.shutdown()


def test_salud_incluye_guia_cuando_no_hay_llm(httpd):
    with urllib.request.urlopen(f"{httpd}/api/salud", timeout=10) as r:
        s = json.loads(r.read().decode())
    assert s["modo"] == "exploracion"
    guia = s.get("guia")
    if guia is None:
        pytest.skip("hay un LLM corriendo en esta máquina: la guía no aplica")
    esperado = {"linux": "linux", "darwin": "macos", "win32": "windows"}.get(
        sys.platform, "linux")
    assert guia["so"] == esperado
    assert len(guia["pasos"]) == 2
    assert any("qwen2.5:3b" in p for p in guia["pasos"])
    # los pasos son comandos legibles, no vacíos
    assert all(isinstance(p, str) and len(p) > 10 for p in guia["pasos"])
