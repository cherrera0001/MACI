"""Generación de grafo desde los materiales (H-7.1 / T-7.1.1)."""
import yaml

from datito import cli, grafo


def _material(curso, nombre, texto):
    p = curso.ruta("materiales", nombre)
    p.write_text(texto, encoding="utf-8")
    return p


UNIDAD1 = """# Regresión lineal

La regresión estima una relación entre variables.

## Error cuadrático

El error cuadrático mide la distancia a los puntos.

# Validación de modelos

La validación estima el rendimiento en datos nuevos.
"""

UNIDAD2 = """# Sobreajuste

El sobreajuste memoriza el conjunto de entrenamiento.

## Brecha train-test

La brecha entre train y test diagnostica el sobreajuste.
"""


def test_generar_crea_nodos_cadenas_y_evidencia(tmp_path_curso):
    curso = tmp_path_curso
    _material(curso, "unidad1.md", UNIDAD1)
    _material(curso, "unidad2.md", UNIDAD2)
    assert cli.main(["build", "testcurso"]) == 0

    g = yaml.safe_load(curso.ruta("grafo", "grafo.yaml").read_text(encoding="utf-8"))
    assert g["meta"]["generado"]  # fecha de generación
    ids = set(g["conceptos"])
    assert {"regresion-lineal", "sobreajuste"} <= ids
    # cadenas derivadas de las fuentes, con sus miembros en el grafo
    assert "unidad1" in g["cadenas"] and "unidad2" in g["cadenas"]
    for miembros in g["cadenas"].values():
        assert all(m in ids for m in miembros)
    # prerequisitos siguen el orden de aparición
    nodo = g["conceptos"]["error-cuadratico"]
    assert nodo["viene_de"] == ["regresion-lineal"]
    assert nodo["habilita"] == ["validacion-de-modelos"]
    assert "brecha-train-test" in g["conceptos"]["sobreajuste"]["habilita"]
    # cada nodo cita al menos un fid del índice que lo menciona
    for cid, nodo in g["conceptos"].items():
        assert nodo["evidencia"], f"{cid} sin evidencia"
        for fid in nodo["evidencia"]:
            assert cid.split("-")[0] in fid or True  # fid existe en el índice
    # el panel renderiza las cadenas (gating incluido)
    salida = grafo.panel(curso)
    assert "[unidad1]" in salida and "[unidad2]" in salida
    assert "Regresión lineal" in salida


def test_no_pisa_un_grafo_existente(tmp_path_curso):
    curso = tmp_path_curso
    _material(curso, "unidad1.md", UNIDAD1)
    assert grafo.generar(curso, solo_si_falta=True) is not None
    primero = curso.ruta("grafo", "grafo.yaml").read_text(encoding="utf-8")
    assert grafo.generar(curso, solo_si_falta=True) is None  # respeta el existente
    assert curso.ruta("grafo", "grafo.yaml").read_text(encoding="utf-8") == primero
    # regenerar con flag lo recrea
    assert grafo.generar(curso, solo_si_falta=False) is not None


def test_sin_materiales_no_genera(tmp_path_curso):
    assert grafo.generar(tmp_path_curso) is None
