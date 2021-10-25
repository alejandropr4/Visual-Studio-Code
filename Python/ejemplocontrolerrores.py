def divisionDosNumeros():
    try:
        #CODIGO QUE PODRIA DAR UNA EXCEPCION
        print('Introduzca un numero: ')
        numero1= int(input())
        print('Introduzca otro numero: ')
        numero2= int(input())
        print('El doble es: ' + str((numero1/numero2)))
    except ValueError:
        print('Error, debes introducir un numero')
    except ZeroDivisionError:
        print('Error, no puedes dividir por zero') 
    except:
        print('ERROR')   

print('Programa principal control de errores')
divisionDosNumeros()