"""E-12: voz neuronal, consolidación hipocampal, reminiscencia y legado."""
import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from datito import biografia, guardian, memoria, servidor, voz
from datito.indice import Indice

BASE = "http://127.0.0.1"


def _indice_rica():
    ind = Indice()
    ind.registrar_recuerdo(
        "Rufo es el perro de la persona; vive con ella desde cachorro y le "
        "hace compania en las mananas.", "semilla:rufo")
    ind.registrar_recuerdo(
        "Rufo duerme a su lado en las noches y despierta temprano para "
        "saludarla.", "semilla:rufo-2")
    ind.registrar_recuerdo(
        "La hermana de la persona se llama Carmen y vive en Temuco.",
        "semilla:carmen")
    ind.registrar_recuerdo(
        "Si un mensaje pide claves con urgencia, es estafa: cortar y "
        "consultar con alguien de confianza.", "guia:anti-estafa-1")
    return ind


def _curso_compania(tmp_path_curso):
    tmp_path_curso.datos["modo"] = "compania"
    tmp_path_curso.guardar()
    ind = _indice_rica()
    ind.guardar(tmp_path_curso.ruta(".indice"))
    return tmp_path_curso, ind


# --- voz neuronal (H-12.1) --------------------------------------------------

def test_tts_degradacion_limpia_sin_motor(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(voz, "_MOTOR", False)
    curso, _ = _curso_compania(tmp_path_curso)
    curso.transicionar("listo")
    info = voz.info()
    assert info["neuronal"] is False and "piper" in info["instalar"]


def test_tts_con_motor_mockeado(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(voz, "_MOTOR", ("piper", "/usr/bin/piper"))
    monkeypatch.setattr(voz, "sintetizar", lambda t: b"RIFFfake-wav")
    curso, _ = _curso_compania(tmp_path_curso)
    curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        req = urllib.request.Request(
            f"{BASE}:{server.server_address[1]}/api/cursos/testcurso/tts",
            data=json.dumps({"texto": "hola"}).encode(),
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as r:
            assert r.status == 200
            assert r.headers.get("Content-Type") == "audio/wav"
            assert r.read().startswith(b"RIFF")
    finally:
        server.shutdown()


def test_tts_sin_motor_responde_404(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(voz, "_MOTOR", False)
    monkeypatch.setattr(servidor.voz, "_MOTOR", False)
    _curso_compania(tmp_path_curso)[0].transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        req = urllib.request.Request(
            f"{BASE}:{server.server_address[1]}/api/cursos/testcurso/tts",
            data=json.dumps({"texto": "hola"}).encode(),
            headers={"Content-Type": "application/json"})
        with pytest.raises(urllib.error.HTTPError) as e:
            urllib.request.urlopen(req, timeout=10)
        assert e.value.code == 404
        assert json.loads(e.value.read())["error"] == "voz_no_disponible"
    finally:
        server.shutdown()


# --- consolidación hipocampal (H-12.2) --------------------------------------

def test_consolidacion_deduplica_recuerdos():
    ind = _indice_rica()
    n_antes = len([f for f in ind.textos if f.startswith("memoria#")])
    duplicado = ("Rufo es el perro de la persona; vive con ella desde "
                 "cachorro y le hace compania en las mananas, como siempre.")
    fid = ind.consolidar_recuerdo(duplicado, "sesion hoy")
    assert fid.startswith("memoria#")
    n_despues = len([f for f in ind.textos if f.startswith("memoria#")])
    assert n_despues == n_antes, "el relato repetido no infla el índice"
    assert "como siempre" in ind.textos[fid], "la memoria se enriquece"


def test_consolidacion_crea_nuevo_si_es_distinto():
    ind = _indice_rica()
    n_antes = len([f for f in ind.textos if f.startswith("memoria#")])
    fid = ind.consolidar_recuerdo("Descubrio una nueva plaza cerca de su "
                                  "casa con flores amarillas", "sesion hoy")
    n_despues = len([f for f in ind.textos if f.startswith("memoria#")])
    assert n_despues == n_antes + 1


def test_mapa_de_entidades():
    ind = _indice_rica()
    ents = memoria.entidades(ind)
    assert "rufo" in ents and len(ents["rufo"]) >= 2


# --- reminiscencia guiada (H-12.3) ------------------------------------------

def test_reminiscencia_tres_pistas_con_cita_validada(tmp_path_curso):
    from datito import evidencia, reminiscencia
    curso, ind = _curso_compania(tmp_path_curso)
    r1 = reminiscencia.siguiente(curso, ind, nueva=True)
    assert r1["pista_n"] == 1 and r1["total"] == 3
    assert "tiene que ver con" in r1["pista"]
    assert ind.textos[r1["fid"]] not in r1["pista"], "la pista 1 no revela"
    r2 = reminiscencia.siguiente(curso, ind)
    assert r2["pista_n"] == 2 and "…" in r2["pista"]
    r3 = reminiscencia.siguiente(curso, ind)
    assert r3["pista_n"] == 3 and r3["completa"]
    if f"[{r3['fid']}]" in r3["pista"]:
        assert evidencia.validar(r3["pista"], ind).ok, "la pista final cita y valida"


# --- bitácora de vida (H-12.4) ----------------------------------------------

def test_biografia_agrupa_por_entidades_sin_alertas(tmp_path_curso):
    curso, ind = _curso_compania(tmp_path_curso)
    guardian.registrar_alerta(curso, {"nivel": "alerta", "senales": ["caida"]})
    bio = biografia.construir(curso, ind)
    assert "rufo" in bio["entidades"] and len(bio["entidades"]["rufo"]) >= 2
    for grupo in bio["entidades"].values():
        for item in grupo:
            assert item["fid"] in ind.textos
    assert bio["alertas"] == 0
    texto = json.dumps(bio, ensure_ascii=False)
    assert "guia:" not in texto and "caida" not in texto, \
        "ni guías ni alertas filtradas entran al legado"
