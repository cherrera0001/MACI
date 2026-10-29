#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Una iteración del Agents Learning Loop (dry-run o eval de un target)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOOP = ROOT / "07_DATITO" / "07_BITACORA" / "learning_loop"
RESULTS = LOOP / "results.tsv"
EVAL = ROOT / "04_CODIGO" / "datito_loop_eval.py"


def append_result(row: dict) -> None:
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    if not RESULTS.exists():
        RESULTS.write_text(
            "ts\tfamily\thypothesis\ttarget_file\tmetric\tscore\tdecision\tlesson_id\n",
            encoding="utf-8",
        )
    line = (
        f"{row['ts']}\t{row['family']}\t{row['hypothesis']}\t{row['target_file']}\t"
        f"{row['metric']}\t{row['score']}\t{row['decision']}\t{row['lesson_id']}\n"
    )
    with RESULTS.open("a", encoding="utf-8") as f:
        f.write(line)


def lesson_id_o_error(lesson_id: str) -> str:
    """T-4.2.1: sin ids por defecto. Registrar exige --lesson-id explícito."""
    if not lesson_id:
        raise SystemExit("error: --lesson-id es obligatorio al registrar (no hay ids por defecto)")
    return lesson_id


def adjuntar_traza(lesson_id: str, traza: dict,
                   lecciones=None, dir_trazas=None) -> Path:
    """Adjunta la evidencia ligera de la corrida a la lección (T-8.4.1).

    Guarda la traza (salida del eval, gate, decisión) en
    learning_loop/trazas/<lesson_id>.json y referencia el archivo en la
    entrada de la lección con una edición de texto mínima que PRESERVA los
    comentarios de agent_lessons.yaml (pyyaml los destruiría).
    """
    import json

    lecciones = Path(lecciones) if lecciones else LOOP / "agent_lessons.yaml"
    dir_trazas = Path(dir_trazas) if dir_trazas else LOOP / "trazas"
    dir_trazas.mkdir(parents=True, exist_ok=True)
    destino = dir_trazas / f"{lesson_id}.json"
    destino.write_text(json.dumps(traza, ensure_ascii=False, indent=2),
                       encoding="utf-8")
    lineas = lecciones.read_text(encoding="utf-8").splitlines()
    id_linea = next((i for i, l in enumerate(lineas)
                     if l.strip() == f"- id: {lesson_id}"), None)
    if id_linea is None:
        return destino  # lección aún no archivada: la traza queda en trazas/
    siguiente = lineas[id_linea + 1] if id_linea + 1 < len(lineas) else ""
    if "traza:" not in siguiente:
        lineas.insert(id_linea + 1, f'    traza: "trazas/{destino.name}"')
        lecciones.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return destino


def contrato_de(path: Path) -> dict | None:
    """Contrato de contrato_conocimiento.yaml que cubre este target, parseado.

    Devuelve None si no hay contrato para el archivo. 'selector' es el primer
    #id del campo comprobar; 'esperados' son las etiquetas listadas entre ( ).
    """
    contratos = LOOP / "contrato_conocimiento.yaml"
    if not contratos.exists():
        return None
    import re

    import yaml

    datos = yaml.safe_load(contratos.read_text(encoding="utf-8"))
    lista = datos if isinstance(datos, list) else [datos]
    rel = Path(path)
    if rel.is_absolute():
        rel = rel.relative_to(ROOT)
    contrato = next((c for c in lista if c and Path(str(c.get("clase", ""))) == rel), None)
    if contrato is None:
        return None
    comprobar = str(contrato.get("comprobar", ""))
    selector = re.search(r"(#[\w-]+)", comprobar)
    par = re.search(r"\((.*?)\)", comprobar)
    return {
        "control": str(contrato.get("control", "")).strip(),
        "selector": selector.group(1) if selector else "",
        "esperados": [t.strip() for t in par.group(1).split(",")] if par else [],
    }


