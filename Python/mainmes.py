from mes import Mes
import random

print("Manejando clases Mes")
nombremeses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
#Necesitamos crear 12 meses y almacenarlos en una lista
meses = []
#Quiero que cada mes ponga Mes 1, Mes 2
for i in range(0, 12):
    #Creamos un mes por cada vuelta de bucle
    mimes = Mes()
    mimes.nombre = nombremeses[i]
    mimes.maxima = random.randint(1, 40)
    mimes.minima = random.randint(1, 40)
    meses.append(mimes)

print("Meses creados " + str(len(meses)))
#Recorremos todos los meses y vemos su contenido
for mes in meses:
    print(mes)

print("Fin de programa")