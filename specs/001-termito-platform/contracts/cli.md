# Contrato CLI — Plataforma Termito

**Versión**: 1.0.0-draft · **Fecha**: 2026-10-17 · **Ejecutable**: `python -m termito.cli` (o el
entry point que defina tasks.md)

Todos los comandos operan sobre el directorio de cursos configurado (por defecto
`15_TERMINITO/cursos/`) y funcionan sin conexión. Salida: texto legible en español;
códigos de salida: 0 éxito, 1 error de uso, 2 error de entorno (ej. Ollama ausente).

## Gestión de cursos y Termitos

```text
termito nuevo <slug> [--nombre "..."] [--periodo "..."] [--idioma es]
    Crea cursos/<slug>/ vacío con curso.yaml en estado configurando.
    Error si <slug> ya existe (kebab-case, min 3 caracteres).

termito ingestar <slug> <ruta...>
    Extrae contenido de las rutas (pdf/pptx/txt/md/srt/vtt/html) hacia fuentes/ y
    fragmentos/, e imprime el resumen de ingesta: fuentes procesadas, fragmentos por
    fuente, advertencias de lo no extraíble. No sobreescribe fuentes existentes sin
    --reemplazar.

termito construir <slug>
    Lanza el asistente interactivo de los 8 componentes (o valida
    prompt/componentes.yaml si ya está completo) y genera prompt/actual.md +
    versions/manifest.yaml. Estado resultante: listo.

termito prompt ver|editar|revertir <slug> [--a <version>]
    ver: muestra el prompt vigente con sus 8 componentes.
    editar: abre edición (componentes o prompt directo con --directo).
    revertir: restaura la versión indicada del manifest como vigente.

termito reindexar <slug>
    Regenera .indice/ desde los fragmentos (tras cambios de fuentes o de modelo).
```

## Uso del tutor y evaluación

```text
termito servir [--puerto 8377] [--solo-local]
    Levanta la API local y la UI web (localhost por defecto; --solo-local prohibe
    escuchar en otras interfaces).

termito evaluar <slug> [--tema <concepto-id>]
    Genera una evaluación por distinciones sobre el tema (o el próximo recomendado
    por el grafo), la guarda en evaluaciones/ y actualiza grafo.yaml.

termito nota <slug> --evaluacion "..." --nota "..." [--observaciones "..."]
    Registra retroalimentación real y muestra los ajustes que derivará en el Termito
    (requiere confirmación).

termito cerrar <slug>
    Cierra el ciclo del curso (estado cerrado). Exige confirmación explícita; deja
    el registro íntegro.

termito exportar <slug> [--destino <ruta>]
    Emite el paquete portable (directorio autocontenido) y valida que no contenga
    rutas absolutas ni secretos.

termito importar <ruta> [--slug <nuevo-slug>]
    Valida el paquete y lo instala como curso; regenera .indice/ si falta.

termito familia
    Lista los Termitos con estado y progreso resumido (panel US6).
```

## Invariantes comprobables por CLI (usados en quickstart.md)

- `termito verificar <slug>` (implícito en CI/tests): curso.yaml válido, 8
  componentes presentes si estado ≥ listo, todo fid citado en dudas.yaml existe en
  fragmentos/, grafo.yaml sin ciclos, progreso.yaml consistente con evaluaciones/.
