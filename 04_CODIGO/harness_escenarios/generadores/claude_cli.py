"""Generador real: la skill /datito via `claude -p` (REQ-TUT-006).

  07_DATITO real --sha256--> h0
        |
  git worktree add --detach <scratch>      (la skill escribe ahi, nunca en el repo)
        |
  turno 1: claude -p "/datito <situacion> <alumno>" --session-id <uuid>
  turno k: claude -p --resume <uuid> "<alumno>"
        |  stream-json -> turnos tutor + acciones (duda:*, lee:*, ejecuta:*)
  git worktree remove --force
        |
  07_DATITO real --sha256--> h1      h0 != h1  => ErrorGeneracion("aislamiento")

No se usa --no-session-persistence: impide --resume y el escenario es multiturno.
La skill cuenta como cargada si el evento init la lista en slash_commands; el
prompt la invoca con /datito.
"""
import datetime
import hashlib
import json
import re
import shlex
import shutil
import subprocess
import tempfile
import uuid
from pathlib import Path

import yaml

from . import BASE, ErrorGeneracion, guion_alumno

REPO = BASE.parent.parent
REALES = BASE / "transcripts_reales"
MARCA = "[ESCENARIO SINTÉTICO · G10 · alumno simulado]"
TIMEOUT_S = 300  # 180 s corto: un turno real con ~9 lecturas Bash lo supero (baseline 671d3f8)
EJECUTA = {"Bash", "NotebookEdit"}
# Bash que solo lee el repo no decide por el alumno (G2): cuenta como lee:Bash.
LECTURA = {"cat", "ls", "grep", "rg", "head", "tail", "find", "wc", "sed",
           "sort", "uniq", "cut", "tr", "file", "stat", "tree", "echo", "pwd", "true"}
GIT_LECTURA = {"log", "show", "status", "diff", "ls-files", "grep", "rev-parse", "blame"}


def hash_arbol(raiz):
    h = hashlib.sha256()
    raiz = Path(raiz)
    if not raiz.exists():
        return h.hexdigest()
    for p in sorted(x for x in raiz.rglob("*") if x.is_file()):
        h.update(str(p.relative_to(raiz)).encode())
        h.update(p.read_bytes())
    return h.hexdigest()


def _tramos(comando):
    """Parte el comando en tramos por ; && || | respetando comillas; None si no se puede."""
    lex = shlex.shlex(comando, posix=True, punctuation_chars=";&|<>")
    lex.whitespace_split = True
    tramos, actual = [], []
    try:
        for tok in lex:
            if tok and set(tok) <= set(";&|"):
                tramos.append(actual)
                actual = []
            elif tok and set(tok) <= set("<>"):
                return None  # redireccion a archivo (las de /dev/null ya se quitaron)
            else:
                actual.append(tok)
    except ValueError:
        return None
    return tramos + [actual]


def es_lectura(comando):
    """True si cada tramo del comando solo lee: sin redireccion a archivo ni edicion in situ."""
    sin_null = re.sub(r"\d?>\s*/dev/null|\d?>&\d", " ", comando.replace("\n", ";"))
    if re.search(r"\$\(|`", sin_null):
        return False
    tramos = _tramos(sin_null)
    if tramos is None:
        return False
    for pal in filter(None, tramos):
        cab = pal[0]
        if cab == "git":
            if len(pal) < 2 or pal[1] not in GIT_LECTURA:
                return False
        elif cab not in LECTURA:
            return False
        if cab == "sed" and any(x.startswith("-i") for x in pal[1:]):
            return False
        if cab == "find" and any(x in ("-delete", "-exec", "-execdir") for x in pal[1:]):
            return False
    return True


def _acciones(bloque):
    nombre = bloque.get("name")
    entrada = bloque.get("input") or {}
    ruta = str(entrada.get("file_path", ""))
    if nombre in ("Write", "Edit") and ruta.endswith("07_DATITO/dudas.yaml"):
        return ["duda:registrada"]
    if nombre == "Bash" and es_lectura(str(entrada.get("command", ""))):
        return ["lee:Bash"]
    if nombre in EJECUTA:
        return [f"ejecuta:{nombre}"]
    return []


