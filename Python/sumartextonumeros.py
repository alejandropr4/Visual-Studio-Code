print("Ejemplo sumando números de String")
print("Introduzca un texto de SOLO NUMEROS")
textonumeros = input()
# Necesitamos acceder caracter a caracter a cada numero del String
# Hay que recorrer toda la cadena de String
longitud = len(textonumeros)
# Declaramos la variable suma FUERA del bucle
# Es más, si no la declaramos fuera del bucle
# en algunos lenguajes no podríamos utilizarla
# como en la linea 25
suma = 0
for i in range(longitud):
    # Podemos declarar caracter y numero dentro del bucle
    # porque solamente las utilizamos ahí dentro en el código
    # Recuperamos cada caracter
    caracter = textonumeros[i]
    # Convertimos cada caracter a int
    numero = int(caracter)
    # En la variable suma, quiero ir sumando cada numero
    # 1 + 2 + 3 + 4
    # Realizamos la suma
    suma = suma + numero
# La suma, solamente queremos dibujarla una vez
# por lo que la dibujamos fuera del bucle
print("La suma es " + str(suma))
print("Fin de programa")
