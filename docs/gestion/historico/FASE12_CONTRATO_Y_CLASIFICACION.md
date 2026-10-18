# FASE 1 — CONTRATO DEL TEMPLATE CANÓNICO v1

**Status:** EXTRACCIÓN COMPLETA DEL CONTRATO  
**Fecha:** 2026-09-25  
**Template SHA256:** `eb7aef7a5ce1b7bf18248c3798c9c3165b3d9102920ef1f2cf69a895bc174664`

---

## 1. METADATA DEL TEMPLATE

| Propiedad | Valor |
|-----------|-------|
| **Versión** | v1 |
| **Marker Identificador** | `<!-- datito:template:v1 -->` |
| **Ubicación del Marker** | Línea 5 (después de `<meta charset="utf-8">`) |
| **Tipo de Documento** | HTML5 autocontenido para educación |
| **Ancho Máximo** | 900px (`max-width: 900px` en `main`) |
| **Lenguaje** | `lang="es"` |
| **Encoding** | UTF-8 |

---

## 2. ESTRUCTURA DOM OBLIGATORIA

```
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <!-- datito:template:v1 -->
  <title>TÍTULO · Datito</title>
  <style>
    :root { /* CSS tokens aquí */ }
    /* Resto de estilos embebidos */
  </style>
</head>
<body>
<main>
  <!-- datito:nav:inicio -->
  <!-- construir_navegacion.py inyecta aquí -->
  <!-- datito:nav:fin -->
  
  <h1>TÍTULO</h1>
  <p class="sub">contexto</p>
  
  <!-- Contenido reemplazable -->
  
  <footer>Generado con template canónico Datito v1</footer>
</main>
</body>
</html>
```

### Elementos DOM Requeridos (CANONICAL):

| Elemento | Ubicación | Editabilidad | Notas |
|----------|-----------|--------------|-------|
| `<!DOCTYPE html>` | Línea 1 | ❌ No | Obligatorio exacto |
| `<html lang="es">` | Línea 2 | ❌ No | Solo cambiar lang si necesario |
| `<meta charset="utf-8">` | Head, antes de marker | ❌ No | Obligatorio exacto |
| `<!-- datito:template:v1 -->` | Línea 5, head | ❌ No | CRÍTICO: marker identificador |
| `<title>TÍTULO · Datito</title>` | Head | ✅ Sí | Editable: cambiar `TÍTULO` |
| `<style>` (inline) | Head | ⚠️ Parcial | Solo :root, no agregar CSS nuevo |
| `<main>` | Body | ❌ No | Contenedor de 900px |
| `<!-- datito:nav:inicio/fin -->` | Dentro main | ❌ No | Marcadores para inyección |
| `<h1>` | Dentro main | ✅ Sí | Editable: título del concepto |
| `<p class="sub">` | Tras h1 | ✅ Sí | Editable: contexto del concepto |
| `<div class="clave">` | Tras .sub | ✅ Sí | Editable: objetivo de aprendizaje |
| `<h2>` secciones | Contenido | ✅ Sí | Editable: estructura pedagógica |
| `<footer>` | Fin main | ❌ No | Texto fijo recomendado |

---

## 3. VARIABLES CSS (:root)

### Colores Canónicos (NO se pueden cambiar):

```css
:root {
  --tinta:   #1a1a1a;  /* Text color (dark gray) */
  --suave:   #666;     /* Soft text (gray) */
  --linea:   #d8d8d8;  /* Borders (light gray) */
  --fondo:   #faf9f7;  /* Background (off-white) */
  --azul:    #2563eb;  /* Blue (primary) */
  --rojo:    #dc2626;  /* Red (danger/error) */
  --verde:   #059669;  /* Green (success/citation) */
  --ambar:   #d97706;  /* Amber (warning/note) */
  --morado:  #7c3aed;  /* Purple (graph/complex) */
}
```

**Clasificación:** ✅ **CANONICAL** — Exactamente estos valores, no variaciones.

