"""Cerebro asociativo de Datito (E-15): memoria episódica en grafo sobre aal.

Fachada sobre el proyecto hermano ``associative-agent-loop`` (aal). Cada turno
de modo compañía ejecuta el ciclo PLAN → RETRIEVE → ACT → OBSERVE → CONSOLIDATE
y persiste el grafo de forma atómica en ``<curso>/.cerebro/grafo.json``.

D-15.1 (zero-lock-in): aal es una dependencia **opcional** detectada en runtime.
Sin aal, ``AAL`` es False, ``habilitado()`` devuelve False y todas las funciones
degradan limpio: el índice TF-IDF (indice.py) sigue siendo la única memoria,
exactamente como en E-10..E-14. Ni el zip del paquete ni CI instalan aal.

Garantías no negociables (D-15.2):
- Todo recuerdo evocado en una respuesta pasa por ``evidencia.validar``:
  el cerebro sugiere, la evidencia decide (cero recuerdos inventados).
- Ante fraude (D-11.3) el relato del engaño **no** se consolida.
- Las alertas (kind="alerta") jamás son recuperables como recuerdo.
"""
from __future__ import annotations

import importlib.util
import json
import math
import re
from pathlib import Path

from . import evidencia

# --------------------------------------------------------------------- aal
_AAL_SPEC = importlib.util.find_spec("associative_agent_loop")
AAL = _AAL_SPEC is not None

if AAL:  # pragma: no branch - trivial
    from associative_agent_loop import MemoryGraph, NodeType
    from associative_agent_loop.memory.associative import RetrievalConfig, Retriever
    from associative_agent_loop.memory.consolidation import Consolidator
    from associative_agent_loop.memory.models import Relation
    from associative_agent_loop.memory.store import JsonGraphStore

    try:
        from importlib.metadata import version

        VERSION_AAL = version("associative-agent-loop")
    except Exception:  # pragma: no cover - metadata siempre presente instalado
        VERSION_AAL = "desconocida"
else:
    MemoryGraph = NodeType = Relation = RetrievalConfig = None  # type: ignore[assignment]
    Retriever = Consolidator = JsonGraphStore = None  # type: ignore[assignment]
    VERSION_AAL = None

DOMINIO_COMPANIA = "compania"
KINDS_RECUPERABLES = ("memoria", "guia")
RECURRENCIA_NUCLEAR = 3       # usos validados para proteger de la poda (D-15.2)
PODA_CADA = 12                # episodios entre podas deterministas
UMBRAL_ENLACE = 0.05          # activación mínima para enlazar contexto al episodio
SLUG_RE = re.compile(r"[^a-z0-9]+")

# Decisión D-15.3 (fijada por el experimento de eval_cerebro.py): "adoptar" si
# el cerebro gana pareado con regresión cero; "opt_in" si empata o regresa.
ADOPCION = "adoptar"


# -------------------------------------------------------------- utilidades
def _slug(texto: str, max_len: int = 48) -> str:
    return SLUG_RE.sub("_", texto.lower()).strip("_")[:max_len] or "x"


def _fuerza_aal() -> None:
    """Test hook: fuerza la detección de aal (usado solo en tests con mock)."""
    global AAL, MemoryGraph, NodeType, Relation, RetrievalConfig, Retriever
    global Consolidator, JsonGraphStore, VERSION_AAL
    AAL = True
    from associative_agent_loop import MemoryGraph as _MG, NodeType as _NT
    from associative_agent_loop.memory.associative import RetrievalConfig as _RC, Retriever as _Rt
    from associative_agent_loop.memory.consolidation import Consolidator as _C
    from associative_agent_loop.memory.models import Relation as _R
    from associative_agent_loop.memory.store import JsonGraphStore as _JS

    MemoryGraph, NodeType, Relation = _MG, _NT, _R
    RetrievalConfig, Retriever = _RC, _Rt
    Consolidator, JsonGraphStore = _C, _JS
    VERSION_AAL = "mock"


