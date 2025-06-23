from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination, paginate
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/atletas/", response_model=schemas.AtletaOut)
def criar_atleta(atleta: schemas.AtletaCreate, db: Session = Depends(get_db)):
    return crud.create_atleta(db, atleta)

@app.get("/atletas/", response_model=Page[schemas.AtletaOut])
def listar_atletas(nome: str = Query(None), cpf: str = Query(None), db: Session = Depends(get_db)):
    atletas = crud.get_atletas_by_filter(db, nome, cpf)
    return paginate(atletas)

add_pagination(app)
