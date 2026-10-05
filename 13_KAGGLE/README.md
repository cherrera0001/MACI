# 13_KAGGLE — Desafíos de Kaggle

Casos de estudio de competencias de Kaggle, documentados paso a paso. Todo lo de Kaggle vive en esta carpeta.

El código, los datos y los resultados crudos de cada experimento no están aquí: viven en el repositorio del
experimento. Aquí queda la lectura del caso: qué se preguntó, qué se midió, qué se aprendió y qué se corrigió.

## Casos

| Caso | Qué es | Página publicada |
|---|---|---|
| [`caso_kaggle_gemma4/`](caso_kaggle_gemma4/README.md) | «Google – The Gemma 4 Developer Agent Competition», con el proyecto Agents Learning Loops y la propuesta ZorzALL | <https://maci.c4a.cl/desafios/kaggle_gemma4.html> |

## Por dónde empezar en el caso Gemma 4

| Si quieres… | Abre |
|---|---|
| Entender el desafío con diagramas | [`desafio_kaggle_gemma4.html`](caso_kaggle_gemma4/desafio_kaggle_gemma4.html) |
| Leer el análisis completo y el estado vigente | [`README.md`](caso_kaggle_gemma4/README.md) |
| Seguir las pruebas una por una, con su lección | [`RECORRIDO_PASO_A_PASO.md`](caso_kaggle_gemma4/RECORRIDO_PASO_A_PASO.md) |
| Saber qué se subió a Kaggle y con qué resultado | [`REGISTRO_DE_PRUEBAS.md`](caso_kaggle_gemma4/REGISTRO_DE_PRUEBAS.md) |
| Ver cada predicción escrita antes de correr | [`BITACORA_MEJORA.md`](caso_kaggle_gemma4/BITACORA_MEJORA.md) |
| Conocer la hipótesis ZorzALL y su revisión | [`HIPOTESIS_ZORZAL.md`](caso_kaggle_gemma4/HIPOTESIS_ZORZAL.md) |

Los documentos `INSTRUCCION_CLAUDE_CODE.md` y `REVISION_*.md` están fechados: son historia del 2026-10-04 y
llevan una nota de vigencia.

## Reglas de esta carpeta

- **Solo agregados.** No se versionan enunciados, parches, pruebas, identificadores de tareas ni salidas
  crudas de una competencia: sus reglas prohíben redistribuirlos.
- **Sin credenciales.** El token de Kaggle vive en `.env`, que git ignora.
- **Cada predicción se escribe antes de correr**, y cada error propio queda anotado donde ocurrió.
