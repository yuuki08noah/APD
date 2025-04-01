from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from ch05.web import todo

app = FastAPI()
app.include_router(todo.router)
templates = Jinja2Templates(directory="templates")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos":todo.get_all()})