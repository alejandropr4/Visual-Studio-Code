print("Validación ISBN")
print("Introduce un número ISBN")
isbn = input()
# Capturamos la longitud
longitud = len(isbn)
# Comprobamos que todos sean números
if (isbn.isdigit() == False):
    print("Debe introducir solo números")
# Debemos tener 10 caracteres
elif (longitud != 10):
    print("El número ISBN debe tener 10 caracteres")
else:
    # Necesitamos una variable suma para ir
    # almacenando las multiplicaciones y utilizarla
    # despues del bucle
    suma = 0
    # Aqui ya ha pasado la prueba y hacemos la lógica
    for i in range(longitud):
        # Capturamos cada letra
        letra = isbn[i]
        # Tenemos que hacer algo de matematicas
        # convertimos la letra a numero
        numero = int(letra)
        # Necesitamos la posicion real de cada caracter
        posicion = i + 1
        multi = numero * posicion
        suma = suma + multi
    # Aqui debemos comprobar si la suma final es divisible entre 11
    if (suma % 11 == 0):
        print("ISBN Correcto!!!")
    else:
        print("ISBN incorrecto")
print("Fin de programa")
