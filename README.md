# MCOC2020-P0

# E1 - Mi computador principal :shipit:

* Marca/modelo: Macbook Pro 13-Inch 2017 (Four Thuderbolt 3 Ports)
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel Cor3 i5-7267U (Kaby Lake)
  * Velocidad Base: 3.10 GHz
  * Velocidad Máxima: 3.50 GHz
  * Numero de núcleos: 2 
  * Humero de hilos: 2
  * Arquitectura: 64-Bit
* Tamaño de las cachés del procesador
  * L1: 32KB/32KB
  * L2/L3: 256KB x2
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 2133 MHz
* Tarjeta Gráfica
  * Marca / Modelo: Intel Iris Plus Graphics 650 (Integrada)
  * VRAM (dinamico, máximo): 1536 MB
  * Resolución: 2560 x 1600
* Disco 1: 
  * Modelo: APPLE SSD AP0256J
  * Tipo: SSD
  * Tamaño: 256GB
  * Particiones: 2 (Macintosh HD 190GB + Bootcamp Windows 10 60GB)
  * Sistema de archivos: Mac Os -> APFS / Windows -> NTFS

  
* Dirección MAC de la tarjeta wifi: 8c:85:90:9c:88:1b
* Dirección IP (Interna, del router): 192.168.0.1
* Dirección IP (Externa, del ISP): 192.168.0.22
* Proveedor internet: VTR Banda Ancha S.A.

<br>  
<br>  
<br>  
<br>  

# E2 - Desempeño MATMUL :shipit:



![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E2.1.png)



### ¿Como difiere del gráfico del profesor/ayudante?
  * 👉 La primera diferencia es el tamaño N de las matrices utilizadas, que en mi caso el limite esta en N=8000 y en el caso del profesor esta en N=20000
  * 👉 En segundo lugar, se produce una alta variabilidad de los tiempos de ejecución para N=20 – N=30 en mi caso, mientras que en el caso del profesor, la mayor variabilidad se encuentra en valores de N=100–1000
  * 👉 En tercer lugar, para valores mayores a N=1000, mi grafico indica que el tiempo que tarda mi computador es mayor que en el caso del profesor.
  * 👉 Cuarto, para los valores iniciales de N, mi computador se demora casi 0.1 s, mientras que el grafico del profesor indica que su computador se demora mucho menos, alrededor de los 0.1 ms.
  * 👉 Quinto, en mi caso hubo una corrida "outlier" que es la que sale en azul en el primer grafico (N vs Tiempo), sin embargo, al ser un valor atipico puede ser no representativo del proceso general y corresponde a una excepcion dada por la aleatoriedad de los datos y el proceso.

### ¿A qué se pueden deber las diferencias?
  * 👉 La primera se debe a que mi computador es menos potente, y se queda muy pegado si le pongo un N mayor a 10000.
  * 👉 Luego, la variabilidad se puede dar por la aleatoriedad del proceso y porque mi computador tiene un procesador con solo 2 nucleos, de menor velocidad (máx 3.5 GHz) y posee menor memoria RAM (8 GB), en contraste al del profesor que tiene mas nucleos, aunque RAM de menor velocidad (1867 MHz). En mi caso tengo un procesador de 7ma generacion con tecnologia de 14 nm, mientras que el profesor tiene un procesador de 4ta generacion con tecnologia de 22 nm, y aún así, es mas potente que el mio. Esto ultimo se puede ver en el tiempo de ejecucion para valores de N mayores a 1000, que son mas chicos en el caso del profesor, en comparación a lo que se demora mi computador.
  
  
### El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * 👉 El grafico de uso de memoria resulta ser lineal (y de cierta forma igual que el del profesor) ya que la memoria utilizada por las matrices es la misma. Esto se debe a que, independiente del valor numerico de los elementos matriciales, cada uno es un componente float que ocupa 8 bytes de almacenamiento. De esta manera, al ser 3 matrices, cada una de N filas y N columnas, se obtiene que la cantidad de memoria se puede calcular mediante la siguiente formula general: 
  
  * ⚙️ Memoria utilizada = (k)· (N^2) · (8) {bytes}
  <br>DONDE <br>[k: numero de matrices involucradas (en este caso 3, la matriz A, la matriz B y la matriz C, resultante de la multiplicacion entre A y B)]<br>
  [N^2: numero de elementos totales de una matriz de N filas por N columnas]<br>
  [8: representa los bytes utilizados por cada elemento, en este caso son 8 bytes porque cada elemento es un float]<br>
      
  * 👉 En el caso del grafico de tamaño de la matriz versus tiempo transcurrido no es lineal ya que el computador realiza otros procesos además de ejecutar el programa, y porque los elementos de las matrices estan dados por floats aleatorios, cada corrida es totalmente distinta.   
  
### ¿Qué versión de python está usando?
  * 👉 Estoy utilizando Python 3.8 en Spyder 4.1.4, mediante Anaconda 1.9.12.
  
  
