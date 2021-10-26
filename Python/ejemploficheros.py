from os import write


print('Ejemplo ficheros Python')
#Vamos a crear un nuevo archivo y escribimos algo en el
#voy a utilizar w+ que Lectura/Escritura
fichero=open('nombre.txt','w+')
print('Introduce su nombre')
nombre=input()
fichero.write('Su nombre es...' + nombre)
#Cerramos el fichero
fichero.close()
#Añadimos un valor al archivo nuevo
#Lo abrimos para añadir
archivo=open("nombre.txt", "a")
print('Introduzca otro nombre')
nombre = input()
archivo.write('\n' + nombre)
archivo.close()
#Vamos a abrir el fichero y leemos su contenido
file=open('nombre.txt','r')
contenido=file.read()
print(contenido)
file.close()
print('Fin del programa')