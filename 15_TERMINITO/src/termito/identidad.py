"""Constructor de identidad: 8 componentes del Termito (spec, descripcion usuario).

Wizard conversacional: una decision por pantalla, con defaults del curso
(patrones Duolingo/Mathigon de la validacion REA). El system prompt se genera
con jinja2, se muestra completo y queda versionado (FR-004, FR-005, research R7).
"""
from __future__ import annotations

import datetime
import shutil
from pathlib import Path

import yaml
from jinja2 import Template

COMPONENTES = {
    "rol_dominio": "Rol y dominio: quien es el tutor y en que materia",
    "mision": "Mision: para que existe este Termito en este curso",
    "funciones": "Funciones: que hace (explicar, proponer ejercicios, corregir...)",
    "estilo_ensenanza": "Estilo de ensenanza (socratico, directo, con ejemplos...)",
    "contexto_curso": "Contexto del curso (resumen aprobado por el estudiante)",
    "estilo_aprendizaje": "Tu estilo de aprendizaje (intuitivo/formal, paso a paso/desafio)",
    "restricciones": "Restricciones (no inventar informacion, fomentar razonamiento critico)",
    "relacion_temporal": "Relacion temporal (acompanar todo el ciclo, recibir notas)",
}

PLANTILLA = Template("""# System Prompt — Termito «{{ curso }}»
# Generado desde 8 componentes. Editable; cada cambio queda versionado.

## 1. Rol y dominio
{{ rol_dominio }}

## 2. Mision
{{ mision }}

## 3. Funciones
{{ funciones }}

## 4. Estilo de ensenanza
{{ estilo_ensenanza }}

## 5. Contexto del curso
{{ contexto_curso }}

## 6. Estilo de aprendizaje del estudiante
{{ estilo_aprendizaje }}

## 7. Restricciones
{{ restricciones }}
- NUNCA inventes informacion sobre el curso: solo afirmas lo que tenga fuente
  citada entre los materiales. Si no hay fuente, dilo explicitamente.
- NUNCA entregues la solucion completa de un ejercicio antes del intento del
  estudiante; ofrece pistas o un paso del procedimiento (lucha productiva).
- Responde SIEMPRE en el idioma en que escribe el estudiante (FR-022).

## 8. Relacion temporal
{{ relacion_temporal }}
""")


def ruta_componentes(curso) -> Path:
    return curso.ruta("prompt", "componentes.yaml")


def cargar(curso) -> dict:
    p = ruta_componentes(curso)
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {}


def guardar(curso, componentes: dict):
    curso.ruta("prompt").mkdir(parents=True, exist_ok=True)
    ruta_componentes(curso).write_text(
        yaml.safe_dump(componentes, allow_unicode=True, sort_keys=False), encoding="utf-8")


def completos(componentes: dict) -> tuple[bool, list[str]]:
    faltantes = [c for c in COMPONENTES if not str(componentes.get(c, "")).strip()]
    return (not faltantes), faltantes


def wizard(curso, defaults: dict | None = None, input_fn=input, print_fn=print) -> dict:
    """Asistente conversacional: una pregunta por pantalla, Enter = default."""
    print_fn(f"\n== Construyamos tu Termito para «{curso.datos.get('nombre')}» ==")
    print_fn("(Enter acepta la sugerencia; escribe para cambiarla)\n")
    datos = dict(defaults or cargar(curso))
    for clave, pregunta in COMPONENTES.items():
        sugerencia = datos.get(clave) or (defaults or {}).get(clave, "")
        print_fn(f"— {pregunta}")
        if sugerencia:
            print_fn(f"  sugerencia: {sugerencia}")
        resp = input_fn("> ").strip()
        datos[clave] = resp or sugerencia or ""
    guardar(curso, datos)
    return datos


def generar_prompt(curso, componentes: dict | None = None) -> Path:
    componentes = componentes or cargar(curso)
    ok, faltantes = completos(componentes)
    if not ok:
        raise ValueError(f"componentes incompletos: {', '.join(faltantes)}")
    texto = PLANTILLA.render(curso=curso.datos.get("nombre"), **componentes)
    ruta = curso.ruta("prompt", "actual.md")
    previa = ruta.read_text(encoding="utf-8") if ruta.exists() else None
    if previa != texto:
        if previa is not None:
            versionar(curso, motivo="regenerado desde componentes")
        ruta.write_text(texto, encoding="utf-8")
    return ruta


def versionar(curso, motivo: str = "edicion manual") -> str:
    """Guarda la version vigente y anota el cambio en manifest (research R7)."""
    actual = curso.ruta("prompt", "actual.md")
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    dir_versions = curso.ruta("prompt", "versions")
    dir_versions.mkdir(parents=True, exist_ok=True)  # pudo no sobrevivir al zip
    if actual.exists():
        shutil.copy2(actual, dir_versions / f"{ts}.md")
    man_path = curso.ruta("prompt", "versions", "manifest.yaml")
    man = yaml.safe_load(man_path.read_text(encoding="utf-8")) if man_path.exists() else []
    man = man or []
    man.append({"version": ts, "motivo": motivo})
    man_path.write_text(yaml.safe_dump(man, allow_unicode=True), encoding="utf-8")
    return ts


def revertir(curso, version: str) -> Path:
    src = curso.ruta("prompt", "versions", f"{version}.md")
    if not src.exists():
        raise ValueError(f"version '{version}' no existe")
    versionar(curso, motivo=f"revertir a {version}")
    shutil.copy2(src, curso.ruta("prompt", "actual.md"))
    return curso.ruta("prompt", "actual.md")
