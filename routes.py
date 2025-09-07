from fastapi import APIRouter, HTTPException, Depends
import crud, database, schemas
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/add-item', response_model=schemas.Item, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, item)

@router.get('/get-all-products', response_model=list[schemas.Item])
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.fetch_products(db, skip, limit)