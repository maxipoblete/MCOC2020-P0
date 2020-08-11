# 88888888888                                                                              ad888888b,  
# 88                          ,d                                                          d8"     "88  
# 88                          88                                                                  a8P  
# 88aaaaa      8b,dPPYba,   MM88MMM  8b,dPPYba,   ,adPPYba,   ,adPPYb,d8  ,adPPYYba,           aad8"   
# 88"""""      88P'   `"8a    88     88P'   "Y8  a8P_____88  a8"    `Y88  ""     `Y8           ""Y8,   
# 88           88       88    88     88          8PP"""""""  8b       88  ,adPPPPP88              "8b  
# 88           88       88    88,    88          "8b,   ,aa  "8a,   ,d88  88,    ,88      Y8,     a88  
# 88888888888  88       88    "Y888  88           `"Ybbd8"'   `"YbbdP"Y8  `"8bbdP"Y8       "Y888888P'  
#                                                             aa,    ,88                               
#                                                              "Y8bbdP"                                

#   __  __                  _               _   _   _                             _____            _       _          _          
#  |  \/  |                (_)             (_) | | (_)                           |  __ \          | |     | |        | |         
#  | \  / |   __ _  __  __  _   _ __ ___    _  | |  _    __ _   _ __     ___     | |__) |   ___   | |__   | |   ___  | |_    ___ 
#  | |\/| |  / _` | \ \/ / | | | '_ ` _ \  | | | | | |  / _` | | '_ \   / _ \    |  ___/   / _ \  | '_ \  | |  / _ \ | __|  / _ \
#  | |  | | | (_| |  >  <  | | | | | | | | | | | | | | | (_| | | | | | | (_) |   | |      | (_) | | |_) | | | |  __/ | |_  |  __/
#  |_|  |_|  \__,_| /_/\_\ |_| |_| |_| |_| |_| |_| |_|  \__,_| |_| |_|  \___/    |_|       \___/  |_.__/  |_|  \___|  \__|  \___|
                                                                                                                               
                                                                                                                               


from scipy import *
from time import perf_counter
import warnings
from matplotlib import pyplot as plt
import matplotlib.ticker

warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 



"""
En primer lugar queremos definir una funcion que sirva para multiplicar matrices
de orden NxN implementando python puro.
"""


def mimatmul(A,B):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            elemento = 0
            for m in range(len(A[0])):
                elemento += ((A[i][m]*B[m][j]))    
            fila.append(elemento)
        matriz.append(fila)
    return (matriz)



"""
El resultado de la multiplicacion es una lista de listas, que en python puro podemos
interpretar como una matriz, lo que realmente nos interesa es saber cuanto se tarda
en realizar las operaciones
"""

# N=2
# A = rand(N,N)
# B = rand(N,N)  

# print (A,"\n")
# print (B,"\n")
# print (mimatmul(A,B))

# print (type(mimatmul(A,B)))



# Master N Size List
MNL = [2,3,4,5,10,30,50,100,200,250,500]

# Master Time List
MTL = []

# Master Memory Use List
MML = []


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NUMERO DE CORRIDAS A REALIZAR
Ncorridas = 10
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# CALCULADORA DE MEMORIA: En total son 3 matrices, cada una con N^2 elementos y cada uno ocupa 8 bytes
for N in MNL:
    MML.append(3*(N**2)*8) 


# CREACION Y MULTIPLICACION DE LAS MATRICES
for corrida in range(Ncorridas):
    MTL_temp = []
    for N in MNL:
            A = rand(N,N)
            B = rand(N,N)  
            t1 = perf_counter()
            C = mimatmul(A,B)  
            t2 = perf_counter()
            dt = t2 - t1
            MTL_temp.append(dt)
    MTL.append(MTL_temp)


#----------------------
#  PLOTEO DE GRAFICOS
#----------------------

fig, axes = plt.subplots(2, 1, figsize=(8,10))

for i in range(Ncorridas):
    axes[0].plot(MNL,MTL[i],"--o")
    axes[0].set_xscale("log")
    x = MNL
    
    axes[0].set_xticks(x)
    axes[0].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axes[0].set_xticklabels(" ")

    y1 = [0.1e-3, 1e-3,1e-2,0.1,1,10,60,60*10]
    yl = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s", "1 min"]
    axes[0].set_yscale("log")
    axes[0].set_yticks(y1)
    axes[0].set_yticklabels(yl,fontweight = 'bold')

    
    axes[1].plot(MNL,MML,"--o")
    axes[1].set_xscale("log")
    x = MNL
    axes[1].set_xticks(x)
    axes[1].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axes[1].set_xticklabels(x,rotation=45,fontweight = 'bold')
    
    y1 = [ 10**3, 10**4   ,10**5 , 10**6  ,10**7  ,10**8  ,10**9 ,8*10**9 ,10**11]
    yl = ['1 KB',"10 KB","100 KB","1 MB","10 MB","100 MB", "1 GB", " RAM Limite=> 8 GB","100 GB"]
    axes[1].set_yscale("log")
    axes[1].set_yticks(y1)
    axes[1].set_yticklabels(yl,fontweight = 'bold')


axes[1].axhline(8*(10**9),0,1000,ls="--",c="r",lw=3)
axes[0].set_title('RENDIMIENTO A@B [Max Poblete – Macbook Pro 13"]', fontsize=15,fontweight = 'bold')
axes[0].set_ylabel('Tiempo Transcurrido',fontsize=15,fontweight = 'bold')
axes[1].set_ylabel('Uso de Memoria',fontsize=15,fontweight = 'bold')
axes[1].set_xlabel('Tamaño de la Matriz (N)',fontsize=15,fontweight = 'bold')
axes[0].grid()
axes[1].grid()

axes[1].get_yticklabels()[7].set_color('red') 

plt.savefig('MPGraph.png', dpi=600)
# plt.show()







    
