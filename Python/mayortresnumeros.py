print("Ejemplo mayor tres números")
print("Introduzca número 1: ")
numero1 = int(input())
print("Introduzca número 2: ")
numero2 = int(input())
print("Introduzca número 3: ")
numero3 = int(input())
# Debemos preguntar si numero1 es mayor al 2
# y si es mayor al 3 también
mayor = 0
menor = 0
suma = 0
intermedio = 0
if ((numero1 >= numero2) and (numero1 >= numero3)):
    # El mayor es el 1
    mayor = numero1
elif ((numero2 >= numero1) and (numero2 >= numero3)):
    # El mayor es el 2
    mayor = numero2
else:
    # Mayor es el 3
    mayor = numero3
if ((numero1 <= numero2) and (numero1 <= numero3)):
    # Menor el 1
    menor = numero1
elif ((numero2 <= numero1) and (numero2 <= numero3)):
    # Menor es el 2
    menor = numero2
else:
    # Menor es el 3
    menor = numero3

suma = numero1 + numero2 + numero3
intermedio = suma - mayor - menor
print("Número mayor: " + str(mayor))
print("Número menor: " + str(menor))
print("Intermedio: " + str(intermedio))
print("Suma " + str(suma))
