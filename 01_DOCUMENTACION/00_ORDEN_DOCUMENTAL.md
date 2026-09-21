# Orden documental — protocolo MACI

**Arquitectura:** A — repo-nativo (README → índice → `00_LEEME` → canónicos → fuentes/archivo).  
**Fuente de verdad:** el repositorio en `F:\MACI`. No hay segunda copia canónica en Obsidian.

---

## Capas

```
1. Entrada          README.md
2. Índice           01_DOCUMENTACION/00_INDICE_GENERAL.md
3. Dominio          …/<dominio>/00_LEEME.md
4. Canónicos        informes, análisis, pitch, resultados JSON
5. Fuentes/Archivo  …/fuentes/  ·  99_ARCHIVO/  ·  10_GRABACIÓN_CLASES/
```

Regla: un agente o humano que solo abre el README debe llegar al documento útil en **≤ 3 saltos**.

---

## Qué es canónico

| Tema | Canónico | No mezclar con |
|---|---|---|
| Cifras Melbourne reproducibles | `05_RESULTADOS/resultados_temporal.json` | Narrativas con cifras distintas sin citar el JSON |
| Informe Proyecto 3 | `06_ENTREGABLES/INFORME_MODELO_FCD_P3.md` | Copias en raíz o en `DOCUMENTACION/` |
| Pitch Hito 2 | `06_ENTREGABLES/PITCH_HITO2_REVISION.md` (+ pptx/pdf ahí) | Rutas antiguas a la raíz |
| Expediente Certamen 2 | `01_DOCUMENTACION/01_CERTAMEN2/` (LEEME → md → Word) | `DOCUMENTACION/01_CERTAMEN2/` (legacy) |
| Originales certamen | `01_CERTAMEN2/fuentes/` | No editar; no “limpiar” |
| Datito estado | `07_DATITO/progreso.yaml` + `estado.md` | Inventar progreso en el chat |
| Obsoleto | `99_ARCHIVO/` + `05_HISTORICO/` | Reintroducir como vigente |

---

## Dónde va un documento nuevo

| Tipo | Destino |
|---|---|
| Mapa / protocolo / índice | `01_DOCUMENTACION/` |
| Expediente de un certamen | `01_DOCUMENTACION/0N_<TEMA>/` + actualizar `00_LEEME` e índice |
| Original intacto (docx/pdf/eml) | `…/fuentes/` del dominio |
| Entregable del curso (informe, pitch) | `06_ENTREGABLES/` |
| Salida de script | `05_RESULTADOS/` (nunca editar a mano como verdad) |
| Material de estudio Datito | `07_DATITO/` según tipo (guias/cuadernillos/…) |
| Transcripción de clase | `09_CLASES/transcripciones/` |
| Presentación/markdown de diapositivas | `11_PRESENTACIÓN/` |
| Invalidado a propósito | `99_ARCHIVO/` o `05_HISTORICO/` + nota en LEEME |

Naming: prefijo numérico `00_`… para orden de lectura; `00_LEEME.md` siempre es la puerta del dominio.

---

## Matriz necesidad → ruta

| Necesidad | Ruta |
|---|---|
| Orientarse en el repo | `README.md` → `00_INDICE_GENERAL.md` |
| Defensa oral Certamen 2 | `01_CERTAMEN2/00_LEEME` → mapa → defensa oral |
| Expediente completo Certamen 2 | análisis md o Word consolidado |
| Fechas/metadatos de archivos del certamen | `01_CERTAMEN2/AUDITORIA_FORENSE_FECHAS_DOCUMENTOS.md` |
| Formato de evaluación (Certamen 1, enunciados) | `06_CERTAMEN1/00_LEEME` (respuestas de tercero = baja fiabilidad) |
| Defender Proyecto 3 | `03_PROYECTO_MELBOURNE/00_LEEME` → informe + pitch en `06_ENTREGABLES/` |
| Reproducir cifras | `README` “Reproducir” + `05_RESULTADOS/*.json` |
| Estudiar con tutor | `07_DATITO/00_LEEME.md` · `spec.md` |
| Prácticos | `08_PRACTICA/00_LEEME` |
| Clases | `09_CLASES/00_LEEME` |
| Diapositivas en markdown | `11_PRESENTACIÓN/_markdown/` |

---

## Integraciones

| Canal | Estado |
|---|---|
| Markdown en repo / GitHub web | **Sí** — mismos links relativos del README |
| NotebookLM MCP | **Sí** — `.mcp.json` (estudio; no sustituye el índice) |
| Obsidian MCP | **No implementar ahora** — duplicaría verdad sin ganar navegación que el índice no cubra |
| GitHub MCP extra | **No implementar ahora** — basta repo + `push_github.ps1` |

---

## Re-auditar drift

```bash
python 03_CODIGO/auditar_drift_documental.py
```

Esperado: exit 0 si las rutas canónicas del checklist existen; exit 1 si falta alguna.
