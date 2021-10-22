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

#PROGRAMA PRINCIPAL
print("Ejemplo matemáticas con métodos")
#En este ejemplo, todos los métodos necesitan
#dos números. Por lo que los pediremos al iniciar.
print("Introduzca número 1: ")
numero1 = int(input())
print("Introduzca número 2")
numero2 = int(input())
#Todo este código, deseo que se repita
#hasta que el usuario escriba 0.
#Necesitamos opción primero para que entre en el bucle
opcion = -1
while (opcion != 0):
    #HACEMOS TODO EL CONTENIDO
    #Llamamos al método que dibuja el menú
    mostrarMenu()
    opcion = int(input())
    if (opcion == 1):
        #Llamamos a sumar
        resultado = sumarNumeros(numero1, numero2)
        print("La suma es " + str(resultado))
    elif (opcion == 2):
        #Llamamos a restar
        resultado = restarNumeros(numero1, numero2)
        print("La resta es " + str(resultado))
    elif (opcion == 3):
        #Llamamos a dividir
        resultado = dividirNumeros(numero1, numero2)
        print("La división es " + str(resultado))
    elif (opcion == 4):
        resultado = multiplicarNumeros(numero1, numero2)
        print("La multiplicación es " + str(resultado))
    elif (opcion == 0):
        print("Hasta luego")
        break
    else:
        print("Opción incorrecta") 
    #Vamos a preguntar si el usuario desea otros números
    print("¿Desea introducir otros números? (s/n)")
    respuesta = input()
    if (respuesta == "s"):
        #Aqui pedimos de nuevo los valores para los números
        print("Introduzca número 1: ")
        numero1 = int(input())
        print("Introduzca número 2")
        numero2 = int(input())
print("Fin de programa")

