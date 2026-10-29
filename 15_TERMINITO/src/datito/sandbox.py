"""Sandbox de ejecución acotado para evaluación de procedimiento (H-8.2/T-8.2.1).

El estudiante pega su script; lo corremos en un directorio efímero con
límites de tiempo y recursos, y convertimos su salida en una TRAZA: lista
ordenada de eventos extraídos de marcadores `#@nombre` impresos a stdout.

Límites honestos (stdlib, sin namespaces): timeout duro, cwd aislado,
rlimits POSIX (CPU, memoria best-effort, sin archivos core). NO bloquea la
red: el docente no debe exigir red en los ítems procedimentales, y el
timeout acota el daño. La traza (eventos + salida + exit code) queda en
resultados.yaml como evidencia del procedimiento, no solo del texto.
"""
from __future__ import annotations

import os
import re
import resource
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

MARCADOR_RE = re.compile(r"^#@(.+?)\s*$")
TIMEOUT_DEFECTO = 10
MEMORIA_MAX_MB = 512


@dataclass
class Evento:
    seq: int            # orden dentro de la corrida
    nombre: str         # marcador #@nombre (normalizado: minúsculas, guiones)
    linea: int          # línea de stdout donde apareció


@dataclass
class Traza:
    eventos: list[Evento] = field(default_factory=list)
    salida: str = ""
    error: str = ""
    codigo_salida: int | None = None
    timeout: bool = False

    def nombres(self) -> list[str]:
        return [e.nombre for e in self.eventos]

    def primera_aparicion(self, nombre: str) -> int | None:
        for e in self.eventos:
            if e.nombre == nombre:
                return e.seq
        return None

    def ultima_aparicion(self, nombre: str) -> int | None:
        ultima = None
        for e in self.eventos:
            if e.nombre == nombre:
                ultima = e.seq
        return ultima


def _limites():
    """rlimits POSIX para la corrida del estudiante."""
    resource.setrlimit(resource.RLIMIT_CPU, (TIMEOUT_DEFECTO, TIMEOUT_DEFECTO + 1))
    try:
        resource.setrlimit(resource.RLIMIT_AS,
                           (MEMORIA_MAX_MB * 1024 * 1024, MEMORIA_MAX_MB * 1024 * 1024))
    except (ValueError, OSError):
        pass  # plataformas sin RLIMIT_AS
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def ejecutar(codigo: str, timeout: int = TIMEOUT_DEFECTO) -> Traza:
    """Corre el script del estudiante y devuelve su traza.

    Marcadores: líneas de stdout que empiecen con `#@` registran un evento
    con ese nombre, en orden. El resto de la salida queda como evidencia.
    """
    with tempfile.TemporaryDirectory(prefix="datito-sandbox-") as dir_tmp:
        script = Path(dir_tmp) / "solucion.py"
        script.write_text(codigo, encoding="utf-8")
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1",
               "HOME": dir_tmp, "LANG": "C.UTF-8"}
        try:
            proc = subprocess.run(
                [sys.executable, "-I", str(script)], cwd=dir_tmp, env=env,
                capture_output=True, text=True, timeout=timeout,
                preexec_fn=_limites if os.name == "posix" else None)
            traza = Traza(salida=proc.stdout, error=proc.stderr,
                          codigo_salida=proc.returncode)
        except subprocess.TimeoutExpired as e:
            traza = Traza(salida=(e.stdout or "") if isinstance(e.stdout, str) else "",
                          error=f"timeout de {timeout}s agotado",
                          codigo_salida=None, timeout=True)
        seq = 0
        for n_linea, linea in enumerate(traza.salida.splitlines(), start=1):
            m = MARCADOR_RE.match(linea)
            if m:
                seq += 1
                nombre = m.group(1).strip().lower().replace(" ", "-")
                traza.eventos.append(Evento(seq=seq, nombre=nombre, linea=n_linea))
        return traza


# ── validación del protocolo pedagógico (T-8.2.2) ────────────────────────────

def validar_protocolo(traza: Traza, reglas: list[dict]) -> tuple[list[str], list[str]]:
    """Valida la traza contra reglas de orden. Cada regla:
      {evento: nombre, requiere: true|false, antes_de: [nombres]}

    Devuelve (reglas_cumplidas, reglas_fallidas), cada una descrita en texto.
    Una regla falla si el evento no aparece (con requiere), o si aparece
    DESPUÉS de alguno de los eventos que debía preceder.
    """
    cumplidas, fallidas = [], []
    for regla in reglas:
        nombre = str(regla.get("evento", "")).strip().lower().replace(" ", "-")
        descripcion = f"{nombre} antes de {regla.get('antes_de') or 'nada'}"
        primera = traza.primera_aparicion(nombre)
        if primera is None:
            if regla.get("requiere", True):
                fallidas.append(f"falta el paso '{nombre}'")
            else:
                cumplidas.append(descripcion)
            continue
        violaciones = []
        for otro in regla.get("antes_de", []) or []:
            otro_n = str(otro).strip().lower().replace(" ", "-")
            ultima_otro = traza.ultima_aparicion(otro_n)
            if ultima_otro is not None and ultima_otro < primera:
                violaciones.append(otro_n)
        if violaciones:
            fallidas.append(f"'{nombre}' ocurrió después de {', '.join(violaciones)}")
        else:
            cumplidas.append(descripcion)
    return cumplidas, fallidas
