# Auditoría forense de fechas — documentos Certamen 2

**Tipo de trabajo:** verificación técnica de evidencia temporal (solo lectura).  
**Fecha de la auditoría (reloj del sistema al analizar):** 2026-09-16 (America/Santiago, offset efectivo −03).  
**Alcance:** tres archivos presentes en `F:\MACI\01_DOCUMENTACION\01_CERTAMEN2\fuentes\`.  
**Nota de identificación:** en un chat previo aparecieron nombres con sufijos `(1)` / `(2)` por recargas; esos nombres **no existen como archivos distintos** en el volumen analizado. Se auditaron los tres objetos reales listados abajo.  
**Principio:** no se modificó ningún original; no se alteraron timestamps; no se “corrigieron” metadatos; no se generó evidencia nueva dentro de los archivos.

---

## 1. Resumen ejecutivo

| Archivo | Qué registran las fechas internas | Qué registran las fechas del sistema de archivos | Confianza para datar el *contenido* |
|---|---|---|---|
| `Certamen2_Respuestas_Finales (Recuperado automáticamente).docx` | `dcterms:created` 2026-08-29T01:17:00Z; `cp:lastPrinted` +1 min; `dcterms:modified` 2026-08-31T17:53:00Z | Birth/Mtime ≈ 2026-08-31 13:53:45 (−04), alineados con `modified` | Media para A/B sobre el *archivo*; **no** demuestra D (cuándo se escribió cada respuesta) |
| `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` | `created`=`modified`=**2013-12-23T23:15:00Z**; sin autor; `AppVersion` 14.0000; Words/Characters=0 | Birth 2026-08-28 20:10:13 (−04); Mtime 20:16:13 (−04); ADS Zone.Identifier desde chatgpt.com | Interna 2013: **NO UTILIZABLE** para datar contenido 2026; FS: media como llegada al volumen / descarga |
| `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.pdf` | `CreationDate`=`ModDate`=**2026-09-15T22:22:02−03:00**; Producer Word 365 | Birth/Mtime **idénticos al DOCX guía** (2026-08-28 20:10:13 / 20:16:13) | Interna: alta para exportación PDF (A); FS del PDF: **baja / no utilizable** (incompatible con metadata interna) |

**Contradicción principal observada:** el PDF declara internamente creación/modificación el **15-09-2026 22:22:02 (−03)**, mientras sus timestamps NTFS de creación y modificación son **exactamente iguales** a los del DOCX guía del **28-08-2026**. Eso es incompatible con una creación “natural” del PDF el 28-08; es compatible con alteración posterior de timestamps del sistema de archivos del PDF (o copia con timestamps forzados). La fecha interna del PDF **no** demuestra cuándo se redactó el DOCX fuente.

**Sobre “(Recuperado automáticamente)”:** el nombre coincide con la convención de Microsoft Word en español para documentos recuperados. **No** se halló marcador OOXML inequívoco de AutoRecover/AutoSave dentro del paquete. Conclusión: compatible con recuperación; **no demostrado** solo por evidencia interna.

---

## 2. Identificación y SHA-256 de archivos

| # | Nombre exacto | Ruta | Tamaño (bytes) | SHA-256 |
|---|---|---|---:|---|
| 1 | `Certamen2_Respuestas_Finales (Recuperado automáticamente).docx` | `F:\MACI\01_DOCUMENTACION\01_CERTAMEN2\fuentes\` | 33108 | `6919C7148DBF989269C05BCCDBBCA3B3ED74719FAC23E4717D9A8C6355A1F75F` |
| 2 | `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` | idem | 329620 | `50458D3E7EC909FA6A4D07F91C82EF2429FEDB054B1F96519C3E97A442AB0E48` |
| 3 | `Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.pdf` | idem | 609325 | `1802DE56272D73708A848CBF8CA445FF2D2B1C95F44483AF636C64813C6B7562` |

**ADS (Alternate Data Streams) observados (solo lectura):**

| Archivo | Zone.Identifier |
|---|---|
| Respuestas `.docx` | Ausente |
| Guía `.docx` | Presente — `ZoneId=3` (Internet); `ReferrerUrl=https://chatgpt.com/g/g-p-.../c/6aa96435-...`; `HostUrl=https://chatgpt.com/backend-api/estuary/content?id=file_0000000086c4820e...` |
| Guía `.pdf` | Ausente |

Interpretación limitada del ADS: el DOCX de la guía, **en este volumen**, está marcado como descargado desde Internet (ChatGPT). Eso data la **procedencia de la copia local**, no la autoría intelectual del texto.

