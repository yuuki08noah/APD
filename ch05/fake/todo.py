from datetime import datetime
from typing import List

from ch05.model.todo import TodoResponse, Todo

_todos = [
    TodoResponse(
        todo_id=0,
        task="study fastapi",
        completed=0,
        created_at='2025-03-31',
    ),
    TodoResponse(
        todo_id=1,
        task="study db",
        completed=0,
        created_at='2025-03-3333',
    )

]

todo_id = 1

def get_all() -> List[TodoResponse]:
    return _todos

def get_one(todo: Todo) -> TodoResponse:
    _todo = next((x for x in _todos if x.task == todo.task), None)
    return _todo

def create(todo: Todo) -> TodoResponse:
    global todo_id
    todo_id += 1
    _todos.append(TodoResponse(
        todo_id=todo_id,
        task=todo.task,
        completed=0,
        created_at=str(datetime.now()),
    ))
    return _todos[todo_id]

def delete(todo: Todo) -> bool:
    for to in _todos:
        if to.task == todo.task:
            _todos.remove(to)
            return True
    return False