"""Micro-talleres prácticos y panel familiar (E-14).

Cubre H-14.1 (pasos con cita validada, ayuda sin penalización, celebración
con memoria), H-14.2 (/familiar sin filtración: alertas solo fecha+tipo),
H-14.3 (vista familiar imprimible) y la regresión fuera de modo compañía.
Todo sin Ollama y sin tocar cursos/ reales.
"""
import json
import threading
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest
import yaml

from datito import evidencia, guardian, progreso, servidor, talleres
from datito.indice import Indice

RAIZ = Path(__file__).resolve().parents[1]
BASE = "http://127.0.0.1"

GUIA_ESTAFA = ("Si un mensaje o llamada pide claves, contraseñas o dinero "
               "con urgencia, es estafa: corte, no comparta nada y consulte "
               "con alguien de confianza.")
GUIA_VIDEO = ("Para ver a su familia por videollamada abra la aplicación "
              "verde de la cámara, toque el nombre de su contacto y elija "
              "el ícono de video; si no contestan, deje un mensaje de voz "
              "con cariño.")

TALLERES_FIXTURE = {
    "talleres": [
        {"id": "anti-estafa-cotidiano",
         "titulo": "Revisar un mensaje sospechoso",
         "tema": "estafa claves banco mensaje urgencia",
         "guia_fid": "",  # se resuelve al montar el fixture
         "pasos": [
             {"objetivo": ("Ante un mensaje que pida claves o contraseñas "
                           "con urgencia, deténgase y no toque enlaces."),
              "ayuda": "Ningún banco pide claves por mensaje; déjelo ahí."},
             {"objetivo": ("Si habla de premio o transferencia, trátelo como "
                           "estafa y corte la comunicación."),
              "ayuda": "«Premio» y «urgente» juntas casi siempre es engaño."},
             {"objetivo": ("Consulte con alguien de confianza antes de "
                           "responder o pagar."),
              "ayuda": "Decidir en compañía siempre es más seguro."}]},
        {"id": "videollamada-familia",
         "titulo": "Videollamar a su familia",
         "tema": "videollamada telefono familia nietas fotos",
         "guia_fid": "",  # se resuelve al montar el fixture
         "pasos": [
             {"objetivo": ("Abra la aplicación de videollamada y toque el "
                           "nombre de su contacto en la lista."),
              "ayuda": "Es el ícono verde de la cámara."},
             {"objetivo": ("Elija el ícono de video para llamar y espere "
                           "con calma a que conteste."),
              "ayuda": "Si no contestan, no pasa nada."},
             {"objetivo": ("Al terminar cuelgue y deje un mensaje de voz "
                           "con cariño."),
              "ayuda": "Repetir otro día la hará más fácil."}]},
        {"id": "taller-guia-rota",
         "titulo": "Taller con guía inexistente",
         "tema": "algo",
         "guia_fid": "memoria#99",
         "pasos": [{"objetivo": "Un paso cualquiera.", "ayuda": "nada"}]},
    ]
}


def _indice_con_todo():
    ind = Indice()
    ind.registrar_recuerdo(
        "Su perro Rufo vive con usted desde que era cachorro.", "semilla:rufo")
    ind.registrar_recuerdo(
        "Guarda las fotos de sus nietas en el teléfono nuevo para "
        "enséñárselas cuando la visitan.", "semilla:fotos")
    fid_estafa = ind.registrar_recuerdo(GUIA_ESTAFA, "guia:anti-estafa-1")
    fid_video = ind.registrar_recuerdo(GUIA_VIDEO, "guia:telefono-videollamada")
    return ind, fid_estafa, fid_video