def info() -> dict:
    """Estado global del cerebro para GET /api/salud (D-15.1)."""
    return {
        "activo": AAL,
        "motor": "aal" if AAL else None,
        "version": VERSION_AAL,
        "adopcion": ADOPCION if AAL else None,
        "guia": ("uv pip install --python .venv/bin/python -e "
                 "../Agents_Learning_Loops") if not AAL else None,
    }


def preferencia(curso) -> str:
    """Preferencia del curso: 'auto' (default), 'aal' (opt-in) u 'off'."""
    return str((getattr(curso, "datos", None) or {}).get("cerebro", "auto")).lower()


def habilitado(curso) -> bool:
    """El cerebro opera en este curso (solo compañía, D-15.1/D-15.3)."""
    if not AAL:
        return False
    from . import identidad

    if not identidad.es_compania(curso):
        return False
    pref = preferencia(curso)
    if pref == "off":
        return False
    if pref == "aal":
        return True
    return ADOPCION == "adoptar"


def ruta_grafo(curso) -> Path:
    return curso.ruta(".cerebro") / "grafo.json"


def estadisticas(curso) -> dict:
    """Nodos/aristas/episodios del grafo del curso ({} si no hay)."""
    base = info()
    ruta = ruta_grafo(curso)
    if not AAL or not ruta.exists():
        return {**base, "nodos": 0, "aristas": 0, "episodios": 0}
    datos = json.loads(ruta.read_text("utf-8"))
    return {**base, "nodos": len(datos.get("nodes", [])),
            "aristas": len(datos.get("edges", [])),
            "episodios": datos.get("clock", 0)}


