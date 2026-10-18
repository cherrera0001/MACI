"""Parser de materiales: PDF/Markdown/TXT/HTML -> fragmentos indexados con fuente citada.

Cada fragmento lleva un fid estable (<fuente>#<n>) y una referencia direccionable
(pagina, timestamp [h:mm:ss] o encabezado). Patron de evidencia de maci.c4a.cl.
"""
from __future__ import annotations

import html as html_mod
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

TAMANO_MIN = 60      # palabras; fragmentos menores se fusionan con el siguiente
TAMANO_MAX = 350     # palabras objetivo por fragmento
TS_RE = re.compile(r"\*\*\[(\d+:\d{2}:\d{2})\]\*\*")
HEAD_RE = re.compile(r"^#{1,4}\s+")


@dataclass
class Fuente:
    id: str
    tipo: str            # md | txt | pdf | html
    ruta: Path           # ruta real (puede ser symlink)
    titulo: str


@dataclass
class Fragmento:
    fid: str
    fuente_id: str
    referencia: str      # "pag. 3" | "0:12:44" | "seccion X"
    texto: str
    tokens: int = 0
    meta: dict = field(default_factory=dict)


def norm_id(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()[:60]


def _extraer_pdf(ruta: Path) -> list[tuple[str, str]]:
    """Devuelve [(referencia, texto)] por pagina. Requiere pypdf; si falta, avisa."""
    try:
        from pypdf import PdfReader
    except ImportError:
        raise RuntimeError(
            "pypdf no instalado: pip install pypdf (o indexa solo md/txt/html)")
    lector = PdfReader(str(ruta))
    paginas = []
    for i, pagina in enumerate(lector.pages, start=1):
        try:
            texto = pagina.extract_text() or ""
        except Exception:
            texto = ""
        paginas.append((f"pag. {i}", texto))
    return paginas


def _extraer_html(ruta: Path) -> list[tuple[str, str]]:
    crudo = ruta.read_text(encoding="utf-8", errors="ignore")
    crudo = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", crudo, flags=re.S | re.I)
    # conservar anclas de seccion como referencia
    bloques = re.split(r"(<h[12][^>]*>)", crudo)
    partes, seccion = [], "inicio"
    for i in range(1, len(bloques), 2):
        etiqueta = bloques[i]
        cuerpo = bloques[i + 1] if i + 1 < len(bloques) else ""
        m = re.search(r"""id=["']([^"']+)["']""", etiqueta)
        if m:
            seccion = m.group(1)
        texto = re.sub(r"<[^>]+>", " ", cuerpo)
        texto = html_mod.unescape(re.sub(r"\s+", " ", texto)).strip()
        if texto:
            partes.append((f"#{seccion}", texto))
    return partes or [("#inicio", re.sub(r"<[^>]+>", " ", crudo))]


def _extraer_texto(ruta: Path) -> list[tuple[str, str]]:
    """Markdown/TXT: parrafos con su timestamp [h:mm:ss] si lo tienen."""
    lineas = ruta.read_text(encoding="utf-8", errors="ignore").splitlines()
    parrafos, actual, ref_actual = [], [], "inicio"
    for ln in lineas:
        if not ln.strip():
            if actual:
                parrafos.append((ref_actual, " ".join(actual)))
                actual = []
            continue
        m = TS_RE.search(ln)
        if m and not actual:
            ref_actual = m.group(1)
        elif HEAD_RE.match(ln) and not actual:
            ref_actual = "#" + norm_id(ln.strip("# ").strip())
        actual.append(ln.strip())
    if actual:
        parrafos.append((ref_actual, " ".join(actual)))
    return parrafos


def _empaquetar(partes: list[tuple[str, str]], fid_base: str) -> list[Fragmento]:
    """Fusiona partes en fragmentos de TAMANO_MAX palabras. Una referencia de
    seccion (prefijo '#') cierra el fragmento actual: las secciones son unidades
    semanticas propias aunque sean cortas."""
    out, buffer, ref, n = [], [], None, 0

    def volcar():
        nonlocal buffer, ref, n
        if buffer:
            n += 1
            texto = " ".join(buffer)
            out.append(Fragmento(fid=f"{fid_base}#{n}", fuente_id=fid_base,
                                 referencia=ref or "inicio", texto=texto,
                                 tokens=len(texto.split())))
            buffer = []
    for referencia, texto in partes:
        palabras_texto = texto.split()
        trozos = [palabras_texto[i:i + TAMANO_MAX]
                  for i in range(0, len(palabras_texto), TAMANO_MAX)] or [[]]
        for trozo in trozos:
            palabras = len(trozo)
            es_seccion = str(referencia).startswith("#")
            if es_seccion:
                volcar()          # frontera semantica: cerrar lo anterior
                ref = referencia
            if buffer and sum(len(b.split()) for b in buffer) + palabras > TAMANO_MAX:
                volcar()
            buffer.append(" ".join(trozo))
            if ref is None:
                ref = referencia
            if palabras >= TAMANO_MIN:
                volcar()
                ref = None
        if trozos and str(referencia).startswith("#"):
            volcar()              # la seccion completa es un fragmento propio
            ref = None
    volcar()
    return out


def parsear_fuente(ruta: Path) -> tuple[Fuente, list[Fragmento]]:
    tipo = ruta.suffix.lower().lstrip(".") or "txt"
    fuente = Fuente(id=norm_id(ruta.stem), tipo=tipo, ruta=ruta, titulo=ruta.stem)
    if tipo == "pdf":
        partes = _extraer_pdf(ruta)
    elif tipo in ("html", "htm"):
        partes = _extraer_html(ruta)
    else:
        partes = _extraer_texto(ruta)
    return fuente, _empaquetar(partes, fuente.id)


def parsear_materiales(rutas: list[Path]) -> tuple[list[Fuente], list[Fragmento]]:
    """Expande directorios, sigue symlinks; parsea cada archivo soportado."""
    SOPORTADOS = {".md", ".txt", ".pdf", ".html", ".htm"}
    fuentes, fragmentos = [], []
    for ruta in rutas:
        ruta = Path(ruta)
        archivos = sorted(ruta.rglob("*")) if ruta.is_dir() else [ruta]
        for arch in archivos:
            if arch.suffix.lower() not in SOPORTADOS or not arch.is_file():
                continue
            try:
                fuente, frags = parsear_fuente(arch)
            except RuntimeError as e:
                print(f"  [aviso] {arch.name}: {e}")
                continue
            fuentes.append(fuente)
            fragmentos.extend(frags)
    return fuentes, fragmentos