**Prohibido:**
- ❌ `#667eea` (AI-generated blue)
- ❌ `#764ba2` (AI-generated purple)
- ❌ Cambiar nombres de variables
- ❌ Agregar nuevas variables sin aprobación

---

## 4. TIPOGRAFÍA (CANONICAL)

| Elemento | Tamaño | Line-Height | Font-Weight | Margin/Padding | Notas |
|----------|--------|-------------|-------------|-----------------|-------|
| **body** | 16px | 1.7 | inherit | margin: 0; padding: 2rem 1rem | Font: "Segoe UI", system-ui, sans-serif |
| **h1** | 1.7rem | inherit | inherit | 0 0 .3rem | Color: --tinta |
| **h2** | 1.2rem | inherit | inherit | 2.6rem 0 .7rem; border-top | Separador visual |
| **h3** | 1rem | inherit | inherit | 1.6rem 0 .4rem | Color: #374151 (gris oscuro) |
| **.sub** | inherit | inherit | inherit | 0 0 2rem | Color: --suave |
| **code** | 0.9em | inherit | inherit | .1rem .35rem | Font: monospace |

**Clasificación:** ✅ **CANONICAL** — Exactamente como se especifica, sin excepciones.

---

## 5. COMPONENTES OBLIGATORIOS (CLASIFICACIÓN)

### CANONICAL (Deben ser exactamente iguales)

#### `.clave` — Objetivo de Aprendizaje
```css
.clave {
  background:   #eff6ff;
  border-left:  3px solid var(--azul);
  padding:      .85rem 1.1rem;
  margin:       1.1rem 0;
  /* No agregar estilos extra */
}
```
- **Propósito:** Resaltar qué aprenderá el alumno
- **Ubicación:** Inmediatamente después de `.sub`
- **Contenido:** `<strong>Qué vas a poder hacer.</strong> [objetivo observable]`
- **Editabilidad:** Solo el texto dentro
- **Obligatoriedad:** ✅ REQUERIDO en todos los documentos

#### `details.resp` — Respuesta Correcta
```css
details.resp {
  background:  #f0fdf4;
  border:      1px solid #bbf7d0;
  border-radius: 8px;
  padding:     .6rem 1rem;
  margin:      .6rem 0 1rem;
}

details.resp summary {
  cursor:      pointer;
  font-weight: 700;
  color:       #065f46;
}
```
- **Propósito:** Respuestas verificadas + resolución + errores típicos
- **Contenido Requerido:**
  - `<summary>Respuesta correcta y cómo se resuelve</summary>`
  - `<p><strong>Respuesta:</strong> [respuesta]</p>`
  - `<p><strong>Resolución:</strong> [pasos]</p>`
  - `<p><strong>Error típico:</strong> [errores frecuentes]</p>`
  - `<p class="f">[DATITO] o [FUENTE · Repo: ruta]</p>`
- **Obligatoriedad:** ✅ REQUERIDO (al menos una por documento)

#### `details` — Expandible Genérica
```css
details {
  background:   #fff;
  border:       1px solid var(--linea);
  border-radius: 9px;
  padding:      .9rem 1.2rem;
  margin:       .7rem 0;
}

summary {
  cursor:       pointer;
  font-weight:  600;
  color:        var(--azul);
  list-style:   none;
  /* Marker: ▸ / ▾ */
}
```
- **Propósito:** Secciones expandibles (detalles, por qué, etc.)
- **Diferencia con `.resp`:** Sin color de fondo verde
- **Obligatoriedad:** ✅ REQUERIDO (estructura pedagógica)

#### `.ecu` — Ecuaciones/Fórmulas
```css
.ecu {
  background:      #fff;
  border:          1px solid var(--linea);
  border-radius:   10px;
  padding:         1.1rem 1.3rem;
  margin:          1rem 0;
}

.ecu .f {
  font-family:     ui-monospace, monospace;
  font-size:       1.1rem;
  text-align:      center;
  padding:         .8rem;
  background:      var(--fondo);
  border-radius:   8px;
  margin-bottom:   .8rem;
}
```
- **Propósito:** Mostrar fórmulas de forma destacada
- **Contenido:** `<div class="f">fórmula</div>` + explicación
- **Obligatoriedad:** ⚠️ REQUERIDO si hay fórmulas

