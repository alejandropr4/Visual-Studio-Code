def menuNarcisista():
    print("-------------Menu--------------")
    print("0.- Salir")
    print("1.- Año Bisiesto")
    print("2.- Número narcisista")
    print("3.- Años bisiestos año nacimiento")
    print("Seleccione una opción: ")

def isBisiesto(anyo):
   if (anyo%4 == 0):
       if (anyo%100 != 0 or anyo%400 == 0):
           return True
       else:
           return False
   else:
       return False

def isNarcisista(textonumero):
    suma = 0
    longitud = len(textonumero)
    for i in range(longitud):
        caracter = textonumero[i]
        numero = int(caracter)
        #potencia = numero**longitud
        potencia = pow(numero, longitud)
        suma = suma + potencia
    
    if (suma == int(textonumero)):
        return True
    else:
        return False

def getAnyoFecha(textofecha):
    #01/01/1980
    #01-01-1980
    #Primero voy a sustituir el caracter / o - por
    #cualquier otro
    if (textofecha.find("/") != -1):
        #Tenemos una barra, la sustituimos
        textofecha = textofecha.replace("/", "@")
    else:
        #Tenemos guiones entonces, lo sustituimos
        textofecha = textofecha.replace("-", "@")        
    #Ya tenemos que buscar la ultima @ para coger el año
    # 01@01@1980
    ultimaarroba = textofecha.rfind("@")
    #Con substring, decimos que queremos recuperar desde 
    # la ultima @ en adelante (año)
    anyo = textofecha[ultimaarroba + 1:]
    #Devolvemos String o devolvemos int
    return int(anyo)