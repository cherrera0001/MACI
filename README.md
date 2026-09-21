# MACI — Fundamentos de Ciencia de Datos

Repositorio de trabajo de **Cristóbal Herrera** para Fundamentos de Ciencia de
Datos (T2-2026), Universidad de Concepción.

Contiene el proyecto semestral (Proyecto 3 — predicción de precios de propiedades
en Melbourne), un desafío de clasificación (Galaxy Zoo), los laboratorios de la
asignatura, la reconstrucción documental del Certamen 2, y **Datito**, un tutor
personal de Ciencia de Datos construido sobre este mismo material.

**Punto de entrada:** [`01_DOCUMENTACION/00_INDICE_GENERAL.md`](01_DOCUMENTACION/00_INDICE_GENERAL.md)
· **Orden documental:** [`01_DOCUMENTACION/00_ORDEN_DOCUMENTAL.md`](01_DOCUMENTACION/00_ORDEN_DOCUMENTAL.md)
· **Contrato de Datito:** [`spec.md`](spec.md)

---

## Orden documental / Cómo leer

Arquitectura **repo-nativa** (sin Obsidian como segunda verdad):

1. Este `README.md`
2. [`01_DOCUMENTACION/00_INDICE_GENERAL.md`](01_DOCUMENTACION/00_INDICE_GENERAL.md) — mapa por necesidad
3. El `00_LEEME.md` del dominio
4. Canónicos del dominio (informe, análisis, JSON de resultados)
5. `fuentes/` o `99_ARCHIVO/` solo como evidencia / histórico

| Si necesitas… | Abre… |
|---|---|
| Orientarte | [`00_INDICE_GENERAL.md`](01_DOCUMENTACION/00_INDICE_GENERAL.md) |
| Protocolo (qué es canónico, dónde va lo nuevo) | [`00_ORDEN_DOCUMENTAL.md`](01_DOCUMENTACION/00_ORDEN_DOCUMENTAL.md) |
| Drift README↔disco | [`DIAGNOSTICO_DRIFT.md`](01_DOCUMENTACION/DIAGNOSTICO_DRIFT.md) · `python 03_CODIGO/auditar_drift_documental.py` |
| Certamen 2 | [`01_CERTAMEN2/00_LEEME.md`](01_DOCUMENTACION/01_CERTAMEN2/00_LEEME.md) |
| Proyecto 3 | [`03_PROYECTO_MELBOURNE/00_LEEME.md`](01_DOCUMENTACION/03_PROYECTO_MELBOURNE/00_LEEME.md) |
| Datito | [`07_DATITO/00_LEEME.md`](07_DATITO/00_LEEME.md) |

**Obsidian MCP / GitHub MCP:** no implementados. El mismo árbol se navega en GitHub con estos links relativos; estudio asistido ya usa NotebookLM (`.mcp.json`).

---

## Estructura

