# MACI — Máquina Asistida de Ciencia de Datos Interactiva

**MACI** es el repositorio de trabajo para **Fundamentos de Ciencia de Datos** (FCD) de la Universidad de Concepción, semestre T2-2026. Contiene:

1. **Datito**: tutor personal interactivo (skill en `.claude/skills/datito/`)
2. **Curso estático**: 22 clases HTML interactivas, transcripciones, certámenes
3. **Spec Kit**: framework de Spec-Driven Development integrado
4. **Sistema de rastreo**: progreso, errores conceptuales, dudas resueltas

## Qué es este repositorio

- **18 Historias de Usuario** mapeadas a aprendizaje (US-01 a US-18 en `historias_usuario.yaml`)
- **17 Conceptos curriculares** organizados en orden de dependencias (`curriculum.yaml`)
- **22 Clases** con estructura Bloom y navegación automática (`clases.yaml`)
- **Rastreo de estado** con cadena de evidencia: explicar → aplicar → interpretar → transferir
- **Sin conexión**: todo funciona localmente en HTML5 + Canvas + SVG

## Cómo estudiar

1. Abre el índice (archivo `07_DATITO/01_CONCEPTOS/visual/00_index.html` localmente, o desde la URL tras el deploy)
2. En cada clase: **predice antes de mover** un control
3. Resuelve los ejercicios **antes de** abrir las respuestas (`<details>`)
4. Lee la lección final y pasa a la siguiente

**21 clases están listas. La clase 19 (Repaso integrado: el proyecto Melbourne) está pendiente.**

## El tutor Datito

Datito es el asistente que **no está en este sitio**. Sigue siendo local en tu máquina (en `F:/MACI`). Aquí solo tienes el curso estático.

En Datito puedes:
- Estudiar cada concepto paso a paso
- Hacer preguntas en lenguaje natural
- Grabar audio de tus respuestas

Ese es un software aparte. **Este deploy es solo el material del curso.**

## Navegación y estructura

```
Entrada
  ↓
07_DATITO/01_CONCEPTOS/visual/00_index.html
  ├─ 22 clases (01_fundamentos.html → 19_deep_learning.html)
  ├─ 3 certámenes (04_EJERCICIOS/certamen_1.html, certamen_2.html, ...)
  ├─ Transcripciones (05_CLASES/transcripciones/)
  └─ Guías y referencias (04_EJERCICIOS/guias/, 02_REFERENCIA/)
```

Cada visual es independiente. Los enlaces funcionan sin servidor.

## Garantías

✅ **Todo funciona sin conexión**
✅ **Todas las clases tienen el mismo diseño (template canónico v1)**
✅ **Los certámenes son autocorregibles**
✅ **Las transcripciones están integradas y citadas**
✅ **Los tests verifican que no hay enlaces rotos**

## Información técnica

- Lenguaje: HTML5 + CSS3 (sin CDN, sin frameworks pesados)
- Gráficos: Canvas y SVG inline
- Interactividad: JavaScript plano (sin librerías remotas)
- Deploy: Static site en Vercel (sin build, sin servidor)
- Almacenamiento: LocalStorage (marca de clases leídas, solo en tu navegador)

## Para estudiantes

Abre `07_DATITO/01_CONCEPTOS/visual/00_index.html` en tu navegador. No necesitas nada más.

Si estás viendo esto desde Internet: la URL que ves es el sitio publicado. Los enlaces funcionan igual.

## Estructura de Datito (tutor interactivo)

Ubicación: `./.claude/skills/datito/SKILL.md` (skill autónoma, se carga por sesión)

