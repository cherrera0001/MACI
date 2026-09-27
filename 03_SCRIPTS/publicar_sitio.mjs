// Arma public/ para maci.c4a.cl: solo el material del curso, con la misma
// estructura relativa que 07_DATITO/ para que los enlaces sigan valiendo.
// Un enlace a algo que no se publica (transcripciones, YAML, auditorías) se
// convierte en texto: en línea no queda ningún 404.
//   node 03_SCRIPTS/publicar_sitio.mjs
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ORIGEN = path.join(RAIZ, "07_DATITO");
const SALIDA = path.join(RAIZ, "public");

// [carpeta relativa a 07_DATITO, filtro de nombres]
const PUBLICAR = [
  ["01_CONCEPTOS/visual", (n) => !n.startsWith("_")],
  ["02_REFERENCIA", (n) => n === "clase6_regresion.html"],
  ["04_EJERCICIOS", (n) => n.endsWith(".html")],
  ["04_EJERCICIOS/assets", () => true],
  ["04_EJERCICIOS/guias", () => true],
  ["04_EJERCICIOS/cuadernillos", () => true],
];
const PORTADA = "01_CONCEPTOS/visual/00_index.html";

function copiarCarpeta(rel, filtro) {
  const desde = path.join(ORIGEN, rel);
  if (!fs.existsSync(desde)) return;
  for (const e of fs.readdirSync(desde, { withFileTypes: true })) {
    const relHijo = path.join(rel, e.name);
    if (e.isDirectory()) {
      if (PUBLICAR.some(([r]) => path.normalize(r) === path.normalize(relHijo))) continue;
      if (filtro(e.name)) copiarCarpeta(relHijo, () => true);
      continue;
    }
    if (!filtro(e.name)) continue;
    const hacia = path.join(SALIDA, relHijo);
    fs.mkdirSync(path.dirname(hacia), { recursive: true });
    fs.copyFileSync(path.join(desde, e.name), hacia);
  }
}

function paginas(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const p = path.join(dir, e.name);
    return e.isDirectory() ? paginas(p) : e.name.endsWith(".html") ? [p] : [];
  });
}

function existe(archivo, href) {
  const ruta = decodeURIComponent(href.split("#")[0]);
  const destino = path.resolve(path.dirname(archivo), ruta);
  return destino.startsWith(SALIDA) && fs.existsSync(destino) && fs.statSync(destino).isFile();
}

fs.rmSync(SALIDA, { recursive: true, force: true });
for (const [rel, filtro] of PUBLICAR) copiarCarpeta(rel, filtro);

let convertidos = 0;
const ENLACE = /<a\b([^>]*?)\bhref="([^"]*)"([^>]*)>([\s\S]*?)<\/a>/g;
for (const archivo of paginas(SALIDA)) {
  const html = fs.readFileSync(archivo, "utf8");
  const nuevo = html.replace(ENLACE, (todo, antes, href, despues, texto) => {
    if (!href || /^(#|https?:|mailto:|javascript:|data:)/.test(href) || href.includes("${")) return todo;
    if (existe(archivo, href)) return todo;
    convertidos++;
    return `<span class="solo-local" title="Disponible en la copia local del repositorio">${texto}</span>`;
  });
  if (nuevo !== html) fs.writeFileSync(archivo, nuevo);
}

fs.writeFileSync(
  path.join(SALIDA, "index.html"),
  `<!DOCTYPE html>\n<html lang="es"><head><meta charset="utf-8">\n` +
    `<meta http-equiv="refresh" content="0; url=${PORTADA}">\n` +
    `<title>Fundamentos de Ciencia de Datos · el curso de Datito</title></head>\n` +
    `<body><p>El curso empieza en <a href="${PORTADA}">el índice</a>.</p></body></html>\n`,
);

const total = paginas(SALIDA).length;
console.log(`public/: ${total} páginas; ${convertidos} enlaces a material solo local convertidos en texto`);
