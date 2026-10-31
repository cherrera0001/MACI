#!/usr/bin/env python3
"""Genera la instancia semilla ``cursos/compania/`` (T-10.4.1, H-10.4).

Idempotente: si la instancia existe, repone prompt, índice (memorias que
falten) y talleres.yaml. Stdlib + el paquete datito; sin red ni LLM.

  python3 15_TERMINITO/scripts/semilla_compania.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

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
    ("Su perro Rufo vive con usted desde que era cachorro y le hace "
     "compañía en las mañanas.", "semilla:rufo"),
    ("Su hermana Carmen vive en Temuco; se ven juntas en las vacaciones "
     "de verano.", "semilla:carmen"),
    ("El veterinario del Dr. Fuentes atiende a Rufo cuando está enfermo; "
     "queda cerca de la plaza.", "semilla:veterinario"),
    ("Le gusta tejer bufandas para sus nietas en las tardes de invierno.",
     "semilla:tejido"),
    ("Carmen le recomendó el teléfono nuevo que usa ahora; lo compraron "
     "juntas en el centro.", "semilla:telefono"),
    ("Guarda las fotos de sus nietas en el teléfono nuevo para "
     "enséñárselas cuando la visitan.", "semilla:fotos"),
    ("Si un mensaje o llamada pide claves, contraseñas o dinero con "
     "urgencia, es estafa: corte, no comparta nada y consulte con alguien "
     "de confianza.", "guia:anti-estafa-1"),
    ("Los bancos nunca piden claves por teléfono ni por mensaje; un "
     "premio inesperado es señal de engaño, verifíquelo siempre con su "
     "familia antes de responder.", "guia:anti-estafa-2"),
    ("Su rutina: té en las tardes, caminar un poco por la casa y llamar a "
     "su hermana los domingos; la rutina la mantiene tranquila.",
     "guia:bienestar"),
    ("Para ver a su familia por videollamada abra la aplicación verde de "
     "la cámara, toque el nombre de su contacto y elija el ícono de video; "
     "si no contestan, deje un mensaje de voz con cariño.",
     "guia:telefono-videollamada"),
    ("Para ordenar sus gastos del mes anote en un cuaderno lo que entra —"
     "la pensión y otros ingresos— y lo que sale: luz, agua, comida y "
     "medicamentos; cada semana descuente lo gastado para saber cuánto le "
     "queda.", "guia:presupuesto-casero"),
]

# Micro-talleres prácticos (D-14.1): cada paso cita su guía [fid] y debe
# compartir al menos MIN_OVERLAP tokens de contenido con ella
# (evidencia.validar). guia_ref se resuelve a guia_fid al construir.
TALLERES = [
    {"id": "anti-estafa-cotidiano",
     "titulo": "Revisar un mensaje sospechoso",
     "tema": "estafa claves banco mensaje urgencia",
     "guia_ref": "guia:anti-estafa-1",
     "pasos": [
         {"objetivo": ("Ante un mensaje que pida claves o contraseñas con "
                       "urgencia, deténgase: no responda ni toque enlaces."),
          "ayuda": ("Respire y recuerde: ningún banco pide claves por "
                    "mensaje. Solo déjelo ahí, sin prisa.")},
         {"objetivo": ("Si habla de un premio, una transferencia o datos de "
                       "su cuenta, trátelo como estafa: corte y no comparta."),
          "ayuda": ("Piense en la señal de alarma: «premio» y «urgente» "
                    "juntas casi siempre son engaño.")},
         {"objetivo": ("Corte la comunicación y consulte con alguien de "
                       "confianza antes de responder o pagar."),
          "ayuda": ("Llame a su hermana o a un vecino y léales el mensaje; "
                    "decidir en compañía siempre es más seguro.")}]},
    {"id": "videollamada-familia",
     "titulo": "Videollamar a su familia",
     "tema": "videollamada teléfono familia nietas fotos",
     "guia_ref": "guia:telefono-videollamada",
     "pasos": [
         {"objetivo": ("Abra la aplicación de videollamada y toque el "
                       "nombre de su contacto en la lista."),
          "ayuda": ("Es el ícono verde de la cámara; buscar entre los "
                    "contactos ya es practicar.")},
         {"objetivo": ("Elija el ícono de video para llamar y espere con "
                       "calma a que conteste."),
          "ayuda": ("Si no contestan, no pasa nada: deje un mensaje de "
                    "voz con cariño.")},
         {"objetivo": ("Al terminar, cuelgue con el botón rojo; enséñele "
                       "después sus fotos en el teléfono."),
          "ayuda": ("Repetir la llamada otro día la hará cada vez más "
                    "fácil. Las fotos de sus nietas alegran la visita.")}]},
    {"id": "presupuesto-del-mes",
     "titulo": "Ordenar los gastos del mes",
     "tema": "gastos presupuesto cuaderno pensión mes",
     "guia_ref": "guia:presupuesto-casero",
     "pasos": [
         {"objetivo": ("Tome su cuaderno y anote lo que entra este mes: "
                       "la pensión y cualquier otro ingreso."),
          "ayuda": "Solo números redondos; no necesita ser exacto."},
         {"objetivo": ("Liste los gastos que salen: luz, agua, comida y "
                       "medicamentos; réstelos del total."),
          "ayuda": ("Si algo le queda grande, anote solo los tres gastos "
                    "más importantes.")},
         {"objetivo": ("Cada semana descuente lo gastado y anote cuánto le "
                       "queda para el resto del mes."),
          "ayuda": ("Ver el número escrito le da control: es su propio "
                    "presupuesto casero.")}]},
]


def _repoblar_indice(curso) -> Indice:
    """Índice completo de la semilla: agrega las memorias que falten."""
    if not curso.ruta(".indice").exists():
        indice = Indice()
        for texto, ref in MEMORIAS_SEMILLA:
            indice.registrar_recuerdo(texto, ref)
        indice.guardar(curso.ruta(".indice"))
        return indice
    indice = Indice.cargar(curso.ruta(".indice"))
    refs = {indice.referencias[f][1] for f in indice.textos}
    faltan = [(t, r) for t, r in MEMORIAS_SEMILLA if r not in refs]
    if faltan:
        for texto, ref in faltan:
            indice.registrar_recuerdo(texto, ref)
        indice.guardar(curso.ruta(".indice"))
    return indice


def _escribir_talleres(curso, indice):
    """talleres.yaml con guia_fid resuelto (idempotente)."""
    ref_a_fid = {ref: f for f, (_, ref) in indice.referencias.items()}
    talleres = []
    for t in TALLERES:
        copia = {k: v for k, v in t.items() if k != "guia_ref"}
        copia["guia_fid"] = ref_a_fid.get(t["guia_ref"], "")
        talleres.append(copia)
    curso.ruta("talleres.yaml").write_text(
        yaml.safe_dump({"talleres": talleres}, allow_unicode=True,
                       sort_keys=False),
        encoding="utf-8")


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

    indice = _repoblar_indice(curso)
    _escribir_talleres(curso, indice)

    if curso.estado == "configurando":
        curso.transicionar("listo")

    return {"slug": slug, "estado": curso.estado,
            "memorias": len(indice.textos), "prompt": str(prompt)}


if __name__ == "__main__":
    info = construir()
    print(f"semilla lista: cursos/{info['slug']} · estado {info['estado']} · "
          f"{info['memorias']} memorias · prompt en {info['prompt']}")
