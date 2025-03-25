from typing import List

from . import cur, conn
from ..model import Todo, TodoResponse

cur.execute('''
create table if not exists todo(
    todo_id integer primary key autoincrement, 
    task text not null unique, 
    completed integer not null default 0, 
    created_at text not null default (datetime('now', 'localtime'))
);
''')

def row_to_model(entity: tuple) -> TodoResponse:
    todo_id, task, completed, created_at = entity
    return TodoResponse(
        todo_id=todo_id,
        task=task,
        completed=completed,
        created_at=created_at
    )

def find_all() -> List[TodoResponse]:
    query = "select * from todo"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]

def insert_one(one: Todo):
    query = "insert into todo(task) values(:task)"
    cur.execute(query, one.model_dump())
    conn.commit()