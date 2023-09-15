from fastapi import FastAPI
import requests
from pprint import pprint
from getToken import get_AaccessToken
from utils import *
from getLeagueData import getData

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

request_ = response_builder(getData(), 'league_standings')
response = requests.get(url=request_['url'], headers=request_['header'], params=request_['params'])
if response.status_code == 200:
    leagues = response.json()
    pprint(leagues)
else:
    print(f"Error {response.status_code}: {response.text}")

# header = {
#     "Authorization": get_bearer_token()
#     }
# params = {
#     'appkey': '3_h1AiUI9kcBduMJ2JoYPP6EXq3FGIy75RiS2DqkxjARGPcVazXVlNcGAOhgAfrU0P',
#     'leagueId': '12064754'
#     }
# print(getData()['base_url'])
# url = get_url(base_url_=getData()['base_url'], functionality=functionality, data=getData(), method='GET')