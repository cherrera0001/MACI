# Fase 2B: Gráficos Pendientes (5 archivos)

**Status:** ANÁLISIS COMPLETADO — Requiere conversión manual

---

## Resumen

5 de 26 archivos fallan el gate `offline_draw` porque **mencionan ROC/FPR/TPR pero no tienen gráficos embebidos (canvas/SVG)**.

| Archivo | Gate Falla | Menciones | Problema |
|---------|-----------|-----------|----------|
| 05_train_validation_test.html | offline_draw | "roc" | Sin gráfico |
| 11_matriz_confusion.html | offline_draw | "FPR", "ROC", "TPR" | Sin gráfico |
| 19_deep_learning.html | offline_draw | "canvas", "roc" | Placeholder sin datos |
| certamen_1.html | offline_draw | "roc" | Sin gráfico |
| certamen_2.html | offline_draw | "Canvas", "FPR", "ROC", "TPR" | Imágenes Canvas no recuperadas |

---

## Por qué Falla

El evaluador `datito_loop_eval.py` detecta:

```python
mentions_chart = bool(re.search(r"<canvas|roc|FPR|TPR", live, re.I))
if mentions_chart:
    g["offline_draw"] = bool(
        re.search(r"<canvas|</svg>|getContext\(\s*['\"]2d['\"]", live, re.I)
    )
```

- Si menciona ROC/FPR/TPR → espera `<canvas>` o `</svg>`
- Si no hay gráfico → score baja (9/11 gates)

---

## Soluciones Posibles

### Opción 1: Agregar SVG Simple
Insertar `<svg>` con curva ROC/matriz básica:
```html
<svg width="300" height="300" style="border:1px solid #ddd">
  <!-- Dibujar curva ROC o matriz confusión -->
</svg>
```
**Tiempo:** ~10 min por archivo

### Opción 2: Agregar Canvas Embebido
```html
<canvas id="roc-chart"></canvas>
<script>
  const ctx = document.getElementById('roc-chart').getContext('2d');
  // Dibujar puntos/líneas de ROC
</script>
```
**Tiempo:** ~15 min por archivo (sin librerías CDN)

### Opción 3: Sacar Menciones
Cambiar "ROC" → "curva de decisión", "FPR" → "tasa falsa", "TPR" → "tasa verdadera"
**Tiempo:** ~5 min por archivo (menos pedagógico)

### Opción 4: DISCARD + Nota
Dejar como DISCARD, documentar que el gráfico debe recuperarse de Canvas.
**Tiempo:** 0 min (ya hecho)

---

## Recomendación

**→ Opción 1 (SVG Simple)** porque:
- Mantenible sin dependencias
- Pedagógicamente clara
- ~50 min para 5 archivos
- Puede hacerse en sesión separada

---

## Próximo Paso

```bash
# Si se decide hacer Opción 1:
python 03_CODIGO/agregar_svg_roc.py --archivo certamen_2.html
python 03_CODIGO/datito_loop_eval.py --path 07_DATITO/04_EJERCICIOS/certamen_2.html
# Si score=1.0 → KEEP
```

---

**Status:** BLOQUEADO EN CONVERSIÓN MANUAL
**Prioridad:** BAJA (13/26 ya KEEP es buen resultado)
**Effort:** ~1 hora total (5 archivos × 10-15 min)
