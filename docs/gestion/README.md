# Gestión de MACI

El trabajo se sigue en GitHub, no en archivos de esta carpeta.

| Qué | Dónde |
|---|---|
| Backlog y estado de cada ítem | [Project MACI](https://github.com/users/cherrera0001/projects/3) y los [issues](https://github.com/cherrera0001/MACI/issues) |
| Versión en curso | [Milestone v1.0](https://github.com/cherrera0001/MACI/milestone/3) |
| Cómo se trabaja y cómo leer el tablero | [Wiki](https://github.com/cherrera0001/MACI/wiki), cuya fuente es [`docs/wiki/`](../wiki/Home.md) |
| Decisiones de arquitectura | [`docs/adr/`](../adr/) |
| Despliegue | [`docs/DEPLOYMENT.md`](../DEPLOYMENT.md) |

## Qué hay aquí

- **`backlog.yaml`**: la semilla con la que se crearon los issues #30 a #77 el 2026-10-01 (6 épicas, 16 historias y decisiones, 26 tareas). Se edita solo para sembrar ítems nuevos con `python 03_SCRIPTS/crear_backlog.py`. Después de sembrar, manda el issue.
- **`historico/`**: 21 documentos de los sprints 01 a 06 y de la corrida del Prompt Maestro v2 (septiembre de 2026). Se conservan como registro. Describen un estado del repo que ya cambió: no se actualizan ni se usan para decidir. `historico/backlog_prompt_maestro_v2.yaml` es el backlog de 7 épicas que nunca se importó.

## Jerarquía

Épica `[E-n]` → historia `[H-n.m]` o decisión `[D-n.m]` → tarea `[T-n.m.p]`, enlazadas como sub-issues. Cada ítem lleva Tipo, Prioridad (P0, P1, P2) y Proceso (P1 a P6). El detalle está en la wiki, páginas «Cómo opera el tablero» y «Procesos».
