"""Banco de evaluación del cerebro (D-15.3): baseline TF-IDF vs cerebro aal.

Mismo índice, mismas sondas, dos recuperadores cara a cara:

- **Baseline**: ``Indice.buscar_asociativo`` (E-12/E-14, la memoria actual).
- **Cerebro**: ``cerebro.Cerebro.recuperar`` con trazas, valencia y filtros
  de dominio/kind (E-15).

Escenarios adversarios heredados del repo hermano:
- **H4 (señuelo léxico/contradictorio)**: una guía o memoria señuelo comparte
  vocabulario con la consulta pero no es el recuerdo buscado.
- **H7 (contaminación cruzada)**: nodos de otro dominio en el grafo no deben
  filtrarse jamás a la recuperación de compañía.
- **Repetición**: contar la misma historia N veces no infla el grafo.
- **Validación**: 100% de los fids devueltos pasan ``evidencia.validar``.

Métricas pre-registradas: MRR, precisión@3, tasa de rechazo de señuelos,
filtración de dominio y validez de evidencia.

Regla de adopción (honesta, D-15.3): el cerebro se adopta como default solo
si **no regresa en ninguna métrica** y mejora estrictamente en al menos una;
si empata sin mejorar o regresa en alguna, queda como opt-in
(``cerebro: aal`` en curso.yaml).
"""
from __future__ import annotations

import json
import tempfile
from dataclasses import dataclass, field

from . import cerebro, evidencia
from .indice import Indice

K = 3

# ------------------------------------------------------------- escenarios
# Memorias objetivo (dominio compañía)
M_RUFO = "Su perrito Rufo la esperaba en la puerta cada tarde"
M_VIDEO = "Hace videollamadas con sus nietas los domingos por la tarde"
M_TEJER = "Aprendió a tejer con su madre en Chillán"
M_SOPAIPILLAS = "Los domingos hacía sopaipillas con su hermana"
# Señuelo contradictorio (H4): mismo eje léxico, recuerdo falso
M_RUFO_FALSO = "Rufo era el gato de su vecina de al lado"
# Señuelo de guía (H4): vocabulario de banco/claves que colisiona con recuerdos
G_CLAVES = ("Nunca comparta las claves de su banco por teléfono: "
            "ningún banco las pide")


@dataclass
class Sonda:
    consulta: str
    objetivo: str | None = None     # fid esperado (MRR/P@3)
    senuelo: str | None = None      # fid que debe quedar fuera del top-K
    dominio: str = cerebro.DOMINIO_COMPANIA


@dataclass
class Resultado:
    mrr: float = 0.0
    p3: float = 0.0
    rechazo_senuelos: float = 0.0   # fracción de señuelos fuera del top-K
    fuga_dominio: int = 0           # nodos de otro dominio recuperados
    validez: float = 1.0            # fracción de fids que validan evidencia
    n: int = 0
    detalle: dict = field(default_factory=dict)


# ------------------------------------------------------------- construcción
def construir_indice() -> tuple[Indice, dict[str, str]]:
    """Índice con objetivos y señuelos; devuelve {clave: fid}."""
    ind = Indice()
    fids = {}
    for clave, texto, ref in (
        ("rufo", M_RUFO, "sesion eval"),
        ("video", M_VIDEO, "sesion eval"),
        ("tejer", M_TEJER, "sesion eval"),
        ("sopaipillas", M_SOPAIPILLAS, "sesion eval"),
        ("rufo_falso", M_RUFO_FALSO, "sesion eval"),
        ("claves", G_CLAVES, "guia: anti-estafa"),
    ):
        fids[clave] = ind.registrar_recuerdo(texto, referencia=ref)
    return ind, fids


