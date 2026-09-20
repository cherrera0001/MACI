# FCD-2026-2_04_CalidadDeDatos

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `FCD-2026-2_04_CalidadDeDatos.pdf` para busqueda e indexacion.
> 29 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

Fundamentos en Ciencia de 
Datos
Calidad de Datos
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #4

## Lamina 2

AGENDA
UNIDAD TEMA
01 Dato
02 Tipos de datos
03 Calidad de datos
 
Clase 4

## Lamina 3

Previamente….
Profesor Guillermo Cabrera Vives

## Lamina 4

Datos
Obtener Datos
Explorar Datos
● Estadística descriptiva
● Visualización de los datos

## Lamina 5

¿Qué es un dato?
“Un dato es una medición de algo en 
una escala que sea comprensible 
tanto para el registrador y como para 
el lector."

## Lamina 6

¿De dónde vienen los datos?
• Fuentes Internas: Ya recopilados o son parte de la 
recolección general de datos de la organización.
• Fuentes Externas Existentes: Disponibles desde una 
fuente externa, ya sea gratis o pagando.
• Fuentes Externas Que Requieren Procesamiento: 
Disponibles desde una fuente externa pero su 
adquisición requiere procesamiento especial.

## Lamina 7

¿De dónde vienen los datos? (Ejemplos)
• Fuentes Internas
• Datos centrados en el negocio que están disponibles en la base 
de datos de la organización para registrar las operaciones diarias; 
datos cientíﬁcos o experimentales.
• Fuentes Externas Existentes
• Bases de datos gubernamentales públicas, datos de mercado
• Datos públicos para investigación (por ejemplo, Kaggle, Zenodo)
• Fuentes Externas Que Requieren Procesamiento
• Datos en páginas web

## Lamina 8

Como obtener datos publicados o alojados 
online 
• API (Application Programming Interface): Usando un conjunto de 
funciones predeﬁnidas desarrolladas por una empresa para acceder 
a sus servicios. Normalmente se pagan.
• Google Map API, Facebook API, Twitter API
• RSS (Rich Site Summary): resume el contenido actualizado 
frecuentemente en formato estándar. Gratis si el sitio lo tiene.
• Páginas relacionadas con noticias, blogs
• Web scraping: usando software, scripts o extrayendo manualmente 
datos de lo que muestra una página o del archivo HTML.

## Lamina 9

Web scraping
• ¿Por qué hacerlo? Es posible que páginas antiguas del 
gobierno o sitios de noticieros pequeños no tengan APIs 
para acceder a los datos, ni publiquen fuentes RSS ni 
tengan bases de datos para descargar. No se quiere 
pagar para usar la API o la base de datos. 
• ¿Cómo se hace? Librerías de Scrapping para extraer 
datos de archivos HTML y XML. (Ej: BeautifulSoup)

## Lamina 10

Web scraping
• ¿Deberías hacerlo?
• Si solo quieres explorar: ¿estás violando los términos 
de servicio? ¿Existen problemas de privacidad para el 
sitio web y sus clientes?
• Si quieres publicar tu análisis o producto: ¿Tienen una 
API o una tarifa que estás evitando? ¿Están dispuestos 
a compartir esta información? ¿Estás violando los 
términos de servicio? ¿Hay problemas de privacidad?

## Lamina 12

¿Cómo lucen los datos?
• ¿Qué tipo de valores contienen tus datos? (Tipos 
de dato)
• Simple o atómico:
• Numérico: Enteros, números con decimales 
• Booleano: Binario o valores de verdad
• Palabras: Secuencia de símbolos

## Lamina 13

¿Cómo lucen los datos?
• Compuesto, mezcla de varios tipos atómicos
• Fecha y hora: Valor compuesto con una estructura 
especíﬁca
• Listas: Secuencia de valores
• Diccionarios: Colección de pares clave-valor, un par de 
valores x : y donde x normalmente es una palabra 
llamada clave que representa el “nombre” del valor, e 
y es un valor de cualquier tipo.

## Lamina 14

¿Cómo lucen los datos?
• Diccionarios
• Ejemplo: Expediente de un estudiante
• Nombre: Guillermo
• Apellido: Cabrera
• Clases : [503622-1, 503640-1, 4171059-0 ]

## Lamina 15

