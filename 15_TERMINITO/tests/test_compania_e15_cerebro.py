"""Cerebro asociativo E-15: aal, trazas, valencia, olvido y evaluación D-15.3.

Cubre H-15.1 (trazas multi-salto verificadas), H-15.2 (aislamiento H7),
H-15.3 (olvido controlado sin duplicados), H-15.4 (evaluación honesta) y la
degradación limpia sin aal (D-15.1). Todo en cursos temporales: nunca toca
cursos/ reales.
"""
import json
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from datito import apertura, biografia, cerebro, eval_cerebro, evidencia
from datito import progreso, reminiscencia, servidor
from datito.indice import Indice

BASE = "http://127.0.0.1"
tiene_aal = cerebro.AAL
skip_sin_aal = pytest.mark.skipif(not tiene_aal, reason="aal no instalado")

MEMORIAS = {
    "rufo": "Su perrito Rufo la esperaba en la puerta cada tarde",
    "video": "Hace videollamadas con sus nietas los domingos por la tarde",
    "tejer": "Aprendió a tejer con su madre en Chillán",
    "sopaipillas": "Los domingos hacía sopaipillas con su hermana",
    "rufo_falso": "Rufo era el gato de su vecina de al lado",
    "claves": ("Nunca comparta las claves de su banco por teléfono: "
               "ningún banco las pide"),
}


def _curso_compania(tmp_path_curso):
    tmp_path_curso.datos["modo"] = "compania"
    tmp_path_curso.guardar()
    ind = Indice()
    fids = {}
    for clave, texto in MEMORIAS.items():
        ref = "guia: anti-estafa" if clave == "claves" else "sesion prueba"
        fids[clave] = ind.registrar_recuerdo(texto, referencia=ref)
    ind.guardar(tmp_path_curso.ruta(".indice"))
    return tmp_path_curso, ind, fids


def _cerebro_activo(curso, ind):
    cer = cerebro.Cerebro(curso)
    cer.sincronizar_indice(ind)
    cer.guardar()
    return cer


# --------------------------------------------------------------- D-15.1
def test_info_salud_incluye_cerebro():
    i = cerebro.info()
    assert set(("activo", "motor", "version", "adopcion")) <= set(i)
    assert i["activo"] in (True, False)


