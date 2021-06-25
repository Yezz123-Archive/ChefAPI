from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class CategoryBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on category creation
class CategoryCreate(CategoryBase):
    name: str


# Properties to receive on category update
class CategoryUpdate(CategoryBase):
    pass


# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):
    id: int
    name: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Category(CategoryInDBBase):
    pass


# Properties stored in DB
class CategoryInDB(CategoryInDBBase):
    pass


# Shared properties
class RecipeBase(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    ingredients: Optional[list] = None
    is_public: Optional[bool] = False


# Properties to receive on recipe creation
class RecipeCreate(RecipeBase):
    category_id: int
    name: str
    description: str
    ingredients: List[str]

    class Config:
        schema_extra = {
            "example": {
                "category_id": 1,
                "name": "Example Ingredient",
                "description": "Sample summarized description instruction",
                "ingredients": ["150ml ingredient 1", "2 tsp mixed ingredient"],
                "is_public": False,
            }
        }


# Properties to receive on recipe update
class RecipeUpdate(RecipeBase):
    pass


# Properties shared by models in DB
class RecipeInDBBase(RecipeBase):
    id: int
    name: str
    owner_id: int
    category_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass
