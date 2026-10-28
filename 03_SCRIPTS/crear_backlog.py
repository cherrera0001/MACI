"""Siembra el backlog de docs/gestion/backlog.yaml como issues del Project. Idempotente.

Crea etiquetas, el milestone, los campos del Project (Tipo, Prioridad, Proceso),
un issue por épica, historia, decisión y tarea, y los enlaza como sub-issues.
Un ítem cuyo título ya existe (por su prefijo «[E-1]», «[H-1.1]»…) no se vuelve
a crear: solo se repasan su padre y sus campos.

  python 03_SCRIPTS/crear_backlog.py --dry-run   # muestra qué haría
  python 03_SCRIPTS/crear_backlog.py             # lo hace

Usa `gh` con el token de .env (GITHUB_TOKEN_CLASIC, luego GITHUB_TOKEN): la
cuenta activa de `gh` puede ser otra.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]
SEMILLA = RAIZ / "docs" / "gestion" / "backlog.yaml"
WIKI = "https://github.com/{repo}/wiki"

TIPOS = {"epica": "Épica", "historia": "Historia", "decision": "Decisión", "tarea": "Tarea", "bug": "Bug"}
ETIQUETAS = {
    "tipo:epica": ("5319e7", "Resultado grande; agrupa historias"),
    "tipo:historia": ("1d76db", "Valor para un usuario, con criterios de aceptación"),
    "tipo:decision": ("d93f0b", "Pregunta que solo el dueño puede responder"),
    "tipo:tarea": ("0e8a16", "Trabajo concreto dentro de una historia"),
    "tipo:bug": ("b60205", "Algo que funcionaba y dejó de funcionar"),
    "area:curso": ("c5def5", "Clases, visuales y certámenes"),
    "area:datito": ("c5def5", "El tutor y el progreso del alumno"),
    "area:plataforma": ("c5def5", "Fuente única, generador, verificación y publicación"),
    "area:loop": ("c5def5", "Agents Learning Loop"),
    "area:proyecto-fcd": ("c5def5", "Melbourne, Galaxy Zoo y certámenes"),
    "area:gobernanza": ("c5def5", "Visibilidad, higiene del repo y gestión"),
    "prioridad:P0": ("b60205", "Bloquea la versión"),
    "prioridad:P1": ("fbca04", "Entra en la versión"),
    "prioridad:P2": ("fef2c0", "Después de la versión"),
}
PRIORIDADES = ["P0", "P1", "P2"]


def token():
    lineas = (RAIZ / ".env").read_text(encoding="utf-8").splitlines()
    for clave in ("GITHUB_TOKEN_CLASIC", "GITHUB_TOKEN"):
        for linea in lineas:
            if linea.startswith(clave + "="):
                return linea.split("=", 1)[1].strip().strip('"')
    sys.exit("Falta GITHUB_TOKEN_CLASIC en .env")


ENV = None


def gh(*args, entrada=None, tolerar=False):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8", env=ENV, input=entrada)
    if r.returncode and not tolerar:
        sys.exit(f"gh {' '.join(args[:4])}…\n{r.stderr}")
    return r.stdout.strip()


def graphql(query, **variables):
    args = ["api", "graphql", "-f", f"query={query}"]
    for k, v in variables.items():
        args += ["-F" if isinstance(v, int) else "-f", f"{k}={v}"]
    return json.loads(gh(*args))["data"]


# ── cuerpos ──────────────────────────────────────────────────────────────────

def lista(items, casilla=False):
    return "\n".join(f"- {'[ ] ' if casilla else ''}{i}" for i in items)


def pie(item, semilla):
    padre = f" · Padre: {item['padre_titulo']}" if item.get("padre_titulo") else ""
    return (f"\n\n---\nTipo: {TIPOS[item['tipo']]} · Prioridad: {item['prioridad']} · "
            f"Proceso: [{semilla['procesos'][item['proceso']]}]({WIKI.format(repo=semilla['repo'])}/Procesos){padre}")


def cuerpo(item, semilla):
    t = item["tipo"]
    if t == "epica":
        b = (f"## Resultado\n{item['resultado']}\n\n## Contexto e historia\n{item['contexto'].rstrip()}\n\n"
             f"## Cómo se mide\n{lista(item['metricas'])}\n\n"
             "## Historias\nSon los sub-issues de esta épica. El avance se lee en «Sub-issues progress».")
    elif t == "historia":
        b = (f"## Historia\n{item['titulo']}.\n\n## Contexto y evidencia\n{item['contexto'].rstrip()}\n\n"
             f"## Criterios de aceptación\n{lista(item['criterios'], True)}\n\n"
             "## Tareas\nSon los sub-issues de esta historia.\n\n"
             "## Definición de hecho\n- [ ] Criterios de aceptación marcados, cada uno con su evidencia en un comentario\n"
             "- [ ] `python 03_SCRIPTS/verificar_todo.py --navegador --en-linea` dice LISTO\n"
             "- [ ] PR fusionado con `Closes #<este issue>`")
    elif t == "decision":
        b = (f"## Pregunta\n{item['titulo']}\n\n## Contexto\n{item['contexto'].rstrip()}\n\n"
             f"## Opciones\n{lista(item['opciones'])}\n\n"
             f"## Se cierra cuando\n{lista(item['criterios'], True)}\n\n"
             "La decisión la escribe el dueño del repo en un comentario. Un agente no la toma.")
    else:
        b = f"## Qué hay que hacer\n{item['titulo']}.\n\n{item.get('detalle', '').rstrip()}"
    return b + pie(item, semilla)


def aplanar(semilla):
    """Épicas, historias y tareas en orden de creación, cada una con su padre."""
    items = []
    for e in semilla["epicas"]:
        e = {**e, "tipo": "epica", "padre": None}
        items.append(e)
        for h in e["historias"]:
            h = {"tipo": "historia", **h, "area": e["area"], "proceso": e["proceso"], "padre": e["id"]}
            items.append(h)
            for t in h.get("tareas", []):
                items.append({**t, "tipo": "tarea", "area": e["area"], "proceso": e["proceso"],
                              "prioridad": h["prioridad"], "v1": h["v1"], "padre": h["id"]})
    titulos = {i["id"]: f"[{i['id']}] {i['titulo']}" for i in items}
    for i in items:
        i["padre_titulo"] = titulos.get(i["padre"], "").split("] ")[0] + "]" if i["padre"] else None
    return items


# ── GitHub ───────────────────────────────────────────────────────────────────

def issues_existentes(repo):
    datos = json.loads(gh("api", f"repos/{repo}/issues?state=all&per_page=100", "--paginate", "--slurp"))
    return {i["number"]: i for pagina in datos for i in pagina if "pull_request" not in i}


def asegurar_campos(dueno, numero, semilla):
    q = """query($o:String!,$n:Int!){user(login:$o){projectV2(number:$n){id fields(first:40){nodes{
      ... on ProjectV2SingleSelectField{id name options{id name}}}}}}}"""
    quiero = {"Tipo": list(TIPOS.values()), "Prioridad": PRIORIDADES, "Proceso": list(semilla["procesos"].values())}
    p = graphql(q, o=dueno, n=numero)["user"]["projectV2"]
    tengo = {f["name"] for f in p["fields"]["nodes"] if f}
    for nombre, opciones in quiero.items():
        if nombre not in tengo:
            gh("project", "field-create", str(numero), "--owner", dueno, "--name", nombre,
               "--data-type", "SINGLE_SELECT", "--single-select-options", ",".join(opciones))
    p = graphql(q, o=dueno, n=numero)["user"]["projectV2"]
    campos = {f["name"]: {"id": f["id"], **{o["name"]: o["id"] for o in f["options"]}} for f in p["fields"]["nodes"] if f}
    return p["id"], campos


def item_del_project(pid, node_id):
    q = "query($c:ID!){node(id:$c){... on Issue{projectItems(first:20){nodes{id project{id}}}}}}"
    return next((n["id"] for n in graphql(q, c=node_id)["node"]["projectItems"]["nodes"] if n["project"]["id"] == pid), None)


def al_project(pid, campos, node_id, valores):
    # El flujo «auto-add» del Project puede adelantarse: por eso se busca antes y después de agregar.
    item = item_del_project(pid, node_id)
    if not item:
        gh("api", "graphql", "-f", "query=mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p,contentId:$c}){item{id}}}",
           "-f", f"p={pid}", "-f", f"c={node_id}", tolerar=True)
        item = item_del_project(pid, node_id)
    m = ("mutation($p:ID!,$i:ID!,$f:ID!,$o:String!){updateProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,"
         "fieldId:$f,value:{singleSelectOptionId:$o}}){clientMutationId}}")
    for campo, valor in valores.items():  # de a uno: varios cambios al mismo ítem en una mutación fallan
        graphql(m, p=pid, i=item, f=campos[campo]["id"], o=campos[campo][valor])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    global ENV
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    semilla = yaml.safe_load(SEMILLA.read_text(encoding="utf-8"))
    repo, dueno, numero = semilla["repo"], semilla["repo"].split("/")[0], semilla["project"]
    items = aplanar(semilla)
    if a.dry_run:
        for i in items:
            print(f"{'  ' * (i['id'].count('.') + (i['tipo'] != 'epica'))}[{i['id']}] {i['titulo'][:90]}")
        print(f"\n{len(items)} ítems · {sum(i['v1'] for i in items)} en «{semilla['milestone']['titulo']}»")
        return
    ENV = {**os.environ, "GH_TOKEN": token()}

    for nombre, (color, desc) in ETIQUETAS.items():
        gh("label", "create", nombre, "-R", repo, "--color", color, "--description", desc, "--force")

    hitos = json.loads(gh("api", f"repos/{repo}/milestones?state=all"))
    hito = next((m["number"] for m in hitos if m["title"] == semilla["milestone"]["titulo"]), None)
    if hito is None:
        hito = json.loads(gh("api", f"repos/{repo}/milestones", "-f", f"title={semilla['milestone']['titulo']}",
                             "-f", f"description={semilla['milestone']['descripcion']}"))["number"]

    existentes = issues_existentes(repo)
    por_prefijo = {m.group(1): i for i in existentes.values() if (m := re.match(r"\[([EHDT]-[\d.]+)\]", i["title"]))}
    pid, campos = asegurar_campos(dueno, numero, semilla)

    for i in items:
        if i["id"] not in por_prefijo:
            args = ["api", f"repos/{repo}/issues", "-f", f"title=[{i['id']}] {i['titulo']}", "-F", "body=@-",
                    "-f", f"labels[]=tipo:{i['tipo']}", "-f", f"labels[]=area:{i['area']}",
                    "-f", f"labels[]=prioridad:{i['prioridad']}"]
            if i["v1"]:
                args += ["-F", f"milestone={hito}"]
            por_prefijo[i["id"]] = json.loads(gh(*args, entrada=cuerpo(i, semilla)))
            print(f"creado #{por_prefijo[i['id']]['number']} [{i['id']}]")
        issue = por_prefijo[i["id"]]
        if i["padre"]:
            gh("api", f"repos/{repo}/issues/{por_prefijo[i['padre']]['number']}/sub_issues",
               "-F", f"sub_issue_id={issue['id']}", tolerar=True)
        al_project(pid, campos, issue["node_id"], {
            "Tipo": TIPOS[i["tipo"]], "Prioridad": i["prioridad"], "Proceso": semilla["procesos"][i["proceso"]],
            "Status": "Done" if issue["state"] == "closed" else "Todo"})

    for n, h in semilla["historicos"].items():
        issue = existentes[n]
        gh("issue", "edit", str(n), "-R", repo, "--add-label", f"tipo:{h['tipo']},area:{h['area']}")
        if h.get("padre"):
            gh("api", f"repos/{repo}/issues/{por_prefijo[h['padre']]['number']}/sub_issues",
               "-F", f"sub_issue_id={issue['id']}", tolerar=True)
        al_project(pid, campos, issue["node_id"],
                   {"Tipo": TIPOS[h["tipo"]], "Proceso": semilla["procesos"][h["proceso"]]})
    print(f"listo: {len(items)} ítems y {len(semilla['historicos'])} históricos en el Project #{numero}")


if __name__ == "__main__":
    main()
