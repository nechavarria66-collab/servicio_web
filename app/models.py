from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    """
    Modelo de datos para la solicitud de registro de usuario.
    Define los campos requeridos y sus validaciones básicas.
    """
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Nombre de usuario para el registro"
    )
    password: str = Field(
        ...,
        min_length=6,
        description="Contraseña de usuario con una longitud mínima de 6 caracteres"
    )


class UserLogin(BaseModel):
    """
    Modelo de datos para la solicitud de inicio de sesión.
    Recibe las credenciales enviadas por el cliente.
    """
    username: str = Field(
        ...,
        description="Nombre de usuario registrado"
    )
    password: str = Field(
        ...,
        description="Contraseña del usuario"
    )


class AuthResponse(BaseModel):
    """
    Modelo de datos para la respuesta del servicio tras procesar
    el registro o la autenticación.
    """
    message: str = Field(
        ...,
        description="Mensaje del estado de la operación (éxito o error)"
    )