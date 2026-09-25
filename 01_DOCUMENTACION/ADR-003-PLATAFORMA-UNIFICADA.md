# ADR-003: Plataforma Unificada (NO Migración Destructiva)

**Estado:** PROPUESTA (sin implementar)  
**Decisión:** Arquitectura de 3 capas sin destruir lo existente  
**Reversibilidad:** 100% (legacy en 10_ARCHIVO/)

---

## CONTEXTO

Hoy: 7 scripts clonados, 3 productos mezclados (FCD + Datito + Canvas), mentiras en README.

Mañana: Una CLI, un README coherente, escalable a N cursos sin clonar.

---

## OPCIÓN DESCARTADA: Full Rewrite
❌ Destruir 01-07_DATITO (instancia FCD funcional)  
❌ Mover courses/ a otro sitio (usuario confundido)  
❌ Cloud multi-usuario (scope creep, 80-90h de trabajo)

---

## DECISIÓN: 3 Capas + Legacy Documented

### CAPA 1: Entry Point Unificado
```python
# F:\MACI\03_SCRIPTS\platform\__main__.py

from platform.cli import main

if __name__ == "__main__":
    main()

# Invocación:
# python -m platform process --course 80014
# python -m platform process --course 80038 --with-videos
# python -m platform status --course 80714
```

**Responsabilidad:** Despachar a subcomandos según course_id  
**No reescribe:** Lógica de procesar_80014.py, procesar_80038.py, etc.  
**Beneficio:** User abre LECTURA desde CLI, no busca script clonado

---

### CAPA 2: Course Manifesto (Data-Driven)
```yaml
# F:\MACI\03_SCRIPTS\platform\courses.yaml

courses:
  80014:
    name: "Emprendimiento Tecnológico"
    source: "canvas"
    state: "partial"      # capacidades reales
    has:
      videos: false       # no tenemos grabaciones aún
      notes: true         # SEMANA_1-6/NOTAS_*.md existe
      exercises: true     # SEMANA_1-6/EJERCICIO_*.md existe
      transcripts: false
      dashboard: false
    path: "courses/80014_Emprendimiento"
    
  80038:
    name: "Procesos de Innovación"
    source: "canvas"
    state: "partial"
    has:
      videos: true        # 5 .mp4 en 10_GRABACIÓN_CLASES/
      notes: true
      exercises: false
      transcripts: true
      dashboard: true
    path: "10_GRABACIÓN_CLASES/80038_Procesos_Innovacion"
    
  80714:
    name: "Fundamentos de BD"
    source: "canvas"
    state: "empty"        # honesto
    has:
      videos: false
      notes: false
      exercises: false
      transcripts: false
      dashboard: false
    path: "courses/80714_Fundamentos_BD"
    
  # … 83703, 83706, 83707

fcd-instance:           # NO es curso, es instancia
  name: "FCD-Cristobal"
  path: "01_DOCUMENTACION/"
  type: "semester-project"
  status: "stable"
```

**Responsabilidad:** Una fuente de verdad sobre qué existe/qué falta  
**No mueve:** Ningún archivo  
**Beneficio:** Matriz de capacidades auto-generada, sin mentiras

---

### CAPA 3: Directorio Coherente (Sin Mover)
```
F:\MACI/
├── 01_DOCUMENTACION/         [DATITO instance: FCD-Cristobal]
├── 08_PROYECTO_FCD/          [Semestral Cristóbal]
├── 03_SCRIPTS/
│   └── platform/             [⭐ NUEVO: CLI + manifesto]
│       ├── __main__.py
│       ├── cli.py
│       ├── courses.yaml
│       └── processors/
│           ├── canvas.py     [Orquesta procesar_*.py viejos]
│           └── datito.py     [Orquesta Datito cuando agregue cursos]
│
├── 02_DATOS/
├── 09_RESULTADOS/
├── 06_ENTREGABLES/
├── 07_DATITO/                [Core pedagógico, no tocado]
├── 06_LABORATORIOS/
├── 05_CLASES/
├── 10_GRABACIÓN_CLASES/      [Videos, permanece]
│   ├── 80038_Procesos_Innovacion/  [✅ procesado]
│   ├── 80014_Emprendimiento/       [preparado para vídeos]
│   └── (4 vacías)
│
├── courses/                  [Contenido Canvas, permanece]
│   ├── 80014_Emprendimiento/    [✅ ZIP integrado]
│   ├── 80038_Procesos_Innovacion/  [✅ videos + índices]
│   ├── 80714_Fundamentos_BD/    [estructura]
│   ├── 83703_Liderazgo/         [estructura]
│   ├── 83706_Prototipos/        [estructura]
│   └── 83707_Ciencias_Datos/    [estructura]
│
├── learners/                 [NUEVO: una carpeta por estudiante]
│   └── .gitkeep (placeholder)
│
├── 10_ARCHIVO/               [Legacy movido, no borrado]
│   ├── pipelines_legacy/
│   │   ├── procesar_80014.py    (moved from root)
│   │   ├── procesar_80038.py    (moved from root)
│   │   ├── procesar_curso_80714.py
│   │   ├── procesar_liderazgo.py
│   │   ├── procesar_prototipos.py
│   │   ├── actualizar_index_80014.py
│   │   ├── limpiar_nombres_80014.py
│   │   └── descargar_contenido.py
│   │
│   └── PROCESADO/            (moved from root, obsolete)
│       ├── README_LEGACY.md   [Explicar qué fue esto]
│       └── (contenido viejo)
│
├── MACI_RESPALDOS/           [Backup Canvas, sin tocar]
│   └── udec/2026-09-22-001/
│
├── README.md                 [Reescrito, sección "3 productos"]
├── courses.yaml              [Manifesto central]
└── INDEX_MAESTRO.md          [Actualizado con matriz]
```

