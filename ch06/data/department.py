# 쿼리
# 1. 테이블 생성
from typing import List

from ch06.data import cur
from ch06.model.department import DepartmentResponse

cur.executescript('''
create table if not exists department(id integer primary key autoincrement, name text not null unique, quota integer not null default 0, description text);
insert or ignore into department(name, quota) values ('sw', 32);
insert or ignore into department(name, quota) values ('em', 32);
''')


def row_to_model(entity: tuple):
    id, name, quota, description = entity
    return DepartmentResponse(id=id, name=name, quota=quota, description=description)

def find_all() -> List[DepartmentResponse]:
    query = "select * from department"
    cur.execute(query)
    return list(map(row_to_model, cur.fetchall()))