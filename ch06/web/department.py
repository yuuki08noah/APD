from typing import List
from fastapi import APIRouter, Path, HTTPException, Body
from starlette import status

from ch06.error import Missing, Duplicated
from ch06.model.department import Department, DepartmentResponse
from ch06.data import department as data

router = APIRouter(prefix="/departments")

# 학과 전체 선택
@router.get("")
def find_all() -> List[DepartmentResponse]:
    return data.find_all()

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_department(id: int = Path(...)) -> DepartmentResponse:
    try:
        return data.find_by_id(id)
    except Missing:
        raise HTTPException(status_code=400)

@router.post("", status_code=status.HTTP_201_CREATED)
def create_department(department: Department = Body(...)) -> DepartmentResponse:
    try:
        return data.save(department)
    except Duplicated:
        raise HTTPException(status_code=409)

@router.patch("/{id}", status_code=status.HTTP_200_OK)
def update(id: int = Path(...), department: Department = Body(...)) -> DepartmentResponse:
    try:
        return data.update(id, department)
    except Missing:
        raise HTTPException(status_code=400)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(id: int = Path(...)) -> DepartmentResponse:
    try:
        return data.delete(id)
    except Missing:
        raise HTTPException(status_code=400)