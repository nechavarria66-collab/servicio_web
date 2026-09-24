# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de credenciales de tu MySQL:
# Formato: mysql+pymysql://USUARIO:CONTRASEÑA@HOST:PUERTO/NOMBRE_BD
MYSQL_USER = "root"
MYSQL_PASSWORD = "3110"  # Cambia esto por tu contraseña de MySQL
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "servicio_autenticacion" # Nombre de tu base de datos en MySQL

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crear el generador de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para definir las tablas
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos en las rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()