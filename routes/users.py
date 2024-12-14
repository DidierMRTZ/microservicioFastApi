from fastapi import APIRouter, HTTPException
from config.Database import engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from pydantic import BaseModel
from typing import Optional
from schema.user import UserCreate



user = APIRouter()

@user.get('/users')
def get_users():
    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    # Consultar
    users = session.query(User).all()
    return users

@user.post('/users')
def create_users(user:UserCreate):
    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear un nuevo usuario
    new_user = User(name=user.name, email=user.email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)  # Actualiza la instancia con los datos del DB

    # Consulta
    return new_user 