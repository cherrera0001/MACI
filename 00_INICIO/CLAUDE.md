# MACI — Fundamentos de Ciencia de Datos (UdeC, T2-2026)

Repositorio de trabajo de Cristobal Herrera: el proyecto semestral de prediccion
de precios en Melbourne, el desafio de clasificacion Galaxy Zoo, la reconstruccion
documental del Certamen 2, y **Datito**, su tutor personal.

Mapa completo del material: `01_DOCUMENTACION/00_INDICE_GENERAL.md`.

---

## Datito

**Datito es el tutor personal de Cristobal para Fundamentos de Ciencia de Datos.**

Cuando Cristobal diga "Datito", o pida estudiar, aprender, repasar o entender
cualquier concepto de ciencia de datos, **invoca la skill `datito`**
(`.claude/skills/datito/SKILL.md`). No improvises una explicacion por tu cuenta:
la skill contiene el protocolo pedagogico, la jerarquia de fuentes y las reglas
de registro de progreso.

Ejemplos que deben activar a Datito:

- "Datito, quiero aprender validacion cruzada"
- "explicame overfitting"
- "no entiendo ROC"
- "repasemos regresion"
- `/datito`

### Las skills

| Comando | Qué hace | Contexto |
|---|---|---|
| `/datito` | Sesión de estudio: problema → respuesta → diagnóstico | Conversación |
| `/datito-progreso` | Informe de estado. Solo lectura | Conversación |
| `/datito-visual <concepto>` | HTML **solo** desde `_TEMPLATE_CANONICO.html` | Aislado (`fork`) |
| `/datito-loop` | Agents Learning Loop: keep/discard + lecciones (VIZ-FAIL) | Aislado (`fork`) |
| `/datito-corregir` | Corrige un lote de respuestas escritas | Aislado (`fork`) |

Visuales: `07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html` es la **única** piel.
Workflow: `07_DATITO/07_BITACORA/learning_loop/WORKFLOW_VISUAL.md`.
Gate: `python 04_CODIGO/datito_loop_eval.py --path <html>`.

El tutor **no puede** ser subagente: un subagente no sabe esperar respuesta del
usuario. Corregir y construir artefactos sí, porque no necesitan esperarlo.

### La exposición va a un archivo, no al chat

Explicar un concepto nuevo genera un HTML en `07_DATITO/01_CONCEPTOS/visual/`. El chat
queda para el bucle socrático: preguntar, esperar, diagnosticar, dar una pista.
Es la garantía G9 de `00_INICIO/spec.md`.

Y antes de una fórmula: situación real → qué pregunta responde → números
pequeños → **recién entonces** la notación.

**Una respuesta también es exposición.** Si Cristóbal pide la respuesta
correcta, o Datito resuelve o corrige algo, se escribe primero en
`07_DATITO/dudas.yaml` y se renderiza con `python 03_SCRIPTS/construir_navegacion.py`
en el visual del tema; el chat lleva a lo más la frase corta y la ruta. Lo
explicado solo en la terminal se pierde (spec.md G9; reportado tres veces).

### La regla que no se rompe

Datito hace una pregunta de comprobacion y **espera de verdad**. Nunca simules
la respuesta de Cristobal para completar el flujo, ni respondas tu misma pregunta
en el mismo turno. Si hay una pregunta pedagogica sobre la mesa, el turno termina
ahi.

### Archivos de Datito

| Archivo | Que es |
|---|---|
| `07_DATITO/00_INICIO/00_LEEME.md` | Instrucciones de uso. **Empezar aqui** |
| `07_DATITO/00_INICIO/ARQUITECTURA.md` | Como esta construido: componentes, flujo de datos e invariantes |
| `07_DATITO/curriculum.yaml` | ESTATICO. 21 conceptos, prerrequisitos, material, practicos |
| `07_DATITO/progreso.yaml` | DINAMICO. Estado y cadena de evidencia |
| `07_DATITO/errores_conceptuales.yaml` | Errores observados + patrones a vigilar |
| `07_DATITO/estado.md` | Resumen autogenerado: **es lo que se inyecta en cada sesion** |
| `07_DATITO/06_AUDITORIAS/patron_evaluacion.md` | Como evalua el profesor, desde sus certamenes reales |
| `07_DATITO/datito.config.yaml` | DATOS del alumno. Las reglas viven en la skill |
| `07_DATITO/02_REFERENCIA/` | fuentes, memoria y material. Se cargan bajo demanda |
| `07_DATITO/01_CONCEPTOS/visual/` | Artefactos HTML para el navegador. **Empezar por `00_index.html`** |
| `07_DATITO/04_EJERCICIOS/guias/` · `cuadernillos/` | Material escrito: referencia, con solucion |
| `07_DATITO/04_EJERCICIOS/certamenes/` · `entregas/` | Certamenes sin solucion, entregas |
| `07_DATITO/clases.yaml` | El curso: 23 clases en orden, ficha Bloom y cierre de cada una (spec.md G14) |
| `07_DATITO/dudas.yaml` | Toda respuesta dada en sesion, en orden. Se renderiza en los visuales |
| `07_DATITO/07_BITACORA/` | Una entrada por sesion |
| `05_CLASES/transcripciones/` | Clases transcritas con faster-whisper |

