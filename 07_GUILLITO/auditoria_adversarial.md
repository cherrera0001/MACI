# Auditoría adversarial del sistema Guillito

**2026-09-20** · Encargo: cuestionar el sistema completo con evidencia, sin
asumir que está mal diseñado ni que sus reglas actuales son correctas.

Cada hallazgo se verifica contra el archivo, no contra el recuerdo.

---

## Resumen: cinco contradicciones

| # | Contradicción | Gravedad |
|---|---|---|
| 1 | La hipótesis pedagógica está codificada como **déficit**, y eso contamina tres reglas | **Alta** |
| 2 | Nueve sliders y **cero** exigencias de predicción previa | **Alta** |
| 3 | La regla del HTML es **contractual**, no pedagógica | Media |
| 4 | El grafo de prerrequisitos existe y **no se usa** | Media |
| 5 | La prioridad se fijó **solo** por peso en el certamen | **Alta** |

---

## 1 · La hipótesis está mal codificada, y la introduje yo

### Evidencia

`.claude/skills/guillito/SKILL.md`, sección «Concrecion, antes que notacion»:

> **«Cristobal no digiere la abstraccion matematica pura.»**

`07_GUILLITO/guillito.config.yaml`, el mismo texto, más:

> *"Nunca abrir con la formula. Nunca usar theta ni sumatorias antes de que el
> fenomeno este claro con numeros."*

### El problema

La frase original del alumno fue *«se me hace muy difícil digerir todo esto
cuando se expresa de forma abstracta»*. La traduje a **una carencia permanente**
—«no digiere»— cuando describía **una dificultad situacional** con una
explicación concreta que yo había dado mal.

Eso es un error de inferencia, y tiene consecuencias.

### Las tres reglas contaminadas

| Regla | Qué produce bajo la hipótesis de déficit |
|---|---|
| «Nunca abrir con la fórmula» | **Prohíbe el camino inverso.** Si le entregan `R² = 1 − SSres/SStot` en una prueba, no puede empezar por ahí — pero la regla se lo impide a Guillito |
| «Recién entonces la notación» | La notación queda como **premio final**, no como una representación más entre varias |
| «Nunca theta ni sumatorias antes de…» | Trata los símbolos como **obstáculo**, no como herramienta |

### El síntoma medible

Símbolos matemáticos por artefacto:

```
clase6_regresion         6
regresion_y_costo        1
matriz_confusion         0   ← es un artefacto ENTERAMENTE sobre fórmulas
generalizacion           0
train_validation_test    0
triaje_de_problemas      0
certamen_1 / certamen_2  0
```

El artefacto de matriz de confusión trata cinco métricas que **son cocientes**, y
no contiene una sola ecuación formal. Muestra `TP/(TP+FP)` como etiqueta de
texto y nunca desarma qué es cada símbolo, qué es dato y qué se decide.

Eso no es hacer accesible la matemática. Es esquivarla.

### REFORMULAR

La hipótesis correcta:

> **Cristóbal aprende cuando puede construir conexiones entre múltiples
> representaciones del mismo concepto, y recorrerlas en ambas direcciones.**

Consecuencia: la regla deja de ser un orden obligatorio y pasa a ser una
**exigencia de cobertura**. Un concepto está bien enseñado cuando existen todas
sus representaciones y hay puentes explícitos entre ellas — no cuando se
presentaron en cierto orden.

Y hace falta el camino inverso, que hoy no existe en ninguna regla:

```
ECUACIÓN → qué compara → qué es cada término → cómo se calcula
         → cómo se ve → qué pasa al cambiar los datos → qué significa aquí
```

---

## 2 · Los sliders no hacen pensar

### Evidencia

```
artefacto               sliders   exige predecir antes
regresion_y_costo          2              0
matriz_confusion           4              0
generalizacion             1              0
clase6_regresion           2              1  (débil)
```

**Nueve controles interactivos. Cero momentos en que se exija predecir antes de
mover.**

### El problema

El patrón actual es **MUEVE → OBSERVA**. Eso produce animación, no razonamiento.
Un alumno puede mover una perilla veinte minutos, ver números cambiar, y no
haber formulado una sola hipótesis.

