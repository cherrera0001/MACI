# Harness de escenarios del tutor (REQ-TUT-001)

Valida el **comportamiento** del tutor, no su formato. Hasta ahora las pruebas
del repo verifican HTML, enlaces y esquemas de datos; ninguna responde "¿el
tutor esperó de verdad?, ¿dio la respuesta antes de tiempo?, ¿la registró?".

## Qué es un escenario

Un archivo YAML en `escenarios/` con:

```yaml
id: g1-espera-basica          # unico, prefijo por garantia
garantia: G1                  # G1 | G11 | INTENTOS | BORDE
titulo: ...
contexto: |                   # situacion que fija la sesion
  ...
entrada: "lo que dice el alumno"
transcript: transcripts/g1-espera-basica.yaml   # dialogo de referencia (cumple)
reglas: [espera_real, no_simula_alumno]         # subconjunto de REGLAS
```

## Qué es un transcript

Un archivo YAML con la secuencia de turnos:

```yaml
turnos:
  - rol: tutor               # tutor | alumno
    texto: "..."
    acciones: [duda:2026-10-27-x]   # opcional; "duda:*" cuenta como registrar_duda
  - rol: alumno
    texto: "..."
    resultado: fallo          # opcional; marca intento fallido para R3
    pide_respuesta: true      # opcional; la peticion explicita de G11
```

## Reglas (cada una apunta a una garantia)

| Regla | Garantia | Qué exige |
|---|---|---|
| `espera_real` | G1 / REGLA CERO | Tras un turno del tutor que termina en pregunta, el siguiente turno es del alumno o es el fin del transcript. El tutor jamas responde su propia pregunta |
| `no_simula_alumno` | G1 | Ningun turno del tutor simula la respuesta del alumno ("probablemente dirias...", "supongamos que responde...") |
| `solucion_tras_dos_intentos` | spec §G1 | La solucion (`senal_solucion` del escenario) solo aparece tras >=2 intentos fallidos consecutivos o tras `pide_respuesta: true` |
| `respuesta_pedida_registrada` | G11 + REGLA UNO-B | Si el alumno pide la respuesta, el turno del tutor que la entrega lleva la accion `duda:*` (registro antes de decirla) |
| `transferencia_tras_respuesta` | G11 | Despues de entregar una respuesta registrada, hay un turno posterior del tutor que pregunta (exige transferirla) |

## Como correrlo

```bash
python 04_CODIGO/harness_escenarios/harness.py              # todos los escenarios
python 04_CODIGO/harness_escenarios/harness.py --solo G1    # filtro por garantia
python 04_CODIGO/harness_escenarios/harness.py --json       # reporte maquina
```

Salida: por escenario, PASS/FAIL y las reglas violadas con turno. Exit code 1 si
alguno falla. El baseline vigente se archiva en `baseline/`:

```bash
python 04_CODIGO/harness_escenarios/harness.py > baseline/baseline-AAAA-MM-DD.txt
```

## Alcance honesto (y su frontera)

El harness valida **transcripts**: dialogos reales (bitacoras) o simulados. No
ejecuta la skill de Claude Code aun: una skill no puede invocarse headless
desde unittest. El modo "generar" (un LLM local responde el `contexto` +
`entrada` y el harness valida) es trabajo del motor portable
(`15_TERMINITO/src/datito/socratico/`, T031 del spec 002); cuando exista, este
mismo archivo de escenarios sera su suite de aceptacion. Eso es deliberado:
las reglas y los escenarios son el contrato; el generador es intercambiable.
