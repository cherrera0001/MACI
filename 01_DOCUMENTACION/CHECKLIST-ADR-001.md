# Checklist de Prueba: ADR-001 Multi-Curso

**Fase 1: Estructura y Configuración**

- [ ] `courses/fcd-2026-2/` contiene archivos copiados correctamente:
  - [ ] `datito.config.yaml` (con `course_id: fcd-2026-2`)
  - [ ] `curriculum.yaml` (21 conceptos)
  - [ ] `clases.yaml` (22 clases en 6 unidades)
  - [ ] `grafo.yaml`
  - [ ] `patron_evaluacion.md`
  - [ ] Directorios: `visual/`, `referencia/`, `guias/`, `cuadernillos/`, `certamenes/`

- [ ] `learners/cristobal_herrera/` contiene archivos copiados correctamente:
  - [ ] `progreso.yaml` (21 conceptos en NO_ESTUDIADO)
  - [ ] `errores_conceptuales.yaml` (vacío)
  - [ ] `estado.md` (auto-generado)
  - [ ] `dudas.yaml` (vacío)
  - [ ] Directorios: `bitacora/`, `entregas/`, `transferencia/`

- [ ] `07_DATITO/datito.config.yaml` actualizado con:
  - [ ] `course_id: fcd-2026-2`
  - [ ] `learner_id: cristobal_herrera`

- [ ] `courses/_template/` existe con estructura válida:
  - [ ] `README.md` (guía de 10 minutos)
  - [ ] `datito.config.yaml` (plantilla)
  - [ ] `curriculum.yaml` (estructura con 0 conceptos)
  - [ ] `clases.yaml` (estructura con 0 clases)
  - [ ] `progreso.yaml`, `errores_conceptuales.yaml`, `estado.md`, `dudas.yaml`
  - [ ] Directorios: `visual/`, `bitacora/`, `referencia/`

**Fase 2: Scripts**

- [ ] `datito_init_learner.py` existe y es ejecutable:
  ```bash
  python 03_CODIGO/datito_init_learner.py --course fcd-2026-2 --learner test_alumno
  ```
  - [ ] Crea `learners/test_alumno_fcd-2026-2/` sin errores
  - [ ] Genera `progreso.yaml` con 21 conceptos en `NO_ESTUDIADO`
  - [ ] Genera `estado.md` con resumen vacío
  - [ ] Copia `datito.config.yaml` correctamente

- [ ] `datito_estado.py` regenera sin errores:
  ```bash
  python 03_CODIGO/datito_estado.py
  ```
  - [ ] Lee `07_DATITO/datito.config.yaml`
  - [ ] Resuelve rutas: `courses/fcd-2026-2/`, `learners/cristobal_herrera/`
  - [ ] Genera `learners/cristobal_herrera/estado.md`
  - [ ] Output contiene línea correcta: `NO_ESTUDIADO 21`

- [ ] `construir_navegacion.py` inyecta sin errores:
  ```bash
  python 03_CODIGO/construir_navegacion.py
  ```
  - [ ] Lee `07_DATITO/datito.config.yaml`
  - [ ] Resuelve rutas a `courses/fcd-2026-2/visual/`
  - [ ] No hay error de "file not found"
  - [ ] Genera `courses/fcd-2026-2/visual/index.html`

**Fase 3: Datito en Conversación**

- [ ] `/datito-progreso` funciona:
  - [ ] Lee config correctamente
  - [ ] Muestra: "NO_ESTUDIADO 21"
  - [ ] Ninguna sesión iniciada aún

- [ ] `/datito` inicia sesión:
  - [ ] Carga `estado.md` de `learners/cristobal_herrera/`
  - [ ] Lee `curriculum.yaml` del curso
  - [ ] Sugiere primer concepto recomendado
  - [ ] Hace una pregunta y **espera de verdad** (no simula respuesta)

**Fase 4: Verificación de Contrato**

- [ ] `verificar_contrato.py` pasa 12 tests:
  ```bash
  python 03_CODIGO/verificar_contrato.py
  ```
  - [ ] Output: `12 ok · 0 fallos`
  - [ ] No hay cambios en las garantías G1–G14

**Fase 5: Ejemplo Ficticio (Multi-Curso)**

- [ ] Crear learner ficticio para "Estadística 2026-2":
  ```bash
  python 03_CODIGO/datito_init_learner.py --course estadistica-2026-2 --learner maria_garcia
  ```
  - [ ] Falla de forma esperada: `curso 'estadistica-2026-2' no existe`
  - [ ] Mensaje sugiere: `cp -r courses/_template courses/estadistica-2026-2`

