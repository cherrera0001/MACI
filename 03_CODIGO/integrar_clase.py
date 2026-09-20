"""
Integra una transcripcion de clase al flujo de Guillito, de principio a fin.

EL PROBLEMA QUE RESUELVE
Una transcripcion suelta es un .md de 85 KB que nadie va a leer entero. Para
que sirva hay que saber DONDE, en que clase y en que minuto, el profesor trato
cada concepto del curriculum. Eso permite preguntar "donde explico validacion
cruzada" y obtener clase y marca de tiempo.

EL FLUJO, EN ORDEN
  1. DETECTAR   transcripciones nuevas, no integradas todavia
  2. MAPEAR     que conceptos del curriculum aparecen, y en que minuto
  3. INDEXAR    escribir 09_CLASES/indice_clases.yaml
  4. SUBIR      a NotebookLM por MCP, si la sesion esta viva
  5. REPORTAR   que quedo disponible para estudiar

Es idempotente: si una clase ya esta integrada, se omite. Y degrada: si
NotebookLM no responde, los pasos 1 a 3 se completan igual y queda anotado.

USO
  python 03_CODIGO/integrar_clase.py             # todas las pendientes
  python 03_CODIGO/integrar_clase.py --sin-subir # no toca NotebookLM
  python 03_CODIGO/integrar_clase.py --estado    # solo muestra el indice
"""
import argparse
import glob
import os
import re
import subprocess
import sys
from datetime import date

import yaml

RAIZ = r"F:\MACI"
TRANSCRIPCIONES = os.path.join(RAIZ, "09_CLASES", "transcripciones")
INDICE = os.path.join(RAIZ, "09_CLASES", "indice_clases.yaml")
NOTEBOOK = "97ce114e-2371-44eb-85b5-527cd28180cb"
NLM = r"C:\Users\herre\.local\bin\notebooklm.exe"

# Terminos que delatan cada concepto del curriculum en el habla del profesor.
# Se buscan sobre el texto con marcas de tiempo, para poder situar el minuto.
TERMINOS = {
    "fundamentos_ciencia_datos": ["ciencia de datos", "ciclo de", "requerimiento"],
    "datos_features_target":     ["atributo", "etiqueta", "variable objetivo", "target", "feature"],
    "eda":                       ["exploratorio", "histograma", "distribuci", "correlaci", "boxplot"],
    "limpieza_preparacion":      ["calidad de datos", "valores faltantes", "dato faltante",
                                  "duplicad", "outlier", "atipico", "atípico", "limpi"],
    "train_validation_test":     ["entrenamiento", "conjunto de prueba", "validaci",
                                  "hold out", "holdout", "test"],
    "validacion_cruzada":        ["validacion cruzada", "validación cruzada", "k-fold",
                                  "kfold", "bootstrap", "submuestreo"],
    "generalizacion":            ["generaliza", "fuera de muestra", "datos nuevos"],
    "overfitting_underfitting":  ["sobreajuste", "sobre ajuste", "subajuste", "overfit",
                                  "sesgo y varianza", "complejidad del modelo"],
    "regresion":                 ["regresion lineal", "regresión lineal", "minimos cuadrados",
                                  "mínimos cuadrados", "polinomi", "funcion de costo",
                                  "función de costo", "r cuadrado", "residu"],
    "clasificacion":             ["clasificacion", "clasificación", "clasificador",
                                  "valor categorico", "categórico"],
    "matriz_confusion":          ["matriz de confusion", "matriz de confusión",
                                  "falso positivo", "falso negativo", "verdadero positivo"],
    "metricas_clasificacion":    ["precision", "precisión", "recall", "sensibilidad",
                                  "f1", "exactitud", "accuracy"],
    "roc_auc":                   ["curva roc", " roc ", "auc", "area bajo la curva",
                                  "área bajo la curva", "umbral"],
    "arboles_decision":          ["arbol de decision", "árbol de decisión", "arbolito",
                                  "entropia", "entropía", "gini", "impureza"],
    "random_forest":             ["random forest", "bosque aleatorio"],
    "gradient_boosting":         ["gradient boosting", "boosting", "xgboost"],
    "ensembles":                 ["ensamble", "ensemble", "combinar modelos", "diversidad"],
    "redes_neuronales":          ["red neuronal", "redes neuronales", "neurona",
                                  "backpropagation", "retropropagacion"],
    "deep_learning":             ["deep learning", "aprendizaje profundo", "capas ocultas"],
    "llm":                       ["modelo de lenguaje", "llm", "transformer", "token"],
    "agentes_ia":                ["agente", "agentes de ia", "herramientas del agente"],
}

MARCA = re.compile(r"\*\*\[(\d+:\d{2}:\d{2})\]\*\*")


