# Experimento: tareas sacadas de repositorios propios

Abierto el 2026-10-05 por decisión del dueño: «tenemos varios repositorios locales, ¿por qué no pruebas contra
data real, corrigiendo código?». Solo agregados: sin enunciados, parches ni identificadores de tareas.

**Estado (2026-10-06, 14:00 UTC):** pasos 1 a 5 de 6 hechos. Con las nueve tareas pequeñas, el arnés real resuelve
9 de 9 aplicando el parche de referencia, una vez que el paquete del repositorio es importable (ver «Paso 5»). No
se ha corrido ninguna tarea propia con el modelo. Nada de esto se subió a Kaggle.

## Por qué

El conjunto con que se puntúa el concurso se curó de repositorios privados. Las 129 tareas públicas son de
cuatro repositorios famosos que el modelo pudo ver al entrenarse. Un repositorio propio es lo más parecido que
tenemos al conjunto oculto: código que el modelo no vio, con correcciones reales y sus pruebas.

## Qué no es

- No entra en el denominador de ninguna hipótesis ya registrada (línea base A, campaña A/B/C/D, ZorzALL).
- No cambia la regla anterior para VT y la landing en los documentos de ALL: aquí se usan como dato de este
  experimento, por decisión del dueño del 2026-10-05.
- No es una nota del concurso ni la predice.

## Proceso

| Paso | Qué se hace | Con qué | Estado |
|---|---|---|---|
| 1. Candidatos | De la rama principal, cada commit sin fusión que cambia a la vez código Python y un archivo de pruebas. Base: su commit padre. Parche de código, parche de pruebas y enunciado (el mensaje del commit) salen de git | `tareas_propias/candidatos.py` | Hecho |
| 2. Validez | En Linux: con las pruebas nuevas, ¿fallan antes del parche de código y pasan después? Solo esas sirven | `tareas_propias/validar.py`, imagen `aal-ensayo:local` | Hecho |
| 3. Selección | Fijar por regla, antes de correr, cuáles se usan | Regla: discriminan y parche de código de 60 líneas o menos, de los commits de los PR | Hecho: 9 tareas (`tareas_9.jsonl`, `seleccion_9.json`) |
| 4. Formato del arnés | Snapshot por tarea como los de la competencia (historia hasta el commit base, sin commits futuros) y fila en `tasks.jsonl` | `tareas_propias/armar_snapshots.py`, en Docker | Hecho: 9 snapshots con su `.git`, sin commits posteriores (uno de 56 archivos, los demás de unos 5 300) |
| 5. Ensayo sin GPU | Arnés real en Linux con el sandbox de subproceso y el modelo falso que aplica el parche de referencia: la tarea debe quedar resuelta | `tareas_propias/ensayo_propias.py` y `correr_propias.sh`; ejecuta las celdas 4, 9 y 10 del notebook `iteracion-03` con un solo grupo | Hecho en dos ciclos: 5 de 9 y después 9 de 9 (ver «Paso 5») |
| 6. Sesión con el modelo | En Kaggle, con un conjunto de datos privado que lleve snapshots, tareas y las ruedas que falten | `tareas_propias/dataset_propias/` (tasks.jsonl + 9 snapshots, 236 MB, `dataset-metadata.json` para `cs4all/tareas-propias-all`) y `tareas_propias/kernel_propias_01/` (armado por `armar_propias.py`: localiza el conjunto privado sin ruta fija y arma un directorio de datos con enlaces; grupo único `propias`, una pasada AP1, configuración enviada) | Preparado, no subido: chequeo previo con 19 comprobaciones y ensayo en Docker 9 de 9. Costo estimado: unos 35 min de sesión, 1,2 h de cuota, tope de 60 min. Requiere el «sube» (conjunto de datos y notebook) |

Los guiones y sus salidas están en el repositorio del experimento, en
`data/rescate_kaggle/instrumentos/tareas_propias/`, que git ignora.

## Paso 5: el arnés con un repositorio que no conoce (2026-10-06)

Nueve tareas pequeñas, el arnés real en Docker con el sandbox de subproceso (el mismo del notebook), la
configuración enviada y un modelo falso que aplica el parche de referencia y entrega.

