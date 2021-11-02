import pyodbc
print('Buscador de departamentos')
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" +usuario + "; PWD=" + password)
conexion=pyodbc.connect(cadenaconexion)
print("Mostramos enfermos")
cursor = conexion.cursor()
sqlselect= "select apellido, inscripcion from enfermo"
cursor.execute(sqlselect)
print("-----------Empleados----------------")
for apellido, inscripcion in cursor:
    print(apellido + ", " + str(inscripcion))
cursor.close()

cursor = conexion.cursor()
print('Numero Que desea eliminar: ')
elimina = int(input())
cursor = conexion.cursor()

sqldelete = "delete from enfermo where inscripcion=?"
cursor.execute(sqldelete,(elimina))
print("Registros eliminados: " + str(cursor.rowcount))
cursor.commit()
cursor.close()
conexion.close()
print("Fin de programa")