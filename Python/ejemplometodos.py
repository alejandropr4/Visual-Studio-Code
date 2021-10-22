# CODIGO DE FUNCIONES/METODOS
def ejemploMetodo1():
    print("Soy el metodo 1...")


def ejemploMetodo2():
    print("Soy el metodo 2...")
    ejemploMetodo3()

# Podemos llamar desde un método a otro


def ejemploMetodo3():
    print("Soy el metodo 3...")


# CODIGO PRINCIPAL DEL PROGRAMA
print("Ejemplo de metodos")
print("Programa principal")
# Si realizamos la llamada, dará un salto
# para leer el contenido del método1
numero = 1
if (numero == 2):
    ejemploMetodo1()
else:
    ejemploMetodo2()
print("Fin de programa")
