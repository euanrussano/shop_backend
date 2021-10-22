from django.test import TestCase
from .models import Cart, CartItem
from . import  test_data

from helpers.modeltest import APIModelTest

class CartModelTest(TestCase, APIModelTest):
    abstract = False
    test_data = test_data
    model = Cart

class CartItemModelTest(TestCase, APIModelTest):
    abstract = False
    test_data = test_data
    model = CartItem

# # Create your tests here.
# class CartModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls) -> None:
#         test_data.initializeData()

#     def test_existing_cart(self):
#         test_id = 1
#         cart = Cart.objects.get(id=test_id)
#         expected_user_id = str(test_data.initial_carts[test_id-1]['user'])
#         current_user_id = str(cart.user.id)
#         self.assertEquals(expected_user_id, current_user_id)

# class CartItemModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls) -> None:
#         test_data.initializeData()
    
#     def test_cart(self):
#         test_id = 1
#         cart_item = CartItem.objects.get(id=test_id)
#         expected_cart_id = str(test_data.initial_cartitems[test_id-1]['cart'])
#         current_cart_id = str(cart_item.cart.id)
#         self.assertEquals(expected_cart_id, current_cart_id)
