from sqlalchemy.orm import Session
from app.models.example import ItemExample
from app.schemas.example import ItemExampleSchema

class CRUDItem:
    def get_item(self, db: Session, item_id: int) -> ItemExample | None:
        return db.query(ItemExample).filter(ItemExample.id == item_id).first()

    def get_items(self, db: Session, skip: int = 0, limit: int = 100) -> list[ItemExample]:
        return db.query(ItemExample).offset(skip).limit(limit).all()

    def create_item(self, db: Session, item: ItemExampleSchema) -> ItemExample:
        db_item = ItemExample(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def update_item(
        self, db: Session, item_id: int, item: ItemExampleSchema
    ) -> ItemExample | None:
        db_item = self.get_item(db, item_id)
        if db_item:
            for key, value in item.model_dump().items():
                setattr(db_item, key, value)
            db.commit()
            db.refresh(db_item)
        return db_item

    def delete_item(self, db: Session, item_id: int) -> ItemExample | None:
        db_item = self.get_item(db, item_id)
        if db_item:
            db.delete(db_item)
            db.commit()
        return db_item

crud_item = CRUDItem()