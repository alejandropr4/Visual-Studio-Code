#import metodosexternosmatematicas, con este debo de hacer metodosexternosmatematicas.metodo()
#from metodosexternosmatematicas import mostrarMenu, sumarNumeros, restarNumeros, dividirNumeros, multiplicarNumeros lo de abjo es igual
from metodosexternosmatematicas import*
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
print("Pulse Enter para finalizar")
input()