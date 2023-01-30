from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    bar_code: str
    price: float
