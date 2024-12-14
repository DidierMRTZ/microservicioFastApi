from fastapi import FastAPI
from routes.users import user
from sqlalchemy.orm import sessionmaker

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

app.include_router(user)