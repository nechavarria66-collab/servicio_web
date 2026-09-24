import pymysql

# Conéctate a MySQL (ajusta el usuario y contraseña si es necesario)
conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="3110"  # Pon tu contraseña de MySQL aquí si tienes una
)

cursor = conexion.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS servicio_autenticacion;")
print("¡Base de datos creada con éxito!")
conexion.close()