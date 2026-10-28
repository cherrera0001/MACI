# MACI — Fundamentos de Ciencia de Datos (UdeC, T2-2026)

**Repositorio de trabajo:** proyecto semestral (Melbourne, Galaxy Zoo), material
del curso y **Datito**, el tutor personal que corre como skill de Claude Code.

Mapa completo del material: `01_DOCUMENTACION/00_INDICE_GENERAL.md`. Contrato del
tutor y garantías G1–G14: [`CLAUDE.md`](CLAUDE.md) y [`spec.md`](spec.md).

---

## Antes de decir «listo»

```bash
python 03_SCRIPTS/verificar_todo.py        # generador, contrato, citas, tests
```

Nada se declara terminado hasta que esto imprime `LISTO: todo verificado`
(`--navegador` y `--en-linea` añaden pruebas con navegador y el sitio publicado).
La CI ejecuta esta verificación en cada push.

## Qué hay en cada carpeta (estructura real)

| Carpeta | Qué contiene |
|---|---|
| `00_INICIO/` | Punto de entrada: este README, `CLAUDE.md`, `spec.md`, `INDEX_MAESTRO.md` |
| `01_DOCUMENTACION/` | Documentación del curso, ADR (001–003), diagnósticos y auditorías (`EVALUACION.md` en la raíz) |
| `02_DATOS/` | Datasets: Melbourne (`housing_dashai_2016_2017.csv`), Galaxy Zoo, cáncer de mama |
| `03_SCRIPTS/` | Scripts operativos: generador del curso, verificadores, experimentos, transcripción |
| `04_CODIGO/` | Tests del curso y del learning loop (`test_*.py`, `datito_loop_eval.py`) |
| `05_CLASES/` | 14 sesiones con transcripción, láminas en `_markdown/`, `mapa_ensenanza.yaml`, `indice_clases.yaml` |
| `06_LABORATORIOS/` | Prácticos P1–P5 del curso, en versiones `(res)` y `(vacio)` |
| `07_DATITO/` | Datito: currículum (21 conceptos), progreso, dudas, errores, bitácora, visuales HTML del curso |
| `08_PROYECTO_FCD/` | Proyecto semestral: Melbourne (`Hito1/`) y desafío Galaxy Zoo (`Desafio/`) |
| `09_RESULTADOS/` | Resultados medidos del proyecto (MAE 188.218, R² 0,757 en `resultados_temporal.json`) y entregables |
| `10_ARCHIVO/` | Histórico y obsoleto conservado a propósito (p. ej. `_obsoleto_split_aleatorio/`, respaldos Canvas) |
| `11_GOOGLE/` · `13_KAGGLE/` · `14_INVESTIGACION/` | Material suelto, caso Kaggle documentado, investigación sobre azar físico |
| `15_TERMINITO/` | Motor Datito 1.0 (MVP): paquete Python instalable, offline-first, con su propio README y spec |
| `docs/` | ADR-004, gestión, wiki, investigación de estado del arte (`docs/investigacion/`) |
| `specs/` | Especificaciones Spec Kit: `001-termito-platform/`, `002-evolucion-app-tutor/` |
| `dist/` · `dist-src/` | Paquete distribuible del motor y sus lanzadores |

## Datito en 30 segundos

- Las reglas pedagógicas viven en `.claude/skills/datito/SKILL.md` (se carga en
  cada sesión); los datos del alumno, en `07_DATITO/*.yaml` (fuente única de verdad).
- La memoria resumida que se inyecta al abrir sesión es `07_DATITO/estado.md`,
  generada con `python 03_SCRIPTS/datito_estado.py`.
- El curso se estudia como secuencia en `07_DATITO/01_CONCEPTOS/visual/00_index.html`.
- Verificación del contrato: `python 03_SCRIPTS/verificar_contrato.py`.

## Convenciones

- Los scripts se ejecutan **desde la raíz del repo**, no desde `03_SCRIPTS/`.
- Estructura numerada `00_`–`10_` + módulos modernos sin numerar (`docs/`,
  `specs/`, `15_TERMINITO/`) según ADR-004.
- Los documentos usan etiquetas auditables `[EVIDENCIA]`, `[INFERENCIA]`,
  `[NO EVIDENCIADO]` y citan archivo:línea.

---

**Última actualización:** 2026-10-27 (sincronizado con la estructura real;
anterior versión de 2026-09-25 describía un árbol que ya no existía).
