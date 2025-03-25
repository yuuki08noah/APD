from fastapi import FastAPI, HTTPException
from fastapi.params import Query, Depends

app = FastAPI()

# 유저 조회 후 리턴 의존성
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

# 토큰 확인 후 권한 부여
def check_admin(token: str = Query(...)):
    if token != "secure_token_2_2":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"role": "admin"}

@app.get("/admin")
def admin(user: dict = Depends(check_admin)) -> dict:
    return {"message":user}

# 데이터베이스 연결을 의존성으로 사용하기
class Database:
    def __init__(self):
        self.connection = "데이터베이스 연결"
    def get_connect(self):
        return self.connection

def get_db():
    db = Database()
    return db.get_connect()

@app.get("/db")
async def read_db(connect: str = Depends(get_db)):
    return {"connect": connect}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("depends:app", reload=True, port=8000)

# 전체 라우터 수준에서 의존성 주입

# 토큰 비교 함수
def verify_token(token: str = Query(...)):
    if token != "secure_token_2_2":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"role": "admin"}

app_dep = FastAPI(dependencies=[Depends(verify_token)])

@app_dep.get("/public")
def public_endpoint():
    return {"message":"connect ok"}

@app_dep.get("/private")
def private_endpoint():
    return {"message":"connect ok"}

# 특정 라우터 하위에 의존성 주입
def check(role: str = Query(...)):
    if role != "admin": raise HTTPException(status_code=401, detail="Invalid role")
    return {"role": role}
@app_dep.get("/admin", dependencies=[Depends(check)])
def admin_endpoint(role: dict):
    return {"message": role}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("depends:app_dep", reload=True)
