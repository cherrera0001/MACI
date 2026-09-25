# MACI — Fundamentos de Ciencia de Datos (UdeC, T2-2026)
## Índice Maestro de Recursos Educativos

---

## 📚 Cursos Procesados y Disponibles

### F:\MACI\courses\
Estructura modular de 6 asignaturas con contenido descargado desde Canvas (2026-09-22).

| Curso | ID | Descripción | Módulos | Recursos |
|-------|-----|-------------|---------|----------|
| **Fundamentos de BD** | 80714 | Bases de datos, SQL, diseño de esquemas | 4 | 37 |
| **Fundamentos Ciencias Datos** | 83707 | Pandas, análisis, visualización | 9 | 25 |
| **Procesos de Innovación** | 80038 | Innovación, metodología, emprendimiento | 10 | 23 |
| **Emprendimiento Tecnológico** | 80014 | Startups, modelos de negocio | 11 | 28 |
| **Prototipos y Creatividad** | 83706 | Diseño, prototipado, iteración | 10 | 25 |
| **Liderazgo y Equipos** | 83703 | Gestión, equipos, comunicación | 10 | 40 |

**Total:** 6 cursos, 54 módulos, 178 recursos procesados ✅

---

## 🎬 Grabaciones de Clases (Estructura Lista)

### F:\MACI\10_GRABACIÓN_CLASES\
Estructura de carpetas creada para cada curso con sesiones listas para recibir videos.

**Estado:** ✅ Estructura creada y lista

**Por Curso:**
- **80714_Fundamentos_BD:** 4 sesiones (SESION_01 a SESION_04)
- **83707_Ciencias_Datos:** 9 sesiones (SESION_01 a SESION_09)
- **80038_Procesos_Innovacion:** 10 sesiones (SESION_01 a SESION_10)
- **80014_Emprendimiento:** 11 sesiones (SESION_01 a SESION_11)
- **83706_Prototipos:** 10 sesiones (SESION_01 a SESION_10)
- **83703_Liderazgo:** 10 sesiones (SESION_01 a SESION_10)

**Total:** 54 sesiones vacías, listas para recibir .mp4

### Cómo Usar:
1. **Descargar** grabación desde Canvas/Zoom → `grabacion.mp4`
2. **Colocar** en: `10_GRABACIÓN_CLASES/{CURSO_ID}_{NOMBRE}/SESION_{N}/`
3. **Ejecutar:** `python 10_GRABACIÓN_CLASES/procesar_grabaciones.py`
4. **Agentes** procesarán automáticamente:
   - Generarán TRANSCRIPT.txt (transcripción automática)
   - Crearán NOTAS.md (resumen + puntos clave)
   - Vincularán con recursos en F:\MACI\courses\
   - Crearán índices por sesión

---

## 🔍 Cómo Navegar Este Proyecto

