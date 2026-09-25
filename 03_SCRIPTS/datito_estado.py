#!/usr/bin/env python3
"""
Genera estado.md: el resumen compacto que Datito inyecta al abrir.

Problema que resuelve: la skill inyectaba progreso.yaml y errores_conceptuales.yaml
completos en cada invocacion -unos 20 KB- y ambos crecen con cada sesion. Datito
necesita saber EN QUE ESTADO esta el alumno, no los 21 registros con su historial.

Este resumen ronda las 30 lineas y no crece: solo lista lo que cambio de estado y
los errores abiertos. El detalle sigue en los YAML, que la skill lee bajo demanda.

USO
  python 03_SCRIPTS/datito_estado.py --course fcd-2026-2 --learner cristobal_herrera
  python 03_SCRIPTS/datito_estado.py  # usa contexto guardado o error

MULTI-CURSO (Fase 1: Primera Entrega)
  Usa context_manager para resolver curso y estudiante de forma centralizada.
  Contexto inválido produce error claro (no silent fallback).
"""
import argparse
import sys
from datetime import date
from pathlib import Path

import yaml

# Importar context manager
sys.path.insert(0, str(Path(__file__).parent))
from context_manager import add_context_args, get_context

ORDEN = ["DOMINADO", "COMPRENDIDO", "COMPRENSION_PARCIAL",
         "REQUIERE_REPASO", "EN_ESTUDIO", "NO_ESTUDIADO"]


def cargar(path):
    """Carga un archivo YAML."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    # Resolver contexto
    parser = argparse.ArgumentParser(description="Regenera estado.md del estudiante.")
    add_context_args(parser)
    args = parser.parse_args()

    ctx = get_context(course_id=args.course, learner_id=args.learner)
    # get_context lanza excepción si contexto es inválido

    # Cargar datos
    cur = cargar(ctx.paths.curriculum)
    pro = cargar(ctx.paths.progreso)
    err = cargar(ctx.paths.errores_conceptuales)

    nombres = {c["id"]: c["nombre"] for c in cur["conceptos"]}
    por_estado = {}
    for c in pro["conceptos"]:
        por_estado.setdefault(c["estado"], []).append(c)

    L = []
    L.append("# Estado del alumno")
    L.append("")
    L.append("> Generado por `03_SCRIPTS/datito_estado.py`. **No editar a mano.**")
    L.append("> El detalle completo esta en `progreso.yaml` y")
    L.append("> `errores_conceptuales.yaml`; leelos solo si necesitas el historial.")
    L.append("")

    m = pro["meta"]
    L.append(f"Alumno: **{m['alumno']}** · sesiones: **{m['sesiones_totales']}** "
             f"· ultima: {m['ultima_sesion'] or 'ninguna'}")
    L.append("")

    # Recuento en una linea
    cuenta = " · ".join(f"{e} {len(por_estado.get(e, []))}"
                        for e in ORDEN if por_estado.get(e))
    L.append(f"**{cuenta}** (de {len(pro['conceptos'])})")
    L.append("")

    # Solo los conceptos que NO estan en NO_ESTUDIADO: son los que importan
    activos = [(e, c) for e in ORDEN if e != "NO_ESTUDIADO"
               for c in por_estado.get(e, [])]
    if activos:
        L.append("## En curso")
        L.append("")
        L.append("| Concepto | Estado | Evidencia |")
        L.append("|---|---|---|")
        for estado, c in activos:
            ev = c.get("evidencias", {}) or {}
            marcas = (("E" if ev.get("explicar") else "·")
                      + ("A" if ev.get("aplicar") else "·")
                      + ("I" if ev.get("interpretar") else "·")
                      + ("T" if ev.get("transferir") else "·"))
            L.append(f"| {nombres.get(c['id'], c['id'])} | `{estado}` | `{marcas}` |")
        L.append("")
        L.append("Evidencia: **E**xplicar · **A**plicar · **I**nterpretar · "
                 "**T**ransferir. `DOMINADO` exige las cuatro.")
        L.append("")

    # Errores abiertos: los unicos que Datito debe anticipar
    abiertos = [o for o in (err.get("observados") or [])
                if o.get("estado") in ("abierto", "reincidente")]
    if abiertos:
        L.append("## Errores abiertos")
        L.append("")
        for o in sorted(abiertos, key=lambda x: -x.get("veces", 0)):
            veces = o.get("veces", 1)
            rep = f" · **{veces} veces**" if veces > 1 else ""
            L.append(f"- **{o['id']}** ({o['concepto']}){rep}")
            L.append(f"  - dijo: \"{(o.get('dijo') or '').strip()[:120]}\"")
        L.append("")
        L.append("Si el concepto a tratar aparece aqui, **anticipa la confusion**: "
                 "ya la tuvo y repetir la misma explicacion no va a funcionar.")
        L.append("")
    else:
        L.append("## Errores abiertos")
        L.append("")
        L.append("Ninguno.")
        L.append("")

    sig = pro["resumen"].get("siguiente_recomendado")
    if sig:
        L.append(f"**Siguiente recomendado:** `{sig}` — {nombres.get(sig, '')}")
        L.append("")

    L.append(f"<!-- generado {date.today().isoformat()} -->")

    salida = "\n".join(L) + "\n"
    with open(ctx.paths.estado, "w", encoding="utf-8", newline="\n") as f:
        f.write(salida)

    print(f"✅ estado.md generado ({len(L)} líneas, {len(salida):,} bytes)")
    print(f"   Ubicación: {ctx.paths.estado.relative_to(ctx.paths.learner_root.parent.parent)}")

    antes = sum(len(open(path, encoding="utf-8").read())
                for path in (ctx.paths.progreso, ctx.paths.errores_conceptuales))
    ratio = 100 - len(salida) * 100 // antes
    print(f"   Reemplaza {antes:,} bytes de YAML ({ratio}% menos)")


if __name__ == "__main__":
    main()
