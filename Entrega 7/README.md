
# E7 - Matrices dispersas y complejidad computacional 





### 1️⃣ Complejidad algoritmica de MATMUL


![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%207/Grafico%20E7.1.png )

1. **COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS MATMUL**<br>

Las principales diferencias entre los algoritmos son:
* El tiempo de ensamblado para matrices llenas es mucho menor que para matrices dispersas. Por ejemplo, para N=20.000, las matrices llenas se demoraron 0.1s, mientras que las matrices dispersas se demoraron casi 1 minuto.
* El ensamblado de las matrices dispersas es mas uniforme que el de matrices llenas que tiene mucha variabilidad. 
* En el caso de las matrices llenas, a medida que aumenta el N, el tiempo de ensamblado se mantiene un poco más constante que en el caso de las matrices dispersas, que aumenta significativamente a medida que aumenta el tamaño N de las matrices.
* En el tiempo de solucion, las matrices dispersas se mantienen en tiempos un poco (muy poco) menores, y con menos outliers que las matrices llenas.
<br>

2. **ESTIMAR Y EXPLICAR LA COMPLEJIDAD ENSAMBLADO/SOLUCION EN AMBOS CASOS**<br>

* TIEMPO DE ENSAMBLADO
    * En el caso del tiempo de ensamblado para matrices llenas, el comportamiento de complejidad asintotico es O(N) cuando N es muy grande, ya que el algoritmo utilizado para ensamblar la matriz laplaciana aprovecha al máximo los recursos y estructura matricial, sin utilizar _for_ y ciclos iterativos.
   
    * En el caso del tiempo de ensamblado para matrices dispersas, el comportamiento de complejidad asintotico es O(N²) cuando N es muy grande, ya que el algoritmo para ensamblar las matrices laplacianas dispersas contiene varios ciclos iterativos _for_, lo que hacen que sea mas lento, y que el tiempo que tarda sea mayor a medida que aumenta N. Especificamente son dos ciclos de recorrido así que puede ser que producto de esas dos iteraciones, de como resultado este tiempo O(N²).
    
* MATRICES DISPERSAS
    * Tanto para matrices llenas como para matrices dispersas, el comportamiento de complejidad asintotico es O(N³) cuando N es muy grande. Es decir, cada vez que aumentamos en N el tamaño de la matriz, el tiempo que tarda el software en resolver la operacion, esta condicionado aritmeticamente a ser ***al cubo*** de cada incremento que le demos a N. En la practica se han desarrollado varios algoritmos cada vez mas rapidos como el Coppersmith–Winograd algorithm que es de orden O(N^2.3).
<br>

3. **COMO AFECTA EL TAMAÑO DE LAS MATRICES N AL COMPORTAMIENTO APARENTE**<br>
* Como indican los graficos, el tamaño de la matriz es directamente proporcional al tiempo que se tarda, tanto en ensamblar la matriz, como en resolver la operacion de multiplicarlas.  Pareciera ser que para valores de N < 1000, los tiempos que tarda en esamblar las matrices llenas tiene mas variabilidad. De todas formas, como ya se ha mencionado, el tiempo de ensamble para este tipo de matrices se mantiene mas "constante" que el del otro algoritmo. Cabe destacar que para valores pequeños de N, el tiempo de ensamblado y solucion en ambos casos es muy alto y eso se explica con que el computador no esta solamente dedicado a la operacion que se le indica, si no que previamente ( y durante ) esta realizado otras operaciones por detras.
<br>

4. **COMENTAR ACERCA DE LA ESTABILIDAD DE LAS CORRIDAS (NCORRIDAS = 5)**<br>

* En el tiempo de solucion (multiplicar las matrices), las corridas se vuelven estables a partir de N=200-500, y se apegan mucho a la recta asintotica de complejidad O(N³). Esto puede deberse a que el alogritmo se vuelve eficiente a partir de tamaños mas grandes de matrices, y tambien hay que recordar que el computador realiza paralelamente otras operaciones. Cabe destacar que el algoritmo de ensamblado y solucion de las matrices dispersas se aprovecha de la estructura de la matriz, "sabiendo" que tiene muchos ceros e "ignorandolos" de cierta forma, lo que hace que la corridas sean mas estables y no se esta ocupando memoria ni procesador para elementos de la matriz que son "inutiles".
<br>





### 2️⃣ Complejidad algorítmica de SOLVE
A partir de aqui el analisis será mas simple ya que se han discutido anteriormente puntos esenciales de los algoritmos que se conservan a traves de las distintas operaciones (multiplicacion, inversion, y solucion de sistemas)

