import numpy as np
import scipy as sp
import scipy.linalg as spLinalg
from scipy.sparse import *
from numpy import float32
from time import perf_counter
import matplotlib.ticker
from matplotlib import pyplot as plt
import sys

def LAP_MAT(N,dtype=float32):
    return diags(np.array([-np.ones(N-1),2*np.ones(N),-np.ones(N-1)]),[-1,0,1],dtype=dtype).toarray()



Ns = [2,10,50,100,300,800,1500,3000,5000,7000,10000]

Ncorridas = 10 

names = ["A_invB_inv.txt","A_invB_npSolve.txt"]

fancynames = ["Invertir Matriz","Sin Invertir Matriz"]

files = [ open(name,"w") for name in names ]

for N in Ns:
    dts = np.zeros((Ncorridas,len(files)))
    
    memorys = np.zeros((Ncorridas,len(files)))
    
    
    
    print (f"N={N}")
    
    for i in range(Ncorridas):
        print (f"i={i}")
        
        
        A = LAP_MAT(N)
        B = np.ones(N)
        t1=perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv @ B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt
        
        memorys[i][0] = 2*N*(sys.getsizeof(B[0])) + 2*N*N*(sys.getsizeof(A[0][0]))

        A = LAP_MAT(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1] = dt
        
        memorys[i][1] = 2*N*(sys.getsizeof(B[0])) + N*N*(sys.getsizeof(A[0][0]))


        
        
    print ("dts: ",dts)
    print ("memorys: ",memorys)
    
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    memorys_mean = [ np.mean(memorys[:,j]) for j in range(len(files)) ]
    
    print ("dts_mean: ", dts_mean)
    print ("memorys mean: ", memorys_mean)
    
    for j in range (len(files)):
        files[j].write(f"{N} {dts_mean[j]} {memorys_mean[j]}\n")
        files[j].flush()
        
[ file.close() for file in files ]



fig, axes = plt.subplots(2,1, figsize=(8,10))


for name in names:
    
    datos = np.loadtxt(name)
    MNL = datos[:, 0]
    MTL = datos[:, 1]
    MML = datos[:, 2]

    axes[0].plot(MNL,MTL,"--o",label=fancynames[names.index(name)])
    axes[0].set_xscale("log")
    x = MNL
    axes[0].set_xticks(x)
    axes[0].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axes[0].set_xticklabels(" ")
    axes[0].legend(loc="upper left", bbox_to_anchor=[0, 1], ncol=2, shadow=True, title="Metodo de Solucion", fancybox=True)
    
    y1 = [0.1e-3, 1e-3,1e-2,0.1,1,10,60,60*10]
    yl = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s", "1 min"]
    axes[0].set_yscale("log")
    axes[0].set_yticks(y1)
    axes[0].set_yticklabels(yl,fontweight = 'bold')


    axes[1].plot(MNL,MML,"--o",label=fancynames[names.index(name)])
    axes[1].legend(loc="upper left", bbox_to_anchor=[0, 1], ncol=2, shadow=True, title="Metodo de Solucion", fancybox=True)

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
axes[0].set_title('Desempeño Ax=b \n [Max Poblete – Macbook Pro 13"]', fontsize=15,fontweight = 'bold')
axes[0].set_ylabel('Tiempo Transcurrido',fontsize=15,fontweight = 'bold')
axes[1].set_ylabel('Uso de Memoria',fontsize=15,fontweight = 'bold')
axes[1].set_xlabel('Tamaño de la Matriz (N)',fontsize=15,fontweight = 'bold')
axes[0].grid()
axes[1].grid()

axes[1].get_yticklabels()[7].set_color('red') 

plt.savefig('.png', dpi=500)
plt.tight_layout()
plt.show()






    
    