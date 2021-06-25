from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.recipes import Category
from schema.recipes import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: CategoryCreate, owner_id: int
    ) -> Category:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Category]:
        return (
            db.query(self.model)
            .filter(Category.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


category = CRUDCategory(Category)
