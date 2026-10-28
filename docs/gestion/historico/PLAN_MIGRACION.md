# Plan de Migración · Estructura Destino (ADR-004)

**Versión:** 1.0 · **Fecha:** 2026-09-27 · **Métodos:** git mv (preserva historia) + redirecciones + tests

---

## Resumen Ejecutivo

**Objetivo:** Migrar de la estructura actual a la Opción A (ADR-004) sin perder historia, con tests en verde en cada paso.

**Riesgos mitigados:**
- ✅ Historia de git preservada: `git mv` no es `rm + add`
- ✅ URLs no se rompen: `vercel.json` redirige antiguas a nuevas
- ✅ Tests pasan: se actualizan ANTES del merge (WIP = 1)

**Duración estimada:** 8 a 12 horas (1 sprint)

---

## Tabla de Migración

| Antigua | Nueva | Método | Nota | PR |
|---------|-------|--------|------|-----|
| `07_DATITO/clases.yaml` | `curso/manifiesto.yaml` (FUSIÓN: clases + curriculum + grafo) | FUSIONAR + elegir canónico | Historia preservada; curriculum.yaml y grafo.yaml se absorben como sub-secciones | #E-1.3 |
| `07_DATITO/00_INICIO/clases.yaml` | (eliminar) | git rm | Era duplicado; su contenido va a `curso/manifiesto.yaml` | #E-1.3 |
| `07_DATITO/00_INICIO/curriculum.yaml` | (eliminar) | git rm | Idem | #E-1.3 |
| `07_DATITO/00_INICIO/grafo.yaml` | (eliminar) | git rm | Idem | #E-1.3 |
| `07_DATITO/01_CONCEPTOS/visual/` | `curso/clases/` | git mv | Renombrar directorio; archivos mantienen su nombre `NN_slug.html` | #E-2.2 |
| `07_DATITO/visual/` | (eliminar) | git rm -r | Era plantilla espejada; la única copia es `curso/_TEMPLATE_CANONICO.html` | #E-2.1 |
| `07_DATITO/visual/_TEMPLATE_CANONICO.html` | `curso/_TEMPLATE_CANONICO.html` | git mv | Una sola copia canónica | #E-2.1 |
| `07_DATITO/04_EJERCICIOS/` | `curso/ejercicios/` | git mv | Certamenes + ejercicios juntos | #E-2.2 |
| `03_SCRIPTS/*` | `herramientas/scripts/` | git mv | 42 archivos; detectar y eliminar duplicados de `03_CODIGO/` | #E-2.3 |
| `03_CODIGO/*` | (fusionar a `herramientas/`) | git rm (tras fusión) | 14 archivos; mantener solo únicos | #E-2.3 |
| `.claude/skills/` | `datito/skills/` | git mv | Una sola copia; `.agents/skills/` se elimina | #E-2.4 |
| `.agents/skills/` | (eliminar) | git rm -r | Era duplicado | #E-2.4 |
| `.claude/agents/` | `datito/agentes/` | git mv | Idem | #E-2.5 |
| `.agents/` (raíz) | (eliminar) | git rm -r | Directorio completo obsoleto | #E-2.5 |
| `.codex/`, `.cursor/` | (eliminar) | git rm -r | Configuraciones IDE obsoletas | #E-2.6 |
| `07_DATITO/dudas.yaml` | `curso/dudas.yaml` | git mv | Métadata del tutor; va a `curso/` | #E-2.7 |
| `07_DATITO/00_INICIO/dudas.yaml` | (eliminar) | git rm | Duplicado | #E-2.7 |
| `05_CLASES/` | `datito/bitacora/clases/` | git mv | Transcripciones y materiales | #E-2.7 |
| `10_ARCHIVO/` | (REVISAR: conservar vs eliminar) | DECISIÓN RESERVADA | Material de terceros; ver H-13, H-14 | — |
| Índices generados | CI regenera desde `curso/manifiesto.yaml` | Workflow | `construir_navegacion.py` sale de `03_SCRIPTS/` | #E-4.1 |

---

## Orden de Ejecución (Fases de F3)

### Fase 1: Tests + Setup CI (Épica E-4 primero)
**PR #1: E-4.1 · Escribir tests de manifiesto y CI**
- Crear `tests/test_manifiesto.py`: valida que `curso/manifiesto.yaml` existe y todas sus rutas existen
- Crear `.github/workflows/ci.yml`: corre tests + verificador de enlaces + gates visuales
- Crear `tests/test_duplicados.py`: busca archivos con el mismo nombre en directorios distintos
- Status: CI ROJO (tests fallan porque aún no existe `curso/manifiesto.yaml`)

### Fase 2: Fusión de Manifiestos (Épica E-1)
**PR #2: E-1.3 · Fusionar clases.yaml, curriculum.yaml, grafo.yaml en manifiesto canónico**
- Leer `07_DATITO/clases.yaml` (702 líneas) como base
- Absorber `curriculum.yaml`: campos `conceptos` van a una sección aparte
- Absorber `grafo.yaml`: estructura de dependencias entera
- Crear `curso/manifiesto.yaml` (nueva ruta, contenido fusionado)
- Eliminar `07_DATITO/00_INICIO/clases.yaml`, `curriculum.yaml`, `grafo.yaml` con `git rm`
- Status: CI VERDE (`test_manifiesto.py` pasa)

