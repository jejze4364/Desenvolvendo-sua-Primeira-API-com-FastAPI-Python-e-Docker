from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from . import models, schemas

def get_atletas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Atleta).offset(skip).limit(limit).all()

def create_atleta(db: Session, atleta: schemas.AtletaCreate):
    db_atleta = models.Atleta(**atleta.dict())
    try:
        db.add(db_atleta)
        db.commit()
        db.refresh(db_atleta)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
    return db_atleta

def get_atletas_by_filter(db: Session, nome: str = None, cpf: str = None):
    query = db.query(models.Atleta)
    if nome:
        query = query.filter(models.Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(models.Atleta.cpf == cpf)
    return query.all()
