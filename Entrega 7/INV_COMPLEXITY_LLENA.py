from numpy import *
from numpy import float32,float64,double, ones
from scipy.sparse import *
from scipy.sparse import lil_matrix
from time import perf_counter
from matplotlib import pyplot as plt
import matplotlib.ticker

# =========================================
#            DEFINO MIS FUNCIONES
# =========================================




def matriz_laplaciana_llena(N,dtype=double):
    return diags(array([-ones(N-1),2*ones(N),-ones(N-1)]),[-1,0,1],dtype=dtype).toarray()

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
    


# =========================================
#     EJECUTO INV SCIPY MATRICES LLENAS
# =========================================



from scipy.linalg import inv

MNL = [2,3,5,10,20,50,100,200,500,1000,2000,5000,10000,20000]
Ncorridas = 5

MTEL = []
MTSL = []

for corrida in range(Ncorridas):    
    
    MTEL_temp = []
    MTSL_temp = [] 
    
    for N in MNL:
        print (f"Corrida {corrida} para N={N} ")
        t1 = perf_counter()
        
        A = matriz_laplaciana_llena(N)
        
    
        t2 = perf_counter()
        
        A_inv = inv(A)     
        
        t3 = perf_counter()
        
        dte = t2 - t1 #Tiem,po Ensamblado
        dts = t3 - t2 #Tiempo Solucionado
        
        
        MTEL_temp.append(dte)
        MTSL_temp.append(dts)
            
            
    MTEL.append(MTEL_temp)
    MTSL.append(MTSL_temp)



















MTEL_mean = 0
MTSL_mean = 0
lastN = MNL[-1]
for z1 in MTEL:
    MTEL_mean+= z1[-1]
MTEL_mean = MTEL_mean / Ncorridas
for z2 in MTSL:
    MTSL_mean+= z2[-1]
MTSL_mean = MTSL_mean / Ncorridas





# =========================================
#     GRAFICO INV MATRICES LLENAS
# =========================================

