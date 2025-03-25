# get_one 예외 처리를 알아보자

class Missing(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def get_one(task: str):
    if task != 'todo':
        raise Missing("없어")
    return "정상 동작"

def web():
    try:
        result = get_one("choi")
    except Missing as e:
        print("MSISIGN" + e.message)

if __name__ == '__main__':
    web()