| Ciclo | Cambio | Resueltas | Lo que se vio |
|---|---|---|---|
| 1 | Snapshots tal cual, al commit base | 5 de 9 | Las 4 que fallan no pasan de la recolección de pytest: no se importa el paquete de `src/` ni un paquete de la raíz |
| 2 | Un `conftest.py` en la raíz del snapshot, fuera de git, que pone `src/` y la raíz en `sys.path` | 9 de 9 | 117 s en total, de 9 a 21 s por tarea; ningún módulo faltante |

**Causa, aislada con la orden exacta del arnés.** Antes de verificar, el arnés escribe su propio `pytest.ini`
en el espacio de trabajo (`[pytest]` con `addopts`, `norecursedirs`, `python_classes`, `python_files`). Un
`pytest.ini` manda sobre `pyproject.toml`, así que el `pythonpath = ["src", "."]` del repositorio deja de
aplicarse; y corre pytest con `PYTHONSAFEPATH=1`, que tampoco añade el directorio actual. La misma orden, a
mano sobre el mismo snapshot con los dos parches aplicados, pasa en las 4. El arnés conserva un `conftest.py`
existente en la raíz (le antepone su cabecera), por eso el ciclo 2 funciona.

**Lectura.** El arnés monta un repositorio que no conoce, aplica el parche, corre las pruebas nombradas en el
parche de pruebas y declara la tarea. Lo único que falta es lo que en la competencia pone el sandbox: el
paquete del repositorio importable (allí, instalado desde ruedas). Para un repositorio propio con disposición
`src/` sin instalar, el `conftest.py` de raíz es el equivalente. Es una propiedad del entorno de la tarea, no
del agente, y no toca el parche ni el enunciado.

**Lo que esto cambia en «Qué falta para que sea una medición».** El punto 3 (el arnés con un repositorio
nuevo) queda resuelto con esa condición. El punto 2 (dependencias sin conexión) se reduce: las nueve tareas no
necesitan `hypothesis`, y `networkx`, `jsonschema` y `pydantic` están en la imagen del ensayo; en la imagen de
Kaggle habría que comprobarlo en la primera celda, como con las ruedas.

## VT como cantera de tareas (2026-10-06, solo lectura sobre VT)

Por decisión del dueño: ZorzALL debe corregir un repositorio real. Primer paso, las issues ya cerradas: commits
de la rama principal que cambian código y una prueba de vitest. Instrumentos en `tareas_propias/vt/`
(`candidatos_vt.py`, `validar_vt.mjs`); validez en Docker con Node 22 y pnpm 9.12, vitest sobre los archivos de
prueba del commit, antes y después del parche de código.

| Medida | Valor |
|---|---|
| Commits sin fusión en la rama principal | 549 |
| Candidatos (código y prueba de vitest) | 112 |
| Con asunto de corrección / citan una issue | 23 / 43 |
| Mediana de líneas del parche | 75 |
| Regla de selección, fijada antes de validar: 60 líneas o menos, un paquete, sin tocar dependencias ni base de datos | 44 |
| Discriminan | 15 (12 de la web, 3 de la biblioteca de interfaz) |
| No pasan ni con el parche | 27 (19 de la API, 5 de interfaz, 3 de guiones) |
| Pasan sin el parche | 2 |

De las 15: 10 tienen 30 líneas o menos, 8 citan una issue, 2 tienen asunto de corrección. Las 19 de la API no
fallan por el parche: su preparación de pruebas exige un `.env` con la base de datos; con un Postgres de
ensayo serían recuperables, sin medir. En la de interfaz que se revisó, las pruebas pasan en el commit
completo: el parche de código deja fuera archivos que no son `.ts` ni `.tsx`.

**Lectura.** Hay 15 tareas reales, pequeñas y con juez automático, de un repositorio que el modelo no vio.
Alcanza para ensayar el ciclo completo con un agente local; no alcanza para una tasa. El arnés del concurso no
las juzga (solo pytest): el juez es vitest, fuera del arnés.

## Repositorios mirados

| Repositorio | Archivos Python | Archivos TypeScript | Archivos de pruebas pytest | ¿Sirve hoy? |
|---|---|---|---|---|
| Agents Learning Loops | 130 | 0 | 61 | Sí |
| VT (plataforma) | 4 | 731 | 0 | No con este arnés: solo juzga con pytest |
| VT landing | 4 | 65 | 0 | No, por lo mismo |
| Estacionamiento | 0 | 143 | 0 | No, por lo mismo |
| KleromanteIA | 12 | 0 | 0 | No: sin pruebas |

