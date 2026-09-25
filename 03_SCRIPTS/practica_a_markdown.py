"""
Convierte los notebooks de 08_PRACTICA a Markdown para subirlos a NotebookLM.

NotebookLM no acepta .ipynb como fuente; si acepta Markdown. Se conserva el
texto explicativo y el codigo, y se descartan las salidas binarias (imagenes
base64), que solo inflarian el archivo sin aportar al indice de busqueda.

Salida: 08_PRACTICA/_markdown/<nombre>.md
"""
import glob
import json
import os
import re

ORIGEN = r"F:\MACI\08_PRACTICA"
DESTINO = os.path.join(ORIGEN, "_markdown")
LIMITE_SALIDA = 2000  # caracteres por salida de celda


def limpiar(nombre):
    n = os.path.basename(nombre).replace(".ipynb", "")
    n = re.sub(r"[^\w\s\-\+]", "_", n, flags=re.UNICODE)
    return re.sub(r"_+", "_", n).strip("_")


def convertir(ruta):
    nb = json.load(open(ruta, encoding="utf-8"))
    partes = [f"# {limpiar(ruta)}\n",
              "> Material practico de Fundamentos de Ciencia de Datos, UdeC T2-2026.\n",
              f"> Convertido desde `{os.path.basename(ruta)}` para indexacion.\n"]

    for celda in nb.get("cells", []):
        fuente = "".join(celda.get("source", [])).rstrip()
        if not fuente:
            continue

        if celda.get("cell_type") == "markdown":
            partes.append(fuente + "\n")
            continue

        partes.append(f"```python\n{fuente}\n```\n")

        # Solo salidas de texto: las imagenes no aportan al indice.
        for salida in celda.get("outputs", []):
            texto = salida.get("text") or (salida.get("data", {}) or {}).get("text/plain") or ""
            if isinstance(texto, list):
                texto = "".join(texto)
            texto = texto.strip()
            if texto:
                if len(texto) > LIMITE_SALIDA:
                    texto = texto[:LIMITE_SALIDA] + "\n... (salida truncada)"
                partes.append(f"*Salida:*\n```\n{texto}\n```\n")

    return "\n".join(partes)


if __name__ == "__main__":
    os.makedirs(DESTINO, exist_ok=True)
    for ruta in sorted(glob.glob(os.path.join(ORIGEN, "*.ipynb"))):
        if "(vacio)" in ruta:
            continue  # los vacios son los ejercicios del alumno, no material de consulta
        md = convertir(ruta)
        destino = os.path.join(DESTINO, limpiar(ruta) + ".md")
        with open(destino, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"{os.path.basename(destino):<55} {len(md):>8,} caracteres")
