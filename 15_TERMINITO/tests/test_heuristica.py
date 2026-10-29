"""Heurística de calificación endurecida (T-7.4.2): respuestas de juguete."""
from datito.evaluador import Item, _calificar_heuristica, _criterio_logrado

ITEM = Item(
    id="d1", conceptos=["sobreajuste", "generalizacion"],
    pregunta="¿Cuál sobreajusta y cuál generaliza?",
    criterios=[
        "identifica A como sobreajuste por brecha grande",
        "identifica B como el que generaliza con brecha pequena",
        "explica que elegir hiperparametros con el test lo contamina",
    ],
    pasos=[], solucion="A memoriza; B generaliza; C subajusta")


def test_respuesta_correcta_lograda():
    res = _calificar_heuristica(ITEM, (
        "A es el sobreajuste porque su brecha es grande, y B es el que "
        "generaliza con una brecha pequena; elegir hiperparametros con el "
        "test contamina la estimacion"))
    assert res.resultado == "logrado"
    assert not res.heuristico is None and res.heuristico  # va rotulada


def test_keyword_stuffing_no_alcanza():
    # las palabras clave sueltas sin el resto de las ideas del criterio
    res = _calificar_heuristica(ITEM, "sobreajuste brecha generaliza pequena contamina")
    assert res.resultado != "logrado"


def test_respuesta_vacia_no_logra_nada():
    res = _calificar_heuristica(ITEM, "no se")
    assert res.resultado == "no_logrado"
    assert res.criterios_logrados == []


def test_mitad_no_es_mayoria():
    # 2 de 4 tokens de contenido no basta: hay que superar la mitad
    assert not _criterio_logrado("alpha bravo charlie delta", "alpha bravo")
    assert _criterio_logrado("alpha bravo charlie delta", "alpha bravo charlie")
    # los verbos de la orden no cuentan: cumplir la accion no es escribirla
    assert _criterio_logrado("identifica A como sobreajuste por brecha grande",
                             "el A tiene brecha grande: es sobreajuste")
