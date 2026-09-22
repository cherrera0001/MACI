# ADR-001: Arquitectura Multi-Curso para Datito

**Fecha:** 2026-09-22  
**Estado:** Propuesto  
**Decisión:** Refactorizar Datito de un sistema mono-alumno/mono-asignatura a un motor parametrizable que otros estudiantes puedan reutilizar en sus propios cursos.

---

## Problema

Datito está acoplado a:
- Una asignatura específica (Fundamentos de Ciencia de Datos, UdeC T2-2026)
- Un alumno específico (Cristóbal Herrera)
- Un repositorio monolítico que mezcla motor, curriculum y progreso

Queremos que otro estudiante pueda:
1. Subir su propio curriculum a `courses/su-ramo/`
2. Usar el mismo código base (`03_CODIGO/`, `.claude/skills/`)
3. Tener su propio progreso aislado en `learners/otro-alumno/`
4. Sin que se rompan las garantías G1–G14

---

## Opciones Consideradas

### Opción A: Multi-tenancy en la nube con auth
- **Ventaja:** Escala, acceso compartido, datos centralizados.
- **Desventaja:** Costo, complejidad, requiere backend, sale fuera del scope de Claude Code.
- **Decisión:** ❌ Rechazada. Demasiada complejidad para fase 1.

### Opción B: Tres directorios independientes (motor · curso · alumno)
- **Ventaja:** Claridad total. Cada cosa en su lugar. Fácil de entender y mantener.
- **Desventaja:** Los scripts deben leer config y resolver rutas; hay que actualizar todos.
- **Decisión:** ✅ Elegida. Simétrica con la arquitectura actual.

### Opción C: SaaS con GitHub Actions y Obsidian MCP
- **Ventaja:** Automatización, versionado, colaboración.
- **Desventaja:** Agrega capas (Actions, secretos, sincronización), más puntos de fallo.
- **Decisión:** ❌ Fuera de alcance ahora. Posible mejora futura.

---

## Decisión

**Implementar Opción B: separación en tres ámbitos (datito-core / courses / learners).**

### Layout de directorios

```
F:\MACI/
├── 01_DOCUMENTACION/
│   └── ADR-001-multi-course.md          ← este documento
│
├── 03_CODIGO/
│   ├── construir_navegacion.py          ✏️ lee config, resuelve paths
│   ├── datito_estado.py                 ✏️ idem
│   ├── datito_init_learner.py           ✨ NUEVO: inicializa learner
│   ├── verificar_contrato.py            ✏️ idem
│   └── ... (resto sin cambios)
│
├── .claude/skills/
│   ├── datito/SKILL.md                  ✏️ lee config, resuelve paths
│   ├── datito-progreso/SKILL.md         ✏️ idem
│   ├── datito-visual/SKILL.md           ✏️ idem
│   └── ... (resto sin cambios)
│
├── courses/                             ✨ NUEVO: paquetes de curso
│   ├── _template/                       ✨ plantilla para nuevos cursos
│   │   ├── README.md                    "cómo usar esta plantilla"
│   │   ├── datito.config.yaml           [plantilla vacía]
│   │   ├── curriculum.yaml              [estructura, 0 conceptos]
│   │   ├── clases.yaml                  [estructura, 0 clases]
│   │   ├── progreso.yaml
│   │   ├── errores_conceptuales.yaml
│   │   ├── estado.md
│   │   ├── patron_evaluacion.md
│   │   ├── grafo.yaml
│   │   ├── visual/
│   │   ├── bitacora/
│   │   ├── referencia/
│   │   └── dudas.yaml
│   │
│   └── fcd-2026-2/                      ✏️ EXISTENTE: Fundamentos FCD (default)
│       ├── datito.config.yaml           ✏️ agregado course_id
│       ├── curriculum.yaml              ✏️ sin cambios en contenido
│       ├── ... (todo lo demás igual)
│
└── learners/                            ✨ NUEVO: perfiles de alumno
    ├── cristobal_herrera/               ✏️ EXISTENTE: default actual
    │   ├── datito.config.yaml           ✏️ agregado learner_id, paths
    │   ├── progreso.yaml
    │   ├── errores_conceptuales.yaml
    │   ├── estado.md
    │   ├── dudas.yaml
    │   ├── bitacora/
    │   └── entregas/
    │
    └── otro_estudiante_fcd_2026_2/      ✨ ejemplo: otro alumno en FCD
        ├── datito.config.yaml
        ├── progreso.yaml
        └── ... (estado vacío)
```

