# Inventario de datos personales y decisión de tratamiento

**Fecha:** 2026-10-27 · **Alcance:** REQ-EST-006 (specs/002-evolucion-app-tutor)
**Regla de este documento:** solo categorías y rutas. Nunca se copian los
valores (emails, citas) aquí.

## Inventario (categoría → dónde vive)

| # | Categoría | Ubicación | Sensibilidad |
|---|---|---|---|
| 1 | ~~Email del alumno~~ **RESUELTO** (valor vaciado, 2636e66) | `07_DATITO/datito.config.yaml` | alta → cerrada |
| 2 | Nombre del alumno | `07_DATITO/progreso.yaml` (meta), `07_DATITO/datito.config.yaml`, bitácoras y `dudas.yaml` (campo `respondio`), `07_DATITO/clases.yaml` (cierre de clase 16) | media |
| 3 | Citas textuales de desempeño | `07_DATITO/errores_conceptuales.yaml` (`dijo`), `07_DATITO/dudas.yaml` (`respondio`) | alta (evaluable, atribuible) |
| 4 | Estado de aprendizaje completo | `07_DATITO/progreso.yaml`, `dudas.yaml`, `07_BITACORA/` | alta (perfil pedagógico) |
| 5 | Capturas con datos académicos | `01_DOCUMENTACION/01_CERTAMEN2/fuentes/*.html` (reportado en EVALUACION.md B-S1) | media-alta |
| 6b | ~~Espejo `.agents/skills`~~ **RESUELTO** (fuera de git, 2636e66, D-4.4) | `.agents/` (ignorado, vive en disco) | — |
| 6 | Emails de terceros | `05_CLASES/10_GRABACIÓN_CLASES/80038_Procesos_Innovacion/NOTAS_INDICE.md`, `01_DOCUMENTACION/PRIMERA-ENTREGA-PLAN.md`, `06_LABORATORIOS/_markdown/2026_P5_Clasificación_res_ _1.md` (consentimiento por verificar) | alta (terceros) |
| 7 | ~~Copia archivada del estado~~ **ELIMINADA** (2026-10-27, REQ-EST-004) | — | — |

## Tamaño de lo versionado (T-6.1.1)

| Categoría | Ruta | Tamaño |
|---|---|---|
| email del alumno (config) | `07_DATITO/datito.config.yaml` | 5.4 KB |
| nombre + meta (progreso) | `07_DATITO/progreso.yaml` | 10.3 KB |
| citas de desempeno (errores) | `07_DATITO/errores_conceptuales.yaml` | 10.3 KB |
| citas + estado (dudas) | `07_DATITO/dudas.yaml` | 14.5 KB |
| bitacoras de sesion | `07_DATITO/07_BITACORA` | 4.5 MB en 132 archivos |
| capturas certamen 2 | `01_DOCUMENTACION/01_CERTAMEN2/fuentes` | 1.8 MB en 5 archivos |
| notas 80038 (email tercero) | `05_CLASES/10_GRABACIÓN_CLASES/80038_Procesos_Innovacion/NOTAS_INDICE.md` | 5.4 KB |
| PRIMERA-ENTREGA-PLAN | `01_DOCUMENTACION/PRIMERA-ENTREGA-PLAN.md` | 10.3 KB |
| P5 res (email tercero) | `06_LABORATORIOS/_markdown/2026_P5_Clasificación_res_ _1.md` | 42.5 KB |

## Decisión (registrada, ejecutable por fases)

1. **El repo ES público (corregido 2026-10-28, #72).** La publicación del
   *sitio* (maci.c4a.cl) va por `publicar_sitio.mjs`, que exige que
   `progreso.yaml`, `datito.config.yaml` y `README.md` no se sirvan. El repo
   público SÍ expone los YAML con citas del alumno (filas 2-4): es una
   decisión del dueño, documentada aquí. Mitigaciones ya aplicadas: email fuera
   de git (fila 1, hecho), `11_GOOGLE/` ignorado, espejo `.agents` fuera de
   git, duplicado archivado eliminado. Pendiente solo si el dueño lo decide:
   anonymization de citas + history rewrite (pesado; ver punto 3).
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
