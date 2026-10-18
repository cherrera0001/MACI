"""Servidor local stdlib (sin dependencias) en 127.0.0.1:8377.

Sirve la interfaz web (src/web) y la API de contracts/api.md. Sin framework:
ThreadingHTTPServer + routing manual. Subida de materiales como PUT binario
(un archivo por llamada) para no parsear multipart.
"""
from __future__ import annotations

import json
import re
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import config, evaluador, evidencia, grafo, identidad, llm, progreso
from . import ciclo, sesion as sesion_mod
from . import dudas as dudas_mod
from . import fragmentos as frag
from . import tutor as tutor_mod
from .indice import Indice
from .modelo import ErrorCurso, cargar, crear as crear_curso, listar

DIR_WEB = config.DIR_WEB
JSON = "application/json; charset=utf-8"


def _datos_panel(curso, mapa_completo: bool = False) -> dict:
    g = grafo.cargar_grafo(curso)
    dominio = grafo.cargar_dominio(curso)
    cadenas = []
    for cadena, miembros in (g.get("cadenas") or {}).items():
        nodos = []
        for m in miembros:
            nodo = (g.get("nodos") or {}).get(m)
            if not nodo:
                continue
            visible = mapa_completo or grafo._visible({**nodo, "id": m}, dominio)
            est = dominio.get(m, {}).get("estado", "no_estudiado")
            nodos.append({"id": m, "nombre": nodo.get("nombre", m),
                          "estado": est if est in config.ESTADOS_DOMINIO else "no_estudiado",
                          "visible": visible})
        cadenas.append({"cadena": cadena.replace("_", " "), "nodos": nodos})
    return {"slug": curso.slug, "nombre": curso.datos.get("nombre"),
            "mapa_completo": mapa_completo, "cadenas": cadenas}


