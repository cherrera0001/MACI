"""
Prueba de comportamiento del núcleo v2 en un navegador real y sin red (REQ-TUT-012…014, 017).
probar_visuales_offline.py comprueba que nada falle al usarlo todo; esto comprueba que los
candados hagan lo que prometen sobre 20_llm.html.

USO
  uv run --with playwright python 03_SCRIPTS/probar_nucleo_v2.py
"""
import os
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probar_visuales_offline import VISUAL, lanzar  # noqa: E402

PAGINA = os.path.join(VISUAL, "20_llm.html")


def comprobar(p):
    fallos = []

    def exige(cond, que):
        if not cond:
            fallos.append(que)

    errores = []
    p.on("pageerror", lambda e: errores.append(str(e)))
    p.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())
    p.goto("file:///" + PAGINA.replace("\\", "/"))

    exige(p.is_disabled("#temp"), "la temperatura no arranca bloqueada")
    exige(not p.eval_on_selector("#n2-temp", "d => d.open"), "el nivel 2 arranca abierto")
    caja = '[data-predice="p1"]'
    p.click(f"{caja} button")
    exige(p.is_disabled("#temp"), "una prediccion vacia desbloquea")
    p.fill(f"{caja} textarea", "se achica y las raras suben")
    p.click(f"{caja} button")
    exige(p.is_enabled("#temp"), "registrar la prediccion no desbloquea")

    p.eval_on_selector('details.resp[data-intento="q2"]', "d => { d.open = true; }")
    p.wait_for_timeout(50)
    exige(not p.eval_on_selector('details.resp[data-intento="q2"]', "d => d.open"),
          "la respuesta se abre sin intento")
    p.fill('.intento[data-intento="q2"] textarea', "baja en boletas, alta en titulos")
    p.dispatch_event('.intento[data-intento="q2"] textarea', "change")
    p.eval_on_selector('details.resp[data-intento="q2"]', "d => { d.open = true; }")
    p.wait_for_timeout(50)
    exige(p.eval_on_selector('details.resp[data-intento="q2"]', "d => d.open"),
          "con intento la respuesta no se abre")

    p.click('button.pedir[data-intento="q1"]')
    exige(p.eval_on_selector('details.resp[data-intento="q1"]', "d => d.open"),
          "'dame la respuesta' no la abre (G11)")

    p.fill('[data-predice="p2"] textarea', "a perro, porque es el que ladra")
    p.click('[data-predice="p2"] button')
    p.click("#bVerAt")
    p.hover('#toksAt button[data-enlace="tok-1"]')
    exige(p.eval_on_selector('#barrasAt [data-enlace="tok-1"]', "e => e.classList.contains('enlazado')"),
          "el hover no enlaza el token con su barra")

    p.fill("#temp", "2")
    p.dispatch_event("#temp", "change")
    export = p.inner_text("#datito-export")
    for marca in ("DATITO-EVENTOS v1", '"prediccion"', '"intento"', '"pidio_respuesta"', '"observacion"'):
        exige(marca in export, f"la exportacion no trae {marca}")

    p.reload()
    exige(p.is_enabled("#temp"), "la prediccion no sobrevive a recargar")
    exige(not errores, f"errores JS: {errores[:2]}")
    return fallos


def main():
    with sync_playwright() as pw:
        nav = lanzar(pw)
        pag = nav.new_context(viewport={"width": 1280, "height": 900}).new_page()
        fallos = comprobar(pag)
        nav.close()
    for f in fallos:
        print(f"[FALLO] {f}")
    print(f"nucleo v2 en 20_llm.html: {'ok' if not fallos else f'{len(fallos)} fallos'}")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
