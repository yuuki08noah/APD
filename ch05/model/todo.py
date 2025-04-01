from pydantic import BaseModel

class Todo(BaseModel):
    todo_id: int

class TodoCreate(BaseModel):
    task: str

class TodoResponse(Todo):
    todo_id: int
    task: str
    completed: int
    created_at: str