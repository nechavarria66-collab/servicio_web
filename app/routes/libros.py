# Schema de respuesta para un libro
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import LibroTable
from app.schemas.libro import LibroCrear, LibroRespuesta, LibroActualizar

# Se define un esquema de respuesta para un libro
router = APIRouter(
    prefix="/libros",
    tags=["Libros"]
)

@router.get("/", response_model=list[LibroRespuesta])
def listar_libros(db: Session = Depends(get_db)):
    libros = db.query(LibroTable).all()

    return libros

@router.post("/", response_model=LibroRespuesta, status_code=201)
def crear_libro(libro: LibroCrear, db: Session = Depends(get_db)):

    nuevo_libro = LibroTable(
        titulo=libro.titulo,
        autor=libro.autor,
        categoria=libro.categoria,
        disponible=libro.disponible
    )

    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)

    return nuevo_libro

@router.get("/{libro_id}", response_model=LibroRespuesta)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.query(LibroTable).filter(
        LibroTable.id == libro_id
    ).first()

    if libro is None:
        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    return libro

@router.put("/{libro_id}", response_model=LibroRespuesta)
def actualizar_libro(
    libro_id: int,
    datos: LibroActualizar,
    db: Session = Depends(get_db)
):
    libro = db.query(LibroTable).filter(
        LibroTable.id == libro_id
    ).first()

    if libro is None:
        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    libro.titulo = datos.titulo
    libro.autor = datos.autor
    libro.categoria = datos.categoria
    libro.disponible = datos.disponible

    db.commit()
    db.refresh(libro)

    return libro

@router.delete("/{libro_id}")
def eliminar_libro(
    libro_id: int,
    db: Session = Depends(get_db)
):
    libro = db.query(LibroTable).filter(
        LibroTable.id == libro_id
    ).first()

    if libro is None:
        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    db.delete(libro)
    db.commit()

    return {
        "mensaje": "Libro eliminado correctamente"
    }
