import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (Boolean,
                        Column,
                        DateTime,
                        ForeignKey,
                        Integer,
                        String,
                        Text)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database.base_class import Base

if TYPE_CHECKING:
    from .users import User


class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=func.now())
    owner = relationship("User", back_populates="categories")
    recipes = relationship("Recipe", back_populates="category")


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=False)
    is_public = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("user.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=func.now())
    ingredients = relationship("Ingredient", back_populates="recipe")
    category = relationship("Category", back_populates="recipes")
    owner = relationship("User", back_populates="recipes")


class Ingredient(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    recipe = relationship("Recipe", back_populates="ingredients")