def gate_contrato(path: Path) -> dict | None:
    """T-4.3.1: si hay contrato, el control tiene que cambiar el texto que
    promete (comprobar). Reusa Playwright; si el navegador no está disponible,
    omite el gate con aviso. None = gate no aplica."""
    contrato = contrato_de(path)
    if contrato is None:
        return None
    if not (contrato["control"] and contrato["selector"]):
        return {"ok": False, "failures": ["contrato sin control o selector comprobable"]}
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("aviso: gate de contrato omitido (playwright no instalado)", file=sys.stderr)
        return None
    control = contrato["control"] if contrato["control"].startswith("#") else "#" + contrato["control"]
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_context(offline=True).new_page()
            page.goto(path.resolve().as_uri(), wait_until="load")
            data = page.evaluate(
                """([ctlSel, tgtSel]) => {
                  const ctl = document.querySelector(ctlSel);
                  const tgt = document.querySelector(tgtSel);
                  if (!ctl || !tgt) return {ok: false, error: 'no encuentro ' + (!ctl ? ctlSel : tgtSel)};
                  const min = ctl.min || '0', max = ctl.max || '100';
                  const vals = [min, String((parseFloat(min) + parseFloat(max)) / 2), max];
                  const visto = new Set();
                  vals.forEach(v => {
                    ctl.value = v;
                    ctl.dispatchEvent(new Event('input', {bubbles: true}));
                    ctl.dispatchEvent(new Event('change', {bubbles: true}));
                    visto.add((tgt.textContent || '').trim());
                  });
                  return {ok: true, visto: [...visto]};
                }""",
                [control, contrato["selector"]],
            )
            browser.close()
    except Exception as e:  # navegador sin libs del sistema, etc.
        print(f"aviso: gate de contrato omitido ({e})", file=sys.stderr)
        return None
    if not data.get("ok"):
        return {"ok": False, "failures": [f"contrato: {data.get('error', 'fallo')}"]}
    visto = data["visto"]
    cambia = len([v for v in visto if v]) > 1
    esperados = contrato["esperados"]
    alcanza = any(e in v for v in visto for e in esperados) if esperados else cambia
    failures = []
    if not cambia:
        failures.append(f"el control {control} no cambia el texto de {contrato['selector']}")
    elif esperados and not alcanza:
        failures.append(f"el texto jamás alcanza las etiquetas del contrato {esperados}: {visto}")
    return {"ok": not failures, "failures": failures, "visto": visto}


def main() -> int:
    ap = argparse.ArgumentParser(description="Datito learning loop — una eval")
    ap.add_argument("--path", required=True)
    ap.add_argument("--hypothesis", default="eval gate template+anti-cdn")
    ap.add_argument("--family", default="visual")
    ap.add_argument("--lesson-id", default="")
    args = ap.parse_args()

    proc = subprocess.run(
        [sys.executable, str(EVAL), "--path", args.path, "--json"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)

    import json

    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print("No JSON de eval", file=sys.stderr)
        return 2

    decision = "keep" if data.get("keep_eligible") else "discard"
    if decision == "keep":
        gate = gate_contrato(ROOT / args.path)
        if gate is not None:
            print(json.dumps({"gate_contrato": gate}, ensure_ascii=False, indent=2))
            if not gate["ok"]:
                decision = "discard"
                print("contrato incumplido: keep bajado a discard", file=sys.stderr)
    try:
        lesson = lesson_id_o_error(args.lesson_id)
    except SystemExit as e:
        print(e, file=sys.stderr)
        return 2
    traza = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "target_file": args.path,
        "hypothesis": args.hypothesis,
        "decision": decision,
        "score": data.get("score"),
        "eval": data,
        "gate": gate if decision == "keep" else None,
        "stderr": proc.stderr[-2000:],
    }
    ruta_traza = adjuntar_traza(lesson, traza)
    append_result(
        {
            "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "family": args.family,
            "hypothesis": args.hypothesis.replace("\t", " "),
            "target_file": args.path.replace("\t", " "),
            "metric": "template_gates",
            "score": data.get("score"),
            "decision": decision,
            "lesson_id": lesson,
        }
    )
    print(f"decision={decision} logged -> {RESULTS}")
    print(f"traza adjunta a la lección -> {ruta_traza}")
    print("Recuerda: si discard, NO dejes el diseno roto; vuelve al template v1.")
    return 0 if decision == "keep" else 1


if __name__ == "__main__":
    raise SystemExit(main())
