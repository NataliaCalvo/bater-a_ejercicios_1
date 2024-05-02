#. Definir un histograma procedimiento() que tome una lista de números enteros e imprima 
#un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******

from ejercicio10 import generar_n_caracteres

def procedimiento(lista):
    for num in lista:
        print("*" * num)

procedimiento ([1, 2, 4, 5, 6])