# ------------------------------------------------------------------ cerebro
class Cerebro:
    """Grafo episódico de un curso: ciclo por turno y recuperación con trazas.

    PLAN     resumir el mensaje como meta del episodio (tick del reloj lógico)
    RETRIEVE siembra + activación propagada sobre el grafo (con traza de camino)
    ACT      registrar episodio: meta → temas → recuerdos evocados → respuesta
    OBSERVE  outcome con signo (+ éxito / − alerta de bienestar)
    CONSOLIDATE hebbiano con signo + EMA, marca nuclear, decaimiento y poda
    """

    def __init__(self, curso):
        if not AAL:
            raise RuntimeError("aal no disponible (D-15.1: usar solo tras habilitado())")
        self.curso = curso
        self.dir = curso.ruta(".cerebro")
        self.dir.mkdir(parents=True, exist_ok=True)
        self.store = JsonGraphStore(self.dir / "grafo.json")
        self.grafo = self.store.load_or_new(decay_rate=0.04)
        self.recuperador = Retriever(
            self.grafo,
            config=RetrievalConfig(damping=0.7, max_hops=3, alpha=0.65,
                                   min_seed_similarity=0.2, seed_top_k=16),
        )
        self.consolidador = Consolidator(self.grafo, prune_threshold=0.02)

    # ------------------------------------------------------------ persistencia
    def guardar(self) -> None:
        self.store.save(self.grafo)

    # ------------------------------------------------------------ sincronía
    def sincronizar_indice(self, indice, dominio: str = DOMINIO_COMPANIA) -> int:
        """Crea nodos memoria/guia para los fids del índice aún ausentes.

        El texto del índice es la fuente de verdad: el cerebro nunca guarda
        un recuerdo que la evidencia no pueda validar (D-15.2).
        """
        creados = 0
        mg = self.grafo
        for fid, texto in indice.textos.items():
            es_memoria = fid.startswith("memoria#")
            ref = indice.referencias.get(fid, ("", ""))[1]
            es_guia = ref.startswith("guia") or fid.startswith("guia")
            if not (es_memoria or es_guia):
                continue
            # una memoria# con referencia de guía ES guía (anclaje anti-estafa)
            kind = "guia" if es_guia else "memoria"
            nodo = f"concept:{kind}:{_slug(texto, 60)}"
            if mg.has_node(nodo):
                continue
            mg.add_node(nodo, NodeType.CONCEPT, texto[:240], kind=kind,
                        fid=fid, domain=dominio, usos=0)
            self._enlazar_temas(nodo, texto, dominio)
            creados += 1
        return creados

    def _enlazar_temas(self, nodo: str, texto: str, dominio: str) -> None:
        """Aristas memoria↔tema: los temas son los puentes de la propagación."""
        from associative_agent_loop.memory.associative import topic_id

        mg = self.grafo
        for token in dict.fromkeys(_tokens(texto)):
            tema = topic_id(token)
            if not mg.has_node(tema):
                mg.add_node(tema, NodeType.CONCEPT, token, kind="topic",
                            domain=dominio)
            mg.add_edge(nodo, tema, Relation.ASSOCIATED_WITH, weight=0.35)

    # ------------------------------------------------------------------ ciclo
    def ciclo(self, mensaje: str, respuesta: str = "", indice=None,
              senal: dict | None = None,
              dominio: str = DOMINIO_COMPANIA, registrar: bool = True) -> list[dict]:
        """Ejecuta PLAN→RETRIEVE→ACT→OBSERVE→CONSOLIDATE y persiste atómicamente.

        Devuelve las asociaciones recuperadas este turno (fid validado,
        activación, camino/traza). Con ``registrar=False`` (fraude, D-11.3)
        solo se recupera y observa: nada del relato se consolida.
        """
        mg = self.grafo
        ep = mg.tick()
        if indice is not None:
            self.sincronizar_indice(indice, dominio)
        asociaciones = self.recuperar(mensaje, k=3, indice=indice, dominio=dominio)
        if registrar:
            self._registrar_episodio(ep, mensaje, respuesta, asociaciones,
                                     senal, dominio)
            if ep % PODA_CADA == 0:
                self._olvidar()
        self.guardar()
        return asociaciones

    def _registrar_episodio(self, ep: int, mensaje: str, respuesta: str,
                            asociaciones: list[dict], senal: dict | None,
                            dominio: str) -> None:
        mg = self.grafo
        cons = self.consolidador
        goal = f"goal:ep{ep}"
        mg.add_node(goal, NodeType.GOAL, mensaje[:200], kind="episodio",
                    domain=dominio, episode=ep)
        for token in dict.fromkeys(_tokens(mensaje)):
            from associative_agent_loop.memory.associative import topic_id

            tema = topic_id(token)
            if not mg.has_node(tema):
                mg.add_node(tema, NodeType.CONCEPT, token, kind="topic",
                            domain=dominio)
            mg.add_edge(goal, tema, Relation.ASSOCIATED_WITH, weight=0.4)

        # ACT: el contexto recuperado enlaza la meta con los recuerdos vivos.
        for a in asociaciones:
            nodo = a["nodo"]
            if mg.has_node(nodo):
                cons.reinforce(goal, nodo, Relation.ASSOCIATED_WITH, 0.8)
                mg.node(nodo).metadata["usos"] = \
                    int(mg.node(nodo).metadata.get("usos", 0)) + 1

        accion = mg.add_node("action:responder", NodeType.ACTION,
                             "responder con calidez", domain=dominio)
        mg.add_edge(goal, accion, Relation.LEADS_TO, weight=0.5)
        exito = not senal or senal.get("nivel", "ok") == "ok"
        outcome = mg.add_node(
            f"outcome:ep{ep}:1", NodeType.OUTCOME,
            "success" if exito else "senal de alerta",
            success=exito, episode=ep, domain=dominio,
            senales=(senal or {}).get("senales", []))
        mg.add_edge(accion, outcome, Relation.LEADS_TO, weight=1.0)

        # OBSERVE + CONSOLIDATE: hebbiano con signo sobre la ruta del episodio.
        cons.hebbian(goal, accion, Relation.LEADS_TO, 1.0, 1.0, 1 if exito else -1)
        if exito:
            cons.reinforce(goal, accion, Relation.RESOLVED_BY, 1.0)
        else:
            alerta = mg.add_node(
                f"concept:alerta:{ep}", NodeType.CONCEPT,
                "alerta de bienestar", kind="alerta", domain=dominio,
                episode=ep, senales=(senal or {}).get("senales", []))
            mg.add_edge(outcome, alerta, Relation.FAILED_DUE_TO, weight=1.0)
            # Valencia negativa para lo que se evocó en el momento de la
            # angustia: queda asociado, pero se recupera menos (lección H4).
            for a in asociaciones:
                if a["kind"] == "memoria" and mg.has_node(a["nodo"]):
                    mg.add_edge(a["nodo"], alerta, Relation.FAILED_DUE_TO,
                                weight=1.0)

    def _olvidar(self) -> None:
        """Decaimiento materializado + poda protegiendo lo nuclear (D-15.2)."""
        mg = self.grafo
        cons = self.consolidador
        cons.decay()
        for nodo in mg.nodes():
            if nodo.metadata.get("kind") == "memoria" and \
                    int(nodo.metadata.get("usos", 0)) >= RECURRENCIA_NUCLEAR:
                nodo.metadata["nuclear"] = True
        # Refuerzo preventivo: una arista nuclear nunca cae bajo el umbral de poda.
        for nodo in mg.nodes():
            if not nodo.metadata.get("nuclear"):
                continue
            for _, dst, edge in list(mg.out_edges(nodo.id)):
                edge.weight = 1.0
                edge.last_updated = mg.clock
            for src, _, edge in list(mg.in_edges(nodo.id)):
                edge.weight = 1.0
                edge.last_updated = mg.clock
        cons.prune()
        self.guardar()

    # ------------------------------------------------------------ recuperación
    def recuperar(self, consulta: str, k: int = 4, indice=None,
                  dominio: str = DOMINIO_COMPANIA,
                  kinds: tuple[str, ...] = KINDS_RECUPERABLES) -> list[dict]:
        """Recuerdos asociados con su traza (camino semilla→puente→recuerdo).

        Filtros duros (anti H7/H8): mismo ``dominio``, kind recuperable,
        nunca alertas. Valencia contextual (éxitos/fallos del propio nodo)
        modula el puntaje: un recuerdo asociado a fracaso pesa menos.
        """
        mg = self.grafo
        if not consulta.strip():
            return []
        semillas = self.recuperador.seed(consulta)
        propagacion = self.recuperador.spread_trace(semillas)
        resultados = []
        for nodo in mg.nodes():
            if nodo.metadata.get("kind") not in kinds:
                continue
            if nodo.metadata.get("domain", dominio) != dominio:
                continue
            activacion = propagacion.activation.get(nodo.id, 0.0)
            if activacion <= 0:
                continue
            valencia = self._valencia(nodo.id)
            # compuerta de bienestar (anti-H4): lo ligado a angustia no se
            # evoca de forma proactiva; queda en el grafo, no en el saludo
            if valencia <= -0.5:
                continue
            puntaje = activacion * (0.5 + 0.5 * valencia)
            camino = [mg.node(p).label for p in propagacion.path_to(nodo.id)]
            fid = nodo.metadata.get("fid", "")
            if indice is not None and fid:
                # la etiqueta es el propio texto del índice: supera la regla
                # MIN_OVERLAP de la evidencia sin trampa (D-15.2)
                if not evidencia.validar(f"{nodo.label} [{fid}]", indice).ok:
                    continue  # cero recuerdos inventados (D-15.2)
            resultados.append({
                "nodo": nodo.id, "fid": fid, "etiqueta": nodo.label,
                "kind": nodo.metadata["kind"], "activacion": round(activacion, 4),
                "valencia": round(valencia, 4), "puntaje": round(puntaje, 4),
                "camino": camino,
            })
        resultados.sort(key=lambda r: -r["puntaje"])
        return resultados[:k]

    def _valencia(self, nodo: str) -> float:
        """tanh(Σ RESOLVED_BY entrantes − Σ FAILED_DUE_TO salientes) efectivos."""
        mg = self.grafo
        pos = sum(mg.effective_weight(e)
                  for *_, e in mg.in_edges(nodo, Relation.RESOLVED_BY))
        neg = sum(mg.effective_weight(e)
                  for *_, e in mg.out_edges(nodo, Relation.FAILED_DUE_TO))
        return math.tanh(pos - neg)


