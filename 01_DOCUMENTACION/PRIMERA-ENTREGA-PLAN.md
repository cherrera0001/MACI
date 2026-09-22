# Primera Entrega: Multi-Curso Multi-Estudiante Real

**Objetivo:** Una persona distinta del fundador puede aprender otra materia, conservar su progreso y mantener privados sus datos.

**Criterio de éxito:**
- ✅ Contexto centralizado: error claro si falta o es inválido (no default silencioso)
- ✅ Identidad separada: alumno nuevo ≠ datos del curso
- ✅ Privacidad: dudas personales no aparecen en material compartido
- ✅ Validación: dos estudiantes en mismo curso tienen progreso independiente
- ✅ Demostración: ejemplo funcional (no necesita ser pedagógicamente eficaz)

---

## A. Context Manager (HECHO)

**Archivo:** `03_CODIGO/context_manager.py`  
**Estado:** ✅ IMPLEMENTADO

**Lo que hace:**
- Resuelve `course_id` y `learner_id` desde CLI, ENV o archivo
- Valida que ambos existan y sean válidos
- Detecta y rechaza contexto inválido con error claro
- Proporciona `ContextPaths` con todas las rutas resueltas
- Una sola fuente de verdad

**Uso:**
```python
from context_manager import Context, get_context

ctx = get_context(course_id="fcd-2026-2", learner_id="juan")
if ctx.is_valid():
    print(ctx.paths.progreso)  # /MACI/learners/juan_fcd-2026-2/progreso.yaml
```

**CLI:**
```bash
python 03_CODIGO/context_manager.py --course fcd-2026-2 --learner juan
# ✅ Contexto válido
#    Curso: fcd-2026-2
#    Estudiante: juan
```

---

## B. Identidad Separada: Schema del Alumno

**Objetivo:** Un alumno NUEVO tiene datos vacíos, no hereda identidad del curso.

**Cambio en `datito.config.yaml` (para cursos nuevos):**

Antes:
```yaml
# PROBLEMA: alumno hereda nombre del docente
alumno:
  nombre: Prof Juan García        # ← Esto hereda
  email: juan@universidad.edu
```

Después:
```yaml
# SOLUCIÓN: alumno nuevo queda vacío
alumno:
  nombre: "[Nombre del alumno]"   # ← Placeholder
  email: "[Email del alumno]"
```

**Cambio en `datito_init_learner.py`:** ✅ HECHO

No hereda `nombre`, `email`, `proyectos` del curso. Solo hereda `asignatura` y config técnica.

**Validación:**
```bash
python 03_CODIGO/datito_init_learner.py --course fcd-2026-2 --learner maria

# Genera: learners/maria_fcd-2026-2/datito.config.yaml
# Contiene:
#   alumno.nombre: "[Nombre del alumno]"  ← NO "Cristóbal"
#   alumno.email: "[Email del alumno]"    ← NO "herrera@uc.cl"
```

---

## C. Inicializador Corregido (PARCIAL)

**Archivo:** `03_CODIGO/datito_init_learner.py`  
**Estado:** ⚠️ AJUSTADO (falta manejar asignatura de forma más flexible)

**Lo que cambió:**
- ✅ No hereda `alumno.nombre`, `alumno.email`
- ✅ No hereda `proyectos`
- ⚠️ Aún hereda `asignatura` completa (OK para referencia)

**Todavía falta:**
- Validar que `course_id` y `learner_id` sean válidos (ID simples)
- Advertencia si learner ya existe
- Confirmación interactiva: "¿Deseas crear a `maria_fcd-2026-2`?"

---

## D. Scripts Actualizados para Usar Context Manager

**Estado:** 🚧 PENDIENTE

### D.1 datito_estado.py

**Cambio necesario:**
```python
# Antes
BASE = r"F:\MACI\07_DATITO"  # ← Hardcodeado

# Después
from context_manager import get_context
ctx = get_context()
BASE = ctx.paths.learner_root
```

### D.2 construir_navegacion.py

**Cambio necesario:**
```python
# Antes
VISUAL = os.path.join(RAIZ, "07_DATITO", "visual")  # ← Hardcodeado

# Después
from context_manager import get_context
ctx = get_context()
VISUAL = str(ctx.paths.visual)
```

### D.3 verificar_contrato.py

