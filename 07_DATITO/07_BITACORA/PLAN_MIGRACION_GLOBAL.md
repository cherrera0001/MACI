# Plan Migración Global → Template Canónico v1

**Status:** 24/24 HTML necesitan migración  
**Fecha:** 2026-09-25  
**Responsable:** /datito-loop

---

## Prioridad y Orden

### Fase 1: CRÍTICO (Certamen 3) ✅ DONE
- `07_DATITO/visual/certamen3_examen_fcd2026.html` 
- `07_DATITO/visual/certamen3_p1a_roc_detallado.html`
- **Status:** Verificar que cumplan template v1
- **Comando:** `python 03_CODIGO/datito_loop_eval.py --path <archivo>`
- **Resultado esperado:** score=1.0 (5/5 gates)

### Fase 2: IMPORTANTE (Conceptos 01-14, 18-19)
Estos son material de **estudio activo** de Cristóbal.
- 01_fundamentos.html → ROC, métricas, matrices
- 03_eda.html, 08_overfitting_underfitting.html, 13_roc_auc.html (frecuentemente usados)
- Resto: migrar en segunda pasada

**Estrategia por archivo:**
```
Para CADA archivo:
1. Leer contenido actual (extraer solo <body>, tablas, detalles pedagógicos)
2. Copiar _TEMPLATE_CANONICO.html como base
3. Reemplazar solo: title, h1, .sub, main (tras nav)
4. Mantener intacto: :root, clases (.clave/.nota/.peligro/details.resp)
5. Evaluar: python 03_CODIGO/datito_loop_eval.py --path <archivo>
6. Si OK (score=1.0): Loguear con datito_loop_once.py
7. Si FALLA: Revisar qué gate falló y corregir
```

### Fase 3: SECUNDARIO (Ejercicios, referencias, casos estudio)
- 04_EJERCICIOS/*.html
- 02_REFERENCIA/clase6_regresion.html
- 03_CASOS_ESTUDIO/cancer_mama/matriz_confusion_dinamica.html

---

## Checklist por Archivo

| Archivo | Template v1 | Anti-CDN | Anti-Gradient | Canvas-Local | Profundidad | Status |
|---|---|---|---|---|---|---|
| certamen3_examen_fcd2026.html | ✓ | ✓ | ✓ | ✓ | ✓ | VERIFICAR |
| certamen3_p1a_roc_detallado.html | ✓ | ✓ | ✓ | ✓ | ✓ | VERIFICAR |
| 01_fundamentos.html | - | - | - | - | - | TODO |
| 02_datos_features_target.html | - | - | - | - | - | TODO |
| ... (21 más) | - | - | - | - | - | TODO |

---

## Gates (5/5 para KEEP)

1. **template_marker:** `<!-- datito:template:v1 -->` ← obligatorio
2. **anti_cdn:** Sin Chart.js, googleapis, fonts.google, unpkg
3. **anti_ai_gradient:** Sin #667eea, #764ba2 (colores IA generadora)
4. **offline_canvas_ok:** Si hay gráfico: Canvas/SVG local (no remoto)
5. **profundidad_min:** Si es certamen/ejercicio: Qué pasó + Pasos + Details.resp + Errores

---

## Patrón de Migración Manual (paso a paso)

### Paso 0: Preparar
```bash
# Copiar template como base
cp 07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html 07_DATITO/01_CONCEPTOS/visual/01_fundamentos_NEW.html
```

### Paso 1: Editar contenido (SOLO reemplazar esto)
```html
<title>Fundamentos en Ciencia de Datos · Datito</title>

<h1>Fundamentos en Ciencia de Datos</h1>
<p class="sub">Qué es ML · etapas básicas · por qué importa</p>

<div class="clave">
  <strong>Qué vas a poder hacer.</strong> Dibujar el pipeline datos→modelo→predicción.
</div>

<!-- Contenido pedagógico del 01_fundamentos.html viejo, adaptado:
     - Títulos h2/h3
     - Tablas (usar <table>, no divs)
     - Gráficos (Canvas/SVG local)
     - <details> para expandibles
     - <details class="resp"> para respuestas
     - .nota, .clave, .peligro si aplica
-->
```

### Paso 2: Verificar
```bash
python 03_CODIGO/datito_loop_eval.py --path 07_DATITO/01_CONCEPTOS/visual/01_fundamentos_NEW.html
# Espera: exit 0 (KEEP) o exit 1 (DISCARD)
```

### Paso 3: Loguear
```bash
python 03_CODIGO/datito_loop_once.py \
  --path 07_DATITO/01_CONCEPTOS/visual/01_fundamentos_NEW.html \
  --hypothesis "migrate 01_fundamentos to template v1"
# Append a results.tsv
```

### Paso 4: Reemplazar original
```bash
mv 07_DATITO/01_CONCEPTOS/visual/01_fundamentos_NEW.html 07_DATITO/01_CONCEPTOS/visual/01_fundamentos.html
```

---

## Script Starter (migración semi-automática)

**Disponible en:** `03_CODIGO/datito_migracion_inicio.py`

```bash
# Migrar UN archivo a la vez (interactivo)
python 03_CODIGO/datito_migracion_inicio.py --archivo 01_fundamentos.html

# Genera:
# 1. _NEW copia basada en template
# 2. Te avisa qué content extraer del viejo
# 3. Te guía a copy-paste contenido
# 4. Evalúa
# 5. Loguea si OK
```

---

## Prohibiciones (No hacer esto)

❌ Usar Chart.js CDN  
❌ Usar gradiente #667eea o #764ba2  
❌ Usar fonts.google  
❌ Inventar CSS nuevo  
❌ Cambiar :root o clases clave  
❌ Declarar "listo" sin score=1.0  
❌ Ignorar results.tsv  

---

## Timeline Estimado

- **Fase 1 (Certamen 3):** Verificar (5 min)
- **Fase 2 (Conceptos 01-14 + 18-19):** ~12 archivos × 15 min = 3 horas
- **Fase 3 (Ejercicios + referencias):** ~10 archivos × 10 min = 1.5 horas
- **Total:** ~4.5 horas (ejecución iterativa)

### Recomendación
Hacer 2-3 archivos por sesión. No en batch ciego para detectar problemas.

---

## Qué Cambió Entre Archivos Viejos y Template v1

| Aspecto | Antes | Después |
|---|---|---|
| CDN | Chart.js remoto | Canvas 2D local |
| Colores | #667eea, #764ba2 | :root vars (--azul, --rojo, etc) |
| CSS | Inventado | :root tokens fijos |
| Estructura | Variada (div soup) | Semántica clara (h1-h3, .bloque, details.resp) |
| Details | Genéricos | `.resp` con respuesta+error|

---

## Próximos Pasos (Inmediatos)

1. **Verificar Certamen 3:** `python 03_CODIGO/datito_loop_eval.py --path 07_DATITO/visual/certamen3_examen_fcd2026.html`
2. **Si OK:** Loguear como KEEP
3. **Si falla:** Corregir (probable: #667eea en CSS)
4. **Luego:** Empezar Fase 2 con 01_fundamentos.html

---

## Contacto

Si hay dudas durante migración, ver:
- Template canónico: `07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html`
- Learning loop: `07_DATITO/07_BITACORA/learning_loop/agent_lessons.yaml`
- Workflow: `07_DATITO/07_BITACORA/learning_loop/WORKFLOW_VISUAL.md`

