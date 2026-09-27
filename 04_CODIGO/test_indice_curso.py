"""El índice del curso abre cada destino que promete, sin conexión."""
import os
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
VISUAL = ROOT / "07_DATITO" / "01_CONCEPTOS" / "visual"
INDICE = VISUAL / "00_index.html"
TRANSCRIPCIONES = ROOT / "05_CLASES" / "transcripciones"
HREF = re.compile(r'href="([^"]*)"')
ID = re.compile(r'\bid="([^"]+)"')
MARCA = re.compile(r'data-marca="(\d+)"')

DESTINOS = {
    "fundamentos_ciencia_datos.html": VISUAL / "01_fundamentos.html",
    "datos_features_target.html": VISUAL / "02_datos_features_target.html",
    "eda.html": VISUAL / "03_eda.html",
    "limpieza_preparacion.html": VISUAL / "04_limpieza_preparacion.html",
    "train_validation_test.html": VISUAL / "05_train_validation_test.html",
    "validacion_cruzada.html": VISUAL / "06_validacion_cruzada.html",
    "generalizacion.html": VISUAL / "07_generalizacion.html",
    "overfitting_underfitting.html": VISUAL / "08_overfitting_underfitting.html",
    "regresion_y_costo.html": VISUAL / "09_regresion.html",
    "clasificacion.html": VISUAL / "10_clasificacion.html",
    "matriz_confusion.html": VISUAL / "11_matriz_confusion.html",
    "metricas_clasificacion.html": VISUAL / "12_metricas_clasificacion.html",
    "roc_auc.html": VISUAL / "13_roc_auc.html",
    "arboles_y_ensambles.html": VISUAL / "14_arboles_decision.html",
    "redes_neuronales.html": VISUAL / "18_redes_neuronales.html",
    "dl_llm_agentes.html": VISUAL / "19_deep_learning.html",
    "clase6_regresion.html": ROOT / "07_DATITO" / "02_REFERENCIA" / "clase6_regresion.html",
    "certamen_1.html": ROOT / "07_DATITO" / "04_EJERCICIOS" / "certamen_1.html",
    "certamen_2.html": ROOT / "07_DATITO" / "04_EJERCICIOS" / "certamen_2.html",
    "certamen_3.html": ROOT / "07_DATITO" / "04_EJERCICIOS" / "certamen_3.html",
    "triaje_de_problemas.html": ROOT / "07_DATITO" / "04_EJERCICIOS" / "triaje_de_problemas.html",
    "index.html": INDICE,
    "patron_evaluacion.md": ROOT / "07_DATITO" / "06_AUDITORIAS" / "patron_evaluacion.md",
    "dudas.yaml": ROOT / "07_DATITO" / "dudas.yaml",
    "grafo.yaml": ROOT / "07_DATITO" / "grafo.yaml",
    "overfitting_underfitting.md": ROOT / "07_DATITO" / "04_EJERCICIOS" / "guias" / "overfitting_underfitting.md",
    "01_sobreajuste_y_calidad_de_datos.md": ROOT / "07_DATITO" / "04_EJERCICIOS" / "cuadernillos" / "01_sobreajuste_y_calidad_de_datos.md",
}


def relativo(origen, destino):
    return Path(os.path.relpath(destino, origen.parent)).as_posix()


def partir(href):
    parsed = urlparse(href)
    path = unquote(parsed.path)
    fragmento = parsed.fragment
    return path, fragmento


def resuelve(origen, href):
    if href.startswith(("http://", "https://", "mailto:", "javascript:")):
        return True
    path, _fragmento = partir(href)
    if not path:
        return True
    return (origen.parent / path).resolve().is_file()


def destino_de(href):
    path, fragmento = partir(href)
    if not path:
        return None, fragmento
    marca = "09_CLASES/transcripciones/"
    if marca in path:
        nombre = path.split(marca, 1)[1]
        return TRANSCRIPCIONES / nombre, fragmento
    base = Path(path).name
    return DESTINOS.get(base), fragmento


def reparar_href(href, origen):
    if href.startswith(("http://", "https://", "mailto:", "javascript:")):
        return href
    if resuelve(origen, href):
        return href
    destino, fragmento = destino_de(href)
    if destino is None or not destino.is_file():
        return href
    nuevo = relativo(origen, destino)
    if fragmento:
        nuevo += "#" + fragmento
    return nuevo


def reparar_archivo(ruta):
    texto = ruta.read_text(encoding="utf-8")
    nuevo = HREF.sub(lambda m: f'href="{reparar_href(m.group(1), ruta)}"', texto)
    if nuevo != texto:
        ruta.write_text(nuevo, encoding="utf-8")
    return nuevo != texto


def enlaces_locales(ruta):
    return HREF.findall(ruta.read_text(encoding="utf-8"))


def ids_de(ruta):
    return set(ID.findall(ruta.read_text(encoding="utf-8")))


def rotos(ruta):
    fallos = []
    for href in enlaces_locales(ruta):
        if href.startswith(("http://", "https://", "mailto:", "javascript:")):
            continue
        path, fragmento = partir(href)
        if not path:
            if fragmento and fragmento not in ids_de(ruta):
                fallos.append(href)
            continue
        destino = (ruta.parent / path).resolve()
        if not destino.is_file():
            fallos.append(href)
            continue
        if fragmento and destino.suffix.lower() in {".html", ".htm"}:
            if fragmento not in ids_de(destino):
                fallos.append(href)
    return fallos


class IndiceCursoTests(unittest.TestCase):
    def test_cada_enlace_del_indice_abre_un_archivo(self):
        self.assertEqual([], rotos(INDICE))

    def test_comenzar_abre_la_clase_1(self):
        html = INDICE.read_text(encoding="utf-8")
        self.assertIn('class="boton" href="01_fundamentos.html"', html)

    def test_el_contador_coincide_con_las_marcas(self):
        html = INDICE.read_text(encoding="utf-8")
        marcas = MARCA.findall(html)
        self.assertNotIn("19", marcas)
        self.assertEqual(len(marcas), len(set(marcas)))
        self.assertIn(f'id="total-clases">{len(marcas)}</b> clases disponibles', html)
        self.assertIn("getElementById('total-clases').textContent=total", html)

    def test_las_paginas_enlazadas_siguen_teniendo_destino(self):
        vistos = set()
        fallos = []
        for href in enlaces_locales(INDICE):
            path, _fragmento = partir(href)
            if not path or href.startswith(("http://", "https://", "mailto:")):
                continue
            destino = (INDICE.parent / path).resolve()
            if destino.suffix.lower() not in {".html", ".htm"} or destino in vistos:
                continue
            vistos.add(destino)
            for roto in rotos(destino):
                fallos.append(f"{destino.name}: {roto}")
        self.assertEqual([], fallos)


if __name__ == "__main__":
    unittest.main()
