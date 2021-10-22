# Debemos utilizar la libreria math
from math import trunc
print("Ejemplo validar DNI String")
print("Introduzca su número DNI")
# Vamos a comprobar si es un número de verdad o no
aux = input()
if (aux.isdigit() == False):
    # Si no es un número
    print("Debe introducir NUMEROS SOLAMENTE")
else:
    # Vamos a realizar el calculo para el DNI
    # ( nº DNI - (Entero(nº DNI / 23) * 23))
    numerodni = int(aux)
    resultado = (numerodni - (trunc(numerodni / 23) * 23))
    print(resultado)
    # Si tuvieramos alguna "forma" de tener la tabla aqui...
    # bastaria con recuperar la posicion 14
    tabladni = "TRWAGMYFPDXBNJZSQVHLCKET"
    letra = tabladni[resultado]
    print("Su letra es: " + letra)
print("Fin de programa")
print("Pulse Enter para finalizar")
input()