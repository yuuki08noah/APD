# 비즈니스 함수들
from typing import List

from ch05.fake import todo as data
from ch05.ml.predictor import predict_category_v2
from ch05.model.todo import TodoResponse, Todo, TodoCreate

def get_all() -> List[TodoResponse]:
    return data.get_all()

def get_one(todo: Todo) -> TodoResponse:
    return data.get_one(todo)

def create(todo: TodoCreate) -> TodoResponse:
    print(predict_category_v2(todo.task))

    return data.create(todo)

def delete(todo: Todo) -> bool:
    return data.delete(todo)

def patch(todo: Todo) -> TodoResponse:
    return data.patch(todo)