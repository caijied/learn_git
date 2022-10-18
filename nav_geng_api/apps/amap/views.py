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
    def get(self, request):
        ip = request.GET.get('ip', '')
        req_url = f'https://restapi.amap.com/v3/geocode/geo?key={settings.AMAP_WEB_SERVICE_KEY}&ip={ip}'
        resp = requests.get(req_url)
        data = json.loads(resp.text)

        return JsonResponse(data)


class DistrictView(View):
    def get(self, request):
        data = get_amap_data('https://restapi.amap.com/v3/config/district', {
            'key': settings.AMAP_WEB_SERVICE_KEY,
            'keywords': request.GET.get('keywords', '')
        })

        return JsonResponse(data)
