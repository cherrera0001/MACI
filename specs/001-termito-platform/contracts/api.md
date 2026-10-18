# Contrato API local — Plataforma Datito

**Versión**: 1.0.0 · **Fecha**: 2026-10-18 · **Base URL**: `http://127.0.0.1:8377`
· **Formato**: JSON UTF-8 · **Autenticación**: ninguna (solo escucha en localhost por
defecto; aceptar otra interfaz exige flag explícito del CLI).

**Estado de implementación (aceptación 2026-10-18)**: todos los endpoints de este
contrato están implementados y verificados (50 tests pytest + aceptación manual
contra el curso real). Decisiones de refinamiento respecto al borrador:

- `PUT /api/cursos/{slug}/componentes` acepta también `POST` (el wizard heredado
  lo usa); misma semántica, mismas validaciones.
- `estado_interaccion` está siempre presente en `/mensajes`. Para interacciones
  sin ejercicio activo el mapeo es: pregunta conceptual respondida → `"revision"`
  (el intercambio quedó resuelto); sin fuente (regla de silencio) → `"pista"`
  (la única acción posible es orientar o esperar). La máquina completa
  (pista → esperando_intento → paso_mostrado → revision) gobierna los ejercicios.
- `POST /mensajes/{id}/revelar` exige `consentimiento: true` y además un intento
  registrado o pasos agotados; si no, responde 409 `aun_no` con la próxima
  acción pedagógica. Toda revelación queda en `sesion.yaml` (auditable, SC-003).
- Un curso en estado `cerrado` rechaza chat/dudas/revelar con 409
  `datito_cerrado`; `GET /registro` sigue disponible (FR-016).

Errores: cuerpo `{ "error": "<codigo>", "detalle": "..." }` con HTTP 4xx/5xx.
`codigo` en snake_case estable (ej. `curso_no_encontrado`, `sin_modelo_local`,
`fuente_sin_extraer`).

## Cursos

```text
GET  /api/cursos
  → 200 { "cursos": [{ "slug", "nombre", "estado", "progreso_resumen" }] }

POST /api/cursos
  { "slug", "nombre"?, "periodo"?, "idioma"? } → 201 { "slug", "estado": "configurando" }
  409 si slug existe; 422 si slug inválido.

GET  /api/cursos/{slug}
  → 200 { "curso": {...curso.yaml}, "componentes": {...}|null, "prompt_editado_manual": bool }
```

## Ingesta y construcción

```text
POST /api/cursos/{slug}/fuentes            (multipart: archivos o { "rutas": [...] })
  → 202 { "resumen_ingesta": { "fuentes": [...], "fragmentos_por_fuente": {...},
          "advertencias": [...] } }

PUT  /api/cursos/{slug}/componentes
  { "rol_dominio": "...", ..., "relacion_temporal": "..." }  (los 8 campos, parciales
  permitidos en borrador) → 200 { "completo": bool, "faltantes": [...] }

POST /api/cursos/{slug}/construir
  → 200 { "prompt": "...", "version": "YYYYmmdd-HHMMSS" }  (exige componentes completos)
```

## Conversación (núcleo del principio II y III)

```text
POST /api/cursos/{slug}/mensajes
  { "texto": "..." }
  → 200 {
      "respuesta": "...",                     // generada SOLO desde fragmentos (R5)
      "evidencia": [ { "fid": "...", "fuente": "...", "referencia": "pág. N | hh:mm:ss" } ],
      // O, si no hay respaldo:
      "evidencia": [], "sin_fuente": true,
      // O, si el estudiante pidió responder fuera del curso:
      "fuera_del_curso": true,
      "estado_interaccion": "pista | esperando_intento | paso_mostrado | revision",
      "paso": { "numero": 1, "total": 3 },   // solo cuando paso_mostrado: pista graduada
      "duda_registrada": { "id": "..." } | null
    }

  Invariantes: si "estado_interaccion" != "revision" en un ejercicio, la respuesta
  NUNCA contiene la solución final (SC-003). "paso_mostrado" revela exactamente un paso
  del procedimiento por llamada, en orden (patrón "Show a step" de Khan Academy,
  validación REA 2026-10-17). Toda entrada en "evidencia" resuelve a un fid existente
  (SC-002).

POST /api/cursos/{slug}/mensajes/{id}/revelar
  Revelación consentida de una solución → 200 { "solucion": "...", "registro": "..." }
  (solo permitido en estado_interaccion == "pista" o "revision", y queda registrado).
```

## Evaluación, grafo, ciclo de vida

```text
POST /api/cursos/{slug}/evaluaciones
  { "tema"?: "..." } → 201 { "id", "items": [ { "id", "conceptos": [...],
                        "pregunta", "criterios" } ] }

POST /api/cursos/{slug}/evaluaciones/{id}/respuestas
  { "items": [ { "id", "respuesta" } ] }
  → 200 { "resultado": "...", "actualizacion_grafo": [ { "concepto", "estado" } ] }

GET  /api/cursos/{slug}/grafo
  → 200 { "nodos": [ { "id", "nombre", "prerrequisitos": [...], "estado_dominio" } ] }

POST /api/cursos/{slug}/notas
  { "evaluacion": "...", "nota": "...", "observaciones"? }
  → 200 { "ajustes_derivados": [...] }

POST /api/cursos/{slug}/cerrar   → 200 { "estado": "cerrado", "registro_integro": true }
GET  /api/cursos/{slug}/registro → 200 { "dudas": n, "evaluaciones": n, "sesiones": n }
```

## Portabilidad y salud

```text
POST /api/cursos/{slug}/exportar → 202 { "ruta": "..." }
POST /api/importar               { "ruta": "..." } → 201 { "slug" }
GET  /api/salud → 200 { "modelo_local": bool, "version_modelo": "...", "modo": "tutor | exploracion" }
```

## Notas de diseño

- La API es una envoltura del dominio; toda regla de negocio vive en el paquete
  `datito/` y es testeable sin HTTP (research.md R4).
- Ningún endpoint realiza llamadas de red salvo al LLM/embeddings configurados por el
  usuario (FR-020); en modo "exploracion" la API lo declara en `/api/salud`.
