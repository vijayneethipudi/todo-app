# main.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from packages.database.database import Base, engine, get_db
from packages.helpers.cust_exc import TodoNotFoundException
from packages.helpers.logger import logger
from packages.helpers.todo_crud import TodoCrud
from packages.models import todo_schemas

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/todos", tags=["todos"], responses={404: {"description": "Not Found"}})


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[todo_schemas.TodoInDB])
def get_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """get todos endpoint

    :param int skip: skip param, defaults to 0
    :param int limit: limit param, defaults to 10
    :param Session db: get_db, defaults to Depends(get_db)
    :raises HTTPException: TodoNotFoundException
    :raises HTTPException: Defualt Exception
    """
    try:
        todo_obj = TodoCrud(db=db, logger=logger)
        result = todo_obj.get_all_todos(skip=skip, limit=limit)
        return result
    except TodoNotFoundException as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc_info))
    except Exception as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))


@router.get("/{todo_id}", status_code=status.HTTP_200_OK, response_model=todo_schemas.TodoInDB)
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    """get todos endpoint

    :param int todo_id: todo_id path param
    :param Session db: get_db, defaults to Depends(get_db)
    :raises HTTPException: TodoNotFoundException
    :raises HTTPException: Defualt Exception
    """
    try:
        todo_obj = TodoCrud(db=db, logger=logger)
        result = todo_obj.get_todo_by_id(todo_id=todo_id)
        return result
    except TodoNotFoundException as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc_info))
    except Exception as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=todo_schemas.TodoInDB)
def create_todo(todo: todo_schemas.TodoCreate, db: Session = Depends(get_db)):
    """create todo

    :param todo_schemas.TodoCreate todo: create todo model
    :param Session db: get_db, defaults to Depends(get_db)
    :raises HTTPException: TodoNotFoundException
    :raises HTTPException: Defualt Exception
    """
    try:
        todo_obj = TodoCrud(db=db, logger=logger)
        result = todo_obj.create_todo(todo=todo)
        return result
    except TodoNotFoundException as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc_info))
    except Exception as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))


@router.put("/{todo_id}", status_code=status.HTTP_200_OK, response_model=todo_schemas.TodoInDB)
def update_todo(todo_id: int, todo: todo_schemas.TodoUpdate, db: Session = Depends(get_db)):
    """update todo

    :param int todo_id: todo_id path param
    :param todo_schemas.TodoUpdate todo: update todo model
    :param Session db: get_db, defaults to Depends(get_db)
    :raises HTTPException: TodoNotFoundException
    :raises HTTPException: Defualt Exception
    """
    try:
        todo_obj = TodoCrud(db=db, logger=logger)
        result = todo_obj.update_todo(todo_id=todo_id, todo=todo)
        return result
    except TodoNotFoundException as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc_info))
    except Exception as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))


@router.delete("/{todo_id}", status_code=status.HTTP_200_OK, response_model=todo_schemas.TodoInDB)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """delete todo

    :param int todo_id: todo_id path param
    :param Session db: get_db, defaults to Depends(get_db)
    :raises HTTPException: TodoNotFoundException
    :raises HTTPException: Defualt Exception
    """
    try:
        todo_obj = TodoCrud(db=db, logger=logger)
        result = todo_obj.delete_todo(todo_id=todo_id)
        return result
    except TodoNotFoundException as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc_info))
    except Exception as exc_info:
        logger.error(str(exc_info), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))
