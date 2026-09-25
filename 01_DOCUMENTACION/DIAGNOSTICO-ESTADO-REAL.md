# Diagnóstico: Estado Real vs. Afirmaciones Previas

**Fecha:** 2026-09-22  
**Evaluación:** Verificación de fase anterior contra código actual  
**Hallazgo:** Múltiples errores en documentación y estructura. Necesaria reorganización desde la base.

---

## 1. ESTADO REAL DEL REPOSITORIO

### 1.1 Estructura Actual (F:\MACI)

```
F:\MACI/                          ← Repositorio de desarrollo
├── 01_DOCUMENTACION/             ← Legacy: numeración antigua
├── 07_DATITO/                    ← ORIGINAL: toda la estructura de tutor
│   ├── curriculum.yaml           ← Original
│   ├── clases.yaml
│   ├── progreso.yaml
│   ├── dudas.yaml
│   ├── bitacora/
│   └── visual/
│
├── courses/                       ← NUEVA ESTRUCTURA (ADR-001)
│   ├── _template/                ← Plantilla vacía
│   ├── fcd-2026-2/               ← COPIA de 07_DATITO/
│   │   ├── curriculum.yaml       ← DUPLICADO (mismo archivo)
│   │   ├── clases.yaml           ← DUPLICADO
│   │   ├── visual/               ← COPIA de directorios
│   │   └── ...
│
├── learners/                      ← NUEVA ESTRUCTURA (ADR-001)
│   └── cristobal_herrera_fcd-2026-2/
│       ├── progreso.yaml
│       ├── dudas.yaml            ← PROBLEMA: debería estar en learners/, pero...
│       └── ...
│
└── 03_SCRIPTS/
    ├── context_manager.py        ← NUEVO (fase 1, no probado)
    ├── datito_estado.py          ← MODIFICADO (usa context_manager)
    └── ... (múltiples scripts aún con rutas hardcodeadas)
```

### 1.2 Fuentes Identificadas

| Fuente | Accesible | Contenido | Estado |
|--------|-----------|-----------|--------|
| **F:\MACI** | ✅ Sí | Desarrollo actual, cursos, code | Desordenado |
| **G:\MACI** | ✅ Sí | 4 carpetas de cursos + materiales | No inventariado |
| **Drive** | ❌ No | Mencionado en instrucción | No accesible aquí |

### 1.3 Cursos Reales Identificados

| Curso | Ubicación | Materiales | Observaciones |
|-------|-----------|-----------|---|
| **Fundamentos de Ciencia de Datos** | F:\MACI (7_DATITO + courses/fcd-2026-2) + G:\MACI | 21 conceptos, visuales, prácticos, certamenes | ✅ Ampliamente documentado |
| **Fundamentos de Bases de Datos** | G:\MACI/Fundamentos de bases de datos | Videos de clases (6 cápsulas) | ⚠️ Solo video, sin curriculum definido |
| **Python** | G:\MACI/Python | Ejercicios locales, ejemplo_env.py | ⚠️ Estructura incompleta |
| **Emprendimiento e Innovación** | G:\MACI/Emprendimiento e innovación | Taller PDF | ⚠️ Mínimo contenido |
| **Liderazgo** | ? | No encontrado en F:\ ni G:\ | ❌ Mencionado pero no localizado |

---

## 2. PROBLEMAS CRITICOS ENCONTRADOS

### 2.1 Duplicación Canónica (Violación Arquitectónica)

**Problema:** El mismo archivo existe en múltiples ubicaciones:

```
curriculum.yaml:
  ✗ 07_DATITO/curriculum.yaml (original)
  ✗ courses/fcd-2026-2/curriculum.yaml (copia de ADR-001)
  ✗ courses/_template/curriculum.yaml (plantilla)

clases.yaml:
  ✗ 07_DATITO/clases.yaml (original)
  ✗ courses/fcd-2026-2/clases.yaml (copia)

visual/:
  ✗ 07_DATITO/visual/ (original con 21 HTMLs)
  ✗ courses/fcd-2026-2/visual/ (copia de los 21 HTMLs)
```

