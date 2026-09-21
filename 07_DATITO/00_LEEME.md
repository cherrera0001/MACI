# 07 · DATITO — Tutor personal de Fundamentos de Ciencia de Datos

Datito **no explica conceptos: entrena resolución de problemas.** La prueba es
escrita, sin Internet, y el criterio de avance es cuántos problemas resuelves
**solo** — no cuánto contenido se te explicó.

Contrato completo y garantías verificables: [`../spec.md`](../spec.md).

---


> **¿Quieres entender cómo está construido, no cómo se usa?**
> [`ARQUITECTURA.md`](ARQUITECTURA.md) — componentes, los tres planos de
> datos, qué invariantes lo sostienen y qué cuesta cada decisión.

## Cómo se usa

Abre Claude Code en `F:\MACI` y habla:

```
Datito, quiero entender validación cruzada
```

| Comando | Qué hace | Dónde corre |
|---|---|---|
| `/datito` | Sesión de estudio: problema → tu respuesta → diagnóstico | Conversación |
| `/datito-progreso` | Informe de estado. Solo lectura | Conversación |
| `/datito-visual <concepto>` | Genera un HTML explicativo | Aislado |
| `/datito-corregir` | Corrige un lote de respuestas escritas | Aislado |

### Por qué dos corren aislados y dos no

El tutor **no puede** ser un subagente: un subagente no sabe pausar y esperar tu
respuesta, y ese es su núcleo. En cambio corregir un lote y construir un
artefacto no necesitan esperarte, así que corren en contexto propio y no gastan
el de la sesión.

---

## Estructura

```
07_DATITO/
├── 00_LEEME.md              este archivo
├── datito.config.yaml     DATOS del alumno. Las reglas viven en la skill
├── curriculum.yaml          21 conceptos: orden, prerrequisitos, material, prácticos
├── progreso.yaml            estado y cadena de evidencia          ← lo escribe Datito
├── errores_conceptuales.yaml  errores observados + patrones vigilados  ← ídem
├── estado.md                resumen autogenerado, es lo que se inyecta
├── patron_evaluacion.md     cómo evalúa el profesor, desde sus certámenes reales
│
├── referencia/              se carga bajo demanda, no en cada sesión
│   ├── fuentes.md               jerarquía, etiquetado, NotebookLM
│   ├── memoria.md               estados, evidencia, qué escribir y dónde
│   └── material.md              prácticos, certámenes, Melbourne, Galaxy Zoo
│
├── visual/                  artefactos HTML para leer en el navegador
├── guias/                   material de referencia escrito
├── cuadernillos/            problemas CON solución — enseñan
├── certamenes/              problemas SIN solución — miden
├── entregas/                donde dejas tus respuestas para corregir
├── transferencia/           dataset sintético de otro dominio
├── bitacora/                una entrada por sesión
└── osint_*.md               investigación de fuentes públicas (en pausa)
```

---

## Lo que ya puedes abrir

### Visuales interactivos — `visual/`

| Archivo | Qué muestra |
|---|---|
| `clase6_regresion.html` | La Clase 6 entera con el ejemplo del profesor: el peso del árbol según el radio del tronco. Incluye la zona sin datos, donde el modelo extrapola |
| `regresion_y_costo.html` | Camiones mineros. Mueves la recta y ves el costo y el R² cambiar en vivo |
| `matriz_confusion.html` | Detección de cáncer. Cuatro barras controlan la matriz; tres botones montan las trampas del certamen |

### Material escrito

- `guias/overfitting_underfitting.md` — los dos criterios, la inversión de métrica, remedios por mecanismo, procedimiento de siete pasos
- `cuadernillos/01_sobreajuste_y_calidad_de_datos.md` — nueve problemas con solución plegable, en los formatos del profesor

---

## Estudiado no es comprendido

Seis estados:

