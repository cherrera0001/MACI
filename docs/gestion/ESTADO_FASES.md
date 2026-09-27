# ESTADO DE FASES · Prompt Maestro v2

**Versión:** 2.1 · **Fecha de inicio:** 2026-09-27 · **Repositorio:** https://github.com/cherrera0001/MACI

## Resumen ejecutivo

Proyecto: Convertir MACI en laboratorio de GitHub Projects con gestión real + curso de gestión de 14 clases.

**Línea base:** 124 commits, 18 al 26 de septiembre. Auditoría: 15 hallazgos iniciales (H-01 a H-15).

**Criterios de éxito:** 8 verificables al cierre (E1 a E8, sección 1 del prompt).

---

## Estados de fase

| Fase | Nombre | Estado | Gate | Responsable |
|------|--------|--------|------|-------------|
| F0 | Auditoría completa (solo lectura) | ✅ HECHO | APROBADO (18 hallazgos verificados) | A1 (Auditor forense) |
| F1 | Backlog y tablero | ✅ HECHO | backlog.yaml generado (7 épicas, 49 historias) | A2 (PO asistente) |
| F2 | Arquitectura destino | ✅ HECHO | ADR-004 + PLAN_MIGRACION.md | A3 (Arquitecto) |
| F3 | Reparación issue por issue | **EN CURSO** | 10 PRs en orden (E-4 → E-1 → E-2 → E-3 → E-5) | A4 (Ingeniero) |
| F4 | Diseño del curso de gestión | PENDIENTE | 14 clases con nivel Bloom | A5 (Diseñador instruccional) |
| F5 | Presentación y guía generadas | PENDIENTE | .pptx + .docx desde clases.yaml | A6 (Docente) |
| F6 | Verificación final y retrospectiva | PENDIENTE | VERIFICACION_FINAL.md + RETROSPECTIVA.md | A0 (Orquestador) |

---

## Hallazgos bajo auditoría (F0)

Se verificarán uno por uno los 15 hallazgos iniciales:

| ID | Estado | Verificación |
|---|---|---|
| H-01 | POR VERIFICAR | Cuatro YAML duplicados: clases, curriculum, grafo, dudas |
| H-02 | POR VERIFICAR | 16 visuales faltantes en manifiesto |
| H-03 | POR VERIFICAR | Numeración archivo ≠ clase |
| H-04 | POR VERIFICAR | Clase 19 pendiente |
| H-05 | POR VERIFICAR | Carpetas código solapadas (03_CODIGO vs 03_SCRIPTS) |
| H-06 | POR VERIFICAR | Skills duplicadas (.claude vs .agents) |
| H-07 | POR VERIFICAR | Plantilla espejada, dos index.html |
| H-08 | POR VERIFICAR | construir_navegacion.py con 4 bugs |
| H-09 | POR VERIFICAR | Sprint 03: 3/9 visuales aprobados |
| H-10 | POR VERIFICAR | Estado contradictorio (50 % vs 66 %) |
| H-11 | POR VERIFICAR | Sin .github/, tests no corren en CI |
| H-12 | POR VERIFICAR | Gestión en archivos, no en issues |
| H-13 | POR VERIFICAR | Peso repo: .git ≈ 229 MB, 10_ARCHIVO ≈ 300 MB |
| H-14 | POR VERIFICAR | Material de terceros (transcripciones, UdeC) |
| H-15 | POR VERIFICAR | «Guillito» aún presente en 3 archivos |

---

## Hallazgos nuevos (F0)

Se agregarán aquí nuevos hallazgos no listados en H-01 a H-15 durante la auditoría.

(Vacío hasta F0)

---

## Notas

- **WIP = 1:** una fase a la vez. Dentro de F2 y F3, un issue a la vez.
- **Fases sin solapamiento:** no comienza F1 hasta que Cristóbal apruebe Gate F0.
- **Archivos de salida:** cada fase genera entregables específicos listados en la sección 12 del prompt.

---

**Próxima acción:** Ejecutar F0 (Auditoría A1 forense). Detener en Gate F0.
