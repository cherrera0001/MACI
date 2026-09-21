# Arquitectura de Datito

**Versión 1 · 2026-09-20**

Cómo está construido el tutor: qué componentes hay, cómo fluyen los datos entre
ellos, qué invariantes los sostienen y qué se rompe si se violan.

> **Esto no es el contrato.** El contrato es [`spec.md`](../spec.md): qué
> garantiza Datito y qué tiene prohibido. Este documento responde otra
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
          /datito                    /datito-visual
          /datito-progreso           /datito-corregir
                                       /datito-pedagogia
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
| `datito` | Conversación | `progreso.yaml`, `errores_conceptuales.yaml`, `bitacora/` | El bucle socrático: problema → respuesta → diagnóstico → pista |
| `datito-progreso` | Conversación | **nada** | Informe de estado. Solo lectura, por diseño |
| `datito-visual` | Fork | `visual/*.html` | Un artefacto HTML autocontenido por concepto |
| `datito-corregir` | Fork | `progreso.yaml`, `errores_conceptuales.yaml` | Corrige un lote entero y devuelve informe |
| `datito-pedagogia` | Fork | **nada** | Audita el diseño instruccional contra Bloom y alineamiento constructivo |

Dos de las cinco son de **solo lectura**, y eso es deliberado: separar
*observar el estado* de *modificarlo* evita que un informe de progreso acabe
alterando el progreso que informa.

### Por qué `datito-pedagogia` no sabe ciencia de datos

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
 (nadie escribe            (solo Datito              (lo regenera un
  durante una sesión)       escribe)                    script, nunca a mano)

 curriculum.yaml  ────►  progreso.yaml       ─────►  estado.md
 21 conceptos,           estado por concepto,        1.105 bytes
 prerrequisitos,         cadena de evidencia         ▲
 material, prácticos             │                   │ datito_estado.py
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

Datito no lee el YAML entero al arrancar: lee el resumen. La verdad completa
sigue disponible para cuando haga falta, pero el arranque de cada sesión cuesta
**un kilobyte**, no veinte. Es una decisión de presupuesto de contexto, y tiene
un precio: **hay que regenerar el resumen después de cada sesión** o la
siguiente abre con datos viejos.

```bash
python 03_CODIGO/datito_estado.py
```

Ese comando no es opcional. Es la contrapartida de la optimización.

---

## 4 · La regla que no puede vivir en un archivo de configuración

La garantía **G8** dice: *una regla vive donde se lee, o no existe*.

Suena a preferencia de estilo. No lo es — es un invariante arquitectónico con
consecuencias:

```
.claude/skills/datito/SKILL.md      se carga en CADA invocación   → aquí van las REGLAS
07_DATITO/datito.config.yaml      NO se carga automáticamente   → aquí van solo DATOS
```

Si una regla de conducta se escribe en `datito.config.yaml`, el modelo **nunca
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
          ├──► /datito-visual  (fork)  ──► 07_DATITO/visual/<concepto>.html
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
3. **Están enlazados entre sí.** Los artefactos forman un grafo navegable:
   cada concepto declara de dónde viene, qué habilita, dónde se evalúa y en qué
   clase y minuto se enseñó. Ese bloque **no se escribe a mano**: lo inyecta
   `03_CODIGO/construir_navegacion.py` entre los marcadores
   `<!-- datito:nav:inicio -->` y `<!-- datito:nav:fin -->`, desde
   `grafo.yaml` y `09_CLASES/mapa_ensenanza.yaml`, y genera `visual/index.html`.

### Estado actual de los artefactos

Al 2026-09-21: **20 artefactos más el índice**, que cubren los 21 conceptos
(cuatro comparten `arboles_y_ensambles.html` y tres `dl_llm_agentes.html`). La
lista comentada está en `07_DATITO/00_LEEME.md` y en `visual/index.html`.

| Tipo | Artefactos |
|---|---|
| Un concepto | `fundamentos_ciencia_datos` · `datos_features_target` · `eda` · `limpieza_preparacion` · `train_validation_test` · `validacion_cruzada` · `generalizacion` · `overfitting_underfitting` · `clase6_regresion` · `clasificacion` · `matriz_confusion` · `metricas_clasificacion` · `roc_auc` · `redes_neuronales` |
| Varios conceptos | `arboles_y_ensambles` (árboles, RF, boosting, ensambles) · `dl_llm_agentes` (deep learning, LLM, agentes) |
| Laboratorio | `regresion_y_costo` |
| Certamen y triaje | `certamen_1` · `certamen_2` · `triaje_de_problemas` |
| Índice | `index.html` — generado |

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
09_CLASES/indice_clases.yaml     qué concepto se MENCIONA, y en qué minuto
          │                      (automático: cuenta palabras, no sabe quién habla)
          │
          │  curación a mano
          ▼
