from sqlalchemy import Column, Integer, String, Numeric
from .db import Base

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Numeric(12, 2), nullable=False)
