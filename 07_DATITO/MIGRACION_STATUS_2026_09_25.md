# Migración Global → Template Canónico v1
## Status Report — 2026-09-25

---

## 📊 RESUMEN EJECUTIVO

| Métrica | Valor |
|---|---|
| **Total HTML bajo 07_DATITO** | 24 archivos |
| **KEEP (cumple template v1)** | 1 ✅ |
| **DISCARD (necesita migración)** | 23 |
| **Fase completada** | Fase 1 (Crítico: Certamen 3) |
| **Score certamen3_examen_fcd2026.html** | 1.0 / 1.0 (5/5 gates) ✅ |

---

## ✅ FASE 1: CRÍTICO (Certamen 3) — COMPLETADO

### Archivo 1: `visual/certamen3_examen_fcd2026.html`

| Métrica | Antes | Después |
|---|---|---|
| Status | DISCARD (0.8) | **KEEP (1.0)** ✅ |
| Cambios | template marker + colores IA | +`<!-- datito:template:v1 -->` + #667eea→#2563eb + #764ba2→#7c3aed |
| Gates OK | 9/11 | **11/11** ✅ |

**Gates pasados:**
```
✓ template_marker
✓ anti_cdn
✓ anti_chart_cdn
✓ anti_ai_gradient
✓ has_style_embed
✓ no_http_script_src
✓ offline_draw
✓ bloque_que_paso
✓ bloque_pasos
✓ details_resp
✓ errores
```

### Archivo 2: `visual/certamen3_p1a_roc_detallado.html`

| Métrica | Status |
|---|---|
| Score | 0.2857 / 1.0 ❌ |
| Gates OK | 2/11 |
| Problema principal | Tiene Chart.js CDN (anti_cdn FALLA) |
| Acción | **Requiere migración completa desde template v1** |

---

## 📋 FASE 2: IMPORTANTE (Conceptos 01-14, 18-19)

**17 archivos listos para migración iterativa.**

### Orden sugerido (por frecuencia de uso):
1. `01_fundamentos.html` ← **INICIADO** (01_fundamentos_NEW.html creado)
2. `03_eda.html`
3. `08_overfitting_underfitting.html`
4. `13_roc_auc.html`
5. `11_matriz_confusion.html`
6. `12_metricas_clasificacion.html`
7. Resto (02, 04-07, 09-10, 14, 18-19)

### Script iniciador disponible:
```bash
python 03_CODIGO/datito_migracion_inicio.py --archivo <nombre>
```
Genera archivo `_NEW.html` basado en template canónico con guía paso a paso.

---

## 📋 FASE 3: SECUNDARIO (Ejercicios, referencias, casos)

**7 archivos para migración posterior:**
- `04_EJERCICIOS/certamen_1.html`
- `04_EJERCICIOS/certamen_2.html`
- `04_EJERCICIOS/simulador_prediccion_falla.html`
- `04_EJERCICIOS/triaje_de_problemas.html`
- `02_REFERENCIA/clase6_regresion.html`
- `03_CASOS_ESTUDIO/cancer_mama/matriz_confusion_dinamica.html`

---

## 📁 ARCHIVOS ENTREGADOS

### Documentación
- ✅ `07_DATITO/07_BITACORA/PLAN_MIGRACION_GLOBAL.md` — Estrategia completa
- ✅ `07_DATITO/07_BITACORA/learning_loop/WORKFLOW_VISUAL.md` — Piezas del sistema
- ✅ `07_DATITO/07_BITACORA/learning_loop/program_loop.md` — Protocolo
- ✅ `07_DATITO/07_BITACORA/learning_loop/agent_lessons.yaml` — Lecciones (VIZ-FAIL-001, VIZ-FAIL-002)

### Scripts
- ✅ `03_CODIGO/datito_loop_eval.py` — Evaluación individual (9 gates)
- ✅ `03_CODIGO/datito_batch_eval.py` — Auditoría en batch
- ✅ `03_CODIGO/datito_migracion_inicio.py` — Generador de base _NEW

### Template canónico
- ✅ `07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html` — Único permitido
- ✅ `07_DATITO/visual/_TEMPLATE_CANONICO.html` — Espejo

---

## 🔧 CÓMO CONTINUAR (Próximas sesiones)

### Para Fase 2 (Conceptos):
```bash
# 1. Generar _NEW con guía
python 03_CODIGO/datito_migracion_inicio.py --archivo 03_eda.html

# 2. Editar 03_eda_NEW.html manualmente:
#    - Copiar contenido pedagógico del viejo
#    - Usar estructura template v1 (h2, details, .clave, etc)
#    - No usar CDN ni colores #667eea/#764ba2

# 3. Evaluar
python 03_CODIGO/datito_loop_eval.py --path 07_DATITO/01_CONCEPTOS/visual/03_eda_NEW.html

# 4. Si score=1.0: Loguear y reemplazar
python 03_CODIGO/datito_loop_once.py --path … --hypothesis "migrate to template v1"
mv 03_eda_NEW.html 03_eda.html
```

### Para Fase 3 (Ejercicios):
Mismo flujo, pero considerar que pueden tener estructura "Qué pasó + Pasos + Details.resp + Errores" (VIZ-FAIL-002).

---

## 🚫 PROHIBICIONES (Recuerda)

❌ Chart.js CDN  
❌ Gradiente #667eea o #764ba2  
❌ Fonts.google  
❌ CSS inventado (solo :root)  
❌ Cambiar clases clave (.clave, .nota, .peligro, details.resp)  
❌ Declarar "listo" sin score=1.0 en datito_loop_eval.py  

---

## 📈 PROGRESO ESPERADO

| Fase | Archivos | Est. Tiempo | Target |
|---|---|---|---|
| 1 ✅ | 1 OK + 1 TODO | 30 min | Certamen 3 completo |
| 2 | 12-17 | 3-4 horas | Conceptos core |
| 3 | 6-7 | 1-1.5 horas | Ejercicios + ref |
| **Total** | **24** | **~5 horas** | **100% KEEP** |

---

## 🎯 CRITERIO DE ÉXITO FINAL

```bash
# Cuando TODOS los HTML cumplan:
grep -r "<!-- datito:template:v1 -->" 07_DATITO/**/*.html | wc -l
# Resultado esperado: 24 (todos)

# Cero ocurrencias de colores IA:
grep -r "#667eea\|#764ba2" 07_DATITO/**/*.html
# Resultado esperado: (vacío — ningún resultado)

# Script de verificación final:
python 03_CODIGO/datito_batch_eval.py
# Resultado esperado: "KEEP (ya cumplen template v1): 24"
```

---

## 📞 REFERENCIA RÁPIDA

| Tarea | Comando |
|---|---|
| Auditar todos | `python 03_CODIGO/datito_batch_eval.py` |
| Evaluar uno | `python 03_CODIGO/datito_loop_eval.py --path <archivo>` |
| Iniciar migración | `python 03_CODIGO/datito_migracion_inicio.py --archivo <nombre>` |
| Loguear decisión | `python 03_CODIGO/datito_loop_once.py --path <archivo> --hypothesis "..."` |
| Ver template | `07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html` |

---

**Generado:** 2026-09-25  
**Responsable:** /datito-loop  
**Status:** Fase 1 ✅ KEEP | Fase 2 INICIADA | Fase 3 PENDIENTE

