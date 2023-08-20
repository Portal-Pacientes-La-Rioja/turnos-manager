from pydantic import BaseModel
from datetime import datetime


class TurnosBase(BaseModel):
    id_person: int
    id_establecimiento: int
    time_created: datetime
    description: str


class Turno(TurnosBase):
    id: int

    class Config:
        orm_mode = True
