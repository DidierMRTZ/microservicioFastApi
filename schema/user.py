from pydantic import BaseModel
from typing import Optional

# Esquema de datos para el POST
class UserCreate(BaseModel):
    id: Optional[str]
    name: str
    email: str