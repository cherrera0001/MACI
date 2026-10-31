"""E2E con navegador real: los viajes del usuario contra un servidor efímero.

Cubre exactamente los bugs que la suite unitaria no pudo ver: un SyntaxError
en el script inline (página muerta), el race del micrófono y flujos rotos de
UI. Requiere node + playwright-core (`npm install` en tests/e2e) y el binario
de Chromium del sistema (ver tests/e2e/setup-chrome-libs.sh para las
dependencias sin root). Sin esos binarios, el test se omite (skip): no frena
CI, pero en la máquina de desarrollo valida lo que una persona vería.
"""
import json
import os
import shutil
import subprocess
import threading
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

E2E = Path(__file__).resolve().parent / "e2e"


def _herramientas():
    node = shutil.which("node")
    if not node or not (E2E / "node_modules" / "playwright-core").is_dir():
        return None
    chrome = (Path.home()
              / ".cache/ms-playwright/chromium-1248/chrome-linux64/chrome")
    if not chrome.exists():
        alternativas = sorted((Path.home() / ".cache/ms-playwright")
                              .glob("chromium-*/chrome-linux*/chrome"))
        chrome = alternativas[-1] if alternativas else None
    libs = E2E / "root/usr/lib/x86_64-linux-gnu"
    return {"node": node, "chrome": str(chrome) if chrome else None,
            "ld": str(libs) if libs.is_dir() else None}


@pytest.fixture
def httpd_compania(tmp_path_curso, monkeypatch):
    from datito import servidor
    from datito.indice import Indice

    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    curso = tmp_path_curso
    curso.datos["modo"] = "compania"
    curso.guardar()
    ind = Indice()
    ind.registrar_recuerdo("Su perrito Rufo la esperaba en la puerta",
                           referencia="sesion e2e")
    ind.guardar(curso.ruta(".indice"))
    curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"http://127.0.0.1:{server.server_address[1]}", curso.slug
    server.shutdown()


def test_e2e_viajes_del_usuario(httpd_compania):
    herr = _herramientas()
    if herr is None or not herr["chrome"]:
        pytest.skip("sin node/playwright-core/chromium: ver tests/e2e/README")

    base, slug = httpd_compania
    env = dict(os.environ, BASE=base, SLUG=slug, CHROME=herr["chrome"])
    if herr["ld"]:
        env["LD_LIBRARY_PATH"] = herr["ld"] + os.pathsep \
            + env.get("LD_LIBRARY_PATH", "")
    proc = subprocess.run(
        [herr["node"], str(E2E / "validar.mjs")],
        capture_output=True, text=True, timeout=180, env=env, cwd=str(E2E))
    print(proc.stdout)
    assert proc.returncode == 0, \
        f"viajes E2E fallaron\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr[-2000:]}"
    assert "todos los viajes ok" in proc.stdout
