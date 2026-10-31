"""Presencia activa (apertura) y guardián anti-fraude/bienestar (E-11).

Cubre H-11.1, H-11.2 (lado servidor) y H-11.3. Todo sin Ollama.
"""
import datetime
import json
import threading
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from datito import apertura, guardian, progreso
from datito import servidor
from datito.indice import Indice

BASE = "http://127.0.0.1"


def _indice_con_guias():
    ind = Indice()
    ind.registrar_recuerdo(
        "Rufo es el perro de la persona; duerme a su lado en las noches.",
        "semilla:rufo")
    ind.registrar_recuerdo(
        "A la persona le gusta tejer bufandas para sus nietas en las tardes "
        "de invierno.", "semilla:tejido")
    ind.registrar_recuerdo(
        "Si un mensaje o llamada pide claves, contraseñas o dinero con "
        "urgencia, es estafa: cortar, no compartir nada y consultar con "
        "alguien de confianza.", "guia:anti-estafa-1")
    ind.registrar_recuerdo(
        "La rutina de la persona: te en las tardes y llamar a su hermana "
        "los domingos; la rutina la mantiene tranquila.", "guia:bienestar")
    return ind


def _curso_compania(tmp_path_curso):
    tmp_path_curso.datos["modo"] = "compania"
    tmp_path_curso.guardar()
    ind = _indice_con_guias()
    ind.guardar(tmp_path_curso.ruta(".indice"))
    return tmp_path_curso, ind


def _forzar_ausencia(curso, horas):
    datos = progreso.cargar(curso)
    datos["ultima_interaccion"] = (
        datetime.datetime.now() - datetime.timedelta(hours=horas)
    ).isoformat(timespec="seconds")
    progreso.guardar(curso, datos)


# --- apertura proactiva (H-11.1) -------------------------------------------

def test_apertura_primera_vez_evoca_recuerdo_validado(tmp_path_curso):
    curso, ind = _curso_compania(tmp_path_curso)
    a = apertura.calcular(curso, ind)
    assert a["modo"] == "compania" and a["horas"] is None
    assert "empieza" in a["saludo"]
    assert a["recuerdo"] and a["recuerdo"]["fid"].startswith("memoria#")
    from datito import evidencia
    val = evidencia.validar(
        f"Recuerdo que {a['recuerdo']['texto']} [{a['recuerdo']['fid']}]", ind)
    assert val.ok, "el recuerdo de apertura cita y valida"


def test_apertura_menos_de_6h_no_evoca(tmp_path_curso):
    curso, ind = _curso_compania(tmp_path_curso)
    _forzar_ausencia(curso, 2)
    a = apertura.calcular(curso, ind)
    assert a["horas"] < 6 and a["recuerdo"] is None


def test_apertura_round_robin_y_excluye_guias(tmp_path_curso):
    curso, ind = _curso_compania(tmp_path_curso)
    vistos = set()
    for _ in range(4):
        _forzar_ausencia(curso, 30)
        a = apertura.calcular(curso, ind)
        fid = a["recuerdo"]["fid"]
        vistos.add(fid)
        assert not ind.referencias[fid][1].startswith("guia:")
    assert len(vistos) >= 2, "la evocación rota entre memorias"


# --- guardián determinista (H-11.3, unitario) ------------------------------

def test_guardian_fraude():
    r = guardian.evaluar(
        "Me pidieron mi clave del banco por un premio urgente")
    assert r["nivel"] == "fraude" and "clave" in r["senales"]


def test_guardian_alerta_y_ok():
    assert guardian.evaluar("Me caí y no puedo levantarme, ayuda")["nivel"] \
        == "alerta"
    assert guardian.evaluar("me siento solo hoy")["nivel"] == "ok"


# --- flujo HTTP (servidor) --------------------------------------------------

def _post(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())


@pytest.fixture
def httpd_guardian(tmp_path_curso, tmp_path, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    curso, _ = _curso_compania(tmp_path_curso)
    curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}", curso
    server.shutdown()


def test_apertura_por_http(httpd_guardian):
    base, _ = httpd_guardian
    s, a = _get(base + "/api/cursos/testcurso/apertura")
    assert s == 200 and a["recuerdo"] and a["modo"] == "compania"


def _get(url):
    with urllib.request.urlopen(url, timeout=10) as r:
        return r.status, json.loads(r.read().decode())


def test_fraude_recibe_guia_citada(httpd_guardian):
    base, _ = httpd_guardian
    s, r = _post(base + "/api/cursos/testcurso/mensajes",
                 {"texto": "Me pidieron mi clave del banco por un premio "
                           "urgente y no se que hacer"})
    assert s == 200
    assert "estafa" in r["respuesta"]
    guias = [e["fid"] for e in r["evidencia"]
             if e["referencia"].startswith("guia:")]
    assert guias, "la protección va anclada a una guía citada"
    assert "[" + guias[0] + "]" in r["respuesta"]


def test_alerta_queda_en_registro(httpd_guardian):
    base, curso = httpd_guardian
    s, r = _post(base + "/api/cursos/testcurso/mensajes",
                 {"texto": "Me caí y no puedo levantarme, ayuda por favor"})
    assert s == 200
    assert curso.ruta("alertas.yaml").exists()
    s, reg = _get(base + "/api/cursos/testcurso/registro")
    assert reg["alertas"] >= 1 and reg["ultima_alerta"]["tipo"] == "bienestar"
    # privacidad: la alerta guarda señales, no el mensaje completo
    assert "texto" not in reg["ultima_alerta"]


def test_conversacion_normal_no_genera_alertas(httpd_guardian):
    base, curso = httpd_guardian
    _post(base + "/api/cursos/testcurso/mensajes",
          {"texto": "Hoy desayuné pan con mermelada y vi el sol"})
    assert not curso.ruta("alertas.yaml").exists()
