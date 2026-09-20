# Índice general de la documentación

Guía paso a paso del material del repositorio, ordenado por para qué sirve.
Si no sabes por dónde empezar, sigue las **rutas de lectura** del final.

**Protocolo (canónicos, capas, dónde va un archivo nuevo):** [`00_ORDEN_DOCUMENTAL.md`](00_ORDEN_DOCUMENTAL.md)  
**Drift README↔disco:** [`DIAGNOSTICO_DRIFT.md`](DIAGNOSTICO_DRIFT.md)

---

## 01 · CERTAMEN 2 — Reconstrucción del proceso de estudio

Carpeta: [`01_CERTAMEN2/`](01_CERTAMEN2/)

| Orden | Documento | Qué contiene | Cuándo leerlo |
|---|---|---|---|
| 0 | [`00_LEEME.md`](01_CERTAMEN2/00_LEEME.md) | Qué es este expediente, qué afirma y qué no | Siempre primero |
| 1 | [`01_ANALISIS_RECONSTRUCCION_CERTAMEN.md`](01_CERTAMEN2/01_ANALISIS_RECONSTRUCCION_CERTAMEN.md) | Análisis completo en 5 fases | Documento principal |
| 2 | [`02_MAPA_PROCESO_ESTUDIO.md`](01_CERTAMEN2/02_MAPA_PROCESO_ESTUDIO.md) | Matriz de las 11 preguntas + patrones | Vista de conjunto |
| 3 | [`03_DEFENSA_ORAL_CERTAMEN.md`](01_CERTAMEN2/03_DEFENSA_ORAL_CERTAMEN.md) | Guion oral por pregunta | Preparar instancia oral |
| 4 | [`Certamen2_Reconstruccion_Completa.docx`](01_CERTAMEN2/Certamen2_Reconstruccion_Completa.docx) | Los tres md consolidados en un Word | Lectura / impresión única |
| 5 | [`AUDITORIA_FORENSE_FECHAS_DOCUMENTOS.md`](01_CERTAMEN2/AUDITORIA_FORENSE_FECHAS_DOCUMENTOS.md) | Fechas observables (FS, OOXML, PDF); qué se puede y no se puede afirmar | Solo cronología de archivos |
| — | [`fuentes/`](01_CERTAMEN2/fuentes/) | Originales: respuestas (Recuperado automáticamente), guía `.docx` / `.pdf`, y otros adjuntos | Referencia; no editar |

**Conclusión del expediente, en una línea:** el material local permite reconstruir **parcialmente** un proceso de comprensión — con doble anclaje (guía de estudio + trabajo propio) en seis de las once preguntas, anclaje solo en la guía en otras, y zonas que ningún archivo explica del todo (secuencia temporal del estudio; cifras AUC de P9).

---

## 02 · CURSO — Enunciados y reglas de evaluación

Carpeta: [`02_CURSO/`](02_CURSO/) · puerta: [`00_LEEME.md`](02_CURSO/00_LEEME.md)

| Archivo | Qué es |
|---|---|
| `Proyectos FCD 2026-2 (6).pdf` | Enunciado oficial |
| `guia_fcd_texto.txt` | Texto extraído (instrucción 2016→2017) |
| `Guia_metodologica_proyecto_FCD.docx` | Guía metodológica |

Pesos Hito 2 (referencia): Modelamiento 15 %, Resultados 15 %, Presentación 20 %, **Preguntas 30 %**.

---

## 03 · PROYECTO MELBOURNE — Hito 1 y Hito 2

Índice: [`03_PROYECTO_MELBOURNE/00_LEEME.md`](03_PROYECTO_MELBOURNE/00_LEEME.md)

Predicción de precio: entrenar 2016, evaluar 2017. Núcleo del trabajo propio del semestre.

**Cifras reproducibles:** [`05_RESULTADOS/resultados_temporal.json`](../05_RESULTADOS/resultados_temporal.json) (el JSON manda si hay discrepancia narrativa).  
**Informe / pitch:** [`06_ENTREGABLES/INFORME_MODELO_FCD_P3.md`](../06_ENTREGABLES/INFORME_MODELO_FCD_P3.md) · [`06_ENTREGABLES/PITCH_HITO2_REVISION.md`](../06_ENTREGABLES/PITCH_HITO2_REVISION.md)

---

## 04 · DESAFÍO GALAXY ZOO — Clasificación

Índice: [`04_DESAFIO_GALAXYZOO/00_LEEME.md`](04_DESAFIO_GALAXYZOO/00_LEEME.md)

Clasificación multiclase; fuente local de matriz de confusión, precision/recall/F1, AUC y ensambles.

---

## 05 · HISTÓRICO — Invalidado a propósito

Índice: [`05_HISTORICO/00_LEEME.md`](05_HISTORICO/00_LEEME.md)

Registro de corrección (split aleatorio → temporal). No es basura.

---

## 06 · CERTAMEN 1 — Material de un compañero

Índice: [`06_CERTAMEN1/00_LEEME.md`](06_CERTAMEN1/00_LEEME.md)

**Uso:** enunciados y tablas = alta utilidad para formato de evaluación.  
**No usar** justificaciones como pauta oficial (procedencia de tercero; plantilla sin validar).

---

## Fuera de `01_DOCUMENTACION` (pero en el orden de lectura)

| Dominio | Puerta |
|---|---|
| Guillito | [`07_GUILLITO/00_LEEME.md`](../07_GUILLITO/00_LEEME.md) |
| Prácticos | [`08_PRACTICA/00_LEEME.md`](../08_PRACTICA/00_LEEME.md) |
| Clases | [`09_CLASES/00_LEEME.md`](../09_CLASES/00_LEEME.md) |
| Presentaciones (md) | [`11_PRESENTACIÓN/_markdown/`](../11_PRESENTACIÓN/_markdown/) |
| Datos | [`04_DATOS/00_LEEME.md`](../04_DATOS/00_LEEME.md) |

---

## Rutas de lectura

**Defensa oral Certamen 2 (2–3 h):**
1. `01_CERTAMEN2/00_LEEME.md`
2. `01_CERTAMEN2/02_MAPA_PROCESO_ESTUDIO.md`
3. `01_CERTAMEN2/03_DEFENSA_ORAL_CERTAMEN.md`
4. Fichas P8 y P9 del análisis completo

**Expediente completo Certamen 2:**
1. `01_ANALISIS_RECONSTRUCCION_CERTAMEN.md`, o
2. `Certamen2_Reconstruccion_Completa.docx`

**Defender Proyecto 3:**
1. `03_PROYECTO_MELBOURNE/00_LEEME.md`
2. `06_ENTREGABLES/INFORME_MODELO_FCD_P3.md`
3. `06_ENTREGABLES/PITCH_HITO2_REVISION.md`

**Reproducibilidad / cifras:**
1. `05_HISTORICO/00_LEEME.md`
2. Informe § fe de erratas
3. `05_RESULTADOS/resultados_temporal.json` + scripts del README

**Estudiar con Guillito:**
1. `07_GUILLITO/00_LEEME.md`
2. `spec.md`

---

## Convención de etiquetas

| Etiqueta | Significado |
|---|---|
| **[EVIDENCIA]** | Explícito en un archivo, con cita y ruta |
| **[INFERENCIA]** | Derivado razonable, no escrito |
| **[NO EVIDENCIADO]** | No se sostiene con el material disponible |