#### `.peligro` — Errores que Castiga el Examen
```css
.peligro {
  background:   #fef2f2;
  border-left:  3px solid var(--rojo);
  padding:      .85rem 1.1rem;
  margin:       1.1rem 0;
}
```
- **Propósito:** Advertencias críticas
- **Contenido:** `<strong>Errores que el examen castiga.</strong> <ul>...</ul>`
- **Obligatoriedad:** ✅ REQUERIDO en todos

#### `.nota` — Reminders/Checklist
```css
.nota {
  background:   #fffbeb;
  border-left:  3px solid var(--ambar);
  padding:      .85rem 1.1rem;
  margin:       1.1rem 0;
  font-size:    .94rem;
}
```
- **Propósito:** Notas y checklists
- **Contenido:** `<strong>Checklist antes de entregar.</strong> <ul>...</ul>`
- **Obligatoriedad:** ✅ REQUERIDO en todos

#### `footer` — Pie de Página
```css
footer {
  margin-top:   3rem;
  padding-top:  1rem;
  border-top:   1px solid var(--linea);
  color:        var(--suave);
  font-size:    .85rem;
}
```
- **Propósito:** Atribución y timestamp
- **Contenido Recomendado:** `Generado con template canónico Datito v1 · sin conexión · <!-- datito:template:v1 -->`
- **Obligatoriedad:** ✅ REQUERIDO

#### `ol.pasos` — Lista de Pasos
```css
ol.pasos {
  margin:   .4rem 0 0 1.1rem;
  padding:  0;
}

ol.pasos li {
  margin-bottom: .4rem;
}
```
- **Propósito:** Enumerar pasos de resolución
- **Ubicación:** Bajo h2 "Cómo se resuelve"
- **Obligatoriedad:** ✅ REQUERIDO (sección "Pasos")

---

### EXTENSION_ALLOWED (Puede haber variaciones específicas)

#### `.cita` — Citas Textuales
```css
.cita {
  border-left:  3px solid var(--verde);
  background:   #f0fdf4;
  padding:      .9rem 1.1rem;
  margin:       1.1rem 0;
  font-style:   italic;
}

.cita .f {
  display:      block;
  font-style:   normal;
  font-size:    .8rem;
  color:        var(--suave);
  margin-top:   .5rem;
}
```
- **Variaciones Permitidas:** Cambiar contenido, no estilos
- **Obligatoriedad:** ⚠️ Opcional (si hay citas)

#### `.grafo` — Diagramas de Conceptos
```css
.grafo {
  display:      flex;
  align-items:  center;
  gap:          .5rem;
  flex-wrap:    wrap;
  font-size:    .86rem;
  background:   #f5f3ff;
  border-left:  3px solid var(--morado);
  padding:      .7rem 1rem;
  margin:       1rem 0;
}

.grafo .n {
  background:       #fff;
  border:           1px solid #ddd6fe;
  border-radius:    6px;
  padding:          .25rem .6rem;
}

.grafo .n.aqui {
  background:       var(--morado);
  color:            #fff;
  border-color:     var(--morado);
  font-weight:      700;
}
```
- **Variaciones Permitidas:** Agregar nodos, cambiar contenido
- **Obligatoriedad:** ⚠️ Opcional (si hay conceptos relacionados)

#### `canvas` — Gráficos Locales
```css
canvas {
  width:          100%;
  height:         auto;
  display:        block;
  border-radius:  8px;
  background:     #fff;
  border:         1px solid var(--linea);
}
```
- **Requisitos:** 
  - SIEMPRE `width: 100%` (responsive)
  - SIEMPRE `height: auto`
  - SIEMPRE `display: block`
  - NUNCA CDN (Chart.js, Plotly, etc.)
  - SIEMPRE JavaScript embebido
- **Obligatoriedad:** ⚠️ Opcional (si hay gráficos)

