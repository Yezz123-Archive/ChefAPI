from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from api import deps

router = APIRouter()


@router.post("/categories", response_model=schemas.Category)
def create_category(
    *,
    db: Session = Depends(deps.get_db),
    category_in: schemas.CategoryCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new category.
    """
    category = crud.category.create_with_owner(
        db=db, obj_in=category_in, owner_id=current_user.id)
    return category


@router.get("/categories", response_model=List[schemas.Category])
def read_categories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve categories
    """
    if crud.user.is_superuser(current_user):
        categories = crud.category.get_multi(db=db, skip=skip, limit=limit)
    else:
        categories = crud.category.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return categories


@router.get("/categories/{id}", response_model=schemas.Category)
def read_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get Category by ID.
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not crud.user.is_superuser(current_user) and (category.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return category


@router.put("/categories/{id}", response_model=schemas.Category)
def update_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    category_in: schemas.CategoryUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update category
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not crud.user.is_superuser(current_user) and (category.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    category = crud.category.update(db=db, db_obj=category, obj_in=category_in)
    return category


@router.delete("/categories/{id}", response_model=schemas.Category)
def delete_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Delete a category
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not crud.user.is_superuser(current_user) and (category.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    category = crud.category.remove(db=db, id=id)
    return category
