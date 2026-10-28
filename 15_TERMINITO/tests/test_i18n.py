"""FR-022: el diccionario i18n debe tener las mismas claves en ES y EN,
y las páginas deben cargar i18n.js antes que api.js (t() disponible)."""
import re
from pathlib import Path

WEB = Path(__file__).parent.parent / "src" / "web"


def _claves(bloque: str) -> set[str]:
    return set(re.findall(r'^\s{4}"([^"]+)":', bloque, re.M))


def test_i18n_claves_pares():
    src = (WEB / "js" / "i18n.js").read_text(encoding="utf-8")
    partes = re.split(r"\n  (es|en): \{", src)
    assert len(partes) >= 5, "esperaba bloques es y en"
    es, en = _claves(partes[2]), _claves(partes[4])
    assert es and es == en, f"claves sin par: {es ^ en}"


def test_paginas_cargan_i18n_antes_que_api():
    for pagina in WEB.glob("*.html"):
        src = pagina.read_text(encoding="utf-8")
        assert "/js/i18n.js" in src, f"{pagina.name} no carga i18n.js"
        assert src.index("i18n.js") < src.index("api.js"), \
            f"{pagina.name}: i18n.js debe ir antes que api.js"


def test_paginas_usan_data_i18n():
    for pagina in WEB.glob("*.html"):
        src = pagina.read_text(encoding="utf-8")
        assert "data-i18n" in src, f"{pagina.name} sin data-i18n (FR-022)"
