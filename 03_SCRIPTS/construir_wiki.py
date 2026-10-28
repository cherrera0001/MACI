#!/usr/bin/env python3
"""Genera el HTML de la wiki del proyecto dentro del arbol del curso.

docs/wiki/*.md -> 07_DATITO/01_CONCEPTOS/visual/wiki/*.html

Por que aqui y no en la wiki de GitHub: la wiki de GitHub exige crear la
primera pagina a mano en la web y su repo no acepta push inicial (verificado).
El sitio propio (maci.c4a.cl) ya publica todo lo demas; estas paginas viajan
con el curso, quedan bajo la pasada de enlaces rotos de publicar_sitio.mjs y
se convierten a texto cualquier enlace a material solo local.

Conversor minimo (stdlib): cubre el subconjunto usado por las paginas de la
wiki: titulos #/##/###, tablas, listas, enlaces, negrita/cursiva, citas y
bloques de codigo. Sin dependencias.

  python 03_SCRIPTS/construir_wiki.py
"""
from __future__ import annotations

import html
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ORIGEN = RAIZ / "docs" / "wiki"
SALIDA = RAIZ / "07_DATITO" / "01_CONCEPTOS" / "visual" / "wiki"

CSS = """
body{max-width:46em;margin:2rem auto;padding:0 1rem;font-family:Georgia,serif;
line-height:1.6;color:#1a1a1a;background:#faf9f6}
h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.25}
h2{border-bottom:1px solid #ddd;padding-bottom:.2rem}
a{color:#5b21b6} table{border-collapse:collapse;width:100%;font-size:.95em}
th,td{border:1px solid #ccc;padding:.35rem .5rem;text-align:left;vertical-align:top}
th{background:#efe9f9} code{background:#eee9f5;padding:.1rem .3rem;border-radius:3px}
pre{background:#241f2e;color:#e8e0f5;padding:.8rem;overflow:auto;border-radius:6px}
pre code{background:none;color:inherit;padding:0}
blockquote{border-left:3px solid #7c3aed;margin-left:0;padding-left:1rem;color:#444}
nav{font-family:system-ui,sans-serif;font-size:.9em;background:#efe9f9;
padding:.6rem .9rem;border-radius:6px;margin-bottom:1.5rem}
nav a{margin-right:1rem}
"""

LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
EMPH = re.compile(r"(?<!\w)\*([^*]+)\*(?!\w)")
CODE = re.compile(r"`([^`]+)`")


def _enlace(m) -> str:
    destino = m.group(2)
    if destino.endswith(".md"):
        destino = destino[:-3] + ".html"
    return f'<a href="{html.escape(destino)}">{m.group(1)}</a>'


def _inline(texto: str) -> str:
    texto = html.escape(texto)
    texto = LINK.sub(_enlace, texto)
    texto = BOLD.sub(r"<strong>\1</strong>", texto)
    texto = EMPH.sub(r"<em>\1</em>", texto)
    texto = CODE.sub(r"<code>\1</code>", texto)
    return texto


def convertir(md: str) -> str:
    lineas = md.splitlines()
    out, i, en_lista = [], 0, False
    while i < len(lineas):
        linea = lineas[i]
        if linea.startswith("```"):
            bloque, i = [], i + 1
            while i < len(lineas) and not lineas[i].startswith("```"):
                bloque.append(lineas[i]); i += 1
            i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(bloque))}</code></pre>")
            continue
        if linea.startswith("|"):
            filas, i = [], i
            while i < len(lineas) and lineas[i].startswith("|"):
                celdas = [c.strip() for c in lineas[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in celdas):
                    filas.append(celdas)
                i += 1
            if filas:
                thead = "".join(f"<th>{_inline(c)}</th>" for c in filas[0])
                tbody = "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>"
                                                 for c in f) + "</tr>"
                                for f in filas[1:])
                out.append(f"<table><tr>{thead}</tr>{tbody}</table>")
            continue
        if linea.startswith("#"):
            nivel = len(linea) - len(linea.lstrip("#"))
            out.append(f"<h{nivel}>{_inline(linea[nivel:].strip())}</h{nivel}>")
        elif linea.startswith(">"):
            out.append(f"<blockquote>{_inline(linea[1:].strip())}</blockquote>")
        elif linea.strip().startswith("- "):
            if not en_lista:
                out.append("<ul>"); en_lista = True
            out.append(f"<li>{_inline(linea.strip()[2:])}</li>")
            if i + 1 >= len(lineas) or not lineas[i + 1].strip().startswith("- "):
                out.append("</ul>"); en_lista = False
        elif linea.strip():
            out.append(f"<p>{_inline(linea.strip())}</p>")
        i += 1
    return "\n".join(out)


def principal() -> int:
    if not ORIGEN.is_dir():
        print("no existe docs/wiki/"); return 1
    SALIDA.mkdir(parents=True, exist_ok=True)
    paginas = sorted(p for p in ORIGEN.glob("*.md") if not p.name.startswith("_"))
    nav = '<nav><a href="Home.html">Inicio</a>' + "".join(
        f'<a href="{p.stem}.html">{p.stem.replace("-", " ")}</a>'
        for p in paginas if p.stem != "Home") + "</nav>"
    for p in paginas:
        cuerpo = convertir(p.read_text(encoding="utf-8"))
        titulo = p.stem.replace("-", " ")
        doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)} · Wiki MACI</title>
<style>{CSS}</style></head>
<body>
{nav}
{cuerpo}
<hr><p style="font-size:.85em;color:#666">Wiki del proyecto MACI · fuente:
<a href="https://github.com/cherrera0001/MACI/tree/main/docs/wiki">docs/wiki/</a>
· <a href="../00_index.html">← Índice del curso</a></p>
</body></html>
"""
        (SALIDA / f"{p.stem}.html").write_text(doc, encoding="utf-8")
    print(f"wiki/: {len(paginas)} paginas en {SALIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principal())
