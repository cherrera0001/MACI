"""Sugerencias de identidad desde el índice (T-7.6.1)."""
from datito import identidad
from datito.indice import Indice
from datito import fragmentos as frag


def _curso_con_indice(tmp_path_curso, tmp_path):
    mat = tmp_path / "mat.md"
    mat.write_text(
        "# Sobreajuste\n\n"
        "El sobreajuste memoriza el entrenamiento y falla en datos nuevos. "
        "La brecha entre entrenamiento y prueba diagnostica el sobreajuste "
        "con una diferencia grande de rendimiento entre ambos conjuntos.\n",
        encoding="utf-8")
    destino = tmp_path_curso.ruta("materiales", "mat.md")
    destino.symlink_to(mat)
    fuentes, frags = frag.parsear_materiales([destino])
    Indice().construir(frags).guardar(tmp_path_curso.ruta(".indice"))
    return tmp_path_curso


def test_sugerencias_desde_el_indice(tmp_path_curso, tmp_path):
    curso = _curso_con_indice(tmp_path_curso, tmp_path)
    s = identidad.sugerencias(curso)
    assert s["rol_dominio"] == "Tutor experto en Curso de prueba"
    assert "mat" in s["contexto_curso"]          # nombre de la fuente
    assert "sobreajuste" in s["contexto_curso"]  # término central del índice


def test_sin_indice_devuelve_vacio(tmp_path_curso):
    assert identidad.sugerencias(tmp_path_curso) == {}


def test_el_wizard_las_usa_como_defaults(tmp_path_curso, tmp_path, monkeypatch):
    curso = _curso_con_indice(tmp_path_curso, tmp_path)
    defaults = identidad.sugerencias(curso)
    datos = identidad.wizard(curso, defaults=defaults, input_fn=lambda _: "",
                             print_fn=lambda *_: None)
    assert datos["rol_dominio"] == defaults["rol_dominio"]
    assert datos["contexto_curso"] == defaults["contexto_curso"]
    # lo que el estudiante escribe siempre gana
    contestadas = {"n": 0}

    def _input(prompt):
        contestadas["n"] += 1
        return "mi rol personalizado" if contestadas["n"] == 1 else ""

    datos2 = identidad.wizard(curso, defaults=defaults, input_fn=_input,
                              print_fn=lambda *_: None)
    assert datos2["rol_dominio"] == "mi rol personalizado"
