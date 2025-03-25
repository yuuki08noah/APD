import sqlite3

# 데이터베이스 연결
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# 테이블 생성
cursor.execute('''
    create table if not exists person(
        id integer primary key,
        name text not null,
        age integer
        );
''')

# 입력
cursor.execute('''
    insert into person(name, age) values(?, ?);
''', ("choi", 25))

name = "AH~ WATASHI NO KOIWA~ MINAMINO~ HASHINI NOTTE HASHIRUWA~ AH~ KAZENI NATTE~ SHIITTE HASHIRE~ ANO SHIMAE~"
age = 25
cursor.execute(f'''
    insert into person(name, age) values('{name}', {age});
''')
print("Success")
connection.commit()

# 검색
cursor.execute("select * from person")
print(*cursor.fetchall(), sep='\n')

# 갱신

cursor.execute("select age from person where name='choi'")
age = cursor.fetchone()[0]+100
params = {"age":age, "name":'choi'}
cursor.execute("update person set age = :age where name=:name", params)
connection.commit()

# 삭제

query = "delete from person where name=:name"
params = {"name":'choi'}
cursor.execute(query, params)
connection.commit()

# 종료
cursor.close()
connection.close()