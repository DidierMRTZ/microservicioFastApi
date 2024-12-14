from sqlalchemy import Column 
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy.ext.declarative import declarative_base
from config.Database import engine



# Definir base y modelo
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)

# Crear tablas
Base.metadata.create_all(engine)