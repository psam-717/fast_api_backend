from sqlalchemy import Column, Integer, String, Float
# import Base from database.py
from database import Base

# defining database models
class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, index=True)
    # index=True ensures that a unique index is set for the column to help in faster sql queries
    name = Column(String, unique=True, index=True) 
    # nullable=True ensures that the description column is optional
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    