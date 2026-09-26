# INVENTARIO FASE 0 — AUDITORÍA Y RECUPERACIÓN DE UX/UI EN DATITO

**Status:** FASE 0 COMPLETA — SIN MODIFICACIONES  
**Fecha:** 2026-09-25  
**Total HTML encontrados:** 25 (+ 2 templates canónicos espejo = 27)

---

## 1. TEMPLATE CANÓNICO IDENTIFICADO

### Ubicación Definitiva:
- **Primario:** `F:\MACI\07_DATITO\01_CONCEPTOS\visual\_TEMPLATE_CANONICO.html`
- **Espejo/Backup:** `F:\MACI\07_DATITO\visual\_TEMPLATE_CANONICO.html` (IDÉNTICO)

### Características del Template:
- **Marker identificador:** `<!-- datito:template:v1 -->`
- **Ubicación del marker:** Línea 5 (tras `<meta charset="utf-8">`)
- **Máximo ancho:** 900px (`main { max-width: 900px; margin: 0 auto; }`)
- **Tipografía:** 16px/1.7 "Segoe UI", system-ui, sans-serif
- **Colores CSS en :root:**
  - `--tinta: #1a1a1a`
  - `--suave: #666`
  - `--linea: #d8d8d8`
  - `--fondo: #faf9f7`
  - `--azul: #2563eb`
  - `--rojo: #dc2626`
  - `--verde: #059669`
  - `--ambar: #d97706`
  - `--morado: #7c3aed`