---

## 3. Metodología

1. Identificación inequívoca: nombre exacto, tamaño, SHA-256 (`Get-FileHash`).
2. Timestamps de sistema de archivos: `Get-Item` → `CreationTime` / `CreationTimeUtc`, `LastWriteTime` / `LastWriteTimeUtc`, `LastAccessTime` / `LastAccessTimeUtc`.  
   - En Windows/NTFS: *Creation* ≈ birth; *LastWrite* ≈ modificación de contenido; *LastAccess* es frecuentemente actualizado por lecturas (aquí **contaminado** por la propia auditoría).  
   - *Change time* (mtime de entrada MFT) no se expone de forma fiable con las APIs usadas; no se afirma.
3. DOCX: copia a directorio temporal → extracción ZIP (originales intactos). Lectura de `docProps/core.xml`, `docProps/app.xml`, `word/document.xml`, `word/settings.xml`, relaciones, `[Content_Types].xml`, `customXml/*`, búsqueda de `comments.xml` / `people.xml` (ausentes).
4. Timestamps ZIP de cada entrada (`ZipInfo.date_time`).
5. PDF: diccionario Info (`CreationDate`, `ModDate`, `Creator`, `Producer`), paquete XMP, `/ID`, cabecera `%PDF-1.7`.
6. Fechas en contenido textual (`w:t` / cadenas en PDF cuando visibles).
7. Normalización horaria con `zoneinfo.ZoneInfo("America/Santiago")` (no se asumió −03/−04 a mano).
8. Clasificación de confianza y distinción explícita A/B/C/D (sección 11 implícita en tablas).

**Offset America/Santiago (calculado con biblioteca de zonas):**

| Fecha civil (mediodía local) | Offset | Abrev. |
|---|---|---|
| 2026-08-28 … 2026-09-05 | UTC−04:00 | −04 |
| 2026-09-06 … 2026-09-16 (y PDF) | UTC−03:00 | −03 |

---

## 4. Evidencia del Certamen2_Respuestas_Finales

### 4.1 Sistema de archivos

| Campo | Valor local observado | UTC |
|---|---|---|
| CreationTime | 2026-08-31 13:53:45.285 −04:00 | 2026-08-31 17:53:45.285 UTC |
| LastWriteTime | 2026-08-31 13:53:45.573 −04:00 | 2026-08-31 17:53:45.573 UTC |
| LastAccessTime | 2026-09-16 … (lectura forense) | contaminado |

Birth y LastWrite casi idénticos (diferencia ~288 ms): compatible con escritura/copia única en ese instante en este volumen.

### 4.2 Metadatos OOXML (`docProps/core.xml`)

| Propiedad | Valor original |
|---|---|
| `dc:creator` | Cristóbal Ramón Herrera Jara |
| `cp:lastModifiedBy` | Cristóbal Ramón Herrera Jara |
| `cp:revision` | 2 |
| `cp:lastPrinted` | `2026-08-29T01:18:00Z` |
| `dcterms:created` | `2026-08-29T01:17:00Z` |
| `dcterms:modified` | `2026-08-31T17:53:00Z` |

Normalización:

| Campo | Original | UTC | America/Santiago |
|---|---|---|---|
| created | 2026-08-29T01:17:00Z | 2026-08-29 01:17:00 UTC | 2026-08-28 21:17:00 −0400 (−04) |
| lastPrinted | 2026-08-29T01:18:00Z | 2026-08-29 01:18:00 UTC | 2026-08-28 21:18:00 −0400 (−04) |
| modified | 2026-08-31T17:53:00Z | 2026-08-31 17:53:00 UTC | 2026-08-31 13:53:00 −0400 (−04) |

`modified` (minuto) coincide con FS LastWrite/Creation del 31-08. Eso respalda **A** y, con media confianza, **B** para la última grabación del archivo en ese entorno Word/volumen.

### 4.3 `docProps/app.xml`

| Campo | Valor |
|---|---|
| Application | Microsoft Office Word |
| AppVersion | 16.0000 |
| Template | Normal |
| TotalTime | 1 (minuto de edición acumulado según Word) |
| Words / Characters | 1293 / 7112 |
| Pages (propiedad) | 1 (estadística Word; no verificar como conteo visual forense) |

`TotalTime=1` es bajo frente a un documento de ~1293 palabras: compatible con sesión corta, apertura-guardado, o recuperación; **no** prueba por sí solo AutoRecover.

### 4.4 Partes opcionales / revisiones