def parse_stream(lineas, exigir_skill=False):
    """Una llamada a `claude -p` -> un turno del tutor y su meta."""
    textos, acciones, meta, init, resultado = [], [], {}, None, None
    for n, linea in enumerate(lineas):
        linea = linea.strip()
        if not linea:
            continue
        try:
            ev = json.loads(linea)
        except json.JSONDecodeError as e:
            raise ErrorGeneracion("parse", f"linea {n}: {e}") from e
        tipo = ev.get("type")
        if tipo == "system" and ev.get("subtype") == "init":
            init = ev
        elif tipo == "assistant":
            for b in (ev.get("message") or {}).get("content") or []:
                if b.get("type") == "text" and b.get("text", "").strip():
                    textos.append(b["text"].strip())
                elif b.get("type") == "tool_use":
                    acciones.extend(_acciones(b))
        elif tipo == "result":
            resultado = ev
    if resultado is None:
        raise ErrorGeneracion("parse", "stream sin evento result (cortado)")
    if resultado.get("subtype") == "error_max_budget_usd":
        raise ErrorGeneracion("budget", "la llamada supero --max-budget-usd")
    if resultado.get("is_error"):
        raise ErrorGeneracion("cli", str(resultado.get("result") or resultado.get("subtype")))
    if exigir_skill:
        cargadas = set((init or {}).get("slash_commands") or []) | set((init or {}).get("skills") or [])
        if "datito" not in cargadas:
            raise ErrorGeneracion("skill-no-cargada", "init no lista la skill datito")
    if not textos:
        raise ErrorGeneracion("parse", "la llamada no produjo texto del tutor")
    meta["sesion"] = resultado.get("session_id")
    meta["costo_usd"] = float(resultado.get("total_cost_usd") or 0.0)
    turno = {"rol": "tutor", "texto": "\n\n".join(textos)}
    if acciones:
        turno["acciones"] = acciones
    return turno, meta


def _llamar(cwd, prompt, sesion, primera, presupuesto, modelo):
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose",
           "--setting-sources", "project", "--permission-mode", "bypassPermissions",
           "--max-budget-usd", f"{presupuesto:.2f}"]
    cmd += ["--session-id", sesion] if primera else ["--resume", sesion]
    if modelo:
        cmd += ["--model", modelo]
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=TIMEOUT_S, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired as e:
        raise ErrorGeneracion("timeout", f"{TIMEOUT_S}s") from e
    except FileNotFoundError as e:
        raise ErrorGeneracion("cli", "no se encontro el binario claude") from e
    if r.returncode != 0 and '"type":"result"' not in r.stdout:
        raise ErrorGeneracion("cli", (r.stderr or r.stdout).strip()[:300])
    return r.stdout.splitlines()


def conversar(esc, llamar, presupuesto):
    """Arma el transcript alternando el guion del alumno con llamadas al tutor."""
    abre_alumno, guion = guion_alumno(esc)
    sesion = str(uuid.uuid4())
    turnos, costo = [], 0.0
    pendientes = list(guion)
    # solo la situacion: el contexto describe lo que se espera del tutor y le daria la respuesta
    prompt = f"/datito\n{MARCA}\n{esc['situacion'].strip()}"
    if abre_alumno and pendientes:
        primero = pendientes.pop(0)
        turnos.append({"rol": "alumno", **primero})
        prompt += f"\n\n{MARCA} Alumno: {primero['texto']}"
    primera = True
    while True:
        turno, meta = parse_stream(llamar(prompt, sesion, primera, presupuesto), exigir_skill=primera)
        turnos.append(turno)
        costo += meta["costo_usd"]
        primera = False
        if not pendientes:
            break
        siguiente = pendientes.pop(0)
        turnos.append({"rol": "alumno", **siguiente})
        prompt = f"{MARCA} Alumno: {siguiente['texto']}"
    return {"turnos": turnos, "meta": {"generador": "claude", "sesion": sesion, "costo_usd": costo}}


def generar(esc, corrida=1, presupuesto=0.50, modelo=None, datito=None, guardar=True):
    datito = Path(datito) if datito else REPO / "07_DATITO"
    h0 = hash_arbol(datito)
    tmp = Path(tempfile.mkdtemp(prefix="harness-claude-")) / "wt"
    subprocess.run(["git", "-C", str(REPO), "worktree", "add", "-q", "--detach", str(tmp), "HEAD"],
                   check=True, capture_output=True)
    try:
        def llamar(prompt, sesion, primera, presup):
            return _llamar(tmp, prompt, sesion, primera, presup, modelo)
        tr = conversar(esc, llamar, presupuesto)
    finally:
        subprocess.run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(tmp)],
                       capture_output=True)
        shutil.rmtree(tmp.parent, ignore_errors=True)
    if hash_arbol(datito) != h0:
        raise ErrorGeneracion("aislamiento", "07_DATITO cambio durante la corrida")
    tr["meta"]["corrida"] = corrida
    if guardar:
        destino = REALES / datetime.date.today().isoformat()
        destino.mkdir(parents=True, exist_ok=True)
        (destino / f"{esc['id']}-{corrida}.yaml").write_text(
            yaml.safe_dump(tr, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return tr
