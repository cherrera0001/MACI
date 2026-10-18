"""Tests del servidor HTTP (stdlib) con curso en tmp."""
import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest
import yaml

from termito import servidor
from termito.indice import Indice
from termito import fragmentos as frag
from termito import identidad, progreso

from conftest import COMPONENTES_OK

BASE = "http://127.0.0.1"


def _get(url):
    with urllib.request.urlopen(url, timeout=10) as r:
        return r.status, json.loads(r.read().decode())


def _post(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())


@pytest.fixture
def httpd(tmp_path_curso, tmp_path, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    # curso con material e indice
    mat = tmp_path / "mat"
    mat.mkdir()
    (mat / "clase.md").write_text(
        "**[0:05:10]** El overfitting memoriza el entrenamiento y falla en prueba.\n\n"
        "# Underfitting\n\n"
        "**[0:06:00]** El underfitting ni siquiera aprende el patron del entrenamiento.\n\n"
        "# La brecha\n\n"
        "**[0:07:00]** La brecha entre entrenamiento y prueba mide el sobreajuste.\n",
        encoding="utf-8")
    destino = tmp_path_curso.ruta("materiales", "clase.md")
    destino.symlink_to(mat / "clase.md")
    identidad.guardar(tmp_path_curso, COMPONENTES_OK)
    fuentes, frags = frag.parsear_materiales([destino])
    Indice().construir(frags).guardar(tmp_path_curso.ruta(".indice"))
    tmp_path_curso.transicionar("listo")
    # ítem de distincion
    item = {"id": "d1", "conceptos": ["overfitting_underfitting", "generalizacion"],
            "pregunta": "¿cuál memoriza?", "criterios": ["menciona overfitting"],
            "solucion": "el que memoriza"}
    (tmp_path_curso.ruta("evaluaciones") / "d.yaml").write_text(
        yaml.safe_dump({"items": [item]}, allow_unicode=True), encoding="utf-8")
    # grafo mínimo
    g = {"cadenas": {"cadena uno": ["overfitting_underfitting"]},
         "conceptos": {"overfitting_underfitting": {"nombre": "Overfitting",
                     "requiere_antes": [], "habilita": []}}}
    (tmp_path_curso.ruta("grafo") / "grafo.yaml").write_text(
        yaml.safe_dump(g, allow_unicode=True), encoding="utf-8")

    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}"
    server.shutdown()


def test_salud_y_lista(httpd):
    s, salud = _get(httpd + "/api/salud")
    assert s == 200 and salud["modo"] in ("tutor", "exploracion")
    s, cursos = _get(httpd + "/api/cursos")
    assert any(c["slug"] == "testcurso" for c in cursos["cursos"])


def test_crear_curso_por_api(httpd):
    s, r = _post(httpd + "/api/cursos", {"slug": "webcurso", "nombre": "Web"})
    assert s == 201 and r["slug"] == "webcurso"


def test_mensajes_con_evidencia(httpd):
    s, r = _post(httpd + "/api/cursos/testcurso/mensajes",
                 {"texto": "¿qué es el overfitting?"})
    assert s == 200
    assert r["evidencia"] and r["evidencia"][0]["fid"].startswith("clase#")
    assert "modo" in r


def test_fragmento_y_evaluacion(httpd):
    from urllib.parse import quote
    s, r = _post(httpd + "/api/cursos/testcurso/mensajes",
                 {"texto": "overfitting"})
    fid = r["evidencia"][0]["fid"]
    s, f = _get(httpd + f"/api/cursos/testcurso/fragmento?fid={quote(fid)}")
    assert s == 200 and "memoriza" in f["texto"]
    s, ev = _get(httpd + "/api/cursos/testcurso/evaluacion")
    assert len(ev["items"]) == 1
    s, res = _post(httpd + "/api/cursos/testcurso/evaluacion",
                   {"item_id": "d1", "respuesta": "el overfitting memoriza"})
    assert s == 200 and res["resultado"] == "logrado"
    assert res["sesion"]["n"] == 1
    s, panel = _get(httpd + "/api/cursos/testcurso/grafo")
    nodo = panel["cadenas"][0]["nodos"][0]
    assert nodo["estado"] == "dominado" and nodo["visible"]


def test_estaticos(httpd):
    with urllib.request.urlopen(httpd + "/", timeout=10) as r:
        html = r.read().decode()
    assert "Termito" in html and "chat.html" in html


