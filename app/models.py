# Servicio de modelos de datos con Pydantic
from pydantic import BaseModel, Field

# Se definen los modelos de datos para las solicitudes y respuestas del servicio de autenticación.
class UserRegister(BaseModel):
   
    # Se definen los campos 'username' y 'password' con validaciones de longitud y descripción.
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Nombre de usuario para el registro"
    )
    # Se define el campo 'password' con una longitud mínima de 6 caracteres y una descripción.
    password: str = Field(
        ...,
        min_length=6,
        description="Contraseña de usuario con una longitud mínima de 6 caracteres"
    )

# Se define el modelo de datos para la solicitud de inicio de sesión, que incluye los mismos campos que el registro.
class UserLogin(BaseModel):

    # Se definen los campos 'username' y 'password' con descripciones para la solicitud de inicio de sesión.
    username: str = Field(
        ...,
        description="Nombre de usuario registrado"
    )
    # Se define el campo 'password' con una descripción para la solicitud de inicio de sesión.
    password: str = Field(
        ...,
        description="Contraseña del usuario"
    )

# Se define el modelo de datos para la respuesta del servicio de autenticación, que incluye un mensaje de estado.
class AuthResponse(BaseModel):

    # Se define el campo 'message' con una descripción para la respuesta del servicio de autenticación.
    message: str = Field(
        ...,
        description="Mensaje del estado de la operación (éxito o error)"
    )