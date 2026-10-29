#!/usr/bin/env python3
"""Arma dist/datito.zip: engine + curso fcd resuelto + wheels + start.

Uso: python 15_TERMINITO/scripts/build_paquete.py
Requiere red solo para descargar wheels la primera vez.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]   # …/MACI
MOTOR = RAIZ / "15_TERMINITO"
DIST_SRC = RAIZ / "dist-src"
SALIDA = RAIZ / "dist"
PAQUETE = SALIDA / "paquete"
ZIP = SALIDA / "datito.zip"
CURSO_REAL = MOTOR / "cursos" / "fcd"

LIMITE_MB = 50


def _patrones_excluir_material(nombre: str) -> list[str]:
    p = ["__pycache__"]
    if nombre == "transcripciones":
        p.append("*_plano.txt")      # duplican a los .md
    if nombre == "visual":
        p.append("_TEMPLATE_CANONICO.html")
        p.append("datito")   # el ZIP distribuible no va dentro de sí mismo
    return p


def descargar_wheels():
    # Cache persistente entre builds (dist/wheels): se descarga solo si falta.
    cache = SALIDA / "wheels"
    if not (cache.exists() and any(cache.iterdir())):
        cache.mkdir(parents=True, exist_ok=True)
        cmd = [sys.executable, "-m", "pip", "download", "--only-binary=:all:",
               "-d", str(cache), "pyyaml", "jinja2", "markdown", "pypdf",
               "python-docx", "python-pptx"]
        r = subprocess.run(cmd)
        if r.returncode != 0:
            # los venvs de uv no traen pip: usar el pip del sistema
            subprocess.run(["pip3", "download", "--only-binary=:all:",
                            "-d", str(cache), "pyyaml", "jinja2", "markdown",
                            "pypdf"], check=True)
    shutil.copytree(cache, PAQUETE / "wheels")


def copiar_motor():
    dest = PAQUETE / "15_TERMINITO"
    shutil.copytree(MOTOR / "src", dest / "src",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for f in ("pyproject.toml", "README.md"):
        shutil.copy2(MOTOR / f, dest / f)
    shutil.copytree(MOTOR / "docs", dest / "docs")
    shutil.copy2(RAIZ / "LICENSE", dest / "LICENSE")
    shutil.copytree(MOTOR / "plantillas", dest / "plantillas")


def copiar_curso():
    """Curso limpio para un estudiante nuevo: materiales resueltos (sin symlinks)."""
    dest = PAQUETE / "15_TERMINITO" / "cursos" / "fcd"
    for sub in ("prompt/versions", "materiales", "grafo", "evaluaciones", "fuentes/fragmentos"):
        (dest / sub).mkdir(parents=True, exist_ok=True)
    # metadatos limpios
    import yaml
    datos = yaml.safe_load((CURSO_REAL / "curso.yaml").read_text(encoding="utf-8"))
    datos["estado"] = "listo"
    datos.pop("cerrado_en", None)
    (dest / "curso.yaml").write_text(
        yaml.safe_dump(datos, allow_unicode=True, sort_keys=False), encoding="utf-8")
    for f in ("prompt/componentes.yaml", "evaluaciones/distinciones.yaml"):
        shutil.copy2(CURSO_REAL / f, dest / f)
    # actual.md solo si el curso ya fue construido localmente; en un clone
    # fresco no existe y start.py lo regenera con `datito build` al primer uso.
    actual = CURSO_REAL / "prompt" / "actual.md"
    if actual.exists():
        shutil.copy2(actual, dest / "prompt" / "actual.md")
    shutil.copy2((CURSO_REAL / "grafo" / "grafo.yaml").resolve(),
                 dest / "grafo" / "grafo.yaml")
    # materiales: copiar contenido real de los symlinks
    for enlace in (CURSO_REAL / "materiales").iterdir():
        if not enlace.is_symlink():
            continue
        real = enlace.resolve()
        nombre = enlace.name
        if real.is_dir():
            sub = dest / "materiales" / nombre
            shutil.copytree(real, sub,
                            ignore=shutil.ignore_patterns(
                                *_patrones_excluir_material(nombre)))
        elif real.is_file():
            shutil.copy2(real, dest / "materiales" / nombre)


def copiar_lanzadores():
    for f in ("start.py", "start.sh", "start.bat", "LEEME.txt"):
        shutil.copy2(DIST_SRC / f, PAQUETE / f)
    shutil.copy2(RAIZ / "LICENSE", PAQUETE / "LICENSE")
    (PAQUETE / "start.sh").chmod(0o755)


def empaquetar():
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(PAQUETE.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(PAQUETE))
    mb = ZIP.stat().st_size / 1024 / 1024
    print(f"{ZIP}  ({mb:.1f} MB)")
    if mb > LIMITE_MB:
        raise SystemExit(f"EXCEDE {LIMITE_MB} MB")


def main():
    SALIDA.mkdir(exist_ok=True)
    if PAQUETE.exists():
        shutil.rmtree(PAQUETE)
    PAQUETE.mkdir(parents=True)
    copiar_lanzadores()
    descargar_wheels()
    copiar_motor()
    copiar_curso()
    empaquetar()


if __name__ == "__main__":
    main()
