import os
import requests
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service:3000/products")

# Crear una sesión de base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para verificar si el producto existe
def get_product_from_product_service(product_id: str):
    response = requests.get(f"{PRODUCT_SERVICE_URL}/{product_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Ruta para crear un pedido
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    product = get_product_from_product_service(order.product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_order = models.Order(product_id=order.product_id, quantity=order.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Ruta para obtener todos los pedidos
@app.get("/orders/")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(models.Order).all()
    return orders
