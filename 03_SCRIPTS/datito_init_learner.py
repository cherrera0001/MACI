#!/usr/bin/env python3
"""
Inicializa un nuevo learner (alumno) en Datito.

Crea la estructura de directorios y archivos necesarios para un alumno nuevo,
clonando desde la plantilla de su curso.

USO
  python 03_SCRIPTS/datito_init_learner.py --course fcd-2026-2 --learner juan_perez
  python 03_SCRIPTS/datito_init_learner.py --course estadistica-2026-2 --learner maria_gonzalez
"""
import argparse
import os
import shutil
import sys
from datetime import date
from pathlib import Path

import yaml


def load_yaml(path):
    """Carga un archivo YAML."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path, data):
    """Guarda un archivo YAML."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def init_learner(course_id, learner_id, force=False):
    """
    Inicializa un nuevo learner.

    Args:
        course_id: identificador del curso (ej: fcd-2026-2)
        learner_id: identificador del alumno (ej: juan_perez)
        force: reemplazar si ya existe
    """

    # Resuelve rutas
    raiz = Path(__file__).parent.parent
    course_dir = raiz / "courses" / course_id
    learner_id_full = f"{learner_id}_{course_id}"  # juan_perez_fcd-2026-2
    learner_dir = raiz / "learners" / learner_id_full

    # Validaciones
    if not course_dir.exists():
        print(f"❌ Curso '{course_id}' no existe en {course_dir}")
        print(f"   Crea primero: cp -r courses/_template courses/{course_id}")
        return False

    if learner_dir.exists() and not force:
        print(f"❌ Learner '{learner_id_full}' ya existe en {learner_dir}")
        print(f"   Usa --force para reemplazar")
        return False

    # Lee config del curso
    config_path = course_dir / "datito.config.yaml"
    if not config_path.exists():
        print(f"❌ No existe datito.config.yaml en {course_dir}")
        return False

    config = load_yaml(config_path)

    # Lee curriculum del curso para generar progreso.yaml
    curriculum_path = course_dir / "curriculum.yaml"
    if not curriculum_path.exists():
        print(f"⚠️  No existe curriculum.yaml en {course_dir}")
        print(f"    Se creará estructura vacía para el learner")
        curriculum = {"conceptos": []}
    else:
        curriculum = load_yaml(curriculum_path)

    # Crea directorio del learner
    if learner_dir.exists() and force:
        shutil.rmtree(learner_dir)
        print(f"🔄 Reemplazando {learner_dir}")
    else:
        print(f"📁 Creando {learner_dir}")

    learner_dir.mkdir(parents=True, exist_ok=True)

    # ========================================================================
    # 1. datito.config.yaml (SOLO datos técnicos, NO hereda datos personales)
    # ========================================================================
    # CRÍTICO: No heredar nombre, email, proyectos del curso.
    # Cada alumno empieza con identidad VACÍA.
    learner_config = {
        "course_id": course_id,
        "learner_id": learner_id_full,

        # NUEVO ALUMNO: datos vacíos esperan ser llenados manualmente
        "alumno": {
            "nombre": "[Nombre del alumno]",  # PLACEHOLDER
            "email": "[Email del alumno]",    # PLACEHOLDER
        },

        # Referencia al curso, sin copiar
        "asignatura": config.get("asignatura", {}),

        # Configuración técnica (de solo lectura)
        "pedagogia": config.get("pedagogia", {}),
        "notebooklm": config.get("notebooklm", {}),
    }
    # Asegura que no queden valores heredados
    learner_config.pop("evaluacion", None)
    learner_config.pop("proyectos", None)

    config_learner = learner_dir / "datito.config.yaml"
    save_yaml(config_learner, learner_config)
    print(f"  ✅ datito.config.yaml")

    # ========================================================================
    # 2. progreso.yaml (vacío: todos los conceptos en NO_ESTUDIADO)
    # ========================================================================
    alumno_nombre = learner_config.get("alumno", {}).get("nombre", "[Nombre]")
    asignatura_nombre = learner_config.get("asignatura", {}).get("nombre", "[Ramo]")

    conceptos_list = []
    for c in curriculum.get("conceptos", []):
        conceptos_list.append({
            "id": c.get("id"),
            "estado": "NO_ESTUDIADO",
            "evidencias": {
                "explicar": None,
                "aplicar": None,
                "interpretar": None,
                "transferir": None,
            },
            "sesiones": 0,
            "ultima_verificacion": None,
        })

    progreso = {
        "meta": {
            "alumno": alumno_nombre,
            "tutor": "Datito",
            "asignatura": f"{asignatura_nombre} ({course_id})",
            "creado": date.today().isoformat(),
            "ultima_sesion": None,
            "sesiones_totales": 0,
            "diagnostico_inicial_hecho": False,
        },
        "resumen": {
            "DOMINADO": 0,
            "COMPRENDIDO": 0,
            "COMPRENSION_PARCIAL": 0,
            "EN_ESTUDIO": 0,
            "REQUIERE_REPASO": 0,
            "NO_ESTUDIADO": len(conceptos_list),
            "siguiente_recomendado": None,
        },
        "conceptos": conceptos_list,
    }

    progreso_path = learner_dir / "progreso.yaml"
    save_yaml(progreso_path, progreso)
    print(f"  ✅ progreso.yaml ({len(conceptos_list)} conceptos en NO_ESTUDIADO)")

    # ========================================================================
    # 3. errores_conceptuales.yaml (vacío)
    # ========================================================================
    errores = {
        "observados": [],
        "vigilados": [],
    }

    errores_path = learner_dir / "errores_conceptuales.yaml"
    save_yaml(errores_path, errores)
    print(f"  ✅ errores_conceptuales.yaml")

    # ========================================================================
    # 4. estado.md (generado vacío, será regenerado por datito_estado.py)
    # ========================================================================
    estado_md = f"""# Estado del alumno

> Generado por `03_SCRIPTS/datito_estado.py`. **No editar a mano.**

Alumno: **{alumno_nombre}** · sesiones: **0** · última: ninguna

NO_ESTUDIADO {len(conceptos_list)}

Ningún error registrado aún.

<!-- generado {date.today().isoformat()} -->
"""

    estado_path = learner_dir / "estado.md"
    with open(estado_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(estado_md)
    print(f"  ✅ estado.md")

    # ========================================================================
    # 5. dudas.yaml (vacío)
    # ========================================================================
    dudas = {"dudas": []}
    dudas_path = learner_dir / "dudas.yaml"
    save_yaml(dudas_path, dudas)
    print(f"  ✅ dudas.yaml")

    # ========================================================================
    # 6. Directorios: bitacora/, entregas/
    # ========================================================================
    (learner_dir / "bitacora").mkdir(exist_ok=True)
    (learner_dir / "entregas").mkdir(exist_ok=True)
    print(f"  ✅ bitacora/ y entregas/")

    # ========================================================================
    # Resumen
    # ========================================================================
    print()
    print(f"✨ Learner '{learner_id_full}' creado correctamente.")
    print()
    print(f"📂 Ubicación:  {learner_dir}")
    print(f"📖 Curso:      {course_id} ({asignatura_nombre})")
    print(f"👤 Alumno:     {alumno_nombre}")
    print()
    print("Próximos pasos:")
    print()
    print("  1. Regenerar navegación:")
    print("     python 03_SCRIPTS/construir_navegacion.py")
    print()
    print("  2. Regenerar estado:")
    print("     python 03_SCRIPTS/datito_estado.py")
    print()
    print("  3. Abrir Claude Code en la raíz:")
    print("     /datito")
    print()

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Inicializa un nuevo learner (alumno) en Datito."
    )
    parser.add_argument(
        "--course",
        required=True,
        help="ID del curso (ej: fcd-2026-2, estadistica-2026-2)",
    )
    parser.add_argument(
        "--learner",
        required=True,
        help="ID del learner/alumno (ej: juan_perez, maria_gonzalez)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reemplazar si el learner ya existe",
    )

    args = parser.parse_args()

    success = init_learner(args.course, args.learner, force=args.force)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