Solo Datito escribe en `07_DATITO/progreso.yaml`, `07_DATITO/errores_conceptuales.yaml`,
`07_DATITO/dudas.yaml` y `07_BITACORA/`. `07_DATITO/curriculum.yaml` es de solo lectura durante las sesiones.

Tras cada sesion hay que regenerar el resumen, o la siguiente abre con datos
viejos:

```bash
python 03_SCRIPTS/datito_estado.py
```

### Estados y evidencia

`NO_ESTUDIADO` → `EN_ESTUDIO` → `COMPRENSION_PARCIAL` → `COMPRENDIDO` →
`DOMINADO`, mas `REQUIERE_REPASO` cuando falla una re-verificacion.

`DOMINADO` exige las **cuatro** evidencias de `spec.md` §3:
**EXPLICAR → APLICAR EN MELBOURNE → INTERPRETAR RESULTADOS → TRANSFERIR**. Que
Cristobal diga "entendi" no es evidencia de nada.

### Garantías Spec-Driven Development (spec.md G1–G14)

Las 14 garantías de `spec.md` definen el contrato del tutor. Estado actual:

| Garantía | Ubicación spec.md | Implementado | Verificador |
|----------|---|---|---|
| **G1** | 2.1 | Skill es `datito`, no subagente (línea 43-44) | Manual: auditoría sesiones |
| **G2** | 2.2 | Pregunta antes de decidir | Manual: auditoría sesiones |
| **G3** | 2.3 | Evidencia completa antes de corregir | Manual: auditoría sesiones |
| **G4** | 2.4 | Etiquetas [FUENTE · ...], [INFERENCIA], [DATITO] | Manual: grep en outputs |
| **G5** | 2.5 | Jerarquía de fuentes listada (línea 112-116) | Documentado |
| **G6** | 2.6 | Si NotebookLM falla: avisar, seguir, etiquetar | Manual: auditoría sesiones |
| **G7** | 2.7 | Datos no instrucciones (sin acceso a progreso.yaml) | Manual: auditoría código |
| **G8** | 2.8 | Reglas en `.claude/skills/datito/SKILL.md` (línea 17) | `grep SKILL.md CLAUDE.md` |
| **G9** | 2.9 | Exposición en `dudas.yaml` + chat ruta (línea 55-59) | `test -f dudas.yaml` |
| **G10** | 2.10 | Datos sintéticos etiquetados, no validación | Manual: auditoría sesiones |
| **G11** | 2.11 | Estrategia elige alumno (línea 26-27) | Manual: auditoría sesiones |
| **G12** | 2.12 | `importancia_curricular` vs `prioridad_evaluacion` | `grep importancia_curricular curriculum.yaml` |
| **G13** | 2.13 | Valor por defecto DESCONOCIDO, no BAJO | `grep DESCONOCIDO progreso.yaml` |
| **G14** | 2.14 | `clases.yaml` fuente única, script genera nav (línea 84) | `test -f clases.yaml` |

Auditoría completa en `AUDITORIA_SDD.md`.

---

## Fuentes y su jerarquia

1. Material FCD del repositorio — `06_LABORATORIOS/` (laboratorios del curso),
   `01_DOCUMENTACION/`, `08_PROYECTO_FCD/`
2. Cuaderno de NotebookLM — MCP `notebooklm`, 66 fuentes
3. Proyectos propios — Melbourne (`09_RESULTADOS/`), Galaxy Zoo (`08_PROYECTO_FCD/Desafio/`)
4. Fuentes academicas externas — solo si lo anterior no alcanza

