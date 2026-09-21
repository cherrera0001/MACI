# Certamen 2 — Expediente de reconstrucción

## Qué es esto

Un análisis de **si el material local de `F:\MACI` permite reconstruir un proceso de comprensión** que explique cómo se resolvieron las preguntas del Certamen 2 de Fundamentos de Ciencia de Datos (28 de agosto de 2026).

> **Corrección estructural, 2026-09-20.** Este expediente y todos sus documentos
> hablan de **11 preguntas**. El registro de Canvas muestra **10 preguntas
> numeradas más un «Espaciador»** (`text_only_question`, **0 puntos**) que
> contiene el ítem de la matriz de confusión. Desde ese ítem en adelante, la
> numeración de estos documentos va **corrida en uno** respecto del sistema:
> lo que aquí es P8/P9/P10/P11 es en Canvas Espaciador/P8/P9/P10.
>
> Los análisis de contenido **siguen siendo válidos** —los temas y su
> tratamiento no cambian—, pero **no cites números de pregunta**: nómbralas por
> tema. Evidencia en
> [`../../07_DATITO/visual/certamen_2.html`](../../07_DATITO/visual/certamen_2.html).

## Qué NO es

- **No es una defensa legal ni administrativa.** No intenta demostrar inocencia.
- **No intenta probar que no se usó IA.** El uso de IA está declarado por el autor y no es lo que este documento evalúa.
- **No determina si hubo o no una infracción académica.** Esa es una decisión institucional, no una conclusión derivable de archivos.
- **No usa Git, logs ni timestamps como argumento.** Las fechas se mencionan una sola vez, en la revisión adversarial, y solo para acotar hasta dónde llega la evidencia.

## La pregunta que sí responde

> ¿Puede reconstruirse, a partir del material local, un proceso de comprensión que explique cómo se resolvieron las preguntas del certamen?

Las tres respuestas admisibles eran: **sí**, **parcialmente**, o **no hay evidencia suficiente**.

**La respuesta obtenida fue: PARCIALMENTE.**

## Resultado en una tabla

| Nivel de evidencia | Preguntas | Total |
|---|---|---|
| **FUERTE** | P1 ensambles · P2 sobreajuste · P3 causas · P4 métricas · P7 polinomial · P11 supuestos | 6 |
| **PARCIAL** | P5 LLMs · P6 revoluciones IA · P8 matriz de confusión · P9 curva ROC | 4 |
| **INSUFICIENTE** | — | 0 |
| No evaluable | P10 punto base | 1 |

## Los tres hallazgos que conviene conocer antes de leer nada más

**1. Sí existe material de estudio, y su diseño es de comprensión, no de memorización.**
`Guia_Estudio_Certamen2_Fundamentos_Ciencia_Datos.docx` cubre diez de las once preguntas. Cada concepto se trabaja con una analogía cotidiana, una traducción técnica, tres ejemplos de dominios distintos, preguntas de reflexión sin respuesta dada y un ejercicio de transferencia. Su criterio de cierre es *"explicarlo sin usar la definición textual de esta guía"* e *"inventar un ejemplo cotidiano distinto"*.

**La reserva, que no debe omitirse al citarla:** la guía declara en su primer párrafo haberse construido *"tomando las preguntas del Certamen 2 como puntos de partida"*, y sus metadatos no permiten fecharla. Evidencia comprensión del contenido evaluado; no establece qué se comprendía al rendir. Además, los siete campos `Respuesta propia: ____` de su interrogación final están en blanco.

**2. Sí existe un ciclo completo de comprensión documentado — pero sobre el proyecto, no sobre el certamen.**
Pregunta → interpretación inicial → identificación del concepto → explicación → contraste → **corrección** → justificación → respuesta. Las ocho etapas son identificables en archivos concretos, incluida una autoinvalidación por escrito de cifras propias (`README_POR_QUE_OBSOLETO.md`, "Fe de erratas" del informe final). Este es el hallazgo más sólido del expediente.

**3. Hay una contradicción numérica real en la pregunta 9.**
El documento declara AUC ≈ 0,78 y ≈ 0,68. Calculando el área por trapecios sobre **los propios puntos de su tabla**, da ≈ 0,894 y ≈ 0,785. La conclusión (Modelo 1 es mejor) es correcta y además demostrable por dominancia, que es un argumento más fuerte. Pero esas dos cifras de AUC no son derivables del documento que las contiene. No se ocultó este hallazgo: está en la Fase 5.3 del análisis y señalado en la guía de defensa oral.

## Orden de lectura

| # | Documento | Extensión |
|---|---|---|
| 1 | Este archivo | 2 min |
| 2 | [`02_MAPA_PROCESO_ESTUDIO.md`](02_MAPA_PROCESO_ESTUDIO.md) — matriz de las 11 preguntas y patrones globales | 15 min |
| 3 | [`03_DEFENSA_ORAL_CERTAMEN.md`](03_DEFENSA_ORAL_CERTAMEN.md) — guion de trabajo por pregunta | 30 min, más práctica en voz alta |
| 4 | [`01_ANALISIS_RECONSTRUCCION_CERTAMEN.md`](01_ANALISIS_RECONSTRUCCION_CERTAMEN.md) — análisis completo en 5 fases | 60 min |
| — | [`Certamen2_Reconstruccion_Completa.docx`](Certamen2_Reconstruccion_Completa.docx) — los tres consolidados en un Word | equivalente |
| — | [`AUDITORIA_FORENSE_FECHAS_DOCUMENTOS.md`](AUDITORIA_FORENSE_FECHAS_DOCUMENTOS.md) — solo si la pregunta es cronología de archivos | técnico |

## Contenido del certamen (referencia rápida)

| # | Tema |
|---|---|
| 1 | Ensambles y diversidad (V/F) |
| 2 | Sobreajuste y generalización (V/F) |
| 3 | Causas y consecuencias del sobreajuste (selección múltiple) |
| 4 | Métricas de clasificación (selección) |
| 5 | LLMs y agentes (selección) |
| 6 | Revoluciones recientes en IA (selección) |
| 7 | Regresión polinomial y sobreajuste (desarrollo) |
| 8 | Matriz de confusión y métricas (cálculo) |
| 9 | Curva ROC y comparación de modelos (cálculo) |
| 10 | Punto base (sin responder: figura no disponible) |
| 11 | Comentarios y supuestos (declaración) |

## Regla que rige todo el expediente

> No fabricar evidencia. No atribuir pensamientos no documentados. No modificar archivos originales. No confundir similitud textual con comprensión.

Donde el material no alcanza, el expediente lo dice explícitamente. Esa es la única razón por la que sus conclusiones positivas pueden tomarse en serio.
