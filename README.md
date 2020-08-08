# MCOC2020-P0

# E1 - Mi computador principal

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


# E2 - Desempeño MATMUL

![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/MP_timing_matmul.png)

* ¿Como difiere del gráfico del profesor/ayudante?
  * 👉 En primer lugar se puede apreciar que para valores pequeños de N, de entre 2 y 3, se tiene que el tiempo transcurrido puede alcanzar hasta cuatro ordenes de magnitud mas grandes. Sin embargo, a medida que N aumenta hacia valores cercanos a 100, el tiempo transcurrido para el profesor es levemente mayor (1 o 2 ordenes de magnitud) alcanzando los 10 ms, mientras que en mi grafico se puede apreciar que no se alcanza 1 ms. Ocurre de forma similar para N = 200. Por otro lado, a partir de valores de N=2000 la situacion se vuelve a dar vuelta, en la que mi grafico indica que mi computador se tarda un poco mas en realizar las operaciones. Finalmente, un aspecto interesante que se puede apreciar es que el grafico del profesor presenta mayor variabilidad en los tiempos de ejecucion, mientras que en mi grafico se muestra que los tiempos transcurridos se mantienen un poco "mas constantes" en general. Cabe destacar que el limite de N lo puse en 8000 en vez de 20000 para que sobrepasara la memoria que dispongo.
  
* ¿A qué se pueden deber las diferencias?
  * 👉 Estas diferencias se pueden deber principalmente a que en general mi computador es menos potente; solamente tiene 2 nucleos, de menor velocidad (máx 3.5 GHz) y posee menor memoria RAM (8 GB). Para el valor de N=2 la exigencia es tan poca que el computador no es tan generoso con el uso de la CPU para realizar la operacion y al tener menor capacidad el tiempo puede parecer mas alto, sin embargo, para valores mayores (N=10 - N=1000), el computador empieza a entregar mayor CPU al programa para realizar las operaciones y lo hace sin problema. Lo que puede explicar la mayor "estabilidad" de mi grafico entre esos valores de N, es la generacion del procesador, ya que el mio es de 7ma generacion con tecnologia de 14 nm , mientras que el procesador del profesor es de 4ta generacion con tecnologia de 22 nm. No obstante, el procesador del profesor sigue siendo mas potente y esto se demuestra al aumentar N por sobre los 2000, teniendo tiempos de operacion un poco menores. (Igual mi compu se defiende! jajaj estoy orgulloso). 
  
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * 👉 El grafico de uso de memoria resulta ser lineal (y de cierta forma igual que el del profesor) ya que la memoria utilizada por las matrices es la misma. Esto se debe a que, independiente del valor numerico de los elementos matriciales, cada uno es un componente float que ocupa 8 bytes de almacenamiento. De esta manera, al ser 3 matrices, cada una de N filas y N columnas, se obtiene que la cantidad de memoria se puede calcular mediante la siguiente formula general: 
  
  * Memoria utilizada = (k)· (N^2) · (8) 
  * DONDE <br>[k: numero de matrices involucradas (en este caso 3, la matriz A, la matriz B y la matriz C, resultante de la multiplicacion entre A y B)]<br>
  [N^2: numero de elementos totales de una matriz de N filas por N columnas]<br>
  [8: representa los bytes utilizados por cada elemento, en este caso son 8 bytes porque cada elemento es un float]<br>
      
* ¿Qué versión de python está usando?
  * 👉 Estoy utilizando Python 3.8 en Spyder 4.1.4, mediante Anaconda 1.9.12.
  
* ¿Qué versión de numpy está usando?
  * 👉 La version de Numpy utilizada es 1.18.5
  
* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
  * 👉 Si la pregunta es "¿se utiliza mas de un *nucleo?", por su puesto que si; en el monitor de actividad se puede apreciar que el porcentaje de uso esta entre 170-200% lo que indicaría que se usan todos los nucleos de mi procesador. Pero si la pregunta es "¿se utiliza más de un procesador?", la respuesta es que, tengo 1 solo procesador y lo uso completo.
  
  ![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E2.2.png)
  
