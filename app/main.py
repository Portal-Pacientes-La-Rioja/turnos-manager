from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from sqlalchemy.orm import Session

from typing import List

from app.database.database import engine, SessionLocal, Base
from app.models.turnos import Turnos
from app.models import schemas
from app.sql_app import crud

Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


from app.config.config import TURNO_BASE_API

app = FastAPI(
    title="Gestor de Turnos - Portal de Pacientes",
    description="Interfaz de programación para exponer api del Gestor de Turnos del Portal de Pacientes de La Rioja",
    version="0.0.1",
)


# region CORS

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endregion

router_app = APIRouter(
    prefix=TURNO_BASE_API, responses={404: {"description": "Not Found"}}
)


@router_app.get("/")
async def root():
    return {"message": "Hello World"}


@router_app.get("/turnos/{user_id}", response_model=List[schemas.Turno])
async def get_turnos_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_turnos_by_user(db, user_id)


@router_app.post("/turnos/", response_model=schemas.Turno)
async def create_turno(turno: schemas.Turno, db: Session = Depends(get_db)):
    return crud.create_turno(db, turno)


app.include_router(router_app)
