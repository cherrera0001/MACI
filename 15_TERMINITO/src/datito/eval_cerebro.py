"""Banco de evaluación del cerebro (D-15.3, ampliado en E-16 a 20 sondas).

Mismo índice, mismas sondas, dos recuperadores cara a cara:

- **Baseline**: ``Indice.buscar_asociativo`` (E-12/E-14, la memoria actual).
- **Cerebro**: ``cerebro.Cerebro.recuperar`` con trazas, valencia y filtros
  de dominio/kind (E-15).

Escenarios adversarios heredados del repo hermano Agents_Learning_Loops:
señuelo léxico contradictorio (H4), señuelo de guía (H4), contaminación cruzada
académico↔compañía (H7, contada ahora para ambos lados), memoria contradictoria
nueva entrenada con alerta, e historia repetida N veces.

Métricas pre-registradas: MRR, precisión@3, tasa de rechazo de señuelos (H4),
fuga de dominio (H7, ambos lados) y validez de evidencia.

Regla de adopción (honesta, D-15.3): el cerebro se adopta como default solo
si **no regresa en ninguna métrica** y mejora estrictamente en al menos una;
si empata sin mejorar o regresa en alguna, queda como opt-in
(``cerebro: aal`` en curso.yaml). Ampliación E-16: 20 sondas; la decisión se
re-evalúa con el banco completo y se publica en docs/gestion/historico/.
"""
from __future__ import annotations

import json
import tempfile
from collections import Counter
from dataclasses import dataclass, field

from . import cerebro, evidencia
from .indice import Indice

K = 3


def _piso_inferencial():
    """Importa lazy el estándar #337 de aal (CI corre sin la dependencia)."""
    try:
        from associative_agent_loop.evaluation.incertidumbre import (
            bootstrap_ganancia, significa)
        from associative_agent_loop.evaluation.rival import (_coseno,
                                                             _tfidf_vector)
        from associative_agent_loop.memory.text import tokenize

        return {"bootstrap_ganancia": bootstrap_ganancia,
                "significa": significa, "_coseno": _coseno,
                "_tfidf_vector": _tfidf_vector, "tokenize": tokenize}
    except Exception:
        return None

# ------------------------------------------------------------- escenarios
# Memorias objetivo (dominio compañía)
M_RUFO = "Su perrito Rufo la esperaba en la puerta cada tarde"
M_VIDEO = "Hace videollamadas con sus nietas los domingos por la tarde"
M_TEJER = "Aprendió a tejer con su madre en Chillán"
M_SOPAIPILLAS = "Los domingos hacía sopaipillas con su hermana"
M_PATIO = "En el patio de la casa vieja crecían rosas y tomates"
M_CANTO = "Su hermana y ella cantaban en las tardes de verano"
M_INVERNO = "Los inviernos de Chillán eran de lluvia y pan amasado"
# Señuelos contradictorios (H4): mismo eje léxico, recuerdo falso
M_RUFO_FALSO = "Rufo era el gato de su vecina de al lado"
M_NIETO_FALSO = "Las videollamadas con sus nietas eran los lunes por la noche"
M_LLUVIA_FALSO = "Recuerda que odiaba la lluvia de Chillán de niña"
# Señuelos de guía (H4): vocabulario que colisiona con recuerdos
G_CLAVES = ("Nunca comparta las claves de su banco por teléfono: "
            "ningún banco las pide")
G_VIDEO = ("Para videollamar abra la aplicación de la cámara y toque "
           "el nombre de su contacto")
# Memorias de otro dominio (H7): registradas en el índice, referencia académica
M_ACAD_REGRESION = "la regresión lineal del curso de datos"
M_ACAD_MATRIZ = "la matriz de confusión del certamen"
M_ACAD_MELBOURNE = "el dataset de Melbourne con precios de casas"
M_ACAD_SPLIT = "los splits de entrenamiento validación y prueba"

