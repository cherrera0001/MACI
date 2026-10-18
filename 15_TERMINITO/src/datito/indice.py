"""Indice TF-IDF en puro Python (offline, sin dependencias pesadas).

Artefacto derivado regenerable (research R3): se guarda en <curso>/.indice/
y se puede reconstruir siempre desde los fragmentos.
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path

from .fragmentos import Fragmento

STOP = set("""el la los las de del que en y a se por para con una un es al como
mas sus le lo su este esta ya o pero desde cuando muy sin sobre tambien hasta hay
donde quien porque antes despues entre durante todo todos todas parte hoy dia
the and for are was with this that from have not you your our their its""".split())

TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenizar(texto: str) -> list[str]:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return [tok for tok in TOKEN_RE.findall(t) if len(tok) > 2 and tok not in STOP]


class Indice:
    def __init__(self):
        self.vectores: dict[str, dict[str, float]] = {}
        self.idf: dict[str, float] = {}
        self.referencias: dict[str, tuple[str, str]] = {}  # fid -> (fuente_id, referencia)
        self.textos: dict[str, str] = {}

    def construir(self, fragmentos: list[Fragmento]):
        df: dict[str, int] = {}
        tf_por_fid: dict[str, dict[str, int]] = {}
        for f in fragmentos:
            tf: dict[str, int] = {}
            for tok in tokenizar(f.texto):
                tf[tok] = tf.get(tok, 0) + 1
            tf_por_fid[f.fid] = tf
            for tok in tf:
                df[tok] = df.get(tok, 0) + 1
        n = max(1, len(fragmentos))
        self.idf = {t: math.log((1 + n) / (1 + d)) + 1.0 for t, d in df.items()}
        self.vectores = {}
        for f in fragmentos:
            vec = {t: (1.0 + math.log(c)) * self.idf[t] for t, c in tf_por_fid[f.fid].items()}
            norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
            self.vectores[f.fid] = {t: v / norm for t, v in vec.items()}
            self.referencias[f.fid] = (f.fuente_id, f.referencia)
            self.textos[f.fid] = f.texto
        return self

    def _vector_consulta(self, consulta: str) -> dict[str, float]:
        tf: dict[str, int] = {}
        for tok in tokenizar(consulta):
            tf[tok] = tf.get(tok, 0) + 1
        vec = {t: (1.0 + math.log(c)) * self.idf.get(t, 1.0) for t, c in tf.items()}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        return {t: v / norm for t, v in vec.items()}

    def buscar(self, consulta: str, k: int = 4) -> list[tuple[str, float]]:
        q = self._vector_consulta(consulta)
        puntajes = []
        for fid, vec in self.vectores.items():
            sim = sum(peso * vec.get(tok, 0.0) for tok, peso in q.items())
            if sim > 0:
                puntajes.append((fid, sim))
        puntajes.sort(key=lambda x: -x[1])
        return puntajes[:k]

    def guardar(self, dir_indice: Path):
        dir_indice.mkdir(parents=True, exist_ok=True)
        (dir_indice / "manifest.json").write_text(json.dumps({
            "modelo": "tfidf-python",
            "fids": sorted(self.vectores),
            "referencias": self.referencias,
        }, ensure_ascii=False), encoding="utf-8")
        (dir_indice / "vectores.json").write_text(json.dumps({
            "idf": self.idf, "vectores": self.vectores,
        }), encoding="utf-8")
        (dir_indice / "textos.json").write_text(
            json.dumps(self.textos, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def cargar(cls, dir_indice: Path) -> "Indice":
        ind = cls()
        man = json.loads((dir_indice / "manifest.json").read_text(encoding="utf-8"))
        vec = json.loads((dir_indice / "vectores.json").read_text(encoding="utf-8"))
        ind.vectores = vec["vectores"]
        ind.idf = vec["idf"]
        ind.referencias = {k: tuple(v) for k, v in man["referencias"].items()}
        ind.textos = json.loads((dir_indice / "textos.json").read_text(encoding="utf-8"))
        return ind
