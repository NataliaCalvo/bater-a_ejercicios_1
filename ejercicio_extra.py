#Definir una función que, dada una lista, retorne los elementos únicos de la lista
#Ejemplo: [1, 2, 2, 3, 4, 4, 5]  -> [1, 2, 3, 4, 5] 
#Sin usar set() ni unique()

def elementos_unicos(lista):
    elementos_unicos = []
    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    return elementos_unicos

lista = [1, 2, 2, 3, 4, 4, 5]
print(elementos_unicos(lista))