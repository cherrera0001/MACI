# FASE 0: Implementación Mínima (1 Semana)

**Objetivo:** CLI unificada + honestidad en README  
**Scope:** Sin migración destructiva, sin nuevo código pedagógico  
**Estimado:** 40 horas (5 días, full-time)

---

## CHECKLIST DE IMPLEMENTACIÓN

### DÍA 1: Estructura Base (8h)

- [ ] Crear `03_SCRIPTS/platform/` (nuevo directorio)
  ```bash
  mkdir -p 03_SCRIPTS/platform/
  mkdir -p 03_SCRIPTS/platform/processors
  mkdir -p 03_SCRIPTS/platform/utils
  ```

- [ ] Crear `03_SCRIPTS/platform/__init__.py`
  ```python
  __version__ = "0.1.0"
  ```

- [ ] Crear `03_SCRIPTS/platform/__main__.py` (entry point)
  ```python
  import sys
  from platform.cli import main
  
  if __name__ == "__main__":
      sys.exit(main())
  ```

- [ ] Crear `03_SCRIPTS/platform/cli.py` (Click CLI)
  ```python
  import click
  from pathlib import Path
  
  @click.group()
  def main():
      """MACI platform CLI — unified entry point"""
      pass
  
  @main.command()
  @click.option('--course', required=True, help='Course ID: 80014, 80038, ...')
  @click.option('--with-videos', is_flag=True, help='Process videos if available')
  def process(course, with_videos):
      """Process a course (Canvas, Datito, or custom)"""
      from platform.processors.canvas import process_course
      process_course(course, with_videos)
  
  @main.command()
  def status():
      """Show course processing status"""
      from platform.manifest import load_manifest
      manifest = load_manifest()
      click.echo(manifest.to_table())
  
  @main.command()
  def report():
      """Generate capability matrix (for README)"""
      from platform.manifest import load_manifest
      manifest = load_manifest()
      # Output table of capabilities
      for course in manifest.courses:
          click.echo(f"{course.id}: {course.capabilities}")
  
  if __name__ == "__main__":
      main()
  ```

- [ ] Crear `03_SCRIPTS/platform/manifest.py` (YAML loader)
  ```python
  import yaml
  from pathlib import Path
  from dataclasses import dataclass
  
  @dataclass
  class CourseCapabilities:
      videos: bool
      notes: bool
      exercises: bool
      transcripts: bool
      dashboard: bool
  
  @dataclass
  class Course:
      id: int
      name: str
      path: str
      capabilities: CourseCapabilities
      last_processed: str
  
  class Manifest:
      def __init__(self, data):
          self.data = data
          self.courses = [Course(**c) for c in data['courses'].values()]
      
      def to_table(self):
          lines = []
          lines.append("| ID | Name | Videos | Notes | Exercises | Dashboard |")
          lines.append("|--|--|--|--|--|--|")
          for c in self.courses:
              lines.append(f"| {c.id} | {c.name} | "
                          f"{'✅' if c.capabilities.videos else '❌'} | "
                          f"{'✅' if c.capabilities.notes else '❌'} | ... |")
          return "\n".join(lines)
  
  def load_manifest():
      path = Path("courses.yaml")
      with open(path) as f:
          data = yaml.safe_load(f)
      return Manifest(data)
  ```

- [ ] Crear `courses.yaml` (manifesto central)
  **Copy from ADR-003 template**

---

### DÍA 2: Procesadores Legacy (8h)

- [ ] Crear `03_SCRIPTS/platform/processors/__init__.py`

- [ ] Crear `03_SCRIPTS/platform/processors/canvas.py`
  ```python
  import subprocess
  from pathlib import Path
  
  def process_course(course_id, with_videos=False):
      """Dispatch to legacy processor scripts"""
      
      # Map course_id to legacy script
      script_map = {
          80014: "10_ARCHIVO/pipelines_legacy/procesar_80014.py",
          80038: "10_ARCHIVO/pipelines_legacy/procesar_80038.py",
          80714: "10_ARCHIVO/pipelines_legacy/procesar_curso_80714.py",
          83703: "10_ARCHIVO/pipelines_legacy/procesar_liderazgo.py",
          83706: "10_ARCHIVO/pipelines_legacy/procesar_prototipos.py",
      }
      
      script = script_map.get(course_id)
      if not script:
          raise ValueError(f"Unknown course: {course_id}")
      
      # Run legacy script
      result = subprocess.run(["python", script], check=False)
      
      # Update manifest with new timestamp
      from platform.manifest import load_manifest
      manifest = load_manifest()
      course = next(c for c in manifest.courses if c.id == course_id)
      course.last_processed = datetime.now().isoformat()
      # Save manifest
      
      return result.returncode
  ```

---

### DÍA 3: Reorganización Física (8h)

