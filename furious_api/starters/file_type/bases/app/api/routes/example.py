from typing import List

from django_melhor.core.database import get_db
from django_melhor.crud.example import crud_item
from django_melhor.schemas.example import ItemExampleSchema
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemExampleSchema)
def create_item(item: ItemExampleSchema, db: Session = Depends(get_db)):
    """Cria um novo item."""
    return crud_item.create_item(db, item)

@router.get("/", response_model=List[ItemExampleSchema])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista todos os itens com paginação."""
    items = crud_item.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=ItemExampleSchema)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Retorna um item específico pelo ID."""
    db_item = crud_item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return db_item

@router.put("/{item_id}", response_model=ItemExampleSchema)
def update_item(item_id: int, item: ItemExampleSchema, db: Session = Depends(get_db)):
    """Atualiza um item existente."""
    return crud_item.update_item(db, item_id=item_id, item=item)

@router.delete("/{item_id}", response_model=ItemExampleSchema)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Remove um item."""
    return crud_item.delete_item(db, item_id=item_id)