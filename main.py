from fastapi import FastAPI
import requests
from pprint import pprint
from getToken import get_AaccessToken
from utils import *
from getLeagueData import getData

app = FastAPI()
data = getData()
print(data)


# access_dict = get_AaccessToken().json()['accessToken']
# print(access_dict)


@app.get("/")
async def root():
    return {"message": "Hello World"}

