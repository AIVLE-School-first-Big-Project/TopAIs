from django.contrib import admin
from .models import User, Agency, Company


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'username', 'email', 'phone', 'user_type']
    list_display_links = ['id', 'user_id']


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'area']
    list_display_links = ['id']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'comp_name', 'comp_homepage', 'comp_category']
    list_display_links = ['id']