¿Cómo lucen los datos?
• ¿Cómo se representan y almacenan los datos? (Formato)
• Datos Tabulados: El conjunto de datos una tabla bidimensional, 
donde cada ﬁla típicamente representa un registro y cada columna 
representa un tipo de medida (csv, tsp, xlsx etc.).

## Lamina 16

¿Cómo lucen los datos?
• ¿Cómo se representan y almacenan los datos? (Formato)
• Datos estructurados: Cada registro de datos se presenta en forma 
de diccionario, posiblemente complejo y de varios niveles (json, 
xml, etc.)

## Lamina 17

¿Cómo lucen los datos?
• ¿Cómo se representan y almacenan los datos? (Formato)
• Datos semiestructurados: No todos los registros están 
representados por el mismo conjunto de claves o algunos 
registros de datos no están representados utilizando la estructura 
de pares clave-valor.

## Lamina 18

Datos Tabulados
• Se espera que cada registro u observación represente un conjunto 
de medidas de un solo objeto o evento.
• Cada tipo de medida se denomina variable o atributo (por ejemplo, 
Altura, Radio y "¿Me gusta?" son variables o atributos). El número 
de atributos se denomina dimensión de los datos.

## Lamina 19

Datos Tabulados
• Cada tipo de medida se denomina variable o atributo (por 
ejemplo, Altura, Radio y "¿Me gusta?" son variables o 
atributos). El número de atributos se denomina dimensión 
de los datos.

## Lamina 20

Datos Tabulados
• Variable cuantitativa: es numérica y puede ser :
• Discreta: puede tener un número ﬁnito de valores en cualquier 
intervalo
• Por ejemplo: "Número de hermanos" es una variable discreta.
• Continua: un número inﬁnito de valores son posibles en cualquier 
intervalo acotado
• Por ejemplo: "Temperatura" es una variable continua
• Variable categórica: sin orden inherente entre los valores
• Por ejemplo: "¿Qué tipo de mascota tienes?" Es una variable 
categórica.

## Lamina 21

Calidad y limpieza de datos

## Lamina 22

¿Son buenos los datos?
• Típicos problemas con los datos:
• Valores faltantes: ¿cómo los completamos?
• Valores incorrectos: ¿cómo podemos detectarlos y 
corregirlos?
• Formato desordenado
• No utilizables: los datos no pueden responder a la 
pregunta planteada

## Lamina 23

Datos desordenados
• La siguiente tabla contabiliza las entregas de productos 
durante un ﬁn de semana.
• ¿Cuáles son las variables en este conjunto de datos?
• ¿Qué objeto o evento estamos midiendo?

## Lamina 24

Datos desordenados
• Se miden las entregas individuales
• Las variables son Hora, Día, Número de productos.

## Lamina 25

Datos desordenados
• Problema: cada encabezado de columna representa un único 
valor en lugar de una variable. Los encabezados "ocultan" la 
variable Día. Los valores de la variable "Número de productos", 
no se registran en una una sola columna.

## Lamina 26

Datos desordenados
• Necesitamos reorganizar la información para hacer explícito el evento 
que estamos observando y sus variables asociadas

## Lamina 27

Ejercicio
¿Cuáles son las variables en este 
conjunto de datos?
¿Qué objeto o evento estamos 
midiendo?
¿Cómo arreglaría la tabla?
Considere los siguientes datos de consumo de bencina de camiones
Consumo Cantidad
El Lunes 
Camión 1 400
Camión 2 3500
Camión 3 2000
El Martes 
Camión 1 350
Camión 2 0
Camión 3 400
El Miércoles 
Camión 1 500
Camión 2 3600
Camión 3 0

## Lamina 28

Respuesta
¿Cuáles son las variables en este 
conjunto de datos?
Día, Camión, Consumo
¿Qué objeto o evento estamos 
midiendo?
Consumo
Consumo Cantidad
El Lunes 
Camión 1 400
Camión 2 3500
Camión 3 2000
El Martes 
Camión 1 350
Camión 2 0
Camión 3 400
El Miércoles 
Camión 1 500
Camión 2 3600
Camión 3 0
ID Día Camión Consumo
1 2026-07-13 1 400
2 2026-07-13 2 3500
3 2026-07-13 3 2000
4 2026-07-14 1 350
5 2026-07-14 2 0
6 2026-07-14 3 400
7 2026-07-15 1 500
8 2026-07-15 2 3600
9 2026-07-15 3 0

## Lamina 29

Fundamentos en Ciencia de 
Datos
Calidad de Datos
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #4
