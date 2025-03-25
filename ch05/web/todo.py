# Endpoints
from typing import List

from fastapi import APIRouter, HTTPException

from ch05.error import Missing, Duplicate
from ch05.service import todo as service
from ch05.model.todo import TodoResponse, Todo

router = APIRouter(prefix="/todo")

@router.get("/")
def get_all() -> List[TodoResponse]:
    return service.get_all()

@router.get("/{task}")
def get_one(task: str) -> TodoResponse:
    try: return service.get_one(Todo(task=task))
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.post("/")
def create(todo: Todo) -> TodoResponse:
    try: return service.create(todo)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.message)

@router.delete("/")
def delete(todo: Todo) -> bool:
    try: return service.delete(todo)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.patch("/")
def patch(todo: Todo) -> TodoResponse:
    try: return service.patch(todo)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)