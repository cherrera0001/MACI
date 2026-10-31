"""Panel familiar y de legado (D-14.2): un solo lugar, privacidad por diseño.

Unifica el pulso del vínculo (progreso), el semáforo de bienestar y el
Libro de Historias de Vida (biografia). Las alertas se exponen SOLO con
fecha y categoría: la privacidad conversacional de D-11.3 manda también
frente al familiar (ni señales léxicas, ni texto del mensaje).
"""
from __future__ import annotations

import yaml

from . import biografia, progreso

RUTA_ALERTAS = "alertas.yaml"


def _alertas_etica(curso) -> list[dict]:
    """[{fecha, tipo}]: lo único que ve el familiar, por diseño."""
    p = curso.ruta(RUTA_ALERTAS)
    if not p.exists():
        return []
    datos = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    return [{"fecha": a.get("fecha"), "tipo": a.get("tipo")}
            for a in (datos.get("alertas") or [])]


def construir(curso, indice) -> dict:
    datos = progreso.cargar(curso)
    m = datos["metricas"]
    recuerdos = sum(
        1 for f in indice.textos if f.startswith("memoria#")
        and not indice.referencias.get(f, ("", ""))[1].startswith("guia:"))
    alertas = _alertas_etica(curso)
    return {
        "curso": {"slug": curso.slug,
                  "nombre": curso.datos.get("nombre", curso.slug),
                  "modo": "compania"},
        "pulso": {
            "racha_dias": m.get("racha_dias", 0),
            "ultima_interaccion": datos.get("ultima_interaccion"),
            "mensajes": m.get("mensajes", 0),
            "sesiones": m.get("sesiones", 0),
            "recuerdos": recuerdos,
            "talleres_completados": m.get("talleres_completados", 0),
        },
        "alertas": {"total": len(alertas), "items": alertas},
        "biografia": biografia.construir(curso, indice),
        "privacidad": ("Este panel muestra solo fechas, categorías e "
                       "historias de vida citadas: el contenido de las "
                       "conversaciones es privado."),
    }
