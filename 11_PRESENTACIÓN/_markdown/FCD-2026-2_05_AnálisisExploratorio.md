# FCD-2026-2_05_AnálisisExploratorio

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `FCD-2026-2_05_AnálisisExploratorio.pdf` para busqueda e indexacion.
> 52 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

Fundamentos en Ciencia de 
Datos
Exploración de 
Datos
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #5

## Lamina 2

AGENDA
UNIDAD TEMA
01 Descripción de datos
02 Herramientas de Visualización
03 Ejemplos
 
Clase 5

## Lamina 3

Previamente….
Profesor Guillermo Cabrera Vives

## Lamina 4

Describiendo Datos
Dado un gran conjunto de datos, nos gustaría 
calcular algunas cantidades que resumen de forma 
intuitiva los datos. Para empezar, nos gustaría saber.
● ¿Cuáles son los valores típicos de nuestras 
variables o atributos?
● ¿Qué tan representativos son estos valores 
típicos?

## Lamina 5

Ejemplo: Mantenimiento 
Predictivo
● Consideraremos una máquina que tiene sensores de voltaje, 
presión, rotación y vibración.
● Además, tenemos las fechas de mantención y la fechas de 
fallas.
https://notebooks.azure.com/api/user/Microsoft/project/PredictiveMaintenance/html/Predictive%20Maintenance%20Modeling%20Guide%20Python%203%20Notebook.ipynb

## Lamina 6

Distribuciones
● La distribución de alguna 
variable (aleatoria) es una 
función que asigna a cada 
suceso posible la probabilidad 
de que dicho suceso ocurra.
● Una forma básica de mostrar 
la distribución de los datos es 
a través de un histograma.

## Lamina 7

Centralidad
¿Cuál es el valor que ocurre con mayor 
frecuencia en mis datos?
Media (promedio):
La media describe cómo se ve un valor 
"típico", o dónde está el "centro" de la 
distribución de los datos.

## Lamina 8

Centralidad
Mediana:
La mediana describe el valor “del medio” 
de los datos.

## Lamina 9

Centralidad
La media es más sensible a outliers 
(valores atípicos) que la mediana.

## Lamina 10

Centralidad
La media es más sensible a asimetrías de la 
distribución.

## Lamina 11

Centralidad: Variables 
categóricas
Para variables categóricas ni la 
media ni la mediana tienen sentido.
Moda: valor que aparece más 
seguido.

## Lamina 12

Extensión
La dispersión de muestras mide qué tan bien la media o mediana describe el conjunto de 
muestras.
Una forma de medir la propagación de un conjunto de muestras es a través del rango.
Rango = Valor máximo - Valor mínimo

## Lamina 13

Extensión: varianza
La varianza (muestral) mide cuanto se desvía en promedio los valores de la media.
Nota: el término |xi -x| representa cuánto se aleja xi de x. Al elevarla al cuadrado, hace 
que la varianza sea más sensible a outliers.
Nota: La varianza no tiene las mismas unidades que xi!

## Lamina 14

Extensión: desviación 
estándar
La desviación estándar (muestral) es la raíz cuadrada de la varianza (muestral).
Nota: La desviación estándar SI tiene las mismas unidades que xi!

## Lamina 15

Extensión: percentiles
El percentil es una medida de posición que indica, una vez ordenados los datos de menor 
a mayor, el valor de la variable por debajo del cual se encuentra un porcentaje dado de 
observaciones en un grupo.

## Lamina 16

Extensión: percentiles

## Lamina 17

Herramientas de 
Visualización

## Lamina 18

Visualización de datos
Los siguientes dataset contienen el Cuarteto de Anscombe: todos tienen las 
mismas estadísticas.

## Lamina 19

Visualización de datos
Los siguientes dataset contienen el Cuarteto de Anscombe: todos tienen las 
mismas estadísticas.

## Lamina 20

Visualización de datos
Si yo les digo que el consumo medio de gasolina de los camiones de la 
compañía es 1440 litros, pero los camiones que Ud. administra gastan sobre 
2500 litros, qué me sugiere?

## Lamina 21

Visualización de datos
Buena práctica para:
● Analizar:
○ Identificar patrones ocultos y tendencias
○ Ayuda a formular hipótesis
○ Ayuda a determinar el siguiente paso de análisis o modelamiento.
● Comunicar:
○ Presentar ideas e información de manera sucinta
○ Proveer evidencia
○ Influenciar y persuadir

## Lamina 22

Criterio de Tufte
○ Excelencia gráfica
■ “El mayor número de ideas, en 
el menor tiempo, usando la 
menor cantidad de tinta, en el 
menor espacio.

## Lamina 23

Integridad Visual

## Lamina 24

Integridad Visual

## Lamina 25

Integridad Visual

## Lamina 26

Distorsión de escalas

## Lamina 27

Distorsión de escalas

## Lamina 28

Tipos de visualizaciones
● Distribuciones
● Relaciones
● Composición
● Comparación

## Lamina 29

Distribución: histograma

## Lamina 30

Distribución acumulada

## Lamina 31

Distribución: histograma 2D

## Lamina 32

Distribución: scatter plot

## Lamina 33

Relaciones: scatter plot

## Lamina 34

Composición: gráfico de torta

## Lamina 35

Composición: gráfico apilado 
de área

## Lamina 36

Composición: gráfico de 
barras
https://chartio.com/learn/charts/stacked-bar-chart-complete-guide/https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html

## Lamina 37

Composición: gráfico de 
barras vs líneas

## Lamina 38

Comparación: múltiples 
distribuciones

## Lamina 39

Variables múltiples: corner 
plot

## Lamina 40

Matriz de correlación

## Lamina 41

Boxplot

## Lamina 42

Tendencias

## Lamina 43

Ejemplos

## Lamina 44

Ejemplo: tipo de vino
Los datos son el resultado de 
un análisis químico de vinos 
cultivados en la misma región 
en Italia por tres cultivadores 
diferentes. Se toman trece 
medidas diferentes para los 
diferentes componentes que 
se encuentran en los tres tipos 
de vino.

## Lamina 45

Ejemplo: tipo de vino

## Lamina 46

Ejemplo: tipo de vino

## Lamina 47

Ejemplo: tipo de vino

## Lamina 48

Ejemplo: tipo de vino

## Lamina 49

Ejemplo: obesidad
Este conjunto de datos incluye 
datos sobre la dieta, la actividad 
física y el peso de los adultos del 
Sistema de vigilancia de factores 
de riesgo conductual. Estos 
datos se utilizan para la base de 
datos, tendencias y mapas de 
DNPAO, que proporciona datos 
nacionales y estatales 
especíﬁcos sobre obesidad, 
nutrición, actividad física y 
lactancia.
https://www.kaggle.com/spittman1248/effect-of-socioeconomic-status-on-obesity

## Lamina 50

Ejemplo: obesidad
https://www.kaggle.com/spittman1248/effect-of-socioeconomic-status-on-obesity

## Lamina 51

Ejemplo: obesidad
https://www.kaggle.com/spittman1248/effect-of-socioeconomic-status-on-obesity

## Lamina 52

Fundamentos en Ciencia de 
Datos
Exploración de 
Datos
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #5
