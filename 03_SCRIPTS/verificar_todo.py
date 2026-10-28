"""Una sola verificación antes de decir «listo». Sale con 1 si algo falla.

Cada comprobación existe porque ese error ya ocurrió (ver la lección única en
la memoria de Claude y 00_INICIO/CLAUDE.md, «Antes de decir listo»).

  python 03_SCRIPTS/verificar_todo.py              # disco: generador, contrato, citas, tests
  python 03_SCRIPTS/verificar_todo.py --navegador  # además Edge real a 390 y 1280 px
  python 03_SCRIPTS/verificar_todo.py --en-linea   # además recorre https://maci.c4a.cl
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from urllib.parse import urldefrag, urljoin, urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}


def correr(cmd):
    r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def generador():
    code, out = correr([sys.executable, "03_SCRIPTS/construir_navegacion.py", "--revisar"])
    pend = [l.strip() for l in out.splitlines() if re.search(r"\b(actualizado|inyectado|cambiaria|actualizadas)\b", l)]
    if pend or code:
        return False, f"{len(pend)} páginas desactualizadas: correr construir_navegacion.py"
    for script in ("sincronizar_nucleo.py", "generar_llm_lab.py", "generar_pipeline_lab.py"):
        code, out = correr([sys.executable, f"03_SCRIPTS/{script}", "--revisar"])
        if code:
            return False, f"visuales v2 desactualizados: correr 03_SCRIPTS/{script} {out.strip()[:80]}"
    return True, "sin pendientes (navegación, núcleo v2, datos de los labs LLM y pipeline)"


def contrato():
    code, out = correr([sys.executable, "03_SCRIPTS/verificar_contrato.py"])
    ultima = next((l for l in reversed(out.splitlines()) if "fallos" in l), out.strip()[-120:])
    return code == 0 and " 0 fallos" in ultima, ultima.strip()


def citas():
    code, out = correr([sys.executable, "03_SCRIPTS/verificar_visuales.py"])
    ultima = next((l for l in reversed(out.splitlines()) if "fallos" in l), "")
    return code == 0 and ultima.startswith("0 fallos"), ultima.strip()


def rutas_documentales():
    code, out = correr([sys.executable, "03_SCRIPTS/auditar_drift_documental.py"])
    ultima = next((l for l in reversed(out.splitlines()) if l.startswith(("OK:", "FALTAN"))), "")
    return code == 0, ultima.strip()


def tests():
    code, out = correr([sys.executable, "-m", "unittest", "discover", "-s", "04_CODIGO", "-p", "test_*.py"])
    ran = next((l for l in out.splitlines() if l.startswith("Ran ")), "")
    fallidos = re.findall(r"^(?:FAIL|ERROR): (\S+)", out, flags=re.M)
    return code == 0, ran + (" · OK" if code == 0 else f" · fallan: {', '.join(fallidos[:4])}")


# Sin sudo en WSL: libnss3/libnspr4/libasound extraidas de sus .deb (apt-get download + dpkg-deb -x)
LIBS_LOCALES = os.path.expanduser("~/.local/lib/chromium-deps/root/usr/lib/x86_64-linux-gnu")


def navegador():
    if not shutil.which("uv"):
        return False, "falta uv (uv run --with playwright …)"
    if os.path.isdir(LIBS_LOCALES):
        ENV["LD_LIBRARY_PATH"] = LIBS_LOCALES + os.pathsep + ENV.get("LD_LIBRARY_PATH", "")
    code, out = correr(["uv", "run", "-q", "--with", "playwright", "python", "03_SCRIPTS/probar_visuales_offline.py"])
    ultima = next((l for l in reversed(out.splitlines()) if "paginas" in l), out.strip()[-160:])
    code2, out2 = correr(["uv", "run", "-q", "--with", "playwright", "python", "03_SCRIPTS/probar_nucleo_v2.py"])
    nucleo = next((l for l in reversed(out2.splitlines()) if "nucleo v2" in l), out2.strip()[-120:])
    return code == 0 and code2 == 0, f"{ultima.strip()} · {nucleo.strip()}"


def en_linea():
    base = "https://maci.c4a.cl"

    def get(u):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "verificar-todo"}), timeout=30)
            return r.status, r.geturl(), r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return e.code, u, ""

    s, inicio, _ = get(base + "/")
    cola, vistos, paginas, malos = [inicio], set(), {}, []
    while cola:
        u = cola.pop()
        if u in vistos:
            continue
        vistos.add(u)
        s, _, t = get(u)
        if s != 200:
            malos.append(f"{s} {u}")
            continue
        if u.endswith(".html"):
            paginas[u] = t
            for h in re.findall(r'(?:href|src)="([^"]*)"', t):
                if h and not re.match(r"(mailto:|javascript:|data:)", h) and "${" not in h:
                    a = urldefrag(urljoin(u, h))[0]
                    if urlparse(a).netloc == urlparse(base).netloc and a not in vistos:
                        cola.append(a)
    anclas = []
    for u, t in paginas.items():
        for h in re.findall(r'href="([^"]*#[^"]+)"', t):
            destino, frag = urldefrag(urljoin(u, h))
            html = paginas.get(destino)
            if html is not None and f'id="{frag}"' not in html:
                anclas.append(f"{u} → {h}")
    privados = [p for p in ("/07_DATITO/progreso.yaml", "/07_DATITO/datito.config.yaml", "/README.md")
                if get(base + p)[0] == 200]
    ok = not malos and not anclas and not privados
    return ok, (f"{len(paginas)} páginas · {len(vistos)} recursos · rotos {len(malos)} · anclas rotas {len(anclas)}"
                f" · privados expuestos {len(privados)}" + (f" · {malos[:2]}{privados[:2]}" if not ok else ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--navegador", action="store_true")
    ap.add_argument("--en-linea", action="store_true")
    a = ap.parse_args()
    pasos = [("generador idempotente", generador), ("contrato de Datito", contrato),
             ("citas y enlaces de visuales", citas), ("rutas documentales", rutas_documentales),
             ("tests (incluye sitio publicado)", tests)]
    if a.navegador:
        pasos.append(("Edge real 390/1280 px", navegador))
    if a.en_linea:
        pasos.append(("maci.c4a.cl en vivo", en_linea))
    malos = 0
    for nombre, f in pasos:
        ok, detalle = f()
        malos += not ok
        print(f"[{'  ok  ' if ok else 'FALLO '}] {nombre:32} {detalle}")
    print("LISTO: todo verificado" if not malos else f"NO ESTÁ LISTO: {malos} comprobación(es) fallan")
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    main()
