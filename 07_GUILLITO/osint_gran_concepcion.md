# OSINT — ¿Hay datos reales de vivienda del Gran Concepción?

**Fecha:** 2026-09-19 · **Estado:** investigación de fuentes. **No se descargó
ningún dataset ni se entrenó ningún modelo.**

Pregunta de aprendizaje: *¿puede un modelo entrenado con Melbourne 2016
evaluarse contra datos reales del Gran Concepción?* Antes de responderla hay que
saber qué datos existen realmente.

---

## Distinción que ordena todo el análisis

**Precio publicado** (lo que pide el vendedor en un portal) **≠ precio real de
transacción** (lo que efectivamente se pagó, inscrito en el Conservador de
Bienes Raíces y declarado al SII).

Confundirlos invalida cualquier medición de error: se estaría midiendo contra
una aspiración, no contra un hecho.

---

## Fuentes evaluadas

### 1 · SII — Servicio de Impuestos Internos

| Campo | Contenido |
|---|---|
| **Período** | Histórico, actualización continua |
| **Unidad de observación** | Propiedad (rol de avalúo) |
| **Target disponible** | **Avalúo fiscal**, no precio de transacción |
| **Features** | Detalle catastral: superficie, destino, material, año |
| **Granularidad** | Propiedad individual, por rol |
| **Formato** | Consulta web por rol; descargas de detalle catastral y roles por comuna |
| **Licencia** | Público; consulta por rol no requiere credenciales del propietario |
| **Calidad aparente** | Alta, es registro administrativo |
| **Compatibilidad** | Parcial: aporta features, **no el target** |

**El dato que importaría — el formulario F2890** — contiene rol, **precio y
fecha** de cada transferencia, copia fiel de lo inscrito en el Conservador. El
SII lo recibe. Según lo reportado por CIPER, el Consejo para la Transparencia
resolvió en varias ocasiones que esa información debía ser pública, pero los
tribunales han fallado a favor del SII de no entregarla.

> **Consecuencia:** el precio real de transacción a nivel de propiedad
> **no es públicamente accesible** en Chile por esta vía.
> `[FUENTE · CIPER Chile, 2022]`

### 2 · MINVU — Observatorio del Mercado de Suelo Urbano

| Campo | Contenido |
|---|---|
| **Período** | Series por año |
| **Unidad de observación** | **Comuna / área urbana / manzana** |
| **Target disponible** | Valor de suelo **agregado**, no precio por propiedad |
| **Features** | Indicadores urbanos, permisos de edificación y urbanización, IPT |
| **Granularidad** | Agregada. Comunas con población urbana > 5.000 hab |
| **Formato** | Visor de mapas; descargas en `ide.minvu.cl/pages/descargas` |
| **Licencia** | Datos abiertos de gobierno |
| **Calidad aparente** | Alta, pero agregada |
| **Compatibilidad** | **No sirve como target**: una observación es una comuna, no una vivienda |

Construido **a partir de** las transacciones de bienes raíces no agrícolas del
SII — es decir, es el dato bueno, ya agregado y despojado del detalle por
propiedad.

### 3 · Banco Central — Índice de Precios de Vivienda (IPV)

| Campo | Contenido |
|---|---|
| **Unidad de observación** | Índice nacional / regional por trimestre |
| **Target disponible** | **Índice**, no precio |
| **Granularidad** | Agregada |
| **Compatibilidad** | Sirve para contexto y deflactar, **no para evaluar predicciones** |

Elaborado con registros administrativos del SII (F2890) más el Conservador de
Bienes Raíces. Misma situación que MINVU: el microdato está detrás.

### 4 · CChC — Cámara Chilena de la Construcción

| Campo | Contenido |
|---|---|
| **Período** | Informes trimestrales |
| **Unidad de observación** | Mercado / comuna |
| **Target disponible** | Unidades vendidas, stock, precios promedio por segmento |
| **Granularidad** | Agregada |
| **Licencia** | Gremial, informes públicos; microdato no publicado |
| **Compatibilidad** | Contexto de mercado. **No hay microdato por propiedad** |

Referencia local: el área metropolitana de Concepción —con Talcahuano, San Pedro
de la Paz y Chiguayante— concentra más de 16.600 unidades nuevas en oferta, ~65 %
departamentos, con mayor dinamismo en Concepción y San Pedro de la Paz.

### 5 · datos.gob.cl

Portal de datos abiertos del Estado. En la búsqueda realizada **no apareció un
dataset de transacciones inmobiliarias a nivel de propiedad** para la Región del
Biobío. Queda pendiente una revisión directa del catálogo antes de descartarlo.

### 6 · Portales inmobiliarios — **fuente no oficial**

Portalinmobiliario, Enlace Inmobiliario, datainmobiliaria.cl y similares.

| Campo | Contenido |
|---|---|
| **Target disponible** | **Precio publicado**, no de transacción |
| **Features** | Superficie, dormitorios, baños, comuna, tipo, a veces georreferencia |
| **Granularidad** | **Propiedad individual** — la única fuente con este nivel |
| **Licencia** | Términos de uso propios; el scraping suele estar restringido |
| **Calidad aparente** | Variable, autodeclarada, sin validación |
| **Compatibilidad** | Features sí. **Target incorrecto** |

