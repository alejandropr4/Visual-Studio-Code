print("Calcular salario trabajadores")
print("Introduzca número de horas trabajadas")
numerohoras = int(input())
print("Introduzca precio hora")
preciohora = int(input())
print("Introduzca número de Kilometros")
kilometros = int(input())
# Debemos calcular las horasextra
# Salario base y el salario Extra
horasextra = 0
salariobase = 0
salarioextra = 0
dieta = ""
salariototal = 0
retencion = ""
if (numerohoras > 36):
    # Tenemos horas extra
    horasextra = numerohoras - 36
    salariobase = preciohora * 36
    salarioextra = horasextra * (preciohora + 2)
else:
    # No tenemos horas extra
    horasextra = 0
    salarioextra = 0
    salariobase = numerohoras * preciohora
# Calculamos el precio para las dietas de Kilometros
if (kilometros < 100):
    dieta = "DIETA LOCAL"
elif (kilometros >= 100 and kilometros <= 500):
    dieta = "DIETA NACIONAL"
else:
    dieta = "DIETA INTERNACIONAL"
# Calculamos si tenemos retencion
salariototal = salariobase + salarioextra
if (salariototal <= 250):
    retencion = "NO TIENE RETENCION"
elif (salariototal >= 251 and salariototal <= 800):
    retencion = "RETENCION 20%"
else:
    retencion = "RETENCION 40%"

print("Numero Horas: " + str(numerohoras))
print("Precio Hora: " + str(preciohora))
print("Kilometros: " + str(kilometros))
print("Horas extra: " + str(horasextra))
print("Salario Extra: " + str(salarioextra))
print("Salario base: " + str(salariobase))
print("Salario total: " + str(salariototal))
print(dieta)
print(retencion)
print("Fin del programa")
