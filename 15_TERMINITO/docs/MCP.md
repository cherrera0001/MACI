# Servidor MCP de Datito (`datito-mcp`)

Expone el motor pedagógico como herramientas MCP (Model Context Protocol) sobre
stdio, para conectar Datito a un orquestador de agentes (p. ej. open-duet) o a
cualquier cliente MCP. Transporte: JSON-RPC 2.0 newline-delimited por
stdin/stdout. Sin dependencias nuevas.

```bash
.venv/bin/datito-mcp --curso fcd        # queda esperando mensajes JSON-RPC
```

Herramientas (todas delegan en `src/datito/`; las de escritura usan los mismos
esquemas que el CLI):

| Herramienta | Entrada | Qué devuelve | Escribe |
|---|---|---|---|
| `progreso` | — | Métricas de adopción y resumen de sesión | no |
| `grafo_dominio` | — | Nodos del grafo con su estado de dominio | no |
| `siguiente_concepto` | — | Siguiente concepto recomendado (prerrequisitos dominados, prioriza lo en estudio) | no |
| `distinciones_pendientes` | — | Items de evaluación sin resultado guardado | no |
| `calificar_distincion` | `item_id`, `respuesta` | Resultado de la rúbrica; guarda resultado, micro-progreso y dominio | sí |
| `buscar_materiales` | `consulta`, `k=4` | Fragmentos del índice TF-IDF con fuente y referencia | no |
| `registrar_dominio` | `conceptos`, `resultado` | Actualiza estados (`logrado`→dominado, resto→en_estudio) | sí |

## Ejemplo de sesión (líneas JSON)

```json
{"jsonrpc":"2.0","id":1,"method":"initialize"}
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"siguiente_concepto","arguments":{}}}
```

## Arquitectura (runtime agentico)

Este servidor es el puente de la Capa 2: el orquestador (open-duet u otro)
instancia agentes cuyo prompt sale de los 8 componentes de identidad de Datito,
y les da memoria, rutinas y aprobaciones. Las herramientas de aquí son lo que
convierte a esos agentes en *este* tutor sobre *estos* materiales: citan las
fuentes reales (`buscar_materiales`), evalúan con las distinciones del certamen
(`calificar_distincion`) y dejan evidencia auditable (`registrar_dominio`).
