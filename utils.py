import datetime
from getToken import get_AaccessToken
from getLeagueData import getData
from endpoints import *


def get_bearer_token():
    bToken_ = 'Bearer ' + get_AaccessToken().json()['accessToken']
    return bToken_


def get_time_from_timestamp(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    print(dt_object)
    formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)


def build_url(base_url_, endpoint, **kwargs):
    full_url_pattern = "{}/{}".format(base_url_.rstrip('/'), endpoint.lstrip('/'))
    return full_url_pattern.format(**kwargs)


def get_url(base_url_, functionality, data, method="GET"):
    if method == "GET":
        endpoint = GET_ENDPOINTS.get(functionality)
    elif method == "POST":
        endpoint = POST_ENDPOINTS.get(functionality)
    else:
        raise ValueError(f"Unsupported method: {method}")

    if not endpoint:
        raise ValueError(f"No endpoint found for functionality: {functionality}")

    return build_url(base_url_, endpoint, **data)


def response_builder(dict_, functionality):
    header = {
        "Authorization": get_bearer_token()
        }
    params = {
        'appKey': dict_['appKey'],
        'leagueId': dict_['leagueId']
        }
    print(getData()['base_url'])
    url = get_url(base_url_=getData()['base_url'], functionality=functionality, data=getData(), method='GET')
    return_ = {
        'header': header,
        'params': params,
        'url': url
        }
    return return_
