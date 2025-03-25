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
    # 예외 처리 필요
    _todo = next((x for x in _todos if x.task == todo.task), None)

    return _todo

def create(todo: Todo) -> TodoResponse:
    # 예외 처리 필요
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
    # 예외 처리 필요
    _todo = get_one(todo)
    if _todo is not None:
        _todos.remove(_todo)
    return False

def patch(todo: Todo) -> TodoResponse:
    # 예외 처리 필요
    _todo = get_one(todo)
    if _todo is not None:
        _todo.completed = not _todo.completed
        return _todo