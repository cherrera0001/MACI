# Cómo construir tu propio tutor (con Datito como ejemplo)

Datito no es un producto cerrado: es el **ejemplo trabajado** de cómo construir un
tutor socrático con materiales reales de un curso. Este documento es el mapa del
ejemplo: las piezas, el orden en que se construyeron y cómo replicarlas para otro
curso. Todo lo que se cita existe y está verificado en este repositorio.

## Las 7 piezas (de adentro hacia afuera)

| # | Pieza | Qué es | Dónde vive |
|---|---|---|---|
| 1 | **Currículo como fuente única** | Los conceptos, prerrequisitos y el material que los cubre, en YAML legible. Sin esto no hay nada que enseñar. | `07_DATITO/curriculum.yaml` (21 conceptos) |
| 2 | **Clases generadas** | El curso se estudia como secuencia, no como carpeta: un generador produce HTML con barra, ficha Bloom, cierre y preguntas con respuesta oculta. | `07_DATITO/clases.yaml` → `03_SCRIPTS/construir_navegacion.py` → `visual/` |
| 3 | **Política socrática** | El comportamiento del tutor como código: espera de verdad, obedece cuando el estudiante pide la respuesta, dos intentos antes de la solución, registro antes de decir, transferencia exigida. | `15_TERMINITO/src/datito/socratico.py` |
| 4 | **Cadena de evidencia** | Qué cuenta como aprendizaje: explicar → aplicar → interpretar → transferir, cada una con fecha y detalle. "Me quedó claro" no es evidencia. | `07_DATITO/progreso.yaml` + `15_TERMINITO/src/datito/socratico.py` (`Concepto`) |
| 5 | **Harness de comportamiento** | Escenarios de diálogo con resultado esperado; el tutor se prueba como se prueba cualquier código. | `04_CODIGO/harness_escenarios/` (15 escenarios, 5 reglas) |
| 6 | **Verificación continua** | Un solo comando que lo valida todo; cada error histórico es una comprobación. | `03_SCRIPTS/verificar_todo.py` (5 pasos, 78 tests) |
| 7 | **Runtime local** | El tutor corre en tu máquina, con LLM local opcional; los datos del estudiante son archivos que él controla. | `15_TERMINITO/` (motor) + skill de Claude Code |

## El orden importa

1. **Primero el contrato, después el código.** Las garantías (G1–G14 en
   `00_INICIO/spec.md`) se escribieron antes de automatizarlas; la mitad lleva
   verificador propio. Una regla sin verificador se reincide (lo documentan las
   propias garantías G8 y G9).
2. **La evidencia antes que la métrica.** El estado de un concepto se calcula de
   evidencias fechadas, no de sensaciones. El registro puede bajar
   (REQUIERE_REPASO): si solo sube, dejó de medir.
3. **El comportamiento se prueba como función.** El harness trata el diálogo como
   cualquier otra interfaz: entrada del alumno → acción esperada del tutor. Los
   15 escenarios incluyen los casos que castigan (pedir la respuesta, abandonar,
   estado corrupto).
4. **Demo antes que sesión.** El demo sintético (`datito demo`) recorre el ciclo
   completo en un curso de juguete para que cualquiera vea el tutor tutoréar
   antes de usarlo con un estudiante real.

## Para replicarlo con otro curso

1. Escribe el currículo: conceptos, prerrequisitos, material real del curso.
2. Genera las clases en secuencia (con cierre y preguntas ocultas).
3. Porta la política: las cinco reglas son independientes del dominio; cambian
   soluciones y pistas, no la máquina de decisiones.
4. Define evidencias de dominio (qué tiene que producir el estudiante, sin ayuda).
5. Escribe 10–15 escenarios de diálogo con resultados esperados.
6. Conecta el runtime: CLI + web + LLM local opcional (`15_TERMINITO` ya es un
   motor reutilizable: `datito init <slug> --materiales <rutas>`).
7. Pon un solo comando que lo verifique todo y no declares nada terminado hasta
   que imprima LISTO.

## Lo que NO copiar

- Dependencias de servicios externos para las fuentes (NotebookLM se descartó:
  ADR-005). Local-first, con criterio documentado si vuelves a evaluar uno.
- Gamificación pesada y trackers de terceros: la evidencia del curso (PISA y la
  REA propia en `docs/investigacion/`) castiga la distracción, no la recompensa.
- Métricas de uso como sustituto del aprendizaje: se mide lo que el estudiante
  puede sin el tutor, no cuánto habla con él (`07_DATITO/06_AUDITORIAS/evaluacion_a_ciegas/`).

---

*Última revisión: 2026-10-28. Se mantiene al día con las verificaciones; las
cifras (21 conceptos, 23 clases, 15 escenarios, 78 tests) las vigilan los tests
(`test_cifras_readme.py`, `test_glosario.py`, `test_harness.py`).*
