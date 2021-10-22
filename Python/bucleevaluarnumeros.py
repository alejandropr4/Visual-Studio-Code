print("Evaluar números While")
respuesta = "s"
while (respuesta == "s"):
    # Iremos pidiendo numeros al usuario
    print("Introduzca un número")
    numero = int(input())
    if (numero > 0):
        print("POSITIVO")
    elif (numero < 0):
        print("NEGATIVO")
    else:
        print("ZERO")
    print("¿Desea continuar? (s/n)")
    respuesta = input()
print("Fin de programa")
