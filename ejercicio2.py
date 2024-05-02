#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def func_max_de_tres(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return(num1)
    elif num2 > num1 and num2 > num3:
        return(num2)
    else: return num3

num1 = 132342
num2 = 3242
num3 = 3243544

print(func_max_de_tres(num1, num2, num3))