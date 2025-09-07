from pydantic import BaseModel

# defining schemas for api validation

class ItemBase(BaseModel): 
    name: str
    description: str | None = None
    price: float | None = None
    quantity: int | None = None

class ItemCreate(ItemBase):
    pass 

class Item(ItemBase):
    id: int
    
    class Config:
        from_attributes = True