### Componentes Obligatorios:
- ✅ `.clave` (azul, borde izquierdo #2563eb)
- ✅ `.nota` (ambar, borde izquierdo #d97706)
- ✅ `.peligro` (rojo, borde izquierdo #dc2626)
- ✅ `.cita` (verde, borde izquierdo #059669)
- ✅ `.grafo` (morado, borde izquierdo #7c3aed)
- ✅ `.panel` (caja blanca)
- ✅ `.ecu` (ecuaciones)
- ✅ `.bloque` / `.bloque-titulo`
- ✅ `details` (expandibles genéricas)
- ✅ `details.resp` (respuestas verificadas)
- ✅ `canvas` (para gráficos locales)
- ✅ `button`, `button.alt`
- ✅ `ol.pasos` (listas de pasos)
- ✅ `footer`

### Prohibiciones Explícitas (en comentario del template):
- ❌ CDN: Chart.js remoto, googleapis, fonts.google, unpkg
- ❌ Colores IA: #667eea (azul IA), #764ba2 (púrpura IA)
- ❌ CSS inventado: solo se permite :root tokens
- ❌ Cambiar clases clave: .clave, .nota, .peligro, details.resp
- ❌ Linear-gradient con colores IA
- ❌ Usar fonts.google
- ❌ Scripts sin contenido embebido

---

## 2. DOCUMENTACIÓN EXISTENTE (SIN MODIFICAR)

### Archivos de Estado y Plan:
- ✅ `07_DATITO/MIGRACION_STATUS_2026_09_25.md` — Estado actual (Fase 1 ✅, Fase 2 INICIADA, Fase 3 PENDIENTE)
- ✅ `07_DATITO/07_BITACORA/PLAN_MIGRACION_GLOBAL.md` — Estrategia completa con fases
- ✅ `07_DATITO/07_BITACORA/NAVEGACION_STATUS.md` — Infraestructura de navegación
- ✅ `07_DATITO/00_INICIO/ARQUITECTURA.md` — Diseño del sistema Datito
- ✅ `07_DATITO/07_BITACORA/TECH_DEBT.md` — Deuda técnica anterior

### Archivos de Configuración YAML:
- ✅ `07_DATITO/00_INICIO/clases.yaml` — 22 clases, 17 conceptos
- ✅ `07_DATITO/00_INICIO/curriculum.yaml` — 21 conceptos indexados
- ✅ `07_DATITO/00_INICIO/dudas.yaml` — vacío, listo para preguntas futuras
- ✅ `07_DATITO/00_INICIO/grafo.yaml` — dependencias de conceptos
- ✅ `07_DATITO/00_INICIO/datito.config.yaml` — configuración del alumno

---

## 3. SCRIPTS AUTOMATIZADOS ENCONTRADOS

### Scripts de Evaluación (ACTIVOS):
- ✅ `03_CODIGO/datito_loop_eval.py` — Evalúa UN archivo (11 gates, retorna score 0-1.0)
- ✅ `03_CODIGO/datito_batch_eval.py` — Evalúa LOTE de archivos
- ✅ `03_CODIGO/datito_loop_once.py` — Registra decisión migración en results.tsv
- ✅ `03_CODIGO/datito_migracion_inicio.py` — Genera _NEW.html basado en template

### Scripts de Generación (ACTIVOS):
- ✅ `03_SCRIPTS/generar_index.py` — Genera index.html desde grafo.yaml (150 líneas)
- ✅ `03_SCRIPTS/construir_navegacion.py` — Inyecta nav entre marcadores datito:nav (ERROR CONOCIDO)
- ✅ `03_SCRIPTS/verificar_contrato.py` — Valida 12 garantías del sistema
- ✅ `03_SCRIPTS/verificar_visuales.py` — Audita HTML: sin red, enlaces, citas
- ✅ `03_SCRIPTS/probar_visuales_offline.py` — Abre cada visual en Edge sin red

### Scripts de Ingesta (ACTIVOS):
- ✅ `03_SCRIPTS/transcribir_clases.py` — Video → transcripción Whisper
- ✅ `03_SCRIPTS/integrar_clase.py` — Transcripción → índice de menciones
- ✅ `03_SCRIPTS/grafo_conceptual.py` — Regenera grafo.yaml
- ✅ `03_SCRIPTS/datito_estado.py` — Regenera estado.md (CRÍTICO: correr tras cada sesión)

---

## 4. INVENTARIO COMPLETO DE ARCHIVOS HTML

### ESTADO ACTUAL: EVALUACIÓN DETALLADA (25 archivos)

| # | ARCHIVO | RUTA | MARKER | SCORE | STATUS | PROBLEMAS |
|---|---------|------|--------|-------|--------|-----------|
| 1 | 01_fundamentos.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 2 | 02_datos_features_target.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 3 | 03_eda.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 4 | 04_limpieza_preparacion.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 5 | 05_train_validation_test.html | 01_CONCEPTOS/visual/ | ❌ | 0.7273 | DISCARD | Sin marker |
| 6 | 06_validacion_cruzada.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 7 | 07_generalizacion.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 8 | 08_overfitting_underfitting.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 9 | 09_regresion.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 10 | 10_clasificacion.html | 01_CONCEPTOS/visual/ | ❌ | 0.9091 | DISCARD | Sin marker, CSS personalizado |
| 11 | 11_matriz_confusion.html | 01_CONCEPTOS/visual/ | ❌ | 0.8182 | DISCARD | Sin marker, CSS personalizado |
| 12 | 12_metricas_clasificacion.html | 01_CONCEPTOS/visual/ | ❌ | 0.9091 | DISCARD | Sin marker, CSS personalizado |
| 13 | 13_roc_auc.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 14 | 14_arboles_decision.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 15 | 18_redes_neuronales.html | 01_CONCEPTOS/visual/ | ✅ | 1.0 | KEEP | ninguno |
| 16 | 19_deep_learning.html | 01_CONCEPTOS/visual/ | ❌ | 0.8182 | DISCARD | Sin marker, CSS personalizado |
| 17 | 00_index.html | 01_CONCEPTOS/visual/ | ❌ | 0.5455 | DISCARD | Generado, sin marker |
| 18 | index.html | 01_CONCEPTOS/visual/ | ❌ | 0.4545 | DISCARD | Generado, sin marker |
| 19 | clase6_regresion.html | 02_REFERENCIA/ | ✅ | 1.0 | KEEP | ninguno |
| 20 | matriz_confusion_dinamica.html | 03_CASOS_ESTUDIO/cancer_mama/ | ❌ | 0.7143 | DISCARD | Sin marker, CSS personalizado |
| 21 | certamen_1.html | 04_EJERCICIOS/ | ❌ | 0.9091 | DISCARD | Marker presente pero no reconocido |
| 22 | certamen_2.html | 04_EJERCICIOS/ | ❌ | 0.9091 | DISCARD | Marker presente pero no reconocido |
| 23 | certamen_3.html | 04_EJERCICIOS/ | ✅ | 1.0 | KEEP | ninguno |
| 24 | simulador_prediccion_falla.html | 04_EJERCICIOS/ | ❌ | 0.5 | DISCARD | Plotly CDN remoto |
| 25 | triaje_de_problemas.html | 04_EJERCICIOS/ | ❌ | 0.9091 | DISCARD | Marker presente pero no reconocido |

### RESUMEN POR ESTADO:
- **KEEP (listo, score=1.0):** 13 archivos (52%)
- **DISCARD (necesita migración):** 12 archivos (48%)
- **TOTAL:** 25 archivos

---

## 5. GIT HISTORY — COMMITS QUE TOCARON HTML/CSS

### Últimos 13 commits relevantes:
```
8ae552c Final: Agregar template canónico + plan iteración + .gitignore
b5a965c Add: index.html generado desde grafo.yaml
bed9518 Fase 3: Migración parcial de ejercicios y referencias
cabca76 Fase 2: Migración de 11 conceptos a template v1
00b8428 Implement Datito learning loop: template v1 + Certamen 3 KEEP + migration plan (Fase 1)
aedc8f9 Iter 2: Matriz confusión dinámica con colores por intensidad
bf2496d Refactor: reorganizar estructura Datito (00_INICIO, 01_CONCEPTOS, etc)
77982a9 Session: Integrar caso Wisconsin + herramientas dinámicas + loop simulador
6d22c43 Iter 1: Simulador predicción de falla - scatter plot + controles de umbral
de77e91 Transcribe la ayudantia del 10-jul y la integra: 15 de 15 clases
e97cff0 Ordena los visuales como curso: 22 clases en 6 unidades (spec G14)
0506248 Integra las 14 transcripciones en los visuales y registra lo respondido
95fc08f Anade clasificacion, el concepto mas transversal que quedaba
```

**Conclusión:** El template canónico fue introducido en commit `00b8428` (hace ~3 sesiones). Los archivos DISCARD son de iteraciones anteriores con CSS personalizado.

---

## 6. CONTRATO DEL TEMPLATE v1 (EXTRAÍDO)

### Estructura DOM Obligatoria:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <!-- datito:template:v1 -->  ← MARKER EN LÍNEA 5
  <title>...</title>
  <style>
    :root { --tinta:#1a1a1a; --suave:#666; ... }
    /* CSS aquí, embebido */
  </style>
</head>
<body>
<main>
  <!-- datito:nav:inicio -->
  <!-- navegación inyectada por construir_navegacion.py -->
  <!-- datito:nav:fin -->
  
  <h1>TÍTULO</h1>
  <p class="sub">contexto · curso · fuente</p>
  
  <div class="clave">
    <strong>Qué vas a poder hacer.</strong> Frase observable.
  </div>
  
  <h2>1 · Qué te dan / qué pasó</h2>
  <p>Descripción. Si hay gráfico: cómo se lee.</p>
  
  <h2>2 · Cómo se resuelve</h2>
  <ol class="pasos">
    <li>Paso 1…</li>
  </ol>
  
  <div class="ecu">
    <div class="f">fórmula = aquí</div>
    <p>Explicación simbólica.</p>
  </div>
  
  <details class="resp">
    <summary>Respuesta correcta y cómo se resuelve</summary>
    <p><strong>Respuesta:</strong> …</p>
    <p><strong>Resolución:</strong> …</p>
    <p><strong>Error típico:</strong> …</p>
    <p class="f">[DATITO] o [FUENTE · Repo: ruta · marca]</p>
  </details>
  
  <div class="peligro">
    <strong>Errores que el examen castiga.</strong>
    <ul><li>…</li></ul>
  </div>
  
  <footer>Generado con template canónico Datito v1</footer>
</main>
</body>
</html>
```

### 11 Gates de Validación (datito_loop_eval.py):
1. **template_marker** — presencia de `<!-- datito:template:v1 -->`
2. **anti_cdn** — sin Chart.js, googleapis, fonts.google, unpkg
3. **anti_chart_cdn** — sin chart bibliotecas remotas específicas
4. **anti_ai_gradient** — sin #667eea o #764ba2
5. **has_style_embed** — CSS embebido en `<style>`, no archivos externos
6. **no_http_script_src** — sin scripts de fuentes HTTP inseguras
7. **offline_draw** — si hay gráfico, debe ser Canvas/SVG local
8. **bloque_que_paso** — sección "Qué pasó" presente
9. **bloque_pasos** — lista de pasos (ol.pasos) presente
10. **details_resp** — al menos un `<details class="resp">`
11. **errores** — sección de errores típicos (`.peligro`)

---

## 7. CAUSAS SISTÉMICAS IDENTIFICADAS

### PATRÓN A: "CSS Personalizado Anterior al Template" (5 archivos)
Archivos que NO tienen `<!-- datito:template:v1 -->` y tienen CSS completamente personalizado:
- 05_train_validation_test.html
- 10_clasificacion.html
- 11_matriz_confusion.html
- 12_metricas_clasificacion.html
- 19_deep_learning.html

**Causa:** Fueron diseñados en sesiones 1-3 (anteriores a commit 00b8428) con variables CSS únicas (--perro, --gato, --papel, etc.)

### PATRÓN B: "Marker Presente pero Mal Ubicado o Incompleto" (3 archivos)
Archivos que tienen `<!-- datito:template:v1 -->` pero el script no lo reconoce:
- certamen_1.html
- certamen_2.html
- triaje_de_problemas.html

**Causa INVESTIGAR:** Posible que el marker esté en línea diferente o con espacios/caracteres distintos. Requiere inspección manual.

### PATRÓN C: "Generados, Sin Marker" (2 archivos)
Archivos generados por scripts (no son artefactos de estudio):
- 00_index.html (generado por construir_navegacion.py en fase anterior)
- index.html (generado por generar_index.py)

**Causa:** Son artefactos de navegación, no conceptos. No necesitan cumplir template.

### PATRÓN D: "CDN Remoto" (1 archivo)
- simulador_prediccion_falla.html — Plotly CDN (`<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>`)

**Causa:** Herramienta interactiva que requería Plotly. Requiere migración a Canvas local.

### PATRÓN E: "Generados Dinámicamente, Sin Marker" (1 archivo)
- matriz_confusion_dinamica.html — del caso Wisconsin, CSS personalizado

**Causa:** Herramienta interactiva generada. Requiere revisión si es crítica.

---

## 8. CRITERIOS DE BLOQUEO PARA FASE 1→2

✅ **INVENTARIO 100% COMPLETO:** 25 archivos (+ 2 templates) documentados  
✅ **TEMPLATE CANÓNICO IDENTIFICADO Y DOCUMENTADO:**
   - Ubicación: `F:\MACI\07_DATITO\01_CONCEPTOS\visual\_TEMPLATE_CANONICO.html`
   - Espejo: `F:\MACI\07_DATITO\visual\_TEMPLATE_CANONICO.html`  
✅ **CONTRATO DEL TEMPLATE DEFINIDO:** 11 gates de validación  
✅ **CAUSAS SISTÉMICAS DOCUMENTADAS:** 5 patrones identificados

**PRÓXIMO PASO:** Autorizar FASE 1 (clasificación detallada con herramientas)

---

## 9. REFERENCIAS RÁPIDAS

| Tarea | Archivo/Comando |
|-------|-----------------|
| Ver template canónico | `07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html` |
| Evaluar un archivo | `python 03_CODIGO/datito_loop_eval.py --path <ruta>` |
| Evaluar lote | `python 03_CODIGO/datito_batch_eval.py` |
| Plan migración | `07_DATITO/07_BITACORA/PLAN_MIGRACION_GLOBAL.md` |
| Estado actual | `07_DATITO/MIGRACION_STATUS_2026_09_25.md` |
| Arquitectura | `07_DATITO/00_INICIO/ARQUITECTURA.md` |

---

**FASE 0 COMPLETADA POR:** Senior Frontend Engineer + QA Visual  
**FECHA:** 2026-09-25  
**ESTADO:** LISTO PARA FASE 1 (FASE 2 INICIADA, FASE 3 PENDIENTE)
