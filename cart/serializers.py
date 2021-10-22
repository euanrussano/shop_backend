from rest_framework import serializers

from .models import Cart, CartItem
from catalogue.serializers import Product

class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'price', 'quantity', 'total_price')
        read_only_fields = ['price']

    def create(self,validated_data):
        # method need to set the cart price equals to product price
        
        cart = validated_data.get('cart')
        product = validated_data.get('product')
        
        cart_item = cart.items.filter(product = product, cart=cart).first()
        quantity = validated_data.get('quantity')

        if not cart_item:
            price = validated_data.get('product').price    
            return CartItem.objects.create(cart=cart, product = product, price=price, quantity=quantity)
        
        # if product is already in cart, update the quantity
        cart_item.quantity += quantity
        cart_item.save()
        return cart_item


    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        return instance

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ('id','user', 'items', 'total_price')

    
