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

    # --- memoria episodica en caliente (modo compania, E-10) ---------------

    def consolidar_recuerdo(self, texto: str, referencia: str = "",
                            umbral: float = 0.55) -> str:
        """Consolidación hipocampal (D-12.2): deduplica antes de registrar.

        Si el relato entrante es casi el mismo (Jaccard de tokens de
        contenido >= umbral) que una memoria existente, fusiona en esa: no
        se crea un memoria#<n> redundante y la memoria se enriquece con la
        versión más informativa. Devuelve el fid consolidado (o nuevo).
        """
        tokens_n = set(tokenizar(texto))
        mejor, sim = None, 0.0
        for f in list(self.textos):
            if not f.startswith("memoria#") \
                    or self.referencias.get(f, ("", ""))[1].startswith("guia:"):
                continue
            existentes = set(tokenizar(self.textos[f]))
            if not existentes:
                continue
            j = len(tokens_n & existentes) / len(tokens_n | existentes)
            if j > sim:
                sim, mejor = j, f
        if mejor and sim >= umbral:
            if len(texto) > len(self.textos[mejor]):
                self.textos[mejor] = texto
                if referencia:
                    self.referencias[mejor] = ("memoria", referencia)
                self._revectorizar(mejor)
            return mejor
        return self.registrar_recuerdo(texto, referencia)

    def _revectorizar(self, fid: str):
        """Reconstruye el vector de un fid tras enriquecer su texto."""
        tf: dict[str, int] = {}
        for tok in tokenizar(self.textos[fid]):
            tf[tok] = tf.get(tok, 0) + 1
        self.vectores[fid] = tf  # provisional, para el df
        n = len(self.vectores)
        df: dict[str, int] = {}
        for vec in self.vectores.values():
            for t in vec:
                df[t] = df.get(t, 0) + 1
        self.idf = {t: math.log((1 + n) / (1 + d)) + 1.0 for t, d in df.items()}
        vec = {t: (1.0 + math.log(c)) * self.idf[t] for t, c in tf.items()}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        self.vectores[fid] = {t: v / norm for t, v in vec.items()}

    def _df(self, termino: str) -> int:
        """Frecuencia de documento reconstruida del IDF (bijection con n fijo)."""
        n = len(self.vectores)
        v = self.idf.get(termino)
        if v is None or n == 0:
            return 0
        return max(0, int(round((1 + n) / math.exp(v - 1.0) - 1)))

    def registrar_recuerdo(self, texto: str, referencia: str = "") -> str:
        """Registra un recuerdo episódico en caliente con fid ``memoria#<n>``.

        El fid cumple CITA_RE, así que el recuerdo queda citable de inmediato
        y valida con evidencia.validar. Recalcula IDF y normaliza el vector
        nuevo; el formato persistido en .indice/ es el de siempre.
        """
        numeros = [int(f.split("#", 1)[1]) for f in self.textos
                   if f.startswith("memoria#")]
        fid = f"memoria#{1 + max(numeros or [0])}"
        tf: dict[str, int] = {}
        for tok in tokenizar(texto):
            tf[tok] = tf.get(tok, 0) + 1
        self.vectores[fid] = tf  # provisional, solo para contar df
        n = len(self.vectores)
        df: dict[str, int] = {}
        for vec in self.vectores.values():
            for t in vec:
                df[t] = df.get(t, 0) + 1
        self.idf = {t: math.log((1 + n) / (1 + d)) + 1.0 for t, d in df.items()}
        vec = {t: (1.0 + math.log(c)) * self.idf[t] for t, c in tf.items()}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        self.vectores[fid] = {t: v / norm for t, v in vec.items()}
        self.textos[fid] = texto
        self.referencias[fid] = ("memoria", referencia or fid)
        return fid

    def _puentes(self, fids: list[str], top_m: int = 6) -> list[str]:
        """Términos puente: altos en IDF y compartidos (2 <= df <= n/2).

        Un término que aparece en un solo documento es un callejón sin
        salida para la propagación; uno que aparece en casi todos es ruido.
        Los puentes son las entidades que conectan recuerdos (HippoRAG ligero).
        """
        n = len(self.vectores)
        scores: dict[str, float] = {}
        for fid in fids:
            for t in (self.vectores.get(fid) or {}):
                d = self._df(t)
                if 2 <= d <= max(2, n // 2):
                    scores[t] = max(scores.get(t, 0.0), self.idf.get(t, 1.0))
        if scores:
            return sorted(scores, key=lambda t: -scores[t])[:top_m]
        # índice pequeño: caer a los términos más raros de la frontera
        raros: dict[str, float] = {}
        for fid in fids:
            for t in (self.vectores.get(fid) or {}):
                raros[t] = max(raros.get(t, 0.0), self.idf.get(t, 1.0))
        return sorted(raros, key=lambda t: -raros[t])[:top_m]

    def buscar_asociativo(self, consulta: str, k: int = 4, saltos: int = 2,
                          por_salto: int = 8, decaimiento: float = 0.5
                          ) -> list[tuple[str, float, list[str]]]:
        """Propagación de activación por nodos puente de alto IDF.

        Semillas por coseno; en cada salto, los términos puente de la
        frontera expanden a fragmentos que los comparten, con decaimiento.
        Devuelve (fid, activación, puentes) ordenado; todo fid existe en
        self.textos: la asociatividad cambia la recuperación, no la verdad.
        """
        semillas = self.buscar(consulta, k=por_salto)
        if not semillas:
            return []
        activacion = {fid: score for fid, score in semillas}
        traza = {fid: [] for fid, _ in semillas}
        frontera = [fid for fid, _ in semillas]
        vistos = set(activacion)
        for salto in range(1, saltos + 1):
            puentes = self._puentes(frontera)
            if not puentes:
                break
            candidatos: dict[str, float] = {}
            for t in puentes:
                peso = self.idf.get(t, 1.0)
                for fid, vec in self.vectores.items():
                    if fid in vistos or t not in vec:
                        continue
                    candidatos[fid] = candidatos.get(fid, 0.0) + peso * vec[t]
            if not candidatos:
                break
            escala = decaimiento ** salto
            nuevos = []
            for fid, a in sorted(candidatos.items(), key=lambda kv: -kv[1])[:por_salto]:
                activacion[fid] = a * escala
                traza[fid] = list(puentes)
                vistos.add(fid)
                nuevos.append(fid)
            frontera = nuevos
        ordenados = sorted(activacion, key=lambda f: -activacion[f])
        return [(fid, activacion[fid], traza[fid]) for fid in ordenados[:k]]

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
