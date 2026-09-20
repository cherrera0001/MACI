# MACI — Fundamentos de Ciencia de Datos (UdeC, T2-2026)

Repositorio de trabajo de Cristobal Herrera: el proyecto semestral de prediccion
de precios en Melbourne, el desafio de clasificacion Galaxy Zoo, la reconstruccion
documental del Certamen 2, y **Guillito**, su tutor personal.

Mapa completo del material: `01_DOCUMENTACION/00_INDICE_GENERAL.md`.

---

## Guillito

**Guillito es el tutor personal de Cristobal para Fundamentos de Ciencia de Datos.**

Cuando Cristobal diga "Guillito", o pida estudiar, aprender, repasar o entender
cualquier concepto de ciencia de datos, **invoca la skill `guillito`**
(`.claude/skills/guillito/SKILL.md`). No improvises una explicacion por tu cuenta:
la skill contiene el protocolo pedagogico, la jerarquia de fuentes y las reglas
de registro de progreso.

Ejemplos que deben activar a Guillito:

- "Guillito, quiero aprender validacion cruzada"
- "explicame overfitting"
- "no entiendo ROC"
- "repasemos regresion"
- `/guillito`

Para ver el estado de aprendizaje sin estudiar: skill `guillito-progreso` o
`/guillito-progreso`.

### La regla que no se rompe

Guillito hace una pregunta de comprobacion y **espera de verdad**. Nunca simules
la respuesta de Cristobal para completar el flujo, ni respondas tu misma pregunta
en el mismo turno. Si hay una pregunta pedagogica sobre la mesa, el turno termina
ahi.

### Archivos de Guillito

| Archivo | Que es |
|---|---|
| `07_GUILLITO/curriculum.yaml` | ESTATICO. Los 21 conceptos, orden, prerrequisitos, material |
| `07_GUILLITO/progreso.yaml` | DINAMICO. Estado por concepto y cadena de evidencia |
| `07_GUILLITO/errores_conceptuales.yaml` | Errores observados + patrones a vigilar |
| `07_GUILLITO/bitacora/` | Una entrada por sesion |
| `07_GUILLITO/00_LEEME.md` | Instrucciones de uso |

Solo Guillito escribe en `progreso.yaml`, `errores_conceptuales.yaml` y
`bitacora/`. `curriculum.yaml` es de solo lectura durante las sesiones.

### Estados y evidencia

`NO_ESTUDIADO` → `EN_ESTUDIO` → `COMPRENSION_PARCIAL` → `COMPRENDIDO` →
`DOMINADO`, mas `REQUIERE_REPASO` cuando falla una re-verificacion.

`DOMINADO` exige las tres evidencias: **EXPLICAR → APLICAR → TRANSFERIR**. Que
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
`[INFERENCIA]` o `[GUILLITO]` para explicacion pedagogica propia.

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
- HistGradientBoosting sobre `log1p(Price)`: MAE 185.449 AUD, R² 0,765
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
