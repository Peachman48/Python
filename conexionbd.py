import mysql.connector

hosts = ""
users = ""
passwords = ""
ports = 1
databases = ""

opcionBaseDeDatos = int(input("Como deseas conectarte? 1-Local 2-Remota: "))
if opcionBaseDeDatos == 1:
    # Forma local
    hosts = "127.0.0.1"
    users = "root"
    passwords = ""
    ports = "3306"
    databases = "mini-siiau"
elif opcionBaseDeDatos == 2:
    # Forma remota
    hosts = "142.44.163.242"
    users = "Alumno5"
    passwords = "AlumnoPython1@."
    ports = "4000"
    databases = "mini-siiau"


try:
    conexion = mysql.connector.connect(
        host=hosts, user=users, password=passwords, port=ports, database=databases
    )
    print("Conexion correcta")

except mysql.connector.Error as err:
    print("Ocurrio un error al conectar: ", err)
