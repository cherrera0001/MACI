# Diagnóstico de drift documental — MACI

**Fecha:** 2026-09-20  
**Alcance:** README.md + `00_INDICE_GENERAL.md` vs inventario real en disco.  
**Sin mover ni borrar evidencia.**

---

## Qué declara el README / índice

| Fuente | Declara |
|---|---|
| README árbol | `01_DOCUMENTACION` con dominios 01…05; no menciona `06_CERTAMEN1` ni `11_PRESENTACIÓN` |
| README | Entregables en `06_ENTREGABLES/`; scripts en `03_SCRIPTS/` |
| README | `02_DATOS/` ≈ solo `housing_dashai_2016_2017.csv` |
| Índice | Certamen 2: LEEME → análisis → mapa → defensa → Word → fuentes (2 docx) |
| Índice rutas Proyecto 3 | `..\INFORME_MODELO_FCD_P3.md` y `..\PITCH_…` **en la raíz** |
| Índice | No lista Certamen 1 ni auditoría forense de fechas |

---

## Qué existe realmente

| Ítem | Estado |
|---|---|
| `01_DOCUMENTACION/06_CERTAMEN1/` + `00_LEEME.md` | Existe; ausente del README e índice |
| `01_DOCUMENTACION/01_CERTAMEN2/AUDITORIA_FORENSE_FECHAS_DOCUMENTOS.md` | Existe; ausente del índice |
| `01_CERTAMEN2/fuentes/` | Incluye docx + pdf guía + otros; índice dice “dos originales” |
| `11_PRESENTACIÓN/` | Existe (markdown de clases/PPT); ausente del README |
| `DOCUMENTACION/` (sin `01_`) | Carpeta legacy con solo `01_CERTAMEN2/` parcial; **no es canónica** |
| `02_DATOS/` | También `GZ_mini_challenge_*.csv` + `00_LEEME.md` |
| `06_ENTREGABLES/INFORME_…` y `PITCH_…` | Existen aquí; **no** en la raíz |
| `08_PROYECTO_FCD/Hito1/` | Canónico actual; `Fundamentos de ciencia de datos\Hito1\` **no existe** |
| `00_LEEME.md` por dominio | Presentes en certámenes, curso, Melbourne, Galaxy, histórico, datos, Datito, práctica, clases |

---

## Huecos / huérfanos / rutas rotas

| Tipo | Detalle |
|---|---|
| **Ruta rota** | Índice: `..\INFORME_MODELO_FCD_P3.md` (raíz) → debe ser `../../06_ENTREGABLES/…` desde el índice o ruta desde dominio |
| **Ruta rota** | `03_PROYECTO_MELBOURNE/00_LEEME.md` apunta a `Fundamentos de ciencia de datos\Hito1\` |
| **Drift README** | Falta `06_CERTAMEN1`, `11_PRESENTACIÓN`, Galaxy CSV en datos |
| **Drift índice** | Falta Certamen 1, auditoría forense, PDF en fuentes |
| **Huérfano / legacy** | `DOCUMENTACION\` (duplicado parcial); `deep-research-report.md` en raíz sin entrada |
| **MCP** | Solo NotebookLM en `.mcp.json`; no Obsidian |

---

## Decisión tomada a partir de este diagnóstico

**Arquitectura A — repo-nativo.** El repo ya tiene numeración + LEEME; el fallo es sincronización, no falta de vault. Obsidian MCP no aporta flujo nuevo frente a Markdown + NotebookLM. GitHub se navega con los mismos links relativos del README (ya existe `push_github.ps1`).
