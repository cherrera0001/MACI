"""Tests: identidad, evaluador, grafo y flujo de integracion."""
from pathlib import Path

import yaml

from datito import config, evaluador, grafo, identidad, progreso
from datito import dudas as dudas_mod
from datito import fragmentos as frag
from datito import tutor as tutor_mod
from datito.indice import Indice

from conftest import COMPONENTES_OK


def test_identidad_flujo_completo(tmp_path_curso):
    c = tmp_path_curso
    ok, faltantes = identidad.completos(identidad.cargar(c))
    assert not ok and len(faltantes) == 8
    identidad.guardar(c, COMPONENTES_OK)
    ruta = identidad.generar_prompt(c)
    texto = ruta.read_text(encoding="utf-8")
    assert "Socratico" in texto and "Razonamiento" not in texto or "razonamiento" in texto
    # versionado: regenerar tras editar componente crea version
    datos = dict(COMPONENTES_OK)
    datos["mision"] = "Nueva mision"
    identidad.guardar(c, datos)
    identidad.generar_prompt(c)
    man = yaml.safe_load(c.ruta("prompt", "versions", "manifest.yaml").read_text())
    assert len(man) == 1 and "regenerado" in man[0]["motivo"]
    v = man[0]["version"]
    identidad.revertir(c, v)
    assert "Socratico" in c.ruta("prompt", "actual.md").read_text(encoding="utf-8")


def test_evaluador_distincion_y_fallback(tmp_path_curso):
    c = tmp_path_curso
    item = {
        "id": "d1", "conceptos": ["overfitting_underfitting", "generalizacion"],
        "pregunta": "Un modelo con 99% en train y 55% en test: ¿sobreajusta, subajusta o esta bien? ¿y uno con 60%/58%?",
        "criterios": ["identifica overfitting 99/55", "identifica underfitting 60/58",
                      "menciona memorizacion train", "menciona generalizacion"],
        "pasos": ["comparar train vs test", "inferir brecha"],
        "solucion": "99/55 sobreajusta; 60/58 subajusta",
    }
    (c.ruta("evaluaciones") / "distinciones.yaml").write_text(
        yaml.safe_dump({"items": [item]}, allow_unicode=True), encoding="utf-8")
    items = evaluador.cargar_items(c)
    assert len(items) == 1 and len(items[0].conceptos) == 2
    res = evaluador._calificar_heuristica(
        items[0], "El 99/55 es overfitting: hay memorizacion del train y no generaliza; "
                  "el 60/58 es underfitting, un modelo demasiado simple")
    assert res.resultado == "logrado"
    res2 = evaluador._calificar_heuristica(items[0], "no se nada")
    assert res2.resultado == "no_logrado"
    # item con <2 conceptos se rechaza
    mal = dict(item, id="d2", conceptos=["solo_uno"])
    (c.ruta("evaluaciones") / "malo.yaml").write_text(
        yaml.safe_dump({"items": [mal]}, allow_unicode=True), encoding="utf-8")
    assert len(evaluador.cargar_items(c)) == 1


def test_grafo_dominio_y_panel(tmp_path_curso):
    c = tmp_path_curso
    g = {"meta": {}, "cadenas": {"del error a la validacion": ["overfitting_underfitting"]},
         "nodos": {"overfitting_underfitting": {
             "nombre": "Overfitting y underfitting",
             "viene_de": ["generalizacion"], "habilita": ["arboles_decision"],
             "requiere_antes": ["generalizacion"]}}}
    (c.ruta("grafo") / "grafo.yaml").write_text(
        yaml.safe_dump(g, allow_unicode=True), encoding="utf-8")
    grafo.actualizar_dominio(c, ["overfitting_underfitting"], "no_logrado")
    assert grafo.estado_nodo(c, "overfitting_underfitting") == "en_estudio"
    grafo.actualizar_dominio(c, ["overfitting_underfitting"], "logrado")
    assert grafo.estado_nodo(c, "overfitting_underfitting") == "comprendido"  # habilita no dominado
    panel = grafo.panel(c, mapa_completo=True, color=False)
    assert "Overfitting y underfitting" in panel
    assert "comprendido" in panel or "●" in panel


def test_integracion_curso_a_dominio(tmp_path_curso, tmp_path):
    """Flujo completo: materiales -> build -> chat (modo exploracion) -> eval -> status."""
    c = tmp_path_curso
    mat = tmp_path / "materiales"
    mat.mkdir()
    (mat / "clase_overfitting.md").write_text(
        "**[0:05:10]** El overfitting ocurre cuando el modelo memoriza los datos de "
        "entrenamiento y falla al generalizar en datos de prueba.\n\n"
        "**[0:06:30]** El underfitting es lo contrario: el modelo es demasiado simple "
        "y ni siquiera aprende el patron del entrenamiento.\n", encoding="utf-8")
    destino = c.ruta("materiales", "clase_overfitting.md")
    destino.symlink_to(mat / "clase_overfitting.md")
    identidad.guardar(c, COMPONENTES_OK)
    identidad.generar_prompt(c)
    # build manual (mismo efecto que CLI)
    fuentes, frags = frag.parsear_materiales([destino])
    indice = Indice().construir(frags)
    indice.guardar(c.ruta(".indice"))
    c.transicionar("listo")
    # chat en modo exploracion (sin Ollama en CI): recupera evidencia citada
    resp = tutor_mod.responder(c, "¿qué diferencia hay entre overfitting y underfitting?",
                               indice)
    assert resp.modo == "exploracion"
    assert resp.citas and resp.citas[0].startswith("clase-overfitting#")
    # eval
    item = {"id": "d1", "conceptos": ["overfitting_underfitting", "generalizacion"],
            "pregunta": "¿Cual memoriza y cual es demasiado simple?",
            "criterios": ["memoriza entrenamiento", "modelo simple"],
            "solucion": "overfitting memoriza; underfitting simple"}
    (c.ruta("evaluaciones") / "d.yaml").write_text(
        yaml.safe_dump({"items": [item]}, allow_unicode=True), encoding="utf-8")
    items = evaluador.cargar_items(c)
    res = evaluador._calificar_heuristica(
        items[0], "overfitting memoriza el entrenamiento; underfitting es modelo simple")
    assert res.resultado == "logrado"
    # dudas + progreso
    dudas_mod.registrar(c, "¿diferencia?", "over memoriza, under simple",
                        "comparar train/test", resp.citas)
    assert len(dudas_mod.cargar(c)) == 1
    progreso.iniciar_sesion(c)
    n, ok = progreso.contar_distincion(c, True)
    assert (n, ok) == (1, 1)
    assert "1/1" in progreso.resumen(c)
