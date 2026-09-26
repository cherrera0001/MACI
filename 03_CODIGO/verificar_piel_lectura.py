#!/usr/bin/env python3
"""Comprueba la piel renderizada de un visual local, sin acceso a red.

Complementa datito_loop_eval: un marcador no demuestra que el CSS se aplique.
Requiere Playwright y Chromium instalados. No modifica el HTML.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def verify(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    live = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    failures = []
    if live.count(":root") != 1:
        failures.append("Debe haber un solo :root fuera de comentarios")
    if not re.search(r"<head>.*?<title>.+?</title>.*?</head>\s*<body", live, re.S):
        failures.append("Head/title/body incompletos o ocultos dentro de un comentario")
    for placeholder in ("TÍTULO DEL CONCEPTO", "fórmula = aquí", "Paso 1…", "Paso 2…"):
        if placeholder in live:
            failures.append(f"Placeholder: {placeholder}")
    if re.search(r"#667eea|#764ba2", live, re.I):
        failures.append("Color ajeno a la piel canónica")
    views = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(offline=True)
        page = context.new_page()
        errors = []
        remote = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda request: remote.append(request.url)
                if request.url.startswith(("http://", "https://")) else None)
        for width in (1280, 390):
            page.set_viewport_size({"width": width, "height": 900})
            page.goto(path.resolve().as_uri(), wait_until="load")
            data = page.evaluate("""() => {
                const style = e => getComputedStyle(e);
                const root = style(document.documentElement);
                const body = style(document.body);
                const main = document.querySelector('main');
                const failures = [];
                const check = (ok, label) => { if (!ok) failures.push(label); };
                check(document.querySelectorAll('h1').length === 1, 'Un solo h1');
                check(document.querySelectorAll('main').length === 1, 'Un solo main');
                check(!!document.title.trim(), 'Título de pestaña');
                check(root.getPropertyValue('--tinta').trim() === '#1a1a1a', '--tinta');
                check(root.getPropertyValue('--morado').trim() === '#7c3aed', '--morado');
                check(body.backgroundColor === 'rgb(250, 249, 247)', 'Fondo canónico');
                check(body.color === 'rgb(26, 26, 26)', 'Texto canónico');
                check(main && main.getBoundingClientRect().width <= 902, 'Ancho de lectura');
                check(document.documentElement.scrollWidth <= innerWidth + 1,
                    'Sin desbordamiento horizontal de página');
                const selectors = {};
                const rules = {
                    '.repreg': s => s.backgroundColor === 'rgb(26, 26, 26)',
                    '.fuente, .cita .f': s => parseFloat(s.fontSize) < parseFloat(body.fontSize),
                    '.dist': s => parseFloat(s.borderTopWidth) > 0 && s.borderTopStyle !== 'none',
                    '.vecino': s => parseFloat(s.borderLeftWidth) >= 3 && s.borderLeftColor === 'rgb(37, 99, 235)',
                    '.pred': s => parseFloat(s.borderTopWidth) > 0 && s.backgroundColor !== 'rgba(0, 0, 0, 0)',
                    '.rol': s => parseFloat(s.borderRadius) >= 10,
                    // En clasificación/métricas .met es una tarjeta individual,
                    // y su contenedor .lect/.metgrid ya organiza las columnas.
                    '.met:not(.lect .met):not(.metgrid .met)': s => s.display === 'grid',
                    '.formula, .ec, .ecu .f': s => s.fontFamily.includes('monospace')
                };
                for (const [selector, rule] of Object.entries(rules)) {
                    const els = [...document.querySelectorAll(selector)];
                    selectors[selector] = els.length;
                    els.forEach(e => check(rule(style(e)), 'Estilo ' + selector));
                }
                check(!document.querySelector('input:disabled, button:disabled, select:disabled'),
                    'Controles disponibles desde el inicio');
                return {width: innerWidth, title: document.title, selectors, failures};
            }""")
            # Comprueba el mecanismo nativo de revelar respuestas, no solo su CSS.
            answer = page.locator("details.resp").first
            if answer.count():
                answer.locator("summary").click()
                if not answer.evaluate("e => e.open"):
                    data["failures"].append("La respuesta no se abre")
                answer.locator("summary").click()
                if answer.evaluate("e => e.open"):
                    data["failures"].append("La respuesta no se cierra")
            if width == 1280:
                # Un slider que cambia su valor pero no el resultado no funciona.
                data["ranges"] = page.evaluate("""() => {
                    const snapshot = () => document.body.innerText +
                        [...document.querySelectorAll('canvas')].map(c => c.toDataURL()).join('') +
                        [...document.querySelectorAll('svg')].map(s => s.outerHTML).join('');
                    return [...document.querySelectorAll('input[type=range]')].map(e => {
                        const old = e.value, before = snapshot();
                        e.value = old === (e.max || '100') ? (e.min || '0') : (e.max || '100');
                        e.dispatchEvent(new Event('input', {bubbles:true}));
                        e.dispatchEvent(new Event('change', {bubbles:true}));
                        const changed = snapshot() !== before;
                        const result = {id:e.id, before:old, after:e.value, resultChanged:changed};
                        e.value = old;
                        e.dispatchEvent(new Event('input', {bubbles:true}));
                        e.dispatchEvent(new Event('change', {bubbles:true}));
                        return result;
                    });
                }""")
                for control in data["ranges"]:
                    if not control["resultChanged"]:
                        data["failures"].append(f"El slider {control['id']} no cambia texto o gráfico")
            views.append(data)
            failures.extend(f"{width}px: {f}" for f in data["failures"])
        browser.close()
    failures.extend(f"JS: {e}" for e in set(errors))
    failures.extend(f"Recurso remoto: {url}" for url in set(remote))
    return {"path": str(path), "ok": not failures, "failures": failures, "views": views}


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.path)
    serialized = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
