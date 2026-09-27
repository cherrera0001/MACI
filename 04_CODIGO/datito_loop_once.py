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
EVAL = ROOT / "03_CODIGO" / "datito_loop_eval.py"


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
    lesson = args.lesson_id or ("VIZ-KEEP-001" if decision == "keep" else "VIZ-FAIL-001")
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
    print("Recuerda: si discard, NO dejes el diseno roto; vuelve al template v1.")
    return 0 if decision == "keep" else 1


if __name__ == "__main__":
    raise SystemExit(main())
