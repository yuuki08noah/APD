# Endpoints
from typing import List

from fastapi import APIRouter, HTTPException

from ch05.error import Missing, Duplicate
from ch05.service import todo as service
from ch05.model.todo import TodoResponse, Todo, TodoCreate

router = APIRouter(prefix="/todo")

@router.get("/")
def get_all() -> List[TodoResponse]:
    return service.get_all()

@router.get("/{todo_id}")
def get_one(todo_id: str) -> TodoResponse:
    try: return service.get_one(Todo(todo_id=todo_id))
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.post("/")
def create(todo: TodoCreate) -> TodoResponse:
    try: return service.create(todo)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.message)

@router.delete("/")
def delete(todo: Todo) -> bool:
    try:
        return service.delete(todo)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.patch("/")
def patch(todo: Todo) -> TodoResponse:
    try: return service.patch(todo)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)