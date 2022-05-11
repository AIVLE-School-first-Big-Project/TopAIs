from django.contrib import admin
from .models import Building, Business, Facility


# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'county', 'district', 'number1']
    list_display_links = ['id', 'name']


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['id', 'board_id', 'facility_id']
    list_display_links = ['id']


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'latitude', 'longitude', 'area', 'facility_type']
    list_display_links = ['id']