### Fase 3: Mover y reorganizar (Épica E-2)
**PR #3: E-2.1 · Mover y unificar plantillas + visuales**
- `git mv 07_DATITO/visual/_TEMPLATE_CANONICO.html curso/_TEMPLATE_CANONICO.html`
- `git rm -r 07_DATITO/visual/` (la otra copia de la plantilla)
- Status: Tests pasan; verificador de enlaces busca en `curso/`, no en `07_DATITO/`

**PR #4: E-2.2 · Mover contenido: clases, ejercicios, certamenes**
- `git mv 07_DATITO/01_CONCEPTOS/visual/ curso/clases/`
- `git mv 07_DATITO/04_EJERCICIOS/ curso/ejercicios/`
- Actualizar referencias en `manifiesto.yaml` (rutas de `NN_slug.html`)
- Status: Verificador de enlaces aún pasa (rutas actualizadas)

**PR #5: E-2.3 · Fusionar herramientas: eliminar duplicados en 03_SCRIPTS vs 03_CODIGO**
- Comparar ambas carpetas; identificar archivos duplicados
- Mantener la versión más reciente (por fecha de commit)
- Eliminar la otra
- `git mv 03_SCRIPTS/* herramientas/scripts/`
- `git rm -r 03_CODIGO/`
- Status: `construir_navegacion.py` está en `herramientas/scripts/`

**PR #6: E-2.4 · Unificar skills**
- `git mv .claude/skills/ datito/skills/`
- `git rm -r .agents/skills/`
- Actualizar referencias en scripts
- Status: Tests pasan

**PR #7: E-2.5 · Limpiar configuraciones IDE**
- `git rm -r .codex/ .agents/ .cursor/`
- Mantener solo `.claude/` (la configuración activa)
- Status: Tests pasan

**PR #8: E-2.6 · Mover bitácora y transcripciones**
- `git mv 05_CLASES/ datito/bitacora/clases/`
- `git mv 07_DATITO/dudas.yaml curso/dudas.yaml`
- `git rm 07_DATITO/00_INICIO/dudas.yaml`
- Status: Todos los tests pasan

### Fase 4: Limpiar raíz y CI final
**PR #9: E-1.4 · Actualizar CI para regenerar índices desde manifiesto**
- Modificar `.github/workflows/ci.yml`: cuando `curso/manifiesto.yaml` cambia, regenera `curso/index.html`
- Quitar scripts manuales de `03_SCRIPTS/` (ya no existen)
- Status: CI regenera estado automáticamente

**PR #10: E-4.2 · Validación final: tests 100 % verde + web en Vercel**
- Correr todos los tests localmente
- Verificar enlaces en `vercel.json` y `_redirects`
- Captura de la web en Vercel mostrando que `curso/` está publicado
- Status: 100 % verde, cierre de F3

---

## Mitigaciones Tecnológicas

### 1. Preservar historia con git mv
```bash
git mv 07_DATITO/01_CONCEPTOS/visual/ curso/clases/
# No:
# rm -r 07_DATITO/01_CONCEPTOS/visual/
# mkdir -p curso/clases && mv ... 
# ↑ Esto rompe la historia de git
```

### 2. Redirects en Vercel
**`vercel.json`:**
```json
{
  "redirects": [
    { "source": "/07_DATITO/01_CONCEPTOS/visual/(.*)", "destination": "/curso/clases/$1" },
    { "source": "/07_DATITO/04_EJERCICIOS/(.*)", "destination": "/curso/ejercicios/$1" }
  ]
}
```

### 3. Tests actualizados ANTES de merge
Cada PR trae consigo las actualizaciones de paths en:
- `test_manifiesto.py`: nuevas rutas
- `construir_navegacion.py`: nuevas carpetas de búsqueda
- `.github/workflows/ci.yml`: nuevos gates

### 4. WIP = 1: Una sola rama
Toda la migración ocurre en la rama `feature/ADR-004-migracion-estructura`. No hay paralelismo; al cierre, merge a `main` de golpe.

---

## Criteria de Aceptación por PR

Cada PR debe cumplir:
1. ✅ `git mv` usado (no `rm + add`)
2. ✅ Tests locales pasan (nada en ROJO)
3. ✅ `git log --name-status` muestra `renamed` no `deleted + added`
4. ✅ Criterios de aceptación del issue cerrados
5. ✅ Revisión de A7 aprobada (`APROBADO` en el PR)

---

## Rollback Plan

Si algo falla en mitad de la migración:
1. No mergear el PR; quedó en rama `feature/ADR-004-migracion-estructura`
2. `git reset --hard main` en local
3. Diagnosticar qué fue mal en la rama
4. Reabrir el PR con correcciones

**No se hace force-push a main.** Solo se mergea cuando 100 % verde.

---

## Entregables

**Al cierre de F3:**
- ✅ Nueva estructura en `main`
- ✅ Todos los tests en verde
- ✅ Web en Vercel publicada con `curso/` accesible
- ✅ Redirects funcionando (URLs antiguas redirigen)
- ✅ CI regenera índice automáticamente

**Métricas de éxito:**
- 0 rutas rotas (verificador de enlaces)
- 0 tests fallando
- 0 hallazgos H-01, H-05, H-06, H-07, H-15 pendientes
- Epic E-1 cerrada (fuente única)
- Epic E-2 cerrada (arquitectura limpia)

