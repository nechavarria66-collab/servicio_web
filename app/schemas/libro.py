from pydantic import BaseModel, Field


# Datos comunes de un libro
class LibroBase(BaseModel):
    titulo: str = Field(
        ...,
        min_length=1,
        max_length=150,
        description="Título del libro"
    )

    autor: str = Field(
        ...,
        min_length=1,
        max_length=150,
        description="Autor del libro"
    )

    categoria: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Categoría del libro"
    )

    disponible: bool = Field(
        default=True,
        description="Indica si el libro está disponible"
    )


# Datos necesarios para crear un libro
class LibroCrear(LibroBase):
    pass


# Datos necesarios para actualizar un libro
class LibroActualizar(LibroBase):
    pass


# Datos que devolverá la API
class LibroRespuesta(LibroBase):
    id: int

    class Config:
        from_attributes = True