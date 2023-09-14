import datetime
from getToken import get_AaccessToken
from getLeagueData import getData

def getBearerToken():
    bToken_ = 'Bearer ' + get_AaccessToken().json()['accessToken']
    return bToken_


def getTimeFromTimestamp(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    print(dt_object)
    formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)


def responseBuilder(args):
    header = {}
    params = {}
    url = args['url']
    return_ = {
        'header': header,
        'params': params,
        'url': url
        }
    return return_


def getLeagueStandings(leagueId):
    base_url_ = getData()['base_url']
    endpoint_ = '/leagues/{leagueId}/standings'
    url_ = base_url_ + endpoint_
    final_url = url_.format(leagueId=leagueId)
    return final_url


def getLeagueStandingsForGame(gameId, leagueId):
    base_url_ = getData()['base_url']
    endpoint_ = '/games/{gameId}/leagues/{leagueId}/standings'
    url_ = base_url_ + endpoint_
    final_url = url_.format(gameId=gameId, leagueId=leagueId)
    return final_url

def getLeagueSeasonStats(leagueId):
    base_url_ = getData()['base_url']
    endpoint_ = '/games/{gameId}/leagues/{leagueId}/standings'
    url_ = base_url_ + endpoint_
    url = 'https://stage.api.fantasy.nfl.com/v3/leagues/{leagueId}/seasonstats'.format(leagueId=leagueId)

def getLeagueStatsForGame(gameId, leagueId):
    url = 'https://stage.api.fantasy.nfl.com/v3/games/{gameId}/leagues/{leagueId}/seasonstats'.format(gameId=gameId, leagueId=leagueId)
    return url