Es la única fuente con granularidad de propiedad, y justamente es la que tiene el
target equivocado.

---

## Matriz de compatibilidad Melbourne ↔ Chile

Sin traducciones semánticas automáticas.

| Melbourne | Posible equivalente Chile | ¿Compatible? | Por qué |
|---|---|---|---|
| `Price` (AUD) | Precio en UF o CLP | **No directo** | La UF es reajustable por inflación; AUD es nominal. Comparar exige definir unidad y deflactor |
| `Rooms` | ¿dormitorios? | **No** | `Rooms` es el total de habitaciones, no dormitorios. En Melbourne `Bedroom2` es el campo de dormitorios |
| `Bedroom2` | Dormitorios | **Sí** | Definición equivalente |
| `Bathroom` | Baños | **Sí** | Definición equivalente |
| `Landsize` | Superficie de terreno | **Sí**, con cuidado | Ambos en m². Verificar criterio de medición |
| `BuildingArea` | Superficie construida | **Sí**, con cuidado | Ídem |
| `Car` | Estacionamientos | **Probable** | Definición similar, verificar |
| `Distance` | ¿distancia al centro? | **No** | En Melbourne es distancia al CBD, un centro único. El Gran Concepción es **policéntrico** — Concepción, Talcahuano, San Pedro. No hay un CBD equivalente |
| `Lattitude` / `Longtitude` | Coordenadas | **Técnicamente sí** | Pero un modelo entrenado con coordenadas de Melbourne es inútil fuera de ese rectángulo geográfico |
| `CouncilArea` | ¿comuna? | **No automático** | Ambas son unidades administrativas locales, pero difieren en tamaño, atribuciones y significado de mercado. Equivalencia estructural ≠ equivalencia semántica |
| `Regionname` | ¿provincia, sector? | **No** | Las regiones de Melbourne son categorías de mercado, no divisiones administrativas |
| `Type` (h/u/t) | Casa / departamento | **Aproximado** | `townhouse` no tiene equivalente limpio |
| `Method` (S/SP/PI/VB/SA) | — | **No** | Codifica modalidad de remate australiana. Chile no tiene ese mecanismo de venta |
| `Propertycount` | Propiedades por sector | **Quizá** | Habría que construirlo; no existe publicado |
| `YearBuilt` | Año de construcción | **Sí** | Disponible en catastro SII |

**Variables sin equivalente razonable: `Distance`, `Method`, `Regionname`.**
Son tres de las doce que usa el modelo actual.

---

## Los tres niveles

### Nivel 1 — Inferencia

Tengo features reales de una vivienda del Gran Concepción. El modelo produce ŷ.

Demuestra que **el pipeline se ejecuta**. No dice nada sobre si ŷ es correcto.

### Nivel 2 — Predicción evaluable

Tengo además el precio real `y` de esa propiedad. Puedo calcular el error de
**esa observación**: `|y − ŷ|`.

Demuestra el error en un caso. Un caso no es una medida de desempeño.

### Nivel 3 — Validación externa

Tengo suficientes propiedades reales con `y` conocido, separadas de todo proceso
de entrenamiento y de selección. Puedo calcular MAE, RMSE, R² y hablar de
generalización.

Es el único nivel que permite afirmar capacidad predictiva.

---

## Lo que este documento **no** concluye

Deliberadamente no se determina hasta qué nivel permiten llegar estas fuentes.
Esa es la pregunta que debe responder Cristóbal (garantía G2 de `spec.md`).

Tampoco se ha descargado nada, ni adaptado Melbourne a Chile, ni entrenado
ningún modelo.

---

## Fuentes consultadas

- [SII · Estadísticas de Bienes Raíces](https://www.sii.cl/sobre_el_sii/estadisticas_bienes_raices.html)
- [SII · Consultar transferencia de bienes raíces](https://www.sii.cl/servicios_online/1048-3665.html)
- [CIPER · La falta de transparencia del SII en el reavalúo de bienes raíces](https://www.ciperchile.cl/2022/06/05/la-falta-de-transparencia-del-sii-en-reavaluos-y-contribuciones/)
- [MINVU · Observatorios del mercado de suelo urbano](https://www.minvu.gob.cl/observatorios-del-mercado-de-suelo-urbano/)
- [MINVU · Geoportal Open Data — descargas](https://ide.minvu.cl/pages/descargas)
- [MINVU · Centro de Estudios, Ciudad y Territorio](https://centrodeestudios.minvu.gob.cl/)
- [Banco Central · Índice de Precios de Vivienda](https://www.bcentral.cl/en/areas/estadisticas/estadisticas-experimentales/ipv)
- [CChC · Centro de Información](https://cchc.cl/centro-de-informacion)
- [Portal de Datos Abiertos de Chile](https://datos.gob.cl/dataset/)