```
F:\MACI\
│
├── README.md                       ← este archivo
├── CLAUDE.md                       ← contexto para Claude Code; activa a Datito
├── spec.md                         ← contrato de Datito: garantías y verificación
├── .mcp.json                       ← conexión MCP a NotebookLM (sin secretos)
├── .env / .env.example             ← token de GitHub; .env NUNCA se versiona
├── push_github.ps1                 ← push con token desde .env, sin filtrar secretos
│
├── 01_DOCUMENTACION\               ← EMPEZAR AQUÍ
│   ├── 00_INDICE_GENERAL.md            mapa completo, paso a paso
│   ├── 00_ORDEN_DOCUMENTAL.md          protocolo: canónicos, capas, dónde va lo nuevo
│   ├── DIAGNOSTICO_DRIFT.md            README/índice vs disco
│   ├── 01_CERTAMEN2\                   reconstrucción del Certamen 2 + Word final
│   ├── 02_CURSO\                       enunciados y guía metodológica
│   ├── 03_PROYECTO_MELBOURNE\          índice del Proyecto 3
│   ├── 04_DESAFIO_GALAXYZOO\           índice del desafío de clasificación
│   ├── 05_HISTORICO\                   versiones invalidadas y por qué
│   └── 06_CERTAMEN1\                   material de compañero (enunciados útiles; respuestas no verificadas)
│
├── 02_PROYECTO_FCD\                ← material del curso
│   ├── Hito1\                          notebooks EDA y modelamiento + anclaje.json
│   └── Desafio\                        Galaxy Zoo: código, análisis, REPORT.md
│
├── 03_CODIGO\                      ← scripts del pipeline
│   ├── modelamiento_temporal.py        jerarquía de modelos, CV 2016, test 2017
│   ├── bootstrap_comparacion.py        bootstrap pareado, segmentos, permutación
│   ├── experimento_councilarea.py      experimento controlado A vs B
│   ├── experimento_councilarea_todos_modelos.py   extensión a los 6 modelos
│   ├── practica_a_markdown.py          convierte los prácticos para NotebookLM
│   ├── preparar_dashai.py              prepara el dataset para DashAI
│   ├── dashai_driver.py                réplica del modelamiento en DashAI
│   ├── generar_informe.py              → 06_ENTREGABLES/INFORME_MODELO_FCD_P3.md
│   ├── generar_pitch_v2.py             → 06_ENTREGABLES/PITCH_HITO2_REVISION.md + .pptx
│   ├── housing_visualizations.py       → visualizaciones/viz_*.html
│   ├── auditoria_dashai_vs_crudo.py    auditoría de consistencia
│   ├── correlacion_dashai.py           análisis de correlación
│   ├── auditar_drift_documental.py     checklist de rutas canónicas del orden documental
│   └── _migrar_rutas.py                registro auditable de la migración
│
├── 04_DATOS\
│   ├── 00_LEEME.md                     qué hay en datos
│   ├── housing_dashai_2016_2017.csv    dataset preprocesado subido a DashAI
│   └── GZ_mini_challenge_*.csv         train/test Galaxy Zoo (mini)
│
├── 05_RESULTADOS\                  ← salidas de los scripts, ninguna a mano
│   ├── resultados_temporal.json        6 modelos × 2 targets × 5 semillas
│   ├── comparacion_estadistica.json    IC bootstrap, error por segmento
│   ├── experimento_councilarea_*.json  experimento A vs B, con fecha
│   ├── dashai_*.json                   runs, split e índices de DashAI
│   ├── correlacion_dashai.json         matriz de correlación replicada
│   ├── auditoria_dashai_vs_crudo.json  auditoría de consistencia
│   └── predicciones_2017.csv           predicciones fila a fila
│
├── 06_ENTREGABLES\
│   ├── INFORME_MODELO_FCD_P3.md        informe final del modelamiento
│   ├── PITCH_HITO2_REVISION.md         revisión lámina por lámina
│   ├── Pitch_Hito2_v2.pptx / .pdf      presentación Hito 2
│   └── visualizaciones\viz_1..10.html  visualizaciones interactivas
│
├── 07_DATITO\                    ← tutor personal de Ciencia de Datos
│   ├── 00_LEEME.md                     cómo se usa — EMPEZAR AQUÍ
│   ├── datito.config.yaml            datos del alumno; las reglas van en la skill
│   ├── curriculum.yaml                 21 conceptos, prerrequisitos, material
│   ├── progreso.yaml                   estado y cadena de evidencia
│   ├── errores_conceptuales.yaml       errores observados + patrones a vigilar
│   ├── estado.md                       resumen autogenerado que se inyecta
│   ├── patron_evaluacion.md            cómo evalúa el profesor, desde sus certámenes
│   ├── referencia\                     fuentes, memoria, material — bajo demanda
│   ├── visual\                         artefactos HTML interactivos
│   ├── guias\                          material de referencia escrito
│   ├── cuadernillos\                   problemas CON solución — enseñan
│   ├── certamenes\                     problemas SIN solución — miden
│   ├── entregas\                       tus respuestas, para corregir
│   ├── transferencia\                  dataset sintético de otro dominio
│   ├── osint_*.md                      fuentes públicas de Ñuble y Gran Concepción
│   └── bitacora\                       una entrada por sesión
│
├── 08_PRACTICA\                    ← laboratorios de la asignatura
│   ├── 00_LEEME.md                     contenido y concepto que cubre cada uno
│   ├── [P1..P5] (res).ipynb            resueltos, material de consulta
│   ├── [P1..P5] (vacio).ipynb          sin resolver: los ejercicios
│   └── _markdown\                      conversión para NotebookLM
│
├── 09_CLASES\                      ← clases transcritas
│   └── transcripciones\                .md con marcas de tiempo + .txt para grep
│
├── 10_GRABACIÓN_CLASES\            ← vídeos originales. NO se versionan
│
├── 11_PRESENTACIÓN\                ← diapositivas / markdown de clases
│   └── _markdown\                      FCD-2026-2_* y resúmenes de clase
│
└── 99_ARCHIVO\                     ← conservado a propósito, no es basura
    ├── _obsoleto_split_aleatorio\      versión invalidada + por qué
    ├── _backup_pre_correlacion_...\    respaldo puntual
    ├── _pitch_img\ · _pitch_v2_png\    imágenes de las presentaciones
    └── CORRELACION_DIFF.patch
```

