"""E-16: STT local, Kokoro + A/B de voces, tokens de un solo uso y evaluadores.

Cubre H-16.1 (audio nunca sale de la máquina), H-16.2 (A/B ciego de voces),
H-16.3 (panel familiar con dispositivo vinculado), D-16.3 (threat model) y
los bancos de medición (eval_conversacion pre-registrado, banco D-15.3 a
20 sondas). Todo en cursos temporales; los tests corren con y sin motores.
"""
import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from datito import acceso, cerebro, eval_conversacion, eval_cerebro
from datito import servidor, stt, voz
from datito.indice import Indice

BASE = "http://127.0.0.1"


def _curso_compania(tmp_path_curso):
    tmp_path_curso.datos["modo"] = "compania"
    tmp_path_curso.datos["cerebro"] = "aal"
    tmp_path_curso.guardar()
    ind = Indice()
    ind.registrar_recuerdo("Su perrito Rufo la esperaba en la puerta",
                           referencia="sesion prueba")
    ind.guardar(tmp_path_curso.ruta(".indice"))
    return tmp_path_curso, ind


# ------------------------------------------------------------------ stt
def test_stt_info_degradacion():
    i = stt.info()
    assert set(("activo", "motor", "modelo")) <= set(i)
    assert i["activo"] in (True, False)
    if not stt.disponible():
        assert i["guia"] and "faster-whisper" in i["guia"]


def test_stt_transcribir_sin_motor(monkeypatch):
    monkeypatch.setattr(stt, "DISPONIBLE", False)
    assert stt.transcribir(b"RIFFxxxx") is None


@pytest.mark.skipif(not stt.disponible(), reason="faster-whisper no instalado")
def test_stt_transcribir_audio_real():
    if not voz.disponible():
        pytest.skip("se necesita un motor TTS para fabricar el audio")
    audio = voz.sintetizar("Hola, que alegria escucharla", motor="auto")
    texto = stt.transcribir(audio)
    assert texto and "alegr" in texto.lower()


# --------------------------------------------------------------- voz AB
def test_voz_motores_info():
    i = voz.info()
    assert "motores" in i and set(("piper", "kokoro")) <= set(i["motores"])
    assert i["neuronal"] == any(i["motores"].values())


