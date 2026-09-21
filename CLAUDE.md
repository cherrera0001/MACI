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

### Las cuatro skills

| Comando | Qué hace | Contexto |
|---|---|---|
| `/datito` | Sesión de estudio: problema → respuesta → diagnóstico | Conversación |
| `/datito-progreso` | Informe de estado. Solo lectura | Conversación |
| `/datito-visual <concepto>` | Genera un HTML explicativo | Aislado (`fork`) |
| `/datito-corregir` | Corrige un lote de respuestas escritas | Aislado (`fork`) |

El tutor **no puede** ser subagente: un subagente no sabe esperar respuesta del
usuario. Corregir y construir artefactos sí, porque no necesitan esperarlo.

### La exposición va a un archivo, no al chat

Explicar un concepto nuevo genera un HTML en `07_DATITO/visual/`. El chat
queda para el bucle socrático: preguntar, esperar, diagnosticar, dar una pista.
Es la garantía G9 de `spec.md`.

Y antes de una fórmula: situación real → qué pregunta responde → números
pequeños → **recién entonces** la notación.

### La regla que no se rompe

Datito hace una pregunta de comprobacion y **espera de verdad**. Nunca simules
la respuesta de Cristobal para completar el flujo, ni respondas tu misma pregunta
en el mismo turno. Si hay una pregunta pedagogica sobre la mesa, el turno termina
ahi.

### Archivos de Datito

| Archivo | Que es |
|---|---|
| `07_DATITO/00_LEEME.md` | Instrucciones de uso. **Empezar aqui** |
| `07_DATITO/ARQUITECTURA.md` | Como esta construido: componentes, flujo de datos e invariantes |
| `07_DATITO/curriculum.yaml` | ESTATICO. 21 conceptos, prerrequisitos, material, practicos |
| `07_DATITO/progreso.yaml` | DINAMICO. Estado y cadena de evidencia |
| `07_DATITO/errores_conceptuales.yaml` | Errores observados + patrones a vigilar |
| `07_DATITO/estado.md` | Resumen autogenerado: **es lo que se inyecta en cada sesion** |
| `07_DATITO/patron_evaluacion.md` | Como evalua el profesor, desde sus certamenes reales |
| `07_DATITO/datito.config.yaml` | DATOS del alumno. Las reglas viven en la skill |
| `07_DATITO/referencia/` | fuentes, memoria y material. Se cargan bajo demanda |
| `07_DATITO/visual/` | Artefactos HTML para el navegador |
| `07_DATITO/guias/` · `cuadernillos/` · `certamenes/` | Material escrito: referencia, con solucion, sin solucion |
| `07_DATITO/bitacora/` | Una entrada por sesion |
| `09_CLASES/transcripciones/` | Clases transcritas con faster-whisper |

Solo Datito escribe en `progreso.yaml`, `errores_conceptuales.yaml` y
`bitacora/`. `curriculum.yaml` es de solo lectura durante las sesiones.

Tras cada sesion hay que regenerar el resumen, o la siguiente abre con datos
viejos:

```bash
python 03_CODIGO/datito_estado.py
```

### Estados y evidencia

`NO_ESTUDIADO` → `EN_ESTUDIO` → `COMPRENSION_PARCIAL` → `COMPRENDIDO` →
`DOMINADO`, mas `REQUIERE_REPASO` cuando falla una re-verificacion.

`DOMINADO` exige las **cuatro** evidencias de `spec.md` §3:
**EXPLICAR → APLICAR EN MELBOURNE → INTERPRETAR RESULTADOS → TRANSFERIR**. Que
Cristobal diga "entendi" no es evidencia de nada.

---

## Fuentes y su jerarquia

1. Material FCD del repositorio — `08_PRACTICA/` (laboratorios del curso),
   `01_DOCUMENTACION/`, `02_PROYECTO_FCD/`
2. Cuaderno de NotebookLM — MCP `notebooklm`, 66 fuentes
3. Proyectos propios — Melbourne (`05_RESULTADOS/`), Galaxy Zoo (`02_PROYECTO_FCD/Desafio/`)
4. Fuentes academicas externas — solo si lo anterior no alcanza

### Los practicos

`08_PRACTICA/` tiene los 5 laboratorios del curso (P1 Pandas, P2 Calidad de
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

Verificadas en `05_RESULTADOS/resultados_temporal.json`. Usalas como ejemplo
concreto en vez de inventar numeros:

- Train 6.336 propiedades de 2016, test 7.244 de 2017
- HistGradientBoosting sobre `log1p(Price)`: MAE **188.218 AUD**, R² **0,757**
- Mediana de precio 2017: 910.000 AUD
- **29,1% del test son suburbios que no existen en el train**
- 6 modelos comparados, cada uno sobre target crudo y logaritmico

`99_ARCHIVO/_obsoleto_split_aleatorio/` conserva una version invalidada que
anunciaba *"81% Precision"* con split aleatorio. Se mantiene a proposito: es el
mejor material disponible para ensenar fuga de informacion.

---

## Convenciones del repositorio

Estructura numerada por funcion (`01_` a `07_`, mas `99_ARCHIVO`). Ningun
documento suelto en la raiz.

El repositorio usa etiquetas auditables en su documentacion: `[EVIDENCIA]`,
`[INFERENCIA]`, `[NO EVIDENCIADO]`. Respetalas al editar documentos existentes.

Los scripts se ejecutan **desde la raiz** (`F:\MACI`), no desde `03_CODIGO/`.
