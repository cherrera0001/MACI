"""Tests del ciclo de vida: notas, cierre, registro, portabilidad (FR-015/016/019)."""
import zipfile

import pytest

from termito import ciclo, config, dudas
from termito import fragmentos as frag
from termito.evaluador import ResultadoItem, Item, guardar_resultado
from termito.indice import Indice
from termito.modelo import ErrorCurso


@pytest.fixture
def curso_completo(tmp_path_curso, tmp_path):
    md = tmp_path / "clase10.md"
    md.write_text("**[0:05:10]** El overfitting memoriza el entrenamiento.\n",
                  encoding="utf-8")
    destino = tmp_path_curso.ruta("materiales", "clase10.md")
    destino.symlink_to(md)
    _, frags = frag.parsear_materiales([destino])
    Indice().construir(frags).guardar(tmp_path_curso.ruta(".indice"))
    tmp_path_curso.ruta("prompt").mkdir(exist_ok=True)
    (tmp_path_curso.ruta("prompt", "actual.md")).write_text("Eres un tutor.",
                                                           encoding="utf-8")
    tmp_path_curso.transicionar("listo")
    return tmp_path_curso


def test_nota_registra_ajustes_y_alimenta_prompt(curso_completo):
    e = ciclo.registrar_nota(curso_completo, "Certamen 1", "3,5",
                             "me faltó tiempo y precision")
    assert any("reforzar" in a for a in e["ajustes_derivados"])
    assert any("ritmo" in a or "precision" in a for a in e["ajustes_derivados"])
    assert curso_completo.datos["retroalimentacion"]


def test_nota_vacia_rechazada(curso_completo):
    with pytest.raises(ErrorCurso):
        ciclo.registrar_nota(curso_completo, "Certamen 1", "  ")


def test_nota_deriva_ajustes_de_evaluaciones_debiles(curso_completo):
    item = Item(id="d1", conceptos=["overfitting_underfitting"],
                pregunta="¿cuál memoriza?", criterios=["menciona brecha"],
                solucion="")
    guardar_resultado(curso_completo,
                      ResultadoItem(item, "x", "no_logrado", "sin criterios", []))
    e = ciclo.registrar_nota(curso_completo, "Certamen 2", "5.0", "")
    assert any("overfitting_underfitting" in a for a in e["ajustes_derivados"])


def test_cerrar_conserva_registro_entero(curso_completo):
    dudas.registrar(curso_completo, "¿qué es la brecha?", "explicación",
                    "procedimiento", ["clase10#1"])
    res = ciclo.cerrar(curso_completo)
    assert res["estado"] == "cerrado"
    assert res["registro_integro"] is True
    assert all(res["integridad"].values())
    assert curso_completo.estado == "cerrado"
    with pytest.raises(ErrorCurso):
        ciclo.cerrar(curso_completo)


def test_registro_cuenta_dudas_notas_y_sesiones(curso_completo):
    ciclo.registrar_nota(curso_completo, "Certamen 1", "4.2", "")
    dudas.registrar(curso_completo, "pregunta", "respuesta", "resolución", [])
    r = ciclo.resumen_registro(curso_completo)
    assert r["notas"] == 1 and r["dudas"] == 1
    assert r["estado"] == "listo"
    for k in ("evaluaciones", "sesiones", "mensajes", "revelaciones"):
        assert k in r


def test_exportar_materializa_symlinks(curso_completo):
    res = ciclo.exportar(curso_completo)
    with zipfile.ZipFile(res["ruta"]) as z:
        nombres = z.namelist()
        assert "curso.yaml" in nombres
        contenido = z.read("materiales/clase10.md").decode("utf-8")
    assert "overfitting" in contenido     # el symlink quedó como contenido real


def test_importar_redondo(curso_completo, tmp_path, monkeypatch):
    res = ciclo.exportar(curso_completo)
    otro = tmp_path / "otra-maquina" / "cursos"
    otro.mkdir(parents=True)
    monkeypatch.setattr(config, "DIR_CURSOS", otro)
    out = ciclo.importar(res["ruta"])
    assert out["slug"] == curso_completo.slug
    assert (otro / curso_completo.slug / "curso.yaml").exists()
    r = ciclo.resumen_registro(ciclo.cargar(out["slug"]))
    assert r["notas"] >= 0      # el curso importado carga y reporta


def test_importar_rechaza_duplicado(curso_completo):
    res = ciclo.exportar(curso_completo)
    with pytest.raises(ErrorCurso):
        ciclo.importar(res["ruta"])   # el slug ya existe en DIR_CURSOS


def test_versionar_recrea_directorio(tmp_path_curso):
    """El dir prompt/versions puede no sobrevivir al ZIP del paquete."""
    from termito import identidad
    tmp_path_curso.ruta("prompt").mkdir(exist_ok=True)
    (tmp_path_curso.ruta("prompt", "actual.md")).write_text("v1", encoding="utf-8")
    import shutil
    shutil.rmtree(tmp_path_curso.ruta("prompt", "versions"))
    identidad.versionar(tmp_path_curso, motivo="prueba")
    assert tmp_path_curso.ruta("prompt", "versions").is_dir()
    assert list(tmp_path_curso.ruta("prompt", "versions").glob("*.md"))


def test_importar_rechaza_no_zip(tmp_path):
    falso = tmp_path / "paquete.term.zip"
    falso.write_text("no es un zip", encoding="utf-8")
    with pytest.raises(ErrorCurso):
        ciclo.importar(str(falso))
