from fastapi import APIRouter, HTTPException
from config.Database import engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from pydantic import BaseModel
from typing import Optional
from schema.user import UserCreate, UserResponse, UserUpdate
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK


user = APIRouter()

@user.get('/users', status_code=HTTP_200_OK)
def get_users():
    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    # Consultar
    users = session.query(User).all()
    return users

@user.get('/users/{id}',status_code=HTTP_200_OK)
def get_users_id(id: str):
    # Crear sesión
    Session = sessionmaker(bind=engine)
    db = Session()
    # Buscar el usuario en la base de datos
    users = db.query(User).filter(User.id == id).first()
    
    if not users :
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return users

@user.post('/users', status_code=HTTP_201_CREATED)
def create_users(user:UserCreate):
   # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    # Asignar el id si fu
     # Crear un nuevo usuario
    new_user = User(**user.dict())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)  # Actualiza la instancia con los datos del DB
    # Consulta
    return new_user 

@user.delete('/users/{id}', status_code=HTTP_204_NO_CONTENT)
def delete_users_id(id: str):
    Session = sessionmaker(bind=engine)
    db = Session()
    # Buscar el usuario en la base de datos
    usuario = db.query(User).filter(User.id == id).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Eliminar el usuario
    db.delete(usuario)
    db.commit()
    return usuario

@user.put('/users/{id}')
def update_users(id: str, user_update: UserUpdate):
    Session = sessionmaker(bind=engine)
    db = Session()
    # Buscar el usuario en la base de datos
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Actualizar los campos si se proporcionan
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user