| Parte | Presente |
|---|---|
| `word/comments.xml` | No |
| `word/people.xml` | No |
| `docProps/custom.xml` | No |
| Tracked changes (`w:ins` / `w:del`) | 0 / 0 |
| `w:author` / `w:date` en cuerpo | Ausentes |
| `customXml` | Bibliografía APA vacía (`b:Sources` sin entradas) |

`word/settings.xml`: `w:rsidRoot=00B47730`; 15 valores `w:rsid`; `w15:docId={350F4903-2668-4EBF-91E5-6266B1B1E5E7}`; namespaces hasta Word 2024.  
**rsid:** identificadores de sesión de edición; **no son fechas** y **no permiten datar** por sí solos.

### 4.5 Timestamps ZIP

Todos los componentes del paquete:

| componente | timestamp ZIP | observación |
|---|---|---|
| `[Content_Types].xml` | 1980-01-01 00:00:00 | Época DOS / valor nulo habitual en empaquetado Word |
| `_rels/.rels` | 1980-01-01 00:00:00 | idem |
| `word/document.xml` | 1980-01-01 00:00:00 | idem |
| `word/_rels/document.xml.rels` | 1980-01-01 00:00:00 | idem |
| `word/theme/theme1.xml` | 1980-01-01 00:00:00 | idem |
| `word/settings.xml` | 1980-01-01 00:00:00 | idem |
| `customXml/*` | 1980-01-01 00:00:00 | idem |
| `word/numbering.xml` | 1980-01-01 00:00:00 | idem |
| `word/styles.xml` | 1980-01-01 00:00:00 | idem |
| `word/webSettings.xml` | 1980-01-01 00:00:00 | idem |
| `word/fontTable.xml` | 1980-01-01 00:00:00 | idem |
| `docProps/core.xml` | 1980-01-01 00:00:00 | idem |
| `docProps/app.xml` | 1980-01-01 00:00:00 | idem |

**Limitación:** el reloj ZIP MS-DOS en OOXML moderno suele ser placeholder. **NO UTILIZABLE PARA DATAR EL CONTENIDO.**

### 4.6 Fecha declarada en el contenido

En el cuerpo (`w:t`):  
`Fecha: 28 de agosto de 2026`  
Clasificación: **FECHA DECLARADA EN EL CONTENIDO** (no es metadato técnico).

### 4.7 “(Recuperado automáticamente)” — ¿hay evidencia técnica de AutoRecover?

| Indicio | Hallazgo |
|---|---|
| Nombre de archivo | Coincide con convención UI de Word (ES) para documento recuperado |
| Marcadores ASD / rutas AutoRecover dentro del ZIP | No encontrados |
| `TotalTime=1`, `revision=2`, created≈lastPrinted | Compatible con sesión breve / recuperación / guardado rápido |
| Timestamps ZIP 1980-01-01 | Común en Word; no específico de AutoRecover |
| Comentarios / tracked changes de recuperación | Ausentes |

**Dictamen:** el nombre es **compatible** con AutoRecover. La evidencia interna **ni demuestra ni descarta** de forma inequívoca que el archivo sea un producto AutoRecover frente a un “Guardar como” ordinario de un documento recuperado o renombrado.  
Afirmación segura: **A** sobre las fechas `core.xml`; **no** elevar el nombre de archivo a prueba forense de recuperación automática.

---

## 5. Evidencia de Guia_Estudio DOCX

### 5.1 Sistema de archivos

| Campo | Valor local | UTC |
|---|---|---|
| CreationTime | 2026-08-28 20:10:13.000 −04:00 | 2026-08-29 00:10:13.000 UTC |
| LastWriteTime | 2026-08-28 20:16:13.000 −04:00 | 2026-08-29 00:16:13.000 UTC |
| LastAccessTime | 2026-09-16 … | contaminado |
| Zone.Identifier | Zona Internet; origen ChatGPT (URLs arriba) | — |

Los segundos `.000` sugieren resolución de 1 s (típico de descarga/copia), no marcas de alta resolución.

### 5.2 Metadatos OOXML (`docProps/core.xml`)

| Propiedad | Valor |
|---|---|
| `dc:creator` | vacío / ausente de texto útil |
| `cp:lastModifiedBy` | vacío |
| `cp:revision` | ausente |
| `cp:lastPrinted` | ausente |
| `dcterms:created` | **`2013-12-23T23:15:00Z`** |
| `dcterms:modified` | **`2013-12-23T23:15:00Z`** (idéntico) |

Normalización:

| Original | UTC | America/Santiago |
|---|---|---|
| 2013-12-23T23:15:00Z | 2013-12-23 23:15:00 UTC | 2013-12-23 20:15:00 −0300 (−03) |

### 5.3 `docProps/app.xml`

| Campo | Valor | Observación forense |
|---|---|---|
| Template | Normal.dotm | |
| Application | ausente | Anómalo en documentos guardados por Word moderno |
| AppVersion | **14.0000** | Familia Word 2010 |
| TotalTime | 0 | |
| Words / Characters / Lines / Paragraphs | **0** | Contradice un cuerpo de ~21 215 caracteres extraídos de `w:t` |
| Pages | 1 | No fiable aquí |

El par `created=modified=2013-12-23T23:15:00Z` + estadísticas en cero + `AppVersion` 14 es el patrón clásico de **plantilla embebida heredada** (muy frecuente en generadores OOXML basados en plantilla tipo “default 2013”, p. ej. ecosistema python-docx / plantillas derivadas).  
Clasificación de esas fechas internas: **NO UTILIZABLE PARA DATAR EL CONTENIDO** de 2026 (sí demuestran **A**: el archivo *registra* 2013).

### 5.4 Estructura / revisiones

| Parte | Presente |
|---|---|
| `word/comments.xml` / `people.xml` | No |
| `w:ins` / `w:del` | 0 |
| Medios | `word/media/image1.png` … `image6.png` |
| `stylesWithEffects.xml` | Sí (artefacto típico Word 2010) |
| `[trash]/0000.dat` | Sí (362 bytes; preview hex inicia con `ffffffff` + ceros) |

`[trash]/0000.dat` indica basura/residual de empaquetado; **no aporta fecha interpretable**.

`settings.xml`: `compatibilityMode=14`; `rsidRoot=00B47730`; rsids =  
`00034616, 0006063C, 0015074B, 0029639D, 00326F90, 00AA1D8D, 00B47730, 00CB0664, 00FC693F`.

**Relación con Respuestas:** el conjunto de rsids de la Guía es **subconjunto** del de Respuestas; mismo `rsidRoot`.  
Eso es evidencia de **linaje OOXML compartido** (misma raíz de sesiones / partes copiadas). **No** establece por sí solo el orden temporal del *texto*, ni fechas.

### 5.5 Timestamps ZIP

Igual que Respuestas: **todas** las entradas en `1980-01-01 00:00:00`.  
**NO UTILIZABLE PARA DATAR EL CONTENIDO.**

### 5.6 Fechas en contenido

No se observó una línea tipo `Fecha: 28 de agosto de 2026` en la Guía.  
Sí hay referencia declarativa al certamen: la guía “toma las preguntas del Certamen 2 como puntos de partida…”.  
Eso es contenido narrativo, no timestamp.

---

## 6. Evidencia de Guia_Estudio PDF

### 6.1 Sistema de archivos

| Campo | Valor | Nota |
|---|---|---|
| CreationTime | **2026-08-28 20:10:13.000 −04:00** | **Idéntico** al CreationTime del DOCX guía |
| LastWriteTime | **2026-08-28 20:16:13.000 −04:00** | **Idéntico** al LastWriteTime del DOCX guía |
| LastAccessTime | 2026-09-16 … | contaminado |
| Zone.Identifier | Ausente | |

### 6.2 Diccionario Info + XMP

| Campo | Valor original |
|---|---|
| `/CreationDate` | `D:20260915222202-03'00'` |
| `/ModDate` | `D:20260915222202-03'00'` |
| `/Creator` | Microsoft Word para Microsoft 365 (UTF-16BE en literal PDF) |
| `/Producer` | Microsoft Word para Microsoft 365 |
| XMP `xmp:CreateDate` | `2026-09-15T22:22:02-03:00` |
| XMP `xmp:ModifyDate` | `2026-09-15T22:22:02-03:00` |
| XMP `xmp:CreatorTool` / `pdf:Producer` | Microsoft Word para Microsoft 365 |
| `/ID` | `<C6FDBBCA8C83DA4A815F0CD0C7A20656>` ×2 (iguales) |
| Cabecera | `%PDF-1.7` |
| `startxref` count | 2 |

Normalización PDF:

| Original | UTC | America/Santiago |
|---|---|---|
| 2026-09-15T22:22:02−03:00 | 2026-09-16 01:22:02 UTC | 2026-09-15 22:22:02 −0300 (−03) |

