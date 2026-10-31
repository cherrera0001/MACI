"""E-13: ergonomía de la entrada, supresión de jerga, trato en segunda
persona y autodescubrimiento del modelo de voz."""
import io
import json
import urllib.request
from pathlib import Path

from datito import servidor, voz
from datito.modelo import cargar
from datito.indice import Indice

CHAT = (Path(servidor.DIR_WEB) / "chat.html").read_text(encoding="utf-8")


def _semilla_en_tmp(tmp_path, monkeypatch):
    import importlib.util
    monkeypatch.setattr("datito.config.DIR_CURSOS", tmp_path / "cursos")
    import datito.config as cfg
    monkeypatch.setattr(cfg, "DIR_CURSOS", tmp_path / "cursos")
    spec = importlib.util.spec_from_file_location(
        "semilla_compania", Path(__file__).resolve().parents[1]
        / "scripts" / "semilla_compania.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.construir()
    curso = cargar("compania")
    return curso, Indice.cargar(curso.ruta(".indice"))


# --- H-13.1 · layout de dos filas y pantalla sin jerga ----------------------

def test_layout_dos_filas_y_textarea_protegido():
    for regla in (".fila-botones", ".fila-escritura",
                  "flex-direction: column", "min-width: 70%",
                  "min-height: 68px"):
        assert regla in CHAT, f"falta {regla}"
    assert "display: contents" in CHAT, "el layout académico se conserva"


def test_jerga_escolar_oculta_en_compania_y_biografia_presente():
    for selector in ('a[data-i18n="c_eval"]', 'a[data-i18n="c_dominio"]',
                     ".estado-motor", "#guia-ollama",
                     '[data-i18n-html="ch_ayuda"]'):
        assert "body.compania " + selector in CHAT, f"no se oculta {selector}"
    assert "btn-biografia" in CHAT and "/biografia" in CHAT
    assert "Mi historia de vida" in CHAT


# --- H-13.2 · trato en segunda persona, con tildes --------------------------

def test_semilla_segunda_persona_sin_tercera_y_con_tildes(tmp_path, monkeypatch):
    _, ind = _semilla_en_tmp(tmp_path, monkeypatch)
    for fid, texto in ind.textos.items():
        assert "la persona" not in texto, f"{fid} habla en tercera persona"
    unidos = " ".join(ind.textos.values())
    assert "usted" in unidos or "su " in unidos
    for tilde in ("compañía", "está", "recomendó", "teléfono", "enséñárselas"):
        assert tilde in unidos, f"falta tilde correcta: {tilde}"


def test_guias_y_saludos_tambien_en_segunda_persona():
    from datito import guardian, tutor
    for senal in guardian.SENALES_ALERTA + guardian.SENALES_FRAUDE:
        assert "la persona" not in senal
    texto_proteccion, _ = guardian.proteccion(
        None, Indice(), {"nivel": "fraude", "senales": ["clave"]})
    assert "la persona" not in texto_proteccion
    assert "la persona" not in tutor._TEXTO_COMPANIA_EXPLORACION
    assert "la persona" not in tutor._TEXTO_NO_RECUERDA


# --- H-13.3 · autodescubrimiento e instalación del modelo .onnnx -----------

def test_autodescubrimiento_de_modelos(tmp_path, monkeypatch):
    p1 = tmp_path / ".piper"
    p2 = tmp_path / "home" / ".local" / "share" / "piper"
    p1.mkdir(parents=True)
    p2.mkdir(parents=True)
    (p1 / "es_ES-davefx-medium.onnx").write_bytes(b"onnx")
    (p2 / "otro.onnx").write_bytes(b"onnx")
    monkeypatch.setattr(voz, "_dirs_modelos",
                        lambda: [p1, p2])
    monkeypatch.setattr(voz, "_MOTOR", None)
    modelos = voz.modelos_locales()
    assert len(modelos) == 2
    assert voz.modelo_a_usar().name == "es_ES-davefx-medium.onnx"


def test_instalar_modelo_descarga_onnx_y_json(tmp_path, monkeypatch):
    class FakeResp(io.BytesIO):
        def __enter__(self):
            return self
        def __exit__(self, *a):
            return False

    llamadas = []
    def fake_urlopen(url, timeout=0):
        llamadas.append(url)
        return FakeResp(b"datos-" + url.rsplit(".", 1)[-1].encode())

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setattr(voz, "_MOTOR", None)
    destino = tmp_path / ".piper"
    onnx = voz.instalar_modelo(destino=destino)
    assert onnx.exists() and onnx.with_suffix(".onnx.json").exists()
    assert any(u.endswith(".onnx") for u in llamadas)
    assert any(u.endswith(".onnx.json") for u in llamadas)
    assert "huggingface.co" in llamadas[0]
