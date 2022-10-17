import json

import requests


def get_amap_data(url, parameters):
    query_string = '&'.join([f'{item[0]}-{item[1]}' for item in parameters.items()])

    req_url = f'{url}?{query_string}'
    resp = requests.get(req_url)

    return json.loads(resp.text)
