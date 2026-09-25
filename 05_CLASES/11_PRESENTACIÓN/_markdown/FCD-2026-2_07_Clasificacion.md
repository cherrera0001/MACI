# FCD-2026-2_07_Clasificacion

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `FCD-2026-2_07_Clasificacion.pdf` para busqueda e indexacion.
> 40 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

Fundamentos en Ciencia de 
Datos
Clasiﬁcación
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #7

## Lamina 2

Previamente….
Profesor Guillermo Cabrera Vives

## Lamina 3

Aprendizaje de Máquinas
• Estudio de algoritmos que
• mejoran su rendimiento P
• en alguna tarea T
• con experiencia E
• Tarea de aprendizaje bien deﬁnida: 
• <P, T, E>

## Lamina 4

Aprendizaje de Máquinas
MÓDULOS
DATOS

## Lamina 5

Regresión
MÓDULOS
EJEMPLO
• Considere la estimación del 
peso de un árbol en función de 
su radio a una altura deﬁnida.
• Me gustaría saber mas menos 
cuál es el peso del árbol sin 
necesidad de cortarlo. radio del tronco
peso

## Lamina 6

Regresión Lineal
MÓDULOS
MÓDULOS

## Lamina 7

Regresión Lineal
GENERALIZACIÓN

## Lamina 8

¿Cómo evaluar si estoy sobreajustado? 
• VALIDACIÓN CRUZADA!
○ Divido mi conjunto de datos en tres:
○ Conjunto de entrenamiento: se usa para que el 
modelo aprenda.
○ Conjunto de validación: Se utiliza para ajustar 
hiperparámetros (por ej, el orden del polinomio).
○ Conjunto de test: Se usa para evaluar. El modelo 
nunca lo ha visto.
● Distintas estrategias de VC: k-fold, shufﬂe split, 
bootstrapping
DATOS
ENTRENAMIENTO VALIDACIÓN TEST

## Lamina 9

AGENDA
UNIDAD TEMA
01 Clasiﬁcación
02 Support Vector Machine
03 Evaluación
04 Métodos basados en árboles
Clase 7

## Lamina 10

Clasiﬁcación
Tamaño de 
las orejas
Tamaño del animal

## Lamina 11

Aprendizaje Supervisado
• Utiliza un conjunto de entrenamiento compuesto por:
○ atributos xi
○ etiquetas yi
• Objetivo: determinar una función que tome los atributos y prediga la etiqueta
• Si la etiqueta a predecir es una categoría, entonces lo 
llamamos clasiﬁcación.

## Lamina 12

Support Vector Machine
Modelos lineales

## Lamina 13

Support Vector Machine
}margen
Support Vector Machine
+1
+1
+1
+1
+1 +1
-1
-1
-1
-1
-1
-1
-1

## Lamina 14

Support Vector Machine
-1
-1
-1
-1
-1
-1
-1+1
+1
+1
+1
+1
+1

## Lamina 15

Evaluación de modelos de clasiﬁcación
https://www.visiondummy.com/2014/04/curse-dimensionality-affect-classification/

## Lamina 16

Positivos
Negativos
Estimación de errores

## Lamina 17

Estimación de errores
• P: Positivos reales.
• N: Negativos reales.
• Verdadero Positivo (VP): Positivo correctamente 
clasiﬁcado.
• Verdadero Negativo (VN): Negativo correctamente 
clasiﬁcado
• Falso Positivo (FP): Negativo incorrectamente 
clasiﬁcado como positivo.
• Falso Negativo (FN): Positivo incorrectamente 
clasiﬁcado como negativo.
Positivos
Negativos

## Lamina 18

Estimación de errores
Exactitud: (VP + VN) / (P + N)
Error: (FP + FN) / (P + N)
Tasa de verdaderos positivos (recall): 
VP /(VP + FN) = VP / P
Precisión: VP / (VP + FP)
Tasa de falsos positivos: FP / (FP + VN)
Positivos
Negativos

## Lamina 19

Positivos
Negativos
 Etiqueta real
 
Etiqueta 
predicha
 
 
6 2
1 7
Matriz de confusión

## Lamina 20

Modelos más complejos
Modelos más complejos

## Lamina 21

¿Cómo evaluar si estoy sobreajustado? 
• VALIDACIÓN CRUZADA!
○ Divido mi conjunto de datos en tres:
○ Conjunto de entrenamiento: se usa para que el 
modelo aprenda.
○ Conjunto de validación: Se utiliza para ajustar 
hiperparámetros (por ej, el orden del polinomio).
○ Conjunto de test: Se usa para evaluar. El modelo 
nunca lo ha visto.
● Distintas estrategias de VC: k-fold, shufﬂe split, 
bootstrapping
DATOS
ENTRENAMIENTO VALIDACIÓN TEST

## Lamina 22

Ejercicio
MÓDULOS
Tasa de Verdaderos Positivos = VP / P
Tasa de Falsos Positivos = FP / N 
Curvas ROC 
(Receiver Operating Characteristic)
Considere los modelos a continuación, donde el modelo puede variar de acuerdo a un hiperparámetro, 
por ejemplo, un humbral de clasiﬁcación. Calcule la tasa de verdaderos positivos y la tasa de falsos 
positivos utilizando los siguientes criterios.

## Lamina 23

