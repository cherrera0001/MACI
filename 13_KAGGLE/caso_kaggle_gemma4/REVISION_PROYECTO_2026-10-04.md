# Revisión completa de Agents Learning Loops y primera nota de Kaggle

> **Vigencia (2026-10-04, 21:33 UTC).** Documento fechado. Desde que se escribió hubo una corrida con el
> modelo, se midió la validez de las tareas y cambió el título del manuscrito. El estado vigente está en
> [`README.md`](README.md), sección 1.6, y en [`RECORRIDO_PASO_A_PASO.md`](RECORRIDO_PASO_A_PASO.md).

- **Fecha:** 2026-10-04, 15:00 UTC.
- **Qué se revisó:** el repositorio en `main` (commit `4af63cc`) y la rama del envío
  (`issue-106-envio-code-track`, commit `13038eb`).
- **Cómo:** en un árbol de trabajo aparte, `F:\Code\.aal-revision-datito`, rama
  `revision-datito-2026-10-04`, para no pisar a la sesión que trabaja en el repositorio.

## 1. Resultado de la validación

| Qué validé | Cómo | Resultado |
|---|---|---|
| Suite de tests | `pytest` completo | 1 989 pasan, 7 omitidos (los de embeddings), 0 fallan; 3 min |
| Experimento 0 | `aal-benchmark --json` contra `evidence/baseline/` | Mismo JSON que la línea base |
| Experimento 1, campaña histórica | `python -m scripts.verify_experiment1` | 144 recibos íntegros, 0 fugas, 0 diferencias en las métricas recalculadas |
| H4 (referencia v2) | Recuento propio desde los 324 recibos de ejecución | 6/18, 0/18 y 0/18 al primer intento con señuelo; 2,0 / 2,5 / 2,5 intentos. Coincide |
| #58 (diagnóstico público) | Recuento propio desde los recibos | 12/18, 18/18, 18/18 en originales; 11/18, 9/18, 9/18 con señuelo. Coincide |
| Conteos de recibos | Conteo de archivos | 396, 860 y 2 830. Coinciden con el README |
| Mutaciones | `len(MUTATIONS)` | 88. Coincide |
| Jobs de CI | Lectura de `ci.yml` | 12. Coincide |
| Clopper-Pearson del análisis de réplicas | Contra `scipy` en 60 casos | Diferencia máxima 3·10⁻¹⁴ |
| McNemar exacto | Contra `scipy`, 624 casos | Diferencia máxima 3·10⁻¹⁶ |
| Suelo de 6 discordantes | Recalculado | Correcto: 2/2⁶ = 0,031; con 5 es 0,0625 |

**Lectura.** Los experimentos del solver son reproducibles y sus números son los que el README
dice. La estadística de los guiones de Kaggle es correcta. No encontré ningún resultado que
corregir, y por la regla del propio repositorio no se edita evidencia.

**Lo que no validé.** La cobertura de 98,7 % (no la volví a medir), `mutation_check` (tarda más
de diez minutos), los conteos de episodios fechados al 2026-10-02, y los guiones de Kaggle más
allá de su estadística y de sus tests.

## 2. Correcciones aplicadas al README de la raíz

Están en el árbol de trabajo aparte, **sin commit**. Son siete cambios en un archivo:

| Dónde | Antes | Ahora | Por qué |
|---|---|---|---|
| Apertura | Una frase de 60 palabras y otra de 45 | Tres párrafos cortos, mismo contenido | Legibilidad |
| § 1, fila «Calidad» | «614 tests» | «1 996 tests (recuento del 2026-10-04)», con la cobertura fechada cuando había 614 | La cifra ya no coincidía con su fuente |
| § 7.1 | «La salida es idéntica a la línea base» | Mismo JSON; en Windows los saltos de línea difieren | En Windows la comparación byte a byte falla |
| § 13 | «hoy no hay ninguna corrida con el modelo ni resultado alguno» | Línea base pre-registrada, ninguna corrida propia, un envío exploratorio con nota 0,06 | Dejó de ser cierto el 2026-10-04 |
| § 14 | No aparece `experiments/gemma_developer_agent/` | Añadido | Omisión |
| § 14 | `docs/` en una línea, solo H4 | Subcarpetas de pre-registros, resultados y figuras | Desactualizado |
| § 14 | `scripts/` con cuatro guiones | Añadidos los de análisis, figuras y Kaggle | Desactualizado |

Para verlos: `git -C F:\Code\.aal-revision-datito diff`.

Las reglas del repositorio piden que un texto público pase por tres roles antes de publicarse
(investigador de papers, validador estadístico y revisor redactor). Estas correcciones no han
pasado por ellos: son una propuesta, no un texto firmado.

## 3. Evaluación de cómo está escrito el README

**Lo que hace bien.** Dice qué se observó, cómo se lee y dónde está la fuente, en una tabla al
inicio. Pone los resultados en contra en negrita. Separa lo que presenta de lo que no presenta.
Cada cifra tiene su archivo. Es más cuidadoso que la mayoría de los README de investigación.

**Lo que le sobra o confunde:**

