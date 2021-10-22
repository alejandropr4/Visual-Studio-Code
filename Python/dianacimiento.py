from math import trunc
print("Día de nacimiento")
print("Introduzca día: ")
# Normalmente, en un programa, se van declarando las variables
# en la parte superior.
# En Python, como no hay que declararlas e iniciarlas
# podemos hacerlo en cualquier parte del código
dia = int(input())
print("Introduzca el mes: ")
mes = int(input())
print("Introduzca el año: ")
anyo = int(input())
op1 = 0
op2 = 0
op3 = 0
op4 = 0
op5 = 0
op6 = 0
resultado = 0
if (mes == 1):
    mes = 13
    # Restar de una forma sencilla
    anyo -= 1
    #anyo = anyo - 1
elif (mes == 2):
    mes = 14
    anyo = anyo - 1
# Necesitamos los calculos, todas las operaciones y
# un resultado que es el paso 7
op1 = trunc(((mes + 1) * 3) / 5)
op2 = trunc(anyo / 4)
op3 = trunc(anyo / 100)
op4 = trunc(anyo / 400)
op5 = trunc(dia + (mes * 2) + anyo + op1 + op2 - op3 + op4 + 2)
op6 = trunc(op5 / 7)
resultado = trunc(op5 - (op6 * 7))
if (resultado == 0):
    print("SABADO")
elif (resultado == 1):
    print("DOMINGO")
elif (resultado == 2):
    print("LUNES")
elif (resultado == 3):
    print("MARTES")
elif (resultado == 4):
    print("MIERCOLES")
elif (resultado == 5):
    print("JUEVES")
elif (resultado == 6):
    print("VIERNES")
print("Fin de programa")
