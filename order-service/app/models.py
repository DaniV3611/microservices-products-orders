from sqlalchemy import Column, Integer, String
from .database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String)  # Ahora almacenamos product_id como una cadena
    quantity = Column(Integer, default=1)
