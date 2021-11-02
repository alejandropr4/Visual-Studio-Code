import pyodbc
print('Buscador de departamentos')
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" +usuario + "; PWD=" + password)
conexion=pyodbc.connect(cadenaconexion)
#vamos a pedir el numero de departamento
print(' introduzca un numero de departamento')
#VAOS A UTILIZAR EL NUMERO PARA CONCATENAR LA CONSULTA SQL
#DEBERIAMOS CAPTURAR EL NUMERO COMO STRING
numero= input()
sql='select DEPT_NO, DNOMBRE, LOC from DEPT where DEPT_NO=' +numero
cursor=conexion.execute(sql)
row= cursor.fetchone()
if(not row):
    print ('NO EXISTE EL DEPARTAMENTO')
else:
    print (row.DNOMBRE + ', ' +row.LOC)
cursor.close()
conexion.close()
print('Fin del Programa')