from fastapi import FastAPI
import requests
from pprint import pprint

app = FastAPI()
# url = "https://stage.api.fantasy.nfl.com/v2/league/teams"
#
# # league_id = '10924006'
# league_id = '6728468' # the original ID that does not work
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
base_url = "https://api.nfl.com"  # This is a placeholder, replace with the actual base URL
endpoint = "/v3/leagues/6728468/standings"
url = 'https://stage.api.fantasy.nfl.com/v3/leagues/6728468/standings'
token1= 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImU1MzVjN2MwLTgxN2YtNDc3Ni04OTkwLTU2NTU2ZjhiMTkyOCIsImNsaWVudEtleSI6IjRjRlVXNkRtd0pwelQ5TDdMckczcVJBY0FCRzVzMDRnIiwiaXNzIjoiTkZMIiwiZGV2aWNlSWQiOiJmNGVjZTYyMy05MzM1LTRjYTktODlkOS02ODk2MzFiZWUyMTUiLCJwbGFucyI6W3sicGxhbiI6ImZyZWUiLCJleHBpcmF0aW9uRGF0ZSI6IjIwMjQtMDktMDYiLCJzb3VyY2UiOiJORkwiLCJzdGFydERhdGUiOiIyMDIzLTA5LTA2Iiwic3RhdHVzIjoiQUNUSVZFIiwidHJpYWwiOmZhbHNlfV0sIkRpc3BsYXlOYW1lIjoiV0VCX0RFU0tUT1BfREVTS1RPUCIsIk5vdGVzIjoiIiwiZm9ybUZhY3RvciI6IkRFU0tUT1AiLCJsdXJhQXBwS2V5IjoiU1pzNTdkQkdSeGJMNzI4bFZwN0RZUSIsInBsYXRmb3JtIjoiREVTS1RPUCIsInByb2R1Y3ROYW1lIjoiV0VCIiwiY2l0eSI6InBvc3RtdW5zdGVyIiwiY291bnRyeUNvZGUiOiJERSIsImRtYUNvZGUiOiIyNzYwMDUiLCJobWFUZWFtcyI6WyIxMDQwMDc1MC0yNTliLTMzYWMtZWVlMy1hMzg1MmU4M2NkMWYiLCIxMDQwMjMxMC1hNDdlLTEwZWEtNzQ0Mi0xNmI2MzM2MzM2MzciLCIxMDQwMzIwMC02OWFiLTllYTYtNWFmNS1lMjQwZmJjMDhiZWEiLCIxMDQwNDkwMC1kNTllLWI0NDktZWY3NS05NjFlMDljYTAyN2UiXSwicmVnaW9uIjoiQlkiLCJicm93c2VyIjoiQ2hyb21lIiwiY2VsbHVsYXIiOmZhbHNlLCJlbnZpcm9ubWVudCI6InByb2R1Y3Rpb24iLCJ1aWQiOiI5MjY5MmM0Y2Q3OTc4NWQ0OGY4YmY2MDBlYzlmMTQyOCIsInJvbGVzIjpbImZyZWUiXSwiZXhwIjoxNjk0MDM4NTczfQ.1dk8RYphPgOAnSg53RzZckA67QATXwnwTy-oUcYu3nk'

headers = {
    "Authorization": token1  # Replace with your actual access token
}

apiKey = '3_h1AiUI9kcBduMJ2JoYPP6EXq3FGIy75RiS2DqkxjARGPcVazXVlNcGAOhgAfrU0P'
params  = {
    'appKey': apiKey
    }
# url = "https://stage.api.fantasy.nfl.com/v2/auth/login"
response = requests.get(base_url + endpoint, headers=headers, params=params)
if response.status_code == 200:
    leagues = response.json()
    pprint(leagues)
else:
    print(f"Error {response.status_code}: {response.text}")


@app.get("/")
async def root():
    return {"message": "Hello World"}

