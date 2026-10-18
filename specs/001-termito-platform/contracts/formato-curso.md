# Contrato Formato de Curso (paquete portable)

**Versión**: 1.0.0-draft · **Fecha**: 2026-10-17

Define el layout autocontenido de un curso/Termito: es a la vez el formato en disco,
el paquete exportable (US7) y la unidad de independencia entre Termitos (principio IX).

## Reglas del paquete

1. Un curso es un directorio `cursos/<slug>/` con exactamente el layout definido en
   `data-model.md` (sección "Layout de una instancia de curso").
2. El paquete es autocontenido: no contiene rutas absolutas de la máquina, ni
   referencias a archivos fuera del directorio, ni secretos. La validación de
   exportación/importación lo comprueba (y falla con reporte de las rutas violadoras).
3. `.indice/` puede faltar en el paquete; al importar se regenera con
   `termito reindexar` (artefacto derivado, research.md R3).
4. `curso.yaml` es obligatorio y minimalista: `slug`, `nombre`, `periodo`, `idioma`,
   `estado`, `creado`. Sin él el paquete se rechaza.
5. Los identificadores son estables: `slug` del curso, `fuente-id` por fuente,
   `fid` por fragmento. Renombrar una fuente rompe evidencias históricas y exige
   migración explícita de ids (la importación rechaza fids huérfanos citados en
   `dudas.yaml` con error claro).
6. Todo archivo de estado es YAML o Markdown legible (restricción constitucional);
   los únicos binarios permitidos son `vectores.npy` y adjuntos de fuentes originales
   (pdf, pptx, video), que son entradas, no estado.
7. Cerrar un curso no altera el layout: solo cambia `estado` en `curso.yaml`. El
   registro del estudiante permanece íntegro en el mismo paquete (FR-016).

## Versionado del formato

- **1.0.0** (este contrato): layout inicial con los 8 componentes del Termito y
  estado de dominio por nodo.
- Cambios mayores del layout requieren `formato_version` en `curso.yaml` y rutas de
  migración documentadas aquí.
