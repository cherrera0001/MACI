# PLATAFORMA_COHERENCIA_GAP.md
## Diagnóstico: MACI NO ES Plataforma (Aún)

**Fecha:** 2026-09-22  
**Veredicto:** `NO_PLATAFORMA` → intentos parciales en 3 dimensiones sin coherencia

---

## 1. MAPA: Qué Carpeta Pertenece a Qué

### Dimensión A: Instancia FCD (Proyecto Semestral Cristóbal)
```
01_DOCUMENTACION/          [Material documental del semestre]
08_PROYECTO_FCD/           [Melbourne housing + Galaxy Zoo]
03_SCRIPTS/                 [Scripts de análisis]
02_DATOS/                  [Datasets]
09_RESULTADOS/             [Outputs FCD]
06_ENTREGABLES/            [Reportes finales]
07_DATITO/                 [Tutor personal Cristóbal]
06_LABORATORIOS/               [Labs del curso (P1-P5)]
05_CLASES/                 [Transcripciones clase]
10_ARCHIVO/                [Obsoleto, no usar]
```
**Propietario:** Estudiante (Cristóbal Herrera)  
**Alcance:** Un semestre, un estudiante, FCD específicamente  
**Estado:** ESTABLE (no debería cambiar)

---

### Dimensión B: Core Datito (Tutor Personal Modulable)
```
07_DATITO/
├── curriculum.yaml        [21 conceptos FCD]
├── progreso.yaml          [Evidencia de aprendizaje Cristóbal]
├── dudas.yaml             [Preguntas + respuestas]
├── visual/                [HTMLs educativos generados]
├── clases.yaml            [22 clases transcritas]
└── bitacora/              [Sesiones de estudio]
```
**Propietario:** Sistema pedagógico  
**Alcance:** Potencialmente multi-estudiante, multi-curso  
**Estado:** PROTOTIPO (especificación en `spec.md`)  
**Problema:** Hardcodeado a FCD; no parametrizable aún

---

### Dimensión C: Ingest Canvas (Respaldo + Grabaciones)
```
courses/                   [6 asignaturas Canvas 2026]
├── 80014_Emprendimiento/
├── 80038_Procesos_Innovacion/
├── 80714_Fundamentos_BD/
├── 83703_Liderazgo/
├── 83706_Prototipos/
└── 83707_Ciencias_Datos/

10_GRABACIÓN_CLASES/       [Videos + índices]
├── 80038_Procesos_Innovacion/  [✅ Procesado]
└── (5 carpetas vacías)

MACI_RESPALDOS/            [Backup Canvas API]
└── udec/2026-09-22-001/   [155 archivos + auditoría]
```
**Propietario:** Usuario (Cristóbal)  
**Alcance:** 6 cursos reales UdeC T2-2026  
**Estado:** PARCIAL  
- 80038: ✅ Videos + índices
- 80014: ✅ ZIP procesado + índices  
- 80714, 83703, 83706, 83707: 📦 Estructura sin contenido

---

### Dimensión D: Learner Tracking (FANTASMA)
```
learners/                  [Directorio existe]
└── (vacío)
```
**Propietario:** Plataforma  
**Alcance:** N estudiantes × M cursos  
**Estado:** PLACEHOLDER (sin implementación)

---

### Dimensión E: Raíz Desordenada (DEUDA TÉCNICA)
```
F:\MACI\
├── PROCESADO/             [Duplicación de courses/]
├── procesar_80014.py      [Script clonado #1]
├── procesar_80038.py      [Script clonado #2]
├── procesar_curso_80714.py [Script clonado #3]
├── procesar_liderazgo.py  [Script clonado #4]
├── procesar_prototipos.py [Script clonado #5]
├── actualizar_index_80014.py [Script clonado #6]
├── limpiar_nombres_80014.py  [Script clonado #7]
├── descargar_contenido.py [Script legacy]
├── DOCUMENTACION/         [Duplica 01_DOCUMENTACION]
└── INDEX_MAESTRO.md       [Intenta ser nav global, falla]
```
**Propietario:** Nadie (basura)  
**Alcance:** Confusión  
**Estado:** ❌ DEBE LIMPIARSE

