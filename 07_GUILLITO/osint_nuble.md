# OSINT Ñuble — Fases 1 y 2

**Fecha:** 2026-09-19 · **Estado:** catálogo de fuentes y análisis del target.
**No se descargó ningún dataset. No se entrenó ningún modelo.**

Pregunta de investigación: *¿podemos construir, exclusivamente con datos
públicos, legales y trazables, un dataset suficientemente bueno para modelar el
valor inmobiliario en Ñuble?*

---

## FASE 1 · Catálogo de fuentes

### 1 · Censo de Población y Vivienda 2024 — INE

| Campo | Contenido |
|---|---|
| **URL** | `censo2024.ine.gob.cl` · documentación regional de Ñuble disponible |
| **Organismo** | Instituto Nacional de Estadísticas |
| **Período** | 2024. Base de datos publicada el 2025-12-04 |
| **Nivel geográfico** | Comuna y **área** (urbana/rural), con zona censal |
| **Unidad de observación** | **Vivienda**, hogar y persona — microdato |
| **Registros aprox.** | 7.642.716 viviendas a nivel nacional |
| **Formato** | Base de microdatos con manual de uso y diccionario de variables |
| **Target potencial** | **Ninguno económico.** No contiene precio ni avalúo |
| **Features** | Materialidad, tipo de vivienda, N.º de dormitorios, servicios básicos, tenencia, hacinamiento |
| **Actualización** | Decenal |
| **Licencia** | Datos públicos INE |
| **Calidad** | Muy alta. Es censo, no muestra |
| **Descarga automatizable** | Sí, archivo descargable |

**Es la única fuente pública con microdato a nivel de vivienda.** Su límite es
decisivo: no tiene ninguna variable de valor económico.

### 2 · SII — Estadísticas de Bienes Raíces No Agrícolas por Comuna

| Campo | Contenido |
|---|---|
| **URL** | `sii.cl/sobre_el_sii/estadisticas_bienes_raices_no_agricolas.html` |
| **Período** | Semestral. Reavalúo no agrícola vigente desde enero 2025 |
| **Nivel geográfico** | **Comuna** |
| **Unidad de observación** | **Comuna-semestre** (agregado) |
| **Registros aprox.** | 21 comunas de Ñuble × períodos |
| **Target potencial** | Avalúo total y número de predios, **agregados** |
| **Features** | Destino del predio, tramos de avalúo |
| **Licencia** | Público |
| **Descarga automatizable** | Sí, tablas publicadas |

### 3 · SII — Consulta de antecedentes de un bien raíz (por rol)

| Campo | Contenido |
|---|---|
| **URL** | `zeus.sii.cl/avalu_cgi/br/brc803.sh` |
| **Unidad de observación** | **Propiedad individual (rol)** |
| **Target potencial** | **Avalúo fiscal** — no precio de mercado |
| **Features** | Detalle catastral: superficie de terreno y construida, destino, año, material |
| **Licencia** | Consulta pública por rol, sin credenciales del propietario |
| **Descarga automatizable** | **Una consulta por rol.** No hay descarga masiva; automatizarla a escala entra en zona gris de términos de uso |

### 4 · MINVU — Observatorio del Mercado de Suelo Urbano

| Campo | Contenido |
|---|---|
| **URL** | `minvu.gob.cl/observatorios-del-mercado-de-suelo-urbano/` |
| **Unidad de observación** | **Comuna / área urbana / manzana** |
| **Target potencial** | Indicadores de **valor de suelo**, agregados |
| **Fuente subyacente** | Transacciones de bienes raíces no agrícolas del **SII** |
| **Licencia** | Datos abiertos de gobierno |

Es el microdato bueno, ya agregado. El detalle por propiedad no se publica.

### 5 · MINVU — Geoportal Open Data (IDE)

| Campo | Contenido |
|---|---|
| **URL** | `ide.minvu.cl/pages/descargas` y `/pages/visores` |
| **Unidad de observación** | Capas geográficas: IPT, límites urbanos |
| **Target potencial** | Ninguno |
| **Uso** | **Feature engineering geográfico**: zonificación, límite urbano, distancias |
| **Formato** | Shapefile / servicios geoespaciales |

### 6 · MINVU — Centro de Estudios, Ciudad y Territorio

| Campo | Contenido |
|---|---|
| **URL** | `centrodeestudios.minvu.gob.cl` |
| **Unidad de observación** | Comuna |
| **Contenido** | Series estadísticas de política habitacional y mercado inmobiliario; visor comunal; **Déficit Habitacional Censo 2024** |
| **Uso** | Features contextuales por comuna |

### 7 · INE Ñuble — Edificación y construcción

| Campo | Contenido |
|---|---|
| **URL** | `regiones.ine.cl/nuble/estadisticas-regionales/economia/edificacion-y-construccion` |
| **Unidad de observación** | **Comuna-mes** |
| **Contenido** | Superficie autorizada en permisos de edificación, obras nuevas y ampliaciones |
| **Uso** | Proxy de dinamismo constructivo por comuna |

### 8 · Conservador de Bienes Raíces — Índice del Registro de Propiedad

| Campo | Contenido |
|---|---|
| **URL** | `conservador.cl/portal/indice_propiedad` (Santiago; cada comuna tiene el suyo) |
| **Unidad de observación** | **Inscripción individual — la transacción real** |
| **Target potencial** | **Precio real de compraventa** |
| **Acceso** | Búsqueda por apellido, comuna y año. Documento a documento, **con costo** |
| **Descarga automatizable** | **No.** Sin API, sin descarga masiva, y cada conservador es una entidad separada |