def test_sin_aal_degradacion_limpia(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(cerebro, "AAL", False)
    curso, ind, _ = _curso_compania(tmp_path_curso)
    assert cerebro.habilitado(curso) is False
    assert cerebro.para_curso(curso) is None
    assert cerebro.sugerir_apertura(curso, ind) is None
    assert cerebro.orden_entidades(curso) == {}
    i = cerebro.info()
    assert i["activo"] is False and i["guia"]


def test_preferencia_off_desactiva(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(cerebro, "ADOPCION", "adoptar")
    curso, _, _ = _curso_compania(tmp_path_curso)
    curso.datos["cerebro"] = "off"
    assert cerebro.habilitado(curso) is False
    curso.datos["cerebro"] = "aal"
    assert cerebro.habilitado(curso) is tiene_aal


# --------------------------------------------------------- Fases 0-1 (ciclo)
@skip_sin_aal
def test_ciclo_crea_grafo_atomico(tmp_path_curso):
    curso, ind, _ = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    cer.ciclo("Cuénteme de mi perrito Rufo", "Qué bonito recuerdo",
              indice=ind)
    ruta = curso.ruta(".cerebro") / "grafo.json"
    assert ruta.exists(), "el grafo persiste atómicamente"
    datos = json.loads(ruta.read_text("utf-8"))
    assert datos["schema_version"] == 2
    tipos = {n["type"] for n in datos["nodes"]}
    assert "Goal" in tipos and "Concept" in tipos
    est = cerebro.estadisticas(curso)
    assert est["nodos"] == len(datos["nodes"]) and est["episodios"] >= 1


@skip_sin_aal
def test_ciclo_fraude_no_consolida(tmp_path_curso):
    curso, ind, _ = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    n_antes = len(list(cer.grafo.nodes()))
    cer.ciclo("Me pidieron las claves y las di", "protección",
              indice=ind, registrar=False)
    n_despues = len(list(cer.grafo.nodes()))
    assert n_despues <= n_antes + 1, "sin episodio no hay inflado del grafo"


# --------------------------------------------- Fases 2-3 (trazas y valencia)
@skip_sin_aal
def test_traza_multisalto_por_puente(tmp_path_curso):
    curso, ind, fids = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    # episodios que consolidan el puente 'domingos' entre dos memorias
    cer.ciclo("Los domingos hacía sopaipillas con su hermana", "b", indice=ind)
    cer.ciclo("Hace videollamadas con sus nietas los domingos", "b", indice=ind)
    hallazgos = cer.recuperar("sopaipillas", k=4, indice=ind)
    fids_hallados = [h["fid"] for h in hallazgos]
    assert fids["sopaipillas"] in fids_hallados
    assert fids["video"] in fids_hallados, "salto asociativo vía puente"
    video = next(h for h in hallazgos if h["fid"] == fids["video"])
    from datito.indice import tokenizar
    assert not (set(tokenizar("sopaipillas"))
                & set(tokenizar(MEMORIAS["video"]))), \
        "la consulta y el recuerdo no comparten lexema: salto ≥ 2"
    assert len(video["camino"]) >= 2, "camino semilla→…→recuerdo trazado"
    assert any("domingo" in paso.lower() for paso in video["camino"]), \
        "la traza nombra el puente (H-15.1)"


@skip_sin_aal
def test_cero_recuerdos_inventados(tmp_path_curso):
    curso, ind, _ = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    for mensaje in ("Cuénteme de Rufo", "los domingos de tejer",
                    "sopaipillas y videollamadas"):
        cer.ciclo(mensaje, "respuesta", indice=ind)
    for consulta in ("Rufo", "domingos", "tejer", "nietas", "Chillán"):
        for h in cer.recuperar(consulta, k=4, indice=ind):
            assert h["fid"] in ind.textos, "fid inventado: imposible"
            assert evidencia.validar(f"{h['etiqueta']} [{h['fid']}]", ind).ok


@skip_sin_aal
def test_h7_aislamiento_dominio(tmp_path_curso):
    curso, ind, _ = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    fid_acad = ind.registrar_recuerdo(
        "la matriz de confusión del curso de datos", referencia="academico")
    cer.sincronizar_indice(ind)
    nodo = [n for n in cer.grafo.nodes()
            if n.metadata.get("fid") == fid_acad][0]
    nodo.metadata["domain"] = "academico"
    cer.guardar()
    hallazgos = cer.recuperar("matriz de confusión del curso de datos",
                              k=4, indice=ind, dominio="compania")
    assert all(h["fid"] != fid_acad for h in hallazgos), "H7: 0 fugas"


@skip_sin_aal
def test_alerta_nunca_recuperable_y_compuerta_bienestar(tmp_path_curso):
    curso, ind, fids = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    cer.ciclo("Hoy vi al gato de la vecina y me sentí triste y sola",
              "contención", indice=ind,
              senal={"nivel": "alerta", "senales": ["tristeza"]})
    kinds = [n.metadata.get("kind") for n in cer.grafo.nodes()]
    assert "alerta" in kinds
    for consulta in ("gato vecina", "Rufo", "tristeza"):
        for h in cer.recuperar(consulta, k=4, indice=ind):
            assert h["kind"] != "alerta", "las alertas jamás se evocan"
    assert all(h["fid"] != fids["rufo_falso"]
               for h in cer.recuperar("gato de la vecina Rufo", k=4, indice=ind)), \
        "señuelo con valencia negativa fuera de la evocación (H4)"


@skip_sin_aal
def test_olvido_controlado_nuclear_unico(tmp_path_curso):
    curso, ind, fids = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    for i in range(30):
        cer.ciclo("Otra vez le cuento de mi perrito Rufo y la puerta",
                  "respuesta", indice=ind)
        if i % 3 == 0:
            cer.ciclo(f"cosas variadas número {i} del barrio", "r", indice=ind)
    rufo = [n for n in cer.grafo.nodes()
            if n.metadata.get("kind") == "memoria" and "perrito" in n.label]
    assert len(rufo) == 1, "H-15.3: la historia repetida no se duplica"
    assert rufo[0].metadata.get("nuclear") is True, "alta recurrencia: nuclear"
    assert cerebro.ruta_grafo(curso).exists()
    hallazgos = cer.recuperar("perrito Rufo puerta", k=4, indice=ind)
    assert any(h["fid"] == fids["rufo"] for h in hallazgos), \
        "el recuerdo nuclear sobrevive al olvido controlado"


# -------------------------------------------------- integración (apertura…)
@skip_sin_aal
def test_apertura_reminiscencia_biografia_con_cerebro(tmp_path_curso):
    curso, ind, fids = _curso_compania(tmp_path_curso)
    cer = _cerebro_activo(curso, ind)
    cer.ciclo("Cuénteme de su perrito Rufo", "b", indice=ind)
    apert = apertura.calcular(curso, ind)
    fid_ap = apert["recuerdo"]["fid"]
    assert fid_ap in fids.values() and fid_ap.startswith("memoria#")
    assert not ind.referencias[fid_ap][1].startswith("guia:")
    rem = reminiscencia.siguiente(curso, ind, nueva=True)
    assert rem["fid"] in fids.values()
    rem2 = reminiscencia.siguiente(curso, ind, nueva=True)
    assert rem2["fid"] in fids.values()
    assert rem2["fid"] != rem["fid"], "rotación dentro de reminiscencia"
    bio = biografia.construir(curso, ind)
    assert bio["total"] == 5 and bio["alertas"] == 0
    assert cerebro.orden_entidades(curso), "temas ordenables para la biografía"


def test_biografia_sin_cerebro_igual_de_valida(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(cerebro, "AAL", False)
    curso, ind, _ = _curso_compania(tmp_path_curso)
    bio = biografia.construir(curso, ind)
    assert bio["total"] == 5 and "entidades" in bio


# --------------------------------------------------------- Fase 4 (D-15.3)
def test_eval_estructura_sin_aal(monkeypatch):
    monkeypatch.setattr(cerebro, "AAL", False)
    r = eval_cerebro.comparar()
    assert r["baseline"]["mrr"] >= 0 and r["baseline"]["validez"] == 1.0
    assert r["cerebro"] is None and r["decision"] == "opt_in"


@skip_sin_aal
def test_eval_comparar_decision_honesta(tmp_path_curso):
    curso, _, _ = _curso_compania(tmp_path_curso)
    r = eval_cerebro.comparar(curso_factory=lambda: curso)
    b, c = r["baseline"], r["cerebro"]
    assert b["validez"] == 1.0 and c["validez"] == 1.0, "validación 100%"
    assert c["fuga_dominio"] == 0, "H7: cero contaminación cruzada"
    assert r["repeticion"]["rufo_unico"] is True
    assert r["decision"] in ("adoptar", "opt_in")
    if r["decision"] == "adoptar":
        assert c["mrr"] >= b["mrr"] and c["p3"] >= b["p3"] \
            and c["rechazo_senuelos"] >= b["rechazo_senuelos"]
        assert (c["mrr"] > b["mrr"] or c["p3"] > b["p3"]
                or c["rechazo_senuelos"] > b["rechazo_senuelos"]), \
            "adoptar exige mejora estricta en algo (D-15.3)"


# ------------------------------------------------------------- flujo HTTP
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
def httpd_e15(tmp_path_curso, monkeypatch):
    monkeypatch.setattr(servidor.config, "PUERTO", 0)
    curso, ind, _ = _curso_compania(tmp_path_curso)
    curso.transicionar("listo")
    server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
    hilo = threading.Thread(target=server.serve_forever, daemon=True)
    hilo.start()
    yield f"{BASE}:{server.server_address[1]}", curso, ind
    server.shutdown()


def test_http_salud_con_cerebro(httpd_e15):
    base, _, _ = httpd_e15
    s, r = _get(base + "/api/salud")
    assert s == 200 and "cerebro" in r
    assert r["cerebro"]["activo"] in (True, False)


@skip_sin_aal
def test_http_mensajes_asociaciones_validadas(httpd_e15):
    base, curso, ind = httpd_e15
    s, r = _post(base + "/api/cursos/testcurso/mensajes",
                 {"texto": "Cuénteme de mi perrito Rufo y la puerta"})
    assert s == 200
    assert "asociaciones" in r, "el cerebro enriquece la envoltura"
    assert len(r["asociaciones"]) >= 1
    # el turno pudo registrar un recuerdo nuevo: validamos contra el índice
    # persistido en disco, no contra la copia en memoria del fixture
    ind2 = Indice.cargar(curso.ruta(".indice"))
    for a in r["asociaciones"]:
        assert a["fid"] in ind2.textos
        assert a["camino"], "cada asociación lleva su traza (H-15.1)"
        assert evidencia.validar(f"{a['etiqueta']} [{a['fid']}]", ind2).ok
    assert cerebro.ruta_grafo(curso).exists(), "el ciclo persistió el grafo"
