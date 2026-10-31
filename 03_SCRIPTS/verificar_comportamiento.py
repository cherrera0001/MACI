#!/usr/bin/env python3
"""Gate de comportamiento del paquete (T-8.3.1 / H-8.3).

Corre una sonda conductual contra el zip construido y la compara con la
referencia almacenada en 04_CODIGO/harness_escenarios/baseline/comportamiento.yaml.

La sonda captura LO QUE EL ESTUDIANTE VIVE (no tiempos ni pids):
  1. demo socrático: estado_final, violaciones, métricas de sesión;
  2. flujo de creación real por HTTP: crear curso → subir material →
     componentes → construir → panel/grafo y evaluación procedural.

Uso:
  python 03_SCRIPTS/verificar_comportamiento.py --guardar   # regenera la referencia
  python 03_SCRIPTS/verificar_comportamiento.py             # compara (exit 0/1)

REA completo queda como mejora de desarrollo (D-8.1, opción híbrida): esta
sonda es la traza ligera que corre en cualquier CI sin dependencias.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import threading
import urllib.request
import zipfile
from http.server import ThreadingHTTPServer
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ZIP = RAIZ / "dist" / "datito.zip"
BASELINE = RAIZ / "04_CODIGO" / "harness_escenarios" / "baseline" / "comportamiento.yaml"
MATERIAL = ("# Sobreajuste\n\nEl sobreajuste memoriza el entrenamiento. "
            "La brecha entre entrenamiento y prueba diagnostica el sobreajuste.\n\n"
            "# Generalizacion\n\nLa generalizacion mide el rendimiento en datos nuevos.\n")

COMPONENTES = {
    "rol_dominio": "Tutor experto", "mision": "Acompanar", "funciones": "Explicar",
    "estilo_ensenanza": "Socratico", "contexto_curso": "Curso de prueba",
    "estilo_aprendizaje": "Paso a paso", "restricciones": "No inventar",
    "relacion_temporal": "Un semestre",
}

ITEM_PROTOCOLO = {
    "id": "d1", "conceptos": ["sobreajuste", "generalizacion"],
    "pregunta": "brecha antes que etiqueta", "criterios": ["orden"],
    "protocolo": [{"evento": "brecha", "antes_de": ["etiquetar"]}]}

SCRIPT_BIEN = 'print("#@brecha")\nprint("#@etiquetar")\n'


def _http(base: str, metodo: str, ruta: str, datos=None) -> dict:
    req = urllib.request.Request(
        base + ruta, data=json.dumps(datos).encode() if datos is not None else None,
        headers={"Content-Type": "application/json"}, method=metodo)
    with urllib.request.urlopen(req, timeout=60) as r:
        cuerpo = r.read().decode()
    try:
        return json.loads(cuerpo)
    except json.JSONDecodeError:
        raise RuntimeError(
            f"{metodo} {ruta} respondió un cuerpo no-JSON: {cuerpo[:200]!r}") from None


def sonda() -> dict:
    if not ZIP.exists():
        subprocess.run([sys.executable, str(RAIZ / "15_TERMINITO" / "scripts" /
                                            "build_paquete.py")], check=True)
    tmp = tempfile.TemporaryDirectory(prefix="datito-comp-")
    with zipfile.ZipFile(ZIP) as z:
        z.extractall(tmp.name)
    motor = Path(tmp.name) / "15_TERMINITO"
    env = {"PYTHONPATH": str(motor / "src")}

    def correr(*args, **kw):
        return subprocess.run([sys.executable, *args], cwd=motor, env=env,
                              capture_output=True, text=True, timeout=180, **kw)

    # 1) demo socrático
    proc = correr("-m", "datito.cli", "demo", "--json")
    if proc.returncode != 0 or not proc.stdout.strip():
        raise RuntimeError(
            f"el demo del zip falló (exit {proc.returncode}); stderr del "
            f"proceso: {proc.stderr.strip()[:400]}")
    demo = json.loads(proc.stdout)

    # 2) flujo de creación por HTTP con el servidor real del zip
    sys.path.insert(0, str(motor / "src"))
    try:
        from datito import servidor  # del ZIP, no del repo
        server = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{server.server_address[1]}"
        _http(base, "POST", "/api/cursos", {"slug": "sonda", "nombre": "Sonda"})
        req = urllib.request.Request(
            base + "/api/cursos/sonda/materiales?nombre=clase.md",
            data=MATERIAL.encode(), method="PUT")
        urllib.request.urlopen(req, timeout=30).read()
        for k, v in COMPONENTES.items():
            _http(base, "POST", "/api/cursos/sonda/componentes", {k: v})
        construido = _http(base, "POST", "/api/cursos/sonda/construir")
        grafo = _http(base, "GET", "/api/cursos/sonda/grafo?mapa=1")
        eval_ok = _http(base, "POST", "/api/cursos/sonda/evaluaciones",
                        {"id": "d1", **ITEM_PROTOCOLO})
        eval_res = _http(base, "POST", "/api/cursos/sonda/evaluacion",
                         {"item_id": "d1", "codigo": SCRIPT_BIEN})
        server.shutdown()
        flujo = {
            "fuentes": construido["fuentes"],
            "fragmentos": construido["fragmentos"],
            "cadenas": len(grafo["cadenas"]),
            "nodos": sum(len(c["nodos"]) for c in grafo["cadenas"]),
            "item_guardado": eval_ok["guardado"],
            "eval_procedural": eval_res["resultado"],
            "eval_eventos": eval_res["traza"]["eventos"],
        }
    finally:
        sys.path.pop(0)

    return {
        "demo": {"estado_final": demo["estado_final"],
                 "violaciones": len(demo["violaciones_protocolo"]),
                 "esperas": demo["metricas"]["preguntas_con_espera_real"]},
        "flujo": flujo,
    }


def comparar(sonda_actual: dict, referencia: dict) -> list[str]:
    diffs = []
    for seccion in ("demo", "flujo"):
        for clave, valor in referencia[seccion].items():
            actual = sonda_actual[seccion].get(clave)
            if actual != valor:
                diffs.append(f"{seccion}.{clave}: referencia={valor!r} actual={actual!r}")
    return diffs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--guardar", action="store_true", help="regenera la referencia")
    args = ap.parse_args()

    import yaml
    actual = sonda()
    if args.guardar:
        BASELINE.parent.mkdir(parents=True, exist_ok=True)
        BASELINE.write_text(yaml.safe_dump(actual, allow_unicode=True, sort_keys=False),
                            encoding="utf-8")
        print(f"referencia guardada en {BASELINE}")
        return 0
    if not BASELINE.exists():
        sys.exit(f"no hay referencia: corre con --guardar primero ({BASELINE})")
    referencia = yaml.safe_load(BASELINE.read_text(encoding="utf-8"))
    diffs = comparar(actual, referencia)
    if diffs:
        print("CAMBIO DE COMPORTAMIENTO respecto a la referencia:")
        for d in diffs:
            print(f"  ✗ {d}")
        return 1
    print("comportamiento igual a la referencia (conducta, no cosmética)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
