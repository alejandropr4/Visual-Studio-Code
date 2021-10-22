import metodosnarcisista
import datetime

print("Ejemplo narcisista y bisiesto")
opcion = -1
while (opcion != 0):
    metodosnarcisista.menuNarcisista();
    opcion = int(input())
    if (opcion == 1):
        print("Introduzca un año")
        numero = int(input())
        respuesta = metodosnarcisista.isBisiesto(numero)
        if (respuesta == True):
            print("AÑO Bisiesto!!!")
        else:
            print("AÑO NO BISIESTO")
    elif (opcion == 2):
        print("Introduzca un número")
        textonumero = input()
        respuesta = metodosnarcisista.isNarcisista(textonumero)
        if (respuesta == True):
            print("NARCISISTA")
        else:
            print("El número NO es narcisista")
    elif (opcion == 3):
        # print("Introduce tu año de nacimiento")
        print("Introduce tu fecha de nacimiento")
        #Tendríamos que tener "algo" para que nos devuelva el año
        #de una fecha  01/01/1980  01-01-1980
        #anyonacimiento = int(input())
        anyonacimiento = metodosnarcisista.getAnyoFecha(input())
        # Podríamos llamar a un método que devuelva los años PRINT
        fechahoy = datetime.date.today()
        anyoactual = fechahoy.year
        for i in range(anyonacimiento, anyoactual + 1):
            if (metodosnarcisista.isBisiesto(i)):
                print(i)
    else:
        print("Hasta luego")
print("Fin de programa")