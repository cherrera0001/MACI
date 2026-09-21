"""
Abre cada visual de 07_DATITO/visual/ en un navegador real SIN RED y lo usa:
mueve todos los controles, pulsa los botones y abre las soluciones. Informa
errores de JavaScript y cualquier intento de pedir algo fuera del disco.

Es la prueba de G9: «los artefactos funcionan sin conexión: su prueba es sin
Internet». verificar_visuales.py revisa el texto; esto revisa el comportamiento.

REQUISITOS
  Microsoft Edge instalado (se usa el del sistema, no se descarga nada) y el
  paquete playwright, que uv trae al vuelo:

USO
  uv run --with playwright python 03_CODIGO/probar_visuales_offline.py
  uv run --with playwright python 03_CODIGO/probar_visuales_offline.py eda.html
"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VISUAL = os.path.join(RAIZ, "07_DATITO", "visual")

USAR = r"""
() => {
  const acciones = [];
  document.querySelectorAll('details').forEach(d => d.open = true);
  document.querySelectorAll('input[type=range]').forEach(r => {
    for (const v of [r.min || 0, r.max || 100, ((+r.min || 0) + (+r.max || 100)) / 2]) {
      r.value = v;
      r.dispatchEvent(new Event('input', {bubbles: true}));
      r.dispatchEvent(new Event('change', {bubbles: true}));
    }
    acciones.push('range');
  });
  document.querySelectorAll('select').forEach(s => {
    for (const o of s.options) { s.value = o.value; s.dispatchEvent(new Event('change', {bubbles: true})); }
    acciones.push('select');
  });
  document.querySelectorAll('input[type=checkbox], input[type=radio]').forEach(c => {
    c.click(); acciones.push('check');
  });
  document.querySelectorAll('button').forEach(b => { try { b.click(); acciones.push('button'); } catch (e) {} });
  return acciones.length;
}
"""


def probar(pagina, ruta):
    errores, externas = [], []
    pagina.on("pageerror", lambda e: errores.append(f"excepcion: {e}"))
    pagina.on("console", lambda m: errores.append(f"consola: {m.text}") if m.type == "error" else None)
    pagina.route("**/*", lambda r: (r.continue_() if r.request.url.startswith("file:")
                                   else (externas.append(r.request.url), r.abort())))
    pagina.goto("file:///" + ruta.replace("\\", "/"), wait_until="load")
    pagina.wait_for_timeout(300)
    n = pagina.evaluate(USAR)
    pagina.wait_for_timeout(300)
    return errores, externas, n


def main():
    nombres = sys.argv[1:] or sorted(os.path.basename(p) for p in glob.glob(os.path.join(VISUAL, "*.html")))
    malos = 0
    with sync_playwright() as p:
        nav = p.chromium.launch(channel="msedge", headless=True)
        ctx = nav.new_context(offline=True)
        for n in nombres:
            pagina = ctx.new_page()
            try:
                errores, externas, acciones = probar(pagina, os.path.join(VISUAL, n))
            except Exception as e:  # la pagina ni siquiera cargo
                errores, externas, acciones = [f"no cargo: {e}"], [], 0
            pagina.close()
            estado = "ok" if not errores and not externas else "FALLO"
            malos += estado != "ok"
            print(f"[{estado:>5}] {n:34} {acciones:4} interacciones · "
                  f"{len(errores)} errores JS · {len(externas)} pedidos externos")
            for e in errores[:5]:
                print(f"          {e[:160]}")
            for u in externas[:3]:
                print(f"          externo: {u[:120]}")
        nav.close()
    print(f"{len(nombres) - malos} de {len(nombres)} visuales sin errores y sin red")
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    main()
