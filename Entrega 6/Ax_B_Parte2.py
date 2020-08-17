import numpy as np
import scipy as sp
import scipy.linalg as splinalg
from scipy.sparse import *
from numpy import float32
from time import perf_counter
import matplotlib.ticker
from matplotlib import pyplot as plt
import sys


def LAP_MAT(N,dtype=float32):
    return diags(np.array([-np.ones(N-1),2*np.ones(N),-np.ones(N-1)]),[-1,0,1],dtype=dtype).toarray()



Ns = [2,10,50,100,300,800,1000,1500,2000,3000,5000,7000,10000]

Ncorridas = 10

colors = ["c","skyblue","black","purple","plum","crimson","tomato","darkgreen","greenyellow"]
 
names = [            "A_invB_NUMPY_INV.txt",
                     "A_invB_NUMPY_SOLVER.txt",
                     "A_invB_SCIPY_INV.txt",
                     "A_invB_SCIPY_OverwriteOFF_GEN.txt",
                     "A_invB_SCIPY_overwriteON_GEN.txt",
                     "A_invB_SCIPY_overwriteOFF_SYM.txt",
                     "A_invB_SCIPY_overwriteON_SYM.txt",
                     "A_invB_SCIPY_overwriteOFF_POS.txt",
                     "A_invB_SCIPY_overwriteON_POS.txt"
                     
                     ]



fancynames = [       "NP INV",
                     "NP SOLVER",
                     "SP INV",
                     "SP SOLVER overwrite OFF - GEN",
                     "SP SOLVER overwrite ON - GEN",
                     "SP SOLVER overwrite OFF - SYM",
                     "SP SOLVER overwrite ON - SYM",
                     "SP SOLVER overwrite OFF - POS",
                     "SP SOLVER overwrite ON - POS"
                     ]





files = [ open(name,"w") for name in names ]

