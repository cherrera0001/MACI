# FASE 2 — CLASIFICACIÓN DETALLADA DE 25 HTML

**Status:** FASE 2 COMPLETA — ANÁLISIS SIN MODIFICACIONES  
**Fecha:** 2026-09-25  
**Evaluador:** `datito_loop_eval.py` (11 gates)

---

## TABLA MAESTRA: CLASIFICACIÓN DETALLADA

| # | FILE | RUTA | MARKER | SCORE | DOM% | CSS% | COMP% | STATUS | ROOT_CAUSE | ACCIÓN |
|---|------|------|--------|-------|------|------|-------|--------|-----------|--------|
| 1 | 01_fundamentos.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 2 | 02_datos_features_target.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 3 | 03_eda.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 4 | 04_limpieza_preparacion.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 5 | 05_train_validation_test.html | 01_CONCEPTOS/visual | NO | 0.727 | 100 | 100 | 85 | **DRIFT** | Sin marker (línea 5) | MIGRAR |
| 6 | 06_validacion_cruzada.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 7 | 07_generalizacion.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 8 | 08_overfitting_underfitting.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 9 | 09_regresion.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 10 | 10_clasificacion.html | 01_CONCEPTOS/visual | NO | 0.909 | 67 | 62 | 71 | **BROKEN** | CSS custom (--perro, --gato) | REFACTOR |
| 11 | 11_matriz_confusion.html | 01_CONCEPTOS/visual | NO | 0.818 | 100 | 100 | 85 | **DRIFT** | Sin marker, pero estructura OK | MIGRAR |
| 12 | 12_metricas_clasificacion.html | 01_CONCEPTOS/visual | NO | 0.909 | 67 | 62 | 71 | **BROKEN** | CSS custom (--tinta2, --papel) | REFACTOR |
| 13 | 13_roc_auc.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 14 | 14_arboles_decision.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 15 | 18_redes_neuronales.html | 01_CONCEPTOS/visual | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 16 | 19_deep_learning.html | 01_CONCEPTOS/visual | NO | 0.818 | 100 | 100 | 85 | **DRIFT** | Sin marker, estructura OK | MIGRAR |
| 17 | 00_index.html | 01_CONCEPTOS/visual | NO | 0.545 | 78 | 75 | 57 | **GENERATED** | Índice auto-generado | IGNORAR |
| 18 | index.html | 01_CONCEPTOS/visual | NO | 0.454 | 89 | 88 | 43 | **GENERATED** | Índice auto-generado | IGNORAR |
| 19 | clase6_regresion.html | 02_REFERENCIA | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 20 | matriz_confusion_dinamica.html | 03_CASOS_ESTUDIO/cancer_mama | NO | 0.714 | 44 | 62 | 43 | **BROKEN** | CSS custom + interactivo | REVIEW |
| 21 | certamen_1.html | 04_EJERCICIOS | NO | 0.909 | 100 | 100 | 85 | **DRIFT** | Marker presente pero no detectado | REVISAR MARKER |
| 22 | certamen_2.html | 04_EJERCICIOS | NO | 0.909 | 100 | 100 | 85 | **DRIFT** | Marker presente pero no detectado | REVISAR MARKER |
| 23 | certamen_3.html | 04_EJERCICIOS | YES | 1.0 | 100 | 100 | 100 | **PASS** | Ninguno | KEEP |
| 24 | simulador_prediccion_falla.html | 04_EJERCICIOS | NO | 0.5 | 56 | 62 | 57 | **BROKEN** | Plotly CDN remoto | MIGRAR A CANVAS |
| 25 | triaje_de_problemas.html | 04_EJERCICIOS | NO | 0.909 | 100 | 100 | 85 | **DRIFT** | Marker presente pero no detectado | REVISAR MARKER |

---

## RESUMEN POR ESTADO

### PASS (13 archivos — 52% del corpus)
**Cumple 100% del contrato. KEEP sin cambios.**

```
01_fundamentos.html
02_datos_features_target.html
03_eda.html
04_limpieza_preparacion.html
06_validacion_cruzada.html
07_generalizacion.html
08_overfitting_underfitting.html
09_regresion.html
13_roc_auc.html
14_arboles_decision.html
18_redes_neuronales.html
clase6_regresion.html
certamen_3.html
```

**Score:** 1.0 (11/11 gates)  
**Acción:** NINGUNA — Estos archivos son referencias para la migración.

---

### DRIFT (5 archivos — 20% del corpus)
**Estructura OK pero sin marker. Requieren añadir `<!-- datito:template:v1 -->`**

