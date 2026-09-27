from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.models import UserRegister, UserLogin, AuthResponse
from app.database import engine, Base, get_db
from app import auth
from app.routes.libros import router as libros_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API Biblioteca Virtual Lumina",
    description="API REST para autenticación de usuarios y gestion de libros de la Biblioteca Virtual Lumina",
    version="2.0.0"
)


app.include_router(libros_router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "Bienvenido a la API de la Biblioteca Virtual Lumina"
    }


@app.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registro de nuevos usuarios"
)
def register(user: UserRegister, db: Session = Depends(get_db)):
    success = auth.register_user(user, db)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error en el registro: el nombre de usuario ya existe."
        )

    return AuthResponse(
        message="Registro realizado de manera satisfactoria."
    )


@app.post(
    "/login",
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK,
    summary="Inicio de sesion de usuarios"
)
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated = auth.authenticate_user(user, db)

    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error en la autenticacion: usuario o contraseña incorrectos."
        )

    return AuthResponse(
        message="Autenticacion satisfactoria."
    )