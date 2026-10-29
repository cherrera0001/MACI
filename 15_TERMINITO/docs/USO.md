# Uso del engine Datito

## Conceptos

- **Curso** = directorio autocontenido en `cursos/<slug>/` (portable por diseño).
- **Fragmento** = unidad de evidencia con `fid` estable (`<fuente>#<n>`) y
  referencia direccionable (timestamp `[h:mm:ss]`, `#ancla` o `pag. N`).
- **Evidencia citada o silencio**: toda afirmación del tutor debe citar un `fid`
  existente; si no hay fuente, lo dice (SC-002). El motor valida las citas
  post-generación.
- **Lucha productiva**: la solución completa nunca se revela antes del intento;
  `mostrar un paso` revela un paso del procedimiento y queda registrado.
- **Dominio**: `no_estudiado → en_estudio → comprendido → dominado`, derivado de
  los resultados de las distinciones. El panel revela por gating (escape:
  `status --mapa`).

## Comandos

| Comando | Qué hace |
|---|---|
| `datito init <slug> [--nombre --periodo] --materiales <rutas>` | Crea el curso; los materiales se **enlazan** (symlinks), no se copian. |
| `datito identidad <slug> wizard` | Conversación de 8 componentes (una decisión por pantalla). Genera y versiona `prompt/actual.md`. |
| `datito identidad <slug> ver` | Muestra el system prompt completo (siempre visible, principio I). |
| `datito identidad <slug> revertir --version <ts>` | Vuelve a una versión anterior. |
| `datito build <slug>` | Parsea materiales → fragmentos → índice TF-IDF; genera el prompt si la identidad está completa. |
| `datito chat <slug>` | Diálogo. `:duda <texto>` registra una duda con evidencia; `:status` muestra dominio. |
| `datito eval <slug>` | Sesión de distinciones: pregunta → respuesta abierta → rúbrica → feedback con frontera conceptual → actualización de dominio. |
| `datito status <slug> [--mapa]` | Métricas, panel de dominio con gating, conteo de dudas. |

## Modo exploración vs modo tutor

El engine detecta Ollama en `OLLAMA_HOST` (default `http://localhost:11434`,
modelo `TERMITO_MODELO`, default `qwen2.5:3b`).

- **Sin Ollama**: modo exploración — el chat recupera y cita los 3 fragmentos
  más relevantes; la evaluación califica con la heurística de criterios
  determinista.
- **Con Ollama**: el tutor genera explicaciones ancladas a los fragmentos
  recuperados (grounded generation, R5) y la evaluación usa la rúbrica con LLM.
  Las citas se validan igual: `fid` existente + soporte mínimo.

## Añadir materiales o ítems

- Materiales: symlink en `cursos/<slug>/materiales/` y `datito build <slug>`.
- Ítems de distinción: YAML en `cursos/<slug>/evaluaciones/*.yaml` con
  `conceptos` (≥2 vecinos del grafo), `pregunta`, `criterios`, `pasos`,
  `solucion`. Sin ≥2 conceptos no es distinción (se rechaza).

## Limitaciones conocidas

- Los `_plano.txt` duplican contenido de las transcripciones `.md` (doble
  fragmento); limpieza pendiente.
- La heurística de calificación compara raíces de 5 caracteres (español simple);
  con Ollama la rúbrica es la vía principal. Sus resultados se rotulan como de
  baja confianza (ver `calificar` en `evaluador.py`).
- La UI web (5 pantallas: home, wizard, chat, eval, panel) está operativa;
  `chat` es el punto de entrada principal y el CLI sigue siendo de primera clase.
