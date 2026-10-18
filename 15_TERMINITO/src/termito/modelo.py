"""Modelo de Curso: curso.yaml con metadatos, identidad del Termito y estado."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import yaml

from . import config

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,}$")

CAMPOS_CURSO = ("slug", "nombre", "periodo", "idioma", "estado", "creado")


class ErrorCurso(Exception):
    pass


def slug_valido(slug: str) -> bool:
    return bool(SLUG_RE.match(slug))


def norm_slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t


class Curso:
    """Un curso/Termito = un directorio autocontenido (data-model.md)."""

    def __init__(self, dir_curso: Path):
        self.dir = Path(dir_curso)
        self.yaml_path = self.dir / "curso.yaml"
        if not self.yaml_path.exists():
            raise ErrorCurso(f"curso.yaml no existe en {self.dir}")
        self.datos = yaml.safe_load(self.yaml_path.read_text(encoding="utf-8")) or {}

    @classmethod
    def crear(cls, slug: str, nombre: str = "", periodo: str = "", idioma: str = "es") -> "Curso":
        if not slug_valido(slug):
            raise ErrorCurso(f"slug invalido '{slug}' (kebab-case, min 3 chars)")
        dir_curso = config.DIR_CURSOS / slug
        if dir_curso.exists():
            raise ErrorCurso(f"ya existe el curso '{slug}'")
        for sub in ("prompt/versions", "fuentes/fragmentos", "materiales", "grafo",
                    "evaluaciones", "sesiones"):
            (dir_curso / sub).mkdir(parents=True, exist_ok=True)
        datos = {
            "slug": slug,
            "nombre": nombre or slug,
            "periodo": periodo,
            "idioma": idioma,
            "estado": "configurando",
            "creado": __import__("datetime").date.today().isoformat(),
            "tiempo_estimado_min": None,
        }
        (dir_curso / "curso.yaml").write_text(
            yaml.safe_dump(datos, allow_unicode=True, sort_keys=False), encoding="utf-8")
        return cls(dir_curso)

    @property
    def slug(self) -> str:
        return self.datos["slug"]

    @property
    def estado(self) -> str:
        return self.datos.get("estado", "configurando")

    def guardar(self):
        self.yaml_path.write_text(
            yaml.safe_dump(self.datos, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def transicionar(self, nuevo: str):
        if nuevo not in config.ESTADOS_CURSO:
            raise ErrorCurso(f"estado desconocido '{nuevo}'")
        orden = config.ESTADOS_CURSO
        if nuevo != "cerrado" and orden.index(nuevo) < orden.index(self.estado):
            raise ErrorCurso(f"transicion invalida {self.estado} -> {nuevo}")
        self.datos["estado"] = nuevo
        if nuevo == "cerrado":
            import datetime
            self.datos["cerrado_en"] = datetime.date.today().isoformat()
        self.guardar()

    def ruta(self, *partes) -> Path:
        return self.dir.joinpath(*partes)


def cargar(slug: str) -> Curso:
    if not slug_valido(slug):
        raise ErrorCurso(f"slug invalido '{slug}'")
    return Curso(config.DIR_CURSOS / slug)


crear = Curso.crear  # alias de modulo para el CLI y tests


def listar() -> list[Curso]:
    if not config.DIR_CURSOS.exists():
        return []
    return [Curso(d) for d in sorted(config.DIR_CURSOS.iterdir()) if (d / "curso.yaml").exists()]
