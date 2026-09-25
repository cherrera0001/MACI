# 2026_P2_Calidad_de_Datos_res

> Material practico de Fundamentos de Ciencia de Datos, UdeC T2-2026.

> Convertido desde `2026_[P2]Calidad_de_Datos(res).ipynb` para indexacion.

# [Práctica 2] Fundamentos de Ciencia de Datos
Alejandra Fernández (afernandezm@inf.udec.cl)

# Contenidos

## Calidad de Datos
Hay veces en que los datos pueden estar incompletos, ruidosos e inconsistentes.

- Duplicados
- Valores fuera de rango (ej: tener valores negativos)
- Valores Faltantes
- Símbolos extraños o valores NULL
- Datos no útiles

Cosas que dificultan el análisis de los datos:
- Indices repetidos
- Indices poco significativos
- Columnas con tipo de dato incorrecto

# Creemos una tabla de ejemplo

Crearemos una tabla (de juguete) que presente los problemas antes mencionados

```python
# importamos las librerías, le damos un seudonimo a las librerias para mejorar
# legibilidad en el código.
import numpy as np
import pandas as pd
from IPython.display import display #Para mostrar la tabla de pandas (No es necesario)
```

```python
columnas = ["_id", "CODIGO", "ENTIDAD", "CALLE", "NUM", "ADICIONAL", "COMUNA", "DIA_INICIO", "DIA_FIN", "HORA_INICIO", "HORA_FIN",
            "CARGA_MAXIMA", "CARGA_MINIMA", "ESTE", "NORTE", "LONGITUD", "LATITUD"]
datos_ej = [[1,"52","FULLCARGA","AV. independencia", "3187", "B","CONCHALI","Lun", "Sab", "08:00", "21:00", "$30.000", 40000, "","6303385","-70.669021","-33.397985"],
            [2,"57","FULLCARGA","mapocho", "4190", "", "QUINTA NORMAL","Lun", "Sab", "08:00", "21:00", "$100.000$", 0, "342767", "","-70.691895","-33.431889"],
            [3,"62","FULLCARGA","PARQUE CENTRAL PONIENTE", "1075", "", "MAIPU","Lun", "Sab", "08:00", "21:00", "$50.000", -5.000, "","6285119","-70.787010","-33.561005"],
            [4,"63","FULLCARGA","AV. GRECIA", "8585", "","PEÑALOLEN","Lun", "Sab", "08:30", "21:00", "$10.000", 4000, "","6294827","-70.544136","-33.476723"],
            [16,"100","FULLCARGA","EL CHAMPION", "1401", "","MAIPU","Lun" , "Sab", "08:00", "21:00", "$100.000", 1000,"335113","6290965","-70.775787","-33.508446"],
            [17,"102","FULLCARGA","Alameda", "3170", "","ESTACION CENTRAL","Lun", "Vie", "05:30", "23:00", "$100.000", 1000, "","6297358","-70.679611","-33.452133"],
            [18,"103","FULLCARGA","ALAMEDA", "3171", "","Estacion central","Lun", "Vie", "05:30", "23:00", "$100.000", 1000, "","6297358","-70.679611","-33.452133"],
            [5,"65","FULLCARGA","estado", "383", "", "SANTIAGO ","Lun", "Sab", "08:00", "21:00", "$6.000", -500, "","6298908","-70.649521","-33.438568"],
            [6,"69","FULLCARGA","BERNARDO O´HIGGINS", "309", "", "QUILICURA\t","Lun", "Sab", "08:00", "21:00", "$25.000", 300, "","6307883","-70.729274","-33.356530"],
            [7,"72","FULLCARGA","AV. WALKER MARTINEZ", "1786", "8A","LA FLORIDA","Lun", "Sab", "08:00", "21:00", "1.000", 10, "","6289782","-70.579819","-33.521778"],
            [8,"73","FULLCARGA","AV. SANTA ROSA", "8035", "A","SAN RAMON","Lun", "Sab", "08:00", "21:00", "$5.000", 10,"348227", "","-70.635071","-33.533241"],
            [9,"75","FULLCARGA","av. central", "6577", "","LO ESPEJO ","Lun", "Sab", "08:00", "21:00", "$10.000", 100, "342908", "","-70.691878","-33.505539"],
            [10,"80","FULLCARGA","av. ZAPADORES", "0216", "","  RECOLETA","Lun", "Sab", "08:00", "21:00", "$-1.000", -100,"348630","6303645","-70.628166","-33.396126"],
            [11,"81","FULLCARGA","av. PROVIDENCIA", "2382", "","PROVIDENCIA","Lun", "Sab", "08:00", "21:00", "$100.000", 1000, "","6301067","-70.606323","-33.419662"],
            [12,"84","FULLCARGA","AV. SANTA RAQUEL", "9685", "","LAFLORIDA","Lun", "Sab", "08:00", "21:00", "$100.000", -1000, "","6287359","-70.603798","-33.543312"],
            [13,"86","FULLCARGA","NONATO COO", "3392", "","PUENTE ALTO","Lunes", "Sab", "08:00", "21:00", "$100.000", 1000, "","6283725","-70.570412","-33.576515"],
            [14,"96","FULLCARGA","AV. LOS TOROS", "5441", "","Puente Alto","Lun", "Dom", "09:00", "22:00", "$50.000", 300, "","6284774","-70.557426","-33.567219"],
            [15,"99","FULLCARGA","SAN LUIS", "18", "","QUILICURA","Lun", "Sab", "08:00", "21:00", "$100.000", 1000, "","6306748","-70.738235","-33.366653"],
            [16,"100","FULLCARGA","EL CHAMPION", "1401", "","MAIPU","Lunes" , "Sab", "08:00", "21:00", "$100.000", 1000,"335113","6290965","-70.775787","-33.508446"],
            [17,"102","FULLCARGA","Alameda", "3170", "","ESTACION CENTRAL","Lunes", "Viernes", "05:30", "23:00", "$100.000", 1000, "","6297358","-70.679611","-33.452133"],
            [18,"103","FULLCARGA","ALAMEDA", "3171", "","Estacion central","Lun", "Vie", "05:30", "23:00", "$100.000", 1000, "","6297358","-70.679611","-33.452133"],
            [20,"105","FULLCARGA","LUCILA GODOY", "2766", "(APROX)","LO ESPEJO","Lun", "Vie", "05:30", "23:00", "$100.000", 1000,"343430","6290439","-70.685795","-33.514151"],
            [14,"96","FULLCARGA","AV. LOS TOROS", "5441", "","Puente Alto","Lunes", "Domingo", "09:00", "22:00", "$50.000", 300, "","6284774","-70.557426","-33.567219"],
            [15,"99","FULLCARGA","SAN LUIS", "18", "","QUILICURA","Lun", "Sab", "08:00", "21:00", "$100.000", 1000, "","6306748","-70.738235","-33.366653"]]
```

```python
ejemplo = pd.DataFrame(datos_ej, columns=columnas)
```

```python
ejemplo.head()
```

*Salida:*
```
_id CODIGO    ENTIDAD                    CALLE   NUM ADICIONAL  \
0    1     52  FULLCARGA        AV. independencia  3187         B   
1    2     57  FULLCARGA                  mapocho  4190             
2    3     62  FULLCARGA  PARQUE CENTRAL PONIENTE  1075             
3    4     63  FULLCARGA               AV. GRECIA  8585             
4   16    100  FULLCARGA              EL CHAMPION  1401             

          COMUNA DIA_INICIO DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  \
0       CONCHALI        Lun     Sab       08:00    21:00      $30.000   
1  QUINTA NORMAL        Lun     Sab       08:00    21:00    $100.000$   
2          MAIPU        Lun     Sab       08:00    21:00      $50.000   
3      PEÑALOLEN        Lun     Sab       08:30    21:00      $10.000   
4          MAIPU        Lun     Sab       08:00    21:00     $100.000   

   CARGA_MINIMA    ESTE    NORTE    LONGITUD     LATITUD  
0       40000.0          6303385  -70.669021  -33.397985  
1           0.0  342767           -70.691895  -33.431889  
2          -5.0          6285119  -70.787010  -33.561005  
3        4000.0          6294827  -70.544136  -33.476723  
4        1000.0  335113  6290965  -70.775787  -33.508446
```

