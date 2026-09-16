from app.models import UserRegister, UserLogin

# Base de datos simulada en memoria.
# En un entorno de producción, esto se reemplaza por una base de datos real (e.g. PostgreSQL, SQLite).
fake_users_db = {}


def register_user(user_data: UserRegister) -> bool:
    """
    Registra un nuevo usuario en el sistema.
    
    Retorna:
        True si el usuario fue registrado correctamente.
        False si el usuario ya existe en la base de datos.
    """
    # Verificar si el nombre de usuario ya está registrado
    if user_data.username in fake_users_db:
        return False
    
    # Guardar el usuario (en un entorno real, la contraseña debe ser encriptada/hasheada)
    fake_users_db[user_data.username] = user_data.password
    return True


def authenticate_user(user_data: UserLogin) -> bool:
    """
    Autentica a un usuario verificando sus credenciales.
    
    Retorna:
        True si la autenticación es correcta.
        False si el usuario no existe o la contraseña es incorrecta.
    """
    # Obtener la contraseña almacenada para el usuario
    stored_password = fake_users_db.get(user_data.username)
    
    # Verificar existencia del usuario y coincidencia de contraseña
    if not stored_password or stored_password != user_data.password:
        return False
    
    return True