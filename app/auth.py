# Servicio de autenticación con FastAPI
from app.models import UserRegister, UserLogin

# Base de datos simulada en memoria.
# En un entorno de producción, esto se reemplaza por una base de datos real (e.g. PostgreSQL, SQLite).
fake_users_db = {}

# Función para registrar un nuevo usuario
def register_user(user_data: UserRegister) -> bool:
    
    # Verificar si el nombre de usuario ya está registrado
    if user_data.username in fake_users_db:
        return False
    
    # Guardar el usuario (en un entorno real, la contraseña debe ser encriptada/hasheada)
    fake_users_db[user_data.username] = user_data.password
    return True

#
def authenticate_user(user_data: UserLogin) -> bool:
    
    # Obtener la contraseña almacenada para el usuario
    stored_password = fake_users_db.get(user_data.username)
    
    # Verificar existencia del usuario y coincidencia de contraseña
    if not stored_password or stored_password != user_data.password:
        return False
    
    return True