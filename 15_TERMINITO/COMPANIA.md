# Vertical Compañía y Estimulación Cognitiva

**Qué es.** Un compañero conversacional de voz para personas mayores que viven
solas (o en abandono): conversa con calidez, recuerda su vida **solo con
verificación** (jamás inventa recuerdos), toma la iniciativa cuando hace días
que no hablan, protege contra estafas telefónicas, guía ejercicios suaves de
reminiscencia y autonomía digital, y entrega a la familia un panel de legado
y bienestar con privacidad por diseño.

**Para quién.** Una persona mayor con miedo a la tecnología y cero tolerancia
a jerga: no abrirá una terminal ni un formulario. Todo se maneja por voz o con
botones grandes en una pantalla. El núcleo de privacidad es duro: **el audio
y las memorias íntimas jamás salen de la máquina** (D-11.3).

**Estado.** Construida en las épocas E-10 a E-17 (+2 fixes en vivo del día de
la primera prueba real). Funcional en esta máquina; **sin piloto humano
todavía** — la ruta a producción está al final de este documento.

---

## Cómo se usa (hoy, en esta máquina)

```bash
# 1. Servidor (todo el motor + interfaz web), con el venv que ya tiene todo:
cd 15_TERMINITO && PYTHONPATH=src .venv/bin/python -m datito.servidor
# 2. Abrir en el navegador:
#    http://localhost:8377/chat.html?curso=compania
#    (el micrófono solo funciona en localhost o HTTPS: política de los
#    navegadores, no del sistema)
```

En la página: el compañero saluda primero (apertura proactiva por horas de
ausencia y memoria asociativa). Se escribe abajo o se toca 🎤 (grabar →
soltar → envía solo). Botones grandes: **Recordar juntos** (reminiscencia con
3 pistas), **Mi historia de vida** (bitácora imprimible), **Aprender paso a
paso** (micro-talleres de autonomía), **Vista familiar** (panel del cuidador).

## Arquitectura (todo local, stdlib-first, dependencias opcionales)

```
navegador (chat.html, paleta cálida, letra ≥20px, Web Speech / MediaRecorder)
   │  HTTP (JSON)
   ▼
datito.servidor :8377
   ├─ sesion/tutor ··· modo compañía: escucha empática sin citas (D-10.2);
   │                    afirmaciones sobre su vida con cita validada
   ├─ evidencia ······· gate innegociable: toda cita [fid] valida contra el
   │                    índice (MIN_OVERLAP) — cero recuerdos inventados
   ├─ guardian ········ anti-fraude (claves/banco/urgencias) y alertas de
   │                    bienestar → alertas.yaml solo {fecha, tipo}
   ├─ índice TF-IDF ··· memoria principal (buscar/buscar_asociativo,
   │                    consolidación anti-duplicados)
   ├─ cerebro (aal) ··· grafo episódico E-15: spreading activation, trazas
   │                    («¿por qué recuerdas eso?»), valencia, olvido hebbiano
   │                    con poda nuclear. OPT-IN desde E-16 (ver más abajo)
   ├─ llm.py ·········· Ollama local (qwen2.5:3b) — anti-echo determinista
   ├─ stt.py ·········· faster-whisper local (el audio nunca sale de la máquina)
   ├─ voz.py ·········· TTS neuronal: Kokoro-82M + Piper, A/B ciego de voces
   └─ apertura/reminiscencia/biografia/talleres/familiar/acceso (tokens)
persistencia por curso: .indice/ .cerebro/ progreso.yaml alertas.yaml
                          biografía (generada) talleres.yaml seguridad.yaml
```

## Qué está verificado con datos reales (no proyecciones)

| Evidencia | Dato medido | Dónde |
|---|---|---|
| Turno de voz completo con LLM real (qwen2.5:3b, CPU) | **p95 0.887 s** < 3 s (STT 0.36 / LLM 0.38 / cerebro 0.06 / TTS 1.98) | `docs/gestion/historico/E17_VOZ_CON_LLM.md` |
| Validación anti-alucinación | 100% de citas válidas en todos los bancos | E-15/E-16/E-17 |
| Ganancia del cerebro sobre el índice | bootstrap #337: Δ mediana +0.425, **IC95 [+0.088, +0.713]** (significativa) | `E17_CEREBRO_PISO_INFERENCIAL.md` |
| Corpus denso (55 recuerdos, vocabulario compartido) | cerebro recall@3 0.636; índice TF-IDF **colapsa a 0.000** | idem |
| Regresión que manda opt-in | P@3 0.60 < 0.80: la compuerta anti-H4 silencia memorias verdaderas tras 1 alerta | idem |
| Viajes del usuario en navegador real | 6/6 E2E (carga, saludo, envío, mic habilitado, pistas, 0 errores JS) | `tests/e2e/` |
| Suite completa | **217 tests verde** + `verificar_todo.py` LISTO | CI |

## Límites conocidos (honestos)

- **Cerebro en opt-in** (`cerebro: aal` en curso.yaml): el default es el
  índice TF-IDF hasta corregir la compuerta anti-H4 (≥2 alertas, no 1) y
  re-ganar el banco de 20 sondas + 8 congeladas (ruta documentada en E17).
- **Cobertura de citas 0% con LLM real**: en el guion medido el modelo no
  evocó recuerdos citados; el gate anti-alucinación quedó en su rama trivial.
  Falta un guion que fuerce evocaciones (y posiblemente recordatorio de cita
  en el prompt de compañía).
- **Micrófono solo en localhost/HTTPS** (política de navegadores). En el
  piloto real se resuelve con la caja local + mDNS o con HTTPS interno.
- **Amenaza modelada para LAN, no para internet** (`docs/gestion/THREAT_MODEL.md`):
  HTTP en claro dentro de la red del hogar; token por dispositivo para
  /familiar y /mensajes; nunca exponer el puerto a internet público.
- El TTS Kokoro en CPU es el cuello de latencia (p95 1.98 s) — usable, pero
  primera candidata a optimización.

## Ruta a producción (Épica E-18, pendiente de tus 5 decisiones)

La "producción" de esta vertical es una **caja en la casa** (appliance de
red), no un servidor cloud. Gaps entre hoy y el piloto: `install.sh` de una
línea (venv, deps, Ollama, modelos), servicios systemd --user con
autoarranque, dirección `http://datito.local` (mDNS), **respaldo diario de las
memorias** (el activo irreemplazable), `datito actualizar` con la suite E2E
como puerta, seguridad activada por defecto. Decisiones que te pedí: dónde
vive el piloto, hardware (¿Voice PE $69?), quiénes son los usuarios y el
cuidador, acceso remoto vía Tailscale sí/no, y fecha objetivo.

## Gobernanza

Épocas E-10…E-17 cerradas (232 ítems en el tablero, 0 abiertos). Historial de
evidencia en `docs/gestion/historico/E1{5,6,7}_*.md`; amenaza en
`docs/gestion/THREAT_MODEL.md`; experimentos reproducibles:
`python3 -m datito.eval_cerebro` · `python3 -m datito.eval_conversacion`.