for N in Ns:
    dts = np.zeros((Ncorridas,len(files)))

    
    print (f"N={N}")
    
    for i in range(Ncorridas):
        print (f"i={i}")
        
        

        """
        1. SOLUCION CON NUMPY - INVERTIR MATRIZ APARTE:
        
        Para resolver el sistema Ax = B
        
        Este solver ocupa la funcion lingalg.inv(A) de numpy para invertir A 
        y luego multiplicar a ambos lados de la expresion "despejando" el valor
        del vector x que se quiere encontrar. De esta forma, se estan usando dos vectores 
        (el vector B y el vector solucion x) y dos matrices (la matriz A inicial y la 
        matriz inversa de A) en total para los datos.
            
            
    
        """
        A = LAP_MAT(N)
        B = np.ones(N)
        t1=perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv @ B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt
        







        
        """
        2. SOLUCION CON NUMPY - FUNCION SOLVER:
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.solve(,) de numpy para encontrar
        directamente la solucion del sistema sin tener que crear una matriz
        inversa aparte. Por esta razon la prediccion al compararlo con el metodo 1
        es que sera mas rapido y ocupara menos memoria. 
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1] = dt
        



        """
        3. SOLUCION CON SCIPY - INVERTIR MATRIZ APARTE:
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.inv() de SCIPY para invertir
        la matriz y luego multiplicarla por el vector B para encontrar la
        solucion.
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        
        t1 = perf_counter()
        
        A_inv = splinalg.inv(A)
        A_invB = A_inv @ B
        
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][2] = dt
        


        """
        4. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / GENERIC MATRIX :
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.solve de SCIPY para
        resolver el sistema sin invertir directamente A.
        
        Las opciones usadas son:  scipy.linalg.solve(A, B, overwrite_a=False, overwrite_b=False, assume_a='gen')
        
            * SIN OVERWRITE
            * ASUMIENDO MATRIZ GENERICA
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        
        t1 = perf_counter()
        
        A_invB = splinalg.solve(A,B,overwrite_a=False,overwrite_b=False,assume_a='gen')
        
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][3] = dt
        
        
        
        
        

        """
        5. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / GENERIC MATRIX :
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.solve de SCIPY para
        resolver el sistema sin invertir directamente A.
        
        Las opciones usadas son:  scipy.linalg.solve(A, B, overwrite_a=True, overwrite_b=True, assume_a='gen')
        
            * CON OVERWRITE
            * ASUMIENDO MATRIZ GENERICA
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        
        t1 = perf_counter()
        
        A_invB = splinalg.solve(A,B,overwrite_a=True,overwrite_b=True,assume_a='gen')
        
        t2 = perf_counter()
        
        dt = t2 - t1
        dts[i][4] = dt
        
        
        
        
        
        """
        6. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / SYMETRIC MATRIX :
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.solve de SCIPY para
        resolver el sistema sin invertir directamente A.
        
        Las opciones usadas son:  scipy.linalg.solve(A, B, overwrite_a=False, overwrite_b=False, assume_a='sym')
        
            * SIN OVERWRITE
            * ASUMIENDO MATRIZ SIMETRICA
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        
        t1 = perf_counter()
        
        A_invB = splinalg.solve(A,B,overwrite_a=False,overwrite_b=False,assume_a='sym')
        
        t2 = perf_counter()
        
        dt = t2 - t1
        dts[i][5] = dt
        
        
        
        
        
        
        
        
        """
        7. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / SYMETRIC MATRIX :
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.solve de SCIPY para
        resolver el sistema sin invertir directamente A.
        
        Las opciones usadas son:  scipy.linalg.solve(A, B, overwrite_a=True, overwrite_b=True, assume_a='sym')
        
            * CON OVERWRITE
            * ASUMIENDO MATRIZ SIMETRICA
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        
        t1 = perf_counter()
        
        A_invB = splinalg.solve(A,B,overwrite_a=True,overwrite_b=True,assume_a="sym")
        
        t2 = perf_counter()
        
        dt = t2 - t1
        dts[i][6] = dt

        """
        8. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / DEF POS MATRIX :
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.solve de SCIPY para
        resolver el sistema sin invertir directamente A.
        
        Las opciones usadas son:  scipy.linalg.solve(A, B, overwrite_a=False, overwrite_b=False, assume_a='pos')
        
            * SIN OVERWRITE
            * ASUMIENDO MATRIZ DEF POS
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        
        t1 = perf_counter()
        
        A_invB = splinalg.solve(A,B,overwrite_a=False,overwrite_b=False,assume_a="pos")
        
        t2 = perf_counter()
        
        dt = t2 - t1
        dts[i][7] = dt


        """
        9. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / DEF POS MATRIX :
        
        Para resolver el sistema Ax = B
        
        Este solver usa la funcion linalg.solve de SCIPY para
        resolver el sistema sin invertir directamente A.
        
        Las opciones usadas son:  scipy.linalg.solve(A, B, overwrite_a=True, overwrite_b=True, assume_a='pos')
        
            * CON OVERWRITE
            * ASUMIENDO MATRIZ DEF POS
        
        """

        A = LAP_MAT(N)
        B = np.ones(N)
        
        t1 = perf_counter()
        
        A_invB = splinalg.solve(A,B,overwrite_a=True,overwrite_b=True,assume_a="pos")
        
        t2 = perf_counter()
        
        dt = t2 - t1
        dts[i][8] = dt






        
    print ("dts: ",dts)

    
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]

    
    print ("dts_mean: ", dts_mean)

    
    for j in range (len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()
        
[ file.close() for file in files ]








plt.figure(figsize=(8,10))

for name in names:
    datos = np.loadtxt(name)
    MNL = datos[:, 0]
    MTL = datos[:, 1]
    
    plt.loglog(MNL,MTL,"--o",color=colors[names.index(name)],label=fancynames[names.index(name)])
    plt.ylabel("Tiempo Transcurrido",fontweight = 'bold',fontsize=15)
    plt.xlabel("\nTamaño de la Matriz N",fontweight = 'bold',fontsize=15)
    plt.grid(True)
    plt.xticks(MNL,MNL,rotation=90,fontweight = 'bold')
    plt.yticks([0.1e-3,0.25e-3,0.5e-3, 1e-3,2.5e-3,5e-3,1e-2,2.5e-2,0.1,0.25,1,2.5,10,60,60*10],['0.1 ms','0.25 ms','0.5 ms',"1 ms","2.5 ms",'5 ms',"10 ms","25 ms","0.1 s","0.25 s","1 s","2.5 s","10 s", "1 min"],fontweight = 'bold')
    plt.legend(loc="upper left", bbox_to_anchor=[0, 1], ncol=2, shadow=True,fontsize=10 ,title="Metodo de Solucion", fancybox=True)

plt.title('Desempeño Solvers Ax=b \n [Max Poblete – Macbook Pro 13"]\n', fontsize=15,fontweight = 'bold')
plt.ylabel('Tiempo Transcurrido',fontsize=15,fontweight = 'bold')
plt.xlabel('\nTamaño de la Matriz N',fontsize=15,fontweight = 'bold')
plt.savefig('Grafico General.png', dpi=500)
plt.tight_layout()
plt.show()



    