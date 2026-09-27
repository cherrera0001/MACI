#!/usr/bin/env python3
"""
Context Manager para Datito: Resolución centralizada de curso y estudiante.

PROBLEMA QUE RESUELVE:
  - Scripts usan defaults silenciosos cuando contexto falta
  - No hay un solo lugar que resuelva "¿qué curso? ¿qué estudiante?"
  - Cambiar de contexto a veces carga datos de contexto anterior

SOLUCIÓN:
  Un módulo que:
  1. Lee contexto explícito desde CLI, ENV o archivo
  2. Valida que exista
  3. Resuelve rutas correctamente
  4. Detecta y rechaza contexto inválido
  5. Proporciona funciones helper a otros scripts

USO:
  from context_manager import Context, get_context

  # Automático: desde línea de comandos o archivo
  ctx = get_context()
  print(ctx.course_id, ctx.learner_id)
  print(ctx.paths.progreso)

  # Manual: construir desde componentes
  ctx = Context(course_id="fcd-2026-2", learner_id="juan_perez")
  if not ctx.is_valid():
      print(f"❌ {ctx.error}")

GARANTÍAS:
  - Si contexto es inválido, lanza error explícito (no default silencioso)
  - Si archivo config no existe, error claro + instrucciones
  - Una sola verdad: ctx.paths.*
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml


@dataclass
class ContextPaths:
    """Rutas resueltas para un contexto curso+estudiante."""

    course_root: Path
    learner_root: Path

    # Archivos del curso (compartidos, estáticos)
    course_config: Path  # no se usa para leer, solo referencia
    curriculum: Path
    clases: Path
    grafo: Path
    visual: Path
    referencia: Path

    # Archivos del estudiante (privados, dinámicos)
    learner_config: Path
    progreso: Path
    errores_conceptuales: Path
    estado: Path
    dudas: Path
    bitacora: Path
    entregas: Path

    # Datos compartidos del curso (solo lectura en visual generado)
    mapa_ensenanza: Path


class Context:
    """Contexto de ejecución: qué curso, qué estudiante, dónde están los datos."""

    def __init__(
        self,
        course_id: Optional[str] = None,
        learner_id: Optional[str] = None,
        raiz: Optional[Path] = None,
    ):
        """
        Inicializa contexto.

        Args:
            course_id: Identificador del curso (ej: fcd-2026-2)
            learner_id: Identificador del estudiante (ej: juan_perez)
            raiz: Raíz del repositorio (por defecto: deduce desde este script)
        """
        self.raiz = raiz or Path(__file__).parent.parent
        self.course_id = course_id
        self.learner_id = learner_id
        self.error: Optional[str] = None
        self.paths: Optional[ContextPaths] = None

        # Validar y resolver rutas
        self._validate_and_resolve()

    def _validate_and_resolve(self):
        """Valida que contexto sea válido y resuelve rutas."""

        # Validación 1: course_id
        if not self.course_id:
            self.error = "course_id no especificado. Usa --course para indicar el curso."
            return

        if not self.course_id.replace("-", "").replace("_", "").isalnum():
            self.error = f"course_id '{self.course_id}' contiene caracteres inválidos. Usa minúsculas, números, - o _."
            return

        course_root = self.raiz / "courses" / self.course_id
        if not course_root.exists():
            available = sorted([d.name for d in (self.raiz / "courses").iterdir() if d.is_dir()])
            self.error = f"Curso '{self.course_id}' no existe.\nCursos disponibles: {', '.join(available)}"
            return

        # Validación 2: learner_id
        if not self.learner_id:
            self.error = "learner_id no especificado. Usa --learner para indicar el estudiante."
            return

        if not self.learner_id.replace("-", "").replace("_", "").isalnum():
            self.error = f"learner_id '{self.learner_id}' contiene caracteres inválidos. Usa minúsculas, números, - o _."
            return

        # Construir learner_id completo con curso
        learner_id_full = f"{self.learner_id}_{self.course_id}"
        learner_root = self.raiz / "learners" / learner_id_full

        # Validación 3: learner debe existir
        if not learner_root.exists():
            self.error = f"Estudiante '{learner_id_full}' no existe en el curso '{self.course_id}'.\nCrea uno con: python 03_SCRIPTS/datito_init_learner.py --course {self.course_id} --learner {self.learner_id}"
            return

        # Validación 4: archivos críticos del curso
        curriculum = course_root / "curriculum.yaml"
        clases = course_root / "clases.yaml"

        if not curriculum.exists():
            self.error = f"Curso '{self.course_id}' incompleto: falta curriculum.yaml"
            return

        if not clases.exists():
            self.error = f"Curso '{self.course_id}' incompleto: falta clases.yaml"
            return

        # Validación 5: archivos críticos del estudiante
        progreso = learner_root / "progreso.yaml"
        estado = learner_root / "estado.md"

        if not progreso.exists():
            self.error = f"Estudiante '{learner_id_full}' incompleto: falta progreso.yaml"
            return

        if not estado.exists():
            self.error = f"Estudiante '{learner_id_full}' incompleto: falta estado.md"
            return

        # Éxito: resolver todas las rutas
        self.paths = ContextPaths(
            course_root=course_root,
            learner_root=learner_root,
            course_config=course_root / "datito.config.yaml",
            curriculum=curriculum,
            clases=clases,
            grafo=course_root / "grafo.yaml",
            visual=course_root / "visual",
            referencia=course_root / "referencia",
            learner_config=learner_root / "datito.config.yaml",
            progreso=progreso,
            errores_conceptuales=learner_root / "errores_conceptuales.yaml",
            estado=estado,
            dudas=learner_root / "dudas.yaml",
            bitacora=learner_root / "bitacora",
            entregas=learner_root / "entregas",
            mapa_ensenanza=self.raiz / "05_CLASES" / "mapa_ensenanza.yaml",
        )

    def is_valid(self) -> bool:
        """Retorna True si contexto es válido."""
        return self.error is None

    def assert_valid(self) -> None:
        """Lanza excepción si contexto es inválido."""
        if not self.is_valid():
            raise ValueError(f"❌ Contexto inválido:\n{self.error}")

    def to_dict(self) -> dict:
        """Serializa contexto a diccionario."""
        return {
            "course_id": self.course_id,
            "learner_id": self.learner_id,
            "raiz": str(self.raiz),
            "valid": self.is_valid(),
            "error": self.error,
        }


def get_context_from_args(args: argparse.Namespace) -> Context:
    """Extrae course_id y learner_id de argparse.Namespace."""
    return Context(
        course_id=getattr(args, "course", None),
        learner_id=getattr(args, "learner", None),
    )


def add_context_args(parser: argparse.ArgumentParser) -> None:
    """Agrega argumentos --course y --learner a un parser."""
    parser.add_argument(
        "--course",
        help="Identificador del curso (ej: fcd-2026-2)",
        required=False,
    )
    parser.add_argument(
        "--learner",
        help="Identificador del estudiante (ej: juan_perez)",
        required=False,
    )


def get_context(
    course_id: Optional[str] = None,
    learner_id: Optional[str] = None,
) -> Context:
    """
    Obtiene contexto desde múltiples fuentes en este orden:
    1. Parámetros explícitos
    2. Variables de entorno
    3. Archivo .context.json en raíz
    4. Error si nada se encuentra

    Returns:
        Context: contexto resuelto y validado

    Raises:
        ValueError: si contexto es inválido
    """

    # Fallback: orden de prioridad
    course_id = course_id or os.environ.get("DATITO_COURSE")
    learner_id = learner_id or os.environ.get("DATITO_LEARNER")

    # Fallback: archivo .context.json en raíz
    raiz = Path(__file__).parent.parent
    context_file = raiz / ".context.json"
    if context_file.exists() and (not course_id or not learner_id):
        try:
            with open(context_file, encoding="utf-8") as f:
                saved = json.load(f)
                course_id = course_id or saved.get("course_id")
                learner_id = learner_id or saved.get("learner_id")
        except (json.JSONDecodeError, KeyError):
            pass  # No válido, ignorar

    ctx = Context(course_id=course_id, learner_id=learner_id, raiz=raiz)

    if not ctx.is_valid():
        # Mostrar error con instrucciones
        print(f"\n{ctx.error}\n", file=sys.stderr)
        sys.exit(1)

    return ctx


def main():
    """CLI simple para verificar contexto."""
    parser = argparse.ArgumentParser(
        description="Verifica y muestra contexto (curso + estudiante)."
    )
    add_context_args(parser)

    args = parser.parse_args()
    ctx = get_context_from_args(args)

    if not ctx.is_valid():
        print(f"❌ {ctx.error}", file=sys.stderr)
        sys.exit(1)

    print(f"✅ Contexto válido")
    print(f"   Curso: {ctx.course_id}")
    print(f"   Estudiante: {ctx.learner_id}")
    print(f"   Curso root: {ctx.paths.course_root}")
    print(f"   Learner root: {ctx.paths.learner_root}")
    print()
    print(f"Archivos:")
    print(f"   Curriculum: {ctx.paths.curriculum.relative_to(ctx.raiz)}")
    print(f"   Progreso: {ctx.paths.progreso.relative_to(ctx.raiz)}")
    print(f"   Estado: {ctx.paths.estado.relative_to(ctx.raiz)}")


if __name__ == "__main__":
    main()