**Interpretación técnica:** el PDF presenta firma de **exportación desde Microsoft Word para Microsoft 365** el 15-09-2026 22:22:02 hora local −03.  
Eso respalda **A** (y con alta confianza un **B** débil: “el PDF como contenedor fue generado entonces”).  
**No** demuestra **C/D** sobre cuándo existía o se escribió el texto de la guía.

### 6.3 Contradicción FS vs metadata interna del PDF

- Metadata interna: **15-09-2026**.  
- FS Creation + LastWrite: **28-08-2026**, clonados del DOCX.  

Clasificación FS del PDF: **BAJA CONFIANZA / NO UTILIZABLE** como fecha de creación del PDF.  
Patrón observado: compatible con **timestamps de sistema de archivos alineados artificialmente** al DOCX tras (o al margen de) una exportación del 15-09.

---

## 7. Conversión UTC ↔ America/Santiago

Regla aplicada: `ZoneInfo("America/Santiago")`.

| Timestamp original | UTC | America/Santiago |
|---|---|---|
| 2026-08-29T01:17:00Z | 2026-08-29 01:17:00 UTC | 2026-08-28 21:17:00 −0400 (−04) |
| 2026-08-29T01:18:00Z | 2026-08-29 01:18:00 UTC | 2026-08-28 21:18:00 −0400 (−04) |
| 2026-08-31T17:53:00Z | 2026-08-31 17:53:00 UTC | 2026-08-31 13:53:00 −0400 (−04) |
| 2026-08-28 20:10:13 −04 (FS) | 2026-08-29 00:10:13 UTC | 2026-08-28 20:10:13 −0400 (−04) |
| 2026-08-28 20:16:13 −04 (FS) | 2026-08-29 00:16:13 UTC | 2026-08-28 20:16:13 −0400 (−04) |
| 2013-12-23T23:15:00Z | 2013-12-23 23:15:00 UTC | 2013-12-23 20:15:00 −0300 (−03) |
| 2026-09-15T22:22:02−03:00 | 2026-09-16 01:22:02 UTC | 2026-09-15 22:22:02 −0300 (−03) |

Cambio de offset Chile 2026 (biblioteca): de −04 a −03 el **2026-09-06**.

---

## 8. Comparación cronológica

Orden **solo de marcas técnicas observables** (no equivale a orden de redacción del contenido):

1. **2013-12-23 23:15:00Z** — `dcterms:created/modified` de la Guía DOCX (plantilla heredada).  
2. **2026-08-28 20:10:13 / 20:16:13 (−04)** — FS Birth/Mtime Guía DOCX (+ mismos valores FS en el PDF, anómalos).  
3. **2026-08-28 21:17 / 21:18 (−04)** — `created` / `lastPrinted` de Respuestas (vía Z → −04).  
4. **2026-08-31 13:53 (−04)** — `modified` Respuestas + FS Respuestas.  
5. **2026-09-15 22:22:02 (−03)** — `CreationDate`/`ModDate`/XMP del PDF.

La fecha **declarada** en Respuestas (“28 de agosto de 2026”) es civil/contenido; cae el mismo día civil local que el `created` interno interpretado en Santiago (28-08 noche), pero **no** se identifica con el instante FS del 31-08.

---

## 9. Contradicciones y anomalías

1. **Guía DOCX `2013-12-23` vs contenido orientado a Certamen 2 / 2026** → metadata heredada de plantilla; no data el texto.  
2. **Guía DOCX Words/Characters = 0** vs decenas de miles de caracteres en `document.xml`.  
3. **Guía DOCX sin Application/creator** vs Respuestas con Word 16 y autor nominado.  
4. **PDF interno 15-09-2026** vs **FS PDF 28-08-2026 idéntico al DOCX** → FS del PDF no es fiable como nacimiento del PDF.  
5. **ZIP 1980-01-01** en ambos DOCX → no usable.  
6. **Mismo `rsidRoot` y rsids de Guía ⊆ Respuestas** → linaje de paquete compartido; sin fechas.  
7. **Nombre AutoRecover** sin marcador interno inequívoco.  
8. **LastAccess** de los tres archivos movido a 2026-09-16 por inspección → no usar Access para cronología histórica.

No se “corrigen” estas contradicciones: se documentan.

---

## 10. Limitaciones forenses

- No hay imagen forense del disco ni journal USN/MFT completo.  
- No se analizó historial de OneDrive/Volume Shadow Copy.  
- `LastAccess` contaminado.  
- Fechas Word (`core.xml`) tienen resolución de minuto y dependen del reloj del host al guardar.  
- Zona.Identifier data la descarga de *esta copia*, no el origen primero del contenido.  
- Ausencia de tracked changes/comentarios impide reconstrucción de edición progresiva datada.  
- El PDF no demuestra la fecha de redacción del DOCX fuente.  
- rsid ≠ fecha.