def cargar_indice():
    if os.path.exists(INDICE):
        with open(INDICE, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {"meta": {"creado": date.today().isoformat()}, "clases": {}}


def guardar_indice(ind):
    ind["meta"]["actualizado"] = date.today().isoformat()
    ind["meta"]["total_clases"] = len(ind["clases"])
    with open(INDICE, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Indice de clases transcritas\n"
                "#\n"
                "# Generado por 03_CODIGO/integrar_clase.py. No editar a mano.\n"
                "#\n"
                "# Para cada clase: que conceptos del curriculum aparecen y en que\n"
                "# minuto se mencionan por primera vez. Permite ir directo al momento\n"
                "# en que el profesor trato un tema, en vez de leer 85 KB.\n"
                "#\n"
                "# Las marcas de tiempo son de la transcripcion automatica: pueden\n"
                "# desviarse unos segundos del video original.\n\n")
        yaml.safe_dump(ind, f, allow_unicode=True, sort_keys=False, width=88)


def mapear(texto):
    """Devuelve {concepto: {'menciones': n, 'primera_marca': 'H:MM:SS'}}."""
    bajo = texto.lower()
    # Posicion de cada marca de tiempo, para situar una coincidencia
    marcas = [(m.start(), m.group(1)) for m in MARCA.finditer(texto)]

    def marca_en(pos):
        ultima = "0:00:00"
        for p, t in marcas:
            if p > pos:
                break
            ultima = t
        return ultima

    hallado = {}
    for concepto, terminos in TERMINOS.items():
        posiciones = []
        for t in terminos:
            posiciones.extend(m.start() for m in re.finditer(re.escape(t), bajo))
        if posiciones:
            hallado[concepto] = {
                "menciones": len(posiciones),
                "primera_marca": marca_en(min(posiciones)),
            }
    return dict(sorted(hallado.items(), key=lambda kv: -kv[1]["menciones"]))


def subir(ruta, titulo):
    """Sube a NotebookLM. Devuelve (ok, detalle). Degrada sin romper."""
    if not os.path.exists(NLM):
        return False, "CLI de notebooklm no instalado"
    try:
        r = subprocess.run(
            [NLM, "source", "add", "-n", NOTEBOOK, "--type", "file",
             "--title", titulo, "--timeout", "240", ruta],
            capture_output=True, text=True, errors="replace", timeout=300)
    except subprocess.TimeoutExpired:
        return False, "tiempo agotado"
    salida = (r.stdout or "") + (r.stderr or "")
    if "Added source" in salida:
        sid = re.search(r"Added source:\s*(\S+)", salida)
        return True, sid.group(1) if sid else "ok"
    if "Authentication" in salida or "re-authenticate" in salida:
        return False, "sesion de NotebookLM caducada"
    return False, salida.strip().splitlines()[-1][:90] if salida.strip() else "error desconocido"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-subir", action="store_true", help="no toca NotebookLM")
    ap.add_argument("--estado", action="store_true", help="solo muestra el indice")
    a = ap.parse_args()

    ind = cargar_indice()

    if a.estado:
        print(f"{len(ind['clases'])} clases integradas\n")
        for nombre, d in ind["clases"].items():
            subido = "en NotebookLM" if d.get("notebooklm") else "solo local"
            print(f"  {nombre}")
            print(f"    {len(d['conceptos'])} conceptos · {subido}")
        return

    pendientes = []
    for ruta in sorted(glob.glob(os.path.join(TRANSCRIPCIONES, "*.md"))):
        nombre = os.path.basename(ruta)[:-3]
        if nombre in ind["clases"] and ind["clases"][nombre].get("notebooklm"):
            continue
        pendientes.append((ruta, nombre))

    if not pendientes:
        print("Nada pendiente: todas las transcripciones estan integradas.")
        return

    print(f"{len(pendientes)} transcripcion(es) por integrar\n")

    for ruta, nombre in pendientes:
        print("=" * 74)
        print(nombre)

        ya = ind["clases"].get(nombre)
        if ya:
            print("  ya mapeada; solo falta subirla")
            conceptos = ya["conceptos"]
        else:
            with open(ruta, encoding="utf-8", errors="replace") as f:
                texto = f.read()
            conceptos = mapear(texto)
            print(f"  {len(conceptos)} conceptos detectados:")
            for c, d in list(conceptos.items())[:6]:
                print(f"    {d['primera_marca']}  {c:<26} ({d['menciones']} menciones)")
            if len(conceptos) > 6:
                print(f"    … y {len(conceptos)-6} mas")
            ind["clases"][nombre] = {
                "archivo": f"09_CLASES/transcripciones/{nombre}.md",
                "plano": f"09_CLASES/transcripciones/{nombre}_plano.txt",
                "integrada": date.today().isoformat(),
                "conceptos": conceptos,
                "notebooklm": None,
            }

        if a.sin_subir:
            print("  subida omitida (--sin-subir)")
        else:
            titulo = "CLASE FCD · " + nombre.replace("_", " ")[:70]
            ok, detalle = subir(ruta, titulo)
            if ok:
                ind["clases"][nombre]["notebooklm"] = detalle
                print(f"  subida a NotebookLM: {detalle}")
            else:
                print(f"  NO subida: {detalle}")
                print("  (el indice local queda igual de util; reintentar luego)")

        guardar_indice(ind)

    print("=" * 74)
    print(f"indice actualizado: {INDICE}")
    sin_subir = sum(1 for d in ind["clases"].values() if not d.get("notebooklm"))
    if sin_subir:
        print(f"{sin_subir} clase(s) sin subir a NotebookLM. Reintentar con:")
        print("  python 03_CODIGO/integrar_clase.py")


if __name__ == "__main__":
    main()