**Aquí sí está el precio real. Y es justamente la fuente que no se puede obtener
a escala.**

### 9 · Banco Central — Índice de Precios de Vivienda

| Campo | Contenido |
|---|---|
| **URL** | `bcentral.cl` · sección estadísticas experimentales |
| **Unidad de observación** | Índice trimestral, nacional y regional |
| **Construido con** | Registros administrativos SII (F2890) + Conservador |
| **Uso** | Deflactar y dar contexto temporal. **No evalúa predicciones** |

### 10 · Portales inmobiliarios — **no oficial**

| Campo | Contenido |
|---|---|
| **Unidad de observación** | **Propiedad individual** |
| **Target potencial** | **Precio publicado** — lo que se pide, no lo que se pagó |
| **Features** | Superficie, dormitorios, baños, comuna, tipo, a veces coordenadas |
| **Licencia** | Términos de uso propios; el scraping suele estar restringido |
| **Calidad** | Autodeclarada, sin validación |

---

## FASE 4 anticipada · El problema de granularidad

Es el hallazgo que ordena todo:

| Nivel | Fuentes | ¿Tiene valor económico? |
|---|---|---|
| **Vivienda individual** | Censo 2024 | **No** |
| **Propiedad (rol)** | SII consulta por rol | Avalúo, una a una |
| **Transacción** | Conservador | **Sí, pero inaccesible a escala** |
| **Comuna** | SII agregado, MINVU, INE | Sí, agregado |

**Las fuentes con valor económico masivo están agregadas por comuna. Las fuentes
granulares no tienen valor económico.**

Ñuble tiene **21 comunas**. Un dataset comunal-anual con 21 filas por año no
sostiene un modelo de valoración de inmuebles individuales: no hay variación
dentro de la comuna que explicar, y el número de observaciones es ridículo frente
al número de parámetros de cualquier modelo no trivial.

Mezclar granularidades —usar features de vivienda con un target comunal— produce
un modelo que parece funcionar y no significa nada.

---

## FASE 2 · Los candidatos a target, y por qué no son equivalentes

| Candidato | Qué es realmente | Disponibilidad |
|---|---|---|
| **Precio real de transacción** | Lo efectivamente pagado, inscrito en el Conservador y declarado al SII (F2890) | Conservador: documento a documento, con costo. **No masivo** |
| **Avalúo fiscal** | Valoración **administrativa** del SII para cobrar impuesto territorial. Se fija por fórmula y se actualiza en reavalúos | Pública por rol. Agregada por comuna |
| **Valor de suelo** | Indicador de MINVU sobre el **suelo**, no sobre la construcción | Agregado por comuna/manzana |
| **Precio publicado** | Lo que **pide** el vendedor. Sesgado al alza y sin validar | Portales, no oficial |
| **UF/m²** | Un cociente, no una fuente. Hereda los defectos del numerador | Derivable |

Tres distinciones que conviene tener claras antes de elegir:

**Avalúo fiscal ≠ precio de mercado.** El avalúo se calcula con una fórmula
administrativa a partir de superficie, materialidad, destino y área homogénea. Un
modelo entrenado para predecir avalúo aprendería a reproducir **la fórmula del
SII**, no el comportamiento del mercado. Podría dar métricas excelentes y no
decir nada sobre cuánto vale una casa.

**Precio publicado ≠ precio de transacción.** Medir error contra un precio
publicado es medir contra una aspiración del vendedor.

**Valor de suelo ≠ valor de la propiedad.** El suelo es un componente. Una casa
es suelo más construcción.

---

## Lo que este documento no concluye

No se determina cuál debe ser el target ni si el proyecto es viable. Esa
decisión es de Cristóbal (garantía G2 de `spec.md`).

Pendiente de verificar antes de cualquier decisión: el catálogo de `datos.gob.cl`
y los portales del Gobierno Regional de Ñuble, SERVIU y municipalidades, que no
alcanzaron a revisarse en esta fase.

---

## Fuentes consultadas

- [SII · Estadísticas de Bienes Raíces No Agrícolas por Comuna](https://www.sii.cl/sobre_el_sii/estadisticas_bienes_raices_no_agricolas.html)
- [SII · Estadísticas de Bienes Raíces por región](https://www.sii.cl/sobre_el_sii/estadisticas/ebbrrpr_bbrr_por_region.html)
- [SII · Consulta de antecedentes de un bien raíz](https://zeus.sii.cl/avalu_cgi/br/brc803.sh)
- [SII · Reavalúo 2025](https://www.sii.cl/destacados/reavaluo/2025/index.html)
- [Censo 2024 · Documentación Región del Ñuble](https://censo2024.ine.gob.cl/documentacion-region-del-nuble/)
- [INE · Base de Datos del Censo de Población y Vivienda 2024](https://www.ine.gob.cl/sala-de-prensa/prensa/general/noticia/2025/12/04/ine-publica-base-de-datos-del-censo-de-poblaci%C3%B3n-y-vivienda-2024)
- [MINVU · Observatorios del mercado de suelo urbano](https://www.minvu.gob.cl/observatorios-del-mercado-de-suelo-urbano/)
- [MINVU · Geoportal Open Data — descargas](https://ide.minvu.cl/pages/descargas)
- [MINVU · Centro de Estudios — Déficit Habitacional Censo 2024](https://centrodeestudios.minvu.gob.cl/deficit-habitacional-censo-2024/)
- [INE Ñuble · Edificación y construcción](https://regiones.ine.cl/nuble/estadisticas-regionales/economia/edificacion-y-construccion)
- [CBR · Índice del Registro de Propiedad](https://www.conservador.cl/portal/indice_propiedad)
