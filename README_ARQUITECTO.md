# MACI — Diagnóstico Arquitectónico

**Fecha:** 2026-09-22  
**Rol:** Arquitecto (no celebrante)  
**Veredicto:** `NO_PLATAFORMA` — 3 productos sin coherencia + deuda técnica

---

## TL;DR: Qué Es MACI Realmente

MACI es **una instancia semestral (FCD-Cristóbal) + un prototipo pedagógico (Datito) + un respaldo parcial de Canvas**, todo en una raíz desordenada con **7 scripts clonados y mentiras en el README**.

**No es:** Plataforma, multi-usuario, escalable, ni listo para producción.

**Sí es:** Funcional para un estudiante, un semestre, 2 de 6 cursos.

---

## QUÉ ABRIR PARA QUÉ (60 segundos)

### 📚 Si Quieres Estudiar FCD con Datito (Cristóbal)
```
Abre:
  01_DOCUMENTACION/       ← Notas del semestre
  07_DATITO/              ← Tutor personal
  08_PRACTICA/            ← Labs (P1-P5)
  
Ignora:
  courses/                ← No es para ti (es Canvas)
  10_GRABACIÓN_CLASES/    ← No es para ti (es Canvas)
```

### 📥 Si Quieres Descargar/Procesar un Curso Canvas
```
Hoy (confuso):
  python procesar_80014.py        ← Busca scripts clonados en raíz
  python procesar_80038.py        ← Múltiples opciones, no está claro

Mañana (con ADR-003):
  python -m platform process --course 80014
  
Resultado: courses/80014_Emprendimiento/ o 10_GRABACIÓN_CLASES/80014/
```

### 👤 Si Quieres Crear Nuevo Estudiante/Curso
```
Hoy: No es posible. Datito está hardcodeado a FCD, canvas al respaldo específico.

Mañana (con plataforma): learners/<id>/, config multitenant.

Estimado: 2-3 semanas de arquitectura después de ADR-003.
```

---

## ESTADO ACTUAL (MATRIZ HONESTA)

### Producto A: Instancia FCD-Cristóbal
```
01_DOCUMENTACION/         ✅ Estable, no cambiar
02_PROYECTO_FCD/          ✅ Completo (Melbourne + Galaxy Zoo)
03_CODIGO/                ✅ Scripts de análisis funcionales
07_DATITO/                ⚠️  Prototipo pedagógico, funcional
08_PRACTICA/              ✅ 5 laboratorios (P1-P5)
09_CLASES/                ✅ 15 transcripciones

VEREDICTO: ESTABLE (no tocar)
```

### Producto B: Core Datito (Pedagógico)
```
07_DATITO/curriculum.yaml    ✅ 21 conceptos FCD documentados
07_DATITO/progreso.yaml      ⚠️  Solo Cristóbal, datos locales
07_DATITO/visual/            ✅ HTMLs educativos generados
07_DATITO/spec.md            ✅ Especificación clara

Capacidad: Funciona para 1 estudiante × 1 curso
Escalabilidad: Nula (hardcodeado)

VEREDICTO: PROTOTIPO VÁLIDO (requiere parametrización)
```

### Producto C: Respaldo Canvas + Grabaciones
```
MACI_RESPALDOS/udec/2026-09-22-001/    ✅ Auditoría forense completada
├── 155 archivos Canvas                ✅ 100% cobertura API
├── 26 URLs externas identificadas      ⚠️  No descargables vía API

courses/
├── 80014_Emprendimiento              ✅ ZIP integrado, notas + ejercicios
├── 80038_Procesos_Innovacion         ✅ Videos + índices + notas + transcripciones
├── 80714_Fundamentos_BD              ✅ 16 videos + material integrado
├── 83703_Liderazgo                   ⚠️  Estructura + índices, sin videos
├── 83706_Prototipos                  ⚠️  Estructura + índices, sin videos
└── 83707_Ciencias_Datos              ⚠️  Estructura + índices, sin videos

10_GRABACIÓN_CLASES/
├── 80038_Procesos_Innovacion         ✅ 5 videos + 13 índices
├── 80014_Emprendimiento              ⚠️  Estructura lista, sin videos
├── 80714_Fundamentos_BD              ✅ 16 videos + índice
└── (3 cursos)                         ⚠️  Estructura lista

VEREDICTO: PARCIAL (3/6 cursos = 50%)
```

