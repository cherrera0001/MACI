# Data Model: MACI 1.0 — Plataforma Datito

**Fecha**: 2026-10-17 · **Fuente**: spec.md (Key Entities), research.md (R6, R7)

## Layout de una instancia de curso (fuente de verdad en archivos)

```text
cursos/<slug>/
├── curso.yaml               # identidad y estado del curso
├── prompt/
│   ├── componentes.yaml     # los 8 componentes (editable por el estudiante)
│   ├── actual.md            # prompt vigente (derivado de componentes + ediciones)
│   └── versions/            # versiones anteriores + manifest.yaml
├── fuentes/
│   ├── <fuente-id>.yaml     # metadatos por fuente
│   └── fragmentos/<fuente-id>.md   # fragmentos con referencia direccionable
├── .indice/                 # artefacto derivado regenerable (research.md R3)
│   ├── manifest.json        # qué fragmentos están indexados y con qué modelo
│   └── vectores.npy
├── grafo.yaml               # conceptos, prerrequisitos, estado de dominio
├── sesiones/<YYYY-mm-dd>.md # historial conversacional
├── dudas.yaml               # dudas resueltas con procedimiento y evidencia
├── evaluaciones/<ev-id>.yaml# ítems de distinción con resultado
├── retroalimentacion.yaml   # notas reales del estudiante
└── progreso.yaml            # dominio agregado (derivado de evaluaciones)
```

## Entidades y reglas

### Curso
- **Campos**: `slug` (único, kebab-case), `nombre`, `periodo`, `idioma` (es|en|...),
  `estado`, `creado`, `cerrado_en` (nullable).
- **Reglas**: `slug` inmutable; no hay dos cursos con el mismo `slug` (garantiza la
  independencia del principio IX). `periodo` es texto libre (ej. "2026-T2").
- **Transición de estado**: `configurando → listo → activo → cerrado`.
  `cerrado` es irreversible sin confirmación explícita (edge case del spec) y deja el
  registro íntegro (FR-016).

### Fuente
- **Campos**: `id` (slug del nombre de archivo), `tipo` (pdf|pptx|web|video|texto),
  `ruta_original`, `estado_extraccion` (completo|parcial|fallido), `advertencias`.
- **Reglas**: `id` único por curso; `estado_extraccion != completo` exige al menos una
  advertencia legible (FR: ingesta transparente, US1 escenario 4).

### Fragmento
- **Campos**: `fid` (estable: `<fuente-id>#<n>`), `texto`, `referencia` (página o
  timestamp), `tema` (inferido, revisable).
- **Reglas**: un fragmento pertenece a exactamente una fuente; la `referencia` es
  direccionable por la UI (clic → salto a página/timestamp). Tamaño objetivo: 150–400
  palabras.

### Evidencia
- **Campos**: lista de `fid` + `referencia` resuelta.
- **Reglas** (research.md R5): toda afirmación del tutor sobre el curso resuelve a
  ≥1 `fid` existente, o la respuesta usa la plantilla "sin fuente". No hay evidencia
  sin fragmento.

### Datito (componentes + prompt)
- **Campos** (`prompt/componentes.yaml`): `rol_dominio`, `mision`, `funciones`
  (lista), `estilo_ensenanza`, `contexto_curso` (resumen aprobado del estudiante),
  `estilo_aprendizaje`, `restricciones` (lista), `relacion_temporal`.
- **Reglas**: los 8 campos siempre existen (pueden estar en borrador); `actual.md` se
  regenera desde componentes salvo que el estudiante haya editado el prompt directo,
  caso en que se marca `prompt_editado_manual: true` y el wizard deja de sobrescribir
  sin aviso. Cada cambio crea entrada en `versions/manifest.yaml`
  (timestamp, componentes afectados, motivo) — reversible (FR-005, research.md R7).

### Sesión / Mensaje
- **Campos por mensaje**: `rol` (estudiante|tutor), `texto`, `evidencia` (lista de
  fid o `fuera_del_curso`), `marca_temporal`.
- **Reglas**: apend-only; una sesión por día de uso (`sesiones/<fecha>.md`); la
  memoria del tutor (FR-009) se deriva de estas sesiones + `dudas.yaml`.

### Duda
- **Campos**: `id`, `pregunta`, `procedimiento_resolucion`, `evidencia` (≥1 fid),
  `estado` (resuelta|reactivada), `sesion_origen`.
- **Reglas**: no se marca `resuelta` sin `evidencia` (principio II); una duda
  `reactivada` reaparece como pendiente en la próxima conversación.

### Ítem de distinción (Evaluación)
- **Campos**: `id`, `conceptos` (≥2 con relación de vecindad del grafo), `pregunta`,
  `criterios` (derivados de fragmentos), `respuesta_estudiante`, `resultado`
  (logrado|parcial|no_logrado), `retroalimentacion`, `fids_base`.
- **Reglas**: un ítem sin ≥2 conceptos vecinos no es de distinción (rechazo en
  generación, principio V); `resultado` actualiza el nodo del grafo (FR-014).

### Concepto / Nodo de grafo
- **Campos**: `id`, `nombre`, `prerrequisitos` (lista de ids), `estado_dominio`,
  `dudas_activas`.
- **Transición de dominio**: `sin_empezar → en_progreso → dominado`; cualquier duda
  reactivada sobre el concepto lo devuelve a `en_progreso`. `en_progreso` con duda
  abierta se muestra como "con dudas activas" en el panel (US5).

### Retroalimentación de nota
- **Campos**: `fecha`, `evaluacion_real` (nombre), `nota`, `observaciones`,
  `ajustes_derivados` (qué cambió en el estilo del Datito).
- **Reglas**: al guardarse, el sistema registra en `ajustes_derivados` cómo se
  incorporó (FR-015), manteniendo el rastro auditable.

### Progreso
- **Derivado** de evaluaciones + grafo; regenerable; nunca se edita a mano.

### Paquete portable
- **Reglas**: exportar = copia íntegra del directorio del curso (layout de arriba);
  importar = validar `curso.yaml` y regenerar `.indice/` si falta (research.md R6,
  principio VII). El paquete no incluye secretos ni rutas absolutas de la máquina.
