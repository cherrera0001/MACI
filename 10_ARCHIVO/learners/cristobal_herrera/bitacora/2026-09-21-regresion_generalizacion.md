# Sesión 4 — regresión y generalización (breve)

**Fecha:** 2026-09-21
**Conceptos:** `regresion`, `generalizacion`
**Modo:** instrucción explícita — «¿Cuál es la respuesta correcta?» (G11: se obedece)
**Estado al cerrar:** `regresion` → `EN_ESTUDIO` · `generalizacion` sin cambio

**Dudas registradas:** 2026-09-21-arbol-45cm, 2026-09-21-theta0-theta1, 2026-09-21-agronomo-lluvia
(además, se trasladaron a `dudas.yaml` las de sesiones anteriores:
2026-09-18-baseline-mejora, 2026-09-19-brecha-abc, 2026-09-19-mae-pqr)

---

## Qué pidió

Leyendo `visual/clase6_regresion.html`, llegó a «Tu pregunta» (árbol de 45 cm con
datos entre 8 y 22 cm; el compañero que confunde θ₁ con el peso a radio cero) y
pidió la respuesta correcta y cómo se resolvía: *«no me sirve solo tener la
tensión de "estará bien, o estaré equivocado"»*.

Pidió además que **todo documento traiga la respuesta correcta y su resolución**.

## Qué se le dio

La resolución completa de las dos preguntas. Quedó registrada en
`07_DATITO/dudas.yaml` y renderizada en `visual/clase6_regresion.html` y
`visual/generalizacion.html` (sección «Dudas resueltas con Datito»).

Se le dejó una pregunta de transferencia (agrónomo, 1.200 mm con datos de
300–600 mm). **No respondió todavía.** Su respuesta correcta está oculta en
`generalizacion.html#duda-2026-09-21-agronomo-lluvia`.

## Evidencia

Ninguna. Recibió la respuesta, no la produjo (spec §3: acertar tras recibir la
respuesta no es evidencia). `regresion` pasa a `EN_ESTUDIO` porque Datito lo
explicó; nada verificado.

---

## El segundo loop: Datito también aprende

### Lo que no funcionó — y es la tercera vez

La respuesta se dio **en la terminal**. Cristóbal lo señaló: *«esto me sirve
registrarlo en orden en los documentos html… en la shell se pierde la
oportunidad de volver a procesar… me sirve que el conocimiento generado sea
reutilizable»*.

No es la primera vez: REGLA UNO de la skill ya decía que Cristóbal lo había
reportado dos veces, y el 2026-09-20 una regla de `datito.config.yaml` nunca se
leyó (origen de G8).

### Por qué volvió a pasar (causa, no síntoma)

1. **Un hueco entre dos reglas.** G11 dice «si pide la respuesta, se la das»,
   pero no dice **dónde**. REGLA UNO dice que la exposición va al HTML, pero su
   tabla ponía «tu análisis de su respuesta» y «confirmar que acertó» en el chat.
   Una respuesta pedida quedaba en tierra de nadie, y el camino más barato era el
   chat.
2. **No había dónde registrar una respuesta suelta.** El único formato
   persistente era un visual completo. Editar un HTML a mitad de otra tarea era
   caro (y ese archivo lo estaba editando otro proceso), así que la respuesta no
   tenía un destino natural.
3. **Nada lo comprobaba.** `verificar_contrato.py` revisaba que cada concepto
   tuviera *algún* material, no que lo explicado en una sesión quedara escrito.

### Qué se cambió

| Causa | Corrección |
|---|---|
| Hueco entre G11 y REGLA UNO | `SKILL.md`: **REGLA UNO-B** — toda respuesta, resolución o corrección se escribe primero en `07_DATITO/dudas.yaml`; el chat lleva a lo más la frase corta y la ruta. G11 dice ahora dónde se entrega |
| Sin destino barato | `dudas.yaml` + `construir_navegacion.py` la renderizan en orden en cada visual listado y en el índice. Registrar cuesta una entrada YAML y un comando |
| Nada lo comprobaba | `verificar_contrato.py`: desde el 2026-09-21 toda bitácora declara «**Dudas registradas:**» con ids que existen en `dudas.yaml`, y cada duda está renderizada en sus visuales |
| Pedido explícito | Toda pregunta de los visuales trae «Respuesta correcta y cómo se resuelve» oculta (`datito-visual/SKILL.md`) |

### Representación útil

Para él: la pregunta, **y debajo** la respuesta oculta con la resolución paso a
paso y el error típico, en el mismo documento que lee. Responde en voz alta,
abre, contrasta. La duda que no se cierra no enseña.

## Siguiente paso

Retomar `2026-09-21-agronomo-lluvia` (transferencia) antes de explicar nada
nuevo de generalización.