# clave -> (texto, referencia): dominio deducido de la referencia ("academico:")
FIXTURE = [
    ("rufo", M_RUFO, "sesion eval"),
    ("video", M_VIDEO, "sesion eval"),
    ("tejer", M_TEJER, "sesion eval"),
    ("sopaipillas", M_SOPAIPILLAS, "sesion eval"),
    ("patio", M_PATIO, "sesion eval"),
    ("canto", M_CANTO, "sesion eval"),
    ("inverno", M_INVERNO, "sesion eval"),
    ("rufo_falso", M_RUFO_FALSO, "sesion eval"),
    ("nieto_falso", M_NIETO_FALSO, "sesion eval"),
    ("lluvia_falso", M_LLUVIA_FALSO, "sesion eval"),
    ("claves", G_CLAVES, "guia: anti-estafa"),
    ("guia_video", G_VIDEO, "guia: videollamada"),
    ("acad_regresion", M_ACAD_REGRESION, "academico: curso"),
    ("acad_matriz", M_ACAD_MATRIZ, "academico: curso"),
    ("acad_melbourne", M_ACAD_MELBOURNE, "academico: curso"),
    ("acad_split", M_ACAD_SPLIT, "academico: curso"),
]


@dataclass
class Sonda:
    consulta: str
    objetivo: str | None = None     # fid esperado (MRR/P@3)
    senuelo: str | None = None      # fid que no debe aparecer en el top-K
    cross: bool = False             # True = senuelo de OTRO dominio (H7)
    dominio: str = cerebro.DOMINIO_COMPANIA


@dataclass
class Resultado:
    mrr: float = 0.0
    p3: float = 0.0
    rechazo_senuelos: float = 0.0   # fracción de señuelos H4 fuera del top-K
    fuga_dominio: int = 0           # senuelos cross-domain que sí aparecieron
    validez: float = 1.0            # fracción de fids que validan evidencia
    n: int = 0
    detalle: dict = field(default_factory=dict)


# 20 sondas: 10 objetivo compañía, 6 señuelos H4 (3 guía + 3 contradictorios
# nuevos/legacy), 4 cross-domain H7 (la fuga se mide en ambos recuperadores).
SONDAS = [
    # objetivo compañía
    Sonda("cuénteme de Rufo, ese perrito", objetivo="rufo", senuelo="rufo_falso"),
    Sonda("las videollamadas con sus nietas", objetivo="video"),
    Sonda("aprendió a tejer con su madre", objetivo="tejer"),
    Sonda("las sopaipillas de domingo", objetivo="sopaipillas"),
    Sonda("el patio con rosas y tomates", objetivo="patio"),
    Sonda("las tardes de canto con su hermana", objetivo="canto"),
    Sonda("los inviernos de Chillán con lluvia", objetivo="inverno"),
    Sonda("qué hacía los domingos con su hermana", objetivo="sopaipillas"),
    Sonda("su hermana y ella cantando", objetivo="canto"),
    Sonda("los domingos y las niñas por videollamada", objetivo="video"),
    # señuelos H4 (guías con vocabulario colisionante)
    Sonda("claves banco teléfono", senuelo="claves"),
    Sonda("cómo videollamar a su familia sola", senuelo="guia_video"),
    Sonda("videollamadas de los lunes con las niñas", senuelo="nieto_falso"),
    Sonda("la lluvia de Chillán y el rencor", senuelo="lluvia_falso"),
    Sonda("rufo gato vecina", senuelo="rufo_falso"),
    Sonda("mensaje urgente del banco pidiendo claves", senuelo="claves"),
    # cross-domain H7: consulta académica, recuperación en dominio compañía
    Sonda("la regresión lineal del curso de datos", senuelo="acad_regresion",
          cross=True),
    Sonda("la matriz de confusión del certamen", senuelo="acad_matriz",
          cross=True),
    Sonda("el dataset de Melbourne con precios", senuelo="acad_melbourne",
          cross=True),
    Sonda("los splits de entrenamiento y prueba", senuelo="acad_split",
          cross=True),
]

# 8 sondas de validación CONGELADAS (E-17): se reportan en cada corrida pero
# NO entran al bootstrap ni a la decisión; son la batería fija para comparar
# contra futuras versiones del cerebro sin selección sesgada.
SONDAS_CONGELADAS = [
    Sonda("los domingos de su perrito en la puerta", objetivo="rufo"),
    Sonda("su madre y el telar en el invierno", objetivo="tejer"),
    Sonda("las rosas que veía por videollamada", objetivo="patio"),
    Sonda("el pan amasado que hacía su hermana", objetivo="inverno"),
    Sonda("me pidieron datos de mi cuenta bancaria", senuelo="claves"),
    Sonda("la cámara del teléfono para ver a las niñas", senuelo="guia_video"),
    Sonda("el certamen y sus notas del curso", senuelo="acad_matriz", cross=True),
    Sonda("los precios de casas para la tarea", senuelo="acad_melbourne",
          cross=True),
]