| Estado | Significado |
|---|---|
| `NO_ESTUDIADO` | No visto |
| `EN_ESTUDIO` | Datito lo explicó. Nada verificado |
| `COMPRENSION_PARCIAL` | Lo explicas con huecos, o el mecanismo incompleto |
| `COMPRENDIDO` | Explicas y aplicas correctamente |
| `DOMINADO` | Explicas, aplicas, interpretas **y** transfieres |
| `REQUIERE_REPASO` | Lo sabías y fallaste en una re-verificación |

### La cadena de evidencia

```
EXPLICAR  →  APLICAR  →  INTERPRETAR  →  TRANSFERIR
```

`DOMINADO` exige las cuatro. **Decir "entendí" no es evidencia de nada**, y
Datito tiene instrucción explícita de no aceptarlo. Tampoco cuenta repetir su
explicación, ni acertar tras una pista fuerte, ni acertar por el motivo
equivocado.

### Tres niveles de problema

| Nivel | Qué es | Acredita |
|---|---|---|
| 1 · Reconocimiento | Del mismo tipo que usa el profesor | — |
| 2 · Aplicación | Mismo concepto, cambian números o representación | `APLICAR` |
| 3 · Transferencia | Otro dominio, tú descubres qué aplica | `TRANSFERIR` |

---

## Cómo evalúa tu profesor

Detalle en [`patron_evaluacion.md`](patron_evaluacion.md). El hallazgo central:

**Las 11 fichas del Certamen 2 comparten un mismo campo sin excepción:
*distinción conceptual clave*.** Cada pregunta se resuelve separando dos
conceptos vecinos — número de modelos ≠ diversidad, más filas ≠ más columnas,
precisión ≠ sensibilidad, comparar un punto ≠ comparar un modelo.

**No evalúa definiciones. Evalúa discriminación.**

Peso por bloque:

| Bloque | Peso |
|---|---|
| Sobreajuste, generalización, validación, ensambles | **36 %** |
| Métricas de clasificación | **27 %** |
| Panorama de IA: LLM, agentes, redes | 18 % |
| Conducta metodológica | 18 % |

Y en el Certamen 1, la pregunta 9B de calidad de datos **vale 2,0 puntos** —
más que las ocho preguntas cerradas juntas.

---

## Fuentes

| Prioridad | Fuente |
|---|---|
| 1 | Laboratorios del curso — `08_PRACTICA/`, 12 de los 21 conceptos |
| 2 | Transcripciones de clase — `09_CLASES/` |
| 3 | Material FCD del repositorio |
| 4 | Cuaderno de NotebookLM |
| 5 | Proyectos propios: Melbourne, Galaxy Zoo |
| 6 | Fuentes académicas externas |

Toda afirmación lleva etiqueta: `[FUENTE · NotebookLM: …]`, `[FUENTE · Repo: …]`,
`[INFERENCIA]` o `[DATITO]` para explicación pedagógica propia.

### Material de terceros

`01_DOCUMENTACION/06_CERTAMEN1/` procede de un compañero. Los **enunciados** son
fiables; las **justificaciones no están verificadas** — el documento se titula
"Pauta Oficial" pero cierra con campos de plantilla sin rellenar.

---

## Mantenimiento

Tras cada sesión, Datito regenera el resumen que se inyecta la próxima vez:

```bash
python 03_CODIGO/datito_estado.py
```

Transcribir una clase nueva:

```bash
uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --listar
uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --todas
```

Reautenticar NotebookLM cuando caduque:

```bash
notebooklm login --browser msedge
notebooklm auth check --test --json     # debe devolver "status": "ok"
```

Datito **no depende** de NotebookLM: si falla, avisa, sigue con el material
local y etiqueta el resto.

---

## Para reutilizarlo en otro curso

1. Editar `datito.config.yaml`: alumno, asignatura, proyectos
2. Reescribir `curriculum.yaml` con los conceptos del nuevo programa
3. Vaciar `progreso.yaml`, `errores_conceptuales.yaml` y `bitacora/`
4. Reconstruir `patron_evaluacion.md` desde las evaluaciones anteriores del
   nuevo profesor — es lo que más cambia y lo que más rinde
5. `python 03_CODIGO/datito_estado.py`

Las skills de `.claude/skills/` **no se tocan**: leen de estos archivos.
