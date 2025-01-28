from fastapi import APIRouter

from packages.endpoints import todo

router = APIRouter()
router.include_router(todo.router)
