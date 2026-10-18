"""Tests: evidencia, lucha productiva, dudas."""
import pytest

from termito import evidencia
from termito.indice import Indice
from termito.lucha import LuchaProductiva


def _indice_falso():
    ind = Indice()
    ind.textos = {"t1#1": "El overfitting memoriza el entrenamiento y falla en prueba.",
                  "t1#2": "La validacion cruzada estima el error fuera de muestra."}
    ind.referencias = {"t1#1": ("t1", "0:05:10"), "t1#2": ("t1", "0:20:00")}
    return ind


def test_cita_valida():
    ind = _indice_falso()
    r = evidencia.validar("El overfitting hace que el modelo falle en prueba [t1#1].", ind)
    assert r.ok and r.citas == ["t1#1"]


def test_cita_invalida_rechazada():
    ind = _indice_falso()
    r = evidencia.validar("Afirmo esto [t9#99].", ind)
    assert not r.ok and r.invalidas == ["t9#99"]


def test_sin_citas_es_sin_fuente():
    r = evidencia.validar("No cito nada aqui.", _indice_falso())
    assert r.sin_fuente and not r.ok


def test_soporte_minimo():
    ind = _indice_falso()
    r = evidencia.validar("Las papas fritas son azules [t1#1].", ind)
    assert not r.ok and r.sin_soporte == ["t1#1"]


def test_lucha_pasos_graduales():
    l = LuchaProductiva(pasos=["paso uno", "paso dos", "paso tres"],
                        solucion="solucion completa")
    with pytest.raises(PermissionError):
        l.ver_solucion()                      # sin intento ni pasos: prohibido
    assert l.mostrar_paso() == "paso uno"
    assert l.mostrar_paso() == "paso dos"
    assert l.estado == "paso_mostrado"
    assert l.mostrar_paso() == "paso tres"
    assert l.mostrar_paso() is None           # agotados
    assert l.puede_ver_solucion()             # pasos agotados habilitan
    assert l.ver_solucion() == "solucion completa"
    assert any(r["tipo"] == "solucion" for r in l.revelaciones)


def test_lucha_intento_habilita_solucion():
    l = LuchaProductiva(pasos=["p1"], solucion="S")
    l.registrar_intento()
    assert l.estado == "revision"
    assert l.puede_ver_solucion()


def test_duda_registro(tmp_path_curso):
    from termito import dudas
    d = dudas.registrar(tmp_path_curso, "¿qué es el overfitting?",
                        "memoriza train", "pasos…", ["t1#1"], ["overfitting_underfitting"])
    assert d["estado"] == "resuelta"
    assert dudas.cargar(tmp_path_curso)[0]["pregunta"].startswith("¿qué")
