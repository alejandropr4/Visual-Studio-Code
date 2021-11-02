import pyodbc
print ("Primera consulta SQL Server")
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
#CADENA CONEXION CON SEGURIDAD SQL SERVER (REMOTO)
cadenadeconexion=("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" +usuario + "; PWD=" + password)
#CADENA CONEXION CON SEGURIDAD WINDOWS (ON PREMISE)
#cadenadeconexion=("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
#+ "; DATABASE=" + bbdd + "; Trusted_connection=yes")
print ("Intentando conectar")
conexion=pyodbc.connect(cadenadeconexion)
print ("Conectado")
#CURSOR se crea con una conexión abierta
cursor= conexion.cursor()
#NECESITAMOS UNA CONSULTA, EL CURSOR
#MANEJA TANTO CONSLUTAS DE SELECCION (SELECT)
#COMO CONSULTAS DE ACCION, NO LE IMPORTA
#CREAMOS CONSULTA SELECT
sql= 'select * from dept'
#ELCURSOR EJECUTARA LA CONSULTA
cursor.execute(sql)
#podemos por ejemplo, recuperar una fila
row = cursor.fetchone()
#pintamos la fila
print (row)
#vamos a escribir fetchibe()
row = cursor.fetchone()
print (row)
#cada vez que ejecutamos fetch
#el cursor se mueve una fila
#No podemos volver a la fila anterior
#tendriamos que ejecutar otra vez el metodo
#execute() de la conexion

#para recorrer se utiliza for
for row in cursor:
    #podemos dibujar un dato de una columna
    #por el indice de la columna consulta
    #1 se corresponde ocn la columna de DNOMBRE
    print(row[1])
    #tambien podemos dibujar con una propiedad de row que es el nombre columna
    #CASE SENSITIVE
    print(row.LOC)
#siempre debemos cerrar el cursor despues de leer
cursor.close()
conexion.close()
print ("Fin Del programa")