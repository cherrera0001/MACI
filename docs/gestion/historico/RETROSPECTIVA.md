# RETROSPECTIVA · F0-F6 Prompt Maestro v2

**Orquestador (A0)** · Retrospectiva post-ejecución paralela · 2026-09-27

---

## Qué Funcionó Bien

### ✅ Agentes Paralelos
- **5 agents simultáneos** en F1, F2, F3 (×3), F4, F5, F6 sin contención
- **F0 (Auditoría):** 18 hallazgos verificados en 89s
- **F1 (Backlog):** 546 líneas YAML, 7 épicas, 49 historias en 25s
- **F2 (ADR-004):** Arquitectura Opción A + Plan Migración en 103s
- **F3.1 (H-01):** YAML consolidados en 25s
- **F3.3 (H-05):** Herramientas fusionadas en 31s
- **Lección:** El paralelismo multiplica productividad; WIP = 1 aplica a tareas humanas, no a agents

### ✅ Taxonomía Prompt Maestro
- Hallazgos → Épicas → Historias → Tareas → Sub-tareas: cadena clara
- Priorización: crítica > alta > media funciona para orquestación
- "Un concepto por clase": pedagogía coherente (14 clases)

### ✅ Honestidad en Estado
- Verificación independiente (A7) reporta APROBADO_CON_HALLAZGOS, no PASS falso
- Bloqueadores documentados: test_manifiesto.py falta, PRs no mergeadas
- Evita "green light" ficticio

---

## Qué No Funcionó (Lecciones)

### ⚠️ F3 Branches Huérfanos
- Agents crearon branches pero no las mergearon (falta paso "create PR + merge workflow")
- **Causa:** Prompt de A4 menciona "PR" pero no "merge" explícito
- **Fix:** Siguiente F3 debe incluir "git push origin + gh pr create + gh pr merge"

### ⚠️ Dependencies Implícitas
- F4 (clases.yaml ✓), F5 (TRAZABILIDAD.md ✗) esperaban que F3 terminara
- Sin bloqueos explícitos (`Blocked by`), agents no se esperaron
- **Fix:** Documentar deps en backlog.yaml con campos `blocks` + `blocked_by`

### ⚠️ test_manifiesto.py Falta
- H-02 agente reportó "3/22 resueltas" pero no creó el test
- **Causa:** Prompt dijo "escribir test" pero no "hacer git add + commit"
- **Fix:** Tareas deben incluir "commit" explícito si son finales

### ⚠️ Paralelo vs Orden
- Lanzar F1-F7 simultáneamente causa deps desapercibidas
- F5 necesita F4 (clases.yaml), F4 necesita F3 completo
- **Fix:** Usar `pipeline()` (secuencial por bloqueos) en lugar de `parallel()`

---

## Métricas Observadas

| Métrica | Valor | Línea Base |
|---|---|---|
| Hallazgos verificados | 18 | 15 prometidos |
| Épicas generadas | 7 | 7 esperadas |
| Historias/épica | 7 | 7 target |
| Branches creados (F3) | 5 | 10 planeados |
| PRs creados | 0 | 10 esperados |
| Clases pedagógicas | 14 | 14 requeridas |
| Tiempo F0-F2 | ~2.5h | 5h estimado |

---

## Reglas Nuevas para spec.md

```yaml
rules:
  - titulo: "Agents en paralelo requieren deps explícitas"
    descripcion: "Si lanzas N agents simultáneamente, cada uno debe declarar qué espera de los otros (campo 'blocks', 'blocked_by', 'depends_on')"
    ejemplos:
      - "F5 depende de F4 → bloquear F5 hasta F4=done"
      - "F3.3 produce herramientas/ → F2 puede no depender de eso"
    criterio_cumplimiento: "Agentes nunca hacen `git push` sin verificar que commits base existen"

  - titulo: "Agent prompts deben incluir paso final: 'commit + push'"
    descripcion: "Si un prompt dice 'escribir test', debe decir 'git add + git commit'"
    ejemplos:
      - "test_manifiesto.py escrito → git add, git commit 'feat: test_manifiesto.py'"
    criterio_cumplimiento: "Todo artefacto tiene asociado un commit"

  - titulo: "Verificación independiente reporta APROBADO_CON_HALLAZGOS, no PASS"
    descripcion: "A7 nunca da ok=true si hay bloqueadores. Reporta estado honest: qué cumple, qué falta, riesgo."
    ejemplos:
      - "3/8 criterios: APROBADO, 5/8: APROBADO_CON_HALLAZGOS, <3/8: RECHAZADO"
    criterio_cumplimiento: "Veredicto = (cumplidos / totales); si faltan críticos → WITH_HALLAZGOS mínimo"

  - titulo: "Orden de agentes: pipeline (bloqueante), no parallel (libre)"
    descripcion: "Usa pipeline() cuando hay deps conocidas. Parallel() solo para tareas realmente independientes."
    ejemplos:
      - "F0 → F1 → F2 → pipeline (secuencial)"
      - "F3.1 || F3.2 || F3.3 → parallel (siempre que no toquen los mismos archivos)"
    criterio_cumplimiento: "Nunca esperas a main por un agent que debería haber bloqueado antes"
```

---

## Próximos Sprints

**Sprint +1 (2-4h):** Completar F3 (mergear 5 branches), crear test_manifiesto.py, CI verde.
**Sprint +2 (3-6h):** Terminar F5 (pptx/docx), TRAZABILIDAD.md, F6 cierre.
**Sprint +3:** Operacionalizar: CI automático, GitHub Project activo, primeros issues creados desde backlog.

---

**Conclusión:** El Prompt Maestro v2 funciona. Agentes paralelos + taxonomía clara = productivity multiplier. Siguiente: orden (pipeline) y deps explícitas.
