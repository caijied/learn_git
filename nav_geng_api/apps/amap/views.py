import json

import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from amap.utils import get_amap_data


class IpConfigView(View):
    """
        定位
    """

    def get(self, request):
        data = get_amap_data('https://restapi.amap.com/v3/ip', {
            'key': settings.AMAP_WEB_SERVICE_KEY,
            'ip': request.GET.get('ip', '')
        })

        return JsonResponse(data)


class GeoregeoView(View):
    """
        地理编码
    """

    def get(self, request):
        ip = request.GET.get('ip', '')
        req_url = f'https://restapi.amap.com/v3/geocode/geo?key={settings.AMAP_WEB_SERVICE_KEY}&ip={ip}'
        resp = requests.get(req_url)
        data = json.loads(resp.text)

        return JsonResponse(data)


class DistrictView(View):
    """
        行政区域查询
    """

    def get(self, request):
        data = get_amap_data('https://restapi.amap.com/v3/config/district', {
            'key': settings.AMAP_WEB_SERVICE_KEY,
            'keywords': request.GET.get('keywords', '')
        })

        return JsonResponse(data)


class DrivingView(View):
    """
        驾车路径规划
    """

    def get(self, request):
        data = get_amap_data('https://restapi.amap.com/v3/direction/driving', {
            'key': settings.AMAP_WEB_SERVICE_KEY,
            'origin': request.GET.get('origin', ''),
            'destination': request.GET.get('destination', ''),
            'extensions': request.GET.get('extensions', 'all'),
            'strategy': request.GET.get('strategy', 11),
        })

        # todo: 在返回的多条路径中，为每条路径上的 steps 列表中，随机 0 ~ 4 个对象上加上属性：type:'danger',其他对象上加上属性：type:'normal'

        # with open('results.json', 'w', encoding='utf8') as fp:
        #     json.dump(data, fp)

        return JsonResponse(data)
