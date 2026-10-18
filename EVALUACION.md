# EVALUACIÓN DEL REPOSITORIO MACI

**Fecha:** 2026-10-17 · **Rama auditada:** `docs/gestion-github-v1` · **Alcance:** arquitectura, calidad de código, seguridad, tests, deuda técnica y documentación. Auditoría de solo lectura; el único archivo creado es este informe.

**Resumen ejecutivo:** El repo muestra gobernanza madura en su producto principal (fuente única YAML → HTML, verificación automatizada `verificar_todo.py`, contrato spec.md con autocontrol, manejo de secretos impecable, tests ejecutables en verde). Su problema dominante es la **deuda de la reestructuración 2026-09-25**: ~22 scripts con rutas `F:\MACI` hardcodeadas que hoy no corren, y varios documentos canónicos (`00_INICIO/README.md`, `INDEX_MAESTRO.md`, `courses.yaml`, `.gitignore`, partes de `spec.md`/`CLAUDE.md`) que describen layouts que ya no existen. Seguridad: sin hallazgos críticos ni altos.

| Severidad | Arquitectura | Código | Seguridad | Tests/ Docs | Total |
|---|---|---|---|---|---|
| Crítico | 1 | 2 | 0 | 3 | **6** |
| Alto | 3 | 3 | 0 | 2 | **8** |
| Medio | 10 | 7 | 0 | 7 | **24** |
| Bajo | 4 | 7 | 5 | 6 | **22** |

---

## 1. HALLAZGOS CRÍTICOS

### C1. Rutas absolutas de Windows (`F:\MACI\...`) hardcodeadas en ~22 archivos — los scripts no son ejecutables
La épica E-5 promete «Las entregas del ramo se reproducen desde el repo» (`README.md:165`), pero los scripts que generan los resultados canónicos apuntan al layout antiguo de la máquina del autor. En este clone (Linux) **fallan todos**. Verificado en vivo: `python3 03_SCRIPTS/verificar_contrato.py` reporta **8 FALLOs y 1 aviso** (G9, G12, G13, G14, Memoria, Estado, Curriculum) precisamente porque `RAIZ = r"F:\MACI"` no existe.