def test_voz_resolver_motor_por_curso(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(voz, "_DETECTADO", {"piper": True, "kokoro": False})
    assert voz.resolver_motor(tmp_path_curso) == "piper"
    tmp_path_curso.datos["voz"] = "kokoro"
    assert voz.resolver_motor(tmp_path_curso) is None, "kokoro no instalado"
    assert voz.resolver_motor(tmp_path_curso, "piper") == "piper"
    monkeypatch.setattr(voz, "_DETECTADO", {"piper": True, "kokoro": True})
    assert voz.resolver_motor(tmp_path_curso) == "kokoro"


# -------------------------------------------------------------- acceso
def test_token_un_solo_uso(tmp_path_curso):
    curso, _ = _curso_compania(tmp_path_curso)
    assert acceso.activada(curso) is False
    assert acceso.autorizado(curso, None) is True, "sin seguridad: abierto"
    token = acceso.emitir(curso, "tablet del cuidador")
    assert acceso.activada(curso) is True
    d1 = acceso.canjear(curso, token)
    assert d1 and acceso.autorizado(curso, d1)
    assert acceso.canjear(curso, token) is None, "no reutilizable"
    assert acceso.canjear(curso, "token-falso") is None
    assert not acceso.autorizado(curso, "desconocido")
    assert acceso.revocar(curso, d1) is True
    assert not acceso.autorizado(curso, d1)


def test_verificar_o_error_headers(tmp_path_curso):
    curso, _ = _curso_compania(tmp_path_curso)
    assert acceso.verificar_o_error(curso, {}) is None
    acceso.emitir(curso, "")
    token = acceso.emitir(curso, "x")
    device = acceso.canjear(curso, token)
    assert acceso.verificar_o_error(curso, {"X-Device-Id": device}) is None
    assert acceso.verificar_o_error(curso, {}) == "faltante"
    assert acceso.verificar_o_error(curso, {"X-Device-Id": "otro"}) == "otro"


# ----------------------------------------------------------- evaluadores
def test_eval_conversacion_estructura_y_preregistro():
    r = eval_conversacion.correr()
    assert r["turnos"] == 20
    assert r["validacion"] == 1.0, "cero citas inválidas en todo el guion"
    assert r["latencia_s"]["total"]["p95"] is not None
    for etapa in ("stt", "intercambio", "cerebro"):
        assert etapa in r["latencia_s"]
    assert r["naturalidad_media"] >= 1.0
    if r["inconcluso_por"]:
        # veredicto honesto: nunca éxito con etapas sin medir
        assert r["exito_preregistrado"] is False
        assert "INCONCLUSO" in r["veredicto"]
    else:
        assert r["exito_preregistrado"] is True
        assert "CUMPLE" in r["veredicto"]


def test_banco_d15_ampliado_a_20_sondas():
    assert len(eval_cerebro.SONDAS) == 20
    n_cross = sum(1 for s in eval_cerebro.SONDAS if s.cross)
    n_obj = sum(1 for s in eval_cerebro.SONDAS if s.objetivo)
    assert n_cross == 4 and n_obj == 10


def test_banco_d15_redecision_honesta():
    r = eval_cerebro.comparar()
    assert r["n_sondas"] == 20
    b, c = r["baseline"], r["cerebro"]
    assert b["validez"] == 1.0 and c["validez"] == 1.0
    assert r["repeticion"]["rufo_unico"] is True
    assert r["decision"] in ("adoptar", "opt_in")
    if r["decision"] == "adoptar":
        assert c["rechazo_senuelos"] > b["rechazo_senuelos"] \
            or c["mrr"] > b["mrr"] or c["p3"] > b["p3"]
    else:  # opt_in: debe haber regresión en alguna métrica o falta mejora
        regresion = any(c[m] < b[m] for m in ("mrr", "p3", "rechazo_senuelos"))
        mejora = any(c[m] > b[m] for m in ("mrr", "p3", "rechazo_senuelos"))
        assert regresion or not mejora


# ------------------------------------------------------------- HTTP
def _post(url, datos=None, headers=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json", **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())


def _get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.status, json.loads(r.read().decode())


@pytest.fixture
def httpd_e16(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    curso, ind = _curso_compania(tmp_path_curso)
    curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}", curso, ind
    server.shutdown()


def test_http_salud_reporta_stt_y_voz(httpd_e16):
    base, _, _ = httpd_e16
    s, r = _get(base + "/api/salud")
    assert s == 200 and "stt" in r and "cerebro" in r
    assert r["stt"]["activo"] in (True, False)
    assert set(("piper", "kokoro")) <= set(r["voz"]["motores"])


@pytest.mark.skipif(not stt.disponible(), reason="faster-whisper no instalado")
def test_http_stt_roundtrip_local(httpd_e16):
    base, _, _ = httpd_e16
    if not voz.disponible():
        pytest.skip("se necesita motor TTS para fabricar audio")
    audio = voz.sintetizar("Hola que tal", motor="auto")
    req = urllib.request.Request(base + "/api/stt", data=audio,
                                 headers={"Content-Type": "audio/wav"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode())
    assert "texto" in d and d["texto"]


def test_http_familiar_exige_dispositivo_cuando_seguridad_activa(httpd_e16):
    base, curso, _ = httpd_e16
    s, r = _get(base + "/api/cursos/testcurso/familiar")
    assert s == 200, "sin seguridad activada: abierto como antes"
    token = acceso.emitir(curso, "test")
    try:
        _get(base + "/api/cursos/testcurso/familiar")
        assert False, "debió exigir dispositivo"
    except urllib.error.HTTPError as e:
        assert e.code == 401
    device = acceso.canjear(curso, token)
    s, r = _get(base + "/api/cursos/testcurso/familiar",
                headers={"X-Device-Id": device})
    assert s == 200 and "pulso" in r


def test_http_mensajes_exige_dispositivo(httpd_e16):
    base, curso, _ = httpd_e16
    token = acceso.emitir(curso, "test")
    device = acceso.canjear(curso, token)
    try:
        _post(base + "/api/cursos/testcurso/mensajes",
              {"texto": "hola"}, headers={"X-Device-Id": "otro"})
        assert False, "debió rechazar"
    except urllib.error.HTTPError as e:
        assert e.code == 401
    s, r = _post(base + "/api/cursos/testcurso/mensajes",
                 {"texto": "Cuénteme de mi perrito Rufo"},
                 headers={"X-Device-Id": device})
    assert s == 200 and "respuesta" in r


def test_http_voz_asignacion_y_voto(httpd_e16):
    base, curso, _ = httpd_e16
    s, r = _get(base + "/api/cursos/testcurso/voz")
    assert s == 200 and "asignacion" in r and "motores" in r
    if len(r["motores"]) > 1:
        assert r["asignacion"] in r["motores"]
        s, p = _post(base + "/api/cursos/testcurso/voz-preferencia",
                     {"eleccion": r["asignacion"]})
        assert s == 200
        assert p["preferencia"].get(r["asignacion"]) == 1


def test_http_vincular_token_invalido(httpd_e16):
    base, _, _ = httpd_e16
    try:
        _post(base + "/api/cursos/testcurso/vincular", {"token": "falso"})
        assert False, "debió rechazar"
    except urllib.error.HTTPError as e:
        assert e.code == 401


# --------------------------------------------------------------- UI
def test_chat_html_usa_media_recorder_y_no_speechrecognition():
    html = open(servidor.RUTA_WEB.joinpath("chat.html")
                if hasattr(servidor, "RUTA_WEB") else
                __import__("pathlib").Path(servidor.__file__).parent.parent
                / "web" / "chat.html", encoding="utf-8").read()
    assert "MediaRecorder" in html
    assert "webkitSpeechRecognition" not in html
    assert "SpeechRecognition ||" not in html
    assert "/api/stt" in html
    assert "voz-preferencia" in html and "Me gustó esta voz" in html


def test_api_js_envia_device_id_y_vincula():
    js = (__import__("pathlib").Path(servidor.__file__).parent.parent
          / "web" / "js" / "api.js").read_text(encoding="utf-8")
    assert "X-Device-Id" in js and "datito_device" in js
    assert "solicitarVinculo" in js and "/vincular" in js


def test_threat_model_existe_con_matriz():
    from pathlib import Path

    doc = Path(__file__).resolve().parents[2] / "docs" / "gestion" / "THREAT_MODEL.md"
    assert doc.exists(), "docs/gestion/THREAT_MODEL.md (D-16.3)"
    texto = doc.read_text(encoding="utf-8")
    assert "quién-puede-leer-qué" in texto or "quién puede leer qué" in texto
    assert "X-Device-Id" in texto and "seguridad.yaml" in texto
