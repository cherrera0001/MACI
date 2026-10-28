# Inventario de datos personales y decisión de tratamiento

**Fecha:** 2026-10-27 · **Alcance:** REQ-EST-006 (specs/002-evolucion-app-tutor)
**Regla de este documento:** solo categorías y rutas. Nunca se copian los
valores (emails, citas) aquí.

## Inventario (categoría → dónde vive)

| # | Categoría | Ubicación | Sensibilidad |
|---|---|---|---|
| 1 | Email del alumno | `07_DATITO/datito.config.yaml` (campo `alumno.email`) | alta (identificador directo) |
| 2 | Nombre del alumno | `07_DATITO/progreso.yaml` (meta), `07_DATITO/datito.config.yaml`, bitácoras y `dudas.yaml` (campo `respondio`), `07_DATITO/clases.yaml` (cierre de clase 16) | media |
| 3 | Citas textuales de desempeño | `07_DATITO/errores_conceptuales.yaml` (`dijo`), `07_DATITO/dudas.yaml` (`respondio`) | alta (evaluable, atribuible) |
| 4 | Estado de aprendizaje completo | `07_DATITO/progreso.yaml`, `dudas.yaml`, `07_BITACORA/` | alta (perfil pedagógico) |
| 5 | Capturas con datos académicos | `01_DOCUMENTACION/01_CERTAMEN2/fuentes/*.html` (reportado en EVALUACION.md B-S1) | media-alta |
| 6 | Emails de terceros | `05_CLASES/10_GRABACIÓN_CLASES/80038_Procesos_Innovacion/NOTAS_INDICE.md`, `01_DOCUMENTACION/PRIMERA-ENTREGA-PLAN.md`, `06_LABORATORIOS/_markdown/2026_P5_Clasificación_res_ _1.md` (consentimiento por verificar) | alta (terceros) |
| 7 | ~~Copia archivada del estado~~ | ~~`10_ARCHIVO/learners/`~~ **eliminada el 2026-10-27** (REQ-EST-004) | — |

## Decisión (registrada, ejecutable por fases)

1. **Repo privado permanente.** MACI sigue privado; la publicación del *sitio*
   (maci.c4a.cl) ya va por `publicar_sitio.mjs` con su propia verificación de
   datos privados (`verificar_todo.py --en-linea` exige que `progreso.yaml`,
   `datito.config.yaml` y `README.md` no se sirvan). La privacidad del repo y
   la del sitio son controles independientes y ambos quedan activos.
2. **Mover el email fuera de git (pendiente, fase tutor).** El email (fila 1)
   debe migrar a configuración local ignorada (`.env` / archivo gitignored) con
   fallback vacío; los scripts que lo usen lo leen de ahí. No se hace en esta
   fase porque toca `07_DATITO/` en caliente; queda como tarea explícita de la
   fase de tutor del spec 002.
3. **History rewrite: explícitamente descartado por ahora.** Reescribir el
   historial (filtro de emails/citas) rompería referencias de issues y el
   trabajo en curso; con el repo privado y la fila 2 resuelta, el riesgo
   residual es aceptable. Se reevalúa solo si el repo cambiara a público:
   en ese caso el gate previo es rewrite + revisión de las filas 5 y 6.
4. **Nada de esto se copia a artefactos de especificación.** Regla ya aplicada
   en specs/002 (verificado con grep: sin nombre ni emails en los artefactos).

## Verificación

- `python 03_SCRIPTS/verificar_contrato.py` (sección "Seguridad sin secretos")
  sigue en verde: ningún secreto ni captura sensible versionada bajo las reglas
  del `.gitignore`.
- La suite `04_CODIGO/test_esquema_estado.py` valida la integridad de los
  YAML que contienen las filas 2–4 (sin tocar su contenido).
