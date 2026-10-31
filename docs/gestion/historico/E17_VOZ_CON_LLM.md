# E-17 — Calidad de voz medida con LLM real (qwen2.5:3b)

Fecha: 2026-10-31 · Reproducible: `PYTHONPATH=15_TERMINITO/src python3 -m datito.eval_conversacion`
(con Ollama 0.40.13 local y `qwen2.5:3b` instalado; antes E-16 midió todo lo
demás sin LLM y quedó INCONCLUSO por esa etapa — aquí se cierra).

## Latencia por componente (20 turnos guionizados, CPU sola)

| Etapa | p50 | p95 |
|---|---|---|
| STT (faster-whisper `base`) | 0.288 s | 0.359 s |
| LLM (qwen2.5:3b vía Ollama, CPU) | 0.204 s | 0.378 s |
| Cerebro (ciclo E-15) | 0.039 s | 0.059 s |
| TTS (Kokoro-82M, CPU) | 1.028 s | 1.984 s |
| **Turno completo** | **0.537 s** | **0.887 s** |

Veredicto pre-registrado: **CUMPLE** — p95 0.887 s < 3 s y validación 100%
(≥ 90%). La holgura es de 3.4× sobre el presupuesto.

## Lecturas honestas

1. **La proyección de E-16 se subestimó**: se temía que un 3B en CPU no
   cabiera en los ~1.6 s restantes; medido, el LLM entero usa p95 0.378 s.
   Lección registrada: la etapa LLM solo se proyecta con incertidumbre;
   la medición real manda (era exactamente el dato que E-16 dijo que faltaba).
2. **El cuello de botella real es el TTS** (p95 1.984 s con los textos más
   largos del LLM): Kokoro en CPU es usable pero domina la latencia. Es la
   primera candidata a optimización (chunking, motor más ligero, o GPU).
3. **Validación 100% con cobertura de citas 0%**: en este guion el LLM no
   evocó recuerdos citados, así que `evidencia.validar` no tuvo citas que
   ejercitar. La garantía anti-alucinación queda probada solo en su rama
   trivial; falta un guion que fuerce evocaciones con cita (trabajo futuro:
   cuando `llm.py` inyecte el recordatorio de cita en modo compañía).
4. Naturalidad rubricada 4.9/5 (una respuesta perdió el punto de fluidez por
   superar el umbral de latencia en su turno).

## Estado del pipeline de voz tras E-16 + E-17

Oreja: MediaRecorder → `/api/stt` (faster-whisper local, el audio jamás sale
de la máquina). Boca: `/api/tts` con Kokoro (y Piper como alternativa),
selección por curso y A/B ciego de preferencia. Cerebro: ciclo por turno con
trazas y valencia (opt-in desde E-16). Todo el turno, medido de punta a
punta con LLM real: **menos de 0.9 s en el percentil 95**.
