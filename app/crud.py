from sqlalchemy.orm import Session
from .models import Producto
from .schemas import ProductoCreate

def create_producto(db: Session, data: ProductoCreate):
    obj = Producto(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_productos(db: Session):
    return db.query(Producto).order_by(Producto.id.asc()).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def update_producto(db: Session, producto_id: int, data: ProductoCreate):
    obj = get_producto(db, producto_id)
    if not obj:
        return None
    for k, v in data.model_dump().items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def delete_producto(db: Session, producto_id: int):
    obj = get_producto(db, producto_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
