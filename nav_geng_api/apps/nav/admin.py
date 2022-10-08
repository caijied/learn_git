from django.contrib import admin

# Register your models here.
from nav.models import (
    Car,
    VPM,
    NavigationTask,
)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(VPM)
class VPMAdmin(admin.ModelAdmin):
    pass


@admin.register(NavigationTask)
class NavigationTaskAdmin(admin.ModelAdmin):
    pass
