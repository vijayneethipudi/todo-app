# models.py

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from packages.database.database import Base


class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, default=False)
    # pylint: disable=not-callable
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, onupdate=func.current_timestamp())
