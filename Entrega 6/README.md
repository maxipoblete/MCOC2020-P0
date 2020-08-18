# MCOC2020-P0

# E6 - Desempeño Ax=B (Parte 2)

### Metodos Utilizados

En esta entrega se han probado distintos metodos para resolver un sistema Ax=B, donde A es una matriz laplaciana (entrega 4) y B es un vector de componentes unitarios. Para cada metodo utilizado, se han realizado 10 corridas para matrizes de hasta tamaño N=10.000 y luego se calculo el promedio para obtener un resultado mas exacto y representativo del tiempo transcurrido durante la ejecucion de las operaciones. Los metodos utilizados fueron los siguientes:<br>


1. SOLUCION CON NUMPY - INVERTIR MATRIZ APARTE ( np.linalg.inv(A) )<br>

2. SOLUCION CON NUMPY - FUNCION SOLVER  ( np.linalg.solve(A,B) )<br>

3. SOLUCION CON SCIPY - INVERTIR MATRIZ APARTE ( sp.linalg.inv(A) )<br>

4. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / GENERIC MATRIX  ( sp.linalg.solve(A,B) )<br>

5. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / GENERIC MATRIX  ( sp.linalg.solve(A,B) )<br>

6. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / SYMETRIC MATRIX  ( sp.linalg.solve(A,B) )<br>

7. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / SYMETRIC MATRIX  ( sp.linalg.solve(A,B) )<br>

8. SOLUCION CON SCIPY - SOLVER OVERWRITE OFF / POSITIVE DEFINITE MATRIX  ( sp.linalg.solve(A,B) )<br>

9. SOLUCION CON SCIPY - SOLVER OVERWRITE ON / POSITIVE DEFINITE MATRIX  ( sp.linalg.solve(A,B) )<br>

### Grafico Obtenido

En esta entrega el grafico ploteado es el siguiente:

![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%206/Grafico%20E6.1.png )


Los resultados esperados eran que los metodos mas lentos fuesen el (1) y el (3), es decir, aquellos que realizaban la inversion de la matriz para luego multiplicarla por el vector B y así obtener el resultado. Esta prediccion se cumplio y para valores altos de N (tamaño de la matriz) el grafico indica que el metodo de numpy es mas lento que el metodo de scipy, es decir, al parecer scipy tiene un mejor algoritmo de inversion de matrices de gran tamaño que numpy. Aún así, para valores de N < 1000 el metodo mas lento, con diferencia, es el de inversion de matrices de scipy (3).

Otro aspecto interesante que no está de más destacar (ya que se vio en la entrega pasada) es la gran diferencia de tiempos que hay entre el metodo de numpy de inversion de matrices (1) y el metodo de numpy de solver (2). Queda una vez más demostrado, por muy trivial que parezca; que la solucion mas conveniente en terminos de "rapidez computacional" es *NO* invertir directamente la matriz, si es que no se va a utilizar entera.

Luego, con respecto a los metodos de SCIPY utilizados, los metodos que tenian la opcion de OVERWRITE = TRUE se mantuvieron muy a la par con los que tenian OVERWRITE = FALSE, ya que el mayor impacto que tiene esta opcion es en el uso de la memoria durante la ejecucion del programa. Sin embargo, al realizar la comparacion entre ***El tipo de matriz*** que se utiliza en el solver, las diferencias fueron bastante marcadas. El metodo mas rapido fue el que asumia una matriz Definida Positiva (color verde), luego le siguio el metodo que asumia una matriz Simetrica (color rojizo), y finalmente el metodo mas lento entre ellos fue el que asumia una matriz Generica. 

Este ultimo resultado cumplio con las expectativas ya que, por ejemplo, si al metodo le decimos que se trata de una matriz cualquiera o generica, se demorará menos que si le decirmos que se trata de una matriz simetrica, en la que quizas se puedan tomar "atajos" para resolver el sistema, ya que se puede utilizar la "mitad" de la matriz y no completa, ya que es "simetrica". De cualquier forma, investigando un poco en la pagina de scipy, las posibles opciones de resolucion son:


1. assume_a='gen' : Asumen una matriz Generica, y la solucion se obtiene llamando a la rutina de bajo nivel de LA-PACK --> "?GESV"
2. assume_a='sym' : Asumen una matriz Simetrica, y la solucion se obtiene llamando a la rutina de bajo nivel de LA-PACK --> "?SYSV"
3. assume_a='her' : Asumen una matriz Hermitiana {Mi Python no pudo usar esta Funcion} 
4. assume_a='pos' : Asumen una matriz Definida Positiva, y la solucion se obtiene llamando a la rutina de bajo nivel de LA-PACK --> "?POSV"

El nombre de estas rutinas de LA-PACK ***? X X Y Y*** significa lo siguiente:<br>
* ? : representa el tipo de dato que se utiliza (S:	REAL / D:	DOUBLE PRECISION / C:	COMPLEX / Z: COMPLEX*16 or DOUBLE COMPLEX)<br>
* XX: significa el tipo de matriz utilizada ( GE: general / SY: simetrica / PO: Definida Positiva / TR: Triangular ... etc)<br>
* YY: Las ultimas letras (a veces pueden ser 3 letras) representan el metodo computacional usado y se aprovecha de las propiedades del esquema o estructura matricial indicado. Según la libreria, SV significa *simple driver* , que resuelve el sistema AX = B mediante la factorizacion de A y la sobreescritura de B con la solucion X (si no es indicado de forma contraria).<br>



### Analisis de Performance CPU


Al inicio de la ejecucion del programa, se tuvo un peak jamas antes visto de 298% de uso de CPU , lo que entiendo que significa que se estan usando los dos nucleos que tengo y un hilo. Este comportamiento se mantuvo hasta que el tamaño de las matrices N sobrepasó los 2000 y se estabilizo entre 170% y 200%, utilizando la totalidad de los nucleos. Como siempre, es necesario recordar que el computador esta haciendo otras cosas por detras y esto puede afectar el rendimiento (lo cual ya se ha explicado en entregas anteriores de como afecta a los tiempos transcurridos).





![alt text](https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%206/Grafico%20E6.2.png )

<br>


