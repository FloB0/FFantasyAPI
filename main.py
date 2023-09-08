from fastapi import FastAPI
import requests
from pprint import pprint
from getToken import get_AaccessToken

app = FastAPI()
# url = "https://stage.api.fantasy.nfl.com/v2/league/teams"
#
# # league_id = '10924006'
league_id = '6728468' # the original ID that does not work
# url_leage = "https://stage.api.fantasy.nfl.com/v3/leagues/{leagueId}/rosters".format(leagueId=league_id)
# apikey_internal = 'internalemailuse'
# apiKey = '3_WPLZFkJ278FjSau2FfLCrTRUyksAjeYpcva-qIfGl71F4VWrI-7Xb5y0snqKXDva'
# payload = {
#     'appKey': apikey_internal,
#     'leagueId': league_id
#     }
# response = requests.get(url, params=payload)
# response_json = response.json()
# pprint(response_json)

# payload_league = {
#     'appKey': apiKey,
#     'league_id': league_id
#     }
#
# response = requests.get(url_leage, params=payload_league)
# response_json = response.json()
# pprint(response_json)

# Define the base URL and endpoint
# base_url = "https://api.nfl.com"  # This is a placeholder, replace with the actual base URL
# endpoint = "/v3/leagues/6728468/standings"
# endpoint_v2 = "/v2/league/players"
# endpoint_v2_1 = 'https://api.fantasy.nfl.com/v2/league/players'
# url = 'https://stage.api.fantasy.nfl.com/v3/leagues/6728468/standings'
token1 = 'Bearer ' + get_AaccessToken().json()['accessToken']

# token_wo_bearer = get_AaccessToken().json()['accessToken']
# url_v2 = 'https://stage.api.fantasy.nfl.com/v2/league/players'

# user_url = 'https://api.fantasy.nfl.com/v2/user'

url = 'https://stage.api.fantasy.nfl.com/v3/leagues'
headers = {
    "Authorization": token1  # Replace with your actual access token
}
url_2 = 'https://stage.api.fantasy.nfl.com/v3/leagues/{leagueId}/standings'.format(leagueId = league_id)
apiKey_old = '3_h1AiUI9kcBduMJ2JoYPP6EXq3FGIy75RiS2DqkxjARGPcVazXVlNcGAOhgAfrU0P'
apiKey = '3_WPLZFkJ278FjSau2FfLCrTRUyksAjeYpcva-qIfGl71F4VWrI-7Xb5y0snqKXDva'
params = {
    'appKey': apiKey,
    'leagueId': '10924006',
    'page[size]': 1000,
    }
# url = "https://stage.api.fantasy.nfl.com/v2/auth/login"
# response = requests.get(url, headers=headers, params=params)

response = requests.get(url_2, headers=headers, params=params)

# response = requests.get(user_url, params=params)
if response.status_code == 200:
    leagues = response.json()
    pprint(leagues)
else:
    print(f"Error {response.status_code}: {response.text}")


@app.get("/")
async def root():
    return {"message": "Hello World"}