def construir_indice() -> tuple[Indice, dict[str, str]]:
    """Índice con objetivos, señuelos y memorias académicas; {clave: fid}."""
    ind = Indice()
    fids = {}
    for clave, texto, ref in FIXTURE:
        fids[clave] = ind.registrar_recuerdo(texto, referencia=ref)
    return ind, fids


def entrenar(cer: cerebro.Cerebro, ind: Indice, fids: dict[str, str]) -> None:
    """Episodios previos: los señuelos contradictorios quedan ligados a una
    alerta (valencia negativa) y los objetivos se refuerzan en éxito."""
    episodios = (
        ("Hoy vi al gato de la vecina y me sentí confundida y triste",
         {"nivel": "alerta", "senales": ["tristeza"]}),
        ("Cuénteme de mi perrito Rufo que me esperaba en la puerta", None),
        ("Videollamo a mis nietas los domingos por la tarde", None),
        # memoria contradictoria nueva (E-16): alerta sobre "lunes por la noche"
        ("Anoche soñé que las videollamadas eran los lunes y me angustié",
         {"nivel": "alerta", "senales": ["angustia"]}),
        # alerta sobre la "lluvia de Chillán" (odiarla contradice la nostalgia)
        ("Hablé de la lluvia de Chillán y me puse muy triste",
         {"nivel": "alerta", "senales": ["tristeza"]}),
    )
    for mensaje, senal in episodios:
        cer.ciclo(mensaje, indice=ind, senal=senal)
    # Las memorias académicas existen en el índice (validan), pero su dominio
    # en el grafo es "academico": así la única defensa posible es el filtro.
    sincronizados = {n.metadata.get("fid"): n for n in cer.grafo.nodes()
                     if n.metadata.get("kind") in ("memoria", "guia")}
    for clave, fid in fids.items():
        if clave.startswith("acad_") and fid in sincronizados:
            sincronizados[fid].metadata["domain"] = "academico"
    cer.guardar()


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
                 ind: Indice, sondas: list[Sonda] | None = None) -> Resultado:
    res = Resultado()
    rr_sum = p3_sum = rechazo = val_sum = 0.0
    n_obj = n_sen = 0
    for sonda in (sondas or SONDAS):
        ranking = rankings[sonda.consulta]
        res.n += 1
        objetivo = fids.get(sonda.objetivo) if sonda.objetivo else None
        if objetivo:
            n_obj += 1
            try:
                rango = ranking.index(objetivo) + 1
            except ValueError:
                rango = 0
            rr_sum += 1.0 / rango if rango else 0.0
            p3_sum += 1.0 if rango and rango <= K else 0.0
        senuelo = fids.get(sonda.senuelo) if sonda.senuelo else None
        if senuelo:
            if sonda.cross:
                # H7: un fid de otro dominio en la recuperación ES fuga
                res.fuga_dominio += 1 if senuelo in ranking[:K] else 0
            else:
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


def filas_por_sonda(rankings: dict[str, list[str]],
                    fids: dict[str, str],
                    sondas: list[Sonda]) -> dict[str, dict]:
    """Filas por sonda en la forma que ``_agrega`` de aal consume (#337).

    score_esperada: RR del objetivo (si hay) promediado con el éxito del
    señuelo (1 = rechazado/fuera del dominio). aplicada_ok: todo bien en la
    sonda. rr_leccion: 0 (no rankeamos lecciones, como el rival de aal).
    """
    filas = {}
    for s in sondas:
        ranking = rankings[s.consulta]
        partes, score, ok = 0, 0.0, True
        if s.objetivo:
            partes += 1
            obj = fids[s.objetivo]
            rango = (ranking.index(obj) + 1) if obj in ranking else 0
            score += 1.0 / rango if rango else 0.0
            ok = ok and bool(rango and rango <= K)
        if s.senuelo:
            partes += 1
            sen = fids[s.senuelo]
            bien = sen not in ranking[:K]
            score += 1.0 if bien else 0.0
            ok = ok and bien
        filas[s.consulta] = {"score_esperada": round(score / max(partes, 1), 6),
                             "aplicada_ok": ok, "rr_leccion": 0.0}
    return filas