```python
ejemplo.info()
```

*Salida:*
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 24 entries, 0 to 23
Data columns (total 17 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   _id           24 non-null     int64  
 1   CODIGO        24 non-null     object 
 2   ENTIDAD       24 non-null     object 
 3   CALLE         24 non-null     object 
 4   NUM           24 non-null     object 
 5   ADICIONAL     24 non-null     object 
 6   COMUNA        24 non-null     object 
 7   DIA_INICIO    24 non-null     object 
 8   DIA_FIN       24 non-null     object 
 9   HORA_INICIO   24 non-null     object 
 10  HORA_FIN      24 non-null     object 
 11  CARGA_MAXIMA  24 non-null     object 
 12  CARGA_MINIMA  24 non-null     float64
 13  ESTE          24 non-null     object 
 14  NORTE         24 non-null     object 
 15  LONGITUD      24 non-null     object 
 16  LATITUD       24 non-null     object 
dtypes: float64(1), int64(1), object(15)
memory usage: 3.3+ KB
```

```python
ejemplo.describe(include="all")
```

*Salida:*
```
_id CODIGO    ENTIDAD    CALLE   NUM ADICIONAL COMUNA  \
count   24.000000     24         24       24    24        24     24   
unique        NaN     19          1       19    19         5     18   
top           NaN    103  FULLCARGA  ALAMEDA  3171            MAIPU   
freq          NaN      2         24        2     2        20      3   
mean    11.291667    NaN        NaN      NaN   NaN       NaN    NaN   
std      5.668212    NaN        NaN      NaN   NaN       NaN    NaN   
min      1.000000    NaN        NaN      NaN   NaN       NaN    NaN   
25%      6.750000    NaN        NaN      NaN   NaN       NaN    NaN   
50%     12.500000    NaN        NaN      NaN   NaN       NaN    NaN   
75%     16.000000    NaN        NaN      NaN   NaN       NaN    NaN   
max     20.000000    NaN        NaN      NaN   NaN       NaN    NaN   

       DIA_INICIO DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA  \
count          24      24          24       24           24     24.000000   
unique          2       5           4        3           10           NaN   
top           Lun     Sab       08:00    21:00     $100.000           NaN   
freq           20      17          16       17           12           NaN   
mean          NaN     NaN         NaN      NaN          NaN   2267.291667   
std           NaN     NaN         NaN      NaN          NaN   8089.621770   
min           NaN     NaN         NaN      NaN          NaN  -1000.000000   
25%           NaN     NaN         NaN      NaN          NaN     10.000000   
50%           NaN     NaN         NaN      NaN          NaN   1000.000000   
75%           NaN     NaN         NaN      NaN          NaN   1000.000000   
max           NaN     NaN         NaN      NaN          NaN  40000.000000   

       ESTE    NORTE    LONGITUD     LATITUD  
count    24       24          24          24  
unique    7       16          18          18  
top          6297358  -70.679611  -33.452133  
freq     17        4           4           4  
m
... (salida truncada)
```

# Duplicados

Para revisar si una tabla contiene filas duplicadas podemos utilizar la función **duplicated()**

Para eliminar los duplicados utilizamos la función **drop_duplicates()**

```python
ejemplo[ejemplo.duplicated()]
```

*Salida:*
```
_id CODIGO    ENTIDAD     CALLE   NUM ADICIONAL            COMUNA  \
20   18    103  FULLCARGA   ALAMEDA  3171            Estacion central   
23   15     99  FULLCARGA  SAN LUIS    18                   QUILICURA   

   DIA_INICIO DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA ESTE  \
20        Lun     Vie       05:30    23:00     $100.000        1000.0        
23        Lun     Sab       08:00    21:00     $100.000        1000.0        

      NORTE    LONGITUD     LATITUD  
20  6297358  -70.679611  -33.452133  
23  6306748  -70.738235  -33.366653
```

Puede pasar que yo no necesite tener duplicados de una columna especifica, en este caso tenemos el id de cada punto de recarga.

```python
#Para ver los duplicados, podemos pedir que revise los duplicados de una columna especifica, en este caso usaremos el nombre
ejemplo[ejemplo._id.duplicated()]
```

*Salida:*
```
_id CODIGO    ENTIDAD          CALLE   NUM ADICIONAL            COMUNA  \
18   16    100  FULLCARGA    EL CHAMPION  1401                       MAIPU   
19   17    102  FULLCARGA        Alameda  3170            ESTACION CENTRAL   
20   18    103  FULLCARGA        ALAMEDA  3171            Estacion central   
22   14     96  FULLCARGA  AV. LOS TOROS  5441                 Puente Alto   
23   15     99  FULLCARGA       SAN LUIS    18                   QUILICURA   

   DIA_INICIO  DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA  \
18      Lunes      Sab       08:00    21:00     $100.000        1000.0   
19      Lunes  Viernes       05:30    23:00     $100.000        1000.0   
20        Lun      Vie       05:30    23:00     $100.000        1000.0   
22      Lunes  Domingo       09:00    22:00      $50.000         300.0   
23        Lun      Sab       08:00    21:00     $100.000        1000.0   

      ESTE    NORTE    LONGITUD     LATITUD  
18  335113  6290965  -70.775787  -33.508446  
19          6297358  -70.679611  -33.452133  
20          6297358  -70.679611  -33.452133  
22          6284774  -70.557426  -33.567219  
23          6306748  -70.738235  -33.366653
```

```python
ejemplo2 = ejemplo.set_index("_id")
```

### Tener indices duplicados

Me quiero detener en esta parte para hablar de indices duplicados.

La tabla "ejemplo2" tiene indices duplicados, siendo el primero el pokemon el registro con indice 14

```python
#Accedamos a la fila con indice 15
ejemplo2.loc[14]
```

*Salida:*
```
CODIGO    ENTIDAD          CALLE   NUM ADICIONAL       COMUNA DIA_INICIO  \
_id                                                                            
14      96  FULLCARGA  AV. LOS TOROS  5441            Puente Alto        Lun   
14      96  FULLCARGA  AV. LOS TOROS  5441            Puente Alto      Lunes   

     DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA ESTE    NORTE  \
_id                                                                          
14       Dom       09:00    22:00      $50.000         300.0       6284774   
14   Domingo       09:00    22:00      $50.000         300.0       6284774   

       LONGITUD     LATITUD  
_id                          
14   -70.557426  -33.567219  
14   -70.557426  -33.567219
```

Veemos que esto nos retorna 2 filas que en este caso son el mismo registro, pero puede pasar cuando estemos concatenando tablas que los indices se repitan y que las filas NO SEAN lo mismo.

Para corregir esto se puede cambiar la columna de indice por una ya existente que no tenga datos repetidos (Por ejemplo, si tuvieramos una tabla con datos de personas, el indice podria ser el rut) En este caso un buen candidato es el pokedex_number, ya que cada pokemon tiene asignado un número.

Para esto se usa la función **set_index()** de la forma

` data.set_index(nombre_columna)`

También se puede utilizar la función **reset_index()** para hacer que los indices se reinicien y que cada fila tenga indices unicos.

```python
ejemplo2.reset_index(inplace=True)
ejemplo2
```

*Salida:*
```
_id CODIGO    ENTIDAD                    CALLE   NUM ADICIONAL  \
0     1     52  FULLCARGA        AV. independencia  3187         B   
1     2     57  FULLCARGA                  mapocho  4190             
2     3     62  FULLCARGA  PARQUE CENTRAL PONIENTE  1075             
3     4     63  FULLCARGA               AV. GRECIA  8585             
4    16    100  FULLCARGA              EL CHAMPION  1401             
5    17    102  FULLCARGA                  Alameda  3170             
6    18    103  FULLCARGA                  ALAMEDA  3171             
7     5     65  FULLCARGA                   estado   383             
8     6     69  FULLCARGA       BERNARDO O´HIGGINS   309             
9     7     72  FULLCARGA      AV. WALKER MARTINEZ  1786        8A   
10    8     73  FULLCARGA           AV. SANTA ROSA  8035         A   
11    9     75  FULLCARGA              av. central  6577             
12   10     80  FULLCARGA            av. ZAPADORES  0216             
13   11     81  FULLCARGA          av. PROVIDENCIA  2382             
14   12     84  FULLCARGA         AV. SANTA RAQUEL  9685             
15   13     86  FULLCARGA               NONATO COO  3392             
16   14     96  FULLCARGA            AV. LOS TOROS  5441             
17   15     99  FULLCARGA                 SAN LUIS    18             
18   16    100  FULLCARGA              EL CHAMPION  1401             
19   17    102  FULLCARGA                  Alameda  3170             
20   18    103  FULLCARGA                  ALAMEDA  3171             
21   20    105  FULLCARGA             LUCILA GODOY  2766   (APROX)   
22   14     96  FULLCARGA            AV. LOS TOROS  5441             
23   15     99  FULLCARGA                 SAN LUIS    18             

              COMUNA DIA_INICIO  DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  \
0           CONCHALI        Lun      Sab       08:00    21:00      $30.000   
1      QUINTA NORMAL        Lun      Sab       08:00    21:00    $100.000$   
2              MAIP
... (salida truncada)
```

## Eliminando las filas duplicadas
Utilizando el drop_duplicates sin argumentos, se eliminan las filas que sean exactamente iguales en todas las columnas (sin contar el indice)

```python
ejemplo.drop_duplicates()
```

*Salida:*
```
_id CODIGO    ENTIDAD                    CALLE   NUM ADICIONAL  \
0     1     52  FULLCARGA        AV. independencia  3187         B   
1     2     57  FULLCARGA                  mapocho  4190             
2     3     62  FULLCARGA  PARQUE CENTRAL PONIENTE  1075             
3     4     63  FULLCARGA               AV. GRECIA  8585             
4    16    100  FULLCARGA              EL CHAMPION  1401             
5    17    102  FULLCARGA                  Alameda  3170             
6    18    103  FULLCARGA                  ALAMEDA  3171             
7     5     65  FULLCARGA                   estado   383             
8     6     69  FULLCARGA       BERNARDO O´HIGGINS   309             
9     7     72  FULLCARGA      AV. WALKER MARTINEZ  1786        8A   
10    8     73  FULLCARGA           AV. SANTA ROSA  8035         A   
11    9     75  FULLCARGA              av. central  6577             
12   10     80  FULLCARGA            av. ZAPADORES  0216             
13   11     81  FULLCARGA          av. PROVIDENCIA  2382             
14   12     84  FULLCARGA         AV. SANTA RAQUEL  9685             
15   13     86  FULLCARGA               NONATO COO  3392             
16   14     96  FULLCARGA            AV. LOS TOROS  5441             
17   15     99  FULLCARGA                 SAN LUIS    18             
18   16    100  FULLCARGA              EL CHAMPION  1401             
19   17    102  FULLCARGA                  Alameda  3170             
21   20    105  FULLCARGA             LUCILA GODOY  2766   (APROX)   
22   14     96  FULLCARGA            AV. LOS TOROS  5441             

              COMUNA DIA_INICIO  DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  \
0           CONCHALI        Lun      Sab       08:00    21:00      $30.000   
1      QUINTA NORMAL        Lun      Sab       08:00    21:00    $100.000$   
2              MAIPU        Lun      Sab       08:00    21:00      $50.000   
3          PEÑALOLEN        Lun      Sab       08:30    21:00      $10.000   
4  
... (salida truncada)
```

Siguiendo con la tabla original, podemos eliminar los registros que tengan el "_id" duplicado y luego asignar esta columna como indice o eliminarla según se requiera.

```python
ejemplo = ejemplo.drop_duplicates(subset=['_id'])
```

Ahora podemos revisar los duplicados de la tabla y comprobar que no hay

```python
ejemplo[ejemplo._id.duplicated()]
```

*Salida:*
```
Empty DataFrame
Columns: [_id, CODIGO, ENTIDAD, CALLE, NUM, ADICIONAL, COMUNA, DIA_INICIO, DIA_FIN, HORA_INICIO, HORA_FIN, CARGA_MAXIMA, CARGA_MINIMA, ESTE, NORTE, LONGITUD, LATITUD]
Index: []
```

# Valores fuera de rango

Para valores númericos esto es facil, simplemente podemos revisar los valores minimos y maximos por columna

Valores fuera de rango puede ser:
- Edades negativas
- Alturas, diámetros, áreas (mediciones) negativas
- Valores imposibles

```python
#CARGA_MINIMA es la única columna númerica
print(ejemplo.CARGA_MINIMA.min(), ejemplo.CARGA_MINIMA.max())
```

*Salida:*
```
-1000.0 40000.0
```

Para ver todas las columnas numericas podemos usar describe

```python
ejemplo.describe()
```

*Salida:*
```
_id  CARGA_MINIMA
count  19.000000     19.000000
mean   10.052632   2637.631579
std     5.720079   9105.142986
min     1.000000  -1000.000000
25%     5.500000      5.000000
50%    10.000000    300.000000
75%    14.500000   1000.000000
max    20.000000  40000.000000
```

Vemos que ciertos valores en CARGA_MINIMA son negativos, cosa que no puede ser.
Aquí se debe tomar una decisión para ver que hacer con estos valores erroneos:


*   Se cambia por algún valor ya registrado o que represente la centralidad (media, mediana)
*   Se elimina el registro
*   Se cambia por el mínimo permitido
*   Otro

```python
#En este caso simplemente asumiremos que es un error de tipeo y que el valor correcto es el valor absoluto
ejemplo.CARGA_MINIMA = ejemplo.CARGA_MINIMA.abs()
```

```python
#Alternativa
ejemplo.loc[ejemplo["CARGA_MINIMA"]<0, "CARGA_MINIMA"] = ejemplo.loc[ejemplo["CARGA_MINIMA"]<0, "CARGA_MINIMA"] *-1
```

```python
#Otra alternativa
ejemplo.CARGA_MINIMA = ejemplo.CARGA_MINIMA.apply(lambda x: -1*x if x<0 else x)
```

```python
#Otra otra alternativa
ejemplo.CARGA_MINIMA = np.where(ejemplo.CARGA_MINIMA<0, ejemplo.CARGA_MINIMA<0 *-1, ejemplo.CARGA_MINIMA)
```

# Valores faltantes
Cuando se omite un valor este se transforma en un "NaN".

Para ver que columnas de datos presentan nulos podemos utilizar el info() o la función **isna()**

```python
ejemplo.info()
```

*Salida:*
```
<class 'pandas.core.frame.DataFrame'>
Index: 19 entries, 0 to 21
Data columns (total 17 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   _id           19 non-null     int64  
 1   CODIGO        19 non-null     object 
 2   ENTIDAD       19 non-null     object 
 3   CALLE         19 non-null     object 
 4   NUM           19 non-null     object 
 5   ADICIONAL     19 non-null     object 
 6   COMUNA        19 non-null     object 
 7   DIA_INICIO    19 non-null     object 
 8   DIA_FIN       19 non-null     object 
 9   HORA_INICIO   19 non-null     object 
 10  HORA_FIN      19 non-null     object 
 11  CARGA_MAXIMA  19 non-null     object 
 12  CARGA_MINIMA  19 non-null     float64
 13  ESTE          19 non-null     object 
 14  NORTE         19 non-null     object 
 15  LONGITUD      19 non-null     object 
 16  LATITUD       19 non-null     object 
dtypes: float64(1), int64(1), object(15)
memory usage: 2.7+ KB
```

```python
ejemplo.isna().sum()
```

*Salida:*
```
_id             0
CODIGO          0
ENTIDAD         0
CALLE           0
NUM             0
ADICIONAL       0
COMUNA          0
DIA_INICIO      0
DIA_FIN         0
HORA_INICIO     0
HORA_FIN        0
CARGA_MAXIMA    0
CARGA_MINIMA    0
ESTE            0
NORTE           0
LONGITUD        0
LATITUD         0
dtype: int64
```

Lo que pasa es que muchos valores "nan" se han puesto como un espacio en blanco en las celdas, entonces aqui utilizaremos la función "replace" para reemplazar esos valores de la tabla con nans

```python
ejemplo = ejemplo.replace(r"^\s*$", np.nan, regex=True) #regex True porque le pasamos una expresión regular
```

```python
ejemplo.info()
```

*Salida:*
```
<class 'pandas.core.frame.DataFrame'>
Index: 19 entries, 0 to 21
Data columns (total 17 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   _id           19 non-null     int64  
 1   CODIGO        19 non-null     object 
 2   ENTIDAD       19 non-null     object 
 3   CALLE         19 non-null     object 
 4   NUM           19 non-null     object 
 5   ADICIONAL     4 non-null      object 
 6   COMUNA        19 non-null     object 
 7   DIA_INICIO    19 non-null     object 
 8   DIA_FIN       19 non-null     object 
 9   HORA_INICIO   19 non-null     object 
 10  HORA_FIN      19 non-null     object 
 11  CARGA_MAXIMA  19 non-null     object 
 12  CARGA_MINIMA  19 non-null     float64
 13  ESTE          6 non-null      object 
 14  NORTE         16 non-null     object 
 15  LONGITUD      19 non-null     object 
 16  LATITUD       19 non-null     object 
dtypes: float64(1), int64(1), object(15)
memory usage: 2.7+ KB
```

```python
ejemplo.isna().sum()
```

*Salida:*
```
_id              0
CODIGO           0
ENTIDAD          0
CALLE            0
NUM              0
ADICIONAL       15
COMUNA           0
DIA_INICIO       0
DIA_FIN          0
HORA_INICIO      0
HORA_FIN         0
CARGA_MAXIMA     0
CARGA_MINIMA     0
ESTE            13
NORTE            3
LONGITUD         0
LATITUD          0
dtype: int64
```

```python
#Podemos preguntar los que no son nan
ejemplo.ADICIONAL.notna()
```

*Salida:*
```
0      True
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9      True
10     True
11    False
12    False
13    False
14    False
15    False
16    False
17    False
21     True
Name: ADICIONAL, dtype: bool
```

Los valores nulos los puedo : dejar, eliminar o reemplazar. Esto depende de los datos con los que trabaje y mi objetivo.

## Reemplazar valores nulos
Para esto se ocupa la función **fillna** PERO debo tener cuidado

```python
#Observemos la ESTE
ejemplo.ESTE.dtype
#Es tipo object, por lo cual yo podria insertar tanto numeros como strings
```

*Salida:*
```
dtype('O')
```

Veamos que pasa al reemplazar.

Podria reemplazar con un 0

```python
ejemplo.ESTE.fillna(0, inplace=True)
```

*Salida:*
```
/tmp/ipykernel_2038/4122719630.py:1: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  ejemplo.ESTE.fillna(0, inplace=True)
```

```python
#Vuelvo a poner la columna en NaN
ejemplo.ESTE.replace({0: np.nan}, inplace=True)

#Tambien puedo usar
ejemplo.ESTE.replace({0: float('nan')}, inplace=True)
```

## Eliminar valores nulos

Para esto ocupamos la función **dropna()**

Sin argumentos la función simplemente elimina cualquier fila que contenga un NaNs en alguna columna

Para considerar NaNs solo en columna especificas se usa:

```
data.dropna(subset=[nombre_columna])
```

```python
ejemplo.dropna(subset=["ESTE"])
```

*Salida:*
```
_id CODIGO    ENTIDAD           CALLE   NUM ADICIONAL         COMUNA  \
1     2     57  FULLCARGA         mapocho  4190       NaN  QUINTA NORMAL   
4    16    100  FULLCARGA     EL CHAMPION  1401       NaN          MAIPU   
10    8     73  FULLCARGA  AV. SANTA ROSA  8035         A      SAN RAMON   
11    9     75  FULLCARGA     av. central  6577       NaN     LO ESPEJO    
12   10     80  FULLCARGA   av. ZAPADORES  0216       NaN       RECOLETA   
21   20    105  FULLCARGA    LUCILA GODOY  2766   (APROX)      LO ESPEJO   

   DIA_INICIO DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA    ESTE  \
1         Lun     Sab       08:00    21:00    $100.000$           0.0  342767   
4         Lun     Sab       08:00    21:00     $100.000        1000.0  335113   
10        Lun     Sab       08:00    21:00       $5.000          10.0  348227   
11        Lun     Sab       08:00    21:00      $10.000         100.0  342908   
12        Lun     Sab       08:00    21:00      $-1.000         100.0  348630   
21        Lun     Vie       05:30    23:00     $100.000        1000.0  343430   

      NORTE    LONGITUD     LATITUD  
1       NaN  -70.691895  -33.431889  
4   6290965  -70.775787  -33.508446  
10      NaN  -70.635071  -33.533241  
11      NaN  -70.691878  -33.505539  
12  6303645  -70.628166  -33.396126  
21  6290439  -70.685795  -33.514151
```

```python
ejemplo.dropna()
```

*Salida:*
```
_id CODIGO    ENTIDAD         CALLE   NUM ADICIONAL     COMUNA DIA_INICIO  \
21   20    105  FULLCARGA  LUCILA GODOY  2766   (APROX)  LO ESPEJO        Lun   

   DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA    ESTE    NORTE  \
21     Vie       05:30    23:00     $100.000        1000.0  343430  6290439   

      LONGITUD     LATITUD  
21  -70.685795  -33.514151
```

Perdemos muchos datos elimnando valores nulos, lo ideal seria ver si las columnas con hartos datos nulos son útiles o no

# Datos no útiles

Cuando tenemos datos no utiles simplemente debemos eliminarlos sin que afecten nuestro dataset (Esto deberia hacerse primero sin es que ocupe alguna operación de dropna general)

```python
#Si yo quisiera por ejemplo, solo puntos de carga donde la carga mínima sean 5 pesos tendría que filtrar
ejemplo = ejemplo[(ejemplo.CARGA_MINIMA>0)]
```

Consideremos que las columnas "ADICIONAL", "ESTE" y "NORTE" no aportan información útil, entonces debemos eliminarlas del conjunto de datos

```python
ejemplo.drop(columns=["ADICIONAL", "ESTE", "NORTE"], inplace=True)
```

```python
ejemplo
```

*Salida:*
```
_id CODIGO    ENTIDAD                    CALLE   NUM            COMUNA  \
0     1     52  FULLCARGA        AV. independencia  3187          CONCHALI   
2     3     62  FULLCARGA  PARQUE CENTRAL PONIENTE  1075             MAIPU   
3     4     63  FULLCARGA               AV. GRECIA  8585         PEÑALOLEN   
4    16    100  FULLCARGA              EL CHAMPION  1401             MAIPU   
5    17    102  FULLCARGA                  Alameda  3170  ESTACION CENTRAL   
6    18    103  FULLCARGA                  ALAMEDA  3171  Estacion central   
7     5     65  FULLCARGA                   estado   383         SANTIAGO    
8     6     69  FULLCARGA       BERNARDO O´HIGGINS   309       QUILICURA\t   
9     7     72  FULLCARGA      AV. WALKER MARTINEZ  1786        LA FLORIDA   
10    8     73  FULLCARGA           AV. SANTA ROSA  8035         SAN RAMON   
11    9     75  FULLCARGA              av. central  6577        LO ESPEJO    
12   10     80  FULLCARGA            av. ZAPADORES  0216          RECOLETA   
13   11     81  FULLCARGA          av. PROVIDENCIA  2382       PROVIDENCIA   
14   12     84  FULLCARGA         AV. SANTA RAQUEL  9685         LAFLORIDA   
15   13     86  FULLCARGA               NONATO COO  3392       PUENTE ALTO   
16   14     96  FULLCARGA            AV. LOS TOROS  5441       Puente Alto   
17   15     99  FULLCARGA                 SAN LUIS    18         QUILICURA   
21   20    105  FULLCARGA             LUCILA GODOY  2766         LO ESPEJO   

   DIA_INICIO DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA  \
0         Lun     Sab       08:00    21:00      $30.000       40000.0   
2         Lun     Sab       08:00    21:00      $50.000           5.0   
3         Lun     Sab       08:30    21:00      $10.000        4000.0   
4         Lun     Sab       08:00    21:00     $100.000        1000.0   
5         Lun     Vie       05:30    23:00     $100.000        1000.0   
6         Lun     Vie       05:30    23:00     $100.000        1000.0   
7         
... (salida truncada)
```

## Inconsistencias

Datos que a veces presentan mayusculas o minusculas o datos que a veces presentan tildes y otras veces no

```python
ejemplo
```

*Salida:*
```
_id CODIGO    ENTIDAD                    CALLE   NUM            COMUNA  \
0     1     52  FULLCARGA        AV. independencia  3187          CONCHALI   
2     3     62  FULLCARGA  PARQUE CENTRAL PONIENTE  1075             MAIPU   
3     4     63  FULLCARGA               AV. GRECIA  8585         PEÑALOLEN   
4    16    100  FULLCARGA              EL CHAMPION  1401             MAIPU   
5    17    102  FULLCARGA                  Alameda  3170  ESTACION CENTRAL   
6    18    103  FULLCARGA                  ALAMEDA  3171  Estacion central   
7     5     65  FULLCARGA                   estado   383         SANTIAGO    
8     6     69  FULLCARGA       BERNARDO O´HIGGINS   309       QUILICURA\t   
9     7     72  FULLCARGA      AV. WALKER MARTINEZ  1786        LA FLORIDA   
10    8     73  FULLCARGA           AV. SANTA ROSA  8035         SAN RAMON   
11    9     75  FULLCARGA              av. central  6577        LO ESPEJO    
12   10     80  FULLCARGA            av. ZAPADORES  0216          RECOLETA   
13   11     81  FULLCARGA          av. PROVIDENCIA  2382       PROVIDENCIA   
14   12     84  FULLCARGA         AV. SANTA RAQUEL  9685         LAFLORIDA   
15   13     86  FULLCARGA               NONATO COO  3392       PUENTE ALTO   
16   14     96  FULLCARGA            AV. LOS TOROS  5441       Puente Alto   
17   15     99  FULLCARGA                 SAN LUIS    18         QUILICURA   
21   20    105  FULLCARGA             LUCILA GODOY  2766         LO ESPEJO   

   DIA_INICIO DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA  \
0         Lun     Sab       08:00    21:00      $30.000       40000.0   
2         Lun     Sab       08:00    21:00      $50.000           5.0   
3         Lun     Sab       08:30    21:00      $10.000        4000.0   
4         Lun     Sab       08:00    21:00     $100.000        1000.0   
5         Lun     Vie       05:30    23:00     $100.000        1000.0   
6         Lun     Vie       05:30    23:00     $100.000        1000.0   
7         
... (salida truncada)
```

```python
#Podemos pasar todo el string a minusculas o mayusculas con las funciones upper o lower
```

```python
"hola".upper()
```

*Salida:*
```
'HOLA'
```

```python
"HolAAAAaaaa".lower()
```

*Salida:*
```
'holaaaaaaaa'
```

```python
"     hola como estas ".strip()
```

*Salida:*
```
'hola como estas'
```

```python
"hola como estas".replace(" ", "")
```

*Salida:*
```
'holacomoestas'
```

```python
for columna in ejemplo.columns:
  print(columna, ejemplo[columna].unique())
  print("-"*50)
```

*Salida:*
```
_id [ 1  3  4 16 17 18  5  6  7  8  9 10 11 12 13 14 15 20]
--------------------------------------------------
CODIGO ['52' '62' '63' '100' '102' '103' '65' '69' '72' '73' '75' '80' '81' '84'
 '86' '96' '99' '105']
--------------------------------------------------
ENTIDAD ['FULLCARGA']
--------------------------------------------------
CALLE ['AV. independencia' 'PARQUE CENTRAL PONIENTE' 'AV. GRECIA' 'EL CHAMPION'
 'Alameda' 'ALAMEDA' 'estado' 'BERNARDO O´HIGGINS' 'AV. WALKER MARTINEZ'
 'AV. SANTA ROSA' 'av. central' 'av. ZAPADORES' 'av. PROVIDENCIA'
 'AV. SANTA RAQUEL' 'NONATO COO' 'AV. LOS TOROS' 'SAN LUIS' 'LUCILA GODOY']
--------------------------------------------------
NUM ['3187' '1075' '8585' '1401' '3170' '3171' '383' '309' '1786' '8035'
 '6577' '0216' '2382' '9685' '3392' '5441' '18' '2766']
--------------------------------------------------
COMUNA ['CONCHALI' 'MAIPU' 'PEÑALOLEN' 'ESTACION CENTRAL' 'Estacion central'
 'SANTIAGO ' 'QUILICURA\t' 'LA FLORIDA' 'SAN RAMON' 'LO ESPEJO '
 '  RECOLETA' 'PROVIDENCIA' 'LAFLORIDA' 'PUENTE ALTO' 'Puente Alto'
 'QUILICURA' 'LO ESPEJO']
--------------------------------------------------
DIA_INICIO ['Lun' 'Lunes']
--------------------------------------------------
DIA_FIN ['Sab' 'Vie' 'Dom']
--------------------------------------------------
HORA_INICIO ['08:00' '08:30' '05:30' '09:00']
--------------------------------------------------
HORA_FIN ['21:00' '23:00' '22:00']
--------------------------------------------------
CARGA_MAXIMA ['$30.000' '$50.000' '$10.000' '$100.000' '$6.000' '$25.000' '1.000'
 '$5.000' '$-1.000']
--------------------------------------------------
CARGA_MINIMA [4.e+04 5.e+00 4.e+03 1.e+03 5.e+02 3.e+02 1.e+01 1.e+02]
--------------------------------------------------
LONGITUD ['-70.669021' '-70.787010' '-70.544136' '-70.775787' '-70.679611'
 '-70.649521' '-70.729274' '-70.579819' '-70.635071' '-70.691878'
 '-70.628166' '-70.606323' '-70.603798' '-70.570412' '-70.557426'
 '-70.738235' '-70.685795
... (salida truncada)
```

```python
#Para los dias solo necesitamos las primeras 3 letras del dia
ejemplo.DIA_INICIO.str[:3]
```

*Salida:*
```
0     Lun
2     Lun
3     Lun
4     Lun
5     Lun
6     Lun
7     Lun
8     Lun
9     Lun
10    Lun
11    Lun
12    Lun
13    Lun
14    Lun
15    Lun
16    Lun
17    Lun
21    Lun
Name: DIA_INICIO, dtype: object
```

```python
ejemplo.DIA_INICIO = ejemplo.DIA_INICIO.str[:3]
```

```python
#Para las calles y la comuna, eliminaremos los espacios en blanco y dejaremos todo en mayuscula
ejemplo.COMUNA.str.strip().str.upper().values
```

*Salida:*
```
array(['CONCHALI', 'MAIPU', 'PEÑALOLEN', 'MAIPU', 'ESTACION CENTRAL',
       'ESTACION CENTRAL', 'SANTIAGO', 'QUILICURA', 'LA FLORIDA',
       'SAN RAMON', 'LO ESPEJO', 'RECOLETA', 'PROVIDENCIA', 'LAFLORIDA',
       'PUENTE ALTO', 'PUENTE ALTO', 'QUILICURA', 'LO ESPEJO'],
      dtype=object)
```

```python
ejemplo.COMUNA = ejemplo.COMUNA.str.strip().str.upper()
ejemplo.CALLE = ejemplo.CALLE.str.strip().str.upper()
```

Para los simbolos $ debemos hacer un reemplazo utilizando la función **replace()** de strings

```python
ejemplo.CARGA_MAXIMA.str.replace("$", "") #hay que acceder al string, si no solo reemplaza las palabras que sean literalmente un "$"
```

*Salida:*
```
0      30.000
2      50.000
3      10.000
4     100.000
5     100.000
6     100.000
7       6.000
8      25.000
9       1.000
10      5.000
11     10.000
12     -1.000
13    100.000
14    100.000
15    100.000
16     50.000
17    100.000
21    100.000
Name: CARGA_MAXIMA, dtype: object
```

```python
ejemplo.CARGA_MAXIMA.str.replace("$", "").str.replace(".", "")
```

*Salida:*
```
0      30000
2      50000
3      10000
4     100000
5     100000
6     100000
7       6000
8      25000
9       1000
10      5000
11     10000
12     -1000
13    100000
14    100000
15    100000
16     50000
17    100000
21    100000
Name: CARGA_MAXIMA, dtype: object
```

```python
ejemplo.CARGA_MAXIMA = ejemplo.CARGA_MAXIMA.str.replace("$", "").str.replace(".", "")
```

```python
ejemplo
```

*Salida:*
```
_id CODIGO    ENTIDAD                    CALLE   NUM            COMUNA  \
0     1     52  FULLCARGA        AV. INDEPENDENCIA  3187          CONCHALI   
2     3     62  FULLCARGA  PARQUE CENTRAL PONIENTE  1075             MAIPU   
3     4     63  FULLCARGA               AV. GRECIA  8585         PEÑALOLEN   
4    16    100  FULLCARGA              EL CHAMPION  1401             MAIPU   
5    17    102  FULLCARGA                  ALAMEDA  3170  ESTACION CENTRAL   
6    18    103  FULLCARGA                  ALAMEDA  3171  ESTACION CENTRAL   
7     5     65  FULLCARGA                   ESTADO   383          SANTIAGO   
8     6     69  FULLCARGA       BERNARDO O´HIGGINS   309         QUILICURA   
9     7     72  FULLCARGA      AV. WALKER MARTINEZ  1786        LA FLORIDA   
10    8     73  FULLCARGA           AV. SANTA ROSA  8035         SAN RAMON   
11    9     75  FULLCARGA              AV. CENTRAL  6577         LO ESPEJO   
12   10     80  FULLCARGA            AV. ZAPADORES  0216          RECOLETA   
13   11     81  FULLCARGA          AV. PROVIDENCIA  2382       PROVIDENCIA   
14   12     84  FULLCARGA         AV. SANTA RAQUEL  9685         LAFLORIDA   
15   13     86  FULLCARGA               NONATO COO  3392       PUENTE ALTO   
16   14     96  FULLCARGA            AV. LOS TOROS  5441       PUENTE ALTO   
17   15     99  FULLCARGA                 SAN LUIS    18         QUILICURA   
21   20    105  FULLCARGA             LUCILA GODOY  2766         LO ESPEJO   

   DIA_INICIO DIA_FIN HORA_INICIO HORA_FIN CARGA_MAXIMA  CARGA_MINIMA  \
0         Lun     Sab       08:00    21:00        30000       40000.0   
2         Lun     Sab       08:00    21:00        50000           5.0   
3         Lun     Sab       08:30    21:00        10000        4000.0   
4         Lun     Sab       08:00    21:00       100000        1000.0   
5         Lun     Vie       05:30    23:00       100000        1000.0   
6         Lun     Vie       05:30    23:00       100000        1000.0   
7         
... (salida truncada)
```

```python
# Como cosa extra, str.contains()
# Consulta si el texto contiene el substring que le paso
# Por ejemplo queremos ver cuales son las calles que son avenidas
ejemplo.CALLE.str.contains("AV.", regex=False)
```

*Salida:*
```
0      True
2     False
3      True
4     False
5     False
6     False
7     False
8     False
9      True
10     True
11     True
12     True
13     True
14     True
15    False
16     True
17    False
21    False
Name: CALLE, dtype: bool
```

```python
ejemplo.loc[ejemplo.CALLE.str.contains("AV.", regex=False), "CALLE"]
```

*Salida:*
```
0       AV. INDEPENDENCIA
3              AV. GRECIA
9     AV. WALKER MARTINEZ
10         AV. SANTA ROSA
11            AV. CENTRAL
12          AV. ZAPADORES
13        AV. PROVIDENCIA
14       AV. SANTA RAQUEL
16          AV. LOS TOROS
Name: CALLE, dtype: object
```

# Columnas con tipo de dato incorrecto

Puede pasar que a veces las columnas tengan el tipo de dato incorrecto y eso me impide analizarlas correctamente

```python
ejemplo.info()
```

*Salida:*
```
<class 'pandas.core.frame.DataFrame'>
Index: 18 entries, 0 to 21
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   _id           18 non-null     int64  
 1   CODIGO        18 non-null     object 
 2   ENTIDAD       18 non-null     object 
 3   CALLE         18 non-null     object 
 4   NUM           18 non-null     object 
 5   COMUNA        18 non-null     object 
 6   DIA_INICIO    18 non-null     object 
 7   DIA_FIN       18 non-null     object 
 8   HORA_INICIO   18 non-null     object 
 9   HORA_FIN      18 non-null     object 
 10  CARGA_MAXIMA  18 non-null     object 
 11  CARGA_MINIMA  18 non-null     float64
 12  LONGITUD      18 non-null     object 
 13  LATITUD       18 non-null     object 
dtypes: float64(1), int64(1), object(12)
memory usage: 2.7+ KB
```

Para hacer consultas de manera eficiente, carga maxima deberia ser una columna númerica.

También las horas podrian ser otro tipo de dato para optimizar las consultas.

```python
#Para cambiar el tipo de dato utilizamos astype
ejemplo.CARGA_MAXIMA = ejemplo.CARGA_MAXIMA.astype("float64")
```

```python
#Existe el tipo de dato datetime
pd.to_timedelta(ejemplo.HORA_INICIO +':00')
```

*Salida:*
```
0    0 days 08:00:00
2    0 days 08:00:00
3    0 days 08:30:00
4    0 days 08:00:00
5    0 days 05:30:00
6    0 days 05:30:00
7    0 days 08:00:00
8    0 days 08:00:00
9    0 days 08:00:00
10   0 days 08:00:00
11   0 days 08:00:00
12   0 days 08:00:00
13   0 days 08:00:00
14   0 days 08:00:00
15   0 days 08:00:00
16   0 days 09:00:00
17   0 days 08:00:00
21   0 days 05:30:00
Name: HORA_INICIO, dtype: timedelta64[ns]
```

```python
ejemplo.HORA_INICIO = pd.to_timedelta(ejemplo.HORA_INICIO +':00')
ejemplo.HORA_FIN = pd.to_timedelta(ejemplo.HORA_FIN +':00')
```

```python
ejemplo.HORA_FIN.max()
```

*Salida:*
```
Timedelta('0 days 23:00:00')
```

```python
#Pasar datos a tipo timedelta me permite acceder de manera facil a la hora
print(ejemplo.HORA_INICIO.dt.components.hours)
```

*Salida:*
```
0     8
2     8
3     8
4     8
5     5
6     5
7     8
8     8
9     8
10    8
11    8
12    8
13    8
14    8
15    8
16    9
17    8
21    5
Name: hours, dtype: int64
```

```python
ejemplo.describe()
```

*Salida:*
```
_id                HORA_INICIO                   HORA_FIN  \
count  18.000000                         18                         18   
mean   10.500000            0 days 07:40:00            0 days 21:23:20   
std     5.533322  0 days 01:01:44.369439078  0 days 00:46:39.159537726   
min     1.000000            0 days 05:30:00            0 days 21:00:00   
25%     6.250000            0 days 08:00:00            0 days 21:00:00   
50%    10.500000            0 days 08:00:00            0 days 21:00:00   
75%    14.750000            0 days 08:00:00            0 days 21:00:00   
max    20.000000            0 days 09:00:00            0 days 23:00:00   

        CARGA_MAXIMA  CARGA_MINIMA  
count      18.000000      18.00000  
mean    54777.777778    2962.50000  
std     43909.741055    9287.80007  
min     -1000.000000       5.00000  
25%     10000.000000     150.00000  
50%     50000.000000    1000.00000  
75%    100000.000000    1000.00000  
max    100000.000000   40000.00000
```

#Ejercicios

https://es.wikipedia.org/wiki/Anexo:Episodios_de_Bob_Esponja

Utilizando PYTHON Y PANDAS (SIN MODIFICAR LA CELDA QUE DEFINE LA TABLA):

- Hacer que la tabla de juguete contenga solo los datos las temporadas de bob esponja. (eliminar las peliculas)
- Eliminar duplicados y reemplazar valores NaN por "TBA"
- Dejar todas las fechas solo con el año
- Eliminar las temporadas que tengan mas de 30 caps
- Ordenar la tabla por numero de temporada

```python
tabla = [
[5, '20', 	'19 de febrero de 2007', 	'19 de julio de 2009', 	'14 de mayo de 2007', 	'17 de julio de 2009', 	'4 de septiembre de 2007', 	'16 de noviembre de 2009'],
['Bob Esponja: Un Héroe Fuera del Agua', 1, 	'6 de febrero de 2015', 	'30 de enero de 2015', 	'6 de febrero de 2015'],
[1, '20', '1 de mayo de 1999', '3 de marzo de 2001', '1 de diciembre de 1999', '17 de diciembre de 2000' ,'1 de mayo de 1999', '14 de abril de 2001'],
[7, '26', 	'19-julio-2009', 	'11-junio-2011', 	'22 de febrero de 2010', 	'11 de febrero de 2013', '9 de marzo de 2013', 	'23 de septiembre de 2011'],
[3 , '20', '5 de octubre de 2001' ,  '11-octubre-2004', '2 de septiembre de 2002', '3-diciembre-2004', '22-marzo-2002' , '3-diciembre-2004'],
['Bob Esponja: La Película', 1, '19 de noviembre de 2004', '3 de diciembre de 2004', '28 de enero de 2005'],
[10, '11', 	'15 de octubre de 2016', '2 de diciembre de 2017', 	'3 de abril de 2017', 	'6 de diciembre de 2017', 	'15 de julio de 2017', 	float("NaN")],
[13, '264', 	'22 de octubre de 2020', 	'TBA', 	'8 de mayo de 2021', 	'TBA', 	'TBA' ,	'TBA' ],
[4, 20, 	'6 de mayo de 2005', 	'24 de julio de 2007', 	'25 de noviembre de 2005', 	'7 de octubre de 2007', 	'15 de febrero de 2006', 	'5 de septiembre de 2007'],
[2, '20', '26 de octubre de 2000' , '26 de julio de 2003', '3 de abril de 2001', '14-noviembre-2003' , '16 de julio de 2001', '7 de junio de 2002'],
[6, '26', 	'3-marzo-2008', 	'5 de julio de 2010', 	'25 de agosto de 2008', 	'12 de noviembre de 2010', 	'29 de abril de 2010', 	'8 de marzo de 2011'],
['Bob Esponja: Un Héroe al Rescate ', 1,	'4 de marzo de 2021', 	'5 de noviembre de 2020'],
[8, '26', 	'26 de marzo de 2011', 	'6 de diciembre de 2012', 	'22 de octubre de 2011', 	'31 de diciembre de 2013', 	'26 de septiembre de 2011', 	'28 de octubre de 2013'],
[9, '26', 	'21 de julio de 2012', 	'20 de febrero de 2017' 	'11 de agosto de 2012' 	'25 de marzo de 2017' 	'24 de noviembre de 2013' 	'25 de marzo de 2017'],
[7, '50', 	'19-julio-2009', 	'11-junio-2011', 	'22 de febrero de 2010', 	'11 de febrero de 2013', '9 de marzo de 2013', 	'23 de septiembre de 2011'],
[2, '20', '26 de octubre de 2000' , '26 de julio de 2003', '3 de abril de 2001', '14-noviembre-2003' , '16 de julio de 2001', '7 de junio de 2002'],
[12, '26', 	'11 de noviembre de 2018', 	'TBA', 	'6 de abril de 2019', 	'16 de agosto de 2021', 	'13 de mayo de 2019', 	'TBA'],
[5, '20', 	'19 de febrero de 2007', 	'19 de julio de 2009', 	'14 de mayo de 2007', 	'17 de julio de 2009', 	'4 de septiembre de 2007', 	'16 de noviembre de 2009'],
[11, '26', 	'24 de junio de 2017', 	'25 de noviembre de 2018' ,	'25 de septiembre de 2017', 	'30-marzo-2019 ',	'25 de septiembre de 2017', 	'31 de enero de 2019']
]
tabla = pd.DataFrame(tabla, columns = ["Temporada", "Episodios", "Comienzo Estados Unidos", "Final Estados Unidos", "Comienzo Hispanoamérica", "Final Hispanoamérica", "Comienzo España", "Final España"])

tabla.head()
```

*Salida:*
```
Temporada Episodios Comienzo Estados Unidos  \
0                                     5        20   19 de febrero de 2007   
1  Bob Esponja: Un Héroe Fuera del Agua         1    6 de febrero de 2015   
2                                     1        20       1 de mayo de 1999   
3                                     7        26           19-julio-2009   
4                                     3        20    5 de octubre de 2001   

  Final Estados Unidos  Comienzo Hispanoamérica     Final Hispanoamérica  \
0  19 de julio de 2009       14 de mayo de 2007      17 de julio de 2009   
1  30 de enero de 2015     6 de febrero de 2015                     None   
2   3 de marzo de 2001   1 de diciembre de 1999  17 de diciembre de 2000   
3        11-junio-2011    22 de febrero de 2010    11 de febrero de 2013   
4      11-octubre-2004  2 de septiembre de 2002         3-diciembre-2004   

           Comienzo España              Final España  
0  4 de septiembre de 2007   16 de noviembre de 2009  
1                     None                      None  
2        1 de mayo de 1999       14 de abril de 2001  
3       9 de marzo de 2013  23 de septiembre de 2011  
4            22-marzo-2002          3-diciembre-2004
```

## Eliminar duplicados

```python
tabla.drop_duplicates()
```

*Salida:*
```
Temporada Episodios  Comienzo Estados Unidos  \
0                                      5        20    19 de febrero de 2007   
1   Bob Esponja: Un Héroe Fuera del Agua         1     6 de febrero de 2015   
2                                      1        20        1 de mayo de 1999   
3                                      7        26            19-julio-2009   
4                                      3        20     5 de octubre de 2001   
5               Bob Esponja: La Película         1  19 de noviembre de 2004   
6                                     10        11    15 de octubre de 2016   
7                                     13       264    22 de octubre de 2020   
8                                      4        20        6 de mayo de 2005   
9                                      2        20    26 de octubre de 2000   
10                                     6        26             3-marzo-2008   
11     Bob Esponja: Un Héroe al Rescate          1       4 de marzo de 2021   
12                                     8        26      26 de marzo de 2011   
13                                     9        26      21 de julio de 2012   
14                                     7        50            19-julio-2009   
16                                    12        26  11 de noviembre de 2018   
18                                    11        26      24 de junio de 2017   

                                 Final Estados Unidos  \
0                                 19 de julio de 2009   
1                                 30 de enero de 2015   
2                                  3 de marzo de 2001   
3                                       11-junio-2011   
4                                     11-octubre-2004   
5                              3 de diciembre de 2004   
6                              2 de diciembre de 2017   
7                                                 TBA   
8                                 24 de julio de 2007   
9                                 26 d
... (salida truncada)
```

```python
tabla = tabla.drop_duplicates(subset=["Temporada"])
```

```python
tabla
```

*Salida:*
```
Temporada Episodios  Comienzo Estados Unidos  \
0                                      5        20    19 de febrero de 2007   
1   Bob Esponja: Un Héroe Fuera del Agua         1     6 de febrero de 2015   
2                                      1        20        1 de mayo de 1999   
3                                      7        26            19-julio-2009   
4                                      3        20     5 de octubre de 2001   
5               Bob Esponja: La Película         1  19 de noviembre de 2004   
6                                     10        11    15 de octubre de 2016   
7                                     13       264    22 de octubre de 2020   
8                                      4        20        6 de mayo de 2005   
9                                      2        20    26 de octubre de 2000   
10                                     6        26             3-marzo-2008   
11     Bob Esponja: Un Héroe al Rescate          1       4 de marzo de 2021   
12                                     8        26      26 de marzo de 2011   
13                                     9        26      21 de julio de 2012   
16                                    12        26  11 de noviembre de 2018   
18                                    11        26      24 de junio de 2017   

                                 Final Estados Unidos  \
0                                 19 de julio de 2009   
1                                 30 de enero de 2015   
2                                  3 de marzo de 2001   
3                                       11-junio-2011   
4                                     11-octubre-2004   
5                              3 de diciembre de 2004   
6                              2 de diciembre de 2017   
7                                                 TBA   
8                                 24 de julio de 2007   
9                                 26 de julio de 2003   
10                                 5 de julio de 2010   
11 
... (salida truncada)
```

## Reemplazar valores NaN por TBA

```python
tabla = tabla.fillna("TBA")
```

## Dejar todas las fechas solo con el año (en string)

```python
"16 de abril de 1998"[:-4]
```

*Salida:*
```
'16 de abril de '
```

```python
tabla["Comienzo Estados Unidos"].str.strip().str[-4:]
```

*Salida:*
```
0     2007
1     2015
2     1999
3     2009
4     2001
5     2004
6     2016
7     2020
8     2005
9     2000
10    2008
11    2021
12    2011
13    2012
16    2018
18    2017
Name: Comienzo Estados Unidos, dtype: object
```

```python
for col in ['Comienzo Estados Unidos',
       'Final Estados Unidos', 'Comienzo Hispanoamérica',
       'Final Hispanoamérica', 'Comienzo España', 'Final España']:
       tabla[col] = tabla[col].str.strip().str[-4:]
```

```python
tabla
```

*Salida:*
```
Temporada Episodios Comienzo Estados Unidos  \
0                                      5        20                    2007   
1   Bob Esponja: Un Héroe Fuera del Agua         1                    2015   
2                                      1        20                    1999   
3                                      7        26                    2009   
4                                      3        20                    2001   
5               Bob Esponja: La Película         1                    2004   
6                                     10        11                    2016   
7                                     13       264                    2020   
8                                      4        20                    2005   
9                                      2        20                    2000   
10                                     6        26                    2008   
11     Bob Esponja: Un Héroe al Rescate          1                    2021   
12                                     8        26                    2011   
13                                     9        26                    2012   
16                                    12        26                    2018   
18                                    11        26                    2017   

   Final Estados Unidos Comienzo Hispanoamérica Final Hispanoamérica  \
0                  2009                    2007                 2009   
1                  2015                    2015                  TBA   
2                  2001                    1999                 2000   
3                  2011                    2010                 2013   
4                  2004                    2002                 2004   
5                  2004                    2005                  TBA   
6                  2017                    2017                 2017   
7                   TBA                    2021                  TBA   
8                  2007                    2005         
... (salida truncada)
```

#Eliminar peliculas y temporadas de mas de 30 caps

```python
tabla.Episodios = tabla.Episodios.astype("int64")
```

```python
tabla = tabla[(tabla.Episodios>1) & (tabla.Episodios<=30)]
```

```python
tabla
```

*Salida:*
```
Temporada  Episodios Comienzo Estados Unidos Final Estados Unidos  \
0          5         20                    2007                 2009   
2          1         20                    1999                 2001   
3          7         26                    2009                 2011   
4          3         20                    2001                 2004   
6         10         11                    2016                 2017   
8          4         20                    2005                 2007   
9          2         20                    2000                 2003   
10         6         26                    2008                 2010   
12         8         26                    2011                 2012   
13         9         26                    2012                 2017   
16        12         26                    2018                  TBA   
18        11         26                    2017                 2018   

   Comienzo Hispanoamérica Final Hispanoamérica Comienzo España Final España  
0                     2007                 2009            2007         2009  
2                     1999                 2000            1999         2001  
3                     2010                 2013            2013         2011  
4                     2002                 2004            2002         2004  
6                     2017                 2017            2017          TBA  
8                     2005                 2007            2006         2007  
9                     2001                 2003            2001         2002  
10                    2008                 2010            2010         2011  
12                    2011                 2013            2011         2013  
13                     TBA                  TBA             TBA          TBA  
16                    2019                 2021            2019          TBA  
18                    2017                 2019            2017         2019
```

```python
#ordenar la tabla por numero de temporada
tabla.sort_values(by=["Temporada"])
```

*Salida:*
```
Temporada  Episodios Comienzo Estados Unidos Final Estados Unidos  \
2          1         20                    1999                 2001   
9          2         20                    2000                 2003   
4          3         20                    2001                 2004   
8          4         20                    2005                 2007   
0          5         20                    2007                 2009   
10         6         26                    2008                 2010   
3          7         26                    2009                 2011   
12         8         26                    2011                 2012   
13         9         26                    2012                 2017   
6         10         11                    2016                 2017   
18        11         26                    2017                 2018   
16        12         26                    2018                  TBA   

   Comienzo Hispanoamérica Final Hispanoamérica Comienzo España Final España  
2                     1999                 2000            1999         2001  
9                     2001                 2003            2001         2002  
4                     2002                 2004            2002         2004  
8                     2005                 2007            2006         2007  
0                     2007                 2009            2007         2009  
10                    2008                 2010            2010         2011  
3                     2010                 2013            2013         2011  
12                    2011                 2013            2011         2013  
13                     TBA                  TBA             TBA          TBA  
6                     2017                 2017            2017          TBA  
18                    2017                 2019            2017         2019  
16                    2019                 2021            2019          TBA
```

ALGO EXTRA! Tecnicamente hay valores en las columnas, eso no deberia ser así, por ejemplo "Estados Unidos", "Hispanoamerica" y "España" son valores de "Lugar"

¿Como se podría ordenar la tabla para que tuviera las columnas "Temporada", "Episodios", "Lugar", "Comienzo" y "Fin"?

```python
tabla_corregida = pd.DataFrame(columns=['Temporada', 'Episodios', "Lugar", "Comienzo", "Final"])
for i in range(2,8,2):
  cols = ['Temporada', "Episodios"] + list(tabla.columns[i:i+2])
  aux_pais = tabla[cols]
  pais = cols[-1][len("Final"):]
  aux_pais.columns = ["Temporada", "Episodios", "Comienzo", "Final"]
  aux_pais["Lugar"] = pais
  tabla_corregida = pd.concat([tabla_corregida, aux_pais], ignore_index=True)
```

*Salida:*
```
/tmp/ipykernel_2038/3806609702.py:7: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  aux_pais["Lugar"] = pais
/tmp/ipykernel_2038/3806609702.py:7: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  aux_pais["Lugar"] = pais
/tmp/ipykernel_2038/3806609702.py:7: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  aux_pais["Lugar"] = pais
```

```python
tabla_corregida
```

*Salida:*
```
Temporada Episodios            Lugar Comienzo Final
0          5        20   Estados Unidos     2007  2009
1          1        20   Estados Unidos     1999  2001
2          7        26   Estados Unidos     2009  2011
3          3        20   Estados Unidos     2001  2004
4         10        11   Estados Unidos     2016  2017
5          4        20   Estados Unidos     2005  2007
6          2        20   Estados Unidos     2000  2003
7          6        26   Estados Unidos     2008  2010
8          8        26   Estados Unidos     2011  2012
9          9        26   Estados Unidos     2012  2017
10        12        26   Estados Unidos     2018   TBA
11        11        26   Estados Unidos     2017  2018
12         5        20   Hispanoamérica     2007  2009
13         1        20   Hispanoamérica     1999  2000
14         7        26   Hispanoamérica     2010  2013
15         3        20   Hispanoamérica     2002  2004
16        10        11   Hispanoamérica     2017  2017
17         4        20   Hispanoamérica     2005  2007
18         2        20   Hispanoamérica     2001  2003
19         6        26   Hispanoamérica     2008  2010
20         8        26   Hispanoamérica     2011  2013
21         9        26   Hispanoamérica      TBA   TBA
22        12        26   Hispanoamérica     2019  2021
23        11        26   Hispanoamérica     2017  2019
24         5        20           España     2007  2009
25         1        20           España     1999  2001
26         7        26           España     2013  2011
27         3        20           España     2002  2004
28        10        11           España     2017   TBA
29         4        20           España     2006  2007
30         2        20           España     2001  2002
31         6        26           España     2010  2011
32         8        26           España     2011  2013
33         9        26           España      TBA   TBA
34        12        26           España     2019   TBA
35        11        26 
... (salida truncada)
```