**Cambios:**
- ➕ Agregado: 03_SCRIPTS/platform/
- ➕ Agregado: learners/
- 🚚 Movido: 7 scripts a 10_ARCHIVO/pipelines_legacy/
- 🚚 Movido: PROCESADO/ a 10_ARCHIVO/
- ✏️ Actualizado: README, INDEX_MAESTRO
- 🚫 No tocado: 01-07_*, courses/*, 10_GRABACIÓN_*, MACI_RESPALDOS/

---

## FLUJO NUEVO

### Usuario quiere procesar un curso
**Hoy:**
```bash
# ¿Cuál script? Busca en raíz, confusión.
python procesar_80014.py          # Requiere git + python path
python procesar_80038.py          # Cada uno tiene su config
```

**Mañana:**
```bash
cd F:\MACI
python -m platform process --course 80014
# ↓
# Lee courses.yaml
# ↓
# Despacha a platform/processors/canvas.py
# ↓
# Llama procesar_80014.py (now in 99_ARCHIVE) sin cambios
# ↓
# Actualiza courses.yaml con capacidades reales
```

---

## IMPLEMENTACIÓN FASE 0 (Mínima, ~4h)

### 1. Crear 03_SCRIPTS/platform/
```
platform/
├── __init__.py
├── __main__.py                [Entry point: python -m platform <cmd>]
├── cli.py                     [Click CLI: process, status, report]
├── courses.yaml               [Manifesto centralizado]
├── processors/
│   ├── __init__.py
│   ├── canvas.py              [Orquesta procesar_*.py viejos]
│   └── datito.py              [Para futuro: agregar cursos a Datito]
└── utils/
    └── manifest.py            [Leer/escribir courses.yaml]
```

### 2. Mover scripts legacy
```bash
mkdir -p 10_ARCHIVO/pipelines_legacy
mv procesar_*.py 10_ARCHIVO/pipelines_legacy/
mv actualizar_*.py actualizar_index_80014.py  # (etc)
mv limpiar_*.py 10_ARCHIVO/pipelines_legacy/
mv PROCESADO/ 10_ARCHIVO/

# Crear 10_ARCHIVO/pipelines_legacy/README.md:
# "Scripts clonados pre-arquitectura. Orquestados por 03_SCRIPTS/platform/cli.py"
```

### 3. Reescribir 03_SCRIPTS/platform/__main__.py
```python
import click
from platform.cli import process_course, report_status

@click.group()
def main():
    pass

@main.command()
@click.option('--course', required=True, help='Course ID: 80014, 80038, ...')
@click.option('--with-videos', is_flag=True)
def process(course, with_videos):
    """Process a course (run procesar_<id>.py via manifest)"""
    from platform.processors.canvas import process_course_by_manifest
    process_course_by_manifest(course, with_videos)

@main.command()
def report():
    """Generate capability matrix (for README)"""
    from platform.manifest import load_manifest
    manifest = load_manifest()
    # Output: course_matrix.csv
    print(manifest.to_table())

if __name__ == '__main__':
    main()
```

### 4. Crear courses.yaml (manifesto)
```yaml
# F:\MACI\courses.yaml
courses:
  80014:
    id: 80014
    name: "Emprendimiento Tecnológico"
    source_type: "canvas"
    path: "courses/80014_Emprendimiento"
    capabilities:
      videos: false
      notes: true          # 6 NOTAS_SEMANA_*.md
      exercises: true      # 6 EJERCICIO_SEMANA_*.md
      transcripts: false
      dashboard: false
    processor_script: "10_ARCHIVO/pipelines_legacy/procesar_80014.py"
    last_processed: "2026-09-22T21:16:00Z"
    
  80038:
    id: 80038
    name: "Procesos de Innovación"
    source_type: "canvas"
    path: "10_GRABACIÓN_CLASES/80038_Procesos_Innovacion"
    capabilities:
      videos: true         # 5 .mp4 grabadas
      notes: true          # 5 NOTAS_*.md
      exercises: false
      transcripts: true
      dashboard: true
    processor_script: "10_ARCHIVO/pipelines_legacy/procesar_80038.py"
    last_processed: "2026-09-22T21:18:00Z"

  # (80714, 83703, 83706, 83707: state="empty", no processor_script yet)

datito_instance:
  name: "fcd-cristobal"
  type: "semester-project"
  path: "01_DOCUMENTACION"
  status: "stable"
  note: "Instance of Datito pedagogy. Do not modify. See 07_DATITO/spec.md"
```

### 5. Actualizar README.md
```markdown
# MACI — Fundamentos de Ciencia de Datos (UdeC, T2-2026)

## ¿Qué abrir para qué?

### 📚 Estudiar FCD con Datito (Cristóbal)
→ `01_DOCUMENTACION/` + `07_DATITO/` (estable, no cambiar)

### 📥 Ingerir un Curso Canvas
→ `python -m platform process --course <id>`
→ Resultado: `courses/<id>/` o `10_GRABACIÓN_CLASES/<id>/`

### 👤 Crear Nuevo Estudiante (Futuro)
→ `learners/<id>/`  (no implementado aún)

---

## Capacidades Reales por Curso

| ID | Nombre | Videos | Notas | Ejercicios | Transcripciones | Dashboard |
|----|--------|--------|-------|------------|-----------------|-----------|
| 80014 | Emprendimiento | ❌ | ✅ (6) | ✅ (6) | ❌ | ❌ |
| 80038 | Proc. Innovación | ✅ (5) | ✅ (5) | ❌ | ✅ | ✅ |
| 80714 | Fundamentos BD | ❌ | ❌ | ❌ | ❌ | ❌ |
| 83703 | Liderazgo | ❌ | ❌ | ❌ | ❌ | ❌ |
| 83706 | Prototipos | ❌ | ❌ | ❌ | ❌ | ❌ |
| 83707 | Ciencias Datos | ❌ | ❌ | ❌ | ❌ | ❌ |

**Progreso:** 2/6 = 33% (no 100%, no "OPERACIONAL")

---

[resto del README actualizado honestamente]
```

### 6. Reescribir ESTADO_PROYECTO_FINAL.txt
```
ESTADO ACTUAL — Septiembre 2026

VEREDICTO: NO_PLATAFORMA → EN_CONSTRUCCIÓN

HECHO:
✅ Respaldo Canvas verificado (155 archivos + auditoría)
✅ Instancia FCD estable (01-07_*)
✅ 2/6 cursos parcialmente procesados (80038, 80014)
✅ Datito prototipo funcional

FALTA:
❌ CLI unificada (7 scripts clonados)
❌ Learner tracking (directorio vacío)
❌ 4 cursos sin procesamiento
❌ Evaluación automática

PRÓXIMA FASE: ADR-003 (Unificación de CLI)
Estimado: 1 semana
```

---

## PROTECCIONES (NO cambiar)

```
Prohibido mover/renombrar:
  - 01_DOCUMENTACION/ (instancia FCD)
  - 08_PROYECTO_FCD/ (semestral)
  - 07_DATITO/ (core pedagógico)
  - MACI_RESPALDOS/ (backup)

Prohibido editar:
  - 07_DATITO/spec.md (educación)
  - .env (credenciales)

Permitido crear:
  - 03_SCRIPTS/platform/ (nueva)
  - 10_ARCHIVO/pipelines_legacy/ (reorganización)
  - learners/ (placeholder)
```

---

## REVERSIBILIDAD

Si todo falla:
```bash
# Restaurar:
git checkout HEAD -- F:\MACI\README.md
git checkout HEAD -- F:\MACI\INDEX_MAESTRO.md
rm -rf 03_SCRIPTS/platform/
mv 10_ARCHIVO/pipelines_legacy/* .
mv 10_ARCHIVO/PROCESADO ./

# Vuelves al estado anterior en 2 minutos
```

---

## CRITERIOS DE ÉXITO (FASE 0)

✅ `python -m platform process --course 80014` funciona sin errores  
✅ `python -m platform report` genera matriz sin mentiras  
✅ README explica qué abrir para qué en <60 segundos de lectura  
✅ 0 scripts procesar_* en la raíz (todos en 10_ARCHIVO/pipelines_legacy/)  
✅ courses.yaml es fuente única de verdad sobre capacidades  
✅ Un tercero entiende que esto NO ES plataforma aún, es contenido + protocolo