def ranking_rival_tfidf(cer, consulta: str, k: int = K) -> list[str]:
    """Rival #337: TF-IDF de 1 salto sobre el MISMO grafo, cero propagación.

    El documento de cada memoria es su etiqueta + la de sus vecinos a 1 salto;
    la consulta rankea por coseno. Núcleo importado de
    ``associative_agent_loop.evaluation.rival``: si el spreading con valencia
    no le gana a esto, su complejidad no está pagando el alquiler.
    """
    piso = _piso_inferencial()
    if piso is None:
        return []
    mg = cer.grafo
    docs: dict[str, str] = {}
    for nodo in mg.nodes():
        if nodo.metadata.get("kind") != "memoria" \
                or nodo.metadata.get("domain", "compania") != "compania":
            continue
        fid = nodo.metadata.get("fid")
        if not fid:
            continue
        vecindad = [nodo.label]
        for _, otro, _ in mg.out_edges(nodo.id):
            vecindad.append(mg.node(otro).label)
        for origen, _, _ in mg.in_edges(nodo.id):
            vecindad.append(mg.node(origen).label)
        docs[fid] = " ".join(vecindad)
    tokens = {f: piso["tokenize"](t) for f, t in docs.items()}
    df: Counter = Counter()
    for ts in tokens.values():
        for t in set(ts):
            df[t] += 1
    n_docs = max(len(tokens), 1)
    q = piso["_tfidf_vector"](piso["tokenize"](consulta), df, n_docs)
    scores = {f: piso["_coseno"](q, piso["_tfidf_vector"](ts, df, n_docs))
              for f, ts in tokens.items()}
    return [f for f, _ in sorted(scores.items(), key=lambda kv: -kv[1])[:k]
            if scores[f] > 0]


# ------------------------------------------------------- corpus denso (#335)
_DENSO_SUJETOS = ["mi hermana", "mi madre", "mi nieta", "mi vecina", "mi primo"]
_DENSO_VERBOS = ["cocinaba", "tejía", "cantaba", "preparaba", "guardaba"]
_DENSO_OBJETOS = ["sopaipillas", "pan amasado", "rosas", "lanas", "empanadas"]
_DENSO_LUGARES = ["en la cocina", "en el patio", "en el pueblo",
                  "en la casa vieja", "los domingos"]
DENSO_N = len(_DENSO_SUJETOS) * 11   # 55 recuerdos