- [ ] Clonar la plantilla y crear el curso:
  ```bash
  cp -r courses/_template courses/estadistica-2026-2
  python 03_CODIGO/datito_init_learner.py --course estadistica-2026-2 --learner maria_garcia
  ```
  - [ ] Crea `learners/maria_garcia_estadistica-2026-2/`
  - [ ] Sin errores

- [ ] Verificar que el learner original no cambió:
  - [ ] `learners/cristobal_herrera/progreso.yaml` sigue intacto
  - [ ] `learners/cristobal_herrera/estado.md` sigue siendo de Fundamentos de Ciencia de Datos

**Fase 6: Documentación**

- [ ] [`01_DOCUMENTACION/ADR-001-multi-course.md`](../01_DOCUMENTACION/ADR-001-multi-course.md) es claro:
  - [ ] Problema está bien definido
  - [ ] Decisión está justificada
  - [ ] Tradeoffs están listados
  - [ ] Cómo reutilizar en 10 minutos es claro

- [ ] [`07_DATITO/00_LEEME.md`](../07_DATITO/00_LEEME.md) actualizado:
  - [ ] Sección "Para reutilizarlo en otro curso" está completa
  - [ ] Quickstart tiene comandos claros
  - [ ] Links a ADR y plantilla están correctos

- [ ] [`courses/_template/README.md`](../courses/_template/README.md) es útil:
  - [ ] Estructura de archivos clara
  - [ ] Checklist antes de activar
  - [ ] FAQ y troubleshooting

**Fase 7: Git**

- [ ] Status:
  ```bash
  git status
  ```
  - [ ] Modificados: `07_DATITO/datito.config.yaml`, `07_DATITO/00_LEEME.md`
  - [ ] Nuevos: `01_DOCUMENTACION/ADR-001-multi-course.md`, `03_CODIGO/datito_init_learner.py`
  - [ ] Nuevos: `courses/` (fcd-2026-2, _template), `learners/cristobal_herrera/`

- [ ] No hay archivos sensibles en staging:
  - [ ] Ningún `.env`, credenciales, binarios

- [ ] Commit message es claro:
  ```
  Refactor: Datito ahora es multi-curso (ADR-001)

  Separa motor (skills, scripts) de paquete de curso (curriculum, clases, visual)
  y perfil de alumno (progreso, estado, dudas).

  Nuevos:
  - ADR-001 de arquitectura multi-curso con backward compatibility
  - courses/{_template,fcd-2026-2}/ con estructura de curso
  - learners/cristobal_herrera/ con historial del alumno
  - datito_init_learner.py para crear alumnos nuevos

  Modificados:
  - datito_estado.py, construir_navegacion.py: leen config, resuelven rutas
  - 00_LEEME.md: quickstart de reutilización
  ```

---

## Si algo falla

**Error:** `"Curso 'fcd-2026-2' no existe"`
- Verificar: `courses/fcd-2026-2/` existe
- Verificar: `datito.config.yaml` está en la raíz de `07_DATITO/`

**Error:** `"archivo no encontrado: courses/fcd-2026-2/curriculum.yaml"`
- Verificar: el archivo fue copiado correctamente (no usar `mv`, usar `cp`)

**Error:** `datito_estado.py` genera estado.md en lugar equivocado
- Verificar: `learner_id` está correctamente configurado en `07_DATITO/datito.config.yaml`
- Verificar: `learners/cristobal_herrera/` existe

**Test de contrato falla:**
- Ejecutar: `python 03_CODIGO/verificar_visuales.py` (ve si los HTML están bien)
- Verificar: `grafo.yaml` está actualizado
- Verificar: `curriculum.yaml` tiene 21 conceptos

---

## Cómo afirmar "está listo"

Cuando las 7 fases estén completas (todos los ✅), escribir:

> ✨ **ADR-001 implementada:** Motor separado, multi-curso, backward compatible.
> 
> - Fase 1 (Estructura): ✅ 
> - Fase 2 (Scripts): ✅ 
> - Fase 3 (Datito): ✅ 
> - Fase 4 (Contrato): ✅
> - Fase 5 (Ejemplo): ✅
> - Fase 6 (Docs): ✅
> - Fase 7 (Git): ✅

Y mergear.
