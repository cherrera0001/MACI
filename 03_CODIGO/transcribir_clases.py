"""
Transcribe las clases grabadas a texto, en local y sin GPU.

POR QUE LOCAL Y NO SUBIR EL VIDEO
NotebookLM acepta audio y video como fuente, pero entonces la transcripcion vive
en sus servidores: no se puede versionar, ni buscar sin conexion, ni leer en una
prueba. Transcribir aqui produce un .md de unos 60 KB que entra en el
repositorio, se busca con grep, se lee offline y ademas se sube al cuaderno
-mucho mas liviano que el video-.

MODELO
faster-whisper con cuantizacion int8, que corre en CPU. No hace falta ffmpeg:
PyAV, que viene incluido, decodifica el MP4 directamente.

  small    ~2 GB RAM   mas rapido, calidad suficiente para buscar temas
  medium   ~5 GB RAM   equilibrio recomendado para estudiar        <- por defecto
  large-v3 ~10 GB RAM  mejor calidad, bastante mas lento en CPU

Orden de magnitud en esta maquina: una clase de 90 minutos con 'medium' tarda
entre 30 y 60 minutos. Conviene dejarlo corriendo en segundo plano.

USO
  uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --listar
  uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py "<ruta.mp4>"
  uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --todas
"""
import argparse
import glob
import os
import re
import sys
import time
from datetime import timedelta

ORIGEN = r"C:\Users\herre\Downloads"
DESTINO = r"F:\MACI\09_CLASES\transcripciones"
PATRON = "*Fundamentos*.mp4"


def limpiar(nombre):
    n = os.path.splitext(os.path.basename(nombre))[0]
    n = re.sub(r"[^\w\s\-]", "_", n, flags=re.UNICODE)
    return re.sub(r"[\s_]+", "_", n).strip("_")


def hhmmss(segundos):
    return str(timedelta(seconds=int(segundos)))


def listar():
    rutas = sorted(glob.glob(os.path.join(ORIGEN, PATRON)))
    if not rutas:
        print(f"Sin coincidencias de {PATRON} en {ORIGEN}")
        return []
    print(f"{len(rutas)} grabaciones:\n")
    for i, r in enumerate(rutas, 1):
        mb = os.path.getsize(r) / 1048576
        destino = os.path.join(DESTINO, limpiar(r) + ".md")
        estado = "ya transcrita" if os.path.exists(destino) else "pendiente"
        print(f"  {i}. [{estado:>13}] {mb:7.1f} MB  {os.path.basename(r)}")
    return rutas


def transcribir(ruta, modelo="medium"):
    from faster_whisper import WhisperModel

    destino = os.path.join(DESTINO, limpiar(ruta) + ".md")
    if os.path.exists(destino):
        print(f"ya existe, se omite: {os.path.basename(destino)}")
        return destino

    os.makedirs(DESTINO, exist_ok=True)
    print(f"\n{'='*70}\n{os.path.basename(ruta)}\nmodelo: {modelo} · int8 · CPU")
    print("cargando modelo (la primera vez lo descarga)...", flush=True)

    t0 = time.time()
    m = WhisperModel(modelo, device="cpu", compute_type="int8")

    segmentos, info = m.transcribe(
        ruta,
        language="es",
        vad_filter=True,               # recorta silencios: acelera bastante
        vad_parameters=dict(min_silence_duration_ms=700),
        beam_size=5,
    )

    print(f"duracion detectada: {hhmmss(info.duration)}", flush=True)

    lineas = [
        f"# {os.path.basename(ruta)}",
        "",
        "> Transcripcion automatica con faster-whisper. **Puede contener errores**,",
        "> sobre todo en terminos tecnicos y nombres propios. Contrastar con el",
        "> material del curso antes de citarla como fuente.",
        "",
        f"- Duracion: {hhmmss(info.duration)}",
        f"- Modelo: `{modelo}` · idioma detectado: `{info.language}` "
        f"(confianza {info.language_probability:.2f})",
        "",
        "---",
        "",
    ]

    texto_plano = []
    for s in segmentos:
        marca = hhmmss(s.start)
        t = s.text.strip()
        lineas.append(f"**[{marca}]** {t}")
        lineas.append("")
        texto_plano.append(t)
        transcurrido = time.time() - t0
        avance = s.end / info.duration * 100
        print(f"\r  {avance:5.1f}%  ({hhmmss(s.end)}/{hhmmss(info.duration)}) "
              f"· {hhmmss(transcurrido)} transcurridos", end="", flush=True)

    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lineas))

    plano = destino.replace(".md", "_plano.txt")
    with open(plano, "w", encoding="utf-8", newline="\n") as f:
        f.write(" ".join(texto_plano))

    print(f"\n-> {destino}")
    print(f"-> {plano}")
    print(f"tiempo total: {hhmmss(time.time() - t0)}")
    return destino


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ruta", nargs="?", help="MP4 concreto a transcribir")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--modelo", default="medium",
                    choices=["tiny", "base", "small", "medium", "large-v3"])
    a = ap.parse_args()

    if a.listar:
        listar()
        return

    if a.todas:
        for r in listar():
            transcribir(r, a.modelo)
        return

    if not a.ruta:
        listar()
        print("\nIndica un archivo, o usa --todas")
        sys.exit(1)

    transcribir(a.ruta, a.modelo)


if __name__ == "__main__":
    main()
