# P1_Laboratorio_Pandas_res

> Material practico de Fundamentos de Ciencia de Datos, UdeC T2-2026.

> Convertido desde `[P1]Laboratorio_Pandas_(res).ipynb` para indexacion.

# [Práctica 1] Fundamentos de Ciencia de Datos
Alejandra Fernández (afernandezm@inf.udec.cl)

# Contenidos

-  **Libreria Pandas**
    - ¿Qué es y para que sirve?
    - Tipos de datos
      - Crear una Serie
        - Acceder a los elementos de una serie
      - Crear una tabla
        - Mostrar una tabla
        - Acceder a una fila/columna
        - Agregar filas/columnas
        - Borrar filas/columnas
        - Recorrer una tabla
-  **Operaciones más complejas en Pandas**
    - Cargar/Guardar tabla existente
    - Combinar tablas
    - Describir los datos
    - Filtrar datos
    - Operaciones sobre los datos
    - Ordenar datos
    - Groupby
-  **Ejercicios**

# Pandas
[Documentación](https://pandas.pydata.org/docs/user_guide/index.html)

## ¿Qué es y para que sirve?

Librería especializada en el manejo y análisis de estructuras de datos.
Principales características:

*   Permite leer y escribir fácilmente ficheros en formato CSV, Excel y bases de datos SQL.
*   Permite acceder a los datos mediante índices o nombres para filas y columnas.
*   Ofrece métodos para reordenar, dividir y combinar conjuntos de datos.
*   Permite trabajar con series temporales.

```python
# importamos las librerías, le damos un seudonimo a las librerias para mejorar
# legibilidad en el código.
import numpy as np
import pandas as pd
from IPython.display import display #Para mostrar la tabla de pandas (No es necesario)
```

```python
pd.__version__
```

*Salida:*
```
'2.2.2'
```

## Tipos de datos

**Series:** estructura de una dimensión. Una serie se compone de un conjunto de datos y una secuencia de identificadores, que son los índices (Básicamente una columna).

**Dataframe:** estructura de dos dimensiones (tabla). Se compone de series y que contiene etiquetas para las filas y las columnas.

### Crear una Serie

Para crear una serie ocupamos **pd.Series(data=datos, index=indices, dtype=tipo)**

- **data** es el conjunto de datos (puede ser una lista, un numpy array o un diccionario)
- **index** es una lista con los indices. Si se omite, toma por defecto los valores desde 0 hasta len(datos) -1
- **dtype** es el tipo de dato. (Especifica como se van a interpretar los datos de la Serie)

```python
#Creamos una serie entregando una lista directamente

datos = [50, 100, 80]

serie = pd.Series(datos)
```

```python
serie
```

*Salida:*
```
0     50
1    100
2     80
dtype: int64
```

```python
#ver el type
type(serie)
```

*Salida:*
```
pandas.core.series.Series
```

```python
# Ahora creemos una serie especificando los indices
# las listas de datos e indices deben tener el mismo largo

index = ['lunes', 'martes', 'miercoles']

serie = pd.Series(datos, index)
serie
```

*Salida:*
```
lunes         50
martes       100
miercoles     80
dtype: int64
```

```python
# Ahora creemos una serie especificando los indices y el tipo de dato
# las listas de datos e indices deben tener el mismo largo

dtype = 'float64' #Para que los considere como float

serie = pd.Series(datos, index, dtype)

serie
```

*Salida:*
```
lunes         50.0
martes       100.0
miercoles     80.0
dtype: float64
```

```python
# Atributos
print('valores: ',serie.values) # Podemos acceder a los valores de la serie
print('indices: ',serie.index)  # a sus indices.
print('tamaño: ', serie.size)   # a su tamaño
print('tipo de dato: ',serie.dtype)  # y a su tipo de dato
```

*Salida:*
```
valores:  [ 50. 100.  80.]
indices:  Index(['lunes', 'martes', 'miercoles'], dtype='object')
tamaño:  3
tipo de dato:  float64
```

```python
type(serie.index)
```

*Salida:*
```
pandas.core.indexes.base.Index
```

```python
# Acceso a los elementos de una serie
print('Acceso por posicion: serie[0] -->', serie[0]) # Devuelve el elemento que ocupa la posicion 0 de la serie
print('Acceso a slice: serie[0:2] \n', serie[0:2]) # Devuelve los elementos entre 0 y 1 (el 2 no se considera)
print('Acceso por un indice: serie[miercoles] -->',serie["miercoles"] ) # devuelve el elemento de 'miercoles'
print('Acceso por multiples indices: serie[[lunes, martes]] \n', serie[["lunes", "martes"]] ) # devuelve una serie con ambos elementos
```

*Salida:*
```
Acceso por posicion: serie[0] --> 50.0
Acceso a slice: serie[0:2] 
 lunes      50.0
martes    100.0
dtype: float64
Acceso por un indice: serie[miercoles] --> 80.0
Acceso por multiples indices: serie[[lunes, martes]] 
 lunes      50.0
martes    100.0
dtype: float64
```

*Salida:*
```
/tmp/ipykernel_1548/1023848662.py:2: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  print('Acceso por posicion: serie[0] -->', serie[0]) # Devuelve el elemento que ocupa la posicion 0 de la serie
```

[**Lista completa de atributos, operaciones y funciones en Series**](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

### Crear una tabla

Para crear un DataFrame (tabla) ocupamos **pd.DataFrame(data=datos, index=indices, columns=columnas)**
- **data** puede ser:
  - Un dicccionario 1D de numpy arrays, listas, diccionarios o Series
  - Numpy array 2D
  - Numpy array estructurado
  - Series
  - Otro DataFrame
- **index**: Opcional. Etiquetas de las filas
- **columns**: Opcional. Etiquetas de las columnas

```python
# Diccionario con datos de juguete.
# Los valores asociados a cada clave del diccionario deben ser listas del mismo
# tamaño.

data = {
    "Producto" : ["A", "B", "C", "D", "E", "F", "G"],
    "Stock" : [10, 20, 30, 40, 30, 20, 10],
    "Precio" : [5000, 2000, 7000, 3000, 2500, 5000, 1000]
}

df_1 = pd.DataFrame(data)
df_1
```

*Salida:*
```
Producto  Stock  Precio
0        A     10    5000
1        B     20    2000
2        C     30    7000
3        D     40    3000
4        E     30    2500
5        F     20    5000
6        G     10    1000
```

```python
# Lista de listas
         # fila 1                               fila 2                         fila 3
rows = [["Aisen", 4, "Apertura Inicial"], ["Algarrobo", 3, "Preparación"], ["Alto Biobío", 2, "Transición"]]

#["Comuna", "Paso", "Estado"]

df_2 = pd.DataFrame(rows, columns = ["Comuna", "Paso", "Estado"])
df_2
```

*Salida:*
```
Comuna  Paso            Estado
0        Aisen     4  Apertura Inicial
1    Algarrobo     3       Preparación
2  Alto Biobío     2        Transición
```

```python
# Atributos de un dataframe
df_2.info()# información de lo que contiene el dataframe
```

*Salida:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Comuna  3 non-null      object
 1   Paso    3 non-null      int64 
 2   Estado  3 non-null      object
dtypes: int64(1), object(2)
memory usage: 204.0+ bytes
```

```python
# Atributos de un dataframe
print('Numero de filas x Numero de columnas: ',df_1.shape)
print('Numero de filas (v2):' ,len(df_1), df_1.shape[0] )
print('Numero de elementos: ', df_1.size )
print('Nombre columnas: ', df_1.columns)
```

*Salida:*
```
Numero de filas x Numero de columnas:  (7, 3)
Numero de filas (v2): 7 7
Numero de elementos:  21
Nombre columnas:  Index(['Producto', 'Stock', 'Precio'], dtype='object')
```

#### Mostrar una tabla

```python
 #Si el dataframe es muy grande, no se mostrará entero
 df_1
```

*Salida:*
```
Producto  Stock  Precio
0        A     10    5000
1        B     20    2000
2        C     30    7000
3        D     40    3000
4        E     30    2500
5        F     20    5000
6        G     10    1000
```

```python
 # devuelve las n primeras filas del dataframe
df_1.head(2)
```

*Salida:*
```
Producto  Stock  Precio
0        A     10    5000
1        B     20    2000
```

```python
 # devuelve las n ultimas filas del dataframe
df_1.tail(1)
```

*Salida:*
```
Producto  Stock  Precio
6        G     10    1000
```

#### Acceder a las filas/columnas

Podemos usar loc o iloc para acceder a cierta fila del dataframe.

loc -> utiliza el indice

iloc -> utiliza la posición

```python
#Vamos a crear un dataframe para mostrar la diferencia
data = {
    "Zona" : ["A", "B", "C", "A", "C", "D", "E"],
    "Peso" : [10, 20, 30, 40, 30, 20, 10],
    "Diametro" : [12, 5, 7.5, 3, 3, 12, 10.5]
}
indices = [50,0,34,5,12,1,20]

df_3 = pd.DataFrame(data, indices)
df_3
```

*Salida:*
```
Zona  Peso  Diametro
50    A    10      12.0
0     B    20       5.0
34    C    30       7.5
5     A    40       3.0
12    C    30       3.0
1     D    20      12.0
20    E    10      10.5
```

```python
#Vamos a acceder con iloc y con loc al elemento 0
print("Con loc :\n", df_3.loc[0])
print("Con iloc :\n",df_3.iloc[0])
```

*Salida:*
```
Con loc :
 Zona          B
Peso         20
Diametro    5.0
Name: 0, dtype: object
Con iloc :
 Zona           A
Peso          10
Diametro    12.0
Name: 50, dtype: object
```

```python
#Acceder al indice usando loc y name
print("Con iloc :\n", df_3.iloc[0])
print("Indice con iloc :", df_3.iloc[0].name)
print("Con loc :\n",df_3.loc[df_3.iloc[0].name])
```

*Salida:*
```
Con iloc :
 Zona           A
Peso          10
Diametro    12.0
Name: 50, dtype: object
Indice con iloc : 50
Con loc :
 Zona           A
Peso          10
Diametro    12.0
Name: 50, dtype: object
```

```python
#Podemos agregar a que elemento de la fila queremos acceder
#Al utilizar loc debemos colocar el nombre de la columna (posicion 0 y diametro)
print("Con loc :\n", df_3.loc[0, "Diametro"])
#Al utilizar loc debemos colocar la posición en la que se encuentra la columna
print("Con iloc :\n",df_3.iloc[0,2])
```

*Salida:*
```
Con loc :
 5.0
Con iloc :
 12.0
```

```python
#Si lo intento al reves da error
"""
print("Con loc :\n", df_3.loc[0,0])
print("Con iloc :\n",df_3.iloc[0, "Diametro"])
"""
```

*Salida:*
```
'\nprint("Con loc :\n", df_3.loc[0,0])\nprint("Con iloc :\n",df_3.iloc[0, "Diametro"])\n'
```

Para acceder a una columa puedo utilizar el operador **.** o el operador **[ ]**

```python
# Acceso a los elementos de un dataframe (acceder a la columna peso)
print('\nAcceso por nombre de columna . : \n', df_3.Peso ) # funciona solo cuando el nombre de la columna no tiene espacios ni .
print('\nAcceso por nombre de columna [] : \n',df_3["Peso"] ) # funciona siempre
```

*Salida:*
```
Acceso por nombre de columna . : 
 50    10
0     20
34    30
5     40
12    30
1     20
20    10
Name: Peso, dtype: int64

Acceso por nombre de columna [] : 
 50    10
0     20
34    30
5     40
12    30
1     20
20    10
Name: Peso, dtype: int64
```

#### Agregar filas/columnas

```python
#Agregar una fila
nueva_fila = {'Comuna': 'Alto Hospicio', 'Paso': 2, 'Estado': 'Transición'}
#dara error por los indices
df_2 = pd.concat([df_2, pd.DataFrame([nueva_fila])], ignore_index=True)

df_2
```

*Salida:*
```
Comuna  Paso            Estado
0          Aisen     4  Apertura Inicial
1      Algarrobo     3       Preparación
2    Alto Biobío     2        Transición
3  Alto Hospicio     2        Transición
```

```python
pd.concat([df_2, pd.DataFrame([nueva_fila])]).reset_index()
```

*Salida:*
```
index         Comuna  Paso            Estado
0      0          Aisen     4  Apertura Inicial
1      1      Algarrobo     3       Preparación
2      2    Alto Biobío     2        Transición
3      3  Alto Hospicio     2        Transición
4      0  Alto Hospicio     2        Transición
```

```python
#Agregar una columna
#Rellena toda la columna con 0s
df_2["Nueva columna"] = 0
df_2
```

*Salida:*
```
Comuna  Paso            Estado  Nueva columna
0          Aisen     4  Apertura Inicial              0
1      Algarrobo     3       Preparación              0
2    Alto Biobío     2        Transición              0
3  Alto Hospicio     2        Transición              0
```

```python
#Agregar una columna 2
nueva_columna2 = [1,0,1,3]

df_2["Nueva columna2"] = df_2.Paso+1
df_2
```

*Salida:*
```
Comuna  Paso            Estado  Nueva columna  Nueva columna2
0          Aisen     4  Apertura Inicial              0               5
1      Algarrobo     3       Preparación              0               4
2    Alto Biobío     2        Transición              0               3
3  Alto Hospicio     2        Transición              0               3
```

#### Borrar filas/columnas
Para esto utilizamos la función **drop**. Para que los cambios se guarden hay que reemplazar el DataFrame existente por el que nos devuelve la función.

```python
#Borrar fila

#borrar fila 3 (indices)
df_2.drop(1)
```

*Salida:*
```
Comuna  Paso            Estado  Nueva columna  Nueva columna2
0          Aisen     4  Apertura Inicial              0               5
2    Alto Biobío     2        Transición              0               3
3  Alto Hospicio     2        Transición              0               3
```

```python
#Borrar columna

#borrar nueva columna
df_2.drop(columns=["Nueva columna"])
```

*Salida:*
```
Comuna  Paso            Estado  Nueva columna2
0          Aisen     4  Apertura Inicial               5
1      Algarrobo     3       Preparación               4
2    Alto Biobío     2        Transición               3
3  Alto Hospicio     2        Transición               3
```

#### Recorrer la tabla

```python
#Podemos recorrer la tabla utilizado un ciclo for
for i in range(len(df_2)):
  print("Fila", i , "Comuna", df_2.iloc[i,0])

for i in df_2.index:
  print("Fila", i , "Comuna", df_2.loc[i,"Comuna"])
```

*Salida:*
```
Fila 0 Comuna Aisen
Fila 1 Comuna Algarrobo
Fila 2 Comuna Alto Biobío
Fila 3 Comuna Alto Hospicio
Fila 0 Comuna Aisen
Fila 1 Comuna Algarrobo
Fila 2 Comuna Alto Biobío
Fila 3 Comuna Alto Hospicio
```

```python
df_2.Comuna
```

*Salida:*
```
0            Aisen
1        Algarrobo
2      Alto Biobío
3    Alto Hospicio
Name: Comuna, dtype: object
```

# ¿Qué podemos hacer con Pandas?
Para ver con un ejemplo mas concreto que cosas nos permite hacer Pandas vamos a utilizar una conjunto de datos llamado "The MovieLens data", que contiene información de calificaciones de películas realizadas por distintos usuarios.

[Fuente dataset](http://files.grouplens.org/datasets/movielens/ml-100k/)

## Cargar/Guardar tabla existente

**Nota:** Para cargar un archivo csv desde el computador:

```
df = pd.read_csv("/path/to/file/file.csv")
```

Más información sobre los argumentos de esta función, los pueden encontrar [aquí](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

Existen funciones para leer distintos tipos de archivos en Pandas, algunas son *read_pickle*, *read_excel*, *read_xml*.

**Nota:** Para guardar un archivo csv al computador:

```
data.to_csv("/path/to/file/file.csv")
```

Más información sobre los argumentos de esta función, los pueden encontrar [aquí](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html).

Existen funciones para guardar distintos tipos de archivos en Pandas, algunas son *to_pickle*, *to_excel*, *to_xml*.

```python
# Obtengamos los datos de los usuarios
u_cols = ['id', 'age', 'sex', 'ocupation', 'zip_code'] #Debemos indicar los nombres de las columnas, ya que no aparecen en el archivo

usuarios = pd.read_csv(
        'http://files.grouplens.org/datasets/movielens/ml-100k/u.user',
        sep='|', names = u_cols)

usuarios.head() #head me entrega las primeras n filas de la tabla, por defecto me entrega las primeras 5
```

*Salida:*
```
id  age sex   ocupation zip_code
0   1   24   M  technician    85711
1   2   53   F       other    94043
2   3   23   M      writer    32067
3   4   24   M  technician    43537
4   5   33   F       other    15213
```

```python
#Guardemos la tabla en el computador de google
usuarios.to_csv("usuarios.csv")
```

## Combinar tablas

Para reunir o combinar tablas en una sola utilizamos [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)

La tabla de usuarios no contiene la información sobre las calificaciones de las peliculas.

Para obtener la información de las calificaciones debemos cargar la tabla "data".

```python
#Cargar los datos de las calificaciones
c_cols = ['id', 'movie_id', 'calification', 'timestamp']
calificaciones = pd.read_csv(
    'http://files.grouplens.org/datasets/movielens/ml-100k/u.data',
    sep='\t', names=c_cols)

calificaciones.head()
```

*Salida:*
```
id  movie_id  calification  timestamp
0  196       242             3  881250949
1  186       302             3  891717742
2   22       377             1  878887116
3  244        51             2  880606923
4  166       346             1  886397596
```

Notamos que las calificaciones poseen un id de la pelicula y un id del usuario que realizó la calificación.

Esto significa que no podemos ver en un solo registro la información de una calificación especifica y la información del usuario que la realizó.

Para que toda la información este en una sola tabla vamos a combinar ambas. En este caso no hay problema, ya que las columnas que tienen el elemento en comun tienen el mismo nombre (en ambas el id del usuario se llama **id**)

Puedo usar **pd.merge** o usar **dataframe.merge**

```python
#Usando pd.merge
tabla = pd.merge(usuarios, calificaciones)
tabla
```

*Salida:*
```
id  age sex   ocupation zip_code  movie_id  calification  timestamp
0        1   24   M  technician    85711        61             4  878542420
1        1   24   M  technician    85711       189             3  888732928
2        1   24   M  technician    85711        33             4  878542699
3        1   24   M  technician    85711       160             4  875072547
4        1   24   M  technician    85711        20             4  887431883
...    ...  ...  ..         ...      ...       ...           ...        ...
99995  943   22   M     student    77841       415             1  888640027
99996  943   22   M     student    77841       219             4  888639575
99997  943   22   M     student    77841       796             3  888640311
99998  943   22   M     student    77841       739             4  888639929
99999  943   22   M     student    77841       391             2  888640291

[100000 rows x 8 columns]
```

```python
#Vemos que las tablas originales no cambian
```

### Tipos de merge con ejemplos simples

```python
alumnos = {
    "Nombre": ["Persona1", "Persona2", "Persona3", "Persona4", "Persona5", "Persona6"],
    "Grupo": [200, 117, 117, 150, 118, 150]

}
notas = {
    "Grupo": [203, 205, 117, 118, 150, 151],
    "Notas": [7.0, 6.1 , 6.3, 4.5, 5.6, 5.5]
}

alumnos = pd.DataFrame(alumnos)
notas = pd.DataFrame(notas)
```

```python
alumnos
```

*Salida:*
```
Nombre  Grupo
0  Persona1    200
1  Persona2    117
2  Persona3    117
3  Persona4    150
4  Persona5    118
5  Persona6    150
```

```python
notas
```

*Salida:*
```
Grupo  Notas
0    203    7.0
1    205    6.1
2    117    6.3
3    118    4.5
4    150    5.6
5    151    5.5
```

```python
#Se usa la tabla "notas" y se buscan los elementos en comun en "alumnos"
pd.merge(alumnos, notas, how="right")
```

*Salida:*
```
Nombre  Grupo  Notas
0       NaN    203    7.0
1       NaN    205    6.1
2  Persona2    117    6.3
3  Persona3    117    6.3
4  Persona5    118    4.5
5  Persona4    150    5.6
6  Persona6    150    5.6
7       NaN    151    5.5
```

```python
#Se usa la tabla "alumnos" y se buscan los elementos en comun en "notas"
pd.merge(alumnos, notas, how="left")
```

*Salida:*
```
Nombre  Grupo  Notas
0  Persona1    200    NaN
1  Persona2    117    6.3
2  Persona3    117    6.3
3  Persona4    150    5.6
4  Persona5    118    4.5
5  Persona6    150    5.6
```

```python
#Solo se agregan los elementos que esten en ambas tablas
pd.merge(alumnos, notas, how="inner") #por defecto
```

*Salida:*
```
Nombre  Grupo  Notas
0  Persona2    117    6.3
1  Persona3    117    6.3
2  Persona4    150    5.6
3  Persona5    118    4.5
4  Persona6    150    5.6
```

```python
#Se agregan todos los elementos (aunque no tengan match)
pd.merge(alumnos, notas, how="outer")
```

*Salida:*
```
Nombre  Grupo  Notas
0  Persona2    117    6.3
1  Persona3    117    6.3
2  Persona5    118    4.5
3  Persona4    150    5.6
4  Persona6    150    5.6
5       NaN    151    5.5
6  Persona1    200    NaN
7       NaN    203    7.0
8       NaN    205    6.1
```

Ahora tenemos la información del usuario y la información de la clasificación, todo en una misma tabla.

Para complementar, vamos a cargar la tabla con la información de las peliculas y la combinaremos con nuestra tabla anterior.

```python
# Cargar los datos de las películas
p_cols = ['movie_id', 'title', 'release_date']

peliculas = pd.read_csv( 'http://files.grouplens.org/datasets/movielens/ml-100k/u.item',
                     sep='|', names=p_cols, usecols=range(3), encoding='latin-1')
peliculas.head()
```

*Salida:*
```
movie_id              title release_date
0         1   Toy Story (1995)  01-Jan-1995
1         2   GoldenEye (1995)  01-Jan-1995
2         3  Four Rooms (1995)  01-Jan-1995
3         4  Get Shorty (1995)  01-Jan-1995
4         5     Copycat (1995)  01-Jan-1995
```

```python
tabla_completa = pd.merge(tabla, peliculas)
tabla_completa
```

*Salida:*
```
id  age sex   ocupation zip_code  movie_id  calification  timestamp  \
0        1   24   M  technician    85711        61             4  878542420   
1        1   24   M  technician    85711       189             3  888732928   
2        1   24   M  technician    85711        33             4  878542699   
3        1   24   M  technician    85711       160             4  875072547   
4        1   24   M  technician    85711        20             4  887431883   
...    ...  ...  ..         ...      ...       ...           ...        ...   
99995  943   22   M     student    77841       415             1  888640027   
99996  943   22   M     student    77841       219             4  888639575   
99997  943   22   M     student    77841       796             3  888640311   
99998  943   22   M     student    77841       739             4  888639929   
99999  943   22   M     student    77841       391             2  888640291   

                                   title release_date  
0             Three Colors: White (1994)  01-Jan-1994  
1                Grand Day Out, A (1992)  01-Jan-1992  
2                       Desperado (1995)  01-Jan-1995  
3             Glengarry Glen Ross (1992)  01-Jan-1992  
4              Angels and Insects (1995)  01-Jan-1995  
...                                  ...          ...  
99995    Apple Dumpling Gang, The (1975)  01-Jan-1975  
99996  Nightmare on Elm Street, A (1984)  01-Jan-1984  
99997                  Speechless (1994)  01-Jan-1994  
99998                Pretty Woman (1990)  01-Jan-1990  
99999            Last Action Hero (1993)  01-Jan-1993  

[100000 rows x 10 columns]
```

## Describir los datos

Utilizando **info()** podemos la información básica de la tabla

(Número de filas y columnas, nombre de las columnas, número de valores no nulos por columna, y también el tipo de dato que contiene cada columna)

```python
# resumen de dataframe
tabla_completa.info()
```

*Salida:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 10 columns):
 #   Column        Non-Null Count   Dtype 
---  ------        --------------   ----- 
 0   id            100000 non-null  int64 
 1   age           100000 non-null  int64 
 2   sex           100000 non-null  object
 3   ocupation     100000 non-null  object
 4   zip_code      100000 non-null  object
 5   movie_id      100000 non-null  int64 
 6   calification  100000 non-null  int64 
 7   timestamp     100000 non-null  int64 
 8   title         100000 non-null  object
 9   release_date  99991 non-null   object
dtypes: int64(5), object(5)
memory usage: 7.6+ MB
```

```python
# resumen de las columnas con valores numéricos
tabla_completa.describe()
```

*Salida:*
```
id            age       movie_id   calification     timestamp
count  100000.00000  100000.000000  100000.000000  100000.000000  1.000000e+05
mean      462.48475      32.969850     425.530130       3.529860  8.835289e+08
std       266.61442      11.562623     330.798356       1.125674  5.343856e+06
min         1.00000       7.000000       1.000000       1.000000  8.747247e+08
25%       254.00000      24.000000     175.000000       3.000000  8.794487e+08
50%       447.00000      30.000000     322.000000       4.000000  8.828269e+08
75%       682.00000      40.000000     631.000000       4.000000  8.882600e+08
max       943.00000      73.000000    1682.000000       5.000000  8.932866e+08
```

```python
#descripcion de las columnas tipo objeto (string)
tabla_completa.describe(include=object)
```

*Salida:*
```
sex ocupation zip_code             title release_date
count   100000    100000   100000            100000        99991
unique       2        21      795              1664          240
top          M   student    55414  Star Wars (1977)  01-Jan-1995
freq     74260     21957     1103               583         9932
```

## Filtrar datos

```python
# Obtener las calificaciones con un puntaje mayor a 3
tabla_completa[tabla_completa.calification > 3]
```

*Salida:*
```
id  age sex   ocupation zip_code  movie_id  calification  timestamp  \
0        1   24   M  technician    85711        61             4  878542420   
2        1   24   M  technician    85711        33             4  878542699   
3        1   24   M  technician    85711       160             4  875072547   
4        1   24   M  technician    85711        20             4  887431883   
5        1   24   M  technician    85711       202             5  875072442   
...    ...  ...  ..         ...      ...       ...           ...        ...   
99986  943   22   M     student    77841       672             5  888640125   
99992  943   22   M     student    77841       193             4  888639093   
99993  943   22   M     student    77841       470             4  888639814   
99996  943   22   M     student    77841       219             4  888639575   
99998  943   22   M     student    77841       739             4  888639929   

                                   title release_date  
0             Three Colors: White (1994)  01-Jan-1994  
2                       Desperado (1995)  01-Jan-1995  
3             Glengarry Glen Ross (1992)  01-Jan-1992  
4              Angels and Insects (1995)  01-Jan-1995  
5                   Groundhog Day (1993)  01-Jan-1993  
...                                  ...          ...  
99986                    Candyman (1992)  01-Jan-1992  
99992            Right Stuff, The (1983)  01-Jan-1983  
99993                   Tombstone (1993)  01-Jan-1993  
99996  Nightmare on Elm Street, A (1984)  01-Jan-1984  
99998                Pretty Woman (1990)  01-Jan-1990  

[55375 rows x 10 columns]
```

```python
#Obtener la tabla con personas que sean del sexo masculino o que sean mayores a 30
 #& -> y | -> o
tabla_completa[(tabla_completa.sex == "M") | (tabla_completa.age > 30) ]
```

*Salida:*
```
id  age sex   ocupation zip_code  movie_id  calification  timestamp  \
0        1   24   M  technician    85711        61             4  878542420   
1        1   24   M  technician    85711       189             3  888732928   
2        1   24   M  technician    85711        33             4  878542699   
3        1   24   M  technician    85711       160             4  875072547   
4        1   24   M  technician    85711        20             4  887431883   
...    ...  ...  ..         ...      ...       ...           ...        ...   
99995  943   22   M     student    77841       415             1  888640027   
99996  943   22   M     student    77841       219             4  888639575   
99997  943   22   M     student    77841       796             3  888640311   
99998  943   22   M     student    77841       739             4  888639929   
99999  943   22   M     student    77841       391             2  888640291   

                                   title release_date  
0             Three Colors: White (1994)  01-Jan-1994  
1                Grand Day Out, A (1992)  01-Jan-1992  
2                       Desperado (1995)  01-Jan-1995  
3             Glengarry Glen Ross (1992)  01-Jan-1992  
4              Angels and Insects (1995)  01-Jan-1995  
...                                  ...          ...  
99995    Apple Dumpling Gang, The (1975)  01-Jan-1975  
99996  Nightmare on Elm Street, A (1984)  01-Jan-1984  
99997                  Speechless (1994)  01-Jan-1994  
99998                Pretty Woman (1990)  01-Jan-1990  
99999            Last Action Hero (1993)  01-Jan-1993  

[86507 rows x 10 columns]
```

```python
# Obtener las calificaciones hechas por personas de edades de entre 30 y 40
 #& -> y | -> o
tabla_completa[(tabla_completa.age < 40) & (tabla_completa.age > 30) ]
```

*Salida:*
```
id  age sex      ocupation zip_code  movie_id  calification  \
412      5   33   F          other    15213         2             3   
413      5   33   F          other    15213        17             4   
414      5   33   F          other    15213       439             1   
415      5   33   F          other    15213       225             2   
416      5   33   F          other    15213       110             1   
...    ...  ...  ..            ...      ...       ...           ...   
99726  940   32   M  administrator    02215       238             4   
99727  940   32   M  administrator    02215       216             4   
99728  940   32   M  administrator    02215      1137             3   
99729  940   32   M  administrator    02215       215             2   
99730  940   32   M  administrator    02215       285             4   

       timestamp                                title release_date  
412    875636053                     GoldenEye (1995)  01-Jan-1995  
413    875636198           From Dusk Till Dawn (1996)  05-Feb-1996  
414    878844423  Amityville: A New Generation (1993)  01-Jan-1993  
415    875635723                101 Dalmatians (1996)  27-Nov-1996  
416    875636493          Operation Dumbo Drop (1995)  01-Jan-1995  
...          ...                                  ...          ...  
99726  885921628               Raising Arizona (1987)  01-Jan-1987  
99727  885921310       When Harry Met Sally... (1989)  01-Jan-1989  
99728  885921577               Beautiful Thing (1996)  09-Oct-1996  
99729  885921451               Field of Dreams (1989)  01-Jan-1989  
99730  885921846                Secrets & Lies (1996)  04-Oct-1996  

[21934 rows x 10 columns]
```

## Operaciones sobre los datos

```python
#Podemos renombrar las columnas
tabla_completa.rename(columns={
        'zip_code': 'Código postal',
        'title': 'Título'
    }, inplace=True)
tabla_completa.head()
```

*Salida:*
```
id  age sex   ocupation Código postal  movie_id  calification  timestamp  \
0   1   24   M  technician         85711        61             4  878542420   
1   1   24   M  technician         85711       189             3  888732928   
2   1   24   M  technician         85711        33             4  878542699   
3   1   24   M  technician         85711       160             4  875072547   
4   1   24   M  technician         85711        20             4  887431883   

                       Título release_date  
0  Three Colors: White (1994)  01-Jan-1994  
1     Grand Day Out, A (1992)  01-Jan-1992  
2            Desperado (1995)  01-Jan-1995  
3  Glengarry Glen Ross (1992)  01-Jan-1992  
4   Angels and Insects (1995)  01-Jan-1995
```

Utilizar **values** te permite acceder a los datos directamente.

Transforma los datos en un arreglo (numpy array)

```python
tabla_completa.values
```

*Salida:*
```
array([[1, 24, 'M', ..., 878542420, 'Three Colors: White (1994)',
        '01-Jan-1994'],
       [1, 24, 'M', ..., 888732928, 'Grand Day Out, A (1992)',
        '01-Jan-1992'],
       [1, 24, 'M', ..., 878542699, 'Desperado (1995)', '01-Jan-1995'],
       ...,
       [943, 22, 'M', ..., 888640311, 'Speechless (1994)', '01-Jan-1994'],
       [943, 22, 'M', ..., 888639929, 'Pretty Woman (1990)',
        '01-Jan-1990'],
       [943, 22, 'M', ..., 888640291, 'Last Action Hero (1993)',
        '01-Jan-1993']], dtype=object)
```

**Contar datos**

Veamos cuantas veces aparece cada título en la tabla. Para esto solo necesito contar los valores de la columna "Título"

```python
 #Cuento cuantas veces aparece cada titulo
tabla_completa["Título"].value_counts()
```

*Salida:*
```
Título
Star Wars (1977)                              583
Contact (1997)                                509
Fargo (1996)                                  508
Return of the Jedi (1983)                     507
Liar Liar (1997)                              485
                                             ... 
Nobody Loves Me (Keiner liebt mich) (1994)      1
Wife, The (1995)                                1
MURDER and murder (1996)                        1
Nothing Personal (1995)                         1
Ripe (1996)                                     1
Name: count, Length: 1664, dtype: int64
```

**Valores únicos**
Con **unique** obtengo los valores únicos que posee una columna, con **nunique**, cuento los valores únicos que posee una columna

```python
tabla_completa.ocupation.unique()
```

*Salida:*
```
array(['technician', 'other', 'writer', 'executive', 'administrator',
       'student', 'lawyer', 'educator', 'scientist', 'entertainment',
       'programmer', 'librarian', 'homemaker', 'artist', 'engineer',
       'marketing', 'none', 'healthcare', 'retired', 'salesman', 'doctor'],
      dtype=object)
```

```python
tabla_completa.calification.nunique()
```

*Salida:*
```
5
```

## Ordenar datos

```python
# Tambien podemos ordenar por mas de una columna, debemos hacer una lista con las columnas de interés.
tabla_completa.sort_values(by=["movie_id"])  #se ordena por "movie_id"
```

*Salida:*
```
id  age sex   ocupation Código postal  movie_id  calification  \
54525  484   27   M     student         21208         1             5   
85242  798   40   F      writer         64131         1             4   
16773  177   20   M  programmer         19104         1             3   
97020  913   27   M     student         76201         1             2   
71056  649   20   M     student         39762         1             5   
...    ...  ...  ..         ...           ...       ...           ...   
91044  863   17   M     student         60089      1678             1   
91022  863   17   M     student         60089      1679             3   
91061  863   17   M     student         60089      1680             2   
95635  896   28   M      writer         91505      1681             3   
97445  916   27   M    engineer         N2L5N      1682             3   

       timestamp                                     Título release_date  
54525  881450058                           Toy Story (1995)  01-Jan-1995  
85242  875295695                           Toy Story (1995)  01-Jan-1995  
16773  880130699                           Toy Story (1995)  01-Jan-1995  
97020  880758579                           Toy Story (1995)  01-Jan-1995  
71056  891440235                           Toy Story (1995)  01-Jan-1995  
...          ...                                        ...          ...  
91044  889289570                          Mat' i syn (1997)  06-Feb-1998  
91022  889289491                           B. Monkey (1998)  06-Feb-1998  
91061  889289570                       Sliding Doors (1998)  01-Jan-1998  
95635  887160722                        You So Crazy (1994)  01-Jan-1994  
97445  880845755  Scream of Stone (Schrei aus Stein) (1991)  08-Mar-1996  

[100000 rows x 10 columns]
```

```python
#Puedo ordenar por más de una columna. (El orden de los parámetros importa)
tabla_completa.sort_values(by=['age',"ocupation", "movie_id"]) #se ordena por 'age',"ocupation", "movie_id"
```

*Salida:*
```
id  age sex ocupation Código postal  movie_id  calification  \
3919    30    7   M   student         55436         2             3   
3914    30    7   M   student         55436         7             4   
3908    30    7   M   student         55436        28             4   
3940    30    7   M   student         55436        29             3   
3926    30    7   M   student         55436        50             3   
...    ...  ...  ..       ...           ...       ...           ...   
54384  481   73   M   retired         37771       678             3   
54376  481   73   M   retired         37771       692             4   
54374  481   73   M   retired         37771       780             1   
54379  481   73   M   retired         37771      1039             4   
54359  481   73   M   retired         37771      1089             3   

       timestamp                          Título release_date  
3919   875061066                GoldenEye (1995)  01-Jan-1995  
3914   875140648           Twelve Monkeys (1995)  01-Jan-1995  
3908   885941321                Apollo 13 (1995)  01-Jan-1995  
3940   875106638           Batman Forever (1995)  01-Jan-1995  
3926   875061066                Star Wars (1977)  01-Jan-1977  
...          ...                             ...          ...  
54384  885828016                  Volcano (1997)  25-Apr-1997  
54376  885828339  American President, The (1995)  01-Jan-1995  
54374  885829240            Dumb & Dumber (1994)  01-Jan-1994  
54379  885828732                   Hamlet (1996)  24-Jan-1997  
54359  885828072  Speed 2: Cruise Control (1997)  13-Jun-1997  

[100000 rows x 10 columns]
```

```python
"s" > "S"
```

*Salida:*
```
True
```

```python
#cambiamos el orden
 #se ordena por 'movie_id',"age", "ocupation"
```

## Groupby
Me permite agrupar por valores de las columnas indicadas.
Cuando se utiliza groupby el resultado ya no es del tipo DataFrame y para que se muestre como una tabla se le debe aplicar alguna operación matemática.

promedio --> **mean()**

contar --> **count()**

sumar --> **sum**

minimo --> **min()**

máximo --> **max()**

```python
tabla_completa.info()
```

*Salida:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 10 columns):
 #   Column         Non-Null Count   Dtype 
---  ------         --------------   ----- 
 0   id             100000 non-null  int64 
 1   age            100000 non-null  int64 
 2   sex            100000 non-null  object
 3   ocupation      100000 non-null  object
 4   Código postal  100000 non-null  object
 5   movie_id       100000 non-null  int64 
 6   calification   100000 non-null  int64 
 7   timestamp      100000 non-null  int64 
 8   Título         100000 non-null  object
 9   release_date   99991 non-null   object
dtypes: int64(5), object(5)
memory usage: 7.6+ MB
```

```python
tabla_completa[["id", "age", "ocupation", "calification"]].groupby("ocupation").mean()
```

*Salida:*
```
id        age  calification
ocupation                                         
administrator  378.662121  39.123145      3.635646
artist         492.750867  30.592288      3.653380
doctor         392.690741  35.592593      3.688889
educator       417.871849  42.789240      3.670621
engineer       491.199755  34.356086      3.541407
entertainment  312.376134  28.766110      3.441050
executive      413.830444  36.614164      3.349104
healthcare     497.511769  38.885164      2.896220
homemaker      505.127090  32.371237      3.301003
lawyer         423.230483  34.556134      3.735316
librarian      456.375687  37.358050      3.560781
marketing      420.097436  36.478462      3.485641
none           269.057714  25.007769      3.779134
other          530.628060  32.568977      3.552377
programmer     454.298039  32.500064      3.568260
retired        380.566190  61.755749      3.466750
salesman       475.370327  33.470794      3.582944
scientist      503.550049  35.343052      3.611273
student        490.843011  22.142870      3.515143
technician     475.596406  31.712493      3.532230
writer         498.096098  34.325867      3.375723
```

```python
#Agrupamos por ocupacion y aplicamos la operacion para obtener el promedio ("ocupation")
lista_medias_calif = tabla_completa[["id", "age", "ocupation", "calification"]].groupby("ocupation").mean()["calification"]
lista_medias_calif
```

*Salida:*
```
ocupation
administrator    3.635646
artist           3.653380
doctor           3.688889
educator         3.670621
engineer         3.541407
entertainment    3.441050
executive        3.349104
healthcare       2.896220
homemaker        3.301003
lawyer           3.735316
librarian        3.560781
marketing        3.485641
none             3.779134
other            3.552377
programmer       3.568260
retired          3.466750
salesman         3.582944
scientist        3.611273
student          3.515143
technician       3.532230
writer           3.375723
Name: calification, dtype: float64
```

Podemos obtener la calificacion promedio por ocupación

```python
print('Calificacion máxima: ', lista_medias_calif.max())
print('Indice(numero) calificación máxima: ', lista_medias_calif.argmax())
print('Ocupación con calificacion máxima: ', lista_medias_calif.idxmax())
```

*Salida:*
```
Calificacion máxima:  3.779134295227525
Indice(numero) calificación máxima:  12
Ocupación con calificacion máxima:  none
```

Cuando utilizas groupby, las columnas por las que agrupas se transforman en los indices de la tabla resultante.

```python
#Obtengamos las calificaciones promedio agrupando por edad y ocupación ( "age", "ocupation" )
a = tabla_completa[["id", "age", "ocupation", "calification"]].groupby(["age", "ocupation"]).mean()
a
```

*Salida:*
```
id  calification
age ocupation                         
7   student         30.0      3.767442
10  student        471.0      3.387097
11  none           289.0      2.925926
13  none           628.0      4.703704
    other          142.0      3.636364
...                  ...           ...
69  librarian      585.0      3.737500
70  administrator  803.0      3.090909
    engineer       767.0      4.432432
    retired        860.0      3.239437
73  retired        481.0      3.982143

[429 rows x 2 columns]
```

```python
a.reset_index()
```

*Salida:*
```
age      ocupation     id  calification
0      7        student   30.0      3.767442
1     10        student  471.0      3.387097
2     11           none  289.0      2.925926
3     13           none  628.0      4.703704
4     13          other  142.0      3.636364
..   ...            ...    ...           ...
424   69      librarian  585.0      3.737500
425   70  administrator  803.0      3.090909
426   70       engineer  767.0      4.432432
427   70        retired  860.0      3.239437
428   73        retired  481.0      3.982143

[429 rows x 4 columns]
```

[**Lista completa de atributos, operaciones y funciones en DataFrames**](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

#Ejercicios 1

Considerando un dataframe de juguete llamado data

## 1.1

Crear un dataframe (llamarlo data) a partir del diccionario entregado llamado publicaciones. Especificar index="id"

```python
publicaciones = {
    "id": [1, 2, 3, 5, 7, 6, 4, 8, 9, 10],
    "usuario": [1, 2, 3, 3, 2, 2, 4, 2, 5, 1],
    "Likes": [8222526, 1486, 3410224, 1347715, 50186, 822, 7812601,79955,2525, 12724254],
    "Comentarios": [0, 43, 46764, 10811, 792, 1,0, 327, 34, 1]
}
```

```python
data = pd.DataFrame(publicaciones)
data
```

*Salida:*
```
id  usuario     Likes  Comentarios
0   1        1   8222526            0
1   2        2      1486           43
2   3        3   3410224        46764
3   5        3   1347715        10811
4   7        2     50186          792
5   6        2       822            1
6   4        4   7812601            0
7   8        2     79955          327
8   9        5      2525           34
9  10        1  12724254            1
```

```python
data = data.set_index("id")
```

```python
data
```

*Salida:*
```
usuario     Likes  Comentarios
id                                
1         1   8222526            0
2         2      1486           43
3         3   3410224        46764
5         3   1347715        10811
7         2     50186          792
6         2       822            1
4         4   7812601            0
8         2     79955          327
9         5      2525           34
10        1  12724254            1
```

## 1.2
Eliminar la primera fila de data

```python
data.drop(1)
```

*Salida:*
```
usuario     Likes  Comentarios
id                                
2         2      1486           43
3         3   3410224        46764
5         3   1347715        10811
7         2     50186          792
6         2       822            1
4         4   7812601            0
8         2     79955          327
9         5      2525           34
10        1  12724254            1
```

## 1.3
Obtener una subtabla con las publicaciones que tengan 40 comentarios o más

```python
subdata = data[data.Comentarios > 40]
```

## 1.4

Modificar data de manera que las fila con mas de 50000 likes tengan 0 comentarios

```python
for i in range(len(data)):
  if data.iloc[i,1] > 50000:
    data.iloc[i,2] = 0
```

```python
data
```

*Salida:*
```
usuario     Likes  Comentarios
id                                
1         1   8222526            0
2         2      1486           43
3         3   3410224            0
5         3   1347715            0
7         2     50186            0
6         2       822            1
4         4   7812601            0
8         2     79955            0
9         5      2525           34
10        1  12724254            0
```

```python
#alternativa mas rapida
data.loc[data["Likes"] > 50000, "Comentarios"] = 0
data
```

*Salida:*
```
usuario     Likes  Comentarios
id                                
1         1   8222526            0
2         2      1486           43
3         3   3410224            0
5         3   1347715            0
7         2     50186            0
6         2       822            1
4         4   7812601            0
8         2     79955            0
9         5      2525           34
10        1  12724254            0
```

# Ejercicios 2
Ocupando el dataframe llamado "tabla_completa"

## 2.1

Muestre la calificación promedio

```python
tabla_completa.calification.mean()
```

*Salida:*
```
np.float64(3.52986)
```

## 2.2

Muestre cuantas peliculas hay en la tabla.

```python
len(tabla_completa.movie_id.unique())
```

*Salida:*
```
1682
```

## 2.3
Cuente cuantas calificaciones existen que hayan sido emitidas por personas entre 18 y 25 años (inclusivo) y cuyo puntaje sea menor a 3

```python
tabla_completa[(tabla_completa.calification<3)&((tabla_completa.age<=25)&(tabla_completa.age>=18))]
```

*Salida:*
```
id  age sex   ocupation Código postal  movie_id  calification  \
8        1   24   M  technician         85711       155             2   
20       1   24   M  technician         85711       266             1   
24       1   24   M  technician         85711        74             1   
34       1   24   M  technician         85711        27             2   
35       1   24   M  technician         85711       260             1   
...    ...  ...  ..         ...           ...       ...           ...   
99982  943   22   M     student         77841       168             2   
99990  943   22   M     student         77841       139             1   
99994  943   22   M     student         77841      1047             2   
99995  943   22   M     student         77841       415             1   
99999  943   22   M     student         77841       391             2   

       timestamp                                  Título release_date  
8      878542201                    Dirty Dancing (1987)  01-Jan-1987  
20     885345728               Kull the Conqueror (1997)  29-Aug-1997  
24     889751736     Faster Pussycat! Kill! Kill! (1965)  01-Jan-1965  
34     876892946                         Bad Boys (1995)  01-Jan-1995  
35     875071713                    Event Horizon (1997)  01-Jan-1997  
...          ...                                     ...          ...  
99982  888638897  Monty Python and the Holy Grail (1974)  01-Jan-1974  
99990  888640027                    Love Bug, The (1969)  01-Jan-1969  
99994  875502146                     Multiplicity (1996)  12-Jul-1996  
99995  888640027         Apple Dumpling Gang, The (1975)  01-Jan-1975  
99999  888640291                 Last Action Hero (1993)  01-Jan-1993  

[5433 rows x 10 columns]
```

## 2.4
Entregue los nombres de las peliculas que han sido calificadas por usuarios ingenieros ("engineer") (sin repetir)

```python
tabla_completa[tabla_completa.ocupation == "engineer"]["Título"].unique()
```

*Salida:*
```
array(['Return of the Jedi (1983)',
       "One Flew Over the Cuckoo's Nest (1975)",
       'Star Trek: First Contact (1996)', ..., 'Waiting to Exhale (1995)',
       'Daytrippers, The (1996)', 'Top Hat (1935)'], dtype=object)
```

## 2.5
Entregue los id de los 10 usuarios con mas calificaciones emitidas

```python
tabla_completa.groupby("id").count().sort_values(by=["calification"]).tail(10).index
```

*Salida:*
```
Index([393, 234, 303, 537, 416, 276, 450, 13, 655, 405], dtype='int64', name='id')
```

## 2.6
Mostrar la calificación mas baja de cada pelicula.

```python
tabla_completa.groupby("Título").min()["calification"]
```

*Salida:*
```
Título
'Til There Was You (1997)                1
1-900 (1994)                             1
101 Dalmatians (1996)                    1
12 Angry Men (1957)                      2
187 (1997)                               1
                                        ..
Young Guns II (1990)                     1
Young Poisoner's Handbook, The (1995)    1
Zeus and Roxanne (1997)                  1
unknown                                  1
Á köldum klaka (Cold Fever) (1994)       3
Name: calification, Length: 1664, dtype: int64
```