Los repositorios TypeScript pueden dar tareas sin juez automático: el resultado se leería a mano contra la
corrección real. No se ha armado ninguna.

## Lo que dicen los datos (Agents Learning Loops, 2026-10-05)

| Medida | Valor |
|---|---|
| Commits sin fusión en la rama principal | 60 |
| Candidatos (cambian código y pruebas) | 32 |
| Discriminan: fallan antes y pasan después | 19 |
| No pasan ni con el parche de código | 12 |
| Pasan sin el parche | 1 |

De las 12 que no pasan, la causa más probable es que el commit también cambió archivos que no son código ni
pruebas (30 de los 32 candidatos lo hacen) y el parche de código no los lleva. No se comprobó una por una.

**El tamaño no es comparable con el concurso.**

| Líneas cambiadas en el parche de referencia | Tareas públicas del concurso (129) | Tareas propias válidas (19) |
|---|---|---|
| Mediana | 12 | 255 |
| De 60 líneas o menos | 103 | 2 |

Los commits de este repositorio son fusiones aplastadas de un PR entero: una funcionalidad, no una corrección.
Un agente que hoy resuelve entre 2 y 4 de 15 tareas de 10 líneas no va a escribir 255. Con estas 19, lo
esperable es cero y no aprenderíamos nada.

Otros datos de las 19: 11 tocan un solo archivo de código; 6 tienen enunciado de menos de 250 caracteres.

### Segunda pasada: commits individuales de los PR (corrida el 2026-10-05, leída el 2026-10-06)

Se miran todos los commits alcanzables desde las referencias de los PR, antes de aplastarse
(`candidatos.py <repo> allpr todos`), y se validan igual que la primera pasada.

| Medida | Commits aplastados | Commits de los PR |
|---|---|---|
| Candidatos (cambian código y pruebas) | 32 | 93 |
| Discriminan: fallan antes y pasan después | 19 | 65 |
| No pasan ni con el parche de código | 12 | 24 |
| Pasan sin el parche | 1 | 4 |
| Líneas del parche, mediana (de las que discriminan) | 255 | 230 |
| De 60 líneas o menos, que discriminan | 2 | 9 |
| De 30 líneas o menos, que discriminan | 2 | 4 |
| Discriminan y tocan un solo archivo de código | 11 | 41 |
| Discriminan y enunciado de menos de 250 caracteres | 6 | 20 |

De las 9 de 60 líneas o menos: 7 tocan un solo archivo de código, 5 tienen enunciado corto y 2 no cambian
ningún otro archivo. Las 24 que no pasan con el parche cambian todas algún archivo que no es código ni pruebas,
igual que en la primera pasada; sigue sin comprobarse una por una.

**Lectura.** Nueve tareas pequeñas que discriminan es un conjunto con el que se puede ensayar el arnés (paso 5);
no alcanza para una tasa. Las de 60 a 230 líneas siguen siendo funcionalidades, no correcciones.

## Qué falta para que sea una medición

1. **Tareas del tamaño correcto.** Dos caminos, sin elegir todavía:
   - partir de los commits individuales de cada PR en GitHub, antes de aplastarlos, que suelen ser correcciones
     pequeñas con su prueba;
   - usar solo las tareas de 60 líneas o menos. Con los commits aplastados son 2; con los commits
     individuales de los PR, 9 (segunda pasada, arriba).
2. **Dependencias sin conexión.** El sandbox de Kaggle no tiene red. De las dependencias de este repositorio,
   en las 124 ruedas de tareas del concurso están pydantic, pytest y setuptools; faltan networkx, hypothesis y
   jsonschema. Habría que llevarlas en el conjunto de datos privado.
3. **El arnés con un repositorio que no conoce.** Su instalación de dependencias de pruebas depende del nombre
   del repositorio. No se ha probado con uno nuevo.

## Límites

- El repositorio es público desde el 2026-09-29. Es posterior a cualquier entrenamiento razonable del modelo,
  pero no es privado.
- Las tareas las escribió un proyecto asistido por agentes: el estilo de sus commits puede no parecerse al de
  los repositorios del conjunto oculto.
- La validez se midió en un contenedor Linux con red, no en el sandbox de Kaggle.
