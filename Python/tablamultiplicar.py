print("Tabla multiplicar")
print("Introduzca un número: ")
numero = int(input())
for i in range(1, 11):
    # Realizamos las operaciones
    # Si es una operación solo para el bucle
    # no es necesario declararla arriba
    multiplicacion = numero * i
    print(str(numero) + " * " + str(i) + " = " + str(multiplicacion))
print("Fin de programa")
