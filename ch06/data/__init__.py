# 연결
from sqlite3 import Connection, Cursor, connect
from typing import Optional

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_db():
    global con, cur
    if con is None:
        con = connect("./mydb.db", check_same_thread=False)
        cur = con.cursor()

get_db()



