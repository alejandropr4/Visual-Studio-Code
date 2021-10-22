# Vamos a declarar todos los métodos que vayamos a utilizar
# Tendremos un método de acción para mostrar el menú
def mostrarMenu():
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    print("Seleccione una opción:")
# Tendremos métodos que nos devolverán un valor
# con la ecuación que sea...
def sumarNumeros(num1, num2):
    suma = num1 + num2
    return suma
def restarNumeros(num1, num2):
    restar = num1 - num2
    return restar
def dividirNumeros(num1, num2):
    dividir = num1 / num2
    return dividir
def multiplicarNumeros(num1, num2):
    multiplicar = num1 * num2
    return multiplicar