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
      
      
### ¿Qué versión de python está usando?
  * 👉 Estoy utilizando Python 3.8 en Spyder 4.1.4, mediante Anaconda 1.9.12.
  
  
### ¿Qué versión de numpy está usando?
  * 👉 La version de Numpy utilizada es 1.18.5
  
  
### Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
  * 👉 Si la pregunta es "¿se utiliza mas de un nucleo?", la respuesta es si; en el monitor de actividad se puede apreciar que el porcentaje de uso esta entre 170-200% lo que indicaría que se usan todos los nucleos de mi procesador (que son 2 nucleos). Pero si la pregunta es "¿se utiliza más de un procesador?", la respuesta es que, tengo 1 solo procesador y lo uso completo.
  
  
  ![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Grafico%20E2.2.png)
  
