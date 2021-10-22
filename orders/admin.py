from django.contrib import admin

from .models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ['user', 'created', 'updated', 'paid']
    list_filter = ['user', 'created', 'updated', 'paid'] 

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin): 
    list_display = ['product', 'price', 'quantity']
    list_filter = ['product'] 
