# Histórico — Lo que quedó invalidado, y por qué se conserva

Esta carpeta no contiene basura. Contiene el **registro documentado de una corrección**, y por eso se conserva deliberadamente.

---

## `_obsoleto_split_aleatorio\` (raíz del repositorio)

**Qué era:** la primera aproximación al modelamiento del Proyecto 3.

**Por qué quedó invalidada.** El propio `README_POR_QUE_OBSOLETO.md` lo declara sin atenuantes:

> *"Estos archivos se generaron ANTES de leer la guía del curso y contienen:*
> *1. Un split aleatorio 80/20 (viola la instrucción del Proyecto 3: entrenar con 2016, evaluar en 2017).*
> *2. Cifras que NO fueron calculadas (p. ej. 'brecha Train-Test 0.8263/0.8226', 'R² 0.7842', los '%' de importancia del HTML y del informe de justificación). Fueron escritas a mano antes de ejecutar código.*
> *3. Una conclusión ('Gradient Boosting es el mejor') basada en (1) y (2)."*

**Qué lo reemplazó:** el pipeline reproducible de la raíz (`modelamiento_temporal.py` → `resultados_temporal.json` → `INFORME_MODELO_FCD_P3.md`), cuyo §0 se titula *"Fe de erratas (léase primero)"*.

**Contenido de la carpeta:**

| Archivo | Nota |
|---|---|
| `README_POR_QUE_OBSOLETO.md` | La declaración de invalidación. **El documento más importante de la carpeta** |
| `JUSTIFICACION_MODELO_MACI_FCD.md` | Informe de justificación con la tabla `R² Train / R² Test / Brecha / Interpretación`. Las cifras están invalidadas, pero el **criterio** (menor brecha = mejor generalización) se mantuvo en la versión final |
| `ANALISIS_HOUSING_MELBOURNE.md` | Análisis descriptivo temprano |
| `JUSTIFICACION_VISUAL.txt`, `RESUMEN_EJECUTIVO.txt`, `RESULTADOS_FINALES.md` | Versiones tempranas |
| `GUIA_RAPIDA.md`, `INDICE_COMPLETO.md`, `00_COMIENZA_AQUI.txt` | Índices de la versión antigua |
| `housing_report.html` | Reporte HTML de la versión antigua |
| `guia_fcd_texto.txt` | Enunciado del curso extraído a texto. **Este sí sigue vigente** — copiado a `..\02_CURSO\` |

---

## `_backup_pre_correlacion_20260904_1813\` (raíz del repositorio)

Respaldo puntual del notebook del Hito 1, tomado antes de un cambio en el análisis de correlación. Sin valor documental propio; se conserva como red de seguridad.

---

## Por qué esto importa

Un repositorio que borra sus errores no puede demostrar que los corrigió. Este conserva:

1. La versión equivocada, completa.
2. Una declaración escrita de **por qué** está equivocada, con los números concretos que no habían sido calculados.
3. La versión correcta, generada desde código y reproducible con semillas fijas.
4. Una fe de erratas al inicio del informe final, antes de presentar cualquier resultado.

En el expediente del Certamen 2 (`..\01_CERTAMEN2\`) esta secuencia es la evidencia que sostiene el hallazgo principal: existe un ciclo completo y documentado de **pregunta → interpretación inicial → identificación del concepto → explicación → contraste → corrección → justificación → respuesta**, con las ocho etapas identificables en archivos concretos.

Ese ciclo está documentado sobre el **proyecto**, no sobre el certamen. La distinción es importante y está mantenida en todo el expediente.
