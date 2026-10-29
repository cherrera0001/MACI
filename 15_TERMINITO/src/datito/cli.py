"""CLI datito (contracts/cli.md): init, build, chat, eval, status, identidad.

El motor corre sin servidor web (principio VII). Uso: datito <comando> [opts]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import config, evaluador, evidencia, grafo, identidad, llm, progreso
from . import ciclo
from . import sesion as sesion_mod
from . import fragmentos as frag
from . import tutor as tutor_mod
from .indice import Indice
from .modelo import ErrorCurso, cargar, listar
from .modelo import crear as crear_curso


def _print(*a):
    print(*a)


def cmd_init(args) -> int:
    curso = crear_curso(args.slug, nombre=args.nombre or args.slug,
                        periodo=args.periodo or "")
    refs = []
    for ruta in args.materiales or []:
        origen = Path(ruta).resolve()
        if not origen.exists():
            print(f"[aviso] material no encontrado: {ruta}")
            continue
        destino = curso.ruta("materiales", origen.name)
        if destino.exists() or destino.is_symlink():
            destino.unlink()
        destino.symlink_to(origen, target_is_directory=origen.is_dir())
        refs.append(origen.name)
    print(f"curso '{curso.slug}' creado en {curso.dir}")
    print(f"materiales referenciados: {len(refs)} (symlinks, sin copiar)")
    return 0


def cmd_build(args) -> int:
    curso = cargar(args.slug)
    rutas = [p for p in curso.ruta("materiales").iterdir()] \
        if curso.ruta("materiales").exists() else []
    if not rutas:
        print("[error] sin materiales: usa datito init --materiales o enlaza en materiales/")
        return 1
    print("parseando materiales…")
    fuentes, frags = frag.parsear_materiales(rutas)
    if not frags:
        print("[error] no se extrajo contenido de los materiales")
        return 1
    dir_frag = curso.ruta("fuentes", "fragmentos")
    dir_frag.mkdir(parents=True, exist_ok=True)
    for viejo in dir_frag.glob("*.md"):
        viejo.unlink()
    por_fuente: dict[str, list] = {}
    for f in frags:
        por_fuente.setdefault(f.fuente_id, []).append(f)
    advertencias = []
    for fuente in fuentes:
        lista = por_fuente.get(fuente.id, [])
        if not lista:
            advertencias.append(fuente.titulo)
        (dir_frag / f"{fuente.id}.md").write_text(
            "\n\n".join(f"<!-- {f.fid} | {f.referencia} -->\n{f.texto}" for f in lista),
            encoding="utf-8")
    indice = Indice().construir(frags)
    indice.guardar(curso.ruta(".indice"))
    print(f"fuentes: {len(fuentes)} · fragmentos: {len(frags)}")
    g = grafo.generar(curso, indice, solo_si_falta=not args.regenerar_grafo)
    if g:
        print(f"grafo generado desde los materiales: {g} (editable; --regenerar-grafo lo recrea)")
    for a in advertencias:
        print(f"  [advertencia] sin fragmentos: {a}")
    # prompt del Datito
    componentes = identidad.cargar(curso)
    ok, faltantes = identidad.completos(componentes)
    if ok:
        identidad.generar_prompt(curso, componentes)
        print("system prompt generado: prompt/actual.md")
    else:
        print(f"componentes incompletos ({', '.join(faltantes)}): "
              "ejecuta 'datito identidad build'")
    if curso.estado == "configurando":
        curso.transicionar("listo")
    print("build completo.")
    return 0


def cmd_identidad(args) -> int:
    curso = cargar(args.slug)
    if args.accion == "wizard":
        identidad.wizard(curso)
        identidad.generar_prompt(curso)
        print("prompt/actual.md generado y versionado.")
    elif args.accion == "ver":
        p = curso.ruta("prompt", "actual.md")
        print(p.read_text(encoding="utf-8") if p.exists() else "(sin prompt aun)")
    elif args.accion == "revertir":
        identidad.revertir(curso, args.version)
        print(f"revertido a {args.version}")
    return 0


def cmd_chat(args) -> int:
    curso = cargar(args.slug)
    if curso.estado == "configurando":
        print("[error] curso sin construir: ejecuta 'datito build' primero")
        return 1
    if curso.estado == "cerrado":
        print("[error] curso cerrado: el Datito ya no conversa (ciclo de vida)")
        return 1
    indice = Indice.cargar(curso.ruta(".indice"))
    progreso.iniciar_sesion(curso)
    if curso.estado == "listo":
        curso.transicionar("activo")
    modo = "tutor (LLM local)" if llm.disponible() else \
        "EXPLORACION (sin Ollama: recupera evidencia, no genera)"
    print(f"== Chat con tu Datito · {curso.datos.get('nombre')} ==  [{modo}]")
    print("comandos: :salir · :duda <texto> · :status\n")
    while True:
        try:
            pregunta = input("tu> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta pronto!")
            break
        if not pregunta:
            continue
        if pregunta == ":salir":
            m = sesion_mod.metricas(curso)
            print(f"[metricas de sesion] preguntas con espera real: "
                  f"{m['esperas_reales']}/{m['preguntas']} · soluciones "
                  f"reveladas: {m['soluciones']} · transferencias: "
                  f"{m['transferencias_cumplidas']}/{m['transferencias_exigidas']} "
                  f"· dudas registradas: {m['dudas_registradas']}")
            break
        if pregunta.startswith(":status"):
            print(grafo.panel(curso))
            print(progreso.resumen(curso))
            continue
        if pregunta.startswith(":duda "):
            duda = tutor_mod.responder(curso, pregunta[6:], indice)
            if duda.modo != "sin_fuente":
                from . import dudas as dudas_mod
                limpio = duda.texto.split("\n\nInstala Ollama")[0].strip()
                dudas_mod.registrar(curso, pregunta[6:], limpio[:400],
                                    "Duda registrada desde chat", duda.citas)
                print(f"[duda registrada en dudas.yaml] citas: {duda.citas}")
            print(duda.texto)
            if duda.citas:
                print(evidencia.bloque_evidencia(duda.citas, indice))
            continue
        resp = sesion_mod.intercambio(curso, pregunta, indice)
        progreso.contar_mensaje(curso, 2)
        print(f"datito> {resp['texto']}")
        if resp["citas"]:
            print(evidencia.bloque_evidencia(resp["citas"], indice))
        if resp.get("aviso"):
            print(f"[aviso] {resp['aviso']}")
        if resp.get("estado_interaccion"):
            print(f"[estado: {resp['estado_interaccion']}]")
    return 0


def cmd_eval(args) -> int:
    curso = cargar(args.slug)
    indice = Indice.cargar(curso.ruta(".indice")) if curso.ruta(".indice").exists() else None
    items = evaluador.cargar_items(curso)
    if not items:
        print("[error] no hay items en evaluaciones/ (se requieren >=2 conceptos por item)")
        return 1
    progreso.iniciar_sesion(curso)
    print(f"== Evaluacion por distinciones · {curso.datos.get('nombre')} ==")
    print(f"{len(items)} distinciones. Escribe tu respuesta; Enter vacio = saltar.\n")
    for item in items:
        print(f"— {item.pregunta}")
        print(f"  (conceptos en juego: {' vs '.join(item.conceptos)})")
        resp = input("> ").strip()
        if not resp:
            print("  (saltada)\n")
            continue
        contexto = ""
        if indice:
            top = indice.buscar(" ".join(item.conceptos), k=2)
            contexto = " ".join(indice.textos[f] for f, _ in top)
        res = evaluador.calificar(item, resp, contexto)
        evaluador.guardar_resultado(curso, res)
        grafo.actualizar_dominio(curso, item.conceptos, res.resultado)
        n, ok = progreso.contar_distincion(curso, res.resultado == "logrado")
        print(f"  {res.resultado.upper()} — {res.retroalimentacion}")
        if res.heuristico:
            print("  [aviso] calificacion heuristica de BAJA CONFIANZA; con Ollama "
                  "la rubrica evalua el razonamiento de verdad")
        print(f"  [{ok}/{n} distinciones de esta sesion]\n")
    datos = progreso.cargar(curso)
    datos["metricas"]["evaluaciones_completadas"] += 1
    progreso.guardar(curso, datos)
    print(grafo.panel(curso))
    print(progreso.resumen(curso))
    return 0


def cmd_status(args) -> int:
    curso = cargar(args.slug)
    print(f"curso: {curso.slug} · estado: {curso.estado}")
    print(progreso.resumen(curso))
    print(grafo.panel(curso, mapa_completo=args.mapa, color=sys.stdout.isatty()))
    dudas_p = curso.ruta("dudas.yaml")
    if dudas_p.exists():
        import yaml
        n = len((yaml.safe_load(dudas_p.read_text(encoding="utf-8")) or {}).get("dudas", []))
        print(f"\ndudas resueltas: {n} (dudas.yaml)")
    return 0


def cmd_lista(args) -> int:
    cursos = listar()
    if not cursos:
        print("sin cursos todavia: datito init <slug> --materiales <ruta>")
        return 0
    for c in cursos:
        print(f"  {c.slug:24} {c.estado:14} {c.datos.get('nombre', '')}")
    return 0


def cmd_nota(args) -> int:
    curso = cargar(args.slug)
    entrada = ciclo.registrar_nota(curso, args.evaluacion, args.nota,
                                   args.observaciones or "")
    print(f"nota registrada ({entrada['fecha']}): {entrada['evaluacion']} "
          f"→ {entrada['nota']}")
    for a in entrada["ajustes_derivados"]:
        print(f"  ajuste derivado: {a}")
    return 0


def cmd_cerrar(args) -> int:
    curso = cargar(args.slug)
    res = ciclo.cerrar(curso)
    print(f"curso {curso.slug}: {res['estado']} · registro integro: "
          f"{res['registro_integro']}")
    return 0


def cmd_exportar(args) -> int:
    curso = cargar(args.slug)
    res = ciclo.exportar(curso)
    print(f"paquete portable: {res['ruta']} ({res['bytes']} bytes)")
    return 0


def cmd_demo(args) -> int:
    import json as _json
    from . import demo_sintetico
    r = demo_sintetico.ejecutar()
    if args.json:
        print(_json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"estado final del concepto: {r['estado_final']}")
        print(f"violaciones del protocolo: {r['violaciones_protocolo'] or 'ninguna'}")
        print(f"metricas: {r['metricas']}")
        print(f"curso sandbox: {r['ruta_curso']} (SINTETICO, sin tocar 07_DATITO)")
    return 1 if r["violaciones_protocolo"] else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="datito",
                                     description="Tutores agenticos disenados por el estudiante.")
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("init", help="crea estructura de curso")
    p.add_argument("slug")
    p.add_argument("--nombre", default="")
    p.add_argument("--periodo", default="")
    p.add_argument("--materiales", nargs="*", default=[])
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("build", help="parsea materiales, construye indice y prompt")
    p.add_argument("slug")
    p.add_argument("--regenerar-grafo", action="store_true",
                   help="recrea grafo/grafo.yaml desde los encabezados de los materiales")
    p.set_defaults(fn=cmd_build)

    p = sub.add_parser("identidad", help="constructor de identidad del Datito")
    p.add_argument("slug")
    p.add_argument("accion", choices=["wizard", "ver", "revertir"])
    p.add_argument("--version", default="")
    p.set_defaults(fn=cmd_identidad)

    p = sub.add_parser("chat", help="dialogo con el Datito")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_chat)

    p = sub.add_parser("eval", help="evaluacion por distinciones")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_eval)

    p = sub.add_parser("status", help="progreso, dudas y dominio del grafo")
    p.add_argument("slug")
    p.add_argument("--mapa", action="store_true", help="revelar mapa completo (escape)")
    p.set_defaults(fn=cmd_status)

    p = sub.add_parser("lista", help="listar cursos")
    p.set_defaults(fn=cmd_lista)

    p = sub.add_parser("nota", help="registrar nota real como retroalimentacion")
    p.add_argument("slug")
    p.add_argument("evaluacion")
    p.add_argument("nota")
    p.add_argument("--observaciones", default="")
    p.set_defaults(fn=cmd_nota)

    p = sub.add_parser("cerrar", help="cerrar el ciclo del Datito (FR-016)")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_cerrar)

    p = sub.add_parser("exportar", help="paquete portable del curso (FR-019)")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_exportar)

    p = sub.add_parser("demo", help="demo sintetico de la politica socratica (G10)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_demo)

    args = parser.parse_args(argv)
    try:
        return args.fn(args)
    except ErrorCurso as e:
        print(f"[error] {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