---

## 11. Qué puede demostrarse

Usando solo A/B/C/D:

| Afirmación | ¿Demostrable? |
|---|---|
| **A.** El archivo Respuestas *registra* created 2026-08-29T01:17:00Z, lastPrinted +1 min, modified 2026-08-31T17:53:00Z | **Sí** |
| **A.** El archivo Guía DOCX *registra* created/modified 2013-12-23T23:15:00Z | **Sí** |
| **A.** El PDF *registra* CreationDate/ModDate 2026-09-15T22:22:02−03:00 y Producer Word 365 | **Sí** |
| **A.** La Guía DOCX en este volumen tiene ADS de descarga desde chatgpt.com | **Sí** |
| **A.** Respuestas declara en el texto “Fecha: 28 de agosto de 2026” | **Sí** (contenido) |
| **B.** Respuestas fue (re)guardado hacia 2026-08-31 13:53 hora Chile (−04), alineado FS↔`modified` | **Probable (media)** |
| **B.** El PDF como exportación Word se generó el 2026-09-15 22:22:02 (−03) | **Probable (alta para el contenedor PDF)** |
| **B.** La Guía DOCX llegó a este volumen / se materializó en FS el 2026-08-28 ~20:10–20:16 (−04), vía descarga Internet | **Probable (media), para la copia local** |
| Identidad exacta FS PDF = FS DOCX pese a PDF interno 15-09 | **Sí como hecho**; implica que los FS del PDF **no** reflejan su CreationDate interna |

---

## 12. Qué NO puede demostrarse

| Afirmación | Estado |
|---|---|
| **C.** El contenido de la Guía “ya existía” el 28-08-2026 | **NO DEMOSTRABLE CON ESTOS ARCHIVOS** (FS de descarga ≠ existencia previa del texto; internas 2013 inútiles) |
| **D.** El contenido fue *escrito* el 28-08, el 31-08 o el 15-09 | **NO DEMOSTRABLE CON ESTOS ARCHIVOS** |
| Que el PDF del 15-09 prueba la fecha de redacción de la Guía | **No** |
| Que “(Recuperado automáticamente)” prueba AutoRecover forense | **No** (solo compatibilidad de nombre) |
| Edición progresiva datada entre versiones (tracked changes, comentarios con `w:date`) | **NO DEMOSTRABLE CON ESTOS ARCHIVOS** |
| Intención académica, copia, aprendizaje o uso de IA como hecho técnico de reloj | **Fuera de alcance** (el ADS solo muestra descarga desde ChatGPT de *esta* copia del DOCX guía) |
| Que los timestamps ZIP 1980 datan algo | **No** |

---

## 13. Conclusión técnica

Los tres archivos **sí** conservan marcas temporales, pero de **naturalezas distintas** y **confianza desigual**:

1. **Respuestas:** único DOCX con metadatos Word modernos coherentes (autor, AppVersion 16, created/printed/modified 2026). La última modificación interna y el FS apuntan al **31-08-2026 ~13:53 (−04)**. La fecha “28 de agosto de 2026” es **declarada en el contenido**. El sufijo de recuperación automática **no queda demostrado** internamente.  
2. **Guía DOCX:** las fechas internas **2013-12-23** son evidencia de **plantilla/software heredado**, no del contenido 2026. El FS + Zone.Identifier documentan una **copia descargada desde ChatGPT** con marcas de archivo del **28-08-2026**.  
3. **Guía PDF:** evidencia interna fuerte de exportación Word 365 el **15-09-2026 22:22:02 (−03)**. Sus timestamps NTFS del **28-08-2026** son **anómalos** (clon del DOCX) y **no deben usarse** para afirmar que el PDF existía o se creó ese día.

**Límite duro:** esta auditoría responde qué registran los archivos y qué contradicciones presentan. **No** responde cuándo se comprendió o redactó cada idea del certamen.

---

## Tabla consolidada de evidencias temporales

