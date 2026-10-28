"""Politica socratica: el protocolo del tutor como codigo ejecutable.

Cubre las cinco reglas (R1-R5), la cadena de 4 evidencias con sus invariantes
(spec §3) y el demo sintetico de punta a punta (G10: corre en curso aislado
por la fixture tmp_path_curso, nunca en 07_DATITO).
"""
import pytest

from datito import demo_sintetico, socratico


def nueva() -> socratico.Politica:
    return socratico.Politica(socratico.Concepto("sobreajuste"),
                              solucion="SOLUCION",
                              pistas=["pista uno"], fecha="2026-10-28")


def test_no_hay_solucion_antes_de_dos_fallos():
    pol = nueva()
    a1 = pol.responder("intento", es_intento=True, acierto=False)
    assert a1.nombre == "PISTA"
    a2 = pol.responder("intento", es_intento=True, acierto=False)
    assert a2.nombre == "DESARROLLAR_SOLUCION"
    assert "SOLUCION" in a2.texto
    assert pol.metricas()["respuestas_antes_de_2_intentos"] == 0


def test_peticion_explicita_se_obedece_y_se_registra():
    pol = nueva()
    accion = pol.responder("dame la respuesta")
    assert accion.nombre == "ENTREGAR_RESPUESTA"
    assert accion.registrar_duda
    assert any(str(x).startswith("duda:") for x in pol.turnos[-1]["acciones"])


def test_modo_estricto_no_entrega_nada():
    accion = nueva().responder("no me la des, hazme pensar")
    assert accion.nombre == "PISTA"


def test_exigir_transferencia_requiere_entrega_previa():
    with pytest.raises(socratico.ErrorPolitica):
        nueva().exigir_transferencia()


def test_la_pregunta_del_tutor_cierra_el_turno():
    pol = nueva()
    accion = pol.responder("que es la brecha?")
    assert accion.nombre == "PREGUNTAR"
    assert pol.turnos[-1]["rol"] == "tutor"
    assert pol.turnos[-2]["rol"] == "alumno"   # REGLA CERO: el turno termina en la pregunta


def test_cualquier_flujo_valido_respeta_el_protocolo():
    pol = nueva()
    pol.responder("que es la brecha?")
    pol.responder("train entrena y test mide")
    pol.responder("dame la respuesta")
    pol.responder("intento", es_intento=True, acierto=False)
    pol.responder("intento", es_intento=True, acierto=False)
    pol.exigir_transferencia()
    pol.responder("intento transferencia", es_intento=True, acierto=True)
    assert pol.validar() == []
    m = pol.metricas()
    assert m["dudas_registradas"] == 2
    assert m["respuestas_antes_de_2_intentos"] == 0


def test_cadena_exige_orden_y_detalle():
    c = socratico.Concepto("x")
    with pytest.raises(socratico.ErrorEvidencia):
        c.registrar("aplicar", "sin explicar antes", "2026-10-28")
    c.registrar("explicar", "lo explico con sus palabras", "2026-10-28")
    assert c.estado == "COMPRENSION_PARCIAL"


def test_cadena_completa_llega_a_dominado():
    c = socratico.Concepto("x")
    for paso in ("explicar", "aplicar", "interpretar", "transferir"):
        c.registrar(paso, f"{paso} con detalle fechado", "2026-10-28")
    assert c.estado == "DOMINADO"


def test_reverificacion_fallida_pasa_a_repaso():
    c = socratico.Concepto("x")
    c.registrar("explicar", "...", "2026-10-28")
    c.registrar("aplicar", "...", "2026-10-28")
    assert c.estado == "COMPRENDIDO"
    c.re_verificar("2026-10-28", acierto=False, detalle="fallo la re-pregunta")
    assert c.estado == "REQUIERE_REPASO"


def test_demo_sintetico_de_punta_a_punta(tmp_path_curso):
    r = demo_sintetico.ejecutar()
    assert r["sintetico"] is True
    assert r["estado_final"] == "DOMINADO"
    assert r["violaciones_protocolo"] == []
    assert r["metricas"]["dudas_registradas"] == 2
    assert "07_DATITO" not in r["ruta_curso"]


def test_degradacion_avisa_una_vez_y_etiqueta_lo_largo():
    pol = socratico.Politica(socratico.Concepto("x"), solucion="S " * 80,
                             degradacion="indice_local")
    pol.responder("hola")
    pol.responder("dame la respuesta")
    textos = [t["texto"] for t in pol.turnos if t["rol"] == "tutor"]
    assert textos[0].startswith("El indice de transcripciones no responde")
    assert sum("no responde" in t for t in textos) == 1
    assert textos[1].startswith("[INFERENCIA]")


def test_degradacion_desconocida_se_rechaza():
    with pytest.raises(ValueError):
        socratico.Politica(socratico.Concepto("x"), degradacion="notebooklm")
