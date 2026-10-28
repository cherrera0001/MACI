"""Servidor MCP (Model Context Protocol) sobre stdio para el runtime agentico.

Expone el motor pedagogico de Datito como herramientas para un orquestador de
agentes (p. ej. open-duet): progreso, grafo de dominio, distinciones y busqueda
sobre los materiales reales del curso. Transporte: JSON-RPC 2.0 newline-
delimited por stdin/stdout (protocolo MCP stdio). Sin dependencias nuevas.

Las herramientas de escritura (calificar_distincion, registrar_dominio) usan
las mismas funciones y esquemas que el CLI; ninguna inventa estado.

Uso:
    datito-mcp --curso fcd

Ver docs/MCP.md para el contrato de cada herramienta.
"""
from __future__ import annotations

import argparse
import json
import sys

from . import evaluador, grafo, modelo, progreso
from .indice import Indice

PROTOCOLO = "2025-06-18"

ES_ESCRITURA = {"calificar_distincion", "registrar_dominio"}

HERRAMIENTAS = [
    {
        "name": "progreso",
        "description": "Metricas de adopcion y micro-progreso de la sesion.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "grafo_dominio",
        "description": ("Nodos del grafo curricular con su estado de dominio "
                        "(no_estudiado, en_estudio, comprendido, dominado)."),
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "siguiente_concepto",
        "description": ("Siguiente concepto recomendado: no dominado, con los "
                        "prerrequisitos dominados; prioriza lo ya en estudio."),
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "distinciones_pendientes",
        "description": "Items de evaluacion por distinciones sin resultado guardado.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "calificar_distincion",
        "description": ("Califica la respuesta del estudiante a un item y guarda "
                        "el resultado (actualiza micro-progreso y dominio)."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "item_id": {"type": "string", "description": "id del item"},
                "respuesta": {"type": "string", "description": "respuesta escrita del estudiante"},
            },
            "required": ["item_id", "respuesta"],
        },
    },
    {
        "name": "buscar_materiales",
        "description": ("Busca en los materiales del curso (indice TF-IDF) y "
                        "devuelve los fragmentos mas relevantes con su fuente."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "consulta": {"type": "string"},
                "k": {"type": "integer", "default": 4},
            },
            "required": ["consulta"],
        },
    },
    {
        "name": "registrar_dominio",
        "description": ("Registra el resultado de una evaluacion sobre uno o mas "
                        "conceptos: logrado -> dominado; parcial/no_logrado -> en_estudio."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "conceptos": {"type": "array", "items": {"type": "string"}},
                "resultado": {"type": "string", "enum": ["logrado", "parcial", "no_logrado"]},
            },
            "required": ["conceptos", "resultado"],
        },
    },
]