---

## 2. MENTIRAS OPERATIVAS vs HECHOS DE DISCO

### Mentira #1: "100% OPERACIONAL"
**Dónde se dice:**
- INDEX_MAESTRO.md: "✅ OPERACIONAL — Listo para usar"
- ESTADO_PROYECTO_FINAL.txt: "✅ Proyecto consolidado"
- REPORTE_FINAL_INTEGRADO.md: "✅ COMPLETO"

**Verdad de disco:**
```
80038: ✅ (videos + 13 .md + transcripciones)
80014: ✅ (ZIP integrado + 5 .md + 12 ejercicios)
80714: ❌ (0 videos, estructura vacía, 0 notas)
83703: ❌ (0 videos, estructura vacía, 0 notas)
83706: ❌ (0 videos, estructura vacía, 0 notas)
83707: ❌ (0 videos, estructura vacía, 0 notas)

Promedio real: 2/6 asignaturas = 33% NO 100%
```

**Riesgo:** Usuario cree tener plataforma cuando hay 4 carpetas vacías

---

### Mentira #2: "PLATAFORMA DE AUTO-ESTUDIO"
**Dónde se dice:** INDEX_MAESTRO.md, ESTADO_PROYECTO_FINAL.txt

**Verdad de disco:**
- No hay sistema de tracking de progreso (learners/ vacío)
- No hay quiz/evaluación interactivo
- No hay adaptabilidad por estudiante
- No hay API ni integración multi-usuario
- Scripts clonados por curso (no escalable)

**Realidad:** Colección de documentos markdown + videos
**¿Es plataforma?** No. Es contenido organizado.

---

### Mentira #3: "ESTRUCTURA LIMPIA"
**Dónde se dice:** Múltiples informes

**Hechos desordenados:**
```
Duplicación:
  - DOCUMENTACION/ (raíz) = 01_DOCUMENTACION/ (instancia FCD)
  - PROCESADO/ (raíz) = courses/ (lugar correcto)
  
Scripts clonados:
  - procesar_80014.py, procesar_80038.py, procesar_curso_80714.py, 
    procesar_liderazgo.py, procesar_prototipos.py (cada uno copia del otro)
  - No hay un CLI unificado
  - Imposible agregar curso 7 sin clonar script

Capacidades inconsistentes:
  - 80038 tiene: videos + transcripciones + dashboard + guía + notas
  - 80014 tiene: ZIP integrado + ejercicios + cronograma
  - 80714 tiene: solo estructura vacía
  - Sin matriz de cobertura que documente qué falta
```

**Riesgo:** Arquitecto siguiente hereda basura + confusión de prioridades

---

## 3. DEPENDENCIAS CRUZADAS ROTAS

### Rotura #1: `DOCUMENTACION/` vs `01_DOCUMENTACION/`
```
DOCUMENTACION/              [en raíz, apunta a INFO docente]
01_DOCUMENTACION/           [legítimo, parte de FCD de Cristóbal]

PROBLEMA: Usuario no sabe cuál leer
SOLUCIÓN: Una debe ser symlink o desaparecer
```

### Rotura #2: `INDEX_MAESTRO.md` apunta a paths que no existen
```
INDEX_MAESTRO.md dice:
  "F:\MACI\10_GRABACIÓN_CLASES\80014_Emprendimiento\SESION_{N}/"

Realidad:
  - SESION_* nunca existieron (se borraron)
  - Apunta a estructura fantasma
  - Links rotos en el README
```

### Rotura #3: `courses/` vs `PROCESADO/`
```
MACI_RESPALDOS/udec/2026-09-22-001/PROCESADO/
  → Contiene copia vieja de 80014, 80038, 80703 (OBSOLETA)

F:\MACI\courses/
  → Contiene copia nueva y procesada

PROBLEMA: ¿Cuál es fuente de verdad? Alumno usa vieja.
SOLUCIÓN: PROCESADO/ debe estar en 10_ARCHIVO
```

