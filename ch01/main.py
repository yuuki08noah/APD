import asyncio

from fastapi import FastAPI, Body, Header

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hi")
def hi(who: str):
    return f"Hello? {who}?"

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/konnichiwa")
def konnichiwa(who: str = Body(embed=True)):
    return who

@app.get("/arigato")
def arigato(who: str = Header()):
    return who

@app.get("/bye")
async def bye():
    await asyncio.sleep(1)
    return "bye"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)