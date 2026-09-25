# Plantilla de Curso para Datito

Esta carpeta es un punto de partida para usar Datito en un nuevo curso.

## Quickstart (10 minutos)

### 1. Copia la plantilla
```bash
cp -r courses/_template courses/tu-ramo-2026-2
cd courses/tu-ramo-2026-2
```

### 2. Edita `datito.config.yaml`
Reemplaza los valores de ejemplo:
- `course_id`: identificador único (ej: `estadistica-2026-2`)
- `alumno.nombre` y `email`
- `asignatura.*`: nombre, período, institución, docentes
- `proyectos`: tus datasets y casos de estudio (opcional)

### 3. Define tu curriculum: `curriculum.yaml`

Estructura:
```yaml
meta:
  alumno: Tu Nombre
  asignatura: Tu Ramo (Período)
  ...

conceptos:
  - id: concepto_1         # identificador único (min-slug)
    nombre: Concepto 1
    definicion: breve párrafo
    prerrequisitos: []
    material_local: [rutas a tu repo]
    prácticos: []
    sin_material_local: false
    ...
  - id: concepto_2
    ...
```

**Tip:** Copia la estructura del curriculum de Fundamentos de Ciencia de Datos (MACI), reemplaza conceptos y material.

### 4. Define tus clases: `clases.yaml`

Estructura (viene desde la versión FCD):
```yaml
unidades:
  1: "Unidad 1: Nombre"
  2: "Unidad 2: Nombre"
  ...

clases:
  - n: 1
    unidad: 1
    titulo: "Primera clase"
    visual: concepto1.html    # apunta a 07_DATITO/visual/ (será courses/TU-RAMO/visual/)
    tipo: concepto
    conceptos: [concepto_1]
    objetivo: "al terminar, podrás..."
    activacion: "una pregunta de calentamiento"
    bloom:
      nivel: Recordar
      ...
```

**Tip:** Ordena las clases por prerrequisitos (de simple a complejo).

### 5. Crea alumnos

```bash
# Desde la raíz del repositorio
python 03_CODIGO/datito_init_learner.py --course tu-ramo-2026-2 --learner primer_alumno
```

Esto genera:
```
learners/
  primer_alumno_tu-ramo-2026-2/
    datito.config.yaml         (heredado de course)
    progreso.yaml              (vacío: todos en NO_ESTUDIADO)
    errores_conceptuales.yaml  (vacío)
    estado.md                  (vacío)
    dudas.yaml                 (vacío)
    bitacora/
    entregas/
```

### 6. Regenera los visuales y navegación

```bash
python 03_CODIGO/construir_navegacion.py
python 03_CODIGO/datito_estado.py
```

Listo. Ya puedes abrir Claude Code en el raíz de MACI y decir:
```
/datito
```

---

## Estructura de archivos

```
courses/tu-ramo-2026-2/
├── README.md                        ← este archivo (opcional)
├── datito.config.yaml              EDITAR: metadatos del alumno y asignatura
├── curriculum.yaml                 EDITAR: los conceptos del ramo
├── clases.yaml                     EDITAR: el plan de clase (22–30 clases)
│
├── progreso.yaml                   Auto-generado (alumno 1, alumno 2, ...)
├── errores_conceptuales.yaml       Auto-generado
├── estado.md                       Auto-generado
├── patron_evaluacion.md            Opcional: cómo califica tu profesor
│
├── grafo.yaml                      Auto-generado (si quieres análisis)
├── dudas.yaml                      Auto-generado (respuestas dadas)
├── visual/                         HTML interactivos (1 por concepto)
│   ├── index.html                  Portada del curso
│   ├── concepto1.html
│   ├── concepto2.html
│   └── ...
├── bitacora/                       Una entrada por sesión de estudio
├── referencia/                     Material local: PDFs, fuentes
└── guias/ · cuadernillos/ · certamenes/  (Opcional)
```

---

## Qué es cada archivo

| Archivo | Editable | Qué contiene |
|---|---|---|
| `datito.config.yaml` | ✅ SÍ (necesario) | Metadatos: alumno, curso, evaluación, proyectos |
| `curriculum.yaml` | ✅ SÍ (necesario) | Los N conceptos del ramo: definición, material, prácticos |
| `clases.yaml` | ✅ SÍ (necesario) | Orden de clase: 20–30 clases en unidades. Objetivo, Bloom, cierre |
| `progreso.yaml` | ❌ No (auto-generado) | Estado del alumno: qué entiende, qué falta. Solo Datito escribe |
| `errores_conceptuales.yaml` | ❌ No (auto-generado) | Errores observados y patrones. Solo Datito escribe |
| `estado.md` | ❌ No (auto-generado) | Resumen compacto (30 líneas). Regréralo tras cada sesión: `python 03_CODIGO/datito_estado.py` |
| `patron_evaluacion.md` | ✅ Opcional | Análisis de cómo califica tu profesor (vacío si no lo tienes) |
| `visual/` | ✅ Parcial | HTMLs de conceptos. Se *auto-inyecta* navegación; no edites entre comentarios datito:* |
| `referencia/` | ✅ Sí | Material local que usa el tutor: guías, PDFs, notebooks |

---

## Checklist antes de activar

- [ ] `datito.config.yaml` está completo
- [ ] `curriculum.yaml` tiene ≥ 5 conceptos
- [ ] `clases.yaml` tiene ≥ 10 clases, bien ordenadas
- [ ] `/datito-pedagogia` audita el alineamiento Bloom ↔ evaluación (si tienes certamenes reales)
- [ ] Corriste: `python 03_CODIGO/construir_navegacion.py`
- [ ] Corriste: `python 03_CODIGO/datito_estado.py`
- [ ] Corriste: `python 03_CODIGO/verificar_contrato.py` → 12 tests ok
- [ ] Creaste al menos un alumno: `python 03_CODIGO/datito_init_learner.py --course tu-ramo-2026-2 --learner primer_alumno`

---

## Preguntas frecuentes

**P: ¿Tengo que tener un proyecto (Melbourne o Galaxy Zoo)?**
R: No. Es *opcional* en `datito.config.yaml` → `proyectos:`. Datito funciona con solo el curriculum.

**P: ¿Puedo copiar los HTMLs de otro curso?**
R: Sí, pero habrá que adaptarlos. Los artefactos incluyen referencias a clase, minuto y transcripción; eso cambia por ramo.

**P: ¿Y si mi profesor no da clases grabadas?**
R: Borra la sección `09_CLASES/` de referencias. Los visuales funcionan sin ello.

**P: ¿Cómo agrego nuevos alumnos en T3?**
R: ```bash
python 03_CODIGO/datito_init_learner.py --course tu-ramo-2026-3 --learner nuevo_alumno
```

---

## Mantén sincronizada esta plantilla

Si cambias algo en `courses/fcd-2026-2/` que aplica a **todos** los cursos (estructura, etiquetas YAML, reglas pedagogía), actualiza también `courses/_template/`. Así el próximo docente tendrá la versión nueva.

---

**¿Dudas?** Lee [`ADR-001-multi-course.md`](../../01_DOCUMENTACION/ADR-001-multi-course.md).
