from fastapi import FastAPI
import data

app = FastAPI()

# findAll
@app.get("/getAll")
async def getAll():
    return data.getChampions()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app", port=7000)