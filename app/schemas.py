from pydantic import BaseModel, Field

class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    descripcion: str | None = None
    precio: float = Field(..., gt=0)

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True
