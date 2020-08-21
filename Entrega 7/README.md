
# E7 - Matrices dispersas y complejidad computacional 





### 1️⃣ Complejidad algoritmica de MATMUL


![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%207/Grafico%20E7.1.png )

1. **COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS MATMUL**<br>

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







### 2️⃣ Complejidad algorítmica de SOLVE


* _Grafico Complejidad SCIPY SOLVE LLENA_
* _Grafico Complejidad SCIPY SOLVE DISPERSA_


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



* _Grafico Complejidad SCIPY INV LLENA_
* _Grafico Complejidad SCIPY INV DISPERSA_


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

