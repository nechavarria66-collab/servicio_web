from fastapi import FastAPI, HTTPException, status
from app.models import UserRegister, UserLogin, AuthResponse
from app import auth

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Servicio de Autenticación",
    description="API para el registro e inicio de sesión de usuarios",
    version="1.0.0"
)


@app.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registro de nuevos usuarios"
)
def register(user: UserRegister):
    """
    Endpoint para registrar un nuevo usuario en la plataforma.
    Recibe un objeto con 'username' y 'password'.
    """
    success = auth.register_user(user)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error en el registro: el nombre de usuario ya existe."
        )
    
    return AuthResponse(message="Registro realizado de manera satisfactoria.")


@app.post(
    "/login",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Inicio de sesión de usuarios"
)
def login(user: UserLogin):
    """
    Endpoint para autenticar un usuario existente.
    Si la verificación es correcta retorna un mensaje exitoso;
    de lo contrario, devuelve un error HTTP 401.
    """
    authenticated = auth.authenticate_user(user)
    
    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error en la autenticación: usuario o contraseña incorrectos."
        )
    
    return AuthResponse(message="Autenticación satisfactoria.")