> **Nota:** existe una carpeta legacy `DOCUMENTACION\` (sin `01_`). No es canónica; usar siempre `01_DOCUMENTACION\`.

---

## Datito — tutor personal

Abre Claude Code en `F:\MACI` y escribe, por ejemplo:

```
Datito, quiero aprender validación cruzada
```

Datito consulta tu cuaderno de NotebookLM y el material del repositorio,
explica, pregunta, **espera tu respuesta**, analiza tu razonamiento y registra el
avance. Un concepto solo llega a `DOMINADO` con cuatro evidencias: explicar,
aplicar, interpretar resultados y transferir a otro problema.

| Comando | Qué hace | Contexto |
|---|---|---|
| `/datito` | Sesión de estudio: problema → tu respuesta → diagnóstico | Conversación |
| `/datito-progreso` | Informe de estado. Solo lectura | Conversación |
| `/datito-visual <concepto>` | Genera un HTML explicativo | Aislado |
| `/datito-corregir` | Corrige un lote de respuestas escritas | Aislado |

El tutor no puede ser un subagente —no sabría esperar tu respuesta—, pero
corregir y construir artefactos sí corren aislados, sin gastar el contexto de la
sesión.

**Las explicaciones van a un archivo, no al chat.** Cada concepto genera un HTML
interactivo en `07_DATITO/visual/`, que funciona sin conexión. El chat queda
para preguntar, esperar y diagnosticar.

Detalle en [`07_DATITO/00_LEEME.md`](07_DATITO/00_LEEME.md). Garantías y
método en [`spec.md`](spec.md).

### Estados de aprendizaje

```
NO_ESTUDIADO → EN_ESTUDIO → COMPRENSION_PARCIAL → COMPRENDIDO → DOMINADO
                                                          ↓
                                                  REQUIERE_REPASO
