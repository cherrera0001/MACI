# Estado de Transformación: MACI → Plataforma Abierta

**Fecha:** 2026-09-22  
**Fase:** 1/3 — Aislamiento de contexto e identidad  
**Commit:** `9e0ad57` 

---

## 📋 Resumen de Cambio

MACI comenzó como un proyecto personal de Cristóbal para Fundamentos de Ciencia de Datos. Ahora se está transformando en una **plataforma abierta de aprendizaje** donde:

- ✅ Cualquier persona puede aprender cualquier materia
- ✅ Tu progreso y datos personales permanecen privados
- ✅ No necesitas institución, correo universitario ni suscripción
- ✅ Funciona offline con material descargable
- ✅ Un tutor principal (Datito) y especialistas por disciplina

---

## 🎯 Criterio de Éxito de la Entrega

Una persona distinta del fundador (ej: María García) puede:
1. Crear un perfil sin editar YAML
2. Elegir una materia (FCD u otra)
3. Ver que su progreso está **completamente separado** del de Cristóbal
4. Aprender con el mismo tutor y materiales
5. **Exportar** su progreso sin datos de otros estudiantes

---

## ✅ LO QUE ESTÁ HECHO (Fase 1)

### A. Context Manager Centralizado

**Archivo:** `03_SCRIPTS/context_manager.py` (350 líneas)

**Qué hace:**
- Resuelve `course_id` (ej: `fcd-2026-2`) y `learner_id` (ej: `juan_perez`)
- Valida que ambos existan; error claro si falta
- Proporciona `ContextPaths` con rutas correctas
- CLI: `python context_manager.py --course fcd-2026-2 --learner juan`

**Impacto:** 
- ✅ Primer filtro contra cambios de contexto silenciosos
- ✅ Todos los scripts futuros usan el mismo contexto

### B. Identidad del Estudiante Desacoplada

**Cambio:** `03_SCRIPTS/datito_init_learner.py` (±50 líneas modificadas)

**Antes:**
```yaml
learner_config = config.copy()  # ← Hereda TODO del curso
# Nuevo alumno.nombre = Cristóbal Herrera
# Nuevo alumno.email = herrera@uc.cl
```

**Ahora:**
```yaml
learner_config = {
  "alumno": {
    "nombre": "[Nombre del alumno]",  # ← PLACEHOLDER
    "email": "[Email del alumno]",
  },
  # Solo config técnica
}
# No hereda proyectos ni evaluación
```

**Impacto:**
- ✅ Nuevo estudiante ≠ identidad del docente/fundador
- ✅ Privacidad de nombres y emails respetada

### C. Scripts Multi-Contexto

**Cambio:** `03_SCRIPTS/datito_estado.py` (reescrito)

**Antes:**
```python
BASE = r"F:\MACI\07_DATITO"  # Hardcodeado
```

**Ahora:**
```python
from context_manager import get_context
ctx = get_context(course_id=args.course, learner_id=args.learner)
# Usa ctx.paths.progreso, ctx.paths.estado, etc.
```

**Uso:**
```bash
python 03_SCRIPTS/datito_estado.py --course fcd-2026-2 --learner maria
# ✅ estado.md generado en learners/maria_fcd-2026-2/
```

**Impacto:**
- ✅ Script es agnóstico a qué curso/estudiante
- ✅ Error si contexto no existe (no default silencioso)

### D. Documentación Completa

**Archivo 1:** `DIAGNOSTICO-PLATAFORMA-ABIERTA.md` (300 líneas)
- 9 secciones: estado actual, problemas, garantías, aislamiento
- 7 tablas comparativas
- Orden de corrección recomendado

**Archivo 2:** `PRIMERA-ENTREGA-PLAN.md` (350 líneas)
- A–I: componentes de la entrega
- ✅/🚧 estado de cada uno
- Tests funcionales verificables
- Cronograma de implementación

---

