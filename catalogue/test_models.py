from django.test import TestCase
from .models import Product, Category
from . import  test_data

from helpers.modeltest import APIModelTest

class ProductModelTest(TestCase, APIModelTest):
    abstract = False
    test_data = test_data
    model = Product

class CategoryModelTest(TestCase, APIModelTest):
    abstract = False
    test_data = test_data
    model = Category
    

# Create your tests here.
# class ProductModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls) -> None:
#         test_data.initializeData()

#     def test_price(self):
#         test_id = 1
#         product = Product.objects.get(id=test_id)
#         expected_price = str(test_data.initial_products[test_id-1]['price'])
#         current_price = str(product.price)
#         self.assertEquals(expected_price, current_price)
    
#     def test_name(self):
#         test_id = 2
#         product = Product.objects.get(id=test_id)
#         expected_name = str(test_data.initial_products[test_id-1]['name'])
#         current_name = str(product.name)
#         self.assertEquals(expected_name, current_name)

# class CategoriesModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls) -> None:
#         test_data.initializeData()
    
#     def test_name(self):
#         test_id = 1
#         category = Category.objects.get(id=test_id)
#         expected_name = str(test_data.initial_categories[test_id-1]['name'])
#         current_name = str(category.name)
#         self.assertEquals(expected_name, current_name)
