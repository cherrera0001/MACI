"""Ciclo de vida del Termito (US4): notas como retroalimentacion, cierre,
registro integral y portabilidad (FR-015, FR-016, FR-019, SC-005).

Todo vive en archivos del curso (FR-021): notas.yaml, curso.yaml
(retroalimentacion derivada), sesion.yaml, y exportados/{slug}.term.zip.
"""
from __future__ import annotations

import datetime
import zipfile

import yaml

from . import config, dudas, progreso, sesion
from .evaluador import cargar_resultados_guardados
from .modelo import ErrorCurso, cargar


def _hoy() -> str:
    return datetime.date.today().isoformat()


# --- Notas (FR-015) -----------------------------------------------------------

def _ruta_notas(curso):
    return curso.ruta("notas.yaml")


def cargar_notas(curso) -> list[dict]:
    p = _ruta_notas(curso)
    if not p.exists():
        return []
    return (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("notas", [])


def _ajustes_desde_nota(curso, nota: str, observaciones: str) -> list[str]:
    """Regla determinista: convierte nota + observaciones en ajustes concretos."""
    ajustes = []
    try:
        valor = float(str(nota).replace(",", "."))
        if valor < 4.0:
            ajustes.append("reforzar los conceptos con mas errores en las "
                           "proximas explicaciones y ejercicios")
    except (TypeError, ValueError):
        pass
    obs = (observaciones or "").lower()
    if any(m in obs for m in ("tiempo", "no alcance", "lento", "rapido", "rápido")):
        ajustes.append("ajustar la longitud de las explicaciones y el ritmo")
    if any(m in obs for m in ("precision", "precisión", "signos", "errores de calculo",
                              "cálculo", "calculo", "distra")):
        ajustes.append("proponer ejercicios de precision con revision paso a paso")
    # reforzar conceptos no logrados en evaluaciones recientes
    recientes = cargar_resultados_guardados(curso)[-5:]
    debiles = sorted({c for r in recientes if r.get("resultado") != "logrado"
                      for c in r.get("conceptos", [])})
    for c in debiles:
        ajustes.append(f"reforzar la distincion de {c}")
    return ajustes


def registrar_nota(curso, evaluacion: str, nota: str,
                   observaciones: str = "") -> dict:
    if not str(nota).strip():
        raise ErrorCurso("nota_vacia")
    notas = cargar_notas(curso)
    ajustes = _ajustes_desde_nota(curso, nota, observaciones)
    entrada = {"fecha": _hoy(), "evaluacion": evaluacion.strip(),
               "nota": str(nota).strip(),
               "observaciones": observaciones.strip(),
               "ajustes_derivados": ajustes}
    notas.append(entrada)
    _ruta_notas(curso).write_text(
        yaml.safe_dump({"notas": notas}, allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    # la retroalimentacion alimenta al prompt desde la siguiente interaccion
    retro = curso.datos.setdefault("retroalimentacion", [])
    retro.append(f"[{entrada['fecha']}] {evaluacion.strip()}: nota {entrada['nota']}"
                 + (f" — {observaciones.strip()}" if observaciones.strip() else ""))
    curso.guardar()
    return entrada


# --- Cierre (FR-016) ----------------------------------------------------------

def _parsea_ok(p) -> bool:
    try:
        yaml.safe_load(p.read_text(encoding="utf-8"))
        return True
    except Exception:  # noqa: BLE001 - integridad: cualquier error de parseo
        return False


def _integridad(curso) -> dict:
    """El registro que el estudiante conserva (FR-016): lo que existe, íntegro.
    Un curso puede cerrarse sin haber chateado: dudas/progreso son opcionales."""
    checks = {
        "evaluaciones": curso.ruta("evaluaciones").exists(),
        "evidencias": curso.ruta(".indice").exists(),
        "dudas": _parsea_ok(dudas.ruta_dudas(curso))
                  if dudas.ruta_dudas(curso).exists() else True,
        "progreso": _parsea_ok(progreso.ruta(curso))
                    if progreso.ruta(curso).exists() else True,
        "grafo": _parsea_ok(curso.ruta("grafo", "grafo.yaml"))
                 if curso.ruta("grafo", "grafo.yaml").exists() else True,
    }
    return checks


def cerrar(curso) -> dict:
    if curso.estado == "cerrado":
        raise ErrorCurso("curso ya cerrado")
    checks = _integridad(curso)
    curso.transicionar("cerrado")
    return {"estado": "cerrado", "registro_integro": all(checks.values()),
            "integridad": checks}


# --- Registro (SC-005) --------------------------------------------------------

def resumen_registro(curso) -> dict:
    datos = progreso.cargar(curso)
    m = datos.get("metricas", {})
    ses = sesion.cargar(curso) or {}
    return {"dudas": len(dudas.cargar(curso)),
            "evaluaciones": len(cargar_resultados_guardados(curso)),
            "notas": len(cargar_notas(curso)),
            "sesiones": m.get("sesiones", 0),
            "mensajes": m.get("mensajes", 0),
            "revelaciones": len(ses.get("revelaciones", [])),
            "distinciones_sesion": datos.get("distinciones_sesion", 0),
            "estado": curso.estado}


# --- Portabilidad (FR-019) ----------------------------------------------------

def _dir_exportados():
    d = config.DIR_CURSOS.parent / "exportados"
    d.mkdir(parents=True, exist_ok=True)
    return d


def exportar(curso) -> dict:
    """Paquete portable del curso completo; symlinks se materializan."""
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    destino = _dir_exportados() / f"{curso.slug}-{ts}.term.zip"
    raiz = curso.dir.resolve()
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(raiz.rglob("*")):
            if p.is_file() or p.is_symlink():
                z.write(p.resolve(), arcname=str(p.relative_to(raiz)))
    return {"ruta": str(destino), "bytes": destino.stat().st_size}


def importar(ruta_zip: str) -> dict:
    ruta_zip = str(ruta_zip).strip().strip('"').strip("'")
    origen = ruta_zip if ruta_zip.startswith("/") else \
        str(_dir_exportados() / ruta_zip)
    if not zipfile.is_zipfile(origen):
        raise ErrorCurso(f"no es un paquete .term.zip: {origen}")
    with zipfile.ZipFile(origen) as z:
        nombres = z.namelist()
        if "curso.yaml" not in nombres:
            raise ErrorCurso("el paquete no contiene curso.yaml")
        meta = yaml.safe_load(z.read("curso.yaml").decode("utf-8")) or {}
        slug = meta.get("slug") or "importado"
        destino = config.DIR_CURSOS / slug
        if destino.exists():
            raise ErrorCurso(f"ya existe un curso '{slug}'")
        destino.mkdir(parents=True)
        z.extractall(destino)
    return {"slug": slug}
