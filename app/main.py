# Se importan las librerías necesarias para crear la API REST con FastAPI y manejar la base de datos con SQLAlchemy.
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.models import UserRegister, UserLogin, AuthResponse
from app.database import engine, Base, get_db
from app import auth

# Crea las tablas en MySQL automáticamente si aún no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Servicio de Autenticación",
    description="API para el registro e inicio de sesión de usuarios",
    version="1.0.0"
)
# Se define la ruta para registrar un nuevo usuario en la base de datos MySQL.
@app.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registro de nuevos usuarios"
)
# Se define la función para manejar la solicitud de registro de un nuevo usuario.
def register(user: UserRegister, db: Session = Depends(get_db)):
    success = auth.register_user(user, db)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error en el registro: el nombre de usuario ya existe."
        )
    
    return AuthResponse(message="Registro realizado de manera satisfactoria.")
# Se define la ruta para autenticar a un usuario existente en la base de datos MySQL.
@app.post(
    "/login",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Inicio de sesión de usuarios"
)
# Se define la función para manejar la solicitud de inicio de sesión de un usuario existente.
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated = auth.authenticate_user(user, db)

    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error en la autenticación: usuario o contraseña incorrectos."
        )
    
    return AuthResponse(message="Autenticación satisfactoria.")