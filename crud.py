from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import models
import schemas


# creating a new item
def create_item(db: Session, item: schemas.ItemCreate) -> schemas.Item:
    try: 
        db_item = models.Item(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return schemas.Item.model_validate(db_item)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail='Item with this name already exists') from exc

# fetching all products(with pagination 10 at a go)
def fetch_products(db: Session, skip: int = 0, limit: int = 0) -> list[schemas.Item]:
    # items should be displayed as a list 
    return [
        schemas.Item.model_validate(item)
        for item in db.query(models.Item).offset(skip).limit(limit).all()
    ]
    
