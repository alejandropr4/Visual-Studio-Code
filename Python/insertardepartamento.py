import pyodbc
print('Buscador de departamentos')
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" +usuario + "; PWD=" + password)
conexion=pyodbc.connect(cadenaconexion)
print('Introduzca un número')
#El numero sera un str porque lo concateno abajo
numero=input()
print('Introduzca un nombre de departamento')
nombre=input()
print('Introduzca una localidad')
localidad=input()
#Creamos el cursor
cursor=conexion.cursor()
#sql="insert into dept values (66, 'PROGRAMACION', 'IBIZA')"
sql="insert into dept values ("+ numero +", '" + nombre + "', '" + localidad +"')"
print(sql)
#EJECUTAMOS LA CONSULTA
cursor.execute(sql)
#VAMOS A IMPRIMIR ROWCONT
print ('Rowcount: ' +str(cursor.rowcount))
cursor.commit()
cursor.close()

cursor=conexion.cursor()
#Vamos a intentar reutilizar el cursor
sqlselect= "select dept_no, dnombre, loc from dept"
cursor.execute(sqlselect)
print("--------------------Departamentos-------------------")
for row in cursor:
    print(row.dnombre + ", " + row.loc)
cursor.close()
conexion.close()
print('Fin del programa')