![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%207/Grafico%20E7.2.png )


1. **COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS SOLVE**<br>

* El tiempo de ensamblado para matrices llenas es mas constante y mucho menor que para matrices dispersas.
* El tiempo de solucion para invertir matrices llenas es mas variable, pero tarda menos en ejectuarse y estabilizarse asintoticamente que el tiempo de inversion de matrices dispersas.

<br>

2. **ESTIMAR Y EXPLICAR LA COMPLEJIDAD ENSAMBLADO/SOLUCION EN AMBOS CASOS**<br>

* En el caso de matrices llenas, el tiempo de ensamblado es asintoticamente O(N) por la efectividad del algoritmo utilizado. En cuanto al tiempo de solucion para invertir la matriz se utilizan algoritmos de scipy que permiten que asintoticamente el tiempo sea O(N³). Según he investigado este tipo de algoritmo puede ser el de eliminacion gaussiana. En terminos simples, a medida que aumentamos el tamaño de la matriz N, el tiempo que tarda en invertirse esta dado deacuerdo a una funcion al cubo del valor de N. 

* En el caso de matrices dispersas, el tiempo de ensamblado es asintoticamente O(N²) por los ciclos for que ya se han explicado. Mientras que el tiempo de solucion de inversion es de O(N³) al igual que en las matrices llenas. Aqui el tiempo que tardan las corridas es un poco mayor debido a que en el codigo de python se esta transformando la matriz al tipo csc, es decir, hay pasos adicionales en el algoritmo para solucionarlo ya que de otra forma el programa tira error. 
<br>

3. **COMO AFECTA EL TAMAÑO DE LAS MATRICES N AL COMPORTAMIENTO APARENTE**<br>

* Para todos los casos realizados en este ejercicio, cuando el N es pequeño, el tiempo de ejecucion (ensamble o solucion) es muy alto en comparacion al resto de tiempos y esto es por razones que ya se han explicado de que el computador esta realizando mas operaciones ademas de las de python en un inicio. Luego, a medida que N aumenta, se puede ver que en el caso de las matrices llenas, el tiempo de ensamblado es bastante variable pero se mantiene sin aumentar o disminuir mucho durante la ejecucion. Para todos los casos, cuando el N es muy grande, las corridas tienen tiempos muy parecidos entre si.
<br>

4. **COMENTAR ACERCA DE LA ESTABILIDAD DE LAS CORRIDAS (NCORRIDAS = 5)**<br>

* Las corridas se vuelven muy estables a partir de N=200 en el caso del ensamble de matrices dispersas. Así mismo ocurre en el caso del tiempo de solucion para matrices llenas a partir de valores de N=500. Y en cuanto al tiempo de solucion de las matrices dispersas, todas las corridas son muy muy parecidas entre sí lo que indica que el algoritmo es muy estable y esto se debe a que se aprovecha de la estructura dispersa de la matriz, es decir; como se ha mencionado, no se pierde CPU ni memoria innecesaria cuando se le dice al programa que la matriz tiene componentes "inutiles". No obstante, no por esta razon el algoritmo se vuelve mas rapido, que es lo que podría esperarse, si no que, es un poco mas lento y esto se puede deber a que hay un "trade off" entre estos dos parametros (estabilidad y velocidad) o bien, es porque hay mas operaciones invlucradas al momento de definir que la matriz es de tipo especial (csc_matrix).
<br>





### 3️⃣ Complejidad algorítmica de INV


![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%207/Grafico%20E7.3.png )


1. **COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS INV**<br>

* El tiempo de ensamblado para matrices llenas sigue siendo menor y mas constante que el de matrices dispersas, aunque tiene un poco mas de variabilidad entre las corridas.
* El tiempo de solucion en el algoritmo de matrices dispersas es significativamente menor que en el caso de matrices llenas, incluso la complejidad asintotica es absolutamente distinta (eso se discute a continuacion)
<br>

2. **ESTIMAR Y EXPLICAR LA COMPLEJIDAD ENSAMBLADO/SOLUCION EN AMBOS CASOS**<br>

