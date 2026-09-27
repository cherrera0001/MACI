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
| F0 | Auditoría completa (solo lectura) | **PENDIENTE** | Cristóbal aprueba lista de hallazgos | A1 (Auditor forense) |
| F1 | Backlog y tablero | PENDIENTE | Cristóbal revisa vistas y fija prioridades | A2 (PO asistente) |
| F2 | Arquitectura destino | PENDIENTE | Cristóbal aprueba ADR-004 y plan migración | A3 (Arquitecto) |
| F3 | Reparación issue por issue | PENDIENTE | CI verde, 0 rutas rotas, web revisada | A4 (Ingeniero) |
| F4 | Diseño del curso de gestión | PENDIENTE | Cristóbal aprueba secuencia y fichas | A5 (Diseñador instruccional) |
| F5 | Presentación y guía generadas | PENDIENTE | A7 verifica coherencia, A8 aprueba castellano | A6 (Docente) |
| F6 | Verificación final y retrospectiva | PENDIENTE | A7 emite veredicto | A0 (Orquestador) |

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
