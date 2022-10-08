from django.shortcuts import render

from rest_framework import viewsets

from nav.models import Car, VPM, NavigationTask
from nav.paginations import CarPagination, VPMPagination, NavigationTaskPagination
from nav.serializers import CarSerializer, VPMSerializer, NavigationTaskSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
        解决方案
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = CarPagination


class VPMViewSet(viewsets.ModelViewSet):
    """
        车队
    """

    queryset = VPM.objects.all()
    serializer_class = VPMSerializer
    pagination_class = VPMPagination


class NavigationTaskViewSet(viewsets.ModelViewSet):
    """
        导航任务
    """

    queryset = NavigationTask.objects.all()
    serializer_class = NavigationTaskSerializer
    pagination_class = NavigationTaskPagination
