from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models import Category, Recipe, Ingredient
from schema import RecipeCreate, RecipeUpdate


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: RecipeCreate, owner_id: int
    ) -> Recipe:
        """
        Add a recipe item by user
        """
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data.pop("ingredients")
        db_obj = self.model(
            **obj_in_data,
            owner_id=owner_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def add_ingredients(
        self, db: Session, *, recipe_id: int, name: str
    ) -> Any:
        """
        Add recipe ingredients
        """
        ing_obj = Ingredient(
            recipe_id=recipe_id,
            name=name
        )
        db.add(ing_obj)
        db.commit()
        db.refresh(ing_obj)
        return ing_obj

    def get_multi_with_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Recipe]:
        """
        Retrieve owner created recipes
        """
        return (
            db.query(self.model)
            .filter(Recipe.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


recipe = CRUDRecipe(Recipe)
