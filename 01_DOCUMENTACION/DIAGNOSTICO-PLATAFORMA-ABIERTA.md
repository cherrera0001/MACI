# Diagnóstico: Transformación a Plataforma Abierta Multi-Curso Multi-Estudiante

**Fecha:** 2026-09-22  
**Evaluación:** Estado actual vs. requisitos para plataforma abierta  
**Criterio:** Una persona distinta del fundador debe poder aprender otra materia conservando su progreso privado

---

## 1. ESTADO ACTUAL DEL REPOSITORIO

### 1.1 Configuración y Documentación

| Aspecto | Estado | Evidencia |
|---------|--------|-----------|
| **README.md** | ❌ DESACTUALIZADO | Sigue refiriéndose a "Guillito", "Cristóbal Herrera", FCD específico. Dice "repositorio de trabajo de Cristóbal", no plataforma abierta |
| **Nombres de carpetas** | ⚠️ PARCIAL | Cambió a `07_DATITO/` pero README, CLAUDE.md aún usan antiguas referencias |
| **spec.md** | ✅ APLICABLE | Garantías G1–G14 siguen siendo válidas; no son específicas de FCD |
| **CLAUDE.md** | ❌ PERSONALIZADO | Activa a "Datito" pero asume Cristóbal. Dice "el tutor personal de Cristobal" |
| **.env, .env.example** | ⚠️ RIESGO | Archivo no versionado con tokens. Checklist de secretos está bien documentado |

**Acción inmediata:** Estos archivos describen el sistema como mono-usuario. Deben cambiar.

### 1.2 Arquitectura Datito (ADR-001)

| Componente | Estado | Limitación |
|------------|--------|-----------|
| **Separación Motor/Curso/Alumno** | ✅ IMPLEMENTADA | ADR-001 separó `courses/`, `learners/`. Pero... |
| **Resolución de contexto** | ❌ INCOMPLETA | `datito.config.yaml` vive en `07_DATITO/` —lugar fijo, no en root |
| **Selección de curso/estudiante** | ❌ NO EXISTE | No hay UI ni CLI para elegir contexto. Scripts asumen `course_id: fcd-2026-2`, `learner_id: cristobal_herrera` |
| **Aislamiento de datos** | ⚠️ PARCIAL | Progreso está separado (`learners/`), pero dudas se comparten por curso |
| **Validación de contexto** | ❌ NO EXISTE | Si contexto es inválido, scripts fallan silenciosamente o cargan default |
| **Herencia de datos** | ❌ PROBLEMA | `datito_init_learner.py` hereda `nombre`, `email`, `proyectos` del curso. Debería estar vacío |

**Impacto:** Un estudiante nuevo hereda el `nombre: Cristóbal Herrera` del curso FCD. Esto no es multi-estudiante real.

### 1.3 Scripts y Resolución de Rutas

