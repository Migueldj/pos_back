from sqlalchemy.orm import Session

from db import models, schemas

def get_products(db: Session):
    model = models.Product
    return db.query(model).all()

def get_product(db: Session, id: int):
    model = models.Product
    return db.query(model).filter(model.id == id).first()

def create_product(db: Session, product: schemas.Product):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, id: int):
    model = models.Product
    product = db.query(model).filter(model.id == id).first()
