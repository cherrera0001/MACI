"""Fixtures: cursos en directorio temporal aislado (nunca toca cursos/ reales)."""
import pytest

from datito import config
from datito.modelo import crear


@pytest.fixture(autouse=True)
def _ambiente_sin_llm(monkeypatch):
    """Hermeticidad: el LLM real del entorno (Ollama instalado en la máquina
    de desarrollo, E-17) no debe filtrarse a los tests. Los tests que
    simulan el LLM lo mockean explícitamente sobre esta base."""
    from datito import llm

    monkeypatch.setattr(llm, "disponible", lambda: False)
    monkeypatch.setattr(llm, "modelo_instalado", lambda *a, **k: False)


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
