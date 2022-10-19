"""nav_geng_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 嘿嘿嘿
# hahahah
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from nav import views as nav_views
from amap import views as amap_views

router = routers.DefaultRouter()
# 车辆
router.register('car', nav_views.CarViewSet, basename='car')
# 车队
router.register('vpm', nav_views.VPMViewSet, basename='vpm')
# 导航任务
router.register('navigation_task', nav_views.NavigationTaskViewSet, basename='navigation_task')

urlpatterns = [
    path('', TemplateView.as_view(template_name='amap.html')),
    path('api/', include(router.urls)),
    path('docs', include_docs_urls('接口文档')),
    path('admin/', admin.site.urls),

    # 高德导航地图 API
    path('amap/ipconfig/', amap_views.IpConfigView.as_view()),
    path('amap/georegeo/', amap_views.GeoregeoView.as_view()),
    path('amap/district/', amap_views.DistrictView.as_view()),
    path('amap/direction/driving/', amap_views.DrivingView.as_view()),
    path('map/direction/bicyckle/', amap_views.BicyclingView.as_view()),
    path('map/weather/weatherInfo/', amap_views.WeatherView.as_view()),
]
