# MCOC2020-P0 (README GENERAL CON TODAS LAS ENTREGAS)

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
        
# E5 - Desempeño Ax=B (Parte 1)

A partir de esta entrega, ordenare las entregas del Proyecto 0 en carpetas. Cada una tendrá su README.md además del que está en la pagina principal, en el que de igual manera se mostrará el progreso realizado.

En esta entrega el grafico ploteado es el siguiente:

![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%205/Grafico%20E5.1%20Ax_B_Parte1.png )

Es necesario destacar que la curva azul "invertir matriz" corresponde al archivo de texto _A_invB_inv.txt_ en el que se realiza la inversion de la matriz para resolver el sistema Ax=B. De esta forma se tienen en total 2 matrices y 2 vectores para el cálculo de bytes o memoria utilizada. En el caso de la curva naranja, "Sin Invertir Matriz" corresponde al archivo _A_invB_npSolve.txt_ y no se realiza la inversion de la matriz A por separado, si no que se hace uso de la funcion de numpy *np.linalg.solve(A,B)*  . Entonces, para el calculo de bytes o memoria usada, se utiliza 1 sola matriz y 2 vectores, dando como resultado un menor consumo de memoria. Para entregas futuras (entrega 6) estos datos no serán mostrados si no se solicita explicitamente. El uso de procesador en % se muestra encerrado en rojo en la siguiente foto, correspondiendo a un uso completo de los 2 procesadores al haber variado entre ~180 y ~200%:


![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%205/Grafico%20E5.2%20Ax_B_Parte1.png )

<br>

# MCOC2020-P0

# E6 - Desempeño Ax=B (Parte 2)

### Metodos Utilizados

En esta entrega se han probado distintos metodos para resolver un sistema Ax=B, donde A es una matriz laplaciana (entrega 4) y B es un vector de componentes unitarios. Para cada metodo utilizado, se han realizado 10 corridas para matrizes de hasta tamaño N=10.000 y luego se calculo el promedio para obtener un resultado mas exacto y representativo del tiempo transcurrido durante la ejecucion de las operaciones. Los metodos utilizados fueron los siguientes:<br>


1. SOLUCION CON NUMPY - INVERTIR MATRIZ APARTE ( np.linalg.inv(A) )<br>

2. SOLUCION CON NUMPY - FUNCION SOLVER  ( np.linalg.solve(A,B) )<br>

3. SOLUCION CON SCIPY - INVERTIR MATRIZ APARTE ( sp.linalg.inv(A) )<br>

4. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / GENERIC MATRIX  ( sp.linalg.solve(A,B) )<br>

5. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / GENERIC MATRIX  ( sp.linalg.solve(A,B) )<br>

6. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / SYMETRIC MATRIX  ( sp.linalg.solve(A,B) )<br>

7. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / SYMETRIC MATRIX  ( sp.linalg.solve(A,B) )<br>

8. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / POSITIVE DEFINITE MATRIX  ( sp.linalg.solve(A,B) )<br>

9. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / POSITIVE DEFINITE MATRIX  ( sp.linalg.solve(A,B) )<br>

### Grafico Obtenido

En esta entrega el grafico ploteado es el siguiente:

![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%206/Grafico%20E6.1.png )


Los resultados esperados eran que los metodos mas lentos fuesen el (1) y el (3), es decir, aquellos que realizaban la inversion de la matriz para luego multiplicarla por el vector B y así obtener el resultado. Esta prediccion se cumplio y para valores altos de N (tamaño de la matriz) el grafico indica que el metodo de numpy es mas lento que el metodo de scipy, es decir, al parecer scipy tiene un mejor algoritmo de inversion de matrices de gran tamaño que numpy. Aún así, para valores de N < 1000 el metodo mas lento, con diferencia, es el de inversion de matrices de scipy (3).

Otro aspecto interesante que no está de más destacar (ya que se vio en la entrega pasada) es la gran diferencia de tiempos que hay entre el metodo de numpy de inversion de matrices (1) y el metodo de numpy de solver (2). Queda una vez más demostrado, por muy trivial que parezca; que la solucion mas conveniente en terminos de "rapidez computacional" es *NO* invertir directamente la matriz, si es que no se va a utilizar entera.

Luego, con respecto a los metodos de SCIPY utilizados, los metodos que tenian la opcion de OVERWRITE = TRUE se mantuvieron muy a la par con los que tenian OVERWRITE = FALSE, ya que el mayor impacto que tiene esta opcion es en el uso de la memoria durante la ejecucion del programa. Sin embargo, al realizar la comparacion entre ***El tipo de matriz*** que se utiliza en el solver, las diferencias fueron bastante marcadas. El metodo mas rapido fue el que asumia una matriz Definida Positiva (color verde), luego le siguio el metodo que asumia una matriz Simetrica (color rojizo), y finalmente el metodo mas lento entre ellos fue el que asumia una matriz Generica. 

Este ultimo resultado cumplio con las expectativas ya que, por ejemplo, si al metodo le decimos que se trata de una matriz cualquiera o generica, se demorará menos que si le decirmos que se trata de una matriz simetrica, en la que quizas se puedan tomar "atajos" para resolver el sistema. De cualquier forma, investigando un poco en la pagina de scipy, las posibles opciones de resolucion son:


1. assume_a='gen' : Asumen una matriz Generica, y la solucion se obtiene llamando a la rutina de bajo nivel de LA-PACK --> "?GESV"
2. assume_a='sym' : Asumen una matriz Simetrica, y la solucion se obtiene llamando a la rutina de bajo nivel de LA-PACK --> "?SYSV"
3. assume_a='her' : Asumen una matriz Hermitiana {Mi Python no pudo usar esta Funcion} 
4. assume_a='pos' : Asumen una matriz Definida Positiva, y la solucion se obtiene llamando a la rutina de bajo nivel de LA-PACK --> "?POSV"

El nombre de estas rutinas de LA-PACK ***? X X Y Y*** significa lo siguiente:<br>
* ? : representa el tipo de dato que se utiliza (S:	REAL / D:	DOUBLE PRECISION / C:	COMPLEX / Z: COMPLEX*16 or DOUBLE COMPLEX)<br>
* XX: significa el tipo de matriz utilizada ( GE: general / SY: simetrica / PO: Definida Positiva / TR: Triangular ... etc)<br>
* YY: Las ultimas letras (a veces pueden ser 3 letras) representan el metodo computacional usado y se aprovecha de las propiedades del esquema o estructura matricial indicado. Según la libreria, SV significa *simple driver* , que resuelve el sistema AX = B mediante la factorizacion de A y la sobreescritura de B con la solucion X (si no es indicado de forma contraria).<br>



### Analisis de Performance CPU


Al inicio de la ejecucion del programa, se tuvo un peak jamas antes visto de 298% de uso de CPU , lo que entiendo que significa que se estan usando los dos nucleos que tengo y un hilo. Este comportamiento se mantuvo hasta que el tamaño de las matrices N sobrepasó los 2000 y se estabilizo entre 170% y 200%, utilizando la totalidad de los nucleos. Como siempre, es necesario recordar que el computador esta haciendo otras cosas por detras y esto puede afectar el rendimiento (lo cual ya se ha explicado en entregas anteriores de como afecta a los tiempos transcurridos).





![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%206/Grafico%20E6.2.png )

<br>



