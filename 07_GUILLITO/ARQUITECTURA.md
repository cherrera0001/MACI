# Arquitectura de Guillito

**Versión 1 · 2026-09-20**

Cómo está construido el tutor: qué componentes hay, cómo fluyen los datos entre
ellos, qué invariantes los sostienen y qué se rompe si se violan.

> **Esto no es el contrato.** El contrato es [`spec.md`](../spec.md): qué
> garantiza Guillito y qué tiene prohibido. Este documento responde otra
> pregunta: *por qué el sistema tiene la forma que tiene*. Cuando una decisión
> de diseño existe para cumplir una garantía, se cita la garantía.

---

## 1 · La restricción que define todo lo demás

Un tutor socrático tiene que **hacer una pregunta y esperar**. No simular la
respuesta, no responderse a sí mismo, no seguir explicando: esperar de verdad,
en un turno que termina ahí. Esa es la garantía G1, y es la razón de ser del
sistema — sin ella es un generador de explicaciones, no un tutor.

De ahí sale la primera decisión de arquitectura, y no es negociable:

```
                     ¿la tarea necesita esperar
                      una respuesta del alumno?
                               │
                ┌──────────────┴──────────────┐
               SÍ                             NO
                │                              │
        corre en la CONVERSACIÓN        corre en un FORK aislado
        (no puede delegarse)            (no gasta contexto de estudio)
                │                              │
          /guillito                    /guillito-visual
          /guillito-progreso           /guillito-corregir
                                       /guillito-pedagogia
```

**Un subagente no sabe esperar al usuario.** Recibe un encargo, lo ejecuta y
devuelve un resultado; no hay nadie al otro lado a quien preguntarle. Por eso el
tutor *no puede* ser subagente — y por eso construir un artefacto o corregir un
lote *sí* pueden, porque ninguna de esas tareas necesita esperar a nadie.

Todo lo demás en esta arquitectura es consecuencia de esa línea divisoria.

---

## 2 · Componentes

### Las cinco skills

| Skill | Ejecución | Escribe | Para qué |
|---|---|---|---|
| `guillito` | Conversación | `progreso.yaml`, `errores_conceptuales.yaml`, `bitacora/` | El bucle socrático: problema → respuesta → diagnóstico → pista |
| `guillito-progreso` | Conversación | **nada** | Informe de estado. Solo lectura, por diseño |
| `guillito-visual` | Fork | `visual/*.html` | Un artefacto HTML autocontenido por concepto |
| `guillito-corregir` | Fork | `progreso.yaml`, `errores_conceptuales.yaml` | Corrige un lote entero y devuelve informe |
| `guillito-pedagogia` | Fork | **nada** | Audita el diseño instruccional contra Bloom y alineamiento constructivo |

Dos de las cinco son de **solo lectura**, y eso es deliberado: separar
*observar el estado* de *modificarlo* evita que un informe de progreso acabe
alterando el progreso que informa.

### Por qué `guillito-pedagogia` no sabe ciencia de datos

Es el componente menos obvio del sistema. No audita si el contenido técnico es
correcto —para eso está el material del curso— sino si el material **apunta al
nivel cognitivo que la evaluación real exige**. Un artefacto puede ser
técnicamente impecable y entrenar *Recordar* cuando el certamen pide *Evaluar*.

Está separado a propósito: un auditor que también enseña tiende a aprobar su
propio material.

---

## 3 · Los tres planos de datos

El error más común al construir algo así es mezclar el plan, el estado y el
resumen en un solo archivo que nadie sabe quién puede tocar. Aquí están
separados por **quién escribe**, no por tema:

```
 PLANO ESTÁTICO            PLANO DINÁMICO              PLANO DERIVADO
 (nadie escribe            (solo Guillito              (lo regenera un
  durante una sesión)       escribe)                    script, nunca a mano)

 curriculum.yaml  ────►  progreso.yaml       ─────►  estado.md
 21 conceptos,           estado por concepto,        1.105 bytes
 prerrequisitos,         cadena de evidencia         ▲
 material, prácticos             │                   │ guillito_estado.py
        │                        │                   │
        │                errores_conceptuales.yaml   │
        │                observados / vigilados      │
        │                        │                   │
        │                   bitacora/                │
        │                   una por sesión           │
        │                                            │
        └──────────────────────────────────────►  grafo.yaml
                          grafo_conceptual.py      importancia_curricular
```