#### `.panel` — Paneles de Contenido
```css
.panel {
  background:     #fff;
  border:         1px solid var(--linea);
  border-radius:  10px;
  padding:        1.2rem;
  margin:         1.2rem 0;
}
```
- **Variaciones Permitidas:** Cambiar contenido
- **Obligatoriedad:** ⚠️ Opcional (para agrupar contenido)

#### `button` / `button.alt` — Botones
```css
button {
  background:     var(--azul);
  color:          #fff;
  border:         0;
  border-radius:  7px;
  padding:        .5rem 1rem;
  font-size:      .88rem;
  cursor:         pointer;
  font-weight:    600;
  margin:         .2rem .35rem .2rem 0;
}

button:hover {
  background:     #1d4ed8;
}

button.alt {
  background:     #6b7280;
}
```
- **Variaciones Permitidas:** Cambiar contenido
- **Obligatoriedad:** ⚠️ Opcional (si hay interactividad)

#### `table` — Tablas
```css
table {
  border-collapse: collapse;
  width:          100%;
  font-size:      .9rem;
  margin:         .9rem 0;
}

th, td {
  border:             1px solid var(--linea);
  padding:            .5rem .65rem;
  text-align:         left;
  vertical-align:     top;
}

th {
  background:         var(--fondo);
  font-weight:        600;
}

td.num {
  text-align:         right;
  font-variant-numeric: tabular-nums;
}
```
- **Variaciones Permitidas:** Cambiar contenido, estructura
- **Obligatoriedad:** ⚠️ Opcional (si hay datos tabulares)

---

### DOCUMENT_SPECIFIC (Cada documento puede tener lo suyo)

#### `.bloque` / `.bloque-titulo`
```css
.bloque {
  margin: 1.2rem 0;
}

.bloque-titulo {
  font-weight: 700;
  margin:      0 0 .5rem;
  color:       #374151;
}
```
- **Variaciones:** Completamente editable
- **Obligatoriedad:** ⚠️ Opcional

#### `code` — Inline Code
```css
code {
  background:     #f1f0ee;
  padding:        .1rem .35rem;
  border-radius:  4px;
  font-size:      .9em;
}
```
- **Variaciones:** Cambiar contenido
- **Obligatoriedad:** ⚠️ Opcional

#### `.highlight` — Resaltes de Texto
```css
.highlight {
  background:     #fef08a;
  padding:        .05rem .25rem;
  border-radius:  3px;
}
```
- **Variaciones:** Cambiar dónde resaltar
- **Obligatoriedad:** ⚠️ Opcional

#### `h2` · Secciones
- **Variaciones:** Cambiar títulos, agregar secciones
- **Estructura Recomendada:**
  1. "Qué te dan / qué pasó"
  2. "Cómo se resuelve"
  3. Otras secciones según concepto
- **Obligatoriedad:** ✅ Mínimo 2

---

## 6. PROHIBICIONES EXPLÍCITAS

### CDN y Recursos Remotos ❌

| Prohibición | Razón |
|-----------|-------|
| `<script src="https://cdn.plot.ly/...">` | Requiere conexión; no funciona offline |
| `<script src="https://.../chart.js">` | Requiere conexión; no funciona offline |
| `<link href="https://fonts.googleapis.com">` | Requiere conexión; no funciona offline |
| `import from "https://unpkg.com/..."` | Requiere conexión |
| Cualquier `http://` (no HTTPS) | Inseguro |

**Consecuencia:** Script `datito_loop_eval.py` marca como DISCARD.

### Colores Prohibidos ❌

| Color | Razón |
|-------|-------|
| `#667eea` | Color azul AI-generated (no autorizado) |
| `#764ba2` | Color púrpura AI-generated (no autorizado) |
| `linear-gradient con estos colores` | Prohibido |

**Razón:** Contaminación de identidad visual; demuestra uso de herramientas IA para generar estilos.

### CSS Personalizado ❌

