# import json
# from rest_framework import status
from django.test import TestCase, Client
# from django.urls import reverse
# from django.conf import settings
# from .models import Product, Category
# from .serializers import ProductSerializer, CategorySerializer
from . import  test_data
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer

from helpers.apitest import APIViewTest

# initialize the APIClient app
client = Client()

class CartViewTest(APIViewTest):
    test_data = test_data
    model = Cart
    serializer = CartSerializer
    list_view = 'cart-list'
    detail_view = 'cart-detail'


class CartItemViewTest(APIViewTest):
    test_data = test_data
    model = CartItem
    serializer = CartItemSerializer
    list_view = 'cartitem-list'
    detail_view = 'cartitem-detail'