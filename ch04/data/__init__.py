# DB 연결
import sqlite3
from sqlite3 import Connection, Cursor
from typing import Optional

conn: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_db():
    global conn, cur
    if conn is None:
        print("Connection")
        conn = sqlite3.connect("todo.db")
        print("Cursor")
        cur = conn.cursor()
    return conn, cur

get_db()
