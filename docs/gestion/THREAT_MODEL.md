# Threat Model — Datito en LAN (D-16.3)

Fecha: 2026-10-31 · Alcance: servidor `datito.servidor` en la máquina del hogar,
clientes web en la misma LAN, modo compañía. Fuera de alcance: exposición
pública a internet (hoy no existe y no se recomienda), compromiso completo del
host, ataques físicos al hardware.

## Supuestos de red

- La LAN **no es confiable**: Wi-Fi con contraseña compartida, visitas que piden
  la clave, dispositivos desconocidos (TV, consolas, IoT ajenos).
- HTTP plano dentro de la LAN: cualquiera en la red puede sniffear tráfico.
  Por eso los endpoints sensibles exigen dispositivo vinculado cuando la
  seguridad está activada (`seguridad.yaml`), y por eso el **audio nunca sale
  de la máquina** (STT local, D-16.1): lo que no existe en la red no se puede
  capturar en tránsito hacia un tercero.
- El servidor escucha en todas las interfaces (`0.0.0.0`). En hogares con red
  de invitados, aislar la máquina allí reduce la superficie sin cambiar código.

## Matriz quién-puede-leer-qué

| Actor | /mensajes (texto) | /familiar (panel) | .indice/ y .cerebro/ (disco) | alertas.yaml | /api/stt (audio) |
|---|---|---|---|---|---|
| Usuario mayor (su dispositivo) | ✅ su conversación | ❌ | ❌ (vive en el servidor) | ❌ | ✅ solo el suyo, local |
| Cuidador/familiar con token (D-16.3) | ✅ | ✅ | ❌ | ✅ (solo fecha+tipo, D-11.3) | ❌ |
| Visita con la URL pero sin vincular | ❌ 401 | ❌ 401 | ❌ | ❌ | ❌ 404/503 sin motor |
| Vecino que entró al Wi-Fi | ⚠️ sniffing pasivo posible (HTTP) | ⚠️ idem | ❌ | ❌ | ⚠️ ver nota abajo |
| Dispositivo robado con device_id válido | ✅ hasta revocación | ✅ hasta revocación | ❌ | ✅ | ❌ |
| Malware en el host | todo | todo | todo | todo | todo (fuera de alcance) |

Nota sniffing: el audio va del navegador al mismo host que sirve la página
(`POST /api/stt`), típicamente por loopback o por el switch local; un sniffer
pasivo en la LAN ve tráfico HTTP entre cliente y servidor, pero el flujo
nunca incluye un tercero en la nube. El texto de la conversación, en cambio,
sí transita en claro — riesgo residual aceptado documentado; mitigación futura
natural: TLS interno o mDNS + cert autofirmado (no implementado en E-16).

## Tokens de un solo uso (implementación E-16)

- `python -m datito.acceso --emitir <slug>` genera un token; se muestra **una
  vez** al cuidador (idealmente por canal fuera de banda: papel, mensaje
  cifrado).
- Canje (`POST /api/cursos/<slug>/vincular`): 1 token → 1 `device_id` (16 hex)
  persistido en `seguridad.yaml` con fecha y etiqueta; el token queda marcado
  como usado (no reutilizable).
- Uso: `X-Device-Id` en cada request; revocación con `--revocar <slug> <id>`.
- Retrocompatibilidad: sin `seguridad.yaml` los endpoints siguen abiertos
  (comportamiento E-15); activar la seguridad es una decisión del cuidador.
- Límite conocido: el device_id viaja en un header HTTP plano; un sniffer
  activo en la LAN puede reutilizarlo (suplantación). Mitigación aceptada por
  ahora: la LAN del hogar sigue siendo el perímetro; registrar dispositivos
  esperados con `--listar` y auditar uso.

## Superficies de ataque del propio stack (auditable)

- `POST /api/stt`: audio arbitrario → faster-whisper (decode PyAV). Riesgo:
  archivos malformados (mitigado: try/except total, tempfile efímero, VAD).
- `POST /api/tts`: texto arbitrario → síntesis (límite de 60 s por subprocess).
- `POST /api/cursos` (crear curso) y `ciclo.importar`: aceptan rutas/texto;
  requieren acceso LAN ya autorizado; `importar` valida contra ErrorCurso.
- Nada persiste audio: `stt.transcribir` usa `tempfile(delete=True)`.