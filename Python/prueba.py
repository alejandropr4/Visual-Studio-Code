print("Primer Python")
numero = 19
texto = "Mi String en Python"
# Esto es un comentario de una sola línea
# Para comentar varias líneas vamos a utilizar
# las teclas de VS Code
#COMENTAR:  Control + K + C
#DESCOMENTAR: Control + K + U
print(numero)
print(texto.lower())
print(texto.upper())
print(texto[0])
print(texto.find("i"))
print(texto.rfind("i"))
print(texto.isdigit())
print(texto.isdigit())
print(texto[0:2])
print(texto[1:])
texto = texto.replace("i", "@")
print(texto)
print(texto.count("@"))
print(texto.startswith("@"))
print(texto.endswith("@"))

# for i in range(len(texto)):
#     print(texto[i])
#     if (i == 2):
#         break
