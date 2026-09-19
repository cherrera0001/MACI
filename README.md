# F:\MACI — Índice maestro del repositorio

Repositorio de trabajo de **Fundamentos de Ciencia de Datos (T2-2026)**, Universidad de Concepción.
Contiene el proyecto semestral (Proyecto 3 — predicción de precios de propiedades en Melbourne), un desafío de clasificación (Galaxy Zoo), y la reconstrucción documental del Certamen 2.

**Punto de entrada recomendado:** [`01_DOCUMENTACION/00_INDICE_GENERAL.md`](01_DOCUMENTACION/00_INDICE_GENERAL.md)

---

## Estructura

Nueve entradas en la raíz. Ningún documento suelto.

```
F:\MACI\
│
├── README.md                       ← este archivo
│
├── 01_DOCUMENTACION\               ← EMPEZAR AQUÍ
│   ├── 00_INDICE_GENERAL.md            mapa completo, paso a paso
│   ├── 01_CERTAMEN2\                   reconstrucción del Certamen 2 + Word final
│   │   ├── 00_LEEME.md
│   │   ├── 01_ANALISIS_RECONSTRUCCION_CERTAMEN.md
│   │   ├── 02_MAPA_PROCESO_ESTUDIO.md
│   │   ├── 03_DEFENSA_ORAL_CERTAMEN.md
│   │   ├── Certamen2_Reconstruccion_Completa.docx   ← el Word
│   │   ├── _construir_word.py          regenera el Word desde los .md
│   │   └── fuentes\                    los dos originales, intactos
│   ├── 02_CURSO\                       enunciados y guía metodológica
│   ├── 03_PROYECTO_MELBOURNE\          índice del Proyecto 3
│   ├── 04_DESAFIO_GALAXYZOO\           índice del desafío de clasificación
│   └── 05_HISTORICO\                   versiones invalidadas y por qué
│
├── 02_PROYECTO_FCD\                ← material del curso
│   ├── Hito1\                          notebooks EDA y modelamiento + anclaje.json
│   └── Desafio\                        Galaxy Zoo: código, análisis, REPORT.md
│
├── 03_CODIGO\                      ← scripts del pipeline
│   ├── modelamiento_temporal.py        jerarquía de modelos, CV 2016, test 2017
│   ├── bootstrap_comparacion.py        bootstrap pareado, segmentos, permutación
│   ├── preparar_dashai.py              prepara el dataset para DashAI
│   ├── dashai_driver.py                réplica del modelamiento en DashAI
│   ├── generar_informe.py              → 06_ENTREGABLES/INFORME_MODELO_FCD_P3.md
│   ├── generar_pitch_v2.py             → 06_ENTREGABLES/PITCH_HITO2_REVISION.md + .pptx
│   ├── housing_visualizations.py       → 06_ENTREGABLES/visualizaciones/viz_*.html
│   ├── auditoria_dashai_vs_crudo.py    auditoría de consistencia
│   ├── correlacion_dashai.py           análisis de correlación
│   └── _migrar_rutas.py                registro auditable de la migración de rutas
│
├── 04_DATOS\
│   └── housing_dashai_2016_2017.csv    dataset preprocesado subido a DashAI
│
├── 05_RESULTADOS\                  ← salidas de los scripts, ninguna a mano
│   ├── resultados_temporal.json        6 modelos × 2 targets × 5 semillas
│   ├── comparacion_estadistica.json    IC bootstrap, error por segmento, importancias
│   ├── dashai_resultados.json          runs de DashAI
│   ├── dashai_split_indices.json       índices del split manual
│   ├── dashai_state.json               estado de la sesión DashAI
│   ├── correlacion_dashai.json         matriz de correlación replicada
│   ├── auditoria_dashai_vs_crudo.json  auditoría de consistencia
│   └── predicciones_2017.csv           predicciones fila a fila del modelo final
│
├── 06_ENTREGABLES\
│   ├── INFORME_MODELO_FCD_P3.md        informe final del modelamiento
│   ├── PITCH_HITO2_REVISION.md         revisión lámina por lámina
│   ├── Pitch_Hito2_v2.pptx / .pdf      presentación Hito 2
│   └── visualizaciones\viz_1..10.html  visualizaciones interactivas
│
├── 07_GUILLITO\                ← tutor personal de Ciencia de Datos
│   ├── 00_LEEME.md                 cómo se usa
│   ├── curriculum.yaml             21 conceptos, orden, prerrequisitos, material
│   ├── progreso.yaml               estado y cadena de evidencia por concepto
│   ├── errores_conceptuales.yaml   errores observados + patrones a vigilar
│   └── bitacora\                   una entrada por sesión
│
└── 99_ARCHIVO\                     ← conservado a propósito, no es basura
    ├── _obsoleto_split_aleatorio\      versión invalidada + el README que explica por qué
    ├── _backup_pre_correlacion_...\    respaldo puntual
    ├── _pitch_img\ · _pitch_v2_png\    imágenes de las presentaciones
    └── CORRELACION_DIFF.patch
```

---

## Guillito — tutor personal

Abre Claude Code en `F:\MACI` y escribe, por ejemplo:

```
Guillito, quiero aprender validación cruzada
```

Guillito consulta el cuaderno de NotebookLM y el material del repositorio,
explica, pregunta, **espera tu respuesta**, analiza tu razonamiento y registra el
avance en `07_GUILLITO/progreso.yaml`. Un concepto solo llega a `DOMINADO` con
las tres evidencias: explicar, aplicar y transferir a un problema nuevo.

Estado de aprendizaje: `/guillito-progreso`. Detalle completo en
[`07_GUILLITO/00_LEEME.md`](07_GUILLITO/00_LEEME.md).

---

## Reproducir el proyecto completo

Ejecutar **desde `F:\MACI`** (no desde `03_CODIGO`), en este orden:

```bash
python 03_CODIGO/modelamiento_temporal.py     # jerarquía de modelos, CV en 2016, test 2017
python 03_CODIGO/bootstrap_comparacion.py     # bootstrap pareado, segmentos, permutación
python 03_CODIGO/preparar_dashai.py
python 03_CODIGO/dashai_driver.py all         # réplica independiente en DashAI
python 03_CODIGO/generar_informe.py           # informe final
python 03_CODIGO/generar_pitch_v2.py          # revisión del pitch + presentación
```

Regenerar el Word del expediente del certamen:

```bash
python 01_DOCUMENTACION/01_CERTAMEN2/_construir_word.py
```

---

## Nota sobre la reestructuración (15-09-2026)

El repositorio tenía 45 entradas sueltas en la raíz. Se reorganizó por función: documentación, material del curso, código, datos, resultados, entregables y archivo histórico.

**Las rutas de los scripts fueron migradas** para que el pipeline siga funcionando. El script `03_CODIGO/_migrar_rutas.py` conserva la lista exacta de los 9 archivos tocados y los reemplazos aplicados; se dejó en el repositorio como registro auditable en vez de borrarlo. La migración se verificó de dos formas: las 45 referencias a archivos resuelven correctamente, y `generar_informe.py` se ejecutó de extremo a extremo produciendo el informe sin errores.

**Ningún archivo original fue modificado.** Los dos documentos del certamen —el de respuestas y la guía de estudio— están intactos en `01_DOCUMENTACION\01_CERTAMEN2\fuentes\`.
