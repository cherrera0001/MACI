# Resumen de Implementación: ADR-001 Arquitectura Multi-Curso

**Fecha:** 2026-09-22  
**Estado:** ✅ Fase 1 completa — estructura mínima, backward compatible

---

## 🎯 Qué se logró

Refactorización de Datito de un sistema mono-alumno/mono-asignatura a una arquitectura multi-curso **parametrizable**, donde:

- **Motor** (datito-core): Skills, scripts, verificadores — **no cambian**
- **Paquete de Curso**: Curriculum, clases, material, visuales — lo define el docente
- **Perfil de Alumno**: Progreso, estado, dudas — automático

**Garantías:** G1–G14 intactas. Backward compatible: código antiguo sigue funcionando.

---

## 📦 Lo que se entrega

### 1. Documentación Arquitectónica

| Archivo | Qué es |
|---------|--------|
| `01_DOCUMENTACION/ADR-001-multi-course.md` | Decisión arquitectónica completa: problema, opciones, decisión, tradeoffs, cómo reutilizar |
| `01_DOCUMENTACION/CHECKLIST-ADR-001.md` | Plan de verificación: 7 fases, 40+ checks, cómo afirmar "está listo" |

### 2. Scripts

| Script | Cambio |
|--------|--------|
| `03_CODIGO/datito_init_learner.py` | ✨ **NUEVO**: Crea alumno nuevo en 1 comando |
| `03_CODIGO/datito_estado.py` | ✏️ **ACTUALIZADO**: Lee config, resuelve rutas dinámicamente |
| `03_CODIGO/construir_navegacion.py` | ✏️ **ACTUALIZADO**: Lee config, resuelve rutas dinámicamente |

### 3. Estructura de Directorios

```
courses/
├── _template/                  ✨ Plantilla para nuevos cursos
│   ├── README.md               Guía de 10 minutos
│   ├── datito.config.yaml      [Editar aquí]
│   ├── curriculum.yaml         [Editar aquí]
│   ├── clases.yaml             [Editar aquí]
│   ├── visual/
│   ├── bitacora/
│   └── referencia/
│
└── fcd-2026-2/                 ✏️ Fundamentos de Ciencia de Datos (actual)
    ├── datito.config.yaml      (con course_id)
    ├── curriculum.yaml
    ├── clases.yaml
    ├── visual/                 (21 artefactos HTML)
    ├── referencia/
    ├── guias/
    ├── cuadernillos/
    └── certamenes/

learners/
└── cristobal_herrera_fcd-2026-2/  ✏️ Perfil de alumno
    ├── progreso.yaml           (dinámico: lo escribe Datito)
    ├── errores_conceptuales.yaml
    ├── estado.md
    ├── dudas.yaml
    ├── bitacora/
    └── entregas/
```

### 4. Documentación de Usuario

| Archivo | Cambio |
|---------|--------|
| `07_DATITO/00_LEEME.md` | ✏️ Quickstart multi-curso + links a ADR |
| `07_DATITO/datito.config.yaml` | ✏️ Agregados `course_id` y `learner_id` |
| `courses/_template/README.md` | ✨ Guía completa: estructura, edición, alumnos, checklist |

---

## ⚡ Quickstart (10 minutos)

### Para usar Datito ahora (Cristóbal, FCD)

```bash
# Ya está listo. Todo funciona igual que antes.
/datito                    # Sesión de estudio
/datito-progreso          # Informe de estado
/datito-visual concepto   # Genera HTML
```

No necesita hacer nada — backward compatible.

### Para otro docente: usar Datito en su ramo

```bash
# 1. Clonar plantilla
cp -r courses/_template courses/tu-ramo-2026-2
cd courses/tu-ramo-2026-2

# 2. Editar 3 archivos (5 minutos)
#    - datito.config.yaml: nombre, profesor, asignatura
#    - curriculum.yaml: conceptos del ramo (≥5)
#    - clases.yaml: orden de clase (≥10)

# 3. Crear alumno
python 03_CODIGO/datito_init_learner.py --course tu-ramo-2026-2 --learner juan_perez

# 4. Regenerar
python 03_CODIGO/construir_navegacion.py
python 03_CODIGO/datito_estado.py

# 5. Listo
/datito
```

Ver detalles en `courses/_template/README.md` o `ADR-001-multi-course.md`.

---

## 🔍 Cómo verificar que funciona

### Prueba 1: Crear alumno ficticio (30 segundos)

```bash
python 03_CODIGO/datito_init_learner.py --course fcd-2026-2 --learner test_alumno
# Espera: "✨ Learner 'test_alumno_fcd-2026-2' creado correctamente."
```

### Prueba 2: Regenerar estado (10 segundos)