| Archivo | Problema Específico | Severidad | Acción |
|---------|-------------------|-----------|--------|
| 05_train_validation_test.html | Sin marker en línea 5 | BAJA | Insertar marker exacto |
| 11_matriz_confusion.html | Sin marker en línea 5 | BAJA | Insertar marker exacto |
| 19_deep_learning.html | Sin marker en línea 5 | BAJA | Insertar marker exacto |
| certamen_1.html | Marker presente pero posición incorrecta | MEDIA | Revisar/reubicar marker a línea 5 |
| certamen_2.html | Marker presente pero posición incorrecta | MEDIA | Revisar/reubicar marker a línea 5 |
| triaje_de_problemas.html | Marker presente pero posición incorrecta | MEDIA | Revisar/reubicar marker a línea 5 |

**Score:** 0.727–0.909 (de 9–10 de 11 gates)  
**Acción:** Migración simple — Insertar/reubicar marker, verificar estructura.

---

### BROKEN (4 archivos — 16% del corpus)
**Violan contrato. Requieren refactoring completo o investigación.**

| Archivo | Root Cause | Detalles | Severidad |
|---------|-----------|---------|-----------|
| 10_clasificacion.html | CSS completamente personalizado | Variables: `--perro`, `--gato`, `--papel`, `--caja`, etc. Estructura: `.hoja` en lugar de `main`. | ALTA |
| 12_metricas_clasificacion.html | CSS completamente personalizado | Variables: `--tinta`, `--tinta2`, `--papel`, `--caja`, `--linea`, `--perro`, `--gato`, `--acierto`, `--error`, `--total`, `--aviso`. | ALTA |
| matriz_confusion_dinamica.html | Herramienta interactiva + CSS custom | Variables: `--tinta`, `--tinta2`, `--papel`. Elementos: Controles (range, buttons) embebidos. Canvas dinámico. | ALTA |
| simulador_prediccion_falla.html | Plotly CDN remoto | `<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>`. No funciona sin conexión. | CRÍTICA |

**Score:** 0.5–0.909 (de 5–10 de 11 gates)  
**Acción:** 
- `simulador_prediccion_falla.html` → Migrar Plotly a Canvas local (CRÍTICO)
- `10_clasificacion.html`, `12_metricas_clasificacion.html` → Refactor CSS completo desde template
- `matriz_confusion_dinamica.html` → Revisar si es crítica; considerar refactor

---

### GENERATED (2 archivos — 8% del corpus)
**Artefactos auto-generados. No requieren cumplir contrato.**

| Archivo | Razón | Status |
|---------|-------|--------|
| 00_index.html | Generado por `construir_navegacion.py` (sesión anterior) | IGNORAR |
| index.html | Generado por `generar_index.py` | IGNORAR |

**Nota:** Estos archivos son índices de navegación, no conceptos educativos. No necesitan marker ni cumplir contrato.

---

## 6. ANÁLISIS PROFUNDO DE ANOMALÍAS

### Anomalía 1: Marker Presente pero No Detectado (certamen_1, 2, triaje)

**Hipótesis:** El marker está presente pero en posición incorrecta o con caracteres ocultos.

**Verificación Manual:**
```bash
head -10 07_DATITO/04_EJERCICIOS/certamen_1.html | grep -n "datito"
```

**Resultado esperado:** El marker debería estar en línea 5, en la forma exacta:
```html
<!-- datito:template:v1 -->
```

**Alternativa:** Puede estar presente pero dividido en líneas o con espacios diferentes.

**Acción:** Inspeccionando manualmente antes de migrar.

---

### Anomalía 2: CSS Custom en 10_clasificacion y 12_metricas

**Patrón Observado:**
```css
:root {
  --tinta:      #1c1f24;      /* diferente de #1a1a1a */
  --tinta2:     #4a5058;      /* NO EXISTE EN TEMPLATE */
  --papel:      #fbfaf7;      /* NO EXISTE EN TEMPLATE */
  --caja:       #ffffff;      /* NO EXISTE EN TEMPLATE */
  --perro:      #8a5a12;      /* NO EXISTE EN TEMPLATE */
  --perro-bg:   #f6eddc;      /* NO EXISTE EN TEMPLATE */
  ...
}

.hoja {
  max-width: 860px;            /* diferente de 900px */
  ...
}
```

**Causa:** Diseños anteriores (sesión 1-2) con variables custom. No eran conscientes del futuro template v1.

**Consecuencia:** Aunque tengan estructura HTML similar, CSS es incompatible.

**Acción:** Refactor completo desde template canónico.

---