Ocurrencias principales:
- `03_SCRIPTS/modelamiento_temporal.py:28,121` · `correlacion_dashai.py:33,102` · `experimento_councilarea.py:46-47` · `experimento_councilarea_todos_modelos.py:37` · `grafo_conceptual.py:32` · `verificar_contrato.py:27` · `dashai_driver.py:12-14,150` · `auditoria_dashai_vs_crudo.py:17-23` · `bootstrap_comparacion.py:20,41,81` · `preparar_dashai.py:12,35,42` · `generar_informe.py:5` (`os.chdir(r"F:\MACI")`) · `generar_pitch_v2.py:16` · `integrar_clase.py:43` · `housing_visualizations.py:12,51,88,117,147,193,220,252,298,328,362` (caso extremo: 10 HTML escritos a `F:\MACI\06_ENTREGABLES\`, hoy `09_RESULTADOS/06_ENTREGABLES/`) · `procesar_80014/80038/80714/liderazgo/prototipos.py` · `04_CODIGO/validar_certamenes_visual.py:50-52`.

**Contraparte positiva:** el patrón correcto ya existe en casa (`construir_navegacion.py:57`, `verificar_visuales.py:38`, `datito_loop_eval.py:13`, `crear_backlog.py:24` derivan `RAIZ` de `__file__`). Hay dos convenciones incompatibles conviviendo.

### C2. `00_INICIO/README.md:37-113` — árbol de estructura completo y falsificado
Describe carpetas que no existen: `04_NOTEBOOKS/` (hoy `04_CODIGO/`), `02_DATOS/melbourne|galaxy-zoo|raw/`, `05_CLASES/laminas/`, `06_LABORATORIOS/P1_Pandas/…P5_Clasificacion/` (los `.ipynb` están sueltos), `07_DATITO/01_CONCEPTOS/` sin `visual/`, `08_PROYECTO_FCD/Melbourne/` (real: `Hito1/`+`Desafio/`), `09_RESULTADOS/melbourne|galaxy-zoo/` (real: `06_ENTREGABLES/`), `10_ARCHIVO/obsoleto_split_aleatorio/` (real: `_obsoleto_split_aleatorio/`). Omite `11_GOOGLE/`, `13_KAGGLE/`, `14_INVESTIGACION/`, `docs/`. Sellado «Última actualización: 2026-09-25» (línea 210), anterior a la estructura vigente. Además manda ejecutar `03_SCRIPTS/verificar_artefactos.py` y `verificar_g1_g9.py` (líneas 162-163), que **no existen**; los vigentes son `verificar_todo.py`, `verificar_contrato.py`, `verificar_visuales.py`.

### C3. `00_INICIO/INDEX_MAESTRO.md` — documento de un proyecto previo
Describe `F:\MACI\courses\` (hoy `10_ARCHIVO/courses/`), `F:\MACI\10_GRABACIÓN_CLASES\` (hoy `05_CLASES/10_GRABACIÓN_CLASES/`), 6 asignaturas ajenas a FCD, y ordena ejecutar `10_GRABACIÓN_CLASES\procesar_grabaciones.py` — **que no existe en el repo** (verificado con `git ls-files` y `find`). Cualquier agente o persona que lo abra recibe un mapa falso.

### C4. Contradicción ADR-004 vs CLAUDE.md: la estructura oficial del repo no está definida
`docs/adr/ADR-004-estructura-destino.md:3-5` dice «Estado: PROPUESTA · Gate: no aprobado… **No está aceptada**», y propone una estructura (`docs/spec.md`, `curso/`, `datito/`, `herramientas/`, `tests/`) que nunca se implementó. Sin embargo `00_INICIO/CLAUDE.md:215-227` trata las «EXCEPCIONES (ADR-004)» como decisión vigente y lista `herramientas/` y `tests/` (líneas 222-223) como directorios existentes — ninguno existe. El lector no puede saber qué estructura manda.

### C5. Scaffolding multi-curso roto: entry points que lanzan `ModuleNotFoundError`
`03_SCRIPTS/cli.py:6`, `__main__.py:4` y `platform.py:16` importan `from maci_platform.cli import main` — **el paquete `maci_platform` no existe** (la carpeta real es `03_SCRIPTS`, nombre no importable). `cli.py:41` es un stub autoconfesado («Processor invocation to be implemented in FASE-1»); `canvas.py` es un stub de 4 líneas. `datito_init_learner.py:46-54` exige `courses/` y `learners/` en la raíz (viven en `10_ARCHIVO/`), inrunnable tras la decisión H-01 de un solo curso.

### C6. `datito_batch_eval.py` toma decisiones sobre cadenas que nunca se imprimen
`04_CODIGO/datito_batch_eval.py:42-47` decide KEEP/DISCARD buscando `"LISTO"`, `"Gate KEEP"` o `"X"` en la salida de `datito_loop_eval.py` — pero ese script **nunca imprime esas cadenas** (imprime `path=…`, `score=…`, `OK/FAIL <gate>`). El «LISTO» lo imprime `verificar_todo.py:120`, que no es quien se invoca. Todo cae en la rama por returncode, y el docstring (líneas 3-6) promete un CSV que nunca se genera. Hoy el learning loop reporta basura.

---

## 2. HALLAZGOS ALTOS

### A1. Segunda copia divergente del estado de Datito en `10_ARCHIVO/learners/cristobal_herrera/`
13 archivos trackeados (`progreso.yaml`, `estado.md`, `dudas.yaml`, `errores_conceptuales.yaml`, `bitacora/…`) duplican los activos de `07_DATITO/` y **ya divergieron** (`dudas.yaml` y bitácora difieren; el archivo no tiene `learning_loop/`). Viola el principio del propio contrato: *«Duplicarlo aquí crearía una segunda fuente de verdad que se desincroniza»* (`spec.md:9-12`). El spec (§4) ni siquiera lista este archivo como fuente, así que nadie lo mantiene.

### A2. Sin manifiesto de dependencias
No hay `requirements.txt`, `pyproject.toml` ni `package.json`. La CI (`.github/workflows/ci.yml`) instala solo `pyyaml`; los scripts de ML importan pandas/numpy/sklearn/catboost/playwright/python-pptx sin forma de instalarlas versionadas. El README resuelve *ad hoc* con `uv run --with playwright` (`README.md:137`). Un clon fresco no puede ejecutar el pipeline completo: la reproducibilidad depende de la memoria del autor.

### A3. Conocimiento del proyecto ML duplicado en ≥5 archivos, con feature sets contradictorios
Listas de features e hiperparámetros copiadas en vez de un módulo compartido: `modelamiento_temporal.py:38-61`, `experimento_councilarea.py:53-57` (con comentario confesando el copy-paste), `:84-88`, `bootstrap_comparacion.py:29-31`, `preparar_dashai.py:20`, `correlacion_dashai.py:34`. Contradicción concreta: `bootstrap_comparacion.py:23` incluye `BuildingArea`/`YearBuilt` como numéricas mientras `modelamiento_temporal.py:41-42` las excluye. Además benchmark quemado en el código (`experimento_councilarea.py:228-232`, `MAE: 188217.698…, R2: 0.757`) que se desactualizará silenciosamente.

### A4. Ejecución a nivel de módulo y estado global
`modelamiento_temporal.py:32-122` (todo el flujo corre al importar; sin `if __name__ == "__main__"`), `housing_visualizations.py` completo (378 líneas, cero funciones), `bootstrap_comparacion.py:21-41`, `generar_pitch_v2.py:16` (`os.chdir` global), `dashai_driver.py:20-21` (dict `state` global mutado por todas las funciones). Impide importar/reutilizar y vuelve los efectos laterales invisibles.

### A5. `sys.exit`/`SystemExit` en funciones importables
`context_manager.py:307` (`get_context()`, cuyo docstring promete «lanza error explícito» pero mata cualquier proceso anfitrión), `correlacion_dashai.py:70`, `auditoria_dashai_vs_crudo.py:37,41,144-156` (`cargar_crudo()` es importado por otros), `construir_navegacion.py:321`.

### A6. `spec.md` (el contrato de auditoría) con rutas internas desactualizadas y contradicción de datos
- `07_DATITO/bitacora/` (`spec.md:9,306`; real: `07_DATITO/07_BITACORA/`) y `07_DATITO/visual/` (`spec.md:155,213,362`; real: `07_DATITO/01_CONCEPTOS/visual/`).
- `CLAUDE.md` y `.mcp.json` citados como si estuvieran en la raíz (`spec.md:308-310`; están en `00_INICIO/`).
- `spec.md:35-37` afirma «18 historias… **No hay historia de usuario sin clase; no hay clase sin historia**», pero `clases.yaml` tiene 23 clases y `historias_usuario.yaml` 18 → 5 clases sin historia. El README raíz (`README.md:113`) admite que «describen una numeración anterior (#42)», lo que invalida la garantía del contrato.

### A7. Datos pedagógicos hardcodeados en Python que contradicen la «fuente única»
`construir_navegacion.py:145-257` (VISUAL_DE, CERTAMEN, C3_ITEMS, ESPECIALES, RUTA_REPASO) y `:731-750` (DIST_VISUAL, C1_ITEMS): cientos de líneas de datos de certámenes en el código, duplicando `grafo.yaml` y `patron_evaluacion.md`, pese al comentario de la línea 725 («la fuente unica»). Igual en `grafo_conceptual.py:42-64,66-83`. Cambiar una pregunta de certamen exige editar código y regenerar a mano.

### A8. `01_DOCUMENTACION/00_INDICE_GENERAL.md` — enlaces rotos y cobertura incompleta
Tres enlaces rotos verificados: línea 86 `../07_DATITO/00_LEEME.md` (real: `07_DATITO/00_INICIO/00_LEEME.md`); línea 89 `../11_PRESENTACIÓN/_markdown/` (real: `05_CLASES/11_PRESENTACIÓN/_markdown/`); líneas 53 y 108 `../06_ENTREGABLES/INFORME_MODELO_FCD_P3.md` (existe en `09_RESULTADOS/06_ENTREGABLES/`). No cubre `04_CODIGO/`, `docs/`, `13_KAGGLE/`, `14_INVESTIGACION/`.

---

## 3. HALLAZGOS MEDIOS

### Arquitectura y estructura

- **M-A1. `courses.yaml` y su loader son código muerto con rutas obsoletas.** Apunta a `courses/80014_Emprendimiento` (real: `10_ARCHIVO/courses/…`), `10_GRABACIÓN_CLASES/80038_…` (real: `05_CLASES/…`) y `99_ARCHIVE/pipelines_legacy/procesar_80014.py` (inexistente). `load_manifest` no tiene callers (verificado por grep).
- **M-A2. `.gitignore` con reglas obsoletas tras la renumeración.** Línea 13 `05_RESULTADOS/dashai_state.json` (hoy `09_RESULTADOS`; el archivo no existe en ninguna parte), línea 42 `09_CLASES/video/` (no existe), línea 53 `11_PRESENTACIÓN/*.pdf` (hoy `05_CLASES/11_PRESENTACIÓN/`), línea 57 `08_PROYECTO_FCD/Certamen3/` (no existe). `.env*` duplicado (líneas 36-38 y 60).
- **M-A3. CSVs de Galaxy Zoo duplicados byte a byte.** `02_DATOS/GZ_mini_challenge_{train,test}.csv` ≡ `08_PROYECTO_FCD/Desafio/` (md5 verificado). ~16 MB duplicados y trackeados. La nota en `02_DATOS/00_LEEME.md` cita `02_PROYECTO_FCD/Desafio/`, ruta que ya no existe (drift).
- **M-A4. Curso completo archivado divergente.** `10_ARCHIVO/courses/fcd-2026-2/` tiene su propio `clases.yaml`, `curriculum.yaml`, `grafo.yaml`, `visual/`, `certamenes/`… y difiere del activo `07_DATITO/` (diff verificado). Segunda fuente completa navegable que confunde cualquier búsqueda.
- **M-A5. ADR fragmentados.** `docs/adr/` contiene solo `ADR-004`; ADR-001 y ADR-003 viven en `01_DOCUMENTACION/`; ADR-002 no existe. La historia de decisiones no se puede reconstruir desde un solo lugar.
- **M-A6. Convención numérica con hueco y carpetas sin versionar.** Falta `12_`. `11_GOOGLE/`, `13_KAGGLE/`, `14_INVESTIGACION/` están sin trackear (`??` en git status). La sección «Estructura» del README (`README.md:116-127`) solo documenta 3 de las 14 carpetas.
- **M-A7. Repo pesado.** 300 MB en `10_ARCHIVO/` (296 MB en cursos) + 231 MB en `.git`. Binarios grandes trackeados: dos `.xlsx` de 42 MB, PPTX de 21 MB, PDF de 20 MB. Ya hay issue abierto (#65, `README.md:87`), pero el peso sigue.
- **M-A8. Artefactos generados y backups en git.** `08_PROYECTO_FCD/Desafio/catboost_info/`, decenas de `.npy/.npz/.csv` en `Desafio/analysis/`, `.bak` en `13_KAGGLE/`, `04_CODIGO/reporte_validacion_nuevo.json` y `validacion_wave3.json` (el `.gitignore` excluye el nombre antiguo, no estos). `04_CODIGO/` mezcla tests con scaffolding de reparación (`css_mobile_fixer.py`, `js_slider_fixer.py`, `estructura_fixer.py`, `plan_reparacion.md`).
- **M-A9. Dos README de entrada con narrativas distintas.** `README.md` raíz define 3 productos; `00_INICIO/README.md` define 4 (añade «Reconstrucción Certamen 2») y dice que `02_DATOS/` contiene `melbourne/` (no existe; el CSV está suelto).
- **M-A10. `context_manager.py:114-217` mantiene la rama multi-curso** que hoy siempre falla y cae en `_resolver_un_curso()`: dos bloques de construcción de `ContextPaths` duplicados (166-183 vs 199-216). `manifest.py:45` tiene default mágico `last_processed='2026-09-22'`.

### Calidad de código

- **M-C1. Scripts one-shot con listas hardcodeadas = código muerto futuro.** `css_mobile_fixer.py:14-19`, `js_slider_fixer.py:16-21,25` (commit `cabca76` quemado), `estructura_fixer.py:18-27`. Nadie debería volver a correrlos, pero siguen en la rama principal junto a los tests.
- **M-C2. Código muerto, ramas inalcanzables y comentarios que mienten.** `js_slider_fixer.py:47-61` (`extract_slider_listeners()` nunca se llama); `estructura_fixer.py:88-89` (rama `else` que imprime `{error}` con `error=None`); `verificar_visuales.py:123` (`f"{e if terr else e}"` ternario redundante); `css_mobile_fixer.py:33` (comentario dice «último `</style>`», el código reemplaza el **primero**); `estructura_fixer.py:5-12` (docstring promete extraer `<title>`, usa h1 hardcodeado); `verificar_visuales.py:3-9` (semi-deprecado pero duplica regex de `datito_loop_eval.py`).
- **M-C3. `except:` desnudo** en `css_mobile_fixer.py:55`, `js_slider_fixer.py:37,86` (tragan `KeyboardInterrupt` y convierten cualquier fallo en un silencioso `False`); `verificar_piel_lectura.py:93` (`except Exception: pass`).
- **M-C4. Magic numbers sin nombre.** `clasificador_visual.py:56,92` («16 conceptos», «13/13 = 100%» quemados en texto); `cli.py:82` (`Courses: {total}/6`); `dashai_driver.py:94` (asertar 6336/7244); `grafo_conceptual.py:137-140` (umbrales 0.45/0.34/0.2/0.9 sin justificación); `auditoria_dashai_vs_crudo.py:93,100,143-156` (valores esperados duplicados en tabla y asserts).
- **M-C5. Dependencia frágil del CWD/sys.path.** `housing_visualizations.py:307` hace `from correlacion_dashai import …` (solo funciona si `03_SCRIPTS/` está en `sys.path`); los fixers y `clasificador_visual.py:34` usan rutas relativas que exigen correr desde la raíz. `descargar_contenido.py:21` busca `.env` en `03_SCRIPTS/.env` (no existe; el real está en la raíz), así que **nunca carga credenciales**; su docstring (línea 8) sigue diciendo `F:\MACI\.env`.
- **M-C6. Mezcla de idiomas sin convención** (docstrings en inglés, salidas en español, sin patrón): `clasificador_visual.py:1-8`, `css_mobile_fixer.py:2-7`, `context_manager.py`. Typo visible al usuario en `verificar_contrato.py:330`: «la comprobacion reviento».
- **M-C7. Definición de datos del curso dividida.** Tercera copia del plan de clases en `docs/curso-gestion/clases.yaml` que difiere de `07_DATITO/clases.yaml`.

### Tests

- **M-T1. Cobertura ~3 % de los módulos.** 60 `.py` activos (43 en `03_SCRIPTS/`, 17 en `04_CODIGO/`); solo 2 módulos de lógica tienen prueba directa (`datito_loop_eval.py` por import, `construir_navegacion.py` por subprocess). Todo `03_SCRIPTS/` (datos, DashAI, bootstrap, migraciones) carece de tests unitarios.
- **M-T2. CI solo vigila `main`** (`.github/workflows/ci.yml:4-7`): pushes a ramas de trabajo no ejecutan tests, pese a que `README.md:140` dice «corren en CI en cada push».
- **M-T3. `test_indice_curso.py:79-98` contiene un mutador escondido** (`reparar_href`/`reparar_archivo` con `write_text`) que ningún test usa: doble propósito y riesgo de ejecución accidental.
- **M-T4. `.agents/` ni trackeado ni ignorado**: el espejo que valida `test_learning_loop.py:46-55` podría committearse por accidente; en CI el test se salta (`skipUnless`) y la divergencia solo se detecta en local.

### Documentación

- **M-D1. `00_INICIO/CLAUDE.md` con reglas falsas.** Línea 213: «Ningún documento suelto en la raíz excepto `.env*` y `.claude/`» (hoy hay README.md, courses.yaml, vercel.json, .env.example, .gitignore, .vercelignore sueltos). Línea 231 manda verificar `00_INICIO/ADR-*.md` — no existe ninguno (contradicción interna con su línea 221). Líneas 222-223 presentan `herramientas/` y `tests/` («Pytest suite») como existentes — ninguno existe y no hay pytest en el repo.
- **M-D2. `00_INICIO/README.md` con cifras y contenido desactualizados.** Línea 84 dice que `07_DATITO/00_INICIO/` contiene «(curriculum, progreso, config)»; solo tiene `00_LEEME.md` y `ARQUITECTURA.md`. Línea 60: «Scripts… (41 total)»; hay 43 `.py`.
- **M-D3. `.env.example` desactualizado respecto al código real.** Lista `GITHUB_USER`/`GITHUB_TOKEN` (placeholder `ghp_` que dispara escáneres), pero no las variables que el código usa: `User_udec`, `Pass_udec`, `CANVAS_TOKEN` (`descargar_contenido.py:24-25,66`) y `GITHUB_TOKEN_CLASIC` (`crear_backlog.py:50`, `push_github.ps1:38`).
- **M-D4. Rutas Windows en un repo Linux** (`F:\MACI` en `00_INICIO/README.md:40,122,196`, `CLAUDE.md:238`, `INDEX_MAESTRO.md` entero); el repo vive en `/home/herre/src/MACI`.
- **M-D5. `10_ARCHIVO/_obsoleto_split_aleatorio/README_POR_QUE_OBSOLETO.md`** sigue citando `F:\MACI\` y scripts que ya están en `03_SCRIPTS/`.
- **M-D6. Outputs de notebooks commitidos** (`06_LABORATORIOS/*.ipynb`): PNG en base64 y CSS embebidos ensucian el historial y generan falsos positivos en escáneres (se detectó la cadena `AIza…` dentro de un PNG — coincidencia fortuita, no un secreto).

---

## 4. HALLAZGOS BAJOS

### Seguridad (sin hallazgos críticos ni altos; verificación en historial Git completo: cero secretos reales)

- **B-S1. Datos personales versionados.** Correos personales: `05_CLASES/10_GRABACIÓN_CLASES/80038_Procesos_Innovacion/NOTAS_INDICE.md:152` (gmail), `01_DOCUMENTACION/PRIMERA-ENTREGA-PLAN.md:78`, y capturas Canvas con datos académicos en `01_DOCUMENTACION/01_CERTAMEN2/fuentes/*.html`. Si el repo se hiciera público, estas capturas irían también. Revisar consentimiento de `06_LABORATORIOS/_markdown/2026_P5_Clasificación_res_ _1.md:8` (email de un tercero).
- **B-S2. Inyección de `<script>` desde historial Git** — `js_slider_fixer.py:63-75` extrae un script de un commit viejo (`git show cabca76`) y lo inyecta en páginas HTML. Fuente = propio repo (confiable en la práctica, sin `shell=True`), pero el patrón es frágil ante un historial reescrito/envenenado. Conviene documentar el commit fijado.
- **B-S3. HTML remoto guardado sin procesar** — `descargar_contenido.py:102-112` escribe el HTML de alumnos.udec.cl tal cual a disco. Hoy es dato no servido; si se publicara tal cual arrastraría el markup del origen.
- **B-S4. `03_SCRIPTS/` mezcla Python con `.sh`, `.ps1` y `.mjs`** (`push_github.ps1`, `setup_cloudflare_dns.sh`, `publicar_sitio.mjs`) — rompe la convención de la carpeta.
- **B-S5. `07_DATITO/01_CONCEPTOS/visual/index.html` duplicado** (redirección a `00_index.html`) junto a `00_index.html`.

### Calidad de código (bajo)

- `verificar_contrato.py:330` «reviento» → «revienta» (aparece 3 veces en la salida real).
- `housing_visualizations.py:306` comenta ruta `F:\MACI\correlacion_dashai.py` que ya no existe.
- `dashai_driver.py` one-liners con `;` (`save()`/`log()`), estilo inconsistente con el resto.
- `datito_loop_eval.py` y `verificar_piel_lectura.py` demuestran el estándar al que el resto debería aspirar (tipado, funciones puras, chequeo visual real) — no es un hallazgo, es la referencia.

---

## 5. ASPECTOS POSITIVOS (VERIFICADOS)

1. **Seguridad ejemplar del manejo de credenciales.** `.env` nunca versionado en todo el historial (`git log --follow -- .env` vacío; `.gitignore:36-38` correcto, doblemente con `.vercelignore`). Escaneo de `ghp_`, `github_pat_`, `AIza`, `sk-ant`, `sk-proj`, `Bearer` sobre todo el historial: **cero secretos reales**. `push_github.ps1:115,135,155` (token solo en memoria, redactado de errores, guard contra `.git/config`), `crear_backlog.py:181` (token vía `GH_TOKEN`, nunca por CLI).
2. **Sin vectores de inyección en Python.** Ningún `eval()`, `exec()`, `os.system()` ni `subprocess` con `shell=True`; los 14 `subprocess` usan listas con comandos fijos. Sin `pickle.loads`, sin `yaml.load` inseguro. Todas las llamadas `requests` son HTTPS con timeout; ningún `verify=False`. Sitio público sin XSS (sinks `innerHTML` con cadenas estáticas o `esc()`, validación de rutas en `publicar_sitio.mjs:52`, headers de seguridad en `vercel.json:13-21`).
3. **Tests ejecutables y en verde.** 25/26 tests pasan localmente (0,5 s) y el patrón del CI resuelve correctamente los imports. Asserts genuinos, docstrings que documentan la regresión con fecha/origen, guards `skipUnless` bien usados, y el patrón elegante de «generador sin nada pendiente» vía subprocess en modo `--revisar` solo-lectura.
4. **Autoverificación empírica real.** `correlacion_dashai.py:38-43,67-71` aborta si no reproduce las 15 celdas de DashAI; `auditoria_dashai_vs_crudo.py:22,36` fija el SHA-256 del insumo; `verificar_todo.py` orquesta generador/contrato/citas/tests/navegador/sitio. Es la defensa real contra regresiones.
5. **README raíz y `docs/` como estándar dorado.** Cifras exactas verificadas una a una contra YAML y disco (23 clases/22 con visual/16 páginas ≡ `clases.yaml:578` y `visual/`), instrucciones de ejecución completas (`README.md:131-138`), estado fechado explícitamente.
6. **Cultura de contrato.** spec.md G1–G14 con verificador por garantía, PR template con Definition of Done que exige tests, material obsoleto segregado con `README_POR_QUE_OBSOLETO.md` explicando el motivo.
7. **Buenas prácticas aisladas.** `construir_navegacion.py` documenta y cumple idempotencia con `--revisar` y escritura solo entre marcadores; `datito_loop_eval.py` (tipado, funciones puras, códigos de salida correctos); `crear_backlog.py` (idempotente, `--dry-run`).

---

## 6. RECOMENDACIONES CONCRETAS (ORDENADAS POR IMPACTO)

### Fase 1 — Destrabar la reproducibilidad (afecta al C1, C6, A2, A4, A5)

1. **Unificar la resolución de rutas.** Extender el patrón `RAIZ = Path(__file__).resolve().parents[N]` ya usado en `construir_navegacion.py:57` a los ~22 archivos con `F:\MACI`. Empezar por `verificar_contrato.py:27` (hoy falla con 8 FALLOs), `modelamiento_temporal.py:28,121`, `correlacion_dashai.py:33,102`. Hasta que esto no se haga, la promesa E-5 (`README.md:165`) no es verificable.
2. **Añadir guardas `if __name__ == "__main__":`** en `modelamiento_temporal.py:32-122`, `bootstrap_comparacion.py:21-41`, `dashai_driver.py:20-21`; refactorizar `housing_visualizations.py` (378 líneas, 0 funciones) a funciones.
3. **Crear `requirements.txt`** (pandas, numpy, scikit-learn, catboost, plotly, python-pptx, playwright, click, python-dotenv, requests, pyyaml — con versiones mínimas verificadas en la máquina del autor) y usarlo en `.github/workflows/ci.yml:27`.
4. **Corregir `datito_batch_eval.py:42-47`** para parsear la salida real de `datito_loop_eval.py` (`path=`/`score=`/`OK/FAIL`) o usar su returncode como única señal; actualizar el docstring o implementar el CSV prometido.

### Fase 2 — Restablecer la fuente única (afecta a C2–C5, A1, A3, A6, A7, A8)

5. **Reescribir o eliminar los documentos de entrada falsos.** `00_INICIO/README.md` (árbbol completo, líneas 37-113), `00_INICIO/INDEX_MAESTRO.md` (proyecto previo), y resolver el estado de ADR-004: o se acepta formalmente y se actualiza `CLAUDE.md:215-227`, o se marca «rechazada/superseded» y se corrige CLAUDE.md.
6. **Eliminar la copia divergente** `10_ARCHIVO/learners/cristobal_herrera/` (13 archivos) o fusionarla a `07_DATITO/`; añadir una nota en el spec §4 si se conserva.
7. **Extraer un módulo compartido** (p. ej. `03_SCRIPTS/melbourne_config.py`) con features e hiperparámetros usado por `modelamiento_temporal.py`, `experimento_councilarea.py`, `bootstrap_comparacion.py`, `preparar_dashai.py`, `correlacion_dashai.py`; resolver la contradicción `BuildingArea`/`YearBuilt` entre los dos primeros; mover el benchmark de `experimento_councilarea.py:228-232` a un fixture generado.
8. **Mover los datos de certámenes** de `construir_navegacion.py:145-257,731-750` y `grafo_conceptual.py:42-83` a YAML junto a `grafo.yaml` (coherente con la «fuente única» que el propio código predica).
9. **Actualizar `spec.md`** (rutas en líneas 9, 155, 213, 306, 308-310, 362) y reconciliar la garantía «18 historias/23 clases» (líneas 35-37) con la realidad de `clases.yaml` o corregir el YAML.
10. **Actualizar `.gitignore`** (reglas en líneas 13, 42, 53, 57; quitar `.env*` duplicado) y añadir exclusiones para `catboost_info/`, `analysis/*.npy`, `*.bak`, `04_CODIGO/*validacion*.json`.
11. **Decidir el destino del scaffolding multi-curso:** completar o borrar `cli.py`, `__main__.py`, `platform.py`, `canvas.py`, `datito_init_learner.py` (C5), y simplificar `context_manager.py:114-217` a la rama de un solo curso.
12. **Corregir `descargar_contenido.py:21`** para leer `.env` desde la raíz del repo (hoy nunca carga credenciales) y actualizar `.env.example` con `User_udec`, `Pass_udec`, `CANVAS_TOKEN`, `GITHUB_TOKEN_CLASIC`.

### Fase 3 — Higiene y cobertura (afecta a M-T1–M-T4, M-C1–M-C7)

13. **Mover los fixers one-shot** (`css_mobile_fixer.py`, `js_slider_fixer.py`, `estructura_fixer.py`, `validar_certamenes_visual.py`, `clasificador_visual.py`, `plan_reparacion.md` y los JSON de validación) a `10_ARCHIVO/` o a una carpeta `04_CODIGO/_herramientas/`.
14. **Extender CI a todas las ramas** (`.github/workflows/ci.yml:4-7`) o corregir el README (`README.md:140`).
15. **Añadir tests unitarios para `03_SCRIPTS/`**: prioridad a `context_manager.py`, `bootstrap_comparacion.py` y la lógica de parsing de `datito_batch_eval.py`. Sustituir `sys.exit` por excepciones en funciones importables (`context_manager.py:307`, `correlacion_dashai.py:70`, `auditoria_dashai_vs_crudo.py:37,41`, `construir_navegacion.py:321`).
16. **Barrido menor:** `except:` desnudos (`css_mobile_fixer.py:55`, `js_slider_fixer.py:37,86`), ternario redundante (`verificar_visuales.py:123`), comentarios que mienten (`css_mobile_fixer.py:33`, `estructura_fixer.py:5-12`), typo «reviento» (`verificar_contrato.py:330`), mutador escondido en `test_indice_curso.py:79-98`, `skipUnless` del espejo `.agents` en CI.
17. **Higiene Git:** considerar `nbstripout` para `06_LABORATORIOS`, resolver los CSVs de Galaxy Zoo duplicados (16 MB, md5 idéntico), y atacar el peso del repo (300 MB + 231 MB `.git`; el issue #65 ya lo reconoce).
18. **Si el repo pasara a público:** revisar capturas con datos personales en `01_DOCUMENTACION/01_CERTAMEN2/fuentes/` y correos (`05_CLASES/…/NOTAS_INDICE.md:152`, `01_DOCUMENTACION/PRIMERA-ENTREGA-PLAN.md:78`).

---

## 7. CONCLUSIÓN

El repositorio es **funcional y bien gobernado en su producto central** (curso Datito generado desde fuente única, verificación automatizada, secretos bien manejados, tests reales en verde), pero arrastra **deuda crítica de portabilidad y de sincronización documental**: la mitad de los scripts de datos no corre fuera de la máquina Windows del autor, y los documentos canónicos de entrada (`00_INICIO/`) describen un repositorio que ya no existe. Ningún hallazgo es de seguridad grave. La ruta de menor esfuerzo y mayor impacto es la Fase 1: unificar rutas con el patrón `__file__` que el propio repo ya demuestra, añadir un manifiesto de dependencias y corregir el parsing del learning loop. Con eso, la promesa de reproducibilidad (E-5) pasa de aspiración a verificable.
