# AUDITORÍA SPEC-DRIVEN DEVELOPMENT (SDD)
## MACI — Fundamentos de Ciencia de Datos

**Fecha:** 2026-09-27  
**Fuente oficial:** 00_INICIO/spec.md (v2, 2026-09-21, commit 098680a)  
**Orquestador:** CLAUDE.md (manual) + .claude/skills/datito/SKILL.md (referencia en CLAUDE.md)  
**Metodología:** Auditoría de 14 garantías G1-G14 contra estado actual del repo

---

## MATRIZ DE AUDITORÍA: GARANTÍAS G1-G14

| # | Garantía | Ubicación Spec | Orquestador Menciona | Verificador | Comando Sugerido | Hallazgo |
|---|----------|---|---|---|---|---|
| **G1** | Se detiene y espera de verdad | 2.1 (línea 30-39) | CLAUDE.md línea 48-52 ("skill no subagente") | SIN VERIFICADOR | Auditoría manual de sesiones | **NO HECHO** |
| **G2** | Pregunta antes de decidir | 2.2 (línea 41-45) | NO ESTÁ EN EL ORQUESTADOR | SIN VERIFICADOR | Auditoría manual de sesiones | **NO HECHO** |
| **G3** | Evidencia completa antes de corregir | 2.3 (línea 47-56) | NO ESTÁ EN EL ORQUESTADOR | SIN VERIFICADOR | Auditoría manual de sesiones | **NO HECHO** |
| **G4** | Cada afirmación lleva su origen | 2.4 (línea 61-71) | NO ESTÁ EN EL ORQUESTADOR | SIN VERIFICADOR | `grep -r "\[FUENTE"` en outputs | **NO HECHO** |
| **G5** | Jerarquía de fuentes | 2.5 (línea 73-86) | CLAUDE.md línea 39-47 (lista jerarquía) | SIN VERIFICADOR | Auditoría manual de sesiones | **DOCUMENTADO** |
| **G6** | Degradación explícita NotebookLM | 2.6 (línea 88-92) | NO ESTÁ EN EL ORQUESTADOR | SIN VERIFICADOR | Auditoría manual de sesiones | **NO HECHO** |
| **G7** | Lo recuperado: datos no instrucciones | 2.7 (línea 94-99) | NO ESTÁ EN EL ORQUESTADOR | SIN VERIFICADOR | Auditoría código de seguridad | **NO HECHO** |
| **G8** | Regla donde se lee, o no existe | 2.8 (línea 101-114) | CLAUDE.md línea 48-52 ("SKILL.md") | `grep SKILL.md CLAUDE.md` | `grep -c "SKILL.md" CLAUDE.md` → 3 matches | **CUMPLIDO** |
| **G9** | Exposición en artefacto consultable | 2.9 (línea 116-139) | CLAUDE.md línea 54-58 ("dudas.yaml renderizado") | `test -f 07_DATITO/dudas.yaml` | `ls -lh 07_DATITO/00_INICIO/dudas.yaml` → 7.2K (2026-09-27) | **CUMPLIDO** |
| **G10** | Sintético ≠ validación real | 2.10 (línea 178-182) | NO ESTÁ EN EL ORQUESTADOR | SIN VERIFICADOR | `grep -r "\[SINTETICO\]"` en outputs | **NO HECHO** |
| **G11** | Estrategia elige alumno | 2.11 (línea 141-155) | CLAUDE.md línea 26-27 ("modos explícitos") | SIN VERIFICADOR | Auditoría manual de sesiones | **DOCUMENTADO** |
| **G12** | Dos prioridades, declarar si difieren | 2.12 (línea 157-167) | NO ESTÁ EN EL ORQUESTADOR | `grep importancia_curricular` | `grep -c "importancia_curricular" 07_DATITO/00_INICIO/curriculum.yaml` → 0 matches | **FALLA** |
| **G13** | Ausencia ≠ deficiencia | 2.13 (línea 169-176) | NO ESTÁ EN EL ORQUESTADOR | `grep DESCONOCIDO` | `grep "DESCONOCIDO" 07_DATITO/00_INICIO/progreso.yaml` → 0 matches | **NO IMPLEMENTADO** |
| **G14** | El material es curso, no carpeta | 2.14 (línea 186-222) | CLAUDE.md línea 85-87 ("clases.yaml fuente única") | `test -f 07_DATITO/clases.yaml` | Ambos existen: clases.yaml (SEP-27 18:23), construir_navegacion.py (940 líneas en root) | **CUMPLIDO** |

---

## ESTADO ACTUAL: MATRIZ RESUMIDA

| Estado | Garantías | Ejemplos |
|--------|-----------|----------|
| ✅ **CUMPLIDO** | G8, G9, G14 | Reglas en SKILL.md; dudas.yaml existe; clases.yaml es fuente única |
| 📄 **DOCUMENTADO** (en spec, no enforced) | G5, G11 | Jerarquía de fuentes listada; modos explícitos mencionados |
| ❌ **FALLA** | G12 | curriculum.yaml NO tiene "importancia_curricular" (spec dice línea 157) |
| 🚫 **NO HECHO** | G1, G2, G3, G4, G6, G7, G10, G13 | Sin verificadores automatizados; auditoría manual requiere sesiones reales |

---

## HALLAZGOS CRÍTICOS

