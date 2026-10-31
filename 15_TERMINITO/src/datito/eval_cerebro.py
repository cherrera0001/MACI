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
                 ind: Indice) -> Resultado:
    res = Resultado()
    rr_sum = p3_sum = rechazo = val_sum = 0.0
    n_obj = n_sen = 0
    for sonda in SONDAS:
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


def comparar(curso_factory=None) -> dict:
    """Cara a cara baseline vs cerebro con el banco completo (20 sondas)."""
    ind, fids = construir_indice()

    base = evaluar_lado({s.consulta: ranking_baseline(ind, s.consulta)
                         for s in SONDAS}, fids, ind)

    salida = {"baseline": base.__dict__, "cerebro": None,
              "decision": "opt_in", "n_sondas": len(SONDAS),
              "regla": ("adoptar solo sin regresión en MRR/P@3/rechazo y con "
                        "mejora estricta en al menos una métrica; si no, opt-in")}

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
    salida["cerebro"] = cero.__dict__
    salida["decision"] = _decision(base, cero, salida["repeticion"])
    salida["nota_h7"] = (
        "La fuga de dominio se mide en AMBOS recuperadores: el baseline no "
        "tiene concepto de dominio y la sufre; el cerebro la filtra.")
    return salida


def _decision(base: Resultado, cero: Resultado, rep: dict) -> str:
    """D-15.3: adoptar solo sin regresión y con mejora estricta en algo."""
    if cero.validez < 1.0 or cero.fuga_dominio > 0 or not rep.get("rufo_unico"):
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
