# Cuadernillo 1 · Sobreajuste y calidad de datos

Problemas **con solución explicada**, para leer antes de practicar a ciegas.
Formato del profesor, resolubles en papel.

Cubre los dos conceptos de mayor peso: sobreajuste y validación (36 % del
Certamen 2) y calidad de datos (la pregunta 9B del Certamen 1 vale 2,0 puntos,
más que las ocho cerradas juntas).

> **Cómo usar esto.** Tapa la solución, resuelve, y recién entonces compara. Leer
> la solución primero se siente productivo y no enseña nada.

---

## Parte A · Sobreajuste y subajuste

### A1 · Verdadero o falso con justificación

> Un modelo que obtiene error cero sobre sus datos de entrenamiento es, por
> definición, el mejor modelo disponible.

<details><summary>Solución</summary>

**Falso.**

Error cero en entrenamiento no mide calidad: mide memorización. Un modelo con
suficiente capacidad puede ajustar cada punto de entrenamiento, incluido el
ruido, y fallar sobre datos nuevos.

La calidad solo se mide sobre datos que el modelo **no vio**. Un polinomio de
grado n−1 interpola exactamente n puntos siempre, y eso no lo convierte en buen
modelo de nada.

**Lo que evalúa:** error de entrenamiento ≠ calidad del modelo. Es la P7 del
Certamen 2.

</details>

### A2 · Diagnóstico desde tabla

Tres modelos, métrica R²:

| Modelo | R² entren. | R² prueba |
|---|---|---|
| A | 0,62 | 0,59 |
| B | 0,98 | 0,54 |
| C | 0,41 | 0,39 |

Diagnostica los tres.

<details><summary>Solución</summary>

Primero las brechas: **A 0,03 · B 0,44 · C 0,02**.

| Modelo | Diagnóstico | Por qué |
|---|---|---|
| A | **Ajuste correcto** | Brecha mínima y nivel aceptable |
| B | **Sobreajuste** | Brecha de 0,44: memoriza y no generaliza |
| C | **Subajuste** | Brecha mínima, pero bajo en **ambos** |

A y C tienen casi la misma brecha. **La brecha sola no distingue subajuste de
ajuste correcto** — hace falta el segundo criterio, el nivel.

</details>

### A3 · La misma tabla, otra métrica

| Modelo | MAE entren. | MAE prueba |
|---|---|---|
| P | 0,15 | 0,92 |
| Q | 0,71 | 0,78 |
| R | 1,84 | 1,90 |

<details><summary>Solución</summary>

**Con MAE, menos es mejor.** Aplicar de memoria "brecha = entrenamiento − prueba"
da un número negativo y el diagnóstico invertido.

| Modelo | Cambio | Diagnóstico |
|---|---|---|
| P | 0,15 → 0,92, empeora mucho | **Sobreajuste** |
| Q | 0,71 → 0,78, estable y aceptable | **Ajuste correcto** |
| R | 1,84 → 1,90, estable pero malo | **Subajuste** |

La brecha es siempre *"cuánto empeora al salir del entrenamiento"*, no una resta
fija. Mira qué significa el número antes de restarlo.

</details>

### A4 · Cuál llevar a producción

De la tabla A3, ¿cuál pondrías en producción y por qué?

<details><summary>Solución</summary>

**Q.**

1. **El criterio es el error sobre datos no vistos.** En producción el modelo ve
   datos nuevos, así que decide la columna de prueba: Q 0,78 · P 0,92 · R 1,90.
2. **La brecha como control de estabilidad.** Q tiene 0,07: no memorizó ruido.
3. **Traducir a la unidad del problema.** 0,78 horas ≈ 47 minutos de error
   promedio, frente a ~55 de P y casi 2 horas de R.

P parece el mejor con 0,15 en entrenamiento. Esa cifra no sirve para decidir, y
caer ahí es exactamente lo que la pregunta busca.

