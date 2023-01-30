from fastapi import (
    FastAPI
)

from db import models, database
from routers import products, sales


database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(router=products.router)
app.include_router(router=sales.router)
