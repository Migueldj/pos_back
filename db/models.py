from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db.database import Base


"""
Inventario
Ventas
Entradas de pedidos
"""

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    bar_code = Column(String)
    price = Column(Float)


class ProductStock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True, index=True)
    product = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer)


class StockInbound(Base):
    __tablename__ = 'stock.inbound'

    id = Column(Integer, primary_key=True, index=True)
    product = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer)


# class Sale(Base):
#     pass