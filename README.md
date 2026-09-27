# API Biblioteca Virtual Lumina

## Descripción

API REST desarrollada para el proyecto formativo Lumina.

El servicio permite gestionar los libros de una biblioteca virtual mediante operaciones CRUD, además de conservar los servicios de registro y autenticación de usuarios desarrollados previamente.

La aplicación fue desarrollada utilizando FastAPI, SQLAlchemy y MySQL.

---

## Tecnologías utilizadas

- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- Uvicorn
- Swagger
- Postman
- Git
- python-dotenv

---

## Estructura del proyecto

servicio_web/

- app/
  - routes/
    - libros.py
  - schemas/
    - libro.py
  - auth.py
  - database.py
  - main.py
  - models.py
- .env
- .gitignore
- README.md
- requirements.txt

---

## Instalación

### 1. Crear un entorno virtual

```bash
python -m venv .venv