import datetime


def getTimeFromTimestamp(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    print(dt_object)
    formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)


def getLeagueStandings(leagueId):
    url = 'https://stage.api.fantasy.nfl.com/v3/leagues/{leagueId}/standings'.format(leagueId)
    return url

def getLeagueStandingsForGame(gameId, leagueId):
    url = 'https://stage.api.fantasy.nfl.com/v3/games/{gameId}/leagues/{leagueId}/standings'.format(gameId=gameId, leagueId=leagueId)
    return url

def getLeagueSeasonStats(leagueId):
    url = 'https://stage.api.fantasy.nfl.com/v3/leagues/{leagueId}/seasonstats'.format(leagueId=leagueId)

def getLeagueStatsForGame(gameId, leagueId):
    url = 'https://stage.api.fantasy.nfl.com/v3/games/{gameId}/leagues/{leagueId}/seasonstats'.format(gameId=gameId, leagueId=leagueId)
    return url