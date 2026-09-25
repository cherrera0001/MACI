"""
Hace utilizable el grafo de conceptos, en vez de solo almacenarlo.

EL PROBLEMA
curriculum.yaml declara prerrequisitos para 20 de 21 conceptos. Eran datos sin
comportamiento: Datito no podia responder de donde viene un concepto, que
depende de el, ni que pasa si no se comprende.

QUE HACE
  - recorre el grafo en ambos sentidos: prerrequisitos y dependientes
  - calcula importancia_curricular a partir de cuantos conceptos dependen de uno,
    directa o indirectamente. NO de cuanto se pregunta en un certamen
  - detecta ciclos y prerrequisitos rotos
  - genera 07_DATITO/grafo.yaml, que la skill consulta al abrir un concepto

LA DISTINCION QUE JUSTIFICA ESTO
importancia_curricular y prioridad_evaluacion son dimensiones distintas. La
regresion aparece poco en los certamenes y es de donde salen los conceptos que
se aplican despues en todo lo demas -lo dice el profesor en clase-. Optimizar
solo por puntaje enseña a rendir, no a entender.

USO
  python 03_SCRIPTS/grafo_conceptual.py                 # genera grafo.yaml
  python 03_SCRIPTS/grafo_conceptual.py --situar roc_auc  # consulta un concepto
"""
import argparse
import os
from collections import defaultdict

import yaml

RAIZ = r"F:\MACI"
CURRICULUM = os.path.join(RAIZ, "07_DATITO", "curriculum.yaml")
SALIDA = os.path.join(RAIZ, "07_DATITO", "grafo.yaml")

# Cadenas con sentido pedagogico. No son el grafo -eso sale de los
# prerrequisitos- sino trayectos que vale la pena recorrer completos.
# Peso en las evaluaciones reales, de 07_DATITO/patron_evaluacion.md.
# Es una dimension DISTINTA de importancia_curricular y no se deriva de ella.
# Un concepto fundacional puede preguntarse poco; uno periferico puede valer
# muchos puntos. Cuando difieren, Datito debe decirlo.
PRIORIDAD_EVALUACION = {
    "overfitting_underfitting":  {"peso": "alta",  "nota": "C2: P2, P3, P7 — 3 preguntas"},
    "limpieza_preparacion":      {"peso": "alta",  "nota": "C1: 9A y 9B; la 9B vale 2,0 pts"},
    "matriz_confusion":          {"peso": "alta",  "nota": "C2: P8, con calculo manual"},
    "metricas_clasificacion":    {"peso": "alta",  "nota": "C2: P4 y P8"},
    "roc_auc":                   {"peso": "media", "nota": "C2: P9"},
    "ensembles":                 {"peso": "media", "nota": "C2: P1"},
    "generalizacion":            {"peso": "media", "nota": "transversal a P2, P3, P7"},
    "train_validation_test":     {"peso": "media", "nota": "transversal"},
    "fundamentos_ciencia_datos": {"peso": "media", "nota": "C1: P1 a P4"},
    "datos_features_target":     {"peso": "media", "nota": "C1: P6 y 9A"},
    "clasificacion":             {"peso": "media", "nota": "C1: P6; base de C2"},
    "llm":                       {"peso": "baja",  "nota": "C2: P5"},
    "agentes_ia":                {"peso": "baja",  "nota": "C2: P5"},
    "redes_neuronales":          {"peso": "baja",  "nota": "C2: P6"},
    "regresion":                 {"peso": "baja",  "nota": "casi no se pregunta directamente"},
    "validacion_cruzada":        {"peso": "baja",  "nota": "aparece como remedio, no como pregunta propia"},
    "eda":                       {"peso": "baja",  "nota": "C1: 9A, de forma indirecta"},
    "arboles_decision":          {"peso": "baja",  "nota": "P4 menciona ganancia de pureza"},
    "random_forest":             {"peso": "baja",  "nota": "no aparece directamente"},
    "gradient_boosting":         {"peso": "baja",  "nota": "no aparece directamente"},
    "deep_learning":             {"peso": "baja",  "nota": "C2: P6, de forma indirecta"},
}

CADENAS = {
    "del error a la validacion": [
        "regresion", "overfitting_underfitting", "generalizacion",
        "train_validation_test", "validacion_cruzada",
    ],
    "de la clasificacion al AUC": [
        "clasificacion", "matriz_confusion", "metricas_clasificacion", "roc_auc",
    ],
    "de un arbol a un ensamble": [
        "arboles_decision", "random_forest", "gradient_boosting", "ensembles",
    ],
    "del dato al modelo": [
        "datos_features_target", "eda", "limpieza_preparacion", "regresion",
    ],
    "hacia los sistemas actuales": [
        "redes_neuronales", "deep_learning", "llm", "agentes_ia",
    ],
}


def cargar():
    with open(CURRICULUM, encoding="utf-8") as f:
        return yaml.safe_load(f)