### Para Estudiar un Curso (Contenido disponible)
1. Ir a `F:\MACI\courses\{CURSO_ID}_{NOMBRE}\`
2. Leer `INDEX.md` para ver estructura de módulos
3. Cada módulo contiene `METADATA.json` con metadatos estructurados
4. Explorar recursos por tema

**Ejemplo:**
```bash
cd "F:\MACI\courses\83707_Ciencias_Datos"
cat INDEX.md  # Ver estructura del curso
```

### Para Acceder a Grabaciones (Cuando estén disponibles)
1. Ir a `F:\MACI\10_GRABACIÓN_CLASES\{CURSO_ID}_{NOMBRE}\`
2. Abrir `SESION_N/` donde colocaste el video
3. Cada sesión contendrá:
   - `grabacion.mp4` — Video de la clase
   - `TRANSCRIPT.txt` — Transcripción (generada automáticamente)
   - `NOTAS.md` — Resumen y puntos clave
   - `RECURSOS.json` — Links a slides, código, datasets
   - `METADATA.json` — Información de la sesión
   - `INDEX.md` — Índice de la sesión con timestamps

### Para Buscar Contenido
Usar `INDEX_MAESTRO.md` (este archivo) para:
- Identificar en qué curso está un tema
- Encontrar módulos relacionados
- Localizar recursos por asignatura

---

## 📊 Estadísticas de Cobertura

### Contenido Descargado desde Canvas API

| Métrica | Valor |
|---------|-------|
| **Archivos Canvas** | 155/155 (100%) ✅ |
| **JSONs metadatos** | 162 |
| **Cursos resguardados** | 6/6 |
| **Módulos temáticos** | 54 |
| **SHA-256 hashes** | Todos verificados |
| **Integridad** | Auditoría forense completada |

### Recursos Externos Identificados Pero No Descargados
- **Google Drive:** 4 enlaces (privados, descarga manual)
- **Zoom/Grabaciones:** 8 enlaces (con MFA, en 10_GRABACIÓN_CLASES/)
- **Videos:** 1 enlace (incrustado)
- **Otros:** 13 enlaces

**Ubicación:** `F:\MACI_RESPALDOS\udec\2026-09-22-001\external_urls_by_course.json`

---

## 🛠️ Agentes Disponibles (Para Procesar Grabaciones)

Una vez tengas grabaciones en `F:\MACI\10_GRABACIÓN_CLASES\`:

### 1. `procesar-grabaciones`
- Organiza videos por sesión
- Genera METADATA.json
- Crea estructura de carpetas
- Indexa por curso

### 2. `transcribir-clase`
- Extrae audio de MP4/MOV
- Genera TRANSCRIPT.txt automático
- Markdownea timestamps
- Etiqueta términos técnicos

### 3. `sincronizar-recursos`
- Vincula slides con videos (timestamps)
- Crea RECURSOS.json
- Indexa por tema
- Búsqueda automática

### 4. `generar-notas-clase`
- Resume transcripciones
- Extrae puntos clave
- Genera NOTAS.md navegable
- Propone ejercicios

### 5. `crear-indice-maestro`
- Consolida índices de cursos + grabaciones
- Crea búsqueda global por tema
- Genera guía de estudio integrada
- Propone secuencia de aprendizaje

---

## 📁 Estructura Completa del Proyecto

```
F:\MACI\
│
├── courses\                         [✅ Contenido Canvas descargado]
│   ├── 80714_Fundamentos_BD\
│   │   ├── INDEX.md
│   │   ├── 00_Introduccion\
│   │   ├── 01_Python_Basico\
│   │   ├── 02_Bases_Datos_Conceptos\
│   │   └── 03_...
│   │
│   ├── 83707_Ciencias_Datos\       [9 módulos]
│   ├── 80038_Procesos_Innovacion\  [10 módulos]
│   ├── 80014_Emprendimiento\       [11 módulos]
│   ├── 83706_Prototipos\           [10 módulos]
│   └── 83703_Liderazgo\            [10 módulos]
│
├── 10_GRABACIÓN_CLASES\            [✅ Estructura lista, vacía]
│   ├── 80714_Fundamentos_BD\
│   │   ├── SESION_01\              [← Coloca: grabacion.mp4]
│   │   ├── SESION_02\
│   │   ├── SESION_03\
│   │   └── SESION_04/
│   │
│   ├── 83707_Ciencias_Datos\       [SESION_01 a SESION_09]
│   ├── 80038_Procesos_Innovacion\  [SESION_01 a SESION_10]
│   ├── 80014_Emprendimiento\       [SESION_01 a SESION_11]
│   ├── 83706_Prototipos\           [SESION_01 a SESION_10]
│   ├── 83703_Liderazgo\            [SESION_01 a SESION_10]
│   │
│   ├── PLANTILLA_ESTRUCTURA.md      [Guía de organización]
│   ├── procesar_grabaciones.py      [Script indexador]
│   └── README.md                    [Instrucciones]
│
├── INDEX_MAESTRO.md                 [Este archivo — Navegación global]
├── ESTADO_PROYECTO_FINAL.txt        [Documentación de estado]
└── DOCUMENTACION\                   [Otras carpetas del proyecto MACI]
```

---

## 🎯 Próximos Pasos

### Inmediato
- ✅ Verificar F:\MACI\courses\ tiene 6 asignaturas
- ✅ Revisar algunos INDEX.md
- ✅ Confirmar estructura de 10_GRABACIÓN_CLASES\

### Corto Plazo (1-3 días)
- ⏳ Descargar grabaciones desde Canvas/Zoom
- ⏳ Colocar en `10_GRABACIÓN_CLASES\{CURSO_ID}\SESION_{N}\grabacion.mp4`
- ⏳ Ejecutar `python 10_GRABACIÓN_CLASES\procesar_grabaciones.py`

### Mediano Plazo (Con grabaciones)
- ⏳ Invocar agentes para procesar videos
- ⏳ Generar transcripciones automáticas
- ⏳ Crear notas de clase por sesión
- ⏳ Vincular con material de F:\MACI\courses\

### Largo Plazo
- ⏳ Crear guía de estudio integrada (cursos + grabaciones)
- ⏳ Generar secuencia de aprendizaje recomendada
- ⏳ Crear ejercicios y evaluaciones por tema
- ⏳ Busca global semántica por contenido

---

## 📝 Preguntas Frecuentes

| Pregunta | Respuesta |
|----------|-----------|
| ¿Está completo el respaldo? | Sí, para Canvas (100%). 26 URLs externos requieren descarga manual. |
| ¿Dónde veo todos los cursos? | `F:\MACI\INDEX_MAESTRO.md` (aquí) o `F:\MACI\courses\` |
| ¿Cómo agrego grabaciones? | Coloca .mp4 en `10_GRABACIÓN_CLASES\{CURSO}\SESION_{N}\` y ejecuta `procesar_grabaciones.py` |
| ¿Puedo buscar contenido? | Sí, en cursos. Búsqueda global se activa cuando agregues grabaciones. |
| ¿Qué agentes tengo? | 5 agentes especializados (ver sección arriba) |

---

## 🔐 Integridad y Auditoría

Todos los archivos de F:\MACI\courses\ han sido:
- ✅ Descargados desde Canvas API oficial
- ✅ Verificados con SHA-256
- ✅ Auditados contra inventario de Canvas
- ✅ Organizados temáticamente

**Auditoría completa:**
- Reporte: `F:\MACI_RESPALDOS\udec\2026-09-22-001\REPORTE_FINAL_INTEGRADO.md`
- Resumen: `F:\MACI_RESPALDOS\udec\2026-09-22-001\RESUMEN_EJECUTIVO.txt`
- Hashes: `F:\MACI_RESPALDOS\udec\2026-09-22-001\local_inventory.json`

---

**Última actualización:** 2026-09-22 21:14 UTC  
**Generado por:** Claude (Auditor Forense Canvas)  
**Status:** ✅ OPERACIONAL — 6 cursos listos, 54 sesiones para grabaciones listas

---

## 🚀 RESUMEN EJECUTIVO

✅ **Contenido Canvas:** 155 archivos descargados, 100% verificado  
✅ **Organización:** 6 asignaturas × 54 módulos temáticos  
✅ **Grabaciones:** Estructura lista para recibir videos  
✅ **Agentes:** Listos para procesar cuando agregues contenido  
✅ **Navegación:** Índices completos, búsqueda integrada

**LISTO PARA USAR.** Descarga grabaciones y colócalas en 10_GRABACIÓN_CLASES\ para que los agentes las procesen automáticamente.