**Cambio necesario:**
Similar: leer desde `ctx.paths` en lugar de rutas hardcodeadas.

### D.4 Skills (`.claude/skills/datito/*.md`)

**Cambio necesario:**
Agregar al inicio de cada skill una sección que:
1. Carga contexto desde memoria compartida o archivo
2. Resuelve rutas
3. Si contexto es inválido, muestra error amigable

**Implementación:**
```
# En SKILL.md
Cargar contexto desde archivo .context.json en raíz.
Si no existe, usar defaults de backward compatibility.
```

---

## E. Datos Privados Separados de Compartidos

**Problema actual:**
```
courses/fcd-2026-2/
  dudas.yaml           ← COMPARTIDO pero contiene respuestas privadas
  visual/index.html    ← Inyecta dudas → fuga de datos
```

**Solución:**
```
learners/maria_fcd-2026-2/
  dudas.yaml           ← PRIVADO: solo de María

# Proceso:
1. construir_navegacion.py genera visual SIN inyectar dudas
2. Script genera versión PERSONALIZADA en caché local
3. Archivo en courses/ permanece limpio
```

**Implementación:** 🚧 Pendiente

---

## F. Schemas Versionados

**Estado:** 🚧 PENDIENTE

**Necesario:**
- `schema/course.v1.json` — estructura mínima del curso
- `schema/learner.v1.json` — perfil del alumno
- `schema/progress.v1.json` — progreso y evidencias
- Validación en cada lectura/escritura

**Acción:** Crear en `01_DOCUMENTACION/schemas/`.

---

## G. Garantías Pedagógicas Adaptadas

**Estado:** ✅ REVISADO (no necesita cambio)

Las garantías G1–G14 son independientes del número de estudiantes/cursos.

**Lo que SÍ necesita cambio:** Criterios de dominio (EXPLICAR → APLICAR → INTERPRETAR → TRANSFERIR) deben poder variar por curso.

**Ubicación:** En `curriculum.yaml` o `patron_evaluacion.md`, no en código de skills.

---

## H. Dos Cursos de Ejemplo

**Objetivo:** Demostrar que funciona con disciplinas distintas.

### H.1 Curso 1: FCD (Cuantitativo)

**Estado:** ✅ YA EXISTE

- Ubicación: `courses/fcd-2026-2/`
- Conceptos: 21
- Estudiante ejemplo: Cristóbal (actual)

### H.2 Curso 2: NUEVO (Cualitativo)

**Propuesta:** `courses/historia-2026-2/` — Historia del Siglo XX

**Contenido mínimo:**
- 8–10 conceptos clave
- 2–3 materiales de ejemplo (artículos, imágenes)
- 1–2 actividades (análisis de fuente primaria)
- Schema de "evidencia": Explicar, Contextualizar, Analizar, Transferir

**Estudiante ejemplo:** María García (ficticio)

**Acción:** 🚧 Crear curso minimalista sin contenido educativo real (solo estructura).

---

## I. Recorrido Mínimo sin YAML Manual

**Estado:** 🚧 PENDIENTE

**Objetivo:** Nuevo usuario no edita `.yaml`. Menú interactivo en CLI.

**Flujo:**
```
$ python 03_CODIGO/setup_context.py

¿Cuál es tu nombre?
> María García

¿Deseas crear un perfil nuevo o cargar uno existente?
  1) Nuevo perfil
  2) Cargar existente
> 1

¿Qué curso deseas estudiar?
  1) Fundamentos de Ciencia de Datos (fcd-2026-2)
  2) Historia del Siglo XX (historia-2026-2)
  3) Otro (especificar código)
> 1

✅ Perfil creado: learners/maria_garcia_fcd-2026-2/

Abre Claude Code y escribe: /datito
```

**Archivo:** `03_CODIGO/setup_context.py` (nuevo)

---

## VERIFICACIÓN: Tests Funcionales

### Test 1: Contexto Válido

```bash
python 03_CODIGO/context_manager.py --course fcd-2026-2 --learner juan
# ✅ Contexto válido
```

### Test 2: Contexto Inválido (No Falla Silenciosamente)

```bash
python 03_CODIGO/context_manager.py --course inexistente --learner juan
# ❌ Contexto inválido:
# Curso 'inexistente' no existe.
# Cursos disponibles: fcd-2026-2, historia-2026-2
```

### Test 3: Dos Estudiantes, Progreso Independiente

