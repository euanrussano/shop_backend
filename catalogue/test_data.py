from .models import Product, Category
from decimal import Decimal

initial_category = [
    {
    'name':'Verduras',
    },
]

initial_product = [
    {
    'category_id':1,
    'name': 'Alface', 
    'price': Decimal('12.99'), 
    'available':True
    },
    {
    'category_id':1,
    'name': 'Agriao', 
    'price': Decimal('0.01'), 
    'available':False
    },
]

def initializeData():
    for category in initial_category:
        Category.objects.create(**category)
    for product in initial_product:
        Product.objects.create(**product)