**Regla dura:** `curriculum.yaml` es de solo lectura durante las sesiones. Si el
tutor pudiera editar el plan de estudio mientras enseña, podría —sin mala
intención— ajustar el objetivo a lo que el alumno ya sabe. El plan se cambia a
mano, fuera de sesión, y queda en el historial de Git.

### `estado.md` es el punto de inyección

Este es el detalle de diseño que más decide el comportamiento del sistema en la
práctica:

```
progreso.yaml   19.997 bytes   ← la verdad completa
estado.md        1.105 bytes   ← lo que se inyecta en cada sesión  (95 % menos)
```

Guillito no lee el YAML entero al arrancar: lee el resumen. La verdad completa
sigue disponible para cuando haga falta, pero el arranque de cada sesión cuesta
**un kilobyte**, no veinte. Es una decisión de presupuesto de contexto, y tiene
un precio: **hay que regenerar el resumen después de cada sesión** o la
siguiente abre con datos viejos.

```bash
python 03_CODIGO/guillito_estado.py
```

Ese comando no es opcional. Es la contrapartida de la optimización.

---

## 4 · La regla que no puede vivir en un archivo de configuración

La garantía **G8** dice: *una regla vive donde se lee, o no existe*.

Suena a preferencia de estilo. No lo es — es un invariante arquitectónico con
consecuencias:

```
.claude/skills/guillito/SKILL.md      se carga en CADA invocación   → aquí van las REGLAS
07_GUILLITO/guillito.config.yaml      NO se carga automáticamente   → aquí van solo DATOS
```

Si una regla de conducta se escribe en `guillito.config.yaml`, el modelo **nunca
la lee** salvo que algo la abra explícitamente. La regla existe en el
repositorio, parece configurada, y no gobierna nada. Es peor que no escribirla:
crea la ilusión de que está aplicada.

Por eso `verificar_contrato.py` comprueba que la densidad de palabras como
*regla*, *prohibido* u *obligatorio* en el config sea **baja**. Un config lleno
de imperativos es la señal de que alguien escribió reglas donde no se leen.

---

## 5 · Los artefactos HTML no son un extra

La garantía **G9** manda que explicar un concepto nuevo deje **material
consultable**, no texto en el chat. La arquitectura lo implementa así:

```
  explicar un concepto
          │
          ├──► /guillito-visual  (fork)  ──► 07_GUILLITO/visual/<concepto>.html
          │                                   autocontenido · sin conexión
          │                                   sin CDN · sin dependencias
          │
          └──► el chat queda libre para el bucle:
               preguntar · esperar · diagnosticar · dar una pista
```

Tres propiedades que no son accidentales:

1. **Autocontenidos.** Un HTML con todo dentro —CSS, JS, datos— abre en el
   navegador sin red. El material de estudio no puede depender de que un CDN
   siga existiendo la noche antes del certamen.
2. **Se corren en fork.** Construir un artefacto de 25 KB consume mucho
   contexto. Hacerlo en la sesión de estudio dejaría al tutor sin memoria de la
   conversación justo cuando más la necesita.
3. **Están enlazados entre sí.** Los nueve artefactos forman un grafo navegable:
   cada concepto declara de dónde viene, qué habilita y dónde se evalúa.

### Estado actual de los artefactos

| Artefacto | Qué cubre |
|---|---|
| `triaje_de_problemas.html` | Árbol de decisión: qué tipo de problema tengo |
| `clase6_regresion.html` | La clase de regresión completa |
| `regresion_y_costo.html` | Laboratorio de la función de coste |
| `generalizacion.html` | La brecha entrenamiento–validación |
| `train_validation_test.html` | Los cuatro métodos de validación |
| `matriz_confusion.html` | Las cinco métricas, por su denominador |
| `limpieza_preparacion.html` | Calidad de datos, sobre la tabla real de la 9B |
| `certamen_1.html` | Certamen 1 auditado pregunta por pregunta |
| `certamen_2.html` | Certamen 2 auditado pregunta por pregunta |

---

## 6 · Ingesta: de un video de 500 MB a una marca de tiempo

El curso se dicta en clases grabadas. Convertirlas en material citable es un
pipeline propio, fuera del bucle de estudio:

```
10_GRABACIÓN_CLASES/*.zip        3 ZIP · 15 videos · 5,8 GB · gitignorados
          │
          │  transcribir_cola.py     extrae uno, transcribe, borra el mp4
          │  transcribir_clases.py   faster-whisper int8 · CPU · sin ffmpeg
          ▼
09_CLASES/transcripciones/       <clase>.md  (con marcas de tiempo)
                                 <clase>_plano.txt  (para grep)
          │
          │  integrar_clase.py
          ▼
09_CLASES/indice_clases.yaml     qué concepto aparece, y en qué minuto
          │
          └──► (opcional) subida a NotebookLM, si la sesión MCP está viva
```

**Por qué transcribir en local y no subir el video.** NotebookLM acepta video
como fuente, pero entonces la transcripción vive en sus servidores: no se
versiona, no se busca sin conexión, y no se puede leer durante una prueba.
Transcribir aquí produce un `.md` de ~60 KB que entra en el repositorio.

**Por qué el índice y no la transcripción entera.** Una clase transcrita son
85 KB que nadie va a leer. El índice responde la pregunta útil —*¿dónde explicó
validación cruzada?*— con clase y marca de tiempo. La transcripción queda como
respaldo citable, no como lectura.

**Cuidado conocido:** `transcribir_clases.py` define `ORIGEN` apuntando a
`C:\Users\herre\Downloads`, no a `10_GRABACIÓN_CLASES/`. `transcribir_cola.py`
esquiva eso pasando rutas explícitas, pero si se invoca el script base a mano,
hay que extraer antes.

---

## 7 · El contrato es ejecutable

Lo que separa este sistema de un conjunto de instrucciones bien escritas es que
**nueve de sus garantías son un test que corre**:

```bash
python 03_CODIGO/verificar_contrato.py
```

| Comprobación | Qué mira realmente |
|---|---|
| **G1** no simula respuestas | Ninguna respuesta del alumno aparece escrita por Guillito en las bitácoras |
| **G8** reglas donde se leen | `SKILL.md` referencia el config; el config tiene pocas marcas de regla |
| **G9** exposición consultable | Cada concepto trabajado tiene material asociado |
| **G12** dos prioridades | Los 21 conceptos tienen ambas prioridades; las tensiones están declaradas |
| **G13** sin deficiencia inferida | Cada error registrado tiene evidencia textual |
| Memoria | Ningún `DOMINADO` sin sus tres evidencias |
| Seguridad | Ningún secreto ni binario pesado versionado |
| Estado | `estado.md` está al día respecto de `progreso.yaml` |
| Currículum | Todas las rutas del currículum existen en disco |

### Qué **no** puede comprobar

Esto importa tanto como lo anterior, y conviene tenerlo escrito:

- **G2, G5, G6, G7, G11** requieren criterio sobre una conversación concreta. No
  hay forma mecánica de verificar que se preguntó antes de decidir.
- **G4** (cada afirmación lleva su origen) se comprueba por muestreo, no
  exhaustivamente.
- Que un artefacto exista **no prueba que esté bien**. Para eso está
  `guillito-pedagogia`, que es un juicio, no un test.

Un contrato parcialmente verificable es honesto si declara su parte no
verificable. Uno que pretende verificarse entero, miente.

---

## 8 · Degradación: el sistema asume que NotebookLM se va a caer