**Fuentes únicas de verdad:**
- `07_DATITO/curriculum.yaml` — 17 conceptos (plan estático)
- `07_DATITO/clases.yaml` — 22 clases en secuencia (orden de estudio)
- `07_DATITO/historias_usuario.yaml` — 18 historias con criterios de aceptación
- `07_DATITO/progreso.yaml` — estado actual (DESCONOCIDO → ... → DOMINADO)
- `07_DATITO/errores_conceptuales.yaml` — observados + patrones vigilados
- `07_DATITO/dudas.yaml` — respuestas dadas (se renderizan en visuales)
- `07_DATITO/datito.config.yaml` — datos del alumno (no reglas)

**Garantías (spec.md §2):**
- G1: Espera de verdad (pausa, no simula respuesta)
- G4: Cada afirmación lleva etiqueta (FUENTE, INFERENCIA, DATITO)
- G9: Exposición en artefactos consultables (HTML, no solo chat)
- G14: Material es un curso, no una carpeta (clases.yaml es fuente única)

## Para profesores / mantenimiento

Regenerar navegación: `python 03_SCRIPTS/construir_navegacion.py`
- Lee `clases.yaml` → genera portada y cierres de clase
- Lee `dudas.yaml` → renderiza respuestas en visuales
- Lee `grafo.yaml` → calcula prerrequisitos

Usar Spec Kit:
- `/speckit-constitution` — Establecer principios del proyecto
- `/speckit-specify` — Crear especificación base
- `/speckit-plan` — Diseñar solución
- `/speckit-tasks` — Generar tareas accionables

**No uses scripts de reparación (repair_*.py) en producción.**

## Estado actual (2026-09-27)

| Componente | Estado |
|---|---|
| **Historias de Usuario** | ✅ 18 definidas (US-01 a US-18), criterios de aceptación auditables |
| **Spec Kit** | ✅ Integrado (.specify/, .claude/skills/speckit-*) |
| **progreso.yaml** | ✅ Rastreador de 17 conceptos (DESCONOCIDO por defecto) |
| **Datito SKILL** | ✅ 14 garantías (G1–G14) documentadas en spec.md |
| **Clases HTML** | ✅ 22 clases con estructura Bloom, generadas desde clases.yaml |
| **Certámenes** | ✅ 3 funcionales (autocorregibles con `<details>`) |
| **Transcripciones** | ✅ 15/15 integradas con marca de tiempo |
| **GitHub Project** | ✅ Project #3 (MACI), issues #20 y #23 en Todo |
| **Árbol canónico** | ✅ 00_INICIO–10_ARCHIVO + docs/.github/.specify/ |
| **Dudas resueltas** | ✅ Sistema en place, 0 dudas logueadas (primera sesión) |

## Cómo empezar

### Como alumno (estudiar)
1. Abre `.claude/skills/datito/SKILL.md` o escribe `/datito` en Claude Code
2. Haz preguntas sobre los conceptos
3. Datito te preguntará, esperará tu respuesta, diagnosticará y te guiará
4. Verifica tu progreso en `07_DATITO/progreso.yaml`

### Como profesor (mantener)
1. Lee `00_INICIO/spec.md` para entender garantías
2. Actualiza `07_DATITO/clases.yaml` si cambias el orden de clases
3. Usa `/speckit-*` skills para cambios estructurales
4. Los cambios a curriculum deben pasar por `00_INICIO/historias_usuario.yaml`

### Como desarrollador (integración)
- Spec Kit está en `.specify/` (no está versionado su Git)
- MCP NotebookLM en `.mcp.json` (credenciales en `~/.notebooklm/`)
- Tests en `04_CODIGO/test_*.py` (corren en CI)
- Visuales en `07_DATITO/01_CONCEPTOS/visual/` (template canonical)

## Licencia y atribución

**Contenido académico:** Profesor Titular, UdeC (Fundamentos de Ciencia de Datos)  
**Datito (tutor interactivo):** Claude Code + Spec Kit framework  
**Estructura y sistema:** 2026-09 · T2-2026

---

Para dudas académicas: consulta las transcripciones en cada clase o pregunta a Datito.  
Para bugs en el sistema: abre issue en GitHub (cherrera0001/MACI).
