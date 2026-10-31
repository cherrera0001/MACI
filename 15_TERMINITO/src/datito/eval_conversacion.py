"""Banco de calidad de la conversación por voz (E-16, T-16.4.1).

20 turnos guionizados de reminiscencia sobre un curso ``compania`` temporal.
Mide por etapa, con lo que esté instalado en la máquina (sin inventar datos):

- **stt**: solo si hay motor neuronal de TTS para fabricar el audio de entrada
  y faster-whisper para transcribirlo; si no, queda ``None`` (no medible aquí).
- **intercambio**: ``sesion.intercambio`` (LLM real si Ollama está; si no, la
  plantilla local, etiquetado ``ollama=False`` — honesto).
- **cerebro**: ``cerebro.ciclo`` (camino real del servidor desde E-15).
- **tts**: ambos motores disponibles, por separado.

Éxito **pre-registrado**: p95 del turno completo < 3 s Y ≥90% de respuestas
que pasan ``evidencia.validar``. Si p95 ≥ 3 s, el reporte atribuye el
componente dominante y la recomendación de hardware queda condicionada a ese
dato (nunca a benchmarks de terceros).
"""
from __future__ import annotations

import json
import tempfile
import time
from pathlib import Path

from . import cerebro, evidencia, llm, stt, voz
from .indice import Indice
from . import sesion as sesion_mod

UMBRAL_P95_S = 3.0
MIN_VALIDACION = 0.90
TURNOS = [
    "Cuénteme de su perrito Rufo y las tardes en la puerta",
    "Hoy me acordé de las sopaipillas con mi hermana",
    "¿Me ayuda a recordar los domingos de videollamada?",
    "Aprendí a tejer con mi madre en Chillán",
    "Mi nieta me llamó por teléfono esta mañana",
    "Qué tiempo hacía en su pueblo cuando era niña",
    "Me gustaría volver a ver el patio de la casa vieja",
    "Cuénteme otra vez de las videollamadas con las niñas",
    "Siento que los días se parecen mucho últimamente",
    "Un señor me dijo que gané un premio y me pidió mis claves",
    "Estoy un poco triste y sola hoy",
    "Qué puedo hacer si un mensaje me pide plata urgente",
    "Recuerdo el olor del pan en la cocina de mi madre",
    "Mi hermana y yo cantábamos en las tardes de verano",
    "Hábleme de su día, qué ha hecho hoy usted conmigo",
    "Quiero aprender a videollamar yo sola a mi familia",
    "Cuénteme de Chillán y los inviernos de su infancia",
    "Otra vez soñé con el patio y con Rufo corriendo",
    "Gracias por acompañarme, me siento mejor",
    "Hasta mañana, que descanse",
]

MEMORIAS = [
    ("Su perrito Rufo la esperaba en la puerta cada tarde", "sesion guion"),
    ("Los domingos hacía sopaipillas con su hermana", "sesion guion"),
    ("Videollama a sus nietas los domingos por la tarde", "sesion guion"),
    ("Aprendió a tejer con su madre en Chillán", "sesion guion"),
    ("En el patio de la casa vieja crecían rosas y tomates", "sesion guion"),
    ("Su hermana y ella cantaban en las tardes de verano", "sesion guion"),
    ("Nunca comparta claves ni datos bancarios por teléfono", "guia: anti-estafa"),
    ("Para videollamar abra la cámara y toque el nombre", "guia: videollamada"),
]


def _curso_temporal():
    from . import config
    from .modelo import crear

    tmp = tempfile.TemporaryDirectory(prefix="e16-voz-")
    config.DIR_CURSOS = Path(tmp.name) / "cursos"
    curso = crear("evalvoz", nombre="Eval voz", periodo="eval")
    curso.datos["modo"] = "compania"
    curso.datos["cerebro"] = "aal"   # opt-in explícito: mido el cerebro (E-16)
    curso.guardar()
    ind = Indice()
    for texto, ref in MEMORIAS:
        ind.registrar_recuerdo(texto, referencia=ref)
    ind.guardar(curso.ruta(".indice"))
    curso.transicionar("listo")
    return curso, ind, tmp


