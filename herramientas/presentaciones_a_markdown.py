"""
Convierte las presentaciones del curso a Markdown buscable.

Por que: los PDF pesan 20 MB en total y no se buscan con grep. El texto
extraido cabe en unos cientos de KB, se versiona, se lee sin conexion y se
sube a NotebookLM mucho mas liviano.

Detecta y omite duplicados por hash, que en esta carpeta los hay -las copias
"(1)" de Clase 5 y Clase 6-.

Salida: 11_PRESENTACION/_markdown/<nombre>.md
"""
import glob
import hashlib
import os
import re

from pypdf import PdfReader

ORIGEN = r"F:\MACI\11_PRESENTACIÓN"
DESTINO = os.path.join(ORIGEN, "_markdown")


def limpiar(nombre):
    n = os.path.splitext(os.path.basename(nombre))[0]
    n = re.sub(r"\s*\(\d+\)$", "", n)          # quita el sufijo de copia
    n = re.sub(r"[^\w\s\-\+]", "_", n, flags=re.UNICODE)
    return re.sub(r"[\s_]+", "_", n).strip("_")


def hash_archivo(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def normalizar(texto):
    """El texto de PDF trae saltos donde no corresponden y espacios dobles."""
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


# PDFs que llegaron a 11_PRESENTACIÓN/ pero son de OTRO curso (Prototipos y
# creatividad, 2026G601): su lamina 1 lo dice. Detectado el 2026-09-21. Se
# convierten igual, pero con una cabecera que impide citarlos como material FCD.
OTRO_CURSO = ("Resumen_Clase1_Prototipos", "Resumen_Clase2_Creatividad",
              "Resumen_Clase3_Metricas_para_Proyectos", "Resumen_Clase5_Validacion_de_Clientes")


def convertir(ruta):
    lector = PdfReader(ruta)
    ajeno = os.path.basename(ruta).startswith(OTRO_CURSO)
    partes = [
        f"# {limpiar(ruta)}",
        "",
        ("> **NO es material de Fundamentos de Ciencia de Datos**: pertenece al curso "
         "Prototipos y creatividad. No citarlo como fuente de Datito." if ajeno else
         "> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026."),
        f"> Texto extraido de `{os.path.basename(ruta)}` para busqueda e indexacion.",
        f"> {len(lector.pages)} laminas. Las figuras no se extraen: si una lamina",
        "> depende de un grafico, hay que abrir el PDF.",
        "",
        "---",
        "",
    ]
    for i, pagina in enumerate(lector.pages, 1):
        texto = normalizar(pagina.extract_text() or "")
        if not texto:
            continue
        partes.append(f"## Lamina {i}")
        partes.append("")
        partes.append(texto)
        partes.append("")
    return "\n".join(partes)


def main():
    os.makedirs(DESTINO, exist_ok=True)
    vistos = {}
    hechos = omitidos = 0

    for ruta in sorted(glob.glob(os.path.join(ORIGEN, "*.pdf"))):
        h = hash_archivo(ruta)
        if h in vistos:
            print(f"  duplicado, se omite: {os.path.basename(ruta)}")
            print(f"    (identico a {os.path.basename(vistos[h])})")
            omitidos += 1
            continue
        vistos[h] = ruta

        try:
            md = convertir(ruta)
        except Exception as e:
            print(f"  ERROR en {os.path.basename(ruta)}: {e}")
            continue

        destino = os.path.join(DESTINO, limpiar(ruta) + ".md")
        with open(destino, "w", encoding="utf-8", newline="\n") as f:
            f.write(md)
        print(f"  {os.path.basename(destino):<52} {len(md):>7,} car.")
        hechos += 1

    print(f"\n{hechos} convertidos, {omitidos} duplicados omitidos")


if __name__ == "__main__":
    main()