# ------------------------------------------------------------- sugerencias
def para_curso(curso) -> Cerebro | None:
    """Instancia del cerebro para el curso, o None si no está habilitado."""
    if not habilitado(curso):
        return None
    return Cerebro(curso)


def _rotacion(curso, clave: str, fid: str, tope: int = 4) -> None:
    from . import progreso

    datos = progreso.cargar(curso)
    usados = [f for f in datos.get(clave, []) if f != fid][: tope - 1]
    datos[clave] = [fid, *usados]
    progreso.guardar(curso, datos)


def sugerir_apertura(curso, indice) -> str | None:
    """Recuerdo semilla para la apertura proactiva (D-11.1 + trazas E-15).

    Elige el recuerdo de mayor grado efectivo (más conectado = más vivo en el
    grafo), rotando para no repetir el mismo cada día. Fallback: None y
    apertura conserva su round-robin actual.
    """
    cer = para_curso(curso)
    if cer is None:
        return None
    cer.sincronizar_indice(indice)
    from . import progreso

    usados = progreso.cargar(curso).get("cerebro_apertura", [])
    mejor, mejor_grado = None, -1.0
    for nodo in cer.grafo.nodes():
        if nodo.metadata.get("kind") != "memoria":
            continue
        fid = nodo.metadata.get("fid", "")
        if not fid or fid not in indice.textos:
            continue
        if fid in usados:
            continue
        grado = sum(cer.grafo.effective_weight(e)
                    for *_, e in list(cer.grafo.out_edges(nodo.id))
                    + list(cer.grafo.in_edges(nodo.id)))
        peso = grado + 0.01 * int(nodo.metadata.get("usos", 0))
        if peso > mejor_grado:
            mejor, mejor_grado = fid, peso
    if mejor is None:  # todos usados recientemente: reiniciar rotación
        for nodo in cer.grafo.nodes():
            if nodo.metadata.get("kind") == "memoria" and \
                    nodo.metadata.get("fid", "") in indice.textos:
                mejor = nodo.metadata["fid"]
                break
    if mejor:
        _rotacion(curso, "cerebro_apertura", mejor)
        cer.guardar()
    return mejor


