# MACI — Fundamentos de Ciencia de Datos (UdeC, T2-2026)

**Estado:** Restructurado (2026-09-25)  
**Autor:** Cristóbal Herrera  
**Repositorio:** https://github.com/cherrera0001/MACI

---

## 🎯 Qué Es MACI

MACI es el repositorio de trabajo de Cristóbal Herrera para:

1. **Proyecto FCD Semestral** — Predicción de precios en Melbourne (2016→2017)
2. **Desafío Galaxy Zoo** — Clasificación de imágenes astronómicas
3. **Datito** — Tutor personal interactivo para Fundamentos de Ciencia de Datos
4. **Reconstrucción Certamen 2** — Documentación de la evaluación

Estructura lógica, navegable, con documentación completa.

---

## ⚡ Inicio Rápido

| Quiero… | Carpeta | Archivo |
|---------|---------|---------|
| **Aprender con Datito** | `07_DATITO/` | [`00_INICIO/00_LEEME.md`](../07_DATITO/00_INICIO/00_LEEME.md) |
| **Ver proyecto Melbourne** | `08_PROYECTO_FCD/` | Análisis + notebooks |
| **Laboratorios (P1-P5)** | `06_LABORATORIOS/` | Ejercicios + soluciones |
| **Clases + transcripciones** | `05_CLASES/` | `.md` + audio |
| **Datos procesados** | `02_DATOS/` | cancer/, melbourne/, etc |
| **Resultados + métricas** | `09_RESULTADOS/` | JSON, CSV, visualizaciones |
| **Scripts (centralizados)** | `03_SCRIPTS/` | datito_*.py, verificar_*.py |
| **Documentación FCD** | `01_DOCUMENTACION/` | Guías, índices, especificaciones |

---

## 📁 Estructura Completa

```
F:\MACI/
│
├── 00_INICIO/                    ← Inicio: README, CLAUDE.md, índices
│   ├── README.md                 (este archivo)
│   ├── CLAUDE.md                 (instrucciones del proyecto)
│   ├── spec.md                   (especificaciones Datito)
│   └── INDEX_MAESTRO.md          (índice general de todo)
│
├── 01_DOCUMENTACION/             ← Documentación del curso FCD
│   ├── 00_INDICE_GENERAL.md      (mapa completo del material)
│   ├── guias/                    (guías temáticas)
│   ├── referencias/              (material de consulta)
│   └── especificaciones/         (definiciones formales)
│
├── 02_DATOS/                     ← Datasets procesados
│   ├── cancer/                   (Wisconsin Diagnostic)
│   ├── melbourne/                (Housing 2016-2017)
│   ├── galaxy-zoo/               (Imágenes astronómicas)
│   └── raw/                      (sin procesar)
│
├── 03_SCRIPTS/                   ← Scripts Python centralizados (41 total)
│   ├── datito_*.py               (tutor: estado, navegación, etc)
│   ├── dashai_*.py               (integración DashAI)
│   ├── procesar_*.py             (procesamiento datos)
│   ├── verificar_*.py            (auditoría: rutas, artefactos, G1/G9)
│   └── probar_*.py               (testing offline)
│
├── 04_NOTEBOOKS/                 ← Análisis interactivos (.ipynb)
│   └── [análisis exploratorios]
│
├── 05_CLASES/                    ← Clases + grabaciones
│   ├── transcripciones/          (faster-whisper + markdown)
│   ├── laminas/                  (presentaciones)
│   ├── mapa_ensenanza.yaml       (quién enseñó qué, cuándo)
│   └── [22 clases ordenadas]
│
├── 06_LABORATORIOS/              ← Prácticos del curso (P1-P5)
│   ├── P1_Pandas/                (vacio + resuelto)
│   ├── P2_Calidad_Datos/
│   ├── P3_Numpy_Descriptivo/
│   ├── P4_Regresion/
│   └── P5_Clasificacion/
│
├── 07_DATITO/                    ← Tutor personal (estructura dedicada)
│   ├── 00_INICIO/                (curriculum, progreso, config)
│   ├── 01_CONCEPTOS/             (21 visuales HTML 01-21)
│   ├── 02_REFERENCIA/            (fuentes, memoria, material)
│   ├── 03_CASOS_ESTUDIO/         (cancer_mama + futuras)
│   ├── 04_EJERCICIOS/            (guías, cuadernillos, certamenes)
│   ├── 05_TRANSFERENCIA/         (datasets sintéticos)
│   ├── 06_AUDITORIAS/            (evaluaciones)
│   ├── 07_BITACORA/              (sesiones por fecha)
│   └── 09_PERSONAL/              (datos privados del alumno)
│
├── 08_PROYECTO_FCD/              ← Proyecto Melbourne + Galaxy Zoo
│   ├── Melbourne/                (análisis temporal 2016→2017)
│   ├── Desafio/                  (Galaxy Zoo clasificación)
│   └── [outputs, reports]
│
├── 09_RESULTADOS/                ← Entregables + métricas
│   ├── melbourne/                (MAE, R², matrices confusion)
│   ├── galaxy-zoo/
│   ├── resultados_temporal.json  (verificados: MAE 188.218, R² 0.757)
│   └── [visualizaciones HTML]
│
├── 10_ARCHIVO/                   ← Histórico (deprecated, old versions)
│   ├── obsoleto_split_aleatorio/ (ejemplo de fuga de información)
│   ├── canvas_respaldos/
│   └── [anteriores iteraciones]
│
└── .claude/
    ├── skills/datito/SKILL.md    (protocolo pedagógico)
    └── [configuración MCP]
```

