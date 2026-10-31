"""Flujo completo modo compañía por HTTP (H-10.4, T-10.3.1).

Un curso con modo: compania registra recuerdos episódicos en caliente al
recibir mensajes y los deja citable y asociativamente recuperables.
"""
import json
import threading
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from datito import servidor
from datito.indice import Indice

BASE = "http://127.0.0.1"


def _post(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())


@pytest.fixture
def httpd_compania(tmp_path_curso, tmp_path, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    tmp_path_curso.datos["modo"] = "compania"
    tmp_path_curso.guardar()
    ind = Indice()
    ind.registrar_recuerdo(
        "Rufo es el perro de la persona; duerme a su lado en las noches.",
        "semilla:rufo")
    ind.guardar(tmp_path_curso.ruta(".indice"))
    tmp_path_curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}", tmp_path_curso
    server.shutdown()


def test_mensajes_registra_recuerdo_en_caliente(httpd_compania):
    base, curso = httpd_compania
    s, r = _post(base + "/api/cursos/testcurso/mensajes",
                 {"texto": "Mi perro Rufo estuvo enfermo ayer "
                           "y lo lleve al veterinario Fuentes."})
    assert s == 200 and r["modo"] == "compania"
    ind = Indice.cargar(curso.ruta(".indice"))
    nuevas = [f for f in ind.textos
              if f.startswith("memoria#") and f != "memoria#1"]
    assert nuevas, "el recuerdo del mensaje quedó persistido en .indice/"
    assert any("veterinario" in ind.textos[f] for f in nuevas)


def test_recuerdo_queda_citable_y_contrato_intacto(httpd_compania):
    base, curso = httpd_compania
    _post(base + "/api/cursos/testcurso/mensajes",
          {"texto": "Mi perro Rufo estuvo enfermo ayer "
                    "y lo lleve al veterinario Fuentes."})
    s, r = _post(base + "/api/cursos/testcurso/mensajes",
                 {"texto": "como esta mi perro"})
    assert s == 200
    fids = [e["fid"] for e in r["evidencia"]]
    assert any(f.startswith("memoria#") for f in fids)
    # el contrato del response no cambia: mismos campos de siempre
    for campo in ("estado_interaccion", "sin_fuente", "fuera_del_curso",
                  "duda_registrada", "evidencia", "respuesta", "modo"):
        assert campo in r
