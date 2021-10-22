print("Programa validar Email")
print("Introduzca su email: ")
email = input()
# Email @
if (email.find("@") == -1):
    print("Email sin @")
elif (email.find(".") == -1):
    print("Email sin punto")
# que el mail no comience ni finalice con @ ni con punto
elif (email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith(".")):
    print("Email con @ o . inicio o al final")
# Que el mail solo tenga una @
# email.find("@", email.find("@") + 1) != -1 #dos arrobas
elif (email.find("@") != email.rfind("@")):
    print("Email con mas de una @")
# Un punto después de la @
elif (email.find("@") > email.rfind(".")):
    print("Necesitamos un punto despues de la @")
else:
    # Y que el dominio (.com) tenga de 2 a 4 caracteres
    # buscamos la posicion del ultimo punto
    ultimopunto = email.rfind(".")
    # recuperamos desde el ultimo punto en adelante
    dominio = email[ultimopunto+1:]
    # recuperamos la longitud del dominio
    longitud = len(dominio)
    if (longitud >= 2 and longitud <= 4):
        print("Email CORRECTO!!!")
    else:
        print("El dominio debe ser de 2 a 4 letras")
print("Fin de programa")
