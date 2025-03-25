from ch04.data import todo as data
from ch04.model import Todo

if __name__ == '__main__':
    data.insert_one(Todo(task="Study FastAPI"))
    print(data.find_all()) # AH~~~~~ WATASHI NO koIWA~~~
    # Minami NO~~~ KAZEni NOttE HASHI~~~RUwa~!
    # AH