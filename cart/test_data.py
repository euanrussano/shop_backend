from django.contrib.auth import get_user_model
from .models import Cart, CartItem
import catalogue.test_data
from catalogue.models import Product

from decimal import Decimal

User = get_user_model()

initial_user = [
    {
        'username': 'testuser1',
        'password': 'testing'
    }, 
    {
        'username': 'testuser2',
        'password': 'testing'
    }
]

initial_cart = [
    {
    'user':1,
    },
]

initial_cartitem = [
    {
    'cart':1,
    'product': 1, 
    'price': Decimal('12.99'), 
    'quantity':3
    },
    {
    'cart':1,
    'product': 2, 
    'price': Decimal('0.99'), 
    'quantity':2
    },
]

def initializeData():
    catalogue.test_data.initializeData()
    for user in initial_user:
        User.objects.create(**user)
    for cart in initial_cart:
        cart_data = cart.copy()
        cart_data['user'] = User.objects.get(pk=cart['user'])
        Cart.objects.create(**cart_data)
    for cartitem in initial_cartitem:
        cartitem_data = cartitem.copy()
        cartitem_data['cart'] = Cart.objects.get(pk=cartitem['cart'])
        cartitem_data['product'] = Product.objects.get(pk=cartitem['product'])
        CartItem.objects.create(**cartitem_data)