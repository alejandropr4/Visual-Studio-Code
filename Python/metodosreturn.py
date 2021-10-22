def convertirTexto(texto):
    # Devolvemos el texto en mayusculas
    print("Estoy en el metodo!!!")
    return texto.upper()


def sumarNumeros(num1, num2):
    suma = num1 + num2
    return suma


# Programa principal
print("Metodos return")
print("Introduzca número 1")
numero1 = int(input())
print("Introduzca número 2")
numero2 = int(input())
# Realizamos la llamada a suma
resultado = sumarNumeros(numero1, numero2)
print("La suma es " + str(resultado))
print("Fin de programa")
