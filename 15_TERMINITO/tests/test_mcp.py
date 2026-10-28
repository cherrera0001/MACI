"""Servidor MCP: protocolo stdio y herramientas sobre el motor real."""
import json

import yaml

from datito import evaluador
from datito.mcp import HERRAMIENTAS, Servidor
from datito.indice import Indice
from datito.fragmentos import Fragmento


def llamar(servidor, nombre, **args):
    resp = servidor.manejar({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                             "params": {"name": nombre, "arguments": args}})
    assert "error" not in resp, resp
    assert resp["result"]["isError"] is False
    return json.loads(resp["result"]["content"][0]["text"])


def test_initialize_y_lista_de_herramientas(tmp_path_curso):
    s = Servidor(tmp_path_curso)
    resp = s.manejar({"jsonrpc": "2.0", "id": 1, "method": "initialize"})
    assert resp["result"]["capabilities"] == {"tools": {}}
    nombres = {h["name"] for h in HERRAMIENTAS}
    assert {"progreso", "grafo_dominio", "siguiente_concepto",
            "distinciones_pendientes", "calificar_distincion",
            "buscar_materiales", "registrar_dominio"} <= nombres
    resp = s.manejar({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    assert len(resp["result"]["tools"]) == len(HERRAMIENTAS)


def test_notificacion_no_responde(tmp_path_curso):
    s = Servidor(tmp_path_curso)
    assert s.manejar({"jsonrpc": "2.0", "method": "notifications/initialized"}) is None


def test_metodo_desconocido_devuelve_error(tmp_path_curso):
    s = Servidor(tmp_path_curso)
    resp = s.manejar({"jsonrpc": "2.0", "id": 1, "method": "resources/list"})
    assert resp["error"]["code"] == -32601


def test_progreso_y_grafo_dominio(tmp_path_curso):
    s = Servidor(tmp_path_curso)
    p = llamar(s, "progreso")
    assert p["metricas"]["sesiones"] == 0
    g = llamar(s, "grafo_dominio")
    assert g["nodos"] == []  # curso de prueba sin grafo todavia


def test_registrar_dominio_y_siguiente_concepto(tmp_path_curso):
    curso = tmp_path_curso
    (curso.ruta("grafo")).mkdir(exist_ok=True)
    curso.ruta("grafo", "grafo.yaml").write_text(yaml.safe_dump({
        "cadenas": {"base": ["a", "b"]},
        "nodos": {"a": {"nombre": "Concepto A"},
                  "b": {"nombre": "Concepto B", "requiere_antes": ["a"]}},
    }, allow_unicode=True), encoding="utf-8")
    s = Servidor(curso)
    assert llamar(s, "siguiente_concepto")["siguiente"]["id"] == "a"
    llamar(s, "registrar_dominio", conceptos=["a"], resultado="logrado")
    assert llamar(s, "siguiente_concepto")["siguiente"]["id"] == "b"
    dominio = llamar(s, "grafo_dominio")
    estados = {n["id"]: n["estado"] for n in dominio["nodos"]}
    assert estados == {"a": "dominado", "b": "no_estudiado"}


def test_distinciones_calificar_y_pendientes(tmp_path_curso):
    curso = tmp_path_curso
    curso.ruta("evaluaciones").mkdir(exist_ok=True)
    curso.ruta("evaluaciones", "distinciones.yaml").write_text(yaml.safe_dump({
        "items": [{"id": "d1", "conceptos": ["a", "b"],
                   "pregunta": "Distingue X de Y",
                   "criterios": ["menciona la brecha"]}],
    }, allow_unicode=True), encoding="utf-8")
    s = Servidor(curso)
    pend = llamar(s, "distinciones_pendientes")
    assert [i["id"] for i in pend["items"]] == ["d1"]
    res = llamar(s, "calificar_distincion", item_id="d1",
                 respuesta="la brecha entre entrenamiento y validacion lo decide")
    assert res["item_id"] == "d1" and "logrado" in res
    hechos = evaluador.cargar_resultados_guardados(curso)
    assert any(r.get("item_id") == "d1" for r in hechos)
    assert llamar(s, "distinciones_pendientes")["items"] == []


def test_calificar_item_inexistente_es_error_controlado(tmp_path_curso):
    s = Servidor(tmp_path_curso)
    resp = s.manejar({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                      "params": {"name": "calificar_distincion",
                                 "arguments": {"item_id": "nope", "respuesta": "x"}}})
    assert "error" in resp  # excepcion del tool: -32603, el servidor sigue vivo


def test_buscar_materiales(tmp_path_curso):
    curso = tmp_path_curso
    ind = Indice().construir([
        Fragmento(fid="f1", fuente_id="clase1", referencia="0:10:00",
                  texto="la validacion cruzada compara modelos con la misma particion"),
        Fragmento(fid="f2", fuente_id="clase2", referencia="0:05:00",
                  texto="la matriz de confusion cuenta verdaderos y falsos positivos"),
    ])
    ind.guardar(curso.ruta(".indice"))
    s = Servidor(curso)
    res = llamar(s, "buscar_materiales", consulta="validacion cruzada particion")
    assert res["fragmentos"][0]["fid"] == "f1"
    assert res["fragmentos"][0]["fuente"] == "clase1"


def test_buscar_sin_indice_da_error_claro(tmp_path_curso):
    s = Servidor(tmp_path_curso)
    resp = s.manejar({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                      "params": {"name": "buscar_materiales",
                                 "arguments": {"consulta": "algo"}}})
    assert resp["error"]["code"] == -32603
    assert "datito build" in resp["error"]["message"]


def test_flujo_stdio_end_to_end(tmp_path_curso, capsys):
    from datito.mcp import main
    entrada = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize"}) + "\n"
    import io, sys
    sys.stdin = io.StringIO(entrada)
    assert main(["--curso", tmp_path_curso.slug]) == 0
    salida = capsys.readouterr().out.strip()
    assert json.loads(salida)["result"]["serverInfo"]["name"] == "datito-mcp"
