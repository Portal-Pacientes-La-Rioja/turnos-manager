from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database.database import Base


class Turnos(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True)
    id_person = Column(Integer)
    id_establecimiento = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    description = Column(String)
