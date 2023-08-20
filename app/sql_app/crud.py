from sqlalchemy.orm import Session

from app.models.turnos import Turnos
from app.models import schemas


def get_turnos_by_user(db: Session, user_id: int):
    return db.query(Turnos).filter(Turnos.id == user_id).all()


def create_turno(db: Session, turno: schemas.Turno):
    db_turno = Turnos(**turno.dict())
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno


def get_number_of_turnos(db: Session):
    return db.query(Turnos).count()