---

## 4. CAPACIDADES REALES POR CURSO (MATRIZ DATA-DRIVEN)

```
Curso                  Videos  Transcripciones  Notas  Ejercicios  Índices  Dashboard  Estado
80714_Fundamentos_BD   ✅ (16) ❌               ❌     ❌          ✅       ❌         PARCIAL
80038_Proc_Innov       ✅ (5)  ✅ (5)           ✅ (5) ❌          ✅ (3)   ✅         PARCIAL
80014_Emprend          ❌      ❌               ✅ (6) ✅ (6)       ✅ (3)   ❌         PARCIAL
83703_Liderazgo        ❌      ❌               ❌     ❌          ✅       ❌         VACÍO
83706_Prototipos       ❌      ❌               ❌     ❌          ✅       ❌         VACÍO
83707_Ciencias_Datos   ❌      ❌               ❌     ❌          ✅       ❌         VACÍO

Cobertura: 3/6 asignaturas parcialmente operacionales (50%)
Déficit: 12 videos pendientes, 4 sets de notas, 3 sets de ejercicios
```

---

## 5. SCRIPTS CLONADOS: LA MAYOR DEUDA

**Ubicación:** raíz de F:\MACI\

```
procesar_80014.py          [Copy of procesar_curso_template.py]
procesar_80038.py          [Copy of procesar_curso_template.py]
procesar_curso_80714.py    [Copy of procesar_curso_template.py]
procesar_liderazgo.py      [Copy of procesar_curso_template.py]
procesar_prototipos.py     [Copy of procesar_curso_template.py]
actualizar_index_80014.py  [Especializado, debe ser flag de CLI]
limpiar_nombres_80014.py   [Debe ser en procesar_curso.py]
descargar_contenido.py     [Legacy, confunde con canvas_downloader.py]
```

**Problema:**
- No hay una fuente de verdad
- Agregar curso 7 → clonar + editar 7 variables
- Bug fix en uno → debe replicarse manualmente en otros
- Imposible de mantener

**Costo:** Cada script toma 5-10 min para entender + modificar

---

## VEREDICTO

### ¿Es MACI una plataforma?
**NO.** Es una **colección de instancias + scripts ad-hoc + contenido sin sistema**.

### Dimensión plataforma:
```
Requisitos de plataforma:     Estado en MACI
├─ CLI unificada              ❌ (7 scripts clonados)
├─ Data model                 ❌ (estructura emergente, no esquema)
├─ Multi-usuario/tenancy      ❌ (hardcodeado a 1 estudiante)
├─ Tracking de progreso       ❌ (learners/ vacío)
├─ Escalabilidad (agregar curso) ❌ (requiere clonar script)
├─ Evaluación automática      ❌ (solo markdown)
└─ Integración externa        ❌ (archivos, no API)

Score: 0/7 = NO_PLATAFORMA
```

### Lo que SÍ existe:
- ✅ Instancia FCD sólida (01-07_*)
- ✅ Respaldo Canvas verificado (MACI_RESPALDOS/)
- ✅ 2 cursos parcialmente procesados (80038, 80014)
- ✅ Datito prototipo (07_DATITO/)

### Lo que FALTA para ser plataforma:
1. Unificación de CLI (1 punto de entrada)
2. Parametrización por curso (no clones)
3. Schema de datos (learner, course, content)
4. Migración de learners/ desde placeholder
5. Evaluación integrada (quiz, ejercicios interactivos)

---

## RECOMENDACIÓN INMEDIATA

**No pierdas tiempo agregando más cursos 2 y 3 hasta que tengas:**

1. Una CLI unificada (`python -m platform.cli process --course <id>`)
2. Un directorio legible (`README explica qué abrir para qué`)
3. Una matriz de capacidades actualizada (para no mentir en README)
4. 10_ARCHIVO/pipelines_legacy/ (para los 7 scripts clonados)

**Esto es una semana de arquitectura. Vale más que 3 semanas de más scripts clonados.**

