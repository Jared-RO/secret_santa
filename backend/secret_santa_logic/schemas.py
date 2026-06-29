from pydantic import BaseModel, EmailStr
from typing import List

class Participante(BaseModel):
    nombre: str
    correo: EmailStr

class SecretSantaRequest(BaseModel):
    participantes: List[Participante]

class AsignacionResponse(BaseModel):
    parejas: dict[str, str]