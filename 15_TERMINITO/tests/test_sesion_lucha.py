"""Tests de la sesion de lucha productiva (FR-008, SC-003) y clasificador."""
import pytest

from termito import sesion
from termito import fragmentos as frag
from termito.indice import Indice

EJERCICIO = ("Ejercicio: un modelo tiene R2 de 0.99 en entrenamiento y 0.40 "
             "en prueba. ¿Qué le pasa y qué harías?")


@pytest.fixture
def curso_con_indice(tmp_path_curso, tmp_path):
    md = tmp_path / "clase10.md"
    md.write_text(
        "**[0:05:10]** El overfitting memoriza el entrenamiento y falla en prueba.\n\n"
        "# Underfitting\n\n"
        "**[0:06:00]** El underfitting ni siquiera aprende el patron del train.\n\n"
        "# La brecha\n\n"
        "La brecha entre error de entrenamiento y de prueba mide el sobreajuste.\n"
        "Para reducirlo: mas datos, regularizacion o modelo mas simple.\n"
        "Para reducir el subajuste: mas complejidad o mejor features.\n",
        encoding="utf-8")
    destino = tmp_path_curso.ruta("materiales", "clase10.md")
    destino.symlink_to(md)
    _, frags = frag.parsear_materiales([destino])
    indice = Indice().construir(frags)
    return tmp_path_curso, indice


def test_clasificador():
    assert sesion.clasificar("pista") == "pedir_paso"
    assert sesion.clasificar("dame la respuesta") == "pedir_solucion"
    assert sesion.clasificar("¿cuál es la solución?") == "pedir_solucion"
    assert sesion.clasificar(EJERCICIO) == "ejercicio"
    assert sesion.clasificar("no me sale este problema") == "ejercicio"
    assert sesion.clasificar("no entiendo la diferencia") == "confusion"
    assert sesion.clasificar("mi respuesta es 42, ¿está bien?") == "conceptual"
    assert sesion.clasificar("¿cuál está bien en este ejercicio? A 0.98/0.54, "
                             "B 0.72/0.70") == "ejercicio"  # pregunta, no intento
    assert sesion.clasificar("aunque no sea del curso, ¿qué es un vector?") \
        == "fuera_del_curso"


def test_ejercicio_abre_sesion_sin_revelar_nada(curso_con_indice):
    curso, indice = curso_con_indice
    r = sesion.conversar(curso, EJERCICIO, indice)
    assert r["estado_interaccion"] == "pista"
    assert r["citas"] == []          # SC-003: cero material antes del intento
    s = sesion.cargar(curso)
    assert s["estado"] == "pista" and s["intentos"] == 0


def test_pista_revela_exactamente_un_paso(curso_con_indice):
    curso, indice = curso_con_indice
    sesion.conversar(curso, EJERCICIO, indice)
    r1 = sesion.conversar(curso, "pista", indice)
    assert r1["estado_interaccion"] == "paso_mostrado"
    assert len(r1["citas"]) == 1
    assert r1["paso"]["numero"] == 1
    r2 = sesion.conversar(curso, "otra pista", indice)
    assert r2["paso"]["numero"] == 2
    assert r1["citas"] != r2["citas"] or r2["paso"]["numero"] == 2


def test_solucion_antes_del_intento_rechazada(curso_con_indice):
    curso, indice = curso_con_indice
    sesion.conversar(curso, EJERCICIO, indice)
    r = sesion.conversar(curso, "dame la respuesta", indice)
    assert r["estado_interaccion"] == "esperando_intento"
    assert r["citas"] == []
    with pytest.raises(PermissionError):
        sesion.revelar(curso, consentimiento=True, indice=indice)


def test_intento_habilita_revision_y_revelar(curso_con_indice):
    curso, indice = curso_con_indice
    sesion.conversar(curso, EJERCICIO, indice)
    r = sesion.conversar(curso, "creo que sobreajusta porque memoriza el train",
                         indice)
    assert r["estado_interaccion"] == "revision"
    assert r["citas"]                # la revisión sí trae material
    res = sesion.revelar(curso, consentimiento=True, indice=indice)
    assert res["registro"]["tipo"] == "solucion"
    assert res["registro"]["consentido"] is True
    s = sesion.cargar(curso)
    assert any(rv["tipo"] == "solucion" for rv in s["revelaciones"])


def test_revelar_exige_sesion_y_consentimiento(curso_con_indice):
    curso, indice = curso_con_indice
    from termito.modelo import ErrorCurso
    with pytest.raises(ErrorCurso):
        sesion.revelar(curso, consentimiento=True, indice=indice)
    sesion.conversar(curso, EJERCICIO, indice)
    sesion.conversar(curso, "mi intento: la brecha es enorme", indice)
    with pytest.raises(ValueError):
        sesion.revelar(curso, consentimiento=False, indice=indice)


def test_confusion_registra_duda(curso_con_indice):
    curso, indice = curso_con_indice
    r = sesion.conversar(curso, "no entiendo el overfitting", indice)
    assert r["estado_interaccion"] == "revision"
    assert r["duda"] is not None and r["duda"]["id"]


def test_conceptual_cita_o_declara_silencio(curso_con_indice):
    curso, indice = curso_con_indice
    r = sesion.conversar(curso, "¿qué es el overfitting?", indice)
    assert r["estado_interaccion"] == "revision"
    assert r["citas"]
    silencio = sesion.conversar(curso, "¿qué opina el curso de los NFT?", indice)
    assert silencio["estado_interaccion"] == "pista"   # sin fuente: orientar/esperar
    assert silencio["modo"] == "sin_fuente"


def test_fuera_del_curso_declarado(curso_con_indice):
    curso, indice = curso_con_indice
    r = sesion.conversar(curso, "aunque no sea del curso, ¿qué es Python?", indice)
    assert r["fuera_del_curso"] is True
    assert r["estado_interaccion"] == "revision"


def test_mismo_ejercicio_no_reinicia_sesion(curso_con_indice):
    curso, indice = curso_con_indice
    sesion.conversar(curso, EJERCICIO, indice)
    sesion.conversar(curso, "pista", indice)
    r = sesion.conversar(curso, EJERCICIO, indice)
    s = sesion.cargar(curso)
    assert s["pasos_revelados"] == 1   # conserva el avance
    assert r["estado_interaccion"] == "paso_mostrado"  # y su estado actual