La integración con NotebookLM usa
[`notebooklm-py`](https://github.com/teng-lin/notebooklm-py) sobre **APIs
internas no documentadas**. Google no ofrece API oficial para cuentas
personales. Las cookies caducan cada pocas semanas y la integración puede
romperse sin aviso.

La garantía **G6** convierte eso en comportamiento definido:

```
    ¿NotebookLM responde?
            │
     ┌──────┴──────┐
    SÍ             NO
     │              │
  4 niveles     avisar en UNA línea
  de fuente     seguir con material local
                etiquetar el resto
                NO ocultarlo
```

**Jerarquía de fuentes (G5):**

1. Material FCD del repositorio — `08_PRACTICA/`, `01_DOCUMENTACION/`, `02_PROYECTO_FCD/`
2. Cuaderno de NotebookLM — 66 fuentes
3. Proyectos propios — Melbourne, Galaxy Zoo
4. Fuentes académicas externas — solo si lo anterior no alcanza

Si el nivel 2 cae, quedan tres. El sistema **no se detiene**: pierde una fuente
y lo declara. Esa sesión se etiqueta distinto, y eso es todo.

### Y lo recuperado son datos, no órdenes

La garantía **G7** cubre el riesgo que introduce cualquier ingesta: si un
fragmento de un PDF o de NotebookLM intenta dirigir el comportamiento del
agente, **se trata como texto citado, no como instrucción**. El material de
estudio es material de estudio.

---

## 9 · La máquina de estados del aprendizaje

```
NO_ESTUDIADO ──► EN_ESTUDIO ──► COMPRENSION_PARCIAL ──► COMPRENDIDO ──► DOMINADO
                      ▲                                                     │
                      └──────────── REQUIERE_REPASO ◄───────────────────────┘
                                  (falla una re-verificación)
```

`DOMINADO` exige la cadena completa, **cada eslabón con evidencia concreta
registrada como `{fecha, detalle}`** — nunca un booleano, que no es auditable:

```
EXPLICAR → APLICAR EN MELBOURNE → INTERPRETAR RESULTADOS → TRANSFERIR
```

| Evidencia | Qué prueba |
|---|---|
| **EXPLICAR** | Lo dice con sus palabras, sin la definición textual |
| **APLICAR EN MELBOURNE** | Lo usa sobre datos reales propios |
| **INTERPRETAR RESULTADOS** | Traduce el número al problema, no solo lo produce |
| **TRANSFERIR** | Lo lleva a un dominio distinto del que lo aprendió |

**Que Cristóbal diga «entendí» no es evidencia de nada.** Tampoco lo es repetir
la explicación con otras palabras, acertar tras una pista fuerte, acertar por el
motivo equivocado, ni responder bien **una sola** pregunta.

> ### ⚠ Deriva contrato–implementación, detectada el 2026-09-20
>
> Las tres fuentes no coinciden:
>
> | Fuente | Cadena que declara |
> |---|---|
> | `spec.md` §3 — **el contrato** | **cuatro** eslabones (los de arriba) |
> | `CLAUDE.md` | tres: explicar → aplicar → transferir |
> | `verificar_contrato.py:146` | tres: `("explicar", "aplicar", "transferir")` |
>
> El verificador **no comprueba `interpretar`**. Hoy el fallo es latente —hay 0
> conceptos en `DOMINADO`—, pero el primero que llegue ahí pasaría el test
> incumpliendo el contrato.
>
> No se resolvió por cuenta propia porque **cambia el estándar de dominio**, y
> esa es una decisión del alumno, no del sistema. Las dos salidas son: subir el
> verificador y `CLAUDE.md` a cuatro, o bajar `spec.md` a tres declarando por
> qué. Lo que no puede quedarse es la discrepancia.

### Los contrapesos a la evaluación circular

Aquí está el riesgo estructural del sistema: **el mismo agente enseña y
evalúa**. Si Guillito diseña el problema, corrige la respuesta y decide el
estado, nada le impide converger a declarar dominio de lo que él mismo explicó.

Los dos que exige el contrato (`spec.md` §3):

1. **Banco fijo de preguntas.** Las `pregunta_diagnostico` de `curriculum.yaml`
   se escribieron **antes** de enseñar. No se reformulan más fáciles ni se
   ablandan.
2. **La transferencia viene de otro dominio.** El mismo problema con otros
   números prueba memoria, no transferencia.

Y dos más que aporta la arquitectura, no el contrato:

3. **Los prácticos `(vacío)`.** `08_PRACTICA/` tiene los 5 laboratorios del
   curso en versión resuelta y sin resolver. Los `(vacío)` son evidencia de
   APLICAR que **no escribió Guillito**.
4. **`guillito-pedagogia`.** Un auditor separado que no enseña, y cuyo trabajo
   es encontrar la brecha entre el nivel cognitivo del material y el de la
   evaluación real.

Ninguno es suficiente por sí solo. Juntos hacen que el bucle no se cierre sobre
sí mismo.

### Re-verificación: sin esto el registro solo sube

Cada concepto guarda `ultima_verificacion`. Al abrir sesión se re-pregunta uno
antiguo; si falla, pasa a `REQUIERE_REPASO`. Es lo que impide que la memoria
pedagógica sea un marcador que solo incrementa — y por tanto deje de medir.

---

## 10 · Mapa de archivos

```
.claude/skills/
  guillito/SKILL.md              ← LAS REGLAS. Se carga en cada invocación (G8)
  guillito-progreso/SKILL.md
  guillito-visual/SKILL.md       ← context: fork
  guillito-corregir/SKILL.md     ← context: fork
  guillito-pedagogia/SKILL.md    ← context: fork

spec.md                          ← el contrato. Manual
CLAUDE.md                        ← hace que Claude Code reconozca a Guillito. Manual

07_GUILLITO/
  ARQUITECTURA.md                ← este documento
  00_LEEME.md                    ← instrucciones de uso
  curriculum.yaml                ← ESTÁTICO · 21 conceptos
  progreso.yaml                  ← DINÁMICO · solo Guillito
  errores_conceptuales.yaml      ← DINÁMICO · observados ≠ vigilados
  estado.md                      ← DERIVADO · el punto de inyección
  grafo.yaml                     ← DERIVADO · importancia_curricular
  guillito.config.yaml           ← DATOS del alumno, nunca reglas
  patron_evaluacion.md           ← cómo evalúa el profesor, desde sus certámenes
  auditoria_*.md                 ← diagnósticos con su cierre
  visual/                        ← 9 artefactos HTML autocontenidos
  bitacora/                      ← una entrada por sesión
  referencia/                    ← fuentes y material, bajo demanda
  guias/ · cuadernillos/ · certamenes/

03_CODIGO/
  guillito_estado.py             ← regenera estado.md   ← CORRER TRAS CADA SESIÓN
  grafo_conceptual.py            ← regenera grafo.yaml
  verificar_contrato.py          ← el contrato como test
  transcribir_clases.py          ← un video → transcripción
  transcribir_cola.py            ← la cola completa, reanudable
  integrar_clase.py              ← transcripción → índice de conceptos

09_CLASES/                       ← transcripciones + índice
10_GRABACIÓN_CLASES/             ← los ZIP. Gitignorado
11_PRESENTACIÓN/                 ← PDF gitignorados; el _markdown/ sí se versiona
08_PRACTICA/                     ← los 5 laboratorios, (res) y (vacío)
```

---

## 11 · Decisiones de diseño y su precio

Ninguna arquitectura es gratis. Estas son las cuentas:

| Decisión | Qué compra | Qué cuesta |
|---|---|---|
| El tutor vive en la conversación | Puede esperar de verdad (G1) | No se puede paralelizar ni correr en background |
| Fork para artefactos y corrección | La sesión de estudio conserva su contexto | El fork no ve la conversación: hay que pasarle todo explícito |
| `estado.md` como punto de inyección | Arranque de 1 KB en vez de 20 | Hay que regenerarlo o se enseña con datos viejos |
| Reglas solo en `SKILL.md` | Lo escrito gobierna de verdad | El `SKILL.md` crece y hay que mantenerlo legible |
| Artefactos autocontenidos | Funcionan sin red, para siempre | Pesan 20–50 KB cada uno y duplican CSS |
| Transcribir en local | Material versionable y buscable offline | Horas de CPU por clase |
| Contrato ejecutable | Nueve garantías dejan de ser buenas intenciones | Las otras cinco siguen dependiendo de criterio |
| Mismo agente enseña y evalúa | Un solo sistema, coherente | Riesgo de circularidad, mitigado pero no eliminado |

---

## 12 · Lo que esta arquitectura todavía no resuelve

**[NO EVIDENCIADO]** Se declara en vez de dejarlo implícito:

- **La circularidad no está cerrada, solo contrapesada.** Los tres contrapesos
  del §9 reducen el riesgo; no lo eliminan. No hay un evaluador externo real.
- **Tres conceptos del currículum no tienen artefacto propio**: segmentación,
  EDA y —hasta hoy— calidad de datos, que acaba de recibir el suyo. La cobertura
  es de 9 artefactos para 21 conceptos.
- **La dimensión `transferencia` está sostenida por un solo dataset.** Es la
  evidencia más difícil de producir y la que menos material tiene.
- **`verificar_contrato.py` comprueba estructura, no calidad.** Que un concepto
  «tenga material» no dice si ese material sirve.
- **La numeración de preguntas del Certamen 2 no coincide** con el registro de
  Canvas desde el ítem de matriz de confusión en adelante. Documentado en
  `visual/certamen_2.html`.
- **`spec.md` y el verificador discrepan sobre `DOMINADO`**: cuatro eslabones
  contra tres. Ver el recuadro del §9. Es la única deriva contrato–implementación
  detectada, y está sin resolver a la espera de una decisión.

---

## Verificación rápida

```bash
python 03_CODIGO/verificar_contrato.py     # debe dar 9 ok · 0 fallos
python 03_CODIGO/guillito_estado.py        # regenera estado.md
python 03_CODIGO/grafo_conceptual.py       # regenera grafo.yaml
python 03_CODIGO/transcribir_cola.py --listar   # qué clases faltan
```
