# MACI — Máquina Asistida de Ciencia de Datos Interactiva

**MACI** es un sistema de **tutoría interactiva** en Fundamentos de Ciencia de Datos (FCD) diseñado para estudiantes de la Universidad de Concepción.

## 🎯 Qué es MACI

- **Tutor personalizado** que enseña conceptos de ciencia de datos paso a paso
- **Loop socrático** que espera respuesta del estudiante antes de continuar
- **Visuales interactivos** (sin conexión) para aprender gráficas, matrices, ROC curves
- **Certámenes autocorregibles** con explicaciones detalladas
- **Learning loop** que captura errores y mejora el material

## 📂 Estructura del Proyecto

```
MACI/
├── 01_CONCEPTOS/         # 19 conceptos (fundamentos → deep learning)
│   └── visual/           # HTMLs interactivos (template canónico v1)
├── 02_DATOS/             # Datasets del curso (Melbourne housing, etc)
├── 03_CODIGO/            # Scripts (EDA, modelos, verificación)
├── 04_EJERCICIOS/        # Certámenes 1-3 + simuladores
├── 05_CLASES/            # Transcripciones de clases
├── 07_DATITO/            # Sistema de tutoría
│   ├── 01_CONCEPTOS/visual/ → Conceptos interactivos
│   ├── 04_EJERCICIOS/       → Certámenes
│   └── 07_BITACORA/         → Learning loop + lecciones
└── 08_PROYECTO_FCD/      # Proyecto final (predicción precios)
```

## 🏗️ Arquitectura de Datito (Tutor IA)

**3 loops de aprendizaje:**

1. **Loop 1: Alumno** → Cristóbal aprende ciencia de datos
2. **Loop 2: Tutor→Alumno** → Datito explica, detecta errores conceptuales
3. **Loop 3: Agente→Datito** → Sistema de construcción aprende de fallos de visuales

**Componentes:**

| Componente | Ruta | Propósito |
|---|---|---|
| **Template Canónico v1** | `07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html` | Único diseño permitido (sin CDN) |
| **Skill /datito-visual** | `.claude/skills/datito-visual/SKILL.md` | Genera visuales HTML interactivos |
| **Skill /datito-loop** | `.claude/skills/datito-loop/SKILL.md` | Learning loop: keep/discard decisiones |
| **Evaluador** | `03_CODIGO/datito_loop_eval.py` | Valida 11 gates (template, anti-CDN, etc) |
| **Lecciones** | `07_DATITO/07_BITACORA/learning_loop/agent_lessons.yaml` | VIZ-FAIL-001, VIZ-FAIL-002, etc |

## ✅ Estado Actual (2026-09-25)

### Completado
- ✅ Certamen 3 (6 preguntas, estructura pedagógica completa)
- ✅ Learning loop documentado (3 fases de migración)
- ✅ Template canónico v1 establecido
- ✅ Scripts de evaluación y migración

### En Progreso
- 📋 Fase 2: Migración de 17 conceptos (01_fundamentos → 19_deep_learning)
- 📋 Fase 3: Ejercicios + referencias

### Status Migración a Template v1
- **KEEP:** 1/24 (Certamen 3 principal)
- **DISCARD:** 23/24 (necesitan migración iterativa)
- **Plan:** `07_DATITO/07_BITACORA/PLAN_MIGRACION_GLOBAL.md`

## 🚀 Cómo Continuar

### Migrar Conceptos (Fase 2)
```bash
# Generar base desde template canónico
python 03_CODIGO/datito_migracion_inicio.py --archivo 03_eda.html

# Editar archivo_NEW.html manualmente (copiar contenido pedagógico)

# Evaluar
python 03_CODIGO/datito_loop_eval.py --path 07_DATITO/01_CONCEPTOS/visual/archivo_NEW.html

# Si score=1.0: Loguear y reemplazar
python 03_CODIGO/datito_loop_once.py --path … --hypothesis "migrate to template v1"
mv archivo_NEW.html archivo.html
```

### Auditoría Batch
```bash
python 03_CODIGO/datito_batch_eval.py  # Ver status de todos los 24 HTML
```

## 📖 Para Estudiantes (Cristóbal)

### Estudiar un Concepto
```bash
# Abrir en navegador
file:///F:/MACI/07_DATITO/01_CONCEPTOS/visual/03_eda.html
# (Sin conexión — todo local)

# Leer explicación → detalles → respuesta correcta → checklist
```

### Hacer un Certamen
```bash
file:///F:/MACI/07_DATITO/04_EJERCICIOS/certamen_3.html
# (6 preguntas, desglosadas en 11 subpreguntas)
# Estructura: Qué pasó + Pasos + Details + Respuesta + Errores + Checklist
```

### Usar Datito (Tutor Interactivo)
```bash
/datito                 # Sesión socrática interactiva
/datito-visual <tema>   # Generar visual HTML
/datito-loop            # Iterar si visual falló
```

## 📝 Reglas del Juego (Learning Loop)

### Prohibido
❌ CDN (Chart.js, fonts.google)  
❌ Colores IA (#667eea, #764ba2)  
❌ CSS inventado  
❌ Declarar "listo" sin score=1.0  

### Obligatorio
✅ Template canónico v1 (`<!-- datito:template:v1 -->`)  
✅ Estructura pedagógica (Qué pasó + Pasos + Details.resp + Errores)  
✅ Canvas/SVG local (sin red)  
✅ Cada gate debe pasar  

## 🔗 GitHub

**Repositorio:** https://github.com/cherrera0001/MACI  
**Rama:** main  
**Auth:** GITHUB_TOKEN_CLASSIC en `.env`

### Qué Pushear
```bash
git add -A
git commit -m "Migrate Datito to template v1 + Certamen 3"
git push origin main
```

**NO incluir en .gitignore:**
- `07_DATITO/**/*.html` (material de aprendizaje)
- `03_CODIGO/datito_*.py` (scripts de automatización)

**Sí ignorar:**
- `.env` (credenciales)
- `02_DATOS/*.csv` (grandes)
- `__pycache__/`

## 📊 Próximos Hitos

1. **Fase 2:** Conceptos core (01_fundamentos, 03_eda, 08_overfitting, 13_roc) → score 1.0
2. **Fase 3:** Ejercicios + referencias → score 1.0
3. **Unificación:** Todos 24 HTML en template v1, navegación regenerada
4. **Push a GitHub:** Rama main con material completo

## 📚 Referencias Internas

- **Plan estratégico:** `07_DATITO/07_BITACORA/PLAN_MIGRACION_GLOBAL.md`
- **Status actual:** `07_DATITO/MIGRACION_STATUS_2026_09_25.md`
- **Workflow:** `07_DATITO/07_BITACORA/learning_loop/WORKFLOW_VISUAL.md`
- **Protocolo:** `07_DATITO/07_BITACORA/learning_loop/program_loop.md`
- **Lecciones:** `07_DATITO/07_BITACORA/learning_loop/agent_lessons.yaml`

---

**Creado:** 2026-09-25  
**Mantenedor:** Cristóbal Herrera + Claude Code  
**Última actualización:** Fase 1 ✅ | Fase 2-3 en marcha