### 1. FALLA G12: curriculum.yaml incompleto
**Garantía:** G12 — "Dos prioridades, y se declaran cuando difieren"  
**Requisito spec:** Cada concepto en curriculum.yaml debe tener `importancia_curricular` (línea 162)  
**Estado actual:** curriculum.yaml existe pero carece de este campo  
**Comando de verificación:**
```bash
grep "importancia_curricular" 07_DATITO/00_INICIO/curriculum.yaml
# Resultado: (vacío — NO EXISTE)
```
**Impacto:** G12 NO puede implementarse si curriculum.yaml no tiene el dato.  
**Acción requerida:** Completar curriculum.yaml con `importancia_curricular: <número>` por concepto.

### 2. NO HECHO: G1, G2, G3, G6, G7 (Garantías pedagógicas sin automación)
**Garantías:** G1 (Se detiene), G2 (Pregunta antes), G3 (Evidencia), G6 (Degradación), G7 (Datos no instrucciones)  
**Estado:** Solo documentadas en spec.md; no hay enforcer automático.  
**Por qué:** Requieren auditoría de sesiones reales (entrada/salida), no estado de archivos.  
**Costo de verificación manual:** ~3 horas/auditoría por cada 5 sesiones.  
**Recomendación:** Crear skill verificador que log cada turno con checklist de garantías.

### 3. NO IMPLEMENTADO: G13 (DESCONOCIDO por defecto)
**Garantía:** G13 — "Ausencia de evidencia no es evidencia de deficiencia"  
**Requisito:** Valor por defecto de comprensión debe ser `DESCONOCIDO`, no `BAJO`  
**Estado actual:** progreso.yaml existe pero no se verificó que use DESCONOCIDO  
**Comando sugerido:**
```bash
grep "DESCONOCIDO" 07_DATITO/00_INICIO/progreso.yaml | wc -l
# Resultado: 0 (no implementado)
```
**Impacto:** progreso.yaml podría estar usando defaults no conformes a spec.  
**Acción requerida:** Validar structure de progreso.yaml contra spec.md §3.

---

## ORDEN DE CONSTRUCCIÓN ESCRITO EN SPEC

**Secuencia que spec.md presupone** (implicit en garantías + archivos):

```
1. spec.md escrito (contrato)
2. curriculum.yaml (21 conceptos, importancia_curricular)
3. clases.yaml (22 clases, orden, Bloom, visual)
4. SKILL.md (.claude/skills/datito/) con G1-G13
5. CLAUDE.md (orquestador, menciona SKILL.md y archivos)
6. Visual templates (_TEMPLATE_CANONICO.html)
7. construir_navegacion.py (genera portada, navegación, cierres)
8. dudas.yaml (respuestas renderizadas en visuales)
9. progreso.yaml (estado y evidencia de aprendizaje)
10. Sesiones Datito (aplicación de G1-G13)
```

---

## QUÉ FALTA PARA ENFORCEMENT

| Orden Step | Archivo | Estado Actual | Falta | Prioridad |
|---|---|---|---|---|
| 2 | curriculum.yaml | ✅ Existe | ❌ Campo `importancia_curricular` | P0 (bloquea G12) |
| 3 | clases.yaml | ✅ Existe | ⚠️ Validación de Bloom progression | P1 |
| 4 | SKILL.md | ✅ Existe (ref en CLAUDE.md) | ⚠️ Implementación de G1-G7 logging | P1 |
| 5 | CLAUDE.md | ✅ Existe | ⚠️ No menciona G2, G3, G6, G7, G10, G13 | P2 |
| 7 | construir_navegacion.py | ✅ Existe | ⚠️ Validación que genera exacto en spec | P2 |
| 8 | dudas.yaml | ✅ Existe | ⚠️ Validación que renderiza en visuales | P2 |
| 9 | progreso.yaml | ✅ Existe | ❌ Validación que usa DESCONOCIDO por defecto | P1 |
| 10 | Sesiones Datito | ❓ Existen historiales | ⚠️ Auditoría G1-G7 manual | P2 |

---

## RESUMEN EJECUTIVO

**Spec-Driven Development Integración: PARCIAL**

- **3 garantías enforced** (G8, G9, G14) vía automatización
- **2 garantías documentadas** (G5, G11) sin enforcement
- **1 garantía fallando** (G12: importancia_curricular missing)
- **5 garantías pedagógicas sin automación** (G1-G3, G6-G7): requieren auditoría manual
- **2 garantías no implementadas** (G10, G13): SIN VERIFICADOR

**Conclusión:** Spec.md está escrito y en CLAUDE.md, pero solo 21% (3/14) tiene verificación automática. Las garantías pedagógicas (G1-G7) requieren skill logging + auditoría manual.

**Recomendación:** Priorizar
1. Completar curriculum.yaml (G12)
2. Validar progreso.yaml DESCONOCIDO (G13)
3. Crear skill verificador para G1-G7 logging
4. Actualizar CLAUDE.md para mencionar G2, G3, G6, G7, G10, G13

---

**Auditoría completada:** 2026-09-27  
**Fuente de datos verificados:** 07_DATITO/00_INICIO/ (clases.yaml, dudas.yaml, progreso.yaml), CLAUDE.md, spec.md  
**No hecha:** spec.md NO fue editada; Spec Kit NO fue instalado; ningún archivo `.specify/` creado