---

## 🎓 Cómo Usar Este Repositorio

### Para Estudiar (Datito)

```bash
cd F:\MACI
python 03_SCRIPTS/datito_estado.py     # actualizar estado
```

Abre: [`07_DATITO/01_CONCEPTOS/00_index.html`](../07_DATITO/01_CONCEPTOS/00_index.html) en el navegador.

O invoca la skill en Claude Code:
```
/datito
```

### Para Revisar Proyecto Melbourne

```bash
cd F:\MACI
# Ver datos
ls 02_DATOS/melbourne/

# Ver análisis
ls 08_PROYECTO_FCD/Melbourne/

# Ver resultados
cat 09_RESULTADOS/resultados_temporal.json
```

**Cifras verificadas:**
- Train: 6.336 propiedades (2016)
- Test: 7.244 propiedades (2017)
- MAE: **188.218 AUD**
- R²: **0,757**
- ⚠️ 29,1% del test son suburbios NO en train (data leakage risk)

### Para Ejecutar Scripts

**Todos los scripts se ejecutan desde raíz**, no desde `03_SCRIPTS/`:

```bash
cd F:\MACI
python 03_SCRIPTS/datito_estado.py                    # regen estado
python 03_SCRIPTS/construir_navegacion.py             # regen visuales
python 03_SCRIPTS/verificar_artefactos.py             # audit HTML
python 03_SCRIPTS/verificar_g1_g9.py                  # audit garantías
```

---

## 📋 Archivos Especiales

| Archivo | Propósito | Quién modifica |
|---------|-----------|----------------|
| `00_INICIO/CLAUDE.md` | Instrucciones del proyecto | Usuario solo |
| `00_INICIO/spec.md` | Especificaciones Datito (G1-G14) | Usuario solo |
| `07_DATITO/00_INICIO/curriculum.yaml` | 21 conceptos del curso | Lectura (NO editar durante sesión) |
| `07_DATITO/00_INICIO/progreso.yaml` | Estado de aprendizaje | Solo Datito |
| `07_DATITO/00_INICIO/dudas.yaml` | Respuestas dadas en sesión | Solo Datito |
| `07_DATITO/07_BITACORA/*.md` | Sesiones por fecha | Solo Datito |
| `09_RESULTADOS/resultados_temporal.json` | Métricas verificadas | Manual solo |

---

## 🔒 Lo Que NO Cambiar

Protegido (funcional, estable):
- `01_DOCUMENTACION/` — Material del curso
- `07_DATITO/00_INICIO/curriculum.yaml` — Plan pedagógico fijo
- `08_PROYECTO_FCD/` — Proyecto semestral
- `09_RESULTADOS/resultados_temporal.json` — Fuente de verdad

---

## 🛠️ Convenciones

- **Estructura:** Carpetas numeradas por función (`00_` a `10_`)
- **Índices:** Cada carpeta principal tiene `00_INDICE.md` o `README.md`
- **Rutas:** Scripts se ejecutan desde `F:\MACI` (raíz)
- **Etiquetas:** `[EVIDENCIA]`, `[INFERENCIA]`, `[NO EVIDENCIADO]` en documentos
- **Commits:** Mensaje claro + hash verificable en `09_RESULTADOS/`

---

## 📞 Contacto

**Repositorio:** https://github.com/cherrera0001/MACI  
**Branch:** main  
**Credenciales:** Usar `GITHUB_TOKEN_CLASIC` de `.env`

---

**Última actualización:** 2026-09-25 · Restructuración completa (00_INICIO a 10_ARCHIVO)
