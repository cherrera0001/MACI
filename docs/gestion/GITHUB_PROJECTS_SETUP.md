# GitHub Projects Setup · MACI · Gestión

**Fecha:** 2026-09-27  
**Estado:** PLANTILLA LISTA PARA CREAR

---

## Pasos Manuales

1. **Crear Proyecto en GitHub**
   - URL: https://github.com/cherrera0001/MACI/projects/new
   - Nombre: `MACI · Gestión`
   - Descripción: "Gestión del proyecto MACI usando GitHub Projects (Épicas, Historias, Tareas)"
   - Template: Table (o Board)

2. **Configurar Campos Personalizados**
   - Status: "Backlog" | "En Progreso" | "En Revisión" | "Hecho" | "Bloqueado"
   - Prioridad: "P0 Crítica" | "P1 Alta" | "P2 Media" | "P3 Baja"
   - Área: "Manifiesto" | "Arquitectura" | "Visuales" | "CI" | "Compliance" | "Gestión"
   - Tipo: "Epic" | "Historia" | "Tarea" | "Bug"

3. **Agregar Issues desde Backlog**
   - Fuente: `docs/gestion/backlog.yaml` (7 épicas, 49 historias, 120+ tareas)
   - Formato: `[E-N] <nombre>` para épicas, `[H-N.M] <titulo>` para historias, `[T-N.M.P] <titulo>` para tareas
   - Crear vía GUI o script (futuro)

---

## Contenido del Backlog

| Épica | Nombre | Historias | Tareas |
|-------|--------|-----------|--------|
| E-1 | Fuente única de verdad | 4 | ~15 |
| E-2 | Arquitectura y orden | 5 | ~20 |
| E-3 | Curso confiable | 3 | ~12 |
| E-4 | CI automatizado | 3 | ~10 |
| E-5 | Higiene/compliance | 2 | ~8 |
| E-6 | Gestión GitHub Projects | 3 | ~10 |
| E-7 | Curso de gestión | 1 | ~45 |
| **Total** | | **49+** | **120+** |

---

## Plantillas de Tickets

### Epic
```
[E-N] Establecer una fuente única de verdad del curso

Resultado: El manifiesto es uno solo, todas las rutas existen, índice y web usan la misma fuente
Métricas:
- 0 archivos duplicados
- 0 rutas rotas
- 100% de clases → visuales existentes

Riesgos: [lista]
```

### Historia
```
[H-N.M] Como mantenedor, quiero un solo manifiesto de clases

Criterios de aceptación (INVEST):
- Dado el repo, cuando busco clases.yaml, entonces existe exactamente uno
- Dado el manifiesto, cuando corro test_manifiesto.py, entonces todas las rutas existen
- Dado el repo, cuando corro CI, entonces index.html se regenera desde el manifiesto
```

### Tarea
```
[T-N.M.P] Comparar 4 pares de YAML duplicados

Descripción: diff clases.yaml, curriculum.yaml, grafo.yaml, dudas.yaml entre raíz y 00_INICIO

Bloqueado por: (si aplica)
Horas estimadas: 2
```

---

## Estado Sesión 2

**Completado (1 proyecto semana):**
- ✅ F0-F4 completas (auditoría, backlog, arquitectura, diseño, curso)
- ✅ F5 completado (PPTX + DOCX + TRAZABILIDAD)
- ✅ F3 hallazgos resueltos: H-01, H-02, H-05, H-06, H-07, H-08, H-11
- ✅ Test CI simplificado (sin automatización no pedida)

**Pendiente Sesión 3:**
- GitHub Project creación (manual, esta plantilla lista)
- F3 finales: H-14 (material terceros, decision actual: mantener), H-15 (verificado OK)
- Crear issues desde backlog.yaml (script o manual)

---

**Siguiente:** Usuario crea proyecto en GitHub → link aquí → script para importar issues
