# Inventario MACI — Repositorio y sistemas

**Fecha de inventario:** 2026-09-27  
**Alcance:** Sistemas, desfases, agentes, tablero GitHub  
**Modo:** Solo lectura. Cada fila cita un archivo abierto en esta pasada.

No es un backlog todavía. Las historias salen de la tabla 2. No se adopta Spec Kit, no se exporta este archivo y no se carga en el cuaderno de Fundamentos.

---

## Tabla 1: Sistemas

| Sistema | Documentos que lo describen | Agentes que escriben | Fuente de verdad | Documentos que contradicen |
|---------|---------------------------|-------------------|------------------|--------------------------|
| **Datito (tutor)** | `00_INICIO/spec.md` (contrato, v2, 2026-09-21). `00_INICIO/CLAUDE.md`. `07_DATITO/00_INICIO/ARQUITECTURA.md` (v1, 2026-09-20). | Seis skills en `.claude/skills/`: `datito`, `datito-progreso`, `datito-visual`, `datito-corregir`, `datito-pedagogia`, `datito-loop`. | `00_INICIO/spec.md` | `ARQUITECTURA.md` enlaza `../spec.md`, que resuelve a `07_DATITO/spec.md` y no existe. El mapa §10 coloca archivos en la raíz de `07_DATITO/` que en disco están en `07_DATITO/00_INICIO/`. §2 y §10 nombran cinco skills y omiten `datito-loop`. |
| **Curso estático** | `README.md`. `07_DATITO/00_INICIO/clases.yaml` (n: 1–22). Portada `07_DATITO/01_CONCEPTOS/visual/00_index.html`. Hay otro `07_DATITO/clases.yaml`, más corto, que no es este curso. | `datito-visual` escribe HTML. `03_SCRIPTS/construir_navegacion.py` regenera navegación. El README manda a `04_CODIGO/test_indice_curso.py`. | `07_DATITO/00_INICIO/clases.yaml` para el orden. El HTML publicado es el de `01_CONCEPTOS/visual/`. | `n: 19` tiene `visual: null`. `n: 18` declara `dl_llm_agentes.html`; en disco la página es `19_deep_learning.html`. Certamen 3 existe como HTML y no tiene `n:`. |
| **Melbourne** | `00_INICIO/CLAUDE.md` (§Cifras). `08_PROYECTO_FCD/Hito1/`. `09_RESULTADOS/resultados_temporal.json`. `.cursor/rules/maci-coherencia-hitos.mdc` y `.cursor/agents/puente-hito.md`. | `puente-hito` no escribe archivos: vigila el relato del Hito 2. | Decisión cerrada del Hito 1: Random Forest, R² test 0.6908, MAE $218,847 (regla `maci-coherencia-hitos` y `puente-hito.md`). | `CLAUDE.md` y el criterio de dominio de `clases.yaml` `n: 19` citan MAE 188.218 y R² 0,757. Esos números están en `resultados_temporal.json`, clave `HistGradientBoosting \| log` (`test2017_MAE` 188217.7, `test2017_R2` 0.757). Son un experimento posterior, no el modelo aceptado. |
| **Galaxy Zoo** | `00_INICIO/CLAUDE.md` (§Fuentes). `08_PROYECTO_FCD/Desafio/`. | Ninguno de los seis skills lo tiene como escritura propia. | CSV en `02_DATOS/GZ_mini_challenge_*.csv` y el análisis en `08_PROYECTO_FCD/Desafio/`. | `README.md` no lo nombra. `01_DOCUMENTACION/DIAGNOSTICO_DRIFT.md` (2026-09-20) ya lo señaló; ese diagnóstico no es el estado de hoy del README. |
| **Vercel** | `README.md`. `vercel.json`. `index.html` en la raíz. | Ningún skill del repo. El deploy es externo. | `vercel.json` (solo headers) e `index.html` (redirige a `07_DATITO/01_CONCEPTOS/visual/00_index.html`). | El catch-all 404 que registró el drift del 2026-09-20 no está en el `vercel.json` abierto hoy. |

---

## Tabla 2: Desfases

Cada fila es una historia futura. La ruta real se abrió, o se comprobó que no existe.