* En el caso del tiempo de ensamblado, para matrices llenas, sigue siendo asintoticamente O(N), y en el caso de las matrices dispersas, sigue siendo del tipo O(N²) ya que nada ha cambiado en este punto de las operaciones pero si puedo agregar que el último es un poco mayor ya que se realiza una transformacion a la matriz A al tipo csr_matriz.
* En el caso del tiempo de solucion, las matrices llenas siguen una complejidad asintotica de O(N³) casi inmediatamente a partir de N = 500, mientras que en el caso de las matrices dispersas siguen una complejidad asintotica impresionante de O(N). Este cambio brutal se debe a que en el ultimo caso, el solver de scipy aprovecha al máximo la estructura de la matriz y sabe que tiene elementos nulos que no sirven, por lo tanto da como resultado un algoritmo en que el tiempo  aumenta linealmente a medida que aumentamos el tamaño de la matriz, en vez de aumentar al cubo como lo hace el algoritmo para matrices llenas.
<br>

3. **COMO AFECTA EL TAMAÑO DE LAS MATRICES N AL COMPORTAMIENTO APARENTE**<br>

* Como es de esperar , a medida que aumenta el tamaño de las matrices, el tiempo de solucion tambien aumenta, aunque no de forma tan significativa en el caso del tiempo de ensamblado de matrices llenas (como ya se ha explicado) y tampoco lo hace significativamente en el caso del tiempo de solucion de matrices dispersas. Podemos notar que para valores de N entre 2 y 2000, el tiempo se mantiene muy por debajo de los 10 ms en todas las corridas, mientras que en el caso de las matrices llenas, el tiempo de solucion aumenta mucho a partir de N = 200. Esto se debe a la complejidad asintotica que tienen y ya se ha explicado anteriormente.
<br>

4. **COMENTAR ACERCA DE LA ESTABILIDAD DE LAS CORRIDAS (NCORRIDAS = 5)**<br>

* En cuanto al ensamble de matrices, las corridas nunca son 100% estables en el caso de las matrices llenas, es decir, que en todos los graficos se puede apreciar mucha mas variabilidad que en el caso de las matrices dispersas, las cuales en este caso de solucion de sistemas de ecuaciones, presenta una estabilidad entre corridas sorprendente desde los primeros valores. Como ya se ha mencionado, esto resulta ser así debido a la estructura dispersa que tiene la matriz y como "le decimos a python donde va cada elemento" de forma que no gaste memoria o CPU innecesariamente.

* La estabilidad para la solucion de sistema en este caso, es bastante alta para las matrices dispersas a partir de valores N=200 aproximadamente, mientas que para el caso de las matrices llenas, existe bastante variabilidad en un principio pero se vuelven mas parecidos los valores del tiempo de solucion a medida que N alcanza valores de 1000 aproximadamente. 

<br>
<br>

### 👾 CODIGO DE ENSAMBLAJE DE MATRICES LAPLACIANAS:

* El codigo utilizado para matrices llenas fue:

```
from numpy import *
from numpy import float32,float64,double, ones
from scipy.sparse import *
from scipy.sparse import lil_matrix
from time import perf_counter
from matplotlib import pyplot as plt
import matplotlib.ticker

def matriz_laplaciana_llena(N,dtype=double):
    return diags(array([-ones(N-1),2*ones(N),-ones(N-1)]),[-1,0,1],dtype=dtype).toarray()
    
```
* El codigo utilizado para matrices dispersas fue:

```
from numpy import *
from numpy import float32,float64,double, ones
from scipy.sparse import *
from scipy.sparse import lil_matrix
from time import perf_counter
from matplotlib import pyplot as plt
import matplotlib.ticker
from scipy.sparse import csc_matrix, csv_matrix


def matriz_laplaciana_dispersa(N,dtype=double):
    A = lil_matrix((N,N),dtype=dtype)
    for i in range(N):
        for j in range(N):  
            if i == j:
                A[i,j]=2    
            if i+1 == j:
                A[i,j]=-1
            if i-1 == j:
                A[i,j]=-1
    return A.toarray()
    
```
<br>

* Como ya se ha mencionado, el primer algoritmo de ensamble de matrices llenas aprovecha al maximo la estructura de la matriz mediante el uso de librerias de numpy y scipy, sin utilizar ciclos iterativos for que recorran la matriz varias veces para ir asignando valores a los elementos. Esto tiene un gran impacto en el tiempo usado para ensamblar las matrices, ya que resulta ser mucho menor que si se utilizara "python puro" o algun otro algoritmo.

* En cuanto al segundo algoritmo, de ensamble de matrices dispersas, se debe tener en cuenta de que mientras mas ciclos iterativos tenga, mas lento será el ensamble de matrices, ya que se esta recorriendo una lista de tamaño N y luego se checkea si los elementos coinciden o no coinciden para luego recien asignarle valor. Esto hace que el algoritmo sea mucho mas lento que en el caso de las matrices llenas, a pesar de que se este aprovechando mejor la estructura de la matriz. 



