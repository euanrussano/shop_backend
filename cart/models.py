from django.db import models
from django.contrib.auth import get_user_model

from catalogue.models import Product

# Create your models here.
User = get_user_model()

class Cart(models.Model): 
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('id',) 

    
    def __str__(self): 
        return 'Cart id ' + str(self.id) + 'from user ' + self.user.__str__()
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class CartItem(models.Model): 
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        ordering = ('id',) 

    def __str__(self): 
        return str(self.id)
    @property
    def total_price(self): 
        return self.price * self.quantity