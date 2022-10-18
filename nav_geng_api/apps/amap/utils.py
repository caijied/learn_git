import json

import requests


def get_amap_data(url, parameters):
    if not isinstance(parameters, dict):
        return {'error': '传入的参数不是字典类型'}

    query_string = '&'.join([f'{item[0]}={item[1]}' for item in parameters.items()])

    req_url = f'{url}?{query_string}'
    resp = requests.get(req_url).text

    return json.loads(resp)
