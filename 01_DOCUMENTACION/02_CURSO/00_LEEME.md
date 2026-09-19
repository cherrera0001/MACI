# Curso — Enunciados y reglas de evaluación

Material oficial del ramo **4321001-0 Fundamentos de Ciencias de Datos (T2-2026)**, Universidad de Concepción.

| Archivo | Qué es |
|---|---|
| `Proyectos FCD 2026-2 (6).pdf` | Enunciado oficial de los proyectos del semestre |
| `guia_fcd_texto.txt` | Texto extraído del enunciado, legible y buscable |
| `Guia_metodologica_proyecto_FCD.docx` | Guía metodológica del proyecto |

---

## La instrucción que gobierna el Proyecto 3

> *"En este proyecto deberán usar las ventas de propiedades para entrenar un modelo predictivo con datos del 2016, y luego predecir y evaluar su modelo sobre las propiedades del año 2017."*

Esta frase es la razón por la que todo el modelamiento usa **partición temporal** y no un split aleatorio. La primera versión del trabajo usó 80/20 aleatorio y por eso quedó invalidada (ver `..\05_HISTORICO\00_LEEME.md`).

---

## Estructura de evaluación

**Hito 1 — Presentación oral de análisis exploratorio** (viernes 14 de agosto)

| Componente | Peso |
|---|---|
| Introducción | 15 % |
| Descripción de los datos | 15 % |
| Análisis exploratorio | 15 % |
| Presentación | 25 % |
| **Preguntas** | **30 %** |

**Hito 2 — Presentación oral final** (viernes 4 de septiembre)

| Componente | Peso |
|---|---|
| Introducción | 10 % |
| Descripción de los datos y análisis exploratorio | 10 % |
| Modelamiento | 15 % |
| Resultados | 15 % |
| Presentación | 20 % |
| **Preguntas** | **30 %** |

No se entrega informe escrito asociado al proyecto. En ambos hitos, **el 30 % de la nota son las preguntas del examinador**: el dominio conceptual pesa más que cualquier otro componente individual.

---

## Los tres proyectos ofrecidos

| # | Proyecto | Tipo de problema |
|---|---|---|
| 1 | Predicción de calidad en planta de flotación minera (% de sílice) | Regresión |
| 2 | Diagnóstico de cáncer de mama (maligno / benigno) | Clasificación binaria |
| 3 | **Predicción de valor de propiedades (Melbourne 2016 → 2017)** | Regresión con partición temporal — **el elegido** |

---

## Nota para el expediente del Certamen 2

Este material es el enunciado del **proyecto**, no del certamen. Dos advertencias que importan al leer el análisis de reconstrucción:

- No contiene contenidos teóricos: es un enunciado con datasets y pesos de evaluación. No sirve como material de estudio para las preguntas del certamen.
- Produce **falsos positivos** en búsquedas por palabra clave: la palabra "agente" aparece como *"Agente de bienes raíces"* (columna `SellerG`) y la palabra "pureza" como *"% de Silica (impureza)"*. Ninguna de las dos es evidencia sobre agentes de IA ni sobre ganancia de pureza. Así está declarado en la Fase 1.4 del análisis.
