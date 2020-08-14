# MCOC2020-P0

# E5 - Desempeño Ax=B (Parte 1)

A partir de esta entrega, ordenare las entregas del Proyecto 0 en carpetas. Cada una tendrá su README.md además del que está en la pagina principal, en el que de igual manera se mostrará el progreso realizado.

En esta entrega el grafico ploteado es el siguiente:

![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%205/Grafico%20E5.1%20Ax_B_Parte1.png )

Es necesario destacar que la curva azul "invertir matriz" corresponde al archivo de texto _A_invB_inv.txt_ en el que se realiza la inversion de la matriz para resolver el sistema Ax=B. De esta forma se tienen en total 2 matrices y 2 vectores para el cálculo de bytes o memoria utilizada. En el caso de la curva naranja, "Sin Invertir Matriz" corresponde al archivo _A_invB_npSolve.txt_ y no se realiza la inversion de la matriz A por separado, si no que se hace uso de la funcion de numpy *np.linalg.solve(A,B)*  . Entonces, para el calculo de bytes o memoria usada, se utiliza 1 sola matriz y 2 vectores, dando como resultado un menor consumo de memoria. Para entregas futuras (entrega 6) estos datos no serán mostrados si no se solicita explicitamente. El uso de procesador en % se muestra encerrado en rojo en la siguiente foto, correspondiendo a un uso completo de los 2 procesadores al haber variado entre ~180 y ~200%:


![alt text]( https://github.com/maxipoblete/MCOC2020-P0/blob/master/Entrega%205/Grafico%20E5.2%20Ax_B_Parte1.png )

<br>