### Resolución de rutas en tiempo de ejecución

**Regla:** Los scripts leen `datito.config.yaml` al inicio y resuelven todas las rutas relativamente.

```python
# Pseudocódigo
config = load_config()  # desde el directorio actual
COURSE_ROOT = f"courses/{config['course_id']}"
LEARNER_ROOT = f"learners/{config['learner_id']}"

curriculum = load_yaml(f"{COURSE_ROOT}/curriculum.yaml")
progreso = load_yaml(f"{LEARNER_ROOT}/progreso.yaml")
estado = load_yaml(f"{LEARNER_ROOT}/estado.md")
visual = f"{COURSE_ROOT}/visual"
```

**Backward compatibility:** Si el config no tiene `course_id` ni `learner_id`, usan valores por defecto:
```yaml
course_id: fcd-2026-2
learner_id: cristobal_herrera
```

---

## Cambios Mínimos (Fase 1)

### 1. Extender `datito.config.yaml` (backward compatible)
```yaml
# NUEVO
course_id: fcd-2026-2        # identificador del curso
learner_id: cristobal_herrera  # identificador del alumno

# EXISTENTE - sin cambios
alumno:
  nombre: Cristobal Herrera
  email: herrera.jara.cristobal@gmail.com

asignatura:
  nombre: Fundamentos de Ciencia de Datos
  ...
```

Si no están presentes, los scripts asumen los valores por defecto y funcionan como ahora.

### 2. Crear `courses/_template/`
- Estructura vacía pero válida
- Archivo README explicando cómo llenarla
- `curriculum.yaml` con ejemplo de la estructura (0 conceptos)
- `datito.config.yaml` con comentarios sobre qué editar

### 3. Crear `datito_init_learner.py`
Script que:
- Clona `courses/_template/` → `learners/<learner_id>/`
- Genera `progreso.yaml` inicial (todos los conceptos en `NO_ESTUDIADO`)
- Genera `estado.md` vacío
- Copia `datito.config.yaml` del nuevo alumno

### 4. Actualizar scripts existentes (sin cambiar lógica)
- `construir_navegacion.py`: leer config, resolver `{COURSE_ROOT}/visual/`
- `datito_estado.py`: leer config, resolver `{LEARNER_ROOT}/progreso.yaml`
- `verificar_contrato.py`: idem
- `.claude/skills/datito/SKILL.md`: inyectar config al inicio (ya lo hace)

### 5. Migración de MACI a la nueva estructura
```bash
# Paso 1: crear estructura nueva
mkdir -p courses/fcd-2026-2 learners/cristobal_herrera

# Paso 2: mover archivos
mv 07_DATITO/* courses/fcd-2026-2/
mv learners/cristobal_herrera/ (es nuevo, sus archivos dinámicos)
# Duplicar solo los dinámicos: progreso.yaml, errores_conceptuales.yaml, estado.md, dudas.yaml, bitacora/

# Paso 3: agregar course_id y learner_id a datito.config.yaml
```

---

## Lo que NO cambia

✅ **Invariantes preservados:**
- Garantías G1–G14: idénticas
- Arquitectura de componentes: skills, planos de datos, scripts
- Contrato (`spec.md`): ejecutable tal cual
- Lógica pedagógica de Datito: cero cambios
- Verificador de contrato: mismo test

✅ **Backward compatibility:**
- Sesiones antiguas siguen funcionando (config con valores por defecto)
- Certificaciones y evidencia auditada no se alteran

❌ **Fuera de alcance (Fase 2+):**
- SaaS, auth multi-usuario, UI de gestión
- Borrar Melbourne/Galaxy Zoo del repo actual
- Reescribir HTMLs a mano
- Migración automática de datos antiguos

---

## Cómo reutilizar en otro curso (10 minutos)

**Docente nuevo: "Quiero usar Datito para mi ramo de Estadística"**

