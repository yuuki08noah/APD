from typing import List, Tuple, Dict, Optional, Union

users = {1:"chhh", 2:"3d", 4:"DK"}

def add(a: int, b: int) -> int: return a + b

# 튜플 (자료형, 자료형)
def get_person_info() -> Tuple[str, int]:
    return "dkl", 30030

# 입력받은 리스트 값들을 순회하면서 2를 곱하여 곱한 결과를 리턴
def process_numbers(numbers: List[int]) -> List[int]:
    return [n*2 for n in numbers]

# 딕셔너리
def get_student_scores() -> Dict[str, float]:
    return {"E":39}

# Optional
def find_user(user_id: int) -> Optional[str]:
    return users.get(user_id)

# union
def union_test(value: Union[int, str]) -> int:
    if isinstance(value, int):
        return value**2
    return len(value)

