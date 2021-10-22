# Declaracion de metodos con parametros
def saludo(nombre):
    print("Bienvenido, " + nombre)


def despedida(nombre, dia):
    print("Ha sido un placer hoy " + dia + ", " + nombre)

 # PROGRAMA PRINCIPAL
print("Ejemplo métodos con parámetros")
print("Tu nombre es???")
name = input()
# En la llamada, el nombre de variable NO tiene
# porque coincidir.  Son código distintos
saludo(name)
print("Qué día es hoy de la semana???")
day = input()
despedida(name, day)
print("Fin de programa")
