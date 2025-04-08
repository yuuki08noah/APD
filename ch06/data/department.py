# 쿼리
# 1. 테이블 생성
import sqlite3
from typing import List

from ch06.data import cur
from ch06.error import Missing, Duplicated
from ch06.model.department import DepartmentResponse, Department

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

def find_by_id(id: int) -> DepartmentResponse:
    query = f"select * from department where id = {id}"
    cur.execute(query)
    res = cur.fetchone()
    if res:
        return row_to_model(res)
    raise Missing(f"No department with id {id}")

def save(department: Department) -> DepartmentResponse:
    query = f"insert into department(name, quota, description) values(:name, :quota, :description)"
    try:
        cur.execute(query, department.model_dump())
        cur.connection.commit()
        query = f"select * from department where id = (select max(id) from department)"
        cur.execute(query)
        return row_to_model(cur.fetchone())
    except sqlite3.IntegrityError:
        raise Duplicated("Department name is already taken")

def update(id: int, department: Department) -> DepartmentResponse:
    query = f"update department set name = :name, quota = :quota, description = :description where id = {id}"
    try:
        cur.execute(query, department.model_dump())
        cur.connection.commit()
        query = f"select * from department where id = {id}"
        cur.execute(query)
        return row_to_model(cur.fetchone())
    except sqlite3.IntegrityError:
        raise Duplicated("Department name is already taken")

def delete(id: int) -> DepartmentResponse:
    query = f"delete from department where id = {id}"
    try:
        cur.execute(f"select * from department where id = {id}")
        department = cur.fetchone()
        cur.execute(query)
        cur.connection.commit()
        return row_to_model(department)
    except:
        raise Missing(f"No department with id {id}")