from typing import Optional

from pydantic import BaseModel

# 생성용 model
class Department(BaseModel):
    name: str
    quota: int
    description: Optional[str] = None

# 응답용 model
class DepartmentResponse(Department):
    id: int
