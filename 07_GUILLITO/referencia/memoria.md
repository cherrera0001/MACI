# Referencia · Memoria pedagógica

Cargar al cerrar sesión, para registrar el progreso.

---

## Los seis estados

| Estado | Significado |
|---|---|
| `NO_ESTUDIADO` | No visto |
| `EN_ESTUDIO` | Se le explicó. Nada verificado |
| `COMPRENSION_PARCIAL` | Lo explica con huecos, o el mecanismo incompleto |
| `COMPRENDIDO` | Explica y aplica correctamente |
| `DOMINADO` | Explica, aplica, interpreta resultados **y** transfiere |
| `REQUIERE_REPASO` | Lo sabía y falló en una re-verificación |

## La cadena de evidencia

```
EXPLICAR  →  APLICAR  →  INTERPRETAR  →  TRANSFERIR
```

| Evidencia | Se cumple cuando |
|---|---|
| `EXPLICAR` | Lo explica con sus palabras, sin leer, sin que se lo dictaran |
| `APLICAR` | Resuelve un **nivel 2** completo sin andamiaje |
| `INTERPRETAR` | Lee resultados reales y dice qué significan y qué no |
| `TRANSFERIR` | Resuelve un **nivel 3**: otro dominio, descubriendo qué aplica |

`DOMINADO` exige las cuatro. Cada una se registra como
`{fecha, detalle}` — nunca un booleano, que no es auditable.

### Qué NO es evidencia

- Decir "entendí", "claro", "tiene sentido"
- Repetir tu explicación con otras palabras
- Acertar tras recibir la respuesta o una pista muy fuerte
- Acertar por el motivo equivocado
- Responder bien **una sola** pregunta

Sé estricto. Un registro inflado no le sirve en el certamen.

## Re-verificación

Cada concepto guarda `ultima_verificacion`. Al abrir sesión, si hay
`COMPRENDIDO` o `DOMINADO` antiguos, elige uno y hazle una pregunta corta. Si
falla, pasa a `REQUIERE_REPASO` y dilo sin dramatismo: olvidar es normal, y
detectarlo es para lo que sirve el registro.

---

## Qué escribir y dónde

### `progreso.yaml`

- `estado` de los conceptos tocados
- `evidencias.*` con fecha y una línea de qué hizo exactamente
- `sesiones`, `ultima_verificacion`
- el bloque `resumen` y `siguiente_recomendado`

### `errores_conceptuales.yaml`

Registra el error **concreto**, no "tuvo dificultades". Campos: `concepto`,
`dijo`, `confusion_de_fondo`, `desmontaje_que_funciono`, `estado`.

**Distingue fallo conceptual de fallo de procedimiento.** Si entiende el
concepto pero se saltó un paso, márcalo con `distincion_no_es_conceptual: true`
y una nota — para que una sesión futura no le reexplique lo que ya sabe.

Si un error reaparece, incrementa `veces` y añade la fecha. Tres veces no es un
despiste: es un modelo mental equivocado que hay que atacar de frente.

Dos secciones que **no se mezclan**:

- `observados` — errores que cometió de verdad
- `patrones_vigilados` — trampas que anticipas. **No son errores suyos**

### `bitacora/AAAA-MM-DD-<concepto>.md`

Una entrada por sesión: qué se enseñó, los problemas planteados, lo que
respondió, dónde estuvo el desvío, y el siguiente paso.

### Y al terminar

```bash
python 03_CODIGO/guillito_estado.py
```

Regenera `estado.md`, que es lo que se inyecta la próxima vez. Si no lo
ejecutas, la siguiente sesión abre con datos viejos.