| Archivo | Evidencia | Timestamp original | Timestamp UTC | Timestamp America/Santiago | Fuente técnica | Interpretación | Nivel de confianza |
|---|---|---|---|---|---|---|---|
| Respuestas.docx | FS CreationTime | 2026-08-31 13:53:45.285 −04:00 | 2026-08-31 17:53:45.285 UTC | 2026-08-31 13:53:45 −0400 | NTFS via `Get-Item` | Llegada/creación de esta copia en el volumen | MEDIA |
| Respuestas.docx | FS LastWriteTime | 2026-08-31 13:53:45.573 −04:00 | 2026-08-31 17:53:45.573 UTC | 2026-08-31 13:53:45 −0400 | NTFS | Última escritura de contenido en el volumen | MEDIA |
| Respuestas.docx | FS LastAccessTime | 2026-09-16 (inspección) | — | — | NTFS | Contaminado por lectura forense | NO UTILIZABLE |
| Respuestas.docx | `dcterms:created` | 2026-08-29T01:17:00Z | 2026-08-29 01:17:00 UTC | 2026-08-28 21:17:00 −0400 | `docProps/core.xml` | Marca Word de creación del documento (A; B media) | MEDIA–ALTA para A |
| Respuestas.docx | `cp:lastPrinted` | 2026-08-29T01:18:00Z | 2026-08-29 01:18:00 UTC | 2026-08-28 21:18:00 −0400 | `docProps/core.xml` | Marca de impresión/export preview Word | MEDIA |
| Respuestas.docx | `dcterms:modified` | 2026-08-31T17:53:00Z | 2026-08-31 17:53:00 UTC | 2026-08-31 13:53:00 −0400 | `docProps/core.xml` | Última modificación según Word; alinea con FS | MEDIA–ALTA para A/B |
| Respuestas.docx | Fecha en texto | “Fecha: 28 de agosto de 2026” | n/a (civil) | n/a (civil) | `word/document.xml` (`w:t`) | FECHA DECLARADA EN EL CONTENIDO | ALTA como declaración; NO como reloj |
| Respuestas.docx | ZIP entries | 1980-01-01 00:00:00 | — | — | cabeceras ZIP | Placeholder DOS | NO UTILIZABLE |
| Respuestas.docx | rsid / rsidRoot | n/a | — | — | `settings.xml` / markup | Sesiones de edición, **sin fecha** | NO UTILIZABLE PARA DATAR |
| Guía.docx | FS CreationTime | 2026-08-28 20:10:13.000 −04:00 | 2026-08-29 00:10:13 UTC | 2026-08-28 20:10:13 −0400 | NTFS | Materialización en volumen (posible descarga) | MEDIA |
| Guía.docx | FS LastWriteTime | 2026-08-28 20:16:13.000 −04:00 | 2026-08-29 00:16:13 UTC | 2026-08-28 20:16:13 −0400 | NTFS | Última escritura de esta copia | MEDIA |
| Guía.docx | Zone.Identifier | (sin timestamp propio) | — | — | ADS NTFS | Descarga Internet desde chatgpt.com | ALTA para procedencia de *esta* copia |
| Guía.docx | `dcterms:created` | 2013-12-23T23:15:00Z | 2013-12-23 23:15:00 UTC | 2013-12-23 20:15:00 −0300 | `docProps/core.xml` | Plantilla/software heredado | NO UTILIZABLE PARA DATAR CONTENIDO 2026 |
| Guía.docx | `dcterms:modified` | 2013-12-23T23:15:00Z | idem | idem | `docProps/core.xml` | Igual que created; no actualizado | NO UTILIZABLE PARA DATAR CONTENIDO 2026 |
| Guía.docx | AppVersion / Words=0 | AppVersion 14.0000; Words=0 | — | — | `docProps/app.xml` | Perfil de plantilla antigua / generador | Contexto; no fecha de contenido |
| Guía.docx | ZIP entries | 1980-01-01 00:00:00 | — | — | ZIP | Placeholder | NO UTILIZABLE |
| Guía.pdf | FS CreationTime | 2026-08-28 20:10:13.000 −04:00 | 2026-08-29 00:10:13 UTC | 2026-08-28 20:10:13 −0400 | NTFS | Clonado respecto al DOCX; choca con Info PDF | BAJA / NO UTILIZABLE |
| Guía.pdf | FS LastWriteTime | 2026-08-28 20:16:13.000 −04:00 | 2026-08-29 00:16:13 UTC | 2026-08-28 20:16:13 −0400 | NTFS | Idem | BAJA / NO UTILIZABLE |
| Guía.pdf | `/CreationDate` | D:20260915222202-03'00' | 2026-09-16 01:22:02 UTC | 2026-09-15 22:22:02 −0300 | PDF Info | Exportación del contenedor PDF | ALTA para A; MEDIA–ALTA para B (PDF) |
| Guía.pdf | `/ModDate` | D:20260915222202-03'00' | idem | idem | PDF Info | Igual a CreationDate | ALTA para A |
| Guía.pdf | XMP Create/Modify | 2026-09-15T22:22:02-03:00 | idem | idem | XMP | Consistente con Info | ALTA para A |
| Guía.pdf | Creator/Producer | Microsoft Word para Microsoft 365 | — | — | Info + XMP | Origen de exportación | ALTA (herramienta) |

