import scipy as sp
from scipy import matmul, rand,float64,float32,float16,int16,int32,int64, zeros, linalg

import numpy as np
from numpy import double, half, single, longdouble, fill_diagonal

import matplotlib.ticker
from matplotlib import pyplot as plt

from time import perf_counter


import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning) 

print ("running")

def lapmat(N,dtype=float32):
    MATRIZ = zeros((N,N),dtype=dtype)
    fill_diagonal(MATRIZ,2)
    for i in range(N):
        for j in range(N):
            if i+1 == j or i-1 == j:
                MATRIZ[i][j]=-1
    return (MATRIZ)


MNL = [2,10,50,100,300,800,1000,1500,2000]
MTL = []
MML = []

tipoDeDato = sp.half


Ncorridas = 10 

for corrida in range(Ncorridas):
    
    MTL_temp = []
    MML_temp = []

    for N in MNL: 
        A = lapmat(N,tipoDeDato)
        t1 = perf_counter()
        C =  sp.linalg.inv(A,overwrite_a=False)   
        t2 = perf_counter()
        dt = t2 - t1
        
        MTL_temp.append(dt)
        totalmemory = 0
        for i in range(N):
            for j in range(N):
                totalmemory += sys.getsizeof(A[i][j])
        size = 2*totalmemory # Ya se incluye el N*N*BytesDelTipoDeDato
        MML_temp.append(size)
    
    MTL.append(MTL_temp)
    MML.append(MML_temp)
        

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

    
    axes[1].plot(MNL,MML[i],"--o")
    axes[1].set_xscale("log")
    x = MNL
    axes[1].set_xticks(x)
    axes[1].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axes[1].set_xticklabels(x,rotation=45,fontweight = 'bold')
    
    y1 = [ 10**3, 10**4   ,10**5 , 10**6  ,10**7  ,10**8  ,10**9 ,8*10**9 ,10**11]
    yl = ['1 KB',"10 KB","100 KB","1 MB","10 MB","100 MB", "1 GB", "8 GB","100 GB"]
    axes[1].set_yscale("log")
    axes[1].set_yticks(y1)
    axes[1].set_yticklabels(yl,fontweight = 'bold')


axes[1].axhline(8*(10**9),0,1000,ls="--",c="r",lw=3)
axes[0].set_title('RENDIMIENTO CASO 2 - HALF \n [Max Poblete – Macbook Pro 13"]', fontsize=15,fontweight = 'bold')
axes[0].set_ylabel('Tiempo Transcurrido',fontsize=15,fontweight = 'bold')
axes[1].set_ylabel('Uso de Memoria',fontsize=15,fontweight = 'bold')
axes[1].set_xlabel('Tamaño de la Matriz (N)',fontsize=15,fontweight = 'bold')
axes[0].grid()
axes[1].grid()

axes[1].get_yticklabels()[7].set_color('red') 

plt.savefig('timing_inv_caso_2_half.png', dpi=400)
plt.show()



    
    
    
    