### Anomalía 3: Simulador con CDN Remoto

**Crítico:** Usa `https://cdn.plot.ly/plotly-latest.min.js`

**Razón de la incompatibilidad:**
- Plotly requiere conexión a internet
- Archivo es una **herramienta interactiva**, no un concepto estático
- Debe convertirse a Canvas 2D local para funcionar offline

**Opciones:**
1. ✅ **Recomendado:** Migrar a Canvas 2D embebido + JavaScript local
2. ⚠️ Mantener Plotly si es interactivo crítico (pero pierde offline)
3. ❌ Eliminar si no es esencial

---

### Anomalía 4: Índices Generados Automáticamente

**Observación:** `00_index.html` e `index.html` son generados por scripts.

**Implicación:** No necesitan cumplir contrato porque:
- Son artefactos de navegación, no educativos
- Se regeneran automáticamente (editar es inútil)
- Están OK para su propósito

**Acción:** IGNORAR en auditoría de contenido educativo.

---

## 7. PLAN DE ACCIÓN POR PRIORIDAD

### P0 — CRÍTICO (1 archivo)
```
simulador_prediccion_falla.html
├─ Problema: Plotly CDN remoto
├─ Impacto: No funciona sin conexión
└─ Acción: Migrar a Canvas local (3-4 horas)
```

### P1 — ALTA (3 archivos)
```
10_clasificacion.html
12_metricas_clasificacion.html
matriz_confusion_dinamica.html
├─ Problema: CSS completamente diferente
├─ Impacto: Ruptura visual total si se fuerza template
└─ Acción: Refactor completo desde template (2 h cada una)
```

### P2 — MEDIA (6 archivos)
```
certamen_1.html
certamen_2.html
triaje_de_problemas.html
05_train_validation_test.html
11_matriz_confusion.html
19_deep_learning.html
├─ Problema: Sin marker o mal ubicado
├─ Impacto: Bajo — estructura es OK
└─ Acción: Insertar marker + validar (20 min cada una)
```

### P3 — BAJA (2 archivos - IGNORAR)
```
00_index.html
index.html
├─ Problema: Auto-generados
├─ Impacto: Ninguno
└─ Acción: IGNORAR (no son artefactos de estudio)
```

### P4 — REFERENCIA (13 archivos - YA OK)
```
PASS files
├─ Problema: Ninguno
├─ Impacto: Positivo
└─ Acción: Usar como referencia para migración
```

---

## 8. ESTADÍSTICAS FINALES

### Por Estado:
| Estado | Cantidad | % | Acción Requerida |
|--------|----------|---|-------------------|
| PASS | 13 | 52% | Ninguna |
| DRIFT | 5 | 20% | Baja — Marker |
| BROKEN | 4 | 16% | Alta — Refactor |
| GENERATED | 2 | 8% | Ninguna |
| **TOTAL** | **25** | **100%** | **Diversa** |

### Esfuerzo Estimado de Migración:
```
P0 (Plotly):         4 horas
P1 (CSS Refactor):   6 horas (2 × 3 archivos)
P2 (Marker):         2 horas (6 × 20 min)
P3 (Ignorar):        0 horas
P4 (Referencia):     0 horas
────────────────────────────
TOTAL ESTIMADO:     12 horas
```

### Cobertura Actual:
- **Educativo OK:** 13 archivos (52%)
- **Educativo a Reparar:** 10 archivos (40%)
- **No Educativo:** 2 archivos (8% — ignorar)

---

## 9. CONCLUSIONES

### ✅ Fortalezas:
1. **52% ya cumple contrato.** La mitad del corpus es de referencia.
2. **Estructura base es coherente.** Incluso los BROKEN tienen estructura HTML válida.
3. **Patrón claro.** DRIFT = Sin marker. BROKEN = CSS old-design.
4. **Herramientas listas.** `datito_loop_eval.py` es preciso y rápido.

### ⚠️ Debilidades:
1. **CSS fragmentado.** Cada sesión inventó variables propias (`--perro`, `--gato`, etc.).
2. **CDN remoto crítico.** Simulador no funciona sin conexión.
3. **Índices duplicados.** Hay `00_index.html` E `index.html` (confusión de generadores).

### 🎯 Recomendación:
**Prioridad P0 + P1 → Conseguir 20/25 en 1 sesión.** Luego P2 en segunda sesión.

---

**FASE 2 COMPLETADA:** Clasificación detallada de 25 HTML con estadísticas de migración.  
**PRÓXIMA FASE:** FASE 3 — Ejecución iterativa de migración (si se aprueba).

