from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import schemas, models, database, crud

router = APIRouter(
    prefix='/products',
    tags=['products']
)

@router.post('/')
def create_product(product: schemas.Product, db: Session = Depends(database.get_db)):
    return crud.create_product


@router.get('/')
def get_products(db: Session = Depends(database.get_db)):
    return crud.get_products(db)


@router.get('/{id}')
def get_product(id: int, db: Session = Depends(database.get_db)):
    return crud.get_product(db, id)


@router.put('/{id}')
def edit_product(id: int, db: Session = Depends(database.get_db)):
    return 