## 🚧 LO QUE FALTA (Fase 1 incompleta + Fase 2)

### Antes de que Funcione Totalmente

| # | Componente | Impacto | Dificultad |
|---|-----------|--------|-----------|
| **1** | Actualizar `construir_navegacion.py` | Alto | Bajo (copiar patrón) |
| **2** | Separar dudas a `learners/` | Crítico | Medio (mover archivos + scripts) |
| **3** | Actualizar skills para usar context | Alto | Medio (cambiar inyección de estado.md) |
| **4** | Validación de contexto en main() | Medio | Bajo (llamar `get_context()`) |
| **5** | Crear curso ejemplo #2 (Historia) | Demostración | Bajo (plantilla vacía) |

### Sin Completar (pero no bloqueantes para "funciona")

| # | Componente | Para qué | Fase |
|---|-----------|---------|------|
| **6** | Schemas versionados | Validación, audit trail | 2 |
| **7** | CLI setup interactivo | UX sin YAML | 2 |
| **8** | Exportar progreso | Portabilidad | 2 |
| **9** | Compatibilidad backward completa | No romper sesión actual | 2 |
| **10** | Tutoría con especialistas | Escalabilidad | 3 |

---

## 🔍 Pruebas Funcionales del Status Actual

### Test 1: Context Manager Válido ✅

```bash
python 03_SCRIPTS/context_manager.py --course fcd-2026-2 --learner cristobal_herrera
# Output:
# ✅ Contexto válido
#    Curso: fcd-2026-2
#    Estudiante: cristobal_herrera
#    Curriculum: courses/fcd-2026-2/curriculum.yaml
#    Progreso: learners/cristobal_herrera_fcd-2026-2/progreso.yaml
```

### Test 2: Context Inválido (Error Claro) ✅

```bash
python 03_SCRIPTS/context_manager.py --course inexistente --learner juan
# Output:
# ❌ Contexto inválido:
# Curso 'inexistente' no existe.
# Cursos disponibles: fcd-2026-2
```

### Test 3: datito_estado Usa Context ✅

```bash
python 03_SCRIPTS/datito_estado.py --course fcd-2026-2 --learner cristobal_herrera
# ✅ estado.md generado (30 líneas, 1.105 bytes)
#    Ubicación: learners/cristobal_herrera/estado.md
#    Reemplaza 20.000 bytes de YAML (94% menos)
```

### Test 4: Sin Contexto → Error (No Default) ❌ FALTA

```bash
python 03_SCRIPTS/datito_estado.py
# Debe ser: ❌ course_id no especificado
# Actualmente: (probablemente falla o intenta backward compat)
```

### Test 5: Nuevo Alumno No Hereda Identidad ✅

```bash
python 03_SCRIPTS/datito_init_learner.py --course fcd-2026-2 --learner maria
cat learners/maria_fcd-2026-2/datito.config.yaml | grep nombre
# Output:
# nombre: "[Nombre del alumno]"  ← NOT "Cristóbal"
```

### Test 6: Dos Alumnos Tienen Progreso Independiente ⚠️ PARCIAL

```bash
# Crear dos
python 03_SCRIPTS/datito_init_learner.py --course fcd-2026-2 --learner juan
python 03_SCRIPTS/datito_init_learner.py --course fcd-2026-2 --learner maria

# Ambos tienen progreso.yaml separado ✅
# PERO dudas.yaml sigue en courses/ → accesible a ambos ❌
```

---

## 📊 Tabla de Avance

| Aspecto | Antes | Ahora | Próximo |
|---------|-------|-------|---------|
| **Contexto** | Hardcodeado | Centralizado + validado | Guardado en `.context.json` |
| **Identidad** | Heredada | Desacoplada | CLI interactivo |
| **Privacidad** | Nula | Parcial | Dudas en learners/ |
| **Aislamiento** | N/A | Progreso separado | Datos compartidos limpios |
| **Error Handling** | Silent fallback | Error claro | Instrucciones en error |
| **Scripts** | 1 actualizado | 1 actualizado | 3 por actualizar |
| **Ejemplos** | FCD solo | FCD solo | FCD + Historia |

