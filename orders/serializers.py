from rest_framework import serializers

from .models import Order, OrderItem

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('url','created', 'updated','paid')

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('url','order', 'product', 'price', 'quantity')