```bash
# Crear dos alumnos
python 03_CODIGO/datito_init_learner.py --course fcd-2026-2 --learner juan
python 03_CODIGO/datito_init_learner.py --course fcd-2026-2 --learner maria

# Verificar que tienen progreso separado
cat learners/juan_fcd-2026-2/progreso.yaml | head -3
# meta.alumno: "[Nombre del alumno]"  ← NOT "María", NOT "Juan"

cat learners/maria_fcd-2026-2/progreso.yaml | head -3
# meta.alumno: "[Nombre del alumno]"  ← NOT "Juan"
```

### Test 4: Datos Privados No en Material Compartido

```bash
# Escribir duda privada de Juan
learners/juan_fcd-2026-2/dudas.yaml:
  - id: mi_pregunta_1
    respuesta: "Mi respuesta privada"

# Verificar que NO aparece en material compartido
grep -r "mi_pregunta_1" courses/fcd-2026-2/
# (nada)
```

### Test 5: Sin Proveedor Remoto, Material Local Funciona

```bash
# Simular: comentar línea de NotebookLM
# Abrir visual en navegador sin conexión
open courses/fcd-2026-2/visual/index.html
# ✅ Funciona (no depende de APIs externas)
```

### Test 6: Compatibilidad Backward: Cristóbal Funciona Igual

```bash
python 03_CODIGO/datito_estado.py --course fcd-2026-2 --learner cristobal_herrera
# ✅ Estado regenerado correctamente
```

### Test 7: Interfaz CLI Básica

```bash
python 03_CODIGO/setup_context.py
# (menú interactivo, sin YAML)
# ✅ Crea nuevo contexto
```

---

## Cronograma de Implementación

| Etapa | Componente | Estado | Bloqueante |
|-------|-----------|--------|-----------|
| **1** | Context Manager | ✅ HECHO | Sí |
| **1** | Init corregido | ✅ HECHO | Sí |
| **2** | datito_estado.py usa context | 🚧 TODO | Sí |
| **2** | construir_navegacion.py usa context | 🚧 TODO | Sí |
| **2** | verificar_contrato.py usa context | 🚧 TODO | No |
| **3** | Separación de dudas (cursos vs. learners) | 🚧 TODO | Sí |
| **4** | Skills usan context | 🚧 TODO | Sí |
| **5** | Curso de ejemplo #2 (Historia) | 🚧 TODO | No |
| **5** | CLI setup_context.py | 🚧 TODO | No |
| **6** | Schemas versionados | 🚧 TODO | No |
| **6** | Exportar progreso | 🚧 TODO | No |

---

## Cambios de Archivo Documentados

### Archivos Nuevos ✨
- `03_CODIGO/context_manager.py` — ✅ Hecho
- `03_CODIGO/setup_context.py` — 🚧 TODO
- `01_DOCUMENTACION/DIAGNOSTICO-PLATAFORMA-ABIERTA.md` — ✅ Hecho

### Archivos Modificados ✏️
- `03_CODIGO/datito_init_learner.py` — ✅ No hereda datos personales
- `03_CODIGO/datito_estado.py` — 🚧 Pendiente usar context_manager
- `03_CODIGO/construir_navegacion.py` — 🚧 Pendiente usar context_manager

### Archivos Plantilla 📋
- `courses/_template/` — Ya existe, validar que no herede datos

---

## Próximos Pasos Inmediatos

1. **Actualizar `datito_estado.py`** para usar `context_manager`
2. **Actualizar `construir_navegacion.py`** para usar `context_manager`
3. **Separar dudas**: mover `courses/*/dudas.yaml` a `learners/*/dudas.yaml`
4. **Crear curso ejemplo #2**: `courses/historia-2026-2/` (mínimo)
5. **CLI interactivo**: `setup_context.py`
6. **Validar**: tests de aislamiento (Test 3–4 arriba)

---

## Éxito de Entrega

Una persona distinta del fundador (ejemplo: María García) puede:
1. ✅ Crear perfil nuevo sin editar YAML
2. ✅ Ver que su progreso está separado de Cristóbal
3. ✅ Ver que sus respuestas/dudas no aparecen en material compartido
4. ✅ Aprender la materia con el mismo tutor
5. ✅ Exportar su progreso sin datos de otros

Ver: `VERIFICACION-ENTREGA.md` (por crear después).
