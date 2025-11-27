from django.contrib import admin
from .models import Airport, Route

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['from_airport', 'direction', 'to_airport', 'duration', 'position']
    list_filter = ['direction']