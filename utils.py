import datetime


def getTimeFromTimestamp(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    print(dt_object)
    formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)


def getLeagueStandings(leagueId)
    url = 'https://stage.api.fantasy.nfl.com/v3/leagues/{leagueId}/standings'.format(leagueId)
    return url