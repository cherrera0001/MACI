"""Parsers docx/pptx (T-7.5.1): fragmentos citables con referencia."""
import docx
from pptx import Presentation
from pptx.util import Inches

from datito import fragmentos as frag


def _docx(ruta, parrafos):
    d = docx.Document()
    for texto in parrafos:
        d.add_paragraph(texto)
    d.save(str(ruta))


def _pptx(ruta, diapositivas):
    p = Presentation()
    for titulo, cuerpo in diapositivas:
        slide = p.slides.add_slide(p.slide_layouts[5])  # solo título
        slide.shapes.title.text = titulo
        cuadro = slide.shapes.add_textbox(Inches(1), Inches(1.5),
                                          Inches(8), Inches(4))
        cuadro.text_frame.text = cuerpo
    p.save(str(ruta))


def test_docx_parsea_por_parrafo(tmp_path):
    ruta = tmp_path / "apuntes.docx"
    _docx(ruta, [
        "La regresión lineal estima una relación entre variables cuantitativas.",
        "El error cuadrático medio mide la distancia promedio a los puntos.",
    ])
    fuente, frags = frag.parsear_fuente(ruta)
    assert fuente.tipo == "docx"
    assert len(frags) >= 1
    assert any("regresión" in f.texto for f in frags)
    assert any(f.referencia.startswith("párrafo") for f in frags)


def test_pptx_parsea_por_diapositiva(tmp_path):
    ruta = tmp_path / "clase.pptx"
    largo1 = ("Memoriza el entrenamiento y falla en prueba. " * 8).strip()
    largo2 = ("Rinde bien en datos que no ha visto, porque aprendió el patrón. " * 7).strip()
    _pptx(ruta, [("Sobreajuste", largo1), ("Generalización", largo2)])
    fuente, frags = frag.parsear_fuente(ruta)
    assert fuente.tipo == "pptx"
    refs = [f.referencia for f in frags]
    # slides de +60 palabras: cada uno es fragmento propio (los cortos se fusionan)
    assert "diapositiva 1" in refs and "diapositiva 2" in refs
    assert any("Sobreajuste" in f.texto for f in frags)


def test_parsear_materiales_acepta_ambos(tmp_path):
    _docx(tmp_path / "a.docx", ["contenido suficiente para un fragmento de apuntes."])
    _pptx(tmp_path / "b.pptx", [("Tema", "contenido suficiente para una diapositiva.")])
    (tmp_path / "c.md").write_text("# Tema\n\ncontenido de apoyo suficiente.\n",
                                   encoding="utf-8")
    fuentes, frags = frag.parsear_materiales(sorted(tmp_path.iterdir()))
    assert {f.tipo for f in fuentes} == {"docx", "pptx", "md"}
    assert frags
