# Endpoints
from typing import List

from fastapi import APIRouter

from ch05.service import todo as service
from ch05.model.todo import TodoResponse, Todo

router = APIRouter(prefix="/todo")

@router.get("/")
def get_all() -> List[TodoResponse]:
    return service.get_all()

@router.get("/{task}")
def get_one(task: str) -> TodoResponse:
    return service.get_one(Todo(task=task))

@router.post("/")
def create(todo: Todo) -> TodoResponse:
    return service.create(todo)

@router.delete("/")
def delete(todo: Todo) -> bool:
    return service.delete(todo)

@router.patch("/")
def patch(todo: Todo) -> TodoResponse:
    return service.patch(todo)