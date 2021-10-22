from django.contrib import admin

from .models import Address

# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin): 
    list_display = ['user', 'address', 'postal_code', 'city', 'state', 'created', 'updated']
    list_filter = ['user', 'city', 'state'] 