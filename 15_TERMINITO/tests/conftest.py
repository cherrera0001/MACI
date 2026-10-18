"""Fixtures: cursos en directorio temporal aislado (nunca toca cursos/ reales)."""
import pytest

from termito import config
from termito.modelo import crear


@pytest.fixture
def tmp_path_curso(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "DIR_CURSOS", tmp_path / "cursos")
    curso = crear("testcurso", nombre="Curso de prueba", periodo="2026-T2")
    return curso


COMPONENTES_OK = {
    "rol_dominio": "Tutor experto en fundamentos de ciencia de datos",
    "mision": "Acompanar el aprendizaje del curso hasta el certamen",
    "funciones": "Explicar, proponer ejercicios, corregir con evidencia",
    "estilo_ensenanza": "Socratico con ejemplos concretos",
    "contexto_curso": "Curso universitario de un semestre",
    "estilo_aprendizaje": "Paso a paso, con ejemplos visuales",
    "restricciones": "No inventar; fomentar razonamiento critico",
    "relacion_temporal": "Todo el semestre, recibiendo notas como retroalimentacion",
}