SONDAS = [
    Sonda("cuénteme de Rufo, ese perrito", objetivo="rufo", senuelo="rufo_falso"),
    Sonda("las videollamadas con sus nietas", objetivo="video"),
    Sonda("aprendió a tejer con su madre", objetivo="tejer"),
    Sonda("las sopaipillas de domingo", objetivo="sopaipillas"),
    # Señuelo de guía: el baseline la devuelve; el cerebro (kind=memoria) no
    Sonda("claves banco teléfono", senuelo="claves"),
    # Puente: 'domingos' conecta sopaipillas↔videollamadas (multi-salto)
    Sonda("qué hacía los domingos con su hermana", objetivo="sopaipillas"),
]


def _clave_a_fid(fids: dict[str, str], clave: str | None) -> str | None:
    return fids.get(clave) if clave else None


def entrenar(cer: cerebro.Cerebro, ind: Indice, fids: dict[str, str]) -> None:
    """Episodios previos: el señuelo contradictorio queda ligado a una alerta
    (valencia negativa) y los objetivos se refuerzan en episodios de éxito."""
    for mensaje, senal in (
        ("Hoy vi al gato de la vecina y me sentí confundida y triste",
         {"nivel": "alerta", "senales": ["tristeza"]}),
        ("Cuénteme de mi perrito Rufo que me esperaba en la puerta",
         None),
        ("Videollamo a mis nietas los domingos por la tarde",
         None),
    ):
        cer.ciclo(mensaje, indice=ind, senal=senal)


def ranking_baseline(ind: Indice, consulta: str) -> list[str]:
    return [fid for fid, _, _ in ind.buscar_asociativo(consulta, k=K, saltos=2)]


def ranking_cerebro(cer: cerebro.Cerebro, ind: Indice,
                    consulta: str, dominio: str = cerebro.DOMINIO_COMPANIA
                    ) -> list[str]:
    return [r["fid"] for r in cer.recuperar(consulta, k=K, indice=ind,
                                            dominio=dominio,
                                            kinds=("memoria",))
            if r["fid"]]


# ------------------------------------------------------------- métricas
def evaluar_lado(rankings: dict[str, list[str]], fids: dict[str, str],
                 ind: Indice) -> Resultado:
    res = Resultado()
    rr_sum = p3_sum = rechazo = val_sum = 0.0
    n_obj = n_sen = 0
    for sonda in SONDAS:
        ranking = rankings[sonda.consulta]
        res.n += 1
        objetivo = _clave_a_fid(fids, sonda.objetivo)
        if objetivo:
            n_obj += 1
            try:
                rango = ranking.index(objetivo) + 1
            except ValueError:
                rango = 0
            rr_sum += 1.0 / rango if rango else 0.0
            p3_sum += 1.0 if rango and rango <= K else 0.0
        senuelo = _clave_a_fid(fids, sonda.senuelo)
        if senuelo:
            n_sen += 1
            rechazo += 0.0 if senuelo in ranking[:K] else 1.0
        for fid in ranking:
            val_sum += 1.0 if evidencia.validar(
                f"{ind.textos[fid]} [{fid}]", ind).ok else 0.0
        res.detalle[sonda.consulta] = ranking
    res.mrr = round(rr_sum / max(n_obj, 1), 4)
    res.p3 = round(p3_sum / max(n_obj, 1), 4)
    res.rechazo_senuelos = round(rechazo / max(n_sen, 1), 4)
    n_fids = sum(len(v) for v in rankings.values())
    res.validez = round(val_sum / max(n_fids, 1), 4)
    return res