09_CLASES/mapa_ensenanza.yaml    dónde se ENSEÑA: rango, hablante, si es ayudantía
          │
          │  construir_navegacion.py
          ▼
07_DATITO/visual/                bloque «Dónde se enseñó» en cada visual + index.html
          │
          └──► (opcional) subida a NotebookLM, si la sesión MCP está viva
```

**Mención ≠ enseñanza.** El índice automático marcaba `roc_auc` por «Congreso
de los Araucos» y `f1` por «df1», y el título del archivo contaba como mención
de «ciencia de datos». Desde el 2026-09-21 busca palabras completas e ignora la
cabecera (`integrar_clase.py --remapear`), pero sigue sin distinguir al
profesor de un alumno: por eso existe el mapa curado.

**Quién habla importa.** Las ayudantías, las presentaciones de alumnos y la
charla del invitado del 21-ago están transcritas, pero el profesor declaró que
solo sus clases entran al certamen. `mapa_ensenanza.yaml` lo registra por tramo.

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
**doce comprobaciones de sus garantías son un test que corre**:

```bash
python 03_CODIGO/verificar_contrato.py
```

| Comprobación | Qué mira realmente |
|---|---|
| **G1** no simula respuestas | Ninguna respuesta del alumno aparece escrita por Datito en las bitácoras |
| **G8** reglas donde se leen | `SKILL.md` referencia el config; el config tiene pocas marcas de regla |
| **G9** exposición consultable | Cada concepto trabajado tiene material asociado |
| **G14** el material es un curso | Cada clase de `clases.yaml` con visual tiene barra, ficha Bloom, cierre y ≥ 3 preguntas con respuesta; la portada existe |
| **G9** lo respondido queda escrito | Cada duda de `dudas.yaml` está renderizada en sus visuales, y cada bitácora desde el 2026-09-21 declara sus «Dudas registradas» |
| **G9** visuales sin red y citables | Ningún recurso remoto, enlaces y anclas existen, JS sin errores de sintaxis, cada cita de clase es un `.md` completo con una marca que existe (`verificar_visuales.py`) |
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
  `datito-pedagogia`, que es un juicio, no un test.
- Que una cita de clase exista en la transcripción **no prueba que la
  transcripción sea fiel al audio**. `verificar_visuales.py` avisa cuando las
  palabras citadas no calzan con el texto alrededor de la marca, pero el audio
  no se contrasta.

La prueba de comportamiento —abrir cada visual en Edge sin red, mover todos los
controles y registrar errores de JavaScript— no está en el contrato porque
necesita un navegador: `uv run --with playwright python 03_CODIGO/probar_visuales_offline.py`.

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

> ### ✅ Deriva contrato–implementación, detectada y cerrada el 2026-09-20
>
> Durante unas horas las tres fuentes no coincidían: `spec.md` exigía cuatro
> eslabones, mientras `CLAUDE.md` y `verificar_contrato.py` comprobaban tres.
> **El verificador se saltaba `interpretar`**, así que un concepto podía pasar
> el test incumpliendo el contrato.
>
> Resuelto subiendo la implementación al contrato, no al revés:
>
> | Archivo | Cambio |
> |---|---|
> | `verificar_contrato.py` | Comprueba las cuatro, `interpretar` incluida |
> | `progreso.yaml` | Clave `interpretar` añadida a los 21 conceptos |
> | `datito_estado.py` | Cuarta marca: las fichas muestran `EAIT`, no `EAT` |
> | `CLAUDE.md` | Declara las cuatro, citando `spec.md` §3 |
>
> Verificado inyectando un `DOMINADO` con tres de cuatro evidencias: el test
> falla con *«sin interpretar»*. La comprobación mide lo que dice medir.

### Los contrapesos a la evaluación circular

Aquí está el riesgo estructural del sistema: **el mismo agente enseña y
evalúa**. Si Datito diseña el problema, corrige la respuesta y decide el
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
   APLICAR que **no escribió Datito**.
4. **`datito-pedagogia`.** Un auditor separado que no enseña, y cuyo trabajo
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
  datito/SKILL.md              ← LAS REGLAS. Se carga en cada invocación (G8)
  datito-progreso/SKILL.md
  datito-visual/SKILL.md       ← context: fork
  datito-corregir/SKILL.md     ← context: fork
  datito-pedagogia/SKILL.md    ← context: fork

spec.md                          ← el contrato. Manual
CLAUDE.md                        ← hace que Claude Code reconozca a Datito. Manual

07_DATITO/
  ARQUITECTURA.md                ← este documento
  00_LEEME.md                    ← instrucciones de uso
  curriculum.yaml                ← ESTÁTICO · 21 conceptos
  progreso.yaml                  ← DINÁMICO · solo Datito
  errores_conceptuales.yaml      ← DINÁMICO · observados ≠ vigilados
  estado.md                      ← DERIVADO · el punto de inyección
  dudas.yaml                     ← DINÁMICO · lo que Datito respondió, en orden → visuales
  clases.yaml                    ← ESTÁTICO · el curso: unidades, clases, ficha Bloom, cierres (G14)
  grafo.yaml                     ← DERIVADO · importancia_curricular
  datito.config.yaml           ← DATOS del alumno, nunca reglas
  patron_evaluacion.md           ← cómo evalúa el profesor, desde sus certámenes
  auditoria_*.md                 ← diagnósticos con su cierre
  visual/                        ← 20 artefactos HTML autocontenidos + index.html
  bitacora/                      ← una entrada por sesión
  referencia/                    ← fuentes y material, bajo demanda
  guias/ · cuadernillos/ · certamenes/

03_CODIGO/
  datito_estado.py             ← regenera estado.md   ← CORRER TRAS CADA SESIÓN
  grafo_conceptual.py            ← regenera grafo.yaml
  verificar_contrato.py          ← el contrato como test
  transcribir_clases.py          ← un video → transcripción
  transcribir_cola.py            ← la cola completa, reanudable
  integrar_clase.py              ← transcripción → índice de menciones
  construir_navegacion.py        ← grafo + mapa de enseñanza → navegación e index.html
  verificar_visuales.py          ← sin red, enlaces, citas (lo llama el contrato)
  probar_visuales_offline.py     ← cada visual en Edge sin red, con sus controles

09_CLASES/                       ← transcripciones + índice + mapa_ensenanza.yaml
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
| Contrato ejecutable | Once comprobaciones dejan de ser buenas intenciones | Las otras garantías siguen dependiendo de criterio |
| Navegación generada | Una clase nueva actualiza los 20 visuales corriendo un script | El bloque entre marcadores no se edita a mano: se pierde al regenerar |
| Mismo agente enseña y evalúa | Un solo sistema, coherente | Riesgo de circularidad, mitigado pero no eliminado |

---

## 12 · Lo que esta arquitectura todavía no resuelve

**[NO EVIDENCIADO]** Se declara en vez de dejarlo implícito:

- **La circularidad no está cerrada, solo contrapesada.** Los tres contrapesos
  del §9 reducen el riesgo; no lo eliminan. No hay un evaluador externo real.
- **Los 21 conceptos tienen artefacto desde el 2026-09-21**, pero siete lo
  comparten (`arboles_y_ensambles`, `dl_llm_agentes`). Gradient boosting es un
  recuadro, no una sección completa: el profesor no lo enseñó como tema.
  Segmentación (no supervisado) aparece en el triaje y no tiene artefacto: no
  está entre los 21 conceptos.
- **La dimensión `transferencia` está sostenida por un solo dataset.** Es la
  evidencia más difícil de producir y la que menos material tiene.
- **`verificar_contrato.py` comprueba estructura, no calidad.** Que un concepto
  «tenga material» no dice si ese material sirve.
- **La numeración de preguntas del Certamen 2 no coincide** con el registro de
  Canvas desde el ítem de matriz de confusión en adelante. Documentado en
  `visual/certamen_2.html`.
- **La deriva de `DOMINADO` está cerrada** (§9), pero fue real: el contrato y
  su verificador se separaron sin que nada lo detectara. **No hay ningún
  mecanismo que compruebe que `verificar_contrato.py` sigue midiendo lo que
  `spec.md` declara** — se encontró leyendo, no corriendo. Es el hueco más
  incómodo que deja esta arquitectura.

---

## Verificación rápida

```bash
python 03_CODIGO/verificar_contrato.py     # debe dar 12 ok · 0 fallos
python 03_CODIGO/construir_navegacion.py   # regenera navegación e index.html
python 03_CODIGO/datito_estado.py        # regenera estado.md
python 03_CODIGO/grafo_conceptual.py       # regenera grafo.yaml
python 03_CODIGO/transcribir_cola.py --listar   # qué clases faltan
```