1. **Clonar la plantilla:**
   ```bash
   cp -r courses/_template courses/estadistica-2026-2
   cd courses/estadistica-2026-2
   ```

2. **Editar `datito.config.yaml`:**
   ```yaml
   course_id: estadistica-2026-2
   asignatura:
     nombre: Estadística Inferencial
     periodo: T2-2026
     ...
   ```

3. **Llenar `curriculum.yaml`:**
   - Listar los conceptos del ramo
   - Indicar prerrequisitos
   - Apuntar al material (PDFs, notebooks, enlaces)

4. **Llenar `clases.yaml`:**
   - Las 15–20 clases en orden
   - Ficha Bloom de cada una
   - Objetivo, activación, cierre

5. **Crear perfiles de alumnos:**
   ```bash
   python 03_CODIGO/datito_init_learner.py --course estadistica-2026-2 --learner juan_perez
   ```

6. **Regenerar navegación:**
   ```bash
   python 03_CODIGO/construir_navegacion.py
   python 03_CODIGO/datito_estado.py
   ```

Listo. El docente ahora tiene:
- Curriculo definido en `courses/estadistica-2026-2/`
- Alumno activo en `learners/juan_perez/`
- Skills de Datito listos en `.claude/skills/`

---

## Verificación y Prueba

**Checklist antes de merging:**

- [ ] `datito.config.yaml` de MACI tiene `course_id: fcd-2026-2` y `learner_id: cristobal_herrera`
- [ ] `courses/fcd-2026-2/` contiene todo lo que antes estaba en `07_DATITO/` (excepto `progreso.yaml`, `errores_conceptuales.yaml`, `estado.md`, `dudas.yaml`, `bitacora/`)
- [ ] `learners/cristobal_herrera/` contiene el estado del alumno (progreso.yaml, etc.)
- [ ] `courses/_template/` existe y es válida (schema, README)
- [ ] `datito_init_learner.py` funciona: crea learner nuevo sin errores
- [ ] `construir_navegacion.py` inyecta navegación correcta (rutas resueltas)
- [ ] `datito_estado.py` regenera `estado.md` en `learners/{id}/`
- [ ] `/datito` funciona igual que antes (inyecta config, lee progreso, todo igual)
- [ ] `verificar_contrato.py` pasa 12 tests (garantías intactas)
- [ ] Docs en `00_LEEME.md` y `courses/_template/README.md` están claras

**Pruebas adicionales (fuera de scope, pero buenas para validar):**
- [ ] Crear learner ficticio para "Estadística 2026-2", verificar que funciona
- [ ] Correr `/datito` con learner ficticio, que haga una sesión
- [ ] Verificar que el learner original (cristobal) sigue intacto

---

## Tradeoffs

| Decisión | Ganancia | Costo |
|---|---|---|
| Tres ámbitos (core/course/learner) | Claridad, reutilización | Scripts más complejos (config + paths) |
| Backward compatibility vía defaults | Transición sin choque | Duplicación de defaults en cada script |
| Plantilla courses/_template/ | Ramp-up rápido para docentes | Hay que mantenerla sincronizada |
| Inventario de paths en cada script | Robusto, legible | No hay centralización (ventaja y desventaja) |

---

## Preguntas Abiertas (Fase 2)

1. **¿Cómo compartir coursepacks?** (p. ej., "Estadística UdeC" como template público)
2. **¿Versionado de curriculum?** Historial de cambios en curriculum.yaml
3. **¿Auditoría entre cursos?** Comparar patrones de error entre Estadística y FCD
4. **¿Datos sintéticos por defecto?** `courses/_template/` incluye datasets de ejemplo

---

## Aprobación

- **Autor:** Claude Haiku 4.5 (Arquitecto propuesto)
- **Revisor:** [Pendiente — Cristóbal Herrera]
- **Merge:** [Pendiente]

---

## Referencias

- `ARQUITECTURA.md` §9: máquina de estados y contrato
- `spec.md`: garantías G1–G14 (no cambian)
- `CLAUDE.md`: instrucciones del proyecto original (no cambian)
- `datito.config.yaml`: archivo de configuración (extendido aquí)
