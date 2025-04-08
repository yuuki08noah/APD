from typing import List

from fastapi import APIRouter

from ch06.model.department import Department
from ch06.data import department as data

router = APIRouter(prefix="/departments")

# 학과 전체 선택
@router.get("")
def find_all() -> List[Department]:
    return data.find_all()