**Impacto:** 
- Scripts leen de ubicaciones inconsistentes
- Cambios en uno no se replican en otro
- No hay una sola verdad

### 2.2 Contexto Manager NO Probado

**Cambio:** Creé `context_manager.py` en fase anterior.  
**Problema:** NO se integró con scripts existentes ni se verificó en ejecución.

```bash
# Lo que DEBERÍA funcionar pero no:
python 03_SCRIPTS/context_manager.py --course fcd-2026-2 --learner juan
# Resultado esperado: "✅ Contexto válido"
# Resultado real: ??? (no verificado)
```

**Efecto:** Scripts posteriores (datito_estado.py, construir_navegacion.py) aún contienen fallbacks hardcodeados.

### 2.3 Nombres Inconsistentes

**Cambio anterior:** Cambié "Guillito" → "Datito"  
**Problema:** Cambio incompleto en múltiples archivos:

| Archivo | Referencia | Estado |
|---------|-----------|--------|
| README.md | "Guillito" | ❌ Aún dice Guillito (línea 8, 146, etc.) |
| CLAUDE.md | ? | No verificado |
| skills/ | ? | No verificado |
| 07_DATITO/00_LEEME.md | "Datito" | ✅ Actualizado |
| courses/_template/README.md | "Datito" | ✅ Actualizado |

**Consecuencia:** El proyecto no tiene identidad consistente.

### 2.4 Perfil Original de Cristóbal

**Afirmación anterior:** "Conservado sin pérdida de progreso"  
**Realidad:**

```
learners/
  cristobal_herrera_fcd-2026-2/  ← NOMBRE NUEVO (concatenado)
    progreso.yaml              ← Archivo movido desde 07_DATITO
    bitacora/                  ← Directorio movido
```

**Problema:** 
- Nombre cambió de `cristobal_herrera` a `cristobal_herrera_fcd-2026-2`
- `CLAUDE.md` aún referencia Cristóbal sin sufijo de curso
- `datito.config.yaml` está en `07_DATITO/` no en `learners/`

### 2.5 Dudas Personales Aún Compartidas

**Afirmación anterior:** "Separar dudas a learners/ está pendiente"  
**Realidad:**

```
courses/fcd-2026-2/
  dudas.yaml          ← ESTÁ AQUÍ (compartido)

learners/cristobal_herrera_fcd-2026-2/
  dudas.yaml          ← COPIADO AQUÍ (duplicado)
```

**Problema:** Tanto en lugar "compartido" como en "privado" → confusión de autoridad.

### 2.6 Scripts con Rutas Hardcodeadas

Cambio anterior dijo "actualizar scripts" pero verifi:

```python
# 03_SCRIPTS/construir_navegacion.py (línea 193)
RUTAS = resolver_rutas(cargar_config())

# Problema: cargar_config() busca en 07_DATITO/
# No usa context_manager
# Si cambias de curso, sigue usando paths de FCD
```

---

## 3. AFIRMACIONES PREVIAS FALSAS O INCOMPLETAS

| Afirmación | Realidad | Verificación |
|-----------|----------|---|
| "Context Manager centralizado ✅" | Existe código pero NO integrado con scripts | ❌ Test falla |
| "datito_estado.py usa context_manager ✅" | Código reescrito pero NO probado | ⚠️ Teórico |
| "No hereda datos personales ✅" | datito_init_learner.py modificado pero NO probado | ⚠️ Teórico |
| "Garantías G1–G14 preservadas ✅" | Verificadas contra spec.md, no contra ejecución | ⚠️ Estática |
| "60% implementado" | Sobreestimación. Más como 20% funcional. | ❌ Falso |

---

## 4. ESTRUCTURA CORRECTA REQUERIDA

Según instrucción, el modelo debe ser:

```
MACI/
  README.md
  docs/
  programs/
    <program-id>/
      program.yaml          ← Define asignaturas
      README.md
  courses/
    <course-id>/           ← Ubicación única
      course.yaml
      curriculum.yaml
      clases.yaml
      fuentes/
      materiales/
      actividades/
      visual/
  learners/
    <learner-id>/          ← Identidad del estudiante
      profile.yaml
      courses/
        <course-id>/       ← Progreso por curso (aislado)
          progreso.yaml
          dudas.yaml
          bitacora/
          proyectos/
          entregas/
  datito/                   ← Motor reutilizable
  scripts/
  tests/
  private/
    expedientes/
  archive/
```

**Diferencia clave:**
- Actual: `learners/cristobal_herrera_fcd-2026-2/progreso.yaml`
- Correcta: `learners/cristobal_herrera/courses/fcd-2026-2/progreso.yaml`

---

## 5. INVENTARIO REAL PENDIENTE

### G:\MACI Identificado Pero No Catalogado

```
Fundamentos de Ciencia de datos/
  → Certamen2_Respuestas_Finales.docx/pdf (personal)
  → Imágenes de respuestas (personal)
  
Fundamentos de bases de datos/
  → 6 cápsulas de video
  → Sin curriculum definido aún

Python/
  → clase_27_03/ (directorio)
  → Ejercicios/ (directorio)
  → ejemplo_env.py

Emprendimiento e innovación/
  → Taller 3 - Emp. Tec - 2026.pdf (1 archivo)
```

### Drive No Accesible

El usuario menciona Google Drive pero este entorno no tiene acceso.  
Necesario: **Usuario debe proporcionar índice o rutas**.

---

## 6. MIGRACIÓN NECESARIA (Alto Nivel)

### Fase 1: Preparación
- [ ] Inventariar todas las fuentes (F:\, G:\, Drive)
- [ ] Calcular hashes de duplicados
- [ ] Identificar todos los cursos reales
- [ ] Identificar contenido personal vs. compartido

### Fase 2: Diseño
- [ ] Crear schema definitivo (program.yaml, course.yaml, profile.yaml)
- [ ] Mapear origen → destino con evidencia
- [ ] Identificar conflictos y referencias rotas

### Fase 3: Ejecución
- [ ] Crear estructura nueva sin tocar originales
- [ ] Copiar con trazabilidad (hashes, manifiestos)
- [ ] Actualizar scripts con nuevas rutas
- [ ] Validar que workflows anteriores sigan funcionando

### Fase 4: Validación
- [ ] Pruebas de aislamiento (2 estudiantes)
- [ ] Pruebas de multi-curso (1 estudiante en 2 cursos)
- [ ] Verificación de no duplicación
- [ ] Verificación de no pérdida de progreso

---

## 7. LISTA DE ACCIONES INMEDIATAS

### Sí, Hacer Ahora
1. Detener cambios experimentales hasta que estructura sea clara
2. Inventariar G:\MACI en detalle
3. Solicitar índice de Drive al usuario
4. Crear catálogo de "origen → destino" con hashes

### No, Esperar
- ✗ Más cambios a scripts (hasta que rutas sean claras)
- ✗ Nuevas migrations (riesgosas con estructura actual)
- ✗ "Pruebas" de isolation (hasta que context manager funcione)

---

## Conclusión

La fase anterior fue **20% teórica, 80% documentación no verificada**. Afirmé "60% completo" pero el código:

- No está integrado
- No fue probado
- Introduce duplicados canónicos
- Deja scripts con hardcodes

**Siguiendo la instrucción del usuario, la prioridad correcta es:**

1. ✅ Comprueba el estado real (HECHO - este documento)
2. 🚧 Inventaría todas las fuentes (G:\, Drive)
3. 🚧 Diseña migración clara
4. 🚧 Ejecuta sin perder trazabilidad
5. 🚧 Valida workflows

**No continuar con transformación a plataforma abierta hasta que MACI tenga base sólida.**
