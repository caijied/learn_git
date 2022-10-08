from rest_framework import serializers

from nav.models import *


class CarSerializer(serializers.ModelSerializer):
    """
        车辆
    """

    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class VPMSerializer(serializers.ModelSerializer):
    """
        车队
    """

    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = VPM
        fields = '__all__'


class NavigationTaskSerializer(serializers.ModelSerializer):
    """
        导航任务
    """

    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = NavigationTask
        fields = '__all__'
