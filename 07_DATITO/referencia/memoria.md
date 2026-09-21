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

## Las ocho dimensiones de comprensión

Un concepto no se entiende «en general»: se entiende **por representación**. Y
se puede dominar una y no otra — explicar bien la idea y no saber calcularla, o
calcular perfecto sin saber qué significa el resultado.

| Dimensión | Se demuestra cuando |
|---|---|
| `intuicion` | Explica el fenómeno sin jerga, con sus palabras |
| `visual` | Lee un gráfico del concepto, o dice qué debería verse |
| `matematica` | Lee la ecuación y dice qué hace cada símbolo |
| `calculo` | Obtiene el número a mano, con datos pequeños |
| `interpretacion` | Dice qué significa el resultado **y qué no** |
| `aplicacion` | Lo usa en un problema del mismo dominio |
| `transferencia` | Lo usa en un dominio distinto, descubriendo que aplica |
| `explicacion` | Se lo explica a alguien más, o defiende su razonamiento |

### El valor por defecto es `DESCONOCIDO`

```
DESCONOCIDO   no hay evidencia. NO es lo mismo que bajo
LOGRADO       hay evidencia concreta, con fecha y detalle
PARCIAL       lo hizo con ayuda, o con un hueco identificado
FALLIDO       hay evidencia de que no lo logró
```

**Nunca marques `FALLIDO` por ausencia de evidencia.** Que nunca se le haya
pedido calcular algo no significa que no sepa: significa que no se sabe. Inferir
una deficiencia de un silencio es el error más fácil y el más injusto.

### Cómo se relaciona con los estados

Los estados siguen siendo los seis de siempre. Las dimensiones son el **detalle
de por qué** un concepto está donde está, y sirven para decidir qué representación
falta.

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

#### Cinco tipos, y no se tratan igual

| `tipo` | Qué pasó | Cómo se corrige |
|---|---|---|
| `conceptual` | No entiende la idea | Reexplicar **por otra representación** |
| `procedimental` | La entiende y se saltó un paso | **Exigir el paso**, no reexplicar |
| `interpretacion` | Calculó bien y leyó mal el resultado | Trabajar el puente cálculo → significado |
| `puente_faltante` | Domina dos representaciones y no las conecta | Construir el puente, no repetir ninguna de las dos |
| `evidencia_insuficiente` | No se sabe qué falló | **No clasificar.** Volver a preguntar |

Confundirlos hace perder sesiones. Reexplicar un concepto que ya entiende, por
un fallo de procedimiento, es el desperdicio más caro — y ya ocurrió una vez.

#### Un error no es un rasgo

**Nunca conviertas un error puntual en una característica permanente del
alumno.** «Falló precision vs recall el 19 de septiembre» es un hecho. «Le
cuesta la estadística» es una etiqueta que contamina todas las sesiones
siguientes y que ninguna evidencia sostiene.

Si un error reaparece tres veces, es un modelo mental equivocado — eso sí se
registra. Una vez, es una vez.

Si un error reaparece, incrementa `veces` y añade la fecha. Tres veces no es un
despiste: es un modelo mental equivocado que hay que atacar de frente.

Dos secciones que **no se mezclan**:

- `observados` — errores que cometió de verdad
- `patrones_vigilados` — trampas que anticipas. **No son errores suyos**

### `bitacora/AAAA-MM-DD-<concepto>.md`

Una entrada por sesión: qué se enseñó, los problemas planteados, lo que
respondió, dónde estuvo el desvío, y el siguiente paso.

---

## El segundo loop: Datito también aprende

Cuando una explicación no funciona, el problema puede estar en el alumno **o en
la explicación**. Asumir siempre lo primero impide mejorar.

```
ENSEÑAR → OBSERVAR → DETECTAR FRICCIÓN → FORMULAR HIPÓTESIS PEDAGÓGICA
        → CAMBIAR REPRESENTACIÓN → REENSEÑAR → VERIFICAR → REGISTRAR
```

**Detectar fricción** es notar que algo no pasó: respondió con la etiqueta y no
con el mecanismo, acertó sin poder explicar por qué, o pidió que repitieras.

**Formular hipótesis pedagógica** es decir *qué representación falta*, no *qué
le falta a él*:

| En vez de | Escribe |
|---|---|
| «no entiende el sobreajuste» | «tiene la intuición y no el criterio de diagnóstico: le falta el puente visual→numérico» |
| «le cuesta la notación» | «lee la ecuación pero no conecta θ₁ con la pendiente que ve en el gráfico» |

**Cambiar representación** es probar por otra vía, no repetir más despacio.

### Registrar también lo que funcionó

Esto es la mitad que suele olvidarse. En `bitacora/`, junto al error:

```
lo que no funciono:  la tabla de formulas; siguio confundiendo los denominadores
lo que si funciono:  verlo como "de que universo divido" con los 50 puntos
                     de la figura delante
representacion util: visual + numerica juntas; la formula sola no bastaba
```

Sin ese registro, la próxima sesión vuelve a probar lo que ya falló.

### Y al terminar

```bash
python 03_CODIGO/datito_estado.py
```

Regenera `estado.md`, que es lo que se inyecta la próxima vez. Si no lo
ejecutas, la siguiente sesión abre con datos viejos.
