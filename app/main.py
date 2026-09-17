# Servicio de autenticación con FastAPI
from fastapi import FastAPI, HTTPException, status
from app.models import UserRegister, UserLogin, AuthResponse
from app import auth

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Servicio de Autenticación",
    description="API para el registro e inicio de sesión de usuarios",
    version="1.0.0"
)

# Endpoint para registrar un nuevo usuario
@app.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registro de nuevos usuarios"
)
# solicitud de registro de usuario
def register(user: UserRegister):
    """
    Endpoint para registrar un nuevo usuario en la plataforma.
    Recibe un objeto con 'username' y 'password'.
    """
    success = auth.register_user(user)
    # Si el registro falla (por ejemplo, si el nombre de usuario ya existe), se lanza una excepción HTTP 400.
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error en el registro: el nombre de usuario ya existe."
        )
    # Si el registro es exitoso, se retorna un mensaje de éxito.
    return AuthResponse(message="Registro realizado de manera satisfactoria.")

# Endpoint para iniciar sesión de un usuario existente
@app.post(
    "/login",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Inicio de sesión de usuarios"
)
# solicitud de inicio de sesión de usuario
def login(user: UserLogin):
    """
    Endpoint para autenticar un usuario existente.
    Si la verificación es correcta retorna un mensaje exitoso;
    de lo contrario, devuelve un error HTTP 401.
    """
    authenticated = auth.authenticate_user(user)

    # Si la autenticación falla (por ejemplo, si el nombre de usuario o la contraseña son incorrectos), se lanza una excepción HTTP 401.
    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error en la autenticación: usuario o contraseña incorrectos."
        )
    # Si la autenticación es exitosa, se retorna un mensaje de éxito.
    return AuthResponse(message="Autenticación satisfactoria.")