def sugerir_reminiscencia(curso, indice) -> str | None:
    """Memoria rica para el ejercicio de reminiscencia guiada (3 pistas)."""
    cer = para_curso(curso)
    if cer is None:
        return None
    cer.sincronizar_indice(indice)
    from . import progreso

    usados = progreso.cargar(curso).get("cerebro_reminiscencia", [])
    candidatas = [
        (len(list(cer.grafo.out_edges(n.id)))
         + len(list(cer.grafo.in_edges(n.id)))
         + 0.01 * int(n.metadata.get("usos", 0)), n.metadata.get("fid", ""))
        for n in cer.grafo.nodes()
        if n.metadata.get("kind") == "memoria"
        and n.metadata.get("fid", "") in indice.textos
        and n.metadata.get("fid", "") not in usados
    ]
    if not candidatas:
        return None
    candidatas.sort(key=lambda t: -t[0])
    fid = candidatas[0][1]
    _rotacion(curso, "cerebro_reminiscencia", fid)
    cer.guardar()
    return fid


def orden_entidades(curso) -> dict[str, int]:
    """Rango de activación de temas/entidades para ordenar la biografía.

    Devuelve {etiqueta_tema: rango} de mayor a menor conexión efectiva.
    """
    cer = para_curso(curso)
    if cer is None:
        return {}
    temas = []
    for nodo in cer.grafo.nodes():
        if nodo.metadata.get("kind") != "topic":
            continue
        grado = sum(cer.grafo.effective_weight(e)
                    for *_, e in list(cer.grafo.out_edges(nodo.id))
                    + list(cer.grafo.in_edges(nodo.id)))
        temas.append((grado, nodo.label))
    temas.sort(key=lambda t: -t[0])
    return {etiqueta: i for i, (_, etiqueta) in enumerate(temas)}


def _tokens(texto: str) -> list[str]:
    import unicodedata

    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return [tok for tok in re.findall(r"[a-z0-9]+", t) if len(tok) > 2]