- [ ] Crear `99_ARQUIVO/pipelines_legacy/` (nuevo directorio)
  ```bash
  mkdir -p 99_ARCHIVE/pipelines_legacy
  ```

- [ ] Mover scripts clonados (NO BORRAR, MOVER)
  ```bash
  # MOVER, no copiar, no borrar original
  git mv procesar_80014.py 99_ARCHIVE/pipelines_legacy/
  git mv procesar_80038.py 99_ARCHIVE/pipelines_legacy/
  git mv procesar_curso_80714.py 99_ARCHIVE/pipelines_legacy/
  git mv procesar_liderazgo.py 99_ARCHIVE/pipelines_legacy/
  git mv procesar_prototipos.py 99_ARCHIVE/pipelines_legacy/
  git mv actualizar_index_80014.py 99_ARCHIVE/pipelines_legacy/
  git mv limpiar_nombres_80014.py 99_ARCHIVE/pipelines_legacy/
  ```

- [ ] Mover `PROCESADO/` a legacy
  ```bash
  git mv PROCESADO/ 99_ARCHIVE/PROCESADO_legacy
  ```

- [ ] Crear `99_ARCHIVE/pipelines_legacy/README.md`
  ```markdown
  # Legacy Pipeline Scripts
  
  These scripts were used before platform/cli.py unification.
  
  They are still functional and called by 03_SCRIPTS/platform/processors/canvas.py.
  
  If you need to modify a processor:
  1. Edit the script here
  2. Test with: python -m platform process --course <id>
  3. Do NOT clone for new courses — add to courses.yaml instead
  ```

- [ ] Crear `99_ARCHIVE/PROCESADO_legacy/README.md`
  ```markdown
  # Old Processed Content (Pre-Architecture)
  
  This directory contains duplicates from courses/ before unified CLI.
  
  Use `courses/` for current content.
  ```

---

### DÍA 4: Actualizar Documentación (8h)

- [ ] Reescribir `README.md` (usa `README_ARQUITECTO.md` como base)
  - Sección: "Qué abrir para qué" (60 seg)
  - Sección: "Capacidades reales por curso" (matriz)
  - Sección: "Próxima fase: ADR-003"
  - Sección: "Protecciones (no tocar)"
  - Remover todas las mentiras ("100%", "OPERACIONAL", "plataforma")

- [ ] Actualizar `INDEX_MAESTRO.md`
  - Reemplazar "OPERACIONAL" con "PARCIAL (2/6)"
  - Agregar tabla de capacidades real
  - Referencia a courses.yaml como fuente de verdad

- [ ] Reescribir `ESTADO_PROYECTO_FINAL.txt`
  - Cambiar veredicto a: "NO_PLATAFORMA → EN_CONSTRUCCIÓN"
  - Agregar matriz de capacidades
  - Explicar próxima fase

- [ ] Crear `ARQUITECTURA.md`
  - Diagrama de 3 capas (entry, manifesto, processors)
  - Flujo de procesar un curso
  - Cómo agregar un nuevo curso sin clonar scripts

---

### DÍA 5: Testing + Commit (8h)

- [ ] Instalar Click
  ```bash
  pip install click pyyaml
  ```

- [ ] Test CLI
  ```bash
  # Test entry point
  python -m platform --help
  python -m platform status
  python -m platform report
  
  # Test course processing (sin modificar nada, solo llamar legacy)
  python -m platform process --course 80014
  ```

- [ ] Validation Checks
  - [ ] courses.yaml es YAML válido
  - [ ] Todos los paths en courses.yaml existen
  - [ ] README no tiene mentiras ("100%", "OPERACIONAL")
  - [ ] 0 scripts procesar_*.py en raíz (todos en 99_ARCHIVE/)

- [ ] Commit y push
  ```bash
  git add 03_SCRIPTS/platform/
  git add 99_ARCHIVE/pipelines_legacy/
  git add 99_ARCHIVE/PROCESADO_legacy/
  git add README.md
  git add INDEX_MAESTRO.md
  git add ESTADO_PROYECTO_FINAL.txt
  git add ARQUITECTURA.md
  git add courses.yaml
  
  git commit -m "FASE-0: CLI unificada + reorganización legacy
  
  - Create 03_SCRIPTS/platform/ with Click CLI
  - Move 7 legacy scripts to 99_ARCHIVE/pipelines_legacy/
  - Move PROCESADO/ to 99_ARCHIVE/ (obsolete)
  - Rewrite README with honest capability matrix
  - Create courses.yaml as single source of truth
  - Update documentation: NO más mentiras de '100%' o 'OPERACIONAL'
  
  VEREDICTO: NO_PLATAFORMA (2/6 cursos, 33% cobertura)
  
  Next: ADR-003 — Multi-usuario, learner tracking, cloud (2-3 weeks)"
  ```

- [ ] Verificar (git log, git status)

---

