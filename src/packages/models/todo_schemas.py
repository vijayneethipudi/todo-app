# schemas.py

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Request body model for creating/updating Todo
class TodoBase(BaseModel):
    """Todo Base Class"""

    title: str
    description: str
    completed: bool


class TodoCreate(TodoBase):
    """Todo Create"""

    pass


class TodoUpdate(TodoBase):
    """Todo Update"""

    id: int


# Response model for Todo item
class TodoInDB(TodoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True  # Tells Pydantic to treat SQLAlchemy models as dicts
