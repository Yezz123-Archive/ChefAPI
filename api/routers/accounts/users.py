from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from . import crud, models, schemas
from api import deps
from core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    user_by_email = crud.user.get_by_email(db, email=user_in.email)
    user_by_username = crud.user.get_by_username(db, username=user_in.username)

    if user_by_email or user_by_username:
        raise HTTPException(
            status_code=400,
            detail="The user with this username or email already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    # TODO: Implement sending email when user is created
    return user
