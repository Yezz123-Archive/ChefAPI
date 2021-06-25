from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Recipe)
def create_recipe(
    *,
    db: Session = Depends(deps.get_db),
    recipe_in: schemas.RecipeCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create a recipe
    """
    ingredients = recipe_in.ingredients
    recipe = crud.recipe.create_with_owner(
        db=db, obj_in=recipe_in, owner_id=current_user.id
    )
    for ing in ingredients:
        crud.recipe.add_ingredients(db=db, recipe_id=recipe.id, name=ing)
    db.refresh(recipe)
    return recipe
