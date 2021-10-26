from coche import Coche
from deportivo import Deportivo
print("Conduciendo mi Coche")
#Construimos nuestro coche
car = Coche()
car.marca = "Toyota"
car.modelo = "Yaris"
supercar = Deportivo(Coche)

supercar.marca = 'Ferrari'
supercar.modelo = 'F10'
supercar.turbo()
print(supercar.marca + ' ' + supercar.modelo)
# opcion = -1
# while (opcion != 0):
#     print("------------------")
#     print("0.- Salir")
#     print("1.- Arrancar")
#     print("2.- Acelerar")
#     print("3.- Frenar")
#     print("4.- Detener coche")
#     print("Seleccione una opcion")
#     opcion = int(input())
#     if (opcion == 1):
#         car.arrancar()
#     elif (opcion == 2):
#         car.acelerar()
#     elif (opcion == 3):
#         car.frenar()
#     elif (opcion == 4):
#         car.detener()
#     elif (opcion == 0):
#         print("Hasta luego")
#     else: 
#         print("Opcion incorrecta")
# print("Fin de programa")