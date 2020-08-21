
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
   
    * En el caso del tiempo de ensamblado para matrices dispersas, el comportamiento de complejidad asintotico es O(N²) cuando N es muy grande, ya que el algoritmo para ensamblar las matrices laplacianas dispersas contiene varios ciclos iterativos _for_, lo que hacen que sea mas lento, y que el tiempo que tarda sea mayor a medida que aumenta N.
    
* MATRICES DISPERSAS
    * Tanto para matrices llenas como para matrices dispersas, el comportamiento de complejidad asintotico es O(N³) cuando N es muy grande. Es decir, cada vez que aumentamos en N el tamaño de la matriz, el tiempo que tarda el software en resolver la operacion, esta condicionado aritmeticamente a ser ***al cubo*** de cada incremento que le demos a N. En la practica se han desarrollado varios algoritmos cada vez mas rapidos como el Coppersmith–Winograd algorithm que es de orden O(N^2.3).
<br>

3. **COMO AFECTA EL TAMAÑO DE LAS MATRICES N AL COMPORTAMIENTO APARENTE**<br>
Como indican los graficos, el tamaño de la matriz es directamente proporcional al tiempo que se tarda, tanto en ensamblar la matriz, como en resolver la operacion de multiplicarlas.  Pareciera ser que para valores de N < 1000, los tiempos que tarda en esamblar las matrices llenas tiene mas variabilidad. De todas formas, como ya se ha mencionado, el tiempo de ensamble para este tipo de matrices se mantiene mas "constante" que el del otro algoritmo. Cabe destacar que para valores pequeños de N, el tiempo de ensamblado y solucion en ambos casos es muy alto y eso se explica con que el computador no esta solamente dedicado a la operacion que se le indica, si no que previamente ( y durante ) esta realizado otras operaciones por detras.
<br>

4. **COMENTAR ACERCA DE LA ESTABILIDAD DE LAS CORRIDAS (NCORRIDAS = 5)**<br>

En el tiempo de solucion (multiplicar las matrices), las corridas se vuelven estables a partir de N=200-500, y se apegan mucho a la recta asintotica de complejidad O(N³). Esto puede deberse a que el alogritmo se vuelve eficiente a partir de tamaños mas grandes de matrices, y tambien hay que recordar que el computador realiza paralelamente otras operaciones. Cabe destacar que el algoritmo de ensamblado y solucion de las matrices dispersas se aprovecha de la estructura de la matriz, "sabiendo" que tiene muchos ceros e "ignorandolos" de cierta forma, lo que hace que la corridas sean mas estables y no se esta ocupando memoria ni procesador para elementos de la matriz que son "inutiles".
<br>





### 2️⃣ Complejidad algorítmica de SOLVE
A partir de aqui el analisis será mas simple ya que se han discutido anteriormente puntos esenciales de los algoritmos que se conservan a traves de las distintas operaciones (multiplicacion, inversion, y solucion de sistemas)

![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%207/Grafico%20E7.2.png )


1. **COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS SOLVE**<br>

TEXTO
<br>

2. **ESTIMAR Y EXPLICAR LA COMPLEJIDAD ENSAMBLADO/SOLUCION EN AMBOS CASOS**<br>

TEXTO
<br>

3. **COMO AFECTA EL TAMAÑO DE LAS MATRICES N AL COMPORTAMIENTO APARENTE**<br>

TEXTO
<br>

4. **COMENTAR ACERCA DE LA ESTABILIDAD DE LAS CORRIDAS (NCORRIDAS = 10)**<br>

TEXTO
<br>





### 3️⃣ Complejidad algorítmica de INV


![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%207/Grafico%20E7.3.png )


1. **COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS INV**<br>

TEXTO
<br>

2. **ESTIMAR Y EXPLICAR LA COMPLEJIDAD ENSAMBLADO/SOLUCION EN AMBOS CASOS**<br>

TEXTO
<br>

3. **COMO AFECTA EL TAMAÑO DE LAS MATRICES N AL COMPORTAMIENTO APARENTE**<br>

TEXTO
<br>

4. **COMENTAR ACERCA DE LA ESTABILIDAD DE LAS CORRIDAS (NCORRIDAS = 10)**<br>

TEXTO
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

Texto explicativo de como influye en el desempeño y complejidad algoritmica