## CAMBIOS VISUALES (Diff Summary)

```
ANTES (Caos):
  F:\MACI\
  ├── procesar_80014.py           ❌
  ├── procesar_80038.py           ❌
  ├── procesar_curso_80714.py     ❌
  ├── procesar_liderazgo.py       ❌
  ├── procesar_prototipos.py      ❌
  ├── actualizar_index_80014.py   ❌
  ├── limpiar_nombres_80014.py    ❌
  ├── PROCESADO/                  ❌
  └── README.md (falsedades)      ❌

DESPUÉS (Coherencia):
  F:\MACI\
  ├── 03_SCRIPTS/platform/         ✅ Nueva CLI
  │   ├── __main__.py
  │   ├── cli.py
  │   ├── manifest.py
  │   └── processors/
  │       └── canvas.py
  │
  ├── 99_ARCHIVE/pipelines_legacy/ ✅ Reorganizado
  │   ├── procesar_80014.py
  │   ├── procesar_80038.py
  │   ├── (5 más)
  │   └── README.md
  │
  ├── courses.yaml                 ✅ Fuente única
  ├── README.md (honesto)          ✅ Actualizado
  ├── INDEX_MAESTRO.md (real)      ✅ Actualizado
  └── ARQUITECTURA.md              ✅ Nuevo
```

---

## USUARIO EXPERIENCE (Antes vs Después)

### ANTES
```
Usuario: "¿Cómo proceso 80714?"
→ Busca scripts en raíz
→ Encuentra 7 opciones confusas
→ Trata de ejecutar procesar_curso_80714.py
→ Funciona (suerte)
→ No sabe qué cambió

Usuario: "¿Qué cursos están listos?"
→ Lee README
→ Dice "✅ OPERACIONAL"
→ Abre las carpetas
→ Ve 3 de 6 cursos con contenido
→ Confundido: ¿33% es "operacional"?
```

### DESPUÉS
```
Usuario: "¿Cómo proceso 80714?"
→ python -m platform process --course 80714
→ Claro, unificado, falla si no existe

Usuario: "¿80038 está listo?"
→ python -m platform report
→ Ve matriz real: 2/6 = 33%
→ Lee README: "NO_PLATAFORMA, parcial"
→ Expectativas claras
```

---

## TESTING PLAN

### Unit Tests (Mínimo)
```python
# test_manifest.py
def test_manifest_loads():
    m = load_manifest()
    assert len(m.courses) == 6

def test_course_capabilities():
    m = load_manifest()
    course_80038 = next(c for c in m.courses if c.id == 80038)
    assert course_80038.capabilities.videos == True
    assert course_80038.capabilities.notes == True
    assert course_80038.capabilities.dashboard == True

def test_cli_entrypoint():
    # python -m platform --help (no error)
    # python -m platform status (prints table)
    pass
```

### Integration Tests
```bash
# Test actual processing (calls legacy script)
python -m platform process --course 80014
# Should exit 0 and update courses.yaml timestamp
```

---

## ROLLBACK PLAN (Si Todo Falla)

```bash
# Deshacer en 2 minutos:
git revert HEAD~5
git reset --hard HEAD

# O específicamente:
git checkout HEAD -- 03_SCRIPTS/
git checkout HEAD -- 99_ARCHIVE/
git checkout HEAD -- courses.yaml
git checkout HEAD -- README.md

# Scripts clonados vuelven a raíz automáticamente
```

---

## SUCCESS CRITERIA (Final Check)

**Antes de cerrar FASE 0:**

- [ ] `python -m platform --help` funciona (no error)
- [ ] `python -m platform status` imprime tabla sin errores
- [ ] `python -m platform process --course 80014` llama legacy script
- [ ] `courses.yaml` es YAML válido y tiene 6+ cursos
- [ ] README no tiene "100%", "OPERACIONAL" ni "plataforma"
- [ ] README tiene sección "Qué abrir para qué" (60 seg)
- [ ] 0 procesar_*.py en raíz (todos en 99_ARCHIVE/)
- [ ] Commit descrito y pusheado
- [ ] ADR-003 entendido por next architect

---

## NEXT PHASE (After FASE 0)

```
FASE 1: Multi-Estudiante (2-3 semanas)
  - learners/<id>/progress.yaml
  - Datito parametrizable por curso
  - Cloud/API prototype

FASE 2: Evaluación Automática (3-4 semanas)
  - Quiz, ejercicios interactivos
  - Scoring, rúbricas
  - Integración con Datito

FASE 3: Real Plataforma (Month 2+)
  - Web UI (React o similar)
  - Multi-usuario concurrente
  - Database backend
  - API REST

Estimado total para "plataforma real": 3-4 meses
```

---

**Implementador:** [Tu nombre]  
**Estimado:** 40 horas  
**Esperado:** Lunes próximo (o 1 semana)

