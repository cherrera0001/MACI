# ADR-004: Estructura Destino del Repositorio

**Estado:** RECHAZADA (no ejecutada) · **Fecha:** 2026-09-27 · **Resuelta:** 2026-10-27 · **Arquitecto:** A3
**Gate:** cerrado. La opción A (reorganización total con `curso/manifiesto.yaml`,
`herramientas/`, `tests/`) nunca se ejecutó. El repositorio siguió el camino de
la opción B (limpieza in-place): estructura numerada `00_`–`10_ARCHIVO` vigente
más módulos modernos sin numerar (`docs/`, `specs/`, `15_TERMINITO/`, `13_KAGGLE/`,
`14_INVESTIGACION/`, `.github/`). Lo que `00_INICIO/CLAUDE.md` documenta como
"excepciones ADR-004" es esa práctica real, no esta propuesta.

---

## Contexto

El repositorio MACI ha acumulado 18 hallazgos críticos (H-01 a H-18, auditoría F0):
- Cuatro archivos YAML duplicados en rutas distintas (`clases.yaml`, `curriculum.yaml`, `grafo.yaml`, `dudas.yaml`)
- Dos carpetas de código con funciones solapadas (`03_SCRIPTS/` con 42 archivos vs `03_CODIGO/` con 14)
- Plantilla canónica espejada en dos directorios (`07_DATITO/visual/` vs `07_DATITO/01_CONCEPTOS/visual/`)
- Dos archivos `index.html` sin propósito claro
- Dos conjuntos de skills (`.claude/skills/` y `.agents/skills/`)
- Dos configuraciones de IDE (`.codex/` y `.cursor/`)
- Material de terceros público (transcripciones UdeC, 529 MB totales)
- Gestión en archivos (`TECH_DEBT.md`, `results.tsv`, `agent_lessons.yaml`) en lugar de issues

**Problema:** El repositorio no tiene una fuente única de verdad. La duplicación obstaculiza CI, la migración a GitHub Projects y la reparabilidad.

---

## Opciones Evaluadas

### Opción A: Reorganización Estructural (ELEGIDA)

```
MACI/
├── README.md                 ← qué es, cómo se usa, estado generado
├── docs/                     ← spec, ADR, gestión, curso de gestión
│   ├── spec.md
│   ├── adr/                  (ADR-001 a ADR-007)
│   ├── gestion/              (gestión con GitHub Projects)
│   └── curso-gestion/        (14 clases de enseñanza)
├── curso/                    ← ÚNICA fuente de contenido publicado
│   ├── manifiesto.yaml       (FUSIÓN de clases.yaml, curriculum.yaml, grafo.yaml)
│   ├── clases/               (NN_slug.html, numeración fija)
│   ├── ejercicios/
│   ├── certamenes/
│   └── _TEMPLATE_CANONICO.html
├── datito/                   ← tutor: estado, bitácora, lecciones
│   ├── skills/               (ÚNICA copia)
│   ├── estado.yaml
│   └── bitacora/
├── herramientas/             ← UN solo paquete Python (fusión de 03_SCRIPTS + 03_CODIGO)
│   ├── scripts/
│   ├── validators/
│   └── setup.py
├── tests/
├── datos/                    ← solo datos públicos
├── .github/                  (plantillas, CI/CD)
└── .gitignore, .vercelignore, etc.
```

**Ventajas:**
- ✅ Una fuente única de verdad por dato (manifiesto, código, documentación)
- ✅ Clara separación de responsabilidades (publishable vs internal vs tools)
- ✅ Fácil CI: un solo `manifiesto.yaml` → regenera índice y estado
- ✅ Facilita GitHub Projects: issues apuntan a `curso/` no a copias
- ✅ Preparado para escala: si hay más cursos, estructura lo permite

**Desventajas:**
- ❌ Migración grande: ~150 `git mv` operaciones
- ❌ Cambios en rutas rompen URLs de versión anterior (se mitigan con redirects en Vercel)
- ❌ Histórico de git se ve alterado por los renames (pero la historia se preserva)

### Opción B: Limpieza In-Place

Solo eliminar duplicados, renombrar directorios mínimamente.

**Ventajas:**
- ✅ Cambios pequeños, riesgo bajo
- ✅ URLs no cambian

**Desventajas:**
- ❌ Sigue siendo confuso (¿cuál es la fuente? ¿07_DATITO o 07_DATITO/00_INICIO?)
- ❌ No escala: si crece a 2-3 cursos, vuelve a enmaraña
- ❌ CI sigue siendo frágil: los scripts siguen apuntando a múltiples rutas

---

## Decisión propuesta (no tomada)

El agente recomendó la opción A. Esa recomendación no es una decisión del mantenedor.

**Justificación:**
1. El repositorio es un laboratorio de GitHub Projects. La Opción B deja irresueltos los hallazgos H-01, H-05, H-06, H-07, H-15 que son críticos para E-1 y E-2.
2. La migración es un costo de una sola vez; el beneficio es permanente (una fuente única, CI confiable, escalabilidad).
3. El plan de migración (ADR-004-PLAN_MIGRACION.md) preserva la historia completa con `git mv`.
4. Las URLs de la web se redirigen en `vercel.json` y `.vercelignore`.

---

## Consecuencias

### Inmediatas (F3)
- 150+ operaciones `git mv` en un único PR grande
- Tests deben actualizarse para nuevas rutas
- `construir_navegacion.py` debe reaprender dónde buscar archivos
- CI debe regenerar todo (test_manifiesto.py, verificador de enlaces)

### A largo plazo
- **Única fuente:** toda herramienta lee de `curso/manifiesto.yaml`, no de múltiples YAML
- **Escalabilidad:** si MACI crece a 3 cursos, la estructura lo soporta (`curso/FCD/`, `curso/Melbourne/`, etc.)
- **Mantenibilidad:** nuevas contribuidoras entienden dónde poner qué
- **CI confiable:** un solo índice generado de un único manifiesto

---

## Mitigaciones de Riesgo

| Riesgo | Mitigación |
|--------|-----------|
| Ruptura de URLs | Redirects en `vercel.json` + `_redirects` en Vercel |
| Historia de git alterada por renames | `git mv` preserva autoría y fecha; no es `rm + add` |
| Tests fallan | Se actualizan ANTES del merge (sección 3.3 del plan) |
| Conflictos en PRs concurrentes | WIP = 1: F3 es una sola rama, sin paralelismo |

---

## Estado

**Resolución (2026-10-27):** cerrada como no ejecutada. La opción A exigía una
migración de ~150 `git mv` y la fusión de `03_SCRIPTS/` + `04_CODIGO/` en
`herramientas/`; ninguna de las dos cosas ocurrió, y el plan de migración al que
este ADR se amarraba (PR #21) no prosperó. Lo que hoy describe `00_INICIO/CLAUDE.md`
en "EXCEPCIONES (ADR-004)" es la práctica consolidada posterior: conservar la
estructura numerada y añadir módulos modernos sin numerar. Esta ADR se conserva
como registro histórico; para la estructura vigente manda el disco y
`00_INICIO/CLAUDE.md` §Convenciones.

---

**Referencias:**
- Auditoría: `docs/gestion/historico/AUDITORIA_F0.md` (hallazgos H-01 a H-18)
- Plan detallado: `docs/gestion/historico/PLAN_MIGRACION.md`
- Taxonomía: Prompt Maestro v2, sección 4
