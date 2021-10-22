from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    address = models.CharField(max_length=200) 
    postal_code = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('address',) 
    
    def __str__(self): 
        return self.name