MNL = array(MNL)
fig, axes = plt.subplots(2, 1, figsize=(8,15))
c=0
for i in range(Ncorridas):
    
    axes[0].loglog(MNL,MTEL[i],"-o",color="k",alpha=0.5,linewidth=1)
    
    if c==0:
        axes[0].loglog(MNL,ones(len(MNL))*MTEL_mean,"--",color="c",alpha=1,linewidth=2,scaley=False)
        axes[0].loglog(MNL,(MTEL_mean / (lastN**1))*MNL      ,"--",color="orange",alpha=1,linewidth=2,scaley=False)   
        axes[0].loglog(MNL,(MTEL_mean / (lastN**2))*((MNL**2)),"--",color="green",alpha=1,linewidth=2,scaley=False)
        axes[0].loglog(MNL,(MTEL_mean / (lastN**3))*((MNL**3)),"--",color="red",alpha=1,linewidth=2,scaley=False)
        axes[0].loglog(MNL,(MTEL_mean / (lastN**4))*((MNL**4)),"--",color="purple",alpha=1,linewidth=2,scaley=False)
        
        c+=1

    axes[0].set_xscale("log")
    x = MNL
    axes[0].set_xticks(x)
    axes[0].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axes[0].set_xticklabels(" ")
    y1 = [0.1e-4,0.1e-3, 1e-3,1e-2,0.1,1,10,60,60*10]
    yl = ['0.01 ms','0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s","1 min"]
    axes[0].set_yscale("log")
    axes[0].set_yticks(y1)
    axes[0].set_yticklabels(yl,fontweight = 'bold')

    
    axes[1].loglog(MNL,MTSL[i],"-o",color="k",alpha=0.5,linewidth=1)
    
    if c==1:
        axes[1].loglog(MNL,ones(len(MNL))*MTSL_mean,"--",color="c",alpha=1,linewidth=2,scaley=False,label="CTE.")
        axes[1].loglog(MNL,(MTSL_mean / (lastN**1))*MNL      ,"--",color="orange",alpha=1,linewidth=2,scaley=False,label="O(N)")   
        axes[1].loglog(MNL,(MTSL_mean / (lastN**2))*((MNL**2)),"--",color="green",alpha=1,linewidth=2,scaley=False,label="O(N²)")
        axes[1].loglog(MNL,(MTSL_mean / (lastN**3))*((MNL**3)),"--",color="red",alpha=1,linewidth=2,scaley=False,label="O(N³)")
        axes[1].loglog(MNL,(MTSL_mean / (lastN**4))*((MNL**4)),"--",color="purple",alpha=1,linewidth=2,scaley=False,label="O(N⁴)")
        
        c+=1
    
    axes[1].set_xscale("log")
    x = MNL
    axes[1].set_xticks(x)
    axes[1].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    axes[1].set_xticklabels(x,rotation=45,fontweight = 'bold')
    y1 = [0.1e-4,0.1e-3, 1e-3,1e-2,0.1,1,10,60,60*10]
    yl = ['0.01 ms','0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s","1 min"]
    axes[1].set_yscale("log")
    axes[1].set_yticks(y1)
    axes[1].set_yticklabels(yl,fontweight = 'bold')


axes[0].set_title('INV COMPLEXITY \n MATRICES LLENAS \n [Max Poblete – Macbook Pro 13"]', fontsize=10,fontweight = 'bold')
axes[0].set_ylabel('Tiempo de Ensamblado',fontsize=15,fontweight = 'bold')
axes[1].set_ylabel('Tiempo de Solucion',fontsize=15,fontweight = 'bold')
axes[1].set_xlabel('Tamaño de la Matriz (N)',fontsize=15,fontweight = 'bold')
axes[0].grid()
axes[1].grid()
axes[1].legend(loc="upper left", bbox_to_anchor=[0, 1], ncol=5, shadow=True,fontsize=12 , fancybox=True)
axes[0].set_ylim([0.000001, 600])
axes[1].set_ylim([0.000001, 600])
plt.tight_layout()
plt.savefig('INV COMPLEXITY MATRICES LLENAS.png', dpi=600)
plt.show()





















# # =========================================
# #     GRAFICO INV MATRICES LLENAS
# # =========================================






# fig, axes = plt.subplots(2, 1, figsize=(5,7))

# for i in range(Ncorridas):
    
    
    
#     axes[0].plot(MNL,MTEL[i],"--o")
#     axes[0].set_xscale("log")
#     x = MNL
#     axes[0].set_xticks(x)
#     axes[0].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#     axes[0].set_xticklabels(" ")
#     y1 = [0.1e-3, 1e-3,1e-2,0.1,1,10,60,60*10]
#     yl = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s", "1 min"]
#     axes[0].set_yscale("log")
#     axes[0].set_yticks(y1)
#     axes[0].set_yticklabels(yl,fontweight = 'bold')

    
#     axes[1].plot(MNL,MTSL[i],"--o")
#     axes[1].set_xscale("log")
#     x = MNL
#     axes[1].set_xticks(x)
#     axes[1].get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#     axes[1].set_xticklabels(x,rotation=45,fontweight = 'bold')
#     y1 = [0.1e-3, 1e-3,1e-2,0.1,1,10,60,60*10]
#     yl = ['0.1 ms',"1 ms","10 ms","0.1 s","1s","10 s", "1 min"]
#     axes[1].set_yscale("log")
#     axes[1].set_yticks(y1)
#     axes[1].set_yticklabels(yl,fontweight = 'bold')


# # axes[1].axhline(8*(10**9),0,1000,ls="--",c="r",lw=3)
# axes[0].set_title('INV COMPLEXITY \n MATRICES LLENAS \n [Max Poblete – Macbook Pro 13"]', fontsize=10,fontweight = 'bold')
# axes[0].set_ylabel('Tiempo de Ensamblado',fontsize=15,fontweight = 'bold')




# axes[1].set_ylabel('Tiempo de Solucion',fontsize=15,fontweight = 'bold')
# axes[1].set_xlabel('Tamaño de la Matriz (N)',fontsize=15,fontweight = 'bold')
# axes[0].grid()
# axes[1].grid()

# # axes[1].get_yticklabels()[7].set_color('red') 

# # plt.savefig('MPGraph.png', dpi=600)
# plt.tight_layout()
# plt.show()









