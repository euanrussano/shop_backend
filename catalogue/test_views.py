from django.test import Client
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from . import  test_data
from django.test import TestCase

from helpers.apitest import APIViewTest

# initialize the APIClient app
client = Client()

class ProductViewTest(APIViewTest):
    test_data = test_data
    model = Product
    serializer = ProductSerializer
    list_view = 'product-list'
    detail_view = 'product-detail'

class CategoryViewTest(APIViewTest):
    test_data = test_data
    model = Category
    serializer = CategorySerializer
    list_view = 'category-list'
    detail_view = 'category-detail'