| Prohibición | Alternativa |
|------------|-------------|
| Agregar variables `:root` nuevas | Usar las 9 existentes |
| Crear clases nuevas sin aprobación | Usar las canónicas + EXTENSION_ALLOWED |
| Cambiar valores de variables existentes | No permitido |
| Modificar selectores core | No permitido |

---

## 7. VALIDACIÓN: 11 GATES

Estos gates son ejecutables por `datito_loop_eval.py`.

| # | Gate | Validación | Peso | Crítico |
|---|------|-----------|------|---------|
| 1 | **template_marker** | `<!-- datito:template:v1 -->` presente exacta | 1.0 | ✅ SÍ |
| 2 | **anti_cdn** | Sin cdn.plot.ly, chart.js, googleapis, fonts.google, unpkg | 1.0 | ✅ SÍ |
| 3 | **anti_chart_cdn** | Sin bibliotecas de charts remotas | 1.0 | ✅ SÍ |
| 4 | **anti_ai_gradient** | Sin #667eea o #764ba2 | 1.0 | ✅ SÍ |
| 5 | **has_style_embed** | CSS embebido en `<style>`, no externos | 1.0 | ✅ SÍ |
| 6 | **no_http_script_src** | Sin `<script src="http://...">` | 1.0 | ✅ SÍ |
| 7 | **offline_draw** | Si canvas/gráficos: locales (no CDN) | 1.0 | ✅ SÍ |
| 8 | **bloque_que_paso** | Sección "Qué pasó" detectable | 1.0 | ✅ SÍ |
| 9 | **bloque_pasos** | `<ol class="pasos">` presente | 1.0 | ✅ SÍ |
| 10 | **details_resp** | `<details class="resp">` presente | 1.0 | ✅ SÍ |
| 11 | **errores** | `<div class="peligro">` presente | 1.0 | ✅ SÍ |

**Score:** (Gates pasados / 11) × 100%
- **KEEP:** score = 1.0 (100%)
- **DISCARD:** score < 1.0

---

## 8. PATRONES ESTRUCTURALES RECOMENDADOS

### Patrón 1: Concepto Simple
```
h1 (Título)
p.sub (Contexto)
div.clave (Objetivo)
h2 "1 · Qué te dan / qué pasó"
p (Descripción)
h2 "2 · Cómo se resuelve"
ol.pasos
div.ecu (Fórmula)
details (Detalle/por qué)
details.resp (Respuesta)
div.peligro (Errores)
div.nota (Checklist)
footer
```

### Patrón 2: Ejercicio/Certamen
```
h1 (Título)
p.sub (Contexto)
div.clave (Objetivo)
div.peligro (Procedencia/crítico)
h2 (Sección 1)
... contenido ...
details.resp (Para cada pregunta)
... más secciones ...
div.nota (Instrucciones finales)
footer
```

### Patrón 3: Herramienta Interactiva
```
h1 (Título)
p.sub (Contexto)
div.clave (Qué hace)
div.panel (Controles)
canvas (Visualización)
details.resp (Interpretación)
div.peligro (Limitaciones)
footer
```

---

## 9. FINGERPRINT Y COMPARACIÓN

**Template Canónico SHA256:**
```
eb7aef7a5ce1b7bf18248c3798c9c3165b3d9102920ef1f2cf69a895bc174664
```

**Cómo verificar duplicado:**
```bash
sha256sum archivo.html
# Comparar contra el SHA del template
```

**Si SHA NO coincide:** El archivo ha sido modificado (puede ser extensión permitida).

---

## PRÓXIMO PASO: FASE 2

Clasificar todos los 25 HTML con esta tabla:

| FILE | MARKER | DOM_MATCH | CSS_MATCH | COMP_MATCH | VISUAL | ROOT_CAUSE | STATUS |
|------|--------|-----------|-----------|------------|--------|-----------|--------|
| ... | ... | ... | ... | ... | ... | ... | ... |

---

**FASE 1 COMPLETADA:** Contrato extraído, documentado y clasificable.  
**PRÓXIMA TAREA:** FASE 2 — Clasificación detallada de 25 HTML.
