#ESTA VARIABLE SIRVE PARA LOS METODOS Y EL PROGRAMA PRINCIPAL
nombres = ["Ana", "Adrian", "Lucia", "Carlos", "Pedro", "Heidi", "Ana"]

def mostrarNombres():
    longitud = len(nombres)
    for i in range(longitud):
        name = nombres[i]
        print(str(i) + ".- " + name)

print("Ejemplo de listas")
#AÑADIMOS UN NUEVO NOMBRE
#nombres.append("El nuevo")
#Insertamos un elemento en el medio
#nombres.insert(3, "El del medio")
#Eliminamos al elemento Ana
#Remove está bien, pero en realidad puede llevarnos
#a errores de lógica, porque a lo mejor el usuario
#quería eliminar el último elemento Ana
#nombres.remove("Ana")
#Eliminamos utilizando el INDICE
#nombres.pop(6)
#Borramos todo el contenido de la lista
nombres.clear()
mostrarNombres()
# print("LISTA DE NUMEROS ENTEROS")
# numeros = [20, 14, 55, 99, 77]
# #ORDENAR NUMEROS
# numeros.sort(reverse=True)
# print("Numeros ordenados")
# for num in numeros:
#     print(num)
#PARA RECUPERAR UN VALOR, SE UTILIZA EL INDICE
#print("Primer número de la lista: " + str(numeros[0]))
#print("LISTA DE STRINGS")
#mostrarNombres()