El patrón que produce aprendizaje es **PREDICE → MUEVE → OBSERVA → EXPLICA**:
la predicción obliga a comprometerse con un modelo mental, y la comprobación lo
confirma o lo rompe. Sin el compromiso previo no hay nada que romper.

### MEJORAR, no eliminar

Los sliders se conservan y se potencian. Lo que se agrega es el compromiso
previo:

```
1. Pregunta cerrada antes de habilitar el control
     "Si aumentas θ₁ dejando θ₀ fijo, ¿la recta sube, gira o se desplaza?"
2. El control se habilita al responder
3. Tras mover: "¿ocurrió lo que esperabas? ¿qué término lo produjo?"
```

---

## 3 · La regla del HTML es contractual, no pedagógica

### Evidencia

`SKILL.md`, REGLA UNO:

> *"Si vas a explicar un concepto nuevo, **genera un HTML**… el archivo ES la
> explicación."*

`spec.md` §G9 convierte eso en garantía verificable, y
`verificar_contrato.py` marca **FALLO** si un concepto trabajado no tiene
artefacto.

### El problema

La regla nació de un error real —yo explicaba por terminal tras dos avisos— pero
se formuló como **obligación de formato**, no como criterio pedagógico.

Consecuencia concreta: el verificador reportó fallo por
`train_validation_test` y `generalizacion`, y yo generé dos HTML **para cerrar
la deuda**. No me pregunté si el HTML era el medio adecuado para cada uno. Para
generalización probablemente sí; para train/validation/test, una tabla y un
diagrama podían bastar.

Un sistema que genera artefactos para satisfacer su propio contrato está
optimizando la métrica, no el aprendizaje.

### REFORMULAR

G9 pasa de *«todo concepto tiene HTML»* a:

> **Toda exposición queda en un artefacto consultable, y el medio se elige por
> el concepto.** El chat es para el bucle socrático.

El verificador deja de exigir `.html` y pasa a exigir **material consultable**
—HTML, guía, cuadernillo o sección— con una justificación registrada de por qué
ese medio.

---

## 4 · El grafo de prerrequisitos existe y no se usa

### Evidencia

```
conceptos con prerrequisitos declarados:  20 de 21
menciones de prerrequisitos en SKILL.md:   1
campos disponibles: id, nombre, orden, prerrequisitos, por_que_importa,
                    material_local, pregunta_diagnostico
```

El grafo **está construido**. Es datos sin comportamiento asociado.

### El problema

Guillito no puede responder hoy, con su instrumental:

- ¿Por qué estoy aprendiendo esto?
- ¿De dónde viene?
- ¿Qué concepto posterior depende de esto?
- ¿Qué pasaría si esta pieza no existiera?

`por_que_importa` existe por concepto, pero es una frase aislada: no dice **con
qué conecta**.

### AGREGAR

Dos cosas, ambas baratas porque el grafo ya existe:

1. **Cadenas nombradas** en el curriculum. No una lista de 21 conceptos sino
   trayectos con sentido:
   ```
   error → residuo → función de costo → optimización → entrenamiento
         → sobreajuste → generalización → validación → test

   clasificación → matriz de confusión → TP/FP/FN/TN → precision/recall
                 → F1 → umbral → ROC → AUC
   ```
2. **Obligación de situar**: al abrir un concepto, Guillito dice de dónde viene
   y qué depende de él. Es una consulta al grafo, no criterio suyo.

---

## 5 · La prioridad se fijó solo por peso en el certamen

### Evidencia

`07_GUILLITO/patron_evaluacion.md` ordena los conceptos exclusivamente por
frecuencia en los dos certámenes:

```
1  overfitting_underfitting   3 preguntas
2  limpieza_preparacion       la 9B vale 2,0 puntos
3  matriz_confusion           cálculo manual
4  metricas_clasificacion     2 preguntas
5  roc_auc                    1 pregunta
```

Y en `curriculum.yaml`:

```
hay importancia_curricular?  False
hay prioridad_evaluacion?    False
```

Una sola dimensión, y es la del examen.

### El problema

`regresion` y `funcion_de_costo` aparecen **poco** en los certámenes. Bajo este
criterio son de prioridad baja.

Pero el propio profesor dice en clase:

> *«Por qué se parte con regresión: los conceptos fundamentales que se ven en
> regresión se aplican después en clasificación y sucesivamente en modelos de IA
> más complejos.»*

