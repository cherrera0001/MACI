#!/usr/bin/env python3
"""start.py — doble clic y a chatear con tu Datito.

1. Verifica Python 3.12+  2. Crea el venv e instala dependencias (offline si
hay wheels/)  3. Construye el indice del curso si falta  4. Levanta el
servidor y abre el navegador en http://localhost:8377
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MOTOR = RAIZ / "15_TERMINITO"
VENV = MOTOR / ".venv"
DEPENDENCIAS = ["pyyaml", "jinja2", "markdown", "pypdf"]
PUERTO = 8377


def log(msg: str):
    print(f"[start] {msg}", flush=True)


def falla(msg: str):
    print(f"\n[start] ERROR: {msg}\n")
    input("Enter para cerrar…")
    raise SystemExit(1)


def verificar_python():
    if sys.version_info < (3, 12):
        falla(f"necesitas Python 3.12 o superior (tienes {sys.version.split()[0]}). "
              "Descargalo de https://python.org")


def venv_python() -> Path:
    return VENV / ("Scripts" if os.name == "nt" else "bin") / ("python.exe" if os.name == "nt" else "python")


def crear_venv():
    if venv_python().exists():
        return
    log("creando entorno virtual (solo la primera vez)…")
    subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
    # hacer visible el paquete datito via .pth (sin pip install -e)
    proc = subprocess.run(
        [str(venv_python()), "-c", "import site; print(site.getsitepackages()[0])"],
        capture_output=True, text=True, check=True)
    site_packages = Path(proc.stdout.strip().splitlines()[-1])
    (site_packages / "datito.pth").write_text(str(MOTOR / "src"), encoding="utf-8")


def instalar_dependencias():
    proc = subprocess.run(
        [str(venv_python()), "-c", "import yaml, jinja2, markdown, pypdf"],
        capture_output=True)
    if proc.returncode == 0:
        return
    log("instalando dependencias (offline desde wheels/ si es posible)…")
    wheels = RAIZ / "wheels"
    offline = wheels.exists()
    cmd = [str(venv_python()), "-m", "pip", "install"]
    if offline:
        cmd += ["--no-index", "--find-links", str(wheels)]
    cmd += DEPENDENCIAS
    r = subprocess.run(cmd)
    if r.returncode != 0 and offline:
        log("las wheels no sirvieron para tu plataforma; reintento con conexion…")
        subprocess.run([str(venv_python()), "-m", "pip", "install"] + DEPENDENCIAS,
                       check=True)


def construir_curso_si_falta():
    indice = MOTOR / "cursos" / "fcd" / ".indice"
    if indice.exists():
        return
    log("construyendo el indice del curso (solo la primera vez, ~1 min)…")
    subprocess.run([str(venv_python()), "-m", "datito.cli", "build", "fcd"],
                   cwd=str(MOTOR), check=True)


def _puerto_ocupado(puerto: int) -> bool:
    import socket
    with socket.socket() as s:
        try:
            s.connect(("127.0.0.1", puerto))
            return True
        except OSError:
            return False


def main():
    verificar_python()
    try:
        crear_venv()
        instalar_dependencias()
        construir_curso_si_falta()
    except subprocess.CalledProcessError as e:
        falla(f"fallo la preparacion (codigo {e.returncode}). "
              "Revisa que tengas conexion la primera vez o que exista wheels/.")
    if _puerto_ocupado(PUERTO):
        log(f"ya hay un Datito corriendo en {PUERTO}: abro el navegador.")
        webbrowser.open(f"http://localhost:{PUERTO}")
        return
    log(f"levantando Datito en http://localhost:{PUERTO} …")
    servidor = subprocess.Popen(
        [str(venv_python()), "-m", "datito.servidor", "--puerto", str(PUERTO)],
        cwd=str(MOTOR))
    time.sleep(1.2)
    webbrowser.open(f"http://localhost:{PUERTO}")
    print("\nDatito esta corriendo. Deja esta ventana abierta; cierrala para salir.\n")
    try:
        servidor.wait()
    except KeyboardInterrupt:
        servidor.terminate()


if __name__ == "__main__":
    main()
