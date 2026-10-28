"""Protocolo UNO-B + R5 + metricas en el chat real (intercambio).

La solucion revelada se registra en dudas.yaml ANTES de decirse, la respuesta
siguiente exige la transferencia, y la sesion acumula las 3 metricas del
spec 002 (REQ-TUT-002). Reutiliza el fixture curso_con_indice de conftest.
"""
import pytest

from datito import dudas, sesion

EJERCICIO = ("Ejercicio: tres modelos, R2 train/test "
             "A 0.62/0.59 B 0.98/0.54 C 0.41/0.39. ¿Cuál sobreajusta?")


@pytest.fixture
def curso_con_indice(tmp_path_curso, tmp_path):
    from datito.indice import Indice
    from datito import fragmentos as frag
    md = tmp_path / "clase.md"
    md.write_text("**[0:10:00]** Sobreajustar es error bajo en train y alto en "
                  "test; la brecha lo diagnostica.\n", encoding="utf-8")
    destino = tmp_path_curso.ruta("materiales", "clase.md")
    destino.symlink_to(md)
    _, frags = frag.parsear_materiales([destino])
    Indice().construir(frags).guardar(tmp_path_curso.ruta(".indice"))
    return tmp_path_curso


def _indice(curso):
    from datito.indice import Indice
    return Indice.cargar(curso.ruta(".indice"))


def test_solucion_revelada_se_registra_en_dudas(curso_con_indice):
    indice = _indice(curso_con_indice)
    sesion.intercambio(curso_con_indice, EJERCICIO, indice)          # abre
    sesion.intercambio(curso_con_indice, "mi respuesta: B está bien", indice)  # intento
    out = sesion.intercambio(curso_con_indice, "dame la respuesta", indice)    # revela
    assert out.get("solucion_revelada")
    registradas = dudas.cargar(curso_con_indice)
    assert len(registradas) == 1
    assert "Sobreajustar" in registradas[0]["respuesta"] or \
        "brecha" in registradas[0]["resolucion"].lower()


def test_tras_revelar_se_exige_transferencia(curso_con_indice):
    indice = _indice(curso_con_indice)
    sesion.intercambio(curso_con_indice, EJERCICIO, indice)
    sesion.intercambio(curso_con_indice, "mi intento: A", indice)
    sesion.intercambio(curso_con_indice, "dame la respuesta", indice)
    siguiente = sesion.intercambio(curso_con_indice, "vale, lo reviso", indice)
    assert "transferir" in siguiente["texto"].lower()
    m = sesion.metricas(curso_con_indice)
    assert m["soluciones"] == 1
    assert m["transferencias_exigidas"] == 1
    assert m["dudas_registradas"] == 1


def test_metricas_consistentes(curso_con_indice):
    # sin LLM local el tutor de exploracion no formula preguntas de cierre:
    # los contadores deben reflejarlo (0/0), no inventarlas
    indice = _indice(curso_con_indice)
    sesion.intercambio(curso_con_indice, EJERCICIO, indice)
    sesion.intercambio(curso_con_indice, "mi intento: B", indice)
    m = sesion.metricas(curso_con_indice)
    assert m["esperas_reales"] <= m["preguntas"]


def test_la_politica_no_se_ablando(curso_con_indice):
    # revelar antes del intento sigue rechazado (principio III intacto)
    indice = _indice(curso_con_indice)
    sesion.intercambio(curso_con_indice, EJERCICIO, indice)
    out = sesion.intercambio(curso_con_indice, "dame la respuesta", indice)
    assert not out.get("solucion_revelada")
    assert "todavia no has intentado" in out["texto"].lower()
    assert dudas.cargar(curso_con_indice) == []


def test_metricas_sobreviven_a_nuevo_ejercicio(curso_con_indice):
    indice = _indice(curso_con_indice)
    sesion.intercambio(curso_con_indice, EJERCICIO, indice)
    sesion.intercambio(curso_con_indice, "mi intento: B", indice)
    sesion.intercambio(curso_con_indice, "dame la respuesta", indice)
    otro = "Ejercicio nuevo: ¿qué métrica uso con clases desbalanceadas?"
    sesion.intercambio(curso_con_indice, otro, indice)
    m = sesion.metricas(curso_con_indice)
    assert m["soluciones"] == 1
