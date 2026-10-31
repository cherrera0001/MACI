#!/usr/bin/env python3
"""Genera la instancia semilla ``cursos/compania/`` (T-10.4.1, H-10.4).

Idempotente: si la instancia existe, repone prompt e índice solo si faltan.
Stdlib + el paquete datito; sin red ni LLM.

  python3 15_TERMINITO/scripts/semilla_compania.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from datito import config, identidad  # noqa: E402
from datito.indice import Indice  # noqa: E402
from datito.modelo import cargar, crear  # noqa: E402

COMPONENTES_COMPANIA = {
    "rol_dominio": "Companero de conversacion y estimulacion cognitiva",
    "mision": ("Acompanar a personas que viven solas: escuchar con empatia, "
               "recordar su vida solo con verificacion y estimular su "
               "autonomia digital sin evaluarla nunca"),
    "funciones": ("Conversar a diario, registrar recuerdos episodicos con "
                  "consentimiento, evocarlos solo con cita validada [memoria#n] "
                  "y proponer pistas decrecientes para habilidades practicas "
                  "(uso del telefono, prevencion de estafas)"),
    "estilo_ensenanza": "Escucha activa, frases cortas y calidas, preguntas abiertas",
    "contexto_curso": ("Acompanamiento de una persona mayor que vive sola; la "
                       "confianza se construye con memoria verificable"),
    "estilo_aprendizaje": "Ritmo propio, sin examenes, celebrando cada intento",
    "restricciones": "Jamás inventar recuerdos; citar [memoria#n] al evocar",
    "relacion_temporal": ("Acompanamiento sostenido; el vinculo se mide en "
                          "racha, frecuencia y confianza"),
}

MEMORIAS_SEMILLA = [
    ("Rufo es el perro de la persona; vive con ella desde cachorro y le "
     "hace compania en las mananas.", "semilla:rufo"),
    ("La hermana de la persona se llama Carmen y vive en Temuco; se ven "
     "juntas cada vacaciones de verano.", "semilla:carmen"),
    ("El veterinario del Dr. Fuentes atiende a Rufo cuando esta enfermo; "
     "queda cerca de la plaza.", "semilla:veterinario"),
    ("A la persona le gusta tejer bufandas para sus nietas en las tardes "
     "de invierno.", "semilla:tejido"),
    ("Carmen recomendo el telefono nuevo que la persona usa ahora; lo "
     "compraron juntas en el centro.", "semilla:telefono"),
    ("La persona guarda las fotos de sus nietas en el telefono nuevo para "
     "ensenarselas cuando la visitan.", "semilla:fotos"),
]


def construir() -> dict:
    """Crea (o repone) la instancia semilla y devuelve un resumen."""
    slug = "compania"
    ruta = config.DIR_CURSOS / slug / "curso.yaml"
    curso = cargar(slug) if ruta.exists() else \
        crear(slug, nombre="Compañía y estimulación cognitiva", periodo="")
    curso.datos["modo"] = "compania"
    curso.guardar()

    identidad.guardar(curso, COMPONENTES_COMPANIA)
    prompt = identidad.generar_prompt(curso, COMPONENTES_COMPANIA)

    if not curso.ruta(".indice").exists():
        indice = Indice()
        fids = [indice.registrar_recuerdo(texto, ref)
                for texto, ref in MEMORIAS_SEMILLA]
        indice.guardar(curso.ruta(".indice"))
    else:
        indice = Indice.cargar(curso.ruta(".indice"))
        fids = [f for f in indice.textos if f.startswith("memoria#")]

    if curso.estado == "configurando":
        curso.transicionar("listo")

    return {"slug": slug, "estado": curso.estado,
            "memorias": len(fids), "prompt": str(prompt)}


if __name__ == "__main__":
    info = construir()
    print(f"semilla lista: cursos/{info['slug']} · estado {info['estado']} · "
          f"{info['memorias']} memorias · prompt en {info['prompt']}")
