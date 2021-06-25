from fastapi import APIRouter

from api.routers.accounts import users, login
from api.routers.recipes import categories, recipes

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    categories.router, prefix="/recipes", tags=["categories"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
