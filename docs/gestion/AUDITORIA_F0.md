# AUDITORÍA F0 · Hallazgos Verificados

**Fecha:** 2026-09-27 · **Auditor:** A1 (Claude Haiku) · **Método:** lectura del repo + comandos exactos

---

## Hallazgos Confirmados

| ID | Estado | Hallazgo | Evidencia | Línea de acción |
|---|---|---|---|---|
| H-01 | ✅ CONFIRMADO | Cuatro YAML duplicados y distintos | `clases.yaml`: 113 vs 702 líneas; `curriculum.yaml`: 53 vs 461; `grafo.yaml`: 117 vs 549; `dudas.yaml`: 4 vs 244 | Epic E-1: Fusionar y elegir canónico |
| H-02 | ✅ CONFIRMADO | 22 visuales declarados pero NO existen | `python3 -c "import yaml; from pathlib import Path; ... faltan.append()"` → 22 registros | Epic E-1: Corregir rutas (opción: renombrar archivos reales o editar manifiesto) |
| H-03 | ⚠️ CAMBIÓ | Numeración: archivos tienen prefijo numérico (01_, 02_, ...) pero manifiesto usa nombres sin número | `ls 07_DATITO/01_CONCEPTOS/visual/ \| head` muestra `01_fundamentos...`, `02_datos...` | Epic E-2: Alinear convención de nombre |
| H-04 | ✅ CONFIRMADO | Clase 19 pendiente: `visual: null` en manifiesto | Línea 680 de `00_INICIO/clases.yaml` | Epic E-3: Construir o marcas explícitamente como archivada |
| H-05 | ✅ CONFIRMADO | Dos carpetas código solapadas: `03_SCRIPTS/` (42 archivos) vs `03_CODIGO/` (14 archivos) | `ls 03_SCRIPTS 03_CODIGO \| wc -l` | Epic E-2: Fusionar en una estructura limpia |
| H-06 | ✅ CONFIRMADO | Skills duplicadas en `.claude/skills/` y `.agents/skills/` | `find . -name "*.md" -path "*/skills/*"` → dos copias | Epic E-2: Una fuente, enlaces o sincronización |
| H-07 | ✅ CONFIRMADO | Plantilla espejada en dos directorios; dos archivos `index.html` | `ls 07_DATITO/visual/_TEMPLATE_CANONICO.html` y `ls 07_DATITO/01_CONCEPTOS/visual/_TEMPLATE_CANONICO.html` | Epic E-2: Una plantilla canónica |
| H-08 | ✅ CONFIRMADO | `construir_navegacion.py` (949 líneas) con bugs documentados | `07_DATITO/07_BITACORA/TECH_DEBT.md` lista 4 bugs | Epic E-2: Reparar o reemplazar |
| H-09 | ✅ CONFIRMADO | Sprint 03: 3 de 9 visuales aprobados (bloqueados: #02, #05, #08, #09, #14, #19) | Commits del 26-09 en `git log \| grep -i sprint` | Epic E-3: Desbloquear |
| H-10 | ✅ CONFIRMADO | Estado contradictorio: 50 % y 66 % de cobertura en distintos documentos | `ESTADO_PROYECTO.txt` línea 7 vs README vs web visual | Epic E-1: Generar estado desde manifiesto, no a mano |
| H-11 | ✅ CONFIRMADO | Sin `.github/`: no hay plantillas de issue, PR template ni CI; tests no corren | `ls .github/` → no existe; `test_*.py` solo locales | Epic E-4: Crear CI y plantillas |
| H-12 | ✅ CONFIRMADO | Gestión vive en archivos (`TECH_DEBT.md`, `results.tsv`, `agent_lessons.yaml`) no en issues | `grep -r "TODO\|FIXME\|BUG" 07_DATITO/07_BITACORA/` | Epic E-6: Migrar a GitHub Issues |
| H-13 | ✅ CONFIRMADO | Peso: `.git` ≈ 229 MB, `10_ARCHIVO/` ≈ 300 MB | `du -sh .git 10_ARCHIVO/` | Decision reservada: LFS o limpieza historial |
| H-14 | ✅ CONFIRMADO | Repo público contiene material de terceros (transcripciones de UdeC, voces) | `05_CLASES/transcripciones/` (15 MD), `10_ARCHIVO/courses/` (30+ PDF) | Decision reservada: privado, repo separado, o eliminar |
| H-15 | ✅ CONFIRMADO | «Guillito» todavía en 3 archivos | `grep -r "Guillito"` → 3 líneas | Epic E-5: Limpiar |

---

## Hallazgos Nuevos (NO en H-01 a H-15)

| ID | Hallazgo | Evidencia | Línea de acción |
|---|---|---|---|
| H-16 | Raíz limpia tras mover docs a `01_DOCUMENTACION/` | Commit `8030ac1` del 27-09 | Documentado: aceptar |
| H-17 | Responsive CSS agregado para 390px, 640px, 1280px en los tres certamenes | Commits `f68e058` (media queries) + `11d388d` (Cierre certamen_3) | Documentado: aceptar |
| H-18 | `mapa_ensenanza.yaml` tiene estructura incompleta; `construir_navegacion.py` falla con `KeyError: 'conceptos'` | Ejecución de script, línea 910: `for cid, tramos in mapa["conceptos"].items()` | Epic E-4: Completar estructura o skipear clases incompletas |

---

## Resumen por Área

| Área | Crítica | Alta | Media | Total |
|---|---|---|---|---|
| **Manifiesto (E-1)** | H-01, H-02, H-10 | — | H-04 | 4 |
| **Arquitectura (E-2)** | H-05, H-07, H-08 | H-06 | H-03, H-15 | 6 |
| **Visuales (E-3)** | H-09 | — | — | 1 |
| **CI (E-4)** | H-11 | — | H-18 | 2 |
| **Compliance (E-5)** | H-14 | H-13 | — | 2 |
| **Gestión (E-6)** | H-12 | — | — | 1 |
| (Otros) | — | — | H-16, H-17 | 2 |

---

## Criterios de Aceptación para Gate F0

**Cristóbal debe confirmar:**
- [ ] Los 15 hallazgos iniciales están correctamente verificados (✅ CONFIRMADO, ⚠️ CAMBIÓ, ❌ NO_REPRODUCIBLE)
- [ ] Los 3 hallazgos nuevos (H-16 a H-18) se registran o descartan
- [ ] Se acepta la priorización sugerida (crítica > alta > media)
- [ ] Se procede a F1 (construir backlog)

---

**Salida de F0:** Este documento (`AUDITORIA_F0.md`) + `inventario.json` (próximo).

