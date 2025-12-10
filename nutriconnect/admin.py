from django.contrib import admin
from .models import Farmer, Client

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm_name', 'location', 'contact', 'produce_type')
    search_fields = ('name', 'farm_name', 'location')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'location', 'interested_produce')
    search_fields = ('name', 'location')
