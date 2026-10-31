"""Política de modo compañía (H-10.1, H-10.2, T-10.2.1).

Escucha empática sin cita (acto de vínculo) y evocación de recuerdos solo
con cita validada (acto factual). Todo sin Ollama salvo los tests con
llm mockeado.
"""
from datito import evidencia, llm, tutor
from datito.indice import Indice


def _curso_compania(tmp_path_curso):
    tmp_path_curso.datos["modo"] = "compania"
    tmp_path_curso.guardar()
    ind = Indice()
    ind.registrar_recuerdo(
        "Rufo es el perro de la persona y duerme a su lado en las noches.",
        "semilla:rufo")
    return tmp_path_curso, ind


def test_escucha_empatica_sin_cita(tmp_path_curso):
    curso, ind = _curso_compania(tmp_path_curso)
    r = tutor.responder(curso, "me siento solo hoy", ind)
    assert r.modo == "compania"
    assert "No tengo fuente" not in r.texto
    assert r.texto.strip()


def test_regresion_curso_academico_sin_modo(tmp_path_curso):
    ind = Indice()
    r = tutor.responder(tmp_path_curso, "me siento solo hoy", ind)
    assert r.modo == "sin_fuente"
    assert "No tengo fuente" in r.texto


def test_recuerdo_citado_en_modo_exploracion(tmp_path_curso):
    curso, ind = _curso_compania(tmp_path_curso)
    r = tutor.responder(curso, "como esta mi perro", ind)
    assert r.modo == "compania"
    assert r.citas and r.citas[0].startswith("memoria#")
    assert "[memoria#" in r.texto                      # la cita es visible (modo exploración)
    assert evidencia.validar(r.texto, ind).ok          # y valida con el gate intacto


def test_no_alucinacion_cita_invalida(tmp_path_curso, monkeypatch):
    curso, ind = _curso_compania(tmp_path_curso)
    monkeypatch.setattr(llm, "disponible", lambda: True)
    inventado = "Ayer me contaste que tuviste fiebre alta. [memoria#99]"
    monkeypatch.setattr(llm, "generar", lambda *a, **k: inventado)
    r = tutor.responder(curso, "como esta mi perro", ind)
    assert "[memoria#99]" not in r.texto               # la cita inválida jamas sale
    assert "fiebre" not in r.texto


def test_reintento_con_contexto_menor_rescata_cita_valida(tmp_path_curso, monkeypatch):
    curso, ind = _curso_compania(tmp_path_curso)
    monkeypatch.setattr(llm, "disponible", lambda: True)
    llamadas = iter([
        "Ayer me contaste que tuviste fiebre alta. [memoria#99]",
        "Tu perro Rufo duerme a tu lado en las noches. [memoria#1]",
    ])
    monkeypatch.setattr(llm, "generar", lambda *a, **k: next(llamadas))
    r = tutor.responder(curso, "como esta mi perro", ind)
    assert r.citas == ["memoria#1"]
    assert "[memoria#99]" not in r.texto and "fiebre" not in r.texto


def test_escucha_sin_cita_con_memoria_disponible(tmp_path_curso, monkeypatch):
    curso, ind = _curso_compania(tmp_path_curso)
    monkeypatch.setattr(llm, "disponible", lambda: True)
    monkeypatch.setattr(llm, "generar",
                        lambda *a, **k: "Gracias por compartirlo conmigo; estoy aqui para escucharla.")
    r = tutor.responder(curso, "como esta mi perro", ind)
    # sin citas: escucha activa permitida aunque haya memoria recuperada
    assert r.modo == "compania" and r.citas == []
    assert "No tengo fuente" not in r.texto
