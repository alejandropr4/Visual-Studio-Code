#Necesitamos importar la clase persona
import persona
from persona import Persona

print('Ejemplo clases persona')
#Creamos una nueva persona
person = Persona()
#Cambiamos sus propiedades
person.nombre = 'Alumno'
person.apellidos = 'Azure'
person.fechanacimiento = 1995
#Podemos llamar a métodos
print(person.getNombreCompleto())
print('Edad ' + str(person.getEdad()))
print(person)