### ¿Qué versión de numpy está usando?
  * 👉 La version de Numpy utilizada es 1.18.5
  
  
### Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
  * 👉 Si la pregunta es "¿se utiliza mas de un nucleo?", la respuesta es si; en el monitor de actividad se puede apreciar que el porcentaje de uso esta entre 170-200% lo que indicaría que se usan todos los nucleos de mi procesador (que son 2 nucleos). Pero si la pregunta es "¿se utiliza más de un procesador?", la respuesta es que, tengo 1 solo procesador y lo uso completo.
  
  
  ![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E2.2.png)
  
<br>  
<br>  
<br>  
<br>  

# E3 - Desempeño _MI_–MATMUL :shipit:




![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E3.1.png)



### ¿Como difiere del gráfico del profesor/ayudante?
  * 👉 La primera diferencia está en el tamaño N de las matrices. En mi caso, llegan hasta valores de N=500, a diferencia del ayudante que tenía valores hasta N=1000.
  * 👉 La segunda diferencia esta en que una de las corridas para un N muy bajo, probablemente 2 o 3, se tarda un tiempo mayor (10 ms) que el del ayudante (1 ms)
  * 👉 El resto del grafico de las corridas es muy parecido, si es que no, igual ( a diferencia de la RAM máxima o límite ).

### ¿A qué se pueden deber las diferencias?
  * 👉 La primera se debe a que en mi caso, mi python se quedaba pegado para valores mayores y tenía que hacer forcequit.
  * 👉 La razon de que las corridas del programa, para valores pequeños de N, esta en que el computador esta realizando otros procesos que ocupan CPU, ademas del de la ejecución del programa. Este tiempo inicial puede ser variable según el tipo de procesador y la velocidad de la RAM.
  
  
### El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * 👉 El grafico de uso de memoria resulta ser lineal (y de cierta forma igual que el del ayudante) ya que la memoria utilizada por las matrices es la misma. Esto se debe a que, independiente del valor numerico de los elementos matriciales, cada uno es un componente float que ocupa 8 bytes de almacenamiento. De esta manera, al ser 3 matrices, cada una de N filas y N columnas, se obtiene que la cantidad de memoria se puede calcular mediante la formula general indicada en la sección anterior, que es invariable. En el caso del grafico de tamaño de la matriz versus tiempo transcurrido, se tiene que es aparentemente lineal, pero como ya se ha mencionado, esto puede no ser así en todos los casos, como por ejemplo al principio que baja y luego sube, y la razón de esto yace en que el computador tambien realiza otros procesos además de ejecutar el programa, y porque los elementos de las matrices estan dados por floats aleatorios.
  
### ¿Qué versión de python está usando?
  * 👉 Estoy utilizando Python 3.8 en Spyder 4.1.4, mediante Anaconda 1.9.12.
  
  
### ¿Qué versión de numpy está usando?
  * 👉 La version de Numpy utilizada es 1.18.5
  
  
### Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
  * 👉 En este caso, el monitor de actividad de mi computador registró que solo se estaba utilizando un solo nucleo para realizar las corridas:
  
  
![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E3.2.png)

Según lo que investigue, que se esté usando un 100% de la CPU indicaría que se está utilizando 1 solo nucleo, lo cual puede ser contraproducente, pero puedo confirmarlo ya que en el caso anterior (entrega 2) mi uso de CPU llegaba a niveles de 200% lo que indicaría que se estaban usando los 2 nucleos que tiene mi procesador. <br> FUENTE: https://forums.macrumors.com/threads/how-to-tell-how-many-cores-an-app-uses.1737218/
<br>  
<br>  
<br>  
<br>  


# E4 - Mi computador principal :shipit:

### Acerca de esta entrega

En esta entrega se han estudiado distintos casos para el tiempo transcurrido durante una ejecucion de inversion de matrices con distintos tipos de datos y el consumo de memoria que la ejecucion de la operacion supone. A continuación se presenta los graficos que resumen los resultados:

![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E4.1.jpeg )
![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E4.2.jpeg )
![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E4.3.jpeg )

<br>
<br>

### Casos realizados

En total se realizaron 10 casos, con 3 casos principales en los que se utilizaron 3 opciones distintas de inversion de matrices: (1) ocupando la librería de numpy, (2) utilizando la librería de scipy, sin reutilizar la memoria de la matriz (overwrite=False) y (3) implementando la librería de scipy, reusando la memoria de la matriz (overwrite=True). En cada uno de estos casos principales se utilizaron los tipos de dato: half, single, double y longdouble, exceptuando el primer caso principal, ya que la inversion de matrices con la libreria de numpy no tiene soporte para datos del tipo float16 (half) ni float128 (longdouble).

<br>
<br>


### Tamaño de los datos

La libreria sys tiene una funcion que es sys.getsizeof(), la cual entrega la cantidad de bytes que ocupa un objeto. De esta manera se utilizo el siguiente comando: <br>

