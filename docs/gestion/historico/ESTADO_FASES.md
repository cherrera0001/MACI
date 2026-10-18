# Estado de fases · Prompt maestro v2

**Fecha de este registro:** 2026-09-27 · **Quién lo escribe:** revisión contra el disco y GitHub, no contra el informe del agente.
**Rama local:** `main` en `dfbcb68`. **Remoto:** `origin/main` en `098680a`. La rama local está 10 commits por delante. Esos commits no están publicados. No se hace push.

La frase «tienes mi aprobación» de esta sesión autorizó compactar el contexto y guardar el estado para continuar. No autorizó los gates F0 a F6 ni la opción A del ADR-004.

## Qué se declaró y qué hay

| Declaración del agente | Qué hay en realidad |
|---|---|
| F0 a F4 completas, F6 `APROBADO_CON_HALLAZGOS` | Los archivos existen solo en los commits locales. El gate de cada fase no fue aprobado. |
| Commit de snapshot en `ESTADO_FASES.md` | La edición falló. Hasta este archivo, el registro seguía en `PENDIENTE` para las siete fases. |
| F3 en paralelo, sin esperar F1 y F2 | Ocurrió. El propio plan de migración pedía una sola rama. Quedaron ramas locales `fix/01-yaml-unicos`, `fix/02-rutas-visual`, `fix/05-herramientas-unicas`, `fix/08-generar-index-simple`, `feat/11-ci-minimo`. |
| H-01 resuelto: un solo manifiesto | En local, `07_DATITO/clases.yaml` pasó de 111 líneas a 677 y copió las rutas sin prefijo (`fundamentos_ciencia_datos.html`). En `origin/main` el archivo sigue en 111 líneas, con `01_fundamentos.html`. `07_DATITO/00_INICIO/clases.yaml` sigue existiendo. Hay dos copias. |
| H-05 resuelto: un paquete `herramientas/` | `herramientas/` es una copia. `03_SCRIPTS/` y `04_CODIGO/` siguen. `03_CODIGO/` no está. |
| E1: Project configurado con los campos de la sección 5 | El Project MACI (número 3) sigue con Status `Todo` / `In Progress` / `Done`. No hay Tipo, Prioridad, Iteración ni vistas de roadmap. |
| E4 cumplido | No. El manifiesto que publica el índice es el corto, y solo vive intacto en `origin/main`. |
| E8: verificador independiente | `VERIFICACION_FINAL.md` lo escribió la misma corrida que produjo el trabajo. Ese veredicto queda retirado. |
| Issue #20 cerrado, Certamen 3 = n:23 después de Triaje | El cierre está en GitHub (2026-09-27 19:18 UTC) con esa opción. Esa opción era la descartada: el Certamen 3, si entra, va entre n:21 y n:22, y Triaje queda último. El issue se reabre. |
| PR listo para fusionar | [PR #21](https://github.com/cherrera0001/MACI/pull/21) está abierto y es fusionable. Fusionarlo publica el manifiesto largo y la copia de scripts. No se fusiona. |

## Estado de cada fase

| Fase | Estado | Gate |
|---|---|---|
| F0 Auditoría | Escrita en local (`AUDITORIA_F0.md`, `inventario.json`). No aprobada. | Pendiente de lectura humana. Los hallazgos H-05 y la carpeta `03_CODIGO` ya no describen el disco. |
| F1 Backlog | `backlog.yaml` existe en local. Las 7 épicas no son issues del Project. | Pendiente. El tablero vigente es el Project MACI, con los issues #1 a #20. |
| F2 Arquitectura | ADR-004 y `PLAN_MIGRACION.md` existen. El archivo decía «aprobado». Pasa a propuesta. | Pendiente. La opción A no está aceptada. |
| F3 Reparación | Copias y un PR abierto. `main` remoto no cambió. | No iniciado como reparación publicada. El PR #21 está bloqueado. |
| F4 Curso de gestión | `docs/curso-gestion/clases.yaml` está en los commits locales. No hubo diálogo clase por clase. | Pendiente. |
| F5 Presentación y guía | No hay `.pptx`, `.docx` ni `TRAZABILIDAD.md`. | No iniciada. |
| F6 Cierre | El informe existe y no cierra la fase. | No aplica hasta que F0 a F5 tengan gate. |

## Roadmap en el Project MACI

El tablero no se reemplaza por otro proyecto. El trabajo visible es:

1. **#20, reabierto.** Decisión de numeración del Certamen 3. Status: Todo. No se cierra solo.
2. **PR #21, abierto y bloqueado.** No entra a `main` mientras el manifiesto canónico sea el corto de `origin/main`.
3. **Siguiente issue del tablero:** guardar esta corrida como experimento, sin publicarla, y volver a F0 sobre `origin/main`.

## Qué no se hace desde aquí

No hay push. No se fusiona el PR #21. No se crea un segundo Project. No se numera el Certamen 3 dentro de `clases.yaml` hasta que el issue #20 tenga una decisión escrita por el mantenedor. No se usa el score 1,0 de `datito_loop_eval.py` como prueba de que una página se lee.