</details>

### A5 · Remedios, sin saber el algoritmo

Te dan un modelo que sobreajusta, pero no te dicen qué algoritmo es. Propón dos
remedios y explica su mecanismo.

<details><summary>Solución</summary>

**El diagnóstico no depende del algoritmo.** Sobreajuste es una propiedad del
comportamiento empírico: una brecha grande lo es sea una regresión, un árbol o
una red.

**Los remedios sí, en parte.** Hay dos familias:

*Agnósticos — siempre disponibles:*

- **Más filas de entrenamiento** — más evidencia por parámetro, el ruido deja de ser ajustable
- **Reducir features** — menos oportunidades de encontrar patrones espurios

*Específicos — exigen conocer el algoritmo:*

- **Regularizar (L1/L2)** — penaliza coeficientes grandes y los encoge hacia cero, sin eliminarlos → **amortigua**. Necesita que haya coeficientes.
- **Podar el árbol** — corta ramas, quita capacidad → **elimina**. Necesita que sea un árbol.

**Qué escribir:** o declaras el supuesto (*"si se trata de un árbol…"*) o te
limitas a los agnósticos. Proponer poda sin que nadie dijera que hay un árbol es
un supuesto sin declarar — la P11 del Certamen 2.

</details>

### A6 · La trampa de "más datos"

> Para reducir el sobreajuste siempre conviene añadir más información al modelo.

<details><summary>Solución</summary>

**Falso**, porque "más información" es ambiguo y las dos lecturas tienen efectos
opuestos:

```
MÁS FILAS     (observaciones)  →  REDUCE el sobreajuste
MÁS COLUMNAS  (variables)      →  lo AUMENTA, si no traen señal
```

Más filas dan más evidencia por parámetro. Más columnas dan más parámetros que
ajustar con la misma evidencia.

Además, **más datos no cura el subajuste**: si el modelo no tiene capacidad para
la relación real, más filas solo confirman lo que ya no podía aprender.

**Lo que evalúa:** es la P3 del Certamen 2, textualmente.

</details>

---

## Parte B · Calidad de datos

### B1 · Tabla de calificaciones

| Nombre | Apellido | Matrícula | 17/9/2017 | 19/10/2017 | 22/11/2017 |
|---|---|---|---|---|---|
| Juanita | Pérez | 0101 | *(vacío)* | 5.6 | 7.5 |
| Pedrito | Gutiérrez | 1203 | 1.2 | N/A | N/A |
| Marcia | Navarro | **N/A** | 6.7 | 7.0 | 5.5 |
| Diego | Hernández | 4309 | 3.2 | 2.7 | 7.0 |

Identifica los problemas y propón una solución.

<details><summary>Solución</summary>

**Problemas:**

1. **Formato ancho, no *tidy*.** Las fechas son encabezados de columna: se mezcla
   metadato (cuándo) con estructura. Cada fila debería ser una observación —
   un alumno en una fecha—, no un alumno con tres fechas.
2. **Tipos inconsistentes.** Conviven `N/A` en texto, celdas vacías y números en
   la misma columna. Cualquier lectura automática deja la columna como texto.
3. **Clave primaria rota.** `Matrícula` es el identificador, y Marcia tiene `N/A`.
   Sin identificador no se puede unir esta tabla con ninguna otra ni detectar
   duplicados con fiabilidad.

**Solución:**

- **Des-pivotar** a formato largo: `Nombre · Apellido · Matricula · Fecha · Nota`
- **Estandarizar**: `N/A` y vacíos a un único valor nulo; `Nota` a decimal,
  `Fecha` a tipo fecha
- **Resolver la clave**: recuperar la matrícula de Marcia desde el registro
  oficial, o marcar la fila como no identificable. **No inventarla.**

**Distinción clave:** un vacío y un `N/A` en texto **no son lo mismo** para la
máquina, aunque signifiquen lo mismo para ti.