```

Decir "entendí" no es evidencia de nada. La regla completa está en `spec.md` §3.

---

## Fuentes

Jerarquía, de mayor a menor prioridad:

1. **Laboratorios de la asignatura** — `08_PRACTICA/`, 5 prácticos que cubren
   12 de los 21 conceptos
2. **Cuaderno de NotebookLM** — *Fundamentals of Data Science Syllabus*,
   **71 fuentes**: syllabus, presentaciones `FCD-2026-2_*`, resúmenes de clase,
   guías de autoestudio, tesis UdeC, ISLR, OpenIntro, el paper de XGBoost
3. **Proyectos propios** — Melbourne y Galaxy Zoo
4. **Fuentes académicas externas** — solo si lo anterior no alcanza

Toda afirmación de Datito lleva etiqueta de origen: `[FUENTE · NotebookLM: …]`,
`[FUENTE · Repo: …]`, `[INFERENCIA]` o `[DATITO]` para explicación propia.

### Las clases transcritas

`09_CLASES/transcripciones/` — grabaciones pasadas a texto con
[`faster-whisper`](https://github.com/SYSTRAN/faster-whisper) en local, sin GPU.
Dos formatos por clase: `.md` con marcas de tiempo por segmento, y `_plano.txt`
para buscar con `grep`.

Se versiona la transcripción, **nunca el vídeo**. Transcribir una clase nueva:

```bash
uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --listar
uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --todas
```

Valen como fuente de prioridad alta: contienen los ejemplos del profesor con sus
propias palabras. La cabecera advierte que son automáticas y pueden errar en
términos técnicos.

### Los prácticos

| | Tema | Conceptos que cubre |
|---|---|---|
| P1 | Pandas | `datos_features_target`, `eda` |
| P2 | Calidad de Datos | `limpieza_preparacion` |
| P3 | Numpy y Análisis Descriptivo | `eda` |
| P4 | Regresión | `regresion`, `train_validation_test`, `validacion_cruzada`, `overfitting_underfitting` |
| P5 | Clasificación | `clasificacion`, `matriz_confusion`, `metricas_clasificacion`, `arboles_decision`, `random_forest` |

Las versiones `(vacio)` son **ejercicios sin resolver** y se reservan como
evidencia de APLICAR. Datito no muestra la versión resuelta antes de que los
intentes.

### NotebookLM

Conectado por MCP mediante [`notebooklm-py`](https://github.com/teng-lin/notebooklm-py)
(MIT). Google **no ofrece API oficial para cuentas personales** — la integración
usa APIs internas no documentadas con cookies de sesión, que **caducan cada
pocas semanas**. Datito no depende de ella: si falla, avisa y sigue con el
material local.

Credenciales en `~/.notebooklm/`, **nunca** en el repositorio. Reautenticar:

```bash
notebooklm login --browser msedge    # Playwright abre Edge con perfil aislado
notebooklm auth check --test --json  # debe devolver "status": "ok"
```

---

## Resultados del Proyecto 3 — Melbourne

Verificados en [`05_RESULTADOS/resultados_temporal.json`](05_RESULTADOS/resultados_temporal.json).
Entrenamiento con 6.336 propiedades de 2016, evaluación sobre 7.244 de 2017.

| Modelo | CV 2016 MAE | Test 2017 MAE | Test R² |
|---|---|---|---|
| Baseline (mediana) | 449.160 | 431.649 | −0,080 |
| Ridge | 270.617 | 294.789 | 0,476 |
| Árbol de decisión | 224.982 | 250.771 | 0,609 |
| Random Forest | 174.525 | 216.400 | 0,696 |
| Gradient Boosting | 169.034 | 204.348 | 0,727 |
| HistGradientBoosting | 165.064 | 196.287 | 0,742 |
| Random Forest · log | 170.467 | 206.843 | 0,711 |
| Gradient Boosting · log | 161.499 | 192.441 | 0,747 |
| **HistGradientBoosting · log** | **159.777** | **188.218** | **0,757** |

Ridge sobre target logarítmico da R² **−17,0**: al deshacer el `expm1` sobre
valores extremos las predicciones se disparan. Es un resultado real y conviene
saber explicarlo.

**Dato clave de generalización:** el **29,1 %** de las propiedades de 2017 están
en suburbios que no existen en 2016.

### Experimento CouncilArea

[`05_RESULTADOS/experimento_councilarea_2026-09-18.json`](05_RESULTADOS/)

Experimento controlado: A sin `CouncilArea`, B idéntico salvo esa columna.
En validación cruzada dentro de 2016, B mejora 599 AUD (0,38 %) y gana 20 de 25
comparaciones pareadas.

**Decisión: se conserva A.** El análisis de faltantes lo explica — `CouncilArea`
tiene 0,0 % de nulos en 2016 y 18,9 % en 2017, y 14 de sus 33 categorías de 2017
nunca aparecen en 2016. Sumando ambas cosas, el **28,5 %** de las filas de 2017
no aportan información por esa columna. La validación en 2016 midió la feature
en condiciones que no se dan en 2017.

---

## Reproducir el proyecto

Ejecutar **desde `F:\MACI`** (no desde `03_CODIGO`), en este orden:

```bash
python 03_CODIGO/modelamiento_temporal.py     # jerarquía de modelos, CV 2016, test 2017
python 03_CODIGO/bootstrap_comparacion.py     # bootstrap pareado, segmentos, permutación
python 03_CODIGO/preparar_dashai.py
python 03_CODIGO/dashai_driver.py all         # réplica independiente en DashAI
python 03_CODIGO/generar_informe.py           # informe final
python 03_CODIGO/generar_pitch_v2.py          # revisión del pitch + presentación
```

Experimento controlado (la fase 3 exige `--config` explícito para que 2017 no se
toque por accidente):

```bash
python 03_CODIGO/experimento_councilarea.py fase1
python 03_CODIGO/experimento_councilarea.py fase3 --config A
```

Regenerar el Word del expediente del certamen:

```bash
python 01_DOCUMENTACION/01_CERTAMEN2/_construir_word.py
```

---

## Subir cambios a GitHub

```powershell
.\push_github.ps1
```

Lee el token desde `.env`, valida que pertenezca a `cherrera0001`, comprueba
permiso de escritura y sube. El token **nunca** pasa por la línea de comandos ni
queda en `.git/config`, y se redacta de cualquier mensaje de error.

`.env` está en `.gitignore`. Verificar en cualquier momento:

```bash
git check-ignore -v .env
git ls-files | grep -iE "storage_state|master_token|auth\.json|cookie|\.env$"   # debe salir vacío
```

---

## Notas de mantenimiento

**Reestructuración (15-09-2026).** El repositorio tenía 45 entradas sueltas en la
raíz. Se reorganizó por función. Las rutas de los scripts fueron migradas y
`03_CODIGO/_migrar_rutas.py` conserva la lista exacta de archivos tocados como
registro auditable. La migración se verificó de dos formas: las 45 referencias
resuelven correctamente, y `generar_informe.py` se ejecutó de extremo a extremo.

**Ningún archivo original fue modificado.** Los dos documentos del certamen están
intactos en `01_DOCUMENTACION\01_CERTAMEN2\fuentes\`.

**Discrepancia conocida.** Tres documentos dan cifras algo distintas para el
mismo modelo final: `resultados_temporal.json` (MAE 188.218, R² 0,757),
`00_INDICE_GENERAL.md` (185.449 / 0,765) e `INFORME_MODELO_FCD_P3.md` (R² 0,78).
El JSON es la fuente reproducible.