1. **Son tres documentos en uno.** Mil líneas que mezclan un informe de resultados, la
   documentación de una biblioteca y el manual de proceso del equipo. Quien llega por los
   resultados tiene que atravesar los algoritmos; quien llega por la biblioteca, las campañas.
2. **La sección 3.2 no es para un lector externo.** Explica qué modelo de Claude construye cada
   issue y dónde se fija su identificador. Es política interna y ya vive en `docs/estimation.md`.
3. **El título y el resultado tiran en sentidos opuestos.** El subtítulo presenta una «memoria
   asociativa en grafo»; el hallazgo principal es que ese grafo no supera a un historial de texto.
   Un lector que lea solo el encabezado se lleva la idea contraria a la del experimento.
4. **«Qué presenta este experimento»** cubre dos experimentos y cuatro campañas. El título no
   coincide con el contenido. No lo cambié porque otros documentos enlazan a ese ancla.
5. **Cifras fechadas que envejecen.** Cobertura, episodios y tests llevan fecha, lo cual es
   correcto, pero obligan a revisar el README en cada cambio. Conviene generarlas o quitarlas.
6. **Frases muy largas en las tablas.** Varias celdas pasan de 60 palabras. La información es
   buena; el formato no ayuda a leerla.

**Qué haría, sin hacerlo ahora:** dejar en el README el resumen de resultados, el inicio rápido y
la estructura; mover algoritmos y modelo de datos a `docs/`, y el proceso de desarrollo a
`CONTRIBUTING.md`. Es una reestructuración grande y toca anclas enlazadas, así que debe ser un
issue propio con su revisión, no un parche.

## 4. La nota de Kaggle: 0,06

El envío 56808559 terminó sin error. Nota pública 0,06: tres o cuatro tareas de 58.

**Qué dice ese número y qué no.** Una nota sola sobre 58 tareas tiene mucho ruido. Probabilidad
de obtener 4 tareas o menos según cuál sea la tasa real del envío:

| Tasa real | Tareas esperadas | Probabilidad de ver 4 o menos |
|---|---|---|
| 0,08 | 4,6 | 0,50 |
| 0,10 | 5,8 | 0,30 |
| 0,12 | 7,0 | 0,16 |
| 0,15 | 8,7 | 0,05 |

- La nota es **compatible** con un envío del mismo nivel que la mayoría de la tabla (0,08 a 0,10).
- Es **poco compatible** con un envío del nivel de 0,15.
- El intervalo exacto del 95 % para 4 de 58 va de 0,02 a 0,17.

El cálculo trata las tareas como independientes y con la misma probabilidad, lo que no es
exacto: muchas tareas fallan siempre y unas pocas cambian. El ruido real entre reenvíos puede ser
menor que el binomial. El foro reporta un mismo zip con 0,12 y 0,15, dos tareas de diferencia.

**Conclusión.** No se puede afirmar que la configuración enviada sea peor que las públicas, ni
que sea igual. Las dos sospechas de la otra sesión (60 segundos por comando y 4 minutos por
tarea) son razonables y no tienen evidencia. Cambiar la configuración ahora, a partir de una
nota, sería ajustar al ruido.

**Qué corresponde hacer:**

1. Reenviar el mismo zip hoy y mañana. Tres notas del mismo envío dicen cuánto se mueve la nota
   sola. Si las tres quedan entre 0,05 y 0,07, la configuración es peor que las públicas y hay
   que buscar la causa. Si se mueven entre 0,06 y 0,12, la primera nota fue mala suerte.
2. Desbloquear el modelo en el notebook. La causa de un 0,06 se ve en la tabla de fallos de
   corridas propias, no en la tabla de Kaggle.
3. No tocar el presupuesto ni los 60 segundos hasta tener una de las dos cosas anteriores.

## 5. Observaciones sobre el experimento Kaggle

1. **El pre-registro cubre bien su propio límite.** Dice que su umbral es de significación y no
   de potencia, y que un efecto real de ese tamaño se declararía la mitad de las veces. Mi
   crítica de potencia sigue en pie para la campaña, pero el documento ya la reconoce.
2. **La Enmienda 2 arrastra un efecto no buscado.** Bajó el tiempo por comando a 60 segundos y
   el guion de validez de tareas hereda ese valor. Una tarea cuyas pruebas tarden más de un
   minuto quedaría clasificada como no válida por una decisión de presupuesto del agente. Está
   pendiente de decisión; conviene que la validez use su propio límite.
3. **El envío se hizo sin haber corrido el agente una sola vez con el modelo.** Lo dice el propio
   registro. Con el notebook funcionando, cada envío futuro debería pasar antes por dos tareas
   locales.
4. **La proporción entre aparato y datos sigue invertida:** unas 20 000 líneas de guiones y
   pruebas para Kaggle, y un número.

## 6. Decisiones que esperan respuesta

1. ¿Apruebas el reenvío del mismo zip hoy? Recomiendo que sí.
2. ¿Qué hago con las correcciones del README? Opciones: dejarlas como propuesta en el árbol
   aparte, o hacer commit en esa rama y abrir un PR para que pase por la revisión del repositorio.
3. ¿El límite de tiempo de la validez de tareas se separa del presupuesto del agente?
