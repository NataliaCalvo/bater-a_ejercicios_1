#Una función sin argumentos que haga un print() y que no tenga return. Asignar su valor a una variable y ver qué ocurre.

#1

def empty_function():
    print("I'm a forever alone function!")


var1 = empty_function()
print(var1)

#2

#Una función con un argumento que haga un print() de este argumento y que no tenga return. Asignar su valor a una variable y ver que ocurre.

def empty_function2(not_alone):
    print(not_alone)

alone = empty_function2()
print(alone)

    
#3

def empty_function3(a, b, c):
    return a + b + c

arg_1 = "a"
arg_2 = "b"
arg_3 = "c"

var3 = empty_function3(arg_1, arg_2, arg_3)
print(var3)
