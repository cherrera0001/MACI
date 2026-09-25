# Referencia · Fuentes y citado

Cargar antes de citar algo o de consultar NotebookLM.

---

## Jerarquía

| Prioridad | Fuente | Dónde |
|---|---|---|
| 1 | **Laboratorios del curso** | `06_LABORATORIOS/` — 5 prácticos, 12 de los 21 conceptos |
| 2 | **Material FCD del repositorio** | Láminas `11_PRESENTACIÓN/_markdown/`, transcripciones `05_CLASES/`, `01_DOCUMENTACION/`, `08_PROYECTO_FCD/` |
| 3 | **Cuaderno de NotebookLM** | MCP `notebooklm`, 72 fuentes |
| 4 | **Proyectos propios** | Melbourne (`09_RESULTADOS/`), Galaxy Zoo (`08_PROYECTO_FCD/Desafio/`) |
| 5 | Fuentes académicas externas | Solo si lo anterior no alcanza |

Dentro del cuaderno: material de la asignatura (syllabus, `FCD-2026-2_*`,
resúmenes de clase, guías de autoestudio) > documentos UdeC > libros y papers
(ISLR, OpenIntro, XGBoost) > documentación técnica.

**Si el material del curso dice algo, eso manda.**

### Las transcripciones de clase — `05_CLASES/`

Son parte del material del curso (nivel 2), pero ceden ante láminas y
prácticos: son automáticas y erran en números y términos.

- **Dónde se enseñó qué**: `05_CLASES/mapa_ensenanza.yaml` (rango y hablante,
  curado). `indice_clases.yaml` solo dice dónde se *menciona* una palabra.
- **Quién habla**: solo el profesor titular es «el profesor». Hay un segundo
  docente (19-jun desde ~1:28 y 26-jun), ayudantías, presentaciones de alumnos
  (14-ago, 4-sep) y un invitado (21-ago, 0:06–1:23). **Solo las clases del
  titular entran al certamen**: «Entran solo mis clases. No entran las clases de
  Alejandra» (`03Clase_Recuperación_…_15_julio.md`, 1:18:16).
- **Cómo se citan**: ruta completa del `.md` y marca o rango, nunca el
  `_plano.txt` (no tiene marcas) ni una ruta truncada:
  `[FUENTE · Repo: 05_CLASES/transcripciones/06Clase_Fundamentos_en_Ciencia_de_Datos_31_de_julio.md · 0:43:44]`.
  Cita textual; las correcciones de la transcripción van entre ⟨ ⟩ y se marcan
  `[INFERENCIA]`; las omisiones, con […].
- **Spoilers**: las ayudantías resuelven P2, P4 y P5 en vivo. No mostrarlas
  antes de que intente el `(vacío)`.

### Documentos que parecen oficiales y no lo son del todo

- `11_PRESENTACIÓN/_markdown/Resumen_Clase6/7/8_*.md` son **híbridos**: láminas
  oficiales más lo dicho en clase según otra transcripción. La lámina manda; lo
  marcado «solo en transcripción» vale como transcripción, y sus citas no
  siempre calzan con las de `05_CLASES/`.
- `Resumen_Clase1/2/3/5_*.md` son de **otro curso** (Prototipos y creatividad).
  No citarlos.

---

## Etiquetado obligatorio

| Etiqueta | Significado |
|---|---|
| `[FUENTE · NotebookLM: <documento>]` | Del cuaderno, citando el documento que él mismo referenció |
| `[FUENTE · Repo: <ruta>]` | De su material, con ruta verificable |
| `[INFERENCIA]` | Se deriva de lo anterior, pero no está escrito |
| `[DATITO]` | **Explicación pedagógica tuya**: analogía, ejemplo inventado |

`[DATITO]` no es de segunda categoría — una buena analogía es trabajo docente
legítimo. Pero debe quedar marcada, para que no atribuya al syllabus algo que
dijiste tú.

---

## Material de terceros

`01_DOCUMENTACION/06_CERTAMEN1/` procede de un compañero y **sus respuestas no
están verificadas**. El documento se titula "Pauta Oficial" pero cierra con
campos de plantilla sin rellenar (`Person`, `Date`).

- **Enunciados y tablas de datos:** fiabilidad alta, úsalos como entrenamiento
- **Justificaciones:** **no** son criterio de corrección

Si contradice al material de la asignatura, manda el material de la asignatura.

---

## NotebookLM

Cuaderno **Fundamentals of Data Science Syllabus**,
`97ce114e-2371-44eb-85b5-527cd28180cb`. Servidor MCP `notebooklm` v3.4.2.

| Herramienta | Uso |
|---|---|
| `mcp__notebooklm__chat_ask` | Preguntar a las fuentes. La principal |
| `mcp__notebooklm__source_list` | Ver qué fuentes hay |
| `mcp__notebooklm__source_read` | Leer una fuente concreta |
| `mcp__notebooklm__note_save` | Guardar una síntesis como nota |
| `mcp__notebooklm__server_info` | Diagnóstico si algo falla |

**Nunca abras conversación nueva con `chat_ask`**: la opción que reinicia el hilo
borra el historial del cuaderno en el servidor, y es irreversible.

### Si falla

La integración usa APIs internas no documentadas con cookies que **caducan cada
pocas semanas**. Si falla: avisa en una línea, sigue con el material local y
etiqueta el resto como `[DATITO]` o `[INFERENCIA]`. No te detengas y no lo
ocultes.

Reautenticar (lo ejecuta Cristóbal, necesita navegador):

```bash
notebooklm login --browser msedge
notebooklm auth check --test --json     # debe devolver "status": "ok"
```
