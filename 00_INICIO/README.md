# MACI — Plataforma de Aprendizaje Semestral (UdeC, T2-2026)

**Estado:** `FASE-0: CLI unificada` (en construcción)  
**Cobertura:** 4/6 cursos (66%) · 29 videos · 43 documentos · 18 ejercicios  
**Repositorio:** https://github.com/cherrera0001/MACI

---

## 🎯 Qué Es MACI

MACI es una plataforma en construcción que integra:
1. **Instancia FCD** — Proyecto semestral + Datito tutor (estable, no cambiar)
2. **6 cursos Canvas** — 80014, 80038, 80714, 83703, 83706, 83707 (procesados)
3. **CLI unificada** — `platform.py` para gestionar cursos sin scripts clonados

**Veredicto actual:** NO_PLATAFORMA → PLATAFORMA_PARCIAL (arquitectura activa)

---

## ⚡ Inicio Rápido (60 segundos)

```bash
# Ver estado de cada curso
python platform.py status

# Ver reporte + cobertura
python platform.py report

# Procesar un curso (futuro: DÍA 2)
python platform.py process --course 80014
```

| Quiero… | Abre… |
|---------|-------|
| **Estudiar FCD con Datito** | `01_DOCUMENTACION/` + `07_DATITO/` |
| **Ver 6 cursos Canvas** | `courses/` + `10_GRABACIÓN_CLASES/` |
| **Arquitectura + plan** | [`README_ARQUITECTO.md`](README_ARQUITECTO.md) |
| **Diagnóstico honesto** | [`PLATAFORMA_COHERENCIA_GAP.md`](PLATAFORMA_COHERENCIA_GAP.md) |
| **Implementación FASE-0** | [`FASE-0-IMPLEMENTACION.md`](FASE-0-IMPLEMENTACION.md) |

---

## 📊 Capacidades por Curso

```
python platform.py report
```

| Curso | Videos | Notas | Ejercicios | Estado |
|-------|--------|-------|-----------|--------|
| 80014_Emprendimiento | ❌ | ✅ (6) | ✅ (6) | ✅ Completo |
| 80038_Procesos_Innovacion | ✅ (5) | ✅ (5) | ❌ | ✅ Completo |
| 80714_Fundamentos_BD | ✅ (16) | ❌ | ❌ | ⚠️ Parcial |
| 83706_Prototipos | ✅ (8) | ❌ | ❌ | ⚠️ Parcial |
| 83703_Liderazgo | ❌ | ❌ | ❌ | ❌ Vacío |
| 83707_Ciencias_Datos | ❌ | ❌ | ❌ | ❌ Vacío |

---

## 🏗️ Estructura

```
F:\MACI/
├── 03_CODIGO/maci_platform/          ← CLI unificada (NUEVO)
├── courses.yaml                       ← Manifesto centralizado (NUEVO)
├── platform.py                        ← Wrapper usuario (NUEVO)
│
├── 01_DOCUMENTACION/                  ← FCD instance (PROTEGIDO)
├── 07_DATITO/                         ← Tutor pedagógico (PROTEGIDO)
│
├── courses/                           ← 6 cursos Canvas
├── 10_GRABACIÓN_CLASES/               ← 29 videos integrados
│
├── README_ARQUITECTO.md               ← Diagnóstico
├── PLATAFORMA_COHERENCIA_GAP.md       ← Mentiras vs hechos
├── ADR-003-PLATAFORMA-UNIFICADA.md    ← Diseño
├── FASE-0-IMPLEMENTACION.md           ← Plan 5 días
└── ESTADO_PROYECTO_FINAL.txt          ← Status actual
```

---

## 🚀 Próximas Fases

**FASE-0** (esta semana):
- ✅ DÍA 1: CLI + manifesto (HECHO)
- ⏳ DÍA 2-3: Procesadores legacy
- ⏳ DÍA 4: Documentación
- ⏳ DÍA 5: Testing

**FASE-1** (2-3 semanas):
- Multi-estudiante (learners/<id>/)
- Parametrizar Datito por curso

**FASE-2+** (2-3 meses):
- API REST + Web UI
- Database backend
- Evaluación automática

---

## 📚 Documentación Clave

| Documento | Qué es | Para quién |
|-----------|--------|-----------|
| [`README_ARQUITECTO.md`](README_ARQUITECTO.md) | Diagnóstico honesto: NO_PLATAFORMA actual | Arquitectos, PMs |
| [`PLATAFORMA_COHERENCIA_GAP.md`](PLATAFORMA_COHERENCIA_GAP.md) | Mentiras en README vs hechos en disco | Auditores |
| [`ADR-003-PLATAFORMA-UNIFICADA.md`](ADR-003-PLATAFORMA-UNIFICADA.md) | Diseño de 3 capas (sin destruir nada) | Implementadores |
| [`FASE-0-IMPLEMENTACION.md`](FASE-0-IMPLEMENTACION.md) | Checklist 5 días con código | Developers |
| [`ESTADO_PROYECTO_FINAL.txt`](ESTADO_PROYECTO_FINAL.txt) | Status actual + métricas | Todos |

---

## 💻 Para Desarrolladores

**Instalar:**
```bash
pip install click pyyaml
```

**Desarrollo:**
```bash
python platform.py --help
python -m maci_platform --help  # o así
```

**Tests:**
- [ ] `status` lista 6 cursos
- [ ] `report` muestra 4/6 = 66%
- [ ] UTF-8 sin errores Windows
- [ ] No hay `procesar_*.py` en raíz (van a 99_ARCHIVE/ en DÍA 3)

---

## 🔒 Lo Que NO Cambiar

Protegido (estable, funcional):
- `01_DOCUMENTACION/` — Instancia FCD semestral
- `02_PROYECTO_FCD/` — Proyecto Melbourne + Galaxy Zoo
- `07_DATITO/` — Core pedagógico
- `MACI_RESPALDOS/` — Backup Canvas

---

## 📞 Contacto & Contribuciones

**Repositorio:** https://github.com/cherrera0001/MACI  
**Branch:** main  
**Token:** GITHUB_TOKEN_CLASIC (en `.env`)

Para reportar errores o sugerir mejoras: revisar `PLATAFORMA_COHERENCIA_GAP.md` primero.

---

**Última actualización:** 2026-09-23 · FASE-0 DÍA 1
