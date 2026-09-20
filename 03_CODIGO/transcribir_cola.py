"""
Transcribe en cola todas las clases que faltan, extrayendo de los ZIP una a una.

EL PROBLEMA QUE RESUELVE
Las 15 grabaciones viven dentro de tres ZIP de ~2 GB en 10_GRABACION_CLASES/.
transcribir_clases.py sabe transcribir UN mp4 suelto, pero espera encontrarlo ya
extraido en Downloads. Extraer los 15 de golpe son 4,5 GB en disco y una lista
que hay que ir pasando a mano.

Este runner cierra ese hueco: mira que hay dentro de los ZIP, compara contra
09_CLASES/transcripciones/, y procesa solo lo que falta. Para cada pendiente:
extrae -> transcribe -> borra el mp4. Nunca hay mas de un video extraido a la vez.

ES REANUDABLE
transcribir_clases.transcribir() omite lo que ya tiene .md. Si esto se corta a
mitad -y se va a cortar, son horas de CPU- basta volver a lanzarlo: retoma donde
iba. No hay estado que mantener.

ORDEN DE PROCESO
Primero las dos clases con mas valor de estudio -el dia de cada certamen-,
despues el resto de menor a mayor tamaño, para que los resultados empiecen a
aparecer pronto en vez de despues de la clase de 700 MB.

USO
  uv run --with faster-whisper python 03_CODIGO/transcribir_cola.py --listar
  uv run --with faster-whisper python 03_CODIGO/transcribir_cola.py
  uv run --with faster-whisper python 03_CODIGO/transcribir_cola.py --modelo medium
"""
import argparse
import os
import shutil
import sys
import time
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribir_clases import DESTINO, limpiar, transcribir, hhmmss

ZIPS = r"F:\MACI\10_GRABACIÓN_CLASES"
TRABAJO = r"F:\MACI\10_GRABACIÓN_CLASES\_extraido"
YA_EXTRAIDOS = os.path.join(os.path.expanduser("~"), "Downloads")

# Las dos que mas rinden al estudiar: el dia de cada certamen.
PRIORIDAD = ["2026-08-28", "05Certamen"]


def inventario():
    """Devuelve [(nombre_mp4, zip_o_None, ruta_suelta_o_None, bytes)] de los 15."""
    items = {}
    for z in sorted(os.listdir(ZIPS)):
        if not z.lower().endswith(".zip"):
            continue
        ruta_zip = os.path.join(ZIPS, z)
        try:
            with zipfile.ZipFile(ruta_zip) as zf:
                for info in zf.infolist():
                    if info.is_dir() or not info.filename.lower().endswith(".mp4"):
                        continue
                    base = os.path.basename(info.filename)
                    items[base] = [info.filename, ruta_zip, None, info.file_size]
        except zipfile.BadZipFile:
            print(f"  aviso: {z} no se pudo abrir, se omite")

    # Si ya esta extraido en Downloads, se usa de ahi y no se toca el ZIP.
    if os.path.isdir(YA_EXTRAIDOS):
        for f in os.listdir(YA_EXTRAIDOS):
            if f.lower().endswith(".mp4") and "Fundamentos" in f:
                p = os.path.join(YA_EXTRAIDOS, f)
                if f in items:
                    items[f][2] = p
                else:
                    items[f] = [f, None, p, os.path.getsize(p)]
    return items


def pendientes(items):
    out = []
    for base, (miembro, ruta_zip, suelto, tam) in items.items():
        destino = os.path.join(DESTINO, limpiar(base) + ".md")
        if not os.path.exists(destino):
            out.append((base, miembro, ruta_zip, suelto, tam))

    def clave(x):
        base = x[0]
        for i, p in enumerate(PRIORIDAD):
            if base.startswith(p):
                return (0, i, 0)
        return (1, 0, x[4])          # el resto: de menor a mayor

    return sorted(out, key=clave)


def extraer(miembro, ruta_zip, base):
    os.makedirs(TRABAJO, exist_ok=True)
    salida = os.path.join(TRABAJO, base)
    if os.path.exists(salida):
        return salida
    print(f"  extrayendo de {os.path.basename(ruta_zip)}...", flush=True)
    with zipfile.ZipFile(ruta_zip) as zf, open(salida, "wb") as f:
        with zf.open(miembro) as src:
            shutil.copyfileobj(src, f, length=8 * 1024 * 1024)
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--listar", action="store_true", help="solo mostrar el estado")
    ap.add_argument("--modelo", default="small",
                    help="small (por defecto, consistente con las ya hechas) | medium | large-v3")
    ap.add_argument("--esperar", metavar="NOMBRE",
                    help="esperar a que exista el .md de NOMBRE antes de empezar, "
                         "para no competir por CPU con otra transcripcion en curso")
    a = ap.parse_args()

    items = inventario()
    pend = pendientes(items)

    print(f"{len(items)} grabaciones · {len(items)-len(pend)} transcritas · "
          f"{len(pend)} pendientes\n")
    for i, (base, _, ruta_zip, suelto, tam) in enumerate(pend, 1):
        origen = "ya extraido" if suelto else os.path.basename(ruta_zip or "?")
        print(f"  {i:2}. {tam/1048576:7.1f} MB  [{origen[:28]:>28}]  {base}")

    if a.listar or not pend:
        return

    if a.esperar:
        md = os.path.join(DESTINO, limpiar(a.esperar) + ".md")
        t0 = time.time()
        while not os.path.exists(md) and time.time() - t0 < 4 * 3600:
            print(f"\r  esperando a que termine {a.esperar} "
                  f"({hhmmss(time.time()-t0)})...", end="", flush=True)
            time.sleep(60)
        print()

    print(f"\n{'#'*70}\nCOLA: {len(pend)} grabaciones con modelo '{a.modelo}'\n{'#'*70}")
    t0 = time.time()
    hechas, fallidas = 0, []

    for i, (base, miembro, ruta_zip, suelto, tam) in enumerate(pend, 1):
        print(f"\n[{i}/{len(pend)}] {base}  ({tam/1048576:.1f} MB)", flush=True)
        temporal = None
        try:
            if suelto:
                ruta = suelto
            else:
                ruta = temporal = extraer(miembro, ruta_zip, base)
            transcribir(ruta, modelo=a.modelo)
            hechas += 1
        except KeyboardInterrupt:
            print("\ninterrumpido. Vuelve a lanzarlo y retoma aqui.")
            break
        except Exception as e:
            print(f"  FALLO: {type(e).__name__}: {e}")
            fallidas.append(base)
        finally:
            if temporal and os.path.exists(temporal):
                os.remove(temporal)      # el ZIP sigue siendo la fuente

    if os.path.isdir(TRABAJO) and not os.listdir(TRABAJO):
        os.rmdir(TRABAJO)

    print(f"\n{'#'*70}")
    print(f"{hechas} transcritas · {len(fallidas)} fallidas · "
          f"tiempo total {hhmmss(time.time()-t0)}")
    for f in fallidas:
        print(f"  fallo: {f}")
    print("\nAhora actualiza el indice:")
    print("  python 03_CODIGO/integrar_clase.py --sin-subir")


if __name__ == "__main__":
    main()