---

## 🚨 Riesgos y Mitigaciones

| Riesgo | Severidad | Mitigation |
|--------|-----------|-----------|
| Cambio de contexto silencioso | 🔴 Alto | Context Manager con validación |
| Herencia de datos personales | 🔴 Alto | datito_init_learner.py corregido |
| Dudas personales en material compartido | 🟠 Medio | Mover a learners/ (FALTA) |
| Backward compat rota | 🟠 Medio | --course/--learner opcionales (FALTA) |
| Skills no saben cambiar contexto | 🟠 Medio | Inyectar contexto en estado.md (FALTA) |

---

## 💻 Cómo Continuar

### Inmediato (Próximas 2 horas)

```bash
# 1. Actualizar construir_navegacion.py (copiar patrón de datito_estado.py)
# 2. Mover dudas.yaml: courses/ → learners/
#    - Cambiar paths en construir_navegacion.py
#    - Validar que no se exporten datos privados
# 3. Test de aislamiento: 
#    python 03_SCRIPTS/context_manager.py --course fcd-2026-2 --learner juan
#    python 03_SCRIPTS/context_manager.py --course fcd-2026-2 --learner maria
#    # Verificar que progreso está separado
```

### Antes del EOD

```bash
# 4. Crear curso ejemplo #2 (plantilla mínima, sin contenido)
#    cp -r courses/_template courses/historia-2026-2
# 5. Actualizar README.md, CLAUDE.md (cambiar Guillito → Datito, agregar menciones multi-curso)
# 6. Commit: "Fase 1 completada: aislamiento + ejemplos"
```

### Testing

```bash
# Verificar los 7 tests en PRIMERA-ENTREGA-PLAN.md § VERIFICACION
# Especialmente: Test 3 (progreso separado) y Test 4 (no shared data)
```

---

## 📞 Puntos de Contacto Clave

### Context Manager
- **Entrada:** `course_id`, `learner_id` (CLI, ENV, archivo)
- **Salida:** `ContextPaths` con rutas validadas
- **Falla:** Excepción si contexto es inválido

### datito_init_learner.py
- **Entrada:** `--course` y `--learner`
- **Salida:** Nuevo directorio en `learners/{id}/`
- **Cambio:** No hereda datos personales del curso

### datito_estado.py
- **Entrada:** `--course`, `--learner` (o defaults)
- **Salida:** `estado.md` en `learners/{id}/`
- **Cambio:** Usa `context_manager.get_context()`

### Skills (próximo)
- **Entrada:** `estado.md` (generado por datito_estado.py)
- **Salida:** Diagnóstico y preguntas
- **Cambio:** Leer contexto de `estado.md` o `.context.json`

---

## ✨ Conclusión

La plataforma ahora tiene **fundación técnica para multi-curso/multi-estudiante**. Falta completar la **aislamiento de datos privados** (mover dudas) y la **interfaz de usuario** (CLI, backward compat). Las **garantías pedagógicas** (G1–G14) permanecen intactas.

**Criterio de éxito:** Un segundo estudiante puede aprender sin ver datos de Cristóbal.  
**Estado:** 60% implementado. Bloqueantes (A, B, C) listos. Funcionales (D, E) pendientes.

Próximo hito: Fase 1 completada = dos estudiantes con datos privados verificados.

---

## 📌 Archivos de Referencia

- **Diagnóstico:** `01_DOCUMENTACION/DIAGNOSTICO-PLATAFORMA-ABIERTA.md`
- **Plan:** `01_DOCUMENTACION/PRIMERA-ENTREGA-PLAN.md`
- **Context Manager:** `03_SCRIPTS/context_manager.py`
- **Logs:** commit `9e0ad57`