| Ruta citada | Ruta real | Archivo que cita | Qué se sostuvo al abrir |
|-------------|-----------|------------------|-------------------------|
| `../spec.md` | `07_DATITO/spec.md` no existe. El contrato está en `00_INICIO/spec.md`. | `07_DATITO/00_INICIO/ARQUITECTURA.md` | Enlace roto. |
| `07_DATITO/ARQUITECTURA.md`, `07_DATITO/visual/`, yaml de Datito en la raíz de `07_DATITO/` | `07_DATITO/00_INICIO/ARQUITECTURA.md`. HTML en `07_DATITO/01_CONCEPTOS/visual/`. Yaml de curso en `07_DATITO/00_INICIO/`. | Mapa §10 de `ARQUITECTURA.md` | El mapa no coincide con el árbol. |
| `.mcp.json` en la raíz, «scope de proyecto» | `00_INICIO/.mcp.json` existe y declara el servidor `notebooklm`. | `00_INICIO/CLAUDE.md` | No es una ausencia. Es una ruta sin carpeta. Credenciales siguen en `~/.notebooklm/`, fuera del repo (spec.md G6). |
| `dl_llm_agentes.html` | `07_DATITO/01_CONCEPTOS/visual/19_deep_learning.html` | `07_DATITO/00_INICIO/clases.yaml`, `n: 18` | El nombre del visual no es el del archivo. |
| `visual: null` en la clase 19 | No hay HTML de «Repaso integrado: el proyecto Melbourne». | `07_DATITO/00_INICIO/clases.yaml`, `n: 19` | El README al decir que la clase 19 está pendiente coincide con `visual: null`. |
| MAE 188.218 y R² 0,757 como cifras para defender Melbourne | Esas cifras son `HistGradientBoosting \| log` en `09_RESULTADOS/resultados_temporal.json`. El Hito 1 aceptado es Random Forest, R² test 0.6908, MAE $218,847. | `00_INICIO/CLAUDE.md` y `clases.yaml` `n: 19` (`criterio_dominio`) | Dos juegos de cifras. El JSON no reemplaza la decisión del Hito 1. |
| Solo `03_SCRIPTS/` | `verificar_visuales.py` está en `03_SCRIPTS/` y en `04_CODIGO/`. | `ARQUITECTURA.md` §10 | El README usa `04_CODIGO/test_indice_curso.py` y prohíbe `04_CODIGO/datito_migracion_inicio.py`. |
| Certamen 3 como parte del curso numerado | `07_DATITO/04_EJERCICIOS/certamen_3.html` existe. `clases.yaml` numera certamen 1 (`n: 20`), certamen 2 (`n: 21`) y triaje (`n: 22`). No hay `n:` para el certamen 3. | `README.md` cuenta 3 certámenes; `clases.yaml` no le da número de clase. | El HTML no es una clase del yaml. |
| Cinco skills | Seis directorios en `.claude/skills/`, incluido `datito-loop`. | `ARQUITECTURA.md` §2 y §10 | La sexta skill no está en el mapa. |
| Agentes solo en `.claude/skills/` | `.cursor/agents/puente-hito.md` y `.cursor/rules/maci-coherencia-hitos.mdc` | `ARQUITECTURA.md` y `CLAUDE.md` no los nombran | El relato del Hito 1 vive en Cursor, no en la arquitectura de Datito. |

Se retiran de la versión anterior: «`.mcp.json` no existe», «Certamen 1 omitido por el README» (el README actual nombra los tres certámenes), «`construir_navegacion.py` no es desfase» y «CLAUDE.md no menciona `dudas.yaml`» (lo nombra en las líneas 57 y 85).

---

## Tabla 3: Agentes

Las rutas de escritura de Datito son bajo `07_DATITO/`, no bajo el `00_INICIO/` de la raíz.

