from fastapi import FastAPI
#comment

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}