def _p50(xs: list[float]) -> float | None:
    return round(sorted(xs)[len(xs) // 2], 3) if xs else None


def _p95(xs: list[float]) -> float | None:
    if not xs:
        return None
    return round(sorted(xs)[min(len(xs) - 1, int(0.95 * (len(xs) - 1)))], 3)


def naturalidad(texto: str, latencia_total: float | None) -> int:
    """Rúbrica fija y determinista (1-5), autoevaluada por reglas."""
    puntuacion = 1
    limpio = evidencia.limpiar_citas(texto)
    palabras = len(limpio.split())
    if evidencia.extraer_citas(texto):
        puntuacion += 1                      # respaldado en evidencia
    if 8 <= palabras <= 60:
        puntuacion += 1                      # longitud conversacional
    if "?" in limpio or any(m in limpio.lower()
                           for m in ("cuénteme", "recuerda", "y usted",
                                     "qué le")):
        puntuacion += 1                      # invita a seguir conversando
    if not any(j in limpio.lower() for j in
               ("vector", "dataset", "algoritmo", "token", "modelo")):
        puntuacion += 1                      # sin jerga técnica
    if latencia_total is not None and latencia_total < UMBRAL_P95_S:
        puntuacion += 1                      # fluidez percibida
    return min(5, puntuacion)


def correr() -> dict:
    curso, ind, tmp = _curso_temporal()
    cer = cerebro.para_curso(curso)
    con_ollama = llm.disponible()
    motores = [m for m, ok in voz.motores_disponibles().items() if ok]

    mediciones = {k: [] for k in ("stt", "intercambio", "cerebro")}
    tts_por_motor = {m: [] for m in motores}
    validados = 0
    cobertura_citas = 0
    naturalezas = []
    transcripciones = 0
    totales = []

    for turno in TURNOS:
        latencia = {}
        # STT: audio real sintetizado (si hay voz) → transcripción real.
        audio = None
        if motores:
            audio = voz.sintetizar(turno, curso, motor=motores[0])
        if audio and stt.disponible():
            t0 = time.perf_counter()
            texto_stt = stt.transcribir(audio)
            latencia["stt"] = time.perf_counter() - t0
            if texto_stt:
                transcripciones += 1
        mensaje = turno
        # Intercambio (LLM real si Ollama está; si no, la plantilla local).
        t0 = time.perf_counter()
        r = sesion_mod.intercambio(curso, mensaje, ind)
        latencia["intercambio"] = time.perf_counter() - t0
        respuesta = r.get("texto", "")
        # Validación: toda cita que aparece debe validar (si no hay citas, el
        # turno es escucha empática legítima — D-10.2 — y cuenta como válido).
        citas = evidencia.extraer_citas(respuesta)
        if all(evidencia.validar(c, ind).ok or c in ind.textos for c in citas):
            validados += 1
        if citas:
            cobertura_citas += 1
        # Cerebro (camino del servidor).
        if cer is not None:
            t0 = time.perf_counter()
            cer.ciclo(mensaje, respuesta, indice=ind)
            latencia["cerebro"] = time.perf_counter() - t0
        # TTS por cada motor disponible (para el A/B D-16.2).
        for m in motores:
            t0 = time.perf_counter()
            voz.sintetizar(respuesta, curso, motor=m)
            tts_por_motor[m].append(time.perf_counter() - t0)
        total = sum(latencia.values())
        totales.append(round(total, 4))
        naturalezas.append(naturalidad(respuesta, total))
        for k, v in latencia.items():
            mediciones[k].append(round(v, 4))

    resumen_etapas = {k: {"p50": _p50(v), "p95": _p95(v), "n": len(v)}
                      for k, v in mediciones.items()}
    resumen_tts = {m: {"p50": _p50(v), "p95": _p95(v)} for m, v in tts_por_motor.items()}
    p95_total = _p95(totales)
    validacion = round(validados / len(TURNOS), 3)
    latencias_por_etapa = {k: (v["p95"] or 0) for k, v in resumen_etapas.items()}
    latencias_por_etapa.update({f"tts:{m}": v["p95"] or 0
                                for m, v in resumen_tts.items()})
    cuello = max(latencias_por_etapa, key=latencias_por_etapa.get) \
        if latencias_por_etapa else None
    faltantes = [e for e in ("stt", "tts", "ollama")
                 if (e == "ollama" and not con_ollama)
                 or (e == "stt" and not mediciones["stt"])
                 or (e == "tts" and not motores)]
    exito = (p95_total is not None and p95_total < UMBRAL_P95_S
             and validacion >= MIN_VALIDACION and not faltantes)
    if faltantes:
        veredicto = (
            f"INCONCLUSO: sin medir {', '.join(faltantes)} en esta máquina. "
            f"Lo medido (intercambio+cerebro) usa p95 {p95_total}s del "
            f"presupuesto de {UMBRAL_P95_S}s; el resto lo consumen las etapas "
            f"ausentes, que deben medirse con los motores instalados "
            f"antes de cualquier compra de hardware.")
    elif exito:
        veredicto = f"CUMPLE: p95 total {p95_total}s < {UMBRAL_P95_S}s y " \
                    f"validación {validacion:.0%} ≥ {MIN_VALIDACION:.0%}."
    else:
        veredicto = (f"NO CUMPLE: p95 {p95_total}s; componente dominante "
                     f"{cuello}. Atacar ese componente antes de comprar "
                     f"hardware; la recomendación queda condicionada a este dato.")
    return {
        "turnos": len(TURNOS),
        "ollama": con_ollama,
        "motores_tts": motores,
        "transcripciones_stt": transcripciones,
        "validacion": validacion,
        "cobertura_citas": round(cobertura_citas / len(TURNOS), 3),
        "umbral_validacion": MIN_VALIDACION,
        "latencia_s": {**resumen_etapas, "total": {"p50": _p50(totales),
                                                   "p95": p95_total}},
        "tts_por_motor_s": resumen_tts,
        "naturalidad_media": round(sum(naturalezas) / len(naturalezas), 2),
        "exito_preregistrado": exito,
        "inconcluso_por": faltantes,
        "cuello_de_botella": cuello,
        "veredicto": veredicto,
        "_tmp": str(tmp),
    }


def main() -> None:  # pragma: no cover - CLI
    print(json.dumps(correr(), indent=2, ensure_ascii=False))


if __name__ == "__main__":  # pragma: no cover
    main()
