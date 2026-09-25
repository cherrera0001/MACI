# Inventario de Fuentes: Aislamiento y Trazabilidad

**Fecha:** 2026-09-22  
**Estado:** En curso — F:\MACI y G:\MACI accesibles; Drive requiere copia manual  
**Objetivo:** Catálogo reproducible de origen → destino antes de migración

---

## Límites de Acceso Registrados

| Fuente | Acceso | Método | Limitación |
|--------|--------|--------|-----------|
| **F:\MACI** | ✅ Directo | Sistema de archivos local | Ninguna |
| **G:\MACI** | ✅ Directo | Sistema de archivos local | Ninguna |
| **Google Drive** | ❌ No disponible | URL: https://drive.google.com/drive/folders/14XEOYf5y72ml4b0N5fdn96A87B8Rvxfi | Requiere navegador o API; no accesible desde IDE |

**Acción:** Usuario debe proporcionar inventario manual de Drive o exportar lista de archivos.

---

## Inventario de G:\MACI (Acceso Directo)

### Estructura Identificada

```
G:\MACI/
├── docs/                          (directorio, no explorado)
├── .playwright-mcp/               (administrativo, ignorar)
├── Fundamentos de Ciencia de datos/
│   ├── Certamen2_Respuestas_Finales.docx    [PERSONAL - expediente]
│   ├── Certamen2_Respuestas_Finales.pdf     [PERSONAL - expediente]
│   ├── 1 (1-4).jpeg                         [PERSONAL - respuestas]
│   └── ...
├── Fundamentos de bases de datos/
│   ├── Cápsula clase 2.mp4
│   ├── Cápsula clase 3.mp4
│   ├── Cápsula clase 4.mp4
│   ├── Cápsula clase 5.mp4
│   ├── Cápsula clase 6.mp4
│   └── GMT20260306-211324_Recording_1920x1080.mp4
├── Python/
│   ├── clase_27_03/                (directorio, no explorado)
│   ├── Ejercicios/                 (directorio, no explorado)
│   └── ejemplo_env.py
├── Emprendimiento e innovación/
│   └── Taller 3 - Emp. Tec - 2026.pdf
├── flujo-login-intranet/           (administrativo, ignorar)
├── .env                            [SECRETO - ignorar]
├── .env.example                    [SECRETO - ignorar]
├── login-udec-exitoso.png          (administrativo, ignorar)
└── console-*.log, page-*.yml       (logs, ignorar)
```

### Cursos Reales en G:\MACI

| Curso | Carpeta | Contenido | Estado |
|-------|---------|----------|--------|
| Fundamentos de BD | `Fundamentos de bases de datos/` | 6 videos de cápsulas | 🟠 Solo videos, sin curriculum |
| Python | `Python/` | Código de ejercicios | 🟠 Estructura incompleta |
| Emprendimiento | `Emprendimiento e innovación/` | 1 taller PDF | 🔴 Mínimo |
| FCD Personal | `Fundamentos de Ciencia de datos/` | Respuestas Certamen 2 | 🔴 PERSONAL (expediente) |

---

## Inventario de F:\MACI (Detalle Necesario)

### A Explorar

Estos directorios requieren inventario con hashes:

```
F:\MACI/
├── 07_DATITO/                    ← Original de tutor
│   ├── curriculum.yaml           [HASH: ?]
│   ├── clases.yaml               [HASH: ?]
│   ├── visual/                   [21 HTMLs - HASH: ?]
│   └── ...
├── courses/fcd-2026-2/           ← Copia (ADR-001)
│   ├── curriculum.yaml           [HASH: ? - DUPLICADO?]
│   ├── clases.yaml               [HASH: ? - DUPLICADO?]
│   ├── visual/                   [HASH: ? - DUPLICADO?]
│   └── ...
├── learners/cristobal_herrera_fcd-2026-2/
│   ├── progreso.yaml             [HASH: ?]
│   ├── dudas.yaml                [HASH: ? - TAMBIÉN EN courses/?]
│   └── ...
├── 06_LABORATORIOS/                  ← Laboratorios
│   ├── [P1-P5] (res).ipynb
│   └── [P1-P5] (vacio).ipynb
├── 05_CLASES/                    ← Transcripciones
│   └── transcripciones/
└── ... (otros legacy)
```

**Próximo paso:** Generar hashes para detectar verdaderos duplicados.

---

## Inventario de Drive (Pendiente - Usuario)

**URL:** https://drive.google.com/drive/folders/14XEOYf5y72ml4b0N5fdn96A87B8Rvxfi

**Formato solicitado:**
```
Carpeta / Archivo | Tipo | Asignatura | Notas
```

**Ejemplo:**
```
/Liderazgo/Clase_1.pdf | PDF | Liderazgo | Material de clase
/Smart_Sense/Prototipo_v1.pptx | PPTX | Emprendimiento + Innovación | Proyecto compartido
```

---

## Proyectos Identificados

| Proyecto | Ubicación | Cursos | Estado |
|----------|-----------|--------|--------|
| **Melbourne** | F:\MACI/08_PROYECTO_FCD/Hito1 + 09_RESULTADOS | FCD | ✅ Completo en F:\ |
| **Galaxy Zoo** | F:\MACI/08_PROYECTO_FCD/Desafio | FCD | ✅ Completo en F:\ |
| **ParkControl** | ? | Prototipado (?) | ❓ Ubicación desconocida |
| **Smart Sense** | ? | Emprendimiento + Innovación | ❓ Ubicación desconocida |

---

## Próxima Acción

### Debe hacer el usuario:

1. **Proporcionar inventario de Drive** (carpetas y archivos principales)
2. **Confirmar ubicación de ParkControl y Smart Sense**
3. **Indicar si hay otros cursos** no mencionados

### Hará el asistente:

1. **Generar hashes** de F:\MACI y G:\MACI para detectar duplicados reales
2. **Crear catálogo completo** con origen → destino propuesto
3. **Diseñar estructura jerárquica** programa → curso → alumno
4. **Proponer manifesto de migración** con verificabilidad

---

**Repositorio:** F:\MACI (commit 55370e5)  
**Acceso:** Aguardando inventario de Drive del usuario
