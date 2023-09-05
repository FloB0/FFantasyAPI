from fastapi import FastAPI
import requests
from pprint import pprint

app = FastAPI()
url = "https://stage.api.fantasy.nfl.com/v2/league/teams"

# league_id = '10924006'
league_id = '6728468' # the original ID that does not work
url_leage = "https://stage.api.fantasy.nfl.com/v3/leagues/{leagueId}/rosters".format(leagueId=league_id)
apikey_internal = 'internalemailuse'
apiKey = '3_WPLZFkJ278FjSau2FfLCrTRUyksAjeYpcva-qIfGl71F4VWrI-7Xb5y0snqKXDva'
payload = {
    'appKey': apikey_internal,
    'leagueId': league_id
    }
response = requests.get(url, params=payload)
response_json = response.json()
pprint(response_json)

# payload_league = {
#     'appKey': apiKey,
#     'league_id': league_id
#     }
#
# response = requests.get(url_leage, params=payload_league)
# response_json = response.json()
# pprint(response_json)

@app.get("/")
async def root():
    return {"message": "Hello World"}

