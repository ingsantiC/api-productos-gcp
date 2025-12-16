from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import SessionLocal, engine, Base
from .schemas import ProductoCreate, ProductoOut
from .crud import create_producto, get_productos, get_producto, update_producto, delete_producto

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API REST - Productos", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/productos", response_model=ProductoOut, status_code=201)
def crear_producto(payload: ProductoCreate, db: Session = Depends(get_db)):
    return create_producto(db, payload)

@app.get("/productos", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return get_productos(db)

@app.get("/productos/{id}", response_model=ProductoOut)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    obj = get_producto(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return obj

@app.put("/productos/{id}", response_model=ProductoOut)
def actualizar_producto(id: int, payload: ProductoCreate, db: Session = Depends(get_db)):
    obj = update_producto(db, id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return obj

@app.delete("/productos/{id}", status_code=204)
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    ok = delete_producto(db, id)
    if not ok:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