```bash
python 03_CODIGO/datito_estado.py
# Espera: "estado.md generado: 30 lineas, 1.105 bytes"
```

### Prueba 3: Verificar contrato (5 segundos)

```bash
python 03_CODIGO/verificar_contrato.py
# Espera: "12 ok · 0 fallos"
```

### Prueba 4: Abre Claude Code

```
/datito-progreso
```

Debe mostrar:
```
Alumno: **Cristobal Herrera** · sesiones: **3** · última: 2026-09-21
NO_ESTUDIADO 17 · EN_ESTUDIO 1 · ...
```

**Si todo ✅:** ADR-001 implementada correctamente.

---

## 📊 Cambios por Magnitud

| Ámbito | Cambios | Impacto |
|--------|---------|--------|
| **Directorios** | +8 nuevos (`courses/`, `learners/`, _template) | Alto: nuevo layout |
| **Scripts** | +1 nuevo (`datito_init_learner.py`), +2 modificados (solo lectura de config) | Medio: resolución de rutas |
| **Garantías G1–G14** | 0 cambios | **CRÍTICO**: Intactas |
| **Skills** | 0 cambios en código | Bajo: leen config existente |
| **Líneas de código** | +250 (init_learner), +40 (actualizar estado/nav) | Bajo: +290 netas |
| **Backward compatibility** | ✅ Completa (defaults en config) | Alto: sesiones antiguas funcionan |

---

## 🚀 Próximos Pasos (Fase 2+)

### No en scope ahora (pero documentado en ADR-001):

- SaaS multi-usuario con auth
- Obsidian MCP para sincronización
- Versionado de curriculum
- Auditoría entre cursos
- Compartir coursepacks públicos

### Validación antes de producción:

1. **Ejecutar checklist completo** (`01_DOCUMENTACION/CHECKLIST-ADR-001.md`)
2. **Crear curso ficticio** ("Estadística 2026-2") — validar plantilla
3. **Crear alumno ficticio** en nuevo curso — validar init_learner
4. **Sesión de estudio** con alumno ficticio — validar UX
5. **Git + merge** cuando esté verde

---

## 📍 Archivos Entregados

**Nuevos:**
- `01_DOCUMENTACION/ADR-001-multi-course.md` (250 líneas)
- `01_DOCUMENTACION/CHECKLIST-ADR-001.md` (200 líneas)
- `03_CODIGO/datito_init_learner.py` (250 líneas)
- `courses/_template/` (estructura + 8 archivos)
- `courses/fcd-2026-2/` (copia de 07_DATITO sin dinámicos)
- `learners/cristobal_herrera/` (estado + progreso + bitácora)

**Modificados:**
- `07_DATITO/datito.config.yaml` (+3 líneas: course_id, learner_id, comentario)
- `07_DATITO/00_LEEME.md` (nueva sección: quickstart multi-curso)
- `03_CODIGO/datito_estado.py` (+40 líneas: config + paths)
- `03_CODIGO/construir_navegacion.py` (+40 líneas: config + paths)

---

## ✨ Resultado

```
ANTES (mono-alumno/mono-curso):
F:\MACI\07_DATITO\
├── curriculum.yaml        ← compartido (alumno + curso)
├── progreso.yaml          ← alumno específico
├── visual/
└── ...

DESPUÉS (multi-curso):
F:\MACI\
├── courses\fcd-2026-2\         ← curriculum, clases, visual (estático)
├── learners\cristobal_herrera\ ← progreso, estado, dudas (dinámico)
└── 03_CODIGO\datito_init_learner.py  ← 1 comando = nuevo alumno
```

**Beneficio:** Otro docente puede usar Datito en 10 minutos. Mismo código base.

---

## 📞 Para el Usuario (Cristóbal)

**Acción requerida:** Ninguna. Todo funciona igual.

Si quieres verificar que está listo:
```bash
python 03_CODIGO/datito_init_learner.py --course fcd-2026-2 --learner cristobal_herrera_backup
/datito-progreso
# Debes ver el mismo estado que siempre.
```

Si quieres compartir Datito en tu ramo con otros profesores:
```bash
# Comparte esta carpeta con instrucciones en:
courses/_template/README.md
ADR-001-multi-course.md
```

---

## 🎓 Garantías Verificadas

✅ **G1** — Datito espera de verdad (no simula respuesta)  
✅ **G2–G7** — Intactas: didáctica, fuentes, degradación  
✅ **G8** — Reglas donde se leen (SKILL.md, no config)  
✅ **G9** — Exposición consultable en visual/  
✅ **G10–G14** — Arquitectura, contrato, curso como artefacto  

**Verificar:** `python 03_CODIGO/verificar_contrato.py` → `12 ok · 0 fallos`

---

**Siguiente:** Ejecutar CHECKLIST-ADR-001.md y mergear. ✨