| Skill o regla | Escribe en | Prohibido | Documento que lo omite | Documento que lo declara |
|--------------|-----------|----------|----------------------|--------------------------|
| `datito` | `07_DATITO/00_INICIO/progreso.yaml`, `errores_conceptuales.yaml`, `dudas.yaml`, `07_DATITO/07_BITACORA/` | Simular la respuesta del alumno. Editar `curriculum.yaml` en sesión. Poner reglas en `datito.config.yaml`. | Ninguno de los documentos de Datito | `.claude/skills/datito/SKILL.md`, `00_INICIO/spec.md`, `00_INICIO/CLAUDE.md`, `ARQUITECTURA.md` §2 |
| `datito-progreso` | Nada | Modificar estado | Ninguno | `.claude/skills/datito-progreso/SKILL.md`, `ARQUITECTURA.md` §2 |
| `datito-visual` | `07_DATITO/01_CONCEPTOS/visual/*.html` | CDN, colores ajenos al template, otra piel que `_TEMPLATE_CANONICO.html` | Ninguno | `.claude/skills/datito-visual/SKILL.md`, `ARQUITECTURA.md` §2 |
| `datito-corregir` | `progreso.yaml`, `errores_conceptuales.yaml` | Enseñar. Pausar a esperar al alumno | Ninguno | `.claude/skills/datito-corregir/SKILL.md`, `ARQUITECTURA.md` §2 |
| `datito-pedagogia` | Nada | Enseñar. Auditar el contenido técnico de ciencia de datos como si fuera su oficio | Ninguno | `.claude/skills/datito-pedagogia/SKILL.md`, `ARQUITECTURA.md` §2 |
| `datito-loop` | `07_DATITO/07_BITACORA/learning_loop/agent_lessons.yaml` | Esperar respuesta del alumno. Gamificar con localStorage. Declarar que Datito aprende solo sin fila nueva en `results.tsv`. | `ARQUITECTURA.md` §2 y §10 | `.claude/skills/datito-loop/SKILL.md` («Qué no eres»), `00_INICIO/CLAUDE.md` |
| `puente-hito` | No escribe archivos. Corrige el relato. | Llamar Hito 2 al Trabajo 2. Reentrenar Dummy→RF como acto principal. Medir H_secundaria. Decir «precios estables» por +1,11 %. | `ARQUITECTURA.md`, `CLAUDE.md` | `.cursor/agents/puente-hito.md` |
| `maci-coherencia-hitos` | No escribe. Obliga cifras y léxico. | Contradecir RF R² test 0.6908 y MAE $218,847. Inventar que H_secundaria está medida. | `ARQUITECTURA.md`, `CLAUDE.md` | `.cursor/rules/maci-coherencia-hitos.mdc` |

---

## Tabla 4: Tablero GitHub

Comandos, 2026-09-27, solo lectura:

```
gh project list --owner cherrera0001 --limit 20
gh issue list --repo cherrera0001/MACI --state open --limit 50
```

Salida del primero:

```
3  Project MACI   open  PVT_kwHOASvtSs4Bkwxr
2  Project c4a-crm open  PVT_kwHOASvtSs4BkwxU
1  Python Prueba2 open  PVT_kwHOASvtSs4AOfb6
```

El segundo no imprimió filas. Issues abiertos en `cherrera0001/MACI`: 0. `gh project list` no devuelve los campos del tablero; esta tabla no los inventa.

| Número | Título | Campos | Estado | Sistemas cubiertos por un issue abierto | Sistemas sin issue abierto |
|--------|--------|--------|--------|------------------------------------------|----------------------------|
| 3 | Project MACI | No vienen en `gh project list` | open | Ninguno | Datito, curso estático, Melbourne, Galaxy Zoo, Vercel |
| 2 | Project c4a-crm | No consultados | open | No es el tablero de este repo | — |
| 1 | Python Prueba2 | No consultados | open | No es el tablero de este repo | — |

La versión anterior decía a la vez «0 issues» y «Datito cubierto por issues». Con 0 issues abiertos, ningún sistema está cubierto.

---

## Cierre

Desfases que un archivo abierto sostiene, y que pueden volverse historias:

1. El enlace `../spec.md` de la arquitectura no resuelve.
2. El mapa §10 no coincide con `07_DATITO/00_INICIO/` ni con `01_CONCEPTOS/visual/`.
3. `CLAUDE.md` cita `.mcp.json` sin la carpeta `00_INICIO/`.
4. La clase 18 apunta a un nombre de archivo que no es el del disco.
5. La clase 19 no tiene visual, y su criterio de dominio usa el R² y el MAE de HistGradientBoosting, no los del Random Forest aceptado.
6. Hay dos `verificar_visuales.py` y la arquitectura solo documenta `03_SCRIPTS/`.
7. El certamen 3 no tiene número en `clases.yaml`.
8. `datito-loop`, `puente-hito` y la regla de coherencia de hitos no están en la arquitectura.

No queda como desfase crítico la ausencia de `.mcp.json`.
