print("Ejemplo con métodos de String")
texto = "primero python"
# En este ejemplo solamente vamos a ir escribiendo los métodos
# y viendo que devuelven.
print("Mayusculas: " + texto.upper())
print("Replace o-@: " + texto.replace("o", "@"))
print("Primera letra: " + texto[0])
print("Longitud texto: " + str(len(texto)))
print("Buscar letra P: " + str(texto.find("P")))
print("Buscar letra p: " + str(texto.find("p")))
# Tenemos la sobrecarga de un método find("texto", posicion)
print("Buscar siguiente letra p: " + str(texto.find("p", 1)))
# Busca la posición de la primera letra p
posicion = texto.find("p")
# Buscamos la letra p a partir de la posición inicial
print("Buscar siguiente letra p: " + str(texto.find("p", posicion + 1)))
# Las posiciones no cambian, da igual como busquemos o lo que hagamos
# Podemos buscar desde el final de la cadena
print("Letra p con RFIND: " + str(texto.rfind("p")))
print("Texto iniciando con A: " + str(texto.startswith("A")))
print("Texto finalizando con n: " + str(texto.endswith("n")))
print("Texto números: " + str(texto.isdigit()))
print("Texto letras: " + str(texto.isalpha()))
# Vamos a ver Slicing, SubString
# Queremos desde la posición 2 en adelante
subcadena1 = texto[2:]
print("Posición 2 en adelante: " + subcadena1)
# También podemos decirle que queremos desde una posición a otra
subcadena2 = texto[2:5]
print("Posición [2-5]: " + subcadena2)
# Tenemos la posibilidad (conocemos FOR) de recorrer todos los caracteres
# del texto uno a uno
longitud = len(texto)
for i in range(longitud):
    # capturamos cada letra
    letra = texto[i]
    print(str(i) + ": " + letra)
# Averiguar si es un número lo que nos ha dado el usuario
print("Introduzca un número")
# El truco es almacenar el valor en un String
# Preguntar con isdigit() si es un número
# y ya hacer lo que queramos...
aux = input()
if (aux.isdigit()):
    print("Es un número")
else:
    print("No es un numero")
print("Fin de programa")
