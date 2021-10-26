nombres = []

def mostrarListaNombres():
    for i in range(len(nombres)):
        name = nombres[i]
        print(str(i) + ".- " + name)

def rellenarNombres():
    #LIMPIAMOS LA LISTA
    nombres.clear()
    #HACEMOS EL BUCLE HASTA QUE DIGA OK
    respuesta = ""
    while (respuesta.upper() != "OK"):
        print("Introduzca un nombre o escriba OK para continuar")
        respuesta = input()
        if (respuesta.upper() != "OK"):
            #NOS HA DADO UN NOMBRE Y LO GUARDAMOS
            nombres.append(respuesta)
            print("Datos almacenados: " + str(len(nombres)))

def mostrarMenu():
    print("---------------------------------------")  
    print("0.- Salir")            
    print("1.- Nuevo nombre")
    print("2.- Eliminar nombre")
    print("3.- Comenzar de nuevo")
    print("Seleccione una opción")

print("Programa nombres listas")
rellenarNombres()
print("Lista de nombres introducidos")
mostrarListaNombres()
try:
    opcion = -1
    while (opcion != 0):
        mostrarMenu()
        opcion = int(input())
        if (opcion == 1):
            print("Introduzca nombre")
            nombre = input()
            nombres.append(nombre)
            mostrarListaNombres()
        elif (opcion == 2):
            mostrarListaNombres()
            print("Introduzca el número a eliminar")
            indice = int(input())
            nombres.pop(indice)
            print("Nombre eliminado")
            mostrarListaNombres()
        elif (opcion == 3):
            rellenarNombres()
            mostrarListaNombres()
        elif (opcion == 0):
            print("Hasta luego")
        else:
            print("Opcion incorrecta")
except IndexError:
        print("Ha introducido un indice no válido")
except ValueError:
        print("Debe introducir números")
        
finally:
    print("Fin de programa")