def _post_raw(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")


def test_mensajes_campos_contrato(httpd):
    s, r = _post(httpd + "/api/cursos/testcurso/mensajes",
                 {"texto": "¿qué es el overfitting?"})
    for campo in ("estado_interaccion", "sin_fuente", "fuera_del_curso",
                  "duda_registrada", "evidencia", "respuesta", "modo"):
        assert campo in r, f"falta {campo}"
    assert r["sin_fuente"] is False
    assert r["estado_interaccion"] == "revision"


def test_flujo_lucha_por_api(httpd):
    base = httpd + "/api/cursos/testcurso"
    s, r = _post(base + "/mensajes",
                 {"texto": "Ejercicio: mi modelo memoriza todo el entrenamiento "
                           "y falla en prueba, ¿qué le pasa?"})
    assert r["estado_interaccion"] == "pista" and r["evidencia"] == []
    s, r = _post(base + "/mensajes", {"texto": "pista"})
    assert r["estado_interaccion"] == "paso_mostrado"
    assert r["paso"]["numero"] == 1 and len(r["evidencia"]) == 1
    s, r = _post(base + "/mensajes", {"texto": "dame la respuesta"})
    assert r["estado_interaccion"] == "esperando_intento"
    s, e = _post_raw(base + "/mensajes/1/revelar", {"consentimiento": True})
    assert s == 409 and e["error"] == "aun_no"
    s, r = _post(base + "/mensajes",
                 {"texto": "mi intento: está sobreajustado, la brecha es grande"})
    assert r["estado_interaccion"] == "revision"
    s, r = _post(base + "/mensajes/1/revelar", {"consentimiento": True})
    assert s == 200 and r["registro"]["tipo"] == "solucion"
    assert r["evidencia"]


def test_revelar_sin_sesion_404(httpd):
    s, e = _post_raw(httpd + "/api/cursos/testcurso/mensajes/9/revelar",
                     {"consentimiento": True})
    assert s == 404 and e["error"] == "sin_sesion"


def test_mensajes_subruta_desconocida(httpd):
    s, e = _post_raw(httpd + "/api/cursos/testcurso/mensajes/xyz/foo", {})
    assert s == 404 and e["error"] == "ruta_desconocida"


def test_componentes_acepta_put_y_post(httpd):
    import urllib.request
    url = httpd + "/api/cursos/testcurso/componentes"
    cuerpo = json.dumps({"rol_dominio": "Tutor de prueba PUT"}).encode()
    # PUT (contrato api.md)
    req = urllib.request.Request(url, data=cuerpo, method="PUT",
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        s, res = r.status, json.loads(r.read().decode())
    assert s == 200 and "completo" in res
    # POST (wizard legacy)
    s, res = _post(url, {"mision": "Misión POST"})
    assert s == 200
    # ambas escrituras quedaron persistidas
    s, curso = _get(httpd + "/api/cursos/testcurso")
    assert curso["componentes"]["rol_dominio"] == "Tutor de prueba PUT"
    assert curso["componentes"]["mision"] == "Misión POST"


def test_notas_registro_exportar(httpd):
    base = httpd + "/api/cursos/testcurso"
    s, r = _post(base + "/notas", {"evaluacion": "Certamen 1", "nota": "3.4",
                                   "observaciones": "me faltó tiempo"})
    assert s == 200 and r["ajustes_derivados"]
    s, e = _post_raw(base + "/notas", {"evaluacion": "x", "nota": ""})
    assert s == 422
    s, r = _get(base + "/registro")
    assert s == 200 and r["notas"] == 1 and "dudas" in r
    s, r = _post(base + "/exportar", {})
    assert s == 202 and r["ruta"].endswith(".term.zip")


def test_cerrar_bloquea_chat_mantiene_registro(httpd):
    base = httpd + "/api/cursos/testcurso"
    s, r = _post(base + "/cerrar", {})
    assert s == 200 and r["estado"] == "cerrado" and r["registro_integro"]
    s, e = _post_raw(base + "/mensajes", {"texto": "hola"})
    assert s == 409 and e["error"] == "termito_cerrado"
    s, r = _get(base + "/registro")
    assert s == 200


def test_importar_endpoint(httpd):
    import shutil
    from termito import config
    base = httpd + "/api/cursos/testcurso"
    s, r = _post(base + "/exportar", {})
    s, e = _post_raw(httpd + "/api/importar", {"ruta": r["ruta"]})
    assert s == 422                       # el slug ya existe en esta máquina
    shutil.rmtree(config.DIR_CURSOS / "testcurso")
    s, r2 = _post(httpd + "/api/importar", {"ruta": r["ruta"]})
    assert s == 201 and r2["slug"] == "testcurso"