Ejercicio
MÓDULOS
Curvas ROC 
(Receiver Operating Characteristic)
Considere los modelos a continuación, donde el modelo puede variar de acuerdo a un hiperparámetro, 
por ejemplo, un umbral de clasiﬁcación. Calcule la tasa de verdaderos positivos y la tasa de falsos 
positivos utilizando los siguientes criterios.
TVP = 0.3
TFP = 0.0
TVP = 0.8
TFP = 0.2
TVP = 0.6
TFP = 0.0
TVP = 1.0
TFP = 0.6
TVP = VP / P
TFP = FP / N

## Lamina 24

EjercicioCurva ROC
TVP = 0.3
TFP = 0.0
TVP = 0.8
TFP = 0.2
TVP = 0.6
TFP = 0.0
TVP = 1.0
TFP = 0.6

## Lamina 25

Decision tree
Árboles de Decisión

## Lamina 26

Decision tree
Árboles de Decisión
• ¿Cómo escoger qué atributo utilizar y dónde dividir?
• Idea: escoger divisiones que hagan “puros” los subconjuntos
 
Datos Conjuntos impuros Conjuntos puros
• ¿Cómo medir la impureza?

## Lamina 27

Impureza de Gini
• Mide el error esperado…
• ...si se escoge aleatoriamente un objeto…
• ...y se predice la clase de todo el conjunto basado en él.
• Ejemplo 1: • La probabilidad de escoger un triángulo es ⅜.
• La probabilidad de escoger un círculo es ⅝.
• Si escojo un triángulo, el error de clasiﬁcar todos los puntos 
como triángulo es ⅝.
• Si escojo un círculo, el error de clasiﬁcar todos los puntos 
como círculo es ⅜.
• El error esperado es entonces ⅜ x ⅝ + ⅝ x ⅜ = 0.46875
P( ) P( )

## Lamina 28

Impureza de Gini
• Mide el error esperado…
• ...si se escoge aleatoriamente un objeto…
• ...y se predice la clase de todo el conjunto basado en él.
• Ejemplo 2: • La probabilidad de escoger un triángulo es ⅛.
• La probabilidad de escoger un círculo es ⅞.
• Si escojo un triángulo, el error de clasiﬁcar todos los puntos 
como triángulo es ⅞.
• Si escojo un círculo, el error de clasiﬁcar todos los puntos 
como círculo es ⅛.
• El error esperado es entonces ⅛ x ⅞ + ⅞ x ⅛ = 0.21875
P( ) P( )

## Lamina 29

Impureza de Gini
• Número de clases : C
• Número de puntos: N
• Número de puntos de la clase i: Ni
⅜ x ⅝ + ⅝ x ⅜ = 0.46875 ⅛ x ⅞ + ⅞ x ⅛ = 0.21875 0 x 1 + 1 x 0 = 0

## Lamina 30

Medidas de impureza
Gini: 
Entropía
Error de 
clasiﬁcación: 
Entropía
Gini
Error de 
clasiﬁcación

## Lamina 31

Ganancia de pureza
Comparar:
• Impureza del nodo padre
• Impureza de los nodos hijos
A
B C

## Lamina 32

Árboles de decisión: algoritmo C4.5
Mientras no se cumpla algún criterio de convergencia:
• Para cada atributo calcular la ganancia de dividir en ese 
atributo
• Sea x el atributo con mayor ganancia
• Crear un nodo de decisión que separe con respecto a x
• Aplique este algoritmo a los subconjuntos creados al dividir 
por x

## Lamina 33

Árboles de decisión: convergencia
• El nodo contiene solamente una clase
• El nodo contiene menos de un valor deseado de objetos
• Se alcanzó una altura máxima
• La pureza es suﬁciente
• Se comienza a sobreajustar (validación cruzada)

## Lamina 34

Random Forests
Anil Mahanty

## Lamina 35

Decision treeLa sabiduría de los grupos
(wisdom of crowds)
El conocimiento colectivo de un grupo 
diverso e independiente de personas 
generalmente excede el conocimiento de 
cualquier individuo y puede aprovecharse 
mediante la votación.
James Surowiecki

## Lamina 36

Decision treeMúltiples árboles
• Un árbol solitario no suele predecir muy bien
• Pero es muy rápido
• Idea: utilizar múltiples árboles
• Debemos asegurarnos de que no aprendan todos 
exactamente lo mismo.

## Lamina 37

Decision treeRandom Forest
• n árboles
• para cada árbol:
• seleccionar aleatoriamente N puntos con reemplazo 
(bootstrapping)
• entrenar usando m atributos seleccionados de manera 
aleatoria
• Predicción: promediar la predicción hecha por los 
árboles

## Lamina 38

Decision treeRandom Forest
• Un gran número de árboles no-correlados tiene 
mejor desempeño que cada uno de los modelos por 
separado.
• Los errores cometidos por un árbol pueden ser 
corregidos por otros.
• Es uno de los algoritmos más certeros que se 
conocen.
• Permiten estimar importancia de las variables 
contando cuántas veces cada variable fue escogida 
por cada árbol como relevante.

## Lamina 39

Resumen
• Clasiﬁcación: aprendizaje supervisado para categorías
• Modelo lineal: Support Vector Machine
• Evaluación y generalización
• Modelos no-lineales:
• árboles de decisión
• random forest
Positivos
Negativos

## Lamina 40

Fundamentos en Ciencia de 
Datos
Clasiﬁcación
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #7
