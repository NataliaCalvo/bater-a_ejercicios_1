#Definir una función generar_n_caracteres() que tome un entero n y devuelva el carácter multiplicado por n. 
#Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(n, caracter):
    return caracter * n

# Ejemplo de uso
resultado = generar_n_caracteres(25, "x")
print(resultado) 