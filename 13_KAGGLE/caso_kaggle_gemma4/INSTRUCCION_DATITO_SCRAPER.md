# Prompt para Datito · scraper del concurso Gemma 4

Se pega completo en la sesión del experimento. Fecha: 2026-10-06.

```text
ROL
Eres Datito. Esta tarea es un scraper. No mejoras el agente.

PROHIBIDO HASTA CERRAR
- Corrida con GPU.
- Envío a Kaggle.
- Cambiar llamadas, razonamiento, subagentes o el zip.
- Copiar al repositorio enunciados, parches, pruebas o identificadores de tareas.

DATO YA LEÍDO (no lo repitas con GPU)
Notebook: hitarthjain0/gemma-4-agent-run-the-real-evaluator-locally
Log: 2082,5 s, GPU L4×4, Python en /usr/local/lib/python3.12.

1. A los 67 s: «Wheelhouse installation complete», 41 ruedas. En Python 3.12
   las ruedas cp312 instalan. El error cp312 es de una imagen con Python 3.13.
2. Chris Carrigan Brolly, versión 2, hace 2 días: él solo puede fijar el
   notebook al 10-02. El autor sí fija un entorno que funciona.
3. Cada tarea: «ensurepip unavailable … creating venv without pip».
   El sandbox nace sin pip.
4. Cierre del log: resolved 1/10, had a patch 10/10, bucles (mismo comando
   ≥5 veces) 3, media 52,5 llamadas.
5. De 9 no resueltas, 6 tienen n_pytest = 0. La resuelta tiene n_pytest = 2,
   17 llamadas y ningún bucle. Dos no resueltas agotan 250 turnos.

TAREA
Un scraper. Tres fuentes. El crudo va a un directorio que git ignora.
En git solo entra un manifiesto: url, fecha, número de comentarios, si hay
log, si hay eval_summary.csv.

1. Comentarios
   Cada notebook público del concurso, todas las versiones, todos los
   comentarios. Campos: autor, fecha, versión del notebook, texto.
   Incluye el hilo de Amit_kumar_@1!22 (ruedas cp312, Python 3.13) y la
   respuesta de Justin Arndt (editar el notebook fijado al entorno anterior).

2. Salidas
   Por cada kernel con Output:
   kaggle kernels output <usuario>/<kernel> -p <directorio>
   Empieza por hitarthjain0/gemma-4-agent-run-the-real-evaluator-locally.
   Archivo: eval_summary.csv.
   Columnas: id, repo, resolved, patch_chars, tool_calls, dur, end, err,
   exit, max_repeat, n_cmd, n_edit, n_pytest.
   Agregados, nada de filas sueltas: resueltas por repo; filas con err no
   vacío; filas con «exceeded turns»; mediana de tool_calls en resueltas y
   en no resueltas; entre las no resueltas, cuántas tienen n_pytest = 0.

3. tasks.jsonl
   El de la página de datos del concurso. No se copia al repositorio.
   Por repositorio: filas con hints_text vacío y no vacío; filas con
   problem_statement de menos de 250 caracteres.
   hints_text son los comentarios del issue.

ENTREGA
Tres líneas:
- comentarios bajados
- eval_summary.csv bajados
- no resueltas con n_pytest = 0, sumando los csv

Si un comentario o un csv contradice la bitácora, escribes las dos cifras.
No propones un cambio de agente.
```