```
numero = 1
print (f" El tamaño de un dato half en mi MacBook Pro 13'' es de {sys.getsizeof(np.half(numero))} bytes")
print (f" El tamaño de un dato single en mi MacBook Pro 13'' es de {sys.getsizeof(np.single(numero))} bytes")
print (f" El tamaño de un dato double en mi MacBook Pro 13'' es de {sys.getsizeof(np.double(numero))} bytes")
print (f" El tamaño de un dato longdouble en mi MacBook Pro 13'' es de {sys.getsizeof(np.longdouble(numero))} bytes")
```
<br>

Y se obtuvo como resultado:
```
El tamaño de un dato half en mi MacBook Pro 13'' es de 26 bytes
El tamaño de un dato single en mi MacBook Pro 13'' es de 28 bytes
El tamaño de un dato double en mi MacBook Pro 13'' es de 32 bytes
El tamaño de un dato longdouble en mi MacBook Pro 13'' es de 48 bytes
```
<br>

### Registro de utilización de memoria

Caso 1 - SINGLE: ~119% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
Caso 1 - DOUBLE: ~120% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
<br>
<br>
Caso 2 - HALF: ~139% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
Caso 2 - SINGLE: ~144% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
Caso 2 - DOUBLE: ~149% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
Caso 2 - LONGDOUBLE: ~150% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
<br>
<br>
Caso 3 - HALF: ~130% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
Caso 3 - SINGLE: ~143% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
Caso 3 - DOUBLE: ~145% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
Caso 3 - LONGDOUBLE: ~147% CPU  de un limite de ~200%  (Intel Core i5 Dual Core)<br>
<br>
Los valores de CPU utilizados corresponden a aproximaciones ya que a medida que se ejecuta el programa este tiene momentos peak y momentos mas bajos, no es exactamente uniforme, tal como indica el grafico extraido del monitor de actividad:<br>
![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E4.png )
<br>

### Breve analisis de graficos

En la clase del 10/08 el profesor Abell nos enseño como el tipo de dato influye en el tiempo de ejecucion del programa y la cantidad de memoria utilizada. Si bien no es el objetivo principal del curso aprender el lenguaje binario, bytes y todo lo relacionado a ello, si es de muchisima utilidad para enteder que los programas pueden ser "optimizados" en uso de tiempo y memoria, si uno esta dispuesto a sacrificar algo de precision en los datos. Los tipos de dato con menos "bytes" suelen ser mas "livianos o rapidos" pero menos precisos que los tipos de dato con mayor cantidad de bytes, por ejemplo, un float32 versus un float64. De esta manera, mientras mas bytes tenga un tipo de dato, mas memoria utilizará y menos rapido será el programa. Esto se puede ver reflejado en los graficos ya que se puede apreciar que, por ejemplo, los datos tipo double suelen tener mayores tiempos que los datos tipo single (28 versus 32 bytes). O de la manera mas contrastante, los datos tipo half de 26 bytes (caso 2) se demoran apenas 0.1 segundo para N=2000 , mientras que para los datos tipo longdouble de 48 bytes (caso 2) tienen tiempos por sobre 0.1 segundo, en incluso en el caso 3 se acercan mucho mas a 1 segundo. De esta forma, por muy trivial que parezca, se comprueba que a medida que los datos son mas pesados en bytes, es mas lento el programa, y logicamente ocupa mas memoria.<br>
<br>
Con respecto a la diferencia entre el caso 2 y el caso 3, esta radica en que en el ultimo se utiliza la memoria de la matriz anterior para reescribir la matriz inversa. Los resultados de la diferencia, a pesar de no ser muy grandes, son bastante evidentes, por ejemplo en el caso 2 del tipo de dato double, la matriz de tamaño N = 2000 ocupa mucho mas de 100 MB, mientras que en el caso 3, para este mismo tipo de dato, se utilizan apenas 100 MB. 
<br>




### Respuesta a las preguntas

* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
<br>
 El "p-adic approximation method" ya que encuentra soluciones aproximadas convergentes

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)
<br>

En clase estudiamos acerca de las jerarquias de memoria, el disco duro de disco es 10 veces mas lento que el de estado solido (SSD), luego la memoria ram es 10 veces mas rapida que el SSD, y si me quedo sin ram lo que hace el computador es paginacion, lo cual conlleva ir guardando informacion en la memoria, y resulta un proceso sumamente lento que en la practica uno no quiere que pase. Luego , 10 veces mas rapidos son los cache, y se dividen en 3 categorias o niveles:<br>
> 10x veces mas rapido que la RAM es el cache L3 de 8192KB<br>
> 10x veces mas rapido que el cache L3 es el cache L2 de 256KB<br>
> 10x veces mas rapido que el cache L2 es el cache L1 de 32KB<br>
<br>
De esta forma si buscamos mas potencia en nuestro equipo debemos fijarnos en estos numeros de los caches. El L1 es el mejor.
        