### Deuda Técnica
```
Raíz desordenada:
  procesar_80014.py         ❌ Script clonado #1
  procesar_80038.py         ❌ Script clonado #2
  procesar_curso_80714.py   ❌ Script clonado #3
  procesar_liderazgo.py     ❌ Script clonado #4
  procesar_prototipos.py    ❌ Script clonado #5
  actualizar_index_80014.py ❌ Script clonado #6
  limpiar_nombres_80014.py  ❌ Script clonado #7
  descargar_contenido.py    ❌ Legacy, confunde

Duplicaciones:
  DOCUMENTACION/            ❌ Duplica 01_DOCUMENTACION/
  PROCESADO/                ❌ Duplica contenido de courses/

README falsedades:
  "✅ OPERACIONAL"          ❌ (2/6 = 33%, no 100%)
  "Plataforma de estudio"   ❌ (es contenido, no plataforma)
  "Estructura limpia"       ❌ (7 scripts clonados + duplicaciones)

COSTO: 2-3 días de limpieza + unificación
```

---

## CAPACIDADES REALES POR CURSO (Data-Driven)

```
ID     Nombre                    Videos  Notas  Ejercicios  Transcripts  Dashboard
80014  Emprendimiento               ❌      ✅(6)    ✅(6)         ❌         ❌
80038  Procesos de Innovación       ✅(5)   ✅(5)    ❌            ✅         ✅
80714  Fundamentos BD               ❌      ❌       ❌            ❌         ❌
83703  Liderazgo                    ❌      ❌       ❌            ❌         ❌
83706  Prototipos                   ❌      ❌       ❌            ❌         ❌
83707  Ciencias Datos               ❌      ❌       ❌            ❌         ❌

COBERTURA: 2/6 = 33% (NO 100%, NO "OPERACIONAL")
```

---

## PRÓXIMA FASE: ADR-003

### Objetivo
Unificar entrada (CLI) sin migración destructiva. Estimado: **1 semana**.

### Plan
```
1. Crear 03_CODIGO/platform/
   ├── __main__.py          (Entry: python -m platform <cmd>)
   ├── cli.py               (Click CLI: process, status, report)
   └── courses.yaml         (Manifesto: fuente única de verdad)

2. Mover 7 scripts a 99_ARCHIVO/pipelines_legacy/
   (Todavía existen, solo organizados)

3. Actualizar README, INDEX_MAESTRO, ESTADO
   (Honesto: matriz de capacidades, no mentiras)

4. Crear learners/ placeholder
   (Para futuro multi-estudiante)
```

### Success Criteria
```
✅ python -m platform process --course 80014  (sin errores)
✅ python -m platform report                  (matriz real)
✅ README explica qué abrir para qué          (<60 seg lectura)
✅ 0 procesar_*.py en raíz                    (todos en 99_ARCHIVO/)
✅ courses.yaml es fuente única               (capacidades reales)
✅ User sabe: "Esto NO es plataforma"         (expectativas claras)
```

---

## ARCHIVOS CLAVE DEL DIAGNÓSTICO

- `PLATAFORMA_COHERENCIA_GAP.md` — Diagnóstico completo (mentiras vs. hechos)
- `ADR-003-PLATAFORMA-UNIFICADA.md` — Diseño target (sin destruir)
- `README_ARQUITECTO.md` — Este documento (honesto)

---

## LO QUE NO VA A CAMBIAR

```
Protegido (no tocar):
  01_DOCUMENTACION/           (instancia FCD)
  02_PROYECTO_FCD/            (semestral)
  07_DATITO/                  (core pedagógico)
  MACI_RESPALDOS/             (backup)
  .env, credenciales

Permitido:
  Crear 03_CODIGO/platform/
  Reorganizar raíz (scripts a 99_ARCHIVO/)
  Actualizar README/INDEX
  Honestidad en capacidades
```

---

## TIMELINE

```
Hoy (22 sep):    Diagnóstico + diseño (ADR-003)
Semana 1:        Implementación FASE 0 (CLI unificada)
Semana 2-3:      Completar 4 cursos faltantes (si hay videos)
Mes 2+:          Multi-usuario, learner tracking, cloud (futuro)
```

---

## CONCLUSIÓN

MACI **no es una plataforma**. Es un **prototipo multi-dimensión que necesita arquitectura coherente**.

La buena noticia: Los productos individuales funcionan (instancia FCD, Datito prototipo, Canvas respaldado).

La mala noticia: Mezclados sin coherencia, escalable cero, lleno de deuda técnica.

La siguiente noticia: ADR-003 lo arregla sin destruir nada (1 semana).

**Recomendación:** Haz ADR-003 antes de agregar cursos 7 y 8. Vale más que 3 semanas de scripts clonados más.

