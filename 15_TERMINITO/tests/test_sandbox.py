"""Sandbox y evaluación de procedimiento (H-8.2 / T-8.2.1–T-8.2.3)."""
import yaml

from datito import evaluador, grafo, sandbox
from datito.evaluador import Item

ITEM_PROTOCOLO = Item(
    id="d1-brecha", conceptos=["overfitting_underfitting", "generalizacion"],
    pregunta="Diagnostica los tres modelos calculando la brecha ANTES de etiquetar.",
    criterios=["calcula la brecha antes de etiquetar"],
    protocolo=[{"evento": "brecha", "antes_de": ["etiquetar"]},
               {"evento": "etiquetar", "requiere": True}])

SCRIPT_BIEN = """
print("#@brecha")
print("A: 1.00-0.54 = 0.44")
print("#@etiquetar")
print("A sobreajusta; B generaliza; C subajusta")
"""

SCRIPT_MAL = """  # etiqueta antes de calcular la brecha
print("#@etiquetar")
print("A sobreajusta")
print("#@brecha")
"""

SCRIPT_SIN_ETIQUETA = """
print("#@brecha")
print("solo calculo, nunca etiqueto")
"""


def test_sandbox_captura_eventos_en_orden():
    traza = sandbox.ejecutar(SCRIPT_BIEN)
    assert traza.codigo_salida == 0
    assert traza.nombres() == ["brecha", "etiquetar"]
    assert "0.44" in traza.salida  # la salida completa queda como evidencia
    assert [e.seq for e in traza.eventos] == [1, 2]


def test_sandbox_timeout():
    traza = sandbox.ejecutar("while True:\n    pass\n", timeout=2)
    assert traza.timeout and traza.codigo_salida is None


def test_sandbox_script_con_error():
    traza = sandbox.ejecutar("raise ValueError('boom')\n")
    assert traza.codigo_salida != 0
    assert "ValueError" in traza.error


def test_protocolo_respeta_el_orden():
    bien = sandbox.ejecutar(SCRIPT_BIEN)
    cumplidas, fallidas = sandbox.validar_protocolo(bien, ITEM_PROTOCOLO.protocolo)
    assert not fallidas and len(cumplidas) == 2

    mal = sandbox.ejecutar(SCRIPT_MAL)
    _, fallidas = sandbox.validar_protocolo(mal, ITEM_PROTOCOLO.protocolo)
    assert any("brecha" in f and "etiquetar" in f for f in fallidas)

    incompleto = sandbox.ejecutar(SCRIPT_SIN_ETIQUETA)
    _, fallidas = sandbox.validar_protocolo(incompleto, ITEM_PROTOCOLO.protocolo)
    assert any("etiquetar" in f for f in fallidas)


def test_calificar_procedimiento_alimenta_dominio(tmp_path_curso):
    curso = tmp_path_curso
    res = evaluador.calificar_procedimiento(ITEM_PROTOCOLO, SCRIPT_BIEN)
    assert res.resultado == "logrado"
    assert res.traza is not None and res.traza.nombres() == ["brecha", "etiquetar"]
    evaluador.guardar_resultado(curso, res)
    grafo.actualizar_dominio(curso, ITEM_PROTOCOLO.conceptos, res.resultado)
    dominio = yaml.safe_load(curso.ruta("grafo", "dominio.yaml").read_text())
    assert dominio["overfitting_underfitting"]["estado"] == "dominado"
    # la evidencia de la traza quedó persistida
    guardado = yaml.safe_load(
        curso.ruta("evaluaciones", "resultados.yaml").read_text())["resultados"][0]
    assert guardado["traza"]["eventos"] == ["brecha", "etiquetar"]
    assert guardado["traza"]["codigo_salida"] == 0

    res2 = evaluador.calificar_procedimiento(ITEM_PROTOCOLO, SCRIPT_MAL)
    # etiquetó antes de calcular la brecha: la regla clave se viola,
    # así que NO puede ser logrado aunque ambos eventos existan
    assert res2.resultado in ("parcial", "no_logrado")
    grafo.actualizar_dominio(curso, ITEM_PROTOCOLO.conceptos, res2.resultado)
    dominio = yaml.safe_load(curso.ruta("grafo", "dominio.yaml").read_text())
    # no baja de dominado: la regla es avanzar o mantener, nunca castigar
    assert dominio["overfitting_underfitting"]["estado"] in ("dominado", "en_estudio")


def test_item_carga_protocolo_desde_yaml(tmp_path_curso):
    item = {"id": "d9", "conceptos": ["a", "b"], "pregunta": "p",
            "criterios": ["c"],
            "protocolo": [{"evento": "x", "antes_de": ["y"]}]}
    (tmp_path_curso.ruta("evaluaciones") / "p.yaml").write_text(
        yaml.safe_dump({"items": [item]}, allow_unicode=True), encoding="utf-8")
    (cargado,) = evaluador.cargar_items(tmp_path_curso)
    assert cargado.protocolo == [{"evento": "x", "antes_de": ["y"]}]