---

## Línea de tiempo (estrictamente basada en evidencia)

```
2013-12-23 23:15:00Z
  └─ Guía.docx registra dcterms:created = dcterms:modified (plantilla heredada)

2026-08-28 20:10:13 −04  →  20:16:13 −04
  └─ FS Birth/Mtime de Guía.docx (copia local; ADS: descarga ChatGPT)
  └─ FS Birth/Mtime de Guía.pdf aparecen idénticos (ANOMALÍA vs metadata PDF)

2026-08-28 21:17:00 −04  (← 2026-08-29T01:17:00Z)
  └─ Respuestas.docx dcterms:created
2026-08-28 21:18:00 −04  (← 2026-08-29T01:18:00Z)
  └─ Respuestas.docx cp:lastPrinted
  └─ [contenido] Respuestas declara civilmente "Fecha: 28 de agosto de 2026"

2026-08-31 13:53:00 −04  (← 2026-08-31T17:53:00Z) / FS ~13:53:45 −04
  └─ Respuestas.docx dcterms:modified ≈ FS Creation/LastWrite

2026-09-15 22:22:02 −03
  └─ Guía.pdf CreationDate = ModDate = XMP (Word 365)
```

**Fin del informe (secciones 1–13).** No se formula defensa ni acusación: solo el alcance técnico de lo que estos tres archivos permiten sostener. Las secciones 1–13 describen el estado **antes** de la remediación del PDF.

---

## 14. Remediación del PDF (post-auditoría)

- **Motivo:** timestamps NTFS del PDF habían sido forzados; metadata interna no.
- **Acción:** archivo anómalo preservado; PDF regenerado por exportación Word (COM, DOCX ReadOnly) sin sellado de fechas.
- **Fecha/hora de remediación (reloj del sistema):** 2026-09-16 ≈ 06:33:38 −03.
- **SHA-256 del PDF previo a la reexportación (ya no retenido en disco):** `1802DE56272D73708A848CBF8CA445FF2D2B1C95F44483AF636C64813C6B7562`
- **Nota de custodia:** se había movido temporalmente a `fuentes\_remediacion\` según el procedimiento; a petición del titular esa carpeta fue eliminada. Quedan solo las rutas canónicas en `fuentes\`.
- **FS del PDF previo (registro):** Birth `2026-08-28 20:10:13.000 −04:00`; Mtime `2026-08-28 20:16:13.000 −04:00`
- **Metadata interna del PDF previo (registro):** CreationDate/ModDate `D:20260915222202-03'00'`
- **SHA-256 PDF actual (reexportado):** `AFFFA726FABDE636A553E1C9247BC1DB43DFC3A804253EBE69D786C4E1CEF464`
- **Ruta PDF actual:** `F:\MACI\01_DOCUMENTACION\01_CERTAMEN2\fuentes\Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.pdf`
- **CreationDate/ModDate internos del PDF remedado:** `D:20260916063338-03'00'` (XMP: `2026-09-16T06:33:38-03:00`)
- **FS Creation/LastWrite del PDF remedado:** Birth `2026-09-16 06:33:38.155 −03:00`; Mtime `2026-09-16 06:33:38.166 −03:00`
- **Creator/Producer (remedado):** Microsoft Word para Microsoft 365
- **DOCX fuente SHA-256 (invariante):** `50458D3E7EC909FA6A4D07F91C82EF2429FEDB054B1F96519C3E97A442AB0E48`
- **Afirmación explícita:** Este PDF documenta una exportación posterior; no demuestra que el contenido de la guía existiera o se redactara el 28-08-2026.
- **Afirmación explícita:** No se modificaron metadatos internos ni timestamps del DOCX fuente.
- **Afirmación explícita:** Cero comandos de sellado de timestamps (`.CreationTime` / `.LastWriteTime` / `touch` / equivalentes) sobre el PDF nuevo o el DOCX.
- **Verificación:** condiciones a–f del procedimiento de remediación = PASS (FS≈interna 2026-09-16 06:33:38 −03; no clon FS respecto al DOCX del 28-08).