def _curso_talleres(tmp_path_curso):
    tmp_path_curso.datos["modo"] = "compania"
    tmp_path_curso.guardar()
    ind, fid_estafa, fid_video = _indice_con_todo()
    ind.guardar(tmp_path_curso.ruta(".indice"))
    talleres_dict = yaml.safe_load(yaml.safe_dump(TALLERES_FIXTURE))
    for t in talleres_dict["talleres"]:
        if t["id"] == "anti-estafa-cotidiano":
            t["guia_fid"] = fid_estafa
        if t["id"] == "videollamada-familia":
            t["guia_fid"] = fid_video
    tmp_path_curso.ruta("talleres.yaml").write_text(
        yaml.safe_dump(talleres_dict, allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    return tmp_path_curso, ind


# --- micro-talleres (H-14.1, unitario) --------------------------------------

def test_taller_flujo_tres_pasos_con_citas_validadas(tmp_path_curso):
    curso, ind = _curso_talleres(tmp_path_curso)
    r = talleres.elegir(curso, ind)
    assert r["paso"]["n"] == 1 and r["paso"]["total"] == 3
    assert r["anclaje"], "el anclaje cita la guía"
    assert evidencia.validar(r["paso"]["texto"], ind).ok
    assert evidencia.validar(r["anclaje"], ind).ok
    assert r["paso"]["texto"].count("[") == 1, "el paso lleva su cita [fid]"

    r2 = talleres.avanzar(curso, ind)
    assert r2["paso"]["n"] == 2 and evidencia.validar(r2["paso"]["texto"], ind).ok
    assert "celebracion" in r2 and "siguiente" in r2["celebracion"]

    talleres.avanzar(curso, ind)
    fin = talleres.avanzar(curso, ind)
    assert fin["completado"] is True
    assert "Taller terminado" in fin["celebracion"]
    datos = progreso.cargar(curso)
    assert datos["metricas"]["talleres_completados"] == 1
    assert talleres.estado(curso, ind)["activo"] is None


def test_taller_ayuda_no_penaliza_ni_avanza(tmp_path_curso):
    curso, ind = _curso_talleres(tmp_path_curso)
    talleres.elegir(curso, ind, taller_id="videollamada-familia")
    a = talleres.ayuda(curso, ind)
    assert a["pista"] and "ícono" in a["pista"]
    assert a["paso"]["n"] == 1, "la ayuda no avanza el paso"
    est = talleres.estado(curso, ind)
    assert est["paso"]["n"] == 1 and est["paso"]["total"] == 3


def test_taller_guia_inexistente_no_se_ofrece(tmp_path_curso):
    curso, ind = _curso_talleres(tmp_path_curso)
    ofrecibles = talleres.estado(curso, ind)["talleres"]
    ids = [t["id"] for t in ofrecibles]
    assert "taller-guia-rota" not in ids, "guía inválida: taller excluido"
    assert len(ids) == 2


def test_taller_celebracion_conecta_memoria_del_usuario(tmp_path_curso):
    curso, ind = _curso_talleres(tmp_path_curso)
    talleres.elegir(curso, ind, taller_id="videollamada-familia")
    talleres.avanzar(curso, ind)
    talleres.avanzar(curso, ind)
    fin = talleres.avanzar(curso, ind)
    assert fin["memoria"], "la celebración conecta con un recuerdo suyo"
    assert fin["memoria"]["fid"].startswith("memoria#")
    assert evidencia.validar(fin["celebracion"], ind).ok
    ref = ind.referencias[fin["memoria"]["fid"]][1]
    assert not ref.startswith("guia:"), "nunca celebra con una guía"


def test_taller_reinicia_elegir_el_siguiente_sin_completar(tmp_path_curso):
    curso, ind = _curso_talleres(tmp_path_curso)
    talleres.elegir(curso, ind, taller_id="anti-estafa-cotidiano")
    talleres.avanzar(curso, ind)
    r = talleres.elegir(curso, ind)
    assert r["paso"]["n"] == 1, "elegir de nuevo reinicia el taller activo"


# --- flujo HTTP (H-14.1/H-14.2) ---------------------------------------------

def _post(url, datos=None):
    req = urllib.request.Request(
        url, data=json.dumps(datos or {}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read().decode())


def _get(url):
    with urllib.request.urlopen(url, timeout=10) as r:
        return r.status, json.loads(r.read().decode())


@pytest.fixture
def httpd_e14(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    curso, _ = _curso_talleres(tmp_path_curso)
    curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}", curso
    server.shutdown()


def test_taller_http_roundtrip(httpd_e14):
    base, _ = httpd_e14
    s, r = _get(base + "/api/cursos/testcurso/taller")
    assert s == 200 and r["activo"] is None and len(r["talleres"]) == 2
    s, r = _post(base + "/api/cursos/testcurso/taller", {"accion": "elegir"})
    assert s == 200 and r["paso"]["n"] == 1
    for _ in range(3):
        s, r = _post(base + "/api/cursos/testcurso/taller", {"accion": "avanzar"})
    assert s == 200 and r["completado"] is True


def test_familiar_contrato_y_privacidad(httpd_e14):
    base, curso = httpd_e14
    guardian.registrar_alerta(curso, {"senales": ["me cai", "ambulancia"]})
    s, f = _get(base + "/api/cursos/testcurso/familiar")
    assert s == 200
    assert set(("curso", "pulso", "alertas", "biografia")) <= set(f)
    p = f["pulso"]
    assert set(("racha_dias", "ultima_interaccion", "mensajes", "sesiones",
                "recuerdos", "talleres_completados")) <= set(p)
    assert p["recuerdos"] == 2, "solo memorias personales, sin guías"
    assert f["alertas"]["total"] == 1
    item = f["alertas"]["items"][0]
    assert set(item) == {"fecha", "tipo"}, "solo fecha y categoría: nada más"
    serializado = json.dumps(f["alertas"], ensure_ascii=False)
    assert "senales" not in serializado and "cai" not in serializado \
        and "ambulancia" not in serializado, "0 filtración del mensaje"
    assert f["biografia"]["total"] == 2


def test_taller_y_familiar_404_fuera_de_compania(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    tmp_path_curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    base = f"{BASE}:{server.server_address[1]}"
    try:
        for ruta in ("/taller", "/familiar"):
            try:
                _get(base + "/api/cursos/testcurso" + ruta)
                assert False, f"{ruta} debió dar 404 fuera de compañía"
            except urllib.error.HTTPError as e:
                assert e.code == 404
        try:
            _post(base + "/api/cursos/testcurso/taller", {"accion": "elegir"})
            assert False, "POST /taller debió dar 404 fuera de compañía"
        except urllib.error.HTTPError as e:
            assert e.code == 404
    finally:
        server.shutdown()


# --- vistas (H-14.3, D-14.3) -------------------------------------------------

def test_chat_html_tiene_controles_taller_y_familiar():
    html = (RAIZ / "src" / "web" / "chat.html").read_text(encoding="utf-8")
    for marca in ("btn-taller", "Aprender paso a paso", "/taller",
                  "Lo hice, siguiente paso", "Necesito ayuda",
                  "btn-familiar", "familiar.html"):
        assert marca in html, f"chat.html debe contener: {marca}"


def test_familiar_html_es_calia_e_imprimible_y_sin_hardcode():
    html = (RAIZ / "src" / "web" / "familiar.html").read_text(encoding="utf-8")
    for marca in ("/familiar", "@media print", "#FAF7F2", "#2E6F5E",
                  "Libro de Historias", "window.print()"):
        assert marca in html, f"familiar.html debe contener: {marca}"
    assert "Rufo" not in html and "Carmen" not in html, \
        "0 contenido conversacional hardcodeado"
