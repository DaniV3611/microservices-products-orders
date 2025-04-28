from pydantic import BaseModel

class OrderBase(BaseModel):
    product_id: str
    quantity: int

class OrderCreate(BaseModel):
    product_id: str
    quantity: int = 1  # Default quantity to 1

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
