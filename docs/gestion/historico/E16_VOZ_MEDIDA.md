# E-16 — Calidad de voz medida: el banco de 20 turnos y el presupuesto de 3 s

Fecha: 2026-10-31 · Reproducible: `PYTHONPATH=15_TERMINITO/src python3 -m datito.eval_conversacion`
Épica E-16 (issues #228–#244) · Éxito pre-registrado: **p95 total < 3 s Y ≥90% de turnos validados**.

## Máquina de medición

Mini-PC del desarrollador (CPU moderna, sin GPU), Python 3.12 venv.
Motores instalados para la medición: faster-whisper `base` (int8, CPU) y
Kokoro-82M (onnx, CPU). **Ollama/qwen2.5:3b no está instalado en esta
máquina** — la etapa LLM queda sin medir y el veredicto es INCONCLUSO por
ella, no un pase.

## Latencia por componente (20 turnos guionizados de reminiscencia)

| Etapa | p50 | p95 | n |
|---|---|---|---|
| STT (faster-whisper base, CPU) | 0.280 s | 0.292 s | 20 |
| Intercambio (plantilla, sin LLM) | 0.001 s | 0.002 s | 20 |
| Cerebro (ciclo E-15) | 0.034 s | 0.044 s | 20 |
| TTS (Kokoro, CPU) | 0.925 s | 1.054 s | 20 |
| **Turno completo sin LLM** | **0.309 s** | **0.336 s** | 20 |
| Turno hablado (todo + TTS) | ~1.23 s | ~1.39 s | 20 |

Calidad: validación de citas 100% (cero recuerdos inventados), cobertura de
citación 65% de los turnos (los de plantilla que evocan recuerdo), naturalidad
rubricada 5.0/5 en el camino de plantilla, 20/20 transcripciones STT correctas
(una con error léxico menor propio de `base`).

## Lectura honesta

1. **El pipeline de voz "gratis" (CPU) consume ~1.4 s del presupuesto de 3 s.**
   Quedan ~1.6 s para el LLM. Un 3B puro en CPU rinde ~1.5–4 tok/s: una
   respuesta de 40–60 palabras (30–80 tokens) tardaría 10–50 s — **no cabe**.
   Es proyección marcada como tal, no medición; la medición real exige instalar
   Ollama y re-correr este mismo banco.
2. **El cuello medido es el TTS** (1.05 s p95), no el STT (0.29 s). Kokoro en
   CPU es usable; bajarlo de 1 s a ~0.2 s requiere GPU o un motor más ligero.
3. **Decisión condicionada a datos**: si el LLM local corre en GPU
   (mini-PC con APU/NPU o GPU dedicada), el turno completo queda en
   ~1.5–2 s < 3 s y el hardware actual basta. Si el LLM debe correr en CPU,
   ningún ajuste de voz salva el presupuesto: toca acortar respuestas o
   subir hardware. **Comprar hardware antes de medir la etapa LLM sería
   especulación: el dato que falta es exactamente ese.**
4. El A/B ciego de voces (D-16.2) queda cableado para cuando convivan dos
   motores (p. ej. piper vs kokoro) y registrar la preferencia real de los
   usuarios en `voz-preferencia`.

## Qué se cerró en código

- `stt.py` + `POST /api/stt` + chat.html con MediaRecorder: el audio del
  usuario **nunca sale de la máquina** (corrige la brecha de E-11 donde
  webkitSpeechRecognition podía enviar audio a servicios del SO/nube).
- `voz.py` multi-motor (piper/kokoro) con selección por curso.yaml y A/B.
- `acceso.py` con tokens de un solo uso + `THREAT_MODEL.md` (D-16.3).
- Banco D-15.3 ampliado a 20 sondas → re-decisión en
  `E16_CEREBRO_BANCO_AMPLIADO.md`.