class Handler(BaseHTTPRequestHandler):
    server_version = "termito/0.1"

    # ---------- utilidades ----------
    def _json(self, payload: dict, status: int = 200):
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", JSON)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _error(self, codigo: str, detalle: str, status: int = 400):
        self._json({"error": codigo, "detalle": detalle}, status)

    def _body_json(self) -> dict:
        n = int(self.headers.get("Content-Length", 0))
        if not n:
            return {}
        return json.loads(self.rfile.read(n).decode("utf-8"))

    def _slug(self, partes: list[str]) -> str | None:
        m = re.fullmatch(r"api/cursos/([a-z0-9-]+)(?:/.*)?", "/".join(partes))
        return m.group(1) if m else None

    def log_message(self, *a):  # silencioso
        pass

    def _evidencia(self, citas: list[str], indice) -> list[dict]:
        return [{"fid": c, "fuente": indice.referencias[c][0],
                 "referencia": indice.referencias[c][1]}
                for c in citas if c in indice.referencias]

    def _envoltura_mensaje(self, r: dict, indice) -> dict:
        """Respuesta de POST /mensajes con los campos del contrato (api.md)."""
        cuerpo = {"respuesta": r["texto"], "evidencia": self._evidencia(r["citas"], indice),
                  "modo": r["modo"], "aviso": r["aviso"],
                  "estado_interaccion": r["estado_interaccion"],
                  "sin_fuente": r["modo"] == "sin_fuente",
                  "fuera_del_curso": r.get("fuera_del_curso", False),
                  "duda_registrada": ({"id": r["duda"]["id"]}
                                      if r.get("duda") else None)}
        if r.get("paso"):
            cuerpo["paso"] = r["paso"]
        return cuerpo

    def _guardar_componentes(self, slug: str):
        curso = cargar(slug)
        d = self._body_json()
        actuales = identidad.cargar(curso)
        actuales.update({k: v for k, v in d.items() if k in identidad.COMPONENTES})
        identidad.guardar(curso, actuales)
        ok, faltantes = identidad.completos(actuales)
        return self._json({"completo": ok, "faltantes": faltantes})

    # ---------- routing ----------
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,PUT,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        u = urlparse(self.path)
        partes = [p for p in u.path.strip("/").split("/") if p]
        try:
            if u.path == "/api/salud":
                return self._json({
                    "modelo_local": llm.disponible(),
                    "version_modelo": config.MODELO if llm.disponible() else None,
                    "modo": "tutor" if llm.disponible() else "exploracion"})
            if partes[:2] == ["api", "cursos"] and len(partes) == 2:
                return self._json({"cursos": [
                    {"slug": c.slug, "nombre": c.datos.get("nombre"),
                     "estado": c.estado} for c in listar()]})
            if u.path.startswith("/api/cursos/"):
                slug = self._slug(partes)
                recurso = partes[3] if len(partes) > 3 else ""
                if recurso == "":
                    curso = cargar(slug)
                    return self._json({"curso": curso.datos,
                                       "componentes": identidad.cargar(curso)})
                if recurso == "grafo":
                    qs = parse_qs(u.query)
                    return self._json(_datos_panel(
                        cargar(slug), mapa_completo=qs.get("mapa", ["0"])[0] == "1"))
                if recurso == "evaluacion":
                    curso = cargar(slug)
                    items = evaluador.cargar_items(curso)
                    return self._json({"items": [
                        {"id": i.id, "conceptos": i.conceptos, "pregunta": i.pregunta}
                        for i in items]})
                if recurso == "fragmento":
                    qs = parse_qs(u.query)
                    fid = qs.get("fid", [""])[0]
                    indice = Indice.cargar(cargar(slug).ruta(".indice"))
                    if fid not in indice.textos:
                        return self._error("fid_inexistente", fid, 404)
                    fuente, ref = indice.referencias[fid]
                    return self._json({"fid": fid, "fuente": fuente, "referencia": ref,
                                       "texto": indice.textos[fid]})
                if recurso == "registro":
                    return self._json(ciclo.resumen_registro(cargar(slug)))
                if recurso == "prompt":
                    p = cargar(slug).ruta("prompt", "actual.md")
                    return self._json({"prompt": p.read_text(encoding="utf-8")
                                       if p.exists() else ""})
            return self._estatico(u.path)
        except ErrorCurso as e:
            self._error("curso_no_encontrado", str(e), 404)
        except Exception as e:  # noqa: BLE001 - servidor local: error legible
            self._error("error_interno", f"{type(e).__name__}: {e}", 500)

    def do_POST(self):
        u = urlparse(self.path)
        partes = [p for p in u.path.strip("/").split("/") if p]
        try:
            if partes == ["api", "cursos"]:
                d = self._body_json()
                curso = crear_curso(d["slug"], nombre=d.get("nombre", ""),
                                    periodo=d.get("periodo", ""))
                return self._json({"slug": curso.slug, "estado": curso.estado}, 201)
            if partes == ["api", "importar"]:
                d = self._body_json()
                try:
                    return self._json(ciclo.importar(d.get("ruta", "")), 201)
                except ErrorCurso as e:
                    return self._error("importacion_invalida", str(e), 422)
            slug = self._slug(partes)
            recurso = partes[3] if len(partes) > 3 else ""
            curso = cargar(slug)
            if recurso == "componentes":
                return self._guardar_componentes(slug)
            if recurso == "construir":
                componentes = identidad.cargar(curso)
                ok, faltantes = identidad.completos(componentes)
                if not ok:
                    return self._error("componentes_incompletos",
                                       ", ".join(faltantes), 422)
                resumen = _build(curso, componentes)
                return self._json(resumen)
            if recurso == "mensajes" and len(partes) == 4:
                if curso.estado == "cerrado":
                    return self._error(
                        "termito_cerrado",
                        "El Termito esta cerrado (FR-016); su registro sigue "
                        "disponible en GET /registro.", 409)
                d = self._body_json()
                indice = Indice.cargar(curso.ruta(".indice"))
                r = sesion_mod.conversar(curso, d.get("texto", ""), indice)
                progreso.contar_mensaje(curso, 2)
                return self._json(self._envoltura_mensaje(r, indice))
            if recurso == "mensajes" and len(partes) == 6 \
                    and partes[5] == "revelar":
                if curso.estado == "cerrado":
                    return self._error("termito_cerrado",
                                       "El Termito esta cerrado (FR-016).", 409)
                d = self._body_json()
                indice = Indice.cargar(curso.ruta(".indice"))
                try:
                    res = sesion_mod.revelar(
                        curso, bool(d.get("consentimiento")), indice)
                except ErrorCurso as e:
                    return self._error("sin_sesion", str(e), 404)
                except ValueError as e:
                    return self._error("consentimiento_requerido", str(e), 422)
                except PermissionError as e:
                    return self._error("aun_no", str(e), 409)
                return self._json({"solucion": res["solucion"],
                                   "evidencia": self._evidencia(res["citas"], indice),
                                   "registro": res["registro"],
                                   "estado_interaccion":
                                       res["estado_interaccion"]})
            if recurso == "mensajes":
                return self._error("ruta_desconocida", u.path, 404)
            if recurso == "dudas":
                if curso.estado == "cerrado":
                    return self._error("termito_cerrado",
                                       "El Termito esta cerrado (FR-016).", 409)
                d = self._body_json()
                indice = Indice.cargar(curso.ruta(".indice"))
                resp = tutor_mod.responder(curso, d.get("texto", ""), indice)
                if resp.modo == "sin_fuente" or not resp.citas:
                    return self._error("sin_fuente",
                                       "La pregunta no tiene respaldo en los materiales", 422)
                duda = tutor_mod.registrar_duda_si_confusion(curso, d.get("texto", ""), resp)
                return self._json({"duda": duda}, 201)
            if recurso == "evaluacion":
                d = self._body_json()
                items = {i.id: i for i in evaluador.cargar_items(curso)}
                item = items.get(d.get("item_id"))
                if not item:
                    return self._error("item_desconocido", d.get("item_id", ""), 404)
                indice = Indice.cargar(curso.ruta(".indice")) \
                    if curso.ruta(".indice").exists() else None
                contexto = ""
                if indice:
                    top = indice.buscar(" ".join(item.conceptos), k=2)
                    contexto = " ".join(indice.textos[f] for f, _ in top)
                res = evaluador.calificar(item, d.get("respuesta", ""), contexto)
                evaluador.guardar_resultado(curso, res)
                grafo.actualizar_dominio(curso, item.conceptos, res.resultado)
                n, ok = progreso.contar_distincion(curso, res.resultado == "logrado")
                return self._json({
                    "item_id": item.id, "resultado": res.resultado,
                    "retroalimentacion": res.retroalimentacion,
                    "criterios": [{"criterio": c, "logrado": c in res.criterios_logrados}
                                  for c in item.criterios],
                    "sesion": {"n": n, "logradas": ok}})
            if recurso == "notas":
                d = self._body_json()
                try:
                    entrada = ciclo.registrar_nota(
                        curso, d.get("evaluacion", ""), d.get("nota", ""),
                        d.get("observaciones", ""))
                except ErrorCurso as e:
                    return self._error("nota_invalida", str(e), 422)
                return self._json({"nota": {"fecha": entrada["fecha"],
                                            "evaluacion": entrada["evaluacion"],
                                            "nota": entrada["nota"]},
                                   "ajustes_derivados": entrada["ajustes_derivados"]})
            if recurso == "cerrar":
                try:
                    return self._json(ciclo.cerrar(curso))
                except ErrorCurso as e:
                    return self._error("cerrado_previamente", str(e), 409)
            if recurso == "exportar":
                return self._json(ciclo.exportar(curso), 202)
            return self._error("ruta_desconocida", u.path, 404)
        except ErrorCurso as e:
            self._error("curso_no_encontrado", str(e), 404)
        except Exception as e:  # noqa: BLE001
            self._error("error_interno", f"{type(e).__name__}: {e}", 500)

    def do_PUT(self):
        u = urlparse(self.path)
        partes = [p for p in u.path.strip("/").split("/") if p]
        try:
            if len(partes) == 4 and partes[:2] == ["api", "cursos"] \
                    and partes[3] == "componentes":
                # el contrato (api.md) lo define como PUT; el wizard legacy usa
                # POST. Ambos se aceptan con la misma semantica.
                return self._guardar_componentes(partes[2])
            if len(partes) == 4 and partes[:2] == ["api", "cursos"] \
                    and partes[3] == "materiales":
                curso = cargar(partes[2])
                nombre = Path(parse_qs(urlparse(self.path).query)
                              .get("nombre", ["archivo"])[0]).name or "archivo"
                n = int(self.headers.get("Content-Length", 0))
                datos = self.rfile.read(n)
                dest = curso.ruta("materiales", "uploads")
                dest.mkdir(parents=True, exist_ok=True)
                (dest / nombre).write_bytes(datos)
                return self._json({"guardado": nombre, "bytes": len(datos)}, 201)
            return self._error("ruta_desconocida", u.path, 404)
        except ErrorCurso as e:
            self._error("curso_no_encontrado", str(e), 404)

    # ---------- estáticos ----------
    def _estatico(self, ruta: str):
        if ruta in ("/", ""):
            ruta = "/index.html"
        destino = (DIR_WEB / ruta.lstrip("/")).resolve()
        if not str(destino).startswith(str(DIR_WEB.resolve())) or not destino.is_file():
            self.send_error(404)
            return
        ctype = {".html": "text/html; charset=utf-8", ".css": "text/css",
                 ".js": "text/javascript", ".svg": "image/svg+xml",
                 ".png": "image/png"}.get(destino.suffix, "application/octet-stream")
        body = destino.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def _build(curso, componentes: dict) -> dict:
    """Parsea materiales + indice + prompt (equivalente a 'termito build')."""
    rutas = [p for p in curso.ruta("materiales").iterdir()] \
        if curso.ruta("materiales").exists() else []
    fuentes, frags = frag.parsear_materiales(rutas)
    if not frags:
        raise RuntimeError("no se extrajo contenido de los materiales")
    dir_frag = curso.ruta("fuentes", "fragmentos")
    dir_frag.mkdir(parents=True, exist_ok=True)
    por_fuente: dict[str, list] = {}
    for f in frags:
        por_fuente.setdefault(f.fuente_id, []).append(f)
    for fuente in fuentes:
        lista = por_fuente.get(fuente.id, [])
        (dir_frag / f"{fuente.id}.md").write_text(
            "\n\n".join(f"<!-- {f.fid} | {f.referencia} -->\n{f.texto}" for f in lista),
            encoding="utf-8")
    Indice().construir(frags).guardar(curso.ruta(".indice"))
    prompt = identidad.generar_prompt(curso, componentes)
    if curso.estado == "configurando":
        curso.transicionar("listo")
    return {"fuentes": len(fuentes), "fragmentos": len(frags),
            "prompt": prompt.read_text(encoding="utf-8")[:4000]}


def servir(puerto: int | None = None, abrir: bool = False) -> None:
    puerto = puerto or config.PUERTO
    httpd = ThreadingHTTPServer(("127.0.0.1", puerto), Handler)
    print(f"Termito en http://127.0.0.1:{puerto}  (Ctrl+C para salir)")
    if abrir:
        webbrowser.open(f"http://127.0.0.1:{puerto}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n¡Hasta pronto!")


def main():
    abrir = "--abrir" in sys.argv
    puerto = None
    for i, a in enumerate(sys.argv):
        if a == "--puerto" and i + 1 < len(sys.argv):
            puerto = int(sys.argv[i + 1])
    servir(puerto=puerto, abrir=abrir)


if __name__ == "__main__":
    main()
