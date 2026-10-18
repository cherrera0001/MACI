"""Tests: fragmentos e indice."""
from pathlib import Path

from datito import fragmentos as frag
from datito.indice import Indice


def test_parse_md_con_timestamps(tmp_path: Path):
    md = tmp_path / "clase8.md"
    md.write_text(
        "**[0:05:10]** El overfitting es cuando el modelo memoriza el train.\n\n"
        "**[0:06:00]** El underfitting es cuando ni siquiera aprende el patron.\n\n"
        "# Seccion dos\n"
        "La validacion cruzada divide los datos en pliegues para estimar error.\n"
        "Cada pliegue se usa como prueba una vez.\n", encoding="utf-8")
    fuente, frags = frag.parsear_fuente(md)
    assert fuente.id == "clase8"
    assert len(frags) >= 2            # la seccion cierra un fragmento propio
    assert frags[0].referencia == "0:05:10"
    assert all(f.fid.startswith("clase8#") for f in frags)
    seccion = [f for f in frags if str(f.referencia).startswith("#")]
    assert seccion, "la cabecera debe abrir un fragmento"


def test_parse_html_secciones(tmp_path: Path):
    h = tmp_path / "visual.html"
    h.write_text("<html><body><h2 id='sesgo'>Sesgo y varianza</h2>"
                 "<p>El sesgo es el error por suposiciones simplistas del modelo.</p>"
                 "<h2 id='tradeoff'>Tradeoff</h2>"
                 "<p>A medida que baja sesgo sube varianza y al reves.</p>"
                 "</body></html>", encoding="utf-8")
    _, frags = frag.parsear_fuente(h)
    refs = {f.referencia for f in frags}
    assert "#sesgo" in refs and "#tradeoff" in refs  # cada seccion = un fragmento


def test_tamano_fragmentos(tmp_path: Path):
    txt = tmp_path / "grande.txt"
    txt.write_text("palabra " * 3000, encoding="utf-8")
    _, frags = frag.parsear_fuente(txt)
    assert all(f.tokens <= frag.TAMANO_MAX + 60 for f in frags)
    assert sum(f.tokens for f in frags) >= 2900


def test_indice_recupera_relevante(tmp_path: Path):
    a = tmp_path / "a.md"
    a.write_text("Overfitting: el modelo memoriza el entrenamiento y falla en prueba.",
                 encoding="utf-8")
    b = tmp_path / "b.md"
    b.write_text("La limpieza de datos elimina duplicados y corrige tipos.",
                 encoding="utf-8")
    fuentes, frags = frag.parsear_materiales([a, b])
    indice = Indice().construir(frags)
    top = indice.buscar("¿qué es el overfitting?", k=2)
    assert top and top[0][0].startswith("a#")
    indice.guardar(tmp_path / ".indice")
    ind2 = Indice.cargar(tmp_path / ".indice")
    assert ind2.buscar("overfitting", k=1)[0][0] == top[0][0]