def construir(cur):
    conceptos = {c["id"]: c for c in cur["conceptos"]}
    prereq = {cid: list(c.get("prerrequisitos") or []) for cid, c in conceptos.items()}

    # Dependientes directos: quien me nombra como prerrequisito
    dependientes = defaultdict(list)
    for cid, pres in prereq.items():
        for p in pres:
            dependientes[p].append(cid)

    def alcanzables(cid, mapa, visto=None):
        """Cierre transitivo, con guardia de ciclos."""
        visto = visto or set()
        salida = []
        for sig in mapa.get(cid, []):
            if sig in visto:
                continue
            visto.add(sig)
            salida.append(sig)
            salida.extend(alcanzables(sig, mapa, visto))
        return salida

    grafo = {}
    for cid, c in conceptos.items():
        dep_todos = alcanzables(cid, dependientes)
        pre_todos = alcanzables(cid, prereq)
        grafo[cid] = {
            "nombre": c["nombre"],
            "viene_de": prereq[cid],
            "habilita": sorted(dependientes.get(cid, [])),
            "habilita_indirectamente": sorted(set(dep_todos) - set(dependientes.get(cid, []))),
            "requiere_antes": sorted(set(pre_todos)),
            # Cuantos conceptos quedan bloqueados si este no se comprende.
            "importancia_curricular": len(set(dep_todos)),
            "prioridad_evaluacion": PRIORIDAD_EVALUACION.get(
                cid, {"peso": "desconocida", "nota": "sin dato"}),
            "es_raiz": not prereq[cid],
            "es_hoja": not dependientes.get(cid),
        }

    # La tension entre ambas dimensiones es lo que Datito debe poder decir.
    orden_peso = {"alta": 3, "media": 2, "baja": 1, "desconocida": 0}
    maxima = max(d["importancia_curricular"] for d in grafo.values()) or 1
    for cid, d in grafo.items():
        estructural = d["importancia_curricular"] / maxima          # 0 a 1
        examen = orden_peso[d["prioridad_evaluacion"]["peso"]] / 3   # 0 a 1
        if estructural >= 0.45 and examen <= 0.34:
            d["tension"] = ("fundacional pero poco preguntado: se necesita para "
                            f"{d['importancia_curricular']} conceptos posteriores")
        elif estructural <= 0.2 and examen >= 0.9:
            d["tension"] = ("muy preguntado y poco estructural: rinde puntos, "
                            "no desbloquea otros conceptos")
        else:
            d["tension"] = None
    return grafo, conceptos


def detectar_ciclos(grafo):
    ciclos = []
    for cid, d in grafo.items():
        if cid in d["requiere_antes"]:
            ciclos.append(cid)
    return ciclos


def situar(cid, grafo):
    """Lo que Datito necesita responder al abrir un concepto."""
    if cid not in grafo:
        print(f"No existe el concepto '{cid}'")
        return
    d = grafo[cid]
    n = lambda x: grafo[x]["nombre"] if x in grafo else x

    print(f"\n{d['nombre']}  ({cid})")
    print("=" * 70)

    print("\nDE DONDE VIENE")
    if d["viene_de"]:
        for p in d["viene_de"]:
            print(f"  <- {n(p)}")
    else:
        print("  es un punto de entrada: no depende de nada anterior")

    print("\nQUE DEPENDE DE EL")
    if d["habilita"]:
        for h in d["habilita"]:
            print(f"  -> {n(h)}")
        if d["habilita_indirectamente"]:
            print(f"  y {len(d['habilita_indirectamente'])} mas por cadena:")
            for h in d["habilita_indirectamente"][:5]:
                print(f"       {n(h)}")
    else:
        print("  ninguno: es terminal en el programa")

    print(f"\nIMPORTANCIA CURRICULAR: {d['importancia_curricular']} conceptos "
          f"quedan bloqueados si este no se comprende")
    pe = d["prioridad_evaluacion"]
    print(f"PRIORIDAD EN EVALUACION: {pe['peso']} — {pe['nota']}")
    if d.get("tension"):
        print(f"\n  ATENCION: {d['tension']}")

    cadenas = [nom for nom, lista in CADENAS.items() if cid in lista]
    if cadenas:
        print("\nAPARECE EN")
        for nom in cadenas:
            partes = [("**" + n(x) + "**" if x == cid else n(x)) for x in CADENAS[nom]]
            print(f"  {nom}:")
            print("    " + "  ->  ".join(partes))
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--situar", metavar="CONCEPTO", help="consultar un concepto")
    a = ap.parse_args()

    cur = cargar()
    grafo, conceptos = construir(cur)

    ciclos = detectar_ciclos(grafo)
    if ciclos:
        print("CICLOS DETECTADOS, el grafo no es valido:", ciclos)
        return

    if a.situar:
        situar(a.situar, grafo)
        return

    doc = {
        "meta": {
            "descripcion": "Grafo de conceptos, generado desde curriculum.yaml. "
                           "No editar a mano.",
            "generado_por": "03_SCRIPTS/grafo_conceptual.py",
            "importancia_curricular": "numero de conceptos que quedan bloqueados "
                                      "si este no se comprende. Es independiente "
                                      "de cuanto se pregunte en un certamen.",
        },
        "cadenas": CADENAS,
        "conceptos": grafo,
    }
    with open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(doc, f, allow_unicode=True, sort_keys=False, width=90)

    print(f"grafo generado: {SALIDA}\n")
    orden = sorted(grafo.items(), key=lambda kv: -kv[1]["importancia_curricular"])
    print("IMPORTANCIA CURRICULAR (cuantos conceptos dependen de el)")
    print("-" * 70)
    for cid, d in orden[:10]:
        raiz = "  [raiz]" if d["es_raiz"] else ""
        print(f"  {d['importancia_curricular']:>2}  {d['nombre']}{raiz}")
    print()
    raices = [d["nombre"] for d in grafo.values() if d["es_raiz"]]
    hojas = [d["nombre"] for d in grafo.values() if d["es_hoja"]]
    print(f"puntos de entrada: {', '.join(raices)}")
    print(f"terminales: {len(hojas)}")


if __name__ == "__main__":
    main()