</details>

### B2 · Consumo de combustible en minería — 2,0 puntos

| CONSUMO | CANTIDAD |
|---|---|
| El Lunes | *(vacío)* |
| Camión 1 | 200 |
| Camión 2 | 200 |
| Camión 3 | **2900** |
| Camión 4 | 200 |
| … | … |
| Camión en mantención | **−999** |

<details><summary>Solución</summary>

**Problemas críticos:**

1. **Sobrecarga semántica.** La columna `CONSUMO` mezcla tres cosas distintas:
   días (*"El Lunes"*), identificadores de camión y estados operativos. Una
   columna debe contener **un solo tipo de cosa**.
2. **Código centinela.** `−999` representa "en mantención", no un consumo. Si se
   calcula un promedio sin tratarlo, el resultado queda destruido: un valor
   imposible entra en la aritmética como si fuera real.
3. **Valor atípico.** `2900` frente a `200` del resto. Puede ser error de digitación,
   falla de sensor, o un camión genuinamente distinto. **No se decide sin
   verificar** — y esa es parte de la respuesta.
4. **Estructura no relacional.** Las filas de día actúan como separadores
   jerárquicos, rompiendo la atomicidad: cada fila debería ser una observación
   completa e independiente.

**Solución:**

- **Normalizar** en una tabla de hechos: `fecha · id_camion · consumo_litros · id_estado`
- **Reemplazar `−999` por nulo** y registrar el estado en una columna aparte.
  El dato "estaba en mantención" es información valiosa: no se borra, se mueve
  a donde corresponde.
- **Investigar el 2900** antes de tocarlo. Documentar la decisión.

**Lo que más puntúa:** no es listar los problemas, es proponer la estructura
correcta y justificar por qué. Vale 2,0 puntos porque pide diseño, no detección.

</details>

### B3 · Verdadero o falso

> Reemplazar los valores faltantes por la media de la columna es siempre
> preferible a eliminar las filas afectadas.

<details><summary>Solución</summary>

**Falso.** "Siempre" es lo que hace falsa la afirmación.

Imputar por la media **reduce artificialmente la varianza** y puede introducir
sesgo si los faltantes no son aleatorios. Si un sensor falla precisamente cuando
los valores son extremos, imputar la media borra justo la señal que importaba.

Eliminar filas tampoco es gratis: pierdes información y, si el faltante no es
aleatorio, sesgas la muestra.

La decisión depende de **cuántos faltan, por qué faltan y qué se hará con los
datos**. Que un valor falte puede ser información en sí mismo — por eso una
columna indicadora de "faltaba" suele ser útil.

</details>

---

## Tarjeta de repaso

```
DIAGNÓSTICO DE AJUSTE
1. ¿La métrica sube o baja cuando mejora?
2. Brecha de cada modelo
3. Brecha grande          → sobreajuste
4. Brecha pequeña + nivel  malo en ambos      → subajuste
                           aceptable en ambos → ajuste correcto
5. Nombrar el MECANISMO, no la etiqueta
6. Remedios: ¿sé el algoritmo? → específicos
             ¿no lo sé?        → declaro supuesto o uso agnósticos
7. ¿Producción? → error sobre datos no vistos

CALIDAD DE DATOS
1. ¿Una fila = una observación?          → si no, des-pivotar
2. ¿Una columna = un solo tipo de cosa?  → si no, separar
3. ¿Hay centinelas (-999, N/A, 0)?       → a nulo, y registrar aparte
4. ¿La clave identifica de verdad?       → si no, recuperar o marcar
5. ¿Tipos consistentes por columna?      → estandarizar
6. ¿Atípicos?                            → investigar, no borrar
```

---

## Siguiente

Cuando hayas trabajado estos problemas tapando las soluciones, pide un
**certamen a ciegas**: problemas nuevos, sin solución, tiempo limitado. Eso mide.
Esto enseña.
