#Definir una función que calcule la longitud de una lista o una cadena dada. No usar la función len.

def list_lenght(list_chain):
    counter = 0
    for _ in list_chain:
        counter += 1
    return counter

my_list = [4, 8, 15, 16, 23, 42]
print("Longitud de la lista:", list_lenght(my_list))


my_chain = "Con diez cañones por banda, viento en popa a toda vela, no corta el mar sino vuela un velero bergantín."
print("Longitud de la cadena:", list_lenght(my_chain))