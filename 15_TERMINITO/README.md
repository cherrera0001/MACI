# Datito — MACI 1.0 (MVP)

Motor de tutores agenticos **diseñados por el estudiante** a partir de los materiales
reales de su curso. Offline-first, sin frameworks pesados, datos en archivos legibles.

Ver: `specs/001-termito-platform/` (spec/plan/contratos) y la constitución en
`.specify/memory/constitution.md`.

> **¿Por qué `15_TERMINITO/` si el producto es Datito?** "Termito" fue el nombre
> provisional del MVP (ejemplo del artículo de Parada Daza); la unificación de marca
> a "Datito" es de producto, no de estructura de disco: renombrar el directorio
> rompería rutas e historial sin beneficio. El paquete Python sí es `src/datito/`
> y el CLI es `datito`.

## Estado del MVP

- ✅ Migración del curso real (Fundamentos de Ciencia de Datos): 50 fuentes,
  2174 fragmentos indexados, grafo v0.0.1 enlazado, 3 distinciones del certamen.
- ✅ Diálogo con evidencia citada (modo exploración sin LLM; modo tutor con Ollama).
- ✅ Evaluación por distinciones con rúbrica (LLM local o heurística offline).
- ✅ Lucha productiva (máquina de estados), registro de dudas, panel de dominio
  con gating, contadores de adopción, versionado del prompt.
- ✅ **Interfaz web** (5 pantallas, vanilla, responsive): home, constructor
  conversacional, chat con citas clickeables, evaluación, panel de dominio.
- ✅ **Política socrática ejecutable** (`src/datito/socratico.py`): REGLA CERO
  (espera de verdad), G11 (la estrategia la elige el estudiante), dos intentos
  antes de la solución, respuesta registrada antes de decirse (UNO-B) y
  transferencia exigida tras entregar. Emite un transcript validado con las
  mismas cinco reglas del harness de especificación (R1–R5).
- ✅ **Demo sintético end-to-end** (`datito demo`, G10): un estudiante de
  juguete recorre el ciclo completo hasta DOMINADO en un curso sandbox
  autocontenido; el transcript se autovalida y reporta métricas de sesión
  (espera real, soluciones anticipadas, dudas registradas).
- ✅ Endpoint `GET /api/demo/socratico` con el mismo demo.
- ✅ **Paquete distribuible**: `python 15_TERMINITO/scripts/build_paquete.py`
  genera `dist/datito.zip` (~2.5 MB); doble clic en `start.py` y a chatear.
  Pruebas manuales: `docs/pruebas-manuales.md`.
- ⏳ Pendiente: instalar **Ollama** para el modo tutor (generación con LLM local).
- ⏳ Post-MVP (spec): familia de Datitos, exportación portable.
- ✅ **Política gobernando el chat** (`sesion.intercambio`): toda solución
  revelada se registra en `dudas.yaml` antes de decirse (UNO-B), la respuesta
  siguiente exige la transferencia (R5) y `:salir` reporta las métricas de
  sesión (REQ-TUT-002): esperas reales, soluciones, transferencias, dudas.

## Instalación

```bash
cd 15_TERMINITO
uv venv .venv && uv pip install -e ".[dev]"
# opcional pero recomendado (modo tutor):
#   curl -fsSL https://ollama.com/install.sh | sh && ollama pull qwen2.5:3b
```

## Uso (30 segundos)

```bash
source .venv/bin/activate
datito lista                          # cursos existentes
datito init fcd --materiales <rutas>  # crear curso (symlinks, no copia)
datito identidad fcd wizard           # definir los 8 componentes (conversación)
datito build fcd                      # parsear + índice + system prompt
datito chat fcd                       # diálogo con citas [:duda :status :salir]
datito eval fcd                       # distinciones con micro-progreso
datito status fcd [--mapa]            # dominio, métricas, dudas
```

Sin Ollama, `chat` opera en **modo exploración**: recupera y cita los fragmentos
más relevantes sin generar explicaciones. Todo lo demás funciona igual.

## Tests

```bash
.venv/bin/python -m pytest tests/ -q   # 15 tests (unidad + integración)
```

## Layout

```
src/datito/    motor (fragmentos, índice TF-IDF, evidencia, llm, identidad,
                tutor, lucha, dudas, evaluador, grafo, progreso, cli)
src/web/        placeholder (UI en post-MVP)
tests/          pytest
cursos/<slug>/  un curso = un directorio autocontenido (data-model.md)
docs/USO.md     documentación de uso del engine
```

Decisiones de diseño: `specs/001-datito-platform/research.md` (R1–R10) y
`docs/investigacion/rea-evidencia/sintesis-arquitectura.md`.