class Servidor:
    """Nucleo del servidor MCP: despacha mensajes JSON-RPC sobre un curso."""

    def __init__(self, curso):
        self.curso = curso

    def manejar(self, mensaje: dict):
        """Devuelve la respuesta JSON-RPC, o None si es notificacion."""
        metodo = mensaje.get("method", "")
        if "id" not in mensaje:  # notificacion: acknowledged, sin respuesta
            return None
        mid = mensaje["id"]
        try:
            if metodo == "initialize":
                return self._respuesta(mid, {
                    "protocolVersion": PROTOCOLO,
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "datito-mcp",
                                   "version": self.curso.datos.get("version_motor", "0.1.0")},
                })
            if metodo == "tools/list":
                return self._respuesta(mid, {"tools": HERRAMIENTAS})
            if metodo == "tools/call":
                return self._llamada(mid, mensaje.get("params") or {})
            return self._error(mid, -32601, f"metodo desconocido: {metodo}")
        except Exception as e:  # un tool no debe tumbar el servidor
            return self._error(mid, -32603, f"{type(e).__name__}: {e}")

    def _llamada(self, mid: int, params: dict):
        nombre = params.get("name", "")
        args = params.get("arguments") or {}
        if nombre not in {h["name"] for h in HERRAMIENTAS}:
            return self._error(mid, -32602, f"herramienta desconocida: {nombre}")
        resultado = self._ejecutar(nombre, args)
        return self._respuesta(mid, {
            "content": [{"type": "text", "text": json.dumps(resultado, ensure_ascii=False)}],
            "isError": False,
        })

    def _ejecutar(self, nombre: str, args: dict):
        curso = self.curso
        if nombre == "progreso":
            datos = progreso.cargar(curso)
            return {"metricas": datos["metricas"], "resumen": progreso.resumen(curso)}
        if nombre == "grafo_dominio":
            g = grafo.cargar_grafo(curso)
            dom = grafo.cargar_dominio(curso)
            return {"nodos": [{"id": cid, "nombre": n.get("nombre", cid),
                               "estado": dom.get(cid, {}).get("estado", "no_estudiado")}
                              for cid, n in g.get("nodos", {}).items()]}
        if nombre == "siguiente_concepto":
            return {"siguiente": self._siguiente()}
        if nombre == "distinciones_pendientes":
            hechos = {r.get("item_id") for r in evaluador.cargar_resultados_guardados(curso)}
            return {"items": [{"id": it.id, "pregunta": it.pregunta,
                               "conceptos": it.conceptos}
                              for it in evaluador.cargar_items(curso) if it.id not in hechos]}
        if nombre == "calificar_distincion":
            item = next((it for it in evaluador.cargar_items(curso)
                         if it.id == args["item_id"]), None)
            if item is None:
                raise ValueError(f"item no existe: {args['item_id']}")
            res = evaluador.calificar(item, args["respuesta"])
            evaluador.guardar_resultado(curso, res)
            progreso.contar_distincion(curso, bool(getattr(res, "logrado", False)))
            grafo.actualizar_dominio(curso, item.conceptos,
                                     "logrado" if getattr(res, "logrado", False) else "no_logrado")
            return {"item_id": item.id, "logrado": bool(getattr(res, "logrado", False)),
                    "feedback": getattr(res, "feedback", "")}
        if nombre == "buscar_materiales":
            k = int(args.get("k", 4))
            if not curso.ruta(".indice", "manifest.json").exists():
                raise ValueError("sin indice todavia: correr 'datito build <slug>' primero")
            ind = Indice.cargar(curso.ruta(".indice"))
            return {"fragmentos": [
                {"fid": fid, "puntaje": round(puntaje, 4),
                 "fuente": ind.referencias.get(fid, ["", ""])[0],
                 "referencia": ind.referencias.get(fid, ["", ""])[1],
                 "texto": ind.textos.get(fid, "")}
                for fid, puntaje in ind.buscar(args["consulta"], k)]}
        if nombre == "registrar_dominio":
            grafo.actualizar_dominio(curso, list(args["conceptos"]), args["resultado"])
            return {"conceptos": args["conceptos"], "resultado": args["resultado"]}
        raise ValueError(f"herramienta sin implementar: {nombre}")

    def _siguiente(self) -> dict | None:
        g = grafo.cargar_grafo(self.curso)
        dom = grafo.cargar_dominio(self.curso)
        orden = [m for miembros in (g.get("cadenas") or {}).values() for m in miembros]
        orden += [c for c in g.get("nodos", {}) if c not in orden]
        def estado(c):
            return dom.get(c, {}).get("estado", "no_estudiado")
        candidatos = []
        for cid in orden:
            nodo = g.get("nodos", {}).get(cid, {})
            if estado(cid) == "dominado":
                continue
            reqs = nodo.get("requiere_antes", []) or nodo.get("viene_de", [])
            if all(estado(r) == "dominado" for r in reqs):
                candidatos.append(cid)
        if not candidatos:
            return None
        en_estudio = [c for c in candidatos if estado(c) == "en_estudio"]
        elegido = (en_estudio or candidatos)[0]
        return {"id": elegido, "nombre": g["nodos"][elegido].get("nombre", elegido),
                "estado": estado(elegido)}

    @staticmethod
    def _respuesta(mid: int, resultado) -> dict:
        return {"jsonrpc": "2.0", "id": mid, "result": resultado}

    @staticmethod
    def _error(mid: int, codigo: int, mensaje: str) -> dict:
        return {"jsonrpc": "2.0", "id": mid,
                "error": {"code": codigo, "message": mensaje}}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Servidor MCP de Datito (stdio).")
    ap.add_argument("--curso", required=True, help="slug del curso")
    args = ap.parse_args(argv)
    curso = modelo.cargar(args.curso)
    servidor = Servidor(curso)
    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue
        try:
            respuesta = servidor.manejar(json.loads(linea))
        except json.JSONDecodeError:
            respuesta = Servidor._error(None, -32700, "JSON invalido")
        if respuesta is not None:
            sys.stdout.write(json.dumps(respuesta, ensure_ascii=False) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
