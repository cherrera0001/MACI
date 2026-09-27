"""
Abre cada visual de 07_DATITO/01_CONCEPTOS/visual/ en un navegador real SIN RED y lo usa:
mueve todos los controles, pulsa los botones y abre las soluciones. Informa
errores de JavaScript y cualquier intento de pedir algo fuera del disco.

Es la prueba de G9: «los artefactos funcionan sin conexión: su prueba es sin
Internet». verificar_visuales.py revisa el texto; esto revisa el comportamiento.

REQUISITOS
  Microsoft Edge instalado (se usa el del sistema, no se descarga nada) y el
  paquete playwright, que uv trae al vuelo:

USO
  uv run --with playwright python 03_SCRIPTS/probar_visuales_offline.py
  uv run --with playwright python 03_SCRIPTS/probar_visuales_offline.py 03_eda.html
  uv run --with playwright python 03_SCRIPTS/probar_visuales_offline.py --capturas=DIR  # guarda PNG a 390 y 1280 px
"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VISUAL = os.path.join(RAIZ, "07_DATITO", "01_CONCEPTOS", "visual")

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


DESBORDE = r"""
() => {
  const w = window.innerWidth, exceso = document.documentElement.scrollWidth - w;
  const culpables = [];
  if (exceso > 1) {
    for (const el of document.body.querySelectorAll('*')) {
      const r = el.getBoundingClientRect();
      if (r.right > w + 1 && r.width > 0 && getComputedStyle(el).position !== 'fixed') {
        let dentro = false;
        for (let p = el.parentElement; p; p = p.parentElement) {
          const o = getComputedStyle(p).overflowX;
          if (o === 'auto' || o === 'scroll' || o === 'hidden') { dentro = true; break; }
        }
        if (!dentro) culpables.push(el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : ''));
      }
      if (culpables.length >= 3) break;
    }
  }
  return [exceso, culpables];
}
"""
ANCHOS = (390, 1280)


def paginas_del_curso():
    """Todas las paginas del curso: visual/ (sin la plantilla), ejercicios y la clase 5."""
    base = [p for p in glob.glob(os.path.join(VISUAL, "*.html")) if not os.path.basename(p).startswith("_")]
    extra = glob.glob(os.path.join(RAIZ, "07_DATITO", "04_EJERCICIOS", "*.html"))
    extra.append(os.path.join(RAIZ, "07_DATITO", "02_REFERENCIA", "clase6_regresion.html"))
    return sorted(base) + sorted(extra)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--capturas=")]
    capturas = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--capturas=")), None)
    rutas = [a if os.path.isabs(a) else os.path.join(VISUAL, a) for a in args] or paginas_del_curso()
    malos = 0
    with sync_playwright() as p:
        nav = p.chromium.launch(channel="msedge", headless=True)
        ctx = nav.new_context(offline=True)
        for ruta in rutas:
            n = os.path.basename(ruta)
            if n == "index.html":  # redireccion a la portada
                continue
            pagina = ctx.new_page()
            try:
                errores, externas, acciones = probar(pagina, ruta)
            except Exception as e:  # la pagina ni siquiera cargo
                errores, externas, acciones = [f"no cargo: {e}"], [], 0
            pagina.close()
            desbordes = []
            for ancho in ANCHOS:
                c = nav.new_context(offline=True, viewport={"width": ancho, "height": 900})
                pg = c.new_page()
                pg.goto("file:///" + ruta.replace("\\", "/"), wait_until="load")
                pg.wait_for_timeout(200)
                exceso, culpables = pg.evaluate(DESBORDE)
                if capturas:
                    os.makedirs(capturas, exist_ok=True)
                    pg.screenshot(path=os.path.join(capturas, f"{n[:-5]}_{ancho}.png"))
                if exceso > 1:
                    desbordes.append(f"{ancho}px: +{exceso}px ({', '.join(culpables) or '?'})")
                c.close()
            estado = "ok" if not errores and not externas and not desbordes else "FALLO"
            malos += estado != "ok"
            print(f"[{estado:>5}] {n:34} {acciones:4} interacciones · "
                  f"{len(errores)} errores JS · {len(externas)} pedidos externos · "
                  f"{'sin desborde' if not desbordes else 'DESBORDE'}")
            for e in errores[:5]:
                print(f"          {e[:160]}")
            for u in externas[:3]:
                print(f"          externo: {u[:120]}")
            for d in desbordes:
                print(f"          desborde {d}")
        nav.close()
    total = len([r for r in rutas if os.path.basename(r) != "index.html"])
    print(f"{total - malos} de {total} paginas sin errores, sin red y sin desborde a {ANCHOS[0]} y {ANCHOS[1]} px")
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    main()