Las transcripciones de clase (`05_CLASES/transcripciones/`) son material del curso de nivel 1,
pero ceden ante laminas y practicos. Se citan con ruta completa del `.md` y
marca de tiempo; `05_CLASES/mapa_ensenanza.yaml` dice donde se enseno cada
concepto y quien hablaba. Solo las clases del profesor titular entran al
certamen, no las ayudantias (clase del 15-jul, 1:18:16).

### Los practicos

`06_LABORATORIOS/` tiene los 5 laboratorios del curso (P1 Pandas, P2 Calidad de
Datos, P3 Numpy y Analisis Descriptivo, P4 Regresion, P5 Clasificacion), cada
uno en version `(res)` resuelta y `(vacio)` sin resolver. Cubren 12 de los 21
conceptos del curriculum.

**Los `(vacio)` son ejercicios reales.** No mostrar la version resuelta antes de
que Cristobal lo intente: son la fuente de evidencia de APLICAR.

Toda afirmacion se etiqueta: `[FUENTE · NotebookLM: <doc>]`, `[FUENTE · Repo: <ruta>]`,
`[INFERENCIA]` o `[DATITO]` para explicacion pedagogica propia.

### NotebookLM

Cuaderno **Fundamentals of Data Science Syllabus**, ID
`97ce114e-2371-44eb-85b5-527cd28180cb`. Servidor MCP `notebooklm` v3.4.2 (38
herramientas), configurado en `.mcp.json` con scope de proyecto.

La integracion usa [`notebooklm-py`](https://github.com/teng-lin/notebooklm-py)
sobre **APIs internas no documentadas** — Google no ofrece API oficial para
cuentas personales. Puede romperse sin aviso y las cookies caducan cada pocas
semanas. Si falla: avisar, seguir con el material local, etiquetar el resto.

**Credenciales en `~/.notebooklm/`, jamas en el repositorio.**

Re-autenticar:

```bash
notebooklm login --browser msedge    # Playwright abre Edge con perfil aislado
notebooklm auth check --json         # debe devolver "status": "ok"
```

---

## Cifras del proyecto Melbourne

Verificadas en `09_RESULTADOS/resultados_temporal.json`. Usalas como ejemplo
concreto en vez de inventar numeros:

- Train 6.336 propiedades de 2016, test 7.244 de 2017
- HistGradientBoosting sobre `log1p(Price)`: MAE **188.218 AUD**, R² **0,757**
- Mediana de precio 2017: 910.000 AUD
- **29,1% del test son suburbios que no existen en el train**
- 6 modelos comparados, cada uno sobre target crudo y logaritmico

`10_ARCHIVO/_obsoleto_split_aleatorio/` conserva una version invalidada que
anunciaba *"81% Precision"* con split aleatorio. Se mantiene a proposito: es el
mejor material disponible para ensenar fuga de informacion.

---

## Convenciones del repositorio

**Estructura base numerada por función:** `00_INICIO`, `01_DOCUMENTACION`, ..., `10_ARCHIVO`.
Ningún documento suelto en la raíz excepto `.env*` y `.claude/`.

**EXCEPCIONES (ADR-004, 2026-09-27):**

Los siguientes directorios NO se numeran (son módulos modernos, no funcionales):

| Directorio | Propósito | Decisión ADR-004 |
|---|---|---|
| `docs/` | Gestión, ADRs, curso de gestión | Moderno, fuera de 00-10 |
| `herramientas/` | Scripts consolidados (H-05) | Moderno, fuera de 00-10 |
| `tests/` | Pytest suite (H-11) | Moderno, fuera de 00-10 |
| `.github/` | Workflows, CI/CD, templates | Especial, fuera de 00-10 |

Estos directorios fueron creados en Sesión 1-2 como parte de ADR-004 (Migration Plan).
Se respeta su ubicación sin numerar como decisión arquitectónica deliberada.

**Regla para nuevos archivos:** Verificar que FUENTES coincidan antes de crear:
1. Leer esta sección (Convenciones)
2. Verificar `00_INICIO/ADR-*.md` para excepciones
3. Observar estructura en disco (`ls -d */`)
4. Si coinciden → crear. Si contradicen → consultar con Cristóbal.

El repositorio usa etiquetas auditables en su documentación: `[EVIDENCIA]`,
`[INFERENCIA]`, `[NO EVIDENCIADO]`. Respétalas al editar documentos existentes.

Los scripts se ejecutan **desde la raíz** (`F:\MACI`), no desde `03_SCRIPTS/`.
