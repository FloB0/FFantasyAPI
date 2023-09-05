from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Flo"}

@app.get("/Team")
async def getTeam():
    return {"team": "Flo's Fantasy Team"}