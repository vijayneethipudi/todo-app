# crud.py

import logging
from typing import List, Union

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from packages.helpers.cust_exc import TodoNotFoundException
from packages.models import todo_schemas, todo_tables


class TodoCrud:
    """Todo crud class"""

    def __init__(self, db: Session, logger: logging.Logger):
        self.db = db
        self.logger = logger

    def get_all_todos(self, skip: int = 0, limit: int = 10) -> List[todo_tables.TodoItem]:
        """get all todos

        :param skip int: skip, defaults to 0
        :param limit int: limit, defaults to 10
        :raises exc_info: SQLAlchemyError
        :raises exc_info: Exception
        :return List[todo_tables.TodoItem]: All Todos
        """
        try:
            result: List[todo_tables.TodoItem] = self.db.query(todo_tables.TodoItem).offset(skip).limit(limit).all()
            self.logger.info(f"fetched data successfully: {result}")
            return result
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def get_todo_by_id(self, todo_id: int) -> Union[todo_tables.TodoItem, None]:
        """get todo by id

        :param int todo_id: todo id
        :raises exc_info: TodoNotFoundException
        :raises exc_info: SQLAlchemyError
        :raises exc_info: Base Exception
        :return Union[todo_tables.TodoItem, None]: if found todo data based on id else None
        """
        try:
            result = self.db.query(todo_tables.TodoItem).filter(todo_tables.TodoItem.id == todo_id).first()
            if not result:
                raise TodoNotFoundException(f"Data not found with id: {todo_id}")
            self.logger.info(f"Todo found with id: {todo_id}")
            return result
        except TodoNotFoundException as exc_info:
            raise exc_info
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def create_todo(self, todo: todo_schemas.TodoCreate) -> Union[todo_tables.TodoItem, None]:
        """create todo

        :param todo_schemas.TodoCreate todo: todo data
        :raises exc_info: SQLAlchemyError
        :raises exc_info: Exception
        :return Union[todo_tables.TodoItem, None]: Created data
        """
        try:
            db_todo = todo_tables.TodoItem(**todo.model_dump())
            self.db.add(db_todo)
            self.db.commit()
            self.db.refresh(db_todo)
            self.logger.info(f"Todo added successfully with id: {db_todo.id}")
            return db_todo
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def update_todo(self, todo_id: int, todo: todo_schemas.TodoUpdate) -> Union[todo_tables.TodoItem, None]:
        """Update todo

        :param int todo_id: todo id
        :param todo_schemas.TodoCreate todo: todo data
        :raises exc_info: SQLAlchemyError
        :raises exc_info: Exception
        :return Union[todo_tables.TodoItem, None]: updated data
        """
        try:
            db_todo = self.get_todo_by_id(todo_id=todo_id)
            if not db_todo:
                raise TodoNotFoundException(f"Todo not found with id: {todo_id}")
            self.logger.info(f"Todo found with id: {todo_id}")
            for key, value in todo.model_dump().items():
                setattr(db_todo, key, value)
            self.db.commit()
            self.db.refresh(db_todo)
            return db_todo
        except TodoNotFoundException as exc_info:
            raise exc_info
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def delete_todo(self, todo_id: int) -> Union[todo_tables.TodoItem, None]:
        """Delete Todo

        :param int todo_id: todo id
        :return Union[todo_tables.TodoItem, None]: todo item
        """
        try:
            db_todo = self.get_todo_by_id(todo_id=todo_id)
            if not db_todo:
                raise TodoNotFoundException(f"Todo not found with id: {todo_id}")
            self.db.delete(db_todo)
            self.db.commit()
            self.logger.info(f"Todo deleted successfully with id: {db_todo.id}")
            return db_todo
        except TodoNotFoundException as exc_info:
            raise exc_info
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info
