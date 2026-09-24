# Se importan las clases y funciones necesarias de SQLAlchemy y los modelos definidos en app/models.py.
from sqlalchemy.orm import Session
from app.models import UserTable, UserRegister, UserLogin

# Función para registrar un nuevo usuario en la base de datos MySQL.
def register_user(user_data: UserRegister, db: Session) -> bool:
    # 1. Verificar si el usuario ya existe en MySQL
    existing_user = db.query(UserTable).filter(UserTable.username == user_data.username).first()
    if existing_user:
        return False
    
    # 2. Crear y guardar el nuevo usuario
    new_user = UserTable(
        username=user_data.username,
        password=user_data.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return True
# Función para autenticar un usuario existente en la base de datos MySQL.
def authenticate_user(user_data: UserLogin, db: Session) -> bool:
    # Buscar el usuario y validar contraseña
    db_user = db.query(UserTable).filter(UserTable.username == user_data.username).first()
    if not db_user or db_user.password != user_data.password:
        return False
    
    return True