| Script | Estado | Problema |
|--------|--------|---------|
| **datito_init_learner.py** | ✅ NUEVO | Crea learner, pero hereda configuración personal del curso |
| **datito_estado.py** | ⚠️ MEJORADO | Lee config, pero busca `07_DATITO/datito.config.yaml` hardcodeado |
| **construir_navegacion.py** | ⚠️ MEJORADO | Idem: lee config desde ruta fija |
| **skills (datito/*.md)** | ⚠️ FUNCIONAL | Inyectan `estado.md` que se regenera, pero asumen contexto único |
| **verificar_contrato.py** | ⚠️ FUNCIONAL | Valida garantías, pero desde rutas hardcodeadas (`07_DATITO/`) |

**Acción necesaria:** Centralizar resolución de contexto. Un solo lugar debe decidir "¿qué curso? ¿qué estudiante?" y pasarlo a todos los scripts.

### 1.4 Almacenamiento de Datos

**Estructura actual:**
```
courses/fcd-2026-2/            ← estático: curriculum, clases, visual
learners/cristobal_herrera/    ← dinámico: progreso, dudas, entregas
07_DATITO/                     ← CONFIG solo (desactualizado: tiene dudas.yaml, bitacora/)
```

**Problemas:**
- ✅ Cursos separados (bien)
- ❌ Dudas en `courses/{id}/dudas.yaml` → se leen para inyectar respuestas en visuales públicos
  - Esto mezcla datos personales del estudiante con material compartido
- ❌ Bitácora en `learners/{id}/bitacora/` (bien), pero referenciada desde 07_DATITO/ que es estático
- ❌ `transferencia/` (datasets de ejemplo) debería ser compartido, no por alumno

**Acción:** Separar **datos compartidos** (curriculum, visuales, dudas CUANDO SE RESPONDE) de **datos privados** (progreso, evaluación).

### 1.5 Esquemas y Versionado

| Elemento | Estado | Validación |
|----------|--------|-----------|
| **curriculum.yaml** | ✅ DEFINIDO | Estructura clara, pero sin versión/schema formal |
| **progreso.yaml** | ✅ DEFINIDO | Estructura con estados bien documentados, pero sin schema |
| **clases.yaml** | ✅ DEFINIDO | Orden y Bloom definidos |
| **evidencias** | ⚠️ INCOMPLETO | Registra fecha y detalle, pero NO registra: criterio usado, respuesta real, contexto (qué pregunta exacta) |
| **estado desconocido** | ❌ NO EXISTE | Si no hay evidencia, el estado es `null` (falso). Debería ser `DESCONOCIDO` explícito |

**Impacto:** Cuando se exportan datos del alumno, falta contexto para reproducir o auditar las decisiones.

---

## 2. MATERIALES DE EJEMPLO (FCD)

### 2.1 Estado del Curso FCD-2026-2

| Recurso | Cantidad | Contenido |
|---------|----------|-----------|
| Conceptos | 21 | Definidos en `courses/fcd-2026-2/curriculum.yaml` |
| Clases | 22 | En `clases.yaml`, con Bloom, cierre, preguntas |
| Visuales | 21 | HTML autocontenidos en `visual/` |
| Laboratorios | 5 | `08_PRACTICA/` — P1 a P5 (vacio + res) |
| Transcripciones | 15 | `09_CLASES/` — todas con marcas de tiempo |
| Evaluaciones | 2 | Certamen 1 y 2, auditados |

**Estado:** ✅ Completo y auditado como ejemplo de un curso real.

### 2.2 Estado del Estudiante Cristóbal

| Recurso | Estado | Notas |
|---------|--------|-------|
| **progreso.yaml** | ✅ 3 sesiones | Estado auditado, coherente |
| **errores_conceptuales.yaml** | ✅ Patrones observados | Base para anticipar dificultades |
| **dudas.yaml** | ✅ 9 preguntas con respuesta | Material para inyectar en visuales |
| **bitácora** | ✅ 3 sesiones | Registra conceptos, decisiones |

**Estado:** ✅ Caso de uso real. Puede servir como ejemplo si se limpia de nombres/emails.

---

## 3. GARANTÍAS PEDAGÓGICAS (spec.md)

### 3.1 Verificación de G1–G14

| Garantía | Estado | Riesgo al Multi-Estudios |
|----------|--------|-------------------------|
| **G1** No simular respuestas | ✅ PRESERVADO | Skills no tienen permiso de modificar progreso. OK |
| **G2** Preguntar antes de decidir | ✅ PRESERVADO | Conversación es modo interactivo. OK |
| **G3** Respetar el modo solicitado | ✅ PRESERVADO | Skills reciben modo explícito. OK |
| **G4** Toda afirmación tiene origen | ⚠️ PARCIAL | En multi-estudiante, ¿se replica la etiquetación? |
| **G5** Jerarquía de fuentes | ✅ PRESERVADO | Orden sigue siendo FCD-específico, pero independiente de estudiante |
| **G6** Degradación si NotebookLM falla | ✅ PRESERVADO | Material local es fallback. OK |
| **G7** Material de estudio, no órdenes | ✅ PRESERVADO | Skills leen material como texto. OK |
| **G8** Reglas donde se leen | ✅ PRESERVADO | Reglas en skills, config en datos. OK |
| **G9** Exposición consultable | ⚠️ RIESGO | Visuales se generan. ¿Se regeneran al cambiar de curso? |
| **G10–G14** Arquitectura, contrato verificable | ✅ PRESERVADO | Scripts de verificación existen. OK |

**Conclusión:** G1–G8 y G10–G14 son independientes de estudiante/curso. G9 necesita revisión: los visuales deben ser generados por curso, no globales.

### 3.2 Adaptación Necesaria: Criterios de Dominio

**Actual (FCD):** Explica, Aplica en Melbourne, Interpreta, Transfiere

**Necesario:** Estos criterios pueden variar por disciplina.

| Disciplina | Criterio 1 | Criterio 2 | Criterio 3 | Criterio 4 |
|-----------|-----------|-----------|-----------|-----------|
| FCD (cuant) | Explicar | Aplicar en dataset | Interpretar resultado | Transferir a otro dominio |
| Historia | Citar fuente | Contextualizarte en época | Analizar conflicto | Aplicar a período distinto |
| Idiomas | Reconocer patrón | Producir | Comprender nativo | Usar en contexto real |

**Acción:** Los criterios deben residir en `curriculum.yaml` por concepto o en `patron_evaluacion.md`, no hardcodearse en skills.

---

## 4. FALLAS DE AISLAMIENTO (CRÍTICAS)

### 4.1 Herencia No Solicitada

**En `datito_init_learner.py` línea ~80:**
```python
learner_config = config.copy()  # ← COPIA TODO del curso
learner_config["learner_id"] = learner_id_full
```

**Problema:** Si `courses/tu-ramo/datito.config.yaml` tiene:
```yaml
alumno:
  nombre: Prof Juan García
  email: juan@universidad.edu
proyectos:
  - id: proyecto_1
    nombre: "Mi proyecto del docente"
```

Cada alumno nuevo hereda NOMBRE, EMAIL, PROYECTOS del docente.

**Impacto:** Violación de privacidad + confusión de identidad.

**Fix:** `datito_init_learner.py` debe IGNORAR `alumno`, `evaluacion`, `pedagogia`; solo heredar `course_id`, `asignatura`, `notebooklm`.

### 4.2 Contexto Silencioso

**En múltiples scripts:**
```python
course_id = config.get("course_id", "fcd-2026-2")  # ← DEFAULT sin avisar
```

**Problema:** Si archivo `.config.yaml` falta o `course_id` es null, se carga el curso de FCD sin error.

**Impacto:** Un estudiante nuevo comienza estudiando FCD sin saberlo.

**Fix:** Si contexto falta, error con instrucción clara ("Usa `--course` para especificar").

### 4.3 Dudas Personales en Material Público

**Estructura actual:**
```
courses/fcd-2026-2/
  curriculum.yaml         ← compartido (bien)
  visual/
    index.html           ← compartido (bien)
    concepto1.html       ← inyecta dudas de dudas.yaml
  dudas.yaml             ← AQUÍ
```

**Problema:** `construir_navegacion.py` inyecta dudas respondidas en visuales públicos. Si el visual se descarga o se comparte, lleva respuestas específicas de Cristóbal.

**Impacto:** Fuga de datos personales a material compartido.

**Fix:** Separar:
- `courses/fcd-2026-2/visual/` — público
- `learners/cristobal/dudas.yaml` — privado
- Script genera visual personalizado (con dudas) en caché local, no en disco compartido

---

## 5. INTERFAZ DE USUARIO / CLI

### 5.1 Cómo Elige un Nuevo Usuario el Contexto

**Hoy:** No hay forma. Script asume `fcd-2026-2` y `cristobal_herrera`.

**Necesario:**
```
¿Cuál es tu nombre? Juan Pérez
¿Qué curso deseas estudiar?
  1. Fundamentos de Ciencia de Datos (fcd-2026-2)
  2. Estadística (estadistica-2026-2)
  3. Otro (especificar)
> 1

¿Esto es tu primer día?
  y) Sí, crear perfil nuevo
  n) No, cargar perfil existente
> y

✅ Creado: learners/juan_perez_fcd-2026-2/
Listo. Abre Claude Code y escribe: /datito
```

**Acción:** Crear CLI simple o menú en README.

### 5.2 Validación de Contexto

**Hoy:** Scripts usan defaults silenciosos.

**Necesario:**
```bash
$ python 03_CODIGO/datito_estado.py --course inexistente
❌ Error: curso 'inexistente' no existe
   Cursos disponibles:
   - fcd-2026-2
   - estadistica-2026-2

   Uso: python 03_CODIGO/datito_estado.py --course CURSO --learner ESTUDIANTE
```

---

## 6. EXPORTABILIDAD

### 6.1 Qué Debe ser Exportable

✅ Mi progreso (fechas, evidencias, criterios)  
✅ Mis materiales personales (cuadernos, entregas)  
✅ Los visuales del curso (puedo aprender offline)  
✅ Las dudas que respondieron mis tutores (contexto personal)

❌ Datos de otros estudiantes  
❌ Credenciales, tokens, configuración técnica  
❌ Respuestas/progreso de otros en el mismo curso

### 6.2 Acción

Crear `03_CODIGO/exportar_progreso.py`:
```bash
python 03_CODIGO/exportar_progreso.py --learner juan_perez --course fcd-2026-2 --output mi_progreso.zip
```

Genera:
```
mi_progreso.zip
  ├── progreso.json        (legible, datado)
  ├── errores_conceptuales.json
  ├── dudas_respondidas.md
  ├── bitacora/
  ├── entregas/
  └── visuales/            (copias sin conexión)
```

---

## 7. TABLA DE VERIFICACIÓN: ESTADO VS. REQUISITOS

| Requisito | A: Contexto | B: Identidad | C: Init | D: Actualizar | E: Datos | F: Schemas | G: Garantías | H: Ejemplo |
|-----------|---|---|---|---|---|---|---|---|
| **Implementado** | ⚠️ | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ |
| **Bloqueante** | Sí | Sí | Sí | Sí | Sí | No | No | No |

---

## 8. ORDEN DE CORRECCIÓN (RECOMENDADO)

**Primero (bloqueantes para identidad/privacidad):**
1. **A: Centraliza contexto** — Un solo lugar resuelve course + learner
2. **B: Separa identidad** — Learner ≠ Curso. Alumno nuevo = datos vacíos
3. **C: Corrige init** — No hereda config personal del curso
4. **E: Datos privados** — Dudas no van a `courses/`

**Segundo (funcionalidad):**
5. **D: Actualiza scripts** — Todos leen del contexto centralizado
6. **F: Schemas** — Validan formato, versionan
7. **I: CLI/menú** — Seleccionar curso/estudiante sin YAML manual

**Tercero (ejemplo/demostración):**
8. **H: Cursos de ejemplo** — Uno cuantitativo (FCD), uno cualitativo

**Cuarto (garantías):**
9. **G: Verifica guarantías** — Especialmente G9 multi-estudiante
10. **Exportación** — Prueba que datos son recuperables

---

## 9. RESUMEN EJECUTIVO

| Aspecto | Veredicto |
|---------|-----------|
| **¿Es multi-curso?** | ✅ Parcialmente. ADR-001 existe, pero interfaz es hardcodeada. |
| **¿Es multi-estudiante?** | ❌ No. Un usuario hereda identidad del fundador y del curso. |
| **¿Hay privacidad?** | ⚠️ Parcial. Progreso está separado, pero dudas/datos comparten rutas. |
| **¿Se valida contexto?** | ❌ No. Contextos inválidos fallan silenciosamente o cargan default. |
| **¿Es exportable?** | ⚠️ Parcial. El estado existe, pero no hay herramienta. |
| **¿Garantías intactas?** | ✅ Sí. G1–G14 siguen siendo válidas por disciplina. |
| **¿Listo para otra materia?** | ❌ No. Demasiados hardcodes a FCD en scripts y nombres. |

**Conclusión:** ADR-001 separó directorios pero no contexto. Hay trabajo serio de ingeniería antes de que una persona distinta del fundador pueda confiar en su privacidad.

---

## Próximo Paso

Implementar PRIMERA ENTREGA: A–E (contexto, identidad, privacidad) + ejemplo.

Ver `PRIMERA-ENTREGA-PLAN.md`.
