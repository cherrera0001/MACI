"""Demo sintetico: un estudiante de juguete recorre el ciclo completo del tutor.

G10 (sintetico != validacion real): todo lo que toca este demo es un curso
sandbox autocontenido (cursos/demo-socratico/), creado y destruible, con datos
de juguete etiquetados SINTETICO. No toca 07_DATITO/ ni el progreso real.
El valor del demo es doble: prueba el motor de politica de punta a punta y
deja un transcript que el harness de especificacion validaria.

Uso: python -m datito.demo_sintetico [--json]
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import yaml

from . import config, modelo, socratico

SLUG = "demo-socratico"
FRAGMENTOS = [
    ("f1", "Diagnostico de sobreajuste",
     "Sobreajustar es tener error muy bajo en entrenamiento y alto fuera de el. "
     "Se diagnostica con la brecha entre ambos, no con un solo numero."),
    ("f2", "Subajuste",
     "Subajustar es fallar en ambos: el modelo no capto la estructura. Con una "
     "metrica de error, menos es mejor; con R2, mas es mejor."),
]

GUION = [
    # (mensaje del estudiante, kwargs de responder, exigir_transferencia despues)
    ("¿que diferencia hay entre train y test?", {}, False),   # -> PREGUNTA (REGLA CERO)
    ("train entrena y test mide, pero no se por que", {}, False),  # espera real
    ("dame la respuesta", {}, False),                         # G11: se obedece
    ("(intento) diagnostica sin calcular la brecha", {"es_intento": True, "acierto": False}, False),
    ("(intento) invierte la metrica", {"es_intento": True, "acierto": False}, True),
    # tras 2 fallos: la politica desarrolla la solucion (R3) y exige transferencia (R5)
    ("transfiere: un tecnico de planta...", {"es_intento": True, "acierto": True}, False),
]


def _curso_demo() -> modelo.Curso:
    dir_demo = config.DIR_CURSOS / SLUG
    if dir_demo.exists():
        shutil.rmtree(dir_demo)
    curso = modelo.crear(SLUG, nombre="Demo Socratico (SINTETICO)",
                         periodo="demo", idioma="es")
    frag_dir = dir_demo / "fragmentos"
    frag_dir.mkdir(exist_ok=True)
    datos = [{"id": fid, "fuente": fuente, "texto": texto}
             for fid, fuente, texto in FRAGMENTOS]
    (frag_dir / "demo.yaml").write_text(
        yaml.safe_dump({"origen": "SINTETICO (G10): datos de juguete para el demo",
                        "fragmentos": datos}, allow_unicode=True),
        encoding="utf-8")
    eva_dir = dir_demo / "evaluaciones"
    eva_dir.mkdir(exist_ok=True)
    (eva_dir / "demo.yaml").write_text(yaml.safe_dump(
        {"items": [{"id": "e1", "conceptos": ["demo"],
                    "pregunta": "brecha grande entre train y test: que es?",
                    "criterios": ["brecha"], "pasos": [], "solucion": "sobreajuste"}]},
        allow_unicode=True), encoding="utf-8")
    return curso


def ejecutar() -> dict:
    curso = _curso_demo()
    concepto = socratico.Concepto("sobreajuste_demo")
    politica = socratico.Politica(
        concepto,
        solucion="sobreajuste: brecha grande entre entrenamiento y prueba",
        pistas=["Calcula la brecha de cada par antes de etiquetar.",
                "Con MAE menos es mejor; con R2 mas es mejor."],
        fecha="2026-10-28")

    politica.turnos.append({"rol": "tutor",
                            "texto": "[demo] Explicacion desde el indice (modo exploracion)"})
    acciones = []
    for mensaje, kw, transferir in GUION:
        accion = politica.responder(mensaje, **kw)
        acciones.append({"entrada": mensaje, "accion": politica.turnos[-1]["texto"][:60]})
        if transferir:
            politica.exigir_transferencia()

    # cadena de evidencia completa -> DOMINADO (reglas del spec §3)
    concepto.registrar("explicar", "lo explico con sus palabras (demo)", "2026-10-28")
    concepto.registrar("aplicar", "resolvio el caso A/B/C (demo)", "2026-10-28")
    concepto.registrar("interpretar", "leyo la cifra y dijo que significa (demo)", "2026-10-28")
    concepto.registrar("transferir", "resolvio el caso de la planta (demo)", "2026-10-28")

    violaciones = politica.validar()
    return {
        "curso": SLUG, "sintetico": True,
        "estado_final": concepto.estado,
        "violaciones_protocolo": violaciones,
        "metricas": politica.metricas(),
        "transcript": politica.turnos,
        "acciones": acciones,
        "ruta_curso": str(curso.dir),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Demo sintetico del tutor (G10).")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    resultado = ejecutar()
    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        print(f"estado final del concepto: {resultado['estado_final']}")
        print(f"violaciones del protocolo: {resultado['violaciones_protocolo'] or 'ninguna'}")
        print(f"metricas: {resultado['metricas']}")
        print(f"curso sandbox: {resultado['ruta_curso']} (SINTETICO, sin tocar 07_DATITO)")
    return 1 if resultado["violaciones_protocolo"] else 0


if __name__ == "__main__":
    sys.exit(main())
