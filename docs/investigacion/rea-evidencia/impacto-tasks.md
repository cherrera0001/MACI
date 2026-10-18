# Impacto en tasks.md — validación REA 2026-10-17

**Evidencia base**: `docs/investigacion/rea-evidencia/sintesis-arquitectura.md` (P1–P7,
A1–A3). Alcance: refinamientos; ninguna tarea existente se elimina ni se reordena
de forma crítica. Las 4 tareas nuevas se añaden al final de tasks.md (IDs T065–T068)
con la fase donde deben ejecutarse.

## Tareas nuevas

| ID | Fase de ejecución | Patrón | Tarea |
|---|---|---|---|
| T065 | Phase 4 (US2), junto a T035 | P1/P2 (Khan H2/H3) | Acción "mostrar un paso" en el feedback de error: `estado_interaccion: "paso_mostrado"`, pistas graduadas por procedimiento (no solución), registro de cada revelación. Tests: 0 soluciones completas antes del intento; paso N solo tras N-1 pasos. |
| T066 | Phase 5 (US3), junto a T045 | P6 (Khan H5) | Micro-progreso visible en evaluación: "N distinciones de esta sesión" con puntos por ítem, en `evaluar.html`. |
| T067 | Phase 2 (foundational), junto a T007–T009 | P4 (Duolingo H2, Century) | Contadores de adopción en `progreso.yaml` (`metricas`: sesiones, mensajes, evaluaciones_completadas, tiempo_minutos, racha_dias) + actualización en cada operación. |
| T068 | Phase 7/8 (US5 UI + polish) | P5 (Mathigon) | Gating del panel de grafo: revelar nodos por dominio con "revelar mapa completo" como escape + `tiempo_estimado_min` por unidad en `curso.yaml`. |

## Ediciones aplicadas a tasks.md

- Añadidas T065–T068 en nueva subsección "Refinamientos por validación REA" dentro de
  Phase 8, con etiqueta [US2]/[US3]/[Foundational]/[US5] según su fase real de
  ejecución (ver tabla).
- Nota en Phase 4 (T035) y Phase 5 (T045): ver T065/T066 respectivamente.

## Qué NO cambia

- Secuencia de fases 1→7 y criterio de parada MVP.
- Tests-first en todas las historias.
- Contratos: solo aditivos (`estado_interaccion` gana `paso_mostrado`; respuesta de
  evaluación gana micro-progreso). Ver contracts/api.md (editado).