Es el concepto del que **dependen todos los demás**, y quedó abajo en la lista
porque se pregunta poco.

Eso es exactamente optimizar puntos en vez de conocimiento.

### AGREGAR

Dos campos independientes por concepto:

| Campo | Qué mide | De dónde sale |
|---|---|---|
| `importancia_curricular` | Cuántos conceptos dependen de él | Del grafo, calculable |
| `prioridad_evaluacion` | Peso en los certámenes | De `patron_evaluacion.md` |

Y una regla: **cuando difieran, Guillito lo dice.** *«Esto se pregunta poco y lo
necesitas para seis conceptos posteriores.»*

---

## 6 · La estrategia no se adapta a la intención declarada

### Evidencia

REGLA CERO:

> *"Si pide la respuesta: pista más concreta y vuelve a esperar. **Solo tras dos
> intentos suyos fallidos** puedes desarrollar la solución."*

### El problema

La regla protege contra un fallo real —dar la respuesta demasiado pronto— pero
no distingue entre:

- *«dame la respuesta»* dicho por frustración → la regla acierta al resistir
- *«explícamelo completo»* como decisión de estudio → la regla **estorba**
- *«no entiendo esta ecuación, desármala»* → la regla lo **impide**

Una estrategia pedagógica que no se adapta a la intención explícita del
estudiante deja de ser pedagogía y pasa a ser rigidez.

### AGREGAR: modos explícitos

| El alumno dice | Modo | Comportamiento |
|---|---|---|
| «hazme pensar», «no me des la respuesta» | **Socrático** | REGLA CERO en pleno vigor |
| «explícamelo completo» | **Exposición** | Desarrollo completo, y al final una pregunta |
| «desarma esta ecuación» | **Descomposición** | El recorrido inverso, símbolo por símbolo |
| «practiquemos» | **Entrenamiento** | Problemas del formato del profesor |
| sin señal explícita | **Socrático** | Por defecto |

La REGLA CERO no desaparece: pasa a ser el **modo por defecto**, no el único.

---

## Lo que se conserva sin tocar

No todo está mal, y reemplazar lo que funciona sería el error simétrico.

| Elemento | Evidencia de que funciona |
|---|---|
| **Trazabilidad e índice de clases** | Convirtió 85 KB en «matriz de confusión, minuto 0:49:48» |
| **Ejemplos del propio profesor** | El árbol y el radio del tronco; Deep-Hub y Arauco |
| **Artefactos interactivos** | El medio es correcto; falta el patrón de predicción |
| **Conexión con Melbourne y Galaxy Zoo** | Cifras que el alumno puede verificar en su repositorio |
| **Certámenes como material** | 22 preguntas reales analizadas |
| **Separación evidencia / inferencia** | Permitió marcar las cifras de AUC de la P9 como no derivables |
| **Memoria pedagógica** | Detectó que el fallo del diagnóstico fue de procedimiento, no conceptual |
| **Funcionamiento sin conexión** | Su prueba es sin Internet |
| **Verificación externa del contrato** | Encontró deuda que yo había olvidado |

---

## Plan, por impacto

| # | Acción | Tipo | Coste |
|---|---|---|---|
| 1 | Reformular la hipótesis a múltiples representaciones, con camino inverso | REFORMULAR | Bajo |
| 2 | Patrón PREDICE → MUEVE → OBSERVA → EXPLICA en todos los sliders | MEJORAR | Medio |
| 3 | Modos explícitos de enseñanza | AGREGAR | Bajo |
| 4 | `importancia_curricular` separada de `prioridad_evaluacion` | AGREGAR | Medio |
| 5 | Cadenas conceptuales y obligación de situar | AGREGAR | Medio |
| 6 | G9 pasa de «HTML» a «artefacto consultable, medio justificado» | REFORMULAR | Bajo |
| 7 | Protocolo de ecuaciones: qué resuelve, cada símbolo, dato / aprendido / decidido | AGREGAR | Alto |

---

## Lo que esta auditoría no revisó

- Si los artefactos existentes tienen errores **técnicos**. No era el encargo.
- La calidad de las transcripciones automáticas frente al audio original.
- Si el curriculum de 21 conceptos cubre el programa oficial completo.