def _recuerdos_densos() -> list[str]:
    """55 recuerdos sintéticos con vocabulario COMPARTIDO denso: cada token
    aparece en ~11 documentos, el caso donde el spreading diluye (estilo #335
    del repo hermano, donde el recall colapsó con corpus grande)."""
    recuerdos = []
    for i in range(DENSO_N):
        s = _DENSO_SUJETOS[i % 5]
        v = _DENSO_VERBOS[(i // 5) % 5]
        o = _DENSO_OBJETOS[(i // 25) % 5]
        l = _DENSO_LUGARES[i % 5]
        recuerdos.append(f"{s.capitalize()} {v} {o} {l} cuando era niña")
    return recuerdos


def eval_corpus_denso(curso=None) -> dict:
    """Sonda crítica: ¿el recall@3 del cerebro sobrevive al corpus denso?

    Devuelve recall@3 del cerebro, del índice TF-IDF propio y del rival
    TF-IDF de aal sobre el mismo grafo, con 10 consultas de objetivo conocido.
    ``colapso`` = cerebro por debajo del mejor baseline (esa es la señal #335).
    """
    ind = Indice()
    fids = {}
    for i, texto in enumerate(_recuerdos_densos()):
        fids[i] = ind.registrar_recuerdo(texto, referencia="sesion densa")
    if curso is None:
        from pathlib import Path

        from . import config
        from .modelo import crear

        tmp = tempfile.TemporaryDirectory(prefix="e17-denso-")
        config.DIR_CURSOS = Path(tmp.name) / "cursos"
        curso = crear("evaldenso", nombre="Denso", periodo="eval")
        curso.datos["modo"] = "compania"
        curso.datos["cerebro"] = "aal"
        curso.guardar()
    cer = cerebro.Cerebro(curso)
    cer.sincronizar_indice(ind)
    consultas = [(f"{_DENSO_SUJETOS[i % 5]} y {_DENSO_OBJETOS[(i // 25) % 5]}",
                  fids[i]) for i in range(0, DENSO_N, 5)]  # 10 consultas
    hits = {"cerebro": 0, "indice": 0, "rival": 0}
    for consulta, objetivo in consultas:
        if objetivo in ranking_cerebro(cer, ind, consulta):
            hits["cerebro"] += 1
        base = [fid for fid, _, _ in ind.buscar_asociativo(consulta, k=K)]
        if objetivo in base:
            hits["indice"] += 1
        if objetivo in ranking_rival_tfidf(cer, consulta):
            hits["rival"] += 1
    n = len(consultas)
    mejor_base = max(hits["indice"], hits["rival"])
    return {
        "recuerdos": DENSO_N,
        "consultas": n,
        "recall_cerebro": round(hits["cerebro"] / n, 3),
        "recall_indice": round(hits["indice"] / n, 3),
        "recall_rival_tfidf": round(hits["rival"] / n, 3),
        "colapso": hits["cerebro"] < mejor_base,
    }


def comparar(curso_factory=None) -> dict:
    """Cara a cara con el piso inferencial de ALL #337 (E-17)."""
    ind, fids = construir_indice()

    base = evaluar_lado({s.consulta: ranking_baseline(ind, s.consulta)
                         for s in SONDAS}, fids, ind)

    salida = {"baseline": base.__dict__, "cerebro": None,
              "decision": "opt_in", "n_sondas": len(SONDAS),
              "sondas_congeladas": None, "bootstrap": None,
              "corpus_denso": None,
              "regla": ("#337: adoptar solo si sin regresión (E-15), con "
                        "mejora estricta, IC95 del Δ con p2.5>0 y corpus denso "
                        "sin colapso; si no, opt-in")}

    if not cerebro.AAL:
        salida["motivo"] = "aal no instalado: cerebro no evaluable (opt-in)"
        return salida

    if curso_factory is None:
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
    salida["cerebro"] = cero.__dict__

    # Piso inferencial #337: filas por sonda + bootstrap importado + rival.
    piso = _piso_inferencial()
    if piso is not None:
        filas_b = filas_por_sonda({s.consulta: ranking_baseline(ind, s.consulta)
                                   for s in SONDAS}, fids, SONDAS)
        filas_c = filas_por_sonda(rank_cer, fids, SONDAS)
        boot = piso["bootstrap_ganancia"](filas_b, filas_c)
        boot["significativo"] = piso["significa"](boot)
        salida["bootstrap"] = boot
        # Rival TF-IDF (1 salto, mismo grafo) rankea las 20 sondas también.
        rank_rival = {s.consulta: ranking_rival_tfidf(cer, s.consulta)
                      for s in SONDAS}
        rival = evaluar_lado(rank_rival, fids, ind)
        rival.__dict__["detalle"] = {}
        salida["rival_tfidf"] = rival.__dict__
        # Sondas CONGELADAS: se reportan, no se seleccionan.
        salida["sondas_congeladas"] = {
            "n": len(SONDAS_CONGELADAS),
            "baseline": evaluar_lado(
                {s.consulta: ranking_baseline(ind, s.consulta)
                 for s in SONDAS_CONGELADAS}, fids, ind,
                sondas=SONDAS_CONGELADAS).__dict__,
            "cerebro": evaluar_lado(
                {s.consulta: ranking_cerebro(cer, ind, s.consulta,
                                             dominio=s.dominio)
                 for s in SONDAS_CONGELADAS}, fids, ind,
                sondas=SONDAS_CONGELADAS).__dict__,
        }
        salida["corpus_denso"] = eval_corpus_denso()
    salida["decision"] = _decision(base, cero, salida["repeticion"],
                                   salida["bootstrap"],
                                   salida["corpus_denso"])
    return salida


def _decision(base: Resultado, cero: Resultado, rep: dict,
              boot: dict | None, denso: dict | None) -> str:
    """E-15 + #337: opt_in ante regresión, IC que toca el cero o corpus denso
    que colapsa. adoptar exige todo: sin regresión, mejora estricta,
    p2.5>0 y recall denso >= baseline."""
    if cero.validez < 1.0 or cero.fuga_dominio > 0 or not rep.get("rufo_unico"):
        return "opt_in"
    regresion = any(getattr(cero, m) < getattr(base, m)
                    for m in ("mrr", "p3", "rechazo_senuelos"))
    mejora = any(getattr(cero, m) > getattr(base, m)
                 for m in ("mrr", "p3", "rechazo_senuelos"))
    if regresion or not mejora:
        return "opt_in"
    if boot is not None and not boot.get("significativo"):
        return "opt_in"
    if denso is not None and denso.get("colapso"):
        return "opt_in"
    return "adoptar"


def main() -> None:  # pragma: no cover - CLI
    print(json.dumps(comparar(), indent=2, ensure_ascii=False))


if __name__ == "__main__":  # pragma: no cover
    main()