def comparar(curso_factory=None) -> dict:
    """Cara a cara baseline vs cerebro. Devuelve métricas y decisión D-15.3."""
    ind, fids = construir_indice()

    base = evaluar_lado({s.consulta: ranking_baseline(ind, s.consulta)
                         for s in SONDAS}, fids, ind)

    salida = {"baseline": base.__dict__, "cerebro": None,
              "decision": "opt_in",
              "regla": ("adoptar solo sin regresión en MRR/P@3/rechazo y con "
                        "mejora estricta en al menos una métrica; si no, opt-in")}

    if not cerebro.AAL:
        salida["motivo"] = "aal no instalado: cerebro no evaluable (opt-in)"
        return salida

    if curso_factory is None:
        # Sin fábrica de curso, evaluamos en un curso temporal aislado.
        from pathlib import Path

        from . import config
        from .modelo import crear

        tmp = tempfile.TemporaryDirectory(prefix="e15-eval-")
        config.DIR_CURSOS = Path(tmp.name) / "cursos"
        curso = crear("evalcerebro", nombre="Eval", periodo="eval")
        curso.datos["modo"] = "compania"
        curso.guardar()
    else:
        curso = curso_factory()
    cer = cerebro.Cerebro(curso)
    cer.sincronizar_indice(ind)
    entrenar(cer, ind, fids)
    # Repetición (H-15.3): la misma historia 12 veces no debe inflar el grafo.
    n_antes = len([n for n in cer.grafo.nodes()
                   if n.metadata.get("kind") == "memoria"])
    for _ in range(12):
        cer.ciclo("Otra vez le cuento de mi perrito Rufo y la puerta",
                  indice=ind)
    despues = [n for n in cer.grafo.nodes()
               if n.metadata.get("kind") == "memoria"]
    rufo_dup = [n for n in despues if "perrito" in n.label.lower()]

    rank_cer = {s.consulta: ranking_cerebro(cer, ind, s.consulta,
                                            dominio=s.dominio)
                for s in SONDAS}
    cero = evaluar_lado(rank_cer, fids, ind)
    salida["repeticion"] = {
        "nodos_memoria_antes": n_antes,
        "nodos_memoria_despues": len(despues),
        "rufo_unico": len(rufo_dup) == 1,
    }
    cero.fuga_dominio = _medir_fuga(cer, ind)
    salida["h7_fuga"] = cero.fuga_dominio
    salida["cerebro"] = cero.__dict__
    salida["decision"] = _decision(base, cero, salida["repeticion"],
                                   salida["h7_fuga"])
    return salida


def _medir_fuga(cer: cerebro.Cerebro, ind: Indice) -> int:
    """H7: memoria académica registrada (valida) pero de otro dominio.

    El fid existe en el índice, así que ``evidencia.validar`` la acepta: solo
    el filtro duro de dominio del cerebro puede rechazarla.
    """
    mg = cer.grafo
    nodo = "concept:memoria:matriz_confusion_curso"
    fid = ind.registrar_recuerdo("la matriz de confusión del curso de datos",
                                 referencia="academico eval")
    mg.add_node(nodo, cerebro.NodeType.CONCEPT,
                "la matriz de confusión del curso de datos",
                kind="memoria", fid=fid, domain="academico")
    cer.guardar()
    hallazgos = cer.recuperar("la matriz de confusión del curso de datos",
                              k=K, indice=ind, dominio="compania",
                              kinds=("memoria",))
    mg.remove_node(nodo)
    cer.guardar()
    return sum(1 for h in hallazgos if h["nodo"] == nodo)


def _decision(base: Resultado, cero: Resultado, rep: dict, fuga: int) -> str:
    """D-15.3: adoptar solo sin regresión y con mejora estricta en algo."""
    if cero.validez < 1.0 or fuga > 0 or not rep.get("rufo_unico"):
        return "opt_in"
    regresion = any(getattr(cero, m) < getattr(base, m)
                    for m in ("mrr", "p3", "rechazo_senuelos"))
    mejora = any(getattr(cero, m) > getattr(base, m)
                 for m in ("mrr", "p3", "rechazo_senuelos"))
    if regresion or not mejora:
        return "opt_in"
    return "adoptar"


def main() -> None:  # pragma: no cover - CLI
    print(json.dumps(comparar(), indent=2, ensure_ascii=False))


if __name__ == "__main__":  # pragma: no cover
    main()
