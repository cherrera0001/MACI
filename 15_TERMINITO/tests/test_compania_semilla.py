"""La semilla cursos/compania/ construye una instancia funcional (H-10.4)."""
import importlib.util
from pathlib import Path

from datito import config, identidad
from datito.indice import Indice
from datito.modelo import cargar

RAIZ = Path(__file__).resolve().parents[1]


def _cargar_script():
    spec = importlib.util.spec_from_file_location(
        "semilla_compania", RAIZ / "scripts" / "semilla_compania.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_semilla_construye_instancia_funcional(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "DIR_CURSOS", tmp_path / "cursos")
    info = _cargar_script().construir()
    assert info["slug"] == "compania" and info["memorias"] == 6

    curso = cargar("compania")
    assert identidad.es_compania(curso)

    indice = Indice.cargar(curso.ruta(".indice"))
    assert "memoria#6" in indice.textos
    salto = [f for f, _, _ in indice.buscar_asociativo("mi hermana", k=6, saltos=2)]
    assert "memoria#6" in salto            # la semilla conecta el grafo asociativo

    prompt = curso.ruta("prompt", "actual.md").read_text(encoding="utf-8")
    assert "JAMAS inventes recuerdos" in prompt
